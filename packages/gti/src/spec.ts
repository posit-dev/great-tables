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

export interface StripingSpec {
  /** Whether alternate data rows have striped stub cells. */
  stub: boolean;
  /** Whether alternate data rows have striped body cells. */
  body: boolean;
}

export type SelectionMode = "single" | "multiple";

const SELECTION_MODES: readonly unknown[] = ["single", "multiple", null];

export interface ControlsSpec {
  /** Whether column labels are buttons that sort by their column. */
  sorting: boolean;
  /** Whether there's a search box. */
  search: boolean;
  /** Whether column labels have handles for resizing their columns. */
  resizing: boolean;
  /** Whether data rows can be selected: one at a time, several, or not at all. */
  selection: SelectionMode | null;
  /**
   * Whether the search and page controls are in one bar below the table (GTI's), rather than a
   * search box above the table and page controls below it (as `pagination.type` says). Without
   * it, the latter.
   */
  bar?: boolean;
}

/** How page controls look: page numbers, previous/next only, first/previous/next/last, or a page input. */
export type PaginationType = "numbers" | "simple" | "full" | "jump";

export interface PaginationSpec {
  /** Whether rows are split into pages. */
  enabled: boolean;
  /** The number of data rows on a page, to start with. */
  page_size: number;
  /** The page sizes the reader can choose from (with `size_select`). */
  page_sizes: number[];
  /** Whether the reader can choose the page size. */
  size_select: boolean;
  /** Whether to say which rows are shown ("11–20 of 310 rows"). */
  info: boolean;
  type: PaginationType;
}

export interface DisplaySpec {
  /** Whether data rows are highlighted under the pointer, or when tapped on a touch screen. */
  highlight: boolean;
  /** Whether rows are compact (already in the table's CSS, as the producer made it). */
  compact: boolean;
  /** Whether cell text wraps; if not, text cut off by a column's width ends in an ellipsis. */
  wrap: boolean;
}

export interface LayoutSpec {
  /**
   * The most the table can take up (a CSS length) before its body scrolls, under column labels
   * that stay in view; `null` to grow with its content.
   */
  height: string | null;
  /**
   * What the table does when it's wider than its container: `"scroll"` sideways, with the stub
   * pinned (and the title and notes kept in view); `null` to scroll sideways as GT's table does.
   */
  responsive: ResponsiveMode | null;
}

export type ResponsiveMode = "scroll";

/** How a column is filtered: by the text it shows, a choice of its values, or a range of its numbers. */
export type FilterType = "text" | "facet" | "range";

const FILTER_TYPES: readonly unknown[] = ["text", "facet", "range"];

/** A data value, as JSON holds it (dates and times as ISO 8601 text). */
export type FilterValue = string | number | boolean | null;

export interface FilterSpec {
  column: string;
  type: FilterType;
  /**
   * A facet or range column's distinct values, in the order of its ranks (a data row's value is
   * `values[rank]`); `null` for a text filter.
   */
  values: FilterValue[] | null;
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
  striping: StripingSpec;
  controls: ControlsSpec;
  pagination: PaginationSpec;
  display: DisplaySpec;
  layout: LayoutSpec;
  /** The columns readers can filter by, in column order. Without it, none. */
  filters?: FilterSpec[];
}

export class SpecError extends Error {
  override name = "SpecError";
}

const isObject = (x: unknown): x is Record<string, unknown> =>
  typeof x === "object" && x !== null && !Array.isArray(x);

const isPageSize = (x: unknown): x is number => Number.isInteger(x) && (x as number) > 0;

const PAGINATION_TYPES: readonly unknown[] = ["numbers", "simple", "full", "jump"];

const isIndex = (x: unknown, n: number): x is number =>
  Number.isInteger(x) && (x as number) >= 0 && (x as number) < n;

const isFilterValue = (x: unknown): x is FilterValue =>
  x === null || typeof x === "string" || typeof x === "boolean" || (typeof x === "number" && Number.isFinite(x));

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
  const striping = raw.striping;
  if (!isObject(striping) || typeof striping.stub !== "boolean" || typeof striping.body !== "boolean") {
    throw new SpecError("`striping` must say whether the stub and body are striped");
  }
  const controls = raw.controls;
  if (
    !isObject(controls) ||
    typeof controls.sorting !== "boolean" ||
    typeof controls.search !== "boolean" ||
    typeof controls.resizing !== "boolean" ||
    !SELECTION_MODES.includes(controls.selection)
  ) {
    throw new SpecError(
      "`controls` must say whether sorting, search and resizing are on, and how rows are selected",
    );
  }
  if (!(controls.bar === undefined || typeof controls.bar === "boolean")) {
    throw new SpecError("`controls.bar` must be `true` or `false`, if given");
  }
  const pagination = raw.pagination;
  if (
    !isObject(pagination) ||
    typeof pagination.enabled !== "boolean" ||
    typeof pagination.size_select !== "boolean" ||
    typeof pagination.info !== "boolean" ||
    !isPageSize(pagination.page_size) ||
    !Array.isArray(pagination.page_sizes) ||
    !pagination.page_sizes.every(isPageSize) ||
    !PAGINATION_TYPES.includes(pagination.type)
  ) {
    throw new SpecError(
      "`pagination` must have a positive `page_size` and `page_sizes`, a known `type`, and say " +
        "whether pages, a page size select and page info are on",
    );
  }

  const display = raw.display;
  if (
    !isObject(display) ||
    typeof display.highlight !== "boolean" ||
    typeof display.compact !== "boolean" ||
    typeof display.wrap !== "boolean"
  ) {
    throw new SpecError("`display` must say whether rows are highlighted and compact, and text wraps");
  }
  const layout = raw.layout;
  if (
    !isObject(layout) ||
    !(layout.height === null || (typeof layout.height === "string" && layout.height.trim() !== ""))
  ) {
    throw new SpecError("`layout` must have a `height`: a CSS length, or `null`");
  }
  if (!(layout.responsive === null || layout.responsive === "scroll")) {
    throw new SpecError('`layout.responsive` must be "scroll" or `null`');
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

  const filters = raw.filters;
  if (filters !== undefined) {
    if (!Array.isArray(filters)) {
      throw new SpecError("`filters` must be an array, if given");
    }
    const allRanks = raw.ranks as Record<string, unknown>;
    filters.forEach((filter: unknown, i) => {
      const column = isObject(filter) ? filter.column : undefined;
      const ranks =
        typeof column === "string" && Object.prototype.hasOwnProperty.call(allRanks, column)
          ? allRanks[column]
          : undefined;
      const values = isObject(filter) ? filter.values : undefined;
      if (
        !isObject(filter) ||
        typeof column !== "string" ||
        !FILTER_TYPES.includes(filter.type) ||
        (filter.type === "text"
          ? values != null
          : !Array.isArray(values) ||
            !values.every(isFilterValue) ||
            !Array.isArray(ranks) ||
            !ranks.every((rank) => rank === null || isIndex(rank, values.length)))
      ) {
        throw new SpecError(
          `\`filters[${i}]\` must name a column and a known \`type\`, with \`values\` for every rank of a facet or range`,
        );
      }
    });
  }

  return raw as unknown as Spec;
}
