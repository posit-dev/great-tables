/**
 * The `<gt-table>` custom element.
 *
 * It wraps a static Great Tables table and adds interactivity on top of it (hydration), rather
 * than rendering a table of its own: it reads the table's spec, maps each body row to its entry,
 * and sorts, searches and pages by moving and hiding the table's own `<tr>`s, so styles, footnote
 * marks and the like move with their rows.
 *
 * `data-gti-state` says how far it got: `pending` (waiting for the document to be parsed),
 * `empty` (no table yet), `static` (a table without a spec, left as it is), `error` (the spec is
 * unusable or doesn't match the table; see the console), or `ready`.
 */

import { type Placed, placeCells, type Side, TableBorders } from "./borders";
import { viewCode } from "./code";
import { toCSV as csv, recordsJSON, toRecords, toTSV } from "./export";
import {
  ColumnFilter,
  dateKey,
  type FilterGroup,
  type FilterQuery,
  filterQuery,
  hasTime,
  isClause,
  MISSING,
  setFilterQuery,
} from "./filter";
import { columnRuns, orderRuns } from "./order";
import { pageCount, pageItems, pageSizeChoices } from "./paging";
import { Profile, timeOf } from "./profile";
import {
  formatColumn,
  formatQuery,
  formatValue,
  NEGATED,
  parseQuery,
  type QueryContext,
  type QuerySyntaxError,
  queryContext,
  queryProblem,
  readQuery,
} from "./query";
import { CellText, fold, rowMatches, searchTerms } from "./search";
import { normalizeSort, type SortKey, type SortKeyInit, sortRows, toggleSort } from "./sort";
import {
  type BodyRow,
  CODE_BACKENDS,
  type CodeBackend,
  type ColumnSpec,
  type ExportFormat,
  type FilterType,
  parseSpec,
  type ResponsiveMode,
  type SelectionMode,
  type Spec,
  SpecError,
  type ViewSpec,
  type ViewStateSpec,
} from "./spec";
import { paramsText, readParams, readView, type View, viewParams, writeParams } from "./state";

export const TAG_NAME = "gt-table";

/** The event fired when the reader changes the sort (not when the `sort` property is set). */
export const SORT_EVENT = "gt-table-sort";

/** The event fired when the reader searches (not when the `search` property is set). */
export const SEARCH_EVENT = "gt-table-search";

/** The event fired when the reader changes a column's filter (not when the `filter` property is set). */
export const FILTER_EVENT = "gt-table-filter";

/** The event fired when the reader changes the page or the page size (not when properties are set). */
export const PAGE_EVENT = "gt-table-page";

/** The event fired when the reader resizes a column (with a handle, or its keys). */
export const RESIZE_EVENT = "gt-table-resize";

/** The event fired when the reader selects or deselects rows (not when `selection` is set). */
export const SELECT_EVENT = "gt-table-select";

/**
 * The event fired when the reader exports rows, or copies the code, from the bar (not when
 * `toCSV()`, `toTSV()`, `toRecords()`, `copyTable()` or `toCode()` is called).
 */
export const EXPORT_EVENT = "gt-table-export";

/**
 * The event fired when the reader changes the view: the filters, sort, search, page, page size or
 * the height of a body that scrolls (with the events for each, but the height's); or resets it, or undoes or redoes a change to it (not when properties
 * are set, or `resetView()`, `undo()` or `redo()` is called).
 */
export const VIEW_EVENT = "gt-table-view";

/** The name of the search highlight, for styling with `::highlight(gt-i-search)`. */
export const SEARCH_HIGHLIGHT = "gt-i-search";

/**
 * The prefix of the names of the query box's highlights, for styling them: `-keyword`, `-string`,
 * `-number` (and `true`, `false` and `null`) and `-error` (the place of what's wrong).
 */
const QUERY_HIGHLIGHT = "gt-i-query";

declare const __GTI_VERSION__: string;

export const VERSION: string = typeof __GTI_VERSION__ === "string" ? __GTI_VERSION__ : "dev";

export type State = "pending" | "empty" | "static" | "error" | "ready";

export interface SortEventDetail {
  sort: SortKey[];
}

export interface SearchEventDetail {
  search: string;
  /** The number of data rows that match. */
  count: number;
}

export interface FilterEventDetail {
  /** The filters, as a query (`null` without any). */
  filter: FilterQuery | null;
  /** The number of data rows that match the filters (and the search). */
  count: number;
}

export interface ResizeEventDetail {
  /** The column's name in the data; `null` for the stub column holding summary row labels. */
  column: string | null;
  /** The column's position among the body cells (from 0, counting the selection column and the stub). */
  index: number;
  /** Its new width, in px. */
  width: number;
}

export interface SelectEventDetail {
  /** The data rows selected (numbered by position in the data), in data order. */
  selection: number[];
}

export interface ExportEventDetail {
  /** How the rows were exported: copied, or downloaded as CSV, TSV or JSON; or "code", for the code copied. */
  format: ExportFormat;
  /** The data rows exported (numbered by position in the data), in the order shown (none, for code). */
  rows: number[];
  /** The code copied, and its library (for "code"). */
  code?: string;
  backend?: CodeBackend;
}

export interface PageEventDetail {
  /** The page shown, from 1. */
  page: number;
  pageSize: number | null;
  pageCount: number;
}

/**
 * The view: as the `filter`, `sort`, `search`, `page`, `pageSize`, `hiddenColumns` and `columnOrder`
 * properties have it, and (for a body that scrolls within a height) `height`, as `bodyMaxHeight` has it.
 */
export type ViewEventDetail = View;

/** A row group, as far as showing and hiding its rows goes. */
interface Group {
  /** The group's heading, shown on every page with some of its data rows. */
  headings: HTMLTableRowElement[];
  /** The group's summary rows above its data rows, shown on the page where the group starts. */
  top: HTMLTableRowElement[];
  /** The group's summary rows below its data rows, shown on the page where the group ends. */
  bottom: HTMLTableRowElement[];
  /** The group's label cell, when row groups are shown as a column of the stub. */
  cell: HTMLTableCellElement | null;
}

/** The part of a group on the current page. */
interface Span {
  /** The number of its data rows on the page. */
  count: number;
  first: HTMLTableRowElement;
  /** Whether the group starts on the page (so its top summary rows are shown). */
  starts: boolean;
  /** Whether the group ends on the page (so its bottom summary rows are shown). */
  ends: boolean;
}

/** A run of data rows of one group (if any) between structural rows: what sorts. */
interface Block {
  /** The block's data rows, in the order GT rendered them. */
  rows: number[];
  /** The structural `<tr>` after the block, which stays put, or `null` at the end of the body. */
  anchor: HTMLTableRowElement | null;
  group: Group | null;
  /** The block's data rows, in the order they're in in the body. */
  placed: number[];
}

/** A column label's resize handle. */
interface Resizer {
  handle: HTMLElement;
  th: HTMLTableCellElement;
  /** The column's position among the body cells (and `<col>`s). */
  index: number;
}

interface SortHeader {
  th: HTMLTableCellElement;
  icon: HTMLElement;
  label: string;
}

/**
 * A column's filter, and its button in the column label, which opens its panel (a disclosure), as
 * its token in the bar does.
 */
interface FilterControl {
  filter: ColumnFilter;
  label: string;
  /** The column label, and its button; `null` for a column without a label (filtered by `filter` only). */
  th: HTMLTableCellElement | null;
  button: HTMLButtonElement | null;
  /** The panel, made when it's first opened; its Clear button, and its inputs. */
  panel: HTMLElement | null;
  clear: HTMLButtonElement | null;
  text: HTMLInputElement | null;
  min: HTMLInputElement | null;
  max: HTMLInputElement | null;
  /**
   * A facet's values: their checkboxes, and the number of rows each would have; or a bool filter's,
   * radio buttons, after one for any value.
   */
  options: FacetOption[];
  /** Its token in the bar, made when the filter is first on. */
  token: FilterToken | null;
  /** The column's values (by rank, a missing one last) with the text a row with each shows, once needed. */
  names: [number, string][] | null;
}

/** A filter's token in the bar: a button saying what it keeps, which opens its panel, and one removing it. */
interface FilterToken {
  item: HTMLElement;
  open: HTMLButtonElement;
  remove: HTMLButtonElement;
}

interface FacetOption {
  key: number;
  item: HTMLElement;
  box: HTMLInputElement;
  count: HTMLElement;
}

/** A bool filter's option for any value (whose other options' keys are ranks, or `MISSING`). */
const ANY = -2;

// Header content that can't go inside a <button>
const INTERACTIVE = "a[href], button, input, select, textarea, details, [tabindex]";

// Whether a click in a row was on something of the row's own (a link, a checkbox), or on a group's
// label cell (not the container the table scrolls in, which can have focus)
const onOwnControl = (target: Element, tr: HTMLTableRowElement) => {
  const hit = target.closest(`${INTERACTIVE}, .gt_stub_row_group`);
  return hit !== null && tr.contains(hit);
};

// The classes of a data row's cells that the cells of the rows padding a page take
const FILLER_CLASSES = ["gt_stub", "gt_stub_row_group", "gt-i-select", "gt-i-pinned", "gt-i-pin"];

// The most data columns an "auto" table shows and is still stacked (as Python has it too)
const STACK_COLUMNS = 6;

// How far a resize handle's arrow keys move it, in px (and with Shift)
const RESIZE_STEP = 10;
const RESIZE_STEP_LARGE = 50;

// How long typing pauses before the search runs
const SEARCH_DELAY_MS = 150;

// How long a touch on a column's label is held to open its sheet, and how far it can move
const PRESS_MS = 500;
const PRESS_SLOP = 10;

// The most changes to the view that can be undone, and how soon after a change to the search, or
// to one filter, another is part of the same change
const UNDO_STEPS = 50;
const STEP_MS = 1000;

type PagerButton = "first" | "previous" | "next" | "last";

const PAGER_BUTTONS: Record<PagerButton, string> = {
  first: "First",
  previous: "Previous",
  next: "Next",
  last: "Last",
};

/** The page controls below the table. */
interface Pager {
  nav: HTMLElement;
  info: HTMLElement | null;
  select: HTMLSelectElement | null;
  buttons: Partial<Record<PagerButton, HTMLButtonElement>>;
  /** The page number buttons (`numbers`). */
  numbers: HTMLElement | null;
  /** "Page 2 of 5" (`simple` and `full`). */
  status: HTMLElement | null;
  /** The page number input (`jump`), and the page count after it. */
  jump: HTMLInputElement | null;
  jumpCount: HTMLElement | null;
}

/**
 * The control bar below the table (`controls.bar`): a search that opens from a button, on the
 * inline start, and arrows either side of the page and page count on the inline end; above them,
 * a token for each filter that's on.
 */
interface Bar {
  root: HTMLElement;
  /** The button that opens the search, and the field it opens into. */
  toggle: HTMLButtonElement | null;
  field: HTMLElement | null;
  /** The number of rows that match, in the field. */
  count: HTMLElement | null;
  /** The button that clears the search, or closes the field when there's none. */
  clear: HTMLButtonElement | null;
  /** The keyboard shortcuts' panel (with keys to list), whose button follows the search's. */
  keys: Keys | null;
  pages: HTMLElement;
  first: HTMLButtonElement;
  previous: HTMLButtonElement;
  next: HTMLButtonElement;
  last: HTMLButtonElement;
  /** The page and page count ("3/12"), which a click makes an input for the page to go to. */
  readout: HTMLButtonElement;
  jump: HTMLElement;
  jumpInput: HTMLInputElement;
  jumpCount: HTMLElement;
  info: Info;
  /** The button putting the author's view back, shown while the view is another (but its page or search). */
  reset: HTMLButtonElement | null;
  /** The export panel (with `export`). */
  exporter: Exporter | null;
  /** The columns panel (with columns readers can hide). */
  columns: Columns | null;
  /** The filters' tokens, in a row above the rest (with filters), and the button clearing them all. */
  tokens: HTMLElement | null;
  clearAll: HTMLElement | null;
  /** The filters as text (with filters). */
  query: QueryBox | null;
  /** The buttons that undo and redo the reader's changes to the view (with `view_state.undo`). */
  undo: HTMLButtonElement | null;
  redo: HTMLButtonElement | null;
  /**
   * The button opening the "Filter & sort" sheet (with filters, or columns readers can hide or
   * move), which on a touch screen the search, the filters as text and the columns fold into when
   * the bar is narrow.
   */
  sheet: HTMLButtonElement | null;
}

/**
 * The query box: the filters as text, to edit, which opens from a button in the bar into the
 * tokens' line (in their place). Its input is a combobox, whose list suggests what can go at the
 * caret.
 */
interface QueryBox {
  toggle: HTMLButtonElement;
  root: HTMLElement;
  input: HTMLInputElement;
  /** The text again, behind the input (whose own text is see-through, where it's highlighted). */
  mirror: HTMLElement;
  list: HTMLElement;
  error: HTMLElement;
  /** The text it opened with. */
  opened: string;
  suggestions: Suggestion[];
  active: number;
  /** What the suggestions are for. */
  context: QueryContext | null;
  /** Its highlights' ranges, in the mirror's text, and the place of what's wrong in the text. */
  ranges: [Highlight, Range][];
  mark: [number, number] | null;
}

interface Suggestion {
  text: string;
  /** What else it is (a column's label, a value as the query has it), if it says more. */
  detail: string;
  insert: string;
  /** How far before the end of what's inserted the caret goes. */
  back: number;
}

// The ops each kind of filter has, as suggestions
const OP_SUGGESTIONS: Record<FilterType, Suggestion[]> = {
  text: [
    { text: 'contains "…"', detail: "", insert: 'contains ""', back: 1 },
    { text: "matches /…/", detail: "pattern", insert: "matches //", back: 1 },
  ],
  facet: [{ text: "in (…)", detail: "", insert: "in (", back: 0 }],
  range: [
    { text: ">= …", detail: "at least", insert: ">= ", back: 0 },
    { text: "<= …", detail: "at most", insert: "<= ", back: 0 },
    { text: "> …", detail: "more than", insert: "> ", back: 0 },
    { text: "< …", detail: "less than", insert: "< ", back: 0 },
    { text: "top …", detail: "largest", insert: "top ", back: 0 },
    { text: "bottom …", detail: "smallest", insert: "bottom ", back: 0 },
  ],
  date: [
    { text: '>= "…"', detail: "on or after", insert: '>= ""', back: 1 },
    { text: '<= "…"', detail: "on or before", insert: '<= ""', back: 1 },
    { text: '> "…"', detail: "after", insert: '> ""', back: 1 },
    { text: '< "…"', detail: "before", insert: '< ""', back: 1 },
    { text: "top …", detail: "latest", insert: "top ", back: 0 },
    { text: "bottom …", detail: "earliest", insert: "bottom ", back: 0 },
  ],
  bool: [{ text: "in (…)", detail: "", insert: "in (", back: 0 }],
};

// (For any filter, after its ops)
const NULL_SUGGESTIONS: Suggestion[] = [
  { text: "is null", detail: "missing", insert: "is null ", back: 0 },
  { text: "is not null", detail: "not missing", insert: "is not null ", back: 0 },
];

/** A panel that a button in the bar opens above the bar (a disclosure). */
interface Popup {
  button: HTMLButtonElement;
  panel: HTMLElement;
}

/**
 * The info panel, which the bar's (i) button opens: which rows are shown, the page size (to
 * change, with `size_select`), the sort, the filters, the selection (with a button clearing it),
 * the columns hidden, and where the view is kept. (The bar's reset button puts the view back.)
 */
interface Info extends Popup {
  /** Which rows are shown ("21–30 of 118 rows"). */
  rows: HTMLElement;
  /** The page size select, and the item it's in (with `size_select`). */
  size: HTMLElement | null;
  select: HTMLSelectElement | null;
  /** The sort (with sorting). */
  sortText: HTMLElement | null;
  /** The filters (with filters). */
  filtersText: HTMLElement | null;
  /** The selection, and the button that clears it (with selection). */
  selection: HTMLElement | null;
  selectionText: HTMLElement | null;
  selectionClear: HTMLButtonElement | null;
  /** The columns hidden (with columns readers can hide). */
  columnsText: HTMLElement | null;
  /** Where the view is kept (with `view_state`). */
  view: HTMLElement | null;
  /** The buttons opening and closing every row's details (with row details). */
  detailsOpen: HTMLButtonElement | null;
  detailsClose: HTMLButtonElement | null;
}

/** The keyboard shortcuts' panel: the keys the table answers to, of which those for paging are listed while there are pages. */
interface Keys extends Popup {
  pageKeys: HTMLElement[];
  // (The info panel's button opening it, in a narrow bar)
  open: HTMLElement;
}

/**
 * The export panel: how many rows it exports, the choice of the selected rows only (with
 * selection), and a button for each format; with code, the choice of its library, and a note
 * that it leaves out the search (while there is one).
 */
interface Exporter extends Popup {
  rows: HTMLElement;
  /** The checkbox for exporting the selected rows only, and the item it's in. */
  selected: HTMLInputElement | null;
  selectedItem: HTMLElement | null;
  backend: HTMLSelectElement | null;
  note: HTMLElement | null;
}

/**
 * The columns panel: an item for each column readers can hide or move (by id), in the order
 * shown; and buttons showing them all (with columns to hide) and putting them back in the author's
 * order (with columns to move).
 */
interface Columns extends Popup {
  list: HTMLElement;
  items: Map<string, ColumnItem>;
  all: HTMLButtonElement | null;
  order: HTMLButtonElement | null;
}

/** A column's item in the columns panel: its checkbox, checked while it's shown (if it can be hidden), and its buttons moving it (if it can be moved). */
interface ColumnItem {
  root: HTMLElement;
  box: HTMLInputElement | null;
  earlier: HTMLButtonElement | null;
  later: HTMLButtonElement | null;
}

/** The rows to export: the data rows, and the cells' text, the column labels' first; with the cells, but a group's label. */
interface Exported {
  rows: number[];
  /** The keys of the cells in a row, as JSON has them: the group's, then the columns' ids. */
  keys: string[];
  text: string[][];
  cells: (Element | null)[][];
}

// How long the mouse is on a bar's button before its tooltip shows, and how far from it that is
const TIP_DELAY_MS = 500;
const TIP_GAP = 6;

// The bar is as wide as the table, but no narrower than this (where there's room)
const BAR_MIN_WIDTH = 300;

// (For the info panels' ids)
let infoCount = 0;

const SVG_NS = "http://www.w3.org/2000/svg";

// The bar's icons, drawn with strokes on a 24 x 24 grid
const ICONS = {
  search: "M4 10.5a6.5 6.5 0 1 0 13 0a6.5 6.5 0 1 0-13 0M15.5 15.5 20 20",
  previous: "M15 5l-7 7 7 7",
  next: "M9 5l7 7-7 7",
  first: "M17 5l-7 7 7 7M7 5v14",
  last: "M7 5l7 7-7 7M17 5v14",
  clear: "M6 6l12 12M18 6 6 18",
  info: "M3 12a9 9 0 1 0 18 0a9 9 0 1 0-18 0M12 11v5M12 7.5v.01",
  filter: "M4 5h16l-6 7.5V18l-4 2v-7.5z",
  query: "M8 4H7a2 2 0 0 0-2 2v4a2 2 0 0 1-2 2a2 2 0 0 1 2 2v4a2 2 0 0 0 2 2h1M16 4h1a2 2 0 0 1 2 2v4a2 2 0 0 0 2 2a2 2 0 0 0-2 2v4a2 2 0 0 1-2 2h-1",
  keys: "M4 5h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2zM6 9h.01M10 9h.01M14 9h.01M18 9h.01M8 12.5h.01M12 12.5h.01M16 12.5h.01M7.5 16h9",
  reset: "M3 12a9 9 0 1 0 2.64-6.36L3 8.3M3 3v5.3h5.3",
  apply: "M5 12.5l4.5 4.5L19 7",
  export: "M12 4v11M7.5 10.5 12 15l4.5-4.5M5 19h14",
  undo: "M9 14 4 9l5-5M4 9h10.5a5.5 5.5 0 0 1 0 11H11",
  redo: "M15 14l5-5-5-5M20 9H9.5a5.5 5.5 0 0 0 0 11H13",
  columns: "M4 5h16v14H4zM9.5 5v14M14.5 5v14",
  earlier: "M12 19V5M6 11l6-6 6 6",
  later: "M12 5v14M6 13l6 6 6-6",
  expand: "M6 9l6 6 6-6",
  grip: "M9 6v.01M15 6v.01M9 12v.01M15 12v.01M9 18v.01M15 18v.01",
};

// Whether the keys are a Mac's (⌘ rather than Ctrl)
const onMac = () => typeof navigator !== "undefined" && /Mac|iP(hone|ad|od)/.test(navigator.platform);

// What can have text typed into it, where `/` is a character rather than the search's key
const TYPED = 'input:not([type="checkbox"]):not([type="radio"]), textarea, select, [contenteditable]';

/** A cell's text, for announcements and exports: without footnote marks. */
function labelText(cell: Element): string {
  return (withoutMarks(cell).textContent ?? "").replace(/\s+/g, " ").trim();
}

// The table's column and spanner labels, by id
const labelCells = (table: HTMLTableElement) =>
  new Map(Array.from(table.querySelectorAll<HTMLTableCellElement>(":scope > thead th[id]"), (th) => [th.id, th]));

// A copy of a cell, without its footnote marks (or the button showing a row's dropped columns)
function withoutMarks(cell: Element): Element {
  const clone = cell.cloneNode(true) as Element;
  for (const mark of clone.querySelectorAll(".gt_footnote_marks, .gt-i-expand, .gt-i-profile")) {
    mark.remove();
  }
  return clone;
}

// Whether two views show the same rows, in the same order, on the same page
const sameView = (a: View, b: View | undefined) => b !== undefined && viewParams(a, b).length === 0;

const plural = (n: number) => `${n} ${n === 1 ? "row" : "rows"}`;

// A date bound (ISO 8601 text) as a date field has it (its date), or a date and time field (a date
// as its midnight, and seconds cut to milliseconds)
function dateField(text: string, clock: boolean): string {
  if (!clock || text === "") {
    return text.split("T")[0] as string;
  }
  return hasTime(text) ? text.replace(/(\.\d{3})\d+$/, "$1") : `${text}T00:00`;
}

// A date bound as a language writes it ("Jun 15, 2015", or with its time "Jun 15, 2015, 9:30 AM")
function dateText(text: string, lang: string | undefined): string {
  const key = dateKey(text);
  if (key === null) {
    return text;
  }
  const options: Intl.DateTimeFormatOptions = { dateStyle: "medium", timeZone: "UTC" };
  if (hasTime(text)) {
    options.timeStyle = key.endsWith(":00.000000000") ? "short" : "medium";
  }
  try {
    return new Intl.DateTimeFormat(lang, options).format(timeOf(text));
  } catch {
    return text;
  }
}

const isPositiveInteger = (x: unknown): x is number => Number.isInteger(x) && (x as number) > 0;

// Show or hide an element, leaving it be if it's as it should be (which costs a style recalc, with many)
const setHidden = (el: HTMLElement, hidden: boolean) => {
  if (el.hidden !== hidden) {
    el.hidden = hidden;
  }
};

/** A `<col>`'s width (`cols_width()`) in px, in a table `table` px wide; `NaN` for other units. */
function authoredWidth(col: HTMLElement, table: number): number {
  const width = col.style.width;
  const value = parseFloat(width);
  if (width.endsWith("px")) {
    return value;
  }
  return width.endsWith("%") ? (value * table) / 100 : Number.NaN;
}

// Set a style property, unless it's set to that already (rows are restyled as they're shown)
function setStyle(el: HTMLElement, property: string, value: string): void {
  if (el.style.getPropertyValue(property) !== value) {
    el.style.setProperty(property, value);
  }
}

const isTransparent = (color: string) =>
  color === "" || color === "transparent" || /^rgba\(.*,\s*0\)$/.test(color) || /\/\s*0\)$/.test(color);

// A computed colour's opacity, from 0 to 1
function opacity(color: string): number {
  if (isTransparent(color)) {
    return 0;
  }
  const match = /^rgba\(.*,\s*([\d.]+)\)$/.exec(color) ?? /\/\s*([\d.]+)(%?)\s*\)$/.exec(color);
  if (match === null) {
    return 1;
  }
  const value = parseFloat(match[1] as string);
  return match[2] === "%" ? value / 100 : value;
}

// The colour behind an element: the first background that isn't transparent, out from it
function backdropColor(el: Element): string {
  for (let node: Element | null = el; node !== null; node = node.parentElement) {
    const color = getComputedStyle(node).backgroundColor;
    if (!isTransparent(color)) {
      return color;
    }
  }
  return "Canvas";
}

// An element of a class, with attributes
function element<K extends keyof HTMLElementTagNameMap>(
  doc: Document,
  tag: K,
  className: string,
  attributes: Record<string, string> = {},
): HTMLElementTagNameMap[K] {
  const el = doc.createElement(tag);
  el.className = className;
  for (const [name, value] of Object.entries(attributes)) {
    el.setAttribute(name, value);
  }
  return el;
}

// Put elements next to one another in this order (in `parent`, or where they are, around `keep`)
// without moving `keep`, which may have focus or a pointer on it
function arrange(elements: readonly Element[], keep: Element | undefined, parent?: Element): void {
  const at = keep === undefined ? -1 : elements.indexOf(keep);
  if (at < 0) {
    parent?.append(...elements);
    return;
  }
  for (const el of elements.slice(0, at)) {
    (keep as Element).before(el);
  }
  for (const el of elements.slice(at + 1).reverse()) {
    (keep as Element).after(el);
  }
}

// The page's highlight of a name (shared by every table on the page), where the browser has them
function pageHighlight(name: string): Highlight | undefined {
  const registry = typeof CSS !== "undefined" ? CSS.highlights : undefined;
  if (registry === undefined || typeof Highlight === "undefined") {
    return undefined;
  }
  let highlight = registry.get(name);
  if (highlight === undefined) {
    highlight = new Highlight();
    registry.set(name, highlight);
  }
  return highlight;
}

function icon(doc: Document, name: keyof typeof ICONS): SVGSVGElement {
  const svg = doc.createElementNS(SVG_NS, "svg");
  svg.setAttribute("class", "gt-i-icon");
  svg.setAttribute("viewBox", "0 0 24 24");
  svg.setAttribute("aria-hidden", "true");
  const path = doc.createElementNS(SVG_NS, "path");
  path.setAttribute("d", ICONS[name]);
  svg.append(path);
  return svg;
}

// A row's role, and its cells', as a table's elements have them: a header cell's by its scope (or,
// without one, by where it is)
function addRowRoles(tr: HTMLTableRowElement): void {
  tr.setAttribute("role", "row");
  for (const cell of Array.from(tr.cells)) {
    let role = "cell";
    if (cell.tagName === "TH") {
      const scope = cell.getAttribute("scope");
      const row = scope === null ? tr.parentElement?.tagName !== "THEAD" : scope === "row" || scope === "rowgroup";
      role = row ? "rowheader" : "columnheader";
    }
    cell.setAttribute("role", role);
  }
}

// Wrap a cell's contents in the box that keeps them in view as the table scrolls sideways
function keepInView(cell: HTMLTableCellElement): HTMLElement {
  const div = cell.ownerDocument.createElement("div");
  div.className = "gt-i-inview";
  div.append(...Array.from(cell.childNodes));
  cell.append(div);
  cell.classList.add("gt-i-inview-cell");
  return div;
}

// The row of a column label's controls (its sort's and its filter's buttons), under the label
function controlsRow(th: HTMLTableCellElement): HTMLElement {
  let row = th.querySelector<HTMLElement>(":scope > .gt-i-head-controls");
  if (row === null) {
    row = th.appendChild(element(th.ownerDocument, "div", "gt-i-head-controls"));
    th.classList.add("gt-i-head");
  }
  return row;
}

// The bottom row's column labels (and those spanning rows down to it)
function bottomLabels(table: HTMLTableElement): HTMLTableCellElement[] {
  const rows = Array.from(table.querySelectorAll<HTMLTableRowElement>(":scope > thead > tr.gt_col_headings"));
  return rows.flatMap((tr, r) =>
    Array.from(tr.cells).filter((th) => r + Number(th.getAttribute("rowspan") ?? 1) >= rows.length),
  );
}

// The place for a column's profile, under its label (and controls)
function profileSlot(th: HTMLTableCellElement): HTMLElement {
  return (
    th.querySelector<HTMLElement>(":scope > .gt-i-profile") ??
    th.appendChild(element(th.ownerDocument, "div", "gt-i-profile", { "aria-hidden": "true" }))
  );
}

// A profile's share of rows, as a percentage ("<1%" for a few)
const percent = (part: number, whole: number) => (part / whole < 0.005 ? "<1%" : `${Math.round((part / whole) * 100)}%`);

// How a histogram's bins' edges are written: numbers with enough digits to tell the bins apart
// ("1.25K"), or dates (with their times, for bins shorter than a day)
function edgeFormat(profile: Profile, lang: string | undefined): (x: number) => string {
  const first = profile.bars[0];
  const last = profile.bars[profile.bars.length - 1];
  const width = first === undefined ? 0 : first.high - first.low;
  const most = Math.max(Math.abs(first?.low ?? 0), Math.abs(last?.high ?? 0));
  const options: Intl.NumberFormatOptions & Intl.DateTimeFormatOptions = profile.times
    ? { dateStyle: "medium", timeZone: "UTC", ...(width < 864e5 ? { timeStyle: "short" } : {}) }
    : {
        // (Short for big numbers: "1.25M", not "1,250,000")
        notation: most < 1e4 ? "standard" : "compact",
        maximumSignificantDigits: Math.min(21, Math.max(2, Math.floor(Math.log10(most || 1)) - Math.floor(Math.log10(width || 1)) + 2)),
      };
  const make = (locale: string | undefined) =>
    profile.times ? new Intl.DateTimeFormat(locale, options) : new Intl.NumberFormat(locale, options);
  let format: Intl.DateTimeFormat | Intl.NumberFormat;
  try {
    format = make(lang);
  } catch {
    format = make(undefined);
  }
  return (x) => format.format(x);
}

/** A column's profile under its label (see `addProfiles()`). */
interface ProfileView {
  profile: Profile;
  /** Its bars, their tooltips and what they name, and its caption. */
  rects: SVGRectElement[];
  titles: SVGTitleElement[];
  names: string[];
  caption: HTMLElement;
  /** A value's text, by its rank, as its cells show it. */
  valueName: (rank: number) => string;
}

export class GtTable extends HTMLElement {
  /** The static `<table>` this element hydrates, or `null` if there isn't one. */
  table: HTMLTableElement | null = null;

  /** The table's spec, once hydrated. */
  spec: Spec | null = null;

  private observer: MutationObserver | null = null;
  private tbody: HTMLTableSectionElement | null = null;
  private rowElements: HTMLTableRowElement[] = [];
  private bodyRows = new WeakMap<HTMLTableRowElement, BodyRow>();
  private blocks: Block[] = [];
  private groups: Group[] = [];
  /** Per data row, its group. */
  private rowGroups: (Group | null)[] = [];
  /** Whether rows can be moved and hidden: not with a hierarchical stub (see `sortableColumns`). */
  private movable = false;
  private sortKeys: SortKey[] = [];
  private sortHeaders = new Map<string, SortHeader>();
  /** The labels of the columns readers can't sort by (that code can), for saying how it's sorted. */
  private unsortedLabels = new Map<string, string>();
  private searchValue = "";
  private terms: string[] = [];
  /** Per data row, whether it matches the search and the filters; `null` without any. */
  private matched: Uint8Array | null = null;
  /** The number of data rows that match the search and the filters (all of them, without any). */
  private matchCount = 0;
  /** The columns' profiles, and the rows (`matched`) they last counted (`undefined` before). */
  private profileViews: ProfileView[] = [];
  private profiled: Uint8Array | null | undefined = undefined;
  /** The columns' filters, in column order. */
  private filters: FilterControl[] = [];
  /** The query's groups (its `or` and `not` parts), which no one column's filter has, in order. */
  private filterGroups: FilterGroup[] = [];
  /** The groups' tokens, in the bar. */
  private groupTokens = new Map<FilterGroup, FilterToken>();
  /** The filter whose panel is open, and the page's handlers for a press outside it and for scrolling. */
  private openFilter: FilterControl | null = null;
  /** What opened it (its column's button, or its token), which it's placed by and focus goes back to. */
  private filterAnchor: HTMLElement | null = null;
  private filterPress: ((event: PointerEvent) => void) | null = null;
  private filterScroll: (() => void) | null = null;
  /** A change to a filter, waiting on the typing to pause. */
  private filterChange: (() => void) | null = null;
  private filterTimer: ReturnType<typeof setTimeout> | null = null;
  private pageValue = 1;
  /** The page size: `null` for one page of every row, or `undefined` for the spec's. */
  private pageSizeValue: number | null | undefined = undefined;
  /** The rows of the current page: from `start` to `end` of the `total` that match. */
  private view = { start: 0, end: 0, total: 0 };
  private pager: Pager | null = null;
  private bar: Bar | null = null;
  /** The element's handler for `/`, which opens the bar's search. */
  private slashKey: ((event: KeyboardEvent) => void) | null = null;
  /** Whether the element has the `tabindex` it was given for its keys (see `addBar()`). */
  private ownTabIndex = false;
  /** Whether the bar's readout is an input for the page to go to. */
  private jumping = false;
  /** The bar's panel that's open (see `Popup`). */
  private popup: Popup | null = null;
  /** The page's handler for a press outside the open panel, which closes it. */
  private outsidePress: ((event: PointerEvent) => void) | null = null;
  /**
   * The "Filter & sort" sheet (see `openSheet()`), with the bar; while it's open, what brings it up
   * to date, and what puts back what it took (the columns panel's items, the live region).
   */
  private sheet: HTMLDialogElement | null = null;
  private sheetSync: (() => void) | null = null;
  private sheetDone: (() => void) | null = null;
  /** Whether a long press on a column's label opened its sheet (so the press isn't a click). */
  private pressed = false;
  /**
   * The column widths of the table with every row shown, which hidden rows mustn't change: in our
   * `<colgroup>`, or in the author's for the columns without a width (`cols_width()`).
   */
  private colgroup: HTMLTableColElement | null = null;
  /** The `<col>`s we set the widths of. */
  private fittedCols: HTMLElement[] = [];
  private widthsFixed = false;
  /** Whether text doesn't wrap, in a table with columns the author sized, which it may overrun. */
  private cutsText = false;
  /** Whether we made the table's layout fixed (with a width), to keep the author's column widths. */
  private tableFitted = false;
  /** The element's width when the column widths were measured. */
  private fittedWidth = 0;
  private refitFrame = 0;
  /** Per data row, the text of its cells; made on the first search. */
  private cellTexts: CellText[][] | null = null;
  /** The columns (by their index in the spec) the search leaves out. */
  private unsearched = new Set<number>();
  private ranges: AbstractRange[] = [];
  private searchBox: HTMLInputElement | null = null;
  private searchTimer: ReturnType<typeof setTimeout> | null = null;
  private toolbar: HTMLElement | null = null;
  private layout: ResizeObserver | null = null;
  private empty: HTMLTableRowElement | null = null;
  /** The empty rows that keep a short page as tall as a full one (see `pad()`), shown or not. */
  private fillers: HTMLTableRowElement[] = [];
  /** The classes of a filler row's cells, one per column. */
  private fillerCells: string[] | null = null;
  /**
   * The page size and table width the body's height on a full page (`padHeight`) and a data row's
   * (`rowHeight`) were measured at; empty if they weren't (the table wasn't laid out).
   */
  private padKey = "";
  private padHeight = 0;
  private rowHeight = 0;
  private live: HTMLElement | null = null;
  private resizers: Resizer[] = [];
  /**
   * The lines along the column whose label the mouse is over (`addGuide()`); that label; and the
   * column before it, if that one is resized from the label's inline start.
   */
  private guide: HTMLElement | null = null;
  private guideTh: HTMLTableCellElement | null = null;
  private guideBefore: Resizer | null = null;
  /** The handle along the foot of the rows, dragged for more or fewer, or a taller body (`addFootHandle()`). */
  private footHandle: HTMLElement | null = null;
  /** The height (in px) the body scrolls within, as the reader has set it; `null` for the author's. */
  private heightValue: number | null = null;
  /**
   * The column widths when the reader first resized one, which a reset goes back to; `null`
   * before. From then on, every column has a fixed width.
   */
  private startWidths: number[] | null = null;
  /** The data row marked by a tap, when rows are highlighted. */
  private marked: HTMLTableRowElement | null = null;
  /** Whether the last press on the body was a touch. */
  private touched = false;
  /** The data rows selected. */
  private selected = new Set<number>();
  /** Whether the table has a column of checkboxes for selecting rows (before the others). */
  private selectColumn = false;
  /** Per data row, its checkbox. */
  private selectBoxes: HTMLInputElement[] = [];
  /** The checkbox selecting every row that matches the search, when several can be selected. */
  private selectAll: HTMLInputElement | null = null;
  /** The row a Shift-click selects a range from: the last one clicked. */
  private selectAnchor: number | null = null;
  /** The data rows that match the search, in the order shown (on every page). */
  private order: number[] = [];
  /** The container the body scrolls in, when it scrolls (`layout.height`). */
  private scroller: HTMLElement | null = null;
  /** The table's borders, drawn on its cells so that they move with the rows that stick. */
  private borders: TableBorders | null = null;
  /** The rows that stick under the column labels (group headings) and to the bottom. */
  private stuckTop: HTMLTableRowElement[] = [];
  private stuckBottom: HTMLTableRowElement[] = [];
  /** The height the rows stuck at the bottom take up. */
  private foot = 0;
  /** Whether the body scrolls down, within a height (`layout.height`). */
  private scrollsDown = false;
  /**
   * The shadows over the scrolling body's top and bottom edges, while there are rows past them;
   * and over its left and right edges, while there are columns past them (`layout.responsive`).
   */
  private shades: Partial<Record<Side, HTMLElement>> = {};
  private shadeFrame = 0;
  /** What the table does when it's wider than its container (`layout.responsive`). */
  private responsive: ResponsiveMode | null = null;
  /**
   * Whether the table is stacked, its rows as cards (by its own CSS, in a container narrower than
   * its stacking width), which its column widths and page padding aren't measured in.
   */
  private stacked = false;
  /** Whether the table's container is as wide as what's in it, which it isn't stacked in (`fitsContent()`). */
  private fitted: boolean | null = null;
  /** The number of columns pinned at the table's inline start: the selection column and the stub (`stubColumns`), and the data columns pinned there. */
  private pinColumns = 0;
  private stubColumns = 0;
  /** The number of data columns pinned at the table's inline end, and of columns in all. */
  private endColumns = 0;
  private gridColumns = 0;
  /** A pinned cell along the pinned columns' inline end, which the shadow over the columns past them is placed by. */
  private edgeCell: HTMLTableCellElement | null = null;
  /** A cell along the inline start of the columns pinned at the inline end, which the shadow before them is placed by. */
  private endEdge: HTMLTableCellElement | null = null;
  /** The cells across the table (its title, group headings and notes), whose contents stay in view. */
  private acrossCells: HTMLTableCellElement[] = [];
  /** The wrappers that keep those cells' contents in view, once the table has been wider than its container. */
  private inView: HTMLElement[] | null = null;
  /** The hint that the table scrolls sideways, until it first does. */
  private hint: HTMLElement | null = null;
  private hinted = false;
  private pinFrame = 0;
  /** Whether we made the container a region that can be focused, as it scrolls. */
  private regioned = false;
  /** The view the table is first shown with (the spec's), which `resetView()` goes back to. */
  private authorView: View | null = null;
  /** Where the reader's view is kept (`view_state`), once it has been read; and its parameters as last kept. */
  private keeper: ViewStateSpec | null = null;
  private keptText: string | null = null;
  /** Whether the reader's changes to the view can be undone (`view_state.undo`). */
  private undoable = false;
  /**
   * The views before each of the reader's changes that can be undone (the last, last), and after
   * each undone; and the view after the last change (`null`, until hydrated, or without undo).
   */
  private past: View[] = [];
  private future: View[] = [];
  private present: View | null = null;
  /** What the last change was to (see `record()`), and when. */
  private lastPart: string | null = null;
  private lastTime = 0;
  /** The element's handler for the keys that undo and redo. */
  private undoKey: ((event: KeyboardEvent) => void) | null = null;
  // (Whether Shift is held, as the last key pressed or let go in the table says)
  private shiftHeld = false;
  /** The columns readers can hide, and those hidden (by id, in column order). */
  private hideable: string[] = [];
  private hiddenIds: string[] = [];
  /** The columns hidden, on the table's grid (where the spec's columns come after the `lead`). */
  private hiddenGrid = new Set<number>();
  /** The cells in or across the columns readers can hide, placed on the grid with every cell shown. */
  private columnCells: Placed[] = [];
  /** The width each column hidden was shown at (by grid column), for when every width is fixed. */
  private hiddenWidths = new Map<number, number>();
  /**
   * A table that drops columns to fit (`layout.responsive` "collapse"): the columns it can drop
   * (by id, in the order it drops them), and those dropped, in that order, with the width the
   * table had before each went (which it has room for again once its container is that wide),
   * and the container's width it was fitted to.
   */
  private drops: string[] = [];
  private dropped: string[] = [];
  private dropNeeds: number[] = [];
  private fitRoom = -1;
  /**
   * Each row's button that opens it, to show what's under it: the columns dropped from it (with
   * some dropped) and its details (`spec.details`, if it has them); the rows open, and the rows
   * under them showing that (made as they're shown).
   */
  private expanders = new Map<HTMLTableRowElement, HTMLButtonElement>();
  private opened = new Set<HTMLTableRowElement>();
  private details = new Map<HTMLTableRowElement, HTMLTableRowElement>();
  /** The data rows' details, by row: each one's `<template>`. */
  private contents = new Map<HTMLTableRowElement, HTMLTemplateElement>();
  /** Whether a row's button (or a tap on a row with details) opens it yet. */
  private expanding = false;
  /** The kind of pointer last pressed on the body ("touch", say), until its click. */
  private pointer = "";
  /** Whether the rows under rows open are left out, as the rows are measured. */
  private measuring = false;
  /** The runs of columns readers can move (by index in the spec; see `order.ts`). */
  private runs: number[][] = [];
  /**
   * With runs, the spec's column at each place (by index in the spec), as shown, and the place of
   * each (where its cells are on the grid, after the `lead`); empty without.
   */
  private columnAt: number[] = [];
  private placeOf: number[] = [];
  /** Per run, its cells in each row with a cell of its own in each of its columns (in the author's order), on hydration. */
  private runCells: { run: number; cells: HTMLTableCellElement[] }[] = [];
  /** The pointer dragging a column's item in the columns panel, and the item. */
  private dragging: { pointer: number; id: string } | null = null;

