import { expect, type Locator, type Page, test } from "@playwright/test";
import { ready } from "./helpers";

// Explorers (`preset="explorer"`): exibble's num, char, fctr and date (8 rows, on one page, with
// row_1... as the stub), every column filtered, profiled, hideable and movable, with CSV export;
// the rows numbered, the dtypes under the labels, the dimensions above the table, and the missing
// values tinted (char's in row_5, num's in row_6, date's in row_7, which `sub_missing()` shows as
// dashes). In a container 800px wide, with rows to select or without; stacked in one 360px wide;
// and dropping the columns but char in one 300px wide.

const el = (page: Page) => page.locator("gt-table");
const bar = (page: Page) => el(page).locator(".gt-i-bar");
const dimensions = (page: Page) => el(page).locator(".gt-i-toolbar > .gt-i-dimensions");
const th = (page: Page, column: string) => page.locator(`th#e-${column}`);
const dtype = (page: Page, column: string) => th(page, column).locator(".gt-i-dtype");
const searchBox = (page: Page) => el(page).locator("input.gt-i-search");
// (From the bar, where the search is behind a button)
const search = async (page: Page, text: string) => {
  if (!(await searchBox(page).isVisible())) {
    await el(page).getByRole("button", { name: "Search the table" }).click();
  }
  await searchBox(page).fill(text);
};
const row = (page: Page, label: string) =>
  el(page).locator("tbody tr", { has: page.locator(`th.gt_stub:text-is("${label}")`) });

/** The shown rows' numbers and labels. */
const numbered = (page: Page) =>
  el(page)
    .locator("tbody tr:visible")
    .evaluateAll((trs) =>
      trs.flatMap((tr) => {
        const number = tr.querySelector(":scope > td.gt-i-select > .gt-i-rownum");
        return number === null ? [] : [[number.textContent, tr.querySelector("th.gt_stub")?.textContent]];
      }),
    );

/** The tinted cells: their rows' labels, and their columns. */
const tinted = (page: Page) =>
  el(page)
    .locator("tbody .gt-i-missing")
    .evaluateAll((cells) =>
      cells.map((cell) => [
        cell.closest("tr")?.querySelector("th.gt_stub")?.textContent,
        cell.getAttribute("headers")?.split(" ").pop() ?? null,
        getComputedStyle(cell).backgroundImage.includes("gradient"),
      ]),
    );

const middle = async (locator: Locator) => {
  const box = (await locator.boundingBox()) as { x: number; y: number; width: number; height: number };
  return { y: box.y + box.height / 2, left: box.x, right: box.x + box.width };
};

const ALL = [1, 2, 3, 4, 5, 6, 7, 8].map((n) => [String(n), `row_${n}`]);
const MISSING = [
  ["row_5", "e-char", true],
  ["row_6", "e-num", true],
  ["row_7", "e-date", true],
];

