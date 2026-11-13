import { expect, type Page, test } from "@playwright/test";
import { dataRows, groupCells, ready, shown, striping, tab } from "./helpers";

// exibble, shown as group grp_b (rows 4-7) then grp_a (rows 0-3), each with a summary row, then a
// grand summary row. `num` is missing in row 5 and `char` in row 4.
const UNSORTED = [
  "group:grp_b", 4, 5, 6, 7, "summary:Total",
  "group:grp_a", 0, 1, 2, 3, "summary:Total",
  "grand:Max",
];

const sortButton = (page: Page, column: string) => page.locator(`th#s-${column} button.gt-i-sort`);

test("sorts within groups when a column label is clicked", async ({ page }) => {
  const errors = await ready(page, "sort.html");
  const th = page.locator("th#s-num");
  const live = page.locator("gt-table .gt-i-live");
  expect(await shown(page)).toEqual(UNSORTED);
  const totals = await page.locator("tr:has(.gt_summary_row)").allTextContents();

  await sortButton(page, "num").click();
  expect(await shown(page)).toEqual([
    "group:grp_b", 4, 6, 7, 5, "summary:Total",
    "group:grp_a", 0, 1, 2, 3, "summary:Total",
    "grand:Max",
  ]);
  await expect(th).toHaveAttribute("aria-sort", "ascending");
  await expect(live).toHaveText("Sorted by num, ascending");

  await sortButton(page, "num").click();
  expect(dataRows(await shown(page))).toEqual([7, 6, 4, 5, 3, 2, 1, 0]);
  await expect(th).toHaveAttribute("aria-sort", "descending");

  await sortButton(page, "num").click();
  expect(await shown(page)).toEqual(UNSORTED);
  await expect(th).not.toHaveAttribute("aria-sort");
  await expect(live).toHaveText("Not sorted");

  // The summary rows weren't touched
  expect(await page.locator("tr:has(.gt_summary_row)").allTextContents()).toEqual(totals);
  expect(errors).toEqual([]);
});

test("sorts by several columns with Shift-click", async ({ page }) => {
  const errors = await ready(page, "sort.html");

  await sortButton(page, "char").click();
  expect(dataRows(await shown(page))).toEqual([5, 6, 7, 4, 0, 1, 2, 3]);
  await sortButton(page, "num").click({ modifiers: ["Shift"] });

  const sort = await page.locator("gt-table").evaluate((node) => (node as any).sort);
  expect(sort).toEqual([
    { column: "char", descending: false },
    { column: "num", descending: false },
  ]);
  await expect(page.locator("th#s-char")).toHaveAttribute("aria-sort", "ascending");
  await expect(page.locator("th#s-num")).not.toHaveAttribute("aria-sort");
  await expect(page.locator("th#s-num")).toHaveAttribute("data-gti-sort", "ascending");
  await expect(page.locator("th#s-num .gt-i-sort-icon")).toHaveAttribute("data-gti-sort-index", "2");

  // Shift-click doesn't select text
  expect(await page.evaluate(() => String(getSelection()))).toBe("");
  expect(errors).toEqual([]);
});

test("sorts from the keyboard", async ({ page }) => {
  const errors = await ready(page, "sort.html");

  await sortButton(page, "num").focus();
  await page.keyboard.press("Enter");
  await expect(page.locator("th#s-num")).toHaveAttribute("aria-sort", "ascending");
  await page.keyboard.press("Space");
  await expect(page.locator("th#s-num")).toHaveAttribute("aria-sort", "descending");

  // The next column label is the next stop, and Shift extends the sort from the keyboard too
  await tab(page);
  await expect(sortButton(page, "char")).toBeFocused();
  await page.keyboard.press("Shift+Enter");
  const sort = await page.locator("gt-table").evaluate((node) => (node as any).sort);
  expect(sort).toEqual([
    { column: "num", descending: true },
    { column: "char", descending: false },
  ]);
  expect(errors).toEqual([]);
});

