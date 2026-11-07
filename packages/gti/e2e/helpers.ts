import { expect, type Locator, type Page } from "@playwright/test";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const fixtures = join(dirname(fileURLToPath(import.meta.url)), ".fixtures");

/** Open a fixture page, returning the errors it logs (filled in as they happen). */
export async function open(page: Page, name: string): Promise<string[]> {
  const errors: string[] = [];
  page.on("pageerror", (err) => errors.push(err.message));
  page.on("console", (msg) => {
    if (msg.type() === "error") {
      errors.push(msg.text());
    }
  });
  await page.goto(pathToFileURL(join(fixtures, name)).href);
  return errors;
}

/** Open a fixture page with one table, once the table is hydrated. */
export async function ready(page: Page, name: string): Promise<string[]> {
  const errors = await open(page, name);
  await expect(page.locator("gt-table")).toHaveAttribute("data-gti-state", "ready");
  return errors;
}

/**
 * The body as shown: data row indices, and labels for the structural rows. With `visibleOnly`,
 * without the rows a search hides.
 */
export function shown(page: Page, visibleOnly = false): Promise<(number | string)[]> {
  return page.locator("gt-table").evaluate((node, visibleOnly) => {
    const el = node as any;
    return Array.from(node.querySelectorAll<HTMLTableRowElement>("tbody.gt_table_body > tr"))
      // (Not the row saying that nothing matches)
      .filter((tr) => el.bodyRow(tr) !== null && (!visibleOnly || tr.getClientRects().length > 0))
      .map((tr) => {
        const entry = el.bodyRow(tr);
        if (typeof entry === "number") {
          return entry;
        }
        if ("grand_summary" in entry) {
          return `grand:${entry.grand_summary}`;
        }
        return "summary" in entry ? `summary:${entry.summary}` : `group:${entry.group}`;
      });
  }, visibleOnly);
}

/** The body rows a reader sees. */
export const visible = (page: Page) => shown(page, true);

export const dataRows = (rows: (number | string)[]) => rows.filter((r) => typeof r === "number");

/** For each data row a reader sees: whether its cells are striped, and their background. */
export function striping(page: Page): Promise<{ striped: boolean; background: string }[]> {
  return page.locator("gt-table").evaluate((node) => {
    const el = node as any;
    return Array.from(node.querySelectorAll<HTMLTableRowElement>("tbody.gt_table_body > tr"))
      .filter((tr) => typeof el.bodyRow(tr) === "number" && tr.getClientRects().length > 0)
      .map((tr) => {
        const td = tr.querySelector("td") as HTMLElement;
        return { striped: td.classList.contains("gt_striped"), background: getComputedStyle(td).backgroundColor };
      });
  });
}

/**
 * Where the label cells of groups shown as a column are: the row each is on, whether it's that
 * row's first cell, the last row it spans, and whether its box fits the rows it spans.
 */
export function groupCells(page: Page) {
  return page.locator("gt-table").evaluate((node) => {
    const el = node as any;
    return Array.from(node.querySelectorAll("th.gt_stub_row_group"))
      .filter((cell) => cell.getClientRects().length > 0)
      .map((cell) => {
        const tr = cell.parentElement as HTMLTableRowElement;
        // The rows the cell spans: the next shown rows
        const span = Number(cell.getAttribute("rowspan"));
        const spanned = [tr];
        let next = tr.nextElementSibling as HTMLTableRowElement | null;
        while (spanned.length < span && next !== null) {
          if (next.getClientRects().length > 0) {
            spanned.push(next);
          }
          next = next.nextElementSibling as HTMLTableRowElement | null;
        }
        const box = cell.getBoundingClientRect();
        const top = spanned[0]?.getBoundingClientRect().top;
        const bottom = spanned[spanned.length - 1]?.getBoundingClientRect().bottom;
        return {
          label: cell.textContent?.trim(),
          row: el.bodyRow(tr),
          first: tr.firstElementChild === cell && tr.classList.contains("gt_row_group_first"),
          last: el.bodyRow(spanned[spanned.length - 1]),
          fits: Math.abs(box.top - (top ?? 0)) < 1 && Math.abs(box.bottom - (bottom ?? 0)) < 1,
        };
      });
  });
}

/**
 * The lines drawn across a table, along a line through it (down at `x` px from the page's left, or
 * across from the table's left at `y` as a fraction of its height, `width` px long): runs of up to
 * 8px in a colour other than white, with the cells' contents hidden. The table is shot as it shows
 * on the page.
 */
export async function borderLines(page: Page, table: Locator, at: { x?: number; y?: number; width?: number }): Promise<string[]> {
  await table.evaluate((node) => {
    for (const cell of Array.from(node.querySelectorAll<HTMLElement>("th, td"))) {
      cell.style.color = "transparent";
    }
    for (const input of Array.from(node.querySelectorAll<HTMLElement>("input"))) {
      input.style.visibility = "hidden";
    }
  });
  const box = await table.evaluate((node) => {
    const { top, left, height } = node.getBoundingClientRect();
    return { top, left, height };
  });
  const clip =
    at.x !== undefined
      ? { x: Math.round(at.x), y: box.top, width: 1, height: box.height }
      : { x: box.left, y: Math.round(box.top + (at.y as number) * (box.height - 1)), width: at.width as number, height: 1 };
  const png = (await page.screenshot({ clip })).toString("base64");
  return page.evaluate(async (png) => {
    const img = new Image();
    img.src = `data:image/png;base64,${png}`;
    await img.decode();
    const canvas = document.createElement("canvas");
    canvas.width = img.width;
    canvas.height = img.height;
    const ctx = canvas.getContext("2d") as CanvasRenderingContext2D;
    ctx.drawImage(img, 0, 0);
    const pixels = ctx.getImageData(0, 0, img.width, img.height).data;
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
  }, png);
}

/**
 * A long press with a finger at the middle of `locator` (Chromium's touch events, through the
 * DevTools protocol, as Playwright's touchscreen only taps).
 */
export async function longPress(page: Page, locator: Locator, ms = 700): Promise<void> {
  const box = await locator.boundingBox();
  if (box === null) {
    throw new Error("nothing to press");
  }
  const point = { x: box.x + box.width / 2, y: box.y + box.height / 2 };
  const cdp = await page.context().newCDPSession(page);
  await cdp.send("Input.dispatchTouchEvent", { type: "touchStart", touchPoints: [point] });
  await page.waitForTimeout(ms);
  await cdp.send("Input.dispatchTouchEvent", { type: "touchEnd", touchPoints: [] });
  await cdp.detach();
}
