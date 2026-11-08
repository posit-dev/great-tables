import { expect, type Locator, type Page, test } from "@playwright/test";
import { ready } from "./helpers";

// exibble three times over (24 rows, grp_b then grp_a, each with a summary row, then a grand
// summary row), selectable, on one page, with char moved to the start and pinned there, and fctr
// moved to the end and pinned there, under a spanner ("Ends") across its edge, in a container
// 480px wide; with groups shown as a column, in a body 300px high (in a container 640px wide); and
// right to left.

const el = (page: Page) => page.locator("gt-table");
const scroller = (page: Page) => el(page).locator(".gt-i-scroller");
const scrollTo = (page: Page, left: number, top = 0) =>
  scroller(page).evaluate((div, [left, top]) => div.scrollTo(left as number, top as number), [left, top]);
const scrollLeft = (page: Page) => scroller(page).evaluate((div) => div.scrollLeft);
const setWidth = (page: Page, width: string) =>
  el(page).evaluate((node, width) => ((node.parentElement as HTMLElement).style.width = width), width);

type Box = { top: number; bottom: number; left: number; right: number };
const rect = (locator: Locator): Promise<Box> =>
  locator.evaluate((node) => {
    const { top, bottom, left, right } = node.getBoundingClientRect();
    return { top, bottom, left, right };
  });

// The part of the scroller its content shows in
const port = (scroller: Locator): Promise<Box> =>
  scroller.evaluate((div) => {
    const box = div.getBoundingClientRect();
    const top = box.top + div.clientTop;
    const left = box.left + div.clientLeft;
    return { top, bottom: top + div.clientHeight, left, right: left + div.clientWidth };
  });

// A data row's cell in a column, by its index among the row's cells (0 for the selection column)
const row = (page: Page, label: string) => el(page).locator("tbody tr", { has: page.locator(`th.gt_stub:text-is("${label}")`) });
const cell = (page: Page, label: string, column: string) => {
  const index = { stub: 1, char: 2, num: 3, fctr: 8 }[column] as number;
  return row(page, label).locator("> *").nth(index);
};
const label = (page: Page, column: string) => el(page).locator(`thead th[id$="-${column}"]`);

// The class of the cell at a point
const at = (page: Page, x: number, y: number) =>
  page.evaluate(([x, y]) => document.elementFromPoint(x as number, y as number)?.closest("th, td")?.className ?? null, [x, y]);

