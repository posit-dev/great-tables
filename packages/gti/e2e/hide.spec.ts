import { readFile } from "node:fs/promises";
import { expect, type Locator, type Page, test } from "@playwright/test";
import { ready } from "./helpers";

// Hiding columns: exibble three times over (24 rows, grp_b then grp_a, each with a summary row),
// on one page, with set widths, char moved to the start and pinned there, and fctr moved to the
// end and pinned there, under a spanner ("Ends") with currency, in a container 480px wide; every
// data column hideable, datetime hidden at first; with a search and CSV export, the view kept in
// the URL. And right to left; and a table without a stub, of num and char, both hideable.

const el = (page: Page) => page.locator("gt-table");
const bar = (page: Page) => el(page).locator(".gt-i-bar");
const toggle = (page: Page) => bar(page).getByRole("button", { name: "Show or hide columns", exact: true });
const panel = (page: Page) => bar(page).getByRole("group", { name: "Columns", exact: true });
const box = (page: Page, name: string) => panel(page).getByRole("checkbox", { name, exact: true });
const showAll = (page: Page) => panel(page).getByRole("button", { name: "Show all" });
const hidden = (page: Page) => el(page).evaluate((node) => (node as any).hiddenColumns as string[]);
const search = (page: Page) => decodeURIComponent(new URL(page.url()).search);

const scroller = (page: Page) => el(page).locator(".gt-i-scroller");
const scrollTo = (page: Page, left: number) => scroller(page).evaluate((div, left) => div.scrollTo(left, 0), left);
const scrollLeft = (page: Page) => scroller(page).evaluate((div) => div.scrollLeft);

type Box = { left: number; right: number; width: number };
const rect = (locator: Locator): Promise<Box> =>
  locator.evaluate((node) => {
    const { left, right, width } = node.getBoundingClientRect();
    return { left, right, width };
  });
const port = (page: Page): Promise<Box> =>
  scroller(page).evaluate((div) => {
    const box = div.getBoundingClientRect();
    const left = box.left + div.clientLeft;
    return { left, right: left + div.clientWidth, width: div.clientWidth };
  });

// A column's label, and a data row's cell in it (by its index among the row's cells, the stub's 0)
const COLUMNS = ["stub", "char", "num", "date", "time", "datetime", "currency", "fctr"];
const label = (page: Page, column: string) => el(page).locator(`thead th[id$="-${column}"]`);
const row = (page: Page, text: string) => el(page).locator("tbody tr", { has: page.locator(`th.gt_stub:text-is("${text}")`) }).first();
const cell = (page: Page, text: string, column: string) => row(page, text).locator("> *").nth(COLUMNS.indexOf(column));
const spanner = (page: Page) => el(page).locator("thead .gt_column_spanner_outer", { hasText: "Ends" });

// Whether each shown column's label is over its cells
async function aligned(page: Page, columns: string[]) {
  for (const column of columns) {
    const [top, below] = [await rect(label(page, column)), await rect(cell(page, "row_5", column))];
    expect(below.left).toBeCloseTo(top.left, 0);
    expect(below.width).toBeCloseTo(top.width, 0);
  }
}

