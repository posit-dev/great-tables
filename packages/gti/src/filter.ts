/**
 * Column filters: which data rows a column's filter keeps, and the query that the filters make.
 *
 * A text filter keeps the rows whose cell in its column has its text (ignoring case and accents,
 * as the search does); a facet, the rows with one of the values chosen; a range, the rows with a
 * number within its bounds; a date filter, the rows with a date (or date and time) within its
 * bounds. Facets, ranges and date filters go by the column's values (the spec's `values`, in the
 * order of the column's ranks), so the query is in the data's terms:
 *
 *   {"and": [{"col": "status", "op": "in", "value": ["single-tier", null]},
 *            {"col": "population", "op": "gte", "value": 10000},
 *            {"col": "founded", "op": "lte", "value": "1900-12-31"}]}
 *
 * (In a facet's values, `null` is a missing value. A date filter's bounds are ISO 8601 text: a
 * date, `"YYYY-MM-DD"`, or for a column of dates and times, either that, meaning its midnight, or a
 * date and time, `"YYYY-MM-DDTHH:MM"`, with seconds and up to six digits of their fraction if
 * wanted.)
 */

import { type CellText, fold } from "./search";
import type { ColumnKind, FilterSpec, FilterValue } from "./spec";

export type FilterClause =
  | { col: string; op: "contains"; value: string }
  | { col: string; op: "in"; value: FilterValue[] }
  | { col: string; op: "gte" | "lte"; value: number | string };

const DATE_TEXT = /^(\d{4})-(\d{2})-(\d{2})(?:T(\d{2}):(\d{2})(?::(\d{2})(?:\.(\d{1,9}))?)?)?$/;

/**
 * A date (or date and time) as ISO 8601 text, as text that sorts as it does
 * (`"YYYY-MM-DDTHH:MM:SS.fffffffff"`); or `null` if it isn't one. A bound can have up to six digits
 * of a second's fraction (as Python's times do), a value up to nine (as pandas' do).
 */
export function dateKey(text: string, digits = 9): string | null {
  const match = DATE_TEXT.exec(text);
  if (match === null) {
    return null;
  }
  const [, year, month, day, hour = "00", minute = "00", second = "00", fraction = ""] = match as unknown as string[];
  const y = Number(year);
  const m = Number(month);
  const d = Number(day);
  const leap = y % 4 === 0 && (y % 100 !== 0 || y % 400 === 0);
  const days = m === 2 ? (leap ? 29 : 28) : [4, 6, 9, 11].includes(m) ? 30 : 31;
  if (
    y < 1 ||
    m < 1 ||
    m > 12 ||
    d < 1 ||
    d > days ||
    Number(hour) > 23 ||
    Number(minute) > 59 ||
    Number(second) > 59 ||
    fraction.length > digits
  ) {
    return null;
  }
  return `${year}-${month}-${day}T${hour}:${minute}:${second}.${fraction.padEnd(9, "0")}`;
}

/** Whether ISO 8601 text is a date and time (rather than a date). */
export const hasTime = (text: string): boolean => text.includes("T");

/** The filters on a table: rows are kept when every clause keeps them. */
export interface FilterQuery {
  and: FilterClause[];
}

/** A missing value, among the values of a facet (whose others are ranks). */
export const MISSING = -1;

interface FilterState {
  text: string;
  chosen: Set<number>;
  min: number | string | null;
  max: number | string | null;
}

