/**
 * Column filters: which data rows a column's filter keeps, and the query that the filters make.
 *
 * A text filter keeps the rows whose cell in its column has its text (ignoring case and accents,
 * as the search does); a facet, the rows with one of the values chosen; a range, the rows with a
 * number within its bounds; a date filter, the rows with a date (or date and time) within its
 * bounds; a bool filter, the rows with the one value chosen (true, false, or a missing one).
 * Facets, ranges, date and bool filters go by the column's values (the spec's `values`, in the
 * order of the column's ranks), so the query is in the data's terms:
 *
 *   {"and": [{"col": "status", "op": "in", "value": ["single-tier", null]},
 *            {"col": "is_city", "op": "in", "value": [true]},
 *            {"col": "population", "op": "gte", "value": 10000},
 *            {"col": "founded", "op": "lte", "value": "1900-12-31"}]}
 *
 * (In a facet's values, and a bool filter's one value, `null` is a missing value. A date filter's bounds are ISO 8601 text: a
 * date, `"YYYY-MM-DD"`, or for a column of dates and times, either that, meaning its midnight, or a
 * date and time, `"YYYY-MM-DDTHH:MM"`, with seconds and up to six digits of their fraction if
 * wanted.)
 *
 * A clause `{"col": "population", "op": "is_null"}`, on a column with any filter, keeps the rows
 * whose value is missing (the spec's `missing`: `null`, or NaN in a column of floats). A clause
 * `{"col": "name", "op": "matches", "value": "^st\\."}`, on a column with a text filter, keeps the
 * rows whose cell's text (as a `contains` has it, but not folded) has a match of the pattern (see
 * `pattern.ts`). No column's filter has either: the table keeps them, as it does a group.
 *
 * A part of the query can also be a group: `{"or": [...]}`, keeping the rows any of its parts
 * keeps; `{"and": [...]}`, those every one does; or `{"not": part}`, those its part doesn't (with a
 * clause leaving out a row whose value is missing, `not` keeps it). Groups nest; the filters keep
 * the query's clauses that aren't in a group, and the table keeps its groups (`FilterGroup`s).
 */

import { checkPattern, type PatternError, patternRegExp } from "./pattern";
import { type CellText, fold } from "./search";
import type { ColumnKind, FilterSpec, FilterValue } from "./spec";

export type FilterClause =
  | { col: string; op: "contains"; value: string }
  | { col: string; op: "matches"; value: string }
  | { col: string; op: "in"; value: FilterValue[] }
  | { col: string; op: "gte" | "lte"; value: number | string }
  | { col: string; op: "is_null" };

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

/**
 * A part of a query: a clause; or a group of parts, keeping the rows any of them keeps (`or`),
 * every one of them does (`and`), or the one part doesn't (`not`).
 */
export type FilterItem = FilterClause | { or: FilterItem[] } | { and: FilterItem[] } | { not: FilterItem };

/** The filters on a table: rows are kept when every part keeps them. */
export interface FilterQuery {
  and: FilterItem[];
}

