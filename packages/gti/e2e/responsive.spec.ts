import { expect, type Locator, type Page, test } from "@playwright/test";
import { borderLines, CHROMIUM_TOUCH, open, ready } from "./helpers";

// exibble three times over with every column (24 rows, grp_b then grp_a, each with a summary row,
// then a grand summary row), striped, with a title, a spanner, a footnote and a source note, in a
// container 360px wide: selectable, with a search box; with groups shown as a column, in a body
// 300px high; and in a page as narrow as a phone's.

const el = (page: Page) => page.locator("gt-table");
const scroller = (page: Page) => el(page).locator(".gt-i-scroller");
const scrollTo = (page: Page, left: number, top = 0) =>
  scroller(page).evaluate((div, [left, top]) => div.scrollTo(left as number, top as number), [left, top]);
const scrollLeft = (page: Page) => scroller(page).evaluate((div) => div.scrollLeft);

type Box = { top: number; bottom: number; left: number; right: number };
const rect = (locator: Locator): Promise<Box> =>
  locator.evaluate((node) => {
    const { top, bottom, left, right } = node.getBoundingClientRect();
    return { top, bottom, left, right };
  });

// The part of the scroller its content shows in
const port = (scroller: Locator): Promise<Box> =>
  scroller.evaluate((div) => {
    const box = div.getBoundingClientRect();
    const top = box.top + div.clientTop;
    const left = box.left + div.clientLeft;
    return { top, bottom: top + div.clientHeight, left, right: left + div.clientWidth };
  });

const stubCell = (page: Page, label: string) => el(page).locator("tbody th.gt_stub", { hasText: new RegExp(`^${label}$`) });
const middle = (box: Box) => (box.left + box.right) / 2;

