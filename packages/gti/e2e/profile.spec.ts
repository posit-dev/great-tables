import { expect, type Page, test } from "@playwright/test";
import { ready } from "./helpers";

// Column profiles: exibble (8 rows, grp_b then grp_a), searchable (from the bar) and filtered by
// fctr (a facet), with profiles under the labels of num (a histogram, with a NaN), char (its most
// common values, with a missing value), fctr (5 values and the 3 others) and date (a histogram of
// datetimes), and none under currency's. In a container 800px wide; and stacked in one 360px wide.

const el = (page: Page) => page.locator("gt-table");
const th = (page: Page, column: string) => page.locator(`th#f-${column}`);
const profile = (page: Page, column: string) => th(page, column).locator(".gt-i-profile");
const caption = (page: Page, column: string) => profile(page, column).locator(".gt-i-profile-text");
const searchBox = (page: Page) => el(page).locator("input.gt-i-search");
// (From the bar, where the search is behind a button)
const search = async (page: Page, text: string) => {
  if (!(await searchBox(page).isVisible())) {
    await el(page).getByRole("button", { name: "Search the table" }).click();
  }
  await searchBox(page).fill(text);
};
const live = (page: Page) => el(page).locator(".gt-i-live");
const filterButton = (page: Page) => el(page).getByRole("button", { name: /^Filter fctr( \(on\))?$/ });
const panel = (page: Page) => el(page).getByRole("group", { name: "Filter fctr", exact: true });

const PROFILED = ["num", "char", "fctr", "date"];

/** Each column's caption. */
const captions = (page: Page) => Promise.all(PROFILED.map((column) => caption(page, column).textContent()));

/** The heights of a column's bars, and their titles. */
const bars = (page: Page, column: string) =>
  profile(page, column)
    .locator("g")
    .evaluateAll((groups) =>
      groups.map((g) => {
        const bar = g.querySelector("rect:not(.gt-i-profile-hit)") as SVGRectElement;
        return { height: Number(bar.getAttribute("height")), title: g.querySelector("title")?.textContent };
      }),
    );

