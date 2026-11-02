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

import { placeCells, type Side, TableBorders } from "./borders";
import { ColumnFilter, type FilterQuery, filterQuery, MISSING, setFilterQuery } from "./filter";
import { pageCount, pageItems, pageSizeChoices } from "./paging";
import { CellText, rowMatches, searchTerms } from "./search";
import { normalizeSort, type SortKey, type SortKeyInit, sortRows, toggleSort } from "./sort";
import {
  type BodyRow,
  parseSpec,
  type ResponsiveMode,
  type SelectionMode,
  type Spec,
  SpecError,
  type ViewSpec,
} from "./spec";

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

/** The name of the search highlight, for styling with `::highlight(gt-i-search)`. */
export const SEARCH_HIGHLIGHT = "gt-i-search";

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

export interface PageEventDetail {
  /** The page shown, from 1. */
  page: number;
  pageSize: number | null;
  pageCount: number;
}

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

/** A column's filter, and its button in the column label, which opens its panel (a disclosure). */
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
  /** A facet's values: their checkboxes, and the number of rows each would have. */
  options: FacetOption[];
}

interface FacetOption {
  key: number;
  item: HTMLElement;
  box: HTMLInputElement;
  count: HTMLElement;
}

// Header content that can't go inside a <button>
const INTERACTIVE = "a[href], button, input, select, textarea, details, [tabindex]";

// Whether a click in a row was on something of the row's own (a link, a checkbox), or on a group's
// label cell (not the container the table scrolls in, which can have focus)
const onOwnControl = (target: Element, tr: HTMLTableRowElement) => {
  const hit = target.closest(`${INTERACTIVE}, .gt_stub_row_group`);
  return hit !== null && tr.contains(hit);
};

// The classes of a data row's cells that the cells of the rows padding a page take
const FILLER_CLASSES = ["gt_stub", "gt_stub_row_group", "gt-i-select", "gt-i-pinned"];

// How far a resize handle's arrow keys move it, in px (and with Shift)
const RESIZE_STEP = 10;
const RESIZE_STEP_LARGE = 50;

// How long typing pauses before the search runs
const SEARCH_DELAY_MS = 150;

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
 * inline start, and arrows either side of the page and page count on the inline end.
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
  pages: HTMLElement;
  previous: HTMLButtonElement;
  next: HTMLButtonElement;
  /** The page and page count ("3/12"), which a click makes an input for the page to go to. */
  readout: HTMLButtonElement;
  jump: HTMLElement;
  jumpInput: HTMLInputElement;
  jumpCount: HTMLElement;
  info: Info;
}

/**
 * The info panel, which the bar's (i) button opens above the bar: which rows are shown, the page
 * size, the sort and the selection (each with a way to change it, where the table has one), and
 * the keys the table answers to.
 */
interface Info {
  button: HTMLButtonElement;
  panel: HTMLElement;
  /** Which rows are shown ("21–30 of 118 rows"). */
  rows: HTMLElement;
  /** The page size select, and the item it's in (with `size_select`). */
  size: HTMLElement | null;
  select: HTMLSelectElement | null;
  /** The sort, and the button that resets it (with sorting). */
  sort: HTMLElement | null;
  sortText: HTMLElement | null;
  sortReset: HTMLButtonElement | null;
  /** The filters, and the button that clears them (with filters). */
  filters: HTMLElement | null;
  filtersText: HTMLElement | null;
  filtersClear: HTMLButtonElement | null;
  /** The selection, and the button that clears it (with selection). */
  selection: HTMLElement | null;
  selectionText: HTMLElement | null;
  selectionClear: HTMLButtonElement | null;
  /** The keys the table answers to, of which those for paging are listed while there are pages. */
  keys: HTMLElement | null;
  pageKeys: HTMLElement[];
}

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
  clear: "M6 6l12 12M18 6 6 18",
  info: "M3 12a9 9 0 1 0 18 0a9 9 0 1 0-18 0M12 11v5M12 7.5v.01",
  filter: "M4 5h16l-6 7.5V18l-4 2v-7.5z",
};

// What can have text typed into it, where `/` is a character rather than the search's key
const TYPED = 'input:not([type="checkbox"]):not([type="radio"]), textarea, select, [contenteditable]';

/** A cell's text, for announcements: without footnote marks. */
function labelText(cell: Element): string {
  const copy = cell.cloneNode(true) as Element;
  for (const mark of copy.querySelectorAll(".gt_footnote_marks")) {
    mark.remove();
  }
  return (copy.textContent ?? "").replace(/\s+/g, " ").trim();
}

const plural = (n: number) => `${n} ${n === 1 ? "row" : "rows"}`;

const isPositiveInteger = (x: unknown): x is number => Number.isInteger(x) && (x as number) > 0;

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

