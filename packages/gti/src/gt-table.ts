/**
 * The `<gt-table>` custom element.
 *
 * It wraps a static Great Tables table and adds interactivity on top of it (hydration), rather
 * than rendering a table of its own: it reads the table's spec, maps each body row to its entry,
 * and sorts by moving the table's own `<tr>`s, so styles, footnote marks and the like move with
 * their rows.
 *
 * `data-gti-state` says how far it got: `pending` (waiting for the document to be parsed),
 * `empty` (no table yet), `static` (a table without a spec, left as it is), `error` (the spec is
 * unusable or doesn't match the table; see the console), or `ready`.
 */

import { normalizeSort, type SortKey, type SortKeyInit, sortRows, toggleSort } from "./sort";
import { type BodyRow, parseSpec, type Spec, SpecError } from "./spec";

export const TAG_NAME = "gt-table";

/** The event fired when the reader changes the sort (not when the `sort` property is set). */
export const SORT_EVENT = "gt-table-sort";

declare const __GTI_VERSION__: string;

export const VERSION: string = typeof __GTI_VERSION__ === "string" ? __GTI_VERSION__ : "dev";

export type State = "pending" | "empty" | "static" | "error" | "ready";

export interface SortEventDetail {
  sort: SortKey[];
}

/** A run of data rows between structural rows (group headings, summary rows): what sorts. */
interface Block {
  /** The block's data rows, in the order GT rendered them. */
  rows: number[];
  /** The `<tr>` after the block, which stays put, or `null` at the end of the body. */
  anchor: HTMLTableRowElement | null;
  /** The group label cell of a row group shown as a column, when it's on one of these rows. */
  groupCell: HTMLTableCellElement | null;
}

interface SortHeader {
  th: HTMLTableCellElement;
  icon: HTMLElement;
  label: string;
}

// Header content that can't go inside a <button>
const INTERACTIVE = "a[href], button, input, select, textarea, details, [tabindex]";

/** A column label's text, for announcements: without footnote marks. */
function labelText(th: HTMLTableCellElement): string {
  const copy = th.cloneNode(true) as HTMLTableCellElement;
  for (const mark of copy.querySelectorAll(".gt_footnote_marks")) {
    mark.remove();
  }
  return (copy.textContent ?? "").replace(/\s+/g, " ").trim();
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
  private sortable = false;
  private sortKeys: SortKey[] = [];
  private sortHeaders = new Map<string, SortHeader>();
  private live: HTMLElement | null = null;

  get state(): State | null {
    return this.getAttribute("data-gti-state") as State | null;
  }

  /**
   * The columns the table can be sorted by. Empty until hydrated, and for a table whose stub has
   * cells merged across rows (a hierarchical stub), since reordering rows would break them.
   */
  get sortableColumns(): string[] {
    return this.sortable && this.spec !== null ? Object.keys(this.spec.ranks) : [];
  }

  /** The current sort: the sort keys, most significant first. */
  get sort(): SortKey[] {
    return this.sortKeys.map((key) => ({ ...key }));
  }

  /** @throws {RangeError} for a column that isn't one of `sortableColumns`, or one given twice. */
  set sort(keys: readonly SortKeyInit[]) {
    const ranks: Spec["ranks"] = this.sortable && this.spec !== null ? this.spec.ranks : {};
    this.sortKeys = normalizeSort(keys, ranks);
    this.applySort();
  }

  connectedCallback(): void {
    if (this.table !== null) {
      // Moved: keep the hydrated table (and its sort), unless its children were replaced
      if (this.contains(this.table)) {
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

    try {
      const spec = parseSpec(script.textContent ?? "");
      this.mapRows(table, spec);
      this.spec = spec;
    } catch (err) {
      if (!(err instanceof SpecError)) {
        throw err;
      }
      // The static table still works; it just isn't interactive.
      console.warn(`<gt-table>: ${err.message}; the table is left static.`);
      this.setState("error");
      return;
    }

    this.sortable = !this.hasMergedStubCells();
    if (this.sortable) {
      this.addSortHeaders(table, this.spec);
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

    const rowElements: HTMLTableRowElement[] = [];
    const bodyRows = new WeakMap<HTMLTableRowElement, BodyRow>();
    const blocks: Block[] = [];
    let block: Block | null = null;

    trs.forEach((tr, i) => {
      const entry = spec.body[i] as BodyRow;
      bodyRows.set(tr, entry);
      if (typeof entry !== "number") {
        if (block !== null) {
          block.anchor = tr;
          block = null;
        }
        return;
      }
      rowElements[entry] = tr;
      if (block === null) {
        block = { rows: [], anchor: null, groupCell: null };
        blocks.push(block);
      }
      block.rows.push(entry);
      const groupCell = tr.querySelector<HTMLTableCellElement>(":scope > th.gt_stub_row_group");
      if (groupCell !== null) {
        block.groupCell = groupCell;
      }
    });

    this.tbody = tbody;
    this.rowElements = rowElements;
    this.bodyRows = bodyRows;
    this.blocks = blocks;
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
      this.live = this.ownerDocument.createElement("div");
      this.live.className = "gt-i-live";
      this.live.setAttribute("aria-live", "polite");
      this.live.setAttribute("aria-atomic", "true");
      this.append(this.live);
    }
  }

  private userSort(keys: SortKey[]): void {
    this.sortKeys = keys;
    this.applySort();
    this.announce();
    this.dispatchEvent(
      new CustomEvent<SortEventDetail>(SORT_EVENT, {
        bubbles: true,
        composed: true,
        detail: { sort: this.sort },
      }),
    );
  }

  private applySort(): void {
    const spec = this.spec;
    const tbody = this.tbody;
    if (spec === null || tbody === null) {
      return;
    }

    // Each block is sorted on its own, so rows stay in their group, and group headings and
    // summary rows stay where they are
    const shown: HTMLTableRowElement[] = [];
    for (const block of this.blocks) {
      const order = sortRows(block.rows, this.sortKeys, spec.ranks);
      const trs = order.map((row) => this.rowElements[row] as HTMLTableRowElement);
      const fragment = this.ownerDocument.createDocumentFragment();
      fragment.append(...trs);
      tbody.insertBefore(fragment, block.anchor);
      shown.push(...trs);

      // The label cell of a group shown as a column goes on the group's first row
      const first = trs[0];
      const cell = block.groupCell;
      if (cell !== null && first !== undefined && cell.parentElement !== first) {
        cell.parentElement?.classList.remove("gt_row_group_first");
        first.prepend(cell);
        first.classList.add("gt_row_group_first");
      }
    }

    this.restripe(shown);
    this.updateSortHeaders();
  }

  // Alternate data rows (counted through the whole body, as GT does) are striped
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

  private announce(): void {
    if (this.live === null) {
      return;
    }
    const parts = this.sortKeys.map((key) => {
      const label = this.sortHeaders.get(key.column)?.label ?? key.column;
      return `${label}, ${key.descending ? "descending" : "ascending"}`;
    });
    this.live.textContent = parts.length === 0 ? "Not sorted" : `Sorted by ${parts.join(", then ")}`;
  }

  private reset(): void {
    this.stopObserving();
    this.live?.remove();
    this.table = null;
    this.spec = null;
    this.tbody = null;
    this.rowElements = [];
    this.bodyRows = new WeakMap();
    this.blocks = [];
    this.sortable = false;
    this.sortKeys = [];
    this.sortHeaders = new Map();
    this.live = null;
    this.removeAttribute("data-gti-state");
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
