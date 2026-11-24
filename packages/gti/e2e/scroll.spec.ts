import { expect, type Locator, type Page, test } from "@playwright/test";
import { CHROMIUM_TOUCH, open, ready } from "./helpers";

// exibble three times over (24 rows, grp_b then grp_a, each with a summary row, then a grand
// summary row), with a title, a spanner, a footnote and a source note, in a body 340px high:
// on one page, selectable, with a search box; with groups shown as a column; and 200px high, 10
// rows to a page, with resizable columns and no text wrapping.

const el = (page: Page) => page.locator("gt-table");
const scroller = (page: Page) => el(page).locator(".gt-i-scroller");
const scrollTo = (page: Page, top: number) => scroller(page).evaluate((div, top) => (div.scrollTop = top), top);
const scrollTop = (page: Page) => scroller(page).evaluate((div) => div.scrollTop);

type Box = { top: number; bottom: number; left: number; right: number };
const rect = (locator: Locator): Promise<Box> =>
  locator.evaluate((node) => {
    const { top, bottom, left, right } = node.getBoundingClientRect();
    return { top, bottom, left, right };
  });

// The part of the scroller its content shows in
const port = (page: Page): Promise<Box> =>
  scroller(page).evaluate((div) => {
    const box = div.getBoundingClientRect();
    const top = box.top + div.clientTop;
    const left = box.left + div.clientLeft;
    return { top, bottom: top + div.clientHeight, left, right: left + div.clientWidth };
  });

// The row at a point in the page
const rowAt = (page: Page, x: number, y: number) =>
  page.evaluate(([x, y]) => {
    const tr = document.elementFromPoint(x as number, y as number)?.closest("tr");
    return tr?.parentElement?.tagName === "THEAD" ? "thead" : (tr?.textContent?.trim().split(/\s+/)[0] ?? null);
  }, [x, y]);

