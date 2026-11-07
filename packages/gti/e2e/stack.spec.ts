import { expect, type Locator, type Page, test } from "@playwright/test";
import { borderLines, dataRows, open, ready, visible } from "./helpers";

// exibble (8 rows, grp_b then grp_a, each with a summary row, then a grand summary row), with a
// title, a spanner over num and currency, a stub, a filter on fctr and selectable rows, 5 to a
// page, stacked below 420px: in a container 360px wide; in one 800px wide; in a page as narrow as
// a phone's; with light text on a dark background; "auto" tables, of 7 columns and of 3; and, of 3,
// in containers as wide as what's in them (a table's cell, and inline blocks, one hidden at first).

const el = (page: Page) => page.locator("gt-table");
const table = (page: Page) => el(page).locator("table");
const card = (page: Page, stub: string) =>
  el(page).locator("tbody tr", { has: page.locator("th.gt_stub", { hasText: new RegExp(`^${stub}$`) }) });
const cell = (page: Page, column: string) => el(page).locator(`tbody td[headers~="k-${column}"]`);
const chip = (page: Page, column: string) => el(page).locator(`thead th#k-${column}`);
const pageButton = (page: Page, name: string) =>
  el(page).getByRole("navigation", { name: "Table pages" }).getByRole("button", { name, exact: true });

type Box = { top: number; bottom: number; left: number; right: number };
const rect = (locator: Locator): Promise<Box> =>
  locator.evaluate((node) => {
    const { top, bottom, left, right } = node.getBoundingClientRect();
    return { top, bottom, left, right };
  });

// The label shown before a cell's value
const label = (locator: Locator) => locator.evaluate((node) => getComputedStyle(node, "::before").content);

const widen = (page: Page, width: string) =>
  page.locator("body > div").evaluate((div, width) => {
    (div as HTMLElement).style.width = width;
  }, width);

