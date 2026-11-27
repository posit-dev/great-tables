import { expect, type Page, test } from "@playwright/test";
import { join } from "node:path";
import { dataRows, fixtures, groupCells, open, ready, shown, striping, visible } from "./helpers";

// exibble, shown as group grp_b (rows 4-7) then grp_a (rows 0-3), each with a summary row, then a
// grand summary row; 3 rows to a page, so pages hold rows 4-6, then 7, 0 and 1, then 2 and 3.

const PAGE_1 = ["group:grp_b", 4, 5, 6, "grand:Max"];
const PAGE_2 = ["group:grp_b", 7, "summary:Total", "group:grp_a", 0, 1, "grand:Max"];
const PAGE_3 = ["group:grp_a", 2, 3, "summary:Total", "grand:Max"];

const pager = (page: Page) => page.locator("gt-table nav.gt-i-pager");
const pageButton = (page: Page, name: string) => pager(page).getByRole("button", { name, exact: true });
const info = (page: Page) => page.locator("gt-table .gt-i-page-info");
const live = (page: Page) => page.locator("gt-table .gt-i-live");
const gtTable = (page: Page) => page.locator("gt-table");

/** The width of each column (from the column labels) and of the table. */
function widths(page: Page): Promise<{ columns: number[]; table: number }> {
  return gtTable(page).evaluate((node) => {
    const table = node.querySelector("table") as HTMLElement;
    const labels = Array.from(table.querySelectorAll(".gt_col_headings > th"));
    return {
      columns: labels.map((th) => th.getBoundingClientRect().width),
      table: table.getBoundingClientRect().width,
    };
  });
}

/** The widths the table has with every row shown and no widths of ours, as GT laid it out. */
function naturalWidths(page: Page): Promise<{ columns: number[]; table: number }> {
  return gtTable(page).evaluate((node) => {
    const el = node as any;
    const table = node.querySelector("table") as HTMLElement;
    const size = el.pageSize;
    el.pageSize = null;
    const colgroup = table.querySelector("colgroup.gt-i-widths");
    colgroup?.remove();
    const minWidth = table.style.minWidth;
    table.style.minWidth = "";
    const labels = Array.from(table.querySelectorAll(".gt_col_headings > th"));
    const result = {
      columns: labels.map((th) => th.getBoundingClientRect().width),
      table: table.getBoundingClientRect().width,
    };
    if (colgroup) {
      table.prepend(colgroup);
    }
    table.style.minWidth = minWidth;
    el.pageSize = size;
    return result;
  });
}

function expectClose(actual: number[], expected: number[], within = 0.5) {
  expect(actual).toHaveLength(expected.length);
  actual.forEach((value, i) => {
    expect(Math.abs(value - (expected[i] as number))).toBeLessThanOrEqual(within);
  });
}

test("splits the rows into pages, repeating group headings and grand summary rows", async ({ page }) => {
  const errors = await ready(page, "pages.html");
  const all = await shown(page);

  expect(await visible(page)).toEqual(PAGE_1);
  await expect(info(page)).toHaveText("1–3 of 8 rows");
  await expect(pageButton(page, "Page 1")).toHaveAttribute("aria-current", "page");

  await pageButton(page, "Next").click();
  await expect(live(page)).toHaveText("Page 2 of 3");
  expect(await visible(page)).toEqual(PAGE_2);
  await expect(info(page)).toHaveText("4–6 of 8 rows");

  await pageButton(page, "Page 3").click();
  expect(await visible(page)).toEqual(PAGE_3);
  await expect(pageButton(page, "Next")).toHaveAttribute("aria-disabled", "true");
  // Every row stays in the table
  expect(await shown(page)).toEqual(all);
  expect(errors).toEqual([]);
});