test.describe("a table wider than its container", () => {
  test("scrolls sideways with the selection column and the stub pinned", async ({ page }) => {
    const errors = await ready(page, "wide.html");
    await expect(el(page)).toHaveAttribute("data-gti-wide", "");
    const view = await port(scroller(page));
    expect(view.right - view.left).toBe(360);
    const cell = el(page).locator("tbody td.gt_row:not(.gt-i-select)").first();
    const before = await rect(cell);

    await scrollTo(page, 200);
    await expect.poll(() => scrollLeft(page)).toBe(200);
    expect((await rect(cell)).left).toBeCloseTo(before.left - 200, 0);
    const select = await rect(el(page).locator("tbody td.gt-i-select").first());
    expect(select.left).toBeCloseTo(view.left, 0);
    const stub = await rect(stubCell(page, "row_5"));
    expect(stub.left).toBeCloseTo(select.right, 0);
    // The select-all checkbox's cell, over the column labels; a summary row's label; and a pinned
    // checkbox still works, over the cells scrolled under it
    expect((await rect(el(page).locator("thead th.gt-i-select"))).left).toBeCloseTo(view.left, 0);
    expect((await rect(stubCell(page, "Total").first())).left).toBeCloseTo(select.right, 0);
    await el(page).locator("tbody td.gt-i-select input").nth(1).click();
    expect(await el(page).evaluate((node) => (node as any).selection)).toEqual([5]);
    // (As does a row clicked, in the container that can have focus)
    await el(page).locator("tbody td.gt_row:not(.gt-i-select)").nth(20).click();
    expect(await el(page).evaluate((node) => (node as any).selection)).toHaveLength(2);
    expect(errors).toEqual([]);
  });

  test("keeps its title, group headings and notes in view", async ({ page }) => {
    await ready(page, "wide.html");
    const view = await port(scroller(page));
    const title = el(page).locator(".gt_title > .gt-i-inview");
    for (const left of [0, 150, 99999]) {
      await scrollTo(page, left);
      await expect.poll(async () => middle(await rect(title))).toBeCloseTo(middle(view), 0);
      const heading = await rect(el(page).locator(".gt_group_heading > .gt-i-inview").first());
      expect(heading.left).toBeGreaterThanOrEqual(view.left);
      expect(heading.left).toBeLessThan(view.left + 10);
      for (const note of [".gt_footnote", ".gt_sourcenote"]) {
        const box = await rect(el(page).locator(`${note} > .gt-i-inview`));
        expect(box.left).toBeGreaterThanOrEqual(view.left);
        expect(box.right).toBeLessThanOrEqual(view.right + 0.5);
      }
    }
    // And the row saying that nothing matches
    await page.getByRole("searchbox").fill("zzz");
    await expect(el(page).locator("tr.gt-i-empty")).toBeVisible();
    await scrollTo(page, 150);
    await expect
      .poll(async () => middle(await rect(el(page).locator("tr.gt-i-empty .gt-i-inview"))))
      .toBeCloseTo(middle(view), 0);
  });

  test("sticks both ways in a body that scrolls", async ({ page }) => {
    const errors = await ready(page, "wide-column.html");
    await scrollTo(page, 150, 400);
    const view = await port(scroller(page));
    const head = await rect(el(page).locator("thead"));
    expect(head.top).toBeCloseTo(view.top, 0);
    // The corner over the pinned columns, and the grand summary row's label at the bottom
    const corner = await rect(el(page).locator("thead th.gt-i-select"));
    expect(corner.left).toBeCloseTo(view.left, 0);
    const max = await rect(stubCell(page, "Max"));
    expect(max.bottom).toBeCloseTo(view.bottom, 0);
    expect(max.left).toBeCloseTo(corner.right, 0);
    // The body scrolls under the pinned columns, which scroll under the column labels
    const stub = await rect(el(page).locator("tbody th.gt_stub").nth(10));
    expect(stub.left).toBeGreaterThan(view.left);
    const at = (x: number, y: number) =>
      page.evaluate(([x, y]) => {
        const hit = document.elementFromPoint(x as number, y as number)?.closest("th, td");
        return hit === null || hit === undefined ? null : hit.className;
      }, [x, y]);
    expect(await at(stub.right - 2, head.bottom + 30)).toMatch(/gt_stub/);
    expect(await at(corner.right - 2, (head.top + head.bottom) / 2)).toMatch(/gt-i-select/);
    expect(await at(stub.right + 4, max.top + 2)).toMatch(/gt_grand_summary_row/);
    expect(errors).toEqual([]);
  });

  test("shades the edges past which there are columns to scroll to", async ({ page }) => {
    await ready(page, "wide.html");
    const start = el(page).locator('.gt-i-shade[data-gti-edge="left"]');
    const end = el(page).locator('.gt-i-shade[data-gti-edge="right"]');
    await expect(start).not.toHaveAttribute("data-gti-shown");
    await expect(end).toHaveAttribute("data-gti-shown");

    await scrollTo(page, 100);
    await expect(start).toHaveAttribute("data-gti-shown");
    await expect(end).toHaveAttribute("data-gti-shown");
    // Along the pinned columns and the container's end, from the column labels down
    const view = await port(scroller(page));
    const stub = await rect(stubCell(page, "row_5"));
    expect((await rect(start)).left).toBeCloseTo(stub.right, 0);
    expect((await rect(end)).right).toBeCloseTo(view.right, 0);
    const labels = await rect(el(page).locator("thead tr.gt_col_headings").first());
    expect((await rect(start)).top).toBeCloseTo(labels.top, 0);

    await scrollTo(page, 99999);
    await expect(end).not.toHaveAttribute("data-gti-shown");
    await expect(start).toHaveCSS("pointer-events", "none");
  });

  test("says it scrolls, until it first does", async ({ page }) => {
    await ready(page, "wide.html");
    const hint = el(page).locator(".gt-i-hint");
    await expect(hint).toBeVisible();
    await expect(hint).toHaveText("Scroll for more →");
    await expect(hint).toHaveAttribute("aria-hidden", "true");
    // By the end of the part in view
    const view = await port(scroller(page));
    expect((await rect(hint)).right).toBeCloseTo(view.right - 8, 0);
    await scrollTo(page, 40);
    await expect(hint).toHaveCount(0);
    await scrollTo(page, 0);
    await page.waitForTimeout(100);
    await expect(hint).toHaveCount(0);
  });

  test("is a region that scrolls with the keyboard", async ({ page, browserName }) => {
    test.skip(browserName === "webkit", "Playwright's WebKit doesn't scroll on arrow keys (not even the page)");
    await ready(page, "wide.html");
    const region = page.getByRole("region", { name: "exibble" });
    await expect(region).toHaveAttribute("tabindex", "0");
    await region.focus();
    await page.keyboard.press("ArrowRight");
    await page.keyboard.press("ArrowRight");
    await expect.poll(() => scrollLeft(page)).toBeGreaterThan(0);
    await expect(el(page).locator('.gt-i-shade[data-gti-edge="left"]')).toHaveAttribute("data-gti-shown");
  });

  test("draws the table's borders as GT does", async ({ page, browserName }) => {
    await page.setViewportSize({ width: 1280, height: 4400 });
    for (const name of ["wide-borders.html", "wide-borders-column.html"]) {
      await open(page, name);
      // (A table as GT draws it, in a container it fits in, and one wider than its container)
      const tables = el(page);
      await expect(tables.nth(0)).toHaveAttribute("data-gti-state", "ready");
      await expect(tables.nth(1)).toHaveAttribute("data-gti-wide", "");
      await expect(tables.nth(0)).not.toHaveAttribute("data-gti-wide");
      await page.addStyleTag({ content: "gt-table .gt-i-shade, gt-table .gt-i-hint { visibility: hidden }" });
      const gt = tables.nth(0).locator("table");
      const pinned = tables.nth(1).locator("table");
      const view = await port(tables.nth(1).locator(".gt-i-scroller"));
      // (Where each table starts on the page, before the wide one scrolls)
      const start = (await rect(gt)).left;
      const pinnedStart = (await rect(pinned)).left;
      const width = view.right - pinnedStart;
      const edge = (await rect(tables.nth(1).locator("tbody th.gt_stub").first())).right - pinnedStart;

      for (const shift of [0, 120]) {
        await tables.nth(1).locator(".gt-i-scroller").evaluate((div, left) => (div.scrollLeft = left), shift);
        await page.waitForTimeout(50);
        // Through the pinned columns, along their edge, and through the columns scrolled under them
        // (but for Firefox and WebKit, which draw a faint corner where the edge meets the double
        // line above the grand summary rows)
        const along = browserName === "chromium" ? [edge - 1] : [];
        for (const x of [5, 30, ...along, edge + 20, width - 30]) {
          const into = x < edge ? x : x + shift;
          const lines = await borderLines(page, gt, { x: start + into });
          expect(lines.length).toBeGreaterThan(0);
          expect(await borderLines(page, pinned, { x: pinnedStart + x }), `${name} at x=${x}, scrolled ${shift}`).toEqual(lines);
        }
        if (shift === 0) {
          for (const y of [0.3, 0.95]) {
            const lines = await borderLines(page, gt, { y, width });
            expect(await borderLines(page, pinned, { y, width }), `${name} at y=${y}`).toEqual(lines);
          }
        }
      }
    }
  });

  test("is left alone while it fits, and pinned once it doesn't", async ({ page }) => {
    const errors = await open(page, "wide-borders.html");
    const table = el(page).nth(0);
    await expect(table).toHaveAttribute("data-gti-state", "ready");
    await expect(table).not.toHaveAttribute("data-gti-wide");
    await expect(table.locator("table")).toHaveCSS("border-collapse", "collapse");
    await expect(table.locator(".gt-i-hint, .gt-i-inview, .gt-i-shade")).toHaveCount(0);
    await expect(table.locator(".gt-i-scroller")).not.toHaveAttribute("role");

    // Its container narrows
    await table.evaluate((node) => ((node.parentElement as HTMLElement).style.width = "300px"));
    await expect(table).toHaveAttribute("data-gti-wide", "");
    await expect(table.locator("table")).toHaveCSS("border-collapse", "separate");
    await expect(table.locator(".gt-i-hint")).toBeVisible();
    await expect(table.locator(".gt-i-scroller")).toHaveAttribute("role", "region");
    // And widens again
    await table.evaluate((node) => ((node.parentElement as HTMLElement).style.width = "2000px"));
    await expect(table).not.toHaveAttribute("data-gti-wide");
    await expect(table.locator(".gt-i-hint")).not.toHaveAttribute("data-gti-shown");
    await expect(table.locator(".gt-i-scroller")).not.toHaveAttribute("role");
    await expect(table.locator(".gt-i-pinned").first()).not.toHaveCSS("position", "sticky");
    expect(errors).toEqual([]);
  });
});

