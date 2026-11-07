import { expect, type Page, test } from "@playwright/test";
import { dataRows, longPress, ready, visible } from "./helpers";

// Run on the phones and the tablet of playwright.config.ts (emulated, in Chromium): the pages as
// narrow as a phone's fit it, the bar folds into the "Filter & sort" sheet's button on a phone
// but not on a tablet, every target in the bar is big enough to touch, and the sheet works by
// touch alone.

const el = (page: Page) => page.locator("gt-table");
const bar = (page: Page) => el(page).locator(".gt-i-bar");
const opener = (page: Page) => bar(page).getByRole("button", { name: "Filter & sort" });
const sheet = (page: Page) => page.getByRole("dialog");
const label = (page: Page, column: string) => el(page).locator(`thead th#fs-${column} button.gt-i-sort`);

const phone = (page: Page) => (page.viewportSize()?.width ?? 0) < 600;

const fits = (page: Page) =>
  page.evaluate(() => document.documentElement.scrollWidth <= document.documentElement.clientWidth);

test("the bar folds on a phone, not on a tablet, and its targets are big enough", async ({ page }) => {
  const errors = await ready(page, "sheet-phone.html");
  expect(await fits(page)).toBe(true);
  if (phone(page)) {
    await expect(opener(page)).toBeVisible();
    await expect(bar(page).locator('[data-gti-bar="columns"]')).toBeHidden();
  } else {
    await expect(opener(page)).toBeHidden();
    await expect(bar(page).getByRole("button", { name: "Search the table" })).toBeVisible();
    await expect(bar(page).locator('[data-gti-bar="columns"]')).toBeVisible();
  }
  for (const button of await bar(page).locator("button:visible").all()) {
    const box = await button.boundingBox();
    expect(Math.min(box?.width ?? 0, box?.height ?? 0)).toBeGreaterThan(43.9);
  }
  // (On one line, as the room kept for it before hydration is)
  expect((await bar(page).boundingBox())?.height).toBeLessThan(45);
  expect(errors).toEqual([]);
});

test("the sheet fits the window, and filters by touch", async ({ page }) => {
  test.skip(!phone(page), "The bar only folds on a phone");
  const errors = await ready(page, "sheet-phone.html");
  await opener(page).tap();
  await expect(sheet(page)).toBeVisible();
  const box = await sheet(page).boundingBox();
  const { width, height } = await page.evaluate(() => ({ width: innerWidth, height: innerHeight }));
  expect(box?.width ?? Infinity).toBeLessThanOrEqual(width);
  expect(Math.abs((box?.y ?? 0) + (box?.height ?? 0) - height)).toBeLessThan(1);
  expect(box?.height ?? Infinity).toBeLessThanOrEqual(height * 0.85 + 1);

  await sheet(page).getByRole("button", { name: "fctr: any" }).tap();
  const panel = sheet(page).getByRole("group", { name: "Filter fctr" });
  await panel.getByRole("checkbox", { name: /^one/ }).tap();
  await expect.poll(async () => dataRows(await visible(page))).toEqual([0, 8, 16]);
  // (Its last controls can be scrolled to, and reached)
  const last = sheet(page).getByRole("group", { name: "Columns" }).getByRole("checkbox", { name: "fctr" });
  await last.scrollIntoViewIfNeeded();
  await last.tap();
  await expect(el(page).locator("thead th#fs-fctr")).toBeHidden();
  await sheet(page).getByRole("button", { name: "Done" }).tap();
  await expect(sheet(page)).toBeHidden();
  await expect(opener(page)).toBeFocused();
  expect(errors).toEqual([]);
});

test("a long press on a column's label opens its sheet; a tap sorts", async ({ page }) => {
  const errors = await ready(page, "sheet-phone.html");
  await longPress(page, label(page, "char"));
  await expect(sheet(page)).toBeVisible();
  await expect(sheet(page)).toHaveAccessibleName("char");
  await sheet(page).getByRole("button", { name: "Descending" }).tap();
  await expect(el(page).locator("thead th#fs-char")).toHaveAttribute("aria-sort", "descending");
  await sheet(page).getByRole("button", { name: "Done" }).tap();
  await expect(sheet(page)).toBeHidden();

  await label(page, "num").tap();
  await expect(el(page).locator("thead th#fs-num")).toHaveAttribute("aria-sort", "ascending");
  await expect(sheet(page)).toBeHidden();
  expect(errors).toEqual([]);
});

test("a table that can be stacked is cards on a phone, and fits the page", async ({ page }) => {
  const errors = await ready(page, "stack-phone.html");
  if (phone(page)) {
    await expect(el(page)).toHaveAttribute("data-gti-stacked", "");
  } else {
    await expect(el(page)).not.toHaveAttribute("data-gti-stacked");
  }
  expect(await fits(page)).toBe(true);
  expect(errors).toEqual([]);
});

test("a table wider than a phone scrolls inside the page", async ({ page }) => {
  const errors = await ready(page, "wide-phone.html");
  expect(await fits(page)).toBe(true);
  const { width, right } = await el(page)
    .locator(".gt-i-scroller")
    .evaluate((node) => ({ width: innerWidth, right: node.getBoundingClientRect().right }));
  expect(right).toBeLessThanOrEqual(width + 0.5);
  expect(errors).toEqual([]);
});