test.describe("an explorer", () => {
  test("numbers the rows, shows the dtypes and dimensions, and tints missing values", async ({ page }) => {
    const errors = await ready(page, "explorer.html");
    await expect(dimensions(page)).toHaveText("8 rows × 5 columns");
    // (Above the table, at its start)
    const [banner, table] = await Promise.all([middle(dimensions(page)), middle(el(page).locator("table"))]);
    expect(Math.abs(banner.left - table.left)).toBeLessThan(2);
    expect(await numbered(page)).toEqual(ALL);
    for (const [column, name] of [["num", "f64"], ["char", "str"], ["fctr", "str"], ["date", "str"]]) {
      await expect(dtype(page, column as string)).toHaveText(name as string);
    }
    // (The controls are named by the label's text, without the dtype)
    await expect(el(page).getByRole("button", { name: "Sort by num", exact: true })).toHaveCount(1);
    expect(await tinted(page)).toEqual(MISSING);
    // The rows can't be selected, so the numbers aren't a target
    const lead = row(page, "row_1").locator("td.gt-i-select");
    expect(await lead.evaluate((td) => getComputedStyle(td).cursor)).toBe("auto");
    await lead.click();
    await expect(el(page).locator("tr.gt-i-selected")).toHaveCount(0);
    expect(errors).toEqual([]);
  });

  test("keeps the rows' numbers with them, and counts the rows and columns shown", async ({ page }) => {
    const errors = await ready(page, "explorer.html");
    const sort = el(page).getByRole("button", { name: "Sort by num", exact: true });
    await sort.click();
    await sort.click();
    await expect(th(page, "num")).toHaveAttribute("aria-sort", "descending");
    const sorted = await numbered(page);
    expect(sorted[0]).toEqual(["8", "row_8"]);
    expect(sorted.slice().sort()).toEqual(ALL);
    expect(await tinted(page)).toHaveLength(3);

    await search(page, "fig");
    await expect(dimensions(page)).toHaveText("1 of 8 rows × 5 columns");
    expect(await numbered(page)).toEqual([["6", "row_6"]]);

    await bar(page).getByRole("button", { name: "Show, hide or reorder columns", exact: true }).click();
    await bar(page).getByRole("group", { name: "Columns", exact: true }).getByRole("checkbox", { name: "fctr", exact: true }).click();
    await expect(dimensions(page)).toHaveText("1 of 8 rows × 4 of 5 columns");
    await search(page, "");
    await expect(dimensions(page)).toHaveText("8 rows × 4 of 5 columns");
    expect(errors).toEqual([]);
  });

  test("doesn't export the numbers or dtypes", async ({ page }) => {
    const errors = await ready(page, "explorer.html");
    const lines = (await el(page).evaluate((node) => (node as any).toCSV() as string)).split(/\r?\n/);
    expect(lines[0]).not.toMatch(/f64|str/);
    expect(lines[1]).toMatch(/^row_1,0\.1111,apricot,one,2015-01-15$/);
    expect(errors).toEqual([]);
  });

  test("puts each row's number beside its checkbox", async ({ page }) => {
    const errors = await ready(page, "explorer-select.html");
    expect(await numbered(page)).toEqual(ALL);
    const lead = row(page, "row_3").locator("td.gt-i-select");
    const [number, box] = await Promise.all([middle(lead.locator(".gt-i-rownum")), middle(lead.locator("input"))]);
    expect(Math.abs(number.y - box.y)).toBeLessThan(3);
    expect(number.right).toBeLessThanOrEqual(box.left);
    await lead.locator("input").click();
    expect(await el(page).evaluate((node) => (node as any).selection)).toEqual([2]);
    await expect(el(page).locator("thead th.gt-i-select-all input")).toHaveAttribute("aria-label", "Select all rows");
    expect(errors).toEqual([]);
  });

  test("is stacked in a narrow container, with the numbers on the cards", async ({ page }) => {
    const errors = await ready(page, "explorer-stack.html");
    await expect(el(page)).toHaveAttribute("data-gti-stacked", "");
    await expect(dimensions(page)).toHaveText("8 rows × 5 columns");
    // (The column of numbers has no chip)
    await expect(el(page).locator("thead th.gt-i-select")).toBeHidden();
    await expect(dtype(page, "num")).toBeVisible();
    expect(await numbered(page)).toEqual(ALL);
    // (On the stub's line)
    const card = row(page, "row_2");
    const [number, label] = await Promise.all([middle(card.locator(".gt-i-rownum")), middle(card.locator("th.gt_stub"))]);
    expect(Math.abs(number.y - label.y)).toBeLessThan(3);
    expect(await tinted(page)).toEqual(MISSING);
    expect(errors).toEqual([]);
  });

  test("drops columns in a narrow container, keeping the numbers", async ({ page }) => {
    const errors = await ready(page, "explorer-collapse.html");
    expect(await numbered(page)).toEqual(ALL);
    await expect(dtype(page, "char")).toBeVisible();
    expect((await tinted(page)).filter(([, , shown]) => shown)).toContainEqual(["row_5", "e-char", true]);
    expect(errors).toEqual([]);
  });
});
