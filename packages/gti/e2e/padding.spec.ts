import { expect, type Locator, type Page, test } from "@playwright/test";
import { borderLines, dataRows, ready, visible } from "./helpers";

// exibble without its groups (8 rows), striped, selectable and searchable, 5 rows to a page (or
// 10): the second page shows rows 5-7, padded with two empty rows. As GT draws it, and in a
// container 300px wide, with the selection column and the stub pinned.

const el = (page: Page) => page.locator("gt-table");
const table = (page: Page) => el(page).locator("table");
const fillers = (page: Page) => el(page).locator("tbody tr.gt-i-filler");
const pageButton = (page: Page, name: string) =>
  el(page).locator("nav.gt-i-pager").getByRole("button", { name, exact: true });
const info = (page: Page) => el(page).locator(".gt-i-page-info");
const height = (locator: Locator) => locator.evaluate((node) => node.getBoundingClientRect().height);
const selection = (page: Page) => el(page).evaluate((node) => (node as any).selection as number[]);

test("pads a short page to the height of a full one", async ({ page }) => {
  const errors = await ready(page, "pad.html");
  const full = await height(table(page));
  await expect(fillers(page)).toHaveCount(0);

  await pageButton(page, "Page 2").click();
  expect(dataRows(await visible(page))).toEqual([5, 6, 7]);
  await expect(info(page)).toHaveText("6–8 of 8 rows");
  await expect(fillers(page)).toHaveCount(2);
  expect(await height(table(page))).toBeCloseTo(full, 1);
  // Empty, unstriped, and hidden from screen readers, with a cell in each column
  const cells = await el(page).locator("tbody tr:not(.gt-i-filler)").first().locator("th, td").count();
  for (const tr of await fillers(page).all()) {
    await expect(tr).toHaveAttribute("aria-hidden", "true");
    await expect(tr.locator("td")).toHaveCount(cells);
    await expect(tr).toHaveText("");
    await expect(tr.locator(".gt_striped")).toHaveCount(0);
  }
  // As a data row is tall
  const row = await height(el(page).locator("tbody tr:not(.gt-i-filler, [hidden])").first());
  expect(Math.abs((await height(fillers(page).first())) - row)).toBeLessThan(1);

  await pageButton(page, "Page 1").click();
  await expect(fillers(page)).toHaveCount(0);
  expect(await height(table(page))).toBeCloseTo(full, 1);
  expect(errors).toEqual([]);
});

test("pads the rows a search finds, and the row saying that none do", async ({ page }) => {
  const errors = await ready(page, "pad.html");
  const full = await height(table(page));
  const search = el(page).locator("input.gt-i-search");

  await search.fill("apricot");
  await expect(info(page)).toHaveText("1 of 1 row (filtered from 8)");
  await expect(fillers(page)).toHaveCount(4);
  expect(await height(table(page))).toBeCloseTo(full, 1);

  await search.fill("zzz");
  await expect(el(page).locator("tr.gt-i-empty")).toBeVisible();
  await expect(fillers(page)).toHaveCount(4);
  expect(await height(table(page))).toBeCloseTo(full, 1);
  // (After it)
  expect(await el(page).locator("tr.gt-i-empty + tr.gt-i-filler").count()).toBe(1);

  await search.fill("");
  await expect(fillers(page)).toHaveCount(0);
  expect(errors).toEqual([]);
});

test("doesn't pad a page that every row fits on", async ({ page }) => {
  await ready(page, "pad.html");
  await pageButton(page, "Page 2").click();
  await expect(fillers(page)).toHaveCount(2);
  await el(page).locator("nav.gt-i-pager select").selectOption("10");
  expect(dataRows(await visible(page))).toHaveLength(8);
  await expect(fillers(page)).toHaveCount(0);
});

test("doesn't select an empty row, or count it", async ({ page }) => {
  const errors = await ready(page, "pad.html");
  await pageButton(page, "Page 2").click();
  await fillers(page).first().click();
  expect(await selection(page)).toEqual([]);

  await el(page).locator("thead input[type=checkbox]").click();
  expect(await selection(page)).toEqual([0, 1, 2, 3, 4, 5, 6, 7]);
  await expect(el(page).locator("tr.gt-i-filler.gt-i-selected")).toHaveCount(0);
  await expect(fillers(page).locator("input")).toHaveCount(0);
  expect(errors).toEqual([]);
});

test("pads to a full page's height again when the table's width changes", async ({ page }) => {
  const errors = await ready(page, "pad.html");
  const wide = await height(table(page));
  await pageButton(page, "Page 2").click();
  // (Narrower, the table's text wraps, and its rows are taller)
  await page.setViewportSize({ width: 420, height: 800 });
  await expect.poll(() => height(table(page))).toBeGreaterThan(wide + 20);
  await page.waitForTimeout(100);
  const short = await height(table(page));
  await pageButton(page, "Page 1").click();
  expect(await height(table(page))).toBeCloseTo(short, 1);
  expect(errors).toEqual([]);
});

for (const name of ["pad.html", "pad-wide.html"]) {
  test(`draws the empty rows' lines as a data row's (${name})`, async ({ page }) => {
    const errors = await ready(page, name);
    if (name === "pad-wide.html") {
      await expect(el(page)).toHaveAttribute("data-gti-wide", "");
      await page.addStyleTag({ content: "gt-table .gt-i-shade, gt-table .gt-i-hint { visibility: hidden }" });
    }
    const width = await el(page).locator(".gt-i-scroller").evaluate((div) => div.clientWidth);
    // Across a data row, then an empty row: the same lines between the columns
    const across = (tr: Locator) =>
      tr.evaluate((row) => {
        const box = (row.closest("table") as HTMLElement).getBoundingClientRect();
        const { top, bottom } = row.getBoundingClientRect();
        return ((top + bottom) / 2 - box.top) / (box.height - 1);
      });
    await pageButton(page, "Page 2").click();
    const row = await borderLines(page, table(page), { y: await across(el(page).locator("tbody tr:not([hidden])").first()), width });
    expect(row.length).toBeGreaterThan(0);
    expect(await borderLines(page, table(page), { y: await across(fillers(page).last()), width })).toEqual(row);
    // And down through the rows, with as many lines between them
    const x = await el(page)
      .locator("tbody tr:not([hidden])")
      .first()
      .locator("td")
      .nth(2)
      .evaluate((cell) => {
        const { left, right } = cell.getBoundingClientRect();
        return (left + right) / 2;
      });
    await pageButton(page, "Page 1").click();
    const down = await borderLines(page, table(page), { x });
    await pageButton(page, "Page 2").click();
    expect((await borderLines(page, table(page), { x })).length).toBe(down.length);
    expect(errors).toEqual([]);
  });
}
