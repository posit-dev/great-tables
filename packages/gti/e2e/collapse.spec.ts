import { expect, type Locator, type Page, test } from "@playwright/test";
import { readFile } from "node:fs/promises";
import { groupCells, ready } from "./helpers";

// exibble (8 rows, grp_b then grp_a, each with a summary row), with a spanner over num and
// currency, a stub, selectable rows, a search, CSV export and columns that can be hidden, 5 to a
// page, dropping columns to fit its container: num has priority 1 (never dropped), char 2 and
// currency 3, and fctr and date none (so date goes first, then fctr, currency and char). In a
// container 360px wide; in one 1000px wide; right to left; with groups as a column, in a body that
// scrolls; with column widths; without a stub; and in a container too narrow for what's left. All
// in a monospace font, so the same columns are dropped at a width on any system.

const DROPS = ["date", "fctr", "currency", "char"];

const el = (page: Page) => page.locator("gt-table");
const scroller = (page: Page) => el(page).locator(".gt-i-scroller");
const row = (page: Page, label: string) => el(page).locator("tbody tr", { has: page.locator(`th.gt_stub:text-is("${label}")`) }).first();
const button = (page: Page, label: string) => row(page, label).locator(".gt-i-expand");
// The row under a row, showing the columns dropped from it
const details = (page: Page, label: string) => row(page, label).locator("+ tr.gt-i-details");
const setWidth = (page: Page, width: string) =>
  el(page).evaluate((node, width) => ((node.parentElement as HTMLElement).style.width = width), width);

// The columns dropped (or hidden), by their labels not shown
const gone = (page: Page) =>
  el(page).evaluate((node) =>
    Array.from(node.querySelectorAll("thead th[id]"), (th) => (th.getClientRects().length === 0 ? th.id.slice(2) : "")).filter(Boolean),
  );
const overflow = (page: Page) => scroller(page).evaluate((div) => div.scrollWidth - div.clientWidth);

type Box = { top: number; bottom: number; left: number; right: number };
const rect = (locator: Locator): Promise<Box> =>
  locator.evaluate((node) => {
    const { top, bottom, left, right } = node.getBoundingClientRect();
    return { top, bottom, left, right };
  });

// A row's dropped columns, as their labels and values
const shownUnder = (page: Page, label: string) =>
  details(page, label)
    .locator("dl")
    .evaluate((dl) => Array.from(dl.querySelectorAll("dt"), (dt) => [dt.textContent, (dt.nextElementSibling as HTMLElement).textContent?.trim()]));

