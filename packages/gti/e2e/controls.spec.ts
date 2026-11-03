import { expect, type Page, test } from "@playwright/test";
import { ready, shown, visible } from "./helpers";

// Column controls: a GTI table of exibble (rows 0-7, on one page) that can't be sorted by `num`
// (filtered by a range), whose search leaves out `char` (filtered by text), and that can't resize
// `currency`.

const label = (page: Page, column: string) => page.locator(`th#cc-${column}`);
const live = (page: Page) => page.locator("gt-table .gt-i-live");

/** The text of each search highlight on the page. */
function highlights(page: Page): Promise<string[]> {
  return page.evaluate(() =>
    Array.from(CSS.highlights.get("gt-i-search") ?? [], (range) => (range as Range).toString()),
  );
}

test("has no sort button for an unsortable column, which can still be filtered and sorted by code", async ({
  page,
}) => {
  const errors = await ready(page, "controls.html");
  const all = await shown(page);

  await expect(label(page, "num").locator("button.gt-i-sort")).toHaveCount(0);
  await expect(label(page, "char").locator("button.gt-i-sort")).toHaveCount(1);
  await expect(label(page, "num").locator("button.gt-i-filter-button")).toHaveCount(1);
  // Clicking the label does nothing
  await label(page, "num").click();
  expect(await shown(page)).toEqual(all);

  await page.locator("gt-table").evaluate((node) => {
    (node as any).sort = [{ column: "num", descending: true }];
  });
  // (Missing values last)
  expect(await shown(page)).toEqual([7, 6, 4, 3, 2, 1, 0, 5]);
  await expect(label(page, "num")).not.toHaveAttribute("aria-sort");
  expect(errors).toEqual([]);
});

test("leaves an unsearchable column out of the search and its highlights, but not its filter", async ({
  page,
}) => {
  const errors = await ready(page, "controls.html");

  await page.locator("gt-table .gt-i-bar").getByRole("button", { name: "Search the table" }).click();
  // (Only `char` has "an": "banana" and "durian")
  await page.locator("gt-table input.gt-i-search").fill("an");
  await expect(live(page)).toHaveText("No matching rows");
  expect(await highlights(page)).toEqual([]);

  await page.locator("gt-table input.gt-i-search").fill("two");
  await expect(live(page)).toHaveText("Showing 1 of 8 rows");
  expect(await visible(page)).toEqual([1]);
  expect(await highlights(page)).toEqual(["two"]);

  await page.locator("gt-table input.gt-i-search").fill("");
  await expect(live(page)).toHaveText("Showing all 8 rows");
  await page.locator("gt-table").evaluate((node) => {
    (node as any).filter = { and: [{ col: "char", op: "contains", value: "an" }] };
  });
  expect(await visible(page)).toEqual([1, 3]);
  expect(await highlights(page)).toEqual(["an", "an", "an"]);
  expect(errors).toEqual([]);
});

test("has no resize handle for an unresizable column", async ({ page }) => {
  const errors = await ready(page, "controls.html");
  await expect(label(page, "currency").locator(".gt-i-resizer")).toHaveCount(0);
  await expect(page.locator("gt-table .gt-i-resizer")).toHaveCount(4);
  await expect(label(page, "num").locator(".gt-i-resizer")).toHaveCount(1);
  expect(errors).toEqual([]);
});
