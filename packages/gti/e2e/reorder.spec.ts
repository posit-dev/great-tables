import { readFile } from "node:fs/promises";
import { expect, type Locator, type Page, test } from "@playwright/test";
import { ready } from "./helpers";

// Reordering columns: exibble three times over (24 rows, grp_b then grp_a, each with a summary
// row), on one page, with set widths, char moved to the start and pinned there, and currency and
// fctr moved to the end and pinned there, under a spanner ("Ends"), in a container 780px wide;
// every data column hideable and reorderable (so num, date, time and datetime move among
// themselves, and currency and fctr between them); with a search and CSV export, the view kept in
// the URL and changes undone. And right to left.

const el = (page: Page) => page.locator("gt-table");
const bar = (page: Page) => el(page).locator(".gt-i-bar");
const toggle = (page: Page) => bar(page).getByRole("button", { name: "Show, hide or reorder columns", exact: true });
const panel = (page: Page) => bar(page).getByRole("group", { name: "Columns", exact: true });
const move = (page: Page, name: string, way: "earlier" | "later") =>
  panel(page).getByRole("button", { name: `Move ${name} ${way}`, exact: true });
const item = (page: Page, id: string) => panel(page).locator(`[data-gti-column="${id}"]`);
const order = (page: Page) => el(page).evaluate((node) => (node as any).columnOrder as string[]);
const search = (page: Page) => decodeURIComponent(new URL(page.url()).search);
const live = (page: Page) => el(page).locator(".gt-i-live");

const scroller = (page: Page) => el(page).locator(".gt-i-scroller");
const scrollTo = (page: Page, left: number) => scroller(page).evaluate((div, left) => div.scrollTo(left, 0), left);
const scrollLeft = (page: Page) => scroller(page).evaluate((div) => div.scrollLeft);

type Box = { left: number; right: number; width: number; top: number; height: number };
const rect = (locator: Locator): Promise<Box> =>
  locator.evaluate((node) => {
    const { left, right, width, top, height } = node.getBoundingClientRect();
    return { left, right, width, top, height };
  });
const port = (page: Page): Promise<Box> =>
  scroller(page).evaluate((div) => {
    const box = div.getBoundingClientRect();
    const left = box.left + div.clientLeft;
    return { left, right: left + div.clientWidth, width: div.clientWidth, top: box.top, height: box.height };
  });

const AUTHOR = ["num", "date", "time", "datetime", "currency", "fctr"];
const WIDTHS: Record<string, number> = { char: 100, num: 140, date: 100, time: 100, datetime: 100, currency: 100, fctr: 100 };
const label = (page: Page, column: string) => el(page).locator(`thead th[id$="-${column}"]`);
const row = (page: Page, text: string) => el(page).locator("tbody tr", { has: page.locator(`th.gt_stub:text-is("${text}")`) }).first();
// A data row's cell in a column, where the columns are now (char can't move)
const cell = async (page: Page, text: string, column: string) =>
  row(page, text).locator("> *").nth(["stub", "char", ...(await order(page))].indexOf(column));
const spanner = (page: Page) => el(page).locator("thead .gt_column_spanner_outer", { hasText: "Ends" });

// Whether the columns are shown in this order, each label over its cells (in a data row and a
// summary row), each as wide as it was set to be (or as `widths` has it)
async function shownIn(page: Page, columns: string[], widths: Record<string, number> = {}) {
  let left = (await rect(label(page, columns[0] as string))).left;
  for (const column of columns) {
    const top = await rect(label(page, column));
    expect(top.left).toBeCloseTo(left, 0);
    expect(top.width).toBeCloseTo((widths[column] ?? WIDTHS[column]) as number, 0);
    for (const below of [await rect(await cell(page, "row_5", column)), await rect(await cell(page, "Total", column))]) {
      expect(below.left).toBeCloseTo(top.left, 0);
      expect(below.width).toBeCloseTo(top.width, 0);
    }
    left = top.right;
  }
}

