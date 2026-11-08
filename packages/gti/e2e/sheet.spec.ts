import { expect, type Page, test } from "@playwright/test";
import { CHROMIUM_TOUCH, dataRows, longPress, ready, visible } from "./helpers";

// The filters' table (exibble three times over: 24 rows, in two groups, 5 to a page; num filtered
// by a range, char by text and fctr by a facet), with a search and columns readers can hide, in a
// container 360px wide: on a touch screen, its bar folds into the "Filter & sort" sheet's button.

const el = (page: Page) => page.locator("gt-table");
const bar = (page: Page) => el(page).locator(".gt-i-bar");
const opener = (page: Page) => bar(page).getByRole("button", { name: "Filter & sort" });
const sheet = (page: Page) => page.getByRole("dialog");
const label = (page: Page, column: string) => el(page).locator(`thead th#fs-${column} button.gt-i-sort`);

const widen = (page: Page, width: string) =>
  page.locator("body > div").evaluate((div, width) => {
    (div as HTMLElement).style.width = width;
  }, width);

test.describe("on a touch screen", () => {
  // (Not `isMobile`, with which Safari lays the page out wider and zooms it out, away from the
  // points touched)
  test.use({ hasTouch: true, viewport: { width: 800, height: 700 } });

  test("a narrow bar folds the search and the columns into the sheet's button", async ({ page }) => {
    const errors = await ready(page, "sheet.html");
    await expect(opener(page)).toBeVisible();
    await expect(opener(page)).toHaveText("Filter & sort");
    await expect(bar(page).getByRole("button", { name: "Search the table" })).toBeHidden();
    await expect(bar(page).locator('[data-gti-bar="columns"]')).toBeHidden();
    await expect(bar(page).locator('[data-gti-bar="query"]')).toBeHidden();
    // (The page controls and the info stay, and every target is big enough)
    await expect(bar(page).getByRole("button", { name: "Next page" })).toBeVisible();
    await expect(bar(page).getByRole("button", { name: "Table info" })).toBeVisible();
    for (const button of await bar(page).locator("button:visible").all()) {
      const box = await button.boundingBox();
      expect(Math.min(box?.width ?? 0, box?.height ?? 0)).toBeGreaterThan(43.9);
    }
    expect(errors).toEqual([]);
  });

  test("a bar that's wide enough doesn't fold", async ({ page }) => {
    const errors = await ready(page, "sheet.html");
    await widen(page, "760px");
    await expect(opener(page)).toBeHidden();
    await expect(bar(page).getByRole("button", { name: "Search the table" })).toBeVisible();
    await expect(bar(page).locator('[data-gti-bar="columns"]')).toBeVisible();
    await widen(page, "360px");
    await expect(opener(page)).toBeVisible();
    expect(errors).toEqual([]);
  });

  test("the sheet comes up from the foot of the window, and searches", async ({ page }) => {
    const errors = await ready(page, "sheet.html");
    await opener(page).tap();
    await expect(sheet(page)).toBeVisible();
    await expect(sheet(page)).toHaveAccessibleName("Filter & sort");
    const box = await sheet(page).boundingBox();
    const height = await page.evaluate(() => innerHeight);
    expect(Math.abs((box?.y ?? 0) + (box?.height ?? 0) - height)).toBeLessThan(1);
    await expect(sheet(page).getByRole("group", { name: "Search" })).toBeVisible();
    await expect(sheet(page).getByRole("group", { name: "Columns" })).toBeVisible();

    await sheet(page).getByRole("searchbox").fill("five");
    await expect.poll(async () => dataRows(await visible(page))).toEqual([4, 12, 20]);
    await expect(sheet(page).locator(".gt-i-info-rows")).toHaveText("1–3 of 3 rows (filtered from 24)");
    // (The search shows in the bar once it closes)
    await sheet(page).getByRole("button", { name: "Done" }).tap();
    await expect(sheet(page)).toBeHidden();
    await expect(opener(page)).toBeFocused();
    await expect(bar(page).getByRole("searchbox")).toHaveValue("five");
    expect(errors).toEqual([]);
  });

  test("the sheet sorts, filters and hides columns", async ({ page }) => {
    const errors = await ready(page, "sheet.html");
    await opener(page).tap();
    const sort = sheet(page).getByRole("group", { name: "Sort" });
    await sort.getByRole("combobox", { name: "Sort by" }).selectOption("num");
    await sort.getByRole("button", { name: "Descending" }).tap();
    await expect(el(page).locator("thead th#fs-num")).toHaveAttribute("aria-sort", "descending");
    await expect(sort.getByRole("button", { name: "Descending" })).toHaveAttribute("aria-pressed", "true");

    // A filter's panel opens below its button
    const filters = sheet(page).getByRole("group", { name: "Filters" });
    const fctr = filters.getByRole("button", { name: "fctr: any" });
    await fctr.tap();
    const panel = sheet(page).getByRole("group", { name: "Filter fctr" });
    await expect(panel).toBeVisible();
    expect((await panel.boundingBox())?.y).toBeGreaterThan((await fctr.boundingBox())?.y ?? 0);
    await panel.getByRole("checkbox", { name: /^one/ }).tap();
    await expect(filters.getByRole("button", { name: "fctr: one" })).toBeVisible();
    await expect.poll(async () => dataRows(await visible(page))).toEqual([0, 8, 16]);

    await sheet(page).getByRole("group", { name: "Columns" }).getByRole("checkbox", { name: "char" }).tap();
    await expect(el(page).locator("thead th#fs-char")).toBeHidden();
    await page.keyboard.press("Escape");
    await expect(sheet(page)).toBeHidden();
    // (The filter's token in the bar)
    await expect(bar(page).getByRole("button", { name: "fctr: one" })).toBeVisible();
    expect(errors).toEqual([]);
  });

  test("the sheet closes on Escape, and on a tap outside it", async ({ page }) => {
    const errors = await ready(page, "sheet.html");
    await opener(page).tap();
    await page.keyboard.press("Escape");
    await expect(sheet(page)).toBeHidden();
    await expect(opener(page)).toBeFocused();
    await opener(page).tap();
    await page.touchscreen.tap(400, 20);
    await expect(sheet(page)).toBeHidden();
    // (While it's open, the page behind it can't be reached)
    await opener(page).tap();
    await expect(sheet(page)).toBeVisible();
    expect(await page.evaluate(() => document.elementFromPoint(400, 20)?.tagName)).toBe("DIALOG");
    expect(errors).toEqual([]);
  });

  test("a long press on a column's label opens its sheet, and doesn't sort", async ({ page, browserName }) => {
    test.skip(browserName !== "chromium", CHROMIUM_TOUCH);
    const errors = await ready(page, "sheet.html");
    await longPress(page, label(page, "fctr"));
    await expect(sheet(page)).toBeVisible();
    await expect(sheet(page)).toHaveAccessibleName("fctr");
    await expect(el(page).locator("thead th#fs-fctr")).not.toHaveAttribute("aria-sort");
    await sheet(page).getByRole("button", { name: "Ascending" }).tap();
    await expect(el(page).locator("thead th#fs-fctr")).toHaveAttribute("aria-sort", "ascending");
    await sheet(page).getByRole("button", { name: "Hide column" }).tap();
    await expect(sheet(page)).toBeHidden();
    await expect(el(page).locator("thead th#fs-fctr")).toBeHidden();

    // (And a tap still sorts)
    await label(page, "num").tap();
    await expect(el(page).locator("thead th#fs-num")).toHaveAttribute("aria-sort", "ascending");
    expect(errors).toEqual([]);
  });
});

test("with a mouse, the bar doesn't fold, and a long press is a click", async ({ page }) => {
  const errors = await ready(page, "sheet.html");
  await expect(opener(page)).toBeHidden();
  await expect(bar(page).getByRole("button", { name: "Search the table" })).toBeVisible();
  await expect(bar(page).locator('[data-gti-bar="columns"]')).toBeVisible();
  await label(page, "num").hover();
  await page.mouse.down();
  await page.waitForTimeout(700);
  await page.mouse.up();
  await expect(sheet(page)).toBeHidden();
  await expect(el(page).locator("thead th#fs-num")).toHaveAttribute("aria-sort", "ascending");
  expect(errors).toEqual([]);
});
