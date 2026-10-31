/**
 * The `<gt-table>` custom element.
 *
 * It wraps a static Great Tables table and adds interactivity on top of it (hydration), rather
 * than rendering a table of its own. For now it reads the table's spec and maps each body row to
 * its entry; sorting and the rest build on that.
 *
 * `data-gti-state` says how far it got: `pending` (waiting for the document to be parsed),
 * `empty` (no table yet), `static` (a table without a spec, left as it is), `error` (the spec is
 * unusable or doesn't match the table; see the console), or `ready`.
 */

import { type BodyRow, parseSpec, type Spec, SpecError } from "./spec";

export const TAG_NAME = "gt-table";

declare const __GTI_VERSION__: string;

export const VERSION: string = typeof __GTI_VERSION__ === "string" ? __GTI_VERSION__ : "dev";

export type State = "pending" | "empty" | "static" | "error" | "ready";

export class GtTable extends HTMLElement {
  /** The static `<table>` this element hydrates, or `null` if there isn't one. */
  table: HTMLTableElement | null = null;

  /** The table's spec, once hydrated. */
  spec: Spec | null = null;

  private observer: MutationObserver | null = null;
  private rowElements: HTMLTableRowElement[] = [];
  private bodyRows = new WeakMap<HTMLTableRowElement, BodyRow>();

  get state(): State | null {
    return this.getAttribute("data-gti-state") as State | null;
  }

  connectedCallback(): void {
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
    this.table = null;
    this.spec = null;
    this.rowElements = [];
    this.bodyRows = new WeakMap();
    this.removeAttribute("data-gti-state");
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
      this.setState("ready");
    } catch (err) {
      if (!(err instanceof SpecError)) {
        throw err;
      }
      // The static table still works; it just isn't interactive.
      console.warn(`<gt-table>: ${err.message}; the table is left static.`);
      this.setState("error");
    }
  }

  private mapRows(table: HTMLTableElement, spec: Spec): void {
    const trs = Array.from(
      table.querySelectorAll<HTMLTableRowElement>(":scope > tbody.gt_table_body > tr"),
    );
    if (trs.length !== spec.body.length) {
      throw new SpecError(
        `the table body has ${trs.length} rows but the spec describes ${spec.body.length}`,
      );
    }

    const rowElements: HTMLTableRowElement[] = [];
    const bodyRows = new WeakMap<HTMLTableRowElement, BodyRow>();
    trs.forEach((tr, i) => {
      const entry = spec.body[i] as BodyRow;
      bodyRows.set(tr, entry);
      if (typeof entry === "number") {
        rowElements[entry] = tr;
      }
    });
    this.rowElements = rowElements;
    this.bodyRows = bodyRows;
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
