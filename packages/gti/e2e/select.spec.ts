import { expect, type Page, test } from "@playwright/test";
import { dataRows, ready, shown, visible } from "./helpers";

// exibble's num, char and currency, with group headings (grp_b, rows 4-7, then grp_a, rows 0-3),
// summary rows, a title and a source note: rows to select several at a time, searchable, 3 rows
// to a page, highlighted; one at a time, on one page; and several, with groups shown as a column
// and resizable columns.

const el = (page: Page) => page.locator("gt-table");
const row = (page: Page, index: number) =>
  el(page).locator("tbody.gt_table_body > tr").filter({ has: page.locator(`th.gt_stub:text-is("row_${index + 1}")`) });
const box = (page: Page, index: number) => row(page, index).locator("> .gt-i-select > input");
const selectAll = (page: Page) => el(page).locator("thead .gt-i-select input");
const selection = (page: Page): Promise<number[]> => el(page).evaluate((node) => (node as any).selection);

/** The select events the table fires, from now on. */
async function selects(page: Page) {
  await el(page).evaluate((node) => {
    (window as any).selects = [];
    node.addEventListener("gt-table-select", (event) =>
      (window as any).selects.push((event as CustomEvent).detail.selection),
    );
  });
  return () => page.evaluate(() => (window as any).selects);
}

// The tint over a cell, if any
const tint = (page: Page, selector: string) =>
  el(page)
    .locator(selector)
    .first()
    .evaluate((cell) => getComputedStyle(cell).boxShadow);

test.describe("the selection column", () => {
  test("comes first, as narrow as its checkboxes, with the rows across the table widened", async ({ page }) => {
    const errors = await ready(page, "select.html");
    const table = await el(page).locator("table").boundingBox();
    const header = await el(page).locator("thead th.gt-i-select").boundingBox();
    const cell = await el(page).locator("tbody td.gt-i-select").first().boundingBox();
    expect(header?.x).toBe(table?.x);
    expect(cell?.x).toBe(header?.x);
    expect(cell?.width).toBe(header?.width);
    expect(cell?.width).toBeLessThan(40);
    // The title, group headings and source note span the table, as before
    for (const selector of ["thead .gt_title", "tbody .gt_group_heading", "tfoot .gt_sourcenote"]) {
      const box = await el(page).locator(selector).first().boundingBox();
      expect(Math.abs((box?.width ?? 0) - (table?.width ?? 0))).toBeLessThan(1);
    }
    // Every data row has a checkbox, and summary rows an empty cell
    await expect(el(page).locator("tbody td.gt-i-select input")).toHaveCount(8);
    await expect(el(page).locator("tbody tr:has(.gt_summary_row) > td.gt-i-select:empty")).toHaveCount(2);
    await expect(el(page).locator("tbody tr:has(.gt_grand_summary_row) > td.gt-i-select:empty")).toHaveCount(1);
    await expect(box(page, 4)).toHaveAccessibleName("Select row_5");
    expect(errors).toEqual([]);
  });

  test("puts the group column after the checkboxes, and counts it in resize events", async ({ page }) => {
    const errors = await ready(page, "select-column.html");
    const lead = await row(page, 4)
      .locator("> *")
      .evaluateAll((cells) => cells.slice(0, 3).map((cell) => cell.className.split(" ").pop()));
    expect(lead).toEqual(["gt-i-select", "gt_stub_row_group", "gt_stub"]);
    // (Laid out in its own column, from its group's first row)
    const select = await row(page, 4).locator("> .gt-i-select").boundingBox();
    const group = await row(page, 4).locator("> .gt_stub_row_group").boundingBox();
    expect(Math.abs((group?.x ?? 0) - ((select?.x ?? 0) + (select?.width ?? 0)))).toBeLessThan(1);
    expect(Math.abs((group?.y ?? 0) - (select?.y ?? 0))).toBeLessThan(1);
    // No handle on the selection column
    await expect(el(page).locator("thead th.gt-i-select .gt-i-resizer")).toHaveCount(0);

    await el(page).evaluate((node) => {
      (window as any).resizes = [];
      node.addEventListener("gt-table-resize", (event) => (window as any).resizes.push((event as CustomEvent).detail));
    });
    await page.getByRole("separator", { name: "Resize char" }).focus();
    await page.keyboard.press("ArrowRight");
    // (Selection, group, stub, num, char)
    expect(await page.evaluate(() => (window as any).resizes.map((detail: any) => [detail.column, detail.index]))).toEqual([
      ["char", 4],
    ]);
    // The group label cell isn't tinted, nor is it a target
    await row(page, 4).locator("> .gt_stub_row_group").click();
    expect(await selection(page)).toEqual([]);
    await row(page, 5).locator("> td").last().click();
    expect(await tint(page, "tr.gt-i-selected > td:last-child")).not.toBe("none");
    expect(await tint(page, "th.gt_stub_row_group")).toBe("none");
    expect(errors).toEqual([]);
  });
});