test("keeps the column widths from page to page", async ({ page }) => {
  const errors = await ready(page, "pages.html");
  const natural = await naturalWidths(page);

  for (const target of ["Page 1", "Page 2", "Page 3"]) {
    await pageButton(page, target).click();
    const now = await widths(page);
    expectClose(now.columns, natural.columns);
    expect(Math.abs(now.table - natural.table)).toBeLessThanOrEqual(2);
  }
  // And while searching
  await page.locator("gt-table input.gt-i-search").fill("fig");
  await expect(info(page)).toHaveText("1 of 1 row (filtered from 8)");
  expectClose((await widths(page)).columns, natural.columns);
  expect(errors).toEqual([]);
});

test("measures the column widths again when the page is narrower", async ({ page }) => {
  const errors = await ready(page, "pages.html");
  await page.setViewportSize({ width: 420, height: 800 });
  // (Measured in the next frame)
  await expect
    .poll(async () => {
      const natural = await naturalWidths(page);
      const now = await widths(page);
      return Math.max(...now.columns.map((width, i) => Math.abs(width - (natural.columns[i] as number))));
    })
    .toBeLessThanOrEqual(0.5);
  await pageButton(page, "Page 3").click();
  expectClose((await widths(page)).columns, (await naturalWidths(page)).columns);
  expect(errors).toEqual([]);
});

test("keeps the column widths the author set, and fixes the others", async ({ page }) => {
  const errors = await ready(page, "pages-widths.html");
  const before = await widths(page);
  const cols = () =>
    page.locator("gt-table colgroup col").evaluateAll((all) => all.map((col) => (col as HTMLElement).style.width));
  await expect(page.locator("gt-table colgroup")).toHaveCount(1);
  expect((await cols())[2]).toBe("180px");
  expect((await cols()).every((width) => width.endsWith("px"))).toBe(true);

  for (const target of ["Page 2", "Page 3"]) {
    await pageButton(page, target).click();
    expectClose((await widths(page)).columns, before.columns);
  }
  expect((await cols())[2]).toBe("180px");
  expect(errors).toEqual([]);
});

test("pages a table with the rows past its first page hidden in its HTML as any other", async ({ page }) => {
  await ready(page, "pages.html");
  const all = await shown(page);
  const before = await widths(page);

  // (As a table of more than 3,000 rows has them)
  const errors = await open(page, "pages-hidden.html");
  await expect(gtTable(page)).toHaveAttribute("data-gti-state", "ready");
  expect(await visible(page)).toEqual(PAGE_1);
  expect(await shown(page)).toEqual(all);
  const now = await widths(page);
  expectClose(now.columns, before.columns);
  expect(Math.abs(now.table - before.table)).toBeLessThanOrEqual(2);

  await pageButton(page, "Next").click();
  expect(await visible(page)).toEqual(PAGE_2);
  await pageButton(page, "Page 3").click();
  expect(await visible(page)).toEqual(PAGE_3);
  await page.locator("gt-table input.gt-i-search").fill("a");
  await expect(info(page)).toHaveText("1–3 of 4 rows (filtered from 8)");
  expect(await visible(page)).toEqual(["group:grp_b", 6, "summary:Total", "group:grp_a", 0, 1, "grand:Max"]);
  await page.locator("th#p-char button.gt-i-sort").click();
  await expect(pageButton(page, "Page 1")).toHaveAttribute("aria-current", "page");
  expect(errors).toEqual([]);
});

/**
 * Open the page with the rows in a file beside it, served (as a page opened from a file can't fetch
 * another), with the file held till `release()`, or not found; returning the errors it logs.
 */
