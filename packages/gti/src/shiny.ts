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
// Built on its own (by scripts/build.mjs, into great_tables/js/gti-shiny.js), as a script that's
// run after the runtime (once per page, as a Shiny dependency), so it imports nothing of it but
// its types (and src/host.ts).

import type { GtTable } from "./gt-table";
import { applyState, type HostView, SELECT_EVENT, VIEW_EVENT, viewOf } from "./host";

export const MESSAGE = "great_tables.update_gti";
export const VIEW_TYPE = "great_tables.gti_view";

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

  const report = (table: GtTable) => {
    const id = outputOf(table);
    if (id === null || table.state !== "ready") {
      return;
    }
    shiny.setInputValue(`${id}_view:${VIEW_TYPE}`, viewOf(table));
    shiny.setInputValue(`${id}_rows`, table.rows);
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

  // (A table hydrated, with what the server set on it before)
  const hydrated = (table: GtTable) => {
    const id = outputOf(table);
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