test("fires an event when the reader sorts", async ({ page }) => {
  const errors = await ready(page, "sort.html");
  await page.evaluate(() => {
    (window as any).sorts = [];
    document.addEventListener("gt-table-sort", (event) => {
      (window as any).sorts.push((event as CustomEvent).detail.sort);
    });
  });

  await sortButton(page, "currency").click();
  await page.locator("gt-table").evaluate((node) => {
    (node as any).sort = [{ column: "num" }];
  });
  expect(await page.evaluate(() => (window as any).sorts)).toEqual([
    [{ column: "currency", descending: false }],
  ]);
  expect(errors).toEqual([]);
});

test("restripes the rows after sorting", async ({ page }) => {
  const errors = await ready(page, "sort.html");
  const expected = (rows: { striped: boolean }[]) => rows.map((_, j) => j % 2 === 1);

  const before = await striping(page);
  expect(before.map((row) => row.striped)).toEqual(expected(before));
  // Ascending, then descending
  for (let i = 0; i < 2; i++) {
    await sortButton(page, "num").click();
    const after = await striping(page);
    expect(after.map((row) => row.striped)).toEqual(expected(after));
    // The stripes still look like stripes
    expect(after.map((row) => row.background)).toEqual(before.map((row) => row.background));
  }
  expect(new Set(before.map((row) => row.background)).size).toBe(2);
  expect(errors).toEqual([]);
});

test("keeps each group's label cell on its first row when groups are a column", async ({ page }) => {
  const errors = await ready(page, "sort-column.html");
  await sortButton(page, "num").click();
  await sortButton(page, "num").click();

  expect(await groupCells(page)).toEqual([
    { label: "grp_b", row: 7, first: true, last: { summary: "Total", group: "grp_b", side: "bottom" }, fits: true },
    { label: "grp_a", row: 3, first: true, last: { summary: "Total", group: "grp_a", side: "bottom" }, fits: true },
  ]);
  await expect(page.locator("tr.gt_row_group_first")).toHaveCount(2);
  expect(errors).toEqual([]);
});

test("keeps groups shown as a column apart when nothing is between them", async ({ page }) => {
  const errors = await ready(page, "sort-column-bare.html");
  await sortButton(page, "num").click();

  expect(await shown(page)).toEqual([4, 6, 7, 5, 0, 1, 2, 3]);
  expect(await groupCells(page)).toEqual([
    { label: "grp_b", row: 4, first: true, last: 5, fits: true },
    { label: "grp_a", row: 0, first: true, last: 3, fits: true },
  ]);
  expect(errors).toEqual([]);
});

test("column labels stay as GT has them, with their controls lined up under them", async ({ page }) => {
  const errors = await ready(page, "sort.html");
  const th = page.locator("th#s-num");
  // The label isn't in a button, and the row of controls is under it, as wide as the cell
  expect(await th.evaluate((th) => th.querySelector("button")?.closest(".gt-i-head-controls") !== null)).toBe(true);
  await expect(th).toHaveCSS("cursor", "pointer");
  const rows = await page.locator("thead .gt-i-head-controls").evaluateAll((rows) =>
    rows.map((row) => {
      const box = row.getBoundingClientRect();
      return { top: box.top, height: box.height };
    }),
  );
  expect(rows.length).toBeGreaterThan(1);
  expect(new Set(rows.map((row) => row.top)).size).toBe(1);
  expect(new Set(rows.map((row) => row.height)).size).toBe(1);

  const button = await sortButton(page, "num").evaluate((button) => {
    const b = getComputedStyle(button);
    return { background: b.backgroundColor, border: b.borderTopWidth, cursor: b.cursor };
  });
  expect(button).toEqual({ background: "rgba(0, 0, 0, 0)", border: "0px", cursor: "pointer" });

  // Both arrows faint while it isn't sorted; the way it's sorted, dark, hovered or not
  const up = th.locator(".gt-i-sort-up");
  const down = th.locator(".gt-i-sort-down");
  await expect(up).toHaveCSS("opacity", "0.35");
  await expect(down).toHaveCSS("opacity", "0.35");
  await sortButton(page, "num").hover();
  await expect(up).toHaveCSS("opacity", "0.6");
  await sortButton(page, "num").click();
  await expect(up).toHaveCSS("opacity", "1");
  await expect(down).toHaveCSS("opacity", "0.2");
  await page.mouse.move(0, 0);
  await expect(up).toHaveCSS("opacity", "1");
  await sortButton(page, "num").click();
  await expect(up).toHaveCSS("opacity", "0.2");
  await expect(down).toHaveCSS("opacity", "1");
  expect(errors).toEqual([]);
});

