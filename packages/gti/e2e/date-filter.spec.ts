import { expect, type Page, test } from "@playwright/test";
import { dataRows, ready, visible } from "./helpers";

// Date filters, on a GTI table of exibble (8 rows, on one page): `date` of dates (shown as
// "15 Jan 2015", one missing) and `datetime` of dates and times (to the minute, one missing),
// each filtered by a date range; with the view kept in the URL.

const el = (page: Page) => page.locator("gt-table");
const filterButton = (page: Page, column: string) =>
  el(page).getByRole("button", { name: new RegExp(`^Filter ${column}( \\(on\\))?$`) });
const panel = (page: Page, column: string) => el(page).getByRole("group", { name: `Filter ${column}`, exact: true });
const field = (page: Page, column: string, which: "from" | "to") =>
  panel(page, column).getByLabel(`${column}, ${which}`, { exact: true });
const tokens = (page: Page) => el(page).getByRole("list", { name: "Filters" }).locator(".gt-i-token-open");
const filter = (page: Page) => el(page).evaluate((node) => (node as any).filter);
const search = (page: Page) => new URL(page.url()).search;
const query = (page: Page) => el(page).getByRole("combobox", { name: "Filters as text" });
const suggestions = (page: Page) => el(page).getByRole("listbox", { name: "Suggestions" });

/** Type a query in the query box, and apply it. */
async function typeQuery(page: Page, text: string): Promise<void> {
  if (!(await query(page).isVisible())) {
    await el(page).getByRole("button", { name: "Edit the filters as text" }).click();
  }
  await query(page).fill(text);
  await expect(suggestions(page)).toBeHidden();
  await query(page).press("Enter");
}

test("filters by dates, from date fields", async ({ page }) => {
  const errors = await ready(page, "dates.html");
  await filterButton(page, "date").click();
  const from = field(page, "date", "from");
  await expect(from).toBeFocused();
  await expect(from).toHaveAttribute("type", "date");
  // (From the column's first date to its last)
  await expect(from).toHaveAttribute("min", "2015-01-15");
  await expect(from).toHaveAttribute("max", "2015-08-15");

  await from.fill("2015-03-01");
  await from.press("Enter");
  expect(await filter(page)).toEqual({ and: [{ col: "date", op: "gte", value: "2015-03-01" }] });
  // (Not the row whose date is missing)
  expect(dataRows(await visible(page))).toEqual([2, 3, 4, 5, 7]);
  await expect(tokens(page)).toHaveText(["date ≥ Mar 1, 2015"]);

  // (A bound that's one of the column's dates is shown as the table shows it)
  const to = field(page, "date", "to");
  await to.fill("2015-05-15");
  await to.press("Enter");
  expect(dataRows(await visible(page))).toEqual([2, 3, 4]);
  await expect(tokens(page)).toHaveText(["date Mar 1, 2015 – 15 May 2015"]);
  await expect(filterButton(page, "date")).toHaveAccessibleName("Filter date (on)");

  await from.fill("");
  await from.press("Enter");
  expect(await filter(page)).toEqual({ and: [{ col: "date", op: "lte", value: "2015-05-15" }] });
  expect(dataRows(await visible(page))).toEqual([0, 1, 2, 3, 4]);
  expect(errors).toEqual([]);
});

test("filters by dates and times, from date and time fields", async ({ page }) => {
  const errors = await ready(page, "dates.html");
  await filterButton(page, "datetime").click();
  const from = field(page, "datetime", "from");
  await expect(from).toHaveAttribute("type", "datetime-local");
  await expect(from).toHaveAttribute("min", "2018-01-01T02:22:00");

  await from.fill("2018-03-03T03:44");
  await from.press("Enter");
  expect(await filter(page)).toEqual({ and: [{ col: "datetime", op: "gte", value: "2018-03-03T03:44" }] });
  expect(dataRows(await visible(page))).toEqual([2, 3, 4, 5, 6]);
  // (A minute later leaves out the row at that minute)
  await from.fill("2018-03-03T03:45");
  await from.press("Enter");
  expect(dataRows(await visible(page))).toEqual([3, 4, 5, 6]);
  await expect(tokens(page)).toHaveText(["datetime ≥ Mar 3, 2018, 3:45 AM"]);
  expect(errors).toEqual([]);
});

test("takes dates in the query box, and keeps them in the URL", async ({ page }) => {
  const errors = await ready(page, "dates.html");
  await typeQuery(page, 'date <= "2015-02-15" and datetime >= "2018-01-01"');
  expect(await filter(page)).toEqual({
    and: [
      { col: "date", op: "lte", value: "2015-02-15" },
      { col: "datetime", op: "gte", value: "2018-01-01" },
    ],
  });
  expect(dataRows(await visible(page))).toEqual([0, 1]);
  await expect(tokens(page)).toHaveText(["date ≤ 15 Feb 2015", "datetime ≥ Jan 1, 2018"]);
  await expect
    .poll(() => search(page))
    .toBe("?dt.filter=date+%3C%3D+%222015-02-15%22+and+datetime+%3E%3D+%222018-01-01%22");

  await page.reload();
  await expect(el(page)).toHaveAttribute("data-gti-state", "ready");
  expect(dataRows(await visible(page))).toEqual([0, 1]);
  // (Its fields show it too)
  await filterButton(page, "date").click();
  await expect(field(page, "date", "to")).toHaveValue("2015-02-15");
  expect(errors).toEqual([]);
});

test("says what's wrong with a date in the query box", async ({ page }) => {
  const errors = await ready(page, "dates.html");
  await typeQuery(page, 'date >= "2015-02-30"');
  await expect(el(page).locator(".gt-i-query-error")).toHaveText(
    /"2015-02-30" isn't a date \("YYYY-MM-DD"\), and date has dates without times/,
  );
  expect(await filter(page)).toBeNull();
  // (Nor a time, for a column of dates)
  await typeQuery(page, 'date >= "2015-02-15T00:00"');
  await expect(el(page).locator(".gt-i-query-error")).toHaveText(/and date has dates without times/);
  expect(errors).toEqual([]);
});
