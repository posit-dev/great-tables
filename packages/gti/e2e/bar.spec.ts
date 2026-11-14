import { expect, type Locator, type Page, test } from "@playwright/test";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { CHROMIUM_TOUCH, dataRows, open, ready, tab, visible } from "./helpers";

// GTI tables, with the control bar below them: exibble three times over (24 rows, in two groups),
// 2 rows to a page (12 pages), with a search; as narrow as one column; in a container 300px wide;
// and on one page, with room to scroll past it.

const RUNTIME = join(dirname(fileURLToPath(import.meta.url)), "..", "..", "..", "great_tables", "js", "gti.js");

const el = (page: Page) => page.locator("gt-table");
const bar = (page: Page) => el(page).locator(".gt-i-bar");
const barButton = (page: Page, name: string) => bar(page).getByRole("button", { name, exact: true });
const field = (page: Page) => bar(page).locator(".gt-i-search-field");
const search = (page: Page) => bar(page).locator("input.gt-i-search");
const pages = (page: Page) => bar(page).locator(".gt-i-bar-pages");
const readout = (page: Page) => bar(page).locator("button.gt-i-readout");
const pageOf = (page: Page) => el(page).evaluate((node) => (node as any).page as number);
const box = (locator: Locator) =>
  locator.evaluate((node) => {
    const { left, right, top, bottom, width } = node.getBoundingClientRect();
    return { left, right, top, bottom, width };
  });

test("is one bar below the table, with no toolbar or pager", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  await expect(bar(page)).toBeVisible();
  await expect(el(page).locator(".gt-i-toolbar, .gt-i-pager")).toHaveCount(0);
  expect((await box(bar(page))).top).toBeGreaterThanOrEqual((await box(el(page).locator("table"))).bottom);
  // In one row, with the page controls at the end, then the info button
  const toggle = await box(barButton(page, "Search the table"));
  const next = await box(barButton(page, "Next page"));
  const info = await box(barButton(page, "Table info"));
  expect(Math.abs(toggle.top - next.top)).toBeLessThan(1);
  expect(Math.abs(info.top - next.top)).toBeLessThan(1);
  expect(info.left).toBeGreaterThanOrEqual(next.right);
  expect(info.right).toBeCloseTo((await box(bar(page))).right, 0);
  await expect(readout(page)).toHaveText("1/12");
  await expect(readout(page)).toHaveAccessibleName("Page 1 of 12");
  expect(errors).toEqual([]);
});

test("searches from a button that opens a field, which Escape clears and then closes", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  await expect(field(page)).toBeHidden();
  await barButton(page, "Search the table").click();
  await expect(field(page)).toBeVisible();
  await expect(search(page)).toBeFocused();
  await expect(barButton(page, "Search the table")).toBeHidden();

  await page.keyboard.type("apricot");
  await expect(bar(page).locator(".gt-i-search-count")).toHaveText("3 rows");
  await expect(readout(page)).toHaveText("1/2");
  expect(dataRows(await visible(page))).toEqual([0, 8]);

  await page.keyboard.press("Escape");
  await expect(search(page)).toHaveValue("");
  await expect(field(page)).toBeVisible();
  await expect(readout(page)).toHaveText("1/12");
  await page.keyboard.press("Escape");
  await expect(field(page)).toBeHidden();
  await expect(barButton(page, "Search the table")).toBeFocused();
  expect(errors).toEqual([]);
});

test("opens the search on `/` from within the table, and closes an empty one on leaving it", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  await el(page).locator("button.gt-i-sort").first().focus();
  await page.keyboard.press("/");
  await expect(search(page)).toBeFocused();
  await expect(search(page)).toHaveValue("");

  await tab(page, true);
  await expect(field(page)).toBeHidden();

  // A search in force stays shown
  await barButton(page, "Search the table").click();
  await page.keyboard.type("fig");
  await page.keyboard.press("Enter");
  await el(page).locator("button.gt-i-sort").first().focus();
  await expect(field(page)).toBeVisible();
  expect(errors).toEqual([]);
});