  get state(): State | null {
    return this.getAttribute("data-gti-state") as State | null;
  }

  /**
   * The columns the table can be sorted by. Empty until hydrated, and for a table whose stub has
   * cells merged across rows (a hierarchical stub), since reordering rows would break them.
   */
  get sortableColumns(): string[] {
    return this.movable && this.spec !== null ? Object.keys(this.spec.ranks) : [];
  }

  /** The current sort: the sort keys, most significant first. */
  get sort(): SortKey[] {
    return this.sortKeys.map((key) => ({ ...key }));
  }

  /** @throws {RangeError} for a column that isn't one of `sortableColumns`, or one given twice. */
  set sort(keys: readonly SortKeyInit[]) {
    const ranks: Spec["ranks"] = this.movable && this.spec !== null ? this.spec.ranks : {};
    this.sortKeys = normalizeSort(keys, ranks);
    this.pageValue = 1;
    this.render();
    this.forget();
  }

  /**
   * The current search: rows are shown when every word of it is in one of their cells, ignoring
   * case and accents. Can be set before the table is hydrated. Like sorting, it does nothing for a
   * table whose stub has cells merged across rows.
   */
  get search(): string {
    return this.searchValue;
  }

  set search(value: string) {
    this.cancelSearchTimer();
    this.applySearch(String(value));
    this.showSearch();
    this.forget();
  }

  /** The columns the table can be filtered by (see `filter`). Empty until hydrated. */
  get filterableColumns(): string[] {
    return this.filters.map((control) => control.filter.column);
  }

  /**
   * The filters, as a query: `{and: [clauses]}`, with a clause `{col, op, value}` for each filter
   * on a column (two for a range or date filter with both bounds), or `null` without any. Rows are
   * shown that every clause, and the search, keep. A clause's `op` is "contains", for a text filter
   * (`value` is the text, matched as the search matches it); "in", for a facet (`value` is the
   * values to keep, `null` for a missing one) or a bool filter (`value` is the one value to keep:
   * `[true]`, `[false]` or `[null]`); or "gte" or "lte", for a range (`value` is the
   * bound) or a date filter (`value` is the bound as ISO 8601 text: a date, "2015-06-15", or for a
   * column with times, either that, meaning its midnight, or a date and time, "2015-06-15T09:30").
   * A clause can also be one the filters don't have, which the query has with the groups: "gt" or
   * "lt", for a range or a date filter (rows more than, or less than, the bound); "top_n" or
   * "bottom_n", for a range or a date filter (`value` is a whole number, n: rows with the n largest,
   * or smallest, values among all the rows, and those tied with the n-th); "matches", for a text
   * filter (rows whose text has a match of a pattern); or "is_null" (rows whose value is missing).
   *
   * A part of the query can also be a group of clauses: `{or: [...]}` (rows that any part keeps),
   * `{and: [...]}` (that every one does), or `{not: part}` (that the part doesn't, so rows whose
   * value is missing, which a clause leaves out, are kept), nested as wanted. The column filters
   * have the clauses that aren't in an `or` or a `not`, and the query has them first, in the
   * filters' order, then the groups, in the order given (an `and` in an `and`, or an `or` in an
   * `or`, spliced in, and a group of one part as the part).
   *
   * @throws {RangeError} for a query that isn't `{and: [...]}`, a group without parts, or a clause
   *   on a column that isn't one of `filterableColumns`, or that the column's filter can't have (an
   *   "in" without values, or a bool filter's with more than one, or a second clause with the same
   *   `op` in an `and`, or in a group, a "contains" without text, too).
   */
  get filter(): FilterQuery | null {
    return this.query();
  }

  set filter(query: FilterQuery | null) {
    this.cancelFilterTimer();
    this.setQuery(query);
    for (const control of this.filters) {
      this.syncFilter(control);
    }
    this.applyFilters();
    this.forget();
  }

  // The query the filters and groups make
  private query(): FilterQuery | null {
    return filterQuery(
      this.filters.map((control) => control.filter),
      this.filterGroups,
    );
  }

  // Set the filters and groups from a query (nothing changes if it's bad; see `filter`)
  private setQuery(query: FilterQuery | null): void {
    this.filterGroups = setFilterQuery(
      this.filters.map((control) => control.filter),
      query,
    );
  }

  /** The columns readers can hide (`hideable` in the spec), in column order. Empty until hydrated. */
  get hideableColumns(): string[] {
    return [...this.hideable];
  }

  /**
   * The columns hidden, in column order: their cells aren't shown, searched or exported (but their
   * filters still keep rows). Setting it hides those and shows the rest.
   *
   * @throws {RangeError} for a column that isn't one of `hideableColumns`.
   */
  get hiddenColumns(): string[] {
    return [...this.hiddenIds];
  }

  set hiddenColumns(ids: readonly string[]) {
    const bad = ids.find((id) => !this.hideable.includes(id));
    if (bad !== undefined) {
      throw new RangeError(`"${bad}" isn't a column that can be hidden`);
    }
    this.hideColumns(ids);
    this.matchRows();
    this.render();
    this.forget();
  }

  /**
   * The columns readers can move (`reorderable` in the spec), in the author's order: each next to
   * another it can move among (see `columnOrder`). Empty until hydrated.
   */
  get reorderableColumns(): string[] {
    return this.runIds().flat();
  }

  /**
   * The order the columns readers can move are shown in. Each moves only among the reorderable
   * columns next to it (in the author's order), under the same spanners and pinned to the same side
   * (if pinned), so it stays under its spanners and by its side. Setting it puts each such run of
   * columns in the order they're given in, then those left out, in the author's order.
   *
   * @throws {RangeError} for a column that isn't one of `reorderableColumns`, or one given twice.
   */
  get columnOrder(): string[] {
    return this.shownRuns().flat();
  }

  set columnOrder(ids: readonly string[]) {
    const movable = this.reorderableColumns;
    const bad = ids.find((id, i) => !movable.includes(id) || ids.indexOf(id) !== i);
    if (bad !== undefined) {
      throw new RangeError(
        movable.includes(bad) ? `"${bad}" is given twice` : `"${bad}" isn't a column that can be moved`,
      );
    }
    this.orderColumns(orderRuns(ids, this.runIds()));
    this.render();
    this.forget();
  }

  /**
   * The page shown, from 1. A new sort or search goes back to the first page. Can be set before
   * the table is hydrated; a page past the last is the last.
   *
   * @throws {RangeError} for a page that isn't a positive integer.
   */
  get page(): number {
    return this.spec === null ? this.pageValue : Math.min(this.pageValue, this.pageCount);
  }

  set page(page: number) {
    if (!isPositiveInteger(page)) {
      throw new RangeError(`\`page\` must be a positive integer, not ${String(page)}`);
    }
    this.pageValue = page;
    this.render();
    // (Going to another page isn't a change that's undone, from code or not)
    this.forget(false);
  }

  /**
   * The number of data rows on a page, or `null` for one page of every row. It starts as the
   * table's page size (from `opt_interactive()`), and can be set before the table is hydrated. When
   * it changes, the first row of the page stays in view. Like sorting, paging does nothing for a
   * table whose stub has cells merged across rows.
   *
   * @throws {RangeError} for a size that isn't a positive integer or `null`.
   */
  get pageSize(): number | null {
    return this.spec === null ? (this.pageSizeValue ?? null) : this.size;
  }

  set pageSize(size: number | null) {
    if (size !== null && !isPositiveInteger(size)) {
      throw new RangeError(`\`pageSize\` must be a positive integer or null, not ${String(size)}`);
    }
    this.resize(size);
    this.forget();
  }

  /**
   * For a body that scrolls within a height (`i_scroll()`): the height (in px) it's set to, as the
   * reader can drag it to, or `null` for the author's. Always `null` for a body that doesn't.
   *
   * @throws {RangeError} for a height that isn't a positive number or `null`.
   */
  get bodyMaxHeight(): number | null {
    return this.heightValue;
  }

  set bodyMaxHeight(height: number | null) {
    if (height !== null && !(typeof height === "number" && Number.isFinite(height) && height > 0)) {
      throw new RangeError(`\`bodyMaxHeight\` must be a positive number or null, not ${String(height)}`);
    }
    if (this.spec?.layout.height == null) {
      return;
    }
    this.heightValue = height;
    this.applyHeight();
    this.heightChanged();
    this.forget();
  }

  /** The number of pages of the rows that match the search; 1 without pagination. */
  get pageCount(): number {
    return pageCount(this.matchCount, this.size);
  }

  /**
   * The data rows selected (numbered by position in the data), in data order. Can be set before
   * the table is hydrated: rows the table doesn't have are dropped then (and all but the first,
   * if only one can be selected).
   *
   * @throws {RangeError} for a row that isn't a data row's index, or more rows than can be
   * selected (one, or none at all).
   */
  get selection(): number[] {
    return Array.from(this.selected).sort((a, b) => a - b);
  }

  set selection(rows: readonly number[]) {
    const unique = Array.from(new Set(rows));
    const bad = unique.find((row) => !Number.isInteger(row) || row < 0);
    if (bad !== undefined) {
      throw new RangeError(`\`selection\` must hold data row indices, not ${String(bad)}`);
    }
    const spec = this.spec;
    if (spec !== null) {
      const mode = spec.controls.selection;
      const missing = unique.find((row) => row >= spec.nrows);
      if (missing !== undefined) {
        throw new RangeError(`the table has no data row ${missing}`);
      }
      if (unique.length > (mode === null ? 0 : mode === "single" ? 1 : Infinity)) {
        throw new RangeError(
          mode === null ? "rows can't be selected in this table" : "only one row can be selected in this table",
        );
      }
    }
    this.selected = new Set(unique);
    this.selectAnchor = null;
    this.showSelection();
  }

  // The page size in use: none until hydrated, or when rows can't be moved
  private get size(): number | null {
    return this.movable ? (this.pageSizeValue ?? null) : null;
  }

  // The grid columns before the spec's: the selection column, and the group column when groups
  // are a column of the stub
  private get lead(): number {
    return (this.selectColumn ? 1 : 0) + (this.spec?.stub.groups_as_column === true ? 1 : 0);
  }

  constructor() {
    super();
    // (Firefox's click from Enter or Space doesn't say whether Shift is held)
    const shift = (event: KeyboardEvent) => {
      this.shiftHeld = event.shiftKey;
    };
    this.addEventListener("keydown", shift, true);
    this.addEventListener("keyup", shift, true);
    // A button or box clicked has focus, as in Chromium, before what the click does: Safari (and
    // Firefox on a Mac) leaves it on the page, out of reach of the table's keys
    this.addEventListener(
      "click",
      (event) => {
        const target = (event.target as Element).closest("button, input[type=checkbox], input[type=radio], label");
        const control = target instanceof HTMLLabelElement ? target.control : target;
        if (control instanceof HTMLElement && this.ownerDocument.activeElement !== control) {
          control.focus({ preventScroll: true });
        }
      },
      true,
    );
  }

  // Whether Shift was held for a click (with the mouse, or from a key)
  private shifted(event: MouseEvent): boolean {
    return event.shiftKey || (event.detail === 0 && this.shiftHeld);
  }

  connectedCallback(): void {
    if (this.table !== null) {
      // Moved: keep the hydrated table (and its view), unless its children were replaced
      if (this.contains(this.table)) {
        this.observeLayout();
        return;
      }
      this.reset();
    }
    // `connectedCallback()` can run before this element's children exist: while the page is
    // still being parsed (the element was already defined when the parser reached it, so its
    // table may be partly parsed), or when a framework adds the children afterwards.
    if (this.ownerDocument.readyState === "loading") {
      this.setState("pending");
      this.ownerDocument.addEventListener("DOMContentLoaded", () => this.hydrate(), { once: true });
      return;
    }
    this.hydrate();
  }

  disconnectedCallback(): void {
    this.closePanel(false);
    this.closeFilter(false);
    this.stopObserving();
    this.layout?.disconnect();
    this.layout = null;
    this.cancelRefit();
    this.cancelShades();
    this.cancelPin();
  }

  /** The `<tr>` of data row `row` (numbered by position in the data), if it's in the table. */
  rowElement(row: number): HTMLTableRowElement | null {
    return this.rowElements[row] ?? null;
  }

  /** What a body `<tr>` is: a data row's index, or a structural row. */
  bodyRow(tr: HTMLTableRowElement): BodyRow | null {
    return this.bodyRows.get(tr) ?? null;
  }

  /**
   * The rows as CSV, as the export panel downloads them: the text each cell shows (in the columns
   * shown), under the column labels (after their spanners'), with a column of the rows' groups
   * first (with groups);
   * each data row the search and filters keep, in the order shown, on every page, or (with
   * `selected`) each one selected. With `guard` (as by default), a cell a spreadsheet would read as
   * a formula starts with a `'`. Empty until hydrated.
   */
  toCSV({ selected = false, guard = true }: { selected?: boolean; guard?: boolean } = {}): string {
    const exported = this.exported(selected);
    return exported === null ? "" : csv(exported.text, guard);
  }

  /**
   * The rows as tab-separated text, as the export panel downloads them: as `toCSV()` has them,
   * with the cells' tabs and line breaks as spaces, and each line ending in a line feed. Empty
   * until hydrated.
   */
  toTSV({ selected = false, guard = true }: { selected?: boolean; guard?: boolean } = {}): string {
    const exported = this.exported(selected);
    return exported === null ? "" : `${toTSV(exported.text, guard)}\n`;
  }

  /**
   * The rows as records, as the export panel downloads them (as JSON): for each row `toCSV()`
   * has, an object with the text of each cell under its column's id, and with groups, the group's
   * label first, under `"group"` (or, while a column has that id, with a `_` before it). Empty
   * until hydrated.
   */
  toRecords({ selected = false }: { selected?: boolean } = {}): Record<string, string>[] {
    const exported = this.exported(selected);
    return exported === null ? [] : toRecords(exported.keys, exported.text.slice(1));
  }

  /**
   * Copy the rows to the clipboard (as `toCSV()` has them), as an HTML table and as tab-separated
   * text. Resolves to whether they were copied, which takes a click (or a key) the call is made in.
   */
  copyTable({ selected = false }: { selected?: boolean } = {}): Promise<boolean> {
    return this.copyRows(selected).then((rows) => rows !== null);
  }

  /**
   * The code for the view, as the export panel copies it: Python that filters and sorts the
   * table's data (as `df`) as the filters and sort do (not the search, which is of the text
   * shown), then drops the columns hidden, for Polars, pandas or Narwhals (by default, the data's
   * library), with its imports.
   * It's what Great Tables' `query_code()` writes. Empty until hydrated, and for a table without
   * "code" among its export formats (whose spec has what the code needs).
   *
   * @throws {RangeError} for another library, or a filter whose values can't be written (durations).
   */
  toCode(backend?: CodeBackend): string {
    const spec = this.spec;
    const code = spec?.export?.code;
    if (backend !== undefined && !CODE_BACKENDS.includes(backend)) {
      throw new RangeError(`\`backend\` must be "polars", "pandas" or "narwhals", not ${JSON.stringify(backend)}`);
    }
    return spec == null || code == null ? "" : viewCode(this.filter, this.sortKeys, this.hiddenIds, spec.filters ?? [], code, backend ?? code.backend);
  }

  /**
   * Go back to the view the table is first shown with: the filters, sort and hidden columns of the
   * author's view (`i_view()`), and the author's column order, without a search, on the first page
   * of the table's page size (and the body as tall as the author's). The view kept in
   * the URL and the browser's storage (with `view_state`) is cleared, and the reader's changes
   * can't be undone (see `undo()`). Does nothing until hydrated.
   */
  resetView(): void {
    if (this.authorView !== null) {
      this.showView(this.authorView);
      this.forget();
    }
  }

  /**
   * Undo the reader's last change to the view (with `view_state.undo`), returning whether there was
   * one. A run of changes to the search, or to one filter, each soon after the last, is one change;
   * going to another page isn't one, but is undone with the change after it. Setting a property
   * (but `page`) or calling `resetView()` forgets the changes before it.
   */
  undo(): boolean {
    return this.travel(this.past, this.future);
  }

  /** Redo the last change undone (see `undo()`), returning whether there was one. */
  redo(): boolean {
    return this.travel(this.future, this.past);
  }

  private hydrate(): void {
    if (!this.isConnected || this.table !== null) {
      return;
    }
    const table = this.querySelector("table");
    if (table === null) {
      // Nothing to hydrate yet; try again when children are added.
      this.setState("empty");
      if (this.observer === null) {
        this.observer = new MutationObserver(() => this.hydrate());
        this.observer.observe(this, { childList: true, subtree: true });
      }
      return;
    }
    this.stopObserving();
    this.table = table;

    // (Whatever its type: jQuery, with which Shiny shows HTML, changes the types of the scripts it
    // adds until they're all in)
    const script = this.querySelector<HTMLScriptElement>(":scope > script[data-gti-spec]");
    if (script === null) {
      this.setState("static");
      return;
    }

    let spec: Spec;
    try {
      spec = parseSpec(script.textContent ?? "");
      this.mapRows(table, spec);
    } catch (err) {
      if (!(err instanceof SpecError)) {
        throw err;
      }
      // The static table still works; it just isn't interactive.
      console.warn(`<gt-table>: ${err.message}; the table is left static.`);
      this.setState("error");
      return;
    }
    this.spec = spec;

    this.movable = !this.hasMergedStubCells();
    const state = spec.view_state;
    this.keeper = this.movable && state?.key != null && (state.url || state.storage) ? state : null;
    this.undoable = this.movable && state?.undo === true;
    this.order = spec.body.filter((entry): entry is number => typeof entry === "number");
    spec.columns.forEach((column, i) => {
      if (column.searchable === false) {
        this.unsearched.add(i);
      }
    });
    // Rows selected before hydration that the table can't have selected are dropped
    const mode = spec.controls.selection;
    const kept = this.selection.filter((row) => row < spec.nrows);
    this.selected = new Set(mode === null ? [] : mode === "single" ? kept.slice(0, 1) : kept);
    if (mode !== null) {
      this.addSelection(table, mode);
    }
    // (Before column widths are measured, since the cells' borders change)
    this.setLayout(table, spec);
    this.setDisplay(spec);
    this.addDetails(spec);
    if (this.movable && spec.controls.sorting) {
      this.addSortHeaders(table, spec);
    }
    if (this.movable && (spec.filters?.length ?? 0) > 0) {
      this.addFilters(table, spec);
    }
    this.alignLabels(table);
    this.addProfiles(table, spec);
    const bar = spec.controls.bar === true;
    if (this.movable && spec.controls.search && !bar) {
      this.addSearchBox(table);
    }
    if (spec.controls.resizing) {
      this.addResizers(table, spec);
    }
    this.addGuide(table);
    this.addFootHandle(spec);
    this.hideable = spec.columns.flatMap((column) =>
      column.role === "data" && column.hideable === true && column.id !== null ? [column.id] : [],
    );
    if (this.hideable.length > 0 || this.drops.length > 0) {
      this.mapColumns(table);
    }
    this.mapRuns(table);
    if (this.pageSizeValue === undefined) {
      this.pageSizeValue = spec.pagination.enabled ? spec.pagination.page_size : null;
    }
    // (With pages only, the bar comes with them)
    if (
      bar &&
      ((spec.export?.formats.length ?? 0) > 0 ||
        this.undoable ||
        this.hideable.length > 0 ||
        this.runs.length > 0 ||
        this.contents.size > 0 ||
        (this.movable && (spec.controls.search || this.filters.length > 0)))
    ) {
      this.addBar();
    }
    // (Columns are hidden whether or not rows can be moved)
    const hidden = spec.view?.hidden ?? [];
    for (const id of hidden.filter((id) => !this.hideable.includes(id))) {
      console.warn(`<gt-table>: the view's hidden column "${id}" is left out (it isn't one that can be hidden).`);
    }
    this.hideColumns(hidden);
    if (this.movable && spec.view !== undefined) {
      this.applySpecView(spec, spec.view);
    }
    if (this.movable) {
      this.authorView = {
        filter: this.filter,
        sort: this.sort,
        search: "",
        page: 1,
        pageSize: spec.pagination.enabled ? spec.pagination.page_size : null,
        hidden: this.hiddenColumns,
        order: this.columnOrder,
        ...(spec.layout.height === null ? {} : { height: null }),
      };
      this.restoreView(spec, this.authorView);
    }
    // A search or page set before hydration applies now
    this.matchRows();
    if (this.fit() || this.matched !== null || this.size !== null || this.sortKeys.length > 0 || this.hiddenIds.length > 0 || this.reordered()) {
      this.render();
    } else {
      // (Not rendered, so every row is shown, as it was)
      this.view = { start: 0, end: spec.nrows, total: spec.nrows };
      if (this.bar !== null) {
        this.updateBar(this.bar);
      }
      this.updateProfiles();
    }
    this.saveView();
    if (this.undoable) {
      this.present = this.currentView();
      this.addUndoKeys();
      this.syncUndo();
    }
    this.setState("ready");
  }

  // Sort and filter the table as the spec's view says (without events). A part of the view the
  // table can't have is left out, with a warning, and the rest applied.
  private applySpecView(spec: Spec, view: ViewSpec): void {
    try {
      this.sortKeys = normalizeSort(view.sort, spec.ranks);
    } catch (err) {
      if (!(err instanceof RangeError)) {
        throw err;
      }
      console.warn(`<gt-table>: the view's sort is left out (${err.message}).`);
    }
    try {
      this.setQuery(view.filter as FilterQuery | null);
    } catch (err) {
      if (!(err instanceof RangeError)) {
        throw err;
      }
      console.warn(`<gt-table>: the view's filter is left out (${err.message}).`);
    }
    for (const control of this.filters) {
      this.syncFilter(control);
    }
  }

  // Show the view kept in the URL, or else in the browser's storage (as `view_state` says), without
  // events. A part of it the table can't have is left out, with a warning, and the rest shown.
  private restoreView(spec: Spec, base: View): void {
    const state = this.keeper;
    const win = this.ownerDocument.defaultView;
    if (state === null || state.key === null || win === null) {
      return;
    }
    const params =
      (state.url ? readParams(win.location.search, state.key) : null) ??
      (state.storage ? readParams(this.storedView(state.key) ?? "") : null);
    if (params === null) {
      return;
    }
    const warn = (message: string) => console.warn(`<gt-table>: ${message}.`);
    const { size_select, page_size, page_sizes } = spec.pagination;
    const view = readView(
      params,
      base,
      {
        ranks: spec.controls.sorting ? spec.ranks : null,
        search: spec.controls.search,
        sizes: !spec.pagination.enabled ? [] : size_select ? [...page_sizes, page_size] : [page_size],
        // (Any, by the handle under the rows)
        maxSize: this.footHandle === null ? 0 : spec.nrows,
        height: spec.layout.height !== null,
        hideable: this.hideable,
        runs: this.runIds(),
      },
      warn,
    );
    try {
      this.setQuery(view.filter);
    } catch (err) {
      if (!(err instanceof RangeError)) {
        throw err;
      }
      warn(`the saved view's filter is left out (${err.message})`);
      view.filter = base.filter;
    }
    this.setView(view);
  }

  // Set the view's parts (the filters, sort, search, page, page size, height, hidden columns and
  // column order), to be shown
  private setView(view: View): void {
    this.orderColumns(view.order);
    this.hideColumns(view.hidden);
    this.cancelSearchTimer();
    this.cancelFilterTimer();
    this.setQuery(view.filter);
    for (const control of this.filters) {
      this.syncFilter(control);
    }
    this.sortKeys = view.sort.map((key) => ({ ...key }));
    this.searchValue = view.search;
    this.showSearch();
    this.pageSizeValue = view.pageSize;
    this.pageValue = view.page;
    this.heightValue = view.height ?? null;
    this.applyHeight();
  }

  // The view shown
  private currentView(): View {
    return {
      filter: this.filter,
      sort: this.sort,
      search: this.searchValue,
      page: this.page,
      pageSize: this.size,
      hidden: this.hiddenColumns,
      order: this.columnOrder,
      // (For a body that scrolls within a height)
      ...(this.spec?.layout.height == null ? {} : { height: this.heightValue }),
    };
  }

  // Whether the view is the one the table is first shown with, but for its page and search (which
  // the reset button, shown otherwise, puts back too)
  private isAuthorView(): boolean {
    return this.authorView === null || sameView({ ...this.currentView(), page: 1, search: "" }, this.authorView);
  }

  // Show a view
  private showView(view: View): void {
    this.setView(view);
    this.matchRows();
    this.render();
  }

  // Note the reader's change to the view, as one to undo. `part` is what it changed (`null`, for a
  // change of its own), and a run of changes to the same part, each soon after the last, is one;
  // going to another page ("page") isn't one, and is undone with the change after it.
  private record(part: string | null): void {
    const before = this.present;
    if (before === null) {
      return;
    }
    const now = this.currentView();
    const time = Date.now();
    const past = this.past;
    const run = part !== null && part === this.lastPart && time - this.lastTime < STEP_MS;
    this.present = now;
    this.lastPart = part;
    this.lastTime = time;
    if (part === "page") {
      return;
    }
    if (run) {
      // (A run that ends where it began is no change, and what follows, another)
      if (sameView(now, past[past.length - 1])) {
        past.pop();
        this.lastPart = null;
      }
    } else if (!sameView(now, before)) {
      past.push(before);
      if (past.length > UNDO_STEPS) {
        past.shift();
      }
      this.future = [];
    }
    this.syncUndo();
  }

  // The view, changed from code: the reader's changes before it can't be undone (with `clear`)
  private forget(clear = true): void {
    const before = this.present;
    if (before === null) {
      return;
    }
    this.present = this.currentView();
    this.lastPart = null;
    if (clear && !sameView(this.present, before)) {
      this.past = [];
      this.future = [];
      this.syncUndo();
    }
  }

  // Show the view last put on `from` (the views before the changes, to undo the last; or after the
  // changes undone, to redo it), putting the view shown on `to`
  private travel(from: View[], to: View[]): boolean {
    const view = from.pop();
    if (view === undefined) {
      return false;
    }
    to.push(this.currentView());
    this.showView(view);
    this.present = this.currentView();
    this.lastPart = null;
    this.syncUndo();
    return true;
  }

  private syncUndo(): void {
    this.bar?.undo?.setAttribute("aria-disabled", String(this.past.length === 0));
    this.bar?.redo?.setAttribute("aria-disabled", String(this.future.length === 0));
  }

  // Ctrl+Z (⌘Z) undoes, and Ctrl+Y or Ctrl+Shift+Z (⇧⌘Z) redoes, from anywhere in the table that
  // isn't for typing (whose text has its own undo)
  private addUndoKeys(): void {
    this.undoKey = (event: KeyboardEvent) => {
      const key = event.key.toLowerCase();
      if (
        !(event.ctrlKey || event.metaKey) ||
        event.altKey ||
        event.defaultPrevented ||
        (event.target as Element).closest(TYPED) !== null ||
        !(key === "z" || (key === "y" && event.ctrlKey && !event.shiftKey))
      ) {
        return;
      }
      event.preventDefault();
      this.userTravel(key === "z" && !event.shiftKey);
    };
    this.addEventListener("keydown", this.undoKey);
  }

  // Keep the view, as `view_state` says, when it has changed: in the URL (replacing the table's
  // parameters there, not adding to the history), and in the browser's storage
  private saveView(): void {
    const state = this.keeper;
    const base = this.authorView;
    const win = this.ownerDocument.defaultView;
    if (state === null || state.key === null || base === null || win === null) {
      return;
    }
    const params = viewParams(this.currentView(), base);
    const text = paramsText(params);
    if (text === this.keptText) {
      return;
    }
    this.keptText = text;
    // (A page in a sandboxed frame, say, can't have either)
    try {
      const { location, history } = win;
      if (state.url && paramsText(readParams(location.search, state.key) ?? []) !== text) {
        const query = writeParams(location.search, state.key, params);
        history.replaceState(history.state, "", `${location.pathname}${query}${location.hash}`);
      }
    } catch {
      // (Not kept in the URL)
    }
    try {
      if (state.storage) {
        const storage = win.localStorage;
        if (text === "") {
          storage.removeItem(this.storageKey(state.key));
        } else {
          storage.setItem(this.storageKey(state.key), text);
        }
      }
    } catch {
      // (Not kept in storage)
    }
  }

  // The view kept in the browser's storage, if any (and it can be read)
  private storedView(key: string): string | null {
    try {
      return this.ownerDocument.defaultView?.localStorage.getItem(this.storageKey(key)) ?? null;
    } catch {
      return null;
    }
  }

  // (Per page, as the URL's view is)
  private storageKey(key: string): string {
    return `gti:${this.ownerDocument.location?.pathname ?? ""}#${key}`;
  }

  private mapRows(table: HTMLTableElement, spec: Spec): void {
    const tbody = table.querySelector<HTMLTableSectionElement>(":scope > tbody.gt_table_body");
    const trs =
      tbody === null ? [] : Array.from(tbody.querySelectorAll<HTMLTableRowElement>(":scope > tr"));
    if (trs.length !== spec.body.length) {
      throw new SpecError(
        `the table body has ${trs.length} rows but the spec describes ${spec.body.length}`,
      );
    }

    // Data rows are in a group if the spec lists them in one
    const groups = new Map<string | null, Group>();
    const groupOf = (key: string | null): Group => {
      let group = groups.get(key);
      if (group === undefined) {
        group = { headings: [], top: [], bottom: [], cell: null };
        groups.set(key, group);
      }
      return group;
    };
    const rowGroups: (Group | null)[] = new Array<Group | null>(spec.nrows).fill(null);
    for (const { id, rows } of spec.groups) {
      for (const row of rows) {
        rowGroups[row] = groupOf(id);
      }
    }
    const groupCell = (tr: HTMLTableRowElement) =>
      tr.querySelector<HTMLTableCellElement>(":scope > th.gt_stub_row_group");

    const rowElements: HTMLTableRowElement[] = [];
    const bodyRows = new WeakMap<HTMLTableRowElement, BodyRow>();
    const blocks: Block[] = [];
    // The blocks since the last structural row, which is their anchor
    let open: Block[] = [];

    trs.forEach((tr, i) => {
      const entry = spec.body[i] as BodyRow;
      bodyRows.set(tr, entry);
      if (typeof entry !== "number") {
        for (const block of open) {
          block.anchor = tr;
        }
        open = [];
        // Group headings and summary rows belong to a group; grand summary rows don't
        if ("group" in entry) {
          const group = groupOf(entry.group);
          if (!("summary" in entry)) {
            group.headings.push(tr);
          } else if (entry.side === "top") {
            group.top.push(tr);
          } else {
            group.bottom.push(tr);
          }
          group.cell = groupCell(tr) ?? group.cell;
        }
        return;
      }
      rowElements[entry] = tr;
      const group = rowGroups[entry] ?? null;
      // Groups shown as a column have no headings between them, so a block also ends where
      // the group changes
      let block = open[open.length - 1];
      if (block === undefined || block.group !== group) {
        block = { rows: [], anchor: null, group, placed: [] };
        blocks.push(block);
        open.push(block);
      }
      block.rows.push(entry);
      block.placed.push(entry);
      const cell = groupCell(tr);
      if (cell !== null && group !== null) {
        group.cell = cell;
      }
    });

    this.tbody = tbody;
    this.rowElements = rowElements;
    this.bodyRows = bodyRows;
    this.blocks = blocks;
    this.groups = Array.from(groups.values());
    this.rowGroups = rowGroups;
  }

  // A body that scrolls within a height (which gti.css applies by the element's attribute), and a
  // table wider than its container that scrolls sideways with its stub pinned
  private setLayout(table: HTMLTableElement, spec: Spec): void {
    const { height } = spec.layout;
    let { responsive } = spec.layout;
    // (An "auto" table whose columns have priorities drops them, rather than being stacked)
    if (responsive === "auto" && spec.columns.some((column) => column.priority != null)) {
      responsive = "collapse";
    }
    this.toggleAttribute("data-gti-scroll", height !== null);
    if (height === null) {
      this.style.removeProperty("--gt-i-height");
    } else {
      this.style.setProperty("--gt-i-height", height);
    }
    if (height === null && responsive === null) {
      return;
    }
    this.addScroller(table);
    if (responsive !== null) {
      this.addPinning(table, spec, responsive);
    }
    if (height !== null) {
      this.addScroll(table);
    }
    if (responsive === "stack" || responsive === "auto") {
      this.addRoles(table);
      this.orderChips();
      this.syncStack();
    }
    if (responsive === "collapse") {
      this.addDrops(spec);
    }
    this.drawBorders();
    this.observeLayout();
  }

  // The columns a table can drop, in the order it drops them: those without a priority (from the
  // last), then those with the highest (from the last, among equals); not those with 1
  private addDrops(spec: Spec): void {
    const rank = (priority: number | null | undefined) => priority ?? Infinity;
    this.drops = spec.columns
      .flatMap((column, i) => (column.role === "data" && column.id !== null && column.priority !== 1 ? [{ id: column.id, i, rank: rank(column.priority) }] : []))
      .sort((a, b) => (a.rank === b.rank ? b.i - a.i : b.rank - a.rank))
      .map((column) => column.id);
    this.addExpanding();
  }

  // The data rows' details, from their templates (in the element), each row with them with a
  // button that opens it
  private addDetails(spec: Spec): void {
    const rows = spec.details ?? [];
    if (rows.length === 0) {
      return;
    }
    const templates = new Map(
      Array.from(this.querySelectorAll<HTMLTemplateElement>(":scope > template[data-gti-details]"), (template) => [
        template.dataset.gtiDetails,
        template,
      ]),
    );
    for (const row of rows) {
      const template = templates.get(String(row));
      const tr = this.rowElements[row];
      if (template === undefined || tr === undefined) {
        console.warn(`<gt-table>: row ${row}'s details are left out (it has no <template data-gti-details="${row}">).`);
        continue;
      }
      this.contents.set(tr, template);
      tr.classList.add("gt-i-has-details");
    }
    if (this.contents.size > 0) {
      this.addExpanding();
      this.syncExpanders();
    }
  }

  // A row's button opens it, or closes it (and isn't a click on the row), as does a tap on a row
  // with details on a touch screen (not on something of its own)
  private addExpanding(): void {
    const tbody = this.tbody;
    if (tbody === null || this.expanding) {
      return;
    }
    this.expanding = true;
    tbody.addEventListener("pointerdown", (event) => {
      this.pointer = event.pointerType;
    });
    tbody.addEventListener("click", (event) => {
      const button = (event.target as Element).closest?.(".gt-i-expand");
      const tapped = this.tapped(event);
      this.pointer = "";
      const tr = button == null ? tapped : button.closest("tr");
      if (tr == null) {
        return;
      }
      this.expand(tr, !this.opened.has(tr));
      this.render();
      // (Which moves the rows, and so the focus from it)
      (button as HTMLElement | null)?.focus({ preventScroll: true });
      this.updateInfo();
    });
  }

  // The row with details tapped on a touch screen (which opens it, rather than selecting it), unless
  // the tap was on something of its own, or ended selecting text in it
  private tapped(event: Event): HTMLTableRowElement | null {
    const target = event.target as Element;
    const tr = target.closest?.("tr");
    if (this.pointer !== "touch" || tr == null || !this.contents.has(tr) || onOwnControl(target, tr)) {
      return null;
    }
    const text = this.ownerDocument.getSelection();
    return text !== null && !text.isCollapsed && (tr.contains(text.anchorNode) || tr.contains(text.focusNode)) ? null : tr;
  }

  // Open or close every row with details (and, closing them, every row open)
  private expandAll(open: boolean): void {
    for (const tr of open ? this.contents.keys() : [...this.opened]) {
      this.expand(tr, open);
    }
    this.render();
    this.updateInfo();
  }

