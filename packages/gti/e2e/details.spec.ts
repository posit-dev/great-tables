import { expect, type Locator, type Page, test } from "@playwright/test";
import { ready } from "./helpers";

// Rows' details: exibble (8 rows, grp_b then grp_a), with a stub, selectable rows and a search, 5 to
// a page, each row but row_3 with details: a table for row_1 and row_5 (with a fill and borders of
// its own), Markdown for row_2, and text with markup (shown as text) for the rest. In a container
// 800px wide; stacked in one 360px wide; and dropping columns in one 300px wide (where currency,
// then char, go first). All in a monospace font.

const el = (page: Page) => page.locator("gt-table");
const row = (page: Page, label: string) => el(page).locator("tbody tr", { has: page.locator(`th.gt_stub:text-is("${label}")`) }).first();
const button = (page: Page, label: string) => row(page, label).locator(".gt-i-expand");
const details = (page: Page, label: string) => row(page, label).locator("+ tr.gt-i-details");
// (Playwright's locators go into open shadow roots)
const content = (page: Page, label: string) => details(page, label).locator(".gt-i-details-content");
const bar = (page: Page) => el(page).locator(".gt-i-bar");
const info = (page: Page) => bar(page).getByRole("button", { name: "Table info", exact: true });
const expandAll = (page: Page) => bar(page).getByRole("button", { name: "Show every row's details" });
const collapseAll = (page: Page) => bar(page).getByRole("button", { name: "Hide every row's details" });
const set = (page: Page, name: string, value: unknown) =>
  el(page).evaluate((node, [name, value]) => ((node as any)[name as string] = value), [name, value]);
const selection = (page: Page) => el(page).evaluate((node) => (node as any).selection as number[]);

type Box = { top: number; bottom: number; left: number; right: number };
const rect = (locator: Locator): Promise<Box> =>
  locator.evaluate((node) => {
    const { top, bottom, left, right } = node.getBoundingClientRect();
    return { top, bottom, left, right };
  });
const style = (locator: Locator, ...names: string[]) =>
  locator.evaluate((node, names) => {
    const css = getComputedStyle(node);
    return names.map((name) => css.getPropertyValue(name));
  }, names);