test.describe("a table wider than a phone", () => {
  // (Not `isMobile`, which lays the page out wider and zooms it out, away from the points touched)
  test.use({ hasTouch: true, viewport: { width: 390, height: 700 } });

  test("fits the page, and scrolls sideways on a swipe with the stub pinned", async ({ page, browserName }) => {
    test.skip(browserName !== "chromium", CHROMIUM_TOUCH);
    const errors = await ready(page, "wide-phone.html");
    await expect(el(page)).toHaveAttribute("data-gti-wide", "");
    // The page doesn't scroll sideways; the table does
    expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(390);
    const view = await port(scroller(page));
    expect(view.right).toBeLessThanOrEqual(390);

    // A real touch drag along a row
    const y = Math.round((await rect(stubCell(page, "row_5"))).top + 10);
    const x = Math.round(view.right - 40);
    const cdp = await page.context().newCDPSession(page);
    const touch = (type: "touchStart" | "touchMove" | "touchEnd", points: { x: number; y: number }[]) =>
      cdp.send("Input.dispatchTouchEvent", { type, touchPoints: points });
    await touch("touchStart", [{ x, y }]);
    for (let dx = 15; dx <= 150; dx += 15) {
      await touch("touchMove", [{ x: x - dx, y }]);
    }
    await touch("touchEnd", []);
    await expect.poll(() => scrollLeft(page)).toBeGreaterThan(50);
    expect((await rect(stubCell(page, "row_5"))).left).toBeCloseTo(view.left, 0);
    expect(middle(await rect(el(page).locator(".gt_title > .gt-i-inview")))).toBeCloseTo(middle(view), 0);
    await expect(el(page).locator(".gt-i-hint")).toHaveCount(0);
    expect(errors).toEqual([]);
  });
});