test("pages with its arrows, and with the keys in the bar", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  await expect(barButton(page, "Previous page")).toHaveAttribute("aria-disabled", "true");
  await barButton(page, "Next page").click();
  expect(await pageOf(page)).toBe(2);
  await expect(readout(page)).toHaveText("2/12");

  await page.keyboard.press("ArrowRight");
  await page.keyboard.press("PageDown");
  expect(await pageOf(page)).toBe(4);
  await page.keyboard.press("ArrowLeft");
  expect(await pageOf(page)).toBe(3);
  await page.keyboard.press("End");
  await expect(readout(page)).toHaveText("12/12");
  await expect(barButton(page, "Next page")).toHaveAttribute("aria-disabled", "true");
  await page.keyboard.press("Home");
  expect(await pageOf(page)).toBe(1);
  expect(errors).toEqual([]);
});

test("goes to the first and last pages, from buttons outside its arrows", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  const [first, last] = [barButton(page, "First page"), barButton(page, "Last page")];
  expect((await box(first)).right).toBeLessThanOrEqual((await box(barButton(page, "Previous page"))).left);
  expect((await box(last)).left).toBeGreaterThanOrEqual((await box(barButton(page, "Next page"))).right);
  await expect(first).toHaveAttribute("aria-disabled", "true");
  await last.click();
  await expect(readout(page)).toHaveText("12/12");
  await expect(last).toHaveAttribute("aria-disabled", "true");
  await expect(first).toHaveAttribute("aria-disabled", "false");
  await first.click();
  expect(await pageOf(page)).toBe(1);
  expect(errors).toEqual([]);
});

test("lists its shortcuts from a button after the search's, which the open search covers", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  const keys = barButton(page, "Keyboard shortcuts");
  const at = await box(keys);
  expect(at.left).toBeGreaterThanOrEqual((await box(barButton(page, "Search the table"))).right);
  await keys.click();
  const panel = bar(page).getByRole("group", { name: "Keyboard shortcuts" });
  await expect(panel).toBeVisible();
  await expect(panel.locator(".gt-i-info-keys")).toContainText("First or last page, in the bar");
  expect((await box(panel)).bottom).toBeLessThanOrEqual((await box(bar(page))).top);

  await barButton(page, "Search the table").click();
  await expect(panel).toBeHidden();
  await expect(keys).toBeHidden();
  expect((await box(field(page))).right).toBeGreaterThanOrEqual(at.right);
  expect(errors).toEqual([]);
});

test("takes its shortcuts after a click in the table", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  await el(page).locator("tbody td.gt_row").first().click();
  expect(await page.evaluate(() => document.activeElement?.tagName)).toBe("GT-TABLE");
  // (Without a ring around it)
  await expect(el(page)).toHaveCSS("outline-style", "none");
  await page.keyboard.press("/");
  await expect(search(page)).toBeFocused();
  expect(errors).toEqual([]);
});

test("resets the view from a button that shows while there's something to reset", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  const reset = barButton(page, "Reset the view");
  await expect(reset).toBeHidden();
  const before = await visible(page);
  await el(page).locator("button.gt-i-sort").first().click();
  await expect(reset).toBeVisible();
  await expect(reset).toHaveText("Reset");
  // (Just before the info button, in the accent colour)
  expect((await box(reset)).right).toBeLessThanOrEqual((await box(barButton(page, "Table info"))).left);
  expect(await reset.evaluate((node) => getComputedStyle(node, "::before").backgroundColor)).toBe("rgb(31, 111, 235)");

  await reset.click();
  await expect(reset).toBeHidden();
  expect(await visible(page)).toEqual(before);
  await expect(barButton(page, "Table info")).toBeFocused();
  expect(errors).toEqual([]);
});

test("names its buttons with tooltips of its own, a moment after the mouse goes onto them", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  const next = barButton(page, "Next page");
  expect(await next.getAttribute("title")).toBeNull();
  const tip = bar(page).getByRole("tooltip");
  await next.hover();
  await expect(tip).toBeVisible();
  await expect(tip).toHaveText("Next page (→)");
  // (Above it, and centred on it)
  const [shown, under] = [await box(tip), await box(next)];
  expect(shown.bottom).toBeLessThanOrEqual(under.top);
  expect((shown.left + shown.right) / 2).toBeCloseTo((under.left + under.right) / 2, 0);

  await page.mouse.move(2, 2);
  await expect(tip).toBeHidden();
  await barButton(page, "Last page").hover();
  await expect(tip).toHaveText("Last page (End)");
  await page.keyboard.press("Escape");
  await expect(tip).toBeHidden();
  expect(errors).toEqual([]);
});

