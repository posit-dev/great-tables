import { expect, type Locator, type Page, test } from "@playwright/test";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { dataRows, open, ready, visible } from "./helpers";

// GTI tables, with the control bar below them: exibble three times over (24 rows, in two groups),
// 2 rows to a page (12 pages), with a search; as narrow as one column; in a container 300px wide;
// and on one page, with room to scroll past it.

const RUNTIME = join(dirname(fileURLToPath(import.meta.url)), "..", "..", "..", "great_tables", "js", "gti.js");

const el = (page: Page) => page.locator("gt-table");
const bar = (page: Page) => el(page).locator(".gt-i-bar");
const barButton = (page: Page, name: string) => bar(page).getByRole("button", { name, exact: true });
const field = (page: Page) => bar(page).locator(".gt-i-search-field");
const search = (page: Page) => bar(page).locator("input.gt-i-search");
const pages = (page: Page) => bar(page).locator(".gt-i-bar-pages");
const readout = (page: Page) => bar(page).locator("button.gt-i-readout");
const pageOf = (page: Page) => el(page).evaluate((node) => (node as any).page as number);
const box = (locator: Locator) =>
  locator.evaluate((node) => {
    const { left, right, top, bottom, width } = node.getBoundingClientRect();
    return { left, right, top, bottom, width };
  });

test("is one bar below the table, with no toolbar or pager", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  await expect(bar(page)).toBeVisible();
  await expect(el(page).locator(".gt-i-toolbar, .gt-i-pager")).toHaveCount(0);
  expect((await box(bar(page))).top).toBeGreaterThanOrEqual((await box(el(page).locator("table"))).bottom);
  // In one row, with the page controls at the end
  const toggle = await box(barButton(page, "Search the table"));
  const next = await box(barButton(page, "Next page"));
  expect(Math.abs(toggle.top - next.top)).toBeLessThan(1);
  expect(next.right).toBeCloseTo((await box(bar(page))).right, 0);
  await expect(readout(page)).toHaveText("1/12");
  await expect(readout(page)).toHaveAccessibleName("Page 1 of 12");
  expect(errors).toEqual([]);
});

test("searches from a button that opens a field, which Escape clears and then closes", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  await expect(field(page)).toBeHidden();
  await barButton(page, "Search the table").click();
  await expect(field(page)).toBeVisible();
  await expect(search(page)).toBeFocused();
  await expect(barButton(page, "Search the table")).toBeHidden();

  await page.keyboard.type("apricot");
  await expect(bar(page).locator(".gt-i-search-count")).toHaveText("3 rows");
  await expect(readout(page)).toHaveText("1/2");
  expect(dataRows(await visible(page))).toEqual([0, 8]);

  await page.keyboard.press("Escape");
  await expect(search(page)).toHaveValue("");
  await expect(field(page)).toBeVisible();
  await expect(readout(page)).toHaveText("1/12");
  await page.keyboard.press("Escape");
  await expect(field(page)).toBeHidden();
  await expect(barButton(page, "Search the table")).toBeFocused();
  expect(errors).toEqual([]);
});

test("opens the search on `/` from within the table, and closes an empty one on leaving it", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  await el(page).locator("button.gt-i-sort").first().focus();
  await page.keyboard.press("/");
  await expect(search(page)).toBeFocused();
  await expect(search(page)).toHaveValue("");

  await page.keyboard.press("Shift+Tab");
  await expect(field(page)).toBeHidden();

  // A search in force stays shown
  await barButton(page, "Search the table").click();
  await page.keyboard.type("fig");
  await page.keyboard.press("Enter");
  await el(page).locator("button.gt-i-sort").first().focus();
  await expect(field(page)).toBeVisible();
  expect(errors).toEqual([]);
});

test("pages with its arrows, and with the keys in the bar", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  await expect(barButton(page, "Previous page")).toHaveAttribute("aria-disabled", "true");
  await barButton(page, "Next page").click();
  expect(await pageOf(page)).toBe(2);
  await expect(readout(page)).toHaveText("2/12");

  await page.keyboard.press("ArrowRight");
  await page.keyboard.press("PageDown");
  expect(await pageOf(page)).toBe(4);
  await page.keyboard.press("ArrowLeft");
  expect(await pageOf(page)).toBe(3);
  await page.keyboard.press("End");
  await expect(readout(page)).toHaveText("12/12");
  await expect(barButton(page, "Next page")).toHaveAttribute("aria-disabled", "true");
  await page.keyboard.press("Home");
  expect(await pageOf(page)).toBe(1);
  expect(errors).toEqual([]);
});

