/**
 * The `<gt-table>` custom element.
 *
 * It wraps a static Great Tables table and adds interactivity on top of it (hydration), rather
 * than rendering a table of its own: it reads the table's spec, maps each body row to its entry,
 * and sorts and searches by moving and hiding the table's own `<tr>`s, so styles, footnote marks
 * and the like move with their rows.
 *
 * `data-gti-state` says how far it got: `pending` (waiting for the document to be parsed),
 * `empty` (no table yet), `static` (a table without a spec, left as it is), `error` (the spec is
 * unusable or doesn't match the table; see the console), or `ready`.
 */

import { CellText, rowMatches, searchTerms } from "./search";
import { normalizeSort, type SortKey, type SortKeyInit, sortRows, toggleSort } from "./sort";
import { type BodyRow, parseSpec, type Spec, SpecError } from "./spec";

export const TAG_NAME = "gt-table";

/** The event fired when the reader changes the sort (not when the `sort` property is set). */
export const SORT_EVENT = "gt-table-sort";

/** The event fired when the reader searches (not when the `search` property is set). */
export const SEARCH_EVENT = "gt-table-search";

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

/** A row group, as far as showing and hiding its rows goes. */
interface Group {
  /** The group's heading and summary rows, shown only while some of its data rows are. */
  structural: HTMLTableRowElement[];
  /** The group's label cell, when row groups are shown as a column of the stub. */
  cell: HTMLTableCellElement | null;
  /** Whether that cell is on a summary row (at the top of the group), where it stays. */
  cellFixed: boolean;
}

/** A run of data rows of one group (if any) between structural rows: what sorts. */
interface Block {
  /** The block's data rows, in the order GT rendered them. */
  rows: number[];
  /** The structural `<tr>` after the block, which stays put, or `null` at the end of the body. */
  anchor: HTMLTableRowElement | null;
  group: Group | null;
}

interface SortHeader {
  th: HTMLTableCellElement;
  icon: HTMLElement;
  label: string;
}

// Header content that can't go inside a <button>
const INTERACTIVE = "a[href], button, input, select, textarea, details, [tabindex]";

// How long typing pauses before the search runs
const SEARCH_DELAY_MS = 150;

/** A column label's text, for announcements: without footnote marks. */
function labelText(th: HTMLTableCellElement): string {
  const copy = th.cloneNode(true) as HTMLTableCellElement;
  for (const mark of copy.querySelectorAll(".gt_footnote_marks")) {
    mark.remove();
  }
  return (copy.textContent ?? "").replace(/\s+/g, " ").trim();
}