test.describe("column profiles", () => {
  test("are drawn under the labels of the columns with them, of the whole table", async ({ page }) => {
    const errors = await ready(page, "profile.html");
    expect(await captions(page)).toEqual([
      "0.11 – 8,880,000.00 · 13% missing",
      "7 values · 13% missing",
      "8 values",
      "2015/01/15 – 2015/08/15 · 13% missing",
    ]);
    for (const column of PROFILED) {
      await expect(profile(page, column)).toBeVisible();
      await expect(profile(page, column)).toHaveAttribute("aria-hidden", "true");
    }
    // A histogram of 20 bins, from the lowest number to the highest
    const num = await bars(page, "num");
    expect(num).toHaveLength(20);
    expect(num[0]).toEqual({ height: 1, title: "0.111 – 444K: 5 rows" });
    expect(num[19]).toEqual({ height: 0.2, title: "8.44M – 8.88M: 1 row" });
    // The values most rows have, then the others, by their text in the table
    expect((await bars(page, "char")).map((bar) => bar.title)).toEqual([
      "apricot: 1 row",
      "banana: 1 row",
      "coconut: 1 row",
      "durian: 1 row",
      "fig: 1 row",
      "2 other values: 2 rows",
    ]);
    expect((await bars(page, "date"))[0]?.title).toBe("Jan 15, 2015 – Jan 25, 2015: 1 row");
    // An empty one under the labels without one, so that the labels line up
    await expect(profile(page, "currency").locator("svg")).toHaveCount(0);
    await expect(th(page, "currency")).not.toHaveClass(/gt-i-profiled/);
    expect(errors).toEqual([]);
  });

  test("line up under the labels", async ({ page }) => {
    const errors = await ready(page, "profile.html");
    const boxes = await el(page)
      .locator("thead tr.gt_col_headings th")
      .evaluateAll((cells) =>
        cells.map((cell) => {
          const slot = cell.querySelector(".gt-i-profile") as HTMLElement;
          return { bottom: cell.getBoundingClientRect().bottom, top: slot.getBoundingClientRect().top, height: slot.offsetHeight };
        }),
      );
    // (The stubhead's, the five columns')
    expect(boxes).toHaveLength(6);
    for (const box of boxes) {
      expect(box.bottom).toBeCloseTo(boxes[0]?.bottom as number, 0);
      expect(box.top).toBeCloseTo(boxes[0]?.top as number, 0);
      expect(box.height).toBe(boxes[0]?.height);
    }
    // (Within its cell, across it)
    const inside = await th(page, "char").evaluate((cell) => {
      const outer = cell.getBoundingClientRect();
      const svg = (cell.querySelector(".gt-i-profile svg") as SVGElement).getBoundingClientRect();
      return svg.left >= outer.left && svg.right <= outer.right && svg.width > outer.width / 2;
    });
    expect(inside).toBe(true);
    expect(errors).toEqual([]);
  });

  test("count the rows a search keeps", async ({ page }) => {
    const errors = await ready(page, "profile.html");
    await search(page, "fig");
    await expect(live(page)).toHaveText("Showing 1 of 8 rows");
    await expect(caption(page, "num")).toHaveText("100% missing");
    expect(await captions(page)).toEqual(["100% missing", "1 value", "1 value", "2015/06/15"]);
    expect((await bars(page, "char")).map((bar) => bar.height)).toEqual([0, 0, 0, 0, 1, 0]);

    await search(page, "zzz");
    await expect(caption(page, "num")).toHaveText("No rows");
    expect((await bars(page, "num")).every((bar) => bar.height === 0)).toBe(true);

    await search(page, "");
    await expect(caption(page, "num")).toHaveText("0.11 – 8,880,000.00 · 13% missing");
    expect(errors).toEqual([]);
  });

  test("count the rows a filter keeps, in its own column too", async ({ page }) => {
    const errors = await ready(page, "profile.html");
    await filterButton(page).click();
    await panel(page).getByRole("checkbox", { name: /^one\b/ }).check();
    await panel(page).getByRole("checkbox", { name: /^five\b/ }).check();
    await expect(live(page)).toHaveText("Showing 2 of 8 rows");
    expect(await captions(page)).toEqual([
      "0.11 – 5,550.00",
      "1 value · 50% missing",
      "2 values",
      "2015/01/15 – 2015/05/15",
    ]);
    expect((await bars(page, "fctr")).map((bar) => bar.title)).toEqual([
      "eight: 0 rows",
      "five: 1 row",
      "four: 0 rows",
      "one: 1 row",
      "seven: 0 rows",
      "3 other values: 0 rows",
    ]);
    expect(errors).toEqual([]);
  });

  test("stay as they are as the rows are sorted, and aren't a way to sort", async ({ page }) => {
    const errors = await ready(page, "profile.html");
    const before = await Promise.all(PROFILED.map((column) => bars(page, column)));
    await th(page, "num").locator("button.gt-i-sort").click();
    await expect(th(page, "num")).toHaveAttribute("aria-sort", "ascending");
    expect(await Promise.all(PROFILED.map((column) => bars(page, column)))).toEqual(before);

    await profile(page, "char").locator("svg").click();
    await profile(page, "date").locator(".gt-i-profile-text").click();
    await expect(th(page, "char")).not.toHaveAttribute("aria-sort");
    await expect(th(page, "date")).not.toHaveAttribute("aria-sort");
    await expect(th(page, "num")).toHaveAttribute("aria-sort", "ascending");
    expect(errors).toEqual([]);
  });

  test("aren't shown in a stacked table", async ({ page }) => {
    const errors = await ready(page, "profile-stack.html");
    await expect(el(page)).toHaveAttribute("data-gti-stacked", "");
    for (const column of PROFILED) {
      await expect(profile(page, column)).toBeHidden();
    }
    // (And are, once its container is wide enough for a table, counting the rows a search keeps)
    await search(page, "fig");
    await page.locator("body > div").evaluate((div) => ((div as HTMLElement).style.width = "800px"));
    await expect(el(page)).not.toHaveAttribute("data-gti-stacked");
    await expect(profile(page, "char")).toBeVisible();
    await expect(caption(page, "char")).toHaveText("1 value");
    expect(errors).toEqual([]);
  });
});
