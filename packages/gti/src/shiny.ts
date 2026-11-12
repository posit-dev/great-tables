// GTI tables in a Shiny app (`render_gt()`, in great_tables/shiny.py): their state as the app's
// inputs, and what the server sets on them (with `update_gti()`).
//
// A table that's the only `<gt-table>` in a Shiny output (whose `id` is the output's) gives the
// server its view (as input `<id>_view`, read by the input handler of type `VIEW_TYPE`), the rows
// it keeps, in the order shown (`<id>_rows`), and those selected (`<id>_selection`): once it's
// hydrated, after each change the reader makes (and after a linked table's selection, which
// changes the rows it keeps), and after each change the server makes (as setting the element's
// properties fires no events). Shiny sends an input's value only when it changes. The server's
// changes come as custom messages (`MESSAGE`), for an output; one for a table that isn't
// hydrated yet (as the output's just been rendered) is kept until it is.
//
// A table whose rows are the server's (in kernel mode, `i_scale()`: its element has
// `data-gti-server`, their count) is remote: its source is a `ShinySource`, which asks the
// server for each page (and a facet's counts) with a request (`Shiny.shinyapp.makeRequest()`) to
// the output's handler (its id, then `ASK_SUFFIX`). Its rows input then gives its view (of type
// `ROWS_TYPE`), whose rows the server finds.
//
// Built on its own (by scripts/build.mjs, into great_tables/js/gti-shiny.js), as a script that's
// run after the runtime (once per page, as a Shiny dependency), so it imports nothing of it but
// its types (and src/host.ts).

import type { GtTable } from "./gt-table";
import { applyState, type HostView, SELECT_EVENT, ServerSource, VIEW_EVENT, viewOf } from "./host";

export const MESSAGE = "great_tables.update_gti";
export const VIEW_TYPE = "great_tables.gti_view";
export const ROWS_TYPE = "great_tables.gti_rows";
export const ASK_SUFFIX = "_gti";

/** What the server sets on a table, in an output. */
export interface Update {
  id: string;
  view?: Partial<Pick<HostView, "filter" | "sort" | "search">>;
  selection?: number[];
}

/** What the glue uses of Shiny's `window.Shiny`. */
export interface ShinyLike {
  setInputValue(name: string, value: unknown): void;
  addCustomMessageHandler(type: string, handler: (message: Update) => void): void;
  shinyapp?: {
    makeRequest(
      method: string,
      args: unknown[],
      onSuccess: (value: unknown) => void,
      onError: (err: string) => void,
      blobs: null,
    ): void;
  };
}

/** The rows of a table in kernel mode, from the server: each answer is asked for with a request. */
export class ShinySource extends ServerSource {
  constructor(
    private readonly shiny: ShinyLike,
    private readonly method: string,
    nrows: number,
  ) {
    super(nrows);
  }

  protected ask(kind: string, content: Record<string, unknown>): Promise<unknown> {
    return new Promise((resolve, reject) => {
      const app = this.shiny.shinyapp;
      if (app === undefined) {
        reject(new Error("Shiny can't be asked for the rows"));
      } else {
        app.makeRequest(this.method, [{ kind, ...content }], resolve, (err) => reject(new Error(err)), null);
      }
    });
  }
}

/** How many rows a table whose rows are the server's has, or `null` if they're the page's. */
export function serverRows(table: GtTable): number | null {
  const count = table.getAttribute("data-gti-server");
  return count === null ? null : Number(count);
}

const isTable = (node: unknown): node is GtTable =>
  node instanceof Element && node.localName === "gt-table";

/** The table in a Shiny output (the only `<gt-table>` in it), or `null`. */
export function tableIn(output: Element | null): GtTable | null {
  if (output === null) {
    return null;
  }
  const tables = Array.from(output.children).filter(isTable);
  return tables.length === 1 ? (tables[0] as GtTable) : null;
}

/** The id of the Shiny output a table is the table of, or `null`. */
export function outputOf(table: GtTable): string | null {
  const output = table.parentElement;
  if (output === null || !output.classList.contains("shiny-html-output") || output.id === "") {
    return null;
  }
  return tableIn(output) === table ? output.id : null;
}

