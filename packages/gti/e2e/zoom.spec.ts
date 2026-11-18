import { expect, type Locator, type Page, test } from "@playwright/test";
import { ready } from "./helpers";

// The tables of bar.spec.ts, pin.spec.ts and resize.spec.ts, under a CSS zoom of 1.25 (as a slide
// scaled to fit has): the sizes a table measures are on the page, 1.25 times its CSS pixels, which
// its styles are in.

const ZOOM = 1.25;
const el = (page: Page) => page.locator("gt-table");
const rect = (locator: Locator) =>
  locator.evaluate((node) => {
    const { left, right, width } = node.getBoundingClientRect();
    return { left, right, width };
  });

// The widths of the table's columns (their <col>s'), of the table and of the bar, in CSS pixels
const sizes = (page: Page) =>
  el(page).evaluate((node) => {
    const table = node.querySelector("table") as HTMLTableElement;
    return {
      columns: Array.from(table.querySelectorAll<HTMLElement>(":scope > colgroup > col"), (col) => parseFloat(col.style.width)),
      table: table.offsetWidth,
      bar: (node.querySelector(".gt-i-bar") as HTMLElement).offsetWidth,
    };
  });

test.describe("a table under a CSS zoom", () => {
  test("has the columns it has without it, and a bar as wide as it", async ({ page, browserName }) => {
    // (WebKit zooms a <col>'s width twice: see BUGS.md)
    test.skip(browserName === "webkit", "WebKit lays out a <col>'s width zoomed twice");
    await ready(page, "bar.html");
    const unzoomed = await sizes(page);
    const errors = await ready(page, "bar-zoom.html");
    const zoomed = await sizes(page);
    expect(zoomed.columns).toHaveLength(unzoomed.columns.length);
    // (Within the text's own small change in width at another size, where they'd be a quarter
    // wider measured on the page)
    const near = (width: number, expected: number) => expect(Math.abs(width - expected)).toBeLessThan(0.03 * expected + 1);
    zoomed.columns.forEach((width, i) => near(width, unzoomed.columns[i] as number));
    near(zoomed.table, unzoomed.table);
    expect(Math.abs(zoomed.bar - zoomed.table)).toBeLessThan(1);
    expect(errors).toEqual([]);
  });

  test("pins its columns next to each other", async ({ page }) => {
    const errors = await ready(page, "pin-zoom.html");
    await expect(el(page)).toHaveAttribute("data-gti-wide", "");
    const scroller = el(page).locator(".gt-i-scroller");
    await scroller.evaluate((div) => div.scrollTo(100, 0));
    await expect.poll(() => scroller.evaluate((div) => div.scrollLeft)).toBeGreaterThan(50);
    const row = el(page).locator("tbody tr", { has: page.locator('th.gt_stub:text-is("row_5")') });
    const stub = await rect(row.locator("> *").nth(1));
    const char = await rect(row.locator("> *").nth(2));
    expect(char.left).toBeCloseTo(stub.right, 0);
    // (The end of the part of the scroller its content shows in)
    const port = await scroller.evaluate((div, zoom) => div.getBoundingClientRect().left + (div.clientLeft + div.clientWidth) * zoom, ZOOM);
    expect((await rect(row.locator("> *").nth(8))).right).toBeCloseTo(port, 0);
    expect(errors).toEqual([]);
  });

  test("resizes a column as far as the pointer goes", async ({ page }) => {
    const errors = await ready(page, "resize-zoom.html");
    await el(page).evaluate((node) => {
      (window as any).resizes = [];
      node.addEventListener("gt-table-resize", (event) => (window as any).resizes.push((event as CustomEvent).detail));
    });
    const num = el(page).locator('th[id$="-num"]');
    const before = (await rect(num)).width;
    const handle = (await num.locator("> .gt-i-resizer").boundingBox()) as { x: number; y: number; width: number; height: number };
    const [x, y] = [handle.x + handle.width / 2, handle.y + handle.height / 2];
    await page.mouse.move(x, y);
    await page.mouse.down();
    await page.mouse.move(x + 50, y, { steps: 5 });
    await page.mouse.up();
    // (On the page, and in CSS pixels in the event: whole ones, rounded up)
    expect(Math.abs((await rect(num)).width - (before + 50))).toBeLessThan(2);
    const [event] = await page.evaluate(() => (window as any).resizes);
    expect(Math.abs(event.width - (before + 50) / ZOOM)).toBeLessThan(1.5);
    expect(errors).toEqual([]);
  });
});
