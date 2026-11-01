import { expect, type Page } from "@playwright/test";
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
