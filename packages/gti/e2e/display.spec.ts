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

// 20 rows (row_1...) on one page, resizable, without text wrapping: title's text short but for row_19's (200
// characters) and row_20's (40); code's all as long, under a longer label; wide's all as long (30
// characters), under a profile; and an image 400px wide in each of picture's cells.
test.describe("column widths without text wrapping", () => {
  const cell = (page: Page, row: number, column: string) =>
    page
      .locator("gt-table tbody > tr")
      .filter({ has: page.locator(`th:text-is("row_${row}")`) })
      .locator(`td[headers~="cp-${column}"]`);
  const cut = (page: Page, row: number, column: string) =>
    cell(page, row, column).evaluate((td) => td.scrollWidth > td.clientWidth);
  const width = (page: Page, row: number, column: string) =>
    cell(page, row, column).evaluate((td) => td.getBoundingClientRect().width);
  const tip = (page: Page) => page.locator("gt-table .gt-i-cell-tip");
  // (Its widths fixed, which WebKit may do a frame after it's ready)
  const capped = async (page: Page) => {
    const errors = await ready(page, "display-caps.html");
    await expect(page.locator("gt-table table")).toHaveCSS("table-layout", "fixed");
    return errors;
  };

  test("fit a column to the text of all but the longest tenth of its cells", async ({ page }) => {
    const errors = await capped(page);
    expect(await cut(page, 19, "title")).toBe(true);
    expect(await cut(page, 20, "title")).toBe(true);
    for (const row of [1, 10, 18]) {
      expect(await cut(page, row, "title")).toBe(false);
    }
    // (Its cells' text ending in an ellipsis, in a fixed layout)
    expect(await cell(page, 20, "title").evaluate((td) => getComputedStyle(td).textOverflow)).toBe("ellipsis");
    expect(await page.locator("gt-table table").evaluate((table) => table.style.tableLayout)).toBe("fixed");
    // Its handle has its width
    const handle = page.locator("th#cp-title .gt-i-resizer");
    expect(Number(await handle.getAttribute("aria-valuenow"))).toBeCloseTo(await width(page, 1, "title"), -0.5);
    expect(errors).toEqual([]);
  });

  test("keep a column whose text is all about as long, and labels, whole", async ({ page }) => {
    const errors = await capped(page);
    expect(await cut(page, 1, "code")).toBe(false);
    expect(await cut(page, 1, "wide")).toBe(false);
    // (The label is wider than the code)
    const label = await page.locator("th#cp-code").evaluate((th) => th.scrollWidth <= th.clientWidth);
    expect(label).toBe(true);
    // A column showing images is as wide as they are
    expect(await width(page, 1, "picture")).toBeGreaterThanOrEqual(400);
    expect(errors).toEqual([]);
  });

  test("give a column no more than 20em", async ({ page }) => {
    const errors = await capped(page);
    // (title's longest tenth has 40 characters and more; at 16px, what's kept is under 20em)
    expect(await width(page, 1, "title")).toBeLessThanOrEqual(320);
    expect(errors).toEqual([]);
  });

  test("give a profile no more than 12em of its own", async ({ page }) => {
    const errors = await capped(page);
    const profile = page.locator("th#cp-wide .gt-i-profile");
    const { profileWidth, fontSize } = await profile.evaluate((el) => ({
      profileWidth: el.getBoundingClientRect().width,
      fontSize: parseFloat(getComputedStyle(el).fontSize),
    }));
    expect(await width(page, 1, "wide")).toBeGreaterThan(12 * fontSize + 20);
    expect(profileWidth).toBeCloseTo(12 * fontSize, 0);
    expect(errors).toEqual([]);
  });

  test("show a cut cell's text in a tooltip, a moment after the mouse goes onto it", async ({ page }) => {
    const errors = await capped(page);
    await cell(page, 20, "title").hover();
    await expect(tip(page)).toBeVisible();
    await expect(tip(page)).toHaveText("A title of forty characters, or so, here");
    // (Under the cell)
    const box = await cell(page, 20, "title").boundingBox();
    expect((await tip(page).boundingBox())?.y).toBeGreaterThan((box?.y ?? 0) + (box?.height ?? 0));
    // Not for a cell that isn't cut
    await cell(page, 1, "title").hover();
    await expect(tip(page)).toBeHidden();
    await page.waitForTimeout(700);
    await expect(tip(page)).toBeHidden();
    // Up to 150 characters of it
    await cell(page, 19, "title").hover();
    await expect(tip(page)).toBeVisible();
    const text = (await tip(page).textContent()) ?? "";
    expect(text.endsWith("…")).toBe(true);
    expect(text.slice(0, -1)).toBe(Array(12).fill("a very long title").join(" ").slice(0, 150).trimEnd());
    // Escape hides it
    await page.keyboard.press("Escape");
    await expect(tip(page)).toBeHidden();
    expect(errors).toEqual([]);
  });

  test.describe("on a touch screen", () => {
    test.use({ hasTouch: true, isMobile: true });

    test("show a cut cell's text in a tooltip as it's tapped, till it's tapped again", async ({ page }) => {
      const errors = await capped(page);
      await cell(page, 20, "title").tap();
      await expect(tip(page)).toHaveText("A title of forty characters, or so, here");
      await cell(page, 20, "title").tap();
      await expect(tip(page)).toBeHidden();
      // (And till another cell is)
      await cell(page, 20, "title").tap();
      await expect(tip(page)).toBeVisible();
      await cell(page, 1, "title").tap();
      await expect(tip(page)).toBeHidden();
      expect(errors).toEqual([]);
    });
  });
});