async function openAsset(page: Page, found = true): Promise<{ errors: string[]; warnings: string[]; release: () => void }> {
  let release = () => {};
  const held = new Promise<void>((resolve) => (release = resolve));
  await page.route("http://gti.test/**", async (route) => {
    const name = new URL(route.request().url()).pathname.slice(1);
    if (!name.endsWith(".gti.json")) {
      await route.fulfill({ path: join(fixtures, name) });
      return;
    }
    await held;
    await (found ? route.fulfill({ path: join(fixtures, name) }) : route.fulfill({ status: 404, body: "" }));
  });
  const errors: string[] = [];
  const warnings: string[] = [];
  // (Not the loop Safari reports when the table, measured again as the rows come, is laid out
  // again in the frame its observer sees it change)
  const error = (text: string) => {
    if (!text.startsWith("ResizeObserver loop")) {
      errors.push(text);
    }
  };
  page.on("pageerror", (err) => error(err.message));
  page.on("console", (msg) => {
    if (msg.type() === "error") {
      error(msg.text());
    } else if (msg.type() === "warning") {
      warnings.push(msg.text());
    }
  });
  await page.goto("http://gti.test/pages-asset.html");
  await expect(gtTable(page)).toHaveAttribute("data-gti-state", "ready");
  return { errors, warnings, release };
}

test("pages a table with the rows past its first page in a file beside it, once they've come", async ({ page }) => {
  await ready(page, "pages.html");
  const all = await shown(page);

  const { errors, release } = await openAsset(page);
  await expect(gtTable(page)).toHaveAttribute("aria-busy", "true");
  await expect(info(page)).toHaveText("Loading rows…");
  expect(await visible(page)).toEqual(PAGE_1);
  release();
  await expect(gtTable(page)).not.toHaveAttribute("aria-busy");
  await expect(info(page)).toHaveText("1–3 of 8 rows");
  expect(await shown(page)).toEqual(all);

  await pageButton(page, "Next").click();
  expect(await visible(page)).toEqual(PAGE_2);
  await page.locator("gt-table input.gt-i-search").fill("a");
  await expect(info(page)).toHaveText("1–3 of 4 rows (filtered from 8)");
  expect(await visible(page)).toEqual(["group:grp_b", 6, "summary:Total", "group:grp_a", 0, 1, "grand:Max"]);
  expect(errors).toEqual([]);
});

test("has only the first page if the file with the other rows doesn't come", async ({ page }) => {
  const { errors, warnings, release } = await openAsset(page, false);
  release();
  await expect(gtTable(page)).not.toHaveAttribute("aria-busy");
  await expect(info(page)).toHaveText("1–3 of 3 rows");
  // (Group grp_b's rows past them left out, so its summary row is shown, after its last)
  expect(await visible(page)).toEqual(["group:grp_b", 4, 5, 6, "summary:Total", "grand:Max"]);
  await expect(pager(page).getByRole("button", { name: "Next" })).toHaveAttribute("aria-disabled", "true");
  expect(warnings.some((text) => text.includes("pages-asset.gti.json are left out"))).toBe(true);
  expect(errors.filter((text) => !text.includes("404"))).toEqual([]);
});

test("shows the rows hidden in its HTML when it has every row on one page", async ({ page }) => {
  // (The page size set to none before the table is hydrated, as a reader's view kept in the URL
  // can have it)
  const errors = await ready(page, "pages-hidden-all.html");
  expect(await visible(page)).toEqual(await shown(page));
  expect(dataRows(await visible(page))).toHaveLength(8);
  await expect(page.locator("tbody.gt_table_body > tr[hidden]")).toHaveCount(0);
  expect(errors).toEqual([]);
});

test("fits the columns of a table of more than 1,000 rows to every row, from the rows that set their widths", async ({ page }) => {
  const errors = await ready(page, "pages-many.html");
  const before = await widths(page);
  expectClose(before.columns, (await naturalWidths(page)).columns, 1);

  // (The longest name, in row 700, and the longest note, in row 1,100)
  for (const text of ["A much longer name", "by far"]) {
    await page.locator("gt-table input.gt-i-search").fill(text);
    await expect(info(page)).toHaveText("1 of 1 row (filtered from 1200)");
    await expect(page.locator("gt-table tbody > tr:not([hidden])").first()).toContainText(text);
    expectClose((await widths(page)).columns, before.columns);
    const cut = await page.locator("gt-table tbody > tr:not([hidden]) > td").evaluateAll((cells) => cells.filter((td) => td.scrollWidth > td.clientWidth + 1).length);
    expect(cut).toBe(0);
  }
  expect(errors).toEqual([]);
});