test.describe("pinned columns", () => {
  test("stay in view after the stub and at the end, as the rest scroll between them", async ({ page }) => {
    const errors = await ready(page, "pin.html");
    await expect(el(page)).toHaveAttribute("data-gti-wide", "");
    const view = await port(scroller(page));
    const num = await rect(cell(page, "row_5", "num"));
    const spanner = await rect(el(page).locator("thead .gt_column_spanner_outer", { hasText: "Ends" }));

    for (const left of [100, 99999]) {
      await scrollTo(page, left);
      await expect.poll(() => scrollLeft(page)).toBeGreaterThan(50);
      const scrolled = await scrollLeft(page);
      const stub = await rect(cell(page, "row_5", "stub"));
      expect(stub.left).toBeGreaterThan(view.left);
      for (const box of [await rect(cell(page, "row_5", "char")), await rect(label(page, "char"))]) {
        expect(box.left).toBeCloseTo(stub.right, 0);
      }
      // (In every row: the summary rows' cells too)
      for (const box of [
        await rect(cell(page, "row_5", "fctr")),
        await rect(label(page, "fctr")),
        await rect(row(page, "Total").first().locator("> *").last()),
        await rect(row(page, "Max").locator("> *").last()),
      ]) {
        expect(box.right).toBeCloseTo(view.right, 0);
      }
      // The others scroll, as does the spanner across the end's edge
      expect((await rect(cell(page, "row_5", "num"))).left).toBeCloseTo(num.left - scrolled, 0);
      expect((await rect(el(page).locator("thead .gt_column_spanner_outer", { hasText: "Ends" }))).left).toBeCloseTo(
        spanner.left - scrolled,
        0,
      );
    }
    // Over the cells scrolled under them
    await scrollTo(page, 100);
    await expect.poll(() => scrollLeft(page)).toBe(100);
    const char = await rect(cell(page, "row_5", "char"));
    const fctr = await rect(cell(page, "row_5", "fctr"));
    expect(await at(page, char.right - 3, char.top + 5)).toMatch(/gt-i-pin\b/);
    expect(await at(page, fctr.left + 3, fctr.top + 5)).toMatch(/gt-i-pin\b/);
    expect(await at(page, char.right + 3, char.top + 5)).not.toMatch(/gt-i-pin/);
    // The footer scrolls (but its notes stay in view)
    expect(await el(page).locator("tfoot .gt-i-pinned").count()).toBe(0);
    expect(errors).toEqual([]);
  });

  test("shade the columns scrolled past them, and the hint is by the ones at the end", async ({ page }) => {
    await ready(page, "pin.html");
    const start = el(page).locator('.gt-i-shade[data-gti-edge="left"]');
    const end = el(page).locator('.gt-i-shade[data-gti-edge="right"]');
    const fctr = await rect(cell(page, "row_5", "fctr"));
    await expect(el(page).locator(".gt-i-hint")).toBeVisible();
    expect((await rect(el(page).locator(".gt-i-hint"))).right).toBeCloseTo(fctr.left - 8, 0);

    await scrollTo(page, 100);
    await expect(start).toHaveAttribute("data-gti-shown");
    await expect(end).toHaveAttribute("data-gti-shown");
    expect((await rect(start)).left).toBeCloseTo((await rect(cell(page, "row_5", "char"))).right, 0);
    expect((await rect(end)).right).toBeCloseTo(fctr.left, 0);
    await scrollTo(page, 99999);
    await expect(end).not.toHaveAttribute("data-gti-shown");
  });

  test("stick both ways in a body that scrolls, with groups as a column", async ({ page }) => {
    const errors = await ready(page, "pin-column.html");
    await scrollTo(page, 80, 400);
    const view = await port(scroller(page));
    const head = await rect(el(page).locator("thead"));
    expect(head.top).toBeCloseTo(view.top, 0);
    // The corners over the pinned columns, and the grand summary row's cells at the bottom
    const fctrLabel = await rect(label(page, "fctr"));
    expect(fctrLabel.right).toBeCloseTo(view.right, 0);
    const charLabel = await rect(label(page, "char"));
    const max = row(page, "Max");
    const maxFctr = await rect(max.locator("> *").last());
    expect(maxFctr.bottom).toBeCloseTo(view.bottom, 0);
    expect(maxFctr.right).toBeCloseTo(view.right, 0);
    expect((await rect(max.locator("> *").nth(2))).left).toBeCloseTo(charLabel.left, 0);
    // The body scrolls under the pinned columns, which scroll under the column labels
    expect(await at(page, fctrLabel.left + 3, head.bottom + 30)).toMatch(/gt-i-pin\b/);
    expect(await at(page, fctrLabel.left + 3, (fctrLabel.top + fctrLabel.bottom) / 2)).toMatch(/gt_col_heading.*gt-i-pin\b/);
    expect(await at(page, fctrLabel.left + 3, maxFctr.top + 2)).toMatch(/gt_grand_summary_row/);
    // (After the row group column, whose label cells are pinned)
    const group = await rect(el(page).locator("tbody .gt_stub_row_group").last());
    expect(group.left).toBeGreaterThan(view.left);
    expect(charLabel.left).toBeGreaterThan(group.right);
    expect(errors).toEqual([]);
  });

  test("are mirrored right to left", async ({ page }) => {
    const errors = await ready(page, "pin-rtl.html");
    const view = await port(scroller(page));
    await expect(el(page).locator(".gt-i-hint")).toHaveText("← Scroll for more");
    await scrollTo(page, -100);
    await expect.poll(() => scrollLeft(page)).toBe(-100);
    const stub = await rect(cell(page, "row_5", "stub"));
    expect(stub.right).toBeLessThan(view.right);
    expect((await rect(cell(page, "row_5", "char"))).right).toBeCloseTo(stub.left, 0);
    const fctr = await rect(cell(page, "row_5", "fctr"));
    expect(fctr.left).toBeCloseTo(view.left, 0);
    const end = el(page).locator('.gt-i-shade[data-gti-edge="left"]');
    await expect(end).toHaveAttribute("data-gti-shown");
    expect((await rect(end)).left).toBeCloseTo(fctr.right, 0);
    expect(errors).toEqual([]);
  });

  test("follow a column resized before them", async ({ page }) => {
    await ready(page, "pin.html");
    // (The stubhead's handle, the first)
    const handle = el(page).locator(".gt-i-resizer").first();
    const before = await rect(cell(page, "row_5", "stub"));
    await handle.focus();
    await page.keyboard.press("ArrowLeft");
    await page.keyboard.press("ArrowLeft");
    await expect.poll(async () => (await rect(cell(page, "row_5", "stub"))).right).toBeLessThan(before.right - 10);
    await scrollTo(page, 100);
    await expect.poll(() => scrollLeft(page)).toBe(100);
    // (Both measured as they settle)
    await expect
      .poll(async () => (await rect(cell(page, "row_5", "char"))).left - (await rect(cell(page, "row_5", "stub"))).right)
      .toBeCloseTo(0, 0);
    expect((await rect(el(page).locator('.gt-i-shade[data-gti-edge="left"]'))).left).toBeCloseTo(
      (await rect(cell(page, "row_5", "char"))).right,
      0,
    );
  });

  test("scroll with the rest in a container they'd take up more than half of, until it widens", async ({ page }) => {
    const errors = await ready(page, "pin.html");
    await setWidth(page, "400px");
    await expect(cell(page, "row_5", "char")).not.toHaveClass(/gt-i-pinned/);
    await expect(cell(page, "row_5", "char")).toHaveCSS("position", "static");
    await scrollTo(page, 100);
    await expect.poll(() => scrollLeft(page)).toBe(100);
    const view = await port(scroller(page));
    const stub = await rect(cell(page, "row_5", "stub"));
    // (The stub's still pinned)
    expect(stub.left).toBeGreaterThan(view.left);
    expect((await rect(cell(page, "row_5", "char"))).left).toBeLessThan(stub.right - 50);
    expect((await rect(cell(page, "row_5", "fctr"))).left).toBeGreaterThan(view.right);
    await expect(el(page).locator('.gt-i-shade[data-gti-edge="left"]')).toHaveAttribute("data-gti-shown");
    expect((await rect(el(page).locator('.gt-i-shade[data-gti-edge="left"]'))).left).toBeCloseTo(stub.right, 0);
    expect((await rect(el(page).locator('.gt-i-shade[data-gti-edge="right"]'))).right).toBeCloseTo(view.right, 0);

    await setWidth(page, "480px");
    await expect(cell(page, "row_5", "char")).toHaveClass(/gt-i-pinned/);
    await expect.poll(async () => (await rect(cell(page, "row_5", "fctr"))).right).toBeCloseTo(
      (await port(scroller(page))).right,
      0,
    );
    expect(errors).toEqual([]);
  });

  test("leave their column labels over their columns once the table fits", async ({ page }) => {
    const errors = await ready(page, "pin.html");
    await setWidth(page, "2400px");
    await expect(el(page)).not.toHaveAttribute("data-gti-wide");
    // (Not moved where they stuck, as the labels placed relative to themselves would be)
    for (const column of ["char", "fctr"]) {
      expect((await rect(label(page, column))).left).toBeCloseTo((await rect(cell(page, "row_5", column))).left, 0);
    }
    expect(errors).toEqual([]);
  });
});