const plural = (n: number) => `${n} ${n === 1 ? "row" : "rows"}`;

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
  /** Whether rows can be moved and hidden: not with a hierarchical stub (see `sortableColumns`). */
  private movable = false;
  private sortKeys: SortKey[] = [];
  private sortHeaders = new Map<string, SortHeader>();
  private searchValue = "";
  private terms: string[] = [];
  /** Per data row, whether it matches the search; `null` without one. */
  private matched: Uint8Array | null = null;
  /** Per data row, the text of its cells; made on the first search. */
  private cellTexts: CellText[][] | null = null;
  private ranges: AbstractRange[] = [];
  private searchBox: HTMLInputElement | null = null;
  private searchTimer: ReturnType<typeof setTimeout> | null = null;
  private toolbar: HTMLElement | null = null;
  private layout: ResizeObserver | null = null;
  private empty: HTMLTableRowElement | null = null;
  private live: HTMLElement | null = null;

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
    if (this.movable && spec.controls.sorting) {
      this.addSortHeaders(table, spec);
    }
    if (this.movable && spec.controls.search) {
      this.addSearchBox(table);
    }
    if (this.searchValue !== "") {
      this.applySearch(this.searchValue);
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
        group = { structural: [], cell: null, cellFixed: false };
        groups.set(key, group);
      }
      return group;
    };
    const rowGroup = new Map<number, Group>();
    for (const { id, rows } of spec.groups) {
      for (const row of rows) {
        rowGroup.set(row, groupOf(id));
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
          group.structural.push(tr);
          const cell = groupCell(tr);
          if (cell !== null) {
            group.cell = cell;
            group.cellFixed = true;
          }
        }
        return;
      }
      rowElements[entry] = tr;
      const group = rowGroup.get(entry) ?? null;
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

  private observeLayout(): void {
    if (this.toolbar === null || this.layout !== null || typeof ResizeObserver === "undefined") {
      return;
    }
    this.layout = new ResizeObserver(() => this.alignToolbar());
    this.layout.observe(this);
    if (this.table !== null) {
      this.layout.observe(this.table);
    }
  }

  private alignToolbar(): void {
    if (this.toolbar === null || this.table === null) {
      return;
    }
    const outer = this.getBoundingClientRect();
    const table = this.table.getBoundingClientRect();
    const left = Math.max(0, table.left - outer.left);
    this.toolbar.style.marginLeft = `${left}px`;
    this.toolbar.style.width = `${Math.max(0, Math.min(table.width, outer.width - left))}px`;
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

  /** Search, returning the number of matching data rows. */
  private applySearch(value: string): number {
    this.searchValue = value;
    this.terms = searchTerms(value);
    const spec = this.spec;
    if (spec === null || !this.movable) {
      return 0;
    }
    if (this.terms.length === 0) {
      this.matched = null;
      this.render();
      return spec.nrows;
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
    this.render();
    return count;
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

  /** Show the data rows for the current sort and search. */
  private render(): void {
    const spec = this.spec;
    const tbody = this.tbody;
    if (spec === null || tbody === null) {
      return;
    }
    const matches = this.matched;

    // Each block is sorted on its own, so rows stay in their group, and group headings and
    // summary rows stay where they are
    const shown: HTMLTableRowElement[] = [];
    const counts = new Map<Group, number>();
    const firsts = new Map<Group, HTMLTableRowElement>();
    for (const block of this.blocks) {
      const order = sortRows(block.rows, this.sortKeys, spec.ranks);
      const fragment = this.ownerDocument.createDocumentFragment();
      let count = 0;
      for (const row of order) {
        const tr = this.rowElements[row] as HTMLTableRowElement;
        fragment.append(tr);
        const visible = matches === null || matches[row] === 1;
        tr.hidden = !visible;
        if (visible) {
          if (count === 0 && block.group !== null) {
            firsts.set(block.group, tr);
          }
          shown.push(tr);
          count++;
        }
      }
      tbody.insertBefore(fragment, block.anchor);
      if (block.group !== null) {
        counts.set(block.group, (counts.get(block.group) ?? 0) + count);
      }
    }

    for (const group of this.groups) {
      const count = counts.get(group) ?? 0;
      for (const tr of group.structural) {
        tr.hidden = count === 0;
      }
      this.placeGroupCell(group, count, firsts.get(group));
    }

    this.restripe(shown);
    this.showEmpty(matches !== null && shown.length === 0);
    this.updateSortHeaders();
    this.highlight(shown);
  }

  // The label cell of a group shown as a column goes on the group's first shown row, and spans
  // its shown rows
  private placeGroupCell(group: Group, count: number, first: HTMLTableRowElement | undefined): void {
    const cell = group.cell;
    if (cell === null || count === 0) {
      return;
    }
    const target = group.cellFixed ? cell.parentElement : first;
    if (target !== undefined && target !== null && cell.parentElement !== target) {
      cell.parentElement?.classList.remove("gt_row_group_first");
      target.prepend(cell);
      target.classList.add("gt_row_group_first");
    }
    cell.setAttribute("rowspan", String(count + group.structural.length));
  }

  // Alternate shown data rows (counted through the whole body, as GT does) are striped
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

  private reset(): void {
    this.stopObserving();
    this.cancelSearchTimer();
    this.layout?.disconnect();
    this.highlightClear();
    this.live?.remove();
    this.toolbar?.remove();
    this.table = null;
    this.spec = null;
    this.tbody = null;
    this.rowElements = [];
    this.bodyRows = new WeakMap();
    this.blocks = [];
    this.groups = [];
    this.movable = false;
    this.sortKeys = [];
    this.sortHeaders = new Map();
    this.searchValue = "";
    this.terms = [];
    this.matched = null;
    this.cellTexts = null;
    this.searchBox = null;
    this.toolbar = null;
    this.layout = null;
    this.empty = null;
    this.live = null;
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