/** The filter on one column, and the rows it keeps. */
export class ColumnFilter {
  readonly spec: FilterSpec;
  /**
   * The column's index in the spec's `columns` (and among a row's data cells); -1 for a column
   * only for querying.
   */
  readonly index: number;
  /** A column only for querying's texts (the spec's `query_columns`), each data row's; or `null`. */
  readonly texts: readonly string[] | null;
  /** The text a text filter keeps rows with, as typed. */
  text = "";
  /** That text, trimmed and folded. */
  needle = "";
  /** The values a facet keeps rows with: ranks, or `MISSING`. */
  chosen = new Set<number>();
  /**
   * A range's bounds, or a date filter's (as ISO 8601 text); either can be open. Set them with
   * `setState()`, or valid ones.
   */
  min: number | string | null = null;
  max: number | string | null = null;
  /** Whether a date filter's column has times (a date bound is its midnight), not just dates. */
  readonly times: boolean;
  private readonly ranks: readonly (number | null)[];
  private keys: Map<FilterValue, number> | null = null;
  private folded: string[] | null = null;
  private dates: (string | null)[] | null = null;
  private bounds: [unknown, string | null, unknown, string | null] = [null, null, null, null];

  constructor(
    spec: FilterSpec,
    index: number,
    ranks: readonly (number | null)[],
    texts: readonly string[] | null = null,
    kind: ColumnKind | null = null,
  ) {
    this.spec = spec;
    this.index = index;
    this.ranks = ranks;
    this.texts = texts;
    this.times = kind === "datetime";
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
      case "date":
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
      case "text": {
        if (this.needle === "") {
          return true;
        }
        const texts = this.texts;
        const text = texts === null ? cell?.folded : (this.folded ??= texts.map(fold))[row];
        return text?.includes(this.needle) ?? false;
      }
      case "facet":
        return this.chosen.size === 0 || this.chosen.has(this.key(row));
      case "range": {
        if (this.min === null && this.max === null) {
          return true;
        }
        const value = this.value(row);
        return (
          typeof value === "number" &&
          (this.min === null || value >= (this.min as number)) &&
          (this.max === null || value <= (this.max as number))
        );
      }
      case "date": {
        if (this.min === null && this.max === null) {
          return true;
        }
        const rank = this.ranks[row];
        const key = rank == null ? null : this.dateKeys()[rank];
        const [low, high] = this.boundKeys();
        return key != null && (low === null || key >= low) && (high === null || key <= high);
      }
    }
  }

  /** The keys (as `dateKey()` makes them) of a date filter's values, in the order of their ranks. */
  dateKeys(): readonly (string | null)[] {
    return (this.dates ??= (this.spec.values ?? []).map((value) => (typeof value === "string" ? dateKey(value) : null)));
  }

  /** The keys of a date filter's bounds (kept while the bounds are the same). */
  private boundKeys(): [string | null, string | null] {
    const bounds = this.bounds;
    if (bounds[0] !== this.min) {
      bounds[0] = this.min;
      bounds[1] = typeof this.min === "string" ? dateKey(this.min) : null;
    }
    if (bounds[2] !== this.max) {
      bounds[2] = this.max;
      bounds[3] = typeof this.max === "string" ? dateKey(this.max) : null;
    }
    return [bounds[1], bounds[3]];
  }

  /**
   * Whether text is a bound a date filter can have: a date, or for a column with times, a date and
   * time.
   */
  isDateBound(text: string): boolean {
    return dateKey(text, 6) !== null && (this.times || !hasTime(text));
  }

  /** The rank of the value that a date filter's bound is (as a date or time, not text), if one is. */
  dateRank(text: string): number | undefined {
    const key = dateKey(text);
    const rank = key === null ? -1 : this.dateKeys().indexOf(key);
    return rank < 0 ? undefined : rank;
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
      case "range":
      case "date": {
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
      } else if (this.spec.type === "date" && (op === "gte" || op === "lte") && typeof value === "string") {
        if (!this.isDateBound(value)) {
          throw new RangeError(
            this.times
              ? `${JSON.stringify(value)} isn't a date ("YYYY-MM-DD") or date and time ("YYYY-MM-DDTHH:MM:SS"), for ${col}`
              : `${JSON.stringify(value)} isn't a date ("YYYY-MM-DD"), for ${col} (of dates, without times)`,
          );
        }
        state[op === "gte" ? "min" : "max"] = value;
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
