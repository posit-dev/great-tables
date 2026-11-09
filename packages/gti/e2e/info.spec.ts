import { expect, type Locator, type Page, test } from "@playwright/test";
import { dataRows, ready, tab, visible } from "./helpers";

// The info panel of a GTI table: exibble three times over (24 rows, in two groups), 2 rows to a
// page (or 5), whose rows can be selected; and the same in a container 300px wide.

const el = (page: Page) => page.locator("gt-table");
const bar = (page: Page) => el(page).locator(".gt-i-bar");
const toggle = (page: Page) => bar(page).getByRole("button", { name: "Table info", exact: true });
const panel = (page: Page) => bar(page).getByRole("group", { name: "Table info" });
const rows = (page: Page) => panel(page).locator(".gt-i-info-rows");
const readout = (page: Page) => bar(page).locator("button.gt-i-readout");
const box = (locator: Locator) =>
  locator.evaluate((node) => {
    const { left, right, top, bottom, height } = node.getBoundingClientRect();
    return { left, right, top, bottom, height };
  });

test("opens above the end of the bar, over the table, filled", async ({ page }) => {
  const errors = await ready(page, "info.html");
  await expect(panel(page)).toBeHidden();
  await toggle(page).click();
  await expect(panel(page)).toBeVisible();
  await expect(toggle(page)).toHaveAttribute("aria-expanded", "true");
  await expect(rows(page)).toHaveText("1–2 of 24 rows");

  const shown = await box(panel(page));
  const under = await box(bar(page));
  expect(shown.bottom).toBeLessThanOrEqual(under.top);
  expect(shown.right).toBeCloseTo(under.right, 0);
  expect(shown.left).toBeGreaterThanOrEqual(under.left);
  // (Over the table's rows, which don't show through)
  expect(await panel(page).evaluate((node) => getComputedStyle(node).backgroundColor)).not.toBe("rgba(0, 0, 0, 0)");
  const top = await panel(page).evaluate((node) => {
    const { left, right, bottom } = node.getBoundingClientRect();
    return document.elementFromPoint((left + right) / 2, bottom - 4)?.closest(".gt-i-info") !== null;
  });
  expect(top).toBe(true);

  await toggle(page).click();
  await expect(panel(page)).toBeHidden();
  expect(errors).toEqual([]);
});

test("opens below the bar when there's more room for it there", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  await toggle(page).click();
  const shown = await box(panel(page));
  const under = await box(bar(page));
  expect(shown.top).toBeGreaterThanOrEqual(under.bottom);
  expect(shown.bottom).toBeLessThanOrEqual(await page.evaluate(() => document.documentElement.clientHeight));
  expect(errors).toEqual([]);
});

test("is gone into with Tab, and closes on Escape, with focus back on its button", async ({ page }) => {
  const errors = await ready(page, "info.html");
  await toggle(page).focus();
  await page.keyboard.press("Enter");
  await expect(panel(page)).toBeVisible();
  await tab(page);
  await expect(panel(page).getByRole("combobox", { name: "Rows per page" })).toBeFocused();
  await page.keyboard.press("Escape");
  await expect(panel(page)).toBeHidden();
  await expect(toggle(page)).toBeFocused();

  // Focus going elsewhere closes it
  await page.keyboard.press("Enter");
  await tab(page, true);
  await expect(bar(page).getByRole("button", { name: "Next page" })).toBeFocused();
  await expect(panel(page)).toBeHidden();
  expect(errors).toEqual([]);
});

test("closes on a click outside it, but not in it", async ({ page }) => {
  const errors = await ready(page, "info.html");
  await toggle(page).click();
  await rows(page).click();
  await expect(panel(page)).toBeVisible();
  await page.mouse.click(2, 2);
  await expect(panel(page)).toBeHidden();
  await expect(toggle(page)).toHaveAttribute("aria-expanded", "false");
  expect(errors).toEqual([]);
});

test("changes the page size", async ({ page }) => {
  const errors = await ready(page, "info.html");
  await toggle(page).click();
  await panel(page).getByRole("combobox", { name: "Rows per page" }).selectOption("5");
  await expect(readout(page)).toHaveText("1/5");
  await expect(rows(page)).toHaveText("1–5 of 24 rows");
  expect(dataRows(await visible(page))).toHaveLength(5);
  await expect(panel(page)).toBeVisible();
  expect(errors).toEqual([]);
});

test("puts the table back in its own order", async ({ page }) => {
  const errors = await ready(page, "info.html");
  const before = await visible(page);
  await el(page).getByRole("button", { name: "Sort by num", exact: true }).click();
  expect(await visible(page)).not.toEqual(before);

  await toggle(page).click();
  await expect(panel(page)).toContainText("Sorted by num, ascending");
  await panel(page).getByRole("button", { name: "Reset the sort" }).click();
  expect(await visible(page)).toEqual(before);
  await expect(panel(page)).toContainText("Not sorted");
  await expect(panel(page).getByRole("button", { name: "Reset the sort" })).toBeFocused();
  expect(errors).toEqual([]);
});

test("clears the selection", async ({ page }) => {
  const errors = await ready(page, "info.html");
  const boxes = el(page).locator("tbody .gt-i-select input");
  await boxes.nth(0).check();
  await boxes.nth(1).check();
  await toggle(page).click();
  await expect(panel(page)).toContainText("2 rows selected");
  await panel(page).getByRole("button", { name: "Clear the selection" }).click();
  await expect(panel(page)).toContainText("No rows selected");
  await expect(el(page).locator("tbody .gt-i-select input:checked")).toHaveCount(0);
  expect(await el(page).evaluate((node) => (node as any).selection)).toEqual([]);
  expect(errors).toEqual([]);
});

test("stays within a narrow container", async ({ page }) => {
  const errors = await ready(page, "info-container.html");
  await toggle(page).click();
  const shown = await box(panel(page));
  const container = await box(page.locator("body > div"));
  expect(shown.left).toBeGreaterThanOrEqual(container.left - 0.5);
  expect(shown.right).toBeLessThanOrEqual(container.right + 0.5);
  // (Its text wraps, rather than overflowing it)
  expect(await panel(page).evaluate((node) => node.scrollWidth <= node.clientWidth)).toBe(true);
  expect(errors).toEqual([]);
});

test.describe("on a touch screen", () => {
  test.use({ hasTouch: true, isMobile: true });

  test("has controls big enough to tap", async ({ page }) => {
    const errors = await ready(page, "info.html");
    await toggle(page).tap();
    await expect(panel(page)).toBeVisible();
    for (const control of [
      panel(page).getByRole("combobox", { name: "Rows per page" }),
      panel(page).getByRole("button", { name: "Reset the sort" }),
      panel(page).getByRole("button", { name: "Clear the selection" }),
    ]) {
      expect((await box(control)).height).toBeGreaterThanOrEqual(44);
    }
    expect(errors).toEqual([]);
  });
});