test.describe("selecting rows by mouse", () => {
  test("toggles a row clicked anywhere, tinting it, and tells listeners", async ({ page }) => {
    const errors = await ready(page, "select.html");
    const events = await selects(page);
    await row(page, 4).locator("td").last().click();
    await expect(box(page, 4)).toBeChecked();
    await box(page, 5).click();
    expect(await selection(page)).toEqual([4, 5]);
    expect(await tint(page, "tr.gt-i-selected > td:last-child")).toContain("inset");
    await row(page, 4).locator("th.gt_stub").click();
    await expect(box(page, 4)).not.toBeChecked();
    expect(await events()).toEqual([[4], [4, 5], [5]]);
    expect(errors).toEqual([]);
  });

  test("tints selected rows more than the row under the pointer", async ({ page }) => {
    await ready(page, "select.html");
    // (As `color(srgb r g b / alpha)`)
    const alpha = (shadow: string) => Number(/\/ ([\d.]+)\)/.exec(shadow)?.[1] ?? 0);
    await row(page, 5).locator("td").last().hover();
    const hovered = alpha(await tint(page, "tr.gt-i-row:hover > td:last-child"));
    await row(page, 5).locator("td").last().click();
    await row(page, 6).locator("td").last().hover();
    const selected = alpha(await tint(page, "tr.gt-i-selected > td:last-child"));
    expect(hovered).toBeGreaterThan(0);
    expect(selected).toBeGreaterThan(hovered);
  });

  test("selects a range in the order shown with Shift, selecting no text", async ({ page }) => {
    const errors = await ready(page, "select.html");
    await page.getByRole("button", { name: "char" }).click();
    // (By char in each group: fig, grapefruit, honeydew, then the missing value; then apricot...)
    expect(dataRows(await visible(page))).toEqual([5, 6, 7]);
    await row(page, 6).locator("td").last().click();
    await page.getByRole("button", { name: "Next", exact: true }).click();
    expect(dataRows(await visible(page))).toEqual([4, 0, 1]);
    await row(page, 0).locator("td").last().click({ modifiers: ["Shift"] });
    expect(await selection(page)).toEqual([0, 4, 6, 7]);
    expect(await page.evaluate(() => String(getSelection()))).toBe("");
    await expect(el(page).locator(".gt-i-live")).toHaveText("4 rows selected");
    expect(errors).toEqual([]);
  });

  test("leaves text selection in a row alone", async ({ page }) => {
    await ready(page, "select.html");
    const cell = row(page, 4).locator("td").last();
    const target = (await cell.boundingBox()) as { x: number; y: number; width: number; height: number };
    await page.mouse.move(target.x + 2, target.y + target.height / 2);
    await page.mouse.down();
    await page.mouse.move(target.x + target.width - 2, target.y + target.height / 2, { steps: 5 });
    await page.mouse.up();
    expect(await page.evaluate(() => String(getSelection()))).not.toBe("");
    expect(await selection(page)).toEqual([]);
  });
});

