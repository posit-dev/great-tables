// A GTI table shown as an anywidget (`GTI.i_as_widget()`, in great_tables/_gti/_widget.py): the
// table's element, set from the model's `_html`, and its state kept in the model, for Python.
//
// The model has the table's view (`_view`), the rows it keeps (`_rows`) and those selected
// (`_selection`), as the browser has them: written after each change the reader makes, and after
// each one made from Python (as setting the element's properties fires no events). Python changes
// the view's filter, sort and search, and the selection, which are set on the element. A view
// shown again (as when its output is shown again) takes the model's state, and so do the others
// of a widget shown more than once. After a change the reader makes, a "change" message tells
// Python to call its callbacks.
//
// Built on its own (by scripts/build.mjs, into great_tables/js/gti-widget.js), as an ES module
// that's run after the runtime, so it imports nothing of it but its types.

import type { FilterQuery } from "./filter";
import type { GtTable, State } from "./gt-table";
import type { SortKey } from "./sort";

// (As gt-table.ts has them, as test/gt-table.test.ts checks)
export const VIEW_EVENT = "gt-table-view";
export const SELECT_EVENT = "gt-table-select";

/** The view, as the model has it (for Python, whose keys are snake case). */
export interface WidgetView {
  filter: FilterQuery | null;
  sort: SortKey[];
  search: string;
  page: number;
  page_size: number | null;
  hidden: string[];
  group_by: string | null;
}

/** What the glue uses of an anywidget model. */
export interface Model {
  get(name: string): unknown;
  set(name: string, value: unknown): void;
  save_changes(): void;
  send(content: unknown): void;
  on(event: string, callback: () => void): void;
  off(event: string, callback: () => void): void;
}

/** The table's view, from its properties. */
export function viewOf(table: GtTable): WidgetView {
  return {
    filter: table.filter,
    sort: table.sort,
    search: table.search,
    page: table.page,
    page_size: table.pageSize,
    hidden: table.hiddenColumns,
    group_by: table.groupBy,
  };
}

const same = (a: unknown, b: unknown): boolean => JSON.stringify(a) === JSON.stringify(b);

// (Which a table is in once it's done hydrating: interactive, or not, which it then stays)
const SETTLED: (State | null)[] = ["ready", "static", "error"];

function render({ model, el }: { model: Model; el: HTMLElement }): () => void {
  el.innerHTML = model.get("_html") as string;
  const table = el.querySelector("gt-table") as GtTable;
  let ready = false;
  // (While the glue writes to the model, which tells it of its own changes, as it makes them)
  let writing = false;

  // Write the table's state to the model, where it's changed (and with `told`, tell Python)
  const report = (told: boolean) => {
    const state: Record<string, unknown> = { _view: viewOf(table), _rows: table.rows, _selection: table.selection };
    const changed = Object.keys(state).filter((key) => !same(state[key], model.get(key)));
    if (changed.length > 0) {
      writing = true;
      try {
        for (const key of changed) {
          model.set(key, state[key]);
        }
      } finally {
        writing = false;
      }
      model.save_changes();
      if (told) {
        model.send({ type: "change" });
      }
    }
  };

  // Set the model's view and selection on the table, where they differ from its own
  const apply = () => {
    const view = model.get("_view") as WidgetView | null;
    const selection = model.get("_selection") as number[] | null;
    try {
      if (view != null) {
        if (!same(view.filter, table.filter)) {
          table.filter = view.filter;
        }
        if (!same(view.sort, table.sort)) {
          table.sort = view.sort;
        }
        if (view.search !== table.search) {
          table.search = view.search;
        }
      }
      if (selection != null && !same(selection, table.selection)) {
        table.selection = selection;
      }
    } catch (err) {
      console.error(`<gt-table>: ${(err as Error).message}`);
    }
  };

  const fromModel = () => {
    if (ready && !writing) {
      apply();
      report(false);
    }
  };
  const fromReader = () => {
    if (ready) {
      report(true);
    }
  };
  // (A linked table's selection changes the rows this one keeps, after it's shared)
  const fromLink = (event: Event) => {
    if (ready && event.target !== table) {
      queueMicrotask(() => report(true));
    }
  };

  // (Once hydrated, with the model's state, unless it isn't interactive, when it's left alone)
  const start = () => {
    ready = table.state === "ready";
    if (ready) {
      apply();
      report(false);
    }
  };
  const observer = new MutationObserver(() => {
    if (SETTLED.includes(table.state)) {
      observer.disconnect();
      start();
    }
  });
  if (SETTLED.includes(table.state)) {
    start();
  } else {
    observer.observe(table, { attributes: true, attributeFilter: ["data-gti-state"] });
  }

  table.addEventListener(VIEW_EVENT, fromReader);
  table.addEventListener(SELECT_EVENT, fromReader);
  const doc = el.ownerDocument;
  doc.addEventListener(SELECT_EVENT, fromLink);
  model.on("change:_view", fromModel);
  model.on("change:_selection", fromModel);
  return () => {
    observer.disconnect();
    table.removeEventListener(VIEW_EVENT, fromReader);
    table.removeEventListener(SELECT_EVENT, fromReader);
    doc.removeEventListener(SELECT_EVENT, fromLink);
    model.off("change:_view", fromModel);
    model.off("change:_selection", fromModel);
  };
}

export default { render };