test.describe("a table in a narrow container", () => {
  test("shows each row as a card, titled by its stub, with a line for each column", async ({ page }) => {
    const errors = await ready(page, "stack.html");
    await expect(el(page)).toHaveAttribute("data-gti-stacked", "");
    await expect(el(page)).not.toHaveAttribute("data-gti-wide");

    // The table fits its container, and doesn't scroll sideways
    const container = await rect(page.locator("body > div"));
    expect((await rect(table(page))).right).toBeLessThanOrEqual(container.right + 0.5);
    const scroller = el(page).locator(".gt-i-scroller");
    expect(await scroller.evaluate((div) => div.scrollWidth - div.clientWidth)).toBeLessThanOrEqual(1);

    // A card: the checkbox and the stub on a line, then each column's label and value, in the
    // order of the column labels (num and currency under their spanner)
    const row = card(page, "row_5");
    await expect(row).toHaveCSS("display", "flex");
    const box = await rect(row.locator("td.gt-i-select"));
    const stub = await rect(row.locator("th.gt_stub"));
    expect(Math.abs(box.top - stub.top)).toBeLessThan(1);
    expect(stub.left).toBeGreaterThan(box.right - 1);
    const values = row.locator("td.gt_row:not(.gt-i-select)");
    await expect(values).toHaveText(["5,550.00", "$1,325.81", "None", "five"]);
    const labels = await values.evaluateAll((cells) => cells.map((td) => getComputedStyle(td, "::before").content));
    expect(labels.map((text) => text.replace(/ \/ ""$/, ""))).toEqual([
      '"Numbers · num"',
      '"Numbers · currency"',
      '"char"',
      '"fctr"',
    ]);
    // (Each line below the one before)
    const tops = await values.evaluateAll((cells) => cells.map((td) => td.getBoundingClientRect().top));
    expect(tops).toEqual([...tops].sort((a, b) => a - b));
    expect(new Set(tops).size).toBe(4);

    // The summary rows are cards too, without a checkbox; the group headings are between them
    const total = card(page, "Total").first();
    await expect(total).toHaveCSS("display", "flex");
    await expect(total.locator("td.gt-i-select")).toBeHidden();
    const heading = await rect(el(page).locator("tr.gt_group_heading_row").nth(1));
    expect(heading.top).toBeGreaterThan((await rect(total)).bottom);

    // No resizers, nor rows to pad the page
    await expect(el(page).locator(".gt-i-resizer").first()).toBeHidden();
    expect(errors).toEqual([]);
  });

  test("is still a table to assistive technology", async ({ page }) => {
    const errors = await ready(page, "stack.html");
    await expect(el(page).getByRole("table")).toHaveCount(1);
    const row = el(page).getByRole("row", { name: /row_5/ });
    await expect(row.getByRole("rowheader")).toHaveText("row_5");
    await expect(row.getByRole("cell", { name: "5,550.00" })).toHaveCount(1);
    await expect(el(page).getByRole("columnheader", { name: /^char/ })).toHaveCount(1);
    // (The labels before the values aren't read out, as the column headers are)
    expect(await label(cell(page, "char").first())).toBe('"char" / ""');
    expect(errors).toEqual([]);
  });

  test("has the column labels as chips, to sort and filter by", async ({ page }) => {
    const errors = await ready(page, "stack.html");
    // The chips: the select-all checkbox, then the columns (under their spanners), on lines
    // above the cards, without the spanners or the stubhead
    const chips = await el(page)
      .locator("thead tr.gt_col_headings > th:visible")
      .evaluateAll((cells) =>
        cells
          .map((th) => ({ text: th.textContent ?? "", box: th.getBoundingClientRect() }))
          // (By line, then along it: chips with buttons are taller, centred on their line)
          .sort((a, b) => a.box.top + a.box.bottom - b.box.top - b.box.bottom > 10 ? 1 : a.box.top + a.box.bottom - b.box.top - b.box.bottom < -10 ? -1 : a.box.left - b.box.left)
          .map(({ text }) => text),
      );
    expect(chips).toEqual(["", "num", "currency", "char", "fctr"]);
    expect(await chip(page, "num").evaluate((th) => getComputedStyle(th, "::before").content)).toBe('"Numbers · "');
    expect(await chip(page, "char").evaluate((th) => getComputedStyle(th, "::before").content)).toBe("none");
    await expect(chip(page, "num")).toHaveCSS("border-radius", "999px");
    const first = await rect(card(page, "row_5"));
    expect((await rect(chip(page, "fctr"))).bottom).toBeLessThan(first.top);

    // Sorting (within the groups)
    await chip(page, "num").locator("button.gt-i-sort").click();
    await expect(chip(page, "num")).toHaveAttribute("aria-sort", "ascending");
    expect(dataRows(await visible(page))).toEqual([4, 6, 7, 5, 0]);
    await expect(el(page).locator("tbody th.gt_stub").first()).toHaveText("row_5");

    // Filtering
    await chip(page, "fctr").getByRole("button", { name: /^Filter fctr/ }).click();
    await el(page).getByRole("group", { name: "Filter fctr", exact: true }).getByRole("textbox").pressSequentially("one");
    await page.keyboard.press("Escape");
    await expect.poll(async () => dataRows(await visible(page))).toEqual([0]);
    await expect(card(page, "row_1")).toHaveCSS("display", "flex");

    // Selecting, from a card's checkbox
    await card(page, "row_1").getByRole("checkbox").check();
    expect(await el(page).evaluate((node) => (node as any).selection)).toEqual([0]);
    expect(errors).toEqual([]);
  });

  test("pages the cards, without padding the last page", async ({ page }) => {
    const errors = await ready(page, "stack.html");
    await pageButton(page, "Next page").click();
    expect(dataRows(await visible(page))).toEqual([1, 2, 3]);
    await expect(el(page).locator("tr.gt-i-filler:visible")).toHaveCount(0);
    expect(errors).toEqual([]);
  });

  test("is a table again when its container is wide enough", async ({ page }) => {
    const errors = await ready(page, "stack.html");
    await pageButton(page, "Next page").click();
    await widen(page, "800px");
    await expect(el(page)).not.toHaveAttribute("data-gti-stacked");
    await expect(card(page, "row_2")).toHaveCSS("display", "table-row");
    await expect(el(page).locator("thead tr.gt_col_headings").last()).toHaveCSS("display", "table-row");
    // (The last page is padded to the height of the others)
    await expect.poll(() => el(page).locator("tr.gt-i-filler").count()).toBeGreaterThan(0);
    await pageButton(page, "Previous page").click();

    // And it's drawn as one that was never stacked is
    const other = await page.context().newPage();
    await ready(other, "stack-wide.html");
    const x = (await rect(cell(page, "num").first())).left + 4;
    expect(await borderLines(page, table(page), { x })).toEqual(await borderLines(other, table(other), { x }));
    for (const y of [0.3, 0.6]) {
      expect(await borderLines(page, table(page), { y, width: 500 })).toEqual(
        await borderLines(other, table(other), { y, width: 500 }),
      );
    }

    // And stacked again in a narrow one
    await widen(page, "360px");
    await expect(el(page)).toHaveAttribute("data-gti-stacked", "");
    await expect(card(page, "row_5")).toHaveCSS("display", "flex");
    expect(errors).toEqual([]);
  });
});

test.describe("a table that can be stacked, without JavaScript", () => {
  test.use({ javaScriptEnabled: false });

  test("is stacked by its CSS, with the column labels left out", async ({ page }) => {
    await open(page, "stack.html");
    await expect(el(page)).not.toHaveAttribute("data-gti-state");
    await expect(card(page, "row_5")).toHaveCSS("display", "flex");
    await expect(el(page).locator("thead tr.gt_col_headings:visible")).toHaveCount(0);
    await expect(el(page).locator("thead .gt_title")).toHaveText("exibble");
    expect(await label(cell(page, "num").first())).toBe('"Numbers · num"');
    expect(await label(cell(page, "fctr").first())).toBe('"fctr"');
    const container = await rect(page.locator("body > div"));
    expect((await rect(table(page))).right).toBeLessThanOrEqual(container.right + 0.5);
  });
});