  /**
   * Drop columns while the table is wider than its container (and it has more it can drop), or
   * have the last dropped back while there's room for them again: with the columns fitted to
   * their contents measured for the container first. Whether the table is to be rendered again,
   * for that (with every row shown) or the columns shown.
   */
  private fit(): boolean {
    const { scroller, table } = this;
    if (scroller === null || table === null || this.drops.length === 0 || table.getClientRects().length === 0) {
      return false;
    }
    const room = scroller.clientWidth;
    this.fitRoom = room;
    const { dropped, dropNeeds } = this;
    const back = dropped.length;
    while (dropped.length > 0 && (dropNeeds[dropped.length - 1] as number) <= room + 1) {
      dropped.pop();
      dropNeeds.pop();
    }
    let changed = dropped.length < back;
    if (changed) {
      this.showColumns();
    } else if (this.colgroup !== null && this.startWidths === null) {
      this.remeasure();
      changed = true;
    }
    while (scroller.scrollWidth > room + 1) {
      const id = this.drops.find((id) => !dropped.includes(id) && !this.hiddenIds.includes(id));
      if (id === undefined) {
        break;
      }
      dropNeeds.push(scroller.scrollWidth);
      dropped.push(id);
      changed = true;
      this.showColumns();
    }
    return changed;
  }

  // Each row's button (in its first cell shown) that opens it: of each data row and summary row,
  // with columns dropped, and of each row with details; and the rows open show the columns dropped
  // now (made again as they're shown), or close, with none, but for those with details
  private syncExpanders(): void {
    const { tbody, spec } = this;
    if (tbody === null || spec === null || (this.drops.length === 0 && this.contents.size === 0)) {
      return;
    }
    const some = this.dropped.length > 0;
    this.toggleAttribute("data-gti-dropped", some);
    for (const tr of Array.from(tbody.querySelectorAll<HTMLTableRowElement>(":scope > tr"))) {
      const row = this.bodyRows.get(tr);
      const drops = some && row !== undefined && (typeof row === "number" || !("group" in row) || "summary" in row);
      if (!this.expanders.has(tr) && (drops || this.contents.has(tr))) {
        const label = this.rowLabel(tr);
        const button = element(this.ownerDocument, "button", "gt-i-expand", {
          type: "button",
          "aria-expanded": String(this.opened.has(tr)),
          "aria-label": label === "" ? "Show more of the row" : `Show more of ${label}`,
        });
        button.append(icon(this.ownerDocument, "expand"));
        this.expanders.set(tr, button);
      }
    }
    for (const [tr, button] of this.expanders) {
      const cell = Array.from(tr.cells).find((cell) => !cell.hidden && !cell.matches(".gt-i-select, .gt_stub_row_group"));
      if (cell !== undefined && button.parentElement !== cell) {
        button.parentElement?.classList.remove("gt-i-expands");
        cell.classList.add("gt-i-expands");
        cell.prepend(button);
      }
    }
    for (const tr of [...this.opened]) {
      this.details.get(tr)?.remove();
      this.details.delete(tr);
      if (!some && !this.contents.has(tr)) {
        this.expand(tr, false);
      }
    }
  }

  // Open a row, to show what's under it, or close it: a row open shows it in a row under it, made
  // as it's shown (see `placeDetails()`)
  private expand(tr: HTMLTableRowElement, open: boolean): void {
    this.details.get(tr)?.remove();
    this.details.delete(tr);
    this.expanders.get(tr)?.setAttribute("aria-expanded", String(open));
    tr.classList.toggle("gt-i-open", open);
    if (open) {
      this.opened.add(tr);
    } else {
      this.opened.delete(tr);
    }
  }

  // The row under a row open: the columns dropped from it, as their labels and values, then its
  // details, apart from the page's styles (and the table's), as the producer made them
  private makeDetails(tr: HTMLTableRowElement): HTMLTableRowElement {
    const spec = this.spec as Spec;
    const doc = this.ownerDocument;
    // (Kept in view, as the cells across the table)
    const body = element(doc, "div", "gt-i-details-body gt-i-inview");
    if (this.dropped.length > 0) {
      const labels = labelCells(this.table as HTMLTableElement);
      const cells = this.dataCells(tr);
      // (A row with stub cells merged into the row above has fewer)
      const skip = spec.columns.length - cells.length;
      const list = element(doc, "dl", "gt-i-details-list");
      spec.columns.forEach((_, place) => {
        const c = this.columnAt[place] ?? place;
        const id = spec.columns[c]?.id;
        const cell = cells[c - skip];
        if (id != null && cell !== undefined && this.dropped.includes(id)) {
          const value = element(doc, "dd", "");
          value.append(...Array.from(withoutMarks(cell).childNodes));
          const term = element(doc, "dt", "");
          term.textContent = this.columnTitle(id, labels);
          list.append(term, value);
        }
      });
      body.append(list);
    }
    const template = this.contents.get(tr);
    if (template !== undefined) {
      const content = element(doc, "div", "gt-i-details-content");
      content.attachShadow({ mode: "open" }).append(doc.importNode(template.content, true));
      body.append(content);
    }
    const details = element(doc, "tr", "gt-i-details");
    const td = element(doc, "td", "gt_row gt_left gt-i-inview-cell");
    td.append(body);
    details.append(td);
    if (this.table?.hasAttribute("role")) {
      addRowRoles(details);
    }
    return details;
  }

  // The rows under the rows open go under them (spanned by their group's label cell, as a column),
  // spanning the columns shown: made once their row is shown, and hidden while the rows are measured
  private placeDetails(): void {
    for (const tr of this.opened) {
      let details = this.details.get(tr);
      if (details === undefined) {
        if (tr.hidden || this.measuring) {
          continue;
        }
        details = this.makeDetails(tr);
        this.details.set(tr, details);
      }
      if (tr.nextSibling !== details) {
        tr.after(details);
      }
      setHidden(details, tr.hidden === true || this.measuring);
      const row = this.bodyRows.get(tr);
      const group = typeof row === "number" ? this.rowGroups[row] : this.groups.find((group) => group.top.includes(tr) || group.bottom.includes(tr));
      const cell = group?.cell;
      const spanned = cell != null && !details.hidden && cell.parentElement !== null;
      if (spanned) {
        cell.rowSpan++;
      }
      // (With a cell of its own in the selection column, when that's before the label cell)
      const first = details.cells[0] as HTMLTableCellElement;
      const lead = spanned && tr.cells[0]?.classList.contains("gt-i-select") === true;
      if (lead !== first.classList.contains("gt-i-select")) {
        if (lead) {
          details.prepend(element(this.ownerDocument, "td", "gt_row gt-i-select"));
        } else {
          first.remove();
        }
      }
      (details.lastElementChild as HTMLTableCellElement).colSpan = this.emptySpan() - (spanned ? 1 : 0) - (lead ? 1 : 0);
    }
  }

  /**
   * A table that can be stacked keeps its rows' and cells' roles (which a table, its rows and its
   * cells laid out as blocks would lose, in some browsers), from its elements.
   */
  private addRoles(table: HTMLTableElement): void {
    table.setAttribute("role", "table");
    for (const section of Array.from(table.querySelectorAll(":scope > :is(thead, tbody, tfoot)"))) {
      section.setAttribute("role", "rowgroup");
    }
    for (const tr of Array.from(table.rows)) {
      addRowRoles(tr);
    }
  }

  /**
   * Whether the table is stacked now (`data-gti-stacked`): by its CSS, which says so with
   * `--gt-i-stacked`, while it isn't stacked whatever its width (`data-gti-stack-off`, for an
   * "auto" table showing more than a few data columns, or one in a container as wide as what's in
   * it). Whether that changed: once it isn't, the
   * cells' borders are read again (for the borders drawn on them).
   */
  private syncStack(): boolean {
    const { table, spec, responsive } = this;
    if (table === null || spec === null || (responsive !== "stack" && responsive !== "auto")) {
      return false;
    }
    const shown = spec.columns.filter((column) => column.role === "data").length - this.hiddenIds.length;
    let off = responsive === "auto" && shown > STACK_COLUMNS;
    if (!off) {
      this.removeAttribute("data-gti-stack-off");
      this.fitted ??= this.fitsContent();
      off = this.fitted === true;
    }
    this.toggleAttribute("data-gti-stack-off", off);
    const stacked = getComputedStyle(table).getPropertyValue("--gt-i-stacked").trim() === "1";
    if (stacked === this.stacked) {
      return false;
    }
    this.stacked = stacked;
    this.toggleAttribute("data-gti-stacked", stacked);
    if (!stacked) {
      this.borders?.reset();
    }
    return true;
  }

  /**
   * Whether the table's container is as wide as what's in it (as a table's cell, a float or an
   * inline block is), which it can't be stacked in: as the container its width is queried in, the
   * table would have no width of its own. Measured as that container, by whether a width for
   * what's in it widens it; `null` while it isn't shown.
   */
  private fitsContent(): boolean | null {
    if (this.getClientRects().length === 0) {
      return null;
    }
    const width = this.offsetWidth;
    this.style.setProperty("contain-intrinsic-inline-size", "9999px");
    const fits = this.offsetWidth > width;
    this.style.removeProperty("contain-intrinsic-inline-size");
    return fits;
  }

  // The column labels, as chips above the cards of a stacked table, are in their columns' order
  // (the labels under spanners being in another row; `order` doesn't change a table's layout)
  private orderChips(): void {
    const thead = this.table?.tHead;
    if (thead == null) {
      return;
    }
    const rows = Array.from(thead.querySelectorAll<HTMLTableRowElement>(":scope > tr.gt_col_headings"));
    for (const { cell, c0 } of placeCells(rows).placed) {
      cell.style.order = String(c0);
    }
  }

  // The container the table scrolls in: GT's `<div>` around the table (or ours, without one)
  private addScroller(table: HTMLTableElement): void {
    let scroller = table.parentElement;
    if (scroller === null || scroller === this || scroller.tagName !== "DIV") {
      scroller = this.ownerDocument.createElement("div");
      table.before(scroller);
      scroller.append(table);
    }
    scroller.classList.add("gt-i-scroller");
    this.scroller = scroller;
    scroller.addEventListener("scroll", () => this.scrolled(), { passive: true });
  }

  private scrolled(): void {
    // The hint goes once the reader has scrolled sideways
    if (this.hint !== null && Math.abs(this.scroller?.scrollLeft ?? 0) > 0.5) {
      this.hint.remove();
      this.hint = null;
      this.hinted = true;
    }
    this.queueShades();
  }

  /**
   * Get ready for the table being wider than its container (see `pin()`): mark the cells of the
   * columns that stay in view at its inline start (the selection column and the stub, with the
   * row group column, and the data columns pinned there) and at its end (`gt-i-pin` marking the
   * data columns', which stay in view while there's room), and the cells across the table, whose
   * contents stay in view.
   */
  private addPinning(table: HTMLTableElement, spec: Spec, mode: ResponsiveMode): void {
    this.responsive = mode;
    // (Every row is shown on hydration)
    const { placed, columns: width } = placeCells(Array.from(table.rows));
    const tbody = this.tbody;
    const stub = placed.filter(
      (p) =>
        p.cell.parentElement?.parentElement === tbody &&
        p.cell.matches(".gt_stub, .gt_stub_row_group, .gt-i-select"),
    );
    const stubColumns = Math.max(0, ...stub.map((p) => p.c1 + 1));
    // The data columns follow the stub's, and pinned ones are next to their side
    const data = spec.columns.filter((column) => column.role === "data");
    let columns = stubColumns;
    while (data[columns - stubColumns]?.pin === "start") {
      columns++;
    }
    let ends = 0;
    while (width - ends > columns && data[data.length - ends - 1]?.pin === "end") {
      ends++;
    }
    for (const p of placed) {
      const start = p.c1 < columns;
      if ((start || p.c0 >= width - ends) && p.cell.parentElement?.parentElement?.tagName !== "TFOOT") {
        p.cell.classList.add("gt-i-pinned");
        p.cell.classList.toggle("gt-i-pin", !start || p.c1 >= stubColumns);
      }
    }
    this.pinColumns = columns;
    this.stubColumns = stubColumns;
    this.endColumns = ends;
    this.gridColumns = width;
    this.acrossCells = Array.from(
      table.querySelectorAll<HTMLTableCellElement>(
        ":scope > thead > tr > :is(.gt_title, .gt_subtitle), " +
          ":scope > tbody > tr > :is(.gt_group_heading, .gt_empty_group_heading), " +
          ":scope > tfoot > tr > :is(.gt_footnote, .gt_sourcenote)",
      ),
    );
  }

  /**
   * Scroll the body within the table's container (GT's `<div>` around the table), under column
   * labels (and the table's header) that stay in view, with each group's heading stuck below them
   * while its rows go by, and the grand summary rows at the bottom stuck to the bottom. Footnotes
   * and source notes scroll with the body.
   */
  private addScroll(table: HTMLTableElement): void {
    this.scrollsDown = true;
    this.stuckTop = this.groups.flatMap((group) => group.headings);
    this.stuckBottom = (this.tbody === null ? [] : Array.from(this.tbody.querySelectorAll<HTMLTableRowElement>(":scope > tr"))).filter((tr) => {
      const entry = this.bodyRows.get(tr);
      return typeof entry === "object" && "grand_summary" in entry && entry.side === "bottom";
    });
    for (const tr of this.stuckBottom) {
      tr.classList.add("gt-i-stuck-bottom");
    }
    this.separateBorders();

    // Rows scroll under the sticky ones, which need a background to hide them
    const backdrop = backdropColor(table);
    const thead = table.tHead;
    if (thead !== null && isTransparent(getComputedStyle(thead).backgroundColor)) {
      thead.style.backgroundColor = backdrop;
    }
    for (const tr of [...this.stuckTop, ...this.stuckBottom]) {
      for (const cell of Array.from(tr.cells)) {
        if (isTransparent(getComputedStyle(cell).backgroundColor)) {
          cell.style.backgroundColor = backdrop;
        }
      }
    }

    this.addShade("top");
    this.addShade("bottom");
    this.setAttribute("data-gti-sticky", "");
  }

  // The table's borders, drawn on its cells (from now on), so that they move with the cells that
  // stick: the sticky rows draw the edges between them and the rows that scroll under them, and
  // the pinned cells the edges between them and the cells that scroll under them
  private separateBorders(): TableBorders {
    if (this.borders === null) {
      const sticky = new Set([...this.stuckTop, ...this.stuckBottom]);
      this.borders = new TableBorders(
        this.table as HTMLTableElement,
        (tr) => tr.parentElement?.tagName === "THEAD" || sticky.has(tr),
        (cell) => cell.matches(".gt-i-pinned, .gt-i-pin"),
      );
    }
    return this.borders;
  }

  private addShade(edge: Side): void {
    const div = this.ownerDocument.createElement("div");
    div.className = "gt-i-shade";
    div.setAttribute("data-gti-edge", edge);
    div.setAttribute("aria-hidden", "true");
    this.append(div);
    this.shades[edge] = div;
  }

  // Draw the borders of the rows shown, pin the stub if the table is wider than its container,
  // and stick the sticky rows where they go
  private drawBorders(): void {
    const borders = this.borders;
    if (borders !== null) {
      borders.redraw();
      // A group heading's own top border slides under the column labels' bottom one as it sticks
      for (const tr of this.stuckTop) {
        for (const cell of Array.from(tr.cells)) {
          const own = borders.drawnBorder(cell, "top")?.width ?? 0;
          setStyle(cell, "top", own > 0 ? `calc(var(--gt-i-head, 0px) - ${own}px)` : "var(--gt-i-head, 0px)");
        }
      }
    }
    this.pin();
    this.stick();
  }

  // Measure the sticky rows: how far down group headings stick, and how far up each row stuck at
  // the bottom does (above the ones after it); and keep what has focus clear of them
  private stick(): void {
    const scroller = this.scroller;
    const table = this.table;
    if (scroller === null || table === null) {
      return;
    }
    if (this.scrollsDown) {
      // Sticky boxes stop short of the container's padding, which rows would show through: they
      // stick over it instead
      const padding = getComputedStyle(scroller);
      const padTop = parseFloat(padding.paddingTop) || 0;
      const padBottom = parseFloat(padding.paddingBottom) || 0;
      const head = table.tHead?.getBoundingClientRect().height ?? 0;
      let foot = 0;
      for (let i = this.stuckBottom.length - 1; i >= 0; i--) {
        const tr = this.stuckBottom[i] as HTMLTableRowElement;
        if (tr.hidden) {
          continue;
        }
        for (const cell of Array.from(tr.cells)) {
          setStyle(cell, "bottom", `${foot - padBottom}px`);
        }
        foot += tr.getBoundingClientRect().height;
      }
      const heading = Math.max(0, ...this.stuckTop.filter((tr) => !tr.hidden).map((tr) => tr.getBoundingClientRect().height));
      this.foot = foot;
      setStyle(this, "--gt-i-pad", `${padTop}px`);
      setStyle(this, "--gt-i-head", `${head - padTop}px`);
      setStyle(scroller, "scroll-padding-top", `${head + heading}px`);
      setStyle(scroller, "scroll-padding-bottom", `${foot}px`);
    }
    this.markRegion();
    this.placeShades();
  }

  /**
   * While the table is wider than its container (`data-gti-wide`, which gti.css sticks the cells
   * marked `gt-i-pinned` by), pin the stub (and the data columns pinned at either side, while
   * they take up at most half the container) where its columns are in the rows shown, and keep the
   * contents of the cells across the table in the part in view. The table's borders are drawn on
   * its cells from the first time, and a hint says it scrolls, until it first does.
   */
  private pin(): void {
    const { scroller, table } = this;
    this.cancelPin();
    if (this.responsive === null || scroller === null || table === null) {
      return;
    }
    // (A stacked table's cards fit its container)
    const wide = !this.stacked && scroller.scrollWidth > scroller.clientWidth + 1;
    this.toggleAttribute("data-gti-wide", wide);
    if (!wide) {
      this.hint?.removeAttribute("data-gti-shown");
      this.placeShades();
      return;
    }
    if (this.inView === null) {
      const across = this.empty === null ? this.acrossCells : [...this.acrossCells, this.empty.cells[0] as HTMLTableCellElement];
      this.inView = across.map(keepInView);
      this.addShade("left");
      this.addShade("right");
    }
    if (!this.hinted && this.hint === null) {
      this.hint = this.ownerDocument.createElement("div");
      this.hint.className = "gt-i-hint";
      this.hint.setAttribute("aria-hidden", "true");
      this.hint.textContent = this.isRtl() ? "← Scroll for more" : "Scroll for more →";
      // (In the table's font, which is the table's own)
      this.hint.style.fontFamily = getComputedStyle(table).fontFamily;
      this.append(this.hint);
    }
    this.hint?.setAttribute("data-gti-shown", "");

    const view = getComputedStyle(scroller);
    const padStart = parseFloat(view.paddingInlineStart) || 0;
    const padEnd = parseFloat(view.paddingInlineEnd) || 0;
    // (On the grid of the columns shown)
    const { pinColumns, endColumns, gridColumns, hiddenGrid } = this;
    const gone = (from: number, to: number) => [...hiddenGrid].filter((c) => from <= c && c < to).length;
    const columns = pinColumns - gone(0, pinColumns);
    const ends = endColumns - gone(gridColumns - endColumns, gridColumns);
    const width = gridColumns - hiddenGrid.size;
    if (columns > 0 || ends > 0) {
      if (this.borders === null) {
        this.separateBorders().redraw();
      }
      // Each pinned column sticks after the ones before it (or, at the end, before the ones after
      // it), as wide as they are in the rows shown
      const rows = Array.from(table.rows).filter((tr) => !tr.hidden && tr.parentElement?.tagName !== "TFOOT");
      const marked = placeCells(rows).placed.filter((p) => p.cell.matches(".gt-i-pinned, .gt-i-pin"));
      const starts = marked.filter((p) => p.c1 < columns);
      const endings = marked.filter((p) => p.c0 >= width - ends);
      const before: (number | undefined)[] = [0];
      for (let c = 0; c < columns; c++) {
        const at = before[c];
        for (const p of starts) {
          if (at !== undefined && p.c0 === c && before[p.c1 + 1] === undefined) {
            before[p.c1 + 1] = at + p.cell.getBoundingClientRect().width;
          }
        }
      }
      const after: (number | undefined)[] = [];
      after[width] = 0;
      for (let c = width; c > width - ends; c--) {
        const at = after[c];
        for (const p of endings) {
          if (at !== undefined && p.c1 === c - 1 && after[p.c0] === undefined) {
            after[p.c0] = at + p.cell.getBoundingClientRect().width;
          }
        }
      }
      // The data columns are pinned while there's room for them: only the stub is, in a container
      // they'd take up more than half of
      const crowded =
        columns + ends > this.stubColumns && (before[columns] ?? 0) + (after[width - ends] ?? 0) > scroller.clientWidth / 2;
      const kept = crowded ? this.stubColumns : columns;
      for (const p of starts) {
        p.cell.classList.toggle("gt-i-pinned", p.c1 < kept);
        if (p.c1 < kept) {
          setStyle(p.cell, "inset-inline-start", `${(before[p.c0] ?? 0) - padStart}px`);
          this.fill(p.cell);
        }
      }
      for (const p of endings) {
        p.cell.classList.toggle("gt-i-pinned", !crowded);
        if (!crowded) {
          setStyle(p.cell, "inset-inline-end", `${(after[p.c1 + 1] ?? 0) - padEnd}px`);
          this.fill(p.cell);
        }
      }
      this.edgeCell = starts.find((p) => p.c1 === kept - 1)?.cell ?? null;
      this.endEdge = crowded ? null : (endings.find((p) => p.c0 === width - ends)?.cell ?? null);
      // (What has focus is kept clear of them)
      setStyle(scroller, "scroll-padding-inline-start", `${before[kept] ?? 0}px`);
      setStyle(scroller, "scroll-padding-inline-end", `${crowded ? 0 : (after[width - ends] ?? 0)}px`);
    }

    // The contents of the cells across the table are as wide as the part in view, and stick in it
    // (and the columns dropped from a row, under it)
    for (const div of [...this.inView, ...Array.from(this.details.values(), (tr) => tr.lastElementChild?.firstElementChild as HTMLElement)]) {
      const cell = div.parentElement;
      if (cell === null || !div.isConnected || (cell.parentElement as HTMLTableRowElement).hidden) {
        continue;
      }
      const style = getComputedStyle(cell);
      const start = (parseFloat(style.paddingInlineStart) || 0) + (parseFloat(style.borderInlineStartWidth) || 0);
      const end = (parseFloat(style.paddingInlineEnd) || 0) + (parseFloat(style.borderInlineEndWidth) || 0);
      setStyle(div, "inset-inline-start", `${start - padStart}px`);
      setStyle(div, "--gt-i-room", `${Math.max(0, scroller.clientWidth - start - end)}px`);
    }
    this.markRegion();
    this.placeShades();
  }

  // A pinned cell hides the cells that scroll under it: one without a background, or with one
  // that's see-through (a stripe), is filled with what's behind it (in gti.css, while pinned)
  private fill(cell: HTMLTableCellElement): void {
    const style = getComputedStyle(cell);
    const filled = cell.classList.contains("gt-i-filled");
    if (!filled && (style.backgroundImage || "none") !== "none") {
      // (The author's)
      return;
    }
    const color = style.backgroundColor;
    if (opacity(color) >= 1) {
      cell.classList.remove("gt-i-filled");
      return;
    }
    const behind = backdropColor(cell.parentElement as Element);
    setStyle(cell, "--gt-i-fill", `linear-gradient(${color || "transparent"}, ${color || "transparent"}), linear-gradient(${behind}, ${behind})`);
    cell.classList.add("gt-i-filled");
  }

  private queuePin(): void {
    if (this.responsive !== null && this.pinFrame === 0 && typeof requestAnimationFrame !== "undefined") {
      this.pinFrame = requestAnimationFrame(() => {
        this.pinFrame = 0;
        this.pin();
      });
    }
  }

  private cancelPin(): void {
    if (this.pinFrame !== 0) {
      cancelAnimationFrame(this.pinFrame);
      this.pinFrame = 0;
    }
  }

  // A container that scrolls is a region named for the table, which can have focus, so that it
  // can be scrolled with the keyboard (unless the author made it focusable already)
  private markRegion(): void {
    const { scroller, table } = this;
    if (scroller === null || table === null) {
      return;
    }
    const scrolls = scroller.scrollWidth > scroller.clientWidth + 1 || scroller.scrollHeight > scroller.clientHeight + 1;
    if (scrolls && !this.regioned && !scroller.hasAttribute("tabindex")) {
      scroller.tabIndex = 0;
      scroller.setAttribute("role", "region");
      const title = table.getAttribute("aria-labelledby");
      if (title !== null) {
        scroller.setAttribute("aria-labelledby", title);
      } else {
        scroller.setAttribute("aria-label", "Table");
      }
      this.regioned = true;
    } else if (!scrolls && this.regioned) {
      for (const name of ["tabindex", "role", "aria-labelledby", "aria-label"]) {
        scroller.removeAttribute(name);
      }
      this.regioned = false;
    }
  }

  private queueShades(): void {
    if (this.shadeFrame === 0 && typeof requestAnimationFrame !== "undefined") {
      this.shadeFrame = requestAnimationFrame(() => {
        this.shadeFrame = 0;
        this.placeShades();
        this.placeGuide();
      });
    }
  }

  private cancelShades(): void {
    if (this.shadeFrame !== 0) {
      cancelAnimationFrame(this.shadeFrame);
      this.shadeFrame = 0;
    }
  }

  // The shadows go over the part of the table in view: the top one under the column labels (and a
  // group heading stuck under them), the bottom one over the rows stuck at the bottom; the one at
  // the inline start along the pinned columns, the one at the end along the container's edge (or
  // the columns pinned there), from the column labels to the end of the body. The hint sits by
  // the end, halfway down (or near the top)
  private placeShades(): void {
    const { scroller, shades, table } = this;
    if (scroller === null || table === null) {
      return;
    }
    const outer = this.getBoundingClientRect();
    const port = scroller.getBoundingClientRect();
    const box = table.getBoundingClientRect();
    const top = port.top + scroller.clientTop;
    const bottom = top + scroller.clientHeight;
    const start = port.left + scroller.clientLeft;
    const end = start + scroller.clientWidth;
    const x = (at: number) => `${at - outer.left - this.clientLeft}px`;
    const y = (at: number) => `${at - outer.top - this.clientTop}px`;

    if (shades.top !== undefined && shades.bottom !== undefined) {
      const left = Math.max(box.left, start);
      const right = Math.min(box.right, end);
      // (Measured, since the column labels stick only once the container's padding scrolls by)
      const head = table.tHead === null ? top : table.tHead.getBoundingClientRect().bottom;
      let under = Math.max(0, head - top);
      for (const tr of this.stuckTop) {
        const cell = tr.hidden ? undefined : tr.cells[0];
        if (cell === undefined) {
          continue;
        }
        const rect = cell.getBoundingClientRect();
        if (rect.top > head + 0.5) {
          // (Headings further down aren't stuck)
          break;
        }
        under = Math.max(under, rect.bottom - top);
      }
      const place = (shade: HTMLElement, at: number, shown: boolean) => {
        setStyle(shade, "top", y(at));
        setStyle(shade, "left", x(left));
        setStyle(shade, "width", `${Math.max(0, right - left)}px`);
        shade.toggleAttribute("data-gti-shown", shown);
      };
      place(shades.top, top + under, scroller.scrollTop > 0);
      place(shades.bottom, bottom - this.foot, scroller.scrollTop + scroller.clientHeight < scroller.scrollHeight - 1);
    }

    if (shades.left === undefined || shades.right === undefined) {
      return;
    }
    const wide = this.hasAttribute("data-gti-wide");
    const labels = table.querySelector(":scope > thead > tr.gt_col_headings") ?? this.tbody;
    const y0 = Math.max(top, labels?.getBoundingClientRect().top ?? box.top);
    const y1 = Math.min(bottom, this.tbody?.getBoundingClientRect().bottom ?? box.bottom);
    const rtl = this.isRtl();
    const edge = this.edgeCell?.isConnected ? this.edgeCell.getBoundingClientRect() : null;
    const endEdge = this.endEdge?.isConnected ? this.endEdge.getBoundingClientRect() : null;
    const scrolled = Math.abs(scroller.scrollLeft);
    const place = (shade: HTMLElement, at: number, shown: boolean) => {
      setStyle(shade, "top", y(y0));
      setStyle(shade, "left", x(at));
      setStyle(shade, "height", `${Math.max(0, y1 - y0)}px`);
      shade.toggleAttribute("data-gti-shown", wide && shown);
    };
    const past = scrolled > 0.5;
    const more = scrolled + scroller.clientWidth < scroller.scrollWidth - 1;
    if (rtl) {
      place(shades.right, edge?.left ?? end, past);
      place(shades.left, endEdge?.right ?? start, more);
    } else {
      place(shades.left, edge?.right ?? start, past);
      place(shades.right, endEdge?.left ?? end, more);
    }
    const hint = this.hint;
    if (hint !== null && wide) {
      // (Not far down a long table, which may go past the window)
      setStyle(hint, "top", y(Math.min((y0 + y1) / 2, y0 + 120)));
      setStyle(hint, "left", x(rtl ? (endEdge?.right ?? start) + 8 : (endEdge?.left ?? end) - 8 - hint.offsetWidth));
    }
  }

  // Row highlighting and text wrapping, which gti.css styles by the element's attributes
  private setDisplay(spec: Spec): void {
    const { highlight, wrap } = spec.display;
    this.toggleAttribute("data-gti-nowrap", !wrap);
    this.toggleAttribute("data-gti-highlight", highlight);
    this.cutsText = !wrap && this.table?.querySelector(":scope > colgroup") != null;
    if (this.cutsText) {
      this.fixWidths();
      this.observeLayout();
    }
    const tbody = this.tbody;
    if (!highlight || tbody === null) {
      return;
    }
    for (const tr of this.rowElements) {
      tr.classList.add("gt-i-row");
    }
    // Nothing hovers on a touch screen, so a tap marks the row instead (until it's tapped again,
    // or another row is)
    tbody.addEventListener("pointerdown", (event) => {
      this.touched = event.pointerType === "touch";
    });
    tbody.addEventListener("click", (event) => {
      const touched = this.touched;
      this.touched = false;
      const target = event.target as Element;
      const tr = target.closest("tr");
      if (
        !touched ||
        tr === null ||
        tr.parentElement !== tbody ||
        typeof this.bodyRow(tr) !== "number" ||
        onOwnControl(target, tr)
      ) {
        return;
      }
      this.marked?.classList.remove("gt-i-marked");
      this.marked = tr === this.marked ? null : tr;
      this.marked?.classList.add("gt-i-marked");
    });
  }

  // A hierarchical stub merges cells across rows (`rowspan`), which reordering would break
  private hasMergedStubCells(): boolean {
    return this.rowElements.some((tr) =>
      Array.from(tr.children).some(
        (cell) =>
          !cell.classList.contains("gt_stub_row_group") &&
          Number(cell.getAttribute("rowspan") ?? 1) > 1,
      ),
    );
  }

  /**
   * A column of checkboxes before the others, for selecting rows: one per data row, and (when
   * several rows can be selected) one in the column labels for every row that matches the search.
   * Clicking anywhere else on a data row selects it too.
   */
  private addSelection(table: HTMLTableElement, mode: SelectionMode): void {
    const doc = this.ownerDocument;
    const tbody = this.tbody as HTMLTableSectionElement;
    // The rows across the table (title, group headings, footer) span the new column too
    const widen = (tr: HTMLTableRowElement) => {
      const cell = tr.firstElementChild;
      cell?.setAttribute("colspan", String(Number(cell.getAttribute("colspan") ?? 1) + 1));
    };
    // A cell in the column, styled as the row's other body cells are
    const cell = (tr: HTMLTableRowElement) => {
      const td = doc.createElement("td");
      const model = tr.querySelector(":scope > td");
      const classes = model === null ? ["gt_row"] : Array.from(model.classList).filter((c) => !/^gt_(left|right|center)$/.test(c));
      td.className = [...classes, "gt_center", "gt-i-select"].join(" ");
      tr.prepend(td);
      return td;
    };

    const headings = Array.from(table.querySelectorAll<HTMLTableRowElement>(":scope > thead > tr.gt_col_headings"));
    const first = headings[0];
    if (first !== undefined) {
      const th = doc.createElement("th");
      th.className = "gt_col_heading gt_columns_bottom_border gt_center gt-i-select";
      th.scope = "col";
      if (headings.length > 1) {
        th.rowSpan = headings.length;
      }
      if (mode === "multiple") {
        const box = this.checkbox("Select all rows");
        box.addEventListener("click", () => this.userSelectAll());
        // (The whole cell is the target)
        th.addEventListener("click", (event) => {
          if (event.target === th) {
            box.click();
          }
        });
        th.append(box);
        this.selectAll = box;
        this.addLiveRegion();
      } else {
        const label = doc.createElement("span");
        label.className = "gt-i-hidden";
        label.textContent = "Select";
        th.append(label);
      }
      first.prepend(th);
    }
    for (const tr of table.querySelectorAll<HTMLTableRowElement>(
      ":scope > thead > tr:not(.gt_col_headings), :scope > tfoot > tr",
    )) {
      widen(tr);
    }
    for (const tr of tbody.querySelectorAll<HTMLTableRowElement>(":scope > tr")) {
      const entry = this.bodyRow(tr);
      if (typeof entry === "number") {
        const box = this.checkbox(`Select ${this.rowLabel(tr) || `row ${entry + 1}`}`);
        box.addEventListener("click", (event) => this.userSelect(entry, this.shifted(event)));
        cell(tr).append(box);
        this.selectBoxes[entry] = box;
      } else if (entry !== null && ("summary" in entry || "grand_summary" in entry)) {
        cell(tr);
      } else {
        widen(tr);
      }
    }
    const colgroup = table.querySelector(":scope > colgroup");
    if (colgroup !== null) {
      const col = doc.createElement("col");
      col.className = "gt-i-select";
      col.style.width = "2.5em";
      colgroup.prepend(col);
    }
    this.selectColumn = true;

    // Shift-click selects a range of rows, rather than extending the page's text selection
    if (mode === "multiple") {
      tbody.addEventListener("mousedown", (event) => {
        if (event.shiftKey && this.clickedRow(event) !== null) {
          event.preventDefault();
        }
      });
    }
    tbody.addEventListener("click", (event) => {
      const row = this.clickedRow(event);
      // (Not when the click ends selecting text in the row, nor for a tap opening it)
      const text = this.ownerDocument.getSelection();
      const tr = row === null ? null : this.rowElements[row];
      if (
        row === null ||
        this.tapped(event) !== null ||
        (text !== null && !text.isCollapsed && (tr?.contains(text.anchorNode) || tr?.contains(text.focusNode)))
      ) {
        return;
      }
      this.userSelect(row, event.shiftKey);
    });
    this.showSelection();
  }

  // The data row clicked, unless the click was on something of its own (a link, a checkbox) or on
  // a group's label cell
  private clickedRow(event: Event): number | null {
    const target = event.target as Element;
    const tr = target.closest("tr");
    const row = tr === null || tr.parentElement !== this.tbody ? null : this.bodyRow(tr);
    return typeof row === "number" && !onOwnControl(target, tr as HTMLTableRowElement) ? row : null;
  }

  private checkbox(label: string): HTMLInputElement {
    const box = this.ownerDocument.createElement("input");
    box.type = "checkbox";
    box.setAttribute("aria-label", label);
    return box;
  }

  // A data row's label: its stub cells' text
  private rowLabel(tr: HTMLTableRowElement): string {
    return Array.from(tr.querySelectorAll<HTMLTableCellElement>(":scope > .gt_stub"), labelText)
      .filter((text) => text !== "")
      .join(" ");
  }

  // A click on a row (or its checkbox) toggles it; with Shift (when several can be selected),
  // the rows from the last one clicked, in the order shown, follow it
  private userSelect(row: number, range: boolean): void {
    const mode = this.spec?.controls.selection;
    const on = !this.selected.has(row);
    let rows = [row];
    if (mode === "multiple" && range && this.selectAnchor !== null) {
      const from = this.order.indexOf(this.selectAnchor);
      const to = this.order.indexOf(row);
      if (from !== -1 && to !== -1) {
        rows = this.order.slice(Math.min(from, to), Math.max(from, to) + 1);
      }
    }
    if (mode === "single") {
      this.selected.clear();
    }
    for (const r of rows) {
      if (on) {
        this.selected.add(r);
      } else {
        this.selected.delete(r);
      }
    }
    this.selectAnchor = row;
    this.showSelection();
    if (rows.length > 1) {
      this.announce(this.selectionText());
    }
    this.dispatchSelect();
  }

  // The select-all checkbox selects every row that matches the search, or deselects them if they
  // all are
  private userSelectAll(): void {
    const all = this.order.every((row) => this.selected.has(row));
    for (const row of this.order) {
      if (all) {
        this.selected.delete(row);
      } else {
        this.selected.add(row);
      }
    }
    this.selectAnchor = null;
    this.showSelection();
    this.announce(this.selectionText());
    this.dispatchSelect();
  }

  // The info panel's clear button deselects every row, matching the search or not
  private userClearSelection(): void {
    if (this.selected.size === 0) {
      return;
    }
    this.selected.clear();
    this.selectAnchor = null;
    this.showSelection();
    this.announce(this.selectionText());
    this.dispatchSelect();
  }

  private selectionText(): string {
    const count = this.selected.size;
    return count === 0 ? "No rows selected" : `${plural(count)} selected`;
  }

  private dispatchSelect(): void {
    this.dispatchEvent(
      new CustomEvent<SelectEventDetail>(SELECT_EVENT, {
        bubbles: true,
        composed: true,
        detail: { selection: this.selection },
      }),
    );
  }

  private showSelection(): void {
    this.selectBoxes.forEach((box, row) => {
      const on = this.selected.has(row);
      box.checked = on;
      this.rowElements[row]?.classList.toggle("gt-i-selected", on);
    });
    this.updateSelectAll();
    this.updateInfo();
  }

  // The select-all checkbox is checked when every row that matches is selected, and mixed when
  // some are
  private updateSelectAll(): void {
    const box = this.selectAll;
    if (box === null) {
      return;
    }
    const count = this.order.filter((row) => this.selected.has(row)).length;
    box.checked = count > 0 && count === this.order.length;
    box.indeterminate = count > 0 && count < this.order.length;
    box.disabled = this.order.length === 0;
    box.setAttribute("aria-label", this.matched === null ? "Select all rows" : "Select all matching rows");
  }

