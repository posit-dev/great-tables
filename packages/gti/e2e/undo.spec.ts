import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { expect, type Page, test } from "@playwright/test";

// Undo: a GTI table (exibble three times over, 24 rows, 5 to a page, with a search, `num` filtered
// by a range and `fctr` by a facet, first sorted by `num`, descending) whose view isn't kept, but
// whose changes to it can be undone.

const FIXTURE = pathToFileURL(join(dirname(fileURLToPath(import.meta.url)), ".fixtures", "undo.html")).href;
const AUTHOR = { filter: null, sort: [{ column: "num", descending: true }], search: "", page: 1, pageSize: 5 };
const BY_CHAR = [{ column: "char", descending: false }];
const ONE = { and: [{ col: "fctr", op: "in", value: ["one"] }] };

const el = (page: Page) => page.locator("gt-table:has(#u)");
const sortButton = (page: Page, column: string) => page.locator(`th#u-${column} button.gt-i-sort`);
const barButton = (page: Page, name: string) =>
  el(page).locator(".gt-i-bar").getByRole("button", { name, exact: true });
const view = (page: Page) =>
  el(page).evaluate((node) => {
    const { filter, sort, search, page, pageSize } = node as any;
    return { filter, sort, search, page, pageSize };
  });

/** Open the page, once the table is hydrated, returning the errors it logs. */
async function openUndo(page: Page): Promise<string[]> {
  const errors: string[] = [];
  page.on("pageerror", (err) => errors.push(err.message));
  page.on("console", (msg) => {
    if (msg.type() === "error" || msg.type() === "warning") {
      errors.push(msg.text());
    }
  });
  await page.goto(FIXTURE);
  await expect(el(page)).toHaveAttribute("data-gti-state", "ready");
  return errors;
}

test("undoes and redoes the reader's changes from the bar, back to the page they were on", async ({ page }) => {
  const errors = await openUndo(page);
  const [undo, redo] = [barButton(page, "Undo"), barButton(page, "Redo")];
  await expect(undo).toHaveAttribute("aria-disabled", "true");
  await expect(redo).toHaveAttribute("aria-disabled", "true");
  // (Before the info button)
  await expect(el(page).locator(".gt-i-bar [data-gti-bar]:visible").last()).toHaveAttribute("data-gti-bar", "info");

  await sortButton(page, "char").click();
  await barButton(page, "Next page").click();
  await expect(undo).toHaveAttribute("aria-disabled", "false");
  await el(page).getByRole("button", { name: /^Filter fctr/ }).click();
  await el(page).getByRole("checkbox", { name: /^one\b/ }).check();
  await page.keyboard.press("Escape");
  expect(await view(page)).toEqual({ ...AUTHOR, filter: ONE, sort: BY_CHAR });

  await undo.click();
  expect(await view(page)).toEqual({ ...AUTHOR, sort: BY_CHAR, page: 2 });
  await expect(el(page).locator(".gt-i-live")).toHaveText("Undone: 6–10 of 24 rows");
  await undo.click();
  expect(await view(page)).toEqual(AUTHOR);
  await expect(undo).toHaveAttribute("aria-disabled", "true");

  await redo.click();
  await redo.click();
  expect(await view(page)).toEqual({ ...AUTHOR, filter: ONE, sort: BY_CHAR });
  await expect(redo).toHaveAttribute("aria-disabled", "true");
  await expect(el(page).locator("th#u-fctr")).toHaveAttribute("data-gti-filtered", "");
  // (Kept nowhere)
  expect(new URL(page.url()).search).toBe("");
  expect(await page.evaluate(() => localStorage.length)).toBe(0);
  expect(errors).toEqual([]);
});

test("undoes with Ctrl+Z (or ⌘Z) and redoes with Ctrl+Y or Ctrl+Shift+Z, from the table's controls", async ({ page }) => {
  await openUndo(page);
  await sortButton(page, "char").click();
  await page.keyboard.press("ControlOrMeta+z");
  expect((await view(page)).sort).toEqual(AUTHOR.sort);
  await page.keyboard.press("ControlOrMeta+Shift+z");
  expect((await view(page)).sort).toEqual(BY_CHAR);
  await page.keyboard.press("ControlOrMeta+z");
  // (From another of its controls, too)
  await el(page).getByRole("button", { name: /^Filter fctr/ }).focus();
  await page.keyboard.press("Control+y");
  expect((await view(page)).sort).toEqual(BY_CHAR);
});

test("leaves Ctrl+Z in the search box to undo its text", async ({ page }) => {
  await openUndo(page);
  await sortButton(page, "char").click();
  await barButton(page, "Search the table").click();
  const input = el(page).locator("input.gt-i-search");
  await page.keyboard.type("ab");
  await expect.poll(async () => (await view(page)).search).toBe("ab");

  await page.keyboard.press("ControlOrMeta+z");
  await expect(input).not.toHaveValue("ab");
  await expect.poll(async () => (await view(page)).search).not.toBe("ab");
  expect((await view(page)).sort).toEqual(BY_CHAR);
});

test("says its keys in the info panel", async ({ page }) => {
  await openUndo(page);
  await barButton(page, "Table info").click();
  const keys = el(page).locator(".gt-i-info-keys");
  await expect(keys).toContainText("Undo a change to the view");
  await expect(keys).toContainText("Redo it");
  // (Its view is kept nowhere, to be reset)
  await expect(el(page).locator('[data-gti-info="view"]')).toHaveCount(0);
});
