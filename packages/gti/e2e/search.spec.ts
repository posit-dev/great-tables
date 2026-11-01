import { expect, type Page, test } from "@playwright/test";
import { groupCells, ready, shown, striping, visible } from "./helpers";

// exibble, shown as group grp_b (rows 4-7) then grp_a (rows 0-3), each with a summary row, then a
// grand summary row. Row 0's `char` ("apricot") has a footnote mark, and row 3's is "Crème
// brûlée".

const searchBox = (page: Page) => page.locator("gt-table input.gt-i-search");
const live = (page: Page) => page.locator("gt-table .gt-i-live");

/** The text of each search highlight on the page. */
function highlights(page: Page): Promise<string[]> {
  return page.evaluate(() =>
    Array.from(CSS.highlights.get("gt-i-search") ?? [], (range) => (range as Range).toString()),
  );
}

test("filters the rows, within their groups, as the reader types", async ({ page }) => {
  const errors = await ready(page, "search.html");
  const all = await shown(page);

  await searchBox(page).fill("ap");
  await expect(live(page)).toHaveText("Showing 2 of 8 rows");
  expect(await visible(page)).toEqual([
    "group:grp_b", 6, "summary:Total",
    "group:grp_a", 0, "summary:Total",
    "grand:Max",
  ]);
  // Hidden rows stay where they are
  expect(await shown(page)).toEqual(all);

  await searchBox(page).fill("fig");
  await expect(live(page)).toHaveText("Showing 1 of 8 rows");
  expect(await visible(page)).toEqual(["group:grp_b", 5, "summary:Total", "grand:Max"]);

  await searchBox(page).fill("");
  await expect(live(page)).toHaveText("Showing all 8 rows");
  expect(await visible(page)).toEqual(all);
  expect(errors).toEqual([]);
});

test("ignores case and accents, but not footnote marks", async ({ page }) => {
  const errors = await ready(page, "search.html");

  await searchBox(page).fill("CREME brulee");
  await expect(live(page)).toHaveText("Showing 1 of 8 rows");
  expect(await visible(page)).toEqual(["group:grp_a", 3, "summary:Total", "grand:Max"]);

  // "apricot" has a footnote mark "1", which isn't part of its value
  await searchBox(page).fill("apricot1");
  await expect(live(page)).toHaveText("No matching rows");
  expect(errors).toEqual([]);
});

test("highlights the matches", async ({ page }) => {
  const errors = await ready(page, "search.html");

  await searchBox(page).fill("ap");
  await expect(live(page)).toHaveText("Showing 2 of 8 rows");
  expect(await highlights(page)).toEqual(["ap", "ap"]);

  // Matches map back to the text as written
  await searchBox(page).fill("creme brulee");
  await expect(live(page)).toHaveText("Showing 1 of 8 rows");
  expect(await highlights(page)).toEqual(["Crème", "brûlée"]);

  // Still on the matches after sorting moves their rows
  await page.locator("th#q-char > button.gt-i-sort").click();
  expect(await highlights(page)).toEqual(["Crème", "brûlée"]);

  await searchBox(page).fill("");
  await expect(live(page)).toHaveText("Showing all 8 rows");
  expect(await highlights(page)).toEqual([]);
  expect(errors).toEqual([]);
});

test("says so when nothing matches", async ({ page }) => {
  const errors = await ready(page, "search.html");

  await searchBox(page).fill("zzz");
  await expect(live(page)).toHaveText("No matching rows");
  expect(await visible(page)).toEqual(["grand:Max"]);
  const empty = page.locator("gt-table tr.gt-i-empty td");
  await expect(empty).toHaveText("No matching rows");
  // Across the whole table, above the grand summary row
  const boxes = await page.locator("gt-table table").evaluate((table) => ({
    table: table.querySelector("tbody.gt_table_body")?.getBoundingClientRect().toJSON(),
    empty: table.querySelector("tr.gt-i-empty td")?.getBoundingClientRect().toJSON(),
    grand: table.querySelector(".gt_grand_summary_row")?.getBoundingClientRect().toJSON(),
  }));
  expect(boxes.empty.width).toBeCloseTo(boxes.table.width, 0);
  expect(boxes.empty.bottom).toBeLessThanOrEqual(boxes.grand.top + 1);

  await searchBox(page).fill("");
  await expect(empty).toHaveCount(0);
  expect(errors).toEqual([]);
});

test("restripes the rows it shows", async ({ page }) => {
  const errors = await ready(page, "search.html");
  const before = await striping(page);

  await searchBox(page).fill("$1");
  await expect(live(page)).toHaveText("Showing 4 of 8 rows");
  const after = await striping(page);
  expect(after.map((row) => row.striped)).toEqual([false, true, false, true]);
  expect(after.map((row) => row.background)).toEqual(
    before.slice(0, 4).map((row) => row.background),
  );
  expect(errors).toEqual([]);
});