test.describe("a body that scrolls", () => {
  test("keeps the column labels, the group heading and the grand summary in view", async ({ page }) => {
    const errors = await ready(page, "scroll.html");
    const view = await port(page);
    expect(view.bottom - view.top).toBeLessThanOrEqual(340);
    await scrollTo(page, 400);
    await expect.poll(() => scrollTop(page)).toBe(400);

    const head = await rect(el(page).locator("thead"));
    expect(head.top).toBeCloseTo(view.top, 0);
    const heading = await rect(el(page).locator(".gt_group_heading").first());
    expect(heading.top).toBeLessThanOrEqual(head.bottom + 0.5);
    expect(heading.bottom).toBeGreaterThan(head.bottom + 10);
    const max = await rect(el(page).locator("tr.gt-i-stuck-bottom > *").first());
    expect(max.bottom).toBeCloseTo(view.bottom, 0);

    // Nothing shows past the sticky rows, over the container's padding
    const x = (view.left + view.right) / 2;
    expect(await rowAt(page, x, view.top + 1)).toBe("thead");
    expect(await rowAt(page, x, head.bottom + 2)).toBe("grp_b");
    expect(await rowAt(page, x, view.bottom - 1)).toBe("Max");
    expect(errors).toEqual([]);
  });

  test("lets the footnotes and source notes scroll in at the end", async ({ page }) => {
    await ready(page, "scroll.html");
    await scrollTo(page, 99999);
    const view = await port(page);
    const notes = await rect(el(page).locator("tfoot").last());
    expect(notes.bottom).toBeLessThanOrEqual(view.bottom + 0.5);
    expect(notes.top).toBeGreaterThan(view.top);
    // The second group's heading has taken the first's place
    const x = (view.left + view.right) / 2;
    const head = await rect(el(page).locator("thead"));
    expect(await rowAt(page, x, head.bottom + 2)).toBe("grp_a");
  });

  test("draws the table's borders as GT does", async ({ page }) => {
    for (const name of ["scroll-borders.html", "scroll-borders-column.html"]) {
      await open(page, name);
      // (A window as tall as the page, so that no screenshot scrolls: to show an element taller than
      // the window, Firefox centers it, at half a pixel when the heights differ by an odd number)
      const { width } = page.viewportSize() ?? { width: 1280 };
      await page.setViewportSize({ width, height: await page.evaluate(() => document.documentElement.scrollHeight) });
      // (A table as GT draws it, and one with a body that scrolls, taller than the table)
      const tables = el(page);
      await expect(tables.nth(0)).toHaveAttribute("data-gti-state", "ready");
      await expect(tables.nth(1)).toHaveAttribute("data-gti-state", "ready");
      await expect(tables.nth(1)).toHaveAttribute("data-gti-sticky", "");
      // (Across the middles of a body row and the grand summary row, as fractions of the height)
      const across = (row: Locator) =>
        row.evaluate((tr) => {
          const box = (tr.closest("table") as HTMLElement).getBoundingClientRect();
          const { top, bottom } = tr.getBoundingClientRect();
          return ((top + bottom) / 2 - box.top) / (box.height - 1);
        });
      const body = tables.nth(0).locator("tbody");
      const ys = [
        await across(body.locator("tr:has(> td.gt_row):not(:has(> .gt_summary_row, > .gt_grand_summary_row))").nth(6)),
        await across(body.locator("tr:has(> .gt_grand_summary_row)")),
      ];
      for (const at of [{ x: 0.01 }, { x: 0.12 }, { x: 0.5 }, { x: 0.99 }, ...ys.map((y) => ({ y }))]) {
        const lines = await borderLines(page, tables.nth(0).locator("table"), at);
        expect(lines.length).toBeGreaterThan(0);
        expect(await borderLines(page, tables.nth(1).locator("table"), at), `${name} at ${JSON.stringify(at)}`).toEqual(
          lines,
        );
      }
    }
  });

  test("shades the edges past which there's more to scroll to", async ({ page }) => {
    await ready(page, "scroll.html");
    const top = el(page).locator('.gt-i-shade[data-gti-edge="top"]');
    const bottom = el(page).locator('.gt-i-shade[data-gti-edge="bottom"]');
    await expect(top).not.toHaveAttribute("data-gti-shown");
    await expect(bottom).toHaveAttribute("data-gti-shown");

    await scrollTo(page, 400);
    await expect(top).toHaveAttribute("data-gti-shown");
    // Under the group heading stuck under the column labels, and over the grand summary row
    const heading = await rect(el(page).locator(".gt_group_heading").first());
    expect((await rect(top)).top).toBeCloseTo(heading.bottom, 0);
    const max = await rect(el(page).locator("tr.gt-i-stuck-bottom > *").first());
    expect((await rect(bottom)).bottom).toBeCloseTo(max.top, 0);
    const table = await rect(el(page).locator("table"));
    expect((await rect(top)).left).toBeCloseTo(table.left, 0);
    expect((await rect(top)).right).toBeCloseTo(table.right, 0);

    await scrollTo(page, 99999);
    await expect(bottom).not.toHaveAttribute("data-gti-shown");
    // (Out of the way)
    await expect(top).toHaveCSS("pointer-events", "none");
  });

  test("goes back to the top on another page", async ({ page }) => {
    const errors = await ready(page, "scroll-pages.html");
    await scrollTo(page, 120);
    await page.getByRole("button", { name: "Next", exact: true }).click();
    await expect.poll(() => scrollTop(page)).toBe(0);
    await expect(el(page).locator(".gt-i-pager")).toContainText("11–20 of 24 rows");
    // Text still doesn't wrap, and the sticky rows still stick
    await expect(el(page).locator("tbody .gt_row").first()).toHaveCSS("white-space", "nowrap");
    await scrollTo(page, 60);
    const view = await port(page);
    expect((await rect(el(page).locator("thead"))).top).toBeCloseTo(view.top, 0);
    expect(errors).toEqual([]);
  });

  test("draws the guide along a column down to the bottom of the part in view", async ({ page }) => {
    await ready(page, "scroll-pages.html");
    await scrollTo(page, 60);
    await expect.poll(() => scrollTop(page)).toBe(60);
    const th = el(page).locator("thead th.gt-i-resizable").nth(1);
    const box = await rect(th);
    await page.mouse.move((box.left + box.right) / 2, box.bottom - 4);
    const guide = el(page).locator(".gt-i-guide");
    await expect(guide).toBeVisible();
    const view = await port(page);
    // (From the label, in the column labels stuck at the top)
    expect((await rect(guide)).top).toBeCloseTo((await rect(th)).top, 0);
    expect((await rect(guide)).bottom).toBeCloseTo(view.bottom, 0);
  });

  test("keeps the select-all checkbox in view, and what has focus clear of the sticky rows", async ({ page }) => {
    await ready(page, "scroll.html");
    await scrollTo(page, 400);
    await el(page).locator("thead .gt-i-select input").click();
    expect(await el(page).evaluate((node) => (node as any).selection.length)).toBe(24);

    // A checkbox scrolled under the column labels is brought out from under them, and the heading
    await el(page).locator("tbody td.gt-i-select input").nth(5).focus();
    const heading = await rect(el(page).locator(".gt_group_heading").first());
    const box = await rect(el(page).locator("tbody td.gt-i-select input").nth(5));
    expect(box.top).toBeGreaterThanOrEqual(heading.bottom - 0.5);
  });

  test("shrinks to a search's matches, and says when there are none", async ({ page }) => {
    const errors = await ready(page, "scroll.html");
    const before = await port(page);
    await page.getByRole("searchbox").fill("zzz");
    await expect(el(page).locator("tr.gt-i-empty")).toBeVisible();
    const after = await port(page);
    expect(after.bottom - after.top).toBeLessThan(before.bottom - before.top);
    await expect(el(page).locator('.gt-i-shade[data-gti-edge="bottom"]')).not.toHaveAttribute("data-gti-shown");
    await page.getByRole("searchbox").fill("");
    await expect(el(page).locator("tr.gt-i-empty")).toHaveCount(0);
    expect(errors).toEqual([]);
  });
});