test.describe("on a touch screen", () => {
  test.use({ hasTouch: true });

  test("shows no tooltips for a tap", async ({ page }) => {
    const errors = await ready(page, "bar.html");
    await barButton(page, "Next page").tap();
    await expect(readout(page)).toHaveText("2/12");
    await page.waitForTimeout(800);
    await expect(bar(page).getByRole("tooltip")).toBeHidden();
    expect(errors).toEqual([]);
  });
});

test.describe("the handle under the rows", () => {
  const handle = (page: Page) => el(page).locator(".gt-i-rows");
  const grand = (page: Page) => el(page).locator("tbody tr:has(> .gt_grand_summary_row)").first();
  // (The last data row on the page)
  const lastData = (page: Page) =>
    el(page).evaluate((node) => {
      const el = node as any;
      const trs = Array.from(node.querySelectorAll<HTMLTableRowElement>("tbody.gt_table_body > tr"));
      const tr = trs.filter((tr) => typeof el.bodyRow(tr) === "number" && tr.getClientRects().length > 0).pop();
      const { top, bottom } = (tr as HTMLTableRowElement).getBoundingClientRect();
      return { top, bottom };
    });
  const count = async (page: Page) => dataRows(await visible(page)).length;
  // A drag from the middle of the handle, `dy` down (or up), in steps
  const drag = async (page: Page, dy: number) => {
    const at = await box(handle(page));
    const x = (at.left + at.right) / 2;
    const y = (at.top + at.bottom) / 2;
    await page.mouse.move(x, y);
    await page.mouse.down();
    await page.mouse.move(x, y + dy, { steps: 10 });
    await page.mouse.up();
  };
  const rowHeight = async (page: Page) => {
    const { top, bottom } = await lastData(page);
    return bottom - top;
  };

  test("is along the foot of the page's rows, above the grand summary rows", async ({ page }) => {
    const errors = await ready(page, "bar.html");
    const at = await box(handle(page));
    const foot = (at.top + at.bottom) / 2;
    expect(foot).toBeCloseTo((await lastData(page)).bottom, 0);
    expect(foot).toBeCloseTo((await box(grand(page))).top, 0);
    const table = await box(el(page).locator("table"));
    expect(at.bottom).toBeLessThan(table.bottom);
    expect(at.left).toBeCloseTo(table.left, 0);
    expect(at.right).toBeCloseTo(table.right, 0);
    await expect(handle(page)).toHaveCSS("cursor", "row-resize");
    expect(errors).toEqual([]);
  });

  test("is dragged down or up for more or fewer rows a page, down to 1, which the reset undoes", async ({ page }) => {
    const errors = await ready(page, "bar.html");
    const reset = barButton(page, "Reset the view");
    const height = await rowHeight(page);
    const count_ = handle(page).locator(".gt-i-rows-count");
    await handle(page).hover();
    await expect(count_).toHaveText("2 rows per page");
    await expect(count_).toHaveCSS("opacity", "1");

    await drag(page, height * 3);
    expect(await count(page)).toBe(5);
    await expect(readout(page)).toHaveText("1/5");
    await expect(handle(page)).toHaveAttribute("aria-valuenow", "5");
    await expect(reset).toBeVisible();
    // (Following the rows)
    expect((await box(handle(page))).top + 6).toBeCloseTo((await box(grand(page))).top, 0);

    await drag(page, -height * 20);
    expect(await count(page)).toBe(1);
    await expect(readout(page)).toHaveText("1/24");

    await reset.click();
    await expect(reset).toBeHidden();
    expect(await count(page)).toBe(2);
    await expect(readout(page)).toHaveText("1/12");
    expect(errors).toEqual([]);
  });

  test("keeps the page's first row as it's dragged", async ({ page }) => {
    const errors = await ready(page, "bar.html");
    await page.evaluate(() => ((document.querySelector("gt-table") as any).page = 4));
    const first = dataRows(await visible(page))[0];
    await drag(page, (await rowHeight(page)) * 2);
    await expect(readout(page)).toHaveText("2/6");
    expect(dataRows(await visible(page))).toContain(first);
    expect(errors).toEqual([]);
  });

  test("comes after the table and before the bar by Tab, and takes the arrows and Enter", async ({ page }) => {
    const errors = await ready(page, "bar.html");
    await handle(page).focus();
    await expect(handle(page).locator(".gt-i-rows-count")).toHaveCSS("opacity", "1");
    await page.keyboard.press("ArrowDown");
    await expect(readout(page)).toHaveText("1/8");
    await page.keyboard.press("PageDown");
    await expect(readout(page)).toHaveText("1/2");
    await page.keyboard.press("Enter");
    await expect(readout(page)).toHaveText("1/12");
    await tab(page);
    await expect(barButton(page, "Search the table")).toBeFocused();
    await tab(page, true);
    await expect(handle(page)).toBeFocused();
    expect(errors).toEqual([]);
  });

  test("works on a search's rows", async ({ page }) => {
    const errors = await ready(page, "bar.html");
    await barButton(page, "Search the table").click();
    await page.keyboard.type("apricot");
    await expect(readout(page)).toHaveText("1/2");
    await drag(page, await rowHeight(page));
    await expect(readout(page)).toHaveText("1/1");
    expect(await count(page)).toBe(3);
    await expect(handle(page)).toHaveAttribute("aria-valuenow", "3");
    expect(errors).toEqual([]);
  });

  test.describe("on a touch screen", () => {
    test.use({ hasTouch: true });

    test("is dragged by a finger, without scrolling the page", async ({ page, browserName }) => {
      test.skip(browserName !== "chromium", CHROMIUM_TOUCH);
      const errors = await ready(page, "bar.html");
      const at = await box(handle(page));
      expect(at.bottom - at.top).toBeCloseTo(24, 0);
      const height = await rowHeight(page);
      const x = Math.round((at.left + at.right) / 2);
      const y = Math.round((at.top + at.bottom) / 2);
      const cdp = await page.context().newCDPSession(page);
      const touch = (type: "touchStart" | "touchMove" | "touchEnd", points: { x: number; y: number }[]) =>
        cdp.send("Input.dispatchTouchEvent", { type, touchPoints: points });
      await touch("touchStart", [{ x, y }]);
      for (let step = 1; step <= 10; step++) {
        await touch("touchMove", [{ x, y: Math.round(y + (step * height * 2) / 10) }]);
      }
      await touch("touchEnd", []);
      await expect(readout(page)).toHaveText("1/6");
      expect(await page.evaluate(() => window.scrollY)).toBe(0);
      expect(errors).toEqual([]);
    });
  });
});

