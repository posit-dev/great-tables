import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { expect, type Page, test } from "@playwright/test";

// The view kept: two GTI tables on a page (exibble three times over, 24 rows, 5 to a page, with a
// search, `num` filtered by a range and `fctr` by a facet, first sorted by `num`, descending),
// `va` kept in the URL and the browser's storage, and `vb` in the URL only.

const FIXTURE = pathToFileURL(join(dirname(fileURLToPath(import.meta.url)), ".fixtures", "state.html")).href;
const AUTHOR = { filter: null, sort: [{ column: "num", descending: true }], search: "", page: 1, pageSize: 5 };

const el = (page: Page, id: string) => page.locator(`gt-table:has(#${id})`);
const sortButton = (page: Page, id: string, column: string) => page.locator(`th#${id}-${column} > button.gt-i-sort`);
const barButton = (page: Page, id: string, name: string) =>
  el(page, id).locator(".gt-i-bar").getByRole("button", { name, exact: true });
const view = (page: Page, id: string) =>
  el(page, id).evaluate((node) => {
    const { filter, sort, search, page, pageSize } = node as any;
    return { filter, sort, search, page, pageSize };
  });
const search = (page: Page) => new URL(page.url()).search;

/** Open the page (with `query`), once both tables are hydrated, returning the errors it logs. */
async function openState(page: Page, query = ""): Promise<string[]> {
  const errors: string[] = [];
  page.on("pageerror", (err) => errors.push(err.message));
  page.on("console", (msg) => {
    if (msg.type() === "error" || msg.type() === "warning") {
      errors.push(msg.text());
    }
  });
  await page.goto(FIXTURE + query);
  for (const id of ["va", "vb"]) {
    await expect(el(page, id)).toHaveAttribute("data-gti-state", "ready");
  }
  return errors;
}

test("keeps the reader's view across a reload", async ({ page }) => {
  const errors = await openState(page);
  await sortButton(page, "va", "char").click();
  await barButton(page, "va", "Next page").click();
  await barButton(page, "va", "Search the table").click();
  await page.keyboard.type("a");
  await expect.poll(() => search(page)).toBe("?va.sort=char&va.search=a");
  await el(page, "va").getByRole("button", { name: /^Filter fctr/ }).click();
  await el(page, "va").getByRole("checkbox", { name: /^one\b/ }).check();
  await page.keyboard.press("Escape");
  await expect.poll(() => search(page)).toBe('?va.filter=fctr+in+(%22one%22)&va.sort=char&va.search=a');
  const kept = await view(page, "va");
  expect(kept).toEqual({
    ...AUTHOR,
    filter: { and: [{ col: "fctr", op: "in", value: ["one"] }] },
    sort: [{ column: "char", descending: false }],
    search: "a",
  });

  await page.reload();
  await expect(el(page, "va")).toHaveAttribute("data-gti-state", "ready");
  expect(await view(page, "va")).toEqual(kept);
  // (Its controls show it too)
  await expect(page.locator("th#va-char")).toHaveAttribute("aria-sort", "ascending");
  await expect(el(page, "va").locator(".gt-i-search")).toHaveValue("a");
  await expect(page.locator("th#va-fctr")).toHaveAttribute("data-gti-filtered", "");
  expect(await view(page, "vb")).toEqual(AUTHOR);
  expect(errors).toEqual([]);
});

test("opens a shared link with its view, rather than the one in storage", async ({ page }) => {
  await openState(page);
  await barButton(page, "va", "Next page").click();
  await expect.poll(() => search(page)).toBe("?va.page=2");
  // (A link to the page with the views of both tables, and another parameter)
  const errors = await openState(page, "?ref=mail&vb.sort=-char&vb.page=3&va.filter=num+%3C%3D+500&va.sort=");
  expect(await view(page, "va")).toEqual({ ...AUTHOR, filter: { and: [{ col: "num", op: "lte", value: 500 }] }, sort: [] });
  expect(await view(page, "vb")).toEqual({ ...AUTHOR, sort: [{ column: "char", descending: true }], page: 3 });
  await expect(el(page, "vb").locator(".gt-i-readout")).toHaveAccessibleName("Page 3 of 5");
  expect(search(page)).toBe("?ref=mail&vb.sort=-char&vb.page=3&va.filter=num+%3C%3D+500&va.sort=");
  expect(errors).toEqual([]);
});

test("keeps the views of two tables apart", async ({ page }) => {
  const errors = await openState(page, "?ref=mail");
  await sortButton(page, "vb", "char").click();
  await barButton(page, "va", "Next page").click();
  await sortButton(page, "va", "num").click();
  await expect.poll(() => search(page)).toBe("?ref=mail&vb.sort=char&va.sort=");
  expect(await view(page, "va")).toEqual({ ...AUTHOR, sort: [] });
  expect(await view(page, "vb")).toEqual({ ...AUTHOR, sort: [{ column: "char", descending: false }] });

  // Without the link's view, `va` has the one in storage, and `vb` (kept in the URL only) its own
  await openState(page);
  expect(await view(page, "va")).toEqual({ ...AUTHOR, sort: [] });
  expect(await view(page, "vb")).toEqual(AUTHOR);
  expect(search(page)).toBe("?va.sort=");
  expect(errors).toEqual([]);
});

test("resets the view from the info panel", async ({ page }) => {
  const errors = await openState(page, "?ref=mail&va.sort=char&va.page=3");
  await barButton(page, "va", "Table info").click();
  const item = el(page, "va").locator('[data-gti-info="view"]');
  await expect(item).toContainText("View kept in the link and this browser");
  const reset = item.getByRole("button", { name: "Reset the view" });
  await expect(reset).toHaveAttribute("aria-disabled", "false");
  await reset.click();
  expect(await view(page, "va")).toEqual(AUTHOR);
  expect(search(page)).toBe("?ref=mail");
  await expect(reset).toHaveAttribute("aria-disabled", "true");
  await expect(reset).toBeFocused();

  await page.reload();
  await expect(el(page, "va")).toHaveAttribute("data-gti-state", "ready");
  expect(await view(page, "va")).toEqual(AUTHOR);
  expect(errors).toEqual([]);
});

test("leaves out a part of a link's view the table can't have, with a warning", async ({ page }) => {
  const errors = await openState(page, "?va.filter=char+contains+%22a%22&va.page=2");
  expect(await view(page, "va")).toEqual({ ...AUTHOR, page: 2 });
  expect(errors).toEqual([expect.stringMatching(/^<gt-table>: the saved view's filter is left out \(.+\)\.$/)]);
  expect(search(page)).toBe("?va.page=2");
});