  private addSortHeaders(table: HTMLTableElement, spec: Spec): void {
    const doc = this.ownerDocument;
    const cells = labelCells(table);

    for (const column of spec.columns) {
      if (column.id === null || column.header === null || !(column.id in spec.ranks)) {
        continue;
      }
      const th = cells.get(column.header);
      if (th === undefined) {
        continue;
      }
      const id = column.id;
      const label = labelText(th) || id;
      if (column.sortable === false) {
        this.unsortedLabels.set(id, label);
        continue;
      }
      const button = element(doc, "button", "gt-i-sort", { type: "button", "aria-label": `Sort by ${label}` });
      // (Both ways' arrows, the one it's sorted by darker)
      const icon = element(doc, "span", "gt-i-sort-icon", { "aria-hidden": "true" });
      const arrows = icon.appendChild(doc.createElementNS(SVG_NS, "svg"));
      arrows.setAttribute("viewBox", "0 0 12 16");
      for (const [way, d] of [["up", "M6 1.5 10.5 7h-9z"], ["down", "M6 14.5 1.5 9h9z"]]) {
        const path = arrows.appendChild(doc.createElementNS(SVG_NS, "path"));
        path.setAttribute("class", `gt-i-sort-${way}`);
        path.setAttribute("d", d as string);
      }
      button.append(icon);
      controlsRow(th).append(button);
      th.classList.add("gt-i-sortable");

      const sort = (event: MouseEvent) => this.userSort(toggleSort(this.sortKeys, id, this.shifted(event)));
      button.addEventListener("click", sort);
      // A click on the label sorts too (by the mouse: the button is the label's for the keyboard),
      // but not one on a link in it, on the controls, or ending a selection of its text
      th.addEventListener("click", (event) => {
        const target = event.target as Element;
        const selection = doc.getSelection();
        if (
          target.closest(`${INTERACTIVE}, .gt-i-head-controls, .gt-i-profile, .gt-i-resizer, .gt-i-resizer-start`) === null &&
          !(selection !== null && !selection.isCollapsed && th.contains(selection.anchorNode))
        ) {
          sort(event);
        }
      });
      // Shift-click would otherwise extend the page's text selection
      th.addEventListener("mousedown", (event) => {
        if (event.shiftKey) {
          event.preventDefault();
        }
      });
      this.sortHeaders.set(id, { th, icon, label });
    }
    // (A column only for querying is sorted by as an unsortable one is: from code, or the URL)
    for (const column of spec.query_columns ?? []) {
      this.unsortedLabels.set(column.id, column.label);
    }

    if (this.sortHeaders.size > 0) {
      this.addLiveRegion();
    }
  }

  // Once a column label has controls, every label in the bottom row of labels has their row (empty,
  // if it has none), so that the labels line up over it
  private alignLabels(table: HTMLTableElement): void {
    if (table.querySelector(":scope > thead .gt-i-head-controls") !== null) {
      bottomLabels(table).forEach(controlsRow);
    }
  }

  // A profile under each profiled column's label (see `profile.ts`), and an empty one under the
  // other labels in the bottom row, so that they line up. Profiles are hidden from assistive
  // technology, as they'd be part of the labels' names
  private addProfiles(table: HTMLTableElement, spec: Spec): void {
    const cells = labelCells(table);
    const doc = this.ownerDocument;
    const lang = this.closest("[lang]")?.getAttribute("lang") || undefined;
    for (const profileSpec of spec.profiles ?? []) {
      const index = spec.columns.findIndex((column) => column.id === profileSpec.column);
      const header = spec.columns[index]?.header;
      const th = header == null ? undefined : cells.get(header);
      const ranks = spec.ranks[profileSpec.column];
      if (th === undefined || ranks === undefined || th.querySelector(":scope > .gt-i-profile") !== null) {
        continue;
      }
      const profile = new Profile(profileSpec, ranks);
      const root = profileSlot(th);
      root.classList.add(`gt-i-profile-${profileSpec.plot}`);
      th.classList.add("gt-i-profiled");
      const svg = root.appendChild(doc.createElementNS(SVG_NS, "svg"));
      svg.setAttribute("viewBox", `0 0 ${Math.max(1, profile.bars.length)} 1`);
      svg.setAttribute("preserveAspectRatio", "none");
      const known = new Map<number, string>();
      const valueName = (rank: number) => {
        let name = known.get(rank);
        if (name === undefined) {
          const tr = this.rowElements[profile.rowOf[rank] ?? -1];
          const cell = tr === undefined ? undefined : this.dataCells(tr)[index];
          name = (cell === undefined ? "" : labelText(cell)) || "(empty)";
          known.set(rank, name);
        }
        return name;
      };
      const edge = edgeFormat(profile, lang);
      const view: ProfileView = { profile, rects: [], titles: [], names: [], caption: root, valueName };
      profile.bars.forEach((bar, i) => {
        const g = svg.appendChild(doc.createElementNS(SVG_NS, "g"));
        view.titles.push(g.appendChild(doc.createElementNS(SVG_NS, "title")));
        // (The column the bar is in, which shows its tooltip, then the bar)
        for (const hit of [true, false]) {
          const rect = g.appendChild(doc.createElementNS(SVG_NS, "rect"));
          rect.setAttribute("x", String(hit ? i : i + 0.1));
          rect.setAttribute("width", hit ? "1" : "0.8");
          rect.setAttribute("height", hit ? "1" : "0");
          if (hit) {
            rect.classList.add("gt-i-profile-hit");
          } else {
            rect.classList.toggle("gt-i-profile-other", bar.rank === -1 && profileSpec.plot === "top");
            view.rects.push(rect);
          }
        }
        view.names.push(
          bar.rank >= 0
            ? valueName(bar.rank)
            : profileSpec.plot === "top"
              ? `${profile.others} other values`
              : bar.low === bar.high
                ? edge(bar.low)
                : `${edge(bar.low)} – ${edge(bar.high)}`,
        );
      });
      view.caption = root.appendChild(element(doc, "div", "gt-i-profile-text"));
      this.profileViews.push(view);
    }
    if (this.profileViews.length > 0) {
      bottomLabels(table).forEach(profileSlot);
    }
  }

  // Count the profiles' rows again, if they're others than they last counted
  private updateProfiles(): void {
    if (this.profileViews.length === 0 || this.profiled === this.matched) {
      return;
    }
    this.profiled = this.matched;
    for (const { profile, rects, titles, names, caption, valueName } of this.profileViews) {
      const counts = profile.count(this.matched);
      const most = Math.max(1, ...counts.bars);
      counts.bars.forEach((count, i) => {
        // (A bar of a few rows is still seen)
        const height = count === 0 ? 0 : Math.max(count / most, 0.06);
        rects[i]?.setAttribute("y", String(1 - height));
        rects[i]?.setAttribute("height", String(height));
        (titles[i] as SVGTitleElement).textContent = `${names[i]}: ${plural(count)}`;
      });
      const parts: string[] = [];
      if (counts.distinct > 0) {
        parts.push(
          profile.spec.plot === "top"
            ? `${counts.distinct} ${counts.distinct === 1 ? "value" : "values"}`
            : counts.low === counts.high
              ? valueName(counts.low)
              : `${valueName(counts.low)} – ${valueName(counts.high)}`,
        );
      }
      if (counts.missing > 0) {
        parts.push(`${percent(counts.missing, counts.rows)} missing`);
      }
      caption.textContent = counts.rows === 0 ? "No rows" : parts.join(" · ");
      caption.title = caption.textContent;
    }
  }

  // A resize handle for each column with a label of its own (not one spanning several columns),
  // unless the spec says it can't be resized
  private addResizers(table: HTMLTableElement, spec: Spec): void {
    const rows = Array.from(
      table.querySelectorAll<HTMLTableRowElement>(":scope > thead > tr.gt_col_headings"),
    );
    // (The spec's columns come after the selection column and the row groups', if there are those)
    const lead = (spec.controls.selection === null ? 0 : 1) + (spec.stub.groups_as_column ? 1 : 0);
    // Lay the labels out on the columns: labels spanning rows (the stubhead, columns without a
    // spanner) take their columns in the rows below. Per column, the row its last label ends before
    const ends: number[] = [];
    rows.forEach((tr, r) => {
      let index = 0;
      for (const th of tr.children as HTMLCollectionOf<HTMLTableCellElement>) {
        while ((ends[index] ?? 0) > r) {
          index += 1;
        }
        const colspan = Number(th.getAttribute("colspan") ?? 1);
        const rowspan = Number(th.getAttribute("rowspan") ?? 1);
        for (let column = index; column < index + colspan; column++) {
          ends[column] = r + rowspan;
        }
        if (
          colspan === 1 &&
          r + rowspan >= rows.length &&
          !th.classList.contains("gt-i-select") &&
          spec.columns[index - lead]?.resizable !== false
        ) {
          this.addResizer(th, index);
        }
        index += colspan;
      }
    });
  }

  private addResizer(th: HTMLTableCellElement, index: number): void {
    const handle = this.ownerDocument.createElement("span");
    handle.className = "gt-i-resizer";
    handle.tabIndex = 0;
    // (The ARIA window splitter pattern)
    handle.setAttribute("role", "separator");
    handle.setAttribute("aria-orientation", "vertical");
    handle.setAttribute("aria-label", `Resize ${labelText(th) || `column ${index + 1}`}`);
    const resizer: Resizer = { handle, th, index };
    this.showWidth(resizer, th.getBoundingClientRect().width);
    th.classList.add("gt-i-resizable");
    th.append(handle);
    this.resizers.push(resizer);

    handle.addEventListener("pointerdown", (event) => this.dragWidth(resizer, handle, event));
    handle.addEventListener("keydown", (event) => {
      const step = (event.shiftKey ? RESIZE_STEP_LARGE : RESIZE_STEP) * (this.isRtl() ? -1 : 1);
      const steps: Record<string, number> = { ArrowRight: step, ArrowLeft: -step };
      const key = event.key;
      if (!(key in steps || key === "Home" || key === "Enter")) {
        return;
      }
      const width = this.columnWidth(resizer);
      if (width === null) {
        return;
      }
      event.preventDefault();
      if (key === "Enter") {
        this.userResetWidth(resizer);
        return;
      }
      // (Home is the narrowest)
      const next = this.setColumnWidth(resizer, key === "Home" ? 0 : width + (steps[key] ?? 0));
      this.placeGuide();
      if (next !== width) {
        this.dispatchResize(resizer, next);
      }
    });
    handle.addEventListener("dblclick", () => this.userResetWidth(resizer));
  }

  // Drag a column's edge, from a press on a handle along it (`grip`: the column's own, or the
  // one at the inline start of the label after it)
  private dragWidth(resizer: Resizer, grip: HTMLElement, event: PointerEvent): void {
    const start = event.button === 0 ? this.columnWidth(resizer) : null;
    if (start === null) {
      return;
    }
    // (No text selection, and no scrolling by touch)
    event.preventDefault();
    const x = event.clientX;
    const direction = this.isRtl() ? -1 : 1;
    let width = start;
    const move = (event: PointerEvent) => {
      width = this.setColumnWidth(resizer, start + (event.clientX - x) * direction);
      this.placeGuide();
    };
    const end = () => {
      grip.removeEventListener("pointermove", move);
      grip.removeEventListener("pointerup", end);
      grip.removeEventListener("pointercancel", end);
      grip.removeEventListener("lostpointercapture", end);
      this.removeAttribute("data-gti-resizing");
      resizer.handle.removeAttribute("data-gti-active");
      if (width !== start) {
        // (Short pages are padded to the new height of a full one)
        if (this.padStale()) {
          this.render();
        }
        this.placeGuide();
        this.dispatchResize(resizer, width);
      }
    };
    grip.setPointerCapture?.(event.pointerId);
    this.setAttribute("data-gti-resizing", "");
    resizer.handle.setAttribute("data-gti-active", "");
    grip.addEventListener("pointermove", move);
    grip.addEventListener("pointerup", end);
    grip.addEventListener("pointercancel", end);
    grip.addEventListener("lostpointercapture", end);
  }

  /**
   * Lines along the column whose label the mouse is over (in the label's cell, its row of controls
   * too), from the label to the end of the body, in the part in view: thicker along the label
   * where its edges can be dragged to resize a column (the label's own at its inline end, the one
   * before it at its inline start, by a handle there while the mouse is over the label). Not
   * while the table is stacked.
   */
  private addGuide(table: HTMLTableElement): void {
    const thead = table.tHead;
    if (thead === null || thead.querySelector("th.gt-i-head, th.gt-i-resizable") === null) {
      return;
    }
    const doc = this.ownerDocument;
    const guide = element(doc, "div", "gt-i-guide", { "aria-hidden": "true" });
    for (const side of ["left", "right"]) {
      guide.append(element(doc, "span", "gt-i-guide-line", { "data-gti-side": side }));
    }
    this.append(guide);
    this.guide = guide;
    // (By a mouse or a pen; and not while a column is dragged, by the handle that has the pointer)
    thead.addEventListener("pointerover", (event) => {
      if (event.pointerType !== "touch" && !this.hasAttribute("data-gti-resizing")) {
        const th = (event.target as Element).closest("th");
        this.showGuide(th?.matches(".gt-i-head, .gt-i-resizable") ? th : null);
      }
    });
    thead.addEventListener("pointerleave", (event) => {
      if (event.pointerType !== "touch" && !this.hasAttribute("data-gti-resizing")) {
        this.showGuide(null);
      }
    });
  }

  private showGuide(th: HTMLTableCellElement | null): void {
    if (th === this.guideTh) {
      return;
    }
    this.guideTh?.removeAttribute("data-gti-resize-start");
    this.guideTh = th;
    this.guideBefore = th === null ? null : this.resizerBefore(th);
    if (th !== null && this.guideBefore !== null) {
      this.startGrip(th);
      th.setAttribute("data-gti-resize-start", "");
    }
    this.placeGuide();
  }

  /**
   * The handle along the foot of the table's rows, dragged down or up: with pages whose size the
   * reader can change, along the foot of the page's rows (over the grand summary rows and the
   * footer), for a row more or fewer on a page for each row's height, from 1 to every row (not
   * while the table is stacked); for a body that scrolls within a height, along the foot of the
   * body, for a taller or shorter one, from a row's height to all of it. By the keys too (the
   * arrows for a row, Page Down and Up for ten, and Enter or a double click for the table's own).
   */
  private addFootHandle(spec: Spec): void {
    const { enabled, size_select, page_size } = spec.pagination;
    const rows = spec.layout.height === null;
    if (!this.movable || spec.controls.bar !== true || (rows && (!enabled || !size_select || spec.nrows === 0))) {
      return;
    }
    const doc = this.ownerDocument;
    // (The ARIA window splitter pattern)
    const handle = element(doc, "div", `gt-i-foot gt-i-${rows ? "rows" : "height"}`, {
      tabindex: "0",
      role: "separator",
      "aria-orientation": "horizontal",
      "aria-label": rows ? "Rows per page" : "Table height",
    });
    if (rows) {
      handle.setAttribute("aria-valuemin", "1");
      handle.setAttribute("aria-valuemax", String(spec.nrows));
      // (Saying the size, like a tooltip)
      handle.append(element(doc, "span", "gt-i-tip gt-i-rows-count", { "aria-hidden": "true" }));
      handle.style.fontFamily = getComputedStyle(this.table as HTMLTableElement).fontFamily;
    }
    this.placeBelow(handle);
    this.footHandle = handle;
    handle.addEventListener("pointerdown", (event) => this.dragFoot(handle, event));
    const reset = () => (rows ? this.userPageSize(page_size) : this.userHeight(null));
    handle.addEventListener("keydown", (event) => {
      const steps: Record<string, number> = { ArrowDown: 1, ArrowUp: -1, PageDown: 10, PageUp: -10 };
      const step = steps[event.key];
      if (event.key === "Enter") {
        reset();
      } else if (step === undefined) {
        return;
      } else if (rows) {
        const shown = this.rowsShown();
        const size = this.rowsWithin(shown + step);
        if (size !== shown) {
          this.userPageSize(size, "size");
        }
      } else {
        const height = this.portHeight();
        const next = this.heightWithin(height + step * this.oneRow());
        if (Math.abs(next - height) >= 1) {
          this.userHeight(next, "height");
        }
      }
      event.preventDefault();
    });
    handle.addEventListener("dblclick", reset);
  }

  // The number of rows a full page shows (all of them, on a page bigger than that)
  private rowsShown(): number {
    return Math.min(this.size ?? Infinity, (this.spec as Spec).nrows);
  }

  private rowsWithin(size: number): number {
    return Math.max(1, Math.min(size, (this.spec as Spec).nrows));
  }

  // The height of the container the body scrolls in
  private portHeight(): number {
    return (this.scroller as HTMLElement).getBoundingClientRect().height;
  }

  // A height for the body to scroll within (in whole px): from the column labels and the rows stuck
  // at the bottom, with a row between them, to all of it
  private heightWithin(height: number): number {
    const scroller = this.scroller as HTMLElement;
    const most = scroller.scrollHeight + scroller.offsetHeight - scroller.clientHeight;
    return Math.round(Math.min(most, Math.max(this.leastHeight(), height)));
  }

  private leastHeight(): number {
    const scroller = this.scroller as HTMLElement;
    const head = this.table?.tHead?.getBoundingClientRect().height ?? 0;
    return head + this.foot + this.oneRow() + scroller.offsetHeight - scroller.clientHeight;
  }

  // The height of a data row shown (the first)
  private oneRow(): number {
    for (const tr of (this.tbody as HTMLTableSectionElement).querySelectorAll<HTMLTableRowElement>(":scope > tr")) {
      if (!tr.hidden && typeof this.bodyRows.get(tr) === "number") {
        return tr.getBoundingClientRect().height || 24;
      }
    }
    return 24;
  }

  // Set the height the body scrolls within (`null` for the author's), as the reader has
  private userHeight(height: number | null, part: string | null = null): void {
    if (height !== this.heightValue) {
      this.heightValue = height;
      this.applyHeight();
      this.heightChanged();
      this.dispatchView(part);
    }
  }

  // Show the reset button for a height that's changed, and keep it
  private heightChanged(): void {
    this.updatePager();
    this.saveView();
  }

  // Show the body within the height it's set to, or the author's
  private applyHeight(): void {
    const height = this.spec?.layout.height ?? null;
    if (height !== null) {
      // (A kept height, no less than a row's)
      const laidOut = this.scroller !== null && this.scroller.getClientRects().length > 0;
      const value = this.heightValue === null ? height : `${laidOut ? Math.max(this.leastHeight(), this.heightValue) : this.heightValue}px`;
      this.style.setProperty("--gt-i-height", value);
      this.placeFoot();
    }
  }

  // Drag the foot of the rows: for pages, a row more or fewer for each data row's height (on
  // average, as the page started) it moves, the page keeping the row it starts with; for a body
  // that scrolls, its height, by as much as it moves
  private dragFoot(handle: HTMLElement, event: PointerEvent): void {
    if (event.button !== 0) {
      return;
    }
    // (No text selection, and no scrolling by touch)
    event.preventDefault();
    const scrolls = (this.spec as Spec).layout.height !== null;
    const before = scrolls ? this.heightValue : this.size;
    const start = scrolls ? this.portHeight() : this.rowsShown();
    const first = (this.page - 1) * (this.size ?? 0);
    const rows = this.view.end - this.view.start;
    const height = scrolls ? 1 : (rows > 0 ? this.dataRowsHeight() / rows : 0) || this.rowHeight || 24;
    const y = event.clientY;
    const move = (event: PointerEvent) => {
      const dy = event.clientY - y;
      if (scrolls) {
        this.heightValue = this.heightWithin(start + dy);
        this.applyHeight();
        return;
      }
      const size = this.rowsWithin(start + Math.round(dy / height));
      if (size !== this.size) {
        this.pageSizeValue = size;
        this.pageValue = Math.floor(first / size) + 1;
        this.render();
      }
    };
    const types = ["pointerup", "pointercancel", "lostpointercapture"];
    const end = () => {
      handle.removeEventListener("pointermove", move);
      for (const type of types) {
        handle.removeEventListener(type, end);
      }
      this.removeAttribute("data-gti-resizing");
      handle.removeAttribute("data-gti-active");
      if (scrolls ? this.heightValue !== before : this.size !== before) {
        if (scrolls) {
          this.heightChanged();
          this.dispatchView(null);
        } else {
          this.sizeChanged(null);
        }
      }
    };
    handle.setPointerCapture?.(event.pointerId);
    this.setAttribute("data-gti-resizing", "rows");
    handle.setAttribute("data-gti-active", "");
    handle.addEventListener("pointermove", move);
    for (const type of types) {
      handle.addEventListener(type, end);
    }
  }

  // The height of the data rows shown
  private dataRowsHeight(): number {
    let height = 0;
    for (const tr of (this.tbody as HTMLTableSectionElement).querySelectorAll<HTMLTableRowElement>(":scope > tr")) {
      if (!tr.hidden && typeof this.bodyRows.get(tr) === "number") {
        height += tr.getBoundingClientRect().height;
      }
    }
    return height;
  }

  // Place the handle along the foot of the rows, across the part of the table in view: for pages,
  // the page's rows (above the grand summary rows at the bottom), saying the page's size; for a
  // body that scrolls, the container it scrolls in
  private placeFoot(): void {
    const handle = this.footHandle;
    const table = this.table;
    const tbody = this.tbody;
    if (handle === null || table === null || tbody === null) {
      return;
    }
    const scroller = this.scroller;
    const scrolls = (this.spec as Spec).layout.height !== null;
    handle.hidden = (this.stacked && !scrolls) || table.getClientRects().length === 0;
    if (handle.hidden) {
      return;
    }
    const grand = this.grandBottom();
    let { left, right } = table.getBoundingClientRect();
    let y = grand !== null && !grand.hidden ? grand.getBoundingClientRect().top : tbody.getBoundingClientRect().bottom;
    if (scroller !== null) {
      const port = scroller.getBoundingClientRect();
      left = Math.max(left, port.left + scroller.clientLeft);
      right = Math.min(right, left + scroller.clientWidth);
      if (scrolls) {
        y = port.bottom;
      }
    }
    const outer = this.getBoundingClientRect();
    setStyle(handle, "top", `${y - outer.top - this.clientTop}px`);
    setStyle(handle, "left", `${left - outer.left - this.clientLeft}px`);
    setStyle(handle, "width", `${Math.max(0, right - left)}px`);
    if (scrolls) {
      handle.setAttribute("aria-valuenow", String(Math.round(this.portHeight())));
      return;
    }
    const shown = this.rowsShown();
    handle.setAttribute("aria-valuenow", String(shown));
    const text = `${plural(shown)} per page`;
    handle.setAttribute("aria-valuetext", text);
    (handle.firstElementChild as HTMLElement).textContent = text;
  }

  // The resizable column whose label ends where a label starts: the one before it (as the columns
  // are shown, moved and hidden), in the same row
  private resizerBefore(th: HTMLTableCellElement): Resizer | null {
    const rtl = this.isRtl();
    const box = th.getBoundingClientRect();
    const at = rtl ? box.right : box.left;
    return (
      this.resizers.find((resizer) => {
        const other = resizer.th === th ? null : resizer.th.getBoundingClientRect();
        return (
          other != null &&
          other.width > 0 &&
          Math.abs((rtl ? other.left : other.right) - at) < 1 &&
          other.top < box.bottom &&
          other.bottom > box.top
        );
      }) ?? null
    );
  }

  // The handle at a label's inline start, which drags the end of the column before it (by the
  // mouse only: that column's own handle is the one for the keyboard and touch)
  private startGrip(th: HTMLTableCellElement): void {
    if (th.querySelector(":scope > .gt-i-resizer-start") !== null) {
      return;
    }
    const grip = element(this.ownerDocument, "span", "gt-i-resizer-start", { "aria-hidden": "true" });
    grip.addEventListener("pointerdown", (event) => {
      if (this.guideTh === th && this.guideBefore !== null) {
        this.dragWidth(this.guideBefore, grip, event);
      }
    });
    grip.addEventListener("dblclick", () => {
      if (this.guideTh === th && this.guideBefore !== null) {
        this.userResetWidth(this.guideBefore);
      }
    });
    th.append(grip);
  }

  // Place the guide along its column, in the part of the table in view (past the pinned columns,
  // for one that scrolls under them), with its edges thick along the label where they're dragged
  private placeGuide(): void {
    const { guide, guideTh: th } = this;
    if (guide === null) {
      return;
    }
    const shown = th !== null && th.isConnected && !this.stacked && th.getClientRects().length > 0;
    guide.toggleAttribute("data-gti-shown", shown);
    if (!shown) {
      return;
    }
    const box = th.getBoundingClientRect();
    let [left, right, top, bottom] = [-Infinity, Infinity, -Infinity, Infinity];
    const scroller = this.scroller;
    if (scroller !== null) {
      const port = scroller.getBoundingClientRect();
      left = port.left + scroller.clientLeft;
      right = left + scroller.clientWidth;
      top = port.top + scroller.clientTop;
      bottom = top + scroller.clientHeight;
    }
    const rtl = this.isRtl();
    if (this.hasAttribute("data-gti-wide") && !th.classList.contains("gt-i-pinned")) {
      const edge = this.edgeCell?.isConnected ? this.edgeCell.getBoundingClientRect() : null;
      const endEdge = this.endEdge?.isConnected ? this.endEdge.getBoundingClientRect() : null;
      if (rtl) {
        right = Math.min(right, edge?.left ?? right);
        left = Math.max(left, endEdge?.right ?? left);
      } else {
        left = Math.max(left, edge?.right ?? left);
        right = Math.min(right, endEdge?.left ?? right);
      }
    }
    const x0 = Math.max(box.left, left);
    const x1 = Math.min(box.right, right);
    const y0 = Math.max(box.top, top);
    const y1 = Math.min(Math.max(box.bottom, this.tbody?.getBoundingClientRect().bottom ?? box.bottom), bottom);
    if (x1 - x0 < 1 || y1 - y0 < 1) {
      guide.removeAttribute("data-gti-shown");
      return;
    }
    const outer = this.getBoundingClientRect();
    setStyle(guide, "left", `${x0 - outer.left - this.clientLeft}px`);
    setStyle(guide, "top", `${y0 - outer.top - this.clientTop}px`);
    setStyle(guide, "width", `${x1 - x0}px`);
    setStyle(guide, "height", `${y1 - y0}px`);
    setStyle(guide, "--gt-i-guide-head", `${Math.max(0, box.bottom - y0)}px`);
    // (An edge out of view isn't drawn)
    const end = th.classList.contains("gt-i-resizable");
    const before = this.guideBefore !== null;
    const [leftLine, rightLine] = Array.from(guide.children) as HTMLElement[];
    for (const [line, at, grip] of [
      [leftLine, box.left >= left - 0.5, rtl ? end : before],
      [rightLine, box.right <= right + 0.5, rtl ? before : end],
    ] as const) {
      if (line !== undefined) {
        line.hidden = !at;
        line.toggleAttribute("data-gti-grip", grip);
      }
    }
  }

  private isRtl(): boolean {
    return getComputedStyle(this.table as HTMLTableElement).direction === "rtl";
  }

  private resizerCol(resizer: Resizer): HTMLElement | null {
    return (this.colgroup?.children[resizer.index] as HTMLElement | undefined) ?? null;
  }

  // A column's width, in px, once every column's width is fixed (`null` if they can't be)
  private columnWidth(resizer: Resizer): number | null {
    const col = this.freezeWidths() ? this.resizerCol(resizer) : null;
    return col === null ? null : parseFloat(col.style.width);
  }

  // A new width for a column, at least 2em of its label; returns the width it gets
  private setColumnWidth(resizer: Resizer, width: number): number {
    const col = this.resizerCol(resizer) as HTMLElement;
    const min = Math.ceil(2 * (parseFloat(getComputedStyle(resizer.th).fontSize) || 16));
    width = Math.max(min, Math.round(width));
    col.style.width = `${width}px`;
    this.showWidth(resizer, width);
    return width;
  }

  private showWidth(resizer: Resizer, width: number): void {
    const px = String(Math.round(width));
    resizer.handle.setAttribute("aria-valuenow", px);
    resizer.handle.setAttribute("aria-valuetext", `${px} pixels`);
  }

  // A double-click or Enter puts the column back to its width before any column was resized
  private userResetWidth(resizer: Resizer): void {
    const width = this.startWidths?.[resizer.index];
    const col = this.resizerCol(resizer);
    if (width === undefined || col === null || parseFloat(col.style.width) === width) {
      return;
    }
    col.style.width = `${width}px`;
    this.showWidth(resizer, width);
    this.placeGuide();
    this.dispatchResize(resizer, width);
  }

  private dispatchResize(resizer: Resizer, width: number): void {
    const place = resizer.index - this.lead;
    const column = (this.spec as Spec).columns[this.columnAt[place] ?? place];
    this.dispatchEvent(
      new CustomEvent<ResizeEventDetail>(RESIZE_EVENT, {
        bubbles: true,
        composed: true,
        detail: { column: column?.id ?? null, index: resizer.index, width },
      }),
    );
  }

  /**
   * Fix every column at the width it has (so that resizing one leaves the others where they
   * are), with the table's layout fixed and as wide as its columns. Returns whether they are.
   */
  private freezeWidths(): boolean {
    if (this.startWidths !== null) {
      return true;
    }
    const table = this.table as HTMLTableElement;
    const widths = this.shownWidths();
    if (widths === null) {
      return false;
    }
    let colgroup = this.colgroup ?? table.querySelector<HTMLTableColElement>(":scope > colgroup");
    if (colgroup === null) {
      colgroup = this.ownerDocument.createElement("colgroup");
      colgroup.className = "gt-i-widths";
      for (const _ of widths) {
        colgroup.append(this.ownerDocument.createElement("col"));
      }
    }
    const cols = Array.from(colgroup.children) as HTMLElement[];
    if (cols.length !== widths.length || cols.some((col) => col.tagName !== "COL" || col.hasAttribute("span"))) {
      return false;
    }
    // (Whole pixels, as the reader sets them; rounded up, so that no text is cut). A hidden column
    // has the width it had when it was hidden, if it was shown, or else the columns' average.
    const shown = widths.filter((_, c) => !this.hiddenGrid.has(c));
    const average = shown.reduce((sum, width) => sum + width, 0) / Math.max(1, shown.length);
    const whole = widths.map((width, c) =>
      Math.ceil((this.hiddenGrid.has(c) ? (this.hiddenWidths.get(c) ?? average) : width) - 0.01),
    );
    cols.forEach((col, i) => {
      col.style.width = `${whole[i]}px`;
    });
    if (!colgroup.isConnected) {
      table.insertBefore(colgroup, table.querySelector(":scope > thead, :scope > tbody"));
    }
    table.style.removeProperty("min-width");
    table.style.tableLayout = "fixed";
    // (A table with a fixed layout is as wide as its columns, or its width if that's wider; Firefox
    // stretches one `fit-content` wide to fill its container)
    table.style.width = "0";
    this.colgroup = colgroup;
    this.fittedCols = [];
    this.widthsFixed = true;
    this.startWidths = whole;
    this.hideCols();
    return true;
  }

  /**
   * The width of each column as shown, from a shown body row with a cell in every column, or else
   * from the column labels; `null` if a column has neither.
   */
  private shownWidths(): number[] | null {
    const trs = Array.from((this.tbody as HTMLTableSectionElement).querySelectorAll(":scope > tr"));
    const span = (cell: Element) => Number(cell.getAttribute("colspan") ?? 1);
    const columns = Math.max(0, ...trs.map((tr) => Array.from(tr.children).reduce((n, cell) => n + span(cell), 0)));
    const full = trs.find(
      (tr) =>
        !(tr as HTMLElement).hidden &&
        tr.children.length === columns &&
        Array.from(tr.children).every((cell) => span(cell) === 1),
    );
    const label = (i: number) => this.resizers.find((resizer) => resizer.index === i)?.th;
    // (A hidden column has none)
    const widths =
      full === undefined
        ? Array.from({ length: columns }, (_, i) => (this.hiddenGrid.has(i) ? 0 : label(i)?.getBoundingClientRect().width))
        : Array.from(full.children, (cell) => cell.getBoundingClientRect().width);
    return columns > 0 && widths.every((width) => width !== undefined) ? (widths as number[]) : null;
  }

  // The cells in the columns readers can hide (or the table can drop), and across them (from every
  // row, on hydration)
  private mapColumns(table: HTMLTableElement): void {
    const spec = this.spec as Spec;
    const grid = new Set([...this.hideable, ...this.drops].map((id) => this.gridOf(spec.columns.findIndex((column) => column.id === id))));
    const { placed, columns } = placeCells(Array.from(table.rows));
    this.gridColumns = columns;
    this.columnCells = placed.filter((p) => [...grid].some((c) => p.c0 <= c && c <= p.c1));
  }

  /**
   * Hide the columns `ids` (of those readers can hide), and show the others: their cells are
   * hidden, and the cells across them (spanners, headings, notes) span the columns shown, or are
   * hidden too, over only hidden ones. The rows are shown again by `render()`.
   */
  private hideColumns(ids: readonly string[]): void {
    const hidden = this.hideable.filter((id) => ids.includes(id));
    if (this.spec === null || JSON.stringify(hidden) === JSON.stringify(this.hiddenIds)) {
      return;
    }
    this.hiddenIds = hidden;
    // (A table that drops columns fits again, from all of them, with the rows showing them open
    // again if some still are)
    const open = [...this.opened];
    this.dropped = [];
    this.dropNeeds = [];
    this.showColumns();
    this.fit();
    if (this.dropped.length > 0) {
      open.forEach((tr) => this.expand(tr, true));
    }
  }

  // Show the columns but those hidden and dropped (see `hideColumns()`)
  private showColumns(): void {
    const spec = this.spec as Spec;
    const grid = new Set([...this.hiddenIds, ...this.dropped].map((id) => this.gridOf(spec.columns.findIndex((column) => column.id === id))));
    // (The width each column hidden has, which it has again if the widths are fixed while it's hidden)
    for (const c of grid) {
      const width = (p: Placed) => p.cell.getBoundingClientRect().width;
      const shown = this.hiddenGrid.has(c)
        ? undefined
        : this.columnCells.find((p) => p.c0 === c && p.c1 === c && width(p) > 0);
      if (shown !== undefined) {
        this.hiddenWidths.set(c, width(shown));
      }
    }
    this.hiddenGrid = grid;
    for (const { cell, c0, c1 } of this.columnCells) {
      let shown = 0;
      for (let c = c0; c <= c1; c++) {
        shown += grid.has(c) ? 0 : 1;
      }
      cell.hidden = shown === 0;
      if (c1 > c0 && shown > 0) {
        cell.colSpan = shown;
      }
    }
    this.hideCols();
    const empty = this.empty?.cells[0];
    if (empty !== undefined) {
      empty.colSpan = this.emptySpan();
    }
    // (Rows padding a page are made again, for the columns shown)
    this.removeFillers();
    this.fillers = [];
    this.fillerCells = null;
    // (An "auto" table showing fewer columns can be stacked, or one showing more not)
    if (this.syncStack()) {
      this.drawBorders();
    }
    this.syncExpanders();
    // The columns fitted to their contents are measured again, but not the reader's widths
    if (this.colgroup !== null && this.startWidths === null) {
      this.remeasure();
    }
    // (The bars follow the table's new width now, rather than as it's observed: a bar that wraps
    // then would resize the element as it's observed, which is a loop)
    this.alignBars();
  }

  // The `<col>`s of the columns hidden are hidden, so that the others are on the columns shown
  private hideCols(): void {
    const table = this.table;
    if (table === null || this.columnCells.length === 0) {
      return;
    }
    for (const colgroup of Array.from(table.querySelectorAll(":scope > colgroup"))) {
      if (colgroup.children.length === this.gridColumns) {
        Array.from(colgroup.children as HTMLCollectionOf<HTMLElement>).forEach((col, c) => {
          col.hidden = this.hiddenGrid.has(c);
        });
      }
    }
  }

  // The grid column of the spec's column `i`: after the `lead`, in its place
  private gridOf(i: number): number {
    return this.lead + (this.placeOf[i] ?? i);
  }

  // The runs' columns, by id
  private runIds(): string[][] {
    const spec = this.spec;
    return spec === null ? [] : this.runs.map((run) => run.map((i) => spec.columns[i]?.id as string));
  }

  // The runs' columns, by id, in the order shown
  private shownRuns(): string[][] {
    const spec = this.spec;
    return spec === null ? [] : this.runs.map((run) => run.map((i) => spec.columns[this.columnAt[i] as number]?.id as string));
  }

  // Whether the columns are in another order than the author's
  private reordered(): boolean {
    return this.columnAt.some((i, place) => i !== place);
  }

  // The runs of columns readers can move, and their cells in each row (from every row, with every
  // cell shown, on hydration): in a row, a run has a cell of its own in each of its columns, or none
  // (it's under a cell across the run, or one spanning the rows above)
  private mapRuns(table: HTMLTableElement): void {
    const spec = this.spec as Spec;
    this.runs = columnRuns(spec);
    this.runCells = [];
    if (this.runs.length === 0) {
      return;
    }
    this.columnAt = spec.columns.map((_, i) => i);
    this.placeOf = [...this.columnAt];
    const rows = Array.from(table.rows);
    const { grid, columns } = placeCells(rows);
    this.gridColumns = columns;
    const lead = this.lead;
    rows.forEach((tr, r) => {
      const line = grid[r] ?? [];
      this.runs.forEach((run, k) => {
        const own = run.map((i) => line[lead + i]).filter((p): p is Placed => p !== undefined && p.r0 === r && p.c0 === p.c1);
        if (own.length === run.length) {
          this.runCells.push({ run: k, cells: own.map((p) => p.cell) });
        }
      });
    });
  }

  /**
   * Put the columns readers can move in the order `ids` (each run's columns, in the order they're
   * shown in, as `orderRuns()` gives them): their cells in each row, and their `<col>`s, with the
   * width each has, and with them whatever goes by a column's place on the grid.
   */
  private orderColumns(ids: readonly string[]): void {
    const spec = this.spec;
    const table = this.table;
    if (spec === null || table === null || this.runs.length === 0 || JSON.stringify(ids) === JSON.stringify(this.columnOrder)) {
      return;
    }
    const index = new Map(spec.columns.map((column, i) => [column.id, i]));
    const columnAt = spec.columns.map((_, i) => i);
    let k = 0;
    for (const run of this.runs) {
      const first = run[0] as number;
      run.forEach((_, j) => {
        columnAt[first + j] = index.get(ids[k++] as string) ?? first + j;
      });
    }
    // Where each column that moves was on the grid, and is now
    const lead = this.lead;
    const moves = new Map<number, number>();
    columnAt.forEach((i, place) => {
      const was = this.placeOf[i] as number;
      if (was !== place) {
        moves.set(lead + was, lead + place);
      }
    });
    this.columnAt = columnAt;
    this.placeOf = columnAt.map((_, i) => columnAt.indexOf(i));

    // (A run's cells in a row are next to one another, in any order: they're put after the last)
    for (const { run, cells } of this.runCells) {
      const first = (this.runs[run] as number[])[0] as number;
      const shown = cells.map((_, j) => cells[(columnAt[first + j] as number) - first] as HTMLTableCellElement);
      let last = cells[0] as Element;
      while (last.nextElementSibling !== null && cells.includes(last.nextElementSibling as HTMLTableCellElement)) {
        last = last.nextElementSibling;
      }
      const after = last.nextSibling;
      for (const cell of shown) {
        last.parentNode?.insertBefore(cell, after);
      }
    }
    const moved = (c: number) => moves.get(c) ?? c;
    for (const colgroup of new Set([...Array.from(table.querySelectorAll(":scope > colgroup")), ...(this.colgroup === null ? [] : [this.colgroup])])) {
      const cols = Array.from(colgroup.children);
      if (cols.length === this.gridColumns) {
        const shown = [...cols];
        cols.forEach((col, c) => {
          shown[moved(c)] = col;
        });
        colgroup.append(...shown);
      }
    }
    for (const p of this.columnCells) {
      if (p.c0 === p.c1) {
        p.c0 = p.c1 = moved(p.c0);
      }
    }
    this.hiddenGrid = new Set(Array.from(this.hiddenGrid, moved));
    this.hiddenWidths = new Map(Array.from(this.hiddenWidths, ([c, width]) => [moved(c), width]));
    if (this.startWidths !== null) {
      const widths = [...this.startWidths];
      this.startWidths.forEach((width, c) => {
        widths[moved(c)] = width;
      });
      this.startWidths = widths;
    }
    for (const resizer of this.resizers) {
      resizer.index = moved(resizer.index);
    }
    // (Rows padding a page are made again, for the columns' places)
    this.removeFillers();
    this.fillers = [];
    this.fillerCells = null;
    if (this.responsive === "stack" || this.responsive === "auto") {
      this.orderChips();
    }
  }