test.describe("a table that drops columns", () => {
  test("drops its least important columns first, to fit a narrow container", async ({ page }) => {
    const errors = await ready(page, "collapse.html");
    await expect(el(page)).toHaveAttribute("data-gti-dropped", "");
    await expect(el(page)).not.toHaveAttribute("data-gti-wide");
    expect((await gone(page)).sort()).toEqual([...DROPS].sort());
    expect(await overflow(page)).toBeLessThanOrEqual(1);
    // (The stub, num and the spanner over it stay; the select-all box too)
    await expect(el(page).locator("thead th#c-num")).toBeVisible();
    await expect(el(page).locator("thead .gt_column_spanner_outer", { hasText: "Numbers" })).toBeVisible();
    await expect(row(page, "row_5").locator("td.gt-i-select input")).toBeVisible();
    // (And it isn't stacked, as an "auto" table without priorities would be)
    await expect(el(page)).not.toHaveAttribute("data-gti-stack");
    expect(errors).toEqual([]);
  });

  test("has its columns back, in the order dropped, as its container widens, and drops them again", async ({ page }) => {
    const errors = await ready(page, "collapse.html");
    const counts: number[] = [];
    for (const width of ["440px", "520px", "600px", "1000px", "360px"]) {
      await setWidth(page, width);
      await expect.poll(() => overflow(page)).toBeLessThanOrEqual(1);
      await page.waitForTimeout(100);
      const dropped = await gone(page);
      // (Always the first of those that go)
      expect(dropped.sort()).toEqual(DROPS.slice(0, dropped.length).sort());
      counts.push(dropped.length);
    }
    expect(counts.slice(0, 4)).toEqual([...counts.slice(0, 4)].sort((a, b) => b - a));
    expect(counts[3]).toBe(0);
    expect(counts[4]).toBe(4);
    // (With nothing dropped, the buttons are gone)
    await setWidth(page, "1000px");
    await expect(el(page)).not.toHaveAttribute("data-gti-dropped");
    await expect(button(page, "row_5")).toBeHidden();
    await expect(row(page, "row_5").locator("td")).toHaveCount(6);
    expect(errors).toEqual([]);
  });

  test("drops none in a container wide enough", async ({ page }) => {
    const errors = await ready(page, "collapse-wide.html");
    await expect(el(page)).not.toHaveAttribute("data-gti-dropped");
    expect(await gone(page)).toEqual([]);
    await expect(el(page).locator(".gt-i-expand")).toHaveCount(0);
    expect(errors).toEqual([]);
  });

  test("shows a row's dropped columns under it, from the button by its first cell", async ({ page }) => {
    const errors = await ready(page, "collapse.html");
    const toggle = button(page, "row_5");
    await expect(toggle).toHaveAttribute("aria-label", "Show more of row_5");
    await expect(toggle).toHaveAttribute("aria-expanded", "false");
    // (Before the stub's text, on its line)
    const stub = row(page, "row_5").locator("th.gt_stub");
    await expect(stub.locator(".gt-i-expand")).toHaveCount(1);
    const box = await rect(toggle);
    const text = await stub.evaluate((th) => {
      const range = document.createRange();
      range.selectNodeContents(th.lastChild as Node);
      const { left, top, bottom } = range.getBoundingClientRect();
      return { left, top, bottom };
    });
    expect(box.right).toBeLessThanOrEqual(text.left + 1);
    expect(box.top).toBeLessThan(text.bottom);
    expect(box.bottom).toBeGreaterThan(text.top);

    await toggle.click();
    await expect(toggle).toHaveAttribute("aria-expanded", "true");
    await expect(details(page, "row_5")).toBeVisible();
    // The dropped columns' labels (with their spanner's) and values, in the columns' order
    expect(await shownUnder(page, "row_5")).toEqual([
      ["Numbers – currency", "$1,325.81"],
      ["char", "None"],
      ["fctr", "five"],
      ["date", "2015-05-15"],
    ]);
    // (Across the row, under it)
    const under = await rect(details(page, "row_5"));
    const above = await rect(row(page, "row_5"));
    expect(under.top).toBeCloseTo(above.bottom, 0);
    expect(under.left).toBeCloseTo(above.left, 0);
    expect(under.right).toBeCloseTo(above.right, 0);
    // (The row's own cells are as they were)
    await expect(row(page, "row_5").locator('td[headers~="c-currency"]')).toBeHidden();
    await expect(row(page, "row_5").locator('td[headers~="c-currency"]')).toHaveText("$1,325.81");

    // Its button again hides them, and Enter on it shows them
    await toggle.click();
    await expect(toggle).toHaveAttribute("aria-expanded", "false");
    await expect(el(page).locator("tr.gt-i-details")).toHaveCount(0);
    await toggle.focus();
    await page.keyboard.press("Enter");
    await expect(details(page, "row_5")).toBeVisible();
    await expect(toggle).toBeFocused();
    expect(errors).toEqual([]);
  });

  test("shows a summary row's dropped columns", async ({ page }) => {
    const errors = await ready(page, "collapse.html");
    const total = button(page, "Total");
    await expect(total).toHaveAttribute("aria-label", "Show more of Total");
    await total.click();
    expect((await shownUnder(page, "Total"))[0]).toEqual(["Numbers – currency", "1339.505"]);
    // (Group headings have none)
    await expect(el(page).locator("tr.gt_group_heading_row .gt-i-expand")).toHaveCount(0);
    expect(errors).toEqual([]);
  });

  test("shows what's dropped as it changes, and closes the rows once nothing is", async ({ page }) => {
    const errors = await ready(page, "collapse.html");
    await button(page, "row_5").click();
    await button(page, "row_6").click();
    await setWidth(page, "520px");
    await expect.poll(async () => (await gone(page)).length).toBeLessThan(4);
    const dropped = await gone(page);
    expect(dropped.length).toBeGreaterThan(0);
    for (const label of ["row_5", "row_6"]) {
      await expect(details(page, label).locator("dt")).toHaveCount(dropped.length);
    }
    await setWidth(page, "1000px");
    await expect(el(page)).not.toHaveAttribute("data-gti-dropped");
    await expect(el(page).locator("tr.gt-i-details")).toHaveCount(0);
    // (And open none when they're dropped again)
    await setWidth(page, "360px");
    await expect(el(page)).toHaveAttribute("data-gti-dropped", "");
    await expect(el(page).locator("tr.gt-i-details")).toHaveCount(0);
    await expect(button(page, "row_5")).toHaveAttribute("aria-expanded", "false");
    expect(errors).toEqual([]);
  });

  test("doesn't select a row from its button, or the row under it", async ({ page }) => {
    const errors = await ready(page, "collapse.html");
    const selection = () => el(page).evaluate((node) => (node as any).selection as number[]);
    await button(page, "row_5").click();
    await details(page, "row_5").locator("dd").first().click();
    expect(await selection()).toEqual([]);
    // (The row itself is)
    await row(page, "row_5").locator('td[headers~="c-num"]').click();
    expect(await selection()).toEqual([4]);
    await expect(details(page, "row_5")).toBeVisible();
    expect(errors).toEqual([]);
  });

  test("keeps a row's dropped columns under it as it's sorted, paged and searched", async ({ page }) => {
    const errors = await ready(page, "collapse.html");
    await button(page, "row_5").click();
    // (Sorted by num, descending: row_8, row_7, row_5 in grp_b)
    const sort = el(page).locator("th#c-num > button.gt-i-sort");
    await sort.click();
    await sort.click();
    await expect(el(page).locator("th#c-num")).toHaveAttribute("aria-sort", "descending");
    await expect(details(page, "row_5")).toBeVisible();
    // (Hidden with its row, on another page)
    await el(page).getByRole("navigation", { name: "Table pages" }).getByRole("button", { name: "Next page" }).click();
    await expect(el(page).locator("tr.gt-i-details")).toBeHidden();
    await el(page).getByRole("navigation", { name: "Table pages" }).getByRole("button", { name: "Previous page" }).click();
    await expect(details(page, "row_5")).toBeVisible();
    // (And the search finds text in the columns dropped)
    await el(page).locator(".gt-i-bar").getByRole("button", { name: "Search" }).click();
    await el(page).getByRole("searchbox").fill("honeydew");
    await expect(row(page, "row_8")).toBeVisible();
    await expect(row(page, "row_5")).toBeHidden();
    await expect(el(page).locator("tr.gt-i-details")).toBeHidden();
    expect(errors).toEqual([]);
  });

  test("exports the columns dropped", async ({ page }) => {
    const errors = await ready(page, "collapse.html");
    await el(page).locator(".gt-i-bar").getByRole("button", { name: "Export the table", exact: true }).click();
    const [file] = await Promise.all([
      page.waitForEvent("download"),
      el(page).getByRole("group", { name: "Export", exact: true }).getByRole("button", { name: "Download CSV" }).click(),
    ]);
    const text = (await readFile(await file.path())).subarray(3).toString("utf-8");
    expect(text.split("\r\n")[0]).toBe(",row,Numbers – num,Numbers – currency,char,fctr,date");
    expect(errors).toEqual([]);
  });

  test("leaves out the columns readers hide, and has room for others", async ({ page }) => {
    const errors = await ready(page, "collapse.html");
    await button(page, "row_5").click();
    await el(page).evaluate((node) => ((node as any).hiddenColumns = ["fctr"]));
    await expect(details(page, "row_5").locator("dt")).toHaveText(["Numbers – currency", "char", "date"]);
    // (Hiding num makes room for some of those dropped)
    await el(page).evaluate((node) => ((node as any).hiddenColumns = ["num"]));
    await expect.poll(async () => (await gone(page)).length).toBeLessThan(DROPS.length + 1);
    const dropped = (await gone(page)).filter((id) => id !== "num");
    expect(dropped.sort()).toEqual(DROPS.slice(0, dropped.length).sort());
    expect(dropped.length).toBeLessThan(DROPS.length);
    expect(await overflow(page)).toBeLessThanOrEqual(1);
    // (And a column a reader shows again is dropped if there's no room for it)
    await el(page).evaluate((node) => ((node as any).hiddenColumns = []));
    await expect.poll(async () => (await gone(page)).sort()).toEqual([...DROPS].sort());
    expect(await overflow(page)).toBeLessThanOrEqual(1);
    expect(errors).toEqual([]);
  });

  test("with groups as a column, has the group's label cell span the rows under its rows", async ({ page }) => {
    const errors = await ready(page, "collapse-column.html");
    await expect(el(page)).toHaveAttribute("data-gti-dropped", "");
    // (The button is in the stub, not the group's label cell)
    await expect(row(page, "row_5").locator("th.gt_stub .gt-i-expand")).toHaveCount(1);
    for (const label of ["row_5", "row_7", "Total"]) {
      await button(page, label).click();
    }
    const cells = await groupCells(page);
    expect(cells.map((cell) => [cell.label, cell.fits])).toEqual([
      ["grp_b", true],
      ["grp_a", true],
    ]);
    // (Under the label cell, as far as the row's last cell)
    // (With a cell of its own in the selection column, before it)
    await expect(details(page, "row_7").locator("> td")).toHaveCount(2);
    await expect(details(page, "row_7").locator("> td").first()).toHaveClass(/gt-i-select/);
    const under = await rect(details(page, "row_7").locator("> td").last());
    const groupCell = await rect(el(page).locator("th.gt_stub_row_group").first());
    expect(under.left).toBeCloseTo(groupCell.right, 0);
    expect(under.right).toBeCloseTo((await rect(row(page, "row_7"))).right, 0);
    expect(errors).toEqual([]);
  });

  test("measures its columns' widths for what's shown", async ({ page }) => {
    const errors = await ready(page, "collapse-widths.html");
    expect((await gone(page)).sort()).toEqual([...DROPS].sort());
    expect(await overflow(page)).toBeLessThanOrEqual(1);
    await setWidth(page, "1000px");
    await expect.poll(() => gone(page)).toEqual([]);
    // (At least the author's widths, and date's fitted to it)
    const width = (column: string) => el(page).locator(`thead th#c-${column}`).evaluate((th) => th.getBoundingClientRect().width);
    expect(await width("num")).toBeGreaterThanOrEqual(120);
    expect(await width("char")).toBeGreaterThanOrEqual(100);
    const date = await row(page, "row_5").locator('td[headers~="c-date"]').evaluate((td) => td.scrollWidth - td.clientWidth);
    expect(date).toBeLessThanOrEqual(0);
    expect(await overflow(page)).toBeLessThanOrEqual(1);
    expect(errors).toEqual([]);
  });

  test("is mirrored right to left", async ({ page }) => {
    const errors = await ready(page, "collapse-rtl.html");
    expect((await gone(page)).sort()).toEqual([...DROPS].sort());
    expect(await overflow(page)).toBeLessThanOrEqual(1);
    // (The button is before the stub's text: to its right)
    const stub = row(page, "row_5").locator("th.gt_stub");
    const box = await rect(button(page, "row_5"));
    const text = await stub.evaluate((th) => {
      const range = document.createRange();
      range.selectNodeContents(th.lastChild as Node);
      return range.getBoundingClientRect().right;
    });
    expect(box.left).toBeGreaterThanOrEqual(text - 1);
    expect(box.right).toBeLessThanOrEqual((await rect(stub)).right);
    await button(page, "row_5").click();
    expect((await shownUnder(page, "row_5"))[0]).toEqual(["Numbers – currency", "$1,325.81"]);
    expect(errors).toEqual([]);
  });

  test("without a stub, has the button in each row's first cell", async ({ page }) => {
    const errors = await ready(page, "collapse-nostub.html");
    await expect(el(page)).toHaveAttribute("data-gti-dropped", "");
    const first = el(page).locator("tbody tr").first();
    await expect(first.locator("td").first().locator(".gt-i-expand")).toHaveAttribute("aria-label", "Show more of the row");
    // (char has priority 1; num, without one, stays while there's room for it)
    expect(await gone(page)).not.toContain("char");
    await first.locator(".gt-i-expand").click();
    await expect(first.locator("+ tr.gt-i-details dt")).toHaveText(await gone(page));
    expect(errors).toEqual([]);
  });

  test("in a container too narrow for what it can't drop, scrolls with its stub and the rows under its rows in view", async ({ page }) => {
    const errors = await ready(page, "collapse-narrow.html");
    await expect(el(page)).toHaveAttribute("data-gti-wide", "");
    expect((await gone(page)).sort()).toEqual([...DROPS].sort());
    await button(page, "row_5").click();
    await scroller(page).evaluate((div) => div.scrollTo(99999, 0));
    await expect.poll(() => scroller(page).evaluate((div) => div.scrollLeft)).toBeGreaterThan(50);
    const view = await rect(scroller(page));
    const stub = await rect(row(page, "row_5").locator("th.gt_stub"));
    expect(stub.left).toBeGreaterThanOrEqual(view.left - 1);
    const list = await rect(details(page, "row_5").locator("dl"));
    expect(list.left).toBeGreaterThanOrEqual(view.left - 1);
    expect(list.right).toBeLessThanOrEqual(view.right + 1);
    // (Its button still works from the pinned stub)
    await button(page, "row_6").click();
    await expect(details(page, "row_6")).toBeVisible();
    expect(errors).toEqual([]);
  });
});

test.describe("on a touch screen", () => {
  test.use({ hasTouch: true, isMobile: true });

  test("the buttons are big enough to tap", async ({ page }) => {
    const errors = await ready(page, "collapse.html");
    const target = await button(page, "row_5").evaluate((node) => {
      const style = getComputedStyle(node, "::before");
      return { width: parseFloat(style.width), height: parseFloat(style.height) };
    });
    expect(target).toEqual({ width: 44, height: 44 });
    await button(page, "row_5").tap();
    await expect(details(page, "row_5")).toBeVisible();
    expect(errors).toEqual([]);
  });
});