test.describe("rows' details", () => {
  test("have a button on each row with them, and none on a row without", async ({ page }) => {
    const errors = await ready(page, "details.html");
    await expect(el(page).locator(":scope > template[data-gti-details]")).toHaveCount(7);
    await expect(el(page).locator("tr.gt-i-has-details")).toHaveCount(7);
    await expect(button(page, "row_5")).toHaveAttribute("aria-label", "Show more of row_5");
    await expect(button(page, "row_5")).toHaveAttribute("aria-expanded", "false");
    // (Before the stub's text, as a table that drops columns has it)
    await expect(row(page, "row_5").locator("th.gt_stub .gt-i-expand")).toBeVisible();
    await expect(el(page).locator("tr.gt-i-details")).toHaveCount(0);
    await set(page, "page", 2);
    await expect(button(page, "row_2")).toBeVisible();
    await expect(row(page, "row_3")).toBeVisible();
    await expect(button(page, "row_3")).toHaveCount(0);
    expect(errors).toEqual([]);
  });

  test("show under their row from its button, which keeps focus", async ({ page }) => {
    const errors = await ready(page, "details.html");
    const toggle = button(page, "row_5");
    await toggle.click();
    await expect(toggle).toHaveAttribute("aria-expanded", "true");
    await expect(toggle).toBeFocused();
    await expect(details(page, "row_5")).toBeVisible();
    await expect(content(page, "row_5").locator(".gt_title")).toHaveText("Inner row_5");
    // (Across the row, under it)
    const under = await rect(details(page, "row_5"));
    const above = await rect(row(page, "row_5"));
    expect(under.top).toBeCloseTo(above.bottom, 0);
    expect(under.left).toBeCloseTo(above.left, 0);
    expect(under.right).toBeCloseTo(above.right, 0);

    await toggle.click();
    await expect(toggle).toHaveAttribute("aria-expanded", "false");
    await expect(el(page).locator("tr.gt-i-details")).toHaveCount(0);
    await page.keyboard.press("Enter");
    await expect(details(page, "row_5")).toBeVisible();
    await expect(toggle).toBeFocused();
    expect(errors).toEqual([]);
  });

  test("show a table with its own styles and borders, apart from the page's", async ({ page }) => {
    const errors = await ready(page, "details.html");
    await button(page, "row_5").click();
    const host = content(page, "row_5");
    expect(await host.evaluate((node) => node.shadowRoot !== null && node.shadowRoot.querySelector("#inner_row_5 table.gt_table") !== null)).toBe(true);
    // Its own CSS (by its ID) styles it: its font, its title's size, and its top border
    const inner = host.locator("table.gt_table");
    const [font, top, topWidth, topColor] = await style(inner, "font-family", "border-top-style", "border-top-width", "border-top-color");
    expect(font).not.toContain("monospace");
    expect([top, topWidth, topColor]).toEqual(["solid", "2px", "rgb(168, 168, 168)"]);
    expect(parseFloat((await style(host.locator(".gt_title"), "font-size"))[0] as string)).toBeCloseTo(20, 0);
    // (Which the outer table's CSS, in the page, doesn't reach)
    expect((await style(row(page, "row_5").locator("td").last(), "font-family"))[0]).toContain("monospace");
    // Its styles: a fill on a, and red borders, 3px, around b's cells
    const [a, b] = [host.locator("td.gt_row").nth(0), host.locator("td.gt_row").nth(1)];
    expect(await style(a, "background-color")).toEqual(["rgb(255, 238, 170)"]);
    expect(await style(b, "border-top-width", "border-right-width", "border-bottom-width", "border-left-width")).toEqual(["3px", "3px", "3px", "3px"]);
    expect(await style(b, "border-top-color", "border-left-color")).toEqual(["rgb(255, 0, 0)", "rgb(255, 0, 0)"]);
    // (Inside the details' cell)
    const cell = await rect(details(page, "row_5").locator(":scope > td"));
    const table = await rect(inner);
    expect(table.left).toBeGreaterThanOrEqual(cell.left);
    expect(table.right).toBeLessThanOrEqual(cell.right);
    expect(errors).toEqual([]);
  });

  test("show Markdown, and text as text", async ({ page }) => {
    const errors = await ready(page, "details.html");
    await button(page, "row_6").click();
    await expect(content(page, "row_6")).toHaveText("<b>Plain</b> row_6");
    await expect(content(page, "row_6").locator("b")).toHaveCount(0);
    await set(page, "page", 2);
    await button(page, "row_2").click();
    await expect(content(page, "row_2").locator("strong")).toHaveText("Bold");
    expect(errors).toEqual([]);
  });

  test("follow their row when it's sorted, and are hidden with it", async ({ page }) => {
    const errors = await ready(page, "details.html");
    await button(page, "row_5").click();
    await set(page, "sort", [{ column: "num", descending: true }]);
    await expect(details(page, "row_5")).toBeVisible();
    await expect(content(page, "row_5").locator(".gt_title")).toHaveText("Inner row_5");
    await expect(el(page).locator("tr.gt-i-details")).toHaveCount(1);
    // (A search leaving the row out hides them, and one keeping it shows them again)
    await set(page, "search", "row_8");
    await expect(row(page, "row_5")).toBeHidden();
    await expect(el(page).locator("tr.gt-i-details")).toBeHidden();
    await set(page, "search", "");
    await expect(details(page, "row_5")).toBeVisible();
    // (As does a page without it)
    await set(page, "sort", []);
    await set(page, "page", 2);
    await expect(el(page).locator("tr.gt-i-details")).toBeHidden();
    await set(page, "page", 1);
    await expect(details(page, "row_5")).toBeVisible();
    await expect(button(page, "row_5")).toHaveAttribute("aria-expanded", "true");
    expect(errors).toEqual([]);
  });

  test("open and close together from the info panel", async ({ page }) => {
    const errors = await ready(page, "details.html");
    await info(page).click();
    await expect(expandAll(page)).toHaveText("Expand all");
    await expect(expandAll(page)).toHaveAttribute("aria-disabled", "false");
    await expect(collapseAll(page)).toHaveAttribute("aria-disabled", "true");

    await expandAll(page).click();
    await expect(expandAll(page)).toBeFocused();
    await expect(expandAll(page)).toHaveAttribute("aria-disabled", "true");
    await expect(collapseAll(page)).toHaveAttribute("aria-disabled", "false");
    // (Every row on the page has details; those on the next page show there)
    await expect(el(page).locator("tr.gt-i-details:visible")).toHaveCount(5);
    for (const label of ["row_5", "row_6", "row_7", "row_8", "row_1"]) {
      await expect(button(page, label)).toHaveAttribute("aria-expanded", "true");
    }
    await set(page, "page", 2);
    await expect(el(page).locator("tr.gt-i-details:visible")).toHaveCount(2);
    await expect(details(page, "row_4")).toBeVisible();

    // (The panel stays open)
    await collapseAll(page).click();
    await expect(el(page).locator("tr.gt-i-details")).toHaveCount(0);
    await expect(collapseAll(page)).toHaveAttribute("aria-disabled", "true");
    // (And a row opened from its button counts)
    await button(page, "row_2").click();
    await info(page).click();
    await expect(collapseAll(page)).toHaveAttribute("aria-disabled", "false");
    await expect(expandAll(page)).toHaveAttribute("aria-disabled", "false");
    expect(errors).toEqual([]);
  });

  test("don't open from a click on their row, which selects it", async ({ page }) => {
    const errors = await ready(page, "details.html");
    await row(page, "row_5").locator("td").last().click();
    expect(await selection(page)).toEqual([4]);
    await expect(button(page, "row_5")).toHaveAttribute("aria-expanded", "false");
    // (Nor does their button select it)
    await button(page, "row_6").click();
    expect(await selection(page)).toEqual([4]);
    expect(errors).toEqual([]);
  });
});

