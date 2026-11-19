// A GTI table in a Panel app or notebook (`GTIPane`, in great_tables/panel.py): a Panel ESM
// component (`pn.custom.ReactiveESM`), which shows the table as a widget does (src/widget.ts),
// given a model of its own as the widget's.
//
// That model has the widget's state (`_view`, `_rows`, `_selection`), which is synced with Python
// as one parameter each way: the component's `_update`, which Python sets (with what it changes,
// and a count, so that each is a change), and `_report`, which the glue sets (with what the reader
// changed). One, as a notebook's Panel (from 1.8) has each change after the first of a message
// from the browser only once the next one comes. The table's HTML (`_html`), and whether its rows
// are in Python (`_kernel`, with `_nrows`), are the component's own; and its messages are Panel's
// (`send_msg()`, and "msg:custom" for Python's). A component shown twice has a view (and a model)
// for each, which follows the other's reports, as it does Python's changes.
//
// Then a notebook's Panel can send a change again after a later one, or lose a message: so each
// change is taken only if it's later than the last from where it's from (by its count), and an
// ask Python hasn't answered is asked again (Python answers it as it did).
//
// Built on its own (by scripts/build.mjs, into great_tables/js/gti-panel.js), as an ES module
// that's run after the runtime, so it imports nothing of it but its types (and src/host.ts).

import widget, { type Model } from "./widget";

/** What the glue uses of Panel's proxy of the component's model. */
export interface PanelModel {
  [name: string]: unknown;
  send_msg(content: unknown): void;
  on(event: string, callback: (content?: unknown) => void): void;
  off(event: string, callback: (content?: unknown) => void): void;
}

type Callback = (content?: unknown) => void;

const STATE = ["_view", "_rows", "_selection"];

// (How long an ask waits for its answer before it's asked again, doubled each time, until it's
// asked no more)
const ASK_AGAIN = 1000;
const ASK_LAST = 16000;

/** The component's model, as an anywidget's, and how to stop following its changes. */
export function modelOf(model: PanelModel): Model & { close(): void } {
  const id = Math.random().toString(36).slice(2);
  const state: Record<string, unknown> = {};
  const pending: Record<string, unknown> = {};
  const callbacks = new Map<string, Set<Callback>>();
  let count = 0;
  // (The count of the last change taken from Python, and from each other view, by its id)
  const last = new Map<unknown, number>();
  // (The asks unanswered, each with the timer to ask it again)
  const asks = new Map<string, ReturnType<typeof setTimeout>>();

  // (Python's changes, and another view's, set on the state, and each told)
  const take = (changes: unknown) => {
    if (changes === null || typeof changes !== "object") {
      return;
    }
    const { n, from } = changes as Record<string, unknown>;
    if (typeof n === "number") {
      if (n <= (last.get(from) ?? -1)) {
        return;
      }
      last.set(from, n);
    }
    const names = STATE.filter((name) => name in changes);
    for (const name of names) {
      state[name] = (changes as Record<string, unknown>)[name];
    }
    for (const name of names) {
      for (const callback of callbacks.get(`change:${name}`) ?? []) {
        callback();
      }
    }
  };
  take(model._update);
  const fromPython = () => take(model._update);
  const fromView = () => {
    const report = model._report as Record<string, unknown> | null;
    if (report !== null && typeof report === "object" && report.from !== id) {
      take(report);
    }
  };
  const answered = (content?: unknown) => {
    const message = content as { type?: unknown; id?: unknown } | null | undefined;
    if (message?.type === "answer" && typeof message.id === "string" && asks.has(message.id)) {
      clearTimeout(asks.get(message.id));
      asks.delete(message.id);
    }
  };
  const ask = (content: { id: string }, wait: number) => {
    model.send_msg(content);
    if (wait <= ASK_LAST) {
      asks.set(content.id, setTimeout(() => ask(content, wait * 2), wait));
    } else {
      asks.delete(content.id);
    }
  };
  model.on("change:_update", fromPython);
  model.on("change:_report", fromView);
  model.on("msg:custom", answered);

  return {
    // (The table's HTML has each `</` written with a NUL after the `<`, as Panel puts a notebook's
    // parameters in a script as they are, which the first `</script` would end)
    get: (name) =>
      name === "_html" ? String(model[name]).split("<\0/").join("</") : STATE.includes(name) ? state[name] : model[name],
    set: (name, value) => {
      state[name] = value;
      pending[name] = value;
    },
    save_changes: () => {
      if (Object.keys(pending).length > 0) {
        model._report = { ...pending, n: ++count, from: id };
        for (const name of Object.keys(pending)) {
          delete pending[name];
        }
      }
    },
    // (Python's told of the reader's changes by the report, so needs no message for them)
    send: (content) => {
      const message = content as { type?: unknown; id?: unknown } | null;
      if (message?.type === "ask" && typeof message.id === "string") {
        ask(message as { id: string }, ASK_AGAIN);
      } else if (message?.type !== "change") {
        model.send_msg(content);
      }
    },
    on: (event, callback) => {
      if (event.startsWith("change:")) {
        callbacks.set(event, (callbacks.get(event) ?? new Set()).add(callback));
      } else {
        model.on(event, callback);
      }
    },
    off: (event, callback) => {
      if (event.startsWith("change:")) {
        callbacks.get(event)?.delete(callback);
      } else {
        model.off(event, callback);
      }
    },
    close: () => {
      model.off("change:_update", fromPython);
      model.off("change:_report", fromView);
      model.off("msg:custom", answered);
      for (const timer of asks.values()) {
        clearTimeout(timer);
      }
      asks.clear();
    },
  };
}

/** The component's function: shows the table in the component's element, as a widget. */
export function render({ model, el }: { model: PanelModel; el: HTMLElement }): void {
  const glue = modelOf(model);
  const cleanup = widget.render({ model: glue, el });
  model.on("remove", () => {
    cleanup();
    glue.close();
  });
}
