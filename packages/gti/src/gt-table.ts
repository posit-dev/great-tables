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

import { pageCount, pageItems, pageSizeChoices } from "./paging";
import { CellText, rowMatches, searchTerms } from "./search";
import { normalizeSort, type SortKey, type SortKeyInit, sortRows, toggleSort } from "./sort";
import { type BodyRow, parseSpec, type Spec, SpecError } from "./spec";

export const TAG_NAME = "gt-table";

/** The event fired when the reader changes the sort (not when the `sort` property is set). */
export const SORT_EVENT = "gt-table-sort";

/** The event fired when the reader searches (not when the `search` property is set). */
export const SEARCH_EVENT = "gt-table-search";

/** The event fired when the reader changes the page or the page size (not when properties are set). */
export const PAGE_EVENT = "gt-table-page";

/** The event fired when the reader resizes a column (with a handle, or its keys). */
export const RESIZE_EVENT = "gt-table-resize";

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

export interface ResizeEventDetail {
  /** The column's name in the data; `null` for the stub column holding summary row labels. */
  column: string | null;
  /** The column's position among the body cells (from 0, counting the stub). */
  index: number;
  /** Its new width, in px. */
  width: number;
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

// Header content that can't go inside a <button>
const INTERACTIVE = "a[href], button, input, select, textarea, details, [tabindex]";

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

/** A column label's text, for announcements: without footnote marks. */
function labelText(th: HTMLTableCellElement): string {
  const copy = th.cloneNode(true) as HTMLTableCellElement;
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
  /** Per data row, whether it matches the search; `null` without one. */
  private matched: Uint8Array | null = null;
  /** The number of data rows that match the search (all of them, without one). */
  private matchCount = 0;
  private pageValue = 1;
  /** The page size: `null` for one page of every row, or `undefined` for the spec's. */
  private pageSizeValue: number | null | undefined = undefined;
  /** The rows of the current page: from `start` to `end` of the `total` that match. */
  private view = { start: 0, end: 0, total: 0 };
  private pager: Pager | null = null;
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
    this.stopObserving();
    this.layout?.disconnect();
    this.layout = null;
    this.cancelRefit();
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
    this.setDisplay(spec);
    if (this.movable && spec.controls.sorting) {
      this.addSortHeaders(table, spec);
    }
    if (this.movable && spec.controls.search) {
      this.addSearchBox(table);
    }
    if (spec.controls.resizing) {
      this.addResizers(table);
    }
    if (this.pageSizeValue === undefined) {
      this.pageSizeValue = spec.pagination.enabled ? spec.pagination.page_size : null;
    }
    // A search or page set before hydration applies now
    this.matchRows();
    if (this.matched !== null || this.size !== null) {
      this.render();
    }
    this.setState("ready");
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
        target.closest(`${INTERACTIVE}, .gt_stub_row_group`) !== null
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
        if (colspan === 1 && r + rowspan >= rows.length) {
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
    // (Body cells start with the group column, when groups are a column of the stub)
    const column = spec.columns[resizer.index - (spec.stub.groups_as_column ? 1 : 0)];
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
    const doc = this.ownerDocument;
    const toolbar = doc.createElement("div");
    toolbar.className = "gt-i-toolbar";
    const input = doc.createElement("input");
    input.type = "search";
    input.className = "gt-i-search";
    input.placeholder = "Search";
    input.setAttribute("aria-label", "Search the table");
    input.setAttribute("enterkeyhint", "search");
    input.autocomplete = "off";
    input.spellcheck = false;
    input.value = this.searchValue;
    toolbar.append(input);

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
      } else if (event.key === "Escape" && input.value !== "") {
        // Clear the search (and don't, say, close a dialog the table is in)
        event.preventDefault();
        event.stopPropagation();
        input.value = "";
        this.cancelSearchTimer();
        this.userSearch("");
      }
    });

    // Outside the table's scrolling container, so that it stays in view
    this.prepend(toolbar);
    this.toolbar = toolbar;
    this.searchBox = input;
    this.addLiveRegion();

    // In the table's font, lined up with the table (which GT may have centred or narrowed)
    toolbar.style.fontFamily = getComputedStyle(table).fontFamily;
    this.observeLayout();
  }

  // The toolbar and page controls are lined up with the table, and the column widths are measured
  // again when the element's width changes
  private observeLayout(): void {
    if (
      this.layout !== null ||
      typeof ResizeObserver === "undefined" ||
      (this.toolbar === null && this.pager === null && this.colgroup === null && !this.cutsText)
    ) {
      return;
    }
    this.layout = new ResizeObserver(() => {
      this.alignBars();
      const resized = this.colgroup !== null && this.clientWidth !== this.fittedWidth;
      const unmeasured = !this.widthsFixed && this.needsWidths();
      if ((resized || unmeasured) && this.refitFrame === 0) {
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
  }

  private alignBars(): void {
    if (this.table === null) {
      return;
    }
    const bars = [this.toolbar, this.pager?.nav].filter((bar) => bar != null);
    if (bars.length === 0) {
      return;
    }
    const outer = this.getBoundingClientRect();
    const table = this.table.getBoundingClientRect();
    const left = Math.max(0, table.left - outer.left);
    for (const bar of bars) {
      bar.style.marginLeft = `${left}px`;
      bar.style.width = `${Math.max(0, Math.min(table.width, outer.width - left))}px`;
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

  // Which data rows match the search
  private matchRows(): void {
    this.terms = searchTerms(this.searchValue);
    const spec = this.spec;
    this.matched = null;
    this.matchCount = spec?.nrows ?? 0;
    if (spec === null || !this.movable || this.terms.length === 0) {
      return;
    }

    const texts = this.cellTexts ?? this.makeCellTexts(spec.nrows);
    const matches = new Uint8Array(spec.nrows);
    let count = 0;
    texts.forEach((cells, row) => {
      if (rowMatches(cells, this.terms)) {
        matches[row] = 1;
        count++;
      }
    });
    this.matched = matches;
    this.matchCount = count;
  }

  private makeCellTexts(nrows: number): CellText[][] {
    const texts: CellText[][] = [];
    for (let row = 0; row < nrows; row++) {
      const tr = this.rowElements[row];
      // A group's label cell is on one of its rows only, so it isn't searched
      const cells =
        tr === undefined
          ? []
          : Array.from(tr.children).filter((cell) => !cell.classList.contains("gt_stub_row_group"));
      texts.push(cells.map((cell) => new CellText(cell)));
    }
    this.cellTexts = texts;
    return texts;
  }

  /** Show the data rows for the current sort, search and page. */
  private render(): void {
    if (this.spec === null || this.tbody === null) {
      return;
    }
    const size = this.size;
    if (!this.widthsFixed && this.needsWidths()) {
      this.fixWidths();
    }
    const { shown, page, start, total } = this.place(this.matched, size, this.pageValue);
    this.pageValue = page;
    this.view = { start, end: start + shown.length, total };

    this.restripe(shown);
    this.showEmpty(this.matched !== null && total === 0);
    this.updateSortHeaders();
    this.highlight(shown);
    this.updatePager();
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
      cell.parentElement?.classList.remove("gt_row_group_first");
      target.prepend(cell);
      target.classList.add("gt_row_group_first");
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
    }
    if (this.empty.parentNode === null) {
      const grand = Array.from(tbody.querySelectorAll<HTMLTableRowElement>(":scope > tr")).find((tr) => {
        const entry = this.bodyRows.get(tr);
        return typeof entry === "object" && "grand_summary" in entry && entry.side === "bottom";
      });
      tbody.insertBefore(this.empty, grand ?? null);
    }
  }

  // The page controls are shown while there are pages: while the table has more rows than fit on a
  // page (of the smallest size the reader can choose), whatever the search
  private updatePager(): void {
    const spec = this.spec as Spec;
    const size = this.size;
    const { size_select, page_sizes } = spec.pagination;
    if (size === null || spec.nrows <= (size_select ? Math.min(size, ...page_sizes) : size)) {
      if (this.pager !== null) {
        this.pager.nav.hidden = true;
      }
      return;
    }
    const pager = this.pager ?? this.addPager();
    pager.nav.hidden = false;

    const page = this.page;
    const count = this.pageCount;
    const { start, end, total } = this.view;
    if (pager.info !== null) {
      const rows = total === 0 ? "0 rows" : `${end - start > 1 ? `${start + 1}–` : ""}${end} of ${plural(total)}`;
      pager.info.textContent = this.matched === null ? rows : `${rows} (filtered from ${spec.nrows})`;
    }
    if (pager.select !== null) {
      const choices = pageSizeChoices(size, page_sizes).map(String);
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
    let below: Element = table;
    while (below.parentElement !== null && below.parentElement !== this) {
      below = below.parentElement;
    }
    below.after(nav);
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
    if (this.terms.length === 0 || this.cellTexts === null) {
      return;
    }
    // (Ranges are made afresh, since moving rows collapses live ranges in them)
    for (const tr of shown) {
      const row = this.bodyRows.get(tr) as number;
      for (const cell of this.cellTexts[row] ?? []) {
        for (const found of cell.find(this.terms)) {
          const range = this.ownerDocument.createRange();
          range.setStart(found.startNode, found.startOffset);
          range.setEnd(found.endNode, found.endOffset);
          highlight.add(range);
          this.ranges.push(range);
        }
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

  private cancelRefit(): void {
    if (this.refitFrame !== 0) {
      cancelAnimationFrame(this.refitFrame);
      this.refitFrame = 0;
    }
  }

  private reset(): void {
    this.stopObserving();
    this.cancelSearchTimer();
    this.cancelRefit();
    this.layout?.disconnect();
    this.highlightClear();
    this.live?.remove();
    this.toolbar?.remove();
    this.pager?.nav.remove();
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
    this.pageValue = 1;
    this.pageSizeValue = undefined;
    this.view = { start: 0, end: 0, total: 0 };
    this.pager = null;
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
    this.live = null;
    this.marked = null;
    this.touched = false;
    this.removeAttribute("data-gti-highlight");
    this.removeAttribute("data-gti-nowrap");
    this.removeAttribute("data-gti-resizing");
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