test.describe("rows' details on a touch screen", () => {
  test.use({ hasTouch: true, isMobile: true });

  test("open and close from a tap on their row, and its checkbox selects it", async ({ page }) => {
    const errors = await ready(page, "details.html");
    await row(page, "row_5").locator("td").last().tap();
    await expect(details(page, "row_5")).toBeVisible();
    expect(await selection(page)).toEqual([]);
    await row(page, "row_5").locator("td").last().tap();
    await expect(el(page).locator("tr.gt-i-details")).toHaveCount(0);
    await row(page, "row_5").locator("td.gt-i-select input").tap();
    expect(await selection(page)).toEqual([4]);
    await expect(button(page, "row_5")).toHaveAttribute("aria-expanded", "false");
    // (A tap in them doesn't close them)
    await button(page, "row_6").tap();
    await content(page, "row_6").tap();
    await expect(details(page, "row_6")).toBeVisible();
    expect(errors).toEqual([]);
  });
});

test("rows' details in a stacked table are part of their row's card", async ({ page }) => {
  const errors = await ready(page, "details-stack.html");
  await button(page, "row_5").click();
  await expect(content(page, "row_5").locator(".gt_title")).toHaveText("Inner row_5");
  const card = await rect(row(page, "row_5"));
  const under = await rect(details(page, "row_5"));
  expect(under.top).toBeCloseTo(card.bottom, 0);
  expect(under.left).toBeCloseTo(card.left, 0);
  expect(under.right).toBeCloseTo(card.right, 0);
  expect(await style(row(page, "row_5"), "border-bottom-left-radius", "margin-bottom")).toEqual(["0px", "0px"]);
  expect(await style(details(page, "row_5"), "border-top-left-radius", "margin-top")).toEqual(["0px", "0px"]);
  // (Without a label, as the cards' other lines have)
  expect(await style(details(page, "row_5").locator(":scope > td"), "display")).toEqual(["block"]);
  expect(await details(page, "row_5").locator(":scope > td").evaluate((td) => getComputedStyle(td, "::before").content)).toBe("none");
  // (The next card is apart from it)
  expect((await rect(row(page, "row_6"))).top).toBeGreaterThan(under.bottom + 4);
  expect(errors).toEqual([]);
});

test("rows' details in a table that drops columns follow the columns dropped", async ({ page }) => {
  const errors = await ready(page, "details-collapse.html");
  await expect(el(page)).toHaveAttribute("data-gti-dropped", "");
  await button(page, "row_5").click();
  const body = details(page, "row_5").locator(".gt-i-details-body");
  // The columns dropped, then the details
  await expect(body.locator(":scope > *")).toHaveCount(2);
  await expect(body.locator(":scope > dl.gt-i-details-list")).toBeVisible();
  await expect(body.locator(":scope > dl + .gt-i-details-content")).toBeVisible();
  await expect(body.locator("dt").first()).toHaveText("char");
  // (Row 3, without details, has a button for its dropped columns)
  await set(page, "page", 2);
  await expect(button(page, "row_3")).toBeVisible();
  await set(page, "page", 1);

  // With nothing dropped, row 5 stays open, with its details only, and row 3's button goes
  await el(page).evaluate((node) => ((node.parentElement as HTMLElement).style.width = "1000px"));
  await expect(el(page)).not.toHaveAttribute("data-gti-dropped");
  await expect(details(page, "row_5")).toBeVisible();
  await expect(details(page, "row_5").locator("dl")).toHaveCount(0);
  await expect(content(page, "row_5").locator(".gt_title")).toHaveText("Inner row_5");
  await expect(button(page, "row_5")).toBeVisible();
  await set(page, "page", 2);
  await expect(row(page, "row_3")).toBeVisible();
  await expect(button(page, "row_3")).toBeHidden();
  expect(errors).toEqual([]);
});
