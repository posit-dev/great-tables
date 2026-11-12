// Where a table's rows come from: the table's own, in the page (`LocalSource`), or a server's. The
// table asks its source which rows its view keeps, with a query in JSON's terms (that a server
// can run as well), and takes the answer as it's given, or, from a source that answers later,
// when it comes (showing the rows it had till then, and dropping an answer to a query it's since
// asked again). A remote table (whose spec has `remote`: its page has only some of its rows)
// asks its source for each page instead, with the rows' HTML.

import { ColumnFilter, type FilterQuery, MISSING, setFilterQuery } from "./filter";
import { type CellText, rowMatches, searchTerms } from "./search";
import type { SortKey } from "./sort";
import type { FilterSpec, FilterValue, Spec } from "./spec";

/** What a table asks its source: the rows its view keeps. */
export interface RowQuery {
  /** The search, as typed (see `GtTable.search`). */
  search: string;
  /** The columns hidden, which the search leaves out (as it does those that aren't searchable). */
  hidden: string[];
  /** The filters (see `GtTable.filter`). */
  filter: FilterQuery | null;
  /** The keys (of the spec's `link.on` column) of each linked table's selection that filters it. */
  links: FilterValue[][];
}

/** The rows a query keeps. */
export interface RowAnswer {
  /** Per data row, 1 if it's kept; `null` if every row is. */
  matched: Uint8Array | null;
  count: number;
}

/** The rows a query keeps of each of a facet's values (its rank, or `MISSING`), by value. */
export type FacetCounts = Map<number, number>;

/** What a remote table asks its source: a page of the rows its view keeps, sorted. */
export interface PageQuery extends RowQuery {
  /** The sort (see `GtTable.sort`). */
  sort: SortKey[];
  /** Where the page starts, among the rows kept (from 0). */
  start: number;
  /** The rows on a page; `null` for one page of every row. */
  size: number | null;
}

/** A page of the rows a query keeps. */
export interface PageAnswer {
  /** The number of rows the query keeps (on every page). */
  count: number;
  /** Where the page starts: the query's, or the last page's, if the query's is past it. */
  start: number;
  /** The page's data rows, in order. */
  rows: number[];
  /**
   * The HTML of the page's rows that the table doesn't have yet (or of all of them): one `<tr>`
   * of the table body per row, in the order of `rows`, as the table's own are.
   */
  html: string;
}

/** Where a table's rows come from. Each answer is given at once, or as a promise of it. */
export interface DataSource {
  rows(query: RowQuery): RowAnswer | Promise<RowAnswer>;
  /** The rows a query keeps of each value of a facet's column (or a bool filter's). */
  facet(query: RowQuery, column: string): FacetCounts | Promise<FacetCounts>;
  /** A page of the rows a query keeps, for a remote table (one whose spec has `remote`). */
  page?(query: PageQuery): PageAnswer | Promise<PageAnswer>;
}

/** A filter of the spec's, on its column (or a column only for querying), or `null` without one. */
export function specFilter(spec: Spec, filter: FilterSpec): ColumnFilter | null {
  const id = filter.column;
  const index = spec.columns.findIndex((column) => column.id === id);
  const query = spec.query_columns?.find((column) => column.id === id);
  return index === -1 && query === undefined
    ? null
    : new ColumnFilter(filter, index, spec.ranks[id] ?? [], query?.texts, spec.columns[index]?.kind ?? query?.kind);
}

/**
 * The rows of the table in the page, from its spec and the text of its rows' cells (each data
 * row's, one per column of the spec, made when a query first needs them).
 */
export class LocalSource implements DataSource {
  private readonly filters: ColumnFilter[] = [];

  constructor(
    private readonly spec: Spec,
    private readonly texts: () => CellText[][],
  ) {
    for (const filterSpec of spec.filters ?? []) {
      const filter = specFilter(spec, filterSpec);
      if (filter !== null && !this.filters.some((other) => other.column === filter.column)) {
        this.filters.push(filter);
      }
    }
  }

  rows(query: RowQuery): RowAnswer {
    const matched = new Uint8Array(this.spec.nrows);
    let count = 0;
    this.each(query, (row) => {
      matched[row] = 1;
      count++;
    });
    return { matched, count };
  }

  facet(query: RowQuery, column: string): FacetCounts {
    const filter = this.filters.find((other) => other.column === column);
    const counts: FacetCounts = new Map();
    this.each(query, (row) => {
      const key = filter?.key(row) ?? MISSING;
      counts.set(key, (counts.get(key) ?? 0) + 1);
    });
    return counts;
  }

  // Call `each` with each data row that the search, the filters, and the linked tables'
  // selections keep
  private each(query: RowQuery, each: (row: number) => void): void {
    const { nrows, columns, link } = this.spec;
    const groups = setFilterQuery(this.filters, query.filter);
    const filters = this.filters.filter((filter) => filter.active);
    const terms = searchTerms(query.search);
    const links = query.links.map((keys) => new Set(keys));
    // (The columns the search leaves out, by their indexes)
    const skipped = new Set(columns.flatMap((column, i) => (column.searchable === false || query.hidden.includes(column.id as string) ? [i] : [])));
    const texts =
      terms.length > 0 || filters.some((filter) => filter.type === "text") || groups.some((group) => group.texts)
        ? this.texts()
        : null;
    for (let row = 0; row < nrows; row++) {
      const cells = texts?.[row] ?? [];
      if (
        (terms.length === 0 || rowMatches(skipped.size === 0 ? cells : cells.filter((_, i) => !skipped.has(i)), terms)) &&
        filters.every((filter) => filter.keeps(row, cells[filter.index])) &&
        groups.every((group) => group.keeps(row, cells)) &&
        links.every((keys) => keys.has(link?.keys[row] as FilterValue))
      ) {
        each(row);
      }
    }
  }
}