test("caps the columns of a table of more than 1,000 rows without text wrapping by all their text", async ({ page }) => {
  const errors = await ready(page, "pages-many-nowrap.html");
  const before = await widths(page);

  // (The longest name and the longest note are cut, as they're fewer than a tenth of them)
  for (const [text, column] of [["A much longer name", 0], ["by far", 2]] as const) {
    await page.locator("gt-table input.gt-i-search").fill(text);
    await expect(info(page)).toHaveText("1 of 1 row (filtered from 1200)");
    await expect(page.locator("gt-table tbody > tr:not([hidden])").first()).toContainText(text);
    expectClose((await widths(page)).columns, before.columns);
    const cell = page.locator("gt-table tbody > tr:not([hidden]) > td").nth(column);
    expect(await cell.evaluate((td) => td.scrollWidth > td.clientWidth)).toBe(true);
  }
  expect(errors).toEqual([]);
});

test("pages the rows that match a search, from the first page", async ({ page }) => {
  const errors = await ready(page, "pages.html");
  await pageButton(page, "Page 2").click();

  // "a": rows 0, 1, 3 and 6
  await page.locator("gt-table input.gt-i-search").fill("a");
  await expect(info(page)).toHaveText("1–3 of 4 rows (filtered from 8)");
  expect(await visible(page)).toEqual(["group:grp_b", 6, "summary:Total", "group:grp_a", 0, 1, "grand:Max"]);
  await pageButton(page, "Page 2").click();
  expect(await visible(page)).toEqual(["group:grp_a", 3, "summary:Total", "grand:Max"]);

  // A new sort goes back to the first page too
  await page.locator("th#p-char button.gt-i-sort").click();
  await expect(pageButton(page, "Page 1")).toHaveAttribute("aria-current", "page");
  expect(errors).toEqual([]);
});

test("restripes each page", async ({ page }) => {
  const errors = await ready(page, "pages.html");
  const before = await striping(page);
  await pageButton(page, "Page 2").click();
  const after = await striping(page);
  expect(after.map((row) => row.striped)).toEqual([false, true, false]);
  expect(after.map((row) => row.background)).toEqual(before.map((row) => row.background));
  expect(errors).toEqual([]);
});

test("spans each group's label cell over its rows on the page when groups are a column", async ({
  page,
}) => {
  const errors = await ready(page, "pages-column.html");
  const summary = (group: string) => ({ summary: "Total", group, side: "bottom" });

  expect(await groupCells(page)).toEqual([{ label: "grp_b", row: 4, first: true, last: 6, fits: true }]);
  await pageButton(page, "Next").click();
  expect(await groupCells(page)).toEqual([
    { label: "grp_b", row: 7, first: true, last: summary("grp_b"), fits: true },
    { label: "grp_a", row: 0, first: true, last: 1, fits: true },
  ]);
  await pageButton(page, "Next").click();
  expect(await groupCells(page)).toEqual([
    { label: "grp_a", row: 2, first: true, last: summary("grp_a"), fits: true },
  ]);
  expect(errors).toEqual([]);
});