test.describe("a body that scrolls, on a page that scrolls", () => {
  test("keeps the column labels where they are from the start, with nothing showing above them", async ({ page }) => {
    const errors = await ready(page, "scroll-page.html");
    await page.evaluate(() => window.scrollTo(0, 500));
    // (The container's padding and the table's margin are above the labels, as GT has them, to
    // a whole pixel)
    const start = (await rect(el(page).locator("thead"))).top;
    expect(Math.abs(start - (await rect(scroller(page))).top - 18.5)).toBeLessThanOrEqual(0.5);
    const max = await rect(el(page).locator("tr.gt-i-stuck-bottom > *").first());
    const x = (max.left + max.right) / 2;
    for (const top of [1, 5, 30, 400]) {
      await scrollTo(page, top);
      await expect.poll(() => scrollTop(page)).toBe(top);
      expect((await rect(el(page).locator("thead"))).top).toBeCloseTo(start, 0);
      expect(await rowAt(page, x, start - 2)).toBeNull();
      // (And the grand summary row, stuck at the bottom, where it is too, with nothing below it)
      expect((await rect(el(page).locator("tr.gt-i-stuck-bottom > *").first())).bottom).toBeCloseTo(max.bottom, 0);
      expect(await rowAt(page, x, max.bottom + 2)).toBeNull();
    }
    expect(errors).toEqual([]);
  });

  test("scrolling past the end of the rows doesn't scroll the page", async ({ page }) => {
    const errors = await ready(page, "scroll-page.html");
    await page.evaluate(() => window.scrollTo(0, 500));
    const view = await port(page);
    await page.mouse.move(view.left + 20, view.bottom - 60);
    // (Firefox scrolls by a few lines for each, whatever its size)
    const atEnd = () => scroller(page).evaluate((div) => div.scrollTop + div.clientHeight >= div.scrollHeight - 1);
    for (let i = 0; i < 40 && !(await atEnd()); i++) {
      await page.mouse.wheel(0, 400);
    }
    // (And past the end)
    for (let i = 0; i < 4; i++) {
      await page.mouse.wheel(0, 400);
    }
    await expect.poll(atEnd).toBe(true);
    // (Wheel events done with, and none more to come)
    await page.waitForTimeout(300);
    expect(await page.evaluate(() => window.scrollY)).toBe(500);
    expect(errors).toEqual([]);
  });

  test("lets the page scroll while its rows are all in view", async ({ page }) => {
    const errors = await ready(page, "scroll-page.html");
    await page.evaluate(() => window.scrollTo(0, 500));
    await page.getByRole("searchbox").fill("zzz");
    await expect(el(page).locator("tr.gt-i-empty")).toBeVisible();
    const empty = await rect(el(page).locator("tr.gt-i-empty"));
    await page.mouse.move(empty.left + 20, (empty.top + empty.bottom) / 2);
    await page.mouse.wheel(0, 200);
    await expect.poll(() => page.evaluate(() => window.scrollY)).toBeGreaterThan(500);
    expect(errors).toEqual([]);
  });
});