test("the line over the labels' controls is one, on a page that sizes boxes, which has no more to scroll", async ({
  page,
}) => {
  const errors = await ready(page, "sort-page-styles.html");
  // Each label's row (the stubhead's empty one too) as tall as the others, so that their lines,
  // solid and as wide as their cells, are at one height and join
  const rows = await page.locator("thead .gt-i-head-controls").evaluateAll((rows) =>
    rows.map((row) => {
      const box = row.getBoundingClientRect();
      const cell = row.parentElement!.getBoundingClientRect();
      const line = getComputedStyle(row, "::before");
      return {
        empty: row.childElementCount === 0,
        top: box.top,
        height: box.height,
        style: line.borderTopStyle,
        left: cell.left,
        right: cell.right,
      };
    }),
  );
  expect(rows.some((row) => row.empty)).toBe(true);
  expect(new Set(rows.map((row) => row.top)).size).toBe(1);
  expect(new Set(rows.map((row) => row.height)).size).toBe(1);
  expect(new Set(rows.map((row) => row.style))).toEqual(new Set(["solid"]));
  for (let i = 1; i < rows.length; i++) {
    expect(rows[i]!.left).toBeCloseTo(rows[i - 1]!.right, 0);
  }
  // The container around the table has nothing to scroll (not the announcements' box, under it)
  const container = await page.locator("body > div").evaluate((div) => ({
    scroll: div.scrollHeight,
    client: div.clientHeight,
  }));
  expect(container.scroll).toBe(container.client);
  expect(errors).toEqual([]);
});

test("sorts when the label itself is clicked, but not when its text is selected", async ({ page }) => {
  const errors = await ready(page, "sort.html");
  const th = page.locator("th#s-num");
  const box = (await th.boundingBox())!;
  // (A drag across the label's text selects it)
  await page.mouse.move(box.x + 4, box.y + 6);
  await page.mouse.down();
  await page.mouse.move(box.x + box.width - 4, box.y + 6, { steps: 4 });
  await page.mouse.up();
  await expect(th).not.toHaveAttribute("aria-sort");

  await page.evaluate(() => document.getSelection()?.removeAllRanges());
  await th.click({ position: { x: 6, y: 6 } });
  await expect(th).toHaveAttribute("aria-sort", "ascending");
  expect(errors).toEqual([]);
});

test.describe("on a touch screen", () => {
  test.use({ hasTouch: true, isMobile: true });

  test("column labels are big enough to tap", async ({ page }) => {
    const errors = await ready(page, "sort.html");
    const target = await sortButton(page, "num").evaluate((button) => {
      const style = getComputedStyle(button, "::before");
      return { width: parseFloat(style.width), height: parseFloat(style.height) };
    });
    expect(target.width).toBeGreaterThanOrEqual(44);
    expect(target.height).toBeGreaterThanOrEqual(44);
    // The sort's arrows show without hovering
    await expect(page.locator("th#s-num .gt-i-sort-up")).toHaveCSS("opacity", "0.35");

    await sortButton(page, "num").tap();
    await expect(page.locator("th#s-num")).toHaveAttribute("aria-sort", "ascending");
    expect(errors).toEqual([]);
  });
});
