import { expect, type Locator, type Page, test } from "@playwright/test";
import { open, ready } from "./helpers";

// exibble three times over (24 rows, grp_b then grp_a, each with a summary row, then a grand
// summary row), with a title, a spanner, a footnote and a source note, in a body 300px high:
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
    expect(view.bottom - view.top).toBeLessThanOrEqual(300);
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
      // (A table as GT draws it, and one with a body that scrolls, taller than the table)
      const tables = el(page);
      await expect(tables.nth(0)).toHaveAttribute("data-gti-state", "ready");
      await expect(tables.nth(1)).toHaveAttribute("data-gti-state", "ready");
      await expect(tables.nth(1)).toHaveAttribute("data-gti-sticky", "");
      for (const at of [{ x: 0.01 }, { x: 0.12 }, { x: 0.5 }, { x: 0.99 }, { y: 0.3 }, { y: 0.95 }]) {
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

test.describe("a body that scrolls, by touch", () => {
  test.use({ hasTouch: true, isMobile: true, viewport: { width: 390, height: 700 } });

  test("scrolls on a swipe, under the column labels", async ({ page }) => {
    const errors = await ready(page, "scroll-column.html");
    const view = await port(page);
    const cdp = await page.context().newCDPSession(page);
    await cdp.send("Input.synthesizeScrollGesture", {
      x: Math.round((view.left + view.right) / 2),
      y: Math.round(view.bottom - 40),
      yDistance: -150,
      gestureSourceType: "touch",
      speed: 800,
    });
    await expect.poll(() => scrollTop(page)).toBeGreaterThan(50);
    expect((await rect(el(page).locator("thead"))).top).toBeCloseTo(view.top, 0);
    expect(errors).toEqual([]);
  });
});

/**
 * The lines drawn across a table, along a line through it (`x` or `y`, as a fraction of its width
 * or height): runs of up to 8px in a colour other than white, with the cells' contents hidden.
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
        const colour = `${pixels[i]},${pixels[i + 1]},${pixels[i + 2]}`;
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