test.describe("a body that scrolls, by touch", () => {
  // (Not `isMobile`, which lays the page out wider and zooms it out, away from the points touched)
  test.use({ hasTouch: true, viewport: { width: 390, height: 700 } });

  test("scrolls on a swipe, under the column labels", async ({ page, browserName }) => {
    test.skip(browserName !== "chromium", CHROMIUM_TOUCH);
    const errors = await ready(page, "scroll-column.html");
    const view = await port(page);
    const x = Math.round((view.left + view.right) / 2);
    const y = Math.round(view.bottom - 40);

    // A real touch drag up the body
    const cdp = await page.context().newCDPSession(page);
    const touch = (type: "touchStart" | "touchMove" | "touchEnd", points: { x: number; y: number }[]) =>
      cdp.send("Input.dispatchTouchEvent", { type, touchPoints: points });
    await touch("touchStart", [{ x, y }]);
    for (let dy = 15; dy <= 150; dy += 15) {
      await touch("touchMove", [{ x, y: y - dy }]);
    }
    await touch("touchEnd", []);
    await expect.poll(() => scrollTop(page)).toBeGreaterThan(50);
    expect((await rect(el(page).locator("thead"))).top).toBeCloseTo(view.top, 0);
    expect(errors).toEqual([]);
  });
});

/**
 * The lines drawn across a table, along a line through it (`x` or `y`, as a fraction of its width
 * or height): runs of up to 8px in a colour other than (nearly) white, with the cells' contents
 * hidden. (Nearly white: WebKit draws faint seams between rows)
 */
async function borderLines(page: Page, table: Locator, at: { x?: number; y?: number }): Promise<string[]> {
  await table.evaluate((node) => {
    for (const cell of Array.from(node.querySelectorAll<HTMLElement>("th, td"))) {
      cell.style.color = "transparent";
    }
    for (const input of Array.from(node.querySelectorAll<HTMLElement>("input"))) {
      input.style.visibility = "hidden";
    }
  });
  const png = (await table.screenshot()).toString("base64");
  return page.evaluate(
    async ({ png, at }) => {
      const img = new Image();
      img.src = `data:image/png;base64,${png}`;
      await img.decode();
      const canvas = document.createElement("canvas");
      canvas.width = img.width;
      canvas.height = img.height;
      const ctx = canvas.getContext("2d") as CanvasRenderingContext2D;
      ctx.drawImage(img, 0, 0);
      const pixels =
        at.x !== undefined
          ? ctx.getImageData(Math.round(at.x * (img.width - 1)), 0, 1, img.height).data
          : ctx.getImageData(0, Math.round((at.y as number) * (img.height - 1)), img.width, 1).data;
      const runs: [string, number][] = [];
      for (let i = 0; i < pixels.length; i += 4) {
        const light = Math.min(pixels[i] as number, pixels[i + 1] as number, pixels[i + 2] as number) >= 240;
        const colour = light ? "255,255,255" : `${pixels[i]},${pixels[i + 1]},${pixels[i + 2]}`;
        const last = runs[runs.length - 1];
        if (last !== undefined && last[0] === colour) {
          last[1]++;
        } else {
          runs.push([colour, 1]);
        }
      }
      return runs.filter(([colour, n]) => n <= 8 && colour !== "255,255,255").map(([colour, n]) => `${colour} x${n}`);
    },
    { png, at },
  );
}
