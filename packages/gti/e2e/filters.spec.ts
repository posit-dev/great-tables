import { expect, type Locator, type Page, test } from "@playwright/test";
import { dataRows, ready, tab, visible } from "./helpers";

// Column filters on a GTI table: exibble three times over (24 rows, in two groups), 5 rows to a
// page, `num` filtered by a range, `char` by text and `fctr` by a facet; and the same in a
// container 300px wide.

const el = (page: Page) => page.locator("gt-table");
const filterButton = (page: Page, column: string) =>
  el(page).getByRole("button", { name: new RegExp(`^Filter ${column}( \\(on\\))?$`) });
const panel = (page: Page, column: string) => el(page).getByRole("group", { name: `Filter ${column}`, exact: true });
const infoRows = (page: Page) => el(page).locator(".gt-i-info-rows");
const box = (locator: Locator) =>
  locator.evaluate((node) => {
    const { left, right, top, bottom, height, width } = node.getBoundingClientRect();
    return { left, right, top, bottom, height, width };
  });
const matched = (page: Page) => el(page).evaluate((node) => (node as any).matchCount as number);

test("opens below its button, over the table, filled", async ({ page }) => {
  const errors = await ready(page, "filters.html");
  await expect(panel(page, "fctr")).toHaveCount(0);
  await filterButton(page, "fctr").click();
  await expect(panel(page, "fctr")).toBeVisible();
  await expect(filterButton(page, "fctr")).toHaveAttribute("aria-expanded", "true");

  const shown = await box(panel(page, "fctr"));
  const button = await box(filterButton(page, "fctr"));
  const host = await box(el(page));
  expect(shown.top).toBeGreaterThanOrEqual(button.bottom);
  expect(shown.top - button.bottom).toBeLessThan(8);
  expect(shown.left).toBeGreaterThanOrEqual(host.left - 0.5);
  expect(shown.right).toBeLessThanOrEqual(host.right + 0.5);
  // (Over the table's rows, which don't show through)
  expect(await panel(page, "fctr").evaluate((node) => getComputedStyle(node).backgroundColor)).not.toBe(
    "rgba(0, 0, 0, 0)",
  );
  const top = await panel(page, "fctr").evaluate((node) => {
    const { left, right, bottom } = node.getBoundingClientRect();
    return document.elementFromPoint((left + right) / 2, bottom - 4)?.closest(".gt-i-filter") === node;
  });
  expect(top).toBe(true);

  await filterButton(page, "fctr").click();
  await expect(panel(page, "fctr")).toBeHidden();
  expect(errors).toEqual([]);
});

test("filters by a facet's values, counting the rows with each", async ({ page }) => {
  const errors = await ready(page, "filters.html");
  await filterButton(page, "fctr").click();
  const options = panel(page, "fctr").locator(".gt-i-filter-option");
  await expect(options).toHaveCount(8);
  await expect(options.locator(".gt-i-filter-count")).toHaveText(Array(8).fill("3"));

  await panel(page, "fctr").getByRole("checkbox", { name: /^one\b/ }).check();
  await panel(page, "fctr").getByRole("checkbox", { name: /^two\b/ }).check();
  expect(await matched(page)).toBe(6);
  expect(dataRows(await visible(page))).toHaveLength(5);
  await expect(el(page).locator(".gt-i-live")).toHaveText("Showing 6 of 24 rows");
  await expect(filterButton(page, "fctr")).toHaveAccessibleName("Filter fctr (on)");
  expect(await el(page).evaluate((node) => (node as any).filter)).toEqual({
    and: [{ col: "fctr", op: "in", value: ["one", "two"] }],
  });
  expect(errors).toEqual([]);
});

test("filters by a range, and its counts follow in another column's facet", async ({ page }) => {
  const errors = await ready(page, "filters.html");
  await filterButton(page, "num").click();
  const least = panel(page, "num").getByRole("textbox", { name: "num, at least" });
  await expect(least).toBeFocused();
  await least.fill("1000");
  await least.press("Enter");
  expect(await matched(page)).toBe(9);
  await expect(panel(page, "num")).toBeVisible();

  // A bound that isn't a number is marked, and left out
  const most = panel(page, "num").getByRole("textbox", { name: "num, at most" });
  await most.fill("lots");
  await most.press("Enter");
  await expect(most).toHaveAttribute("aria-invalid", "true");
  expect(await matched(page)).toBe(9);

  await filterButton(page, "fctr").click();
  await expect(panel(page, "num")).toBeHidden();
  const counts = await panel(page, "fctr")
    .locator(".gt-i-filter-option")
    .evaluateAll((items) =>
      items.map((item) => {
        const value = item.querySelector(".gt-i-filter-value")?.textContent;
        return `${value} ${item.querySelector(".gt-i-filter-count")?.textContent}`;
      }),
    );
  expect(counts).toEqual(["eight 3", "five 3", "four 0", "one 0", "seven 3", "six 0", "three 0", "two 0"]);
  expect(errors).toEqual([]);
});

