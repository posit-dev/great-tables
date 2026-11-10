import { expect, type Page, test } from "@playwright/test";
import { ready, visible } from "./helpers";

// A table of fruits (apple, avocado, banana, blueberry, cherry, date) whose n and m are colored
// with `data_color()` (apple's n red, after; date's n missing): n's colors are made again from the
// rows a search keeps, m's stay as they are. The page has, as JSON, n's fills and text colors (by
// row) with every row shown, and with each search, as `data_color()` makes them from those rows.

type Colors = Record<string, [string, string]>;

const searchBox = (page: Page) => page.locator("gt-table input.gt-i-search");
// (From the bar, where the search is behind a button)
const search = async (page: Page, text: string) => {
  if (!(await searchBox(page).isVisible())) {
    await page.locator("gt-table").getByRole("button", { name: "Search the table" }).click();
  }
  await searchBox(page).fill(text);
};

// Each column's cells' fills and text colors, by row, as the browser has them
const colorsOf = (page: Page, column: number) =>
  page.locator("gt-table").evaluate((node, column) => {
    const el = node as any;
    return Object.fromEntries(
      Array.from(node.querySelectorAll<HTMLTableRowElement>("tbody.gt_table_body > tr"), (tr) => {
        const td = tr.querySelectorAll("td")[column] as HTMLElement;
        const style = getComputedStyle(td);
        return [String(el.bodyRow(tr)), [style.backgroundColor, style.color]];
      }),
    );
  }, column);

// The colors, as the browser has them
const asShown = (page: Page, colors: Colors) =>
  page.evaluate((colors) => {
    const div = document.createElement("div");
    document.body.append(div);
    const css = (color: string, property: "backgroundColor" | "color") => {
      div.style[property] = color;
      return getComputedStyle(div)[property];
    };
    const shown = Object.fromEntries(
      Object.entries(colors).map(([row, [fill, text]]) => [row, [css(fill, "backgroundColor"), css(text, "color")]]),
    );
    div.remove();
    return shown;
  }, colors);

async function expected(page: Page): Promise<Record<string, Colors>> {
  return JSON.parse((await page.locator("#expected").textContent()) as string);
}

test.describe("colors made again from the rows kept", () => {
  test("color the rows a search keeps as data_color() colors them alone, and come back after", async ({ page }) => {
    const errors = await ready(page, "colors.html");
    const made = await expected(page);
    const first = await asShown(page, made[""] as Colors);
    const m = await colorsOf(page, 1);
    expect(await colorsOf(page, 0)).toEqual(first);

    await search(page, "b");
    await expect.poll(() => visible(page)).toEqual([2, 3]);
    expect(await colorsOf(page, 0)).toEqual(await asShown(page, made.b as Colors));
    // (Apple's red counts, though it isn't changed)
    await search(page, "a");
    await expect.poll(() => visible(page)).toEqual([0, 1, 2, 5]);
    expect(await colorsOf(page, 0)).toEqual(await asShown(page, made.a as Colors));
    // (Not m's)
    expect(await colorsOf(page, 1)).toEqual(m);

    await search(page, "");
    await expect.poll(() => visible(page)).toEqual([0, 1, 2, 3, 4, 5]);
    expect(await colorsOf(page, 0)).toEqual(first);
    expect(errors).toEqual([]);
  });

  test("don't change for a sort", async ({ page }) => {
    await ready(page, "colors.html");
    const made = await expected(page);
    await search(page, "b");
    await expect.poll(() => visible(page)).toEqual([2, 3]);
    await page.locator("gt-table").evaluate((node) => {
      (node as any).sort = [{ column: "n", descending: true }];
    });
    await expect.poll(() => visible(page)).toEqual([3, 2]);
    expect(await colorsOf(page, 0)).toEqual(await asShown(page, made.b as Colors));
  });
});