  private addSearchBox(table: HTMLTableElement): void {
    const toolbar = this.ownerDocument.createElement("div");
    toolbar.className = "gt-i-toolbar";
    const input = this.searchInput();
    toolbar.append(input);

    input.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && input.value !== "") {
        // Clear the search (and don't, say, close a dialog the table is in)
        event.preventDefault();
        event.stopPropagation();
        this.clearSearch(input);
      }
    });

    // Outside the table's scrolling container, so that it stays in view
    this.prepend(toolbar);
    this.toolbar = toolbar;
    this.addLiveRegion();

    // In the table's font, lined up with the table (which GT may have centred or narrowed)
    toolbar.style.fontFamily = getComputedStyle(table).fontFamily;
    this.observeLayout();
  }

  // The search field, which searches once typing pauses, or at once on Enter (and, unless it's the
  // sheet's, the one a search set elsewhere shows in)
  private searchInput(own = true): HTMLInputElement {
    const input = this.ownerDocument.createElement("input");
    input.type = "search";
    input.className = "gt-i-search";
    input.placeholder = "Search";
    input.setAttribute("aria-label", "Search the table");
    input.setAttribute("enterkeyhint", "search");
    input.autocomplete = "off";
    input.spellcheck = false;
    input.value = this.searchValue;

    input.addEventListener("input", () => {
      this.cancelSearchTimer();
      this.searchTimer = setTimeout(() => {
        this.searchTimer = null;
        this.userSearch(input.value);
      }, SEARCH_DELAY_MS);
    });
    input.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        this.cancelSearchTimer();
        this.userSearch(input.value);
      }
    });
    if (own) {
      this.searchBox = input;
    }
    return input;
  }

  private clearSearch(input: HTMLInputElement): void {
    input.value = "";
    this.cancelSearchTimer();
    this.userSearch("");
  }

  /**
   * Add the control bar below the table: the search's button and field (with a search), and the
   * page arrows and readout (hidden until there are pages).
   */
  private addBar(): Bar {
    const doc = this.ownerDocument;
    const table = this.table as HTMLTableElement;
    const spec = this.spec as Spec;
    const root = doc.createElement("div");
    root.className = "gt-i-bar";
    // (The arrow keys go the way the arrows point, which a right-to-left table turns around)
    const rtl = getComputedStyle(table).direction === "rtl";
    const [back, ahead] = rtl ? ["→", "←"] : ["←", "→"];

    const pages = doc.createElement("nav");
    pages.className = "gt-i-bar-pages";
    pages.setAttribute("aria-label", "Table pages");
    pages.hidden = true;
    const first = this.barButton("first", "First page", "First page (Home)");
    const previous = this.barButton("previous", "Previous page", `Previous page (${back})`);
    const next = this.barButton("next", "Next page", `Next page (${ahead})`);
    const last = this.barButton("last", "Last page", "Last page (End)");
    const readout = doc.createElement("button");
    readout.type = "button";
    readout.className = "gt-i-readout";
    readout.dataset.gtiTip = "Go to a page";
    const jump = doc.createElement("label");
    jump.className = "gt-i-readout-jump";
    jump.hidden = true;
    const jumpInput = doc.createElement("input");
    jumpInput.type = "text";
    jumpInput.inputMode = "numeric";
    jumpInput.autocomplete = "off";
    jumpInput.setAttribute("enterkeyhint", "go");
    const jumpCount = doc.createElement("span");
    jump.append(jumpInput, jumpCount);
    // (Kept as wide as the readout at its widest, so the arrows stay put)
    const box = doc.createElement("span");
    box.className = "gt-i-readout-box";
    box.append(readout, jump);
    pages.append(first, previous, box, next, last);
    const info = this.makeInfo();
    const formats = spec.export?.formats ?? [];
    const exporter = formats.length > 0 ? this.makeExporter(formats) : null;

    const bar: Bar = {
      root,
      toggle: null,
      field: null,
      count: null,
      clear: null,
      keys: null,
      pages,
      first,
      previous,
      next,
      last,
      readout,
      jump,
      jumpInput,
      jumpCount,
      info,
      reset: null,
      exporter,
      columns: null,
      tokens: null,
      clearAll: null,
      query: null,
      undo: null,
      redo: null,
      sheet: null,
    };
    if (this.undoable) {
      const mac = onMac();
      bar.undo = this.barButton("undo", "Undo", `Undo (${mac ? "⌘Z" : "Ctrl+Z"})`);
      bar.redo = this.barButton("redo", "Redo", `Redo (${mac ? "⇧⌘Z" : "Ctrl+Y"})`);
      bar.undo.setAttribute("aria-keyshortcuts", "Control+Z Meta+Z");
      bar.redo.setAttribute("aria-keyshortcuts", "Control+Y Control+Shift+Z Meta+Shift+Z");
      bar.undo.addEventListener("click", () => this.userTravel(true));
      bar.redo.addEventListener("click", () => this.userTravel(false));
    }
    this.bar = bar;
    if (this.filters.length > 0) {
      this.addTokens(bar, rtl);
      this.addQuery(bar);
    }
    if (this.movable && spec.controls.search) {
      this.addBarSearch(bar);
    }
    // (After the search's button, which its field covers; or at the start)
    const keys = this.makeKeys(info);
    if (keys !== null) {
      bar.keys = keys;
      (bar.field?.parentElement ?? root).append(keys.button, keys.panel);
      // (So that a click in the table puts focus in it, for its keys)
      if (!this.hasAttribute("tabindex")) {
        this.tabIndex = -1;
        this.ownTabIndex = true;
      }
    }
    const columns = this.hideable.length > 0 || this.runs.length > 0 ? this.makeColumns() : null;
    bar.columns = columns;
    if (this.filters.length > 0 || columns !== null) {
      // (Shown, with its name, only in a folded bar: see gti.css)
      const sheet = this.barButton("filter", "Filter & sort", "Filter & sort");
      sheet.dataset.gtiBar = "sheet";
      this.setAttribute("data-gti-sheet", "");
      sheet.setAttribute("aria-haspopup", "dialog");
      const name = element(this.ownerDocument, "span", "gt-i-bar-name");
      name.textContent = "Filter & sort";
      sheet.append(name);
      sheet.addEventListener("click", () => this.openSheet(null, sheet));
      bar.sheet = sheet;
      root.append(sheet);
      this.addPress(table);
    }
    if (this.movable) {
      const reset = this.barButton("reset", "Reset the view", "Reset the view");
      // (Only its icon in a narrow bar: see gti.css)
      const name = element(doc, "span", "gt-i-bar-name");
      name.textContent = "Reset";
      reset.append(name);
      reset.hidden = true;
      reset.addEventListener("click", () => {
        // (Focus, on the button going, goes on to the next)
        const focused = reset.contains(doc.activeElement);
        this.userResetView();
        if (focused) {
          info.button.focus();
        }
      });
      bar.reset = reset;
    }
    // (A panel follows its button, so that Tab goes from one into the other)
    root.append(
      pages,
      ...(bar.query === null ? [] : [bar.query.toggle]),
      ...(columns === null ? [] : [columns.button, columns.panel]),
      ...(exporter === null ? [] : [exporter.button, exporter.panel]),
      ...(bar.undo === null || bar.redo === null ? [] : [bar.undo, bar.redo]),
      ...(bar.reset === null ? [] : [bar.reset]),
      info.button,
      info.panel,
    );

    first.addEventListener("click", () => {
      if (first.getAttribute("aria-disabled") !== "true") {
        this.userPage(1);
      }
    });
    last.addEventListener("click", () => {
      if (last.getAttribute("aria-disabled") !== "true") {
        this.userPage(this.pageCount);
      }
    });

    previous.addEventListener("click", () => {
      if (previous.getAttribute("aria-disabled") !== "true") {
        this.userPage(this.page - 1);
      }
    });
    next.addEventListener("click", () => {
      if (next.getAttribute("aria-disabled") !== "true") {
        this.userPage(this.page + 1);
      }
    });
    readout.addEventListener("click", () => this.startJump());
    jumpInput.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        // (And don't submit a form the table is in)
        event.preventDefault();
        this.endJump(true);
      } else if (event.key === "Escape") {
        event.preventDefault();
        event.stopPropagation();
        this.endJump(false);
      }
    });
    jumpInput.addEventListener("blur", () => this.endJump(true));

    // In the bar (but not while typing in it, or in a panel), the arrow keys and Page Up and Down go
    // to the page before or after, and Home and End to the first or last; Escape closes the panel
    root.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && this.popup !== null) {
        // (And don't, say, close a dialog the table is in)
        event.preventDefault();
        event.stopPropagation();
        this.closePanel(true);
        return;
      }
      if (
        pages.hidden ||
        event.altKey ||
        event.ctrlKey ||
        event.metaKey ||
        event.target instanceof HTMLInputElement ||
        this.popup?.panel.contains(event.target as Node) ||
        bar.tokens?.contains(event.target as Node) ||
        bar.query?.root.contains(event.target as Node)
      ) {
        return;
      }
      const page = this.page;
      const before = page - 1;
      const after = page + 1;
      const targets: Record<string, number> = {
        ArrowLeft: rtl ? after : before,
        ArrowRight: rtl ? before : after,
        PageUp: before,
        PageDown: after,
        Home: 1,
        End: this.pageCount,
      };
      const target = targets[event.key];
      if (target !== undefined) {
        event.preventDefault();
        this.userPage(target);
      }
    });

    this.addTips(root);
    // Below the table, outside its scrolling container, in the table's font
    this.placeBelow(root);
    root.style.fontFamily = getComputedStyle(table).fontFamily;
    this.addLiveRegion();
    this.observeLayout();
    this.alignBars();
    return bar;
  }

  private addBarSearch(bar: Bar): void {
    const doc = this.ownerDocument;
    const search = doc.createElement("div");
    search.className = "gt-i-bar-search";
    const toggle = this.barButton("search", "Search the table", "Search (/)");
    const field = doc.createElement("div");
    field.className = "gt-i-search-field";
    field.hidden = true;
    const input = this.searchInput();
    const count = doc.createElement("span");
    count.className = "gt-i-search-count";
    // (The live region says how many rows match)
    count.setAttribute("aria-hidden", "true");
    count.hidden = true;
    const clear = this.barButton("clear", "Close the search", "Close (Esc)");
    field.append(icon(doc, "search"), input, count, clear);
    search.append(toggle, field);
    bar.root.append(search);
    bar.toggle = toggle;
    bar.field = field;
    bar.count = count;
    bar.clear = clear;

    // The clear button clears the search, or closes the field when there's none
    const updateClear = () => {
      const close = input.value === "";
      clear.setAttribute("aria-label", close ? "Close the search" : "Clear the search");
      clear.dataset.gtiTip = close ? "Close (Esc)" : "Clear (Esc)";
    };
    toggle.addEventListener("click", () => this.openSearch(true));
    input.addEventListener("input", updateClear);
    input.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        // Clear the search, then close the field (and don't, say, close a dialog the table is in)
        event.preventDefault();
        event.stopPropagation();
        if (input.value === "") {
          this.closeSearch(true);
        } else {
          this.clearSearch(input);
          updateClear();
        }
      }
    });
    clear.addEventListener("click", () => {
      if (input.value === "") {
        this.closeSearch(true);
      } else {
        this.clearSearch(input);
        updateClear();
        input.focus();
      }
    });
    // An empty field closes when focus leaves it
    field.addEventListener("focusout", (event) => {
      if (!field.contains(event.relatedTarget as Node | null)) {
        this.closeSearch(false);
      }
    });

    // `/` opens the search, from anywhere in the table that isn't for typing
    this.slashKey = (event: KeyboardEvent) => {
      const target = event.target as Element;
      if (
        event.key !== "/" ||
        event.altKey ||
        event.ctrlKey ||
        event.metaKey ||
        event.defaultPrevented ||
        target.closest(TYPED) !== null
      ) {
        return;
      }
      event.preventDefault();
      this.openSearch(true);
    };
    this.addEventListener("keydown", this.slashKey);

    // (A search set before hydration shows in it)
    if (this.searchValue !== "") {
      this.openSearch(false);
    }
    updateClear();
  }

  private barButton(name: keyof typeof ICONS, label: string, title: string): HTMLButtonElement {
    const button = this.ownerDocument.createElement("button");
    button.type = "button";
    button.className = "gt-i-bar-button";
    button.dataset.gtiBar = name;
    button.setAttribute("aria-label", label);
    button.dataset.gtiTip = title;
    button.append(icon(this.ownerDocument, name));
    return button;
  }

  /**
   * The bar's tooltips: what a button (with `data-gti-tip`) does, and its key, over it (or under,
   * without room above), a moment after the mouse goes onto it (at once, just after another),
   * or when it's focused from the keyboard; described by it while it's shown
   */
  private addTips(root: HTMLElement): void {
    const doc = this.ownerDocument;
    const tip = element(doc, "div", "gt-i-tip", { role: "tooltip", id: `gt-i-tip-${++infoCount}` });
    tip.hidden = true;
    root.append(tip);
    let shown: HTMLElement | null = null;
    let next: HTMLElement | null = null;
    let timer: ReturnType<typeof setTimeout> | undefined;
    let left = 0;
    // (Escape hides it, wherever focus is)
    const escape = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        hide();
      }
    };
    const hide = () => {
      clearTimeout(timer);
      next = null;
      doc.removeEventListener("keydown", escape, true);
      if (shown !== null) {
        shown.removeAttribute("aria-describedby");
        shown = null;
        tip.hidden = true;
        left = Date.now();
      }
    };
    const show = (target: HTMLElement) => {
      hide();
      // (Not over its open panel)
      if (!target.isConnected || target.getAttribute("aria-expanded") === "true") {
        return;
      }
      shown = target;
      target.setAttribute("aria-describedby", tip.id);
      tip.textContent = target.dataset.gtiTip as string;
      tip.hidden = false;
      doc.addEventListener("keydown", escape, true);
      const bar = root.getBoundingClientRect();
      const box = target.getBoundingClientRect();
      const { width, height } = tip.getBoundingClientRect();
      const top = box.top - height - TIP_GAP;
      tip.style.left = `${Math.max(Math.min(box.left + (box.width - width) / 2, bar.right - width), bar.left) - bar.left}px`;
      tip.style.top = `${(top < 0 ? box.bottom + TIP_GAP : top) - bar.top}px`;
    };
    const target = (event: Event) => (event.target as Element).closest<HTMLElement>("[data-gti-tip]");
    root.addEventListener("pointerover", (event) => {
      const el = target(event);
      if (el === null || el === shown || el === next || event.pointerType === "touch") {
        return;
      }
      if (shown !== null || Date.now() - left < TIP_DELAY_MS) {
        show(el);
      } else {
        clearTimeout(timer);
        next = el;
        timer = setTimeout(() => show(el), TIP_DELAY_MS);
      }
    });
    root.addEventListener("pointerout", (event) => {
      const el = target(event);
      if (el !== null && !el.contains(event.relatedTarget as Node | null)) {
        hide();
      }
    });
    root.addEventListener("focusin", (event) => {
      const el = target(event);
      if (el?.matches(":focus-visible")) {
        show(el);
      }
    });
    // (And on a click from the keyboard, which may open a panel over it)
    for (const type of ["focusout", "pointerdown", "click"]) {
      root.addEventListener(type, hide);
    }
  }

  /** Make a panel, and the bar's button that opens it (a disclosure). */
  private makePanel(name: keyof typeof ICONS, label: string, title: string): Popup {
    const button = this.barButton(name, label, title);
    const panel = element(this.ownerDocument, "div", "gt-i-info", {
      id: `gt-i-info-${++infoCount}`,
      role: "group",
      "aria-label": title,
    });
    panel.hidden = true;
    button.setAttribute("aria-expanded", "false");
    button.setAttribute("aria-controls", panel.id);
    const popup = { button, panel };
    button.addEventListener("click", () => {
      if (panel.hidden) {
        this.openPanel(popup);
      } else {
        this.closePanel(false);
      }
    });
    // The panel closes when focus goes elsewhere (but not when the window loses it, nor to what
    // it's in, as a press in it that focuses nothing in it sends it: a press outside it closes it)
    const leave = (event: FocusEvent) => {
      const to = event.relatedTarget as Node | null;
      if (to !== null && to !== button && !panel.contains(to) && !to.contains(panel)) {
        this.closePanel(false, popup);
      }
    };
    button.addEventListener("focusout", leave);
    panel.addEventListener("focusout", leave);
    return popup;
  }

  /**
   * Open the "Filter & sort" sheet, a modal dialog at the foot of the window: for the table (`id`
   * `null`), with the search, the sort, the filters and the columns panel's items; or for a column
   * (from a long press on its label), with its sort and filter, and a button hiding it. Focus goes
   * back to `button` when it closes.
   */
  private openSheet(id: string | null, button: HTMLButtonElement): void {
    const bar = this.bar;
    if (bar === null) {
      return;
    }
    this.closePanel(false);
    this.closeFilter(false);
    const doc = this.ownerDocument;
    const dialog = this.sheet ?? this.makeSheet();
    const header = id === null ? undefined : this.sortHeaders.get(id);
    const controls = id === null ? this.filters : this.filters.filter((control) => control.filter.spec.column === id);
    const title = id === null ? "Filter & sort" : (header?.label ?? controls[0]?.label ?? id);
    // What brings it up to date, as the view changes; and what puts back what it took
    const syncs: (() => void)[] = [];
    const undos: (() => void)[] = [];
    const action = (text: string, act: () => void) => {
      const el = element(doc, "button", "gt-i-info-button", { type: "button" });
      el.textContent = text;
      // (Disabled with ARIA, so that it keeps focus)
      el.addEventListener("click", () => {
        if (el.getAttribute("aria-disabled") !== "true") {
          act();
        }
      });
      return el;
    };

    const body = element(doc, "div", "gt-i-sheet-body");
    const head = element(doc, "div", "gt-i-filter-head");
    const name = element(doc, "span", "gt-i-filter-title");
    name.textContent = title;
    head.append(name, action("Done", () => this.closePanel(true)));
    const rows = element(doc, "p", "gt-i-info-rows");
    syncs.push(() => (rows.textContent = this.rowsText()));
    body.append(head, rows);
    const section = (text: string) => {
      const heading = element(doc, "p", "gt-i-info-heading", { id: `gt-i-sheet-${++infoCount}` });
      heading.textContent = text;
      const el = element(doc, "div", "gt-i-sheet-section", { role: "group", "aria-labelledby": heading.id });
      el.append(heading);
      body.append(el);
      return el;
    };

    // The bar's search (whose field shows the search once the sheet closes)
    if (id === null && bar.field !== null) {
      const input = this.searchInput(false);
      input.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
          // (Which would clear it, not close the sheet)
          event.preventDefault();
          this.closePanel(true);
        }
      });
      section("Search").append(input);
      syncs.push(() => {
        if (doc.activeElement !== input) {
          input.value = this.searchValue;
        }
      });
      undos.push(() => {
        // (A search waiting on the typing to pause)
        if (this.searchTimer !== null) {
          this.cancelSearchTimer();
          this.userSearch(input.value);
        }
      });
    }

    // The sort: for the table, by a column (the first it's sorted by), then either way; for a column,
    // either way. The way it's sorted is pressed, and pressing it again unsorts it
    if (id === null ? this.sortHeaders.size > 0 : header !== undefined) {
      const part = section("Sort");
      let select: HTMLSelectElement | null = null;
      if (id === null) {
        const choice = element(doc, "select", "", { "aria-label": "Sort by" });
        select = choice;
        for (const [key, label] of [["", "Not sorted"], ...Array.from(this.sortHeaders, ([key, { label }]) => [key, label])]) {
          const option = doc.createElement("option");
          option.value = key as string;
          option.textContent = label as string;
          choice.append(option);
        }
        choice.addEventListener("change", () => this.userSort(choice.value === "" ? [] : [{ column: choice.value, descending: false }]));
        part.append(choice);
        syncs.push(() => {
          const first = this.sortKeys[0]?.column;
          choice.value = first !== undefined && this.sortHeaders.has(first) ? first : "";
        });
      }
      const column = () => id ?? (select?.value || null);
      const ways = element(doc, "div", "gt-i-sheet-ways");
      for (const [text, descending] of [["Ascending", false], ["Descending", true]] as const) {
        const way = action(text, () => {
          const at = column() as string;
          this.userSort(way.getAttribute("aria-pressed") === "true" ? this.sortKeys.filter((key) => key.column !== at) : [{ column: at, descending }]);
        });
        ways.append(way);
        syncs.push(() => {
          const at = column();
          const key = this.sortKeys.find((key) => key.column === at);
          way.setAttribute("aria-pressed", String(key?.descending === descending));
          way.setAttribute("aria-disabled", String(at === null));
        });
      }
      part.append(ways);
    }

    // The filters: a button for each, saying what it keeps, which opens its panel below it; and for
    // the table, the filters as text
    if (controls.length > 0) {
      const part = section(id === null ? "Filters" : "Filter");
      for (const control of controls) {
        const open = element(doc, "button", "gt-i-info-button gt-i-sheet-filter", { type: "button", "aria-expanded": "false" });
        open.addEventListener("click", () => {
          if (this.openFilter === control && this.filterAnchor === open) {
            this.closeFilter(false);
          } else {
            this.openFilterPanel(control, open);
            open.setAttribute("aria-controls", control.panel?.id ?? "");
          }
        });
        open.addEventListener("focusout", (event) => this.leaveFilter(control, event));
        part.append(open);
        syncs.push(() => {
          open.textContent = this.tokenText(control);
          open.toggleAttribute("data-gti-on", control.filter.active);
        });
      }
      const query = bar.query;
      if (id === null && query !== null) {
        part.append(
          action("Filters as text", () => {
            this.closePanel(false);
            this.openQuery();
          }),
        );
      }
      undos.push(() => {
        for (const control of controls) {
          if (control.panel !== null && body.contains(control.panel)) {
            this.append(control.panel);
          }
        }
      });
    }

    // The columns panel's items, for the table; a button hiding the column, for one
    const columns = bar.columns;
    if (id === null && columns !== null) {
      const items = Array.from(columns.panel.children);
      section("Columns").append(...items);
      undos.push(() => columns.panel.append(...items));
    } else if (id !== null && columns !== null && this.hideable.includes(id)) {
      const hide = action("Hide column", () => {
        this.closePanel(false);
        this.userColumns([...this.hiddenIds, id], `${title} hidden`);
        // (Its label, which focus would go back to, is hidden)
        bar.info.button.focus({ preventScroll: true });
      });
      section("Column").append(hide);
      syncs.push(() => hide.setAttribute("aria-disabled", String(columns.items.get(id)?.box?.disabled === true)));
    }

    // (The live region, outside the modal sheet, would be inert)
    const live = this.live;
    if (live !== null) {
      body.append(live);
      undos.push(() => {
        if (live.parentNode === body) {
          this.append(live);
        }
      });
    }
    dialog.setAttribute("aria-label", title);
    dialog.replaceChildren(body);
    this.sheetSync = () => syncs.forEach((sync) => sync());
    this.sheetDone = () => {
      undos.forEach((undo) => undo());
      this.showSearch();
    };
    this.openPanel({ button, panel: dialog });
  }

  // The sheet, which closes on Escape, or a press on its backdrop (one that began there)
  private makeSheet(): HTMLDialogElement {
    const dialog = element(this.ownerDocument, "dialog", "gt-i-sheet");
    let down = false;
    dialog.addEventListener("pointerdown", (event) => (down = event.target === dialog));
    dialog.addEventListener("click", (event) => {
      if (down && event.target === dialog) {
        this.closePanel(true);
      }
      down = false;
    });
    dialog.addEventListener("close", () => {
      if (this.popup?.panel === dialog) {
        this.closePanel(true);
      }
    });
    this.append(dialog);
    this.sheet = dialog;
    return dialog;
  }

  // On a touch screen, a long press on a column's label opens the column's sheet; the click the
  // press ends with doesn't sort by it
  private addPress(table: HTMLTableElement): void {
    const thead = table.tHead;
    if (thead === null) {
      return;
    }
    let timer: ReturnType<typeof setTimeout> | null = null;
    let open: (() => void) | null = null;
    let x = 0;
    let y = 0;
    const cancel = () => {
      if (timer !== null) {
        clearTimeout(timer);
      }
      timer = open = null;
    };
    thead.addEventListener("pointerdown", (event) => {
      cancel();
      this.pressed = false;
      const target = event.target as Element;
      const th = target.closest("th");
      if (event.pointerType === "mouse" || th === null || target.closest(".gt-i-resizer") !== null) {
        return;
      }
      const id =
        Array.from(this.sortHeaders).find(([, header]) => header.th === th)?.[0] ??
        this.filters.find((control) => control.th === th)?.filter.spec.column;
      const anchor = target.closest("button") ?? th.querySelector("button");
      if (id === undefined || anchor === null) {
        return;
      }
      x = event.clientX;
      y = event.clientY;
      open = () => {
        cancel();
        this.pressed = true;
        this.openSheet(id, anchor);
      };
      timer = setTimeout(open, PRESS_MS);
    });
    thead.addEventListener("pointermove", (event) => {
      if (Math.hypot(event.clientX - x, event.clientY - y) > PRESS_SLOP) {
        cancel();
      }
    });
    thead.addEventListener("pointerup", cancel);
    thead.addEventListener("pointercancel", cancel);
    // (Android's long press is a context menu, which the sheet is instead)
    thead.addEventListener("contextmenu", (event) => {
      if (open !== null || this.pressed) {
        event.preventDefault();
        open?.();
      }
    });
    thead.addEventListener(
      "click",
      (event) => {
        if (this.pressed) {
          this.pressed = false;
          event.preventDefault();
          event.stopPropagation();
        }
      },
      true,
    );
  }

  /** Make the info panel, and the bar's button that opens it. */
  private makeInfo(): Info {
    const doc = this.ownerDocument;
    const spec = this.spec as Spec;
    const popup = this.makePanel("info", "Table info", "Table info");
    const panel = popup.panel;
    const rows = element(doc, "p", "gt-i-info-rows");
    panel.append(rows);
    const info: Info = {
      ...popup,
      rows,
      size: null,
      select: null,
      sortText: null,
      filtersText: null,
      selection: null,
      selectionText: null,
      selectionClear: null,
      columnsText: null,
      view: null,
      detailsOpen: null,
      detailsClose: null,
    };

    // An item: what it's about, then the control that changes it (if there's one)
    const item = (name: string, tag: "div" | "label", text: HTMLElement, control?: HTMLElement) => {
      const el = doc.createElement(tag);
      el.className = "gt-i-info-item";
      el.dataset.gtiInfo = name;
      el.append(text, ...(control === undefined ? [] : [control]));
      panel.append(el);
      return el;
    };
    const span = (text = "") => {
      const el = doc.createElement("span");
      el.textContent = text;
      return el;
    };

    if (spec.pagination.size_select) {
      const select = doc.createElement("select");
      select.addEventListener("change", () => this.userPageSize(Number(select.value)));
      info.size = item("size", "label", span("Rows per page"), select);
      info.select = select;
    }
    if (this.sortHeaders.size > 0) {
      info.sortText = span();
      item("sort", "div", info.sortText);
    }
    if (this.filters.length > 0) {
      info.filtersText = span();
      item("filters", "div", info.filtersText);
    }
    if (spec.controls.selection !== null) {
      const clear = doc.createElement("button");
      clear.type = "button";
      clear.className = "gt-i-info-button";
      clear.textContent = "Clear";
      clear.setAttribute("aria-label", "Clear the selection");
      // (Disabled with ARIA, so that it keeps focus once it has done what it does)
      clear.addEventListener("click", () => {
        if (clear.getAttribute("aria-disabled") !== "true") {
          this.userClearSelection();
        }
      });
      info.selectionText = span();
      info.selectionClear = clear;
      info.selection = item("selection", "div", info.selectionText, clear);
    }
    if (this.hideable.length > 0) {
      info.columnsText = span();
      item("columns", "div", info.columnsText);
    }
    if (this.contents.size > 0) {
      // (Disabled with ARIA, as the selection's button is)
      const button = (text: string, label: string, open: boolean) => {
        const el = element(doc, "button", "gt-i-info-button", { type: "button", "aria-label": label });
        el.textContent = text;
        el.addEventListener("click", () => {
          if (el.getAttribute("aria-disabled") !== "true") {
            this.expandAll(open);
          }
        });
        return el;
      };
      info.detailsOpen = button("Expand all", "Show every row's details", true);
      info.detailsClose = button("Collapse all", "Hide every row's details", false);
      const buttons = element(doc, "span", "gt-i-info-buttons");
      buttons.append(info.detailsOpen, info.detailsClose);
      item("details", "div", span("Row details"), buttons);
    }
    const kept = this.keeper;
    if (kept !== null) {
      const where = kept.url ? (kept.storage ? "the link and this browser" : "the link") : "this browser";
      info.view = item("view", "div", span(`View kept in ${where}`));
    }
    return info;
  }

  /**
   * Make the keyboard shortcuts' panel, and the bar's button that opens it: the keys the table
   * answers to (with focus in it), and the clicks with Shift. `null` if there are none.
   */
  private makeKeys(info: Info): Keys | null {
    const doc = this.ownerDocument;
    const spec = this.spec as Spec;
    const keys = doc.createElement("dl");
    keys.className = "gt-i-info-keys";
    const key = (names: string[], text: string, click = false) => {
      const entry = doc.createElement("div");
      const dt = doc.createElement("dt");
      names.forEach((name, i) => {
        const kbd = doc.createElement("kbd");
        kbd.textContent = name;
        dt.append(...(i > 0 ? [" "] : []), kbd);
      });
      if (click) {
        dt.append(" + click");
      }
      const dd = doc.createElement("dd");
      dd.textContent = text;
      entry.append(dt, dd);
      keys.append(entry);
      return entry;
    };
    if (this.movable && spec.controls.search) {
      key(["/"], "Search");
      key(["Esc"], "Clear the search, then close it");
    }
    const pageKeys = spec.pagination.enabled
      ? [key(["←", "→"], "Previous or next page, in the bar"), key(["Home", "End"], "First or last page, in the bar")]
      : [];
    if (this.sortHeaders.size > 0) {
      key(["Shift"], "Sort by more than one column", true);
    }
    if (spec.controls.selection === "multiple") {
      key(["Shift"], "Select a range of rows", true);
    }
    if (this.runs.length > 0) {
      key([onMac() ? "⌥" : "Alt", "↑", "↓"], "Move a column, in the Columns panel");
    }
    if (this.undoable) {
      const mac = onMac();
      key(mac ? ["⌘", "Z"] : ["Ctrl", "Z"], "Undo a change to the view");
      key(mac ? ["⇧", "⌘", "Z"] : ["Ctrl", "Y"], "Redo it");
    }
    if (keys.childElementCount === 0) {
      return null;
    }
    const popup = this.makePanel("keys", "Keyboard shortcuts", "Keyboard shortcuts");
    const heading = element(doc, "p", "gt-i-info-heading");
    heading.textContent = "Keyboard shortcuts";
    const note = element(doc, "p", "gt-i-export-note");
    note.textContent = "With the table clicked, or focus in it";
    // (Opening from the bar's start)
    popup.panel.setAttribute("data-gti-start", "");
    popup.panel.append(heading, keys, note);
    // In a narrow bar, without room for its button, it's opened from the info panel's (see gti.css)
    const open = element(doc, "button", "gt-i-info-button", { type: "button", "data-gti-info": "keys" });
    open.textContent = "Keyboard shortcuts";
    open.addEventListener("click", () => {
      this.openPanel({ ...popup, button: info.button });
      info.button.focus();
    });
    info.panel.append(open);
    // (The popup its button opens, which `closePanel()` knows it by)
    return Object.assign(popup, { pageKeys, open });
  }

  private openPanel(popup: Popup): void {
    if (this.popup === popup) {
      return;
    }
    this.closePanel(false);
    this.closeFilter(false);
    this.updateInfo();
    const { button, panel } = popup;
    // (Over the table, so filled with what's behind it)
    panel.style.backgroundColor = backdropColor(this);
    if (panel === this.sheet) {
      // (A modal dialog, in the window's top layer: in the table's font, and closed by itself)
      panel.style.fontFamily = getComputedStyle(this.table as HTMLTableElement).fontFamily;
      this.popup = popup;
      this.sheet.showModal();
      return;
    }
    panel.hidden = false;
    button.setAttribute("aria-expanded", "true");
    this.popup = popup;
    this.placePanel(panel);
    // A press anywhere else closes it
    this.outsidePress = (event: PointerEvent) => {
      const path = event.composedPath();
      if (!path.includes(panel) && !path.includes(button)) {
        this.closePanel(false);
      }
    };
    this.ownerDocument.addEventListener("pointerdown", this.outsidePress);
  }

  // Above the bar, or below it if there's more room in the view there than above, for a panel
  // that doesn't fit above; no taller than the room it has
  private placePanel(panel: HTMLElement): void {
    panel.removeAttribute("data-gti-below");
    panel.style.maxHeight = "";
    const bar = (this.bar as Bar).root.getBoundingClientRect();
    const gap = 8;
    const above = bar.top - gap;
    const below = this.ownerDocument.documentElement.clientHeight - bar.bottom - gap;
    const height = panel.getBoundingClientRect().height;
    const down = height > above && below > above;
    panel.toggleAttribute("data-gti-below", down);
    const room = down ? below : above;
    if (height > room) {
      panel.style.maxHeight = `${Math.max(room, 160)}px`;
    }
  }

  // Close the open panel (if it's `popup`)
  private closePanel(focus: boolean, popup = this.popup): void {
    if (popup === null || popup !== this.popup) {
      return;
    }
    this.popup = null;
    if (this.outsidePress !== null) {
      this.ownerDocument.removeEventListener("pointerdown", this.outsidePress);
      this.outsidePress = null;
    }
    if (popup.panel === this.sheet) {
      // (The sheet's filter panel closes with it, and what it took goes back)
      this.closeFilter(false);
      this.sheetDone?.();
      this.sheetSync = this.sheetDone = null;
      this.sheet.close();
    } else {
      popup.panel.hidden = true;
      popup.button.setAttribute("aria-expanded", "false");
    }
    if (focus) {
      popup.button.focus();
    }
  }

  private updateInfo(): void {
    const bar = this.bar;
    if (bar === null) {
      return;
    }
    const info = bar.info;
    const size = this.size;
    info.rows.textContent = this.rowsText();
    info.rows.hidden = !(this.spec as Spec).pagination.info;

    if (info.size !== null && info.select !== null) {
      info.size.hidden = !this.pagesOffered();
      if (size !== null) {
        const choices = this.sizeChoices(size).map(String);
        if (Array.from(info.select.options, (option) => option.value).join() !== choices.join()) {
          info.select.replaceChildren(
            ...choices.map((choice) => {
              const option = this.ownerDocument.createElement("option");
              option.value = option.textContent = choice;
              return option;
            }),
          );
        }
        info.select.value = String(size);
      }
    }
    if (info.sortText !== null) {
      info.sortText.textContent = this.sortText();
    }
    if (info.filtersText !== null) {
      info.filtersText.textContent = this.filtersText();
    }
    if (info.selectionText !== null && info.selectionClear !== null) {
      info.selectionText.textContent = this.selectionText();
      info.selectionClear.setAttribute("aria-disabled", String(this.selected.size === 0));
    }
    if (info.columnsText !== null) {
      const n = this.hiddenIds.length;
      info.columnsText.textContent = n === 0 ? "No columns hidden" : `${n} ${n === 1 ? "column" : "columns"} hidden`;
    }
    if (info.detailsOpen !== null && info.detailsClose !== null) {
      const all = [...this.contents.keys()].every((tr) => this.opened.has(tr));
      info.detailsOpen.setAttribute("aria-disabled", String(all));
      info.detailsClose.setAttribute("aria-disabled", String(this.opened.size === 0));
    }
    if (bar.exporter !== null) {
      this.updateExporter(bar.exporter);
    }
    if (bar.columns !== null) {
      this.updateColumns(bar.columns);
    }
    this.sheetSync?.();
  }

  /**
   * Make the columns panel, and the bar's button that opens it: an item per column readers can hide
   * or move, in the order shown, with a checkbox for one they can hide, and for one they can move, a
   * handle to drag it by and buttons moving it (as Alt+↑ and Alt+↓ do).
   */
  private makeColumns(): Columns {
    const doc = this.ownerDocument;
    const spec = this.spec as Spec;
    const hideable = this.hideable;
    const movable = this.reorderableColumns;
    const label =
      movable.length === 0 ? "Show or hide columns" : hideable.length === 0 ? "Reorder columns" : "Show, hide or reorder columns";
    const popup = this.makePanel("columns", label, "Columns");
    popup.panel.classList.add("gt-i-columns");
    const labels = labelCells(this.table as HTMLTableElement);
    const list = element(doc, "div", "gt-i-filter-options");
    const columns: Columns = { ...popup, list, items: new Map(), all: null, order: null };
    const alt = onMac() ? "⌥" : "Alt+";
    for (const { id } of spec.columns) {
      if (id === null || !(hideable.includes(id) || movable.includes(id))) {
        continue;
      }
      const title = this.columnTitle(id, labels);
      const root = element(doc, "div", "gt-i-column", { "data-gti-column": id });
      const item: ColumnItem = { root, box: null, earlier: null, later: null };
      const name = element(doc, "span", "gt-i-filter-value");
      name.textContent = title;
      if (hideable.includes(id)) {
        const option = element(doc, "label", "gt-i-filter-option");
        const box = element(doc, "input", "", { type: "checkbox" });
        box.addEventListener("change", () => {
          const hidden = this.hiddenIds;
          this.userColumns(box.checked ? hidden.filter((x) => x !== id) : [...hidden, id], `${title} ${box.checked ? "shown" : "hidden"}`);
        });
        option.append(box, name);
        root.append(option);
        item.box = box;
      } else {
        const option = element(doc, "div", "gt-i-filter-option");
        option.append(name);
        root.append(option);
      }
      if (!movable.includes(id) && movable.length > 0) {
        // (Where the handle is on the others, so that the names line up)
        const spacer = element(doc, "span", "gt-i-column-grip", { "aria-hidden": "true", "data-gti-none": "" });
        spacer.append(icon(doc, "grip"));
        root.prepend(spacer);
      }
      if (movable.includes(id)) {
        const grip = element(doc, "span", "gt-i-column-grip", { "aria-hidden": "true" });
        grip.append(icon(doc, "grip"));
        grip.addEventListener("pointerdown", (event) => this.startDrag(columns, id, event));
        const move = (way: "earlier" | "later", step: -1 | 1, arrow: string) => {
          const button = element(doc, "button", "gt-i-column-move", {
            type: "button",
            "aria-label": `Move ${title} ${way}`,
            title: `Move ${way} (${alt}${arrow})`,
            "aria-keyshortcuts": `Alt+Arrow${step < 0 ? "Up" : "Down"}`,
          });
          button.append(icon(doc, way));
          button.addEventListener("click", () => this.userMove(id, step));
          return button;
        };
        item.earlier = move("earlier", -1, "↑");
        item.later = move("later", 1, "↓");
        root.prepend(grip);
        root.append(item.earlier, item.later);
        root.addEventListener("keydown", (event) => {
          if ((event.key === "ArrowUp" || event.key === "ArrowDown") && event.altKey && !event.ctrlKey && !event.metaKey && !event.shiftKey) {
            event.preventDefault();
            this.userMove(id, event.key === "ArrowUp" ? -1 : 1);
          }
        });
      }
      list.append(root);
      columns.items.set(id, item);
    }
    const actions = element(doc, "div", "gt-i-export-actions");
    // (A button that's done what it does is disabled with ARIA, so that it keeps focus)
    const action = (text: string, act: () => void) => {
      const button = element(doc, "button", "gt-i-info-button", { type: "button" });
      button.textContent = text;
      button.addEventListener("click", () => {
        if (button.getAttribute("aria-disabled") !== "true") {
          act();
        }
      });
      actions.append(button);
      return button;
    };
    if (hideable.length > 0) {
      columns.all = action("Show all", () => this.userColumns([], "Every column shown"));
    }
    if (movable.length > 0) {
      columns.order = action("Reset order", () => this.userOrder(movable, "Column order reset"));
    }
    popup.panel.append(list, actions);
    return columns;
  }

  // Each column's checkbox: checked if it's shown, and disabled if it's the only one shown (without a
  // stub), so that there's always a column; and its buttons moving it, disabled where it can't move.
  // The items are in the order the columns are shown in (but while one is dragged).
  private updateColumns(columns: Columns): void {
    const spec = this.spec as Spec;
    const hidden = this.hiddenIds;
    const shown = spec.columns.filter(
      (column) => column.role === "stub" || (column.role === "data" && (column.id === null || !hidden.includes(column.id))),
    );
    const only = shown.length === 1 && !spec.stub.groups_as_column ? shown[0]?.id : undefined;
    for (const [id, { box, earlier, later }] of columns.items) {
      if (box !== null) {
        box.checked = !hidden.includes(id);
        box.disabled = id === only;
        box.parentElement?.toggleAttribute("data-gti-disabled", box.disabled);
      }
      earlier?.setAttribute("aria-disabled", String(this.moveOrder(id, -1) === null));
      later?.setAttribute("aria-disabled", String(this.moveOrder(id, 1) === null));
    }
    columns.all?.setAttribute("aria-disabled", String(hidden.length === 0));
    columns.order?.setAttribute("aria-disabled", String(!this.reordered()));
    if (this.dragging === null) {
      const roots = spec.columns.flatMap((_, place) => {
        const id = spec.columns[this.columnAt[place] ?? place]?.id;
        return id == null ? [] : (columns.items.get(id)?.root ?? []);
      });
      if (roots.some((root, i) => columns.list.children[i] !== root)) {
        const focused = (this.getRootNode() as Document | ShadowRoot).activeElement;
        arrange(roots, roots.find((root) => root.contains(focused)), columns.list);
      }
    }
  }

  /**
   * The order of the columns readers can move (as `columnOrder` has it) with `id` moved past the
   * column shown before it (`step` -1) or after it (1) in its run, and its run's; `null` if there's
   * none. (Columns hidden are passed over.)
   */
  private moveOrder(id: string, step: -1 | 1): { order: string[]; run: string[] } | null {
    const runs = this.shownRuns();
    const run = runs.find((ids) => ids.includes(id));
    if (run === undefined) {
      return null;
    }
    const hidden = this.hiddenIds;
    const shown = run.filter((x) => x === id || !hidden.includes(x));
    const past = shown[shown.indexOf(id) + step];
    if (past === undefined) {
      return null;
    }
    const moved = run.filter((x) => x !== id);
    moved.splice(moved.indexOf(past) + (step > 0 ? 1 : 0), 0, id);
    return { order: runs.flatMap((ids) => (ids === run ? moved : ids)), run: moved };
  }

  // What's said of a column moved in its run (in its new order): the column shown before it now,
  // or else the one after it
  private movedText(id: string, run: readonly string[]): string {
    const labels = labelCells(this.table as HTMLTableElement);
    const hidden = this.hiddenIds;
    const shown = run.filter((x) => x === id || !hidden.includes(x));
    const at = shown.indexOf(id);
    const before = shown[at - 1];
    const next = before ?? shown[at + 1];
    const title = this.columnTitle(id, labels);
    return next === undefined
      ? `${title} moved`
      : `${title} moved ${before === undefined ? "before" : "after"} ${this.columnTitle(next, labels, false)}`;
  }

  private userMove(id: string, step: -1 | 1): void {
    const moved = this.moveOrder(id, step);
    if (moved !== null) {
      this.userOrder(moved.order, this.movedText(id, moved.run));
    }
  }

  private userOrder(ids: readonly string[], text: string): void {
    const order = this.columnOrder;
    this.orderColumns(ids);
    if (JSON.stringify(this.columnOrder) === JSON.stringify(order)) {
      return;
    }
    this.render();
    this.announce(text);
    this.dispatchView(null);
  }

  /**
   * Drag a column's item by its handle among its run's (the others make way for it, by where the
   * pointer is on them); dropped, the column moves there, and Escape puts it back.
   */
  private startDrag(columns: Columns, id: string, event: PointerEvent): void {
    if (event.button !== 0 || this.dragging !== null) {
      return;
    }
    event.preventDefault();
    const doc = this.ownerDocument;
    const pointer = event.pointerId;
    const root = (columns.items.get(id) as ColumnItem).root;
    const k = this.runIds().findIndex((ids) => ids.includes(id));
    const run = this.runIds()[k] as string[];
    const items = () =>
      Array.from(columns.list.children as HTMLCollectionOf<HTMLElement>).filter((item) => run.includes(item.dataset.gtiColumn as string));
    this.dragging = { pointer, id };
    root.toggleAttribute("data-gti-dragging", true);
    const move = (event: PointerEvent) => {
      if (event.pointerId !== pointer) {
        return;
      }
      const others = items().filter((item) => item !== root);
      const at = others.filter((item) => {
        const box = item.getBoundingClientRect();
        return event.clientY > box.top + box.height / 2;
      }).length;
      others.splice(at, 0, root);
      arrange(others, root);
    };
    const end = (drop: boolean) => {
      doc.removeEventListener("pointermove", move);
      doc.removeEventListener("pointerup", up);
      doc.removeEventListener("pointercancel", cancel);
      doc.removeEventListener("keydown", escape, true);
      root.removeAttribute("data-gti-dragging");
      this.dragging = null;
      if (drop) {
        const order = items().map((item) => item.dataset.gtiColumn as string);
        this.userOrder(
          this.shownRuns().flatMap((ids, j) => (j === k ? order : ids)),
          this.movedText(id, order),
        );
      }
      this.updateColumns(columns);
    };
    const up = (event: PointerEvent) => {
      if (event.pointerId === pointer) {
        move(event);
        end(true);
      }
    };
    const cancel = (event: PointerEvent) => {
      if (event.pointerId === pointer) {
        end(false);
      }
    };
    const escape = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        // (Only the drag is cancelled: the panel stays open)
        event.preventDefault();
        event.stopPropagation();
        end(false);
      }
    };
    doc.addEventListener("pointermove", move);
    doc.addEventListener("pointerup", up);
    doc.addEventListener("pointercancel", cancel);
    doc.addEventListener("keydown", escape, true);
  }

  /** Make the export panel, and the bar's button that opens it. */
  private makeExporter(formats: readonly ExportFormat[]): Exporter {
    const doc = this.ownerDocument;
    const popup = this.makePanel("export", "Export the table", "Export");
    const panel = popup.panel;
    panel.classList.add("gt-i-export");
    const rows = element(doc, "p", "gt-i-info-rows");
    panel.append(rows);
    const exporter: Exporter = { ...popup, rows, selected: null, selectedItem: null, backend: null, note: null };
    if ((this.spec as Spec).controls.selection !== null) {
      const item = element(doc, "label", "gt-i-filter-option");
      const box = element(doc, "input", "", { type: "checkbox" });
      box.addEventListener("change", () => this.updateExporter(exporter));
      item.append(box, "Selected rows only");
      panel.append(item);
      exporter.selected = box;
      exporter.selectedItem = item;
    }
    const code = (this.spec as Spec).export?.code;
    if (formats.includes("code") && code != null) {
      const item = element(doc, "label", "gt-i-info-item");
      const select = element(doc, "select", "");
      for (const name of ["Polars", "pandas", "Narwhals"]) {
        const option = element(doc, "option", "", { value: name.toLowerCase() });
        option.textContent = name;
        select.append(option);
      }
      select.value = code.backend;
      const text = doc.createElement("span");
      text.textContent = "Code for";
      item.append(text, select);
      panel.append(item);
      exporter.backend = select;
    }
    const actions = element(doc, "div", "gt-i-export-actions");
    for (const format of formats) {
      if (format === "code" && exporter.backend === null) {
        continue;
      }
      const button = element(doc, "button", "gt-i-info-button", { type: "button" });
      button.dataset.gtiExport = format;
      button.textContent =
        format === "clipboard" ? "Copy" : format === "code" ? "Copy code" : `Download ${format.toUpperCase()}`;
      button.addEventListener("click", () => this.userExport(exporter, format));
      actions.append(button);
    }
    panel.append(actions);
    if (exporter.backend !== null) {
      const note = element(doc, "p", "gt-i-export-note", { hidden: "" });
      note.textContent = "The code leaves out the search.";
      panel.append(note);
      exporter.note = note;
    }
    return exporter;
  }

  // How many rows the panel exports: those the search and filters keep, or those selected
  private updateExporter(exporter: Exporter): void {
    const count = this.selected.size;
    if (exporter.selected !== null && exporter.selectedItem !== null) {
      exporter.selectedItem.hidden = count === 0;
      exporter.selected.checked &&= count > 0;
    }
    if (exporter.note !== null) {
      exporter.note.hidden = this.searchValue === "";
    }
    const total = this.matchCount;
    exporter.rows.textContent = exporter.selected?.checked === true
      ? this.selectionText()
      : this.matched === null
        ? plural(total)
        : `${plural(total)} (filtered from ${(this.spec as Spec).nrows})`;
  }

  private userExport(exporter: Exporter, format: ExportFormat): void {
    const selected = exporter.selected?.checked === true;
    const done = (text: string, detail: ExportEventDetail | null) => {
      exporter.rows.textContent = text;
      this.announce(text);
      if (detail !== null) {
        this.dispatchEvent(new CustomEvent<ExportEventDetail>(EXPORT_EVENT, { bubbles: true, composed: true, detail }));
      }
    };
    if (format === "csv" || format === "tsv" || format === "json") {
      const exported = this.exported(selected) as Exported;
      this.download(
        format,
        format === "csv"
          ? csv(exported.text)
          : format === "tsv"
            ? `${toTSV(exported.text, true)}\n`
            : recordsJSON(exported.keys, exported.text.slice(1)),
      );
      done(`Downloaded ${plural(exported.rows.length)}`, { format, rows: exported.rows });
    } else if (format === "code") {
      // (Of the view, whichever rows are selected)
      const backend = (exporter.backend as HTMLSelectElement).value as CodeBackend;
      let code: string;
      try {
        code = this.toCode(backend);
      } catch {
        done("Couldn't write the code", null);
        return;
      }
      void this.clip({ "text/plain": code }).then((ok) =>
        ok ? done("Copied the code", { format, rows: [], code, backend }) : done("Couldn't copy the code", null),
      );
    } else {
      // (Written in the click, while the page may still write to the clipboard)
      void this.copyRows(selected).then((rows) =>
        rows === null ? done("Couldn't copy the rows", null) : done(`Copied ${plural(rows.length)}`, { format, rows }),
      );
    }
  }

  // Download CSV, TSV or JSON, as a file named for the spec's `export.filename` (CSV and TSV with a
  // byte order mark, so that spreadsheets read them as UTF-8; JSON can't have one)
  private download(format: "csv" | "tsv" | "json", text: string): void {
    const type = format === "csv" ? "text/csv" : format === "tsv" ? "text/tab-separated-values" : "application/json";
    const parts = format === "json" ? [text] : ["\uFEFF", text];
    const url = URL.createObjectURL(new Blob(parts, { type: `${type};charset=utf-8` }));
    const link = element(this.ownerDocument, "a", "", {
      href: url,
      download: `${(this.spec as Spec).export?.filename}.${format}`,
    });
    this.append(link);
    link.click();
    link.remove();
    // (Once the download has surely started)
    setTimeout(() => URL.revokeObjectURL(url), 4e4);
  }

  // Copy the rows to the clipboard, as an HTML table and as tab-separated text, returning the rows
  // copied (or `null`, if they couldn't be)
  private copyRows(selected: boolean): Promise<number[] | null> {
    const exported = this.exported(selected);
    if (exported === null) {
      return Promise.resolve(null);
    }
    return this.clip({ "text/html": this.exportHTML(exported), "text/plain": toTSV(exported.text) }).then((ok) =>
      ok ? exported.rows : null,
    );
  }

  // Write to the clipboard (the text of each type), returning whether it was written
  private clip(data: Record<string, string>): Promise<boolean> {
    const doc = this.ownerDocument;
    // Without the Clipboard API (or its permission), as a copy would
    const fallback = () => {
      const copy = (event: ClipboardEvent) => {
        event.preventDefault();
        for (const type in data) {
          event.clipboardData?.setData(type, data[type] as string);
        }
      };
      doc.addEventListener("copy", copy);
      try {
        return doc.execCommand("copy");
      } catch {
        return false;
      } finally {
        doc.removeEventListener("copy", copy);
      }
    };
    const blobs: Record<string, Blob> = {};
    for (const type in data) {
      blobs[type] = new Blob([data[type] as string], { type });
    }
    try {
      return navigator.clipboard.write([new ClipboardItem(blobs)]).then(() => true, fallback);
    } catch {
      return Promise.resolve(fallback());
    }
  }

  // The rows as an HTML table: the column labels' text, then copies of the cells (keeping their
  // authored styles, but not ours), aligned as their columns are
  private exportHTML({ text, cells }: Exported): string {
    const doc = this.ownerDocument;
    const spec = this.spec as Spec;
    const aligns = [
      ...(spec.groups.length > 0 ? [null] : []),
      ...this.exportedColumns().map((c) => spec.columns[c]?.align ?? null),
    ];
    const table = doc.createElement("table");
    const head = table.createTHead();
    const body = table.createTBody();
    text.forEach((row, i) => {
      const tr = (i > 0 ? body : head).insertRow();
      row.forEach((label, c) => {
        const cell = cells[i - 1]?.[c];
        const copy = (cell == null ? doc.createElement(i > 0 ? "td" : "th") : withoutMarks(cell)) as HTMLElement;
        if (cell == null) {
          copy.textContent = label;
        }
        for (const name of ["class", "id", "rowspan", "headers"]) {
          copy.removeAttribute(name);
        }
        for (const property of Array.from(copy.style)) {
          if (/^(--|top$|bottom$|inset)/.test(property)) {
            copy.style.removeProperty(property);
          }
        }
        // (Unless it has its own)
        copy.style.textAlign ||= aligns[c] ?? "";
        tr.append(copy);
      });
    });
    return table.outerHTML;
  }

  // The rows to export: each data row the search and filters keep (or each one selected), in the
  // order shown, on every page; with a cell for each column but those hidden (and the stub's for
  // summary rows' labels), after one for the row's group's label (with groups). The labels are the
  // columns', after their spanners' ("Revenue – gross").
  private exported(selected: boolean): Exported | null {
    const spec = this.spec;
    const table = this.table;
    if (spec === null || table === null || this.tbody === null) {
      return null;
    }
    const labels = labelCells(table);
    const kept = this.exportedColumns();
    const grouped = spec.groups.length > 0;
    const head = kept.map((c) => this.columnTitle((spec.columns[c] as ColumnSpec & { id: string }).id, labels));
    const ids = kept.map((c) => (spec.columns[c] as ColumnSpec & { id: string }).id);
    // (The group's key is "group", with a `_` before it while a column has that id)
    let group = "group";
    while (ids.includes(group)) {
      group = `_${group}`;
    }
    const exported: Exported = {
      rows: [],
      keys: [...(grouped ? [group] : []), ...ids],
      text: [[...(grouped ? [""] : []), ...head]],
      cells: [],
    };

    // (A cell merged across rows, in a hierarchical stub, is each of its rows')
    const spans: [Element | undefined, number][] = [];
    for (const tr of Array.from(this.tbody.children) as HTMLTableRowElement[]) {
      const row = this.bodyRow(tr);
      if (typeof row !== "number") {
        continue;
      }
      const own = this.dataCells(tr);
      let k = 0;
      const all = spec.columns.map((_, c) => {
        const span = spans[c];
        if (span !== undefined && span[1] > 0) {
          span[1]--;
          return span[0];
        }
        const cell = own[k++];
        spans[c] = [cell, ((cell as HTMLTableCellElement | undefined)?.rowSpan ?? 1) - 1];
        return cell;
      });
      if (selected ? !this.selected.has(row) : this.matched !== null && this.matched[row] !== 1) {
        continue;
      }
      const group = this.rowGroups[row];
      const heading = group?.headings[0] ?? group?.cell;
      const cells = kept.map((c) => all[c] ?? null);
      exported.rows.push(row);
      exported.cells.push([...(grouped ? [null] : []), ...cells]);
      exported.text.push([
        ...(grouped ? [heading == null ? "" : labelText(heading)] : []),
        ...cells.map((cell) => (cell === null ? "" : labelText(cell))),
      ]);
    }
    return exported;
  }

  // The columns exported (by index in the spec), in the order shown: each with an id, but those
  // hidden
  private exportedColumns(): number[] {
    const spec = this.spec as Spec;
    return spec.columns.flatMap((_, place) => {
      const c = this.columnAt[place] ?? place;
      const id = spec.columns[c]?.id ?? null;
      return id === null || this.hiddenIds.includes(id) ? [] : [c];
    });
  }

  // A column's label, after its spanners' ("Revenue – gross"), or its id, without one
  private columnTitle(id: string, labels: Map<string, HTMLTableCellElement>, spanned = true): string {
    const spec = this.spec as Spec;
    const label = (key: string | null) => {
      const th = key === null ? undefined : labels.get(key);
      return th === undefined ? "" : labelText(th);
    };
    const spanners = spec.spanners
      .filter((spanner) => spanned && spanner.columns.includes(id))
      .sort((a, b) => b.level - a.level)
      .map((spanner) => label(spanner.header));
    const header = spec.columns.find((column) => column.id === id)?.header ?? null;
    return [...spanners, label(header) || id].filter(Boolean).join(" – ");
  }

  // A filter button in the label of each column that can be filtered (after its sort button), and
  // a filter for each, whether or not it has a label (and so a button)
  private addFilters(table: HTMLTableElement, spec: Spec): void {
    const doc = this.ownerDocument;
    const cells = labelCells(table);

    for (const filterSpec of spec.filters ?? []) {
      const id = filterSpec.column;
      const index = spec.columns.findIndex((column) => column.id === id);
      // (Or a column only for querying, which has no cells, nor a label cell)
      const query = spec.query_columns?.find((column) => column.id === id);
      const header = spec.columns[index]?.header;
      if ((header === undefined && query === undefined) || this.filters.some((control) => control.filter.column === id)) {
        continue;
      }
      const th = header == null ? null : (cells.get(header) ?? null);
      const label = this.sortHeaders.get(id)?.label ?? ((th !== null && labelText(th)) || query?.label || id);
      const filter = new ColumnFilter(filterSpec, index, spec.ranks[id] ?? [], query?.texts, spec.columns[index]?.kind ?? query?.kind);
      const control: FilterControl = {
        filter,
        label,
        th,
        button: null,
        panel: null,
        clear: null,
        text: null,
        min: null,
        max: null,
        options: [],
        token: null,
        names: null,
      };
      this.filters.push(control);
      if (th === null) {
        continue;
      }

      const button = doc.createElement("button");
      button.type = "button";
      button.className = "gt-i-filter-button";
      button.title = "Filter";
      button.setAttribute("aria-expanded", "false");
      button.append(icon(doc, "filter"));
      controlsRow(th).append(button);
      control.button = button;
      button.addEventListener("click", () => {
        if (this.openFilter === control) {
          this.closeFilter(false);
        } else {
          this.openFilterPanel(control);
        }
      });
      button.addEventListener("focusout", (event) => this.leaveFilter(control, event));
    }

    if (this.filters.length > 0) {
      this.updateFilterButtons();
      this.addLiveRegion();
      this.observeLayout();
    }
  }

  /**
   * Make a filter's panel: the column's label and a Clear button, over a text field (a text
   * filter), a checkbox for each value (a facet), fields for the bounds (a range, or a date
   * filter's date fields), or a radio button for each value and one for any (a bool filter).
   */
  private makeFilterPanel(control: FilterControl): HTMLElement {
    const doc = this.ownerDocument;
    const { filter, label } = control;
    const panel = doc.createElement("div");
    panel.className = "gt-i-filter";
    panel.id = `gt-i-filter-${++infoCount}`;
    panel.dataset.gtiFilter = filter.type;
    panel.setAttribute("role", "group");
    panel.setAttribute("aria-label", `Filter ${label}`);
    panel.hidden = true;
    control.button?.setAttribute("aria-controls", panel.id);

    const head = doc.createElement("div");
    head.className = "gt-i-filter-head";
    const title = doc.createElement("span");
    title.className = "gt-i-filter-title";
    title.textContent = label;
    const clear = doc.createElement("button");
    clear.type = "button";
    clear.className = "gt-i-info-button";
    clear.textContent = "Clear";
    clear.setAttribute("aria-label", `Clear the filter on ${label}`);
    // (Disabled with ARIA, so that it keeps focus once it has cleared the filter)
    clear.addEventListener("click", () => {
      if (clear.getAttribute("aria-disabled") !== "true") {
        this.cancelFilterTimer();
        this.userFilter(() => filter.clear());
        this.syncFilter(control);
      }
    });
    head.append(title, clear);
    panel.append(head);
    control.clear = clear;

    // A field for text, which filters once typing pauses, or at once on Enter
    const field = (name: string, placeholder: string, mode: "text" | "decimal") => {
      const input = doc.createElement("input");
      input.type = "text";
      input.inputMode = mode;
      input.placeholder = placeholder;
      input.setAttribute("aria-label", name);
      input.setAttribute("enterkeyhint", "done");
      input.autocomplete = "off";
      input.spellcheck = false;
      input.addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
          // (And don't submit a form the table is in)
          event.preventDefault();
          this.flushFilter();
        }
      });
      return input;
    };

    if (filter.type === "text") {
      const input = field(`${label} contains`, "Contains", "text");
      input.className = "gt-i-filter-text";
      input.addEventListener("input", () => this.queueFilter(() => filter.setText(input.value)));
      panel.append(input);
      control.text = input;
    } else if (filter.type === "range") {
      // (The bounds the column's numbers have, as placeholders)
      const numbers = (filter.spec.values ?? []).filter((value): value is number => typeof value === "number");
      const bounds = doc.createElement("div");
      bounds.className = "gt-i-filter-range";
      const bound = (text: string, placeholder: number | undefined) => {
        const el = doc.createElement("label");
        el.className = "gt-i-filter-bound";
        const name = doc.createElement("span");
        name.textContent = text;
        const hint = placeholder === undefined ? "" : String(placeholder);
        const input = field(`${label}, ${text.toLowerCase()}`, hint, "decimal");
        input.addEventListener("input", () => this.queueFilter(() => this.readBounds(control)));
        el.append(name, input);
        bounds.append(el);
        return input;
      };
      control.min = bound("At least", numbers[0]);
      control.max = bound("At most", numbers[numbers.length - 1]);
      panel.append(bounds);
    } else if (filter.type === "date") {
      // (Date fields, or for a column with times other than midnight, date and time ones; from the
      // column's first date to its last, with seconds if any of its times has them)
      const dates = (filter.spec.values ?? []).filter((value): value is string => typeof value === "string");
      const keys = filter.times ? filter.dateKeys() : [];
      const clock = keys.some((key) => key !== null && !key.endsWith("T00:00:00.000000000"));
      const seconds = keys.some((key) => key !== null && !key.endsWith(":00.000000000"));
      const bounds = doc.createElement("div");
      // (Date and time fields, too wide to be side by side, one above the other)
      bounds.className = clock ? "gt-i-filter-range gt-i-filter-range-stacked" : "gt-i-filter-range";
      const bound = (text: string, which: "min" | "max") => {
        const el = doc.createElement("label");
        el.className = "gt-i-filter-bound";
        const name = doc.createElement("span");
        name.textContent = text;
        const input = doc.createElement("input");
        input.type = clock ? "datetime-local" : "date";
        if (seconds) {
          input.step = "1";
        }
        input.min = dateField(dates[0] ?? "", clock);
        input.max = dateField(dates[dates.length - 1] ?? "", clock);
        input.setAttribute("aria-label", `${label}, ${text.toLowerCase()}`);
        input.setAttribute("enterkeyhint", "done");
        input.addEventListener("keydown", (event) => {
          if (event.key === "Enter") {
            event.preventDefault();
            this.flushFilter();
          }
        });
        input.addEventListener("input", () => this.queueFilter(() => this.readDate(control, which)));
        el.append(name, input);
        bounds.append(el);
        return input;
      };
      control.min = bound("From", "min");
      control.max = bound("To", "max");
      panel.append(bounds);
    } else if (filter.type === "bool") {
      // (Any value, then true, false and a missing one, as the table shows them)
      const list = doc.createElement("div");
      list.className = "gt-i-filter-options";
      list.setAttribute("role", "radiogroup");
      list.setAttribute("aria-label", label);
      for (const [key, text] of [[ANY, "Any"] as [number, string], ...this.boolNames(control)]) {
        const item = doc.createElement("label");
        item.className = "gt-i-filter-option";
        const box = doc.createElement("input");
        box.type = "radio";
        box.name = panel.id;
        const name = doc.createElement("span");
        name.className = "gt-i-filter-value";
        name.textContent = text;
        const count = doc.createElement("span");
        count.className = "gt-i-filter-count";
        item.append(box, name, count);
        list.append(item);
        box.addEventListener("change", () =>
          this.userFilter(() => {
            filter.chosen = key === ANY ? new Set() : new Set([key]);
          }),
        );
        control.options.push({ key, item, box, count });
      }
      panel.append(list);
    } else {
      const list = doc.createElement("div");
      list.className = "gt-i-filter-options";
      for (const [key, text] of this.facetNames(control)) {
        const item = doc.createElement("label");
        item.className = "gt-i-filter-option";
        const box = doc.createElement("input");
        box.type = "checkbox";
        const name = doc.createElement("span");
        name.className = "gt-i-filter-value";
        name.textContent = text;
        const count = doc.createElement("span");
        count.className = "gt-i-filter-count";
        item.append(box, name, count);
        list.append(item);
        box.addEventListener("change", () =>
          this.userFilter(() => {
            if (box.checked) {
              filter.chosen.add(key);
            } else {
              filter.chosen.delete(key);
            }
          }),
        );
        control.options.push({ key, item, box, count });
      }
      panel.append(list);
    }

    // Escape closes it, as Tab does out of either end of it (back to its button: the panel is at
    // the end of the element, not after the button)
    panel.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        // (And don't, say, close a dialog the table is in)
        event.preventDefault();
        event.stopPropagation();
        this.closeFilter(true);
      } else if (event.key === "Tab") {
        // (Of a bool filter's radio buttons, only the one checked is a stop)
        const controls = Array.from(panel.querySelectorAll<HTMLElement>('button, input:not([type="radio"]), input:checked'));
        if (event.target === (event.shiftKey ? controls[0] : controls[controls.length - 1])) {
          event.preventDefault();
          this.closeFilter(true);
        }
      }
    });
    panel.addEventListener("focusout", (event) => this.leaveFilter(control, event));

    // Outside the table's scrolling containers, so that it isn't cut off
    this.append(panel);
    control.panel = panel;
    this.syncFilter(control);
    return panel;
  }

  // A column's values, in order (a missing one last), with the text a row with each shows
  private facetNames(control: FilterControl): [number, string][] {
    if (control.names !== null) {
      return control.names;
    }
    const { filter } = control;
    const values = filter.spec.values ?? [];
    const labels = new Map<number, string>();
    let missing = false;
    this.rowElements.forEach((tr, row) => {
      const key = filter.key(row);
      if (key === MISSING) {
        missing = true;
      } else if (!labels.has(key)) {
        const cell = this.dataCells(tr)[filter.index];
        labels.set(key, (cell !== undefined && labelText(cell)) || filter.texts?.[row] || String(values[key]));
      }
    });
    const entries = values.map((value, key): [number, string] => [key, labels.get(key) ?? String(value)]);
    if (missing) {
      entries.push([MISSING, "(Missing)"]);
    }
    control.names = entries;
    return entries;
  }

  // A bool filter's values, as `facetNames()` has them, but true first, then false, then missing
  private boolNames(control: FilterControl): [number, string][] {
    const values = control.filter.spec.values ?? [];
    const order = (key: number) => (key === MISSING ? 2 : values[key] === true ? 0 : 1);
    return [...this.facetNames(control)].sort(([a], [b]) => order(a) - order(b));
  }

  // A range's bounds, from its fields: a bound that isn't a number is marked, and left as it was
  private readBounds(control: FilterControl): void {
    const read = (input: HTMLInputElement | null, old: number | null) => {
      const text = input?.value.trim() ?? "";
      const value = text === "" ? null : Number(text);
      const bad = value !== null && !Number.isFinite(value);
      if (bad) {
        input?.setAttribute("aria-invalid", "true");
      } else {
        input?.removeAttribute("aria-invalid");
      }
      return bad ? old : value;
    };
    const { filter } = control;
    filter.min = read(control.min, filter.min as number | null);
    filter.max = read(control.max, filter.max as number | null);
  }

  // A date filter's bound, from its field (which has a date, or nothing; and while one is part
  // typed, nothing, but a bad input): a part-typed date is marked, and leaves the bound as it was
  private readDate(control: FilterControl, which: "min" | "max"): void {
    const input = control[which];
    if (input === null) {
      return;
    }
    const { filter } = control;
    const value = input.value;
    const bad = value === "" ? input.validity.badInput : !filter.isDateBound(value);
    if (bad) {
      input.setAttribute("aria-invalid", "true");
    } else {
      input.removeAttribute("aria-invalid");
      // (Unless the field has the bound as it shows it, cut to milliseconds, or to its date)
      if (dateKey(value) !== dateKey(dateField(String(filter[which] ?? ""), input.type === "datetime-local"))) {
        filter[which] = value === "" ? null : value;
      }
    }
  }

  // Show a filter's state in its panel's fields
  private syncFilter(control: FilterControl): void {
    const { filter } = control;
    if (control.text !== null) {
      control.text.value = filter.text;
    }
    for (const [input, value] of [
      [control.min, filter.min],
      [control.max, filter.max],
    ] as const) {
      if (input !== null) {
        input.value =
          value === null ? "" : filter.type === "date" ? dateField(String(value), input.type === "datetime-local") : String(value);
        input.removeAttribute("aria-invalid");
      }
    }
    for (const option of control.options) {
      option.box.checked = option.key === ANY ? filter.chosen.size === 0 : filter.chosen.has(option.key);
    }
  }

  private openFilterPanel(control: FilterControl, button: HTMLElement | null = control.button): void {
    if (button === null) {
      return;
    }
    // (A filter's panel in the sheet opens below its button there, the sheet staying open)
    const sheet = this.sheet?.contains(button) === true;
    this.closeFilter(false);
    if (!sheet) {
      this.closePanel(false);
    }
    const panel = control.panel ?? this.makeFilterPanel(control);
    if (sheet) {
      button.after(panel);
    } else if (panel.parentNode !== this) {
      this.append(panel);
    }
    // (Over the table, so filled with what's behind it; in the table's font)
    panel.style.backgroundColor = backdropColor(this);
    panel.style.fontFamily = getComputedStyle(this.table as HTMLTableElement).fontFamily;
    panel.hidden = false;
    button.setAttribute("aria-expanded", "true");
    this.openFilter = control;
    this.filterAnchor = button;
    this.updateFilterPanel();

    // A press anywhere else closes it; it follows its button as anything scrolls
    const doc = this.ownerDocument;
    this.filterPress = (event: PointerEvent) => {
      const path = event.composedPath();
      if (!path.includes(panel) && !path.includes(button)) {
        this.closeFilter(false);
      }
    };
    this.filterScroll = () => this.placeFilter();
    doc.addEventListener("pointerdown", this.filterPress);
    doc.addEventListener("scroll", this.filterScroll, { capture: true, passive: true });
    (panel.querySelector<HTMLElement>('input[type="radio"]:checked') ?? panel.querySelector<HTMLElement>("input"))?.focus();
  }

  // The open panel closes when focus goes elsewhere (but not when the window loses it, nor to what
  // it's in, as a press in it that focuses nothing in it sends it: a press outside it closes it)
  private leaveFilter(control: FilterControl, event: FocusEvent): void {
    const to = event.relatedTarget as Node | null;
    const { panel } = control;
    if (
      this.openFilter === control &&
      to !== null &&
      to !== this.filterAnchor &&
      !(panel !== null && (panel.contains(to) || to.contains(panel)))
    ) {
      this.closeFilter(false);
    }
  }

  private closeFilter(focus: boolean): void {
    const doc = this.ownerDocument;
    if (this.filterPress !== null) {
      doc.removeEventListener("pointerdown", this.filterPress);
      this.filterPress = null;
    }
    if (this.filterScroll !== null) {
      doc.removeEventListener("scroll", this.filterScroll, { capture: true });
      this.filterScroll = null;
    }
    const control = this.openFilter;
    const anchor = this.filterAnchor;
    if (control === null) {
      return;
    }
    this.openFilter = null;
    this.filterAnchor = null;
    // (A change may be waiting on the typing to pause)
    this.flushFilter();
    if (control.panel !== null) {
      control.panel.hidden = true;
    }
    anchor?.setAttribute("aria-expanded", "false");
    // (A token kept for its open panel goes, if its filter is off)
    this.updateTokens();
    if (focus) {
      (anchor?.isConnected ? anchor : (control.button ?? this.bar?.info.button))?.focus();
    }
  }

  // The open panel is below its button, from the button's inline start (as far as the element's
  // width allows); or, from a token in the bar, above it where there's room in the window
  private placeFilter(): void {
    const panel = this.openFilter?.panel;
    const anchor = this.filterAnchor;
    if (anchor === null || panel == null || this.sheet?.contains(panel)) {
      return;
    }
    const host = this.getBoundingClientRect();
    const button = anchor.getBoundingClientRect();
    const width = panel.offsetWidth;
    const height = panel.offsetHeight;
    const start = this.isRtl() ? button.right - width : button.left;
    const above = anchor !== this.openFilter?.button && button.top - height - 4 >= 0;
    panel.style.left = `${Math.max(0, Math.min(start - host.left, host.width - width))}px`;
    panel.style.top = `${(above ? button.top - height - 4 : button.bottom + 4) - host.top}px`;
  }

  private updateFilters(): void {
    if (this.filters.length > 0) {
      this.updateFilterButtons();
      this.updateTokens();
      this.updateFilterPanel();
    }
  }

  // A filtered column's button is marked (and says so)
  private updateFilterButtons(): void {
    for (const { filter, label, th, button } of this.filters) {
      if (th !== null && button !== null) {
        th.toggleAttribute("data-gti-filtered", filter.active);
        button.setAttribute("aria-label", filter.active ? `Filter ${label} (on)` : `Filter ${label}`);
      }
    }
  }

  // The tokens' row, in the bar, in which the arrow keys go from token to token and Backspace or
  // Delete removes one
  private addTokens(bar: Bar, rtl: boolean): void {
    const list = this.ownerDocument.createElement("ul");
    list.className = "gt-i-tokens";
    list.setAttribute("aria-label", "Filters");
    list.hidden = true;
    bar.root.append(list);
    bar.tokens = list;
    list.addEventListener("keydown", (event) => {
      if (event.altKey || event.ctrlKey || event.metaKey) {
        return;
      }
      const items = Array.from(list.children);
      const at = items.findIndex((item) => item.contains(event.target as Node));
      const control = this.filters.find((c) => c.token?.item === items[at]);
      const group = Array.from(this.groupTokens).find(([, token]) => token.item === items[at])?.[0];
      const targets: Record<string, number> = {
        ArrowLeft: rtl ? at + 1 : at - 1,
        ArrowRight: rtl ? at - 1 : at + 1,
        Home: 0,
        End: items.length - 1,
      };
      const target = items[targets[event.key] ?? -1];
      if ((event.key === "Backspace" || event.key === "Delete") && (control ?? group) !== undefined) {
        event.preventDefault();
        if (control !== undefined) {
          this.removeToken(control);
        } else {
          this.removeGroup(group as FilterGroup);
        }
      } else if (target !== undefined) {
        event.preventDefault();
        target.querySelector("button")?.focus();
      }
    });
  }

  // A token for each filter that's on (and one whose panel is open from it), in column order, then
  // one for each of the query's groups, and a button clearing them all when there's more than one.
  // Tokens that stay are kept in the row, so that they keep focus.
  private updateTokens(): void {
    const bar = this.bar;
    const list = bar?.tokens;
    if (list == null) {
      return;
    }
    const items: Element[] = [];
    for (const control of this.filters) {
      if (control.filter.active || (control.token !== null && control.token.open === this.filterAnchor)) {
        const token = control.token ?? this.makeToken(control);
        const text = this.tokenText(control);
        // (Text set again, as it is, scrolls the line back to its start in WebKit)
        if (token.open.textContent !== text) {
          token.open.textContent = text;
          token.open.title = text;
        }
        items.push(token.item);
      }
    }
    const tokens = new Map<FilterGroup, FilterToken>();
    for (const group of this.filterGroups) {
      const token = this.groupTokens.get(group) ?? this.makeGroupToken(group);
      tokens.set(group, token);
      items.push(token.item);
    }
    this.groupTokens = tokens;
    if (items.length > 1) {
      items.push(bar?.clearAll ?? this.makeClearAll(bar as Bar));
    }
    let at = list.firstElementChild;
    for (const item of items) {
      if (item === at) {
        at = at.nextElementSibling;
      } else {
        list.insertBefore(item, at);
      }
    }
    while (at !== null) {
      const next = at.nextElementSibling;
      at.remove();
      at = next;
    }
    // (In the query box's place while it's open)
    list.hidden = items.length === 0 || bar?.query?.root.hidden === false;
  }

  private makeToken(control: FilterControl): FilterToken {
    const doc = this.ownerDocument;
    const item = doc.createElement("li");
    item.className = "gt-i-token";
    const open = doc.createElement("button");
    open.type = "button";
    open.className = "gt-i-token-open";
    open.setAttribute("aria-expanded", "false");
    const remove = doc.createElement("button");
    remove.type = "button";
    remove.className = "gt-i-token-remove";
    remove.setAttribute("aria-label", `Remove the filter on ${control.label}`);
    remove.title = "Remove (Delete)";
    remove.append(icon(doc, "clear"));
    item.append(open, remove);
    open.addEventListener("click", () => {
      if (this.openFilter === control && this.filterAnchor === open) {
        this.closeFilter(false);
      } else {
        this.openFilterPanel(control, open);
        open.setAttribute("aria-controls", control.panel?.id ?? "");
      }
    });
    open.addEventListener("focusout", (event) => this.leaveFilter(control, event));
    remove.addEventListener("click", () => this.removeToken(control));
    control.token = { item, open, remove };
    return control.token;
  }

  // A group's token: its query text (or for an `is_null` clause, "Population is missing"), which
  // opens the query box with the text selected
  private makeGroupToken(group: FilterGroup): FilterToken {
    const doc = this.ownerDocument;
    const text = formatQuery({ and: [group.item] });
    const part = group.item;
    const clause = "not" in part ? part.not : part;
    const label = this.filters.find((control) => control.filter === group.filters[0])?.label;
    const shown = isClause(clause) && clause.op === "is_null" ? `${label} is ${clause === part ? "" : "not "}missing` : text;
    const item = doc.createElement("li");
    item.className = "gt-i-token";
    item.toggleAttribute("data-gti-group", true);
    const open = doc.createElement("button");
    open.type = "button";
    open.className = "gt-i-token-open";
    open.textContent = shown;
    open.title = `${text} (edit as text)`;
    const remove = doc.createElement("button");
    remove.type = "button";
    remove.className = "gt-i-token-remove";
    remove.setAttribute("aria-label", `Remove the filter ${shown}`);
    remove.title = "Remove (Delete)";
    remove.append(icon(doc, "clear"));
    item.append(open, remove);
    open.addEventListener("click", () => this.openQuery(text));
    remove.addEventListener("click", () => this.removeGroup(group));
    return { item, open, remove };
  }

  private makeClearAll(bar: Bar): HTMLElement {
    const doc = this.ownerDocument;
    const item = doc.createElement("li");
    const button = doc.createElement("button");
    button.type = "button";
    button.className = "gt-i-token-clear";
    button.textContent = "Clear all";
    button.setAttribute("aria-label", "Clear all the filters");
    item.append(button);
    button.addEventListener("click", () => {
      this.closeFilter(false);
      this.cancelFilterTimer();
      this.userFilter(() => this.clearFilters());
      bar.info.button.focus();
    });
    bar.clearAll = item;
    return item;
  }

  // What a filter keeps, in the column's terms: "Status: single-tier, city", "Population ≥ 10,000"
  // or "Name contains “cote”" (with the values as the table shows them)
  private tokenText(control: FilterControl): string {
    const { filter, label } = control;
    if (!filter.active) {
      return `${label}: any`;
    }
    if (filter.type === "text") {
      return `${label} contains “${filter.text.trim()}”`;
    }
    const names = this.facetNames(control);
    if (filter.type === "facet" || filter.type === "bool") {
      const chosen = names.filter(([key]) => filter.chosen.has(key)).map(([, name]) => name);
      return `${label}: ${chosen.length > 3 ? `${chosen.slice(0, 2).join(", ")} +${chosen.length - 2}` : chosen.join(", ")}`;
    }
    const lang = this.closest("[lang]")?.getAttribute("lang") || undefined;
    const { min, max } = filter;
    if (filter.type === "date") {
      // (A bound that's one of the column's dates as the table shows it, or else as the language
      // has dates)
      const bound = (value: string) => names[filter.dateRank(value) ?? -1]?.[1] ?? dateText(value, lang);
      return `${label} ${
        min === null
          ? `≤ ${bound(max as string)}`
          : max === null
            ? `≥ ${bound(min as string)}`
            : `${bound(min as string)} – ${bound(max as string)}`
      }`;
    }
    // (A bound that's one of the column's values as the table shows it, or else as a number)
    const bound = (value: number) => {
      const name = names[filter.rankOf(value) ?? -1]?.[1];
      if (name !== undefined) {
        return name;
      }
      try {
        return new Intl.NumberFormat(lang).format(value);
      } catch {
        return String(value);
      }
    };
    return `${label} ${
      min === null
        ? `≤ ${bound(max as number)}`
        : max === null
          ? `≥ ${bound(min as number)}`
          : `${bound(min as number)}–${bound(max as number)}`
    }`;
  }

  // Turn a filter off from its token
  private removeToken(control: FilterControl): void {
    this.dropToken(control.token?.item, () => {
      if (this.openFilter === control) {
        this.closeFilter(false);
      }
      this.userFilter(() => control.filter.clear());
      this.syncFilter(control);
    });
  }

  // Take a group out of the query, from its token
  private removeGroup(group: FilterGroup): void {
    this.dropToken(this.groupTokens.get(group)?.item, () =>
      this.userFilter(() => {
        this.filterGroups = this.filterGroups.filter((other) => other !== group);
      }),
    );
  }

  // Remove a token's filter (with `remove`), with focus on the token after it (or before it, or the
  // info button, without one)
  private dropToken(item: Element | undefined, remove: () => void): void {
    const list = this.bar?.tokens;
    if (list == null || item === undefined) {
      return;
    }
    const at = Array.from(list.children).indexOf(item);
    remove();
    const tokens = Array.from(list.children).filter((el) => el !== this.bar?.clearAll);
    (tokens[Math.min(at, tokens.length - 1)]?.querySelector("button") ?? this.bar?.info.button)?.focus();
  }

  // The query box, on the tokens' line, whose text applies on Enter (or with its ✓ button), unless
  // it isn't a query the table can have, which is said below it (and announced), with the place
  // marked. The text is highlighted as it's typed, and a list suggests what can go at the caret:
  // the arrow keys go through it, and Tab or Enter take a suggestion.
  private addQuery(bar: Bar): void {
    const doc = this.ownerDocument;
    const id = `gt-i-query-${++infoCount}`;
    const toggle = this.barButton("query", "Edit the filters as text", "Filters as text");
    toggle.setAttribute("aria-expanded", "false");
    toggle.setAttribute("aria-controls", id);
    // (Drawn by the input over its highlighted copy, where the browser has highlights)
    const root = element(doc, "div", "gt-i-query", { id, hidden: "" });
    root.toggleAttribute("data-gti-painted", pageHighlight(`${QUERY_HIGHLIGHT}-keyword`) !== undefined);
    const field = element(doc, "div", "gt-i-query-field");
    const text = element(doc, "span", "gt-i-query-text", { dir: "ltr" });
    const mirror = element(doc, "span", "gt-i-query-mirror", { "aria-hidden": "true" });
    // (An example, in the first filter's column)
    const first = this.filters[0]?.filter as ColumnFilter;
    const input = element(doc, "input", "", {
      type: "text",
      autocomplete: "off",
      spellcheck: "false",
      autocapitalize: "off",
      enterkeyhint: "go",
      placeholder: `${formatColumn(first.column)} ${OP_SUGGESTIONS[first.type][0]?.text}`,
      role: "combobox",
      "aria-label": "Filters as text",
      "aria-autocomplete": "list",
      "aria-expanded": "false",
      "aria-controls": `${id}-list`,
    });
    const apply = this.barButton("apply", "Apply the filters", "Apply (Enter)");
    const cancel = this.barButton("clear", "Cancel", "Cancel (Esc)");
    const list = element(doc, "ul", "gt-i-query-list", {
      id: `${id}-list`,
      role: "listbox",
      "aria-label": "Suggestions",
      hidden: "",
    });
    const error = element(doc, "p", "gt-i-query-error", { id: `${id}-error`, hidden: "" });
    text.append(mirror, input);
    field.append(text, apply, cancel);
    root.append(field, list, error);
    bar.root.append(root);
    const box: QueryBox = {
      toggle,
      root,
      input,
      mirror,
      list,
      error,
      opened: "",
      suggestions: [],
      active: -1,
      context: null,
      ranges: [],
      mark: null,
    };
    bar.query = box;

    toggle.addEventListener("click", () => (root.hidden ? this.openQuery() : this.closeQuery(false)));
    apply.addEventListener("click", () => this.applyQuery(box));
    cancel.addEventListener("click", () => this.closeQuery(true));
    // (Suggestions as text is typed, not deleted)
    input.addEventListener("input", (event) =>
      this.editQuery(box, !(event as InputEvent).inputType?.startsWith("delete") && input.value.trim() !== ""),
    );
    input.addEventListener("keydown", (event) => this.queryKey(box, event));
    for (const type of ["input", "scroll", "keyup", "pointerup", "select"]) {
      input.addEventListener(type, () => {
        mirror.scrollLeft = input.scrollLeft;
      });
    }
    input.addEventListener("blur", () => this.suggest(box, false));
    // (A press on a suggestion leaves focus in the input: on the mouse's press, as WebKit makes
    // no click of a tap whose pointer press is prevented)
    list.addEventListener("mousedown", (event) => event.preventDefault());
    list.addEventListener("click", (event) => {
      const item = (event.target as Element).closest("li");
      this.takeSuggestion(box, Array.prototype.indexOf.call(list.children, item));
    });
    // Unchanged, it closes when focus leaves it (but not when the window loses it, nor to what
    // it's in, as a press in it that focuses nothing in it sends it)
    root.addEventListener("focusout", (event) => {
      const to = event.relatedTarget as Node | null;
      if (to !== null && to !== toggle && !root.contains(to) && !to.contains(root) && input.value === box.opened) {
        this.closeQuery(false);
      }
    });
  }

  // (With a part of its text selected, if it's there)
  private openQuery(select = ""): void {
    const box = this.bar?.query;
    if (box == null || !box.root.hidden) {
      return;
    }
    this.closeFilter(false);
    this.closePanel(false);
    const text = formatQuery(this.query());
    box.opened = text;
    box.input.value = text;
    box.root.hidden = false;
    box.toggle.setAttribute("aria-expanded", "true");
    this.updateTokens();
    // (Its highlights in colours for what's behind it, light or dark, as its text's is; the list, over
    // the table, filled with it)
    const [r = 0, g = 0, b = 0] = (getComputedStyle(box.root).color.match(/[\d.]+/g) ?? []).map(Number);
    box.root.toggleAttribute("data-gti-dark", 0.2126 * r + 0.7152 * g + 0.0722 * b >= 128);
    box.list.style.backgroundColor = backdropColor(this);
    this.editQuery(box, false);
    box.input.focus();
    const from = select === "" ? -1 : text.indexOf(select);
    box.input.setSelectionRange(from < 0 ? text.length : from, from < 0 ? text.length : from + select.length);
    if (from < 0) {
      // (WebKit doesn't scroll the text to its caret)
      box.input.scrollLeft = box.input.scrollWidth;
    }
    box.mirror.scrollLeft = box.input.scrollLeft;
  }

  private closeQuery(focus: boolean): void {
    const box = this.bar?.query;
    if (box == null || box.root.hidden) {
      return;
    }
    this.suggest(box, false);
    box.mark = null;
    box.input.value = "";
    this.paintQuery(box);
    box.root.hidden = true;
    box.toggle.setAttribute("aria-expanded", "false");
    this.updateTokens();
    if (focus) {
      this.orSheet(box.toggle).focus();
    }
  }

  // The text changed: what was wrong with it goes, and it's highlighted afresh (with suggestions,
  // with `suggest`)
  private editQuery(box: QueryBox, suggest: boolean): void {
    box.mark = null;
    box.error.hidden = true;
    box.input.removeAttribute("aria-invalid");
    box.input.closest(".gt-i-query-field")?.removeAttribute("data-gti-invalid");
    box.input.removeAttribute("aria-describedby");
    this.paintQuery(box);
    this.suggest(box, suggest);
  }

  private queryKey(box: QueryBox, event: KeyboardEvent): void {
    const count = box.suggestions.length;
    const { key } = event;
    if (event.altKey || event.metaKey || event.isComposing) {
      return;
    }
    if (key === "ArrowDown" || key === "ArrowUp") {
      event.preventDefault();
      if (count === 0) {
        this.suggest(box, true);
      } else {
        this.setSuggestion(box, (box.active + (key === "ArrowDown" ? 1 : count - 1)) % count);
      }
    } else if (key === " " && event.ctrlKey) {
      event.preventDefault();
      this.suggest(box, true);
    } else if ((key === "Enter" || (key === "Tab" && !event.shiftKey)) && box.active >= 0) {
      event.preventDefault();
      this.takeSuggestion(box, box.active);
    } else if (key === "Enter") {
      // (And don't submit a form the table is in)
      event.preventDefault();
      this.applyQuery(box);
    } else if (key === "Escape") {
      // Close the suggestions, then the box (and don't, say, close a dialog the table is in)
      event.preventDefault();
      event.stopPropagation();
      if (count > 0) {
        this.suggest(box, false);
      } else {
        this.closeQuery(true);
      }
    } else if (["ArrowLeft", "ArrowRight", "Home", "End"].includes(key)) {
      this.suggest(box, false);
    }
  }

  // Highlight each part of the text by what it is, and mark what's wrong, in the input's copy
  private paintQuery(box: QueryBox): void {
    for (const [highlight, range] of box.ranges) {
      highlight.delete(range);
    }
    box.ranges = [];
    const text = box.input.value;
    // (A space after it, for the caret's room at the end)
    box.mirror.textContent = `${text} `;
    const node = box.mirror.firstChild as Text;
    const mark = (name: string, from: number, to: number) => {
      const highlight = pageHighlight(`${QUERY_HIGHLIGHT}-${name}`);
      if (highlight !== undefined && from < to) {
        const range = this.ownerDocument.createRange();
        range.setStart(node, from);
        range.setEnd(node, to);
        highlight.add(range);
        box.ranges.push([highlight, range]);
      }
    };
    for (const { role, from, to } of readQuery(text).parts) {
      if (role === "keyword" || role === "string" || role === "number" || role === "literal") {
        mark(role === "literal" ? "number" : role, from, to);
      }
    }
    // (One at the end, on the space after the text)
    if (box.mark !== null) {
      mark("error", box.mark[0], Math.max(box.mark[1], box.mark[0] + 1));
    }
  }

  // Apply the text's query, or say what's wrong with it (and go to where it is)
  private applyQuery(box: QueryBox): void {
    const text = box.input.value;
    const filters = this.filters.map((control) => control.filter);
    let query: FilterQuery | null;
    let problem: { message: string; mark: [number, number] | null } | null = null;
    try {
      query = parseQuery(text);
      const found = queryProblem(filters, query);
      if (found !== null) {
        problem = { message: found.message, mark: readQuery(text).clauses[found.clause] ?? null };
      }
    } catch (err) {
      const { message, from, to } = err as QuerySyntaxError;
      // (The place is marked)
      problem = { message: message.replace(/, at (character \d+|the end)$/, ""), mark: [from, to] };
      query = null;
    }
    if (problem !== null) {
      const message = problem.message.charAt(0).toUpperCase() + problem.message.slice(1);
      box.error.textContent = message;
      box.error.hidden = false;
      box.input.setAttribute("aria-invalid", "true");
      // (For gti.css, which has no `:has()`, as it makes moving rows slow in Chromium)
      box.input.closest(".gt-i-query-field")?.setAttribute("data-gti-invalid", "");
      box.input.setAttribute("aria-describedby", box.error.id);
      box.mark = problem.mark;
      this.suggest(box, false);
      this.paintQuery(box);
      box.input.focus();
      if (problem.mark !== null) {
        box.input.setSelectionRange(problem.mark[0], problem.mark[0]);
        box.mirror.scrollLeft = box.input.scrollLeft;
      }
      this.announce(message);
      return;
    }
    this.closeQuery(true);
    this.cancelFilterTimer();
    this.userFilter(() => this.setQuery(query));
    for (const control of this.filters) {
      this.syncFilter(control);
    }
  }

  // Show the suggestions for the caret's place (or none, without `open`), the first one active
  private suggest(box: QueryBox, open: boolean): void {
    const items = open ? this.suggestions(box) : [];
    const { list, input } = box;
    box.suggestions = items;
    list.replaceChildren(
      ...items.map((item, i) => {
        const li = element(this.ownerDocument, "li", "", { id: `${list.id}-${i}`, role: "option" });
        const detail = element(this.ownerDocument, "span", "gt-i-query-detail");
        detail.textContent = item.detail;
        li.append(item.text, detail);
        return li;
      }),
    );
    list.hidden = items.length === 0;
    input.setAttribute("aria-expanded", String(items.length > 0));
    this.setSuggestion(box, items.length > 0 ? 0 : -1);
    if (items.length === 0 || box.context === null) {
      return;
    }
    // (Above the text it's for, as far as the box's width allows)
    const node = box.mirror.firstChild;
    let left = 0;
    if (node !== null) {
      const range = this.ownerDocument.createRange();
      range.setStart(node, box.context.from);
      left = range.getBoundingClientRect().left - box.root.getBoundingClientRect().left;
    }
    list.style.left = `${Math.max(0, Math.min(left, box.root.clientWidth - list.offsetWidth))}px`;
  }

  private setSuggestion(box: QueryBox, active: number): void {
    box.active = active;
    Array.from(box.list.children).forEach((li, i) => li.setAttribute("aria-selected", String(i === active)));
    const li = box.list.children[active];
    if (li === undefined) {
      box.input.removeAttribute("aria-activedescendant");
    } else {
      box.input.setAttribute("aria-activedescendant", li.id);
      li.scrollIntoView?.({ block: "nearest" });
    }
  }

  // What can go at the caret: columns (with a filter), ops (the column's filter's), values (a
  // facet's, as the table shows them, but those already chosen), bounds (a date filter's first and
  // last dates) or `and`, as far as they match
  // what's typed there (but not what's there already); and `not`, `or` and a group's `)`
  private suggestions(box: QueryBox): Suggestion[] {
    const { input } = box;
    const text = input.value;
    const caret = input.selectionStart ?? text.length;
    if (input.selectionEnd !== caret) {
      return [];
    }
    const context = queryContext(text, caret);
    box.context = context;
    const { expect, prefix } = context;
    const control = this.filters.find((c) => c.filter.column === context.col);
    const needle = fold(prefix.replace(/^[`"]|[`"]$/g, ""));
    const fits = (...texts: string[]) => texts.some((t) => fold(t).includes(needle));
    const word = prefix.toLowerCase();
    let items: Suggestion[] = [];
    if (expect === "column") {
      items = this.filters
        .filter(({ filter, label }) => fits(filter.column, label))
        .map(({ filter, label }) => {
          const name = formatColumn(filter.column);
          return { text: name, detail: label === filter.column ? "" : label, insert: `${name} `, back: 0 };
        });
      if (word !== "" && "not".startsWith(word)) {
        items.push({ text: "not", detail: "", insert: "not ", back: 0 });
      }
    } else if ((expect === "op" || expect === "negated") && control !== undefined) {
      // (And those that can be after `not`, with it, or after it)
      const ops = OP_SUGGESTIONS[control.filter.type];
      const negatable = ops.filter((item) => NEGATED.some((op) => item.insert.startsWith(`${op} `)));
      const not = (item: Suggestion) => ({ ...item, text: `not ${item.text}`, insert: `not ${item.insert}` });
      items = (expect === "op" ? [...ops, ...negatable.map(not), ...NULL_SUGGESTIONS] : negatable).filter((item) =>
        item.insert.startsWith(word),
      );
    } else if (expect === "is" || expect === "null") {
      // (What's after `is`, or after `is not`)
      const after = expect === "is" ? 3 : 7;
      items = NULL_SUGGESTIONS.slice(expect === "is" ? 0 : 1)
        .map(({ insert, detail }) => ({ text: insert.slice(after, -1), detail, insert: insert.slice(after), back: 0 }))
        .filter((item) => item.insert.startsWith(word));
    } else if (
      expect === "value" &&
      (control?.filter.type === "facet" || (control?.filter.type === "bool" && context.values.length === 0))
    ) {
      const values = control.filter.spec.values ?? [];
      const chosen = new Set(context.values.map(formatValue));
      items = (control.filter.type === "bool" ? this.boolNames(control) : this.facetNames(control))
        .map(([key, name]) => {
          const literal = key === MISSING ? "null" : formatValue(values[key] ?? null);
          return { text: name, detail: literal === JSON.stringify(name) ? "" : literal, insert: literal, back: 0 };
        })
        .filter((item) => !chosen.has(item.insert) && fits(item.text, item.insert));
    } else if (expect === "bound" && control?.filter.type === "date" && !(prefix.length > 1 && /^".*"$/s.test(prefix))) {
      // (The column's first and last dates; but not once a date's typed, its string closed, so that
      // Enter applies it)
      const names = this.facetNames(control);
      const values = control.filter.spec.values ?? [];
      items = [0, values.length - 1]
        .filter((key, i) => typeof values[key] === "string" && (i === 0 || key > 0))
        .map((key) => {
          const literal = formatValue(values[key] ?? null);
          return { text: names[key]?.[1] ?? literal, detail: literal, insert: `${literal} `, back: 0 };
        })
        .filter((item) => fits(item.text, item.detail));
    } else if (expect === "and" && (word !== "" || /\s/.test(text[caret - 1] ?? ""))) {
      items = ["and", "or"]
        .filter((keyword) => keyword.startsWith(word))
        .map((keyword) => ({ text: keyword, detail: "", insert: `${keyword} `, back: 0 }));
      if (word === "" && context.depth > 0) {
        items.push({ text: ")", detail: "", insert: ") ", back: 0 });
      }
    }
    // (Those starting with what's typed first)
    const later = (item: Suggestion) => Number(!fold(item.text).startsWith(needle));
    const there = text.slice(context.from, context.to);
    return items
      .filter((item) => item.insert.trimEnd() !== there)
      .sort((a, b) => later(a) - later(b))
      .slice(0, 50);
  }

  // Put a suggestion in place of what's typed at the caret (without a second space, before one),
  // and suggest what can go after it
  private takeSuggestion(box: QueryBox, index: number): void {
    const item = box.suggestions[index];
    const context = box.context;
    if (item === undefined || context === null) {
      return;
    }
    const { input } = box;
    const text = input.value;
    const insert = item.insert.endsWith(" ") && /^\s/.test(text.slice(context.to)) ? item.insert.trimEnd() : item.insert;
    const caret = context.from + item.insert.length - item.back;
    input.value = text.slice(0, context.from) + insert + text.slice(context.to);
    input.setSelectionRange(caret, caret);
    this.editQuery(box, true);
    box.mirror.scrollLeft = input.scrollLeft;
  }

  // The open panel's Clear button, and a facet's counts: the rows with each value that the search,
  // the other filters and the query's groups keep (so a value with none can still be chosen, but
  // is dimmed)
  private updateFilterPanel(): void {
    const control = this.openFilter;
    if (control === null) {
      return;
    }
    const { filter } = control;
    control.clear?.setAttribute("aria-disabled", String(!filter.active));
    if (control.options.length > 0) {
      const counts = new Map<number, number>();
      const others = this.activeFilters().filter((other) => other !== filter);
      this.eachKept(others, (row) => {
        const key = filter.key(row);
        counts.set(key, (counts.get(key) ?? 0) + 1);
      });
      let total = 0;
      counts.forEach((count) => (total += count));
      for (const option of control.options) {
        const count = option.key === ANY ? total : (counts.get(option.key) ?? 0);
        option.count.textContent = String(count);
        option.item.toggleAttribute("data-gti-none", count === 0);
      }
    }
    this.placeFilter();
  }

  private activeFilters(): ColumnFilter[] {
    return this.filters.map((control) => control.filter).filter((filter) => filter.active);
  }

  private clearFilters(): void {
    this.filterGroups = [];
    for (const control of this.filters) {
      control.filter.clear();
      this.syncFilter(control);
    }
  }

  // (With the columns of the query's groups, too)
  private filtersText(): string {
    const grouped = new Set(this.filterGroups.flatMap((group) => group.filters));
    const labels = this.filters
      .filter((control) => control.filter.active || grouped.has(control.filter))
      .map((control) => control.label);
    return labels.length === 0 ? "Not filtered" : `Filtered by ${labels.join(", ")}`;
  }

  // Change a filter once typing pauses (or sooner, with `flushFilter()`)
  private queueFilter(change: () => void): void {
    this.cancelFilterTimer();
    this.filterChange = change;
    this.filterTimer = setTimeout(() => this.flushFilter(), SEARCH_DELAY_MS);
  }

  private flushFilter(): void {
    const change = this.filterChange;
    this.cancelFilterTimer();
    if (change !== null) {
      this.userFilter(change);
    }
  }

  // Change the filters (or the query's groups) as the reader asked, and filter the rows by them,
  // if they changed
  private userFilter(change: () => void): void {
    const filters = this.filters.map((control) => control.filter);
    const texts = () => [
      ...filters.map((filter) => JSON.stringify(filterQuery([filter]))),
      JSON.stringify(this.filterGroups.map((group) => group.item)),
    ];
    const before = texts();
    change();
    const changed = texts().flatMap((text, i) => (text === before[i] ? [] : [i]));
    if (changed.length === 0 || this.spec === null) {
      this.updateFilters();
      return;
    }
    const query = this.query();
    this.applyFilters();
    const count = this.matchCount;
    const total = this.spec.nrows;
    this.announce(
      this.matched === null
        ? `Showing all ${plural(total)}`
        : count === 0
          ? "No matching rows"
          : `Showing ${count} of ${plural(total)}`,
    );
    this.dispatchEvent(
      new CustomEvent<FilterEventDetail>(FILTER_EVENT, {
        bubbles: true,
        composed: true,
        detail: { filter: query, count },
      }),
    );
    // (Changes to one filter can be one change to undo; to more, at once, are one of their own)
    this.dispatchView(changed.length === 1 ? `filter ${changed[0]}` : null);
  }

  private applyFilters(): void {
    this.pageValue = 1;
    this.matchRows();
    this.render();
  }

  // Show the search in its box. The bar's search is open while there's a search (and closes after
  // one, unless it has focus).
  private showSearch(): void {
    if (this.searchBox !== null) {
      this.searchBox.value = this.searchValue;
    }
    const field = this.bar?.field;
    if (field != null) {
      if (this.searchValue !== "") {
        this.openSearch(false);
      } else if (!field.contains(this.ownerDocument.activeElement)) {
        this.closeSearch(false);
      }
    }
  }

  private openSearch(focus: boolean): void {
    const bar = this.bar;
    if (bar?.field == null || bar.toggle === null) {
      return;
    }
    bar.field.hidden = false;
    bar.toggle.hidden = true;
    bar.root.setAttribute("data-gti-searching", "");
    // (The field covers the shortcuts' button)
    if (bar.keys !== null) {
      this.closePanel(false, bar.keys);
    }
    if (focus) {
      this.searchBox?.focus();
    }
  }

  // The field closes only without a search in it, so that a search in force shows
  private closeSearch(focus: boolean): void {
    const bar = this.bar;
    const input = this.searchBox;
    if (bar?.field == null || bar.toggle === null || input === null || input.value !== "") {
      return;
    }
    // (A search for nothing may be waiting on the typing to pause)
    this.cancelSearchTimer();
    this.userSearch("");
    bar.field.hidden = true;
    bar.toggle.hidden = false;
    bar.root.removeAttribute("data-gti-searching");
    if (focus) {
      this.orSheet(bar.toggle).focus();
    }
  }

  // A button in the bar, or the sheet's, if the bar is folded into that (and the button isn't shown)
  private orSheet(button: HTMLElement): HTMLElement {
    const sheet = this.bar?.sheet;
    return sheet != null && button.offsetWidth === 0 && sheet.offsetWidth > 0 ? sheet : button;
  }

  private startJump(): void {
    const bar = this.bar;
    if (bar === null) {
      return;
    }
    this.jumping = true;
    bar.jumpInput.value = String(this.page);
    bar.readout.hidden = true;
    bar.jump.hidden = false;
    bar.jumpInput.focus();
    bar.jumpInput.select();
  }

  // Back to the readout, going to the page typed (with `go`, if it's a whole number)
  private endJump(go: boolean): void {
    const bar = this.bar;
    if (bar === null || !this.jumping) {
      return;
    }
    // (Before the input is hidden, which takes its focus and so ends the jump again)
    this.jumping = false;
    const focused = bar.jump.contains(this.ownerDocument.activeElement);
    const value = bar.jumpInput.value.trim();
    bar.jump.hidden = true;
    bar.readout.hidden = false;
    if (focused) {
      bar.readout.focus();
    }
    const page = Number(value);
    if (go && value !== "" && Number.isInteger(page)) {
      this.userPage(page);
    }
  }

  // The bar shows while it has a search, filters (whose info panel says how many rows they leave),
  // an export or undo, or there are pages (or could be, in the page sizes the info panel offers); the page
  // controls, while there are pages: while the table has more rows than fit on a page, whatever
  // the search
  private updateBar(bar: Bar): void {
    const spec = this.spec as Spec;
    const size = this.size;
    const paged = size !== null && spec.nrows > size;
    bar.pages.hidden = !paged;
    bar.root.hidden =
      !this.pagesOffered() && bar.field === null && this.filters.length === 0 && bar.exporter === null && bar.undo === null;
    if (bar.root.hidden) {
      this.closePanel(false);
    }

    // A table of every row, with no height to scroll in, keeps its bar in view as it's scrolled
    // past (over the rows, so filled with what's behind them)
    const sticks = size === null && spec.layout.height === null;
    if (sticks !== bar.root.hasAttribute("data-gti-stick")) {
      bar.root.toggleAttribute("data-gti-stick", sticks);
      bar.root.style.backgroundColor = sticks ? backdropColor(this) : "";
    }
    if (bar.count !== null) {
      const searching = this.terms.length > 0;
      bar.count.hidden = !searching;
      bar.count.textContent = searching ? plural(this.matchCount) : "";
    }
    if (bar.keys !== null) {
      for (const entry of bar.keys.pageKeys) {
        entry.hidden = !paged;
      }
      bar.keys.button.hidden = bar.keys.open.hidden = Array.from(
        bar.keys.panel.querySelectorAll<HTMLElement>("dl > div"),
        (entry) => entry.hidden,
      ).every(Boolean);
      if (bar.keys.button.hidden) {
        this.closePanel(false, bar.keys);
      }
    }
    if (bar.reset !== null) {
      bar.reset.hidden = this.isAuthorView();
    }
    this.updateInfo();
    if (!paged) {
      return;
    }

    const page = this.page;
    const count = this.pageCount;
    bar.first.setAttribute("aria-disabled", String(page === 1));
    bar.previous.setAttribute("aria-disabled", String(page === 1));
    bar.next.setAttribute("aria-disabled", String(page === count));
    bar.last.setAttribute("aria-disabled", String(page === count));
    bar.readout.replaceChildren(String(page), this.slash(), String(count));
    bar.readout.setAttribute("aria-label", `Page ${page} of ${count}`);
    bar.jumpCount.replaceChildren(this.slash(), String(count));
    bar.jumpInput.setAttribute("aria-label", `Go to page (of ${count})`);
    // (Room for the most pages the rows can have, unsearched)
    bar.pages.style.setProperty("--gt-i-digits", String(String(pageCount(spec.nrows, size)).length));
  }

  private slash(): HTMLElement {
    const slash = this.ownerDocument.createElement("span");
    slash.className = "gt-i-of";
    slash.textContent = "/";
    return slash;
  }

  // Which rows are shown: "21–30 of 118 rows" (or "118 rows", without pages), and of how many
  // without the search
  private rowsText(): string {
    const { start, end, total } = this.view;
    const rows =
      total === 0 || this.size === null
        ? plural(total)
        : `${end - start > 1 ? `${start + 1}–` : ""}${end} of ${plural(total)}`;
    return this.matched === null ? rows : `${rows} (filtered from ${(this.spec as Spec).nrows})`;
  }

  // The page sizes the reader can choose from, with the size shown: the author's (with
  // `size_select`), and in the info panel the table's own too, so that it can be gone back to
  private sizeChoices(size: number): number[] {
    const spec = this.spec as Spec;
    const { size_select, page_sizes, page_size } = spec.pagination;
    if (!size_select) {
      return [size];
    }
    return pageSizeChoices(size, spec.controls.bar === true ? [...page_sizes, page_size] : page_sizes);
  }

  // Whether there are pages, or could be: whether the table has more rows than fit on a page of
  // the size shown, or the smallest the reader can choose
  private pagesOffered(): boolean {
    const size = this.size;
    return size !== null && (this.spec as Spec).nrows > Math.min(...this.sizeChoices(size));
  }

  // Put a control below the table, outside its scrolling container
  private placeBelow(el: HTMLElement): void {
    let below: Element = this.table as HTMLTableElement;
    while (below.parentElement !== null && below.parentElement !== this) {
      below = below.parentElement;
    }
    // (After the handle under the rows, which is next in the order of focus)
    (this.footHandle ?? below).after(el);
  }

  // The toolbar and page controls are lined up with the table, and the column widths are measured
  // again when the element's width changes
  private observeLayout(): void {
    if (
      this.layout !== null ||
      typeof ResizeObserver === "undefined" ||
      (this.toolbar === null &&
        this.pager === null &&
        this.bar === null &&
        this.colgroup === null &&
        this.filters.length === 0 &&
        !this.cutsText &&
        this.scroller === null)
    ) {
      return;
    }
    this.layout = new ResizeObserver(() => {
      if (this.syncStack()) {
        this.drawBorders();
      }
      this.alignBars();
      this.placeFoot();
      this.placeFilter();
      this.stick();
      // (In the next frame, like the column widths below)
      this.queuePin();
      const resized =
        (this.colgroup !== null && this.clientWidth !== this.fittedWidth) ||
        (this.drops.length > 0 && this.scroller?.clientWidth !== this.fitRoom);
      const unmeasured = !this.widthsFixed && this.needsWidths();
      if ((resized || unmeasured || this.padStale()) && this.refitFrame === 0) {
        // (In the next frame: changing the layout while it's being observed is a loop)
        this.refitFrame = requestAnimationFrame(() => {
          this.refitFrame = 0;
          this.refit();
        });
      }
    });
    this.layout.observe(this);
    if (this.table !== null) {
      this.layout.observe(this.table);
    }
    // (The column labels' height, as they wrap; the scrolling container's, as rows are hidden)
    if (this.scroller !== null) {
      this.layout.observe(this.scroller);
      const thead = this.table?.tHead;
      if (thead != null) {
        this.layout.observe(thead);
      }
    }
  }

  private alignBars(): void {
    if (this.table === null) {
      return;
    }
    const bars = [this.toolbar, this.pager?.nav].filter((bar) => bar != null);
    if (bars.length === 0 && this.bar === null) {
      return;
    }
    // (Measured without the widths and offsets they were given: in a container as wide as what's in
    // it, those would keep the element wider than the table, narrowing a frame at a time, each a
    // loop of the observer)
    for (const bar of [...bars, this.bar?.root]) {
      if (bar != null) {
        bar.style.marginLeft = bar.style.width = "";
      }
    }
    const outer = this.getBoundingClientRect();
    const table = this.table.getBoundingClientRect();
    const left = Math.max(0, table.left - outer.left);
    for (const bar of bars) {
      bar.style.marginLeft = `${left}px`;
      bar.style.width = `${Math.max(0, Math.min(table.width, outer.width - left))}px`;
    }
    // The control bar is no narrower than its controls need (where there's room), centred under a
    // narrower table
    if (this.bar !== null) {
      const width = Math.min(outer.width, Math.max(table.width, BAR_MIN_WIDTH));
      const centre = table.left - outer.left + table.width / 2;
      const at = Math.max(0, Math.min(centre - width / 2, outer.width - width));
      this.bar.root.style.marginLeft = `${at}px`;
      this.bar.root.style.width = `${width}px`;
    }
  }

  private addLiveRegion(): void {
    if (this.live !== null) {
      return;
    }
    this.live = this.ownerDocument.createElement("div");
    this.live.className = "gt-i-live";
    this.live.setAttribute("aria-live", "polite");
    this.live.setAttribute("aria-atomic", "true");
    this.append(this.live);
  }

  private userSort(keys: SortKey[]): void {
    this.sortKeys = keys;
    this.pageValue = 1;
    this.render();
    this.announce(this.sortText());
    this.dispatchEvent(
      new CustomEvent<SortEventDetail>(SORT_EVENT, {
        bubbles: true,
        composed: true,
        detail: { sort: this.sort },
      }),
    );
    this.dispatchView(null);
  }

  private userSearch(value: string): void {
    if (value === this.searchValue) {
      return;
    }
    const count = this.applySearch(value);
    if (this.spec === null) {
      return;
    }
    const total = this.spec.nrows;
    this.announce(
      this.terms.length === 0
        ? `Showing all ${plural(total)}`
        : count === 0
          ? "No matching rows"
          : `Showing ${count} of ${plural(total)}`,
    );
    this.dispatchEvent(
      new CustomEvent<SearchEventDetail>(SEARCH_EVENT, {
        bubbles: true,
        composed: true,
        detail: { search: this.searchValue, count },
      }),
    );
    this.dispatchView("search");
  }

  private userPage(page: number): void {
    const count = this.pageCount;
    page = Math.min(Math.max(1, page), count);
    if (page === this.page) {
      this.updatePager();
      return;
    }
    this.pageValue = page;
    this.render();
    this.announce(`Page ${page} of ${count}`);
    this.dispatchPage();
    this.dispatchView("page");
  }

  private userPageSize(size: number, part: string | null = null): void {
    if (size !== this.size) {
      this.resize(size);
      this.sizeChanged(part);
    }
  }

  // (A run of changes by the keys on the handle under the rows, `part` "size", is one to undo)
  private sizeChanged(part: string | null): void {
    this.announce(`${plural(this.size as number)} per page, page ${this.page} of ${this.pageCount}`);
    this.dispatchPage();
    this.dispatchView(part);
  }

  private userColumns(ids: string[], text: string): void {
    this.hideColumns(ids);
    this.matchRows();
    this.render();
    this.announce(text);
    this.dispatchView(null);
  }

  // (A reset is a change to undo)
  private userResetView(): void {
    this.showView(this.authorView as View);
    this.announce(`The view is reset: ${this.rowsText()}`);
    this.dispatchView(null);
  }

  // Undo the last change to the view (`back`), or redo it, as the reader asked
  private userTravel(back: boolean): void {
    if (back ? this.undo() : this.redo()) {
      this.announce(`${back ? "Undone" : "Redone"}: ${this.rowsText()}`);
      this.dispatchView();
    }
  }

  // (With `part`, noting the change as one to undo; see `record()`)
  private dispatchView(part?: string | null): void {
    if (part !== undefined) {
      this.record(part);
    }
    this.dispatchEvent(
      new CustomEvent<ViewEventDetail>(VIEW_EVENT, {
        bubbles: true,
        composed: true,
        detail: this.currentView(),
      }),
    );
  }

  private dispatchPage(): void {
    this.dispatchEvent(
      new CustomEvent<PageEventDetail>(PAGE_EVENT, {
        bubbles: true,
        composed: true,
        detail: { page: this.page, pageSize: this.pageSize, pageCount: this.pageCount },
      }),
    );
  }

  // A new page size keeps the first row of the page in view
  private resize(size: number | null): void {
    const old = this.size;
    const first = old === null ? 0 : (this.page - 1) * old;
    this.pageSizeValue = size;
    if (this.spec === null) {
      return;
    }
    const now = this.size;
    this.pageValue = now === null ? 1 : Math.floor(first / now) + 1;
    this.render();
  }

  /** Search, returning the number of matching data rows. */
  private applySearch(value: string): number {
    this.searchValue = value;
    this.pageValue = 1;
    this.matchRows();
    this.render();
    return this.matchCount;
  }

  // Which data rows match the search and the filters
  private matchRows(): void {
    this.terms = searchTerms(this.searchValue);
    const spec = this.spec;
    this.matched = null;
    this.matchCount = spec?.nrows ?? 0;
    const filters = this.activeFilters();
    if (
      spec === null ||
      !this.movable ||
      (this.terms.length === 0 && filters.length === 0 && this.filterGroups.length === 0)
    ) {
      return;
    }

    const matches = new Uint8Array(spec.nrows);
    let count = 0;
    this.eachKept(filters, (row) => {
      matches[row] = 1;
      count++;
    });
    this.matched = matches;
    this.matchCount = count;
  }

  // Call `each` with each data row that matches the search, `filters` and the query's groups
  private eachKept(filters: readonly ColumnFilter[], each: (row: number) => void): void {
    const nrows = (this.spec as Spec).nrows;
    const groups = this.filterGroups;
    const texts =
      this.terms.length > 0 || filters.some((filter) => filter.type === "text") || groups.some((group) => group.texts)
        ? (this.cellTexts ?? this.makeCellTexts(nrows))
        : null;
    for (let row = 0; row < nrows; row++) {
      const cells = texts?.[row] ?? [];
      if (
        (this.terms.length === 0 || rowMatches(this.searched(cells), this.terms)) &&
        filters.every((filter) => filter.keeps(row, cells[filter.index])) &&
        groups.every((group) => group.keeps(row, cells))
      ) {
        each(row);
      }
    }
  }

  private makeCellTexts(nrows: number): CellText[][] {
    const texts: CellText[][] = [];
    for (let row = 0; row < nrows; row++) {
      const tr = this.rowElements[row];
      texts.push(tr === undefined ? [] : this.dataCells(tr).map((cell) => new CellText(cell)));
    }
    this.cellTexts = texts;
    return texts;
  }

  // A data row's cells that the search looks in: not those of the columns hidden (but those dropped)
  private searched(cells: CellText[]): CellText[] {
    const { unsearched, hiddenIds } = this;
    const columns = (this.spec as Spec).columns;
    return unsearched.size === 0 && hiddenIds.length === 0
      ? cells
      : cells.filter((_, i) => !unsearched.has(i) && !hiddenIds.includes(columns[i]?.id as string));
  }

  // A data row's cells, one per column of the spec, in the spec's order: not a group's label cell,
  // which is on one of its rows only (so it isn't searched), nor the selection column's
  private dataCells(tr: HTMLTableRowElement): Element[] {
    const cells = Array.from(tr.children).filter((cell) => !cell.matches(".gt_stub_row_group, .gt-i-select"));
    const places = this.placeOf;
    if (places.length === 0) {
      return cells;
    }
    // (A row without the stub's cells merged into the row above, in a hierarchical stub, has fewer;
    // the stub's columns don't move)
    const skip = places.length - cells.length;
    return cells.map((cell, k) => cells[(places[k + skip] ?? k + skip) - skip] ?? cell);
  }

  /** Show the data rows for the current sort, search and page. */
  private render(): void {
    if (this.spec === null || this.tbody === null) {
      return;
    }
    const size = this.size;
    this.removeFillers();
    if (!this.widthsFixed && this.needsWidths()) {
      this.fixWidths();
    }
    // (Not a stacked table's, whose cards are as tall as their contents)
    const pads = size !== null && this.spec.nrows > size && !this.stacked;
    if (pads) {
      this.measurePage(size);
    }
    const { shown, page, start, total } = this.place(this.matched, size, this.pageValue);
    const before = this.view;
    this.pageValue = page;
    this.view = { start, end: start + shown.length, total };

    this.restripe(shown);
    this.showEmpty(this.matched !== null && total === 0);
    this.drawBorders();
    if (pads) {
      // (The row saying that nothing matches is one of the page's)
      this.pad(size - Math.max(1, shown.length));
    }
    // Other rows (a new page, or search results) are shown from the top
    if (this.scroller !== null && (start !== before.start || total !== before.total)) {
      this.scroller.scrollTop = 0;
    }
    this.updateSelectAll();
    this.updateSortHeaders();
    this.highlight(shown);
    this.updatePager();
    this.updateFilters();
    this.updateProfiles();
    this.placeGuide();
    this.placeFoot();
    this.saveView();
  }

  /**
   * Put the data rows in order, and show the ones that match (`matches`) and are on page `page`
   * (of `size` rows), with their groups' headings and summary rows. Returns the rows shown, the
   * page (the last, if `page` is past it), and where the page starts in the `total` rows that match.
   */
  private place(
    matches: Uint8Array | null,
    size: number | null,
    page: number,
  ): { shown: HTMLTableRowElement[]; page: number; start: number; total: number } {
    const spec = this.spec as Spec;
    const tbody = this.tbody as HTMLTableSectionElement;

    // Each block is sorted on its own, so rows stay in their group, and group headings and
    // summary rows stay where they are. Its rows are moved only when its order changes (moving
    // rows is slow in some browsers, with many of them), and then taken out in one go
    const order: number[] = [];
    for (const block of this.blocks) {
      const sorted = sortRows(block.rows, this.sortKeys, spec.ranks);
      if (sorted.some((row, i) => row !== block.placed[i])) {
        this.moveRows(tbody, block.placed, sorted);
        block.placed = sorted;
      }
      for (const row of sorted) {
        if (matches === null || matches[row] === 1) {
          order.push(row);
        }
      }
    }

    this.order = order;
    page = Math.min(page, pageCount(order.length, size));
    const start = size === null ? 0 : (page - 1) * size;
    const end = size === null ? order.length : Math.min(order.length, start + size);

    // A group's rows are together, so it starts on the page unless the row before the page is in
    // it, and ends on it unless the row after is
    const groupAt = (i: number) => this.rowGroups[order[i] as number] ?? null;
    const onPage = new Uint8Array(spec.nrows);
    const shown: HTMLTableRowElement[] = [];
    const spans = new Map<Group, Span>();
    for (let i = start; i < end; i++) {
      const row = order[i] as number;
      const tr = this.rowElements[row] as HTMLTableRowElement;
      onPage[row] = 1;
      shown.push(tr);
      const group = groupAt(i);
      if (group === null) {
        continue;
      }
      let span = spans.get(group);
      if (span === undefined) {
        span = { count: 0, first: tr, starts: i === 0 || groupAt(i - 1) !== group, ends: false };
        spans.set(group, span);
      }
      span.count++;
      span.ends = i === order.length - 1 || groupAt(i + 1) !== group;
    }

    this.rowElements.forEach((tr, row) => {
      setHidden(tr, onPage[row] !== 1);
    });
    for (const group of this.groups) {
      const span = spans.get(group);
      for (const tr of group.headings) {
        setHidden(tr, span === undefined);
      }
      for (const tr of group.top) {
        setHidden(tr, span?.starts !== true);
      }
      for (const tr of group.bottom) {
        setHidden(tr, span?.ends !== true);
      }
      this.placeGroupCell(group, span);
    }
    this.placeDetails();
    this.reinsertEdges(tbody);
    return { shown, page, start, total: order.length };
  }

  // Put each data row shown that hidden rows part from the next row shown, if that isn't a data
  // row (a group's heading or a summary row), or from the end of the body, back where it is:
  // WebKit lays out a row's collapsed borders again as it's put in, but not as the rows after it
  // are hidden or shown (so the last row on a page could be without its share of the body's
  // bottom border, and the table half a px shorter than on another page). Not those followed by
  // other data rows, whose borders are the same (as putting back many rows, one by one, is slow
  // in Chromium), nor one with what has the focus in it, which putting it back would take the
  // focus from
  private reinsertEdges(tbody: HTMLTableSectionElement): void {
    const edges: HTMLTableRowElement[] = [];
    let last: HTMLTableRowElement | null = null;
    let gap = false;
    for (let tr = tbody.firstElementChild as HTMLTableRowElement | null; ; ) {
      if (tr === null || !tr.hidden) {
        if (last !== null && gap && (tr === null || typeof this.bodyRows.get(tr) !== "number")) {
          edges.push(last);
        }
        if (tr === null) {
          break;
        }
        last = typeof this.bodyRows.get(tr) === "number" ? tr : null;
        gap = false;
      } else {
        gap = true;
      }
      tr = tr.nextElementSibling as HTMLTableRowElement | null;
    }
    const focused = this.ownerDocument.activeElement;
    for (const tr of edges) {
      if (!tr.contains(focused)) {
        tbody.insertBefore(tr, tr.nextSibling);
      }
    }
  }

  // Put a block's rows (in the body in the order `placed`) in the order `sorted`: taken out
  // together, in a range from the first to the last (with any rows of dropped columns between them,
  // which go under their rows again after), put in order out of the body, and put back
  private moveRows(tbody: HTMLTableSectionElement, placed: number[], sorted: number[]): void {
    const rows = this.rowElements;
    const last = rows[placed[placed.length - 1] as number] as HTMLTableRowElement;
    const next = last.nextSibling;
    const range = this.ownerDocument.createRange();
    range.setStartBefore(rows[placed[0] as number] as HTMLTableRowElement);
    range.setEndAfter(last);
    range.deleteContents();
    const fragment = this.ownerDocument.createDocumentFragment();
    for (const row of sorted) {
      fragment.append(rows[row] as HTMLTableRowElement);
    }
    tbody.insertBefore(fragment, next);
  }

  // The label cell of a group shown as a column goes on the group's first shown row, and spans
  // its shown rows
  private placeGroupCell(group: Group, span: Span | undefined): void {
    const cell = group.cell;
    if (cell === null || span === undefined) {
      return;
    }
    const top = span.starts ? group.top.length : 0;
    const bottom = span.ends ? group.bottom.length : 0;
    const target = (top > 0 ? group.top[0] : undefined) ?? span.first;
    if (cell.parentElement !== target) {
      const from = cell.parentElement as HTMLTableRowElement | null;
      from?.classList.remove("gt_row_group_first");
      // (After the selection column's cell)
      const lead = target.firstElementChild;
      target.insertBefore(cell, lead?.classList.contains("gt-i-select") ? lead.nextSibling : lead);
      target.classList.add("gt_row_group_first");
      // (GT's CSS gives the cells of a group's first row a border)
      if (from !== null) {
        this.borders?.forget(from);
      }
      this.borders?.forget(target);
    }
    cell.setAttribute("rowspan", String(span.count + top + bottom));
  }

  // Whether the search or paging hides data rows
  private hidesRows(): boolean {
    const size = this.size;
    return this.matchCount < (this.spec?.nrows ?? 0) || (size !== null && this.matchCount > size);
  }

  // Hiding rows would narrow columns sized to their content, so they keep the widths they have
  // with every row shown; and text that doesn't wrap would widen columns the author sized
  private needsWidths(): boolean {
    return this.cutsText || this.hidesRows();
  }

  // Fix the column widths (those the author didn't set with `cols_width()`)
  private fixWidths(): void {
    const table = this.table as HTMLTableElement;
    if (table.getClientRects().length === 0 || this.stacked) {
      // Not laid out (say, in a hidden tab), or not as a table: try again once it is
      return;
    }
    this.widthsFixed = true;
    const authored = table.querySelector<HTMLTableColElement>(":scope > colgroup");
    const widths = this.measureWidths();
    if (widths === null) {
      return;
    }
    let colgroup = authored;
    if (colgroup === null) {
      colgroup = this.ownerDocument.createElement("colgroup");
      colgroup.className = "gt-i-widths";
      for (const _ of widths.columns) {
        colgroup.append(this.ownerDocument.createElement("col"));
      }
    }
    const cols = Array.from(colgroup.children) as HTMLElement[];
    if (cols.length !== widths.columns.length || cols.some((col) => col.tagName !== "COL" || col.hasAttribute("span"))) {
      return;
    }
    this.fittedCols = cols.filter((col) => col.style.width === "");
    if (this.fittedCols.length === 0 && !this.cutsText) {
      return;
    }
    this.colgroup = colgroup;
    this.setWidths(widths);
    this.observeLayout();
    // Text in a font that hasn't loaded yet has the wrong width
    const fonts = (this.ownerDocument as Partial<Document>).fonts;
    if (fonts !== undefined && fonts.status !== "loaded") {
      fonts.ready.then(() => this.refit());
    }
  }

  // Measure the column widths again (for a new element width, or once fonts have loaded)
  private refit(): void {
    const colgroup = this.colgroup;
    // (A table that drops columns measures the widths again as it fits)
    if (this.fit() || this.startWidths !== null) {
      // The reader's widths stay
      this.render();
      return;
    }
    if (colgroup === null || this.table === null) {
      // Widths not measured yet are measured on rendering (but a table that drops columns may have
      // none to measure)
      if (this.drops.length === 0 || (!this.widthsFixed && this.needsWidths()) || this.padStale()) {
        this.render();
      }
      return;
    }
    this.remeasure();
    this.render();
  }

  // Measure the fitted widths again (leaving every row shown, for `render()`), or leave the columns
  // as they are without a row to measure them by
  private remeasure(): void {
    if (this.stacked) {
      // (Measured again once the table isn't stacked, as its width changes)
      return;
    }
    const colgroup = this.colgroup as HTMLTableColElement;
    const widths = this.measureWidths();
    if (widths !== null && widths.columns.length === colgroup.children.length) {
      this.setWidths(widths);
    } else {
      this.colgroup = null;
      this.fittedCols = [];
    }
  }

  /**
   * The width of each column with every row shown, as in the static table, from a row with a cell
   * in every column, and of the table; `null` if there isn't such a row. Leaves every row shown,
   * without our widths.
   */
  private measureWidths(): { columns: number[]; table: number } | null {
    const table = this.table as HTMLTableElement;
    for (const col of this.fittedCols) {
      col.style.removeProperty("width");
    }
    table.style.removeProperty("min-width");
    if (this.tableFitted) {
      table.style.removeProperty("width");
      this.tableFitted = false;
    }
    this.empty?.remove();
    this.removeFillers();
    // (Without the rows under rows open, which span the columns: they're shown again by `render()`)
    this.measuring = true;
    this.place(null, null, 1);
    this.measuring = false;
    const trs = Array.from((this.tbody as HTMLTableSectionElement).querySelectorAll(":scope > tr:not(.gt-i-details)"));
    const span = (cell: Element) => Number(cell.getAttribute("colspan") ?? 1);
    const columns = Math.max(0, ...trs.map((tr) => Array.from(tr.children).reduce((n, cell) => n + span(cell), 0)));
    const full = trs.find(
      (tr) => tr.children.length === columns && Array.from(tr.children).every((cell) => span(cell) === 1),
    );
    if (full === undefined || columns === 0) {
      return null;
    }
    return {
      columns: Array.from(full.children).map((cell) => cell.getBoundingClientRect().width),
      table: table.getBoundingClientRect().width,
    };
  }

  private setWidths(widths: { columns: number[]; table: number }): void {
    const colgroup = this.colgroup as HTMLTableColElement;
    const table = this.table as HTMLTableElement;
    const cols = Array.from(colgroup.children);
    for (const col of this.fittedCols) {
      col.style.width = `${widths.columns[cols.indexOf(col)]}px`;
    }
    if (!colgroup.isConnected) {
      // (A <colgroup> goes before the table's rows, after any caption)
      table.insertBefore(colgroup, table.querySelector(":scope > thead, :scope > tbody"));
    }
    // Without text wrapping, a column the author sized is as wide as its text, unless the table's
    // layout is fixed, which takes a table width (GT sets one only if every column is sized)
    const overrun = cols.some(
      (col, i) =>
        !this.fittedCols.includes(col as HTMLElement) &&
        (widths.columns[i] ?? 0) > authoredWidth(col as HTMLElement, widths.table) + 1,
    );
    if (this.cutsText && overrun) {
      // (As wide as its columns, as in `freezeWidths()`)
      table.style.width = "0";
      this.tableFitted = true;
    } else {
      // Column widths alone let a table that overflows its container shrink to fit it
      table.style.minWidth = `${widths.table}px`;
    }
    this.fittedWidth = this.clientWidth;
    this.hideCols();
  }

  // Alternate shown data rows (counted through the page's body, as GT counts through the table's)
  // are striped
  private restripe(trs: HTMLTableRowElement[]): void {
    const { stub, body } = (this.spec as Spec).striping;
    if (!stub && !body) {
      return;
    }
    trs.forEach((tr, j) => {
      const odd = j % 2 === 1;
      for (const cell of tr.children) {
        if (cell.tagName === "TD" ? body : stub && cell.classList.contains("gt_stub")) {
          cell.classList.toggle("gt_striped", odd);
        }
      }
    });
  }

  // A row saying that nothing matches, where the data rows would be: before the grand summary
  // rows at the bottom (it isn't a body row, since rows were mapped on hydration)
  private showEmpty(show: boolean): void {
    if (!show) {
      this.empty?.remove();
      return;
    }
    const tbody = this.tbody as HTMLTableSectionElement;
    if (this.empty === null) {
      const doc = this.ownerDocument;
      this.empty = doc.createElement("tr");
      this.empty.className = "gt-i-empty";
      const td = doc.createElement("td");
      td.className = "gt_row gt_center";
      td.colSpan = this.emptySpan();
      td.textContent = "No matching rows";
      this.empty.append(td);
      if (this.table?.hasAttribute("role")) {
        addRowRoles(this.empty);
      }
      // (Kept in view, like the rows across the table, once it's been wider than its container)
      this.inView?.push(keepInView(td));
    }
    if (this.empty.parentNode === null) {
      tbody.insertBefore(this.empty, this.grandBottom());
    }
  }

  // The columns the row saying that nothing matches spans: those shown
  private emptySpan(): number {
    const width = Math.max(
      1,
      ...this.rowElements.map((tr) =>
        Array.from(tr.children).reduce((sum, cell) => sum + Number(cell.getAttribute("colspan") ?? 1), 0),
      ),
    );
    return Math.max(1, width - this.hiddenGrid.size);
  }

  // The first of the grand summary rows at the bottom, which the rows we add to the body go before
  private grandBottom(): HTMLTableRowElement | null {
    const tbody = this.tbody as HTMLTableSectionElement;
    const grand = Array.from(tbody.querySelectorAll<HTMLTableRowElement>(":scope > tr")).find((tr) => {
      const entry = this.bodyRows.get(tr);
      return typeof entry === "object" && "grand_summary" in entry && entry.side === "bottom";
    });
    return grand ?? null;
  }

  // What the body's height on a full page depends on: the page size and the table's width (as
  // text wraps); empty if the table isn't laid out
  private padKeyNow(size: number): string {
    const table = this.table;
    return table === null || table.getClientRects().length === 0
      ? ""
      : `${size} ${Math.round(table.getBoundingClientRect().width)}`;
  }

  // Whether short pages are padded to a height measured at another page size or table width (or
  // not measured, as the table wasn't laid out); not while a column is being resized
  private padStale(): boolean {
    const size = this.size;
    return (
      size !== null &&
      (this.spec?.nrows ?? 0) > size &&
      !this.stacked &&
      this.padKey !== this.padKeyNow(size) &&
      !this.hasAttribute("data-gti-resizing")
    );
  }

  /**
   * Measure the body's height on the first page of every row, which shorter pages are padded to,
   * and the average height of its data rows; again for each page size and table width.
   */
  private measurePage(size: number): void {
    const key = this.padKeyNow(size);
    if (key === this.padKey) {
      return;
    }
    this.padKey = key;
    this.padHeight = 0;
    this.rowHeight = 0;
    if (key === "") {
      // Not laid out (say, in a hidden tab): measured once it is
      return;
    }
    this.empty?.remove();
    // (Without the rows under rows open, as a page with some is as much taller as they are)
    this.measuring = true;
    const { shown } = this.place(null, size, 1);
    this.measuring = false;
    this.borders?.redraw();
    this.padHeight = this.bodyHeight();
    const heights = shown.map((tr) => tr.getBoundingClientRect().height);
    this.rowHeight = heights.length === 0 ? 0 : heights.reduce((a, b) => a + b, 0) / heights.length;
  }

  // The body's height, but for the rows under rows open
  private bodyHeight(): number {
    let height = (this.tbody as HTMLTableSectionElement).getBoundingClientRect().height;
    for (const details of this.details.values()) {
      if (!details.hidden && details.isConnected) {
        height -= details.getBoundingClientRect().height;
      }
    }
    return height;
  }

  /**
   * Pad a short page (the last, or a search's) with up to `room` empty rows, so that the body is
   * as tall as on a full page (the first, or the tallest seen since): the table keeps its height
   * from page to page. Each is about a data row's height, the last making up the difference.
   */
  private pad(room: number): void {
    if (this.padKey === "" || this.rowHeight <= 0) {
      return;
    }
    const height = this.bodyHeight();
    this.padHeight = Math.max(this.padHeight, height);
    const short = this.padHeight - height;
    const count = Math.min(room, Math.round(short / this.rowHeight));
    if (count <= 0) {
      return;
    }
    const tbody = this.tbody as HTMLTableSectionElement;
    const anchor = this.grandBottom();
    const fillers = this.fillers.slice(0, count);
    while (fillers.length < count) {
      fillers.push(this.makeFiller());
    }
    for (const tr of fillers) {
      tr.style.height = `${short / count}px`;
      tbody.insertBefore(tr, anchor);
    }
    // (Their borders, and their pinned cells)
    this.drawBorders();
    const last = fillers[count - 1] as HTMLTableRowElement;
    const off = this.padHeight - this.bodyHeight();
    if (Math.abs(off) > 0.01) {
      last.style.height = `${Math.max(0, short / count + off)}px`;
    }
  }

  private removeFillers(): void {
    for (const tr of this.fillers) {
      tr.remove();
    }
  }

  // A row padding a page: an empty cell in each column, for the lines between them, without a
  // data row's text, stripes or styles; not a body row, and hidden from screen readers
  private makeFiller(): HTMLTableRowElement {
    const doc = this.ownerDocument;
    const tr = doc.createElement("tr");
    tr.className = "gt-i-filler";
    tr.setAttribute("aria-hidden", "true");
    if (this.fillerCells === null) {
      this.fillerCells = this.columnClasses();
    }
    for (const classes of this.fillerCells) {
      const td = doc.createElement("td");
      td.className = classes;
      tr.append(td);
    }
    this.fillers.push(tr);
    return tr;
  }

  // Per column, the classes a filler row's cell takes from a data row's cell in it: whether it's
  // in the stub or the row group column (which have their own borders), and whether it's pinned
  private columnClasses(): string[] {
    const tbody = this.tbody as HTMLTableSectionElement;
    const isData = (tr: HTMLTableRowElement) => typeof this.bodyRows.get(tr) === "number";
    const all = Array.from(tbody.querySelectorAll<HTMLTableRowElement>(":scope > tr"));
    const shownRows = all.filter((tr) => !tr.hidden);
    // (Or, with none shown, any data row: one in every column, with the label cell of its group)
    const rows = shownRows.some(isData) ? shownRows : all;
    const { grid, columns } = placeCells(rows);
    const filled = (line: unknown[]) => line.filter((p) => p !== undefined).length;
    let best: ReturnType<typeof placeCells>["grid"][number] = [];
    rows.forEach((tr, r) => {
      const line = grid[r] ?? [];
      if (isData(tr) && filled(line) > filled(best)) {
        best = line;
      }
    });
    return Array.from({ length: columns }, (_, c) => {
      const cell = best[c]?.cell;
      const kept = FILLER_CLASSES.filter((name) => cell?.classList.contains(name) === true);
      return ["gt_row", ...kept].join(" ");
    });
  }

  // The page controls are shown while there are pages: while the table has more rows than fit on a
  // page (of the smallest size the reader can choose), whatever the search
  private updatePager(): void {
    const spec = this.spec as Spec;
    const size = this.size;
    if (spec.controls.bar === true) {
      // (A bar without a search comes with the pages, or the page sizes)
      if (this.bar !== null || this.pagesOffered()) {
        this.updateBar(this.bar ?? this.addBar());
      }
      return;
    }
    if (size === null || !this.pagesOffered()) {
      if (this.pager !== null) {
        this.pager.nav.hidden = true;
      }
      return;
    }
    const pager = this.pager ?? this.addPager();
    pager.nav.hidden = false;

    const page = this.page;
    const count = this.pageCount;
    if (pager.info !== null) {
      pager.info.textContent = this.rowsText();
    }
    if (pager.select !== null) {
      const choices = this.sizeChoices(size).map(String);
      if (Array.from(pager.select.options, (option) => option.value).join() !== choices.join()) {
        pager.select.replaceChildren(
          ...choices.map((choice) => {
            const option = this.ownerDocument.createElement("option");
            option.value = option.textContent = choice;
            return option;
          }),
        );
      }
      pager.select.value = String(size);
    }

    const { first, previous, next, last } = pager.buttons;
    for (const button of [first, previous]) {
      button?.setAttribute("aria-disabled", String(page === 1));
    }
    for (const button of [next, last]) {
      button?.setAttribute("aria-disabled", String(page === count));
    }
    if (pager.numbers !== null) {
      this.updatePageNumbers(pager.numbers, page, count);
    }
    if (pager.status !== null) {
      pager.status.textContent = `Page ${page} of ${count}`;
    }
    if (pager.jump !== null && pager.jumpCount !== null) {
      pager.jump.value = String(page);
      pager.jumpCount.textContent = ` of ${count}`;
    }
  }

  private updatePageNumbers(numbers: HTMLElement, page: number, count: number): void {
    const key = `${page}/${count}`;
    if (numbers.dataset.gtiPages === key) {
      return;
    }
    numbers.dataset.gtiPages = key;
    // A page number keeps focus as it's replaced: the new page's has it
    const active = this.ownerDocument.activeElement;
    const focused = active !== null && numbers.contains(active);
    numbers.replaceChildren(
      ...pageItems(page, count).map((item) => {
        if (item === null) {
          const gap = this.ownerDocument.createElement("span");
          gap.className = "gt-i-page-gap";
          gap.setAttribute("aria-hidden", "true");
          gap.textContent = "…";
          return gap;
        }
        const button = this.pageButton(String(item), String(item));
        button.setAttribute("aria-label", `Page ${item}`);
        if (item === page) {
          button.setAttribute("aria-current", "page");
        }
        return button;
      }),
    );
    if (focused) {
      numbers.querySelector<HTMLButtonElement>('[aria-current="page"]')?.focus();
    }
  }

  private pageButton(target: string, text: string): HTMLButtonElement {
    const button = this.ownerDocument.createElement("button");
    button.type = "button";
    button.className = "gt-i-page";
    button.dataset.gtiPage = target;
    button.textContent = text;
    return button;
  }

  private addPager(): Pager {
    const doc = this.ownerDocument;
    const table = this.table as HTMLTableElement;
    const { type, info, size_select } = (this.spec as Spec).pagination;
    const nav = doc.createElement("nav");
    nav.className = "gt-i-pager";
    nav.setAttribute("aria-label", "Table pages");
    const pager: Pager = {
      nav,
      info: null,
      select: null,
      buttons: {},
      numbers: null,
      status: null,
      jump: null,
      jumpCount: null,
    };

    if (info) {
      pager.info = doc.createElement("span");
      pager.info.className = "gt-i-page-info";
      nav.append(pager.info);
    }
    if (size_select) {
      const label = doc.createElement("label");
      label.className = "gt-i-page-size";
      const select = doc.createElement("select");
      label.append("Rows per page ", select);
      nav.append(label);
      select.addEventListener("change", () => this.userPageSize(Number(select.value)));
      pager.select = select;
    }

    const controls = doc.createElement("div");
    controls.className = "gt-i-pages";
    const add = (name: PagerButton) => {
      const button = this.pageButton(name, PAGER_BUTTONS[name]);
      pager.buttons[name] = button;
      controls.append(button);
    };
    if (type === "full") {
      add("first");
    }
    add("previous");
    if (type === "numbers") {
      pager.numbers = doc.createElement("span");
      pager.numbers.className = "gt-i-page-numbers";
      controls.append(pager.numbers);
    } else if (type === "jump") {
      const label = doc.createElement("label");
      label.className = "gt-i-page-jump";
      const input = doc.createElement("input");
      input.type = "text";
      input.inputMode = "numeric";
      input.autocomplete = "off";
      input.setAttribute("enterkeyhint", "go");
      pager.jumpCount = doc.createElement("span");
      label.append("Page ", input, pager.jumpCount);
      controls.append(label);
      const go = () => {
        const page = Number(input.value.trim());
        if (input.value.trim() !== "" && Number.isInteger(page)) {
          this.userPage(page);
        } else {
          input.value = String(this.page);
        }
      };
      input.addEventListener("change", go);
      input.addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
          // (And don't submit a form the table is in)
          event.preventDefault();
          go();
        }
      });
      pager.jump = input;
    } else {
      pager.status = doc.createElement("span");
      pager.status.className = "gt-i-page-status";
      controls.append(pager.status);
    }
    add("next");
    if (type === "full") {
      add("last");
    }
    nav.append(controls);

    nav.addEventListener("click", (event) => {
      const button = (event.target as Element).closest<HTMLButtonElement>("button[data-gti-page]");
      if (button === null || button.getAttribute("aria-disabled") === "true") {
        return;
      }
      const target = button.dataset.gtiPage;
      const page = this.page;
      this.userPage(
        target === "first"
          ? 1
          : target === "previous"
            ? page - 1
            : target === "next"
              ? page + 1
              : target === "last"
                ? this.pageCount
                : Number(target),
      );
    });
    nav.addEventListener("keydown", (event) => {
      if ((event.key === "PageUp" || event.key === "PageDown") && !(event.target instanceof HTMLSelectElement)) {
        event.preventDefault();
        this.userPage(this.page + (event.key === "PageUp" ? -1 : 1));
      }
    });

    // Below the table, outside its scrolling container, in the table's font
    this.placeBelow(nav);
    nav.style.fontFamily = getComputedStyle(table).fontFamily;
    this.pager = pager;
    this.addLiveRegion();
    this.observeLayout();
    this.alignBars();
    return pager;
  }

  private highlight(shown: HTMLTableRowElement[]): void {
    // (Each table adds its ranges to the one highlight of the page)
    const highlight = pageHighlight(SEARCH_HIGHLIGHT);
    if (highlight === undefined) {
      return;
    }
    for (const range of this.ranges) {
      highlight.delete(range);
    }
    this.ranges = [];
    // The search's terms, in every cell it looks in, and a text filter's, in its column's
    const texts = this.activeFilters().filter((filter) => filter.type === "text");
    if ((this.terms.length === 0 && texts.length === 0) || this.cellTexts === null) {
      return;
    }
    // (Ranges are made afresh, since moving rows collapses live ranges in them)
    for (const tr of shown) {
      const row = this.bodyRows.get(tr) as number;
      const cells = this.cellTexts[row] ?? [];
      const found = this.searched(cells).flatMap((cell) => cell.find(this.terms));
      for (const filter of texts) {
        found.push(...(cells[filter.index]?.find([filter.needle]) ?? []));
      }
      for (const { startNode, startOffset, endNode, endOffset } of found) {
        const range = this.ownerDocument.createRange();
        range.setStart(startNode, startOffset);
        range.setEnd(endNode, endOffset);
        highlight.add(range);
        this.ranges.push(range);
      }
    }
  }

  private updateSortHeaders(): void {
    const multiple = this.sortKeys.length > 1;
    for (const [column, { th, icon }] of this.sortHeaders) {
      const index = this.sortKeys.findIndex((key) => key.column === column);
      const key = this.sortKeys[index];
      if (key === undefined) {
        th.removeAttribute("aria-sort");
        th.removeAttribute("data-gti-sort");
        icon.removeAttribute("data-gti-sort-index");
        continue;
      }
      const direction = key.descending ? "descending" : "ascending";
      th.setAttribute("data-gti-sort", direction);
      // Only the main sort column is marked for assistive technology (one at a time, as ARIA
      // advises); the announcement gives the rest
      if (index === 0) {
        th.setAttribute("aria-sort", direction);
      } else {
        th.removeAttribute("aria-sort");
      }
      if (multiple) {
        icon.setAttribute("data-gti-sort-index", String(index + 1));
      } else {
        icon.removeAttribute("data-gti-sort-index");
      }
    }
  }

  private sortText(): string {
    const parts = this.sortKeys.map((key) => {
      const label = this.sortHeaders.get(key.column)?.label ?? this.unsortedLabels.get(key.column) ?? key.column;
      return `${label}, ${key.descending ? "descending" : "ascending"}`;
    });
    return parts.length === 0 ? "Not sorted" : `Sorted by ${parts.join(", then ")}`;
  }

  private announce(text: string): void {
    if (this.live !== null) {
      this.live.textContent = text;
    }
  }

  private cancelSearchTimer(): void {
    if (this.searchTimer !== null) {
      clearTimeout(this.searchTimer);
      this.searchTimer = null;
    }
  }

  private cancelFilterTimer(): void {
    if (this.filterTimer !== null) {
      clearTimeout(this.filterTimer);
      this.filterTimer = null;
    }
    this.filterChange = null;
  }

  private cancelRefit(): void {
    if (this.refitFrame !== 0) {
      cancelAnimationFrame(this.refitFrame);
      this.refitFrame = 0;
    }
  }

  private reset(): void {
    this.stopObserving();
    this.cancelSearchTimer();
    this.cancelFilterTimer();
    this.closeFilter(false);
    for (const control of this.filters) {
      control.panel?.remove();
    }
    this.cancelRefit();
    this.cancelShades();
    this.cancelPin();
    this.layout?.disconnect();
    this.highlightClear();
    this.live?.remove();
    for (const shade of Object.values(this.shades)) {
      shade.remove();
    }
    this.guide?.remove();
    this.footHandle?.remove();
    this.hint?.remove();
    this.toolbar?.remove();
    this.pager?.nav.remove();
    this.closePanel(false);
    this.closeQuery(false);
    this.bar?.root.remove();
    this.sheet?.remove();
    this.sheet = null;
    if (this.slashKey !== null) {
      this.removeEventListener("keydown", this.slashKey);
    }
    if (this.undoKey !== null) {
      this.removeEventListener("keydown", this.undoKey);
    }
    this.table = null;
    this.spec = null;
    this.tbody = null;
    this.rowElements = [];
    this.bodyRows = new WeakMap();
    this.blocks = [];
    this.groups = [];
    this.rowGroups = [];
    this.movable = false;
    this.sortKeys = [];
    this.sortHeaders = new Map();
    this.unsortedLabels = new Map();
    this.searchValue = "";
    this.terms = [];
    this.matched = null;
    this.matchCount = 0;
    this.profileViews = [];
    this.profiled = undefined;
    this.filters = [];
    this.filterGroups = [];
    this.groupTokens = new Map();
    this.pageValue = 1;
    this.pageSizeValue = undefined;
    this.authorView = null;
    this.keeper = null;
    this.keptText = null;
    this.undoable = false;
    this.past = [];
    this.future = [];
    this.present = null;
    this.lastPart = null;
    this.undoKey = null;
    this.hideable = [];
    this.hiddenIds = [];
    this.hiddenGrid = new Set();
    this.columnCells = [];
    this.hiddenWidths = new Map();
    this.drops = [];
    this.dropped = [];
    this.dropNeeds = [];
    this.fitRoom = -1;
    for (const details of this.details.values()) {
      details.remove();
    }
    this.expanders = new Map();
    this.opened = new Set();
    this.details = new Map();
    this.contents = new Map();
    this.expanding = false;
    this.pointer = "";
    this.measuring = false;
    this.runs = [];
    this.columnAt = [];
    this.placeOf = [];
    this.runCells = [];
    this.dragging = null;
    this.view = { start: 0, end: 0, total: 0 };
    this.pager = null;
    this.bar = null;
    this.slashKey = null;
    if (this.ownTabIndex) {
      this.removeAttribute("tabindex");
      this.ownTabIndex = false;
    }
    this.jumping = false;
    this.colgroup = null;
    this.fittedCols = [];
    this.widthsFixed = false;
    this.cutsText = false;
    this.tableFitted = false;
    this.fittedWidth = 0;
    this.resizers = [];
    this.guide = null;
    this.footHandle = null;
    this.heightValue = null;
    this.guideTh = null;
    this.guideBefore = null;
    this.startWidths = null;
    this.cellTexts = null;
    this.unsearched = new Set();
    this.searchBox = null;
    this.toolbar = null;
    this.layout = null;
    this.empty = null;
    this.removeFillers();
    this.fillers = [];
    this.fillerCells = null;
    this.padKey = "";
    this.padHeight = 0;
    this.rowHeight = 0;
    this.live = null;
    this.marked = null;
    this.touched = false;
    this.selected = new Set();
    this.selectColumn = false;
    this.selectBoxes = [];
    this.selectAll = null;
    this.selectAnchor = null;
    this.order = [];
    this.scroller = null;
    this.borders = null;
    this.stuckTop = [];
    this.stuckBottom = [];
    this.foot = 0;
    this.scrollsDown = false;
    this.shades = {};
    this.responsive = null;
    this.stacked = false;
    this.pinColumns = 0;
    this.stubColumns = 0;
    this.endColumns = 0;
    this.gridColumns = 0;
    this.edgeCell = null;
    this.endEdge = null;
    this.acrossCells = [];
    this.inView = null;
    this.hint = null;
    this.hinted = false;
    this.regioned = false;
    this.removeAttribute("data-gti-highlight");
    this.removeAttribute("data-gti-nowrap");
    this.removeAttribute("data-gti-resizing");
    this.removeAttribute("data-gti-scroll");
    this.removeAttribute("data-gti-sheet");
    this.removeAttribute("data-gti-sticky");
    this.removeAttribute("data-gti-wide");
    this.removeAttribute("data-gti-stacked");
    this.removeAttribute("data-gti-dropped");
    this.style.removeProperty("--gt-i-height");
    this.style.removeProperty("--gt-i-head");
    this.style.removeProperty("--gt-i-pad");
    this.removeAttribute("data-gti-state");
  }

  private highlightClear(): void {
    const highlight = typeof CSS !== "undefined" ? CSS.highlights?.get(SEARCH_HIGHLIGHT) : undefined;
    for (const range of this.ranges) {
      highlight?.delete(range);
    }
    this.ranges = [];
  }

  private setState(state: State): void {
    this.setAttribute("data-gti-state", state);
  }

  private stopObserving(): void {
    this.observer?.disconnect();
    this.observer = null;
  }
}

/**
 * Register `<gt-table>` unless it already is, and return the class in use.
 *
 * The runtime can be inlined into every notebook output or document, so it may run more than once
 * on a page; the first registration wins (`customElements.define()` throws on a second one).
 */
export function define(registry: CustomElementRegistry = customElements): CustomElementConstructor {
  const existing = registry.get(TAG_NAME);
  if (existing !== undefined) {
    return existing;
  }
  registry.define(TAG_NAME, GtTable);
  return GtTable;
}
