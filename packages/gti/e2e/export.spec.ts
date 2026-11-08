import { readFile } from "node:fs/promises";
import { expect, type Locator, type Page, test } from "@playwright/test";
import { allowClipboard, ready, tab } from "./helpers";

// Export from a GTI table: exibble three times over (24 rows, in two groups), with a spanner over
// `num` and `currency`, 5 rows to a page, whose rows can be selected; exported in every format, and
// downloaded as "exibble.csv" (or ".tsv", or ".json").

const el = (page: Page) => page.locator("gt-table");
const bar = (page: Page) => el(page).locator(".gt-i-bar");
const toggle = (page: Page) => bar(page).getByRole("button", { name: "Export the table", exact: true });
const panel = (page: Page) => bar(page).getByRole("group", { name: "Export", exact: true });
const status = (page: Page) => panel(page).locator(".gt-i-info-rows");
const box = (locator: Locator) =>
  locator.evaluate((node) => {
    const { left, right, top, bottom, height } = node.getBoundingClientRect();
    return { left, right, top, bottom, height };
  });

const HEADER = ",row,Numbers – num,Numbers – currency,char";

// The export events the table fires, as they happen
async function events(page: Page) {
  await el(page).evaluate((node) => {
    (window as any).exports = [];
    node.addEventListener("gt-table-export", (event) => (window as any).exports.push((event as CustomEvent).detail));
  });
  return () => page.evaluate(() => (window as any).exports);
}

// The file downloaded by clicking the panel's button for a format (CSV, by default), its name, and
// its lines (after a CSV's or TSV's byte order mark)
async function download(page: Page, format = "CSV") {
  const [file] = await Promise.all([
    page.waitForEvent("download"),
    panel(page).getByRole("button", { name: `Download ${format}` }).click(),
  ]);
  const bytes = await readFile(await file.path());
  const text = bytes.subarray(format === "JSON" ? 0 : 3).toString("utf-8");
  return { name: file.suggestedFilename(), bytes, text, lines: text.split(format === "CSV" ? "\r\n" : "\n").slice(0, -1) };
}

// What the clipboard has, by type
const clipboard = (page: Page) =>
  page.evaluate(async () => {
    const [item] = await navigator.clipboard.read();
    const entry: Record<string, string> = {};
    for (const type of item?.types ?? []) {
      entry[type] = await (await (item as ClipboardItem).getType(type)).text();
    }
    return entry;
  });

test("downloads every row as CSV, on every page, named as the author asked", async ({ page }) => {
  const errors = await ready(page, "export.html");
  const fired = await events(page);
  await toggle(page).click();
  await expect(panel(page)).toBeVisible();
  await expect(status(page)).toHaveText("24 rows");

  const { name, bytes, lines } = await download(page);
  expect(name).toBe("exibble.csv");
  // (After a byte order mark, so that spreadsheets read it as UTF-8)
  expect(Array.from(bytes.subarray(0, 3))).toEqual([0xef, 0xbb, 0xbf]);
  expect(lines).toHaveLength(25);
  expect(lines.slice(0, 3)).toEqual([
    HEADER,
    'grp_b,row_5,"5,550.00","$1,325.81",None',
    "grp_b,row_6,None,$13.26,fig",
  ]);
  expect(lines.filter((line) => line.startsWith("grp_a,"))).toHaveLength(12);
  await expect(status(page)).toHaveText("Downloaded 24 rows");
  await expect(panel(page)).toBeVisible();
  const [detail] = await fired();
  expect(detail.format).toBe("csv");
  expect(detail.rows).toHaveLength(24);
  expect(errors).toEqual([]);
});