/** Whether a part of a query is a clause (rather than a group). */
export const isClause = (item: FilterItem): item is FilterClause => "col" in item;

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
  /** The values a facet keeps rows with (a bool filter's, at most one): ranks, or `MISSING`. */
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
  private gaps: Set<number> | null = null;

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
      case "bool":
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

  /** Whether a data row's value is missing (as an `is_null` clause has it). */
  isMissing(row: number): boolean {
    // (Without the spec's `missing`, the rows without a rank)
    this.gaps ??= new Set(this.spec.missing ?? this.ranks.flatMap((rank, i) => (rank == null ? [i] : [])));
    return this.gaps.has(row);
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
      case "bool":
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
      case "facet":
      case "bool": {
        if (this.chosen.size === 0) {
          return [];
        }
        return [{ col, op: "in", value: this.values(this.chosen) }];
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
   * @throws {RangeError} for a clause this kind of filter can't have, an `in` without values (or a
   *   bool filter's with more than one), or a second clause with the same `op`.
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
      } else if ((this.spec.type === "facet" || this.spec.type === "bool") && op === "in" && Array.isArray(value)) {
        if (value.length === 0) {
          throw new RangeError(`the "in" clause on ${col} needs at least one value`);
        }
        if (this.spec.type === "bool" && value.length > 1) {
          throw new RangeError(`the "in" clause on ${col} (a bool filter) can have only one value`);
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

  /**
   * A clause on this column as a group has it: an `in`'s values once each, in the order of the
   * column's values (with a missing one last).
   *
   * @throws {RangeError} for a clause the filter can't have (as `parse()` does), a `contains`
   *   without text (which keeps every row, and so means nothing in a group), or a `matches` whose
   *   pattern can't be read.
   */
  groupClause(clause: FilterClause): FilterClause {
    const col = this.column;
    if (clause.op === "is_null") {
      return { col, op: "is_null" };
    }
    if (clause.op === "matches") {
      const { value } = clause as { value: unknown };
      if (this.spec.type !== "text" || typeof value !== "string") {
        throw new RangeError(`${JSON.stringify(col)} has a ${this.spec.type} filter, which can't be ${JSON.stringify(clause)}`);
      }
      try {
        return { col, op: "matches", value: checkPattern(value) };
      } catch (err) {
        // (Counted in characters, as Python counts them)
        const { at, message } = err as PatternError;
        const place = at >= value.length ? "the end" : `character ${Array.from(value.slice(0, at)).length + 1}`;
        throw new RangeError(`the pattern of the "matches" clause on ${JSON.stringify(col)} can't be read: ${message}, at ${place}`);
      }
    }
    const state = this.parse([clause]);
    if (clause.op === "contains" && fold(state.text.trim()) === "") {
      throw new RangeError(`the "contains" clause on ${JSON.stringify(col)} needs text, in an "or" or a "not"`);
    }
    return clause.op === "in"
      ? { col, op: "in", value: this.values(state.chosen) }
      : ({ col, op: clause.op, value: clause.value } as FilterClause);
  }

  /** Whether a clause on this column (one `groupClause()` gives) keeps a data row, whose cell in the column is `cell`. */
  matcher(clause: FilterClause): (row: number, cell: CellText | undefined) => boolean {
    const filter = new ColumnFilter(this.spec, this.index, this.ranks, this.texts, this.times ? "datetime" : null);
    filter.setState(this.parse([clause]));
    return (row, cell) => filter.keeps(row, cell);
  }

  // A facet's values (ranks, or `MISSING`) as the data has them, in their order, with a missing one last
  private values(keys: Set<number>): FilterValue[] {
    const sorted = Array.from(keys).sort((a, b) => (a === MISSING ? 1 : b === MISSING ? -1 : a - b));
    return sorted.map((key) => (key === MISSING ? null : this.valueOf(key)));
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

type RowTest = (row: number, cells: readonly (CellText | undefined)[]) => boolean;
type Find = (column: unknown) => ColumnFilter;

/**
 * A part of a query that's a group (an `or`, or a `not`), or an `is_null` or `matches` clause,
 * which no one column's filter has; the table keeps it, beside the filters.
 */
export class FilterGroup {
  /** The group, as `setFilterQuery()` writes it. */
  readonly item: FilterItem;
  /** The filters of the columns it has clauses on, once each, in the order of its clauses. */
  readonly filters: readonly ColumnFilter[];
  /**
   * Whether it needs a row's cells' text (for a `contains` or a `matches` on one of the table's
   * columns).
   */
  readonly texts: boolean;
  private readonly test: RowTest;

  constructor(item: FilterItem, find: Find) {
    const filters = new Set<ColumnFilter>();
    let texts = false;
    const make = (part: FilterItem): RowTest => {
      if (isClause(part)) {
        const filter = find(part.col);
        filters.add(filter);
        if (part.op === "is_null") {
          return (row) => filter.isMissing(row);
        }
        if (part.op === "matches") {
          const re = patternRegExp(part.value);
          const own = filter.texts;
          texts ||= own === null;
          return (row, cells) => {
            const text = own === null ? cells[filter.index]?.text : own[row];
            return text !== undefined && re.test(text);
          };
        }
        const keeps = filter.matcher(part);
        texts ||= part.op === "contains" && filter.texts === null;
        return (row, cells) => keeps(row, cells[filter.index]);
      }
      if ("not" in part) {
        const test = make(part.not);
        return (row, cells) => !test(row, cells);
      }
      const tests = ("or" in part ? part.or : part.and).map(make);
      return "or" in part
        ? (row, cells) => tests.some((test) => test(row, cells))
        : (row, cells) => tests.every((test) => test(row, cells));
    };
    this.item = item;
    this.test = make(item);
    this.filters = Array.from(filters);
    this.texts = texts;
  }

  /** Whether the group keeps a data row, whose cells are `cells` (by the columns' indexes). */
  keeps(row: number, cells: readonly (CellText | undefined)[]): boolean {
    return this.test(row, cells);
  }
}

/** The query that filters (and groups) make, or `null` if none is active. */
export function filterQuery(filters: readonly ColumnFilter[], groups: readonly FilterGroup[] = []): FilterQuery | null {
  const items: FilterItem[] = [...filters.flatMap((filter) => filter.clauses()), ...groups.map((group) => group.item)];
  return items.length === 0 ? null : { and: items };
}

// The kind of group a part of a query is, if it's one: an object with just an "or", "and" or "not"
function groupKind(item: unknown): "or" | "and" | "not" | null {
  if (item === null || typeof item !== "object" || Array.isArray(item)) {
    return null;
  }
  const keys = Object.keys(item);
  const [key] = keys;
  return keys.length === 1 && (key === "or" || key === "and" || key === "not") ? key : null;
}

// A group's parts
function groupParts(item: unknown, kind: "or" | "and"): unknown[] {
  const parts = (item as Record<string, unknown>)[kind];
  if (!Array.isArray(parts) || parts.length === 0) {
    throw new RangeError(`an "${kind}" group needs a list of at least one part`);
  }
  return parts;
}

// A part of a query in a group, checked, as the table writes it: an "and" in an "and" (or an "or"
// in an "or") is spliced into it, a group of one part is that part, and a clause is as
// `groupClause()` gives it
function normalItem(item: unknown, find: Find): FilterItem {
  const kind = groupKind(item);
  if (kind === "not") {
    return { not: normalItem((item as { not: unknown }).not, find) };
  }
  if (kind === null) {
    return find((item as { col?: unknown } | null)?.col).groupClause(item as FilterClause);
  }
  const items = groupParts(item, kind).flatMap((part) => {
    const normal = normalItem(part, find);
    return kind in normal ? ((normal as Record<string, FilterItem[]>)[kind] as FilterItem[]) : [normal];
  });
  if (kind === "and") {
    const seen = new Set<string>();
    for (const part of items.filter(isClause)) {
      const key = JSON.stringify([part.col, part.op]);
      if (seen.has(key)) {
        throw new RangeError(`${JSON.stringify(part.col)} has more than one ${JSON.stringify(part.op)} clause`);
      }
      seen.add(key);
    }
  }
  return items.length === 1 ? (items[0] as FilterItem) : ({ [kind]: items } as FilterItem);
}

// The clauses that no column's filter has
const GROUPED: readonly unknown[] = ["is_null", "matches"];

/**
 * Set filters from a query (`null` clears them), giving the query's groups (its `or` and `not`
 * parts, and its `is_null` and `matches` clauses) for the table to keep. Its other clauses that aren't in a group
 * (or are in an `and` that isn't in one) go to their columns' filters; its groups are as
 * `normalItem()` writes them, and in the order given. Nothing changes if the query is bad.
 *
 * @throws {RangeError} for a query that isn't `{and: [...]}`, a part that isn't a clause or a
 *   group, a group without parts, a clause on a column that can't be filtered, or that its
 *   column's filter can't have (or in a group, a `contains` without text), or a second `is_null`
 *   (or `matches`) clause on a column.
 */
export function setFilterQuery(filters: readonly ColumnFilter[], query: FilterQuery | null): FilterGroup[] {
  const items: unknown = query === null ? [] : (query as { and?: unknown } | undefined)?.and;
  if (!Array.isArray(items)) {
    throw new RangeError("a filter must be `{and: [...parts]}`, or `null`");
  }
  const byName = new Map(filters.map((filter) => [filter.column, filter]));
  const find: Find = (column) => {
    const filter = typeof column === "string" ? byName.get(column) : undefined;
    if (filter === undefined) {
      throw new RangeError(`${JSON.stringify(column)} isn't a column that can be filtered`);
    }
    return filter;
  };
  const byColumn = new Map(filters.map((filter) => [filter, [] as FilterClause[]]));
  const groups: FilterItem[] = [];
  // (The `is_null` and `matches` clauses not in a group, by their columns and ops)
  const seen = new Set<string>();
  const add = (item: FilterItem): void => {
    if (isClause(item) && !GROUPED.includes(item.op)) {
      byColumn.get(find(item.col))?.push(item);
    } else if ("and" in item) {
      item.and.forEach(add);
    } else {
      if (isClause(item)) {
        const key = JSON.stringify([item.col, item.op]);
        if (seen.has(key)) {
          throw new RangeError(`${JSON.stringify(item.col)} has more than one ${JSON.stringify(item.op)} clause`);
        }
        seen.add(key);
      }
      groups.push(item);
    }
  };
  const visit = (item: unknown): void => {
    const kind = groupKind(item);
    if (kind === "and") {
      groupParts(item, kind).forEach(visit);
    } else if (kind !== null || GROUPED.includes((item as { op?: unknown } | null)?.op)) {
      add(normalItem(item, find));
    } else {
      byColumn.get(find((item as { col?: unknown } | null)?.col))?.push(item as FilterClause);
    }
  };
  items.forEach(visit);
  const states = filters.map((filter) => filter.parse(byColumn.get(filter) ?? []));
  const made = groups.map((item) => new FilterGroup(item, find));
  filters.forEach((filter, i) => filter.setState(states[i] as FilterState));
  return made;
}
