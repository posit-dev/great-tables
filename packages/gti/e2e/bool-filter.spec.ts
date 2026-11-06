import { expect, type Page, test } from "@playwright/test";
import { dataRows, ready, visible } from "./helpers";

// A bool filter, on a GTI table of exibble (8 rows, on one page): `big`, whether `num` is over 100
// (shown as "yes" or "no"; rows 3, 4, 6 and 7 are, 0 to 2 aren't, and 5 is missing); with the view
// kept in the URL.

const el = (page: Page) => page.locator("gt-table");
const filterButton = (page: Page) => el(page).getByRole("button", { name: /^Filter big( \(on\))?$/ });
const panel = (page: Page) => el(page).getByRole("group", { name: "Filter big", exact: true });
const radio = (page: Page, name: string) => panel(page).getByRole("radio", { name, exact: false });
const tokens = (page: Page) => el(page).getByRole("list", { name: "Filters" }).locator(".gt-i-token-open");
const filter = (page: Page) => el(page).evaluate((node) => (node as any).filter);
const search = (page: Page) => new URL(page.url()).search;
const query = (page: Page) => el(page).getByRole("combobox", { name: "Filters as text" });
const suggestions = (page: Page) => el(page).getByRole("listbox", { name: "Suggestions" });

test("chooses any value, true, false or a missing one, from radio buttons", async ({ page }) => {
  const errors = await ready(page, "bools.html");
  await filterButton(page).click();
  await expect(panel(page).getByRole("radiogroup", { name: "big" })).toBeVisible();
  // (As the table shows the values, true first, with the rows with each)
  await expect(panel(page).locator(".gt-i-filter-option")).toHaveText(["Any8", "yes4", "no3", "(Missing)1"]);
  await expect(radio(page, "Any")).toBeChecked();
  await expect(radio(page, "Any")).toBeFocused();

  await radio(page, "yes").check();
  expect(await filter(page)).toEqual({ and: [{ col: "big", op: "in", value: [true] }] });
  expect(dataRows(await visible(page))).toEqual([3, 4, 6, 7]);
  await expect(tokens(page)).toHaveText(["big: yes"]);
  await expect(filterButton(page)).toHaveAccessibleName("Filter big (on)");

  // (The arrow keys move among them, choosing as they go)
  await radio(page, "yes").press("ArrowDown");
  await expect(radio(page, "no")).toBeChecked();
  expect(dataRows(await visible(page))).toEqual([0, 1, 2]);
  await radio(page, "no").press("ArrowDown");
  expect(await filter(page)).toEqual({ and: [{ col: "big", op: "in", value: [null] }] });
  expect(dataRows(await visible(page))).toEqual([5]);

  // (Tab leaves the panel from the one checked)
  await radio(page, "(Missing)").press("Tab");
  await expect(panel(page)).toBeHidden();
  await expect(filterButton(page)).toBeFocused();

  await filterButton(page).click();
  await expect(radio(page, "(Missing)")).toBeFocused();
  await radio(page, "Any").check();
  expect(await filter(page)).toBeNull();
  expect(dataRows(await visible(page))).toEqual([0, 1, 2, 3, 4, 5, 6, 7]);
  expect(errors).toEqual([]);
});

test("takes one value in the query box, and keeps it in the URL", async ({ page }) => {
  const errors = await ready(page, "bools.html");
  await el(page).getByRole("button", { name: "Edit the filters as text" }).click();
  await query(page).fill("big in (");
  await expect(suggestions(page).getByRole("option")).toHaveText([/^yes/, /^no/, /^\(Missing\)/]);
  await query(page).fill("big in (true, false)");
  await expect(suggestions(page)).toBeHidden();
  await query(page).press("Enter");
  await expect(el(page).locator(".gt-i-query-error")).toHaveText(
    /Big has a bool filter: give one value, true, false or null/,
  );
  expect(await filter(page)).toBeNull();

  await query(page).fill("big in (false)");
  await query(page).press("Enter");
  expect(dataRows(await visible(page))).toEqual([0, 1, 2]);
  await expect(tokens(page)).toHaveText(["big: no"]);
  await expect.poll(() => search(page)).toBe("?bl.filter=big+in+(false)");

  await page.reload();
  await expect(el(page)).toHaveAttribute("data-gti-state", "ready");
  expect(dataRows(await visible(page))).toEqual([0, 1, 2]);
  await filterButton(page).click();
  await expect(radio(page, "no")).toBeChecked();
  expect(errors).toEqual([]);
});
