import { expect, type Locator, type Page, test } from "@playwright/test";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { dataRows, open, ready, visible } from "./helpers";

// Filter tokens, in the control bar of a GTI table (the filters' table, 24 rows) whose view is
// filtered by every column, as text: `num >= 1000 and char contains "a" and fctr in (...)`, which
// keeps 3 rows; the same in a container 300px wide; and without the runtime, added by the test.

const RUNTIME = join(dirname(fileURLToPath(import.meta.url)), "..", "..", "..", "great_tables", "js", "gti.js");

const el = (page: Page) => page.locator("gt-table");
const tokens = (page: Page) => el(page).getByRole("list", { name: "Filters" });
const token = (page: Page, text: string | RegExp) => tokens(page).getByRole("button", { name: text });
const remove = (page: Page, column: string) =>
  tokens(page).getByRole("button", { name: `Remove the filter on ${column}`, exact: true });
const clearAll = (page: Page) => tokens(page).getByRole("button", { name: "Clear all the filters" });
const panel = (page: Page, column: string) => el(page).getByRole("group", { name: `Filter ${column}`, exact: true });
const infoButton = (page: Page) => el(page).getByRole("button", { name: "Table info", exact: true });
const texts = (page: Page) => tokens(page).locator(".gt-i-token-open");
const matched = (page: Page) => el(page).evaluate((node) => (node as any).matchCount as number);
// (From the table to the text after it)
const gap = (page: Page) =>
  page.evaluate(() => {
    const table = (document.querySelector("gt-table table") as HTMLElement).getBoundingClientRect();
    return (document.getElementById("after") as HTMLElement).getBoundingClientRect().top - table.bottom;
  });
const box = (locator: Locator) =>
  locator.evaluate((node) => {
    const { left, right, top, bottom, width } = node.getBoundingClientRect();
    return { left, right, top, bottom, width };
  });

test("shows the view's filters as tokens, on the bar's first line", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await expect(texts(page)).toHaveText(["num ≥ 1,000", "char contains “a”", "fctr: eight, one +2"]);
  await expect(clearAll(page)).toBeVisible();
  expect(await matched(page)).toBe(3);
  expect(dataRows(await visible(page))).toHaveLength(3);

  // (Above the search and the pages, inside the bar)
  const row = await box(tokens(page));
  const bar = await box(el(page).locator(".gt-i-bar"));
  expect(row.bottom).toBeLessThanOrEqual((await box(el(page).locator(".gt-i-bar-search"))).top);
  expect(row.top).toBeGreaterThanOrEqual(bar.top);
  expect(row.top).toBeGreaterThanOrEqual((await box(el(page).locator("table"))).bottom);
  expect(errors).toEqual([]);
});

test("opens a filter's panel from its token, above it, with focus back on Escape", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await token(page, "char contains “a”").click();
  await expect(panel(page, "char")).toBeVisible();
  await expect(token(page, "char contains “a”")).toHaveAttribute("aria-expanded", "true");
  await expect(panel(page, "char").getByRole("textbox")).toBeFocused();
  const shown = await box(panel(page, "char"));
  const pill = await box(token(page, "char contains “a”"));
  expect(shown.bottom).toBeLessThanOrEqual(pill.top);
  expect(pill.top - shown.bottom).toBeLessThan(8);

  // (The token follows the panel)
  await panel(page, "char").getByRole("textbox").fill("ap");
  await expect(token(page, /^char contains/)).toHaveText("char contains “ap”");
  await page.keyboard.press("Escape");
  await expect(panel(page, "char")).toBeHidden();
  await expect(token(page, "char contains “ap”")).toBeFocused();
  await expect(token(page, "char contains “ap”")).toHaveAttribute("aria-expanded", "false");

  // A second click closes it
  await token(page, "num ≥ 1,000").click();
  await expect(panel(page, "num")).toBeVisible();
  await token(page, "num ≥ 1,000").click();
  await expect(panel(page, "num")).toBeHidden();
  expect(errors).toEqual([]);
});

test("removes a filter with its ×, with focus on the next token", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await remove(page, "char").click();
  await expect(texts(page)).toHaveText(["num ≥ 1,000", "fctr: eight, one +2"]);
  await expect(token(page, "fctr: eight, one +2")).toBeFocused();
  expect(await matched(page)).toBe(6);
  expect(await el(page).evaluate((node) => (node as any).filter)).toEqual({
    and: [
      { col: "num", op: "gte", value: 1000 },
      { col: "fctr", op: "in", value: ["eight", "one", "seven", "two"] },
    ],
  });

  // The last one's, with focus on the one before it; then no Clear all, for one token
  await remove(page, "fctr").click();
  await expect(texts(page)).toHaveText(["num ≥ 1,000"]);
  await expect(token(page, "num ≥ 1,000")).toBeFocused();
  await expect(clearAll(page)).toBeHidden();
  // And the only one's, with focus on the info button
  await remove(page, "num").click();
  await expect(tokens(page)).toBeHidden();
  await expect(infoButton(page)).toBeFocused();
  expect(await matched(page)).toBe(24);
  expect(errors).toEqual([]);
});