test.describe("the handle under a body that scrolls", () => {
  const handle = (page: Page) => el(page).locator(".gt-i-height");
  const scroller = (page: Page) => el(page).locator(".gt-i-scroller");
  const tall = async (page: Page) => (await box(scroller(page))).bottom - (await box(scroller(page))).top;
  const query = (page: Page) => new URL(page.url()).search;
  // (The body's foot: the bottom of the scroller, above the clear border around it that keeps
  // GT's space there)
  const foot = (page: Page) =>
    scroller(page).evaluate(
      (div) =>
        div.getBoundingClientRect().bottom -
        (div.style.borderBottomColor === "transparent" ? parseFloat(div.style.borderBottomWidth) : 0),
    );
  const drag = async (page: Page, dy: number) => {
    const at = await box(handle(page));
    const x = (at.left + at.right) / 2;
    const y = (at.top + at.bottom) / 2;
    await page.mouse.move(x, y);
    await page.mouse.down();
    await page.mouse.move(x, y + dy, { steps: 10 });
    await page.mouse.up();
  };

  test("is along the foot of the body, across it, without saying a size", async ({ page }) => {
    const errors = await ready(page, "bar-scroll.html");
    await expect(el(page).locator(".gt-i-rows")).toHaveCount(0);
    const [at, port] = [await box(handle(page)), await box(scroller(page))];
    expect((at.top + at.bottom) / 2).toBeCloseTo(await foot(page), 0);
    expect(at.left).toBeGreaterThanOrEqual(port.left - 1);
    expect(at.right).toBeLessThanOrEqual(port.right + 1);
    expect(await tall(page)).toBeCloseTo(300, 0);
    await expect(handle(page)).toHaveAccessibleName("Table height");
    await expect(handle(page)).toHaveAttribute("aria-valuenow", "300");
    await expect(handle(page).locator(".gt-i-rows-count")).toHaveCount(0);
    expect(errors).toEqual([]);
  });

  test("is dragged for a taller or shorter body, kept in the URL, which the reset undoes", async ({ page }) => {
    const errors = await ready(page, "bar-scroll.html");
    const reset = barButton(page, "Reset the view");
    await expect(reset).toBeHidden();
    await drag(page, 100);
    expect(await tall(page)).toBeCloseTo(400, 0);
    await expect(handle(page)).toHaveAttribute("aria-valuenow", "400");
    await expect.poll(() => query(page)).toBe("?c.height=400");
    await expect(reset).toBeVisible();
    // (Following the body's foot)
    expect(((await box(handle(page))).top + (await box(handle(page))).bottom) / 2).toBeCloseTo(await foot(page), 0);

    // No shorter than the column labels, a row, and the rows stuck to the bottom (with the space
    // above and below them in the container, a border of its own by now)
    // (To the top of the page: Firefox misses a mouse let go outside it)
    await drag(page, -((await box(handle(page))).top + 4));
    const least = await el(page).evaluate((node) => {
      const head = (node.querySelector("thead") as HTMLElement).getBoundingClientRect().height;
      const row = (node.querySelector("tbody td.gt_row") as HTMLElement).getBoundingClientRect().height;
      const scroller = node.querySelector(".gt-i-scroller") as HTMLElement;
      return head + row + (node as any).foot + scroller.offsetHeight - scroller.clientHeight;
    });
    expect(await tall(page)).toBeGreaterThanOrEqual(least - 1);
    expect(await tall(page)).toBeLessThan(least + 4);

    // And no taller than every row
    await handle(page).focus();
    for (let i = 0; i < 5; i++) {
      await page.keyboard.press("PageDown");
    }
    expect(await scroller(page).evaluate((node) => node.scrollHeight - node.clientHeight)).toBeLessThanOrEqual(0);

    await reset.click();
    await expect(reset).toBeHidden();
    expect(await tall(page)).toBeCloseTo(300, 0);
    await expect.poll(() => query(page)).toBe("");
    expect(errors).toEqual([]);
  });

  test("takes the arrows, Page Down and Enter, and its drag is undone", async ({ page }) => {
    const errors = await ready(page, "bar-scroll.html");
    const row = await el(page).evaluate((node) => (node.querySelector("tbody td.gt_row") as HTMLElement).getBoundingClientRect().height);
    await handle(page).focus();
    await page.keyboard.press("ArrowDown");
    expect(await tall(page)).toBeCloseTo(300 + row, 0);
    // (Ten rows up, as far as a row's height)
    await page.keyboard.press("PageUp");
    expect(await tall(page)).toBeLessThan(300 - row);
    await page.keyboard.press("Enter");
    expect(await tall(page)).toBeCloseTo(300, 0);

    await drag(page, 50);
    expect(await tall(page)).toBeCloseTo(350, 0);
    expect(await el(page).evaluate((node) => (node as any).undo())).toBe(true);
    expect(await tall(page)).toBeCloseTo(300, 0);
    expect(await el(page).evaluate((node) => (node as any).bodyMaxHeight)).toBeNull();
    expect(errors).toEqual([]);
  });

  test("keeps the height the URL has", async ({ page }) => {
    const errors = await open(page, "bar-scroll.html");
    await page.goto(`${page.url()}?c.height=200`);
    await expect(el(page)).toHaveAttribute("data-gti-state", "ready");
    expect(await tall(page)).toBeCloseTo(200, 0);
    await expect(barButton(page, "Reset the view")).toBeVisible();
    expect(errors).toEqual([]);
  });

  test.describe("on a touch screen", () => {
    test.use({ hasTouch: true });

    test("is dragged by a finger, without scrolling the page", async ({ page, browserName }) => {
      test.skip(browserName !== "chromium", CHROMIUM_TOUCH);
      const errors = await ready(page, "bar-scroll.html");
      const at = await box(handle(page));
      const x = Math.round((at.left + at.right) / 2);
      const y = Math.round((at.top + at.bottom) / 2);
      const cdp = await page.context().newCDPSession(page);
      const touch = (type: "touchStart" | "touchMove" | "touchEnd", points: { x: number; y: number }[]) =>
        cdp.send("Input.dispatchTouchEvent", { type, touchPoints: points });
      await touch("touchStart", [{ x, y }]);
      for (let step = 1; step <= 10; step++) {
        await touch("touchMove", [{ x, y: y + step * 6 }]);
      }
      await touch("touchEnd", []);
      await expect.poll(() => tall(page)).toBeCloseTo(360, 0);
      expect(await page.evaluate(() => window.scrollY)).toBe(0);
      expect(errors).toEqual([]);
    });
  });
});