test("downloads the rows sorted as shown, and those the search keeps", async ({ page }) => {
  const errors = await ready(page, "export.html");
  const sort = el(page).locator("button.gt-i-sort", { hasText: "num" });
  await sort.click();
  await sort.click();
  await toggle(page).click();
  const sorted = (await download(page)).lines;
  expect(sorted.slice(0, 5)).toEqual([
    HEADER,
    'grp_b,row_8,"8,880,000.00",$0.44,honeydew',
    'grp_b,row_16,"8,880,000.00",$0.44,honeydew',
    'grp_b,row_24,"8,880,000.00",$0.44,honeydew',
    'grp_b,row_7,"777,000.00",None,grapefruit',
  ]);

  await bar(page).getByRole("button", { name: "Search the table" }).click();
  await page.keyboard.type("grape");
  await expect(bar(page).locator(".gt-i-search-count")).toHaveText("3 rows");
  await toggle(page).click();
  await expect(status(page)).toHaveText("3 rows (filtered from 24)");
  expect((await download(page)).lines).toEqual([
    HEADER,
    'grp_b,row_7,"777,000.00",None,grapefruit',
    'grp_b,row_15,"777,000.00",None,grapefruit',
    'grp_b,row_23,"777,000.00",None,grapefruit',
  ]);
  expect(errors).toEqual([]);
});

test("downloads the rows as TSV, and as JSON records, of the rows the search keeps", async ({ page }) => {
  const errors = await ready(page, "export.html");
  const fired = await events(page);
  await bar(page).getByRole("button", { name: "Search the table" }).click();
  await page.keyboard.type("grape");
  await expect(bar(page).locator(".gt-i-search-count")).toHaveText("3 rows");
  await toggle(page).click();

  const tsv = await download(page, "TSV");
  expect(tsv.name).toBe("exibble.tsv");
  expect(Array.from(tsv.bytes.subarray(0, 3))).toEqual([0xef, 0xbb, 0xbf]);
  expect(tsv.lines).toEqual([
    HEADER.replace(/,/g, "\t"),
    "grp_b\trow_7\t777,000.00\tNone\tgrapefruit",
    "grp_b\trow_15\t777,000.00\tNone\tgrapefruit",
    "grp_b\trow_23\t777,000.00\tNone\tgrapefruit",
  ]);
  await expect(status(page)).toHaveText("Downloaded 3 rows");

  // (Without a byte order mark; keyed by the columns' names in the data, the group's first)
  const json = await download(page, "JSON");
  expect(json.name).toBe("exibble.json");
  expect(json.text.startsWith("[\n  {\n")).toBe(true);
  const records = JSON.parse(json.text);
  expect(records).toEqual(
    [7, 15, 23].map((i) => ({ group: "grp_b", row: `row_${i}`, num: "777,000.00", currency: "None", char: "grapefruit" })),
  );
  expect(Object.keys(records[0])).toEqual(["group", "row", "num", "currency", "char"]);
  expect(json.text).toBe(`${JSON.stringify(records, null, 2)}\n`);
  expect(await el(page).evaluate((node) => (node as any).toRecords())).toEqual(records);
  expect((await fired()).map((detail: { format: string }) => detail.format)).toEqual(["tsv", "json"]);
  expect(errors).toEqual([]);
});

test("copies the rows as a table and as tab-separated text", async ({ page, context, browserName }) => {
  await allowClipboard(context, browserName);
  const errors = await ready(page, "export.html");
  const fired = await events(page);
  await toggle(page).click();
  await panel(page).getByRole("button", { name: "Copy", exact: true }).click();
  await expect(status(page)).toHaveText("Copied 24 rows");

  const copied = await clipboard(page);
  const text = (copied["text/plain"] as string).split("\n");
  expect(text).toHaveLength(25);
  expect(text[0]).toBe(HEADER.replace(/,/g, "\t"));
  expect(text[1]).toBe("grp_b\trow_5\t5,550.00\t$1,325.81\tNone");
  // (A table of the cells, which pastes into a spreadsheet or a document)
  const table = await page.evaluate((html) => {
    const div = document.createElement("div");
    div.innerHTML = html;
    const t = div.querySelector("table") as HTMLTableElement;
    return {
      rows: t.rows.length,
      first: Array.from((t.rows[1] as HTMLTableRowElement).cells, (cell) => cell.textContent),
      classes: t.querySelectorAll("[class]").length,
    };
  }, copied["text/html"] as string);
  expect(table).toEqual({ rows: 25, first: ["grp_b", "row_5", "5,550.00", "$1,325.81", "None"], classes: 0 });
  expect((await fired())[0].format).toBe("clipboard");
  expect(errors).toEqual([]);
});