test("goes between tokens with the arrow keys, and removes one with Delete or Backspace", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await token(page, "num ≥ 1,000").focus();
  await page.keyboard.press("ArrowRight");
  await expect(token(page, "char contains “a”")).toBeFocused();
  // (From a token's ×, too)
  await remove(page, "char").focus();
  await page.keyboard.press("ArrowRight");
  await expect(token(page, "fctr: eight, one +2")).toBeFocused();
  await page.keyboard.press("End");
  await expect(clearAll(page)).toBeFocused();
  await page.keyboard.press("Home");
  await expect(token(page, "num ≥ 1,000")).toBeFocused();
  await page.keyboard.press("ArrowLeft");
  await expect(token(page, "num ≥ 1,000")).toBeFocused();

  await page.keyboard.press("Delete");
  await expect(texts(page)).toHaveText(["char contains “a”", "fctr: eight, one +2"]);
  await expect(token(page, "char contains “a”")).toBeFocused();
  await page.keyboard.press("Backspace");
  await expect(texts(page)).toHaveText(["fctr: eight, one +2"]);
  await expect(token(page, "fctr: eight, one +2")).toBeFocused();
  expect(errors).toEqual([]);
});

test("clears every filter with Clear all", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await token(page, "fctr: eight, one +2").click();
  await expect(panel(page, "fctr")).toBeVisible();
  await clearAll(page).click();
  await expect(panel(page, "fctr")).toBeHidden();
  await expect(tokens(page)).toBeHidden();
  await expect(infoButton(page)).toBeFocused();
  expect(await matched(page)).toBe(24);
  expect(await el(page).evaluate((node) => (node as any).filter)).toBeNull();
  expect(errors).toEqual([]);
});

test("follows filters set from their columns, or by the page", async ({ page }) => {
  const errors = await ready(page, "tokens.html");
  await el(page).evaluate((node) => {
    (node as any).filter = { and: [{ col: "num", op: "lte", value: 33.33 }] };
  });
  await expect(texts(page)).toHaveText(["num ≤ 33.33"]);
  await el(page).getByRole("button", { name: /^Filter fctr/ }).click();
  await panel(page, "fctr").getByRole("checkbox", { name: /^two\b/ }).check();
  await expect(texts(page)).toHaveText(["num ≤ 33.33", "fctr: two"]);
  expect(errors).toEqual([]);
});

test("scrolls sideways when they don't fit, keeping the focused token in view", async ({ page }) => {
  const errors = await ready(page, "tokens-container.html");
  const container = await box(page.locator("body > div"));
  const row = await box(tokens(page));
  expect(row.left).toBeGreaterThanOrEqual(container.left - 0.5);
  expect(row.right).toBeLessThanOrEqual(container.right + 0.5);
  expect(await tokens(page).evaluate((node) => node.scrollWidth > node.clientWidth)).toBe(true);
  // (One line, still)
  await expect(tokens(page).locator("li").first()).toHaveCSS("flex-shrink", "0");

  await token(page, "num ≥ 1,000").focus();
  await page.keyboard.press("End");
  await expect(clearAll(page)).toBeFocused();
  const last = await box(clearAll(page));
  expect(last.right).toBeLessThanOrEqual(row.right + 0.5);
  expect(last.left).toBeGreaterThanOrEqual(row.left - 0.5);
  expect(await tokens(page).evaluate((node) => node.scrollLeft)).toBeGreaterThan(0);
  expect(errors).toEqual([]);
});

test("keeps their room before hydration, so that what's below doesn't move", async ({ page }) => {
  const errors = await open(page, "tokens-late.html");
  const before = await gap(page);
  await page.addScriptTag({ path: RUNTIME });
  await expect(el(page)).toHaveAttribute("data-gti-state", "ready");
  await expect(tokens(page)).toBeVisible();
  expect(Math.abs((await gap(page)) - before)).toBeLessThan(1);
  expect(errors).toEqual([]);
});

test.describe("on a touch screen", () => {
  test.use({ hasTouch: true, isMobile: true });

  test("has tokens big enough to tap", async ({ page }) => {
    const errors = await ready(page, "tokens.html");
    for (const control of [token(page, "num ≥ 1,000"), remove(page, "num"), clearAll(page)]) {
      const { width } = await box(control);
      expect(width).toBeGreaterThanOrEqual(44);
      expect(await control.evaluate((node) => node.getBoundingClientRect().height)).toBeGreaterThanOrEqual(44);
    }
    expect(errors).toEqual([]);
  });

  test("keeps their room before hydration", async ({ page }) => {
    const errors = await open(page, "tokens-late.html");
    const before = await gap(page);
    await page.addScriptTag({ path: RUNTIME });
    await expect(el(page)).toHaveAttribute("data-gti-state", "ready");
    expect(Math.abs((await gap(page)) - before)).toBeLessThan(1);
    expect(errors).toEqual([]);
  });
});
