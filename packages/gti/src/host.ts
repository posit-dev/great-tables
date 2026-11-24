// What the glue of a host whose server reads and sets a table's state (src/widget.ts, for an
// anywidget, and src/shiny.ts, for Shiny) shares: the table's view, as the server has it, setting
// the server's view and selection on the table, and a source whose rows the server has (for a
// table in kernel mode, as great_tables/_gti/_kernel.py serves it).
//
// Built into each glue, which is run after the runtime, so this imports nothing of it but its
// types.

import type { FilterQuery } from "./filter";
import type { GtTable, State } from "./gt-table";
import type { SortKey } from "./sort";
import type { DataSource, FacetCounts, PageAnswer, PageQuery, RowAnswer, RowQuery } from "./source";

// (As gt-table.ts has them, as test/gt-table.test.ts checks)
export const VIEW_EVENT = "gt-table-view";
export const SELECT_EVENT = "gt-table-select";

/** The view, as the server has it (for Python, whose keys are snake case). */
export interface HostView {
  filter: FilterQuery | null;
  sort: SortKey[];
  search: string;
  page: number;
  page_size: number | null;
  hidden: string[];
  group_by: string | null;
}

/** The table's view, from its properties. */
export function viewOf(table: GtTable): HostView {
  return {
    filter: table.filter,
    sort: table.sort,
    search: table.search,
    page: table.page,
    page_size: table.pageSize,
    hidden: table.hiddenColumns,
    group_by: table.groupBy,
  };
}

export const same = (a: unknown, b: unknown): boolean => JSON.stringify(a) === JSON.stringify(b);

// (Which a table is in once it's done hydrating: interactive, or not, which it then stays)
export const SETTLED: (State | null)[] = ["ready", "static", "error"];

/**
 * Set the server's filter, sort and search (those it has), and selection (if it has one), on the
 * table, where they differ from its own. An error (as with a filter the table can't apply, its
 * columns having changed) is logged, and the rest isn't set.
 */
export function applyState(
  table: GtTable,
  view: Partial<Pick<HostView, "filter" | "sort" | "search">> | null,
  selection: number[] | null,
): void {
  try {
    if (view != null) {
      if (view.filter !== undefined && !same(view.filter, table.filter)) {
        table.filter = view.filter;
      }
      if (view.sort !== undefined && !same(view.sort, table.sort)) {
        table.sort = view.sort;
      }
      if (view.search !== undefined && view.search !== table.search) {
        table.search = view.search;
      }
    }
    if (selection != null && !same(selection, table.selection)) {
      table.selection = selection;
    }
  } catch (err) {
    console.error(`<gt-table>: ${(err as Error).message}`);
  }
}

/**
 * The rows of a table in kernel mode, from the server: each answer is asked for (with what's
 * asked, its `kind`, and the query), as the host's glue sends it.
 */
export abstract class ServerSource implements DataSource {
  constructor(private readonly nrows: number) {}

  /** Ask the server (for a "page", a "facet"'s counts, or the "rows" a query keeps). */
  protected abstract ask(kind: string, content: Record<string, unknown>): Promise<unknown>;

  rows(query: RowQuery): Promise<RowAnswer> {
    return this.ask("rows", { query }).then((answer) => {
      const rows = answer as number[];
      const matched = new Uint8Array(this.nrows);
      for (const row of rows) {
        matched[row] = 1;
      }
      return { matched, count: rows.length };
    });
  }

  facet(query: RowQuery, column: string): Promise<FacetCounts> {
    return this.ask("facet", { query, column }).then((answer) => new Map(answer as [number, number][]));
  }

  page(query: PageQuery): Promise<PageAnswer> {
    return this.ask("page", { query }).then((answer) => answer as PageAnswer);
  }
}