test("exports the selected rows only, when asked", async ({ page, context, browserName }) => {
  await allowClipboard(context, browserName);
  const errors = await ready(page, "export.html");
  await toggle(page).click();
  const only = panel(page).getByRole("checkbox", { name: "Selected rows only" });
  await expect(only).toBeHidden();
  await page.mouse.click(2, 2);

  // A row on the first page, and one on the second
  const boxes = el(page).locator("tbody .gt-i-select input");
  await boxes.nth(1).check();
  await bar(page).getByRole("button", { name: "Next page" }).click();
  await boxes.nth(5).check();
  await toggle(page).click();
  await only.check();
  await expect(status(page)).toHaveText("2 rows selected");

  await panel(page).getByRole("button", { name: "Copy", exact: true }).click();
  await expect(status(page)).toHaveText("Copied 2 rows");
  expect((await clipboard(page))["text/plain"]).toBe(
    `${HEADER.replace(/,/g, "\t")}\ngrp_b\trow_6\tNone\t$13.26\tfig\ngrp_b\trow_14\tNone\t$13.26\tfig`,
  );
  const { lines } = await download(page);
  expect(lines).toHaveLength(3);
  const records = JSON.parse((await download(page, "JSON")).text);
  expect(records.map((record: { row: string }) => record.row)).toEqual(["row_6", "row_14"]);
  expect(errors).toEqual([]);
});

test("is gone into with Tab, and closes on Escape, with focus back on its button", async ({ page }) => {
  const errors = await ready(page, "export.html");
  await toggle(page).focus();
  await page.keyboard.press("Enter");
  await expect(panel(page)).toBeVisible();
  await tab(page);
  await expect(panel(page).getByRole("combobox", { name: "Code for" })).toBeFocused();
  await tab(page);
  await expect(panel(page).getByRole("button", { name: "Download CSV" })).toBeFocused();
  await page.keyboard.press("Escape");
  await expect(panel(page)).toBeHidden();
  await expect(toggle(page)).toBeFocused();

  // Opening the info panel closes it
  await page.keyboard.press("Enter");
  await bar(page).getByRole("button", { name: "Table info", exact: true }).click();
  await expect(panel(page)).toBeHidden();
  await expect(bar(page).getByRole("group", { name: "Table info" })).toBeVisible();
  expect(errors).toEqual([]);
});

test("opens within the view, by the bar", async ({ page }) => {
  const errors = await ready(page, "export.html");
  await toggle(page).click();
  const shown = await box(panel(page));
  const under = await box(bar(page));
  expect(shown.top >= under.bottom || shown.bottom <= under.top).toBe(true);
  expect(shown.top).toBeGreaterThanOrEqual(0);
  expect(shown.bottom).toBeLessThanOrEqual(await page.evaluate(() => document.documentElement.clientHeight));
  expect(await panel(page).evaluate((node) => node.scrollWidth <= node.clientWidth)).toBe(true);
  // (With a button for each of the five formats, wrapping as they need to)
  const buttons = panel(page).locator(".gt-i-export-actions button");
  await expect(buttons).toHaveCount(5);
  for (const button of await buttons.all()) {
    const { left, right } = await box(button);
    expect(left).toBeGreaterThanOrEqual(shown.left);
    expect(right).toBeLessThanOrEqual(shown.right);
  }
  expect(errors).toEqual([]);
});

test.describe("on a touch screen", () => {
  test.use({ hasTouch: true, isMobile: true });

  test("has controls big enough to tap", async ({ page }) => {
    const errors = await ready(page, "export.html");
    await el(page).locator("tbody .gt-i-select input").first().check();
    await toggle(page).tap();
    await expect(panel(page)).toBeVisible();
    for (const control of [
      toggle(page),
      panel(page).locator("label", { hasText: "Selected rows only" }),
      ...["Download CSV", "Download TSV", "Download JSON", "Copy", "Copy code"].map((name) =>
        panel(page).getByRole("button", { name, exact: true }),
      ),
    ]) {
      expect((await box(control)).height).toBeGreaterThanOrEqual(44);
    }
    expect(errors).toEqual([]);
  });
});