test.describe("reordering columns", () => {
  test("moves columns from the Columns panel, with their widths", async ({ page }) => {
    const errors = await ready(page, "reorder.html");
    await toggle(page).click();
    await expect(panel(page).locator(".gt-i-column")).toHaveText(["char", "num", "date", "time", "datetime", "Ends – currency", "Ends – fctr"]);
    // (char can't move: it's alone, at its side)
    await expect(item(page, "char").locator("button")).toHaveCount(0);
    await expect(move(page, "num", "earlier")).toHaveAttribute("aria-disabled", "true");
    await expect(move(page, "datetime", "later")).toHaveAttribute("aria-disabled", "true");

    await move(page, "num", "later").click();
    expect(await order(page)).toEqual(["date", "num", "time", "datetime", "currency", "fctr"]);
    await expect(live(page)).toHaveText("num moved after date");
    await expect(panel(page).locator(".gt-i-column")).toHaveText(["char", "date", "num", "time", "datetime", "Ends – currency", "Ends – fctr"]);
    await expect(move(page, "num", "later")).toBeFocused();
    await expect(panel(page)).toBeVisible();
    await shownIn(page, ["char", "date", "num", "time", "datetime"]);

    // From the keyboard
    await page.keyboard.press("Alt+ArrowDown");
    await page.keyboard.press("Alt+ArrowDown");
    expect(await order(page)).toEqual(["date", "time", "datetime", "num", "currency", "fctr"]);
    await expect(move(page, "num", "later")).toBeFocused();
    await expect(live(page)).toHaveText("num moved after datetime");
    await shownIn(page, ["char", "date", "time", "datetime", "num"]);

    // (A column hidden is passed over)
    await panel(page).getByRole("checkbox", { name: "datetime", exact: true }).uncheck();
    await move(page, "num", "earlier").click();
    expect(await order(page)).toEqual(["date", "num", "time", "datetime", "currency", "fctr"]);
    await expect(live(page)).toHaveText("num moved after date");
    await panel(page).getByRole("checkbox", { name: "datetime", exact: true }).check();
    await shownIn(page, ["char", "date", "num", "time", "datetime"]);

    await panel(page).getByRole("button", { name: "Reset order" }).click();
    expect(await order(page)).toEqual(AUTHOR);
    await shownIn(page, ["char", "num", "date", "time", "datetime"]);
    expect(errors).toEqual([]);
  });

  test("moves a column dragged by its handle", async ({ page }) => {
    const errors = await ready(page, "reorder.html");
    await toggle(page).click();
    const grip = await rect(item(page, "datetime").locator(".gt-i-column-grip"));
    const num = await rect(item(page, "num"));
    await page.mouse.move(grip.left + grip.width / 2, grip.top + grip.height / 2);
    await page.mouse.down();
    await page.mouse.move(grip.left + grip.width / 2, num.top + 2, { steps: 5 });
    await expect(item(page, "datetime")).toHaveAttribute("data-gti-dragging", "");
    await expect(panel(page).locator(".gt-i-column").nth(1)).toHaveText("datetime");
    // (It doesn't move until it's dropped)
    expect(await order(page)).toEqual(AUTHOR);
    await page.mouse.up();
    expect(await order(page)).toEqual(["datetime", "num", "date", "time", "currency", "fctr"]);
    await expect(live(page)).toHaveText("datetime moved before num");
    await shownIn(page, ["char", "datetime", "num", "date", "time"]);

    // Escape puts it back, and leaves the panel open
    const handle = await rect(item(page, "time").locator(".gt-i-column-grip"));
    await page.mouse.move(handle.left + handle.width / 2, handle.top + handle.height / 2);
    await page.mouse.down();
    await page.mouse.move(handle.left + handle.width / 2, num.top - 20, { steps: 5 });
    await page.keyboard.press("Escape");
    await page.mouse.up();
    await expect(panel(page)).toBeVisible();
    await expect(panel(page).locator(".gt-i-column")).toHaveText(["char", "datetime", "num", "date", "time", "Ends – currency", "Ends – fctr"]);
    expect(await order(page)).toEqual(["datetime", "num", "date", "time", "currency", "fctr"]);
    expect(errors).toEqual([]);
  });

  test("keeps the pinned columns at their side, under their spanner", async ({ page }) => {
    const errors = await ready(page, "reorder.html");
    const view = await port(page);
    await el(page).evaluate((node) => ((node as any).columnOrder = ["fctr"]));
    expect(await order(page)).toEqual(["num", "date", "time", "datetime", "fctr", "currency"]);
    // (Pinned at the end, currency is now at the edge, and fctr before it)
    expect((await rect(await cell(page, "row_5", "currency"))).right).toBeCloseTo(view.right, 0);
    expect((await rect(await cell(page, "row_5", "fctr"))).right).toBeCloseTo(view.right - 100, 0);
    await scrollTo(page, 99999);
    await expect.poll(() => scrollLeft(page)).toBeGreaterThan(20);
    expect((await rect(await cell(page, "row_5", "currency"))).right).toBeCloseTo(view.right, 0);
    const ends = await rect(spanner(page));
    expect(ends.left).toBeCloseTo((await rect(label(page, "fctr"))).left, 0);
    expect(ends.right).toBeCloseTo((await rect(label(page, "currency"))).right, 0);
    await shownIn(page, ["fctr", "currency"]);
    expect(errors).toEqual([]);
  });

  test("keeps a column's width the reader set as it moves", async ({ page }) => {
    const errors = await ready(page, "reorder.html");
    await page.getByRole("separator", { name: "Resize num", exact: true }).focus();
    await page.keyboard.press("Shift+ArrowRight");
    await el(page).evaluate((node) => ((node as any).columnOrder = ["date", "time", "num"]));
    await shownIn(page, ["char", "date", "time", "num", "datetime"], { num: 190 });
    // (And the one resized next is the one where it is)
    await page.getByRole("separator", { name: "Resize time", exact: true }).focus();
    await page.keyboard.press("Shift+ArrowLeft");
    await shownIn(page, ["char", "date", "time", "num", "datetime"], { num: 190, time: 50 });
    expect(errors).toEqual([]);
  });

  test("is mirrored right to left", async ({ page }) => {
    const errors = await ready(page, "reorder-rtl.html");
    await toggle(page).click();
    await move(page, "num", "later").click();
    const [date, num] = [await rect(label(page, "date")), await rect(label(page, "num"))];
    expect(num.right).toBeCloseTo(date.left, 0);
    for (const column of ["date", "num", "time"]) {
      const [top, below] = [await rect(label(page, column)), await rect(await cell(page, "row_5", column))];
      expect(below.left).toBeCloseTo(top.left, 0);
      expect(below.width).toBeCloseTo(top.width, 0);
    }
    // (Pinned at the end, on the left)
    const view = await port(page);
    await move(page, "Ends – fctr", "earlier").click();
    expect((await rect(await cell(page, "row_5", "currency"))).left).toBeCloseTo(view.left, 0);
    expect((await rect(await cell(page, "row_5", "fctr"))).left).toBeCloseTo(view.left + 100, 0);
    expect(errors).toEqual([]);
  });

  test("keeps the order in the URL, undoes a move, and a reset puts back the author's", async ({ page }) => {
    const errors = await ready(page, "reorder.html");
    await toggle(page).click();
    await move(page, "Ends – fctr", "earlier").click();
    expect(search(page)).toBe("?r.order=num&r.order=date&r.order=time&r.order=datetime&r.order=fctr&r.order=currency");
    await move(page, "time", "earlier").click();
    await bar(page).getByRole("button", { name: "Undo", exact: true }).click();
    expect(await order(page)).toEqual(["num", "date", "time", "datetime", "fctr", "currency"]);
    await page.reload();
    await expect(el(page)).toHaveAttribute("data-gti-state", "ready");
    expect(await order(page)).toEqual(["num", "date", "time", "datetime", "fctr", "currency"]);
    await shownIn(page, ["fctr", "currency"]);
    await el(page).evaluate((node) => (node as any).resetView());
    expect(await order(page)).toEqual(AUTHOR);
    expect(search(page)).toBe("");
    expect(errors).toEqual([]);
  });

  test("searches and exports the columns in the order shown", async ({ page }) => {
    const errors = await ready(page, "reorder.html");
    await el(page).evaluate((node) => ((node as any).columnOrder = ["time", "num"]));
    await el(page).evaluate((node) => ((node as any).search = "apricot"));
    await expect(row(page, "row_1")).toBeVisible();
    await expect(row(page, "row_2")).toBeHidden();
    await el(page).evaluate((node) => ((node as any).search = ""));

    await bar(page).getByRole("button", { name: "Export the table", exact: true }).click();
    const [file] = await Promise.all([
      page.waitForEvent("download"),
      bar(page).getByRole("group", { name: "Export", exact: true }).getByRole("button", { name: "Download CSV" }).click(),
    ]);
    const lines = (await readFile(await file.path())).subarray(3).toString("utf-8").split("\r\n");
    expect(lines[0]).toBe(",row,char,time,num,date,datetime,Ends – currency,Ends – fctr");
    expect(lines[1]).toMatch(/^grp_b,row_5,None,17:55,"5,550.00",2015-05-15,/);
    expect(errors).toEqual([]);
  });
});
