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
// A table in kernel mode (`i_scale(engine="kernel")`) is remote: its page has only some of its
// rows, and Python has them all (see great_tables/_gti/_kernel.py). Its source is a
// `KernelSource`, which asks Python for each page (and a facet's counts) with an "ask" message,
// answered with an "answer" message; and the rows it keeps aren't in the model (Python has them).
//
// Built on its own (by scripts/build.mjs, into great_tables/js/gti-widget.js), as an ES module
// that's run after the runtime, so it imports nothing of it but its types (and src/host.ts).

import type { GtTable } from "./gt-table";
import { applyState, type HostView, SELECT_EVENT, SETTLED, ServerSource, same, VIEW_EVENT, viewOf } from "./host";

export { SELECT_EVENT, VIEW_EVENT, viewOf };

/** The view, as the model has it. */
export type WidgetView = HostView;

/** What the glue uses of an anywidget model. */
export interface Model {
  get(name: string): unknown;
  set(name: string, value: unknown): void;
  save_changes(): void;
  send(content: unknown): void;
  on(event: string, callback: (content?: unknown) => void): void;
  off(event: string, callback: (content?: unknown) => void): void;
}

/** What Python answers an "ask" message with: the answer, or why there's none. */
interface Answer {
  type: "answer";
  id: string;
  answer?: unknown;
  error?: string;
}

/**
 * The rows of a table in kernel mode, from Python: each answer is asked for with a message, and
 * comes in one.
 */
export class KernelSource extends ServerSource {
  // (Python answers every view of the widget, so each view's asks have their own ids)
  private readonly view = Math.random().toString(36).slice(2);
  private asked = 0;
  private readonly pending = new Map<string, { resolve: (answer: unknown) => void; reject: (err: Error) => void }>();

  constructor(
    private readonly model: Model,
    nrows: number,
  ) {
    super(nrows);
  }

  /** Take an answer from Python (a "msg:custom" message), if it's one this source asked for. */
  readonly onMessage = (content?: unknown): void => {
    const message = content as Partial<Answer> | null | undefined;
    if (message?.type !== "answer" || typeof message.id !== "string") {
      return;
    }
    const pending = this.pending.get(message.id);
    this.pending.delete(message.id);
    if (message.error !== undefined) {
      pending?.reject(new Error(message.error));
    } else {
      pending?.resolve(message.answer);
    }
  };

  /** Drop the answers to come (as when the table's view is gone). */
  close(): void {
    for (const { reject } of this.pending.values()) {
      reject(new Error("the table is gone"));
    }
    this.pending.clear();
  }

  protected ask(kind: string, content: Record<string, unknown>): Promise<unknown> {
    const id = `${this.view}:${++this.asked}`;
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      this.model.send({ type: "ask", id, kind, ...content });
    });
  }
}

function render({ model, el }: { model: Model; el: HTMLElement }): () => void {
  el.innerHTML = model.get("_html") as string;
  const table = el.querySelector("gt-table") as GtTable;
  // (The model says whether the table is in kernel mode, and how many rows it has)
  const kernel = model.get("_kernel") === true;
  const source = kernel ? new KernelSource(model, Number(model.get("_nrows"))) : null;
  if (source !== null) {
    table.source = source;
    model.on("msg:custom", source.onMessage);
  }
  let ready = false;
  // (While the glue writes to the model, which tells it of its own changes, as it makes them)
  let writing = false;

  // Write the table's state to the model, where it's changed (and with `told`, tell Python)
  const report = (told: boolean) => {
    const state: Record<string, unknown> = { _view: viewOf(table), _selection: table.selection };
    if (!kernel) {
      state._rows = table.rows;
    }
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
  const apply = () => applyState(table, model.get("_view") as WidgetView | null, model.get("_selection") as number[] | null);

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
    if (source !== null) {
      model.off("msg:custom", source.onMessage);
      source.close();
    }
  };
}

export default { render };