/** Follow the page's tables, for Shiny; returns a function that stops. */
export function start(shiny: ShinyLike, doc: Document = document): () => void {
  const pending = new Map<string, Update>();
  // (The tables whose source is the server, once it's set)
  const served = new WeakSet<GtTable>();

  const report = (table: GtTable) => {
    const id = outputOf(table);
    if (id === null || table.state !== "ready") {
      return;
    }
    const view = viewOf(table);
    shiny.setInputValue(`${id}_view:${VIEW_TYPE}`, view);
    if (serverRows(table) === null) {
      shiny.setInputValue(`${id}_rows`, table.rows);
    } else {
      // (The server finds the rows the view keeps, on every page)
      const { filter, sort, search, hidden } = view;
      shiny.setInputValue(`${id}_rows:${ROWS_TYPE}`, { filter, sort, search, hidden });
    }
    shiny.setInputValue(`${id}_selection`, table.selection);
  };
  const reportAll = () => {
    for (const table of Array.from(doc.querySelectorAll("gt-table")) as GtTable[]) {
      report(table);
    }
  };

  const apply = (table: GtTable, update: Update) => {
    applyState(table, update.view ?? null, update.selection ?? null);
    report(table);
  };

  // (A table hydrated, with its rows from the server if they're its, and what the server set on
  // it before)
  const hydrated = (table: GtTable) => {
    const id = outputOf(table);
    const nrows = serverRows(table);
    if (id !== null && nrows !== null && !served.has(table)) {
      served.add(table);
      table.source = new ShinySource(shiny, `${id}${ASK_SUFFIX}`, nrows);
    }
    const update = id === null ? undefined : pending.get(id);
    if (id !== null && update !== undefined) {
      pending.delete(id);
      apply(table, update);
    } else {
      report(table);
    }
  };

  // (As a table's hydrated, or one that is is put in the page)
  const observer = new MutationObserver((records) => {
    const tables = new Set<GtTable>();
    for (const record of records) {
      if (record.type === "attributes" && isTable(record.target)) {
        tables.add(record.target);
      }
      for (const node of Array.from(record.addedNodes)) {
        if (node instanceof Element) {
          for (const table of [node, ...Array.from(node.querySelectorAll("gt-table"))]) {
            if (isTable(table)) {
              tables.add(table);
            }
          }
        }
      }
    }
    for (const table of tables) {
      if (table.isConnected && table.state === "ready") {
        hydrated(table);
      }
    }
  });
  observer.observe(doc.documentElement, {
    subtree: true,
    childList: true,
    attributes: true,
    attributeFilter: ["data-gti-state"],
  });

  const fromReader = (event: Event) => {
    if (isTable(event.target)) {
      report(event.target);
    }
  };
  // (A linked table's selection changes the rows the others keep, after it's shared)
  const fromLink = () => queueMicrotask(reportAll);
  doc.addEventListener(VIEW_EVENT, fromReader);
  doc.addEventListener(SELECT_EVENT, fromLink);

  shiny.addCustomMessageHandler(MESSAGE, (update) => {
    const table = tableIn(doc.getElementById(update.id));
    if (table !== null && table.state === "ready") {
      apply(table, update);
    } else {
      // (Merged with one kept before, the later's parts winning)
      const before = pending.get(update.id);
      pending.set(update.id, {
        id: update.id,
        view: { ...before?.view, ...update.view },
        selection: update.selection ?? before?.selection,
      });
    }
  });

  for (const table of Array.from(doc.querySelectorAll("gt-table")) as GtTable[]) {
    if (table.state === "ready") {
      hydrated(table);
    }
  }

  return () => {
    observer.disconnect();
    doc.removeEventListener(VIEW_EVENT, fromReader);
    doc.removeEventListener(SELECT_EVENT, fromLink);
  };
}

// (Once, in a page with Shiny)
declare global {
  interface Window {
    Shiny?: ShinyLike;
    __gtiShiny?: boolean;
  }
}
if (typeof window !== "undefined" && window.Shiny !== undefined && !window.__gtiShiny) {
  window.__gtiShiny = true;
  start(window.Shiny);
}