test("goes to the page typed in its readout", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  await readout(page).click();
  const input = bar(page).locator(".gt-i-readout-jump input");
  await expect(input).toBeFocused();
  await expect(input).toHaveValue("1");
  await page.keyboard.type("9");
  await page.keyboard.press("Enter");
  expect(await pageOf(page)).toBe(9);
  await expect(readout(page)).toBeFocused();
  await expect(readout(page)).toHaveText("9/12");

  await readout(page).click();
  await page.keyboard.type("4");
  await page.keyboard.press("Escape");
  expect(await pageOf(page)).toBe(9);
  expect(errors).toEqual([]);
});

test("keeps its page controls in place as the page and readout change", async ({ page }) => {
  await ready(page, "bar.html");
  // (Across: the table's height changes with the structural rows on a page)
  const at = async () =>
    Promise.all(
      ["Previous page", "Next page"].map(async (name) => {
        const { left, right } = await box(barButton(page, name));
        return { left, right };
      }),
    );
  const first = await at();
  await page.evaluate(() => ((document.querySelector("gt-table") as any).page = 12));
  await expect(readout(page)).toHaveText("12/12");
  expect(await at()).toEqual(first);
  await readout(page).click();
  expect(await at()).toEqual(first);
});

test("is at least 300px wide, centred under a narrower table", async ({ page }) => {
  const errors = await ready(page, "bar-narrow.html");
  const table = await box(el(page).locator("table"));
  const shown = await box(bar(page));
  expect(table.width).toBeLessThan(300);
  expect(shown.width).toBeCloseTo(300, 0);
  expect((shown.left + shown.right) / 2).toBeCloseTo((table.left + table.right) / 2, 0);
  await expect(readout(page)).toHaveText("1/12");
  expect(errors).toEqual([]);
});

test("gives a narrow bar's room to the open search", async ({ page }) => {
  const errors = await ready(page, "bar-container.html");
  expect((await box(bar(page))).width).toBeCloseTo(300, 0);
  await expect(pages(page)).toBeVisible();
  await barButton(page, "Search the table").click();
  await expect(pages(page)).toBeHidden();
  expect((await box(field(page))).width).toBeGreaterThan(250);
  await page.keyboard.press("Escape");
  await expect(pages(page)).toBeVisible();
  expect(errors).toEqual([]);
});

test("sticks to the bottom of the view for a table of every row", async ({ page }) => {
  await page.setViewportSize({ width: 1000, height: 400 });
  const errors = await ready(page, "bar-sticky.html");
  await expect(pages(page)).toBeHidden();
  await expect(bar(page)).toHaveAttribute("data-gti-stick", "");
  const shown = await box(bar(page));
  expect(shown.bottom).toBeLessThanOrEqual(400);
  expect((await box(el(page).locator("table"))).bottom).toBeGreaterThan(400);
  // Over the rows, with a fill
  expect(await bar(page).evaluate((node) => getComputedStyle(node).backgroundColor)).not.toBe("rgba(0, 0, 0, 0)");

  // And, scrolled past the table, below it
  await page.mouse.wheel(0, 3000);
  await expect
    .poll(async () => (await box(bar(page))).top - (await box(el(page).locator("table"))).bottom)
    .toBeGreaterThanOrEqual(-1);
  expect(errors).toEqual([]);
});

test("keeps its room before hydration, so that what's below doesn't move", async ({ page }) => {
  const errors = await open(page, "bar-late.html");
  const gap = () =>
    page.evaluate(() => {
      const table = (document.querySelector("gt-table table") as HTMLElement).getBoundingClientRect();
      return (document.getElementById("after") as HTMLElement).getBoundingClientRect().top - table.bottom;
    });
  const before = await gap();
  await page.addScriptTag({ path: RUNTIME });
  await expect(el(page)).toHaveAttribute("data-gti-state", "ready");
  await expect(bar(page)).toBeVisible();
  expect(Math.abs((await gap()) - before)).toBeLessThan(1);
  expect(errors).toEqual([]);
});
