// A GTI table in a Streamlit app (`st_gti()`, in great_tables/streamlit.py): a component
// (Streamlit's `st.components.v2`) showing the table's element, set from the data Python gives it,
// whose state Python reads, and sets (with `update_gti()`).
//
// Python runs the app's script again for each change the component makes to its state, and then
// gives it its data again (calling the component's function again, for the same element). Its
// state is one value (`gti`): the table's (`token`, as Python numbers each table it renders), its
// view, the rows the view keeps (in the order shown) and those selected, as last reported (`state`,
// with its own id, `report`, as it's sent again with each ask), and for a table in kernel mode,
// the asks for rows its source is waiting on (`asks`). The table's state is reported once it's
// hydrated, and after each change to it (the reader's, a linked table's selection, and Python's),
// unless it's what Python has already (its data's `known`), or what was reported last (while
// Python has what it had then).
//
// The data has the table's element (`html`): one that differs is a new table, shown with its own
// view. A table shown again, as when its component is mounted again, takes the view and selection
// Python has for it (`view`, `selection`); and Python's changes (`update`, numbered by its `nonce`)
// are set on the table once.
//
// A table in kernel mode (`i_scale(engine="kernel")`) is remote: its page has only some of its rows,
// and Python has them all (see great_tables/_gti/_kernel.py). Its source is a `StreamlitSource`,
// whose asks are in the state (as one that isn't answered yet stays there, through each run of the
// script), answered in the data (`answers`, by id). The rows its view keeps aren't reported (Python
// finds them).
//
// Built on its own (by scripts/build.mjs, into great_tables/js/gti-streamlit.js), as an ES module
// that's run after the runtime, so it imports nothing of it but its types (and src/host.ts).

import type { GtTable } from "./gt-table";
import { applyState, type HostView, SELECT_EVENT, SETTLED, ServerSource, VIEW_EVENT, viewOf } from "./host";

/** The table's state, as it's reported. */
export interface Reported {
  view: HostView;
  rows: number[] | null;
  selection: number[];
}

/** An ask for rows, as Python answers it. */
export interface Ask {
  id: string;
  kind: string;
  [part: string]: unknown;
}

/** The data Python gives the component. */
export interface Data {
  html: string;
  token: number;
  kernel: boolean;
  nrows: number;
  // (Whether the table's state is reported, or only its asks)
  report: boolean;
  view: Partial<Pick<HostView, "filter" | "sort" | "search">> | null;
  selection: number[] | null;
  known: Reported | null;
  update: { nonce: number; view?: Partial<Pick<HostView, "filter" | "sort" | "search">>; selection?: number[] } | null;
  answers: Record<string, { answer?: unknown; error?: string }> | null;
}

/** What the component's function is given (of what Streamlit gives it). */
export interface Component {
  data: Data;
  parentElement: HTMLElement | ShadowRoot;
  setStateValue(name: string, value: unknown): void;
}

// (A value as JSON, its objects' keys sorted, so that two values the same are the same text)
function canonical(value: unknown): string {
  return JSON.stringify(value, (_, item) =>
    item !== null && typeof item === "object" && !Array.isArray(item)
      ? Object.fromEntries(Object.keys(item).sort().map((key) => [key, item[key]]))
      : item,
  );
}

const equal = (a: unknown, b: unknown): boolean => canonical(a) === canonical(b);

/**
 * The rows of a table in kernel mode, from Python: each ask is put in the component's state
 * (with those still waiting), and its answer comes in the data.
 */
export class StreamlitSource extends ServerSource {
  // (Each table shown has its own asks' ids)
  private readonly view = Math.random().toString(36).slice(2);
  private asked = 0;
  private readonly pending = new Map<string, { ask: Ask; resolve: (answer: unknown) => void; reject: (err: Error) => void }>();

  constructor(
    nrows: number,
    private readonly send: () => void,
  ) {
    super(nrows);
  }

  /** The asks waiting on an answer. */
  get asks(): Ask[] {
    return Array.from(this.pending.values(), ({ ask }) => ask);
  }

  /** Take the answers in the data, to the asks they answer. */
  answer(answers: Data["answers"]): void {
    for (const [id, { resolve, reject }] of Array.from(this.pending)) {
      const answer = answers?.[id];
      if (answer !== undefined) {
        this.pending.delete(id);
        if (answer.error !== undefined) {
          reject(new Error(answer.error));
        } else {
          resolve(answer.answer);
        }
      }
    }
  }

  /** Drop the answers to come (as when the table is gone). */
  close(): void {
    for (const { reject } of this.pending.values()) {
      reject(new Error("the table is gone"));
    }
    this.pending.clear();
  }

  protected ask(kind: string, content: Record<string, unknown>): Promise<unknown> {
    const id = `${this.view}:${++this.asked}`;
    return new Promise((resolve, reject) => {
      this.pending.set(id, { ask: { id, kind, ...content }, resolve, reject });
      this.send();
    });
  }
}

