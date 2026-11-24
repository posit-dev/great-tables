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

test.describe("colors of a column dropped to fit", () => {
  // (n, dropped from the table in a narrow container, and shown under each row open)
  const el = (page: Page) => page.locator("gt-table");
  const row = (page: Page, fruit: string) => el(page).locator("tbody tr", { has: page.locator(`th.gt_stub:text-is("${fruit}")`) });
  const value = (page: Page, fruit: string) => row(page, fruit).locator("+ tr.gt-i-details dd").first();
  const shown = (page: Page, fruit: string) =>
    value(page, fruit).evaluate((dd) => {
      const style = getComputedStyle(dd);
      return [style.backgroundColor, style.color];
    });
  const searchFor = (page: Page, text: string) => el(page).evaluate((node, text) => ((node as any).search = text), text);

  test("are its cells', under a row open, and made again as a search changes", async ({ page }) => {
    const errors = await ready(page, "colors-collapse.html");
    await expect(el(page)).toHaveAttribute("data-gti-dropped", "");
    await expect(el(page).locator("thead th#c-n")).toBeHidden();
    const made = await expected(page);
    const first = await asShown(page, made[""] as Colors);
    await row(page, "apple").locator(".gt-i-expand").click();
    await row(page, "banana").locator(".gt-i-expand").click();
    // (Apple's its own red, from tab_style())
    expect(await shown(page, "apple")).toEqual(first["0"]);
    expect(await shown(page, "banana")).toEqual(first["2"]);

    await searchFor(page, "b");
    await expect.poll(() => visible(page)).toEqual([2, 3]);
    expect(await shown(page, "banana")).toEqual((await asShown(page, made.b as Colors))["2"]);
    await searchFor(page, "a");
    await expect.poll(() => visible(page)).toEqual([0, 1, 2, 5]);
    const a = await asShown(page, made.a as Colors);
    expect(await shown(page, "banana")).toEqual(a["2"]);
    expect(await shown(page, "apple")).toEqual(a["0"]);
    await searchFor(page, "");
    await expect.poll(() => visible(page)).toEqual([0, 1, 2, 3, 4, 5]);
    expect(await shown(page, "banana")).toEqual(first["2"]);

    // (Around the value, not across the row)
    const widths = await value(page, "banana").evaluate((dd) => [dd.getBoundingClientRect().width, (dd.parentElement as HTMLElement).getBoundingClientRect().width]);
    expect(widths[0]).toBeLessThan((widths[1] as number) / 2);
    expect(errors).toEqual([]);
  });
});