test("goes to the page typed in its readout", async ({ page }) => {
  const errors = await ready(page, "bar.html");
  await readout(page).click();
  const input = bar(page).locator(".gt-i-readout-jump input");
  await expect(input).toBeFocused();
  await expect(input).toHaveValue("1");
  await page.keyboard.type("9");
  await page.keyboard.press("Enter");
  expect(await pageOf(page)).toBe(9);
  await expect(readout(page)).toBeFocused();
  await expect(readout(page)).toHaveText("9/12");

  await readout(page).click();
  await page.keyboard.type("4");
  await page.keyboard.press("Escape");
  expect(await pageOf(page)).toBe(9);
  expect(errors).toEqual([]);
});

test("keeps its page controls in place as the page and readout change", async ({ page }) => {
  await ready(page, "bar.html");
  // (Across: the table's height changes with the structural rows on a page)
  const at = async () =>
    Promise.all(
      ["Previous page", "Next page"].map(async (name) => {
        const { left, right } = await box(barButton(page, name));
        return { left, right };
      }),
    );
  const first = await at();
  await page.evaluate(() => ((document.querySelector("gt-table") as any).page = 12));
  await expect(readout(page)).toHaveText("12/12");
  expect(await at()).toEqual(first);
  await readout(page).click();
  expect(await at()).toEqual(first);
});