/** A table shown by a component. */
interface Shown {
  html: string;
  token: number;
  table: GtTable;
  source: StreamlitSource | null;
  ready: boolean;
  // (The nonce of Python's change last set on the table)
  nonce: number | null;
  // (What was last reported, its id, what Python had then, and whether a report is waiting to be
  // sent)
  sent: Reported | null;
  report: string;
  basis: string;
  queued: boolean;
  // (The ids of the asks last sent)
  asked: string;
  stop: () => void;
}

/** A component, as its function is called again: the table it shows, and its latest data. */
interface Mounted {
  component: Component;
  shown: Shown | null;
}

const mounted = new WeakMap<HTMLElement | ShadowRoot, Mounted>();

function stateOf(shown: Shown, kernel: boolean): Reported {
  const { table } = shown;
  return { view: viewOf(table), rows: kernel ? null : table.rows, selection: table.selection };
}

// Send the component's state (in a microtask, so that a change's report and the asks it makes
// are sent at once, in one run of the script)
function send(mount: Mounted): void {
  const shown = mount.shown;
  if (shown === null || shown.queued) {
    return;
  }
  shown.queued = true;
  queueMicrotask(() => {
    shown.queued = false;
    if (mount.shown !== shown) {
      return;
    }
    const { data } = mount.component;
    const state = shown.ready && data.report ? stateOf(shown, data.kernel) : null;
    // (Not what Python has, nor what was last reported while it had the same, as Python's change
    // since makes it worth reporting again)
    const known = canonical(data.known);
    const reported =
      state !== null && !equal(state, data.known) && !(equal(state, shown.sent) && shown.basis === known)
        ? state
        : null;
    // (Those answered are left in the state, until it's sent again)
    const asks = shown.source?.asks ?? [];
    const ids = asks.map((ask) => ask.id).join(" ");
    if (reported === null && ids === shown.asked) {
      return;
    }
    if (reported !== null) {
      shown.sent = reported;
      shown.report = Math.random().toString(36).slice(2);
      shown.basis = known;
    }
    shown.asked = ids;
    mount.component.setStateValue("gti", { token: shown.token, report: shown.report, state: shown.sent, asks });
  });
}

// Show a table (the data's), in place of the one shown before
function show(mount: Mounted, root: HTMLElement | ShadowRoot): Shown {
  const { data } = mount.component;
  const doc = root.ownerDocument;
  const el = doc.createElement("div");
  el.innerHTML = data.html;
  root.append(el);
  const table = el.querySelector("gt-table") as GtTable;
  const shown: Shown = {
    html: data.html,
    token: data.token,
    table,
    source: null,
    ready: false,
    // (The data's view and selection have Python's changes)
    nonce: data.update?.nonce ?? null,
    sent: null,
    report: "",
    basis: "",
    queued: false,
    asked: "",
    stop: () => {},
  };
  // (Shown before its source is set, which may ask for rows at once)
  mount.shown = shown;
  if (data.kernel) {
    shown.source = new StreamlitSource(data.nrows, () => send(mount));
    table.source = shown.source;
  }

  const fromReader = () => send(mount);
  // (A linked table's selection changes the rows this one keeps, after it's shared)
  const fromLink = (event: Event) => {
    if (event.target !== table) {
      queueMicrotask(() => send(mount));
    }
  };
  // (Once hydrated, with Python's view and selection, unless it isn't interactive)
  const start = () => {
    shown.ready = table.state === "ready";
    if (shown.ready) {
      const { data } = mount.component;
      applyState(table, data.view, data.selection);
      send(mount);
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
  doc.addEventListener(SELECT_EVENT, fromLink);
  shown.stop = () => {
    observer.disconnect();
    table.removeEventListener(VIEW_EVENT, fromReader);
    table.removeEventListener(SELECT_EVENT, fromReader);
    doc.removeEventListener(SELECT_EVENT, fromLink);
    shown.source?.close();
    el.remove();
  };
  return shown;
}

/** The component's function: called with each run of the script's data. */
export default function render(component: Component): () => void {
  const root = component.parentElement;
  let mount = mounted.get(root);
  if (mount === undefined) {
    mount = { component, shown: null };
    mounted.set(root, mount);
  }
  mount.component = component;
  const { data } = component;

  let shown = mount.shown;
  if (shown === null || shown.html !== data.html || shown.token !== data.token) {
    shown?.stop();
    shown = show(mount, root);
  } else {
    // (Python's change, once, then its answers)
    const update = data.update;
    if (update !== null && update.nonce !== shown.nonce) {
      shown.nonce = update.nonce;
      if (shown.ready) {
        applyState(shown.table, update.view ?? null, update.selection ?? null);
        send(mount);
      }
    }
  }
  shown.source?.answer(data.answers);

  const current = mount;
  return () => {
    current.shown?.stop();
    current.shown = null;
    mounted.delete(root);
  };
}
