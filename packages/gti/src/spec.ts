/**
 * The GTI spec: what `<gt-table>` knows about a table beyond its static HTML.
 *
 * Producers (Great Tables' `great_tables/_gti/_spec.py`, later R gt) embed it as JSON in a
 * `<script type="application/json" data-gti-spec>` inside the element. These types mirror the
 * Python `TypedDict`s; fields may be added without a version change, so unknown ones are ignored.
 */

export const SPEC_VERSION = 1;

export type ColumnKind =
  | "number"
  | "string"
  | "boolean"
  | "date"
  | "datetime"
  | "time"
  | "duration"
  | "category"
  | "other";

export interface ColumnSpec {
  /** The column's name in the data; `null` for the stub column holding summary row labels. */
  id: string | null;
  role: "stub" | "data";
  kind: ColumnKind;
  align: string | null;
  /** The id of the column's label cell, if it has one. */
  header: string | null;
}

export interface SpannerSpec {
  id: string;
  level: number;
  columns: string[];
  header: string | null;
}

export interface StubSpec {
  columns: string[];
  groups_as_column: boolean;
}

export interface GroupSpec {
  id: string | null;
  /** The group's data rows, in display order. */
  rows: number[];
}

export interface GroupHeadingRow {
  group: string | null;
}

export interface SummaryRow {
  summary: string;
  group: string | null;
  side: "top" | "bottom";
}

export interface GrandSummaryRow {
  grand_summary: string;
  side: "top" | "bottom";
}

/** One `<tr>` of the table body: a data row's index, or a structural row. */
export type BodyRow = number | GroupHeadingRow | SummaryRow | GrandSummaryRow;

export interface Spec {
  version: number;
  /** The number of data rows; data rows are numbered 0 to `nrows - 1`, by position in the data. */
  nrows: number;
  columns: ColumnSpec[];
  spanners: SpannerSpec[];
  stub: StubSpec;
  groups: GroupSpec[];
  body: BodyRow[];
  /** Per sortable column, each data row's dense sort rank (`null` for a missing value). */
  ranks: Record<string, (number | null)[]>;
}

export class SpecError extends Error {
  override name = "SpecError";
}

const isObject = (x: unknown): x is Record<string, unknown> =>
  typeof x === "object" && x !== null && !Array.isArray(x);

const isIndex = (x: unknown, n: number): x is number =>
  Number.isInteger(x) && (x as number) >= 0 && (x as number) < n;

function isBodyRow(x: unknown, nrows: number): x is BodyRow {
  if (typeof x === "number") {
    return isIndex(x, nrows);
  }
  return isObject(x) && ("group" in x || "summary" in x || "grand_summary" in x);
}

/**
 * Parse and check a spec. Checks the structure the element relies on, not every field.
 *
 * @throws {SpecError} if the text isn't a spec this version of the runtime can use.
 */
export function parseSpec(text: string): Spec {
  let raw: unknown;
  try {
    raw = JSON.parse(text);
  } catch (err) {
    throw new SpecError(`the spec isn't valid JSON (${(err as Error).message})`);
  }

  if (!isObject(raw) || !Number.isInteger(raw.version)) {
    throw new SpecError("the spec has no version");
  }
  if (raw.version !== SPEC_VERSION) {
    throw new SpecError(`spec version ${raw.version} isn't supported (expected ${SPEC_VERSION})`);
  }

  const nrows = raw.nrows;
  if (!Number.isInteger(nrows) || (nrows as number) < 0) {
    throw new SpecError("`nrows` must be a non-negative integer");
  }
  for (const key of ["columns", "spanners", "groups", "body"]) {
    if (!Array.isArray(raw[key])) {
      throw new SpecError(`\`${key}\` must be an array`);
    }
  }
  if (!isObject(raw.stub) || !isObject(raw.ranks)) {
    throw new SpecError("`stub` and `ranks` must be objects");
  }

  const body = raw.body as unknown[];
  const bad = body.findIndex((row) => !isBodyRow(row, nrows as number));
  if (bad >= 0) {
    throw new SpecError(`\`body[${bad}]\` isn't a data row index or a structural row`);
  }

  for (const [column, ranks] of Object.entries(raw.ranks)) {
    if (!Array.isArray(ranks) || ranks.length !== nrows) {
      throw new SpecError(`\`ranks.${column}\` must have one entry per data row`);
    }
  }

  return raw as unknown as Spec;
}