test("is at least 300px wide, centred under a narrower table", async ({ page }) => {
  const errors = await ready(page, "bar-narrow.html");
  const table = await box(el(page).locator("table"));
  const shown = await box(bar(page));
  expect(table.width).toBeLessThan(300);
  expect(shown.width).toBeCloseTo(300, 0);
  expect((shown.left + shown.right) / 2).toBeCloseTo((table.left + table.right) / 2, 0);
  await expect(readout(page)).toHaveText("1/12");
  expect(errors).toEqual([]);
});

test("gives a narrow bar's room to the open search", async ({ page }) => {
  const errors = await ready(page, "bar-container.html");
  expect((await box(bar(page))).width).toBeCloseTo(300, 0);
  await expect(pages(page)).toBeVisible();
  await barButton(page, "Search the table").click();
  await expect(pages(page)).toBeHidden();
  expect((await box(field(page))).width).toBeGreaterThan(250);
  await page.keyboard.press("Escape");
  await expect(pages(page)).toBeVisible();
  expect(errors).toEqual([]);
});

test("sticks to the bottom of the view for a table of every row", async ({ page }) => {
  await page.setViewportSize({ width: 1000, height: 400 });
  const errors = await ready(page, "bar-sticky.html");
  await expect(pages(page)).toBeHidden();
  await expect(bar(page)).toHaveAttribute("data-gti-stick", "");
  const shown = await box(bar(page));
  expect(shown.bottom).toBeLessThanOrEqual(400);
  expect((await box(el(page).locator("table"))).bottom).toBeGreaterThan(400);
  // Over the rows, with a fill
  expect(await bar(page).evaluate((node) => getComputedStyle(node).backgroundColor)).not.toBe("rgba(0, 0, 0, 0)");

  // And, scrolled past the table, below it
  // (Firefox scrolls by a wheel slowly, a line at a time)
  await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight));
  await expect
    .poll(async () => (await box(bar(page))).top - (await box(el(page).locator("table"))).bottom)
    .toBeGreaterThanOrEqual(-1);
  expect(errors).toEqual([]);
});

test("keeps its room before hydration, so that what's below doesn't move", async ({ page }) => {
  const errors = await open(page, "bar-late.html");
  const gap = () =>
    page.evaluate(() => {
      const table = (document.querySelector("gt-table table") as HTMLElement).getBoundingClientRect();
      return (document.getElementById("after") as HTMLElement).getBoundingClientRect().top - table.bottom;
    });
  const before = await gap();
  await page.addScriptTag({ path: RUNTIME });
  await expect(el(page)).toHaveAttribute("data-gti-state", "ready");
  await expect(bar(page)).toBeVisible();
  expect(Math.abs((await gap()) - before)).toBeLessThan(1);
  expect(errors).toEqual([]);
});
