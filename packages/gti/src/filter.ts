/**
 * Column filters: which data rows a column's filter keeps, and the query that the filters make.
 *
 * A text filter keeps the rows whose cell in its column has its text (ignoring case and accents,
 * as the search does); a facet, the rows with one of the values chosen; a range, the rows with a
 * number within its bounds. Facets and ranges go by the column's values (the spec's `values`, in
 * the order of the column's ranks), so the query is in the data's terms:
 *
 *   {"and": [{"col": "status", "op": "in", "value": ["single-tier", null]},
 *            {"col": "population", "op": "gte", "value": 10000}]}
 *
 * (In a facet's values, `null` is a missing value.)
 */

import { type CellText, fold } from "./search";
import type { FilterSpec, FilterValue } from "./spec";

export type FilterClause =
  | { col: string; op: "contains"; value: string }
  | { col: string; op: "in"; value: FilterValue[] }
  | { col: string; op: "gte" | "lte"; value: number };

/** The filters on a table: rows are kept when every clause keeps them. */
export interface FilterQuery {
  and: FilterClause[];
}

/** A missing value, among the values of a facet (whose others are ranks). */
export const MISSING = -1;

interface FilterState {
  text: string;
  chosen: Set<number>;
  min: number | null;
  max: number | null;
}

/** The filter on one column, and the rows it keeps. */
export class ColumnFilter {
  readonly spec: FilterSpec;
  /** The column's index in the spec's `columns` (and among a row's data cells). */
  readonly index: number;
  /** The text a text filter keeps rows with, as typed. */
  text = "";
  /** That text, trimmed and folded. */
  needle = "";
  /** The values a facet keeps rows with: ranks, or `MISSING`. */
  chosen = new Set<number>();
  /** A range's bounds (either can be open). */
  min: number | null = null;
  max: number | null = null;
  private readonly ranks: readonly (number | null)[];
  private keys: Map<FilterValue, number> | null = null;

  constructor(spec: FilterSpec, index: number, ranks: readonly (number | null)[]) {
    this.spec = spec;
    this.index = index;
    this.ranks = ranks;
  }

  get column(): string {
    return this.spec.column;
  }

  get type(): FilterSpec["type"] {
    return this.spec.type;
  }

  /** Whether the filter leaves out any rows. */
  get active(): boolean {
    switch (this.spec.type) {
      case "text":
        return this.needle !== "";
      case "facet":
        return this.chosen.size > 0;
      case "range":
        return this.min !== null || this.max !== null;
    }
  }

  setText(text: string): void {
    this.text = text;
    this.needle = fold(text.trim());
  }

  clear(): void {
    this.setState({ text: "", chosen: new Set(), min: null, max: null });
  }

  /** A data row's value, for a facet: its rank, or `MISSING`. */
  key(row: number): number {
    return this.ranks[row] ?? MISSING;
  }

  /** A data row's value, as the data has it. */
  value(row: number): FilterValue {
    const rank = this.ranks[row];
    return rank == null ? null : (this.spec.values?.[rank] ?? null);
  }

  /** Whether the filter keeps a data row (whose cell in the column is `cell`). */
  keeps(row: number, cell: CellText | undefined): boolean {
    switch (this.spec.type) {
      case "text":
        return this.needle === "" || (cell?.folded.includes(this.needle) ?? false);
      case "facet":
        return this.chosen.size === 0 || this.chosen.has(this.key(row));
      case "range": {
        if (this.min === null && this.max === null) {
          return true;
        }
        const value = this.value(row);
        return (
          typeof value === "number" &&
          (this.min === null || value >= this.min) &&
          (this.max === null || value <= this.max)
        );
      }
    }
  }

  /** The filter, as query clauses (none if it isn't active). */
  clauses(): FilterClause[] {
    const col = this.column;
    switch (this.spec.type) {
      case "text":
        return this.needle === "" ? [] : [{ col, op: "contains", value: this.text.trim() }];
      case "facet": {
        if (this.chosen.size === 0) {
          return [];
        }
        // (In the order of the values, with missing ones last)
        const keys = Array.from(this.chosen).sort((a, b) => (a === MISSING ? 1 : b === MISSING ? -1 : a - b));
        return [{ col, op: "in", value: keys.map((key) => (key === MISSING ? null : this.valueOf(key))) }];
      }
      case "range": {
        const clauses: FilterClause[] = [];
        if (this.min !== null) {
          clauses.push({ col, op: "gte", value: this.min });
        }
        if (this.max !== null) {
          clauses.push({ col, op: "lte", value: this.max });
        }
        return clauses;
      }
    }
  }

