import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { expect, type Page, test } from "@playwright/test";
import { allowClipboard, ready } from "./helpers";

// Export as code, from GTI tables of exibble (8 rows, in two groups), with a search, filters on
// `num`, `char`, `fctr` and `date`: of pandas data (code.html), and of Polars data with a view
// (code-polars.html). The code should be what Python's `query_code()` writes for the view,
// character for character, as make_fixtures.py has it (in code-cases.json).

type Backend = "polars" | "pandas" | "narwhals";
interface Case {
  filter: object | null;
  sort: object[];
  code: Record<Backend, string>;
}

const CASES: Record<"pandas" | "polars", Case[]> = JSON.parse(
  readFileSync(join(dirname(fileURLToPath(import.meta.url)), ".fixtures", "code-cases.json"), "utf-8"),
);
const BACKENDS: Backend[] = ["polars", "pandas", "narwhals"];

const el = (page: Page) => page.locator("gt-table");
const bar = (page: Page) => el(page).locator(".gt-i-bar");
const toggle = (page: Page) => bar(page).getByRole("button", { name: "Export the table", exact: true });
const panel = (page: Page) => bar(page).getByRole("group", { name: "Export", exact: true });
const status = (page: Page) => panel(page).locator(".gt-i-info-rows");
const library = (page: Page) => panel(page).getByRole("combobox", { name: "Code for" });
const copyCode = (page: Page) => panel(page).getByRole("button", { name: "Copy code", exact: true });
const note = (page: Page) => panel(page).getByText("The code leaves out the search.");

// The code for a view, for each library
const viewCode = (page: Page, { filter, sort }: Case) =>
  el(page).evaluate(
    (node, [filter, sort, backends]) => {
      const table = node as any;
      table.filter = filter;
      table.sort = sort;
      return Object.fromEntries((backends as Backend[]).map((backend) => [backend, table.toCode(backend)]));
    },
    [filter, sort, BACKENDS] as const,
  );

for (const [data, fixture] of [
  ["pandas", "code.html"],
  ["polars", "code-polars.html"],
] as const) {
  test(`writes the code query_code() does, for ${data} data`, async ({ page }) => {
    const errors = await ready(page, fixture);
    expect(CASES[data].length).toBeGreaterThan(4);
    for (const view of CASES[data]) {
      expect(await viewCode(page, view)).toEqual(view.code);
    }
    expect(errors).toEqual([]);
  });
}

test("copies the code of the view, for the library chosen", async ({ page, context, browserName }) => {
  await allowClipboard(context, browserName);
  const errors = await ready(page, "code-polars.html");
  await el(page).evaluate((node) => {
    (window as any).exports = [];
    node.addEventListener("gt-table-export", (event) => (window as any).exports.push((event as CustomEvent).detail));
  });
  const view = CASES.polars[1] as Case;
  await toggle(page).click();
  // (The data's library, to begin with)
  await expect(library(page)).toHaveValue("polars");
  for (const backend of ["polars", "narwhals", "pandas"] as const) {
    await library(page).selectOption(backend);
    await copyCode(page).click();
    await expect(status(page)).toHaveText("Copied the code");
    // (Once written: the status was already this, after the first)
    await expect.poll(() => page.evaluate(() => navigator.clipboard.readText())).toBe(view.code[backend]);
  }
  const fired = await page.evaluate(() => (window as any).exports);
  expect(fired.map((detail: { backend: string }) => detail.backend)).toEqual(["polars", "narwhals", "pandas"]);
  expect(fired[0]).toEqual({ format: "code", rows: [], code: view.code.polars, backend: "polars" });
  expect(errors).toEqual([]);
});

test("copies the code of the filters chosen, leaving out the search", async ({ page, context, browserName }) => {
  await allowClipboard(context, browserName);
  const errors = await ready(page, "code.html");
  // `fctr` in ("seven"), with the column's filter, after `num` <= 0.5 (the fourth case's view)
  await el(page).evaluate((node) => {
    (node as any).filter = { and: [{ col: "num", op: "lte", value: 0.5 }] };
  });
  const filterButton = el(page).locator("th", { hasText: "fctr" }).locator(".gt-i-filter-button");
  await filterButton.click();
  await page.getByRole("checkbox", { name: /^seven/ }).check();
  await page.keyboard.press("Escape");

  await bar(page).getByRole("button", { name: "Search the table" }).click();
  await page.keyboard.type("grape");
  await toggle(page).click();
  await expect(note(page)).toBeVisible();
  await expect(library(page)).toHaveValue("pandas");
  await copyCode(page).click();
  await expect(status(page)).toHaveText("Copied the code");
  expect(await page.evaluate(() => navigator.clipboard.readText())).toBe((CASES.pandas[3] as Case).code.pandas);

  await el(page).evaluate((node) => {
    (node as any).search = "";
  });
  await expect(note(page)).toBeHidden();
  expect(errors).toEqual([]);
});

test.describe("on a touch screen", () => {
  test.use({ hasTouch: true, isMobile: true });

  test("has controls big enough to tap", async ({ page }) => {
    const errors = await ready(page, "code.html");
    await toggle(page).tap();
    await expect(panel(page)).toBeVisible();
    for (const control of [library(page), copyCode(page)]) {
      const { height } = (await control.boundingBox()) ?? { height: 0 };
      expect(height).toBeGreaterThanOrEqual(44);
    }
    expect(errors).toEqual([]);
  });
});