test.describe("selecting every row", () => {
  test("selects the rows matching the search on every page, and shows when some are", async ({ page }) => {
    const errors = await ready(page, "select.html");
    const all = selectAll(page);
    await expect(all).toHaveAccessibleName("Select all rows");
    await all.click();
    expect(await selection(page)).toEqual([0, 1, 2, 3, 4, 5, 6, 7]);
    await expect(el(page).locator(".gt-i-live")).toHaveText("8 rows selected");
    await all.click();
    expect(await selection(page)).toEqual([]);

    await page.getByRole("searchbox").fill("grp_b");
    await expect(all).toHaveAccessibleName("Select all matching rows");
    expect(dataRows(await visible(page))).toHaveLength(0);
    await page.getByRole("searchbox").fill("e");
    await expect(page.locator(".gt-i-pager")).toContainText(/of \d+ rows \(filtered from 8\)/);
    const total = Number(/of (\d+) rows/.exec((await page.locator(".gt-i-pager").textContent()) ?? "")?.[1]);
    // (More than a page, fewer than all)
    expect(total).toBeGreaterThan(3);
    expect(total).toBeLessThan(8);
    await all.click();
    expect(await selection(page)).toHaveLength(total);
    await expect(all).toBeChecked();

    await page.getByRole("searchbox").fill("");
    // (Some of all the rows)
    await expect.poll(() => all.evaluate((input) => (input as HTMLInputElement).indeterminate)).toBe(true);
    await expect(all).not.toBeChecked();
    expect(errors).toEqual([]);
  });

  test("takes a click anywhere in its cell", async ({ page }) => {
    await ready(page, "select.html");
    const cell = (await el(page).locator("thead th.gt-i-select").boundingBox()) as { x: number; y: number };
    await page.mouse.click(cell.x + 2, cell.y + 2);
    expect(await selection(page)).toHaveLength(8);
  });
});

test.describe("selecting rows by keyboard", () => {
  test("toggles a checkbox with Space, and selects a range with Shift+Space", async ({ page }) => {
    const errors = await ready(page, "select.html");
    const events = await selects(page);
    await box(page, 4).focus();
    await page.keyboard.press("Space");
    expect(await selection(page)).toEqual([4]);
    await box(page, 6).focus();
    await page.keyboard.press("Shift+Space");
    expect(await selection(page)).toEqual([4, 5, 6]);
    // Tab moves through the checkboxes
    await page.keyboard.press("Shift+Tab");
    await expect(box(page, 5)).toBeFocused();
    expect(await events()).toEqual([[4], [4, 5, 6]]);
    expect(errors).toEqual([]);
  });
});

test.describe("selecting one row at a time", () => {
  test("clears the row selected before, with no select-all", async ({ page }) => {
    const errors = await ready(page, "select-single.html");
    await expect(selectAll(page)).toHaveCount(0);
    await row(page, 4).locator("td").last().click();
    await row(page, 0).locator("td").last().click();
    expect(await selection(page)).toEqual([0]);
    await expect(box(page, 4)).not.toBeChecked();
    await expect(el(page).locator("tr.gt-i-selected")).toHaveCount(1);
    expect(errors).toEqual([]);
  });

  test("keeps the selection as rows are sorted", async ({ page }) => {
    await ready(page, "select-single.html");
    await box(page, 2).click();
    await page.getByRole("button", { name: "num" }).click();
    expect(await selection(page)).toEqual([2]);
    await expect(box(page, 2)).toBeChecked();
    expect(await shown(page)).not.toEqual([]);
  });
});

test.describe("selecting rows by touch", () => {
  test.use({ hasTouch: true, viewport: { width: 360, height: 700 } });

  test("toggles a row tapped, marking it", async ({ page }) => {
    const errors = await ready(page, "select.html");
    await row(page, 4).locator("td").last().tap();
    expect(await selection(page)).toEqual([4]);
    await expect(row(page, 4)).toHaveClass(/gt-i-marked/);
    await box(page, 5).tap();
    expect(await selection(page)).toEqual([4, 5]);
    const size = await box(page, 5).boundingBox();
    expect(size?.width).toBeGreaterThan(16);
    expect(errors).toEqual([]);
  });
});