  /**
   * The state that query clauses (all on this column) give the filter.
   *
   * @throws {RangeError} for a clause this kind of filter can't have, an `in` without values, or
   *   a second clause with the same `op`.
   */
  parse(clauses: readonly FilterClause[]): FilterState {
    const state: FilterState = { text: "", chosen: new Set(), min: null, max: null };
    const col = JSON.stringify(this.column);
    const ops = new Set<unknown>();
    for (const clause of clauses) {
      const { op, value } = clause as { op: unknown; value: unknown };
      if (ops.has(op)) {
        throw new RangeError(`${col} has more than one ${JSON.stringify(op)} clause`);
      }
      ops.add(op);
      if (this.spec.type === "text" && op === "contains" && typeof value === "string") {
        state.text = value;
      } else if (this.spec.type === "facet" && op === "in" && Array.isArray(value)) {
        if (value.length === 0) {
          throw new RangeError(`the "in" clause on ${col} needs at least one value`);
        }
        for (const item of value) {
          const key = item === null ? MISSING : this.rankOf(item);
          if (key === undefined) {
            throw new RangeError(`${JSON.stringify(item)} isn't a value of ${col}`);
          }
          state.chosen.add(key);
        }
      } else if (this.spec.type === "range" && (op === "gte" || op === "lte") && Number.isFinite(value)) {
        state[op === "gte" ? "min" : "max"] = value as number;
      } else {
        throw new RangeError(`${col} has a ${this.spec.type} filter, which can't be ${JSON.stringify(clause)}`);
      }
    }
    return state;
  }

  setState(state: FilterState): void {
    this.setText(state.text);
    this.chosen = state.chosen;
    this.min = state.min;
    this.max = state.max;
  }

  private valueOf(rank: number): FilterValue {
    return this.spec.values?.[rank] ?? null;
  }

  /** The rank of one of the column's values (not a missing one), if it's one of them. */
  rankOf(value: unknown): number | undefined {
    if (this.keys === null) {
      this.keys = new Map();
      this.spec.values?.forEach((item, rank) => {
        if (item !== null && !this.keys?.has(item)) {
          this.keys?.set(item, rank);
        }
      });
    }
    return this.keys.get(value as FilterValue);
  }
}

/** The query that filters make, or `null` if none is active. */
export function filterQuery(filters: readonly ColumnFilter[]): FilterQuery | null {
  const clauses = filters.flatMap((filter) => filter.clauses());
  return clauses.length === 0 ? null : { and: clauses };
}

/**
 * Set filters from a query (`null` clears them). Nothing changes if the query is bad.
 *
 * @throws {RangeError} for a query that isn't `{and: [...]}`, or a clause on a column that can't
 *   be filtered, or that its column's filter can't have.
 */
export function setFilterQuery(filters: readonly ColumnFilter[], query: FilterQuery | null): void {
  const clauses: unknown = query === null ? [] : (query as { and?: unknown } | undefined)?.and;
  if (!Array.isArray(clauses)) {
    throw new RangeError("a filter must be `{and: [...clauses]}`, or `null`");
  }
  const byColumn = new Map(filters.map((filter) => [filter.column, [] as FilterClause[]]));
  for (const clause of clauses as unknown[]) {
    const column = (clause as { col?: unknown } | null)?.col;
    const list = typeof column === "string" ? byColumn.get(column) : undefined;
    if (list === undefined) {
      throw new RangeError(`${JSON.stringify(column)} isn't a column that can be filtered`);
    }
    list.push(clause as FilterClause);
  }
  const states = filters.map((filter) => filter.parse(byColumn.get(filter.column) ?? []));
  filters.forEach((filter, i) => filter.setState(states[i] as FilterState));
}