test("pages from the keyboard", async ({ page }) => {
  const errors = await ready(page, "pages.html");
  await page.evaluate(() => {
    (window as any).pages = [];
    document.addEventListener("gt-table-page", (event) => {
      (window as any).pages.push((event as CustomEvent).detail);
    });
  });

  await pageButton(page, "Next").focus();
  await page.keyboard.press("Enter");
  await expect(info(page)).toHaveText("4–6 of 8 rows");
  await page.keyboard.press("PageDown");
  await expect(info(page)).toHaveText("7–8 of 8 rows");
  // Next is now unavailable, but keeps focus
  await expect(pageButton(page, "Next")).toBeFocused();
  await expect(pageButton(page, "Next")).toHaveAttribute("aria-disabled", "true");
  await page.keyboard.press("PageUp");
  await expect(info(page)).toHaveText("4–6 of 8 rows");

  // A page number keeps focus as the numbers change
  await pageButton(page, "Page 3").focus();
  await page.keyboard.press("Space");
  await expect(pageButton(page, "Page 3")).toBeFocused();

  expect(await page.evaluate(() => (window as any).pages)).toEqual([
    { page: 2, pageSize: 3, pageCount: 3 },
    { page: 3, pageSize: 3, pageCount: 3 },
    { page: 2, pageSize: 3, pageCount: 3 },
    { page: 3, pageSize: 3, pageCount: 3 },
  ]);
  expect(errors).toEqual([]);
});

test("changes the page size, keeping the first row of the page in view", async ({ page }) => {
  const errors = await ready(page, "pages.html");
  await pageButton(page, "Page 2").click();

  await pager(page).getByLabel("Rows per page").selectOption("5");
  await expect(live(page)).toHaveText("5 rows per page, page 1 of 2");
  expect(await visible(page)).toEqual(["group:grp_b", 4, 5, 6, 7, "summary:Total", "group:grp_a", 0, "grand:Max"]);
  await pageButton(page, "Page 2").click();
  await expect(info(page)).toHaveText("6–8 of 8 rows");
  expect(errors).toEqual([]);
});

test("goes to the page typed in", async ({ page }) => {
  const errors = await ready(page, "pages-jump.html");
  const input = pager(page).getByRole("textbox", { name: /Page/ });
  await expect(input).toHaveValue("1");

  await input.fill("3");
  await input.press("Enter");
  expect(await visible(page)).toEqual(PAGE_3);
  await input.fill("x");
  await input.blur();
  await expect(input).toHaveValue("3");
  expect(errors).toEqual([]);
});

test("lines up below the table, in its font", async ({ page }) => {
  const errors = await ready(page, "pages.html");
  const boxes = await gtTable(page).evaluate((node) => {
    const table = node.querySelector("table") as HTMLElement;
    const nav = node.querySelector("nav.gt-i-pager") as HTMLElement;
    const pages = nav.querySelector(".gt-i-pages") as HTMLElement;
    return {
      table: table.getBoundingClientRect().toJSON(),
      nav: nav.getBoundingClientRect().toJSON(),
      pages: pages.getBoundingClientRect().toJSON(),
      fonts: [getComputedStyle(table).fontFamily, getComputedStyle(nav).fontFamily],
    };
  });
  expect(boxes.nav.left).toBeCloseTo(boxes.table.left, 0);
  expect(boxes.nav.width).toBeCloseTo(boxes.table.width, 0);
  expect(boxes.pages.right).toBeCloseTo(boxes.table.right, 0);
  expect(boxes.nav.top).toBeGreaterThanOrEqual(boxes.table.bottom);
  expect(boxes.fonts[1]).toBe(boxes.fonts[0]);
  expect(errors).toEqual([]);
});

test.describe("on a touch screen", () => {
  test.use({ hasTouch: true, isMobile: true });

  test("the page controls are big enough to tap", async ({ page }) => {
    const errors = await ready(page, "pages.html");
    const sizes = await pager(page).evaluate((nav) =>
      Array.from(nav.querySelectorAll("button, select"), (control) => {
        const box = control.getBoundingClientRect();
        return Math.min(box.width, box.height);
      }),
    );
    expect(sizes.length).toBeGreaterThan(0);
    for (const size of sizes) {
      expect(size).toBeGreaterThanOrEqual(44);
    }

    await pageButton(page, "Next").tap();
    expect(await visible(page)).toEqual(PAGE_2);
    expect(errors).toEqual([]);
  });
});
