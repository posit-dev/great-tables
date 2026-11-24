import { expect, type Page, test } from "@playwright/test";
import { open } from "./helpers";

// Linked tables (`i_link()`), on one page: "Groups" (grp_a, grp_b), whose rows can be selected,
// and "Rows" (exibble's 8 rows, grp_a's first, 5 to a page), linked by exibble's group.

const groups = (page: Page) => page.locator("gt-table:has(#groups)");
const rows = (page: Page) => page.locator("gt-table:has(#rows)");
const box = (page: Page, label: string) =>
  groups(page).locator("tbody tr", { has: page.locator(`td:text-is("${label}")`) }).locator("> .gt-i-select > input");
const token = (page: Page) => rows(page).getByRole("list", { name: "Filters" }).locator(".gt-i-token[data-gti-link]");
const shownRows = (page: Page) =>
  rows(page).evaluate((node) => {
    const el = node as any;
    return Array.from(node.querySelectorAll<HTMLTableRowElement>("tbody.gt_table_body > tr"))
      .filter((tr) => typeof el.bodyRow(tr) === "number" && tr.getClientRects().length > 0)
      .map((tr) => el.bodyRow(tr) as number);
  });
const infoButton = (page: Page) => rows(page).getByRole("button", { name: "Table info", exact: true });

async function ready(page: Page): Promise<string[]> {
  const errors = await open(page, "link.html");
  for (const el of await page.locator("gt-table").all()) {
    await expect(el).toHaveAttribute("data-gti-state", "ready");
  }
  return errors;
}

test.describe("linked tables", () => {
  test("filter one table to the rows with the values selected in the other", async ({ page }) => {
    const errors = await ready(page);
    expect(await shownRows(page)).toEqual([0, 1, 2, 3, 4]);
    await expect(token(page)).toHaveCount(0);
    await box(page, "grp_b").click();
    await expect(token(page)).toHaveText("Selected in Groups: grp_b");
    expect(await shownRows(page)).toEqual([4, 5, 6, 7]);
    await expect(rows(page).locator(".gt-i-live")).toHaveText("Rows: Showing 4 of 8 rows");
    // (The table selected in isn't filtered)
    await expect(groups(page).locator("tbody tr:visible")).toHaveCount(2);
    await box(page, "grp_a").click();
    await expect(token(page)).toHaveText("Selected in Groups: grp_a, grp_b");
    expect(await shownRows(page)).toEqual([0, 1, 2, 3, 4]);
    await box(page, "grp_a").click();
    await box(page, "grp_b").click();
    await expect(token(page)).toHaveCount(0);
    expect(await shownRows(page)).toEqual([0, 1, 2, 3, 4]);
    expect(errors).toEqual([]);
  });

  test("go to the selection from the token, and lift the filter with its remove button", async ({ page }) => {
    await ready(page);
    await box(page, "grp_b").click();
    await token(page).locator(".gt-i-token-open").click();
    await expect(box(page, "grp_b")).toBeFocused();
    await token(page).getByRole("button", { name: "Show the rows not selected in Groups" }).click();
    await expect(token(page)).toHaveCount(0);
    expect(await shownRows(page)).toEqual([0, 1, 2, 3, 4]);
    // (Focus on the info button, without another token)
    await expect(infoButton(page)).toBeFocused();
    // (Until the selection changes)
    await box(page, "grp_a").click();
    await expect(token(page)).toHaveText("Selected in Groups: grp_a, grp_b");
  });

  test("say so in the info panel, which shows every row again", async ({ page }) => {
    await ready(page);
    await infoButton(page).click();
    const item = rows(page).locator('.gt-i-info-item[data-gti-info="link"]');
    await expect(item).toContainText("Linked to other tables by group");
    const show = item.getByRole("button", { name: "Show the rows the linked tables' selections leave out" });
    await expect(show).toHaveAttribute("aria-disabled", "true");
    await box(page, "grp_a").click();
    await infoButton(page).click();
    await expect(item).toContainText("Filtered by the selection in Groups");
    await show.click();
    expect(await shownRows(page)).toEqual([0, 1, 2, 3, 4]);
    await expect(show).toHaveAttribute("aria-disabled", "true");
    await expect(token(page)).toHaveCount(0);
  });
});