test("filters by text once typing pauses, marking it in its column", async ({ page }) => {
  const errors = await ready(page, "filters.html");
  await filterButton(page, "char").click();
  await panel(page, "char").getByRole("textbox", { name: "char contains" }).pressSequentially("an");
  await expect.poll(() => matched(page)).toBe(6);
  const marked = await page.evaluate(() =>
    Array.from(CSS.highlights.get("gt-i-search") ?? [], (range) => (range as Range).toString()),
  );
  expect(marked.length).toBeGreaterThan(0);
  expect(new Set(marked)).toEqual(new Set(["an"]));
  expect(errors).toEqual([]);
});

test("is opened from the keyboard, and closes on Escape or Tab, with focus back on its button", async ({ page }) => {
  const errors = await ready(page, "filters.html");
  await filterButton(page, "char").focus();
  await page.keyboard.press("Enter");
  await expect(panel(page, "char")).toBeVisible();
  await expect(panel(page, "char").getByRole("textbox")).toBeFocused();
  await page.keyboard.press("Escape");
  await expect(panel(page, "char")).toBeHidden();
  await expect(filterButton(page, "char")).toBeFocused();

  // Tab out of its end
  await page.keyboard.press("Enter");
  await tab(page);
  await expect(panel(page, "char")).toBeHidden();
  await expect(filterButton(page, "char")).toBeFocused();
  // Shift + Tab out of its start (its Clear button)
  await page.keyboard.press("Enter");
  await tab(page, true);
  await expect(panel(page, "char").getByRole("button", { name: "Clear the filter on char" })).toBeFocused();
  await tab(page, true);
  await expect(panel(page, "char")).toBeHidden();
  await expect(filterButton(page, "char")).toBeFocused();
  expect(errors).toEqual([]);
});

test("closes on a click outside it, but not in it", async ({ page }) => {
  const errors = await ready(page, "filters.html");
  await filterButton(page, "fctr").click();
  await panel(page, "fctr").locator(".gt-i-filter-title").click();
  await expect(panel(page, "fctr")).toBeVisible();
  await page.mouse.click(2, 2);
  await expect(panel(page, "fctr")).toBeHidden();
  await expect(filterButton(page, "fctr")).toHaveAttribute("aria-expanded", "false");
  expect(errors).toEqual([]);
});

test("is cleared, with the other filters, from the info panel", async ({ page }) => {
  const errors = await ready(page, "filters.html");
  await el(page).evaluate((node) => {
    (node as any).filter = {
      and: [
        { col: "num", op: "gte", value: 1 },
        { col: "char", op: "contains", value: "a" },
      ],
    };
  });
  const info = el(page).getByRole("group", { name: "Table info" });
  await el(page).getByRole("button", { name: "Table info", exact: true }).click();
  await expect(info).toContainText("Filtered by num, char");
  await expect(infoRows(page)).toHaveText(/of \d+ rows \(filtered from 24\)$/);
  await info.getByRole("button", { name: "Clear the filters" }).click();
  await expect(info).toContainText("Not filtered");
  await expect(infoRows(page)).toHaveText("1–5 of 24 rows");
  await expect(info.getByRole("button", { name: "Clear the filters" })).toBeFocused();
  expect(errors).toEqual([]);
});

test("stays within a narrow container", async ({ page }) => {
  const errors = await ready(page, "filters-container.html");
  const container = await box(page.locator("body > div"));
  for (const column of ["num", "fctr"]) {
    await filterButton(page, column).click();
    const shown = await box(panel(page, column));
    expect(shown.left).toBeGreaterThanOrEqual(container.left - 0.5);
    expect(shown.right).toBeLessThanOrEqual(container.right + 0.5);
  }
  expect(errors).toEqual([]);
});

test.describe("on a touch screen", () => {
  test.use({ hasTouch: true, isMobile: true });

  test("has controls big enough to tap", async ({ page }) => {
    const errors = await ready(page, "filters.html");
    // (The button's target reaches past it)
    const target = await filterButton(page, "fctr").evaluate((node) => {
      const { width, height } = getComputedStyle(node, "::before");
      return [Number.parseFloat(width), Number.parseFloat(height)];
    });
    expect(Math.min(...target)).toBeGreaterThanOrEqual(44);

    await filterButton(page, "fctr").tap();
    await expect(panel(page, "fctr")).toBeVisible();
    for (const control of [
      panel(page, "fctr").getByRole("button", { name: "Clear the filter on fctr" }),
      panel(page, "fctr").locator(".gt-i-filter-option").first(),
    ]) {
      expect((await box(control)).height).toBeGreaterThanOrEqual(44);
    }
    await filterButton(page, "num").tap();
    expect((await box(panel(page, "num").getByRole("textbox").first())).height).toBeGreaterThanOrEqual(44);
    expect(errors).toEqual([]);
  });
});
