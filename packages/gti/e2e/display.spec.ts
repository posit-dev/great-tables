import { expect, type Page, test } from "@playwright/test";
import { ready } from "./helpers";

// exibble's num, char and currency, with group headings (or groups as a column), group and grand
// summary rows, striping, a filled cell (row 0's currency), and a long value in a narrow column
// (row 2's char, 90px wide).

const FILL = "rgb(173, 216, 230)";

/** A body row: data row `row`, or the first row headed `label` (a group heading, a summary row). */
function row(page: Page, which: number | string) {
  const label = typeof which === "number" ? `row_${which + 1}` : which;
  return page
    .locator("gt-table tbody.gt_table_body > tr")
    .filter({ has: page.locator("th", { hasText: new RegExp(`^${label}$`) }) })
    .first();
}

/** For each cell of a body row: whether it's tinted, and its background colour. */
function cells(page: Page, which: number | string) {
  return row(page, which).evaluate((tr) =>
    Array.from(tr.children, (cell) => {
      const css = getComputedStyle(cell);
      return {
        group: cell.classList.contains("gt_stub_row_group"),
        tinted: css.boxShadow.includes("inset"),
        background: css.backgroundColor,
      };
    }),
  );
}

const tinted = async (page: Page, which: number | string) =>
  (await cells(page, which)).map((cell) => cell.tinted);

const height = (page: Page, which: number | string) =>
  row(page, which).evaluate((tr) => tr.getBoundingClientRect().height);

test.describe("highlighting", () => {
  test("tints the data row under the pointer, over the cells' own backgrounds", async ({ page }) => {
    const errors = await ready(page, "display-highlight.html");
    const before = await cells(page, 0);
    expect(before.every((cell) => !cell.tinted)).toBe(true);

    await row(page, 0).locator("td").first().hover();
    const after = await cells(page, 0);
    expect(after.every((cell) => cell.tinted)).toBe(true);
    // The fill and striping still show
    expect(after.map((cell) => cell.background)).toEqual(before.map((cell) => cell.background));
    expect(after.map((cell) => cell.background)).toContain(FILL);
    expect(await tinted(page, 1)).toEqual([false, false, false, false]);

    // Striped rows too
    await row(page, 1).locator("td").first().hover();
    expect(await tinted(page, 1)).toEqual([true, true, true, true]);
    expect(await tinted(page, 0)).toEqual([false, false, false, false]);
    expect(errors).toEqual([]);
  });

  test("leaves group headings and summary rows alone", async ({ page }) => {
    const errors = await ready(page, "display-highlight.html");
    for (const which of ["grp_a", "Total", "Max"]) {
      await row(page, which).hover();
      expect((await row(page, which).evaluate((tr) =>
        Array.from(tr.children, (cell) => getComputedStyle(cell).boxShadow),
      )).every((shadow) => shadow === "none")).toBe(true);
    }
    expect(errors).toEqual([]);
  });

  test("leaves a group's label cell alone when groups are a column", async ({ page }) => {
    const errors = await ready(page, "display-highlight-column.html");
    // Row 4 is grp_b's first row, so it holds the label cell
    await row(page, 4).locator("td").first().hover();
    expect(await cells(page, 4)).toEqual([
      expect.objectContaining({ group: true, tinted: false }),
      expect.objectContaining({ tinted: true }),
      expect.objectContaining({ tinted: true }),
      expect.objectContaining({ tinted: true }),
      expect.objectContaining({ tinted: true }),
    ]);
    expect(errors).toEqual([]);
  });

  test("is off unless asked for", async ({ page }) => {
    const errors = await ready(page, "display.html");
    await row(page, 0).locator("td").first().hover();
    expect(await tinted(page, 0)).toEqual([false, false, false, false]);
    expect(errors).toEqual([]);
  });

  test.describe("on a touch screen", () => {
    test.use({ hasTouch: true, isMobile: true });

    test("marks the row tapped, until it or another row is tapped", async ({ page }) => {
      const errors = await ready(page, "display-highlight.html");
      // (Nothing hovers here)
      expect(await page.evaluate(() => matchMedia("(hover: hover)").matches)).toBe(false);

      await row(page, 0).locator("td").first().tap();
      expect(await tinted(page, 0)).toEqual([true, true, true, true]);
      await row(page, 1).locator("td").first().tap();
      expect(await tinted(page, 0)).toEqual([false, false, false, false]);
      expect(await tinted(page, 1)).toEqual([true, true, true, true]);
      await row(page, 1).locator("td").first().tap();
      expect(await tinted(page, 1)).toEqual([false, false, false, false]);
      expect(errors).toEqual([]);
    });
  });
});

test("compact rows have half the vertical padding", async ({ page }) => {
  await ready(page, "display.html");
  const normal = { data: await height(page, 0), heading: await height(page, "grp_a") };
  const labels = await page.locator("gt-table .gt_col_headings").evaluate((tr) => tr.getBoundingClientRect().height);

  const errors = await ready(page, "display-compact.html");
  // 4px less above and below
  expect(await height(page, 0)).toBeCloseTo(normal.data - 8, 0);
  expect(await height(page, "grp_a")).toBeCloseTo(normal.heading - 8, 0);
  expect(await page.locator("gt-table .gt_col_headings").evaluate((tr) => tr.getBoundingClientRect().height)).toBeCloseTo(
    labels,
    0,
  );
  expect(errors).toEqual([]);
});

test.describe("text wrapping", () => {
  const longCell = (page: Page) => row(page, 2).locator("td").nth(1);

  test("wraps long text by default", async ({ page }) => {
    const errors = await ready(page, "display.html");
    expect(await height(page, 2)).toBeGreaterThan((await height(page, 1)) + 10);
    expect(errors).toEqual([]);
  });

  test("when off, keeps text on one line and ends what's cut off with an ellipsis", async ({ page }) => {
    const errors = await ready(page, "display-nowrap.html");
    expect(await height(page, 2)).toBeCloseTo(await height(page, 1), 0);
    const cell = await longCell(page).evaluate((td) => ({
      cut: td.scrollWidth > td.clientWidth,
      width: td.getBoundingClientRect().width,
      whiteSpace: getComputedStyle(td).whiteSpace,
      textOverflow: getComputedStyle(td).textOverflow,
      text: td.textContent,
    }));
    expect(cell).toEqual({
      cut: true,
      width: expect.closeTo(90, 0),
      whiteSpace: "nowrap",
      textOverflow: "ellipsis",
      // All of it is still there, for screen readers and search
      text: "a coconut, cracked open at noon",
    });
    expect(errors).toEqual([]);
  });

  test("when off, keeps the column's width in a narrow window", async ({ page }) => {
    await page.setViewportSize({ width: 250, height: 600 });
    const errors = await ready(page, "display-nowrap.html");
    expect(await longCell(page).evaluate((td) => td.getBoundingClientRect().width)).toBeCloseTo(90, 0);
    // (The table scrolls rather than squeezing the other columns)
    const table = await page.locator("gt-table table").evaluate((table) => table.getBoundingClientRect().width);
    expect(table).toBeGreaterThan(250);
    expect(errors).toEqual([]);
  });

  test("when off, still finds text that's cut off", async ({ page }) => {
    const errors = await ready(page, "display-nowrap.html");
    await page.locator("gt-table").evaluate((el) => {
      (el as any).search = "noon";
    });
    await expect(row(page, 2)).toBeVisible();
    await expect(row(page, 1)).toBeHidden();
    expect(errors).toEqual([]);
  });
});