test.describe("hiding columns", () => {
  test("hides and shows columns from the Columns panel", async ({ page }) => {
    const errors = await ready(page, "hide.html");
    await expect(label(page, "datetime")).toBeHidden();
    await toggle(page).click();
    await expect(panel(page)).toBeVisible();
    await expect(panel(page).locator("label")).toHaveText(["char", "num", "date", "time", "datetime", "Ends – currency", "Ends – fctr"]);
    await expect(box(page, "datetime")).not.toBeChecked();
    await expect(box(page, "num")).toBeChecked();
    const date = await rect(label(page, "date"));

    await panel(page).locator("label", { hasText: "num" }).click();
    expect(await hidden(page)).toEqual(["num", "datetime"]);
    for (const hid of [label(page, "num"), cell(page, "row_5", "num"), cell(page, "Total", "num")]) {
      await expect(hid).toBeHidden();
    }
    await expect(el(page).locator(".gt-i-live")).toHaveText("num hidden");
    // (Each column keeps its width, and its label is over its cells)
    expect((await rect(label(page, "date"))).width).toBeCloseTo(date.width, 0);
    await aligned(page, ["char", "date", "time", "currency", "fctr"]);

    // From the keyboard, the panel staying open
    await box(page, "date").focus();
    await page.keyboard.press("Space");
    await expect(label(page, "date")).toBeHidden();
    await page.keyboard.press("Space");
    await expect(label(page, "date")).toBeVisible();
    await expect(panel(page)).toBeVisible();

    await showAll(page).click();
    expect(await hidden(page)).toEqual([]);
    await expect(label(page, "datetime")).toBeVisible();
    await expect(panel(page).getByRole("checkbox", { checked: false })).toHaveCount(0);
    await aligned(page, ["char", "num", "date", "time", "datetime", "currency", "fctr"]);
    await page.keyboard.press("Escape");
    expect(errors).toEqual([]);
  });

  test("narrows a spanner to the columns shown, and hides it over none", async ({ page }) => {
    const errors = await ready(page, "hide.html");
    await toggle(page).click();
    await box(page, "Ends – currency").uncheck();
    const fctr = await rect(label(page, "fctr"));
    const over = await rect(spanner(page));
    expect(over.left).toBeCloseTo(fctr.left, 0);
    expect(over.width).toBeCloseTo(fctr.width, 0);
    await box(page, "Ends – fctr").uncheck();
    await expect(spanner(page)).toBeHidden();
    await box(page, "Ends – currency").check();
    await expect(spanner(page)).toBeVisible();
    expect((await rect(spanner(page))).width).toBeCloseTo((await rect(label(page, "currency"))).width, 0);
    await aligned(page, ["char", "num", "date", "time", "currency"]);
    expect(errors).toEqual([]);
  });

  test("keeps the pinned columns at their sides, among the columns shown", async ({ page }) => {
    const errors = await ready(page, "hide.html");
    await el(page).evaluate((node) => ((node as any).hiddenColumns = ["char", "date"]));
    const view = await port(page);
    // (The columns after a hidden one take its place)
    expect((await rect(cell(page, "row_5", "num"))).left).toBeCloseTo((await rect(cell(page, "row_5", "stub"))).right, 0);
    await scrollTo(page, 99999);
    await expect.poll(() => scrollLeft(page)).toBeGreaterThan(50);
    expect((await rect(cell(page, "row_5", "fctr"))).right).toBeCloseTo(view.right, 0);
    await aligned(page, ["num", "time", "datetime", "currency", "fctr"]);

    // (With the column pinned at the end hidden, the others scroll up to the end)
    await el(page).evaluate((node) => ((node as any).hiddenColumns = ["date", "fctr"]));
    await scrollTo(page, 99999);
    const stub = await rect(cell(page, "row_5", "stub"));
    expect((await rect(cell(page, "row_5", "char"))).left).toBeCloseTo(stub.right, 0);
    expect((await rect(cell(page, "row_5", "currency"))).right).toBeCloseTo(view.right, 0);
    expect((await rect(cell(page, "row_5", "num"))).left).toBeLessThan(stub.right);
    expect(errors).toEqual([]);
  });

  test("keeps a hidden column's width as the reader resizes the others", async ({ page }) => {
    const errors = await ready(page, "hide.html");
    const num = await rect(label(page, "num"));
    const date = await rect(label(page, "date"));
    await el(page).evaluate((node) => ((node as any).hiddenColumns = ["num"]));
    await page.getByRole("separator", { name: "Resize date", exact: true }).focus();
    await page.keyboard.press("Shift+ArrowRight");
    expect((await rect(label(page, "date"))).width).toBeCloseTo(date.width + 50, 0);
    await el(page).evaluate((node) => ((node as any).hiddenColumns = []));
    expect((await rect(label(page, "num"))).width).toBeCloseTo(num.width, 0);
    expect((await rect(label(page, "date"))).width).toBeCloseTo(date.width + 50, 0);
    await aligned(page, ["char", "num", "date", "time", "datetime", "currency", "fctr"]);
    expect(errors).toEqual([]);
  });

  test("is mirrored right to left", async ({ page }) => {
    const errors = await ready(page, "hide-rtl.html");
    await toggle(page).click();
    await box(page, "char").uncheck();
    const view = await port(page);
    expect((await rect(cell(page, "row_5", "num"))).right).toBeCloseTo((await rect(cell(page, "row_5", "stub"))).left, 0);
    await scrollTo(page, -99999);
    await expect.poll(() => scrollLeft(page)).toBeLessThan(-50);
    expect((await rect(cell(page, "row_5", "fctr"))).left).toBeCloseTo(view.left, 0);
    await aligned(page, ["num", "date", "time", "currency", "fctr"]);
    expect(errors).toEqual([]);
  });

  test("keeps the columns hidden in the URL, and a reset shows the author's", async ({ page }) => {
    const errors = await ready(page, "hide.html");
    expect(search(page)).toBe("");
    await toggle(page).click();
    await box(page, "num").uncheck();
    expect(search(page)).toBe("?h.hidden=num&h.hidden=datetime");
    await page.reload();
    await expect(el(page)).toHaveAttribute("data-gti-state", "ready");
    expect(await hidden(page)).toEqual(["num", "datetime"]);
    await expect(label(page, "num")).toBeHidden();

    // (Every column shown is kept too, as none of the author's hidden)
    await toggle(page).click();
    await showAll(page).click();
    expect(search(page)).toBe("?h.hidden=");
    await page.reload();
    await expect(el(page)).toHaveAttribute("data-gti-state", "ready");
    await expect(label(page, "datetime")).toBeVisible();
    await el(page).evaluate((node) => (node as any).resetView());
    await expect(label(page, "datetime")).toBeHidden();
    expect(search(page)).toBe("");
    expect(errors).toEqual([]);
  });

  test("searches and exports the columns shown", async ({ page }) => {
    const errors = await ready(page, "hide.html");
    await el(page).evaluate((node) => ((node as any).search = "apricot"));
    await expect(row(page, "row_1")).toBeVisible();
    await el(page).evaluate((node) => ((node as any).hiddenColumns = ["char"]));
    await expect(row(page, "row_1")).toBeHidden();
    const empty = el(page).locator(".gt-i-empty td");
    await expect(empty).toBeVisible();
    expect((await rect(empty)).width).toBeCloseTo((await rect(el(page).locator("table"))).width, 0);
    await el(page).evaluate((node) => ((node as any).search = ""));

    await bar(page).getByRole("button", { name: "Export the table", exact: true }).click();
    const [file] = await Promise.all([
      page.waitForEvent("download"),
      bar(page).getByRole("group", { name: "Export", exact: true }).getByRole("button", { name: "Download CSV" }).click(),
    ]);
    const lines = (await readFile(await file.path())).subarray(3).toString("utf-8").split("\r\n");
    expect(lines[0]).toBe(",row,num,date,time,datetime,Ends – currency,Ends – fctr");
    expect(errors).toEqual([]);
  });

  test("can't hide the last column shown of a table without a stub", async ({ page }) => {
    const errors = await ready(page, "hide-nostub.html");
    await toggle(page).click();
    await box(page, "num").uncheck();
    await expect(box(page, "char")).toBeDisabled();
    await expect(box(page, "char")).toBeChecked();
    await box(page, "num").check();
    await expect(box(page, "char")).toBeEnabled();
    expect(errors).toEqual([]);
  });
});