test("searches from the keyboard", async ({ page }) => {
  const errors = await ready(page, "search.html");
  await page.evaluate(() => {
    (window as any).searches = [];
    document.addEventListener("gt-table-search", (event) => {
      (window as any).searches.push((event as CustomEvent).detail);
    });
  });
  const search = () => page.locator("gt-table").evaluate((node) => (node as any).search);

  // The search box comes before the column labels
  await page.keyboard.press("Tab");
  await expect(searchBox(page)).toBeFocused();
  await page.keyboard.type("fig");
  // Enter searches without waiting for typing to pause
  await page.keyboard.press("Enter");
  expect(await search()).toBe("fig");

  await page.keyboard.press("Escape");
  await expect(searchBox(page)).toHaveValue("");
  expect(await search()).toBe("");
  expect(await visible(page)).toEqual(await shown(page));

  // Setting `search` doesn't fire the event
  await page.locator("gt-table").evaluate((node) => {
    (node as any).search = "ap";
  });
  await expect(searchBox(page)).toHaveValue("ap");
  expect(await page.evaluate(() => (window as any).searches)).toEqual([
    { search: "fig", count: 1 },
    { search: "", count: 8 },
  ]);

  await page.keyboard.press("Tab");
  await expect(page.locator("th#q-num > button.gt-i-sort")).toBeFocused();
  expect(errors).toEqual([]);
});

test("moves each group's label cell to its first shown row when groups are a column", async ({
  page,
}) => {
  const errors = await ready(page, "search-column.html");
  const summary = (group: string) => ({ summary: "Total", group, side: "bottom" });

  await searchBox(page).fill("ap");
  await expect(live(page)).toHaveText("Showing 2 of 8 rows");
  expect(await groupCells(page)).toEqual([
    { label: "grp_b", row: 6, first: true, last: summary("grp_b"), fits: true },
    { label: "grp_a", row: 0, first: true, last: summary("grp_a"), fits: true },
  ]);

  await searchBox(page).fill("fig");
  await expect(live(page)).toHaveText("Showing 1 of 8 rows");
  expect(await groupCells(page)).toEqual([
    { label: "grp_b", row: 5, first: true, last: summary("grp_b"), fits: true },
  ]);
  await expect(page.locator("tr.gt_row_group_first")).toHaveCount(2);

  await searchBox(page).fill("");
  await expect(live(page)).toHaveText("Showing all 8 rows");
  expect(await groupCells(page)).toEqual([
    { label: "grp_b", row: 4, first: true, last: summary("grp_b"), fits: true },
    { label: "grp_a", row: 0, first: true, last: summary("grp_a"), fits: true },
  ]);
  expect(errors).toEqual([]);
});

test("the search box lines up with the table, in its font", async ({ page }) => {
  const errors = await ready(page, "search.html");
  const boxes = await page.locator("gt-table").evaluate((node) => {
    const table = node.querySelector("table") as HTMLElement;
    const input = node.querySelector("input.gt-i-search") as HTMLElement;
    const toolbar = input.parentElement as HTMLElement;
    return {
      table: table.getBoundingClientRect().toJSON(),
      toolbar: toolbar.getBoundingClientRect().toJSON(),
      input: input.getBoundingClientRect().toJSON(),
      fonts: [getComputedStyle(table).fontFamily, getComputedStyle(input).fontFamily],
    };
  });
  // GT centres the table; the toolbar spans it, with the search box at its end
  expect(boxes.toolbar.left).toBeCloseTo(boxes.table.left, 0);
  expect(boxes.toolbar.width).toBeCloseTo(boxes.table.width, 0);
  expect(boxes.input.right).toBeCloseTo(boxes.table.right, 0);
  expect(boxes.input.bottom).toBeLessThanOrEqual(boxes.table.top);
  expect(boxes.fonts[1]).toBe(boxes.fonts[0]);

  // And keeps lining up when the page is narrower
  await page.setViewportSize({ width: 500, height: 800 });
  await expect
    .poll(() =>
      page.locator("gt-table").evaluate((node) => {
        const table = (node.querySelector("table") as HTMLElement).getBoundingClientRect();
        const input = (node.querySelector("input.gt-i-search") as HTMLElement).getBoundingClientRect();
        return Math.round(input.right - Math.min(table.right, node.getBoundingClientRect().right));
      }),
    )
    .toBe(0);
  expect(errors).toEqual([]);
});

test.describe("on a touch screen", () => {
  test.use({ hasTouch: true, isMobile: true });

  test("the search box is big enough to tap, and doesn't zoom the page", async ({ page }) => {
    const errors = await ready(page, "search.html");
    const box = await searchBox(page).evaluate((input) => ({
      height: input.getBoundingClientRect().height,
      fontSize: parseFloat(getComputedStyle(input).fontSize),
    }));
    expect(box.height).toBeGreaterThanOrEqual(44);
    expect(box.fontSize).toBeGreaterThanOrEqual(16);

    await searchBox(page).tap();
    await expect(searchBox(page)).toBeFocused();
    await page.keyboard.type("fig");
    await expect(live(page)).toHaveText("Showing 1 of 8 rows");
    expect(errors).toEqual([]);
  });
});