// Wrap a cell's contents in the box that keeps them in view as the table scrolls sideways
function keepInView(cell: HTMLTableCellElement): HTMLElement {
  const div = cell.ownerDocument.createElement("div");
  div.className = "gt-i-inview";
  div.append(...Array.from(cell.childNodes));
  cell.append(div);
  return div;
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
  private searchValue = "";
  private terms: string[] = [];
  /** Per data row, whether it matches the search and the filters; `null` without any. */
  private matched: Uint8Array | null = null;
  /** The number of data rows that match the search and the filters (all of them, without any). */
  private matchCount = 0;
  /** The columns' filters, in column order. */
  private filters: FilterControl[] = [];
  /** The filter whose panel is open, and the page's handlers for a press outside it and for scrolling. */
  private openFilter: FilterControl | null = null;
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
  /** Whether the bar's readout is an input for the page to go to. */
  private jumping = false;
  /** The page's handler for a press outside the open info panel, which closes it. */
  private outsidePress: ((event: PointerEvent) => void) | null = null;
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
  /** The number of columns pinned at the table's inline start (the selection column and the stub). */
  private pinColumns = 0;
  /** A pinned cell along the pinned columns' inline end, which the shadow over the columns past them is placed by. */
  private edgeCell: HTMLTableCellElement | null = null;
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
    if (this.searchBox !== null) {
      this.searchBox.value = this.searchValue;
    }
    // The bar's search is open while there's a search (and closes after one, unless it has focus)
    const field = this.bar?.field;
    if (field != null) {
      if (this.searchValue !== "") {
        this.openSearch(false);
      } else if (!field.contains(this.ownerDocument.activeElement)) {
        this.closeSearch(false);
      }
    }
  }

  /** The columns the table can be filtered by (see `filter`). Empty until hydrated. */
  get filterableColumns(): string[] {
    return this.filters.map((control) => control.filter.column);
  }

  /**
   * The filters, as a query: `{and: [clauses]}`, with a clause `{col, op, value}` for each filter
   * on a column (two for a range with both bounds), or `null` without any. Rows are shown that
   * every clause, and the search, keep. A clause's `op` is "contains", for a text filter (`value`
   * is the text, matched as the search matches it); "in", for a facet (`value` is the values to
   * keep, `null` for a missing one); or "gte" or "lte", for a range (`value` is the bound).
   *
   * @throws {RangeError} for a query that isn't `{and: [...]}`, or with a clause on a column that
   *   isn't one of `filterableColumns`, or that the column's filter can't have (an "in" without
   *   values, or a second clause with the same `op` on a column, too).
   */
  get filter(): FilterQuery | null {
    return filterQuery(this.filters.map((control) => control.filter));
  }

  set filter(query: FilterQuery | null) {
    this.cancelFilterTimer();
    setFilterQuery(
      this.filters.map((control) => control.filter),
      query,
    );
    for (const control of this.filters) {
      this.syncFilter(control);
    }
    this.applyFilters();
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
    this.closeInfo(false);
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

    const script = this.querySelector<HTMLScriptElement>(
      ':scope > script[type="application/json"][data-gti-spec]',
    );
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
    this.order = spec.body.filter((entry): entry is number => typeof entry === "number");
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
    if (this.movable && spec.controls.sorting) {
      this.addSortHeaders(table, spec);
    }
    if (this.movable && (spec.filters?.length ?? 0) > 0) {
      this.addFilters(table, spec);
    }
    const bar = spec.controls.bar === true;
    if (this.movable && spec.controls.search && !bar) {
      this.addSearchBox(table);
    }
    if (spec.controls.resizing) {
      this.addResizers(table);
    }
    if (this.pageSizeValue === undefined) {
      this.pageSizeValue = spec.pagination.enabled ? spec.pagination.page_size : null;
    }
    // (With pages only, the bar comes with them)
    if (this.movable && (spec.controls.search || this.filters.length > 0) && bar) {
      this.addBar();
    }
    if (this.movable && spec.view !== undefined) {
      this.applySpecView(spec, spec.view);
    }
    // A search or page set before hydration applies now
    this.matchRows();
    if (this.matched !== null || this.size !== null || this.sortKeys.length > 0) {
      this.render();
    } else {
      // (Not rendered, so every row is shown, as it was)
      this.view = { start: 0, end: spec.nrows, total: spec.nrows };
      if (this.bar !== null) {
        this.updateBar(this.bar);
      }
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
      setFilterQuery(
        this.filters.map((control) => control.filter),
        view.filter as FilterQuery | null,
      );
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
        block = { rows: [], anchor: null, group };
        blocks.push(block);
        open.push(block);
      }
      block.rows.push(entry);
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
    const { height, responsive } = spec.layout;
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
      this.addPinning(table, responsive);
    }
    if (height !== null) {
      this.addScroll(table);
    }
    this.drawBorders();
    this.observeLayout();
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
   * row group column), and the cells across the table, whose contents stay in view.
   */
  private addPinning(table: HTMLTableElement, mode: ResponsiveMode): void {
    this.responsive = mode;
    // (Every row is shown on hydration)
    const { placed } = placeCells(Array.from(table.rows));
    const tbody = this.tbody;
    const stub = placed.filter(
      (p) =>
        p.cell.parentElement?.parentElement === tbody &&
        p.cell.matches(".gt_stub, .gt_stub_row_group, .gt-i-select"),
    );
    const columns = Math.max(0, ...stub.map((p) => p.c1 + 1));
    for (const p of placed) {
      if (p.c1 < columns && p.cell.parentElement?.parentElement?.tagName !== "TFOOT") {
        p.cell.classList.add("gt-i-pinned");
      }
    }
    this.pinColumns = columns;
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
        (cell) => cell.classList.contains("gt-i-pinned"),
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
   * marked `gt-i-pinned` by), pin the stub where its columns are in the rows shown, and keep the
   * contents of the cells across the table in the part in view. The table's borders are drawn on
   * its cells from the first time, and a hint says it scrolls, until it first does.
   */
  private pin(): void {
    const { scroller, table } = this;
    this.cancelPin();
    if (this.responsive === null || scroller === null || table === null) {
      return;
    }
    const wide = scroller.scrollWidth > scroller.clientWidth + 1;
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
    const columns = this.pinColumns;
    if (columns > 0) {
      if (this.borders === null) {
        this.separateBorders().redraw();
      }
      // Each pinned column sticks after the ones before it, as wide as they are in the rows shown
      const rows = Array.from(table.rows).filter((tr) => !tr.hidden && tr.parentElement?.tagName !== "TFOOT");
      const pinned = placeCells(rows).placed.filter((p) => p.c1 < columns && p.cell.classList.contains("gt-i-pinned"));
      const offsets: (number | undefined)[] = [0];
      for (let c = 0; c < columns; c++) {
        const at = offsets[c];
        for (const p of pinned) {
          if (at !== undefined && p.c0 === c && offsets[p.c1 + 1] === undefined) {
            offsets[p.c1 + 1] = at + p.cell.getBoundingClientRect().width;
          }
        }
      }
      for (const p of pinned) {
        setStyle(p.cell, "inset-inline-start", `${(offsets[p.c0] ?? 0) - padStart}px`);
        this.fill(p.cell);
      }
      this.edgeCell = pinned.find((p) => p.c1 === columns - 1)?.cell ?? null;
      // (What has focus is kept clear of them)
      setStyle(scroller, "scroll-padding-inline-start", `${offsets[columns] ?? 0}px`);
    }

    // The contents of the cells across the table are as wide as the part in view, and stick in it
    for (const div of this.inView) {
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
  // the inline start along the pinned columns, the one at the end along the container's edge, from
  // the column labels to the end of the body. The hint sits by the end, halfway down (or near the top)
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
      place(shades.left, start, more);
    } else {
      place(shades.left, edge?.right ?? start, past);
      place(shades.right, end, more);
    }
    const hint = this.hint;
    if (hint !== null && wide) {
      // (Not far down a long table, which may go past the window)
      setStyle(hint, "top", y(Math.min((y0 + y1) / 2, y0 + 120)));
      setStyle(hint, "left", x(rtl ? start + 8 : end - 8 - hint.offsetWidth));
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
        box.addEventListener("click", (event) => this.userSelect(entry, event.shiftKey));
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
      // (Not when the click ends selecting text in the row)
      const text = this.ownerDocument.getSelection();
      const tr = row === null ? null : this.rowElements[row];
      if (
        row === null ||
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
    const cells = new Map<string, HTMLTableCellElement>();
    for (const th of table.querySelectorAll<HTMLTableCellElement>(":scope > thead th[id]")) {
      cells.set(th.id, th);
    }

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
      const button = this.ownerDocument.createElement("button");
      button.type = "button";
      button.className = "gt-i-sort";

      if (th.querySelector(INTERACTIVE) === null) {
        // The label itself becomes the button
        button.append(...Array.from(th.childNodes));
      } else {
        // A label with links (say) keeps them, with a separate button
        button.classList.add("gt-i-sort-only");
        button.setAttribute("aria-label", `Sort by ${label}`);
      }
      const icon = this.ownerDocument.createElement("span");
      icon.className = "gt-i-sort-icon";
      icon.setAttribute("aria-hidden", "true");
      button.append(icon);
      th.append(button);

      // Shift-click would otherwise extend the page's text selection
      button.addEventListener("mousedown", (event) => {
        if (event.shiftKey) {
          event.preventDefault();
        }
      });
      button.addEventListener("click", (event) => {
        this.userSort(toggleSort(this.sortKeys, id, event.shiftKey));
      });
      this.sortHeaders.set(id, { th, icon, label });
    }

    if (this.sortHeaders.size > 0) {
      this.addLiveRegion();
    }
  }

  // A resize handle for each column with a label of its own (not one spanning several columns)
  private addResizers(table: HTMLTableElement): void {
    const rows = Array.from(
      table.querySelectorAll<HTMLTableRowElement>(":scope > thead > tr.gt_col_headings"),
    );
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
        if (colspan === 1 && r + rowspan >= rows.length && !th.classList.contains("gt-i-select")) {
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

    handle.addEventListener("pointerdown", (event) => {
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
      };
      const end = () => {
        handle.removeEventListener("pointermove", move);
        handle.removeEventListener("pointerup", end);
        handle.removeEventListener("pointercancel", end);
        handle.removeEventListener("lostpointercapture", end);
        this.removeAttribute("data-gti-resizing");
        handle.removeAttribute("data-gti-active");
        if (width !== start) {
          // (Short pages are padded to the new height of a full one)
          if (this.padStale()) {
            this.render();
          }
          this.dispatchResize(resizer, width);
        }
      };
      handle.setPointerCapture?.(event.pointerId);
      this.setAttribute("data-gti-resizing", "");
      handle.setAttribute("data-gti-active", "");
      handle.addEventListener("pointermove", move);
      handle.addEventListener("pointerup", end);
      handle.addEventListener("pointercancel", end);
      handle.addEventListener("lostpointercapture", end);
    });
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
      if (next !== width) {
        this.dispatchResize(resizer, next);
      }
    });
    handle.addEventListener("dblclick", () => this.userResetWidth(resizer));
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
    this.dispatchResize(resizer, width);
  }

  private dispatchResize(resizer: Resizer, width: number): void {
    const spec = this.spec as Spec;
    // (Body cells start with the selection column, and the group column when groups are a column
    // of the stub)
    const lead = (this.selectColumn ? 1 : 0) + (spec.stub.groups_as_column ? 1 : 0);
    const column = spec.columns[resizer.index - lead];
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
    // (Whole pixels, as the reader sets them; rounded up, so that no text is cut)
    const whole = widths.map((width) => Math.ceil(width - 0.01));
    cols.forEach((col, i) => {
      col.style.width = `${whole[i]}px`;
    });
    if (!colgroup.isConnected) {
      table.insertBefore(colgroup, table.querySelector(":scope > thead, :scope > tbody"));
    }
    table.style.removeProperty("min-width");
    table.style.tableLayout = "fixed";
    table.style.width = "fit-content";
    this.colgroup = colgroup;
    this.fittedCols = [];
    this.widthsFixed = true;
    this.startWidths = whole;
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
    const widths =
      full === undefined
        ? Array.from({ length: columns }, (_, i) => label(i)?.getBoundingClientRect().width)
        : Array.from(full.children, (cell) => cell.getBoundingClientRect().width);
    return columns > 0 && widths.every((width) => width !== undefined) ? (widths as number[]) : null;
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

  // The search field, which searches once typing pauses, or at once on Enter
  private searchInput(): HTMLInputElement {
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
    this.searchBox = input;
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
    const previous = this.barButton("previous", "Previous page", `Previous page (${back})`);
    const next = this.barButton("next", "Next page", `Next page (${ahead})`);
    const readout = doc.createElement("button");
    readout.type = "button";
    readout.className = "gt-i-readout";
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
    pages.append(previous, box, next);
    const info = this.makeInfo();

    const bar: Bar = {
      root,
      toggle: null,
      field: null,
      count: null,
      clear: null,
      pages,
      previous,
      next,
      readout,
      jump,
      jumpInput,
      jumpCount,
      info,
    };
    this.bar = bar;
    if (spec.controls.search) {
      this.addBarSearch(bar);
    }
    // (The panel follows its button, so that Tab goes from one into the other)
    root.append(pages, info.button, info.panel);

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

    // In the bar (but not while typing in it, or in the info panel), the arrow keys and Page Up and
    // Down go to the page before or after, and Home and End to the first or last; Escape closes the
    // info panel
    root.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && !info.panel.hidden) {
        // (And don't, say, close a dialog the table is in)
        event.preventDefault();
        event.stopPropagation();
        this.closeInfo(true);
        return;
      }
      if (
        pages.hidden ||
        event.altKey ||
        event.ctrlKey ||
        event.metaKey ||
        event.target instanceof HTMLInputElement ||
        info.panel.contains(event.target as Node)
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
      clear.title = close ? "Close (Esc)" : "Clear (Esc)";
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
    button.title = title;
    button.append(icon(this.ownerDocument, name));
    return button;
  }

  /** Make the info panel, and the bar's button that opens it (a disclosure). */
  private makeInfo(): Info {
    const doc = this.ownerDocument;
    const spec = this.spec as Spec;
    const button = this.barButton("info", "Table info", "Table info");
    const panel = doc.createElement("div");
    panel.className = "gt-i-info";
    panel.id = `gt-i-info-${++infoCount}`;
    panel.setAttribute("role", "group");
    panel.setAttribute("aria-label", "Table info");
    panel.hidden = true;
    button.setAttribute("aria-expanded", "false");
    button.setAttribute("aria-controls", panel.id);

    const rows = doc.createElement("p");
    rows.className = "gt-i-info-rows";
    panel.append(rows);
    const info: Info = {
      button,
      panel,
      rows,
      size: null,
      select: null,
      sort: null,
      sortText: null,
      sortReset: null,
      filters: null,
      filtersText: null,
      filtersClear: null,
      selection: null,
      selectionText: null,
      selectionClear: null,
      keys: null,
      pageKeys: [],
    };

    // An item: what it's about, then the control that changes it
    const item = (name: string, tag: "div" | "label", text: HTMLElement, control: HTMLElement) => {
      const el = doc.createElement(tag);
      el.className = "gt-i-info-item";
      el.dataset.gtiInfo = name;
      el.append(text, control);
      panel.append(el);
      return el;
    };
    const span = (text = "") => {
      const el = doc.createElement("span");
      el.textContent = text;
      return el;
    };
    const action = (text: string, label: string, act: () => void) => {
      const el = doc.createElement("button");
      el.type = "button";
      el.className = "gt-i-info-button";
      el.textContent = text;
      el.setAttribute("aria-label", label);
      // (Disabled with ARIA, so that it keeps focus once it has done what it does)
      el.addEventListener("click", () => {
        if (el.getAttribute("aria-disabled") !== "true") {
          act();
        }
      });
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
      info.sortReset = action("Reset", "Reset the sort", () => this.userSort([]));
      info.sort = item("sort", "div", info.sortText, info.sortReset);
    }
    if (this.filters.length > 0) {
      info.filtersText = span();
      info.filtersClear = action("Clear", "Clear the filters", () => {
        this.cancelFilterTimer();
        this.userFilter(() => this.clearFilters());
      });
      info.filters = item("filters", "div", info.filtersText, info.filtersClear);
    }
    if (spec.controls.selection !== null) {
      info.selectionText = span();
      info.selectionClear = action("Clear", "Clear the selection", () => this.userClearSelection());
      info.selection = item("selection", "div", info.selectionText, info.selectionClear);
    }

    // The keys the table answers to, and the clicks with Shift
    const heading = doc.createElement("p");
    heading.className = "gt-i-info-heading";
    heading.textContent = "Shortcuts";
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
    if (spec.controls.search) {
      key(["/"], "Search");
      key(["Esc"], "Clear the search, then close it");
    }
    if (spec.pagination.enabled) {
      info.pageKeys = [
        key(["←", "→"], "Previous or next page, in the bar"),
        key(["Home", "End"], "First or last page, in the bar"),
      ];
    }
    if (this.sortHeaders.size > 0) {
      key(["Shift"], "Sort by more than one column", true);
    }
    if (spec.controls.selection === "multiple") {
      key(["Shift"], "Select a range of rows", true);
    }
    if (keys.childElementCount > 0) {
      info.keys = doc.createElement("div");
      info.keys.className = "gt-i-info-shortcuts";
      info.keys.append(heading, keys);
      panel.append(info.keys);
    }

    button.addEventListener("click", () => {
      if (panel.hidden) {
        this.openInfo();
      } else {
        this.closeInfo(false);
      }
    });
    // The panel closes when focus goes elsewhere (but not when the window loses it)
    const leave = (event: FocusEvent) => {
      const to = event.relatedTarget as Node | null;
      if (to !== null && to !== button && !panel.contains(to)) {
        this.closeInfo(false);
      }
    };
    button.addEventListener("focusout", leave);
    panel.addEventListener("focusout", leave);
    return info;
  }

  private openInfo(): void {
    const info = this.bar?.info;
    if (info === undefined || !info.panel.hidden) {
      return;
    }
    this.closeFilter(false);
    this.updateInfo();
    // (Over the table, so filled with what's behind it)
    info.panel.style.backgroundColor = backdropColor(this);
    info.panel.hidden = false;
    info.button.setAttribute("aria-expanded", "true");
    this.placeInfo(info);
    // A press anywhere else closes it
    this.outsidePress = (event: PointerEvent) => {
      const path = event.composedPath();
      if (!path.includes(info.panel) && !path.includes(info.button)) {
        this.closeInfo(false);
      }
    };
    this.ownerDocument.addEventListener("pointerdown", this.outsidePress);
  }

  // Above the bar, or below it if there's more room in the view there than above, for a panel
  // that doesn't fit above; no taller than the room it has
  private placeInfo(info: Info): void {
    const panel = info.panel;
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

  private closeInfo(focus: boolean): void {
    if (this.outsidePress !== null) {
      this.ownerDocument.removeEventListener("pointerdown", this.outsidePress);
      this.outsidePress = null;
    }
    const info = this.bar?.info;
    if (info === undefined || info.panel.hidden) {
      return;
    }
    info.panel.hidden = true;
    info.button.setAttribute("aria-expanded", "false");
    if (focus) {
      info.button.focus();
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
    if (info.sortText !== null && info.sortReset !== null) {
      info.sortText.textContent = this.sortText();
      info.sortReset.setAttribute("aria-disabled", String(this.sortKeys.length === 0));
    }
    if (info.filtersText !== null && info.filtersClear !== null) {
      info.filtersText.textContent = this.filtersText();
      info.filtersClear.setAttribute("aria-disabled", String(this.activeFilters().length === 0));
    }
    if (info.selectionText !== null && info.selectionClear !== null) {
      info.selectionText.textContent = this.selectionText();
      info.selectionClear.setAttribute("aria-disabled", String(this.selected.size === 0));
    }
    for (const entry of info.pageKeys) {
      entry.hidden = bar.pages.hidden;
    }
    if (info.keys !== null) {
      info.keys.hidden = Array.from(info.keys.querySelectorAll<HTMLElement>("dl > div"), (entry) => entry.hidden).every(Boolean);
    }
  }

  // A filter button in the label of each column that can be filtered (after its sort button), and
  // a filter for each, whether or not it has a label (and so a button)
  private addFilters(table: HTMLTableElement, spec: Spec): void {
    const doc = this.ownerDocument;
    const cells = new Map<string, HTMLTableCellElement>();
    for (const th of table.querySelectorAll<HTMLTableCellElement>(":scope > thead th[id]")) {
      cells.set(th.id, th);
    }

    for (const filterSpec of spec.filters ?? []) {
      const id = filterSpec.column;
      const index = spec.columns.findIndex((column) => column.id === id);
      const column = spec.columns[index];
      if (column === undefined || this.filters.some((control) => control.filter.column === id)) {
        continue;
      }
      const th = column.header === null ? null : (cells.get(column.header) ?? null);
      const label = this.sortHeaders.get(id)?.label ?? ((th !== null && labelText(th)) || id);
      const filter = new ColumnFilter(filterSpec, index, spec.ranks[id] ?? []);
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
      th.append(button);
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
   * filter), a checkbox for each value (a facet), or fields for the bounds (a range).
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
    } else {
      const list = doc.createElement("div");
      list.className = "gt-i-filter-options";
      for (const [key, text] of this.facetLabels(filter)) {
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
        const controls = Array.from(panel.querySelectorAll<HTMLElement>("button, input"));
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

  // A facet's values, in order (a missing one last), with the text a row with each shows
  private facetLabels(filter: ColumnFilter): [number, string][] {
    const values = filter.spec.values ?? [];
    const labels = new Map<number, string>();
    let missing = false;
    this.rowElements.forEach((tr, row) => {
      const key = filter.key(row);
      if (key === MISSING) {
        missing = true;
      } else if (!labels.has(key)) {
        const cell = this.dataCells(tr)[filter.index];
        labels.set(key, (cell !== undefined && labelText(cell)) || String(values[key]));
      }
    });
    const entries = values.map((value, key): [number, string] => [key, labels.get(key) ?? String(value)]);
    if (missing) {
      entries.push([MISSING, "(Missing)"]);
    }
    return entries;
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
    filter.min = read(control.min, filter.min);
    filter.max = read(control.max, filter.max);
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
        input.value = value === null ? "" : String(value);
        input.removeAttribute("aria-invalid");
      }
    }
    for (const option of control.options) {
      option.box.checked = filter.chosen.has(option.key);
    }
  }

  private openFilterPanel(control: FilterControl): void {
    const button = control.button;
    if (button === null) {
      return;
    }
    this.closeFilter(false);
    this.closeInfo(false);
    const panel = control.panel ?? this.makeFilterPanel(control);
    // (Over the table, so filled with what's behind it; in the table's font)
    panel.style.backgroundColor = backdropColor(this);
    panel.style.fontFamily = getComputedStyle(this.table as HTMLTableElement).fontFamily;
    panel.hidden = false;
    button.setAttribute("aria-expanded", "true");
    this.openFilter = control;
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
    panel.querySelector<HTMLElement>("input")?.focus();
  }

  // The open panel closes when focus goes elsewhere (but not when the window loses it)
  private leaveFilter(control: FilterControl, event: FocusEvent): void {
    const to = event.relatedTarget as Node | null;
    if (this.openFilter === control && to !== null && to !== control.button && !control.panel?.contains(to)) {
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
    if (control === null) {
      return;
    }
    this.openFilter = null;
    // (A change may be waiting on the typing to pause)
    this.flushFilter();
    if (control.panel !== null) {
      control.panel.hidden = true;
    }
    control.button?.setAttribute("aria-expanded", "false");
    if (focus) {
      control.button?.focus();
    }
  }

  // The open panel is below its button, from the button's inline start (as far as the element's
  // width allows)
  private placeFilter(): void {
    const control = this.openFilter;
    const panel = control?.panel;
    if (control?.button == null || panel == null) {
      return;
    }
    const host = this.getBoundingClientRect();
    const button = control.button.getBoundingClientRect();
    const width = panel.offsetWidth;
    const start = this.isRtl() ? button.right - width : button.left;
    panel.style.left = `${Math.max(0, Math.min(start - host.left, host.width - width))}px`;
    panel.style.top = `${button.bottom - host.top + 4}px`;
  }

  private updateFilters(): void {
    if (this.filters.length > 0) {
      this.updateFilterButtons();
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

  // The open panel's Clear button, and a facet's counts: the rows with each value that the search
  // and the other filters keep (so a value with none can still be chosen, but is dimmed)
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
      for (const option of control.options) {
        const count = counts.get(option.key) ?? 0;
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
    for (const control of this.filters) {
      control.filter.clear();
      this.syncFilter(control);
    }
  }

  private filtersText(): string {
    const labels = this.filters.filter((control) => control.filter.active).map((control) => control.label);
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

  // Change the filters as the reader asked, and filter the rows by them, if they changed
  private userFilter(change: () => void): void {
    const filters = this.filters.map((control) => control.filter);
    const before = JSON.stringify(filterQuery(filters));
    change();
    const query = filterQuery(filters);
    if (JSON.stringify(query) === before || this.spec === null) {
      this.updateFilters();
      return;
    }
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
  }

  private applyFilters(): void {
    this.pageValue = 1;
    this.matchRows();
    this.render();
  }

  private openSearch(focus: boolean): void {
    const bar = this.bar;
    if (bar?.field == null || bar.toggle === null) {
      return;
    }
    bar.field.hidden = false;
    bar.toggle.hidden = true;
    bar.root.setAttribute("data-gti-searching", "");
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
      bar.toggle.focus();
    }
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

  // The bar shows while it has a search or filters (whose info panel says how many rows they
  // leave), or there are pages (or could be, in the page sizes the info panel offers); the page
  // controls, while there are pages: while the table has more rows than fit on a page, whatever
  // the search
  private updateBar(bar: Bar): void {
    const spec = this.spec as Spec;
    const size = this.size;
    const paged = size !== null && spec.nrows > size;
    bar.pages.hidden = !paged;
    bar.root.hidden = !this.pagesOffered() && bar.field === null && this.filters.length === 0;
    if (bar.root.hidden) {
      this.closeInfo(false);
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
    this.updateInfo();
    if (!paged) {
      return;
    }

    const page = this.page;
    const count = this.pageCount;
    bar.previous.setAttribute("aria-disabled", String(page === 1));
    bar.next.setAttribute("aria-disabled", String(page === count));
    bar.readout.replaceChildren(String(page), this.slash(), String(count));
    bar.readout.setAttribute("aria-label", `Page ${page} of ${count}`);
    bar.readout.title = "Go to a page";
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
    below.after(el);
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
      this.alignBars();
      this.placeFilter();
      this.stick();
      // (In the next frame, like the column widths below)
      this.queuePin();
      const resized = this.colgroup !== null && this.clientWidth !== this.fittedWidth;
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
  }

  private userPageSize(size: number): void {
    if (size === this.size) {
      return;
    }
    this.resize(size);
    this.announce(`${plural(size)} per page, page ${this.page} of ${this.pageCount}`);
    this.dispatchPage();
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
    if (spec === null || !this.movable || (this.terms.length === 0 && filters.length === 0)) {
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

  // Call `each` with each data row that matches the search and `filters`
  private eachKept(filters: readonly ColumnFilter[], each: (row: number) => void): void {
    const nrows = (this.spec as Spec).nrows;
    const texts =
      this.terms.length > 0 || filters.some((filter) => filter.type === "text")
        ? (this.cellTexts ?? this.makeCellTexts(nrows))
        : null;
    for (let row = 0; row < nrows; row++) {
      const cells = texts?.[row] ?? [];
      if (
        (this.terms.length === 0 || rowMatches(cells, this.terms)) &&
        filters.every((filter) => filter.keeps(row, cells[filter.index]))
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

  // A data row's cells, one per column of the spec: not a group's label cell, which is on one of
  // its rows only (so it isn't searched), nor the selection column's
  private dataCells(tr: HTMLTableRowElement): Element[] {
    return Array.from(tr.children).filter((cell) => !cell.matches(".gt_stub_row_group, .gt-i-select"));
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
    const pads = size !== null && this.spec.nrows > size;
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
    // summary rows stay where they are
    const order: number[] = [];
    for (const block of this.blocks) {
      const fragment = this.ownerDocument.createDocumentFragment();
      for (const row of sortRows(block.rows, this.sortKeys, spec.ranks)) {
        fragment.append(this.rowElements[row] as HTMLTableRowElement);
        if (matches === null || matches[row] === 1) {
          order.push(row);
        }
      }
      tbody.insertBefore(fragment, block.anchor);
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
      tr.hidden = onPage[row] !== 1;
    });
    for (const group of this.groups) {
      const span = spans.get(group);
      for (const tr of group.headings) {
        tr.hidden = span === undefined;
      }
      for (const tr of group.top) {
        tr.hidden = span?.starts !== true;
      }
      for (const tr of group.bottom) {
        tr.hidden = span?.ends !== true;
      }
      this.placeGroupCell(group, span);
    }
    return { shown, page, start, total: order.length };
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
    if (table.getClientRects().length === 0) {
      // Not laid out (say, in a hidden tab): try again once it is
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
    if (this.startWidths !== null) {
      // The reader's widths stay
      this.render();
      return;
    }
    if (colgroup === null || this.table === null) {
      // Widths not measured yet are measured on rendering
      this.render();
      return;
    }
    const widths = this.measureWidths();
    if (widths !== null && widths.columns.length === colgroup.children.length) {
      this.setWidths(widths);
    } else {
      this.colgroup = null;
      this.fittedCols = [];
    }
    this.render();
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
    this.place(null, null, 1);
    const trs = Array.from((this.tbody as HTMLTableSectionElement).querySelectorAll(":scope > tr"));
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
      table.style.width = "fit-content";
      this.tableFitted = true;
    } else {
      // Column widths alone let a table that overflows its container shrink to fit it
      table.style.minWidth = `${widths.table}px`;
    }
    this.fittedWidth = this.clientWidth;
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
      const width = Math.max(
        1,
        ...this.rowElements.map((tr) =>
          Array.from(tr.children).reduce(
            (sum, cell) => sum + Number(cell.getAttribute("colspan") ?? 1),
            0,
          ),
        ),
      );
      this.empty = doc.createElement("tr");
      this.empty.className = "gt-i-empty";
      const td = doc.createElement("td");
      td.className = "gt_row gt_center";
      td.colSpan = width;
      td.textContent = "No matching rows";
      this.empty.append(td);
      // (Kept in view, like the rows across the table, once it's been wider than its container)
      this.inView?.push(keepInView(td));
    }
    if (this.empty.parentNode === null) {
      tbody.insertBefore(this.empty, this.grandBottom());
    }
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
    const { shown } = this.place(null, size, 1);
    this.borders?.redraw();
    this.padHeight = this.bodyHeight();
    const heights = shown.map((tr) => tr.getBoundingClientRect().height);
    this.rowHeight = heights.length === 0 ? 0 : heights.reduce((a, b) => a + b, 0) / heights.length;
  }

  private bodyHeight(): number {
    return (this.tbody as HTMLTableSectionElement).getBoundingClientRect().height;
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
    const registry = typeof CSS !== "undefined" ? CSS.highlights : undefined;
    if (registry === undefined || typeof Highlight === "undefined") {
      return;
    }
    let highlight = registry.get(SEARCH_HIGHLIGHT);
    // Each table adds its ranges to the one highlight of the page
    if (highlight === undefined) {
      highlight = new Highlight();
      registry.set(SEARCH_HIGHLIGHT, highlight);
    }
    for (const range of this.ranges) {
      highlight.delete(range);
    }
    this.ranges = [];
    // The search's terms, in every cell, and a text filter's, in its column's
    const texts = this.activeFilters().filter((filter) => filter.type === "text");
    if ((this.terms.length === 0 && texts.length === 0) || this.cellTexts === null) {
      return;
    }
    // (Ranges are made afresh, since moving rows collapses live ranges in them)
    for (const tr of shown) {
      const row = this.bodyRows.get(tr) as number;
      const cells = this.cellTexts[row] ?? [];
      const found = cells.flatMap((cell) => cell.find(this.terms));
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
      const label = this.sortHeaders.get(key.column)?.label ?? key.column;
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
    this.hint?.remove();
    this.toolbar?.remove();
    this.pager?.nav.remove();
    this.closeInfo(false);
    this.bar?.root.remove();
    if (this.slashKey !== null) {
      this.removeEventListener("keydown", this.slashKey);
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
    this.searchValue = "";
    this.terms = [];
    this.matched = null;
    this.matchCount = 0;
    this.filters = [];
    this.pageValue = 1;
    this.pageSizeValue = undefined;
    this.view = { start: 0, end: 0, total: 0 };
    this.pager = null;
    this.bar = null;
    this.slashKey = null;
    this.jumping = false;
    this.colgroup = null;
    this.fittedCols = [];
    this.widthsFixed = false;
    this.cutsText = false;
    this.tableFitted = false;
    this.fittedWidth = 0;
    this.resizers = [];
    this.startWidths = null;
    this.cellTexts = null;
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
    this.pinColumns = 0;
    this.edgeCell = null;
    this.acrossCells = [];
    this.inView = null;
    this.hint = null;
    this.hinted = false;
    this.regioned = false;
    this.removeAttribute("data-gti-highlight");
    this.removeAttribute("data-gti-nowrap");
    this.removeAttribute("data-gti-resizing");
    this.removeAttribute("data-gti-scroll");
    this.removeAttribute("data-gti-sticky");
    this.removeAttribute("data-gti-wide");
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
