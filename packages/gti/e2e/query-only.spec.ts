import { readFile } from "node:fs/promises";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { expect, type Page, test } from "@playwright/test";
import { dataRows, ready, visible } from "./helpers";

// Columns only for querying, in a GTI table of exibble three times over (24 rows, in two groups):
// `fctr` (shown in upper case, with a facet filter), `date` (with a text filter) and `currency`
// (with a range filter), labelled "Factor", "Day" and "Price", are left out of the table with
// `display=False`. The rows a view keeps, and its code, should be what Python's `view_rows()` and
// `query_code()` have for it, as make_fixtures.py has them (in query-only-cases.json).

type Backend = "polars" | "pandas" | "narwhals";
interface Case {
  filter: object | null;
  sort: object[];
  rows: number[];
  code: Record<Backend, string>;
}

const FIXTURES = join(dirname(fileURLToPath(import.meta.url)), ".fixtures");
const CASES: Case[] = JSON.parse(readFileSync(join(FIXTURES, "query-only-cases.json"), "utf-8"));
const BACKENDS: Backend[] = ["polars", "pandas", "narwhals"];

const el = (page: Page) => page.locator("gt-table");
const bar = (page: Page) => el(page).locator(".gt-i-bar");
const labels = (page: Page) => el(page).locator("thead th");
const toggle = (page: Page) => el(page).getByRole("button", { name: "Edit the filters as text" });
const query = (page: Page) => el(page).getByRole("combobox", { name: "Filters as text" });
const options = (page: Page) => el(page).getByRole("listbox", { name: "Suggestions" }).getByRole("option");
const tokens = (page: Page) => el(page).getByRole("list", { name: "Filters" });
const texts = (page: Page) => tokens(page).locator(".gt-i-token-open");
const panel = (page: Page, column: string) => el(page).getByRole("group", { name: `Filter ${column}`, exact: true });
const matched = (page: Page) => el(page).evaluate((node) => (node as any).matchCount as number);
const exportPanel = (page: Page) => bar(page).getByRole("group", { name: "Export", exact: true });
const info = (page: Page) => bar(page).getByRole("group", { name: "Table info" });

// Apply a query, as text
async function filterBy(page: Page, text: string) {
  await toggle(page).click();
  await query(page).fill(text);
  await query(page).press("Enter");
  await expect(query(page)).toBeHidden();
}

test("leaves the columns out of the table, and out of a CSV", async ({ page }) => {
  const errors = await ready(page, "query-only.html");
  await expect(labels(page)).not.toHaveText([]);
  for (const label of ["Factor", "Day", "Price"]) {
    await expect(labels(page).filter({ hasText: label })).toHaveCount(0);
  }
  expect(await el(page).evaluate((node) => node.querySelectorAll("tbody td").length)).toBeGreaterThan(0);

  await bar(page).getByRole("button", { name: "Export the table", exact: true }).click();
  const [file] = await Promise.all([
    page.waitForEvent("download"),
    exportPanel(page).getByRole("button", { name: "Download CSV" }).click(),
  ]);
  const header = (await readFile(await file.path())).subarray(3).toString("utf-8").split("\r\n")[0]?.split(",");
  expect(header).toContain("num");
  for (const label of ["fctr", "date", "currency", "Factor", "Day", "Price"]) {
    expect(header).not.toContain(label);
  }
  expect(errors).toEqual([]);
});

test("filters by them from the query bar, by their labels", async ({ page }) => {
  const errors = await ready(page, "query-only.html");
  // (Suggested, with their labels, and the facet's values as the table would show them)
  await toggle(page).click();
  await query(page).fill("");
  await page.keyboard.type("Fa");
  await expect(options(page)).toHaveText([/^fctr\s*Factor$/]);
  await query(page).fill("fctr in (");
  await page.keyboard.type("O");
  await expect(options(page).first()).toContainText("ONE");
  await page.keyboard.press("Escape");
  await page.keyboard.press("Escape");

  await filterBy(page, 'fctr in ("one", "five") and currency >= 10');
  await expect(texts(page)).toHaveText(["Factor: FIVE, ONE", "Price ≥ 10"]);
  expect(await matched(page)).toBe(6);
  expect(dataRows(await visible(page)).sort((a, b) => Number(a) - Number(b))).toEqual([0, 4, 8, 12, 16, 20]);

  // (A token opens the filter's panel)
  await texts(page).first().click();
  await expect(panel(page, "Factor")).toBeVisible();
  await expect(panel(page, "Factor")).toContainText("ONE");
  expect(errors).toEqual([]);
});

test("keeps the rows view_rows() does, and writes the code query_code() does", async ({ page }) => {
  const errors = await ready(page, "query-only.html");
  expect(CASES.length).toBe(3);
  for (const { filter, sort, rows, code } of CASES) {
    const written = await el(page).evaluate(
      (node, [filter, sort, backends]) => {
        const table = node as any;
        table.filter = filter;
        table.sort = sort;
        return Object.fromEntries((backends as Backend[]).map((backend) => [backend, table.toCode(backend)]));
      },
      [filter, sort, BACKENDS] as const,
    );
    expect(written).toEqual(code);
    expect(await matched(page)).toBe(rows.length);
    const kept = dataRows(await visible(page));
    if (sort.length === 0) {
      expect(kept).toEqual(rows);
    } else {
      expect(kept.sort((a, b) => Number(a) - Number(b))).toEqual([...rows].sort((a, b) => a - b));
    }
  }
  expect(errors).toEqual([]);
});

test("doesn't search them", async ({ page }) => {
  const errors = await ready(page, "query-only.html");
  // ("may" is in the dates, and in no column shown)
  await el(page).evaluate((node) => {
    (node as any).search = "may";
  });
  expect(await matched(page)).toBe(0);
  expect(errors).toEqual([]);
});

test("sorts by them from the URL, by their labels", async ({ page }) => {
  const errors: string[] = [];
  page.on("pageerror", (err) => errors.push(err.message));
  await page.goto(`${pathToFileURL(join(FIXTURES, "query-only.html")).href}?q.sort=-currency`);
  await expect(el(page)).toHaveAttribute("data-gti-state", "ready");
  expect(await el(page).evaluate((node) => (node as any).sort)).toEqual([{ column: "currency", descending: true }]);

  await bar(page).getByRole("button", { name: "Table info", exact: true }).click();
  await expect(info(page)).toContainText("Sorted by Price, descending");
  // (No button to sort by them)
  await expect(el(page).getByRole("button", { name: "Sort by Price", exact: true })).toHaveCount(0);
  expect(errors).toEqual([]);
});