test.describe("a table that can be stacked, on a phone", () => {
  test.use({ hasTouch: true, viewport: { width: 390, height: 700 } });

  test("is stacked, and fits the page", async ({ page }) => {
    const errors = await ready(page, "stack-phone.html");
    await expect(el(page)).toHaveAttribute("data-gti-stacked", "");
    expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(390);
    await card(page, "row_6").locator("th.gt_stub").tap();
    expect(await el(page).evaluate((node) => (node as any).selection)).toEqual([5]);
    expect(errors).toEqual([]);
  });
});

test("a stacked table with light text on a dark background keeps its colours", async ({ page }) => {
  const errors = await ready(page, "stack-dark.html");
  await expect(el(page)).toHaveAttribute("data-gti-stacked", "");
  // (The labels in the values' light colour, a little fainter, and the chips' and cards' borders
  // grey, on either)
  const { value, before } = await cell(page, "char")
    .first()
    .evaluate((td) => ({ value: getComputedStyle(td).color, before: getComputedStyle(td, "::before").color }));
  expect(before).toBe(value);
  expect(Number(/\d+/.exec(value)?.[0])).toBeGreaterThan(200);
  await expect(card(page, "row_5")).toHaveCSS("border-top-color", "rgba(128, 128, 128, 0.4)");
  await expect(chip(page, "char")).toHaveCSS("border-top-color", "rgba(128, 128, 128, 0.4)");
  await expect(el(page).locator("thead")).toHaveCSS("background-color", "rgb(30, 30, 30)");
  expect(errors).toEqual([]);
});

test.describe('an "auto" table', () => {
  test("with many columns scrolls, until enough of them are hidden", async ({ page }) => {
    const errors = await ready(page, "stack-auto.html");
    await expect(el(page)).toHaveAttribute("data-gti-stack-off", "");
    await expect(el(page)).not.toHaveAttribute("data-gti-stacked");
    await expect(el(page)).toHaveAttribute("data-gti-wide", "");

    await el(page).evaluate((node) => {
      (node as any).hiddenColumns = ["date", "time", "datetime"];
    });
    await expect(el(page)).not.toHaveAttribute("data-gti-stack-off");
    await expect(el(page)).toHaveAttribute("data-gti-stacked", "");
    await expect(el(page)).not.toHaveAttribute("data-gti-wide");
    await expect(card(page, "row_5")).toHaveCSS("display", "flex");

    await el(page).evaluate((node) => {
      (node as any).hiddenColumns = [];
    });
    await expect(el(page)).toHaveAttribute("data-gti-stack-off", "");
    await expect(el(page)).not.toHaveAttribute("data-gti-stacked");
    await expect(el(page)).toHaveAttribute("data-gti-wide", "");
    expect(errors).toEqual([]);
  });

  test("with few columns is stacked", async ({ page }) => {
    const errors = await ready(page, "stack-auto-few.html");
    await expect(el(page)).not.toHaveAttribute("data-gti-stack-off");
    await expect(el(page)).toHaveAttribute("data-gti-stacked", "");
    expect(errors).toEqual([]);
  });
});

test.describe("a table that could be stacked, in a container as wide as what's in it", () => {
  // (Which, as the container its width is queried in, would have no width of its own)
  const fits = async (page: Page) => {
    await expect(el(page)).toHaveAttribute("data-gti-stack-off", "");
    await expect(el(page)).not.toHaveAttribute("data-gti-stacked");
    await expect(card(page, "row_5")).toHaveCSS("display", "table-row");
    // (As wide as the table, or its bar)
    await expect
      .poll(() =>
        el(page).evaluate((node) => {
          const inner = (node.querySelector("table") as HTMLElement).offsetWidth;
          return (node as HTMLElement).offsetWidth >= inner && inner > 300;
        }),
      )
      .toBe(true);
  };

  test("isn't stacked, in a table's cell or an inline block", async ({ page }) => {
    for (const name of ["stack-fit.html", "stack-fit-inline.html"]) {
      const errors = await ready(page, name);
      await fits(page);
      expect(errors).toEqual([]);
    }
  });

  test("isn't stacked as it shows fewer columns", async ({ page }) => {
    const errors = await ready(page, "stack-fit.html");
    await el(page).evaluate((node) => {
      (node as any).hiddenColumns = ["fctr"];
    });
    await expect(el(page).locator("thead th#k-fctr")).toBeHidden();
    await fits(page);
    expect(errors).toEqual([]);
  });

  test("isn't stacked once it's shown", async ({ page }) => {
    const errors = await ready(page, "stack-fit-hidden.html");
    await page.locator("body > div").evaluate((div) => div.removeAttribute("hidden"));
    await fits(page);
    expect(errors).toEqual([]);
  });
});
