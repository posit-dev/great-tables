import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import {
  type BodyRow,
  type CodeSpec,
  type ColumnSpec,
  type ControlsSpec,
  type DisplaySpec,
  define,
  EXPORT_EVENT,
  type ExportEventDetail,
  type ExportFormat,
  FILTER_EVENT,
  type FilterEventDetail,
  type FilterQuery,
  type FilterSpec,
  GtTable,
  type LayoutSpec,
  PAGE_EVENT,
  type PageEventDetail,
  type PaginationSpec,
  type QueryColumnSpec,
  RESIZE_EVENT,
  type ResizeEventDetail,
  SEARCH_EVENT,
  type SearchEventDetail,
  SELECT_EVENT,
  type SelectEventDetail,
  SORT_EVENT,
  type SortEventDetail,
  SPEC_VERSION,
  type SpannerSpec,
  type StripingSpec,
  TAG_NAME,
  VIEW_EVENT,
  type ViewEventDetail,
} from "../src/index";

// Let mutation observers run.
const tick = () => new Promise((resolve) => setTimeout(resolve, 0));

async function mount(html: string): Promise<GtTable> {
  document.body.innerHTML = html;
  await tick();
  return document.querySelector(TAG_NAME) as GtTable;
}

const specScript = (spec: object | string) =>
  `<script type="application/json" data-gti-spec>${
    typeof spec === "string" ? spec : JSON.stringify(spec)
  }</script>`;

// The data: a stub column `row` ("row_1", ...) and two sortable columns, `x` (with a missing
// value) and `y`
const X = ["20", "5", "10", "", "20"];
const Y = ["b", "a", "c", "a", "a"];
const RANKS = { row: [0, 1, 2, 3, 4], x: [2, 0, 1, null, 2], y: [1, 0, 2, 0, 0] };

// GT shows group "b" (rows 3, 0, 4, then a summary row) before group "a" (rows 1, 2), then a
// grand summary row
const GROUPED: BodyRow[] = [
  { group: "b" },
  3,
  0,
  4,
  { summary: "Total", group: "b", side: "bottom" },
  { group: "a" },
  1,
  2,
  { grand_summary: "Max", side: "bottom" },
];

interface TableOptions {
  striping?: StripingSpec;
  controls?: Partial<ControlsSpec>;
  /** Pagination is off unless set. */
  pagination?: Partial<PaginationSpec>;
  display?: Partial<DisplaySpec>;
  layout?: Partial<LayoutSpec>;
  groupsAsColumn?: boolean;
  yLabel?: string;
  /** The column label rows, if not one row of a label per column. */
  thead?: string;
  filters?: FilterSpec[];
  view?: object;
  /** The spanners over the column labels (in `thead`). */
  spanners?: SpannerSpec[];
  /** Export is off unless set. */
  export?: { formats: ExportFormat[]; filename?: string; code?: CodeSpec | null };
  /** The view isn't kept unless set. */
  viewState?: object;
  /** The columns only for querying, and their ranks. */
  queryColumns?: QueryColumnSpec[];
  queryRanks?: Record<string, (number | null)[]>;
  /** What readers can do with each column (by its id), if not everything, and where it's pinned. */
  columns?: Record<string, Pick<ColumnSpec, "sortable" | "searchable" | "resizable" | "pin" | "hideable" | "reorderable">>;
}

/** A table shaped like GT's, and its spec. */
function gtTable(body: BodyRow[], options: TableOptions = {}) {
  const striping = options.striping ?? { stub: false, body: false };
  const groupsAsColumn = options.groupsAsColumn ?? false;
  const cell = (tag: string, classes: string, text: string) =>
    `<${tag} class="${classes}">${text}</${tag}>`;

  let j = 0;
  let lead: string | null = null;
  const trs: string[] = [];
  const groups: { id: string | null; rows: number[] }[] = [];
  for (const entry of body) {
    if (typeof entry === "number") {
      groups[groups.length - 1]?.rows.push(entry);
    }
    if (typeof entry === "object" && "group" in entry && !("summary" in entry)) {
      groups.push({ id: entry.group, rows: [] });
      if (groupsAsColumn) {
        lead = entry.group;
      } else {
        trs.push(`<tr class="gt_group_heading_row"><th class="gt_group_heading" colspan="3">${entry.group}</th></tr>`);
      }
      continue;
    }
    const leading =
      lead === null ? "" : `<th class="gt_row gt_left gt_stub_row_group" rowspan="2">${lead}</th>`;
    const trClass = lead === null ? "" : ` class="gt_row_group_first"`;
    lead = null;

    if (typeof entry === "number") {
      const striped = (on: boolean) => (on && j % 2 === 1 ? " gt_striped" : "");
      trs.push(
        `<tr${trClass}>${leading}` +
          cell("th", `gt_row gt_left gt_stub${striped(striping.stub)}`, `row_${entry + 1}`) +
          cell("td", `gt_row gt_right${striped(striping.body)}`, X[entry] as string) +
          cell("td", `gt_row gt_left${striped(striping.body)}`, Y[entry] as string) +
          "</tr>",
      );
      j++;
    } else {
      const kind = "grand_summary" in entry ? "gt_grand_summary_row" : "gt_summary_row";
      const label = "grand_summary" in entry ? entry.grand_summary : entry.summary;
      trs.push(
        `<tr${trClass}>${leading}` +
          cell("th", `gt_row gt_left gt_stub ${kind}`, label) +
          cell("td", `gt_row gt_right ${kind}`, "-") +
          cell("td", `gt_row gt_left ${kind}`, "-") +
          "</tr>",
      );
    }
  }

  const thead =
    `<thead>${
      options.thead ??
      `<tr class="gt_col_headings"><th class="gt_col_heading"></th>` +
        `<th class="gt_col_heading gt_right" id="t-x">x</th>` +
        `<th class="gt_col_heading gt_left" id="t-y">${options.yLabel ?? "y"}</th></tr>`
    }</thead>`;
  const html =
    `<div id="t"><table class="gt_table">${thead}` +
    `<tbody class="gt_table_body">${trs.join("")}</tbody></table></div>`;

  const spec = {
    version: SPEC_VERSION,
    nrows: X.length,
    columns: [
      { id: "row", role: "stub", kind: "string", align: "left", header: null },
      { id: "x", role: "data", kind: "number", align: "right", header: "t-x" },
      { id: "y", role: "data", kind: "string", align: "left", header: "t-y" },
    ].map((column) => ({ ...column, ...options.columns?.[column.id] })),
    spanners: options.spanners ?? [],
    stub: { columns: ["row"], groups_as_column: groupsAsColumn },
    groups,
    body: groupsAsColumn
      ? body.filter((entry) => typeof entry !== "object" || !("group" in entry) || "summary" in entry)
      : body,
    ranks: { ...RANKS, ...options.queryRanks },
    striping,
    controls: { sorting: true, search: false, resizing: false, selection: null, ...options.controls },
    pagination: {
      enabled: false,
      page_size: 2,
      page_sizes: [2, 4],
      size_select: false,
      info: true,
      type: "numbers",
      ...options.pagination,
    },
    display: { highlight: false, compact: false, wrap: true, ...options.display },
    layout: { height: null, responsive: null, ...options.layout },
    ...(options.filters === undefined ? {} : { filters: options.filters }),
    ...(options.queryColumns === undefined ? {} : { query_columns: options.queryColumns }),
    ...(options.view === undefined ? {} : { view: options.view }),
    ...(options.export === undefined ? {} : { export: { filename: "table", ...options.export } }),
    ...(options.viewState === undefined ? {} : { view_state: options.viewState }),
  };
  return { html, spec };
}

async function mountTable(body: BodyRow[] = GROUPED, options: TableOptions = {}) {
  const { html, spec } = gtTable(body, options);
  return mount(`<gt-table>${html}${specScript(spec)}</gt-table>`);
}

/** The body as shown: data row indices, and labels for the structural rows. */
function shown(el: GtTable): (number | string)[] {
  const trs = el.querySelectorAll<HTMLTableRowElement>("tbody.gt_table_body > tr:not(.gt-i-empty)");
  return Array.from(trs).map((tr) => {
    const entry = el.bodyRow(tr);
    if (typeof entry === "number") {
      return entry;
    }
    if (entry === null) {
      return "?";
    }
    if ("grand_summary" in entry) {
      return `grand:${entry.grand_summary}`;
    }
    return "summary" in entry ? `summary:${entry.summary}` : `group:${entry.group}`;
  });
}

const header = (el: GtTable, column: string) =>
  el.querySelector(`th[id="t-${column}"]`) as HTMLTableCellElement;
const button = (el: GtTable, column: string) =>
  header(el, column).querySelector("button") as HTMLButtonElement;
const click = (el: GtTable, column: string, shiftKey = false) =>
  button(el, column).dispatchEvent(new MouseEvent("click", { bubbles: true, shiftKey }));

afterEach(() => {
  document.body.innerHTML = "";
  vi.restoreAllMocks();
});

describe("define()", () => {
  it("registers <gt-table> on import", () => {
    expect(customElements.get(TAG_NAME)).toBe(GtTable);
  });

  it("keeps the first registration when called again", () => {
    expect(define()).toBe(GtTable);
    expect(customElements.get(TAG_NAME)).toBe(GtTable);
  });

  it("returns the class already registered under the tag name", () => {
    class Other extends HTMLElement {}
    const registry = {
      get: (name: string) => (name === TAG_NAME ? Other : undefined),
      define: () => {
        throw new Error("should not be called");
      },
    } as unknown as CustomElementRegistry;
    expect(define(registry)).toBe(Other);
  });
});

describe("<gt-table>", () => {
  it("leaves a table without a spec static", async () => {
    const { html } = gtTable(GROUPED);
    const el = await mount(`<gt-table>${html}</gt-table>`);
    expect(el).toBeInstanceOf(GtTable);
    expect(el.table).toBe(el.querySelector("table.gt_table"));
    expect(el.spec).toBeNull();
    expect(el.state).toBe("static");
    expect(el.sortableColumns).toEqual([]);
    expect(el.querySelector("button")).toBeNull();
  });

  it("marks itself empty when there is no table", async () => {
    const el = await mount(`<gt-table></gt-table>`);
    expect(el.table).toBeNull();
    expect(el.state).toBe("empty");
  });

  it("hydrates a table added after it was connected", async () => {
    const el = await mount(`<gt-table></gt-table>`);
    const { html, spec } = gtTable(GROUPED);
    el.insertAdjacentHTML("beforeend", html + specScript(spec));
    await tick();
    expect(el.table).toBe(el.querySelector("table"));
    expect(el.state).toBe("ready");
  });

  it("keeps its table, and the sort, when moved", async () => {
    const el = await mountTable();
    el.sort = [{ column: "x" }];
    const before = shown(el);

    const host = document.createElement("section");
    document.body.append(host);
    host.append(el);
    await tick();

    expect(el.state).toBe("ready");
    expect(el.sort).toEqual([{ column: "x", descending: false }]);
    expect(shown(el)).toEqual(before);
    expect(el.querySelectorAll("button.gt-i-sort")).toHaveLength(2);
  });

  it("hydrates the new table when its children were replaced while detached", async () => {
    const el = await mountTable();
    el.sort = [{ column: "x" }];
    el.remove();
    const { html, spec } = gtTable(GROUPED);
    el.innerHTML = html + specScript(spec);
    document.body.append(el);
    await tick();

    expect(el.table).toBe(el.querySelector("table"));
    expect(el.sort).toEqual([]);
    expect(shown(el)).toEqual(["group:b", 3, 0, 4, "summary:Total", "group:a", 1, 2, "grand:Max"]);
    expect(el.querySelectorAll(".gt-i-live")).toHaveLength(1);
  });
});

describe("<gt-table> with a spec", () => {
  it("maps every body row to its spec entry", async () => {
    const { html, spec } = gtTable(GROUPED);
    const el = await mount(`<gt-table>${html}${specScript(spec)}</gt-table>`);

    expect(el.state).toBe("ready");
    expect(el.spec).toEqual(spec);

    const trs = Array.from(el.querySelectorAll("tbody tr")) as HTMLTableRowElement[];
    expect(trs.map((tr) => el.bodyRow(tr))).toEqual(GROUPED);
    for (const i of [0, 1, 2, 3, 4]) {
      expect(el.rowElement(i)?.querySelector("th")?.textContent).toBe(`row_${i + 1}`);
    }
    expect(el.rowElement(5)).toBeNull();
    expect(el.bodyRow(el.querySelector("thead tr") as HTMLTableRowElement)).toBeNull();
  });

  it("only reads its own spec", async () => {
    // A nested <gt-table>'s spec isn't this one's.
    const { html, spec } = gtTable(GROUPED);
    const el = await mount(`<gt-table>${html}<div>${specScript(spec)}</div></gt-table>`);
    expect(el.state).toBe("static");
  });

  it.each([
    ["an unusable spec", () => specScript("{"), /valid JSON/],
    [
      "another spec version",
      () => specScript({ ...gtTable(GROUPED).spec, version: 99 }),
      /version 99/,
    ],
    [
      "a spec for other rows",
      () => specScript({ ...gtTable(GROUPED).spec, body: GROUPED.slice(1) }),
      /9 rows .* 8/,
    ],
  ])("stays static and warns with %s", async (_, script, message) => {
    const warn = vi.spyOn(console, "warn").mockImplementation(() => {});
    const el = await mount(`<gt-table>${gtTable(GROUPED).html}${script()}</gt-table>`);

    expect(el.state).toBe("error");
    expect(el.table).not.toBeNull();
    expect(el.spec).toBeNull();
    expect(el.rowElement(0)).toBeNull();
    expect(el.sortableColumns).toEqual([]);
    expect(el.querySelector("button")).toBeNull();
    expect(warn).toHaveBeenCalledOnce();
    expect(warn.mock.calls[0]?.[0]).toMatch(message);
  });
});

describe("sorting", () => {
  it("makes the labels of sortable columns buttons", async () => {
    const el = await mountTable();

    expect(el.sortableColumns).toEqual(["row", "x", "y"]);
    // The stub has no label cell, so it's sortable through `sort` only
    expect(el.querySelectorAll("button.gt-i-sort")).toHaveLength(2);
    expect(button(el, "x").type).toBe("button");
    expect(button(el, "x").textContent).toBe("x");
    expect(button(el, "x").querySelector(".gt-i-sort-icon")?.getAttribute("aria-hidden")).toBe(
      "true",
    );
    expect(header(el, "x").hasAttribute("aria-sort")).toBe(false);
  });

  it("keeps the label's markup inside the button", async () => {
    const el = await mountTable(GROUPED, { yLabel: "<em>y</em> (<span>units</span>)" });

    expect(button(el, "y").querySelector("em")?.textContent).toBe("y");
    expect(button(el, "y").querySelector("span:not(.gt-i-sort-icon)")?.textContent).toBe("units");
    expect(header(el, "y").children).toHaveLength(1);
  });

  it("adds a separate button to a label with a link", async () => {
    const el = await mountTable(GROUPED, { yLabel: `y<a href="#note">1</a>` });
    const th = header(el, "y");

    expect(th.querySelector(":scope > a")?.textContent).toBe("1");
    expect(button(el, "y").textContent).toBe("");
    expect(button(el, "y").getAttribute("aria-label")).toBe("Sort by y1");
  });

  it("leaves footnote marks out of the label it announces", async () => {
    const el = await mountTable(GROUPED, {
      yLabel: `Long\n  label<span class="gt_footnote_marks">1</span>`,
    });
    click(el, "y");

    expect(button(el, "y").querySelector(".gt_footnote_marks")?.textContent).toBe("1");
    expect(el.querySelector(".gt-i-live")?.textContent).toBe("Sorted by Long label, ascending");
  });

  it("cycles a column through ascending, descending and unsorted on clicks", async () => {
    const el = await mountTable();

    click(el, "x");
    expect(shown(el)).toEqual(["group:b", 0, 4, 3, "summary:Total", "group:a", 1, 2, "grand:Max"]);
    expect(header(el, "x").getAttribute("aria-sort")).toBe("ascending");
    expect(header(el, "x").getAttribute("data-gti-sort")).toBe("ascending");

    click(el, "x");
    expect(shown(el)).toEqual(["group:b", 0, 4, 3, "summary:Total", "group:a", 2, 1, "grand:Max"]);
    expect(header(el, "x").getAttribute("aria-sort")).toBe("descending");

    click(el, "x");
    expect(shown(el)).toEqual(["group:b", 3, 0, 4, "summary:Total", "group:a", 1, 2, "grand:Max"]);
    expect(header(el, "x").hasAttribute("aria-sort")).toBe(false);
    expect(header(el, "x").hasAttribute("data-gti-sort")).toBe(false);
    expect(el.sort).toEqual([]);
  });

  it("sorts by another column alone on a click", async () => {
    const el = await mountTable();
    click(el, "x");
    click(el, "y");

    expect(el.sort).toEqual([{ column: "y", descending: false }]);
    expect(header(el, "x").hasAttribute("aria-sort")).toBe(false);
    expect(shown(el)).toEqual(["group:b", 3, 4, 0, "summary:Total", "group:a", 1, 2, "grand:Max"]);
  });

  it("sorts by several columns with Shift-click", async () => {
    const el = await mountTable();
    click(el, "y");
    click(el, "x", true);
    click(el, "x", true);

    expect(el.sort).toEqual([
      { column: "y", descending: false },
      { column: "x", descending: true },
    ]);
    expect(shown(el)).toEqual(["group:b", 4, 3, 0, "summary:Total", "group:a", 1, 2, "grand:Max"]);
    // Only the main sort column has `aria-sort`; both show their direction and position
    expect(header(el, "y").getAttribute("aria-sort")).toBe("ascending");
    expect(header(el, "x").hasAttribute("aria-sort")).toBe(false);
    expect(header(el, "x").getAttribute("data-gti-sort")).toBe("descending");
    const index = (column: string) =>
      header(el, column).querySelector(".gt-i-sort-icon")?.getAttribute("data-gti-sort-index");
    expect([index("y"), index("x")]).toEqual(["1", "2"]);

    click(el, "x", true);
    expect(el.sort).toEqual([{ column: "y", descending: false }]);
    expect(index("y")).toBeNull();
  });

  it("announces the sort, and fires an event, on clicks", async () => {
    const el = await mountTable();
    const events: SortEventDetail[] = [];
    document.addEventListener(SORT_EVENT, (event) => {
      events.push((event as CustomEvent<SortEventDetail>).detail);
    });
    const live = el.querySelector(".gt-i-live") as HTMLElement;
    expect(live.getAttribute("aria-live")).toBe("polite");
    expect(live.textContent).toBe("");

    click(el, "x");
    expect(live.textContent).toBe("Sorted by x, ascending");
    click(el, "y", true);
    expect(live.textContent).toBe("Sorted by x, ascending, then y, ascending");
    click(el, "y");
    click(el, "y");
    click(el, "y");
    expect(live.textContent).toBe("Not sorted");

    expect(events.map((detail) => detail.sort)).toEqual([
      [{ column: "x", descending: false }],
      [
        { column: "x", descending: false },
        { column: "y", descending: false },
      ],
      [{ column: "y", descending: false }],
      [{ column: "y", descending: true }],
      [],
    ]);
  });

  it("sorts when `sort` is set, without an event or an announcement", async () => {
    const el = await mountTable();
    const listener = vi.fn();
    el.addEventListener(SORT_EVENT, listener);

    el.sort = [{ column: "row", descending: true }];
    expect(shown(el)).toEqual(["group:b", 4, 3, 0, "summary:Total", "group:a", 2, 1, "grand:Max"]);
    expect(el.sort).toEqual([{ column: "row", descending: true }]);

    el.sort = [];
    expect(shown(el)).toEqual(["group:b", 3, 0, 4, "summary:Total", "group:a", 1, 2, "grand:Max"]);
    expect(listener).not.toHaveBeenCalled();
    expect(el.querySelector(".gt-i-live")?.textContent).toBe("");
  });

  it("rejects a sort by a column it can't sort", async () => {
    const el = await mountTable();
    el.sort = [{ column: "x" }];

    expect(() => {
      el.sort = [{ column: "nope" }];
    }).toThrow(RangeError);
    expect(el.sort).toEqual([{ column: "x", descending: false }]);
  });

  it("returns copies of the sort keys", async () => {
    const el = await mountTable();
    el.sort = [{ column: "x" }];
    const sort = el.sort;
    (sort[0] as { descending: boolean }).descending = true;
    expect(el.sort).toEqual([{ column: "x", descending: false }]);
  });

  it("sorts a table without groups as one block", async () => {
    const el = await mountTable([0, 1, 2, 3, 4]);
    click(el, "x");
    expect(shown(el)).toEqual([1, 2, 0, 4, 3]);
  });

  it("restripes the rows", async () => {
    const el = await mountTable(GROUPED, { striping: { stub: true, body: true } });
    const striped = () =>
      Array.from(el.querySelectorAll<HTMLTableRowElement>("tbody > tr"))
        .filter((tr) => typeof el.bodyRow(tr) === "number")
        .map((tr) => Array.from(tr.children).map((cell) => cell.classList.contains("gt_striped")));
    const off = [false, false, false];
    const on = [true, true, true];
    expect(striped()).toEqual([off, on, off, on, off]);

    click(el, "x");
    expect(striped()).toEqual([off, on, off, on, off]);
    expect(el.rowElement(4)?.querySelector("td")?.classList.contains("gt_striped")).toBe(true);
    expect(el.rowElement(0)?.querySelector("td")?.classList.contains("gt_striped")).toBe(false);
  });

  it("restripes only the parts GT striped", async () => {
    const el = await mountTable(GROUPED, { striping: { stub: false, body: true } });
    click(el, "x");
    const second = el.rowElement(4) as HTMLTableRowElement;
    expect(second.querySelector("th")?.classList.contains("gt_striped")).toBe(false);
    expect(second.querySelector("td")?.classList.contains("gt_striped")).toBe(true);
  });

  it("leaves the striping alone when GT didn't stripe", async () => {
    const el = await mountTable();
    click(el, "x");
    expect(el.querySelector(".gt_striped")).toBeNull();
  });

  it("keeps a group's label cell on its first row when groups are a column", async () => {
    const el = await mountTable(GROUPED, { groupsAsColumn: true });
    const groupCell = (row: number) => el.rowElement(row)?.querySelector(".gt_stub_row_group");
    expect(groupCell(3)?.textContent).toBe("b");

    click(el, "x");
    expect(shown(el)).toEqual([0, 4, 3, "summary:Total", 1, 2, "grand:Max"]);
    expect(groupCell(0)?.textContent).toBe("b");
    expect(groupCell(3)).toBeNull();
    expect(el.rowElement(0)?.classList.contains("gt_row_group_first")).toBe(true);
    expect(el.rowElement(3)?.classList.contains("gt_row_group_first")).toBe(false);

    click(el, "x");
    expect(groupCell(2)?.textContent).toBe("a");
    expect(groupCell(1)).toBeNull();
    // Each group label cell is still the first cell of its row
    expect(el.rowElement(2)?.firstElementChild?.textContent).toBe("a");
  });

  it("leaves a group's label cell on a top summary row", async () => {
    const body: BodyRow[] = [{ group: "a" }, { summary: "Total", group: "a", side: "top" }, 1, 2];
    const el = await mountTable(body, { groupsAsColumn: true });
    const summary = el.querySelector("tbody > tr") as HTMLTableRowElement;

    click(el, "x");
    click(el, "x");
    expect(shown(el)).toEqual(["summary:Total", 2, 1]);
    expect(summary.querySelector(".gt_stub_row_group")?.textContent).toBe("a");
    expect(el.querySelectorAll(".gt_stub_row_group")).toHaveLength(1);
  });

  it("keeps groups shown as a column apart without summary rows between them", async () => {
    const body: BodyRow[] = [{ group: "b" }, 3, 0, 4, { group: "a" }, 1, 2];
    const el = await mountTable(body, { groupsAsColumn: true });
    click(el, "x");
    expect(shown(el)).toEqual([0, 4, 3, 1, 2]);
    const groupCell = (row: number) => el.rowElement(row)?.querySelector(".gt_stub_row_group");
    expect(groupCell(0)?.textContent).toBe("b");
    expect(groupCell(1)?.textContent).toBe("a");
  });

  it("doesn't sort a table whose stub has merged cells", async () => {
    const { html, spec } = gtTable([0, 1, 2, 3, 4]);
    const merged = html.replace(
      `<th class="gt_row gt_left gt_stub">row_1</th>`,
      `<th class="gt_row gt_left gt_stub" rowspan="2">row_1</th>`,
    );
    const el = await mount(`<gt-table>${merged}${specScript(spec)}</gt-table>`);

    expect(el.state).toBe("ready");
    expect(el.sortableColumns).toEqual([]);
    expect(el.querySelector("button")).toBeNull();
    expect(() => {
      el.sort = [{ column: "x" }];
    }).toThrow(RangeError);
  });
});

/** The body rows that aren't hidden, as `shown()` gives them. */
function visible(el: GtTable): (number | string)[] {
  const trs = Array.from(
    el.querySelectorAll<HTMLTableRowElement>("tbody.gt_table_body > tr:not(.gt-i-empty)"),
  );
  const all = shown(el);
  return all.filter((_, i) => !(trs[i] as HTMLTableRowElement).hidden);
}

const live = (el: GtTable) => el.querySelector(".gt-i-live")?.textContent;
const searchBox = (el: GtTable) => el.querySelector<HTMLInputElement>("input.gt-i-search");

describe("searching", () => {
  it("shows the rows that match, keeping their group's heading and summary rows", async () => {
    const el = await mountTable();
    el.search = "a";

    expect(el.search).toBe("a");
    expect(visible(el)).toEqual(["group:b", 3, 4, "summary:Total", "group:a", 1, "grand:Max"]);
    // Rows stay where they are, hidden
    expect(shown(el)).toEqual(["group:b", 3, 0, 4, "summary:Total", "group:a", 1, 2, "grand:Max"]);
  });

  it("hides a group without matches, but not the grand summary", async () => {
    const el = await mountTable();
    el.search = "c";
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
  });

  it("ignores case and accents", async () => {
    const el = await mountTable();
    el.search = "RÓW_3";
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
  });

  it("needs every word of the search in the row, each in one of its cells", async () => {
    const el = await mountTable();
    el.search = "row_1 20";
    expect(visible(el)).toEqual(["group:b", 0, "summary:Total", "grand:Max"]);
    el.search = "  20   ";
    expect(visible(el)).toEqual(["group:b", 0, 4, "summary:Total", "grand:Max"]);
    // Not across cells
    el.search = "520";
    expect(visible(el)).toEqual(["grand:Max"]);
  });

  it("doesn't search group headings or summary rows", async () => {
    const el = await mountTable();
    el.search = "total";
    expect(visible(el)).toEqual(["grand:Max"]);
  });

  it("says so when nothing matches, until the search changes", async () => {
    const el = await mountTable();
    el.search = "zzz";
    const empty = el.querySelector("tr.gt-i-empty") as HTMLTableRowElement;
    expect(empty.querySelector("td")?.textContent).toBe("No matching rows");
    expect(empty.querySelector("td")?.colSpan).toBe(3);
    // Where the data rows would be, and not a body row
    expect(empty.nextElementSibling).toBe(el.querySelector(".gt_grand_summary_row")?.parentElement);
    expect(el.bodyRow(empty)).toBeNull();

    el.search = "zz";
    expect(el.querySelectorAll("tr.gt-i-empty")).toHaveLength(1);
    el.search = "";
    expect(el.querySelector("tr.gt-i-empty")).toBeNull();
    expect(visible(el)).toEqual(shown(el));
  });

  it("puts the empty row at the end of a body without grand summary rows at the bottom", async () => {
    const body: BodyRow[] = [{ grand_summary: "Max", side: "top" }, 0, 1, 2, 3, 4];
    const el = await mountTable(body);
    el.search = "zzz";
    expect(el.querySelector("tbody")?.lastElementChild?.className).toBe("gt-i-empty");
    expect(visible(el)).toEqual(["grand:Max"]);
  });

  it("shows every row for a blank search", async () => {
    const el = await mountTable();
    el.search = "a";
    el.search = " ";
    expect(visible(el)).toEqual(shown(el));
    expect(el.querySelector("tr.gt-i-empty")).toBeNull();
  });

  it("keeps the search when sorting, and the sort when searching", async () => {
    const el = await mountTable();
    el.search = "a";
    click(el, "x");
    expect(visible(el)).toEqual(["group:b", 4, 3, "summary:Total", "group:a", 1, "grand:Max"]);
    el.search = "";
    expect(visible(el)).toEqual(["group:b", 0, 4, 3, "summary:Total", "group:a", 1, 2, "grand:Max"]);
  });

  it("restripes the rows it shows", async () => {
    const el = await mountTable(GROUPED, { striping: { stub: true, body: true } });
    const striped = () =>
      Array.from(el.querySelectorAll<HTMLTableRowElement>("tbody > tr"))
        .filter((tr) => typeof el.bodyRow(tr) === "number" && !tr.hidden)
        .map((tr) => (tr.querySelector("td") as HTMLElement).classList.contains("gt_striped"));

    el.search = "a";
    expect(striped()).toEqual([false, true, false]);
    expect(el.rowElement(4)?.querySelector("th")?.classList.contains("gt_striped")).toBe(true);
    el.search = "";
    expect(striped()).toEqual([false, true, false, true, false]);
  });

  it("moves a group's label cell to its first shown row when groups are a column", async () => {
    const el = await mountTable(GROUPED, { groupsAsColumn: true });
    const groupCell = (row: number) =>
      el.rowElement(row)?.querySelector<HTMLTableCellElement>(".gt_stub_row_group") ?? null;

    el.search = "row_5";
    expect(visible(el)).toEqual([4, "summary:Total", "grand:Max"]);
    expect(groupCell(4)?.textContent).toBe("b");
    // Its shown data row and the summary row
    expect(groupCell(4)?.getAttribute("rowspan")).toBe("2");
    expect(el.rowElement(4)?.classList.contains("gt_row_group_first")).toBe(true);
    expect(el.rowElement(3)?.classList.contains("gt_row_group_first")).toBe(false);

    el.search = "c";
    expect(visible(el)).toEqual([2, "grand:Max"]);
    expect(groupCell(2)?.textContent).toBe("a");
    expect(groupCell(2)?.getAttribute("rowspan")).toBe("1");

    // Back on each group's first row
    el.search = "";
    expect(groupCell(3)?.getAttribute("rowspan")).toBe("4");
    expect(groupCell(1)?.getAttribute("rowspan")).toBe("2");
    expect(el.querySelectorAll(".gt_stub_row_group")).toHaveLength(2);
  });

  it("doesn't search a group's label cell", async () => {
    const el = await mountTable(GROUPED, { groupsAsColumn: true });
    // Only row 0's own cells have a "b"; group b's label cell is on row 3
    el.search = "b";
    expect(visible(el)).toEqual([0, "summary:Total", "grand:Max"]);
  });

  it("leaves a table whose stub has merged cells unfiltered", async () => {
    const { html, spec } = gtTable([0, 1, 2, 3, 4], { controls: { search: true } });
    const merged = html.replace(
      `<th class="gt_row gt_left gt_stub">row_1</th>`,
      `<th class="gt_row gt_left gt_stub" rowspan="2">row_1</th>`,
    );
    const el = await mount(`<gt-table>${merged}${specScript(spec)}</gt-table>`);
    el.search = "c";

    expect(visible(el)).toEqual([0, 1, 2, 3, 4]);
    expect(searchBox(el)).toBeNull();
  });

  it("searches once hydrated when `search` is set before", async () => {
    const { html, spec } = gtTable(GROUPED, { controls: { search: true } });
    const el = document.createElement(TAG_NAME) as GtTable;
    el.search = "c";
    el.innerHTML = html + specScript(spec);
    document.body.append(el);
    await tick();

    expect(el.state).toBe("ready");
    expect(el.search).toBe("c");
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
    expect(searchBox(el)?.value).toBe("c");
  });

  it("forgets the search when its table is replaced", async () => {
    const el = await mountTable();
    el.search = "c";
    el.remove();
    const { html, spec } = gtTable(GROUPED);
    el.innerHTML = html + specScript(spec);
    document.body.append(el);
    await tick();

    expect(el.search).toBe("");
    expect(visible(el)).toEqual(shown(el));
  });
});

describe("the search box", () => {
  afterEach(() => {
    vi.useRealTimers();
  });

  const type = (input: HTMLInputElement, value: string) => {
    input.value = value;
    input.dispatchEvent(new Event("input", { bubbles: true }));
  };
  const press = (input: HTMLInputElement, key: string) => {
    const event = new KeyboardEvent("keydown", { key, bubbles: true, cancelable: true });
    input.dispatchEvent(event);
    return event;
  };

  async function mountSearch() {
    const el = await mountTable(GROUPED, { controls: { search: true } });
    const events: SearchEventDetail[] = [];
    el.addEventListener(SEARCH_EVENT, (event) => {
      events.push((event as CustomEvent<SearchEventDetail>).detail);
    });
    return { el, input: searchBox(el) as HTMLInputElement, events };
  }

  it("is a labelled search field in a toolbar before the table", async () => {
    const { el, input } = await mountSearch();
    const toolbar = el.firstElementChild as HTMLElement;

    expect(toolbar.className).toBe("gt-i-toolbar");
    expect(input.parentElement).toBe(toolbar);
    expect(input.type).toBe("search");
    expect(input.getAttribute("aria-label")).toBe("Search the table");
    expect(input.getAttribute("enterkeyhint")).toBe("search");
    expect(input.getAttribute("autocomplete")).toBe("off");
    expect(input.value).toBe("");
    expect(el.querySelector(".gt-i-live")?.getAttribute("aria-live")).toBe("polite");
  });

  it("searches once typing pauses", async () => {
    const { el, input, events } = await mountSearch();
    vi.useFakeTimers();

    type(input, "a");
    vi.advanceTimersByTime(100);
    type(input, "c");
    vi.advanceTimersByTime(100);
    expect(el.search).toBe("");
    expect(events).toEqual([]);

    vi.advanceTimersByTime(50);
    expect(el.search).toBe("c");
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
    expect(events).toEqual([{ search: "c", count: 1 }]);
    expect(live(el)).toBe("Showing 1 of 5 rows");
  });

  it("searches at once on Enter, and only when the search changed", async () => {
    const { el, input, events } = await mountSearch();
    vi.useFakeTimers();

    type(input, "a");
    press(input, "Enter");
    expect(events).toEqual([{ search: "a", count: 3 }]);
    expect(live(el)).toBe("Showing 3 of 5 rows");

    vi.advanceTimersByTime(500);
    press(input, "Enter");
    expect(events).toHaveLength(1);

    type(input, "zzz");
    press(input, "Enter");
    expect(events[1]).toEqual({ search: "zzz", count: 0 });
    expect(live(el)).toBe("No matching rows");
  });

  it("clears the search on Escape", async () => {
    const { el, input, events } = await mountSearch();
    type(input, "a");
    press(input, "Enter");

    const escape = press(input, "Escape");
    expect(escape.defaultPrevented).toBe(true);
    expect(input.value).toBe("");
    expect(el.search).toBe("");
    expect(visible(el)).toEqual(shown(el));
    expect(events[1]).toEqual({ search: "", count: 5 });
    expect(live(el)).toBe("Showing all 5 rows");

    // With nothing to clear, Escape is left to the page
    expect(press(input, "Escape").defaultPrevented).toBe(false);
    expect(events).toHaveLength(2);
  });

  it("follows `search` when it's set, without an event or an announcement", async () => {
    const { el, input, events } = await mountSearch();
    vi.useFakeTimers();
    type(input, "a");
    el.search = "c";
    // The pending search from typing is dropped
    vi.advanceTimersByTime(500);

    expect(input.value).toBe("c");
    expect(el.search).toBe("c");
    expect(events).toEqual([]);
    expect(live(el)).toBe("");
  });

  it("takes the table's font", async () => {
    const { el } = await mountSearch();
    const toolbar = el.querySelector(".gt-i-toolbar") as HTMLElement;
    expect(toolbar.style.fontFamily).toBe(getComputedStyle(el.table as HTMLTableElement).fontFamily);
  });
});

describe("controls", () => {
  it("has sort buttons and no search box by default", async () => {
    const el = await mountTable();
    expect(el.querySelectorAll("button.gt-i-sort")).toHaveLength(2);
    expect(el.querySelector(".gt-i-toolbar")).toBeNull();
  });

  it("leaves out the sort buttons when sorting is off, but sorts through `sort`", async () => {
    const el = await mountTable(GROUPED, { controls: { sorting: false } });
    expect(el.querySelector("button")).toBeNull();
    expect(el.querySelector(".gt-i-live")).toBeNull();
    expect(el.sortableColumns).toEqual(["row", "x", "y"]);

    el.sort = [{ column: "x" }];
    expect(shown(el)).toEqual(["group:b", 0, 4, 3, "summary:Total", "group:a", 1, 2, "grand:Max"]);
  });

  it("searches through `search` without a search box", async () => {
    const el = await mountTable();
    el.search = "c";
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
  });

  it("has a search box and no sort buttons when asked", async () => {
    const el = await mountTable(GROUPED, { controls: { sorting: false, search: true } });
    expect(el.querySelector("button")).toBeNull();
    expect(searchBox(el)).not.toBeNull();
    expect(el.querySelectorAll(".gt-i-live")).toHaveLength(1);
  });
});

describe("pagination", () => {
  // Pages of 2 rows: [3, 0], [4, 1] and [2]
  const paged = (options: TableOptions = {}) =>
    mountTable(GROUPED, { ...options, pagination: { enabled: true, ...options.pagination } });

  it("shows the first page", async () => {
    const el = await paged();
    expect([el.page, el.pageSize, el.pageCount]).toEqual([1, 2, 3]);
    expect(visible(el)).toEqual(["group:b", 3, 0, "grand:Max"]);
    // Every row stays in the table
    expect(shown(el)).toEqual(["group:b", 3, 0, 4, "summary:Total", "group:a", 1, 2, "grand:Max"]);
  });

  it("repeats a group's heading on each of its pages, and the grand summary rows on every page", async () => {
    const el = await paged();
    el.page = 2;
    expect(visible(el)).toEqual(["group:b", 4, "summary:Total", "group:a", 1, "grand:Max"]);
    el.page = 3;
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
  });

  it("shows top summary rows where the group starts and bottom ones where it ends", async () => {
    const body: BodyRow[] = [
      { grand_summary: "Min", side: "top" },
      { group: "b" },
      { summary: "Top", group: "b", side: "top" },
      3,
      0,
      4,
      { summary: "Total", group: "b", side: "bottom" },
      { group: "a" },
      1,
      2,
    ];
    const el = await mountTable(body, { pagination: { enabled: true } });
    expect(visible(el)).toEqual(["grand:Min", "group:b", "summary:Top", 3, 0]);
    el.page = 2;
    expect(visible(el)).toEqual(["grand:Min", "group:b", 4, "summary:Total", "group:a", 1]);
  });

  it("takes a page past the last as the last, and rejects pages that aren't positive integers", async () => {
    const el = await paged();
    el.page = 9;
    expect(el.page).toBe(3);
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
    for (const page of [0, -1, 1.5, Number.NaN]) {
      expect(() => {
        el.page = page;
      }).toThrow(RangeError);
    }
    expect(el.page).toBe(3);
  });

  it("goes back to the first page on a new sort or search", async () => {
    const el = await paged();
    el.page = 2;
    click(el, "x");
    expect(el.page).toBe(1);
    el.page = 2;
    el.sort = [];
    expect(el.page).toBe(1);
    el.page = 2;
    el.search = "a";
    expect(el.page).toBe(1);
  });

  it("pages the rows that match the search, in sorted order", async () => {
    const el = await paged();
    el.search = "a";
    expect(el.pageCount).toBe(2);
    expect(visible(el)).toEqual(["group:b", 3, 4, "summary:Total", "grand:Max"]);
    el.page = 2;
    expect(visible(el)).toEqual(["group:a", 1, "grand:Max"]);

    el.sort = [{ column: "x", descending: true }];
    expect(visible(el)).toEqual(["group:b", 4, 3, "summary:Total", "grand:Max"]);
    el.search = "zzz";
    expect([el.page, el.pageCount]).toEqual([1, 1]);
    expect(visible(el)).toEqual(["grand:Max"]);
  });

  it("keeps the first row of the page in view when the page size changes", async () => {
    const el = await paged();
    el.page = 3;
    el.pageSize = 4;
    // Row 5 of 5 is on page 2 of 4 rows
    expect([el.page, el.pageCount]).toEqual([2, 2]);
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
    el.pageSize = 1;
    expect([el.page, el.pageCount]).toEqual([5, 5]);

    el.pageSize = null;
    expect([el.page, el.pageSize, el.pageCount]).toEqual([1, null, 1]);
    expect(visible(el)).toEqual(shown(el));
    for (const size of [0, 2.5, -2]) {
      expect(() => {
        el.pageSize = size;
      }).toThrow(RangeError);
    }
  });

  it("restripes each page from its first row", async () => {
    const el = await paged({ striping: { stub: true, body: true } });
    const striped = () =>
      Array.from(el.querySelectorAll<HTMLTableRowElement>("tbody > tr"))
        .filter((tr) => typeof el.bodyRow(tr) === "number" && !tr.hidden)
        .map((tr) => (tr.querySelector("td") as HTMLElement).classList.contains("gt_striped"));
    expect(striped()).toEqual([false, true]);
    el.page = 3;
    expect(striped()).toEqual([false]);
  });

  it("puts a group's label cell on its first row on the page when groups are a column", async () => {
    const el = await paged({ groupsAsColumn: true });
    const groupCell = (row: number) =>
      el.rowElement(row)?.querySelector<HTMLTableCellElement>(".gt_stub_row_group") ?? null;

    expect(groupCell(3)?.getAttribute("rowspan")).toBe("2");
    el.page = 2;
    // Row 4 and the summary row; row 1
    expect(visible(el)).toEqual([4, "summary:Total", 1, "grand:Max"]);
    expect(groupCell(4)?.textContent).toBe("b");
    expect(groupCell(4)?.getAttribute("rowspan")).toBe("2");
    expect(groupCell(1)?.getAttribute("rowspan")).toBe("1");
    expect(el.rowElement(4)?.classList.contains("gt_row_group_first")).toBe(true);
    expect(el.rowElement(3)?.classList.contains("gt_row_group_first")).toBe(false);

    el.pageSize = null;
    expect(groupCell(3)?.getAttribute("rowspan")).toBe("4");
    expect(groupCell(1)?.getAttribute("rowspan")).toBe("2");
  });

  it("keeps a group's label cell on its top summary row on the page where the group starts", async () => {
    const body: BodyRow[] = [{ group: "b" }, { summary: "Top", group: "b", side: "top" }, 3, 0, 4, { group: "a" }, 1, 2];
    const el = await mountTable(body, { groupsAsColumn: true, pagination: { enabled: true } });
    const top = el.querySelector(".gt_summary_row")?.parentElement as HTMLTableRowElement;
    const cell = el.querySelector(".gt_stub_row_group") as HTMLTableCellElement;

    expect(cell.parentElement).toBe(top);
    expect(cell.getAttribute("rowspan")).toBe("3");
    el.page = 2;
    expect(cell.parentElement).toBe(el.rowElement(4));
    expect(cell.getAttribute("rowspan")).toBe("1");
    el.page = 1;
    expect(cell.parentElement).toBe(top);
    expect(top.classList.contains("gt_row_group_first")).toBe(true);
  });

  it("isn't on unless the spec says so, but `pageSize` turns it on", async () => {
    const el = await mountTable();
    expect([el.page, el.pageSize, el.pageCount]).toEqual([1, null, 1]);
    expect(el.querySelector(".gt-i-pager")).toBeNull();
    el.pageSize = 2;
    expect(visible(el)).toEqual(["group:b", 3, 0, "grand:Max"]);
    expect(el.querySelector(".gt-i-pager")).not.toBeNull();
  });

  it("applies a page and page size set before hydration", async () => {
    const { html, spec } = gtTable(GROUPED, { pagination: { enabled: true, page_size: 4 } });
    const el = document.createElement(TAG_NAME) as GtTable;
    el.pageSize = 2;
    el.page = 2;
    expect([el.page, el.pageSize]).toEqual([2, 2]);
    el.innerHTML = html + specScript(spec);
    document.body.append(el);
    await tick();

    expect([el.page, el.pageSize, el.pageCount]).toEqual([2, 2, 3]);
    expect(visible(el)).toEqual(["group:b", 4, "summary:Total", "group:a", 1, "grand:Max"]);
  });

  it("doesn't page a table whose stub has merged cells", async () => {
    const { html, spec } = gtTable([0, 1, 2, 3, 4], { pagination: { enabled: true } });
    const merged = html.replace(
      `<th class="gt_row gt_left gt_stub">row_1</th>`,
      `<th class="gt_row gt_left gt_stub" rowspan="2">row_1</th>`,
    );
    const el = await mount(`<gt-table>${merged}${specScript(spec)}</gt-table>`);
    el.page = 2;

    expect([el.page, el.pageSize, el.pageCount]).toEqual([1, null, 1]);
    expect(visible(el)).toEqual([0, 1, 2, 3, 4]);
    expect(el.querySelector(".gt-i-pager")).toBeNull();
  });
});

describe("padding short pages", () => {
  // (happy-dom has no layout: a row is 20px tall, or as tall as set, and a body as its rows shown)
  const layOut = (laidOut = true) => {
    const height = (tr: Element) => parseFloat((tr as HTMLElement).style.height) || 20;
    vi.spyOn(Element.prototype, "getClientRects").mockImplementation(
      () => (laidOut ? [new DOMRect(0, 0, 100, 20)] : []) as unknown as DOMRectList,
    );
    vi.spyOn(Element.prototype, "getBoundingClientRect").mockImplementation(function (this: Element) {
      if (this.tagName === "TR") {
        return new DOMRect(0, 0, 100, height(this));
      }
      if (this.tagName === "TBODY") {
        const rows = Array.from(this.children).filter((tr) => !(tr as HTMLElement).hidden);
        return new DOMRect(0, 0, 100, rows.reduce((sum, tr) => sum + height(tr), 0));
      }
      return new DOMRect(0, 0, 100, 20);
    });
  };
  // Pages of 2 rows: [0, 1], [2, 3] and [4], then a grand summary row
  const UNGROUPED: BodyRow[] = [0, 1, 2, 3, 4, { grand_summary: "Max", side: "bottom" }];
  const paged = (body: BodyRow[] = UNGROUPED, options: TableOptions = {}) => {
    layOut();
    return mountTable(body, { ...options, pagination: { enabled: true, ...options.pagination } });
  };
  const fillers = (el: GtTable) => Array.from(el.querySelectorAll<HTMLTableRowElement>("tbody tr.gt-i-filler"));

  it("pads a short page with empty rows, to a full page's height", async () => {
    const el = await paged();
    expect(fillers(el)).toEqual([]);
    el.page = 3;
    // (Before the grand summary rows at the bottom)
    expect(visible(el)).toEqual([4, "?", "grand:Max"]);
    const [tr] = fillers(el) as [HTMLTableRowElement];
    expect(tr.getAttribute("aria-hidden")).toBe("true");
    expect(tr.style.height).toBe("20px");
    expect(el.bodyRow(tr)).toBeNull();
    // An empty cell in each column, with the stub's class (for its borders), and none of a data
    // row's others
    expect(Array.from(tr.cells, (cell) => [cell.tagName, cell.className, cell.textContent])).toEqual([
      ["TD", "gt_row gt_stub", ""],
      ["TD", "gt_row", ""],
      ["TD", "gt_row", ""],
    ]);
    // Not counted
    expect(el.querySelector(".gt-i-page-info")?.textContent).toBe("5 of 5 rows");

    el.page = 1;
    expect(fillers(el)).toEqual([]);
    expect(visible(el)).toEqual([0, 1, "grand:Max"]);
  });

  it("pads the rows a search finds, and the row saying that none do", async () => {
    const el = await paged(UNGROUPED, { controls: { search: true } });
    el.search = "row_3";
    expect(visible(el)).toEqual([2, "?", "grand:Max"]);
    el.search = "zzz";
    const trs = Array.from(el.querySelectorAll("tbody tr")).filter((tr) => !(tr as HTMLElement).hidden);
    expect(trs.map((tr) => tr.className)).toEqual(["gt-i-empty", "gt-i-filler", ""]);
    el.search = "";
    expect(fillers(el)).toEqual([]);
  });

  it("isn't done when every row fits on a page, or the table isn't laid out", async () => {
    const el = await paged();
    el.pageSize = 5;
    expect(fillers(el)).toEqual([]);
    el.pageSize = null;
    expect(fillers(el)).toEqual([]);

    vi.restoreAllMocks();
    layOut(false);
    const hidden = await mountTable(UNGROUPED, { pagination: { enabled: true } });
    hidden.page = 3;
    expect(fillers(hidden)).toEqual([]);
  });

  it("pads to a full page's height at the new page size", async () => {
    const el = await paged();
    el.pageSize = 3;
    el.page = 2;
    expect(visible(el)).toEqual([3, 4, "?", "grand:Max"]);
    el.pageSize = 4;
    el.page = 2;
    expect(visible(el)).toEqual([4, "?", "?", "?", "grand:Max"]);
  });

  it("has a cell in the selection column and the row group column, without a checkbox", async () => {
    const el = await paged(GROUPED, { groupsAsColumn: true, controls: { selection: "multiple" } });
    el.page = 3;
    const [tr] = fillers(el) as [HTMLTableRowElement];
    expect(Array.from(tr.cells, (cell) => cell.className)).toEqual([
      "gt_row gt-i-select",
      "gt_row gt_stub_row_group",
      "gt_row gt_stub",
      "gt_row",
      "gt_row",
    ]);
    expect(tr.querySelector("input")).toBeNull();
    // Clicking it selects nothing
    (tr.cells[3] as HTMLElement).click();
    expect(el.selection).toEqual([]);
  });
});

describe("the page controls", () => {
  const pager = (el: GtTable) => el.querySelector(".gt-i-pager") as HTMLElement;
  const info = (el: GtTable) => el.querySelector(".gt-i-page-info")?.textContent;
  const pageButton = (el: GtTable, target: string) =>
    el.querySelector(`.gt-i-pager button[data-gti-page="${target}"]`) as HTMLButtonElement;
  const press = (target: HTMLElement, key: string) => {
    const event = new KeyboardEvent("keydown", { key, bubbles: true, cancelable: true });
    target.dispatchEvent(event);
    return event;
  };
  const numbers = (el: GtTable) =>
    Array.from(el.querySelectorAll(".gt-i-page-numbers > *"), (item) =>
      item.getAttribute("aria-current") === "page" ? `[${item.textContent}]` : item.textContent,
    );

  async function mountPager(pagination: Partial<PaginationSpec> = {}, options: TableOptions = {}) {
    const el = await mountTable(GROUPED, { ...options, pagination: { enabled: true, ...pagination } });
    const events: PageEventDetail[] = [];
    el.addEventListener(PAGE_EVENT, (event) => {
      events.push((event as CustomEvent<PageEventDetail>).detail);
    });
    return { el, events };
  }

  it("is a labelled nav below the table, in the table's font", async () => {
    const { el } = await mountPager();
    const nav = pager(el);
    expect(nav.tagName).toBe("NAV");
    expect(nav.getAttribute("aria-label")).toBe("Table pages");
    expect(nav.previousElementSibling).toBe(el.querySelector("#t"));
    expect(nav.hidden).toBe(false);
    expect(nav.style.fontFamily).toBe(getComputedStyle(el.table as HTMLTableElement).fontFamily);
    expect(el.querySelector(".gt-i-live")?.getAttribute("aria-live")).toBe("polite");
  });

  it("has previous and next buttons and page numbers", async () => {
    const { el } = await mountPager();
    expect(info(el)).toBe("1–2 of 5 rows");
    expect(numbers(el)).toEqual(["[1]", "2", "3"]);
    expect(pageButton(el, "2").getAttribute("aria-label")).toBe("Page 2");
    expect(pageButton(el, "previous").textContent).toBe("Previous");
    expect(pageButton(el, "previous").getAttribute("aria-disabled")).toBe("true");
    expect(pageButton(el, "next").getAttribute("aria-disabled")).toBe("false");
    expect(pageButton(el, "first")).toBeNull();
  });

  it("changes the page, with an event and an announcement", async () => {
    const { el, events } = await mountPager();
    pageButton(el, "next").click();
    expect(el.page).toBe(2);
    expect(events).toEqual([{ page: 2, pageSize: 2, pageCount: 3 }]);
    expect(live(el)).toBe("Page 2 of 3");
    expect(info(el)).toBe("3–4 of 5 rows");
    expect(numbers(el)).toEqual(["1", "[2]", "3"]);

    pageButton(el, "3").click();
    expect(info(el)).toBe("5 of 5 rows");
    expect(pageButton(el, "next").getAttribute("aria-disabled")).toBe("true");
    // Not past the last page, nor to the page it's on
    pageButton(el, "next").click();
    pageButton(el, "3").click();
    expect(events).toHaveLength(2);
    pageButton(el, "previous").click();
    expect(el.page).toBe(2);
  });

  it("doesn't fire an event or announce when `page` is set", async () => {
    const { el, events } = await mountPager();
    el.page = 3;
    el.pageSize = 4;
    expect(events).toEqual([]);
    expect(live(el)).toBe("");
    expect(info(el)).toBe("5 of 5 rows");
  });

  it("keeps focus on the current page number as the numbers change", async () => {
    const { el } = await mountPager();
    pageButton(el, "2").focus();
    pageButton(el, "2").click();
    expect(document.activeElement).toBe(pageButton(el, "2"));
    expect(document.activeElement?.getAttribute("aria-current")).toBe("page");
  });

  it("pages with Page Up and Page Down", async () => {
    const { el, events } = await mountPager();
    const next = pageButton(el, "next");
    expect(press(next, "PageDown").defaultPrevented).toBe(true);
    expect(el.page).toBe(2);
    press(next, "PageDown");
    press(next, "PageDown");
    expect(el.page).toBe(3);
    press(next, "PageUp");
    expect(el.page).toBe(2);
    expect(events.map((event) => event.page)).toEqual([2, 3, 2]);
  });

  it("says how many rows match a search", async () => {
    const { el } = await mountPager();
    el.search = "a";
    expect(info(el)).toBe("1–2 of 3 rows (filtered from 5)");
    expect(numbers(el)).toEqual(["[1]", "2"]);
    el.search = "c";
    expect(info(el)).toBe("1 of 1 row (filtered from 5)");
    el.search = "zzz";
    expect(info(el)).toBe("0 rows (filtered from 5)");
    // Still there, so it doesn't come and go while searching
    expect(pager(el).hidden).toBe(false);
    expect(pageButton(el, "next").getAttribute("aria-disabled")).toBe("true");
  });

  it("leaves out the row info when asked", async () => {
    const { el } = await mountPager({ info: false });
    expect(el.querySelector(".gt-i-page-info")).toBeNull();
  });

  it("isn't shown when every row fits on a page", async () => {
    const { el } = await mountPager({ page_size: 5 });
    expect(el.querySelector(".gt-i-pager")).toBeNull();
    expect(visible(el)).toEqual(shown(el));

    el.pageSize = 2;
    expect(pager(el).hidden).toBe(false);
    el.pageSize = null;
    expect(pager(el).hidden).toBe(true);
  });

  it("can have first and last buttons", async () => {
    const { el } = await mountPager({ type: "full" });
    const labels = Array.from(el.querySelectorAll(".gt-i-pages button"), (b) => b.textContent);
    expect(labels).toEqual(["First", "Previous", "Next", "Last"]);
    expect(el.querySelector(".gt-i-page-status")?.textContent).toBe("Page 1 of 3");

    pageButton(el, "last").click();
    expect(el.page).toBe(3);
    expect(el.querySelector(".gt-i-page-status")?.textContent).toBe("Page 3 of 3");
    expect(pageButton(el, "last").getAttribute("aria-disabled")).toBe("true");
    pageButton(el, "first").click();
    expect(el.page).toBe(1);
  });

  it("can have previous and next buttons only", async () => {
    const { el } = await mountPager({ type: "simple" });
    const labels = Array.from(el.querySelectorAll(".gt-i-pages button"), (b) => b.textContent);
    expect(labels).toEqual(["Previous", "Next"]);
    expect(el.querySelector(".gt-i-page-numbers")).toBeNull();
  });

  it("can have a page number input", async () => {
    const { el, events } = await mountPager({ type: "jump" });
    const input = el.querySelector(".gt-i-page-jump input") as HTMLInputElement;
    expect(input.value).toBe("1");
    expect(input.inputMode).toBe("numeric");
    expect(el.querySelector(".gt-i-page-jump")?.textContent).toBe("Page  of 3");

    input.value = "3";
    expect(press(input, "Enter").defaultPrevented).toBe(true);
    expect(el.page).toBe(3);
    // Past the last page is the last; anything else is undone
    el.page = 1;
    input.value = "99";
    input.dispatchEvent(new Event("change", { bubbles: true }));
    expect([el.page, input.value]).toEqual([3, "3"]);
    input.value = "two";
    input.dispatchEvent(new Event("change", { bubbles: true }));
    expect([el.page, input.value]).toEqual([3, "3"]);
    expect(events.map((event) => event.page)).toEqual([3, 3]);
  });

  it("can have a page size select", async () => {
    const { el, events } = await mountPager({ size_select: true, page_size: 3 });
    const select = el.querySelector(".gt-i-page-size select") as HTMLSelectElement;
    expect(select.closest("label")?.textContent).toContain("Rows per page");
    expect(Array.from(select.options, (option) => option.value)).toEqual(["2", "3", "4"]);
    expect(select.value).toBe("3");

    el.page = 2;
    select.value = "2";
    select.dispatchEvent(new Event("change", { bubbles: true }));
    // Row 4 stays in view
    expect([el.page, el.pageSize, el.pageCount]).toEqual([2, 2, 3]);
    expect(events).toEqual([{ page: 2, pageSize: 2, pageCount: 3 }]);
    expect(live(el)).toBe("2 rows per page, page 2 of 3");
  });

  it("stays with a page size select while a smaller page size could have pages", async () => {
    const { el } = await mountPager({ size_select: true, page_size: 5 });
    expect(pager(el).hidden).toBe(false);
    expect(el.pageCount).toBe(1);
  });
});

describe("the control bar", () => {
  afterEach(() => {
    vi.useRealTimers();
  });

  const bar = (el: GtTable) => el.querySelector(".gt-i-bar") as HTMLElement;
  const part = (el: GtTable, name: string) =>
    el.querySelector(`.gt-i-bar [data-gti-bar="${name}"]`) as HTMLButtonElement;
  const field = (el: GtTable) => el.querySelector(".gt-i-search-field") as HTMLElement;
  const count = (el: GtTable) => el.querySelector(".gt-i-search-count") as HTMLElement;
  const readout = (el: GtTable) => el.querySelector(".gt-i-readout") as HTMLButtonElement;
  const jump = (el: GtTable) => el.querySelector(".gt-i-readout-jump") as HTMLElement;
  const jumpInput = (el: GtTable) => jump(el).querySelector("input") as HTMLInputElement;
  const type = (input: HTMLInputElement, value: string) => {
    input.value = value;
    input.dispatchEvent(new Event("input", { bubbles: true }));
  };
  const press = (target: Element, key: string, init: KeyboardEventInit = {}) => {
    const event = new KeyboardEvent("keydown", { key, bubbles: true, cancelable: true, ...init });
    target.dispatchEvent(event);
    return event;
  };

  // A search, and pages of 2 rows ([3, 0], [4, 1] and [2]), unless set otherwise
  async function mountBar(options: TableOptions = {}) {
    const el = await mountTable(GROUPED, {
      ...options,
      controls: { search: true, bar: true, ...options.controls },
      pagination: { enabled: true, ...options.pagination },
    });
    const events: (PageEventDetail | SearchEventDetail)[] = [];
    for (const name of [PAGE_EVENT, SEARCH_EVENT]) {
      el.addEventListener(name, (event) => {
        events.push((event as CustomEvent<PageEventDetail | SearchEventDetail>).detail);
      });
    }
    return { el, events };
  }

  it("is one bar below the table, in the table's font, instead of a toolbar and pager", async () => {
    const { el } = await mountBar();
    expect(bar(el).previousElementSibling).toBe(el.querySelector("#t"));
    expect(bar(el).hidden).toBe(false);
    expect(bar(el).style.fontFamily).toBe(getComputedStyle(el.table as HTMLTableElement).fontFamily);
    expect(el.querySelector(".gt-i-toolbar")).toBeNull();
    expect(el.querySelector(".gt-i-pager")).toBeNull();
    expect(el.querySelectorAll(".gt-i-live")).toHaveLength(1);

    const nav = el.querySelector(".gt-i-bar-pages") as HTMLElement;
    expect(nav.tagName).toBe("NAV");
    expect(nav.getAttribute("aria-label")).toBe("Table pages");
    expect(part(el, "search").getAttribute("aria-label")).toBe("Search the table");
    expect(part(el, "search").title).toBe("Search (/)");
    expect(part(el, "previous").title).toBe("Previous page (←)");
    expect(part(el, "next").title).toBe("Next page (→)");
    expect(part(el, "search").querySelector("svg")?.getAttribute("aria-hidden")).toBe("true");
  });

  it("opens the search field from its button", async () => {
    const { el } = await mountBar();
    expect(field(el).hidden).toBe(true);
    part(el, "search").click();

    expect(field(el).hidden).toBe(false);
    expect(part(el, "search").hidden).toBe(true);
    expect(bar(el).hasAttribute("data-gti-searching")).toBe(true);
    expect(document.activeElement).toBe(searchBox(el));
    expect(searchBox(el)?.getAttribute("aria-label")).toBe("Search the table");
  });

  it("searches as the search box does, and says how many rows match", async () => {
    const { el, events } = await mountBar();
    part(el, "search").click();
    const input = searchBox(el) as HTMLInputElement;
    vi.useFakeTimers();

    type(input, "a");
    vi.advanceTimersByTime(100);
    expect(el.search).toBe("");
    vi.advanceTimersByTime(50);
    expect(el.search).toBe("a");
    expect(count(el).hidden).toBe(false);
    expect(count(el).textContent).toBe("3 rows");
    expect(live(el)).toBe("Showing 3 of 5 rows");

    type(input, "c");
    press(input, "Enter");
    expect(count(el).textContent).toBe("1 row");
    expect(events).toEqual([
      { search: "a", count: 3 },
      { search: "c", count: 1 },
    ]);
    // The pages stay, so the bar doesn't change while searching
    expect(el.querySelector<HTMLElement>(".gt-i-bar-pages")?.hidden).toBe(false);
  });

  it("clears the search on Escape, then closes the field", async () => {
    const { el } = await mountBar();
    part(el, "search").click();
    const input = searchBox(el) as HTMLInputElement;
    type(input, "a");
    press(input, "Enter");
    expect(part(el, "clear").getAttribute("aria-label")).toBe("Clear the search");
    expect(part(el, "clear").title).toBe("Clear (Esc)");

    expect(press(input, "Escape").defaultPrevented).toBe(true);
    expect([input.value, el.search]).toEqual(["", ""]);
    expect(field(el).hidden).toBe(false);
    expect(count(el).hidden).toBe(true);
    expect(part(el, "clear").getAttribute("aria-label")).toBe("Close the search");
    expect(part(el, "clear").title).toBe("Close (Esc)");

    expect(press(input, "Escape").defaultPrevented).toBe(true);
    expect(field(el).hidden).toBe(true);
    expect(part(el, "search").hidden).toBe(false);
    expect(bar(el).hasAttribute("data-gti-searching")).toBe(false);
    expect(document.activeElement).toBe(part(el, "search"));
  });

  it("clears the search with its clear button, then closes the field", async () => {
    const { el } = await mountBar();
    part(el, "search").click();
    const input = searchBox(el) as HTMLInputElement;
    type(input, "a");
    press(input, "Enter");

    part(el, "clear").click();
    expect(el.search).toBe("");
    expect(field(el).hidden).toBe(false);
    expect(document.activeElement).toBe(input);

    part(el, "clear").click();
    expect(field(el).hidden).toBe(true);
    expect(document.activeElement).toBe(part(el, "search"));
  });

  it("closes an empty field when focus leaves it, and drops a search waiting on typing", async () => {
    const { el, events } = await mountBar();
    part(el, "search").click();
    const input = searchBox(el) as HTMLInputElement;
    const leave = (to: Element | null) =>
      input.dispatchEvent(new FocusEvent("focusout", { bubbles: true, relatedTarget: to }));

    // Not when focus goes to the clear button, or the field has a search in it
    leave(part(el, "clear"));
    expect(field(el).hidden).toBe(false);
    type(input, "a");
    press(input, "Enter");
    leave(null);
    expect(field(el).hidden).toBe(false);

    vi.useFakeTimers();
    type(input, "");
    leave(null);
    expect(field(el).hidden).toBe(true);
    expect(el.search).toBe("");
    vi.advanceTimersByTime(500);
    expect(events).toEqual([
      { search: "a", count: 3 },
      { search: "", count: 5 },
    ]);
  });

  it("opens the search on `/`, but not from a field for typing", async () => {
    const { el } = await mountBar();
    const cell = el.querySelector("tbody td") as HTMLElement;
    expect(press(cell, "/", { ctrlKey: true }).defaultPrevented).toBe(false);
    expect(field(el).hidden).toBe(true);

    expect(press(cell, "/").defaultPrevented).toBe(true);
    expect(field(el).hidden).toBe(false);
    expect(document.activeElement).toBe(searchBox(el));
    // (A `/` typed in the search is the search's)
    expect(press(searchBox(el) as HTMLInputElement, "/").defaultPrevented).toBe(false);
  });

  it("follows `search`, opening the field for a search and closing it for none", async () => {
    const { el, events } = await mountBar();
    el.search = "a";
    expect(field(el).hidden).toBe(false);
    expect(searchBox(el)?.value).toBe("a");
    expect(count(el).textContent).toBe("3 rows");

    el.search = "";
    expect(field(el).hidden).toBe(true);
    expect(events).toEqual([]);
    expect(live(el)).toBe("");
  });

  it("keeps the field open when `search` is emptied while it has focus", async () => {
    const { el } = await mountBar();
    part(el, "search").click();
    el.search = "a";
    el.search = "";
    expect(field(el).hidden).toBe(false);
    expect(document.activeElement).toBe(searchBox(el));
  });

  it("shows a search set before hydration", async () => {
    const { html, spec } = gtTable(GROUPED, { controls: { search: true, bar: true } });
    const el = document.createElement(TAG_NAME) as GtTable;
    el.search = "c";
    el.innerHTML = html + specScript(spec);
    document.body.append(el);
    await tick();

    expect(field(el).hidden).toBe(false);
    expect(searchBox(el)?.value).toBe("c");
    expect(count(el).textContent).toBe("1 row");
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
  });

  it("has a readout of the page and page count", async () => {
    const { el } = await mountBar();
    expect(readout(el).textContent).toBe("1/3");
    expect(readout(el).getAttribute("aria-label")).toBe("Page 1 of 3");
    expect(readout(el).title).toBe("Go to a page");
    expect(el.querySelector<HTMLElement>(".gt-i-bar-pages")?.style.getPropertyValue("--gt-i-digits")).toBe("1");

    el.search = "a";
    expect(readout(el).textContent).toBe("1/2");
  });

  it("changes the page with its arrows, with an event and an announcement", async () => {
    const { el, events } = await mountBar();
    expect(part(el, "previous").getAttribute("aria-disabled")).toBe("true");
    part(el, "previous").click();
    expect(events).toEqual([]);

    part(el, "next").click();
    expect(el.page).toBe(2);
    expect(events).toEqual([{ page: 2, pageSize: 2, pageCount: 3 }]);
    expect(live(el)).toBe("Page 2 of 3");
    expect(readout(el).textContent).toBe("2/3");

    part(el, "next").click();
    expect(part(el, "next").getAttribute("aria-disabled")).toBe("true");
    part(el, "next").click();
    expect(events).toHaveLength(2);
    part(el, "previous").click();
    expect(el.page).toBe(2);
  });

  it("pages with the arrow keys, Page Up and Down, and Home and End", async () => {
    const { el, events } = await mountBar();
    const next = part(el, "next");
    expect(press(next, "ArrowRight").defaultPrevented).toBe(true);
    expect(el.page).toBe(2);
    press(next, "PageDown");
    press(readout(el), "ArrowLeft");
    press(next, "End");
    press(next, "PageUp");
    press(next, "Home");
    expect(events.map((event) => (event as PageEventDetail).page)).toEqual([2, 3, 2, 3, 2, 1]);

    // Not with a modifier, or while typing
    expect(press(next, "ArrowRight", { altKey: true }).defaultPrevented).toBe(false);
    part(el, "search").click();
    expect(press(searchBox(el) as HTMLInputElement, "ArrowRight").defaultPrevented).toBe(false);
    expect(press(next, "Escape").defaultPrevented).toBe(false);
    expect(el.page).toBe(1);
  });

  it("turns the readout into an input for the page to go to", async () => {
    const { el, events } = await mountBar();
    readout(el).click();
    const input = jumpInput(el);
    expect([readout(el).hidden, jump(el).hidden]).toEqual([true, false]);
    expect(document.activeElement).toBe(input);
    expect(input.value).toBe("1");
    expect(input.inputMode).toBe("numeric");
    expect(input.getAttribute("aria-label")).toBe("Go to page (of 3)");
    expect(jump(el).textContent).toBe("/3");

    input.value = "3";
    expect(press(input, "Enter").defaultPrevented).toBe(true);
    expect(el.page).toBe(3);
    expect([readout(el).hidden, jump(el).hidden]).toEqual([false, true]);
    expect(document.activeElement).toBe(readout(el));
    expect(events).toEqual([{ page: 3, pageSize: 2, pageCount: 3 }]);
  });

  it("goes to the last page for one past it, and nowhere for anything else", async () => {
    const { el } = await mountBar();
    readout(el).click();
    jumpInput(el).value = "99";
    press(jumpInput(el), "Enter");
    expect(el.page).toBe(3);

    for (const value of ["two", "1.5", ""]) {
      readout(el).click();
      jumpInput(el).value = value;
      press(jumpInput(el), "Enter");
      expect(el.page).toBe(3);
    }
  });

  it("goes nowhere on Escape, and to the page typed when the input loses focus", async () => {
    const { el } = await mountBar();
    readout(el).click();
    jumpInput(el).value = "2";
    const escape = press(jumpInput(el), "Escape");
    expect(escape.defaultPrevented).toBe(true);
    expect(el.page).toBe(1);
    expect(jump(el).hidden).toBe(true);
    expect(document.activeElement).toBe(readout(el));

    readout(el).click();
    jumpInput(el).value = "2";
    jumpInput(el).dispatchEvent(new FocusEvent("blur"));
    expect(el.page).toBe(2);
    expect(jump(el).hidden).toBe(true);
  });

  it("has no pages, and sticks to the bottom of the view, when every row fits on a page", async () => {
    const { el } = await mountBar({ pagination: { enabled: false } });
    expect(bar(el).hidden).toBe(false);
    expect(el.querySelector<HTMLElement>(".gt-i-bar-pages")?.hidden).toBe(true);
    expect(bar(el).hasAttribute("data-gti-stick")).toBe(true);

    el.pageSize = 2;
    expect(el.querySelector<HTMLElement>(".gt-i-bar-pages")?.hidden).toBe(false);
    expect(bar(el).hasAttribute("data-gti-stick")).toBe(false);
    expect(bar(el).style.backgroundColor).toBe("");
    // (Pages that every row fits on aren't pages)
    el.pageSize = 5;
    expect(el.querySelector<HTMLElement>(".gt-i-bar-pages")?.hidden).toBe(true);
  });

  it("doesn't stick in a body that scrolls", async () => {
    const { el } = await mountBar({ pagination: { enabled: false }, layout: { height: "300px" } });
    expect(bar(el).hasAttribute("data-gti-stick")).toBe(false);
  });

  it("comes with the pages, without a search", async () => {
    const { el } = await mountBar({ controls: { search: false }, pagination: { page_size: 5 } });
    expect(bar(el)).toBeNull();

    el.pageSize = 2;
    expect(bar(el).hidden).toBe(false);
    expect(el.querySelector(".gt-i-bar-search")).toBeNull();
    expect(readout(el).textContent).toBe("1/3");
    el.pageSize = null;
    expect(bar(el).hidden).toBe(true);
  });

  it("isn't there without a search or pages", async () => {
    const { el } = await mountBar({ controls: { search: false }, pagination: { enabled: false } });
    expect(bar(el)).toBeNull();
  });

  it("is at least 300px wide, centred under a narrower table, within the element", async () => {
    vi.spyOn(Element.prototype, "getBoundingClientRect").mockImplementation(function (this: Element) {
      if (this instanceof GtTable) {
        return new DOMRect(0, 0, 800, 200);
      }
      return this.tagName === "TABLE" ? new DOMRect(350, 0, 100, 180) : new DOMRect(0, 0, 0, 0);
    });
    const { el } = await mountBar();
    expect([bar(el).style.marginLeft, bar(el).style.width]).toEqual(["250px", "300px"]);
  });

  it("is as wide as a wider table, and kept within the element", async () => {
    let table = new DOMRect(100, 0, 500, 180);
    vi.spyOn(Element.prototype, "getBoundingClientRect").mockImplementation(function (this: Element) {
      if (this instanceof GtTable) {
        return new DOMRect(0, 0, 800, 200);
      }
      return this.tagName === "TABLE" ? table : new DOMRect(0, 0, 0, 0);
    });
    const { el } = await mountBar();
    expect([bar(el).style.marginLeft, bar(el).style.width]).toEqual(["100px", "500px"]);

    table = new DOMRect(0, 0, 100, 180);
    el.search = "a";
    (el as unknown as { alignBars(): void }).alignBars();
    expect([bar(el).style.marginLeft, bar(el).style.width]).toEqual(["0px", "300px"]);
  });

  it("isn't used without `bar` in the spec", async () => {
    const el = await mountTable(GROUPED, { controls: { search: true }, pagination: { enabled: true } });
    expect(bar(el)).toBeNull();
    expect(el.querySelector(".gt-i-toolbar")).not.toBeNull();
    expect(el.querySelector(".gt-i-pager")).not.toBeNull();
  });

  it("goes when the table's children are replaced, as does its `/` key", async () => {
    const { el } = await mountBar();
    const { html, spec } = gtTable(GROUPED, { controls: { search: false } });
    el.remove();
    el.innerHTML = html + specScript(spec);
    document.body.append(el);
    await tick();

    expect(bar(el)).toBeNull();
    expect(el.querySelector(".gt-i-toolbar")).toBeNull();
    expect(press(el.querySelector("tbody td") as HTMLElement, "/").defaultPrevented).toBe(false);
  });
});

describe("the info panel", () => {
  const bar = (el: GtTable) => el.querySelector(".gt-i-bar") as HTMLElement;
  const toggle = (el: GtTable) => el.querySelector('.gt-i-bar [data-gti-bar="info"]') as HTMLButtonElement;
  const panel = (el: GtTable) => el.querySelector(".gt-i-info") as HTMLElement;
  const rows = (el: GtTable) => el.querySelector(".gt-i-info-rows") as HTMLElement;
  const item = (el: GtTable, name: string) => el.querySelector(`[data-gti-info="${name}"]`) as HTMLElement | null;
  const action = (el: GtTable, name: string) => item(el, name)?.querySelector("button") as HTMLButtonElement;
  const select = (el: GtTable) => item(el, "size")?.querySelector("select") as HTMLSelectElement;
  const keys = (el: GtTable) =>
    Array.from(el.querySelectorAll<HTMLElement>(".gt-i-info-keys > div"))
      .filter((entry) => !entry.hidden)
      .map((entry) => `${entry.querySelector("dt")?.textContent}: ${entry.querySelector("dd")?.textContent}`);
  const press = (target: Element, key: string) => {
    const event = new KeyboardEvent("keydown", { key, bubbles: true, cancelable: true });
    target.dispatchEvent(event);
    return event;
  };

  // A search, and pages of 2 rows ([3, 0], [4, 1] and [2]), unless set otherwise
  async function mountInfo(options: TableOptions = {}) {
    const el = await mountTable(GROUPED, {
      ...options,
      controls: { search: true, bar: true, ...options.controls },
      pagination: { enabled: true, ...options.pagination },
    });
    const events: unknown[] = [];
    for (const name of [PAGE_EVENT, SORT_EVENT, SELECT_EVENT]) {
      el.addEventListener(name, (event) => events.push((event as CustomEvent).detail));
    }
    return { el, events };
  }

  it("opens from a button at the end of the bar, and closes from it", async () => {
    const { el } = await mountInfo();
    const button = toggle(el);
    expect(button.getAttribute("aria-label")).toBe("Table info");
    expect(button.getAttribute("aria-expanded")).toBe("false");
    expect(button.getAttribute("aria-controls")).toBe(panel(el).id);
    expect(button.previousElementSibling).toBe(el.querySelector(".gt-i-bar-pages"));
    // (Next to its button, so that Tab goes from one into the other)
    expect(button.nextElementSibling).toBe(panel(el));
    expect(panel(el).getAttribute("role")).toBe("group");
    expect(panel(el).getAttribute("aria-label")).toBe("Table info");
    expect(panel(el).hidden).toBe(true);

    button.click();
    expect(panel(el).hidden).toBe(false);
    expect(button.getAttribute("aria-expanded")).toBe("true");
    button.click();
    expect(panel(el).hidden).toBe(true);
    expect(button.getAttribute("aria-expanded")).toBe("false");
  });

  it("gives every panel its own id", async () => {
    const { html, spec } = gtTable(GROUPED, { controls: { search: true, bar: true } });
    document.body.innerHTML = `<gt-table>${html}${specScript(spec)}</gt-table>`.repeat(2);
    await tick();
    const [one, two] = Array.from(document.querySelectorAll(".gt-i-info"), (node) => node.id);
    expect(one).not.toBe(two);
  });

  it("says which rows are shown, and of how many without the search", async () => {
    const { el } = await mountInfo();
    expect(rows(el).textContent).toBe("1–2 of 5 rows");
    expect(rows(el).hidden).toBe(false);
    el.page = 3;
    expect(rows(el).textContent).toBe("5 of 5 rows");
    el.search = "a";
    expect(rows(el).textContent).toBe("1–2 of 3 rows (filtered from 5)");
    el.search = "zzz";
    expect(rows(el).textContent).toBe("0 rows (filtered from 5)");
    // Without pages, how many
    el.search = "";
    el.pageSize = null;
    expect(rows(el).textContent).toBe("5 rows");
  });

  it("says how many rows there are, without pages from the start", async () => {
    const { el } = await mountInfo({ pagination: { enabled: false } });
    expect(rows(el).textContent).toBe("5 rows");
    el.search = "a";
    expect(rows(el).textContent).toBe("3 rows (filtered from 5)");
  });

  it("leaves out which rows are shown when asked", async () => {
    const { el } = await mountInfo({ pagination: { info: false } });
    expect(rows(el).hidden).toBe(true);
  });

  it("chooses the page size, from the author's and the table's own", async () => {
    const { el, events } = await mountInfo({ pagination: { size_select: true, page_sizes: [4, 10] } });
    const choices = () => Array.from(select(el).options, (option) => option.value);
    expect(item(el, "size")?.tagName).toBe("LABEL");
    expect(item(el, "size")?.textContent).toContain("Rows per page");
    expect(choices()).toEqual(["2", "4", "10"]);
    expect(select(el).value).toBe("2");

    select(el).value = "4";
    select(el).dispatchEvent(new Event("change", { bubbles: true }));
    expect(el.pageSize).toBe(4);
    expect(events).toEqual([{ page: 1, pageSize: 4, pageCount: 2 }]);
    expect(live(el)).toBe("4 rows per page, page 1 of 2");
    expect(choices()).toEqual(["2", "4", "10"]);

    el.pageSize = 3;
    expect(choices()).toEqual(["2", "3", "4", "10"]);
    expect(select(el).value).toBe("3");
  });

  it("has no page size to choose without `size_select`", async () => {
    const { el } = await mountInfo();
    expect(item(el, "size")).toBeNull();
  });

  it("keeps the bar for page sizes that the rows can be split into", async () => {
    const { el } = await mountInfo({
      controls: { search: false },
      pagination: { page_size: 5, page_sizes: [2], size_select: true },
    });
    expect(bar(el).hidden).toBe(false);
    expect(el.querySelector<HTMLElement>(".gt-i-bar-pages")?.hidden).toBe(true);
    expect(item(el, "size")?.hidden).toBe(false);
    // (Nor are there keys for paging, without pages)
    expect(keys(el)).toEqual(["Shift + click: Sort by more than one column"]);

    select(el).value = "2";
    select(el).dispatchEvent(new Event("change", { bubbles: true }));
    expect(el.querySelector<HTMLElement>(".gt-i-bar-pages")?.hidden).toBe(false);
    expect(keys(el)).toEqual([
      "← →: Previous or next page, in the bar",
      "Home End: First or last page, in the bar",
      "Shift + click: Sort by more than one column",
    ]);
  });

  it("says how the table is sorted, and puts it back in its own order", async () => {
    const { el, events } = await mountInfo();
    expect(item(el, "sort")?.textContent).toBe("Not sortedReset");
    expect(action(el, "sort").getAttribute("aria-label")).toBe("Reset the sort");
    expect(action(el, "sort").getAttribute("aria-disabled")).toBe("true");
    action(el, "sort").click();
    expect(events).toEqual([]);

    el.sort = [{ column: "x", descending: true }, { column: "y" }];
    expect(item(el, "sort")?.firstElementChild?.textContent).toBe("Sorted by x, descending, then y, ascending");
    expect(action(el, "sort").getAttribute("aria-disabled")).toBe("false");
    el.page = 2;
    action(el, "sort").click();
    expect(el.sort).toEqual([]);
    expect(el.page).toBe(1);
    expect(events).toEqual([{ sort: [] }]);
    expect(live(el)).toBe("Not sorted");
    expect(action(el, "sort").getAttribute("aria-disabled")).toBe("true");
  });

  it("has no sort without sorting", async () => {
    const { el } = await mountInfo({ controls: { sorting: false } });
    expect(item(el, "sort")).toBeNull();
  });

  it("says how many rows are selected, and clears them", async () => {
    const { el, events } = await mountInfo({ controls: { selection: "multiple" } });
    expect(item(el, "selection")?.firstElementChild?.textContent).toBe("No rows selected");
    expect(action(el, "selection").getAttribute("aria-label")).toBe("Clear the selection");
    expect(action(el, "selection").getAttribute("aria-disabled")).toBe("true");

    el.selection = [0, 2];
    expect(item(el, "selection")?.firstElementChild?.textContent).toBe("2 rows selected");
    // (Rows that don't match the search too)
    el.search = "c";
    action(el, "selection").click();
    expect(el.selection).toEqual([]);
    expect(events).toEqual([{ selection: [] }]);
    expect(live(el)).toBe("No rows selected");
    expect(el.querySelectorAll("tr.gt-i-selected")).toHaveLength(0);
    expect(action(el, "selection").getAttribute("aria-disabled")).toBe("true");
  });

  it("has no selection without selection", async () => {
    const { el } = await mountInfo();
    expect(item(el, "selection")).toBeNull();
  });

  it("lists the shortcuts the table has", async () => {
    const { el } = await mountInfo({ controls: { selection: "multiple" } });
    expect(keys(el)).toEqual([
      "/: Search",
      "Esc: Clear the search, then close it",
      "← →: Previous or next page, in the bar",
      "Home End: First or last page, in the bar",
      "Shift + click: Sort by more than one column",
      "Shift + click: Select a range of rows",
    ]);
    expect(el.querySelectorAll(".gt-i-info-keys kbd")).toHaveLength(8);
  });

  it("has no shortcuts to list without any", async () => {
    const { el } = await mountInfo({
      controls: { search: false, sorting: false },
      pagination: { page_size: 5, page_sizes: [2], size_select: true },
    });
    expect(el.querySelector<HTMLElement>(".gt-i-info-shortcuts")?.hidden).toBe(true);
  });

  it("closes on Escape, giving focus back to its button", async () => {
    const { el } = await mountInfo();
    toggle(el).click();
    action(el, "sort").focus();
    expect(press(action(el, "sort"), "Escape").defaultPrevented).toBe(true);
    expect(panel(el).hidden).toBe(true);
    expect(document.activeElement).toBe(toggle(el));
    // (Escape is the table's only while the panel is open)
    expect(press(toggle(el), "Escape").defaultPrevented).toBe(false);
  });

  it("closes on a press outside it, or when focus goes elsewhere", async () => {
    const { el } = await mountInfo();
    const outside = el.querySelector("tbody td") as HTMLElement;
    toggle(el).click();
    panel(el).dispatchEvent(new PointerEvent("pointerdown", { bubbles: true, composed: true }));
    expect(panel(el).hidden).toBe(false);
    outside.dispatchEvent(new PointerEvent("pointerdown", { bubbles: true, composed: true }));
    expect(panel(el).hidden).toBe(true);

    toggle(el).click();
    const leave = (from: Element, to: Element | null) =>
      from.dispatchEvent(new FocusEvent("focusout", { bubbles: true, relatedTarget: to }));
    leave(toggle(el), action(el, "sort"));
    leave(action(el, "sort"), toggle(el));
    // (Not when the window loses focus)
    leave(action(el, "sort"), null);
    expect(panel(el).hidden).toBe(false);
    leave(action(el, "sort"), outside);
    expect(panel(el).hidden).toBe(true);
    expect(document.activeElement).not.toBe(toggle(el));
  });

  it("doesn't page with the keys pressed in it", async () => {
    const { el } = await mountInfo();
    toggle(el).click();
    expect(press(action(el, "sort"), "ArrowRight").defaultPrevented).toBe(false);
    expect(press(action(el, "sort"), "End").defaultPrevented).toBe(false);
    expect(el.page).toBe(1);
    // (But does on its button, in the bar)
    expect(press(toggle(el), "ArrowRight").defaultPrevented).toBe(true);
    expect(el.page).toBe(2);
  });

  it("closes when the bar goes, and when the table does", async () => {
    const { el } = await mountInfo({ controls: { search: false } });
    toggle(el).click();
    el.pageSize = null;
    expect(bar(el).hidden).toBe(true);
    expect(panel(el).hidden).toBe(true);

    el.pageSize = 2;
    toggle(el).click();
    el.remove();
    expect(panel(el).hidden).toBe(true);
    expect((el as unknown as { outsidePress: unknown }).outsidePress).toBeNull();
  });
});

describe("export", () => {
  const toggle = (el: GtTable) => el.querySelector('.gt-i-bar [data-gti-bar="export"]') as HTMLButtonElement;
  const panel = (el: GtTable) => el.querySelector(".gt-i-export") as HTMLElement;
  const status = (el: GtTable) => panel(el).querySelector(".gt-i-info-rows") as HTMLElement;
  const action = (el: GtTable, format: ExportFormat) =>
    panel(el).querySelector(`[data-gti-export="${format}"]`) as HTMLButtonElement;
  const selectedOnly = (el: GtTable) => panel(el).querySelector<HTMLInputElement>("input[type=checkbox]");
  const check = (el: GtTable, on: boolean) => {
    const box = selectedOnly(el) as HTMLInputElement;
    box.checked = on;
    box.dispatchEvent(new Event("change", { bubbles: true }));
  };
  const lines = (csv: string) => csv.split("\r\n").slice(0, -1);
  const press = (target: Element, key: string) => {
    const event = new KeyboardEvent("keydown", { key, bubbles: true, cancelable: true });
    target.dispatchEvent(event);
    return event;
  };

  // GROUPED in pages of 2 rows, with a search and export as both formats, unless set otherwise
  async function mountExport(options: TableOptions = {}) {
    const el = await mountTable(GROUPED, {
      ...options,
      controls: { search: true, bar: true, ...options.controls },
      pagination: { enabled: true, ...options.pagination },
      export: options.export ?? { formats: ["csv", "clipboard"], filename: "towny" },
    });
    const events: ExportEventDetail[] = [];
    el.addEventListener(EXPORT_EVENT, (event) => events.push((event as CustomEvent<ExportEventDetail>).detail));
    return { el, events };
  }

  // The download's link (as clicked) and its CSV
  function catchDownload() {
    const blobs: Blob[] = [];
    const links: { href: string; download: string; connected: boolean }[] = [];
    vi.spyOn(URL, "createObjectURL").mockImplementation((blob) => {
      blobs.push(blob as Blob);
      return `blob:gti-${blobs.length}`;
    });
    const revoke = vi.spyOn(URL, "revokeObjectURL").mockImplementation(() => undefined);
    vi.spyOn(HTMLAnchorElement.prototype, "click").mockImplementation(function (this: HTMLAnchorElement) {
      links.push({ href: this.getAttribute("href") ?? "", download: this.download, connected: this.isConnected });
    });
    return { blobs, links, revoke };
  }

  // What's written to the clipboard (with the Clipboard API), by type
  function catchClipboard(write: "ok" | "rejected" = "ok") {
    const written: Record<string, string>[] = [];
    vi.spyOn(navigator.clipboard, "write").mockImplementation(async (items) => {
      if (write === "rejected") {
        throw new DOMException("Not allowed", "NotAllowedError");
      }
      for (const item of items) {
        const entry: Record<string, string> = {};
        for (const type of item.types) {
          entry[type] = await (await item.getType(type)).text();
        }
        written.push(entry);
      }
    });
    return written;
  }

  // A copy as the browser would make it, without the Clipboard API: the data set in the copy event
  function catchCopyEvent(copied: boolean | "throws" = true) {
    const data: Record<string, string> = {};
    const doc = document as Document & { execCommand: unknown };
    const execCommand = vi.fn((command: string) => {
      if (copied === "throws") {
        throw new Error("Not allowed");
      }
      const event = new Event("copy", { bubbles: true, cancelable: true });
      Object.defineProperty(event, "clipboardData", {
        value: { setData: (type: string, value: string) => (data[type] = value) },
      });
      document.dispatchEvent(event);
      return copied && command === "copy" && event.defaultPrevented;
    });
    doc.execCommand = execCommand;
    return { data, execCommand };
  }

  const copied = (html: string) => {
    const div = document.createElement("div");
    div.innerHTML = html;
    return div.firstElementChild as HTMLTableElement;
  };

  afterEach(() => {
    delete (document as unknown as { execCommand?: unknown }).execCommand;
  });

  it("opens from a button in the bar, before the info panel's", async () => {
    const { el } = await mountExport();
    const button = toggle(el);
    expect(button.getAttribute("aria-label")).toBe("Export the table");
    expect(button.getAttribute("aria-expanded")).toBe("false");
    expect(button.getAttribute("aria-controls")).toBe(panel(el).id);
    expect(button.nextElementSibling).toBe(panel(el));
    expect(panel(el).nextElementSibling).toBe(el.querySelector('.gt-i-bar [data-gti-bar="info"]'));
    expect(panel(el).getAttribute("role")).toBe("group");
    expect(panel(el).getAttribute("aria-label")).toBe("Export");
    expect(panel(el).id).not.toBe(el.querySelector(".gt-i-info:not(.gt-i-export)")?.id);
    expect(panel(el).hidden).toBe(true);

    button.click();
    expect(panel(el).hidden).toBe(false);
    expect(button.getAttribute("aria-expanded")).toBe("true");
    button.click();
    expect(panel(el).hidden).toBe(true);
  });

  it("has a button for each format, in the author's order", async () => {
    const { el } = await mountExport({ export: { formats: ["clipboard", "csv"] } });
    const buttons = Array.from(panel(el).querySelectorAll("button"), (button) => button.textContent);
    expect(buttons).toEqual(["Copy", "Download CSV"]);
    const { el: one } = await mountExport({ export: { formats: ["csv"] } });
    expect(Array.from(panel(one).querySelectorAll("button"), (button) => button.textContent)).toEqual([
      "Download CSV",
    ]);
    const { el: all } = await mountExport({ export: { formats: ["json", "tsv", "csv", "clipboard"] } });
    expect(Array.from(panel(all).querySelectorAll("button"), (button) => button.textContent)).toEqual([
      "Download JSON",
      "Download TSV",
      "Download CSV",
      "Copy",
    ]);
  });

  it("isn't there without formats", async () => {
    const { el } = await mountExport({ export: { formats: [] } });
    expect(toggle(el)).toBeNull();
    expect(panel(el)).toBeNull();
    const plain = await mountTable(GROUPED, { controls: { search: true, bar: true } });
    expect(toggle(plain)).toBeNull();
  });

  it("is one panel open at a time with the info panel", async () => {
    const { el } = await mountExport();
    const info = el.querySelector('.gt-i-bar [data-gti-bar="info"]') as HTMLButtonElement;
    const infoPanel = el.querySelector(".gt-i-info:not(.gt-i-export)") as HTMLElement;
    toggle(el).click();
    info.click();
    expect(panel(el).hidden).toBe(true);
    expect(toggle(el).getAttribute("aria-expanded")).toBe("false");
    expect(infoPanel.hidden).toBe(false);
    toggle(el).click();
    expect(infoPanel.hidden).toBe(true);
    expect(panel(el).hidden).toBe(false);
  });

  it("says how many rows it exports", async () => {
    const { el } = await mountExport();
    expect(status(el).textContent).toBe("5 rows");
    el.search = "a";
    expect(status(el).textContent).toBe("3 rows (filtered from 5)");
    el.search = "zzz";
    expect(status(el).textContent).toBe("0 rows (filtered from 5)");
  });

  it("exports the rows the search keeps, on every page, in the order shown", async () => {
    const { el } = await mountExport();
    expect(lines(el.toCSV())).toEqual([",row,x,y", "b,row_4,,a", "b,row_1,20,b", "b,row_5,20,a", "a,row_2,5,a", "a,row_3,10,c"]);

    el.sort = [{ column: "x", descending: true }];
    el.page = 2;
    el.search = "a";
    expect(lines(el.toCSV())).toEqual([",row,x,y", "b,row_5,20,a", "b,row_4,,a", "a,row_2,5,a"]);
  });

  it("leaves out summary rows, and has no group column without groups", async () => {
    const el = await mountTable([{ grand_summary: "Max", side: "top" }, 0, 1, 2, 3, 4], {
      controls: { bar: true },
      export: { formats: ["csv"] },
    });
    expect(lines(el.toCSV())).toEqual(["row,x,y", "row_1,20,b", "row_2,5,a", "row_3,10,c", "row_4,,a", "row_5,20,a"]);
  });

  it("labels the group column's cells with groups as a column", async () => {
    const body: BodyRow[] = [{ group: "b" }, 3, 0, 4, { group: "a" }, 1, 2];
    const el = await mountTable(body, { groupsAsColumn: true, controls: { bar: true }, export: { formats: ["csv"] } });
    expect(lines(el.toCSV())).toEqual([",row,x,y", "b,row_4,,a", "b,row_1,20,b", "b,row_5,20,a", "a,row_2,5,a", "a,row_3,10,c"]);
  });

  it("labels columns with their spanners', and the text they show", async () => {
    // A spanner over `x` and `y`, the latter's label with a footnote mark
    const thead =
      `<tr class="gt_col_headings gt_spanner_row"><th class="gt_col_heading" rowspan="2"></th>` +
      `<th class="gt_column_spanner_outer" colspan="2" id="t-s"><span class="gt_column_spanner">Values</span></th></tr>` +
      `<tr class="gt_col_headings"><th class="gt_col_heading" id="t-x">x</th>` +
      `<th class="gt_col_heading" id="t-y"> y\n<span class="gt_footnote_marks">1</span></th></tr>`;
    const { el } = await mountExport({
      thead,
      spanners: [{ id: "s", level: 1, columns: ["x", "y"], header: "t-s" }],
    });
    expect(lines(el.toCSV())[0]).toBe(",row,Values – x,Values – y");
  });

  it("guards cells a spreadsheet would read as a formula, unless asked not to", async () => {
    const { el } = await mountExport({ yLabel: "=y" });
    expect(lines(el.toCSV())[0]).toBe(",row,x,'=y");
    expect(lines(el.toCSV({ guard: false }))[0]).toBe(",row,x,=y");
  });

  it("exports the selected rows, when asked, whether or not the search keeps them", async () => {
    const { el } = await mountExport({ controls: { selection: "multiple" } });
    const item = selectedOnly(el)?.closest("label") as HTMLElement;
    expect(item.textContent).toBe("Selected rows only");
    expect(item.hidden).toBe(true);
    expect(el.toCSV({ selected: true })).toBe(",row,x,y\r\n");

    el.selection = [2, 0];
    expect(item.hidden).toBe(false);
    el.search = "c";
    expect(lines(el.toCSV({ selected: true }))).toEqual([",row,x,y", "b,row_1,20,b", "a,row_3,10,c"]);
    expect(lines(el.toCSV())).toEqual([",row,x,y", "a,row_3,10,c"]);

    check(el, true);
    expect(status(el).textContent).toBe("2 rows selected");
    // (Unchecked when there's no longer a selection)
    el.selection = [];
    expect(item.hidden).toBe(true);
    expect(selectedOnly(el)?.checked).toBe(false);
    expect(status(el).textContent).toBe("1 row (filtered from 5)");
  });

  it("has no selected rows option without selection", async () => {
    const { el } = await mountExport();
    expect(selectedOnly(el)).toBeNull();
  });

  it("gives each row of a merged stub cell its text", async () => {
    const { html, spec } = gtTable([0, 1, 2, 3, 4], { controls: { bar: true }, export: { formats: ["csv"] } });
    const merged = html
      .replace(`<th class="gt_row gt_left gt_stub">row_1</th>`, `<th class="gt_row gt_left gt_stub" rowspan="2">row_1</th>`)
      .replace(`<th class="gt_row gt_left gt_stub">row_2</th>`, "");
    const el = await mount(`<gt-table>${merged}${specScript(spec)}</gt-table>`);
    expect(el.sortableColumns).toEqual([]);
    // (With a bar for the export alone)
    expect(el.querySelector<HTMLElement>(".gt-i-bar")?.hidden).toBe(false);
    expect(toggle(el)).not.toBeNull();
    expect(lines(el.toCSV())).toEqual(["row,x,y", "row_1,20,b", "row_1,5,a", "row_3,10,c", "row_4,,a", "row_5,20,a"]);
  });

  it("downloads CSV, with a byte order mark, named as the author asked", async () => {
    const { blobs, links, revoke } = catchDownload();
    const { el, events } = await mountExport();
    toggle(el).click();
    vi.useFakeTimers();
    try {
      action(el, "csv").click();
      expect(links).toEqual([{ href: "blob:gti-1", download: "towny.csv", connected: true }]);
      expect(el.querySelector("a[download]")).toBeNull();
      expect(revoke).not.toHaveBeenCalled();
      vi.advanceTimersByTime(4e4);
      expect(revoke).toHaveBeenCalledWith("blob:gti-1");
    } finally {
      vi.useRealTimers();
    }
    const blob = blobs[0] as Blob;
    expect(blob.type).toBe("text/csv;charset=utf-8");
    const bytes = new Uint8Array(await blob.arrayBuffer());
    expect(Array.from(bytes.slice(0, 3))).toEqual([0xef, 0xbb, 0xbf]);
    expect(new TextDecoder().decode(bytes.slice(3))).toBe(el.toCSV());

    expect(events).toEqual([{ format: "csv", rows: [3, 0, 4, 1, 2] }]);
    expect(status(el).textContent).toBe("Downloaded 5 rows");
    expect(live(el)).toBe("Downloaded 5 rows");
    // (Still open, to export again)
    expect(panel(el).hidden).toBe(false);
  });

  it("downloads the selected rows, when asked", async () => {
    const { blobs } = catchDownload();
    const { el, events } = await mountExport({ controls: { selection: "multiple" }, export: { formats: ["csv"] } });
    el.selection = [1];
    check(el, true);
    action(el, "csv").click();
    expect((await (blobs[0] as Blob).text()).replace("\uFEFF", "")).toBe(",row,x,y\r\na,row_2,5,a\r\n");
    expect(events).toEqual([{ format: "csv", rows: [1] }]);
    expect(status(el).textContent).toBe("Downloaded 1 row");
  });

  it("downloads TSV, with a byte order mark, guarding formulas", async () => {
    const { blobs, links } = catchDownload();
    const { el, events } = await mountExport({ yLabel: "=y", export: { formats: ["tsv"], filename: "towny" } });
    el.search = "a";
    action(el, "tsv").click();
    expect(links).toEqual([{ href: "blob:gti-1", download: "towny.tsv", connected: true }]);
    const blob = blobs[0] as Blob;
    expect(blob.type).toBe("text/tab-separated-values;charset=utf-8");
    const bytes = new Uint8Array(await blob.arrayBuffer());
    expect(Array.from(bytes.slice(0, 3))).toEqual([0xef, 0xbb, 0xbf]);
    expect(new TextDecoder().decode(bytes.slice(3))).toBe("\trow\tx\t'=y\nb\trow_4\t\ta\nb\trow_5\t20\ta\na\trow_2\t5\ta\n");
    expect(new TextDecoder().decode(bytes.slice(3))).toBe(el.toTSV());
    expect(el.toTSV({ guard: false }).split("\n")[0]).toBe("\trow\tx\t=y");
    expect(events).toEqual([{ format: "tsv", rows: [3, 4, 1] }]);
    expect(status(el).textContent).toBe("Downloaded 3 rows");
  });

  it("downloads JSON, an object for each row, keyed by the columns' ids", async () => {
    const { blobs, links } = catchDownload();
    const { el, events } = await mountExport({
      controls: { selection: "multiple" },
      export: { formats: ["json"], filename: "towny" },
    });
    expect(el.toRecords()[0]).toEqual({ group: "b", row: "row_4", x: "", y: "a" });
    el.selection = [2, 0];
    check(el, true);
    action(el, "json").click();
    expect(links).toEqual([{ href: "blob:gti-1", download: "towny.json", connected: true }]);
    const blob = blobs[0] as Blob;
    expect(blob.type).toBe("application/json;charset=utf-8");
    // (Without a byte order mark, which JSON can't have)
    const text = new TextDecoder("utf-8", { ignoreBOM: true }).decode(await blob.arrayBuffer());
    expect(text).toBe(
      '[\n  {\n    "group": "b",\n    "row": "row_1",\n    "x": "20",\n    "y": "b"\n  },\n' +
        '  {\n    "group": "a",\n    "row": "row_3",\n    "x": "10",\n    "y": "c"\n  }\n]\n',
    );
    expect(JSON.parse(text)).toEqual(el.toRecords({ selected: true }));
    expect(events).toEqual([{ format: "json", rows: [0, 2] }]);
    expect(status(el).textContent).toBe("Downloaded 2 rows");
  });

  it("keys a row's group apart from a column of that id, and leaves it out without groups", async () => {
    const { html, spec } = gtTable(GROUPED, { controls: { bar: true }, export: { formats: ["json"] } });
    // (`y` as "group", then "_group")
    for (const id of ["group", "_group"]) {
      const named = { ...spec, columns: spec.columns.map((c) => (c.id === "y" ? { ...c, id } : c)) };
      const el = await mount(`<gt-table>${html}${specScript(named)}</gt-table>`);
      expect(el.toRecords()[0]).toEqual({ [id === "group" ? "_group" : "group"]: "b", row: "row_4", x: "", [id]: "a" });
    }
    const flat = await mountTable([0, 1, 2, 3, 4], {
      controls: { bar: true },
      export: { formats: ["json"] },
      columns: { x: { hideable: true } },
    });
    expect(flat.toRecords()[1]).toEqual({ row: "row_2", x: "5", y: "a" });
    // (Nor any hidden column, in the order shown)
    flat.hiddenColumns = ["x"];
    expect(flat.toRecords()[1]).toEqual({ row: "row_2", y: "a" });
  });

  it("copies the rows as an HTML table and as tab-separated text", async () => {
    const written = catchClipboard();
    const { el, events } = await mountExport();
    // An author's style, and one of GTI's
    const td = el.rowElement(0)?.querySelector("td") as HTMLElement;
    td.style.cssText = "color: red; text-align: center; top: 3px; --gt-i-x: 1px";
    td.innerHTML = `20<span class="gt_footnote_marks">2</span>`;
    action(el, "clipboard").click();
    await tick();

    expect(written).toHaveLength(1);
    const { "text/plain": text, "text/html": html } = written[0] as { "text/plain": string; "text/html": string };
    expect(text).toBe("\trow\tx\ty\nb\trow_4\t\ta\nb\trow_1\t20\tb\nb\trow_5\t20\ta\na\trow_2\t5\ta\na\trow_3\t10\tc");
    const table = copied(html);
    expect(Array.from(table.rows, (tr) => Array.from(tr.cells, (cell) => cell.textContent))).toEqual([
      ["", "row", "x", "y"],
      ["b", "row_4", "", "a"],
      ["b", "row_1", "20", "b"],
      ["b", "row_5", "20", "a"],
      ["a", "row_2", "5", "a"],
      ["a", "row_3", "10", "c"],
    ]);
    expect(table.querySelectorAll("thead th")).toHaveLength(4);
    expect(table.querySelectorAll("[class], [id], [rowspan], [headers]")).toHaveLength(0);
    // (The stub's cells are still header cells)
    const row1 = table.rows[2] as HTMLTableRowElement;
    expect(Array.from(row1.cells, (cell) => cell.tagName)).toEqual(["TD", "TH", "TD", "TD"]);
    expect(Array.from(row1.cells, (cell) => cell.style.textAlign)).toEqual(["", "left", "center", "left"]);
    const x = row1.cells[2] as HTMLElement;
    expect(x.style.color).toBe("red");
    expect(x.style.top).toBe("");
    expect(x.style.getPropertyValue("--gt-i-x")).toBe("");
    expect(Array.from((table.rows[1] as HTMLTableRowElement).cells, (cell) => cell.style.textAlign)).toEqual([
      "",
      "left",
      "right",
      "left",
    ]);
    // (Leaving the table's own cells as they were)
    expect(td.querySelector(".gt_footnote_marks")).not.toBeNull();

    expect(events).toEqual([{ format: "clipboard", rows: [3, 0, 4, 1, 2] }]);
    expect(status(el).textContent).toBe("Copied 5 rows");
    expect(live(el)).toBe("Copied 5 rows");
  });

  it("copies as a copy would, without the Clipboard API", async () => {
    catchClipboard("rejected");
    const { data, execCommand } = catchCopyEvent();
    const { el, events } = await mountExport();
    el.search = "c";
    action(el, "clipboard").click();
    await tick();
    expect(execCommand).toHaveBeenCalledWith("copy");
    expect(data["text/plain"]).toBe("\trow\tx\ty\na\trow_3\t10\tc");
    expect(copied(data["text/html"] as string).rows).toHaveLength(2);
    expect(events).toEqual([{ format: "clipboard", rows: [2] }]);
    // (Only for the copy)
    document.dispatchEvent(new Event("copy"));
    expect(execCommand).toHaveBeenCalledTimes(1);

    // And when the Clipboard API isn't there at all
    vi.spyOn(navigator.clipboard, "write").mockImplementation(() => {
      throw new TypeError("No clipboard");
    });
    await expect(el.copyTable()).resolves.toBe(true);
    expect(execCommand).toHaveBeenCalledTimes(2);
  });

  it("says when it couldn't copy", async () => {
    catchClipboard("rejected");
    catchCopyEvent(false);
    const { el, events } = await mountExport();
    action(el, "clipboard").click();
    await tick();
    expect(status(el).textContent).toBe("Couldn't copy the rows");
    expect(live(el)).toBe("Couldn't copy the rows");
    expect(events).toEqual([]);

    catchCopyEvent("throws");
    await expect(el.copyTable()).resolves.toBe(false);
  });

  it("exports from code without an event", async () => {
    const written = catchClipboard();
    const { el, events } = await mountExport({ controls: { selection: "multiple" } });
    el.selection = [4];
    await expect(el.copyTable({ selected: true })).resolves.toBe(true);
    expect(written[0]?.["text/plain"]).toBe("\trow\tx\ty\nb\trow_5\t20\ta");
    el.toCSV();
    el.toTSV();
    el.toRecords();
    expect(events).toEqual([]);
    // (Nor does it change the panel)
    expect(status(el).textContent).toBe("5 rows");
  });

  it("exports nothing before the table is ready", async () => {
    const el = await mount("<gt-table><table></table></gt-table>");
    expect(el.toCSV()).toBe("");
    expect(el.toTSV()).toBe("");
    expect(el.toRecords()).toEqual([]);
    await expect(el.copyTable()).resolves.toBe(false);
  });

  describe("as code", () => {
    // `x`, of floats, with a range, and `y`, of strings, with a facet; the data pandas'
    const CODE: CodeSpec = {
      backend: "pandas",
      columns: {
        x: { dtype: "float", nullable: false, literals: null },
        y: { dtype: "string", nullable: false, literals: ['"a"', '"b"', '"c"'] },
      },
    };
    const FILTERS: FilterSpec[] = [
      { column: "x", type: "range", values: [5, 10, 20] },
      { column: "y", type: "facet", values: ["a", "b", "c"] },
    ];
    const PANDAS = 'df[\n    df["y"].isin(["a"])\n].sort_values(["x"], ascending=[False], na_position="last", kind="stable")\n';
    const mountCode = (code: CodeSpec | null = CODE, options: TableOptions = {}) =>
      mountExport({ filters: FILTERS, export: { formats: ["csv", "clipboard", "code"], code }, ...options });
    const select = (el: GtTable) => panel(el).querySelector("select") as HTMLSelectElement;
    const note = (el: GtTable) => panel(el).querySelector(".gt-i-export-note") as HTMLElement;
    const view = (el: GtTable) => {
      el.filter = { and: [{ col: "y", op: "in", value: ["a"] }] };
      el.sort = [{ column: "x", descending: true }];
    };

    it("has a choice of library, the data's to begin with", async () => {
      const { el } = await mountCode();
      const item = select(el).closest("label") as HTMLElement;
      expect(item.textContent).toBe("Code forPolarspandasNarwhals");
      expect(Array.from(select(el).options, (option) => [option.value, option.textContent])).toEqual([
        ["polars", "Polars"],
        ["pandas", "pandas"],
        ["narwhals", "Narwhals"],
      ]);
      expect(select(el).value).toBe("pandas");
      expect(Array.from(panel(el).querySelectorAll("button"), (button) => button.textContent)).toEqual([
        "Download CSV",
        "Copy",
        "Copy code",
      ]);
      const { el: polars } = await mountCode({ ...CODE, backend: "polars" });
      expect(select(polars).value).toBe("polars");
    });

    it("isn't there without the code's spec", async () => {
      const { el } = await mountCode(null);
      expect(select(el)).toBeNull();
      expect(action(el, "code")).toBeNull();
      expect(note(el)).toBeNull();
      expect(el.toCode()).toBe("");
      // (Nor without the format)
      const { el: csv } = await mountExport({ filters: FILTERS, export: { formats: ["csv"], code: CODE } });
      expect(select(csv)).toBeNull();
      expect(action(csv, "code")).toBeNull();
    });

    it("copies the view's code, for the library chosen", async () => {
      const written = catchClipboard();
      const { el, events } = await mountCode();
      view(el);
      toggle(el).click();
      action(el, "code").click();
      await tick();
      expect(written).toEqual([{ "text/plain": PANDAS }]);
      expect(events).toEqual([{ format: "code", rows: [], code: PANDAS, backend: "pandas" }]);
      expect(status(el).textContent).toBe("Copied the code");
      expect(live(el)).toBe("Copied the code");

      select(el).value = "polars";
      select(el).dispatchEvent(new Event("change", { bubbles: true }));
      action(el, "code").click();
      await tick();
      const polars =
        'import polars as pl\n\ndf.filter(\n    pl.col("y").is_in(["a"]),\n' +
        ').sort(["x"], descending=[True], nulls_last=True, maintain_order=True)\n';
      expect(written[1]).toEqual({ "text/plain": polars });
      expect(events[1]).toEqual({ format: "code", rows: [], code: polars, backend: "polars" });
      // (Still open, to copy again)
      expect(panel(el).hidden).toBe(false);
    });

    it("leaves out the search, saying so, and the selection", async () => {
      const written = catchClipboard();
      const { el } = await mountCode(CODE, { controls: { selection: "multiple" } });
      view(el);
      expect(note(el).textContent).toBe("The code leaves out the search.");
      expect(note(el).hidden).toBe(true);
      el.search = "row_4";
      expect(note(el).hidden).toBe(false);
      el.selection = [1];
      check(el, true);
      action(el, "code").click();
      await tick();
      expect(written).toEqual([{ "text/plain": PANDAS }]);
      el.search = "";
      expect(note(el).hidden).toBe(true);
    });

    it("copies as a copy would, without the Clipboard API", async () => {
      catchClipboard("rejected");
      const { data } = catchCopyEvent();
      const { el, events } = await mountCode();
      view(el);
      action(el, "code").click();
      await tick();
      expect(data).toEqual({ "text/plain": PANDAS });
      expect(events).toHaveLength(1);
    });

    it("says when it couldn't copy the code, or write it", async () => {
      catchClipboard("rejected");
      catchCopyEvent(false);
      const { el, events } = await mountCode();
      action(el, "code").click();
      await tick();
      expect(status(el).textContent).toBe("Couldn't copy the code");
      expect(live(el)).toBe("Couldn't copy the code");

      // (A value without Python for it, as a duration's)
      const written = catchClipboard();
      const { el: other, events: others } = await mountCode({
        ...CODE,
        columns: { ...CODE.columns, y: { dtype: "other", nullable: false, literals: [null, null, null] } },
      });
      view(other);
      action(other, "code").click();
      await tick();
      expect(status(other).textContent).toBe("Couldn't write the code");
      expect(live(other)).toBe("Couldn't write the code");
      expect(() => other.toCode()).toThrow(RangeError);
      expect(written).toEqual([]);
      expect([...events, ...others]).toEqual([]);
    });

    it("writes the code from code, for any library, without an event", async () => {
      const { el, events } = await mountCode();
      expect(el.toCode()).toBe("df\n");
      view(el);
      expect(el.toCode()).toBe(PANDAS);
      expect(el.toCode("pandas")).toBe(PANDAS);
      expect(el.toCode("narwhals")).toMatch(/^import narwhals as nw\n\n\(\n {4}nw\.from_native\(df\)\n/);
      expect(() => el.toCode("duckdb" as never)).toThrow(
        new RangeError('`backend` must be "polars", "pandas" or "narwhals", not "duckdb"'),
      );
      expect(events).toEqual([]);
      expect(status(el).textContent).toBe("3 rows (filtered from 5)");
      // (Nor any before the table is ready)
      const bare = await mount("<gt-table><table></table></gt-table>");
      expect(bare.toCode()).toBe("");
    });
  });

  it("closes on Escape, giving focus back to its button", async () => {
    const { el } = await mountExport();
    toggle(el).click();
    action(el, "csv").focus();
    expect(press(action(el, "csv"), "Escape").defaultPrevented).toBe(true);
    expect(panel(el).hidden).toBe(true);
    expect(document.activeElement).toBe(toggle(el));
    expect(press(toggle(el), "Escape").defaultPrevented).toBe(false);
  });

  it("doesn't page with the keys pressed in it", async () => {
    const { el } = await mountExport();
    toggle(el).click();
    expect(press(action(el, "csv"), "ArrowRight").defaultPrevented).toBe(false);
    expect(el.page).toBe(1);
  });

  it("closes when focus goes elsewhere, and when the table goes", async () => {
    const { el } = await mountExport();
    const outside = el.querySelector("tbody td") as HTMLElement;
    toggle(el).click();
    action(el, "csv").dispatchEvent(new FocusEvent("focusout", { bubbles: true, relatedTarget: outside }));
    expect(panel(el).hidden).toBe(true);

    toggle(el).click();
    el.remove();
    expect(panel(el).hidden).toBe(true);
    expect((el as unknown as { outsidePress: unknown }).outsidePress).toBeNull();
  });
});

describe("filters", () => {
  afterEach(() => {
    vi.useRealTimers();
  });

  const RANGE: FilterSpec = { column: "x", type: "range", values: [5, 10, 20] };
  const FACET: FilterSpec = { column: "y", type: "facet", values: ["a", "b", "c"] };
  const filterButton = (el: GtTable, column: string) =>
    header(el, column).querySelector(".gt-i-filter-button") as HTMLButtonElement;
  const panel = (el: GtTable, column: string) =>
    el.querySelector(`#${filterButton(el, column).getAttribute("aria-controls")}`) as HTMLElement;
  const clearButton = (el: GtTable, column: string) =>
    panel(el, column).querySelector(".gt-i-filter-head button") as HTMLButtonElement;
  const inputs = (el: GtTable, column: string) =>
    Array.from(panel(el, column).querySelectorAll<HTMLInputElement>("input"));
  const options = (el: GtTable, column: string) =>
    Array.from(
      panel(el, column).querySelectorAll(".gt-i-filter-option"),
      (item) =>
        `${item.querySelector(".gt-i-filter-value")?.textContent} ${item.querySelector(".gt-i-filter-count")?.textContent}` +
        (item.hasAttribute("data-gti-none") ? " (none)" : ""),
    );
  const check = (el: GtTable, column: string, i: number) => inputs(el, column)[i]?.click();
  const type = (input: HTMLInputElement | undefined, value: string) => {
    (input as HTMLInputElement).value = value;
    input?.dispatchEvent(new Event("input", { bubbles: true }));
  };
  const press = (target: Element | undefined, key: string, shiftKey = false) => {
    const event = new KeyboardEvent("keydown", { key, shiftKey, bubbles: true, cancelable: true });
    target?.dispatchEvent(event);
    return event;
  };
  const leave = (from: Element, to: Element | null) =>
    from.dispatchEvent(new FocusEvent("focusout", { bubbles: true, relatedTarget: to }));

  // A range on `x` and a facet on `y`, in the bar's table, unless set otherwise
  async function mountFilters(options: TableOptions = {}) {
    const el = await mountTable(GROUPED, {
      filters: [RANGE, FACET],
      ...options,
      controls: { bar: true, ...options.controls },
    });
    const events: FilterEventDetail[] = [];
    el.addEventListener(FILTER_EVENT, (event) => events.push((event as CustomEvent<FilterEventDetail>).detail));
    return { el, events };
  }

  it("puts a filter button in the label of each column that can be filtered, after its sort button", async () => {
    const { el } = await mountFilters();
    expect(el.filterableColumns).toEqual(["x", "y"]);
    for (const column of ["x", "y"]) {
      const filter = filterButton(el, column);
      expect(filter.previousElementSibling).toBe(button(el, column));
      expect(filter.type).toBe("button");
      expect(filter.title).toBe("Filter");
      expect(filter.getAttribute("aria-label")).toBe(`Filter ${column}`);
      expect(filter.getAttribute("aria-expanded")).toBe("false");
      expect(header(el, column).hasAttribute("data-gti-filtered")).toBe(false);
    }
    // (Its panel is made when it first opens)
    expect(el.querySelector(".gt-i-filter")).toBeNull();
  });

  it("has no filters without any in the spec", async () => {
    const el = await mountTable();
    expect(el.filterableColumns).toEqual([]);
    expect(el.querySelector(".gt-i-filter-button")).toBeNull();
    expect(el.filter).toBeNull();
    el.filter = null;
    expect(() => {
      el.filter = { and: [{ col: "x", op: "gte", value: 1 }] };
    }).toThrow(/"x" isn't a column that can be filtered/);
  });

  it("ignores a filter on a column the table doesn't have, and a second one on a column", async () => {
    const { el } = await mountFilters({
      filters: [{ column: "w", type: "text", values: null }, RANGE, { ...RANGE, type: "facet" }],
    });
    expect(el.filterableColumns).toEqual(["x"]);
    expect(el.querySelectorAll(".gt-i-filter-button")).toHaveLength(1);
  });

  it("opens a panel for a filter from its button, and closes it from it", async () => {
    const { el } = await mountFilters();
    filterButton(el, "y").click();
    const open = panel(el, "y");
    expect(open.hidden).toBe(false);
    expect(open.getAttribute("role")).toBe("group");
    expect(open.getAttribute("aria-label")).toBe("Filter y");
    expect(open.dataset.gtiFilter).toBe("facet");
    expect(open.querySelector(".gt-i-filter-title")?.textContent).toBe("y");
    expect(clearButton(el, "y").getAttribute("aria-label")).toBe("Clear the filter on y");
    expect(clearButton(el, "y").getAttribute("aria-disabled")).toBe("true");
    expect(filterButton(el, "y").getAttribute("aria-expanded")).toBe("true");
    // (Its first field has focus; the panel is in the element, outside the table)
    expect(document.activeElement).toBe(inputs(el, "y")[0]);
    expect(open.parentElement).toBe(el);

    filterButton(el, "y").click();
    expect(open.hidden).toBe(true);
    expect(filterButton(el, "y").getAttribute("aria-expanded")).toBe("false");
    // One panel is open at a time
    filterButton(el, "y").click();
    filterButton(el, "x").click();
    expect(panel(el, "y").hidden).toBe(true);
    expect(panel(el, "x").hidden).toBe(false);
    expect(panel(el, "x").id).not.toBe(panel(el, "y").id);
  });

  it("chooses a facet's values, counting the rows with each", async () => {
    const { el, events } = await mountFilters();
    filterButton(el, "y").click();
    expect(options(el, "y")).toEqual(["a 3", "b 1", "c 1"]);

    check(el, "y", 2);
    expect(el.filter).toEqual({ and: [{ col: "y", op: "in", value: ["c"] }] });
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
    expect(events).toEqual([{ filter: { and: [{ col: "y", op: "in", value: ["c"] }] }, count: 1 }]);
    expect(live(el)).toBe("Showing 1 of 5 rows");
    expect(header(el, "y").hasAttribute("data-gti-filtered")).toBe(true);
    expect(filterButton(el, "y").getAttribute("aria-label")).toBe("Filter y (on)");
    expect(clearButton(el, "y").getAttribute("aria-disabled")).toBe("false");
    // (Its own values keep their counts)
    expect(options(el, "y")).toEqual(["a 3", "b 1", "c 1"]);

    check(el, "y", 1);
    expect(el.filter).toEqual({ and: [{ col: "y", op: "in", value: ["b", "c"] }] });
    expect(visible(el)).toEqual(["group:b", 0, "summary:Total", "group:a", 2, "grand:Max"]);
    check(el, "y", 2);
    check(el, "y", 1);
    expect(el.filter).toBeNull();
    expect(live(el)).toBe("Showing all 5 rows");
    expect(events[events.length - 1]).toEqual({ filter: null, count: 5 });
    expect(header(el, "y").hasAttribute("data-gti-filtered")).toBe(false);
  });

  it("counts a facet's rows within the search and the other filters", async () => {
    const { el } = await mountFilters({ controls: { search: true } });
    el.filter = { and: [{ col: "x", op: "gte", value: 10 }] };
    filterButton(el, "y").click();
    expect(options(el, "y")).toEqual(["a 1", "b 1", "c 1"]);
    el.search = "row_1";
    expect(options(el, "y")).toEqual(["a 0 (none)", "b 1", "c 0 (none)"]);
    // (A value without any can still be chosen)
    check(el, "y", 0);
    expect(visible(el)).toEqual(["grand:Max"]);
    expect(live(el)).toBe("No matching rows");
  });

  it("lists a facet's missing value last, as the cells show the values", async () => {
    const { el } = await mountFilters({ filters: [{ ...RANGE, type: "facet" }] });
    filterButton(el, "x").click();
    expect(options(el, "x")).toEqual(["5 1", "10 1", "20 2", "(Missing) 1"]);
    check(el, "x", 3);
    expect(el.filter).toEqual({ and: [{ col: "x", op: "in", value: [null] }] });
    expect(visible(el)).toEqual(["group:b", 3, "summary:Total", "grand:Max"]);
  });

  it("filters by a range once typing pauses, or at once on Enter", async () => {
    const { el, events } = await mountFilters();
    filterButton(el, "x").click();
    const [min, max] = inputs(el, "x");
    expect(min?.getAttribute("aria-label")).toBe("x, at least");
    expect(max?.getAttribute("aria-label")).toBe("x, at most");
    expect([min?.placeholder, max?.placeholder]).toEqual(["5", "20"]);
    expect(min?.inputMode).toBe("decimal");

    vi.useFakeTimers();
    type(min, "10");
    vi.advanceTimersByTime(100);
    expect(events).toEqual([]);
    vi.advanceTimersByTime(50);
    expect(el.filter).toEqual({ and: [{ col: "x", op: "gte", value: 10 }] });
    expect(visible(el)).toEqual(["group:b", 0, 4, "summary:Total", "group:a", 2, "grand:Max"]);
    expect(events).toEqual([{ filter: { and: [{ col: "x", op: "gte", value: 10 }] }, count: 3 }]);
    expect(live(el)).toBe("Showing 3 of 5 rows");

    type(max, " 10 ");
    expect(press(max, "Enter").defaultPrevented).toBe(true);
    expect(el.filter).toEqual({
      and: [
        { col: "x", op: "gte", value: 10 },
        { col: "x", op: "lte", value: 10 },
      ],
    });
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
    // (Nothing more once the time's up, nor on Enter when nothing changed)
    vi.advanceTimersByTime(500);
    press(max, "Enter");
    expect(events).toHaveLength(2);
  });

  it("marks a bound that isn't a number, keeping the one before", async () => {
    const { el, events } = await mountFilters();
    filterButton(el, "x").click();
    const [min] = inputs(el, "x");
    type(min, "10");
    press(min, "Enter");
    type(min, "1O");
    press(min, "Enter");
    expect(min?.getAttribute("aria-invalid")).toBe("true");
    expect(el.filter).toEqual({ and: [{ col: "x", op: "gte", value: 10 }] });
    expect(events).toHaveLength(1);

    type(min, "");
    press(min, "Enter");
    expect(min?.hasAttribute("aria-invalid")).toBe(false);
    expect(el.filter).toBeNull();
  });

  it("filters by the text a column shows, and with the search", async () => {
    const { el, events } = await mountFilters({
      filters: [{ column: "y", type: "text", values: null }],
      controls: { search: true },
    });
    filterButton(el, "y").click();
    const [input] = inputs(el, "y");
    expect(input?.className).toBe("gt-i-filter-text");
    expect(input?.placeholder).toBe("Contains");
    expect(input?.getAttribute("aria-label")).toBe("y contains");

    type(input, " A ");
    press(input, "Enter");
    expect(el.filter).toEqual({ and: [{ col: "y", op: "contains", value: "A" }] });
    expect(visible(el)).toEqual(["group:b", 3, 4, "summary:Total", "group:a", 1, "grand:Max"]);
    expect(events).toEqual([{ filter: { and: [{ col: "y", op: "contains", value: "A" }] }, count: 3 }]);
    // (In its column only; and the search has to match too)
    type(input, "row");
    press(input, "Enter");
    expect(visible(el)).toEqual(["grand:Max"]);
    type(input, "a");
    press(input, "Enter");
    el.search = "row_4";
    expect(visible(el)).toEqual(["group:b", 3, "summary:Total", "grand:Max"]);
  });

  it("clears a filter from its panel, keeping focus on the Clear button", async () => {
    const { el, events } = await mountFilters();
    filterButton(el, "y").click();
    check(el, "y", 0);
    clearButton(el, "y").focus();
    clearButton(el, "y").click();
    expect(el.filter).toBeNull();
    expect(inputs(el, "y").map((box) => box.checked)).toEqual([false, false, false]);
    expect(events[events.length - 1]).toEqual({ filter: null, count: 5 });
    expect(clearButton(el, "y").getAttribute("aria-disabled")).toBe("true");
    expect(document.activeElement).toBe(clearButton(el, "y"));
    // (Not again)
    clearButton(el, "y").click();
    expect(events).toHaveLength(2);
  });

  it("gets and sets the filters as a query, without an event", async () => {
    const { el, events } = await mountFilters({ pagination: { enabled: true } });
    el.page = 2;
    el.filter = {
      and: [
        { col: "y", op: "in", value: ["a", "b"] },
        { col: "x", op: "lte", value: 10 },
      ],
    };
    expect(el.filter).toEqual({
      and: [
        { col: "x", op: "lte", value: 10 },
        { col: "y", op: "in", value: ["a", "b"] },
      ],
    });
    expect(el.page).toBe(1);
    expect(visible(el)).toEqual(["group:a", 1, "grand:Max"]);
    expect(events).toEqual([]);
    expect(header(el, "x").hasAttribute("data-gti-filtered")).toBe(true);
    expect(header(el, "y").hasAttribute("data-gti-filtered")).toBe(true);

    // The panels show it, open or not
    filterButton(el, "x").click();
    expect(inputs(el, "x").map((input) => input.value)).toEqual(["", "10"]);
    el.filter = { and: [{ col: "x", op: "gte", value: 6 }] };
    expect(inputs(el, "x").map((input) => input.value)).toEqual(["6", ""]);
    filterButton(el, "y").click();
    expect(inputs(el, "y").map((box) => box.checked)).toEqual([false, false, false]);
    el.filter = null;
    expect(el.filter).toBeNull();
    expect(visible(el)).toEqual(["group:b", 3, 0, "grand:Max"]);
    expect(header(el, "x").hasAttribute("data-gti-filtered")).toBe(false);
  });

  it("rejects a query that it can't take, changing nothing", async () => {
    const { el } = await mountFilters();
    const query = { and: [{ col: "x", op: "gte" as const, value: 10 }] };
    el.filter = query;
    for (const bad of [
      { and: [{ col: "y", op: "in", value: ["d"] }] },
      { and: [{ col: "y", op: "in", value: ["a"] }, { col: "x", op: "contains", value: "1" }] },
      { and: [{ col: "row", op: "contains", value: "1" }] },
      { or: [] },
    ]) {
      expect(() => {
        el.filter = bad as never;
      }).toThrow(RangeError);
      expect(el.filter).toEqual(query);
    }
    expect(visible(el)).toEqual(["group:b", 0, 4, "summary:Total", "group:a", 2, "grand:Max"]);
  });

  it("filters a column without a label by the `filter` property only", async () => {
    const { el } = await mountFilters({ filters: [{ column: "row", type: "text", values: null }] });
    expect(el.filterableColumns).toEqual(["row"]);
    expect(el.querySelector(".gt-i-filter-button")).toBeNull();
    el.filter = { and: [{ col: "row", op: "contains", value: "ROW_2" }] };
    expect(visible(el)).toEqual(["group:a", 1, "grand:Max"]);
  });

  it("selects the rows that the filters keep with the select-all checkbox", async () => {
    const { el } = await mountFilters({ controls: { selection: "multiple", search: true } });
    const all = el.querySelector<HTMLInputElement>("thead .gt-i-select input") as HTMLInputElement;
    el.filter = { and: [{ col: "y", op: "in", value: ["a"] }] };
    expect(all.getAttribute("aria-label")).toBe("Select all matching rows");
    all.click();
    expect(el.selection).toEqual([1, 3, 4]);
    // (And the search's too)
    el.search = "row_2";
    all.click();
    expect(el.selection).toEqual([3, 4]);
  });

  it("closes on Escape, giving focus back to its button", async () => {
    const { el } = await mountFilters();
    filterButton(el, "y").click();
    const event = press(inputs(el, "y")[1], "Escape");
    expect(event.defaultPrevented).toBe(true);
    expect(panel(el, "y").hidden).toBe(true);
    expect(document.activeElement).toBe(filterButton(el, "y"));
  });

  it("closes on Tab out of either end, giving focus back to its button", async () => {
    const { el } = await mountFilters();
    filterButton(el, "x").click();
    // (Not within it)
    expect(press(inputs(el, "x")[0], "Tab").defaultPrevented).toBe(false);
    expect(press(inputs(el, "x")[0], "Tab", true).defaultPrevented).toBe(false);
    expect(panel(el, "x").hidden).toBe(false);
    expect(press(inputs(el, "x")[1], "Tab").defaultPrevented).toBe(true);
    expect(panel(el, "x").hidden).toBe(true);
    expect(document.activeElement).toBe(filterButton(el, "x"));

    filterButton(el, "x").click();
    expect(press(clearButton(el, "x"), "Tab", true).defaultPrevented).toBe(true);
    expect(panel(el, "x").hidden).toBe(true);
  });

  it("closes on a press outside it, or when focus goes elsewhere", async () => {
    const { el } = await mountFilters();
    const outside = el.querySelector("tbody td") as HTMLElement;
    filterButton(el, "y").click();
    panel(el, "y").dispatchEvent(new PointerEvent("pointerdown", { bubbles: true, composed: true }));
    expect(panel(el, "y").hidden).toBe(false);
    outside.dispatchEvent(new PointerEvent("pointerdown", { bubbles: true, composed: true }));
    expect(panel(el, "y").hidden).toBe(true);
    expect(document.activeElement).not.toBe(filterButton(el, "y"));

    filterButton(el, "y").click();
    leave(filterButton(el, "y"), inputs(el, "y")[0] as Element);
    leave(inputs(el, "y")[0] as Element, filterButton(el, "y"));
    // (Not when the window loses focus)
    leave(inputs(el, "y")[0] as Element, null);
    expect(panel(el, "y").hidden).toBe(false);
    leave(inputs(el, "y")[0] as Element, outside);
    expect(panel(el, "y").hidden).toBe(true);
  });

  it("filters by what was typed when it closes before typing pauses", async () => {
    const { el, events } = await mountFilters();
    vi.useFakeTimers();
    filterButton(el, "x").click();
    type(inputs(el, "x")[0], "10");
    press(inputs(el, "x")[0], "Escape");
    expect(el.filter).toEqual({ and: [{ col: "x", op: "gte", value: 10 }] });
    expect(events).toHaveLength(1);
    vi.advanceTimersByTime(500);
    expect(events).toHaveLength(1);
  });

  it("closes the info panel when it opens, and the other way round", async () => {
    const { el } = await mountFilters();
    const info = el.querySelector(".gt-i-info") as HTMLElement;
    const toggle = el.querySelector('.gt-i-bar [data-gti-bar="info"]') as HTMLButtonElement;
    toggle.click();
    filterButton(el, "y").click();
    expect(info.hidden).toBe(true);
    expect(panel(el, "y").hidden).toBe(false);
    toggle.click();
    expect(info.hidden).toBe(false);
    expect(panel(el, "y").hidden).toBe(true);
  });

  it("shows the bar for filters alone, whose info panel says how the table is filtered", async () => {
    const { el, events } = await mountFilters();
    const bar = el.querySelector(".gt-i-bar") as HTMLElement;
    const item = el.querySelector('[data-gti-info="filters"]') as HTMLElement;
    const clear = item.querySelector("button") as HTMLButtonElement;
    const rows = el.querySelector(".gt-i-info-rows") as HTMLElement;
    expect(bar.hidden).toBe(false);
    expect(item.firstElementChild?.textContent).toBe("Not filtered");
    expect(clear.getAttribute("aria-label")).toBe("Clear the filters");
    expect(clear.getAttribute("aria-disabled")).toBe("true");
    // (Before the selection's and after the sort's)
    expect(item.previousElementSibling?.getAttribute("data-gti-info")).toBe("sort");

    el.filter = {
      and: [
        { col: "x", op: "gte", value: 10 },
        { col: "y", op: "in", value: ["a"] },
      ],
    };
    expect(item.firstElementChild?.textContent).toBe("Filtered by x, y");
    expect(rows.textContent).toBe("1 row (filtered from 5)");
    expect(clear.getAttribute("aria-disabled")).toBe("false");
    clear.click();
    expect(el.filter).toBeNull();
    expect(events).toEqual([{ filter: null, count: 5 }]);
    expect(live(el)).toBe("Showing all 5 rows");
    expect(item.firstElementChild?.textContent).toBe("Not filtered");
    expect(header(el, "x").hasAttribute("data-gti-filtered")).toBe(false);
  });

  it("works without the bar", async () => {
    const { el } = await mountFilters({ controls: { bar: false } });
    expect(el.querySelector(".gt-i-bar")).toBeNull();
    filterButton(el, "y").click();
    check(el, "y", 1);
    expect(visible(el)).toEqual(["group:b", 0, "summary:Total", "grand:Max"]);
  });

  it("goes when the table does", async () => {
    const { el } = await mountFilters();
    filterButton(el, "y").click();
    el.remove();
    expect(panel(el, "y").hidden).toBe(true);
    expect((el as unknown as { filterPress: unknown }).filterPress).toBeNull();
    expect((el as unknown as { filterScroll: unknown }).filterScroll).toBeNull();
  });
});

describe("filter tokens", () => {
  const RANGE: FilterSpec = { column: "x", type: "range", values: [5, 10, 20] };
  const FACET: FilterSpec = { column: "y", type: "facet", values: ["a", "b", "c"] };
  const row = (el: GtTable) => el.querySelector(".gt-i-tokens") as HTMLElement;
  const tokens = (el: GtTable) =>
    Array.from(row(el).querySelectorAll(".gt-i-token-open, .gt-i-token-clear"), (b) => b.textContent);
  const token = (el: GtTable, i: number) => row(el).querySelectorAll<HTMLButtonElement>(".gt-i-token-open")[i] as HTMLButtonElement;
  const remove = (el: GtTable, i: number) =>
    row(el).querySelectorAll<HTMLButtonElement>(".gt-i-token-remove")[i] as HTMLButtonElement;
  const clearAll = (el: GtTable) => row(el).querySelector(".gt-i-token-clear") as HTMLButtonElement;
  const panel = (el: GtTable) => el.querySelector(".gt-i-filter:not([hidden])") as HTMLElement | null;
  const press = (target: Element | null | undefined, key: string) => {
    const event = new KeyboardEvent("keydown", { key, bubbles: true, cancelable: true });
    target?.dispatchEvent(event);
    return event;
  };

  async function mountTokens(options: TableOptions = {}) {
    const el = await mountTable(GROUPED, {
      filters: [RANGE, FACET],
      ...options,
      controls: { bar: true, ...options.controls },
    });
    const events: FilterEventDetail[] = [];
    el.addEventListener(FILTER_EVENT, (event) => events.push((event as CustomEvent<FilterEventDetail>).detail));
    return { el, events };
  }

  it("shows a token for each filter that's on, in column order, above the rest of the bar", async () => {
    const { el } = await mountTokens();
    const list = row(el);
    expect(list.tagName).toBe("UL");
    expect(list.getAttribute("aria-label")).toBe("Filters");
    expect(list.parentElement?.classList.contains("gt-i-bar")).toBe(true);
    expect(list.hidden).toBe(true);

    el.filter = { and: [{ col: "y", op: "in", value: ["c", "b"] }] };
    expect(list.hidden).toBe(false);
    expect(tokens(el)).toEqual(["y: b, c"]);
    // (A token's whole text is its title too, as it can be cut short)
    expect(token(el, 0).title).toBe("y: b, c");
    expect(token(el, 0).getAttribute("aria-expanded")).toBe("false");
    expect(remove(el, 0).getAttribute("aria-label")).toBe("Remove the filter on y");

    el.filter = { and: [{ col: "y", op: "in", value: ["a"] }, { col: "x", op: "gte", value: 10 }] };
    expect(tokens(el)).toEqual(["x ≥ 10", "y: a", "Clear all"]);
    el.filter = null;
    expect(list.hidden).toBe(true);
    expect(tokens(el)).toEqual([]);
  });

  it("has no token row without filters, or without the bar", async () => {
    expect((await mountTokens({ filters: [] })).el.querySelector(".gt-i-tokens")).toBeNull();
    const { el } = await mountTokens({ controls: { bar: false } });
    el.filter = { and: [{ col: "x", op: "gte", value: 10 }] };
    expect(el.querySelector(".gt-i-tokens")).toBeNull();
  });

  it("says what a range keeps, with its bounds as the table shows them", async () => {
    const { el } = await mountTokens();
    el.setAttribute("lang", "de");
    el.filter = { and: [{ col: "x", op: "lte", value: 20 }] };
    expect(tokens(el)).toEqual(["x ≤ 20"]);
    el.filter = { and: [{ col: "x", op: "gte", value: 5 }, { col: "x", op: "lte", value: 10 }] };
    expect(tokens(el)).toEqual(["x 5–10"]);
    // (A bound that isn't one of the column's values, as a number in the page's language)
    el.filter = { and: [{ col: "x", op: "gte", value: 1234.5 }] };
    expect(tokens(el)).toEqual(["x ≥ 1.234,5"]);
  });

  it("says what a facet and a text filter keep, shortening a long list of values", async () => {
    const { el } = await mountTokens({
      filters: [{ ...RANGE, type: "facet" }, { column: "y", type: "text", values: null }],
    });
    el.filter = { and: [{ col: "x", op: "in", value: [null, 20, 5] }] };
    expect(tokens(el)).toEqual(["x: 5, 20, (Missing)"]);
    el.filter = {
      and: [
        { col: "x", op: "in", value: [5, 10, 20, null] },
        { col: "y", op: "contains", value: "  a " },
      ],
    };
    expect(tokens(el)).toEqual(["x: 5, 10 +2", "y contains “a”", "Clear all"]);
  });

  it("opens its filter's panel from a token, by it, and closes it back to it", async () => {
    const { el } = await mountTokens();
    el.filter = { and: [{ col: "y", op: "in", value: ["b"] }] };
    token(el, 0).click();
    const open = panel(el) as HTMLElement;
    expect(open.getAttribute("aria-label")).toBe("Filter y");
    expect(token(el, 0).getAttribute("aria-expanded")).toBe("true");
    expect(token(el, 0).getAttribute("aria-controls")).toBe(open.id);
    // (Not the column's button)
    const columnButton = header(el, "y").querySelector(".gt-i-filter-button") as HTMLButtonElement;
    expect(columnButton.getAttribute("aria-expanded")).toBe("false");
    expect(open.contains(document.activeElement)).toBe(true);

    press(document.activeElement, "Escape");
    expect(panel(el)).toBeNull();
    expect(token(el, 0).getAttribute("aria-expanded")).toBe("false");
    expect(document.activeElement).toBe(token(el, 0));

    // A second click closes it
    token(el, 0).click();
    token(el, 0).click();
    expect(panel(el)).toBeNull();
  });

  it("keeps a token while its panel is open, even with its filter cleared there", async () => {
    const { el } = await mountTokens();
    el.filter = { and: [{ col: "y", op: "in", value: ["b"] }] };
    token(el, 0).click();
    (panel(el)?.querySelector(".gt-i-filter-head button") as HTMLButtonElement).click();
    expect(el.filter).toBeNull();
    expect(tokens(el)).toEqual(["y: any"]);
    press(document.activeElement, "Escape");
    // (Its token gone, focus goes to the column's button)
    expect(row(el).hidden).toBe(true);
    expect(document.activeElement).toBe(header(el, "y").querySelector(".gt-i-filter-button"));
  });

  it("opens the panel of a column without a label, from its token", async () => {
    const { el } = await mountTokens({ filters: [{ column: "row", type: "text", values: null }] });
    el.filter = { and: [{ col: "row", op: "contains", value: "row_1" }] };
    expect(tokens(el)).toEqual(["row contains “row_1”"]);
    token(el, 0).click();
    expect((panel(el)?.querySelector("input") as HTMLInputElement).value).toBe("row_1");
    press(document.activeElement, "Escape");
    expect(document.activeElement).toBe(token(el, 0));
  });

  it("removes a filter from its token, with focus on the next token", async () => {
    const { el, events } = await mountTokens();
    el.filter = { and: [{ col: "x", op: "gte", value: 10 }, { col: "y", op: "in", value: ["a"] }] };
    remove(el, 0).click();
    expect(el.filter).toEqual({ and: [{ col: "y", op: "in", value: ["a"] }] });
    expect(events).toEqual([{ filter: { and: [{ col: "y", op: "in", value: ["a"] }] }, count: 3 }]);
    expect(tokens(el)).toEqual(["y: a"]);
    expect(document.activeElement).toBe(token(el, 0));
    // The last one goes to the info button
    press(token(el, 0), "Backspace");
    expect(el.filter).toBeNull();
    expect(document.activeElement).toBe(el.querySelector(".gt-i-bar [aria-controls^='gt-i-info']"));
  });

  it("goes from token to token with the arrow keys, and removes one with Delete", async () => {
    const { el } = await mountTokens({ pagination: { enabled: true } });
    el.filter = { and: [{ col: "x", op: "gte", value: 5 }, { col: "y", op: "in", value: ["a", "b"] }] };
    token(el, 0).focus();
    // (Not paging, as the arrow keys do elsewhere in the bar)
    expect(press(token(el, 0), "ArrowRight").defaultPrevented).toBe(true);
    expect(el.page).toBe(1);
    expect(document.activeElement).toBe(token(el, 1));
    press(document.activeElement, "ArrowRight");
    expect(document.activeElement).toBe(clearAll(el));
    press(document.activeElement, "Home");
    expect(document.activeElement).toBe(token(el, 0));
    press(document.activeElement, "End");
    press(document.activeElement, "ArrowLeft");
    expect(document.activeElement).toBe(token(el, 1));
    // (From a token's remove button too)
    press(remove(el, 1), "ArrowLeft");
    expect(document.activeElement).toBe(token(el, 0));
    press(document.activeElement, "Delete");
    expect(el.filter).toEqual({ and: [{ col: "y", op: "in", value: ["a", "b"] }] });
    expect(document.activeElement).toBe(token(el, 0));
    // (Delete on the Clear all button does nothing)
    expect(press(clearAll(el), "Delete").defaultPrevented).toBe(false);
  });

  it("clears every filter with Clear all, with focus on the info button", async () => {
    const { el, events } = await mountTokens();
    el.filter = { and: [{ col: "x", op: "gte", value: 10 }, { col: "y", op: "in", value: ["a"] }] };
    token(el, 1).click();
    clearAll(el).click();
    expect(el.filter).toBeNull();
    expect(events).toEqual([{ filter: null, count: 5 }]);
    expect(panel(el)).toBeNull();
    expect(row(el).hidden).toBe(true);
    expect(clearAll(el)).toBeNull();
    expect(document.activeElement).toBe(el.querySelector(".gt-i-bar [aria-controls^='gt-i-info']"));
  });

  it("shows the spec's view's filter", async () => {
    const el = await mountTable(GROUPED, {
      filters: [RANGE, FACET],
      controls: { bar: true },
      view: { filter: { and: [{ col: "x", op: "gte", value: 10 }] }, sort: [] },
    });
    expect(tokens(el)).toEqual(["x ≥ 10"]);
  });

  it("follows the filters as the reader changes them", async () => {
    const { el } = await mountTokens();
    (header(el, "y").querySelector(".gt-i-filter-button") as HTMLButtonElement).click();
    (panel(el)?.querySelectorAll("input")[2] as HTMLInputElement).click();
    expect(tokens(el)).toEqual(["y: c"]);
  });

  it("goes when the table does", async () => {
    const { el } = await mountTokens();
    el.filter = { and: [{ col: "x", op: "gte", value: 10 }] };
    const list = row(el);
    el.remove();
    expect(list.isConnected).toBe(false);
  });
});

describe("date filters", () => {
  // (On `x`, as dates: rows 0 and 4 on the 20th, 1 on the 5th, 2 on the 10th, and 3 missing)
  const DATES: FilterSpec = { column: "x", type: "date", values: ["2015-01-05", "2015-01-10", "2015-01-20"] };
  const TIMES: FilterSpec = {
    column: "x",
    type: "date",
    values: ["2015-01-05T00:00:00", "2015-01-10T09:30:00", "2015-01-20T12:00:05.123456"],
  };
  const filterButton = (el: GtTable) => header(el, "x").querySelector(".gt-i-filter-button") as HTMLButtonElement;
  const inputs = (el: GtTable) => {
    const panel = el.querySelector(`#${filterButton(el).getAttribute("aria-controls")}`) as HTMLElement;
    return Array.from(panel.querySelectorAll<HTMLInputElement>("input")) as [HTMLInputElement, HTMLInputElement];
  };
  const type = (input: HTMLInputElement, value: string) => {
    input.value = value;
    input.dispatchEvent(new Event("input", { bubbles: true }));
  };
  const enter = (input: HTMLInputElement) => {
    const event = new KeyboardEvent("keydown", { key: "Enter", bubbles: true, cancelable: true });
    input.dispatchEvent(event);
    return event;
  };
  const tokens = (el: GtTable) => Array.from(el.querySelectorAll(".gt-i-token-open"), (b) => b.textContent);

  const mountDates = (filter: FilterSpec, kind: "date" | "datetime") =>
    mountTable(GROUPED, {
      filters: [filter],
      columns: { x: { kind } as never },
      controls: { bar: true },
    });

  it("filters by dates from date fields, from the column's first to its last", async () => {
    const el = await mountDates(DATES, "date");
    filterButton(el).click();
    const [from, to] = inputs(el);
    expect([from.type, to.type]).toEqual(["date", "date"]);
    expect([from.getAttribute("aria-label"), to.getAttribute("aria-label")]).toEqual(["x, from", "x, to"]);
    expect([from.min, from.max]).toEqual(["2015-01-05", "2015-01-20"]);
    expect(from.step).toBe("");
    expect(from.closest(".gt-i-filter-range")?.classList.contains("gt-i-filter-range-stacked")).toBe(false);

    type(from, "2015-01-10");
    expect(enter(from).defaultPrevented).toBe(true);
    expect(el.filter).toEqual({ and: [{ col: "x", op: "gte", value: "2015-01-10" }] });
    expect(visible(el)).toEqual(["group:b", 0, 4, "summary:Total", "group:a", 2, "grand:Max"]);
    type(to, "2015-01-19");
    enter(to);
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
    type(from, "");
    enter(from);
    expect(el.filter).toEqual({ and: [{ col: "x", op: "lte", value: "2015-01-19" }] });

    // (And shows a filter set otherwise)
    el.filter = { and: [{ col: "x", op: "gte", value: "2015-01-06" }] };
    expect([from.value, to.value]).toEqual(["2015-01-06", ""]);
    expect(() => {
      el.filter = { and: [{ col: "x", op: "gte", value: "2015-01-06T00:00" }] };
    }).toThrow(/isn't a date \("YYYY-MM-DD"\), for "x"/);
  });

  it("filters by dates and times, a date as its midnight", async () => {
    const el = await mountDates(TIMES, "datetime");
    filterButton(el).click();
    const [from, to] = inputs(el);
    expect(from.type).toBe("datetime-local");
    // (One above the other, being wide)
    expect(from.closest(".gt-i-filter-range")?.classList.contains("gt-i-filter-range-stacked")).toBe(true);
    // (With seconds, as a time has them; and milliseconds at most)
    expect(from.step).toBe("1");
    expect([from.min, from.max]).toEqual(["2015-01-05T00:00:00", "2015-01-20T12:00:05.123"]);

    el.filter = { and: [{ col: "x", op: "gte", value: "2015-01-10" }] };
    expect(visible(el)).toEqual(["group:b", 0, 4, "summary:Total", "group:a", 2, "grand:Max"]);
    expect(from.value).toBe("2015-01-10T00:00");
    el.filter = { and: [{ col: "x", op: "gte", value: "2015-01-10T09:30:00.000001" }] };
    expect(visible(el)).toEqual(["group:b", 0, 4, "summary:Total", "grand:Max"]);
    // (A field that has its bound, as it shows it, leaves it be)
    from.dispatchEvent(new Event("input", { bubbles: true }));
    enter(from);
    expect(el.filter).toEqual({ and: [{ col: "x", op: "gte", value: "2015-01-10T09:30:00.000001" }] });
    type(from, "2015-01-10T09:29");
    enter(from);
    expect(el.filter).toEqual({ and: [{ col: "x", op: "gte", value: "2015-01-10T09:29" }] });
    expect(visible(el)).toEqual(["group:b", 0, 4, "summary:Total", "group:a", 2, "grand:Max"]);
  });

  it("has date fields for dates and times that are all at midnight", async () => {
    // (As pandas holds dates)
    const midnights = { ...DATES, values: DATES.values?.map((value) => `${value}T00:00:00`) ?? null };
    const el = await mountDates(midnights, "datetime");
    filterButton(el).click();
    const [from] = inputs(el);
    expect([from.type, from.min, from.step]).toEqual(["date", "2015-01-05", ""]);
    type(from, "2015-01-10");
    enter(from);
    expect(el.filter).toEqual({ and: [{ col: "x", op: "gte", value: "2015-01-10" }] });
    // (But still takes a time)
    el.filter = { and: [{ col: "x", op: "gte", value: "2015-01-10T09:30" }] };
    expect(from.value).toBe("2015-01-10");
    expect(visible(el)).toEqual(["group:b", 0, 4, "summary:Total", "grand:Max"]);
  });

  it("says what it keeps, with its dates as the table shows them, or as the language has them", async () => {
    const el = await mountDates(DATES, "date");
    el.setAttribute("lang", "de");
    el.filter = { and: [{ col: "x", op: "gte", value: "2015-01-10" }] };
    expect(tokens(el)).toEqual(["x ≥ 10"]);
    el.filter = { and: [{ col: "x", op: "gte", value: "2015-01-07" }, { col: "x", op: "lte", value: "2015-01-20" }] };
    expect(tokens(el)).toEqual(["x 07.01.2015 – 20"]);

    const times = await mountDates(TIMES, "datetime");
    times.setAttribute("lang", "de");
    times.filter = { and: [{ col: "x", op: "lte", value: "2015-01-10T09:30" }] };
    expect(tokens(times)).toEqual(["x ≤ 10"]);
    times.filter = { and: [{ col: "x", op: "lte", value: "2015-01-07T09:30" }] };
    expect(tokens(times)).toEqual(["x ≤ 07.01.2015, 09:30"]);
    times.filter = { and: [{ col: "x", op: "lte", value: "2015-01-07T09:30:15" }] };
    expect(tokens(times)).toEqual(["x ≤ 07.01.2015, 09:30:15"]);
  });

  it("suggests its ops, and its first and last dates, in the query box", async () => {
    const el = await mountDates(DATES, "date");
    (el.querySelector('[data-gti-bar="query"]') as HTMLButtonElement).click();
    const input = el.querySelector(".gt-i-query input") as HTMLInputElement;
    const options = () =>
      Array.from(el.querySelectorAll('.gt-i-query [role="listbox"] li'), (li) => (li.firstChild as Text).data);
    const press = (key: string) =>
      input.dispatchEvent(new KeyboardEvent("keydown", { key, bubbles: true, cancelable: true }));
    input.value = "x ";
    input.setSelectionRange(2, 2);
    input.dispatchEvent(new Event("input", { bubbles: true }));
    expect(options()).toEqual(['>= "…"', '<= "…"', "is null", "is not null"]);
    press("Enter");
    expect(input.value).toBe('x >= ""');
    expect(input.selectionStart).toBe(6);
    expect(options()).toEqual(["5", "20"]);
    press("ArrowDown");
    press("Enter");
    expect(input.value).toBe('x >= "2015-01-20" ');
    press("Escape");
    press("Enter");
    expect(el.filter).toEqual({ and: [{ col: "x", op: "gte", value: "2015-01-20" }] });

    // (While a date's typed, the dates it fits; but none once it's closed, so Enter applies it)
    (el.querySelector('[data-gti-bar="query"]') as HTMLButtonElement).click();
    input.value = 'x <= "2015-01';
    input.dispatchEvent(new Event("input", { bubbles: true }));
    expect(options()).toEqual(["5", "20"]);
    input.value = 'x <= "2015-01-1"';
    input.dispatchEvent(new Event("input", { bubbles: true }));
    expect(options()).toEqual([]);
    input.value = 'x <= "2015-01-10"';
    input.dispatchEvent(new Event("input", { bubbles: true }));
    press("Enter");
    expect(el.filter).toEqual({ and: [{ col: "x", op: "lte", value: "2015-01-10" }] });

    (el.querySelector('[data-gti-bar="query"]') as HTMLButtonElement).click();
    input.value = "x >= 5";
    input.dispatchEvent(new Event("input", { bubbles: true }));
    press("Enter");
    expect(el.querySelector(".gt-i-query-error")?.textContent).toBe(
      'X has a date filter: give a date in double quotes ("YYYY-MM-DD")',
    );
  });
});

describe("bool filters", () => {
  // (On `y`, as booleans: rows 0 and 4 true, shown as "b"; 1 and 3 false, as "a"; and 2 missing)
  const BOOL: FilterSpec = { column: "y", type: "bool", values: [false, true] };
  const filterButton = (el: GtTable) => header(el, "y").querySelector(".gt-i-filter-button") as HTMLButtonElement;
  const panel = (el: GtTable) => el.querySelector(`#${filterButton(el).getAttribute("aria-controls")}`) as HTMLElement;
  const radios = (el: GtTable) => Array.from(panel(el).querySelectorAll<HTMLInputElement>("input"));
  const options = (el: GtTable) =>
    Array.from(
      panel(el).querySelectorAll(".gt-i-filter-option"),
      (item) =>
        `${item.querySelector(".gt-i-filter-value")?.textContent} ${item.querySelector(".gt-i-filter-count")?.textContent}`,
    );
  const checked = (el: GtTable) => radios(el).map((radio) => radio.checked);
  const tokens = (el: GtTable) => Array.from(el.querySelectorAll(".gt-i-token-open"), (b) => b.textContent);
  const mountBool = (options: TableOptions = {}) =>
    mountTable(GROUPED, {
      filters: [BOOL],
      columns: { y: { kind: "boolean" } as never },
      queryRanks: { y: [1, 0, null, 0, 1] },
      ...options,
      controls: { bar: true, ...options.controls },
    });

  it("chooses any value, true, false or a missing one, from radio buttons", async () => {
    const el = await mountBool();
    const events: FilterEventDetail[] = [];
    el.addEventListener(FILTER_EVENT, (event) => events.push((event as CustomEvent<FilterEventDetail>).detail));
    filterButton(el).click();
    expect(panel(el).dataset.gtiFilter).toBe("bool");
    const group = panel(el).querySelector('[role="radiogroup"]') as HTMLElement;
    expect(group.getAttribute("aria-label")).toBe("y");
    // (As the table shows the values, true first, with the rows with each; and any, all of them)
    expect(options(el)).toEqual(["Any 5", "b 2", "a 2", "(Missing) 1"]);
    expect(radios(el).every((radio) => radio.type === "radio" && radio.name === panel(el).id)).toBe(true);
    expect(checked(el)).toEqual([true, false, false, false]);
    expect(document.activeElement).toBe(radios(el)[0]);

    radios(el)[1]?.click();
    expect(el.filter).toEqual({ and: [{ col: "y", op: "in", value: [true] }] });
    expect(visible(el)).toEqual(["group:b", 0, 4, "summary:Total", "grand:Max"]);
    expect(events).toEqual([{ filter: { and: [{ col: "y", op: "in", value: [true] }] }, count: 2 }]);
    expect(checked(el)).toEqual([false, true, false, false]);
    // (Its own values keep their counts)
    expect(options(el)).toEqual(["Any 5", "b 2", "a 2", "(Missing) 1"]);
    expect(tokens(el)).toEqual(["y: b"]);

    radios(el)[3]?.click();
    expect(el.filter).toEqual({ and: [{ col: "y", op: "in", value: [null] }] });
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
    expect(tokens(el)).toEqual(["y: (Missing)"]);
    radios(el)[0]?.click();
    expect(el.filter).toBeNull();
    expect(events[events.length - 1]).toEqual({ filter: null, count: 5 });
  });

  it("shows a filter set otherwise, focusing its value on opening", async () => {
    const el = await mountBool({ controls: { search: true } });
    el.filter = { and: [{ col: "y", op: "in", value: [false] }] };
    expect(visible(el)).toEqual(["group:b", 3, "summary:Total", "group:a", 1, "grand:Max"]);
    filterButton(el).click();
    expect(checked(el)).toEqual([false, false, true, false]);
    expect(document.activeElement).toBe(radios(el)[2]);
    // (Counted within the search)
    el.search = "row_1";
    expect(options(el)).toEqual(["Any 1", "b 1", "a 0", "(Missing) 0"]);
    el.filter = null;
    expect(checked(el)).toEqual([true, false, false, false]);
    expect(() => {
      el.filter = { and: [{ col: "y", op: "in", value: [true, false] }] };
    }).toThrow('the "in" clause on "y" (a bool filter) can have only one value');
  });

  it("has no missing value to choose in a column without one", async () => {
    const el = await mountBool({ queryRanks: { y: [1, 0, 1, 0, 1] } });
    filterButton(el).click();
    expect(options(el)).toEqual(["Any 5", "b 3", "a 2"]);
  });

  it("tabs out of the panel from the radio button checked", async () => {
    const el = await mountBool();
    el.filter = { and: [{ col: "y", op: "in", value: [true] }] };
    filterButton(el).click();
    const tab = (target: Element | undefined, shiftKey = false) => {
      const event = new KeyboardEvent("keydown", { key: "Tab", shiftKey, bubbles: true, cancelable: true });
      target?.dispatchEvent(event);
      return event;
    };
    // (The others aren't stops)
    expect(tab(radios(el)[1]).defaultPrevented).toBe(true);
    expect(panel(el).hidden).toBe(true);
  });

  it("suggests in, then its values, true first, in the query box", async () => {
    const el = await mountBool();
    (el.querySelector('[data-gti-bar="query"]') as HTMLButtonElement).click();
    const input = el.querySelector(".gt-i-query input") as HTMLInputElement;
    const suggestions = () =>
      Array.from(el.querySelectorAll('.gt-i-query [role="listbox"] li'), (li) => (li.firstChild as Text).data);
    const type = (text: string) => {
      input.value = text;
      input.setSelectionRange(text.length, text.length);
      input.dispatchEvent(new Event("input", { bubbles: true }));
    };
    const press = (key: string) =>
      input.dispatchEvent(new KeyboardEvent("keydown", { key, bubbles: true, cancelable: true }));
    type("y ");
    expect(suggestions()).toEqual(["in (…)", "is null", "is not null"]);
    type("y in (");
    expect(suggestions()).toEqual(["b", "a", "(Missing)"]);
    press("ArrowDown");
    press("Enter");
    expect(input.value).toBe("y in (false");
    // (One value only)
    type("y in (false, ");
    expect(suggestions()).toEqual([]);
    type("y in (false)");
    press("Enter");
    expect(el.filter).toEqual({ and: [{ col: "y", op: "in", value: [false] }] });

    (el.querySelector('[data-gti-bar="query"]') as HTMLButtonElement).click();
    type("y in (true, false)");
    press("Enter");
    expect(el.querySelector(".gt-i-query-error")?.textContent).toBe(
      "Y has a bool filter: give one value, true, false or null",
    );
  });
});

describe("the query box", () => {
  const RANGE: FilterSpec = { column: "x", type: "range", values: [5, 10, 20] };
  const FACET: FilterSpec = { column: "y", type: "facet", values: ["a", "b", "c"] };
  const toggle = (el: GtTable) => el.querySelector('[data-gti-bar="query"]') as HTMLButtonElement;
  const root = (el: GtTable) => el.querySelector(".gt-i-query") as HTMLElement;
  const input = (el: GtTable) => root(el).querySelector("input") as HTMLInputElement;
  const list = (el: GtTable) => root(el).querySelector('[role="listbox"]') as HTMLElement;
  const error = (el: GtTable) => root(el).querySelector(".gt-i-query-error") as HTMLElement;
  const options = (el: GtTable) =>
    Array.from(list(el).querySelectorAll("li"), (li) => (li.firstChild as Text).data);
  const press = (target: Element, key: string, init: KeyboardEventInit = {}) => {
    const event = new KeyboardEvent("keydown", { key, bubbles: true, cancelable: true, ...init });
    target.dispatchEvent(event);
    return event;
  };
  // Type text at the end, as a reader does
  const type = (el: GtTable, text: string) => {
    const field = input(el);
    field.value += text;
    field.setSelectionRange(field.value.length, field.value.length);
    field.dispatchEvent(new Event("input", { bubbles: true }));
  };
  const replace = (el: GtTable, text: string) => {
    input(el).value = "";
    type(el, text);
  };

  async function mountQuery(options: TableOptions = {}) {
    const el = await mountTable(GROUPED, {
      filters: [RANGE, FACET],
      ...options,
      controls: { bar: true, ...options.controls },
    });
    const events: FilterEventDetail[] = [];
    el.addEventListener(FILTER_EVENT, (event) => events.push((event as CustomEvent<FilterEventDetail>).detail));
    return { el, events };
  }

  it("opens from the bar's button with the filters as text, in the tokens' place", async () => {
    const { el } = await mountQuery();
    const button = toggle(el);
    expect(button.getAttribute("aria-label")).toBe("Edit the filters as text");
    expect(button.getAttribute("aria-expanded")).toBe("false");
    expect(button.getAttribute("aria-controls")).toBe(root(el).id);
    // (Before the info button)
    expect(button.nextElementSibling?.getAttribute("data-gti-bar")).toBe("info");
    expect(root(el).hidden).toBe(true);

    el.filter = { and: [{ col: "y", op: "in", value: ["b"] }, { col: "x", op: "gte", value: 10 }] };
    const tokens = el.querySelector(".gt-i-tokens") as HTMLElement;
    expect(tokens.hidden).toBe(false);
    button.click();
    expect(root(el).hidden).toBe(false);
    expect(button.getAttribute("aria-expanded")).toBe("true");
    expect(tokens.hidden).toBe(true);
    expect(input(el).value).toBe('x >= 10 and y in ("b")');
    expect(document.activeElement).toBe(input(el));
    expect(input(el).selectionStart).toBe(input(el).value.length);
    expect(list(el).hidden).toBe(true);

    // A second click closes it, with the text as it was
    button.click();
    expect(root(el).hidden).toBe(true);
    expect(tokens.hidden).toBe(false);
    expect(el.filter).toEqual({ and: [{ col: "x", op: "gte", value: 10 }, { col: "y", op: "in", value: ["b"] }] });
  });

  it("is a combobox, with an example in the first filter's column", async () => {
    const { el } = await mountQuery();
    const field = input(el);
    expect(field.getAttribute("role")).toBe("combobox");
    expect(field.getAttribute("aria-label")).toBe("Filters as text");
    expect(field.getAttribute("aria-autocomplete")).toBe("list");
    expect(field.getAttribute("aria-expanded")).toBe("false");
    expect(field.getAttribute("aria-controls")).toBe(list(el).id);
    expect(field.getAttribute("enterkeyhint")).toBe("go");
    expect(field.getAttribute("spellcheck")).toBe("false");
    expect(field.placeholder).toBe("x >= …");
    expect(list(el).getAttribute("aria-label")).toBe("Suggestions");
    expect(root(el).querySelector('[aria-label="Apply the filters"]')).not.toBeNull();
  });

  it("applies the text on Enter, as the reader's filter", async () => {
    const { el, events } = await mountQuery();
    toggle(el).click();
    replace(el, 'y in ("a", "c") and x <= 10');
    const event = press(input(el), "Enter");
    expect(event.defaultPrevented).toBe(true);
    expect(el.filter).toEqual({
      and: [
        { col: "x", op: "lte", value: 10 },
        { col: "y", op: "in", value: ["a", "c"] },
      ],
    });
    expect(events).toHaveLength(1);
    expect(live(el)).toBe("Showing 2 of 5 rows");
    expect(root(el).hidden).toBe(true);
    expect(document.activeElement).toBe(toggle(el));
    expect(Array.from(el.querySelectorAll(".gt-i-token-open"), (b) => b.textContent)).toEqual(["x ≤ 10", "y: a, c"]);

    // (And empty text, none)
    toggle(el).click();
    replace(el, " ");
    press(input(el), "Enter");
    expect(el.filter).toBeNull();
    expect(events).toHaveLength(2);
  });

  it("applies the text with its button, and leaves the filters with Cancel or Escape", async () => {
    const { el, events } = await mountQuery();
    toggle(el).click();
    replace(el, "x >= 10");
    (root(el).querySelector('[aria-label="Apply the filters"]') as HTMLButtonElement).click();
    expect(el.filter).toEqual({ and: [{ col: "x", op: "gte", value: 10 }] });

    toggle(el).click();
    replace(el, "x >= 20");
    (root(el).querySelector('[aria-label="Cancel"]') as HTMLButtonElement).click();
    expect(root(el).hidden).toBe(true);
    expect(document.activeElement).toBe(toggle(el));
    toggle(el).click();
    replace(el, "x >= 20");
    const event = press(input(el), "Escape");
    expect(event.defaultPrevented).toBe(true);
    expect(root(el).hidden).toBe(true);
    expect(el.filter).toEqual({ and: [{ col: "x", op: "gte", value: 10 }] });
    expect(events).toHaveLength(1);

    // (Opened again, it has the filters as they are)
    toggle(el).click();
    expect(input(el).value).toBe("x >= 10");
  });

  it("says what's wrong with text that isn't a query, and where, without applying it", async () => {
    const { el, events } = await mountQuery();
    toggle(el).click();
    replace(el, "x >= ten");
    press(input(el), "Enter");
    expect(error(el).hidden).toBe(false);
    expect(error(el).textContent).toBe("Expected a number, or a date in double quotes");
    expect(input(el).getAttribute("aria-invalid")).toBe("true");
    expect(input(el).getAttribute("aria-describedby")).toBe(error(el).id);
    expect(live(el)).toBe("Expected a number, or a date in double quotes");
    expect(input(el).selectionStart).toBe(5);
    expect(root(el).hidden).toBe(false);
    expect(el.filter).toBeNull();
    expect(events).toHaveLength(0);

    // (Until it changes)
    type(el, "x");
    expect(error(el).hidden).toBe(true);
    expect(input(el).hasAttribute("aria-invalid")).toBe(false);
    expect(input(el).hasAttribute("aria-describedby")).toBe(false);

    replace(el, "x >=");
    press(input(el), "Enter");
    expect(error(el).textContent).toBe("Expected a number, or a date in double quotes");
    replace(el, "x >= 1 y in (1)");
    press(input(el), "Enter");
    expect(error(el).textContent).toBe('Expected "and", "or" or the end of the query');
  });

  it("says why the table can't have a query's clause", async () => {
    const { el } = await mountQuery();
    toggle(el).click();
    const problem = (text: string) => {
      replace(el, text);
      press(input(el), "Enter");
      return error(el).hidden ? null : error(el).textContent;
    };
    expect(problem('row contains "1"')).toBe("Row isn't a column with a filter");
    expect(problem('x >= 5 and y contains "a"')).toBe("Y has a facet filter: use in");
    expect(input(el).selectionStart).toBe(11);
    expect(problem("x >= 5 and x >= 10")).toBe("X has more than one >= clause");
    expect(problem('y in ("a", "d")')).toBe('"d" isn\'t a value of y');
    expect(el.filter).toBeNull();
    expect(problem('y in ("a", null)')).toBeNull();
    expect(el.filter).toEqual({ and: [{ col: "y", op: "in", value: ["a", null] }] });
  });

  it("suggests columns, then their ops, then a facet's values, as text is typed", async () => {
    const { el } = await mountQuery();
    toggle(el).click();
    input(el).value = "";
    // (Not as it opens; with ArrowDown)
    expect(list(el).hidden).toBe(true);
    press(input(el), "ArrowDown");
    expect(list(el).hidden).toBe(false);
    expect(options(el)).toEqual(["x", "y"]);
    expect(input(el).getAttribute("aria-expanded")).toBe("true");
    const first = list(el).querySelector("li") as HTMLElement;
    expect(first.getAttribute("role")).toBe("option");
    expect(first.getAttribute("aria-selected")).toBe("true");
    expect(input(el).getAttribute("aria-activedescendant")).toBe(first.id);

    press(input(el), "ArrowDown");
    expect(input(el).getAttribute("aria-activedescendant")).toBe(list(el).children[1]?.id);
    press(input(el), "ArrowDown");
    expect(input(el).getAttribute("aria-activedescendant")).toBe(first.id);
    press(input(el), "ArrowUp");
    expect(press(input(el), "Enter").defaultPrevented).toBe(true);
    expect(input(el).value).toBe("y ");
    expect(options(el)).toEqual(["in (…)", "is null", "is not null"]);
    press(input(el), "Tab");
    expect(input(el).value).toBe("y in (");
    expect(options(el)).toEqual(["a", "b", "c"]);
    type(el, '"b');
    expect(options(el)).toEqual(["b"]);
    press(input(el), "Tab");
    expect(input(el).value).toBe('y in ("b"');
    // (Not a value already chosen)
    type(el, ", ");
    expect(options(el)).toEqual(["a", "c"]);
    type(el, '"c") ');
    expect(options(el)).toEqual(["and", "or"]);
    press(input(el), "Enter");
    expect(input(el).value).toBe('y in ("b", "c") and ');
    expect(options(el)).toEqual(["x", "y"]);
    type(el, "x ");
    expect(options(el)).toEqual([">= …", "<= …", "is null", "is not null"]);
    type(el, "<");
    expect(options(el)).toEqual(["<= …"]);
    press(input(el), "Enter");
    expect(input(el).value).toBe('y in ("b", "c") and x <= ');
    expect(list(el).hidden).toBe(true);
    expect(el.filter).toBeNull();
  });

  it("suggests `null` and `not null` after `is`, and `null` after `is not`", async () => {
    const { el } = await mountQuery();
    toggle(el).click();
    replace(el, "x is");
    expect(options(el)).toEqual(["is null", "is not null"]);
    replace(el, "x is ");
    expect(options(el)).toEqual(["null", "not null"]);
    type(el, "no");
    expect(options(el)).toEqual(["not null"]);
    press(input(el), "Tab");
    expect(input(el).value).toBe("x is not null ");
    expect(options(el)).toEqual(["and", "or"]);
    replace(el, "x is not ");
    expect(options(el)).toEqual(["null"]);
    press(input(el), "Enter");
    expect(input(el).value).toBe("x is not null ");
  });

  it("puts a column's label beside its name, and matches it", async () => {
    const { el } = await mountQuery({ yLabel: "Kind" });
    toggle(el).click();
    replace(el, "ki");
    expect(options(el)).toEqual(["y"]);
    expect(list(el).querySelector(".gt-i-query-detail")?.textContent).toBe("Kind");
  });

  it("doesn't suggest as text is deleted, or for none", async () => {
    const { el } = await mountQuery();
    toggle(el).click();
    replace(el, "x >= 1");
    input(el).value = "x ";
    input(el).dispatchEvent(new InputEvent("input", { inputType: "deleteContentBackward" }));
    expect(list(el).hidden).toBe(true);
    replace(el, "  ");
    expect(list(el).hidden).toBe(true);
    press(input(el), "ArrowDown");
    expect(options(el)).toEqual(["x", "y"]);
  });

  it("doesn't suggest what's typed already, so Enter applies it", async () => {
    const { el } = await mountQuery();
    toggle(el).click();
    replace(el, "x >= 10");
    expect(list(el).hidden).toBe(true);
    press(input(el), "Enter");
    expect(el.filter).toEqual({ and: [{ col: "x", op: "gte", value: 10 }] });
    toggle(el).click();
    replace(el, "x");
    expect(options(el)).toEqual([]);
  });

  it("closes the suggestions on Escape, as the caret moves, and as focus leaves", async () => {
    const { el } = await mountQuery();
    toggle(el).click();
    replace(el, "x ");
    expect(list(el).hidden).toBe(false);
    press(input(el), "Escape");
    expect(list(el).hidden).toBe(true);
    expect(input(el).getAttribute("aria-expanded")).toBe("false");
    expect(input(el).hasAttribute("aria-activedescendant")).toBe(false);
    expect(root(el).hidden).toBe(false);
    press(input(el), " ", { ctrlKey: true });
    expect(list(el).hidden).toBe(false);
    press(input(el), "ArrowLeft");
    expect(list(el).hidden).toBe(true);
    // (Enter, then, applies)
    press(input(el), "Enter");
    expect(error(el).textContent).toBe('Expected "contains", "matches", "in", ">=", "<=" or "is"');
  });

  it("takes a suggestion that's clicked, keeping focus", async () => {
    const { el } = await mountQuery();
    toggle(el).click();
    replace(el, "y in (");
    const item = list(el).children[2] as HTMLElement;
    const down = new Event("pointerdown", { bubbles: true, cancelable: true });
    item.dispatchEvent(down);
    expect(down.defaultPrevented).toBe(true);
    item.click();
    expect(input(el).value).toBe('y in ("c"');
  });

  it("closes as focus leaves it, unless its text changed", async () => {
    const { el } = await mountQuery({ controls: { search: true } });
    const elsewhere = el.querySelector('[data-gti-bar="info"]') as HTMLButtonElement;
    toggle(el).click();
    input(el).dispatchEvent(new FocusEvent("focusout", { bubbles: true, relatedTarget: elsewhere }));
    expect(root(el).hidden).toBe(true);
    toggle(el).click();
    type(el, "x");
    input(el).dispatchEvent(new FocusEvent("focusout", { bubbles: true, relatedTarget: elsewhere }));
    expect(root(el).hidden).toBe(false);
  });

  it("closes a filter's panel as it opens", async () => {
    const { el } = await mountQuery();
    (header(el, "y").querySelector(".gt-i-filter-button") as HTMLButtonElement).click();
    expect(el.querySelector(".gt-i-filter:not([hidden])")).not.toBeNull();
    toggle(el).click();
    expect(el.querySelector(".gt-i-filter:not([hidden])")).toBeNull();
  });

  it("is there only with filters and the bar", async () => {
    expect((await mountQuery({ filters: [] })).el.querySelector(".gt-i-query")).toBeNull();
    expect((await mountQuery({ controls: { bar: false } })).el.querySelector(".gt-i-query")).toBeNull();
  });

  it("goes when the table does", async () => {
    const { el } = await mountQuery();
    toggle(el).click();
    const box = root(el);
    el.remove();
    expect(box.isConnected).toBe(false);
  });

  it("applies or, not and parentheses", async () => {
    const { el, events } = await mountQuery();
    toggle(el).click();
    replace(el, 'y in ("a", "b") AND (x >= 20 Or not x >= 10)');
    press(input(el), "Enter");
    expect(error(el).hidden).toBe(true);
    const filter = {
      and: [
        { col: "y", op: "in", value: ["a", "b"] },
        { or: [{ col: "x", op: "gte", value: 20 }, { not: { col: "x", op: "gte", value: 10 } }] },
      ],
    };
    expect(el.filter).toEqual(filter);
    expect(events).toEqual([{ filter, count: 4 }]);
    expect(visible(el)).toEqual(["group:b", 3, 0, 4, "summary:Total", "group:a", 1, "grand:Max"]);
    // (Written back with only the parentheses needed)
    toggle(el).click();
    expect(input(el).value).toBe('y in ("a", "b") and (x >= 20 or not x >= 10)');
  });

  it("says what's wrong with a group", async () => {
    const { el } = await mountQuery({ filters: [RANGE, FACET, { column: "row", type: "text", values: null }] });
    toggle(el).click();
    const problem = (text: string) => {
      replace(el, text);
      press(input(el), "Enter");
      return error(el).hidden ? null : error(el).textContent;
    };
    expect(problem("(x >= 5 or y in (\"a\")")).toBe('Expected "and", "or" or ")"');
    expect(problem('x >= 5 or y in ("d")')).toBe('"d" isn\'t a value of y');
    expect(problem("(x >= 5 and x >= 10) or x <= 5")).toBe("X has more than one >= clause");
    expect(problem('not row contains " "')).toBe('Row needs text to look for, in an "or" or a "not"');
    expect(el.filter).toBeNull();
    // (The same clause in two parts is fine)
    expect(problem("x >= 5 and (x >= 5 or y in (\"a\"))")).toBeNull();
  });

  it("suggests or, not and a closing parenthesis", async () => {
    const { el } = await mountQuery();
    toggle(el).click();
    replace(el, "n");
    expect(options(el)).toEqual(["not"]);
    replace(el, "(not x >= 5 ");
    expect(options(el)).toEqual(["and", "or", ")"]);
    type(el, "o");
    expect(options(el)).toEqual(["or"]);
    press(input(el), "Enter");
    expect(input(el).value).toBe("(not x >= 5 or ");
    expect(options(el)).toEqual(["x", "y"]);
    replace(el, "x >= 5 ");
    expect(options(el)).toEqual(["and", "or"]);
  });

  it("suggests and applies matches, saying what's wrong with a pattern", async () => {
    const { el } = await mountQuery({ filters: [RANGE, { column: "y", type: "text", values: null }] });
    toggle(el).click();
    replace(el, "y ");
    expect(options(el)).toEqual(['contains "…"', "matches /…/", "is null", "is not null"]);
    type(el, "ma");
    expect(options(el)).toEqual(["matches /…/"]);
    press(input(el), "Enter");
    expect(input(el).value).toBe("y matches //");
    expect(input(el).selectionStart).toBe(11);
    // (Nothing's suggested in a pattern)
    type(el, "x");
    expect(list(el).hidden).toBe(true);

    replace(el, "y matches /^A/i or x >= 20");
    press(input(el), "Enter");
    expect(error(el).hidden).toBe(true);
    expect(el.filter).toEqual({
      and: [{ or: [{ col: "y", op: "matches", value: "(?i)^A" }, { col: "x", op: "gte", value: 20 }] }],
    });
    expect(visible(el)).toEqual(["group:b", 3, 0, 4, "summary:Total", "group:a", 1, "grand:Max"]);
    toggle(el).click();
    expect(input(el).value).toBe("y matches /^A/i or x >= 20");
    const problem = (text: string) => {
      replace(el, text);
      press(input(el), "Enter");
      return error(el).hidden ? null : error(el).textContent;
    };
    expect(problem("y matches /(/")).toBe('Expected ")"');
    expect(problem("y matches /a/g")).toBe('A pattern can have only the flag "i"');
    expect(problem("x matches /a/")).toBe("X has a range filter: use >= or <=");
    expect(problem("y matches /a/ and y matches /b/")).toBe("Y has more than one matches clause");
  });
});

describe("the query's groups", () => {
  const RANGE: FilterSpec = { column: "x", type: "range", values: [5, 10, 20] };
  const FACET: FilterSpec = { column: "y", type: "facet", values: ["a", "b", "c"] };
  const row = (el: GtTable) => el.querySelector(".gt-i-tokens") as HTMLElement;
  const tokens = (el: GtTable) =>
    Array.from(row(el).querySelectorAll(".gt-i-token-open, .gt-i-token-clear"), (b) => b.textContent);
  const token = (el: GtTable, i: number) => row(el).querySelectorAll<HTMLButtonElement>(".gt-i-token-open")[i] as HTMLButtonElement;
  const remove = (el: GtTable, i: number) =>
    row(el).querySelectorAll<HTMLButtonElement>(".gt-i-token-remove")[i] as HTMLButtonElement;
  const press = (target: Element | null | undefined, key: string) => {
    const event = new KeyboardEvent("keydown", { key, bubbles: true, cancelable: true });
    target?.dispatchEvent(event);
    return event;
  };
  const counts = (el: GtTable) =>
    Array.from(
      el.querySelectorAll(".gt-i-filter:not([hidden]) .gt-i-filter-option"),
      (item) => `${item.querySelector(".gt-i-filter-value")?.textContent} ${item.querySelector(".gt-i-filter-count")?.textContent}`,
    );
  const GROUP = { or: [{ col: "x", op: "gte" as const, value: 20 }, { col: "x", op: "lte" as const, value: 5 }] };
  const QUERY = { and: [{ col: "y", op: "in" as const, value: ["a", "b"] }, GROUP] };

  async function mountGroups(options: TableOptions = {}) {
    const el = await mountTable(GROUPED, {
      filters: [RANGE, FACET],
      ...options,
      controls: { bar: true, ...options.controls },
    });
    const events: FilterEventDetail[] = [];
    el.addEventListener(FILTER_EVENT, (event) => events.push((event as CustomEvent<FilterEventDetail>).detail));
    return { el, events };
  }

  it("filter the rows, as the `filter` property has them, after the filters' clauses", async () => {
    const { el } = await mountGroups();
    el.filter = { and: [GROUP, { col: "y", op: "in", value: ["a", "b"] }] };
    expect(el.filter).toEqual(QUERY);
    expect(visible(el)).toEqual(["group:b", 0, 4, "summary:Total", "group:a", 1, "grand:Max"]);
    // (A group's columns aren't marked as filtered, as their filters aren't on)
    expect(header(el, "x").hasAttribute("data-gti-filtered")).toBe(false);
    expect(header(el, "y").hasAttribute("data-gti-filtered")).toBe(true);
    el.filter = null;
    expect(el.filter).toBeNull();
    expect(visible(el)).toEqual(["group:b", 3, 0, 4, "summary:Total", "group:a", 1, 2, "grand:Max"]);
  });

  it("each have a token, of their text", async () => {
    const { el } = await mountGroups();
    el.filter = QUERY;
    expect(tokens(el)).toEqual(["y: a, b", "x >= 20 or x <= 5", "Clear all"]);
    const item = token(el, 1).parentElement as HTMLElement;
    expect(item.hasAttribute("data-gti-group")).toBe(true);
    expect(token(el, 1).title).toBe("x >= 20 or x <= 5 (edit as text)");
    expect(token(el, 1).hasAttribute("aria-expanded")).toBe(false);
    expect(remove(el, 1).getAttribute("aria-label")).toBe("Remove the filter x >= 20 or x <= 5");
    el.filter = { and: [{ not: { col: "y", op: "in", value: ["c"] } }] };
    expect(tokens(el)).toEqual(['not y in ("c")']);
  });

  it("include `is_null` clauses, whose tokens say the column is missing", async () => {
    const { el } = await mountGroups({ filters: [{ ...RANGE, missing: [3] }, FACET], yLabel: "Kind" });
    el.filter = { and: [{ col: "y", op: "is_null" }, { not: { col: "x", op: "is_null" } }] };
    expect(el.filter).toEqual({ and: [{ col: "y", op: "is_null" }, { not: { col: "x", op: "is_null" } }] });
    expect(visible(el)).toEqual(["grand:Max"]);
    el.filter = { and: [{ not: { col: "x", op: "is_null" } }, { col: "y", op: "in", value: ["a"] }] };
    // (Row 3's "a", but its x is missing)
    expect(visible(el)).toEqual(["group:b", 4, "summary:Total", "group:a", 1, "grand:Max"]);
    expect(tokens(el)).toEqual(["Kind: a", "x is not missing", "Clear all"]);
    expect(token(el, 1).parentElement?.hasAttribute("data-gti-group")).toBe(true);
    expect(token(el, 1).title).toBe("x is not null (edit as text)");
    expect(remove(el, 1).getAttribute("aria-label")).toBe("Remove the filter x is not missing");
    el.filter = { and: [{ col: "x", op: "is_null" }] };
    expect(visible(el)).toEqual(["group:b", 3, "summary:Total", "grand:Max"]);
    expect(tokens(el)).toEqual(["x is missing"]);
    el.filter = { and: [{ col: "y", op: "is_null" }] };
    expect(tokens(el)).toEqual(["Kind is missing"]);
  });

  it("include `matches` clauses, whose tokens are their text", async () => {
    const { el } = await mountGroups({ filters: [RANGE, { column: "y", type: "text", values: null }] });
    el.filter = { and: [{ col: "y", op: "matches", value: "(?i)^[A-B]$" }] };
    expect(el.filter).toEqual({ and: [{ col: "y", op: "matches", value: "(?i)^[A-B]$" }] });
    expect(visible(el)).toEqual(["group:b", 3, 0, 4, "summary:Total", "group:a", 1, "grand:Max"]);
    expect(tokens(el)).toEqual(["y matches /^[A-B]$/i"]);
    expect(token(el, 0).parentElement?.hasAttribute("data-gti-group")).toBe(true);
    expect(token(el, 0).title).toBe("y matches /^[A-B]$/i (edit as text)");
    el.filter = { and: [{ not: { col: "y", op: "matches", value: "a/b" } }] };
    expect(tokens(el)).toEqual(["not y matches /a\\/b/"]);
    expect(() => {
      el.filter = { and: [{ col: "x", op: "matches", value: "1" }] };
    }).toThrow(RangeError);
  });

  it("open the query box from a token, with its text selected", async () => {
    const { el } = await mountGroups();
    el.filter = QUERY;
    token(el, 1).click();
    const input = el.querySelector(".gt-i-query input") as HTMLInputElement;
    expect(row(el).hidden).toBe(true);
    expect(document.activeElement).toBe(input);
    expect(input.value).toBe('y in ("a", "b") and (x >= 20 or x <= 5)');
    expect(input.value.slice(input.selectionStart ?? 0, input.selectionEnd ?? 0)).toBe("x >= 20 or x <= 5");
  });

  it("are removed from their tokens, with focus on the token before", async () => {
    const { el, events } = await mountGroups();
    el.filter = { and: [...QUERY.and, { not: { col: "y", op: "in", value: ["a"] } }] };
    remove(el, 1).click();
    expect(el.filter).toEqual({ and: [QUERY.and[0], { not: { col: "y", op: "in", value: ["a"] } }] });
    expect(events).toEqual([{ filter: el.filter, count: 1 }]);
    expect(live(el)).toBe("Showing 1 of 5 rows");
    expect(document.activeElement).toBe(token(el, 1));
    press(token(el, 1), "Backspace");
    expect(el.filter).toEqual({ and: [QUERY.and[0]] });
    expect(document.activeElement).toBe(token(el, 0));
    // (And with Clear all, with the filters)
    el.filter = QUERY;
    (row(el).querySelector(".gt-i-token-clear") as HTMLButtonElement).click();
    expect(el.filter).toBeNull();
    expect(row(el).hidden).toBe(true);
  });

  it("are left as the filters change, and count in their facets' counts", async () => {
    const { el } = await mountGroups();
    el.filter = { and: [{ not: { col: "x", op: "gte", value: 10 } }] };
    (header(el, "y").querySelector(".gt-i-filter-button") as HTMLButtonElement).click();
    expect(counts(el)).toEqual(["a 2", "b 0", "c 0"]);
    (el.querySelectorAll<HTMLInputElement>(".gt-i-filter:not([hidden]) input")[0] as HTMLInputElement).click();
    expect(el.filter).toEqual({ and: [{ col: "y", op: "in", value: ["a"] }, { not: { col: "x", op: "gte", value: 10 } }] });
    expect(visible(el)).toEqual(["group:b", 3, "summary:Total", "group:a", 1, "grand:Max"]);
  });

  it("are in the info panel's filters, which clear them", async () => {
    const { el, events } = await mountGroups();
    const item = el.querySelector('[data-gti-info="filters"]') as HTMLElement;
    const clear = item.querySelector("button") as HTMLButtonElement;
    el.filter = { and: [{ not: { col: "x", op: "gte", value: 10 } }] };
    expect(item.firstElementChild?.textContent).toBe("Filtered by x");
    expect(clear.getAttribute("aria-disabled")).toBe("false");
    clear.click();
    expect(el.filter).toBeNull();
    expect(events).toEqual([{ filter: null, count: 5 }]);
    expect(item.firstElementChild?.textContent).toBe("Not filtered");
  });
});

describe("the spec's view", () => {
  const RANGE: FilterSpec = { column: "x", type: "range", values: [5, 10, 20] };
  const FACET: FilterSpec = { column: "y", type: "facet", values: ["a", "b", "c"] };
  const SORT = [{ column: "x", descending: true }];
  const FILTER = { and: [{ col: "x", op: "gte", value: 10 }] };

  async function mountView(view: object, options: TableOptions = {}) {
    const dispatch = vi.spyOn(GtTable.prototype, "dispatchEvent");
    const el = await mountTable(GROUPED, { filters: [RANGE, FACET], view, ...options, controls: { bar: true, ...options.controls } });
    const events = dispatch.mock.calls.map(([event]) => event.type).filter((type) => type.startsWith("gt-table-"));
    return { el, events };
  }

  it("sorts and filters the table as it's made ready, without events", async () => {
    const { el, events } = await mountView({ filter: FILTER, sort: SORT });
    expect(el.state).toBe("ready");
    expect(visible(el)).toEqual(["group:b", 0, 4, "summary:Total", "group:a", 2, "grand:Max"]);
    expect(el.sort).toEqual(SORT);
    expect(el.filter).toEqual(FILTER);
    expect(events).toEqual([]);
    expect(header(el, "x").hasAttribute("data-gti-filtered")).toBe(true);
    expect(header(el, "x").getAttribute("aria-sort")).toBe("descending");
  });

  it("shows the filter in its panel", async () => {
    const { el } = await mountView({ filter: { and: [...FILTER.and, { col: "y", op: "in", value: ["b"] }] }, sort: [] });
    (header(el, "x").querySelector(".gt-i-filter-button") as HTMLButtonElement).click();
    expect(Array.from(el.querySelectorAll<HTMLInputElement>(".gt-i-filter input"), (input) => input.value)).toEqual(["10", ""]);
    expect(visible(el)).toEqual(["group:b", 0, "summary:Total", "grand:Max"]);
  });

  it("sorts in the view's order without sort buttons", async () => {
    const { el } = await mountView({ filter: null, sort: SORT }, { controls: { sorting: false } });
    expect(el.querySelector(".gt-i-sort")).toBeNull();
    expect(visible(el)).toEqual(["group:b", 0, 4, 3, "summary:Total", "group:a", 2, 1, "grand:Max"]);
  });

  it("changes nothing with an empty view", async () => {
    const { el } = await mountView({ filter: null, sort: [] });
    expect(visible(el)).toEqual(shown(await mountTable(GROUPED)));
  });

  it.each([
    ["sort", { filter: FILTER, sort: [{ column: "w", descending: false }] }, ["group:b", 0, 4, "summary:Total", "group:a", 2, "grand:Max"]],
    ["filter", { filter: { and: [{ col: "y", op: "gte", value: 1 }] }, sort: SORT }, ["group:b", 0, 4, 3, "summary:Total", "group:a", 2, 1, "grand:Max"]],
  ])("leaves out a %s it can't have, with a warning", async (part, view, rows) => {
    const warn = vi.spyOn(console, "warn").mockImplementation(() => {});
    const { el } = await mountView(view);
    expect(el.state).toBe("ready");
    expect(visible(el)).toEqual(rows);
    expect(warn).toHaveBeenCalledOnce();
    expect(warn.mock.calls[0]?.[0]).toMatch(new RegExp(`the view's ${part} is left out`));
  });

  it("leaves a table whose stub has merged cells as it is", async () => {
    const warn = vi.spyOn(console, "warn").mockImplementation(() => {});
    const { html, spec } = gtTable([0, 1, 2, 3, 4], { filters: [RANGE], view: { filter: FILTER, sort: SORT } });
    const merged = html.replace(
      `<th class="gt_row gt_left gt_stub">row_1</th>`,
      `<th class="gt_row gt_left gt_stub" rowspan="2">row_1</th>`,
    );
    const el = await mount(`<gt-table>${merged}${specScript(spec)}</gt-table>`);
    expect(el.state).toBe("ready");
    expect(visible(el)).toEqual([0, 1, 2, 3, 4]);
    expect(el.sort).toEqual([]);
    expect(warn).not.toHaveBeenCalled();
  });
});

describe("the view kept", () => {
  const RANGE: FilterSpec = { column: "x", type: "range", values: [5, 10, 20] };
  const FILTER: FilterQuery = { and: [{ col: "x", op: "gte", value: 10 }] };
  const AUTHOR_SORT = [{ column: "y", descending: true }];
  const STORED = "gti:/page#t1";
  const at = (url: string) => history.replaceState(null, "", url);
  const item = (el: GtTable) => el.querySelector('[data-gti-info="view"]') as HTMLElement | null;
  const reset = (el: GtTable) => item(el)?.querySelector("button") as HTMLButtonElement;
  const openInfo = (el: GtTable) => (el.querySelector('.gt-i-bar [data-gti-bar="info"]') as HTMLButtonElement).click();

  // Table `t1`, kept in the URL (unless set otherwise), with a search, a filter on `x`, pages of 2
  // rows (or 4), and the author's view sorted by `y`, descending
  async function mountKept(viewState: object = {}, options: TableOptions = {}) {
    const dispatch = vi.spyOn(GtTable.prototype, "dispatchEvent");
    const el = await mountTable(GROUPED, {
      filters: [RANGE],
      view: { filter: null, sort: AUTHOR_SORT },
      viewState: { url: true, storage: false, key: "t1", undo: false, ...viewState },
      ...options,
      controls: { search: true, bar: true, ...options.controls },
      pagination: { enabled: true, size_select: true, ...options.pagination },
    });
    const events = dispatch.mock.calls.map(([event]) => event.type).filter((type) => type.startsWith("gt-table-"));
    return { el, events };
  }

  beforeEach(() => {
    at("/page?other=a%20b");
    localStorage.clear();
  });
  afterEach(() => {
    at("/");
    localStorage.clear();
  });

  it("keeps the view in the URL as it changes, with the page's other parameters", async () => {
    const { el } = await mountKept();
    const length = history.length;
    expect(location.search).toBe("?other=a%20b");
    click(el, "x");
    expect(el.sort).toEqual([{ column: "x", descending: false }]);
    expect(location.search).toBe("?other=a%20b&t1.sort=x");
    // (However it changes)
    el.page = 2;
    el.filter = FILTER;
    expect(location.search).toBe("?other=a%20b&t1.filter=x+%3E%3D+10&t1.sort=x");
    el.search = "row";
    el.pageSize = 4;
    expect(location.search).toBe("?other=a%20b&t1.filter=x+%3E%3D+10&t1.sort=x&t1.search=row&t1.size=4");
    // (The author's view has none)
    el.filter = null;
    el.sort = AUTHOR_SORT;
    el.search = "";
    el.pageSize = 2;
    expect(location.search).toBe("?other=a%20b");
    expect(location.pathname).toBe("/page");
    // (Replacing the page's place in the history, not adding to it)
    expect(history.length).toBe(length);
  });

  it("shows the view in the URL as it's made ready, without events", async () => {
    at("/page?t1.filter=x+%3E%3D+10&t1.sort=x&t1.page=2&other=1");
    const { el, events } = await mountKept();
    expect(el.state).toBe("ready");
    expect(el.filter).toEqual(FILTER);
    expect(el.sort).toEqual([{ column: "x", descending: false }]);
    expect(el.page).toBe(2);
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
    expect(header(el, "x").hasAttribute("data-gti-filtered")).toBe(true);
    expect(events).toEqual([]);
    // (As it was)
    expect(location.search).toBe("?t1.filter=x+%3E%3D+10&t1.sort=x&t1.page=2&other=1");

    at("/page?t1.search=row&t1.size=4&t1.sort=");
    const { el: other } = await mountKept();
    expect([other.search, other.pageSize, other.sort]).toEqual(["row", 4, []]);
    expect((other.querySelector(".gt-i-search") as HTMLInputElement).value).toBe("row");
    expect(other.querySelector(".gt-i-bar")?.hasAttribute("data-gti-searching")).toBe(true);
  });

  it("shows the view in the browser's storage, unless the URL has one", async () => {
    localStorage.setItem(STORED, "sort=x&page=2");
    const { el } = await mountKept({ storage: true });
    expect([el.sort, el.page]).toEqual([[{ column: "x", descending: false }], 2]);
    // (Which the URL has too, now)
    expect(location.search).toBe("?other=a%20b&t1.sort=x&t1.page=2");
    el.page = 1;
    expect(localStorage.getItem(STORED)).toBe("sort=x");

    at("/page?t1.sort=-x");
    const { el: shared } = await mountKept({ storage: true });
    expect([shared.sort, shared.page]).toEqual([[{ column: "x", descending: true }], 1]);
    expect(localStorage.getItem(STORED)).toBe("sort=-x");
  });

  it("keeps the view in storage alone, with `url` off", async () => {
    at("/page?t1.page=2");
    localStorage.setItem(STORED, "search=row");
    const { el } = await mountKept({ url: false, storage: true });
    expect([el.page, el.search]).toEqual([1, "row"]);
    click(el, "x");
    expect(localStorage.getItem(STORED)).toBe("sort=x&search=row");
    expect(location.search).toBe("?t1.page=2");
    el.resetView();
    expect(localStorage.getItem(STORED)).toBeNull();
  });

  it("leaves out a part of the view the table can't have, with a warning", async () => {
    const warn = vi.spyOn(console, "warn").mockImplementation(() => {});
    at("/page?t1.filter=y+%3E%3D+1&t1.sort=w&t1.page=2&t1.size=3");
    const { el } = await mountKept();
    expect(el.state).toBe("ready");
    expect([el.filter, el.sort, el.page, el.pageSize]).toEqual([null, AUTHOR_SORT, 2, 2]);
    expect(warn.mock.calls.map(([message]) => message)).toEqual([
      `<gt-table>: the saved view's size is left out ("3" isn't a page size the table has).`,
      `<gt-table>: the saved view's sort is left out ("w" isn't a sortable column).`,
      expect.stringMatching(/^<gt-table>: the saved view's filter is left out \(.+\)\.$/),
    ]);
    // (And from the URL)
    expect(location.search).toBe("?t1.page=2");
  });

  it("resets the view from the info panel", async () => {
    at("/page?other=1&t1.sort=x&t1.page=2");
    const { el } = await mountKept({ storage: true });
    const fired: ViewEventDetail[] = [];
    el.addEventListener(VIEW_EVENT, (event) => fired.push((event as CustomEvent<ViewEventDetail>).detail));
    openInfo(el);
    expect(item(el)?.textContent).toBe("View kept in the link and this browserReset");
    expect(reset(el).getAttribute("aria-label")).toBe("Reset the view");
    expect(reset(el).getAttribute("aria-disabled")).toBe("false");
    expect(localStorage.getItem(STORED)).toBe("sort=x&page=2");

    reset(el).click();
    expect([el.sort, el.page]).toEqual([AUTHOR_SORT, 1]);
    expect(location.search).toBe("?other=1");
    expect(localStorage.getItem(STORED)).toBeNull();
    expect(reset(el).getAttribute("aria-disabled")).toBe("true");
    expect(el.querySelector(".gt-i-live")?.textContent).toMatch(/^The view is reset: /);
    expect(fired).toEqual([{ filter: null, sort: AUTHOR_SORT, search: "", page: 1, pageSize: 2, hidden: [], order: [] }]);
    // (Disabled, it does nothing)
    reset(el).click();
    expect(fired).toHaveLength(1);
  });

  it("says where the view is kept", async () => {
    for (const [state, text] of [
      [{}, "View kept in the link"],
      [{ url: false, storage: true }, "View kept in this browser"],
    ] as const) {
      const { el } = await mountKept(state);
      openInfo(el);
      expect(item(el)?.firstElementChild?.textContent).toBe(text);
    }
    // (Not kept, it has no reset)
    const { el } = await mountKept({ url: false, storage: false, key: null });
    openInfo(el);
    expect(item(el)).toBeNull();
  });

  it("fires an event as the reader changes the view, not when properties are set", async () => {
    // (Kept or not)
    const el = await mountTable(GROUPED, {
      filters: [RANGE],
      controls: { search: true, bar: true },
      pagination: { enabled: true },
    });
    const fired: ViewEventDetail[] = [];
    el.addEventListener(VIEW_EVENT, (event) => fired.push((event as CustomEvent<ViewEventDetail>).detail));
    click(el, "x");
    (el.querySelector('.gt-i-bar [data-gti-bar="next"]') as HTMLButtonElement).click();
    expect(fired).toEqual([
      { filter: null, sort: [{ column: "x", descending: false }], search: "", page: 1, pageSize: 2, hidden: [], order: [] },
      { filter: null, sort: [{ column: "x", descending: false }], search: "", page: 2, pageSize: 2, hidden: [], order: [] },
    ]);
    el.sort = [];
    el.filter = FILTER;
    el.page = 2;
    el.resetView();
    expect([el.filter, el.sort, el.page]).toEqual([null, [], 1]);
    expect(fired).toHaveLength(2);
    expect(location.search).toBe("?other=a%20b");
  });

  it("keeps the views of two tables apart", async () => {
    const one = gtTable(GROUPED, { viewState: { url: true, storage: true, key: "t1", undo: false } });
    const two = gtTable(GROUPED, { viewState: { url: true, storage: true, key: "t2", undo: false } });
    at("/page?t2.sort=-x");
    await mount(`<gt-table>${one.html}${specScript(one.spec)}</gt-table><gt-table>${two.html}${specScript(two.spec)}</gt-table>`);
    const [first, second] = Array.from(document.querySelectorAll(TAG_NAME)) as GtTable[];
    expect([first?.sort, second?.sort]).toEqual([[], [{ column: "x", descending: true }]]);
    click(first as GtTable, "x");
    expect(location.search).toBe("?t2.sort=-x&t1.sort=x");
    click(second as GtTable, "y");
    expect(location.search).toBe("?t1.sort=x&t2.sort=y");
    expect([localStorage.getItem("gti:/page#t1"), localStorage.getItem("gti:/page#t2")]).toEqual(["sort=x", "sort=y"]);
  });

  it("keeps nothing of a table whose stub has merged cells", async () => {
    at("/page?t1.sort=x");
    const { html, spec } = gtTable([0, 1, 2, 3, 4], { viewState: { url: true, storage: false, key: "t1", undo: false } });
    const merged = html.replace(
      `<th class="gt_row gt_left gt_stub">row_1</th>`,
      `<th class="gt_row gt_left gt_stub" rowspan="2">row_1</th>`,
    );
    const el = await mount(`<gt-table>${merged}${specScript(spec)}</gt-table>`);
    expect(el.sort).toEqual([]);
    el.resetView();
    expect(location.search).toBe("?t1.sort=x");
  });

  it("goes on without the URL or storage, where the page can't have them", async () => {
    vi.spyOn(history, "replaceState").mockImplementation(() => {
      throw new DOMException("denied", "SecurityError");
    });
    vi.spyOn(Storage.prototype, "getItem").mockImplementation(() => {
      throw new DOMException("denied", "SecurityError");
    });
    vi.spyOn(Storage.prototype, "setItem").mockImplementation(() => {
      throw new DOMException("denied", "SecurityError");
    });
    const { el } = await mountKept({ storage: true });
    click(el, "x");
    expect(el.sort).toEqual([{ column: "x", descending: false }]);
    expect(el.state).toBe("ready");
    vi.restoreAllMocks();
  });
});

describe("undo", () => {
  const RANGE: FilterSpec = { column: "x", type: "range", values: [5, 10, 20] };
  const FACET: FilterSpec = { column: "y", type: "facet", values: ["a", "b", "c"] };
  const X_UP = [{ column: "x", descending: false }];
  // (How long after a change another is a change of its own, rather than part of the same)
  const STEP_MS = 1000;
  const barButton = (el: GtTable, name: string) =>
    el.querySelector(`.gt-i-bar [data-gti-bar="${name}"]`) as HTMLButtonElement | null;
  const disabled = (el: GtTable) => ["undo", "redo"].map((name) => barButton(el, name)?.getAttribute("aria-disabled"));
  const facet = (el: GtTable, i: number) => {
    const filter = header(el, "y").querySelector(".gt-i-filter-button") as HTMLButtonElement;
    if (filter.getAttribute("aria-expanded") !== "true") {
      filter.click();
    }
    const panel = el.querySelector(`#${filter.getAttribute("aria-controls")}`) as HTMLElement;
    panel.querySelectorAll("input")[i]?.click();
  };
  const typeSearch = (el: GtTable, value: string) => {
    const open = barButton(el, "search") as HTMLButtonElement;
    if (!open.hidden) {
      open.click();
    }
    const input = searchBox(el) as HTMLInputElement;
    input.value = value;
    input.dispatchEvent(new Event("input", { bubbles: true }));
    vi.advanceTimersByTime(150);
  };
  const press = (target: Element, key: string, init: KeyboardEventInit = {}) => {
    const event = new KeyboardEvent("keydown", { key, bubbles: true, cancelable: true, ...init });
    target.dispatchEvent(event);
    return event;
  };

  // A range on `x`, a facet on `y`, a search, and pages of 2 rows (or 4), whose changes can be undone
  async function mountUndo(options: TableOptions = {}) {
    vi.useRealTimers();
    const el = await mountTable(GROUPED, {
      filters: [RANGE, FACET],
      ...options,
      viewState: { url: false, storage: false, key: null, undo: true, ...options.viewState },
      controls: { search: true, bar: true, ...options.controls },
      pagination: { enabled: true, size_select: true, ...options.pagination },
    });
    const fired: ViewEventDetail[] = [];
    el.addEventListener(VIEW_EVENT, (event) => fired.push((event as CustomEvent<ViewEventDetail>).detail));
    // (Once ready, as mounting waits for it)
    vi.useFakeTimers();
    return { el, views: () => fired };
  }

  afterEach(() => {
    vi.useRealTimers();
    history.replaceState(null, "", "/");
    localStorage.clear();
  });

  it("puts buttons that undo and redo in the bar, before the info button, disabled until they can", async () => {
    vi.spyOn(navigator, "platform", "get").mockReturnValue("Win32");
    const { el } = await mountUndo();
    const [undo, redo] = [barButton(el, "undo"), barButton(el, "redo")] as HTMLButtonElement[];
    expect(undo?.nextElementSibling).toBe(redo);
    expect(redo?.nextElementSibling).toBe(barButton(el, "info"));
    expect([undo?.getAttribute("aria-label"), undo?.title, undo?.getAttribute("aria-keyshortcuts")]).toEqual([
      "Undo",
      "Undo (Ctrl+Z)",
      "Control+Z Meta+Z",
    ]);
    expect([redo?.getAttribute("aria-label"), redo?.title]).toEqual(["Redo", "Redo (Ctrl+Y)"]);
    expect(disabled(el)).toEqual(["true", "true"]);
    // (Disabled, they do nothing)
    undo?.click();
    expect(live(el)).toBe("");
    const keys = Array.from(el.querySelectorAll(".gt-i-info-keys > div"), (entry) => entry.textContent);
    expect(keys).toContain("Ctrl ZUndo a change to the view");
    expect(keys).toContain("Ctrl YRedo it");

    // (With a Mac's keys)
    vi.spyOn(navigator, "platform", "get").mockReturnValue("MacIntel");
    const { el: mac } = await mountUndo();
    expect([barButton(mac, "undo")?.title, barButton(mac, "redo")?.title]).toEqual(["Undo (⌘Z)", "Redo (⇧⌘Z)"]);
    expect(Array.from(mac.querySelectorAll(".gt-i-info-keys dt"), (dt) => dt.textContent)).toContain("⇧ ⌘ Z");
  });

  it("has a bar for them alone, and no buttons without undo", async () => {
    const { el } = await mountUndo({ filters: [], controls: { search: false }, pagination: { enabled: false } });
    expect((el.querySelector(".gt-i-bar") as HTMLElement).hidden).toBe(false);
    expect(barButton(el, "undo")).not.toBeNull();
    const { el: without } = await mountUndo({ viewState: { undo: false } });
    expect(barButton(without, "undo")).toBeNull();
    expect(without.querySelector(".gt-i-info-keys")?.textContent ?? "").not.toContain("Undo");
    click(without, "x");
    expect(without.undo()).toBe(false);
    expect(without.sort).toEqual(X_UP);
  });

  it("undoes the removal of a query's group", async () => {
    const { el } = await mountUndo();
    const query: FilterQuery = { and: [{ col: "y", op: "in", value: ["a"] }, { not: { col: "x", op: "gte", value: 10 } }] };
    el.filter = query;
    (el.querySelectorAll<HTMLButtonElement>(".gt-i-token-remove")[1] as HTMLButtonElement).click();
    expect(el.filter).toEqual({ and: [{ col: "y", op: "in", value: ["a"] }] });
    barButton(el, "undo")?.click();
    expect(el.filter).toEqual(query);
    expect(Array.from(el.querySelectorAll(".gt-i-token-open"), (b) => b.textContent)).toEqual(["y: a", "not x >= 10"]);
  });

  it("undoes and redoes the reader's changes, one by one", async () => {
    const { el, views } = await mountUndo();
    click(el, "x");
    vi.advanceTimersByTime(STEP_MS);
    facet(el, 0);
    expect([el.filter, el.sort]).toEqual([{ and: [{ col: "y", op: "in", value: ["a"] }] }, X_UP]);
    expect(disabled(el)).toEqual(["false", "true"]);

    barButton(el, "undo")?.click();
    expect([el.filter, el.sort]).toEqual([null, X_UP]);
    expect(live(el)).toBe("Undone: 1–2 of 5 rows");
    expect(disabled(el)).toEqual(["false", "false"]);
    barButton(el, "undo")?.click();
    expect([el.filter, el.sort]).toEqual([null, []]);
    expect(disabled(el)).toEqual(["true", "false"]);
    // (With nothing to undo)
    barButton(el, "undo")?.click();
    expect(views()).toHaveLength(4);

    barButton(el, "redo")?.click();
    expect(live(el)).toBe("Redone: 1–2 of 5 rows");
    barButton(el, "redo")?.click();
    expect([el.filter, el.sort]).toEqual([{ and: [{ col: "y", op: "in", value: ["a"] }] }, X_UP]);
    expect(disabled(el)).toEqual(["false", "true"]);
    // (Shown in the filter's panel, too)
    expect(header(el, "y").hasAttribute("data-gti-filtered")).toBe(true);
    expect(views()).toEqual([
      { filter: null, sort: X_UP, search: "", page: 1, pageSize: 2, hidden: [], order: [] },
      { filter: { and: [{ col: "y", op: "in", value: ["a"] }] }, sort: X_UP, search: "", page: 1, pageSize: 2, hidden: [], order: [] },
      { filter: null, sort: X_UP, search: "", page: 1, pageSize: 2, hidden: [], order: [] },
      { filter: null, sort: [], search: "", page: 1, pageSize: 2, hidden: [], order: [] },
      { filter: null, sort: X_UP, search: "", page: 1, pageSize: 2, hidden: [], order: [] },
      { filter: { and: [{ col: "y", op: "in", value: ["a"] }] }, sort: X_UP, search: "", page: 1, pageSize: 2, hidden: [], order: [] },
    ]);

    // A new change, after one is undone, can't be redone
    el.undo();
    click(el, "y");
    expect(disabled(el)).toEqual(["false", "true"]);
    expect(el.redo()).toBe(false);
    expect(el.undo()).toBe(true);
    expect([el.filter, el.sort]).toEqual([null, X_UP]);
  });

  it("counts a run of changes to the search, or to one filter, as one change", async () => {
    const { el } = await mountUndo();
    // (A run that ends where it began is none)
    typeSearch(el, "r");
    typeSearch(el, "");
    expect(disabled(el)).toEqual(["true", "true"]);
    typeSearch(el, "ro");
    typeSearch(el, "row");
    typeSearch(el, "row_");
    vi.advanceTimersByTime(STEP_MS);
    facet(el, 0);
    facet(el, 1);
    vi.advanceTimersByTime(STEP_MS);
    facet(el, 2);
    expect(el.filter).toEqual({ and: [{ col: "y", op: "in", value: ["a", "b", "c"] }] });

    el.undo();
    expect(el.filter).toEqual({ and: [{ col: "y", op: "in", value: ["a", "b"] }] });
    el.undo();
    expect(el.filter).toBeNull();
    expect(el.search).toBe("row_");
    el.undo();
    expect(el.search).toBe("");
    expect(searchBox(el)?.value).toBe("");
    expect(el.undo()).toBe(false);

    // (But not sorting, or another filter)
    el.redo();
    click(el, "x");
    click(el, "x");
    facet(el, 0);
    el.filter = el.filter;
    expect(el.undo()).toBe(true);
    expect(el.sort).toEqual([{ column: "x", descending: true }]);
    el.undo();
    expect(el.sort).toEqual(X_UP);
  });

  it("undoes a change with the page it was on, but not going to another page", async () => {
    const { el } = await mountUndo();
    barButton(el, "next")?.click();
    expect(el.page).toBe(2);
    expect(disabled(el)).toEqual(["true", "true"]);
    click(el, "x");
    expect(el.page).toBe(1);
    barButton(el, "next")?.click();
    barButton(el, "next")?.click();
    el.undo();
    expect([el.sort, el.page]).toEqual([[], 2]);
    el.redo();
    expect([el.sort, el.page]).toEqual([X_UP, 3]);

    // (And the page size)
    const select = el.querySelector('[data-gti-info="size"] select') as HTMLSelectElement;
    barButton(el, "info")?.click();
    select.value = "4";
    select.dispatchEvent(new Event("change"));
    expect(el.pageSize).toBe(4);
    el.undo();
    expect([el.pageSize, el.page]).toEqual([2, 3]);
  });

  it("undoes a reset, and the info panel's resets", async () => {
    const { el } = await mountUndo({ viewState: { url: false, storage: true, key: "t1" } });
    click(el, "x");
    vi.advanceTimersByTime(STEP_MS);
    facet(el, 2);
    barButton(el, "info")?.click();
    (el.querySelector('[data-gti-info="view"] button') as HTMLButtonElement).click();
    expect([el.filter, el.sort]).toEqual([null, []]);
    expect(localStorage.getItem("gti:/#t1")).toBeNull();
    el.undo();
    expect([el.filter, el.sort]).toEqual([{ and: [{ col: "y", op: "in", value: ["c"] }] }, X_UP]);
    expect(localStorage.getItem("gti:/#t1")).toMatch(/^filter=.+&sort=x$/);

    (el.querySelector('[data-gti-info="sort"] button') as HTMLButtonElement).click();
    (el.querySelector('[data-gti-info="filters"] button') as HTMLButtonElement).click();
    expect([el.filter, el.sort]).toEqual([null, []]);
    el.undo();
    el.undo();
    expect([el.filter, el.sort]).toEqual([{ and: [{ col: "y", op: "in", value: ["c"] }] }, X_UP]);
  });

  it("answers to Ctrl+Z and Ctrl+Y (or Ctrl+Shift+Z, or ⌘), but not in what's for typing", async () => {
    const { el, views } = await mountUndo();
    click(el, "x");
    const target = button(el, "y");
    expect(press(target, "z", { ctrlKey: true }).defaultPrevented).toBe(true);
    expect(el.sort).toEqual([]);
    expect(press(target, "y", { ctrlKey: true }).defaultPrevented).toBe(true);
    expect(el.sort).toEqual(X_UP);
    press(target, "z", { metaKey: true });
    expect(el.sort).toEqual([]);
    press(target, "Z", { ctrlKey: true, shiftKey: true });
    expect(el.sort).toEqual(X_UP);
    press(target, "z", { metaKey: true });
    press(target, "z", { metaKey: true, shiftKey: true });
    expect(el.sort).toEqual(X_UP);
    expect(views()).toHaveLength(7);
    expect(live(el)).toBe("Redone: 1–2 of 5 rows");

    // (Not other keys, nor where the text has its own undo)
    for (const [key, init] of [
      ["z", {}],
      ["z", { ctrlKey: true, altKey: true }],
      ["y", { metaKey: true }],
      ["y", { ctrlKey: true, shiftKey: true }],
    ] as const) {
      expect(press(target, key, init).defaultPrevented).toBe(false);
    }
    typeSearch(el, "row");
    expect(press(searchBox(el) as HTMLInputElement, "z", { ctrlKey: true }).defaultPrevented).toBe(false);
    expect(el.search).toBe("row");
    expect(el.sort).toEqual(X_UP);
  });

  it("forgets the reader's changes when the view is set from code (but the page)", async () => {
    const { el, views } = await mountUndo();
    click(el, "x");
    // (Set as it is, it's no change)
    el.sort = el.sort;
    el.search = "";
    el.filter = el.filter;
    el.pageSize = 2;
    expect(disabled(el)).toEqual(["false", "true"]);
    el.page = 2;
    expect(el.undo()).toBe(true);
    expect([el.sort, el.page]).toEqual([[], 1]);
    expect(el.redo()).toBe(true);
    expect([el.sort, el.page]).toEqual([X_UP, 2]);

    el.search = "row";
    expect(disabled(el)).toEqual(["true", "true"]);
    expect(el.undo()).toBe(false);
    for (const set of [
      () => (el.sort = []),
      () => (el.filter = { and: [{ col: "x", op: "gte", value: 10 }] }),
      () => (el.pageSize = 4),
      () => el.resetView(),
    ]) {
      vi.advanceTimersByTime(STEP_MS);
      click(el, "y");
      set();
      expect(el.undo()).toBe(false);
    }
    // (Undone from code, without events)
    expect(views()).toHaveLength(5);
  });

  it("undoes at most 50 changes", async () => {
    const { el } = await mountUndo();
    for (let i = 0; i < 60; i++) {
      click(el, "x");
    }
    let undone = 0;
    while (el.undo()) {
      undone++;
    }
    expect(undone).toBe(50);
  });

  it("keeps what's undone in the URL", async () => {
    history.replaceState(null, "", "/page");
    const { el } = await mountUndo({ viewState: { url: true, key: "t1" } });
    click(el, "x");
    expect(location.search).toBe("?t1.sort=x");
    el.undo();
    expect(location.search).toBe("");
    el.redo();
    expect(location.search).toBe("?t1.sort=x");
  });

  it("forgets it all, and its keys, when the table is replaced", async () => {
    const { el } = await mountUndo();
    click(el, "x");
    vi.useRealTimers();
    const { html, spec } = gtTable(GROUPED, { controls: { bar: true } });
    el.remove();
    el.innerHTML = html + specScript(spec);
    document.body.append(el);
    await tick();

    expect(barButton(el, "undo")).toBeNull();
    expect(el.undo()).toBe(false);
    expect(press(button(el, "y"), "z", { ctrlKey: true }).defaultPrevented).toBe(false);
    // (Nor are changes to the new table's view kept to be undone)
    click(el, "y");
    expect(el.undo()).toBe(false);
  });

  it("starts from the view kept, once ready", async () => {
    history.replaceState(null, "", "/page?t1.sort=x");
    const { el } = await mountUndo({ viewState: { url: true, key: "t1" } });
    expect(disabled(el)).toEqual(["true", "true"]);
    click(el, "y");
    el.undo();
    expect(el.sort).toEqual(X_UP);
    expect(el.undo()).toBe(false);
  });
});

describe("row display", () => {
  const tap =(target: Element, pointerType = "touch") => {
    target.dispatchEvent(new PointerEvent("pointerdown", { bubbles: true, pointerType }));
    (target as HTMLElement).click();
  };
  const marked = (el: GtTable) =>
    Array.from(el.querySelectorAll("tr.gt-i-marked"), (tr) => el.bodyRow(tr as HTMLTableRowElement));

  it("marks the element when text doesn't wrap", async () => {
    expect((await mountTable(GROUPED, { display: { wrap: false } })).hasAttribute("data-gti-nowrap")).toBe(
      true,
    );
    const { html, spec } = gtTable(GROUPED);
    // (The spec decides, whatever the producer wrote)
    const el = await mount(`<gt-table data-gti-nowrap>${html}${specScript(spec)}</gt-table>`);
    expect(el.hasAttribute("data-gti-nowrap")).toBe(false);
  });

  it("marks the data rows when rows are highlighted", async () => {
    const el = await mountTable(GROUPED, { display: { highlight: true } });
    expect(el.hasAttribute("data-gti-highlight")).toBe(true);
    const rows = Array.from(el.querySelectorAll("tr.gt-i-row"), (tr) => el.bodyRow(tr as HTMLTableRowElement));
    expect(rows).toEqual([3, 0, 4, 1, 2]);
  });

  it("leaves the rows alone when they aren't highlighted", async () => {
    const el = await mountTable();
    expect(el.hasAttribute("data-gti-highlight")).toBe(false);
    expect(el.querySelector("tr.gt-i-row")).toBeNull();
    tap(el.rowElement(0)?.cells[1] as Element);
    expect(marked(el)).toEqual([]);
  });

  it("marks the row tapped on a touch screen, until it or another row is tapped", async () => {
    const el = await mountTable(GROUPED, { display: { highlight: true } });
    const cell = (row: number) => el.rowElement(row)?.cells[1] as Element;
    tap(cell(0));
    expect(marked(el)).toEqual([0]);
    tap(cell(1));
    expect(marked(el)).toEqual([1]);
    tap(cell(1));
    expect(marked(el)).toEqual([]);
    // Not by a mouse, which hovers
    tap(cell(2), "mouse");
    expect(marked(el)).toEqual([]);
  });

  it("doesn't mark structural rows, group labels or rows tapped on a link", async () => {
    const el = await mountTable(GROUPED, { display: { highlight: true }, groupsAsColumn: true });
    tap(el.querySelector(".gt_grand_summary_row") as Element);
    tap(el.querySelector(".gt_stub_row_group") as Element);
    const link = el.ownerDocument.createElement("a");
    link.href = "#";
    el.rowElement(2)?.cells[1]?.append(link);
    link.addEventListener("click", (event) => event.preventDefault());
    tap(link);
    expect(marked(el)).toEqual([]);
  });

  it("keeps the mark on its row as rows move", async () => {
    const el = await mountTable(GROUPED, { display: { highlight: true } });
    tap(el.rowElement(4)?.cells[1] as Element);
    el.sort = [{ column: "x", descending: true }];
    expect(marked(el)).toEqual([4]);
  });
});

describe("column resizing", () => {
  // (happy-dom has no layout: every box is 100px wide)
  const resizable = (options: TableOptions = {}) => {
    vi.spyOn(Element.prototype, "getBoundingClientRect").mockReturnValue(new DOMRect(0, 0, 100, 20));
    return mountTable(GROUPED, { ...options, controls: { resizing: true, ...options.controls } });
  };
  const handles = (el: GtTable) => Array.from(el.querySelectorAll<HTMLElement>(".gt-i-resizer"));
  const widths = (el: GtTable) =>
    Array.from(el.querySelectorAll<HTMLElement>("table > colgroup > col"), (col) => col.style.width);
  const press = (target: Element, key: string, shiftKey = false) =>
    target.dispatchEvent(new KeyboardEvent("keydown", { key, shiftKey, bubbles: true, cancelable: true }));
  const pointer = (target: Element, type: string, clientX: number, button = 0) =>
    target.dispatchEvent(
      new PointerEvent(type, { clientX, button, pointerId: 1, pointerType: "mouse", bubbles: true, cancelable: true }),
    );
  const resizes = (el: GtTable) => {
    const details: ResizeEventDetail[] = [];
    el.addEventListener(RESIZE_EVENT, (event) => details.push((event as CustomEvent<ResizeEventDetail>).detail));
    return details;
  };

  it("isn't on unless the spec says so", async () => {
    const el = await mountTable();
    expect(handles(el)).toEqual([]);
    expect(el.querySelector(".gt-i-resizable")).toBeNull();
  });

  it("puts a labelled, focusable splitter at the end of each column label", async () => {
    const el = await resizable();
    const all = handles(el);
    expect(all.map((handle) => handle.getAttribute("aria-label"))).toEqual([
      "Resize column 1",
      "Resize x",
      "Resize y",
    ]);
    for (const handle of all) {
      expect(handle.getAttribute("role")).toBe("separator");
      expect(handle.getAttribute("aria-orientation")).toBe("vertical");
      expect(handle.getAttribute("aria-valuenow")).toBe("100");
      expect(handle.getAttribute("aria-valuetext")).toBe("100 pixels");
      expect(handle.tabIndex).toBe(0);
      // (Beside the sort button, not in it)
      expect(handle.parentElement?.classList.contains("gt-i-resizable")).toBe(true);
      expect(handle.closest("button")).toBeNull();
    }
  });

  it("resizes a column with the arrow keys, fixing every column's width", async () => {
    const el = await resizable();
    const details = resizes(el);
    const handle = handles(el)[1] as HTMLElement;
    expect(el.querySelector("colgroup")).toBeNull();

    press(handle, "ArrowRight");
    const table = el.querySelector("table") as HTMLTableElement;
    expect(table.firstElementChild?.matches("colgroup.gt-i-widths")).toBe(true);
    expect(widths(el)).toEqual(["100px", "110px", "100px"]);
    expect(table.style.tableLayout).toBe("fixed");
    expect(table.style.width).toBe("fit-content");
    expect(handle.getAttribute("aria-valuenow")).toBe("110");

    press(handle, "ArrowRight", true);
    press(handle, "ArrowLeft");
    expect(widths(el)).toEqual(["100px", "150px", "100px"]);
    // Home makes it as narrow as it gets: 2em
    press(handle, "Home");
    expect(widths(el)).toEqual(["100px", "32px", "100px"]);
    press(handle, "ArrowLeft");
    expect(details).toEqual([
      { column: "x", index: 1, width: 110 },
      { column: "x", index: 1, width: 160 },
      { column: "x", index: 1, width: 150 },
      { column: "x", index: 1, width: 32 },
    ]);
    // Other keys are left alone
    expect(press(handle, "a")).toBe(true);
    expect(press(handle, "ArrowRight")).toBe(false);
  });

  it("puts a column back to its starting width with Enter or a double-click", async () => {
    const el = await resizable();
    const details = resizes(el);
    const [stub, x] = handles(el) as [HTMLElement, HTMLElement];
    press(x, "ArrowRight", true);
    press(stub, "ArrowLeft");
    press(x, "Enter");
    expect(widths(el)).toEqual(["90px", "100px", "100px"]);
    expect(x.getAttribute("aria-valuenow")).toBe("100");
    stub.dispatchEvent(new MouseEvent("dblclick", { bubbles: true }));
    expect(widths(el)).toEqual(["100px", "100px", "100px"]);
    // (Already there)
    press(x, "Enter");
    expect(details.map((detail) => [detail.column, detail.width])).toEqual([
      ["x", 150],
      ["row", 90],
      ["x", 100],
      ["row", 100],
    ]);
  });

  it("resizes a column by dragging, without sorting it", async () => {
    const el = await resizable();
    const details = resizes(el);
    const handle = handles(el)[2] as HTMLElement;
    pointer(handle, "pointerdown", 50);
    expect(el.hasAttribute("data-gti-resizing")).toBe(true);
    expect(handle.hasAttribute("data-gti-active")).toBe(true);
    pointer(handle, "pointermove", 90);
    expect(widths(el)).toEqual(["100px", "100px", "140px"]);
    pointer(handle, "pointermove", 20);
    pointer(handle, "pointerup", 20);
    expect(widths(el)).toEqual(["100px", "100px", "70px"]);
    expect(el.hasAttribute("data-gti-resizing")).toBe(false);
    expect(handle.hasAttribute("data-gti-active")).toBe(false);
    // (Once, when the drag ends)
    expect(details).toEqual([{ column: "y", index: 2, width: 70 }]);
    // Moving after the drag does nothing
    pointer(handle, "pointermove", 0);
    expect(widths(el)).toEqual(["100px", "100px", "70px"]);

    handle.click();
    expect(el.sort).toEqual([]);
    expect(header(el, "y").hasAttribute("aria-sort")).toBe(false);
  });

  it("doesn't drag with other buttons, or fire an event for a drag that goes nowhere", async () => {
    const el = await resizable();
    const details = resizes(el);
    const handle = handles(el)[1] as HTMLElement;
    pointer(handle, "pointerdown", 50, 2);
    expect(el.hasAttribute("data-gti-resizing")).toBe(false);
    pointer(handle, "pointerdown", 50);
    pointer(handle, "pointermove", 70);
    pointer(handle, "pointermove", 50);
    pointer(handle, "pointercancel", 50);
    expect(el.hasAttribute("data-gti-resizing")).toBe(false);
    expect(details).toEqual([]);
  });

  it("runs the other way in a right-to-left table", async () => {
    const el = await resizable();
    (el.querySelector("table") as HTMLTableElement).style.direction = "rtl";
    const handle = handles(el)[1] as HTMLElement;
    press(handle, "ArrowRight");
    expect(widths(el)).toEqual(["100px", "90px", "100px"]);
    pointer(handle, "pointerdown", 50);
    pointer(handle, "pointermove", 20);
    pointer(handle, "pointerup", 20);
    expect(widths(el)).toEqual(["100px", "120px", "100px"]);
  });

  it("uses the author's column widths", async () => {
    vi.spyOn(Element.prototype, "getBoundingClientRect").mockReturnValue(new DOMRect(0, 0, 100, 20));
    const { html, spec } = gtTable(GROUPED, { controls: { resizing: true } });
    const colgroup = `<colgroup><col style="width:100px"><col style="width:100px"><col style="width:100px"></colgroup>`;
    const el = await mount(
      `<gt-table>${html.replace('<table class="gt_table">', `<table class="gt_table" style="table-layout:fixed">${colgroup}`)}${specScript(spec)}</gt-table>`,
    );
    press(handles(el)[1] as HTMLElement, "ArrowRight");
    expect(el.querySelectorAll("colgroup")).toHaveLength(1);
    expect(el.querySelector("colgroup.gt-i-widths")).toBeNull();
    expect(widths(el)).toEqual(["100px", "110px", "100px"]);
  });

  it("has handles on the bottom row of labels only, laid out under the spanners", async () => {
    // A spanner over `x` alone; the stubhead and `y` span both rows
    const thead =
      `<tr class="gt_col_headings gt_spanner_row"><th class="gt_col_heading" rowspan="2"></th>` +
      `<th class="gt_column_spanner_outer" colspan="1"><span class="gt_column_spanner">X</span></th>` +
      `<th class="gt_col_heading" rowspan="2" id="t-y">y</th></tr>` +
      `<tr class="gt_col_headings"><th class="gt_col_heading" id="t-x">x</th></tr>`;
    const el = await resizable({ thead });
    const details = resizes(el);
    expect(el.querySelector(".gt_column_spanner_outer .gt-i-resizer")).toBeNull();
    const all = handles(el);
    expect(all.map((handle) => handle.getAttribute("aria-label"))).toEqual(["Resize column 1", "Resize y", "Resize x"]);
    for (const handle of all) {
      press(handle, "ArrowRight");
    }
    expect(details.map((detail) => [detail.column, detail.index])).toEqual([
      ["row", 0],
      ["y", 2],
      ["x", 1],
    ]);
  });

  it("has no handle on a label over the group column and the stub", async () => {
    const thead =
      `<tr class="gt_col_headings"><th class="gt_col_heading" colspan="2">Rows</th>` +
      `<th class="gt_col_heading" id="t-x">x</th><th class="gt_col_heading" id="t-y">y</th></tr>`;
    const el = await resizable({ thead, groupsAsColumn: true });
    const details = resizes(el);
    expect(handles(el).map((handle) => handle.getAttribute("aria-label"))).toEqual(["Resize x", "Resize y"]);
    press(handles(el)[0] as HTMLElement, "ArrowRight");
    expect(widths(el)).toEqual(["100px", "100px", "110px", "100px"]);
    expect(details).toEqual([{ column: "x", index: 2, width: 110 }]);
  });

  it("keeps the widths as rows are sorted", async () => {
    const el = await resizable();
    press(handles(el)[1] as HTMLElement, "ArrowRight");
    el.sort = [{ column: "y", descending: false }];
    expect(widths(el)).toEqual(["100px", "110px", "100px"]);
  });
});

describe("column controls", () => {
  const handles = (el: GtTable) =>
    Array.from(el.querySelectorAll<HTMLElement>(".gt-i-resizer"), (handle) => handle.getAttribute("aria-label"));
  const infoItem = (el: GtTable, name: string) => el.querySelector(`[data-gti-info="${name}"]`) as HTMLElement | null;
  const keys = (el: GtTable) =>
    Array.from(el.querySelectorAll<HTMLElement>(".gt-i-info-keys > div"))
      .filter((entry) => !entry.hidden)
      .map((entry) => entry.querySelector("dd")?.textContent);
  const SORTED_BY_X = ["group:b", 0, 4, 3, "summary:Total", "group:a", 1, 2, "grand:Max"];

  it("gives an unsortable column no sort button, though code can sort by it", async () => {
    const el = await mountTable(GROUPED, { columns: { x: { sortable: false } }, yLabel: "Why" });
    expect(header(el, "x").querySelector("button")).toBeNull();
    expect(header(el, "x").textContent).toBe("x");
    expect(button(el, "y")).not.toBeNull();
    expect(el.sortableColumns).toContain("x");

    el.sort = [{ column: "x", descending: false }];
    expect(shown(el)).toEqual(SORTED_BY_X);
    expect(header(el, "x").hasAttribute("aria-sort")).toBe(false);
  });

  it("starts sorted by an unsortable column, as the spec's view says", async () => {
    const el = await mountTable(GROUPED, {
      columns: { x: { sortable: false } },
      view: { filter: null, sort: [{ column: "x", descending: false }] },
    });
    expect(shown(el)).toEqual(SORTED_BY_X);
  });

  it("says how the table is sorted by an unsortable column with its label", async () => {
    const thead =
      `<tr class="gt_col_headings"><th class="gt_col_heading"></th>` +
      `<th class="gt_col_heading" id="t-x">Ex</th><th class="gt_col_heading" id="t-y">y</th></tr>`;
    const el = await mountTable(GROUPED, {
      thead,
      columns: { x: { sortable: false } },
      controls: { bar: true, search: true },
    });
    el.sort = [{ column: "x", descending: true }];
    expect(infoItem(el, "sort")?.firstElementChild?.textContent).toBe("Sorted by Ex, descending");
  });

  it("leaves the sort out of the info panel when no column has a sort button", async () => {
    const el = await mountTable(GROUPED, {
      columns: { x: { sortable: false }, y: { sortable: false } },
      controls: { bar: true, search: true },
    });
    expect(el.querySelector("button.gt-i-sort")).toBeNull();
    expect(el.querySelector(".gt-i-info")).not.toBeNull();
    expect(infoItem(el, "sort")).toBeNull();
    expect(keys(el)).not.toContain("Sort by more than one column");
  });

  it("filters by an unsortable column", async () => {
    const el = await mountTable(GROUPED, {
      columns: { y: { sortable: false } },
      filters: [{ column: "y", type: "facet", values: ["a", "b", "c"] }],
    });
    expect(header(el, "y").querySelector("button.gt-i-sort")).toBeNull();
    expect(header(el, "y").querySelector("button.gt-i-filter-button")).not.toBeNull();
    el.filter = { and: [{ col: "y", op: "in", value: ["c"] }] };
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
  });

  describe("a column only for querying", () => {
    // `q`, not in the table: "pear" for rows 0 and 4, "apple" for the rest (as a facet)
    const QUERY = { queryRanks: { q: [1, 0, 0, 0, 1] }, controls: { bar: true, search: true } };
    const facet = (texts: string[] | null = ["<Pear>", "Apple", "Apple", "Apple", "<Pear>"]) => ({
      ...QUERY,
      queryColumns: [{ id: "q", kind: "string" as const, label: "Kind", texts }],
      filters: [{ column: "q", type: "facet" as const, values: ["apple", "pear"] }],
    });
    const tokens = (el: GtTable) =>
      Array.from(el.querySelectorAll(".gt-i-tokens .gt-i-token-open"), (b) => b.textContent);

    it("filters by it, with its label, and its values' texts", async () => {
      const el = await mountTable(GROUPED, facet());
      expect(el.filterableColumns).toEqual(["q"]);
      expect(el.querySelector(".gt-i-filter-button")).toBeNull();
      el.filter = { and: [{ col: "q", op: "in", value: ["pear"] }] };
      expect(visible(el)).toEqual(["group:b", 0, 4, "summary:Total", "grand:Max"]);
      expect(tokens(el)).toEqual(["Kind: <Pear>"]);
      // (Without texts, its values)
      const plain = await mountTable(GROUPED, facet(null));
      plain.filter = { and: [{ col: "q", op: "in", value: ["pear"] }] };
      expect(tokens(plain)).toEqual(["Kind: pear"]);
    });

    it("filters it by its texts, which the search doesn't look in", async () => {
      const el = await mountTable(GROUPED, {
        ...QUERY,
        queryColumns: [{ id: "q", kind: "string", label: "Kind", texts: ["Crème", "", "x\ncreme", "", "pie"] }],
        filters: [{ column: "q", type: "text", values: null }],
      });
      el.filter = { and: [{ col: "q", op: "contains", value: "CREME" }] };
      expect(visible(el)).toEqual(["group:b", 0, "summary:Total", "group:a", 2, "grand:Max"]);
      el.filter = null;
      el.search = "creme";
      expect(visible(el)).toEqual(["grand:Max"]);
    });

    it("sorts by it, as by an unsortable column, saying so with its label", async () => {
      const el = await mountTable(GROUPED, { ...facet(), view: { filter: null, sort: [{ column: "q", descending: true }] } });
      expect(el.sortableColumns).toContain("q");
      expect(shown(el)).toEqual(["group:b", 0, 4, 3, "summary:Total", "group:a", 1, 2, "grand:Max"]);
      expect(el.querySelector('[data-gti-info="sort"]')?.firstElementChild?.textContent).toBe("Sorted by Kind, descending");
    });
  });

  it("leaves an unsearchable column out of the search", async () => {
    const el = await mountTable(GROUPED, { columns: { x: { searchable: false } }, controls: { search: true } });
    // (Rows 0 and 4 have "20" in x; none has it in another column)
    el.search = "20";
    expect(visible(el)).toEqual(["grand:Max"]);
    el.search = "c";
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
    // (Every word in one of the cells it looks in)
    el.search = "row_1 b";
    expect(visible(el)).toEqual(["group:b", 0, "summary:Total", "grand:Max"]);
    el.search = "row_1 20";
    expect(visible(el)).toEqual(["grand:Max"]);
  });

  it("leaves an unsearchable stub column out of the search", async () => {
    const el = await mountTable(GROUPED, { columns: { row: { searchable: false } }, controls: { search: true } });
    el.search = "row_1";
    expect(visible(el)).toEqual(["grand:Max"]);
    el.search = "5";
    expect(visible(el)).toEqual(["group:a", 1, "grand:Max"]);
  });

  it("filters an unsearchable column by its text", async () => {
    const el = await mountTable(GROUPED, {
      columns: { x: { searchable: false } },
      controls: { search: true },
      filters: [{ column: "x", type: "text", values: null }],
    });
    el.filter = { and: [{ col: "x", op: "contains", value: "20" }] };
    expect(visible(el)).toEqual(["group:b", 0, 4, "summary:Total", "grand:Max"]);
  });

  describe("resizing", () => {
    const resizable = (options: TableOptions = {}) => {
      vi.spyOn(Element.prototype, "getBoundingClientRect").mockReturnValue(new DOMRect(0, 0, 100, 20));
      return mountTable(GROUPED, { ...options, controls: { resizing: true, ...options.controls } });
    };

    it("gives an unresizable column no handle", async () => {
      const el = await resizable({ columns: { x: { resizable: false } } });
      expect(handles(el)).toEqual(["Resize column 1", "Resize y"]);
      expect(header(el, "x").classList.contains("gt-i-resizable")).toBe(false);
    });

    it("finds the column after the selection column", async () => {
      const el = await resizable({ columns: { row: { resizable: false } }, controls: { selection: "multiple" } });
      expect(handles(el)).toEqual(["Resize x", "Resize y"]);
    });

    it("finds the column after the row group column", async () => {
      const thead =
        `<tr class="gt_col_headings"><th class="gt_col_heading">Group</th><th class="gt_col_heading"></th>` +
        `<th class="gt_col_heading" id="t-x">x</th><th class="gt_col_heading" id="t-y">y</th></tr>`;
      const el = await resizable({ thead, groupsAsColumn: true, columns: { y: { resizable: false } } });
      // (The row group column stays resizable)
      expect(handles(el)).toEqual(["Resize Group", "Resize column 2", "Resize x"]);
    });
  });
});

describe("row selection", () => {
  const selectable = (mode: "single" | "multiple" = "multiple", options: TableOptions = {}, body = GROUPED) =>
    mountTable(body, { ...options, controls: { selection: mode, ...options.controls } });
  const box = (el: GtTable, row: number) =>
    el.rowElement(row)?.querySelector<HTMLInputElement>(":scope > .gt-i-select > input") as HTMLInputElement;
  const all = (el: GtTable) => el.querySelector<HTMLInputElement>("thead .gt-i-select input") as HTMLInputElement;
  const press = (target: Element, shiftKey = false) =>
    target.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true, shiftKey }));
  const selects = (el: GtTable) => {
    const details: number[][] = [];
    el.addEventListener(SELECT_EVENT, (event) =>
      details.push((event as CustomEvent<SelectEventDetail>).detail.selection),
    );
    return details;
  };
  const tinted = (el: GtTable) =>
    Array.from(el.querySelectorAll("tr.gt-i-selected"), (tr) => el.bodyRow(tr as HTMLTableRowElement));
  const colspans = (el: GtTable, selector: string) =>
    Array.from(el.querySelectorAll(selector), (cell) => cell.getAttribute("colspan"));

  it("isn't on unless the spec says so", async () => {
    const el = await mountTable();
    expect(el.querySelector(".gt-i-select")).toBeNull();
    expect(el.selection).toEqual([]);
    expect(() => {
      el.selection = [0];
    }).toThrow(/can't be selected/);
    el.selection = [];
  });

  it("puts a labelled checkbox before each data row's cells", async () => {
    const el = await selectable();
    for (const row of [0, 1, 2, 3, 4]) {
      const tr = el.rowElement(row) as HTMLTableRowElement;
      const cell = tr.cells[0] as HTMLTableCellElement;
      expect(cell.matches("td.gt_row.gt_center.gt-i-select")).toBe(true);
      expect(cell.classList.contains("gt_right")).toBe(false);
      expect(box(el, row).type).toBe("checkbox");
      expect(box(el, row).getAttribute("aria-label")).toBe(`Select row_${row + 1}`);
      expect(tr.cells).toHaveLength(4);
    }
  });

  it("names rows without a stub by number", async () => {
    const { html, spec } = gtTable([0, 1], { controls: { selection: "single" } });
    const plain = html.replace(/<th class="gt_row gt_left gt_stub">row_\d<\/th>/g, "<td class=\"gt_row\">-</td>");
    const el = await mount(`<gt-table>${plain}${specScript(spec)}</gt-table>`);
    expect(box(el, 1).getAttribute("aria-label")).toBe("Select row 2");
  });

  it("widens the rows across the table, and gives summary rows an empty cell", async () => {
    const thead =
      `<tr class="gt_heading"><td class="gt_heading gt_title" colspan="3">Title</td></tr>` +
      `<tr class="gt_col_headings"><th class="gt_col_heading"></th>` +
      `<th class="gt_col_heading" id="t-x">x</th><th class="gt_col_heading" id="t-y">y</th></tr>`;
    const { html, spec } = gtTable(GROUPED, { thead, controls: { selection: "multiple" } });
    const footed = html.replace("</tbody>", `</tbody><tfoot><tr><td class="gt_footnote" colspan="3">Note</td></tr></tfoot>`);
    const el = await mount(`<gt-table>${footed}${specScript(spec)}</gt-table>`);
    expect(colspans(el, ".gt_title, .gt_group_heading, .gt_footnote")).toEqual(["4", "4", "4", "4"]);
    // Styled as the row's other cells are
    const lead = (kind: string) => el.querySelector(`th.gt_stub.${kind}`)?.closest("tr")?.cells[0];
    expect(lead("gt_summary_row")?.matches("td.gt_summary_row.gt-i-select:empty")).toBe(true);
    expect(lead("gt_grand_summary_row")?.matches("td.gt_grand_summary_row.gt-i-select:empty")).toBe(true);
    expect(el.querySelectorAll("td.gt-i-select:empty")).toHaveLength(2);
  });

  it("puts a select-all checkbox in the column labels, across every row of them", async () => {
    const thead =
      `<tr class="gt_col_headings gt_spanner_row"><th class="gt_col_heading" rowspan="2"></th>` +
      `<th class="gt_column_spanner_outer" colspan="2"><span class="gt_column_spanner">XY</span></th></tr>` +
      `<tr class="gt_col_headings"><th class="gt_col_heading" id="t-x">x</th><th class="gt_col_heading" id="t-y">y</th></tr>`;
    const el = await selectable("multiple", { thead });
    const th = el.querySelector("thead th.gt-i-select") as HTMLTableCellElement;
    expect(th.parentElement?.classList.contains("gt_spanner_row")).toBe(true);
    expect(th.parentElement?.firstElementChild).toBe(th);
    expect(th.rowSpan).toBe(2);
    expect(th.scope).toBe("col");
    expect(all(el).getAttribute("aria-label")).toBe("Select all rows");
    // One row: no rowspan
    expect((await selectable()).querySelector("thead th.gt-i-select")?.hasAttribute("rowspan")).toBe(false);
  });

  it("labels the column for screen readers when one row is selected at a time", async () => {
    const el = await selectable("single");
    const th = el.querySelector("thead th.gt-i-select") as HTMLTableCellElement;
    expect(th.querySelector("input")).toBeNull();
    expect(th.querySelector(".gt-i-hidden")?.textContent).toBe("Select");
  });

  it("adds a column to the author's column widths", async () => {
    const { html, spec } = gtTable(GROUPED, { controls: { selection: "multiple" } });
    const colgroup = `<colgroup><col style="width:100px"><col style="width:100px"><col style="width:100px"></colgroup>`;
    const el = await mount(
      `<gt-table>${html.replace('<table class="gt_table">', `<table class="gt_table">${colgroup}`)}${specScript(spec)}</gt-table>`,
    );
    const cols = el.querySelectorAll<HTMLElement>("colgroup > col");
    expect(cols).toHaveLength(4);
    expect(cols[0]?.classList.contains("gt-i-select")).toBe(true);
    expect(cols[0]?.style.width).toBe("2.5em");
  });

  it("selects and deselects rows with their checkboxes, telling listeners", async () => {
    const el = await selectable();
    const details = selects(el);
    box(el, 4).click();
    box(el, 1).click();
    expect(el.selection).toEqual([1, 4]);
    expect(box(el, 4).checked).toBe(true);
    expect(tinted(el)).toEqual([4, 1]);
    box(el, 4).click();
    expect(el.selection).toEqual([1]);
    expect(box(el, 4).checked).toBe(false);
    expect(details).toEqual([[4], [1, 4], [1]]);
  });

  it("selects a row clicked anywhere but on its own controls or a group's label", async () => {
    const el = await selectable("multiple", { groupsAsColumn: true });
    press(el.rowElement(0)?.cells[2] as Element);
    expect(el.selection).toEqual([0]);
    press(el.rowElement(0)?.querySelector(".gt_stub") as Element);
    expect(el.selection).toEqual([]);
    // (The click on the group label cell, on row 3's row)
    press(el.querySelector(".gt_stub_row_group") as Element);
    const link = el.ownerDocument.createElement("a");
    link.href = "#";
    link.addEventListener("click", (event) => event.preventDefault());
    el.rowElement(2)?.cells[2]?.append(link);
    press(link);
    press(el.querySelector(".gt_grand_summary_row") as Element);
    expect(el.selection).toEqual([]);
  });

  it("doesn't select a row when the click ends selecting text in it", async () => {
    const el = await selectable();
    const cell = el.rowElement(0)?.cells[2] as HTMLTableCellElement;
    const range = document.createRange();
    range.selectNodeContents(cell);
    getSelection()?.addRange(range);
    press(cell);
    expect(el.selection).toEqual([]);
    getSelection()?.removeAllRanges();
    press(cell);
    expect(el.selection).toEqual([0]);
  });

  it("selects one row at a time in single mode", async () => {
    const el = await selectable("single");
    const details = selects(el);
    box(el, 0).click();
    press(el.rowElement(2)?.cells[2] as Element);
    expect(el.selection).toEqual([2]);
    expect(box(el, 0).checked).toBe(false);
    // Shift selects no range
    press(el.rowElement(1)?.cells[2] as Element, true);
    expect(el.selection).toEqual([1]);
    press(el.rowElement(1)?.cells[2] as Element);
    expect(el.selection).toEqual([]);
    expect(details).toEqual([[0], [2], [1], []]);
  });

  it("selects a range in the order shown with Shift", async () => {
    const el = await selectable("multiple", {}, [0, 1, 2, 3, 4]);
    el.sort = [{ column: "y", descending: true }];
    // (Rows by y, descending: 2, 0, then 1, 3, 4)
    expect(shown(el)).toEqual([2, 0, 1, 3, 4]);
    press(el.rowElement(0)?.cells[2] as Element);
    press(el.rowElement(3)?.cells[2] as Element, true);
    expect(el.selection).toEqual([0, 1, 3]);
    expect(live(el)).toBe("3 rows selected");
    // A range follows the row clicked: here, deselecting
    box(el, 2).click();
    expect(el.selection).toEqual([0, 1, 2, 3]);
    press(el.rowElement(1)?.cells[2] as Element, true);
    expect(el.selection).toEqual([3]);
  });

  it("keeps Shift-clicks from selecting text", async () => {
    const el = await selectable();
    const cell = el.rowElement(0)?.cells[2] as Element;
    const down = (shiftKey: boolean) =>
      cell.dispatchEvent(new MouseEvent("mousedown", { bubbles: true, cancelable: true, shiftKey }));
    expect(down(true)).toBe(false);
    expect(down(false)).toBe(true);
  });

  it("ranges over the rows that match the search only", async () => {
    const el = await selectable("multiple", {}, [0, 1, 2, 3, 4]);
    el.search = "a";
    expect(visible(el)).toEqual([1, 3, 4]);
    press(el.rowElement(1)?.cells[2] as Element);
    press(el.rowElement(4)?.cells[2] as Element, true);
    expect(el.selection).toEqual([1, 3, 4]);
  });

  it("selects every row that matches the search with the select-all checkbox, on every page", async () => {
    const el = await selectable("multiple", { pagination: { enabled: true } }, [0, 1, 2, 3, 4]);
    const details = selects(el);
    all(el).click();
    expect(el.selection).toEqual([0, 1, 2, 3, 4]);
    expect(all(el).checked).toBe(true);
    expect(live(el)).toBe("5 rows selected");
    all(el).click();
    expect(el.selection).toEqual([]);
    expect(live(el)).toBe("No rows selected");

    el.search = "a";
    expect(all(el).getAttribute("aria-label")).toBe("Select all matching rows");
    box(el, 0).click();
    all(el).click();
    expect(el.selection).toEqual([0, 1, 3, 4]);
    expect(all(el).checked).toBe(true);
    // Deselecting them leaves the rest alone
    all(el).click();
    expect(el.selection).toEqual([0]);
    expect(details).toEqual([[0, 1, 2, 3, 4], [], [0], [0, 1, 3, 4], [0]]);
  });

  it("shows whether all, some or none of the matching rows are selected", async () => {
    const el = await selectable("multiple", {}, [0, 1, 2, 3, 4]);
    const state = () => [all(el).checked, all(el).indeterminate];
    expect(state()).toEqual([false, false]);
    box(el, 1).click();
    expect(state()).toEqual([false, true]);
    el.selection = [0, 1, 2, 3, 4];
    expect(state()).toEqual([true, false]);
    el.selection = [1, 3];
    el.search = "a";
    expect(state()).toEqual([false, true]);
    el.search = "zzz";
    expect(state()).toEqual([false, false]);
    expect(all(el).disabled).toBe(true);
    el.search = "";
    expect(all(el).disabled).toBe(false);
  });

  it("selects the whole header cell's checkbox from a click on the cell", async () => {
    const el = await selectable();
    press(el.querySelector("thead th.gt-i-select") as Element);
    expect(el.selection).toEqual([0, 1, 2, 3, 4]);
  });

  it("keeps the selection as rows are sorted, searched and paged", async () => {
    const el = await selectable("multiple", { pagination: { enabled: true } }, [0, 1, 2, 3, 4]);
    el.selection = [0, 3];
    el.sort = [{ column: "x" }];
    el.search = "b";
    el.search = "";
    el.page = 2;
    expect(el.selection).toEqual([0, 3]);
    expect(box(el, 3).checked).toBe(true);
    expect(tinted(el).sort()).toEqual([0, 3]);
  });

  it("sets the selection without telling listeners, checking the rows", async () => {
    const el = await selectable("single");
    const details = selects(el);
    el.selection = [3];
    expect(box(el, 3).checked).toBe(true);
    el.selection = [];
    expect(details).toEqual([]);
    expect(() => {
      el.selection = [0, 1];
    }).toThrow(/only one row/);
    expect(() => {
      el.selection = [5];
    }).toThrow(/no data row 5/);
    for (const bad of [-1, 1.5, Number.NaN]) {
      expect(() => {
        el.selection = [bad];
      }).toThrow(RangeError);
    }
    // (Duplicates are one row)
    el.selection = [2, 2];
    expect(el.selection).toEqual([2]);
  });

  it("takes a selection set before hydration, dropping what the table can't have", async () => {
    const { html, spec } = gtTable(GROUPED, { controls: { selection: "multiple" } });
    document.body.innerHTML = "";
    const el = document.createElement(TAG_NAME) as GtTable;
    el.selection = [4, 1, 9];
    expect(el.selection).toEqual([1, 4, 9]);
    el.innerHTML = `${html}${specScript(spec)}`;
    document.body.append(el);
    await tick();
    expect(el.state).toBe("ready");
    expect(el.selection).toEqual([1, 4]);
    expect(box(el, 4).checked).toBe(true);

    const single = gtTable(GROUPED, { controls: { selection: "single" } });
    const other = document.createElement(TAG_NAME) as GtTable;
    other.selection = [4, 1];
    other.innerHTML = `${single.html}${specScript(single.spec)}`;
    document.body.append(other);
    await tick();
    expect(other.selection).toEqual([1]);
  });

  it("puts the group column after the checkboxes, as the groups' rows move", async () => {
    const el = await selectable("multiple", { groupsAsColumn: true });
    const lead = (row: number) =>
      Array.from(el.rowElement(row)?.cells ?? [], (cell) => cell.className.split(" ").pop()).slice(0, 2);
    expect(lead(3)).toEqual(["gt-i-select", "gt_stub_row_group"]);
    el.sort = [{ column: "x" }];
    // (Group "b" now starts with row 0, its row with the lowest x)
    expect(lead(0)).toEqual(["gt-i-select", "gt_stub_row_group"]);
    expect(lead(3)).toEqual(["gt-i-select", "gt_stub"]);
  });

  it("stripes the checkboxes' cells as the body's", async () => {
    const el = await selectable("multiple", { striping: { stub: false, body: true } }, [0, 1, 2, 3, 4]);
    const striped = () =>
      [0, 1, 2, 3, 4].map((row) => el.rowElement(row)?.cells[0]?.classList.contains("gt_striped"));
    expect(striped()).toEqual([false, true, false, true, false]);
    el.sort = [{ column: "row", descending: true }];
    expect(striped()).toEqual([false, true, false, true, false].reverse());
  });

  it("doesn't search the checkboxes' cells", async () => {
    const el = await selectable("multiple", {}, [0, 1, 2, 3, 4]);
    el.search = "Select";
    expect(visible(el)).toEqual([]);
  });

  it("has no resize handle, counting the column in resize events", async () => {
    vi.spyOn(Element.prototype, "getBoundingClientRect").mockReturnValue(new DOMRect(0, 0, 100, 20));
    const el = await selectable("multiple", { controls: { resizing: true } });
    const details: ResizeEventDetail[] = [];
    el.addEventListener(RESIZE_EVENT, (event) => details.push((event as CustomEvent<ResizeEventDetail>).detail));
    const handles = Array.from(el.querySelectorAll<HTMLElement>(".gt-i-resizer"));
    // (The stub is the second column now)
    expect(handles.map((handle) => handle.getAttribute("aria-label"))).toEqual(["Resize column 2", "Resize x", "Resize y"]);
    handles[1]?.dispatchEvent(new KeyboardEvent("keydown", { key: "ArrowRight", bubbles: true, cancelable: true }));
    expect(details).toEqual([{ column: "x", index: 2, width: 110 }]);
    expect(Array.from(el.querySelectorAll<HTMLElement>("colgroup > col"), (col) => col.style.width)).toEqual([
      "100px",
      "100px",
      "110px",
      "100px",
    ]);
  });

  it("selects rows in a table whose stub has merged cells", async () => {
    const { html, spec } = gtTable([0, 1, 2, 3, 4], { controls: { selection: "multiple" } });
    const merged = html.replace(
      `<th class="gt_row gt_left gt_stub">row_1</th>`,
      `<th class="gt_row gt_left gt_stub" rowspan="2">row_1</th>`,
    );
    const el = await mount(`<gt-table>${merged}${specScript(spec)}</gt-table>`);
    expect(el.rowElement(1)?.cells[0]?.classList.contains("gt-i-select")).toBe(true);
    press(el.rowElement(0)?.cells[2] as Element);
    press(el.rowElement(2)?.cells[2] as Element, true);
    expect(el.selection).toEqual([0, 1, 2]);
    all(el).click();
    expect(el.selection).toEqual([0, 1, 2, 3, 4]);
  });

  it("clears the selection when the table is hydrated again", async () => {
    const el = await selectable();
    el.selection = [1];
    // (New children, then a move)
    const { html, spec } = gtTable(GROUPED, { controls: { selection: "multiple" } });
    el.innerHTML = `${html}${specScript(spec)}`;
    el.remove();
    document.body.append(el);
    await tick();
    expect(el.state).toBe("ready");
    expect(el.selection).toEqual([]);
    expect(el.querySelectorAll("tr.gt-i-selected")).toHaveLength(0);
  });
});

describe("a body that scrolls", () => {
  const scrolling = (options: TableOptions = {}) => mountTable(GROUPED, { layout: { height: "200px" }, ...options });
  const scroller = (el: GtTable) => el.querySelector(".gt-i-scroller") as HTMLElement;

  it("scrolls in GT's container, within the height, with the rows stuck to its edges marked", async () => {
    const el = await scrolling();
    expect(el.hasAttribute("data-gti-scroll")).toBe(true);
    expect(el.hasAttribute("data-gti-sticky")).toBe(true);
    expect(el.style.getPropertyValue("--gt-i-height")).toBe("200px");
    expect(scroller(el).id).toBe("t");
    // Only the grand summary rows at the bottom stick to the bottom
    expect(Array.from(el.querySelectorAll("tr.gt-i-stuck-bottom"), (tr) => tr.textContent)).toEqual(["Max--"]);
    // Group headings stick under the column labels
    expect((el.querySelector(".gt_group_heading") as HTMLElement).style.top).toContain("var(--gt-i-head");
    const table = el.querySelector("table") as HTMLTableElement;
    expect(table.style.borderCollapse).toBe("separate");
  });

  it("wraps a table without a container in one", async () => {
    const { html, spec } = gtTable(GROUPED, { layout: { height: "50vh" } });
    const el = await mount(`<gt-table>${html.replace(/^<div id="t">|<\/div>$/g, "")}${specScript(spec)}</gt-table>`);
    expect(scroller(el).tagName).toBe("DIV");
    expect(scroller(el).firstElementChild?.tagName).toBe("TABLE");
  });

  it("has shadows over its edges, hidden at first", async () => {
    const el = await scrolling();
    const shades = Array.from(el.querySelectorAll(":scope > .gt-i-shade"));
    expect(shades.map((shade) => shade.getAttribute("data-gti-edge"))).toEqual(["top", "bottom"]);
    expect(shades.every((shade) => shade.getAttribute("aria-hidden") === "true")).toBe(true);
    expect(shades.some((shade) => shade.hasAttribute("data-gti-shown"))).toBe(false);
  });

  it("goes back to the top on another page, but not when sorting", async () => {
    const el = await scrolling({ pagination: { enabled: true } });
    scroller(el).scrollTop = 40;
    el.sort = [{ column: "x" }];
    expect(scroller(el).scrollTop).toBe(40);
    el.page = 2;
    expect(scroller(el).scrollTop).toBe(0);
  });

  it("follows the spec, whatever the producer wrote, and undoes it all when the table is replaced", async () => {
    const { html, spec } = gtTable(GROUPED);
    const el = await mount(
      `<gt-table data-gti-scroll style="--gt-i-height: 200px">${html}${specScript(spec)}</gt-table>`,
    );
    expect(el.hasAttribute("data-gti-scroll")).toBe(false);
    expect(el.style.getPropertyValue("--gt-i-height")).toBe("");
    expect(el.querySelector(".gt-i-scroller, .gt-i-shade")).toBeNull();

    const replace = async (table: { html: string; spec: object }) => {
      el.remove();
      el.innerHTML = table.html + specScript(table.spec);
      document.body.append(el);
      await tick();
    };
    await replace(gtTable(GROUPED, { layout: { height: "200px" } }));
    expect(el.hasAttribute("data-gti-sticky")).toBe(true);
    await replace({ html, spec });
    expect(el.hasAttribute("data-gti-sticky")).toBe(false);
    expect(el.style.getPropertyValue("--gt-i-head")).toBe("");
    expect(el.querySelector(".gt-i-shade")).toBeNull();
  });

  it("moves a group's label cell with its borders when groups are a column", async () => {
    const el = await scrolling({ groupsAsColumn: true });
    el.search = "20";
    const label = el.querySelector(".gt_stub_row_group") as HTMLTableCellElement;
    // (On group b's first row shown, row 0)
    expect(el.bodyRow(label.parentElement as HTMLTableRowElement)).toBe(0);
    expect(label.style.getPropertyValue("border-top-style")).not.toBe("");
  });
});

describe("a table wider than its container", () => {
  // (happy-dom has no layout: the table is as wide as `width`, in a container 300px wide, and every
  // cell is 100px wide)
  let width = 800;
  let room = 300;
  const layout = () => {
    vi.spyOn(Element.prototype, "scrollWidth", "get").mockImplementation(() => width);
    vi.spyOn(HTMLElement.prototype, "clientWidth", "get").mockImplementation(() => room);
    vi.spyOn(Element.prototype, "getBoundingClientRect").mockReturnValue(new DOMRect(0, 0, 100, 20));
  };
  const responsive = (options: TableOptions = {}) => {
    layout();
    return mountTable(GROUPED, { layout: { responsive: "scroll" }, ...options });
  };
  const scroller = (el: GtTable) => el.querySelector(".gt-i-scroller") as HTMLElement;
  const inset = (cell: Element | null) => (cell as HTMLElement).style.getPropertyValue("inset-inline-start");
  const hint = (el: GtTable) => el.querySelector(".gt-i-hint");

  afterEach(() => {
    width = 800;
    room = 300;
  });

  it("pins the selection column and the stub, filled, drawing their borders", async () => {
    const el = await responsive({ controls: { selection: "multiple" } });
    expect(el.hasAttribute("data-gti-wide")).toBe(true);
    expect(scroller(el).id).toBe("t");
    const stub = Array.from(el.querySelectorAll("tbody th.gt_stub"));
    expect(stub.length).toBeGreaterThan(0);
    expect(stub.every((cell) => cell.classList.contains("gt-i-pinned"))).toBe(true);
    expect(Array.from(el.querySelectorAll("thead th"), (th) => th.classList.contains("gt-i-pinned"))).toEqual([
      true,
      true,
      false,
      false,
    ]);
    expect(el.querySelector("tbody td.gt_row:not(.gt-i-select)")?.classList.contains("gt-i-pinned")).toBe(false);
    // Each column after the ones before it, with what has focus kept clear of them
    expect(inset(el.querySelector("tbody td.gt-i-select"))).toBe("0px");
    expect(inset(stub[0] as Element)).toBe("100px");
    expect(scroller(el).style.getPropertyValue("scroll-padding-inline-start")).toBe("200px");
    // (Without a background of their own, they're filled with what's behind them)
    expect(stub[0]?.classList.contains("gt-i-filled")).toBe(true);
    expect((stub[0] as HTMLElement).style.getPropertyValue("--gt-i-fill")).toContain("linear-gradient");
    expect((el.querySelector("table") as HTMLTableElement).style.borderCollapse).toBe("separate");
  });

  it("selects a row clicked, in the container that has focus", async () => {
    const el = await responsive({ controls: { selection: "multiple" } });
    expect(scroller(el).tabIndex).toBe(0);
    (el.querySelector("tbody td.gt_row:not(.gt-i-select)") as HTMLElement).click();
    expect(el.selection).toEqual([3]);
  });

  it("pins the row group column too, when groups are a column", async () => {
    const el = await responsive({ groupsAsColumn: true });
    const label = el.querySelector(".gt_stub_row_group") as HTMLElement;
    expect(label.classList.contains("gt-i-pinned")).toBe(true);
    expect(inset(label)).toBe("0px");
    expect(inset(el.querySelector("tbody th.gt_stub"))).toBe("100px");
  });

  it("keeps the contents of the cells across the table in view", async () => {
    const el = await responsive();
    const headings = Array.from(el.querySelectorAll<HTMLElement>(".gt_group_heading"));
    expect(headings.map((th) => th.firstElementChild?.className)).toEqual(["gt-i-inview", "gt-i-inview"]);
    expect(headings.map((th) => th.textContent)).toEqual(["b", "a"]);
    const div = headings[0]?.firstElementChild as HTMLElement;
    expect(div.style.getPropertyValue("--gt-i-room")).toBe("300px");
    expect(div.style.getPropertyValue("inset-inline-start")).toBe("0px");
    // And the row saying that nothing matches
    el.search = "zzz";
    expect(el.querySelector("tr.gt-i-empty td > .gt-i-inview")?.textContent).toBe("No matching rows");
  });

  it("says it scrolls, until it first does, and shades its sides", async () => {
    const el = await responsive();
    expect(hint(el)?.textContent).toBe("Scroll for more →");
    expect(hint(el)?.getAttribute("aria-hidden")).toBe("true");
    expect(hint(el)?.hasAttribute("data-gti-shown")).toBe(true);
    expect(Array.from(el.querySelectorAll(":scope > .gt-i-shade"), (shade) => shade.getAttribute("data-gti-edge"))).toEqual([
      "left",
      "right",
    ]);
    scroller(el).scrollLeft = 40;
    scroller(el).dispatchEvent(new Event("scroll"));
    expect(hint(el)).toBeNull();
    el.search = "2";
    expect(hint(el)).toBeNull();
  });

  it("is a region that can have focus, named for the table", async () => {
    layout();
    const { html, spec } = gtTable(GROUPED, { layout: { responsive: "scroll" } });
    const el = await mount(
      `<gt-table>${html.replace('<table class="gt_table">', '<table class="gt_table" aria-labelledby="t-title">')}${specScript(spec)}</gt-table>`,
    );
    expect(scroller(el).tabIndex).toBe(0);
    expect(scroller(el).getAttribute("role")).toBe("region");
    expect(scroller(el).getAttribute("aria-labelledby")).toBe("t-title");
    // (Or "Table", without a title)
    const untitled = await responsive();
    expect(scroller(untitled).getAttribute("aria-label")).toBe("Table");
  });

  it("is left alone while it fits, and pinned once it doesn't", async () => {
    width = 300;
    const el = await responsive();
    expect(el.hasAttribute("data-gti-wide")).toBe(false);
    expect(el.querySelector(".gt-i-hint, .gt-i-inview, .gt-i-shade")).toBeNull();
    expect((el.querySelector("table") as HTMLTableElement).style.borderCollapse).toBe("");
    expect(scroller(el).hasAttribute("role")).toBe(false);

    width = 800;
    el.search = "2";
    expect(el.hasAttribute("data-gti-wide")).toBe(true);
    expect(hint(el)?.hasAttribute("data-gti-shown")).toBe(true);
    expect(scroller(el).getAttribute("role")).toBe("region");

    width = 300;
    el.search = "";
    expect(el.hasAttribute("data-gti-wide")).toBe(false);
    expect(hint(el)?.hasAttribute("data-gti-shown")).toBe(false);
    expect(scroller(el).hasAttribute("role")).toBe(false);
    expect(scroller(el).hasAttribute("tabindex")).toBe(false);
  });

  describe("with data columns pinned", () => {
    const end = (cell: Element | null) => (cell as HTMLElement).style.getPropertyValue("inset-inline-end");
    const padding = (el: GtTable, side: string) => scroller(el).style.getPropertyValue(`scroll-padding-inline-${side}`);
    const pinned = (cells: Iterable<Element>) =>
      Array.from(cells, (cell) => (cell.classList.contains("gt-i-pinned") ? "pinned" : "") + (cell.classList.contains("gt-i-pin") ? "+pin" : ""));
    const both = { x: { pin: "start" as const }, y: { pin: "end" as const } };
    beforeEach(() => {
      width = 2000;
      room = 600;
    });

    it("pins them after the stub, and at the end", async () => {
      const el = await responsive({ columns: both });
      expect(pinned(el.querySelectorAll("thead th"))).toEqual(["pinned", "pinned+pin", "pinned+pin"]);
      const row = el.querySelector("tbody tr:not(.gt_group_heading_row)") as HTMLTableRowElement;
      expect(pinned(row.cells)).toEqual(["pinned", "pinned+pin", "pinned+pin"]);
      expect(Array.from(row.cells, inset)).toEqual(["0px", "100px", ""]);
      expect(Array.from(row.cells, end)).toEqual(["", "", "0px"]);
      expect([padding(el, "start"), padding(el, "end")]).toEqual(["200px", "100px"]);
      // (Not the group headings, across the table)
      expect(el.querySelector(".gt_group_heading")?.classList.contains("gt-i-pinned")).toBe(false);
    });

    it("pins those at the end before the ones after them, with the stub alone at the start", async () => {
      const el = await responsive({ columns: { x: { pin: "end" }, y: { pin: "end" } } });
      const row = el.querySelector("tbody tr:not(.gt_group_heading_row)") as HTMLTableRowElement;
      expect(pinned(row.cells)).toEqual(["pinned", "pinned+pin", "pinned+pin"]);
      expect(Array.from(row.cells, end)).toEqual(["", "100px", "0px"]);
      expect([padding(el, "start"), padding(el, "end")]).toEqual(["100px", "200px"]);
    });

    it("pins them after the selection column, the row group column, and the stub", async () => {
      room = 1200;
      const el = await responsive({ controls: { selection: "single" }, groupsAsColumn: true, columns: both });
      const row = el.querySelector("tbody tr.gt_row_group_first") as HTMLTableRowElement;
      expect(pinned(row.cells)).toEqual(["pinned", "pinned", "pinned", "pinned+pin", "pinned+pin"]);
      expect(Array.from(row.cells, inset)).toEqual(["0px", "100px", "200px", "300px", ""]);
      expect(end(row.cells[4] as Element)).toBe("0px");
      // (A row in a group, without its label cell)
      const next = row.nextElementSibling as HTMLTableRowElement;
      expect(Array.from(next.cells, inset)).toEqual(["0px", "200px", "300px", ""]);
    });

    it("doesn't pin a spanner over columns on either side of a pinned edge", async () => {
      const el = await responsive({
        columns: { x: { pin: "start" } },
        thead:
          `<tr class="gt_col_spanners"><th class="gt_col_heading" rowspan="2"></th>` +
          `<th class="gt_column_spanner_outer" colspan="2">both</th></tr>` +
          `<tr class="gt_col_headings"><th class="gt_col_heading gt_right" id="t-x">x</th>` +
          `<th class="gt_col_heading gt_left" id="t-y">y</th></tr>`,
      });
      expect(pinned(el.querySelectorAll("thead th"))).toEqual(["pinned", "", "pinned+pin", ""]);
    });

    it("shades the scrolling columns before the ones pinned at the end", async () => {
      const el = await responsive({ columns: both });
      const shade = el.querySelector('.gt-i-shade[data-gti-edge="right"]') as HTMLElement;
      // (At the end column's inline start, which every cell's is in happy-dom, not the container's end)
      expect(shade.style.left).toBe("0px");
      const plain = await responsive();
      expect((plain.querySelector('.gt-i-shade[data-gti-edge="right"]') as HTMLElement).style.left).toBe("600px");
    });

    it("pins only the stub while they'd take up more than half the container", async () => {
      room = 300;
      const el = await responsive({ columns: both });
      const row = el.querySelector("tbody tr:not(.gt_group_heading_row)") as HTMLTableRowElement;
      expect(pinned(row.cells)).toEqual(["pinned", "+pin", "+pin"]);
      expect([padding(el, "start"), padding(el, "end")]).toEqual(["100px", "0px"]);
      expect(el.hasAttribute("data-gti-wide")).toBe(true);

      room = 600;
      el.search = "2";
      const shown = el.querySelector("tbody tr:not(.gt_group_heading_row):not([hidden])") as HTMLTableRowElement;
      expect(pinned(shown.cells)).toEqual(["pinned", "pinned+pin", "pinned+pin"]);
      expect(Array.from(shown.cells, end)).toEqual(["", "", "0px"]);
      expect([padding(el, "start"), padding(el, "end")]).toEqual(["200px", "100px"]);
    });

    it("pins the filler rows' cells as the data rows'", async () => {
      layout();
      // (A body as tall as its rows shown, for the filler rows' height)
      vi.spyOn(Element.prototype, "getBoundingClientRect").mockImplementation(function (this: Element) {
        const rows = this.tagName === "TBODY" ? Array.from(this.children).filter((tr) => !(tr as HTMLElement).hidden).length : 1;
        return new DOMRect(0, 0, 100, 20 * rows);
      });
      vi.spyOn(Element.prototype, "getClientRects").mockImplementation(() => [new DOMRect(0, 0, 100, 20)] as unknown as DOMRectList);
      // (Pages of 2 rows, the last with 1)
      const el = await mountTable([0, 1, 2, 3, 4], { layout: { responsive: "scroll" }, columns: both, pagination: { enabled: true } });
      el.page = 3;
      const filler = el.querySelector("tbody tr.gt-i-filler") as HTMLTableRowElement;
      expect(filler).not.toBeNull();
      expect(pinned(filler.cells)).toEqual(["pinned", "pinned+pin", "pinned+pin"]);
      expect(end(filler.cells[2] as Element)).toBe("0px");
    });
  });

  it("is GT's table without a responsive layout, and undoes it all when the table is replaced", async () => {
    layout();
    const plain = gtTable(GROUPED);
    const el = await mount(`<gt-table>${plain.html}${specScript(plain.spec)}</gt-table>`);
    expect(el.querySelector(".gt-i-scroller, .gt-i-pinned")).toBeNull();

    const replace = async (table: { html: string; spec: object }) => {
      el.remove();
      el.innerHTML = table.html + specScript(table.spec);
      document.body.append(el);
      await tick();
    };
    await replace(gtTable(GROUPED, { layout: { responsive: "scroll" } }));
    expect(el.hasAttribute("data-gti-wide")).toBe(true);
    await replace(plain);
    expect(el.hasAttribute("data-gti-wide")).toBe(false);
    expect(el.querySelector(".gt-i-shade, .gt-i-hint, .gt-i-pinned, .gt-i-inview, [role=region]")).toBeNull();
  });
});

describe("hiding columns", () => {
  const BOTH = { x: { hideable: true }, y: { hideable: true } };
  const SPANNED =
    `<tr class="gt_col_headings gt_spanner_row"><th class="gt_col_heading" rowspan="2"></th>` +
    `<th class="gt_column_spanner_outer" colspan="2" id="t-s"><span class="gt_column_spanner">Values</span></th></tr>` +
    `<tr class="gt_col_headings"><th class="gt_col_heading" id="t-x">x</th><th class="gt_col_heading" id="t-y">y</th></tr>`;
  const toggle = (el: GtTable) => el.querySelector<HTMLButtonElement>('.gt-i-bar [data-gti-bar="columns"]');
  const panel = (el: GtTable) => el.querySelector(".gt-i-columns") as HTMLElement;
  const boxes = (el: GtTable) => Array.from(panel(el).querySelectorAll<HTMLInputElement>("input[type=checkbox]"));
  const choose = (el: GtTable, i: number) => boxes(el)[i]?.click();
  const showAll = (el: GtTable) => panel(el).querySelector(".gt-i-info-button") as HTMLButtonElement;
  // The text of a row's cells shown
  const cells = (tr: HTMLTableRowElement | null) =>
    Array.from((tr as HTMLTableRowElement).cells, (cell) => (cell.hidden ? null : cell.textContent)).filter((text) => text !== null);

  // GROUPED, with a bar, `x` and `y` hideable (unless set otherwise), and the view events fired
  async function mountHide(options: TableOptions = {}) {
    const el = await mountTable(GROUPED, { columns: BOTH, ...options, controls: { bar: true, ...options.controls } });
    const views: ViewEventDetail[] = [];
    el.addEventListener(VIEW_EVENT, (event) => views.push((event as CustomEvent<ViewEventDetail>).detail));
    return { el, views };
  }

  it("hides and shows columns from a panel in the bar", async () => {
    const { el, views } = await mountHide();
    const button = toggle(el) as HTMLButtonElement;
    expect(button.getAttribute("aria-label")).toBe("Show or hide columns");
    expect(button.nextElementSibling).toBe(panel(el));
    expect(panel(el).getAttribute("aria-label")).toBe("Columns");
    expect(el.hideableColumns).toEqual(["x", "y"]);
    button.click();
    expect(panel(el).hidden).toBe(false);
    expect(Array.from(panel(el).querySelectorAll("label"), (label) => label.textContent)).toEqual(["x", "y"]);
    expect(boxes(el).map((box) => box.checked)).toEqual([true, true]);
    expect(showAll(el).getAttribute("aria-disabled")).toBe("true");

    choose(el, 0);
    expect(el.hiddenColumns).toEqual(["x"]);
    expect(header(el, "x").hidden).toBe(true);
    expect(cells(el.rowElement(0))).toEqual(["row_1", "b"]);
    expect(el.querySelector(".gt-i-live")?.textContent).toBe("x hidden");
    choose(el, 1);
    expect(cells(el.rowElement(0))).toEqual(["row_1"]);
    // (With a stub, every column can be hidden)
    expect(boxes(el).map((box) => [box.checked, box.disabled])).toEqual([
      [false, false],
      [false, false],
    ]);

    showAll(el).click();
    expect(el.hiddenColumns).toEqual([]);
    expect(cells(el.rowElement(0))).toEqual(["row_1", "20", "b"]);
    expect(boxes(el).map((box) => box.checked)).toEqual([true, true]);
    expect(showAll(el).getAttribute("aria-disabled")).toBe("true");
    expect(el.querySelector(".gt-i-live")?.textContent).toBe("Every column shown");
    expect(views.map((view) => view.hidden)).toEqual([["x"], ["x", "y"], []]);
  });

  it("has no panel without a column readers can hide, and a bar with one", async () => {
    const plain = await mountTable(GROUPED, { controls: { bar: true, search: true } });
    expect(toggle(plain)).toBeNull();
    expect(plain.hideableColumns).toEqual([]);
    expect(plain.querySelector('[data-gti-info="columns"]')).toBeNull();
    const { el } = await mountHide({ columns: { y: { hideable: true } } });
    expect(el.querySelector(".gt-i-bar")).not.toBeNull();
    expect(boxes(el)).toHaveLength(1);
  });

  it("narrows the cells across the columns shown, and hides a spanner over none", async () => {
    const { el } = await mountHide({
      thead: SPANNED,
      spanners: [{ id: "s", level: 1, columns: ["x", "y"], header: "t-s" }],
    });
    const spanner = header(el, "s");
    const heading = el.querySelector(".gt_group_heading") as HTMLTableCellElement;
    el.hiddenColumns = ["y"];
    expect([spanner.colSpan, spanner.hidden, heading.colSpan]).toEqual([1, false, 2]);
    el.hiddenColumns = ["x", "y"];
    expect([spanner.hidden, heading.colSpan]).toEqual([true, 1]);
    el.hiddenColumns = [];
    expect([spanner.colSpan, spanner.hidden, heading.colSpan]).toEqual([2, false, 3]);
    // (Each labelled after its spanners)
    expect(Array.from(panel(el).querySelectorAll("label"), (label) => label.textContent)).toEqual([
      "Values – x",
      "Values – y",
    ]);
  });

  it("hides columns set from code, without events, but not a column readers can't hide", async () => {
    const { el, views } = await mountHide({ columns: { y: { hideable: true } } });
    expect(el.hideableColumns).toEqual(["y"]);
    expect(() => {
      el.hiddenColumns = ["x"];
    }).toThrow(RangeError);
    expect(() => {
      el.hiddenColumns = ["row"];
    }).toThrow('"row" isn\'t a column that can be hidden');
    el.hiddenColumns = ["y", "y"];
    expect(el.hiddenColumns).toEqual(["y"]);
    expect(boxes(el)[0]?.checked).toBe(false);
    expect(views).toEqual([]);
  });

  it("leaves hidden columns out of the search, but keeps their filters", async () => {
    const { el } = await mountHide({
      controls: { search: true },
      filters: [{ column: "y", type: "facet", values: ["a", "b", "c"] }],
    });
    el.search = "c";
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
    el.hiddenColumns = ["y"];
    expect(visible(el)).toEqual(["grand:Max"]);
    // (The row saying that nothing matches spans the columns shown)
    const empty = el.querySelector(".gt-i-empty td") as HTMLTableCellElement;
    expect(empty.colSpan).toBe(2);
    el.hiddenColumns = ["x", "y"];
    expect(empty.colSpan).toBe(1);
    el.search = "";
    el.filter = { and: [{ col: "y", op: "in", value: ["c"] }] };
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
  });

  it("says in the info panel how many are hidden", async () => {
    const { el } = await mountHide();
    const item = el.querySelector('[data-gti-info="columns"]') as HTMLElement;
    const show = item.querySelector("button") as HTMLButtonElement;
    const open = () => (el.querySelector('.gt-i-bar [data-gti-bar="info"]') as HTMLButtonElement).click();
    open();
    expect(item.firstElementChild?.textContent).toBe("No columns hidden");
    expect(show.getAttribute("aria-disabled")).toBe("true");
    el.hiddenColumns = ["x"];
    expect(item.firstElementChild?.textContent).toBe("1 column hidden");
    el.hiddenColumns = ["x", "y"];
    expect(item.firstElementChild?.textContent).toBe("2 columns hidden");
    expect(show.getAttribute("aria-disabled")).toBe("false");
    show.click();
    expect(el.hiddenColumns).toEqual([]);
    expect(item.firstElementChild?.textContent).toBe("No columns hidden");
  });

  it("exports the columns shown, with code that drops the others", async () => {
    const { el } = await mountHide({
      export: { formats: ["csv", "code"], code: { backend: "polars", columns: {} } },
    });
    el.hiddenColumns = ["x"];
    expect(el.toCSV().split("\r\n").slice(0, 2)).toEqual([",row,y", "b,row_4,a"]);
    expect(el.toCode()).toContain('df.drop(["x"])');
    el.hiddenColumns = [];
    expect(el.toCSV().split("\r\n")[0]).toBe(",row,x,y");
  });

  it("pins the columns shown", async () => {
    vi.spyOn(Element.prototype, "scrollWidth", "get").mockReturnValue(2000);
    vi.spyOn(HTMLElement.prototype, "clientWidth", "get").mockReturnValue(600);
    vi.spyOn(Element.prototype, "getBoundingClientRect").mockReturnValue(new DOMRect(0, 0, 100, 20));
    const { el } = await mountHide({
      layout: { responsive: "scroll" },
      columns: { x: { pin: "start", hideable: true }, y: { pin: "end", hideable: true } },
    });
    const scroller = el.querySelector(".gt-i-scroller") as HTMLElement;
    const padding = () =>
      ["start", "end"].map((side) => scroller.style.getPropertyValue(`scroll-padding-inline-${side}`));
    expect(padding()).toEqual(["200px", "100px"]);
    el.hiddenColumns = ["x"];
    expect(padding()).toEqual(["100px", "100px"]);
    const y = el.rowElement(0)?.cells[2] as HTMLElement;
    expect(y.style.getPropertyValue("inset-inline-end")).toBe("0px");
    el.hiddenColumns = ["y"];
    expect(padding()).toEqual(["200px", "0px"]);
  });

  it("keeps a hidden column's width when the reader's widths are fixed", async () => {
    vi.spyOn(Element.prototype, "getBoundingClientRect").mockImplementation(function (this: Element) {
      return new DOMRect(0, 0, (this as HTMLElement).hidden ? 0 : 100, 20);
    });
    const { el } = await mountHide({ controls: { resizing: true } });
    el.hiddenColumns = ["x"];
    const handle = header(el, "y").querySelector(".gt-i-resizer") as HTMLElement;
    handle.dispatchEvent(new KeyboardEvent("keydown", { key: "ArrowRight", bubbles: true, cancelable: true }));
    const cols = Array.from(el.querySelectorAll<HTMLElement>("colgroup > col"));
    expect(cols.map((col) => [col.style.width, col.hidden])).toEqual([
      ["100px", false],
      ["100px", true],
      ["110px", false],
    ]);
    el.hiddenColumns = [];
    expect(cols.map((col) => [col.style.width, col.hidden])).toEqual([
      ["100px", false],
      ["100px", false],
      ["110px", false],
    ]);
  });

  describe("in the view", () => {
    const at = (url: string) => history.replaceState(null, "", url);
    beforeEach(() => at("/page"));
    afterEach(() => at("/"));

    it("starts with the columns the spec's view hides, which a reset shows again", async () => {
      const warn = vi.spyOn(console, "warn").mockImplementation(() => undefined);
      const { el } = await mountHide({
        columns: { y: { hideable: true } },
        view: { filter: null, sort: [], hidden: ["x", "y"] },
      });
      expect(el.hiddenColumns).toEqual(["y"]);
      expect(header(el, "y").hidden).toBe(true);
      expect(cells(el.rowElement(0))).toEqual(["row_1", "20"]);
      expect(warn).toHaveBeenCalledWith(
        '<gt-table>: the view\'s hidden column "x" is left out (it isn\'t one that can be hidden).',
      );
      el.hiddenColumns = [];
      el.resetView();
      expect(el.hiddenColumns).toEqual(["y"]);
    });

    it("keeps the columns hidden in the URL", async () => {
      at("/page?t1.hidden=y");
      const viewState = { url: true, storage: false, key: "t1", undo: false };
      const { el } = await mountHide({ viewState });
      expect(el.hiddenColumns).toEqual(["y"]);
      expect(header(el, "y").hidden).toBe(true);
      choose(el, 0);
      expect(location.search).toBe("?t1.hidden=x&t1.hidden=y");
      choose(el, 0);
      choose(el, 1);
      expect(location.search).toBe("");
      // (Once empty, for none of the author's)
      at("/page");
      const { el: authored } = await mountHide({ viewState, view: { filter: null, sort: [], hidden: ["x"] } });
      choose(authored, 0);
      expect(location.search).toBe("?t1.hidden=");
    });

    it("undoes each change, one by one", async () => {
      const { el } = await mountHide({ viewState: { url: false, storage: false, key: null, undo: true } });
      choose(el, 0);
      choose(el, 1);
      expect(el.undo()).toBe(true);
      expect(el.hiddenColumns).toEqual(["x"]);
      expect(el.undo()).toBe(true);
      expect(el.hiddenColumns).toEqual([]);
      expect(el.undo()).toBe(false);
      expect(el.redo()).toBe(true);
      expect(el.hiddenColumns).toEqual(["x"]);
      expect(boxes(el).map((box) => box.checked)).toEqual([false, true]);
    });
  });
});

describe("reordering columns", () => {
  const BOTH = { x: { reorderable: true }, y: { reorderable: true } };
  const toggle = (el: GtTable) => el.querySelector<HTMLButtonElement>('.gt-i-bar [data-gti-bar="columns"]');
  const panel = (el: GtTable) => el.querySelector(".gt-i-columns") as HTMLElement;
  const items = (el: GtTable) => Array.from(panel(el).querySelectorAll<HTMLElement>(".gt-i-column"));
  const names = (el: GtTable) => items(el).map((item) => item.textContent);
  const item = (el: GtTable, id: string) => panel(el).querySelector(`[data-gti-column="${id}"]`) as HTMLElement;
  const earlier = (el: GtTable, id: string) => item(el, id).querySelectorAll<HTMLButtonElement>(".gt-i-column-move")[0] as HTMLButtonElement;
  const later = (el: GtTable, id: string) => item(el, id).querySelectorAll<HTMLButtonElement>(".gt-i-column-move")[1] as HTMLButtonElement;
  const resetOrder = (el: GtTable) =>
    Array.from(panel(el).querySelectorAll<HTMLButtonElement>(".gt-i-info-button")).find((b) => b.textContent === "Reset order") as HTMLButtonElement;
  const live = (el: GtTable) => el.querySelector(".gt-i-live")?.textContent;
  const cells = (tr: HTMLTableRowElement | null) =>
    Array.from((tr as HTMLTableRowElement).cells, (cell) => (cell.hidden ? null : cell.textContent)).filter((text) => text !== null);
  const labels = (el: GtTable) => Array.from(el.querySelectorAll("thead th"), (th) => th.textContent);

  // GROUPED, with a bar, `x` and `y` reorderable (unless set otherwise), and the view events fired
  async function mountOrder(options: TableOptions = {}) {
    const el = await mountTable(GROUPED, { columns: BOTH, ...options, controls: { bar: true, ...options.controls } });
    const views: ViewEventDetail[] = [];
    el.addEventListener(VIEW_EVENT, (event) => views.push((event as CustomEvent<ViewEventDetail>).detail));
    return { el, views };
  }

  it("moves columns from a panel in the bar, keeping focus on the button", async () => {
    const { el, views } = await mountOrder();
    const button = toggle(el) as HTMLButtonElement;
    expect(button.getAttribute("aria-label")).toBe("Reorder columns");
    expect(panel(el).getAttribute("aria-label")).toBe("Columns");
    expect(el.reorderableColumns).toEqual(["x", "y"]);
    expect(el.columnOrder).toEqual(["x", "y"]);
    button.click();
    expect(names(el)).toEqual(["x", "y"]);
    // (No checkboxes, for columns readers can't hide)
    expect(panel(el).querySelector("input")).toBeNull();
    expect(earlier(el, "x").getAttribute("aria-label")).toBe("Move x earlier");
    expect(earlier(el, "x").getAttribute("aria-disabled")).toBe("true");
    expect(later(el, "x").getAttribute("aria-disabled")).toBe("false");
    expect(later(el, "y").getAttribute("aria-disabled")).toBe("true");
    expect(resetOrder(el).getAttribute("aria-disabled")).toBe("true");

    const move = later(el, "x");
    move.focus();
    move.click();
    expect(el.columnOrder).toEqual(["y", "x"]);
    expect(labels(el)).toEqual(["", "y", "x"]);
    expect(cells(el.rowElement(0))).toEqual(["row_1", "b", "20"]);
    expect(cells(el.querySelector<HTMLTableRowElement>(".gt_summary_row")?.closest("tr") ?? null)).toEqual(["Total", "-", "-"]);
    expect(names(el)).toEqual(["y", "x"]);
    expect(document.activeElement).toBe(move);
    expect(move.getAttribute("aria-disabled")).toBe("true");
    expect(live(el)).toBe("x moved after y");
    expect(resetOrder(el).getAttribute("aria-disabled")).toBe("false");
    // (Disabled, it does nothing)
    move.click();
    expect(views.map((view) => view.order)).toEqual([["y", "x"]]);

    earlier(el, "x").click();
    expect(el.columnOrder).toEqual(["x", "y"]);
    expect(live(el)).toBe("x moved before y");
    later(el, "x").click();
    resetOrder(el).click();
    expect(el.columnOrder).toEqual(["x", "y"]);
    expect(cells(el.rowElement(0))).toEqual(["row_1", "20", "b"]);
    expect(live(el)).toBe("Column order reset");
    expect(views.map((view) => view.order)).toEqual([["y", "x"], ["x", "y"], ["y", "x"], ["x", "y"]]);
  });

  it("moves a column with Alt and the arrow keys", async () => {
    const { el } = await mountOrder();
    toggle(el)?.click();
    const press = (target: Element, key: string, init: KeyboardEventInit = {}) => {
      const event = new KeyboardEvent("keydown", { key, bubbles: true, cancelable: true, ...init });
      target.dispatchEvent(event);
      return event;
    };
    expect(press(later(el, "y"), "ArrowUp", { altKey: true }).defaultPrevented).toBe(true);
    expect(el.columnOrder).toEqual(["y", "x"]);
    press(earlier(el, "y"), "ArrowDown");
    expect(el.columnOrder).toEqual(["y", "x"]);
    press(earlier(el, "y"), "ArrowDown", { altKey: true });
    expect(el.columnOrder).toEqual(["x", "y"]);
    expect(el.querySelector(".gt-i-info-shortcuts")?.textContent).toContain("Move a column, in the Columns panel");
  });

  it("moves a column dragged by its handle, or puts it back on Escape", async () => {
    const { el, views } = await mountOrder();
    toggle(el)?.click();
    // (Each item 20px tall, in the order shown)
    vi.spyOn(Element.prototype, "getBoundingClientRect").mockImplementation(function (this: Element) {
      const i = items(el).indexOf(this as HTMLElement);
      return new DOMRect(0, Math.max(0, i) * 20, 100, 20);
    });
    const grip = (id: string) => item(el, id).querySelector(".gt-i-column-grip") as HTMLElement;
    const pointer = (target: EventTarget, type: string, clientY: number) =>
      target.dispatchEvent(new PointerEvent(type, { bubbles: true, cancelable: true, pointerId: 1, button: 0, clientY }));

    pointer(grip("x"), "pointerdown", 10);
    expect(item(el, "x").hasAttribute("data-gti-dragging")).toBe(true);
    pointer(document, "pointermove", 35);
    expect(names(el)).toEqual(["y", "x"]);
    expect(el.columnOrder).toEqual(["x", "y"]);
    document.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape", bubbles: true }));
    expect(names(el)).toEqual(["x", "y"]);
    expect(item(el, "x").hasAttribute("data-gti-dragging")).toBe(false);
    expect(panel(el).hidden).toBe(false);
    expect(views).toEqual([]);

    pointer(grip("y"), "pointerdown", 30);
    pointer(document, "pointermove", 5);
    pointer(document, "pointerup", 5);
    expect(el.columnOrder).toEqual(["y", "x"]);
    expect(live(el)).toBe("y moved before x");
    expect(views.map((view) => view.order)).toEqual([["y", "x"]]);
    // (Dropped where it was, it doesn't move)
    pointer(grip("y"), "pointerdown", 5);
    pointer(document, "pointerup", 5);
    expect(views).toHaveLength(1);
  });

  it("sets the order from code, without events, but not of a column readers can't move", async () => {
    const { el, views } = await mountOrder();
    el.columnOrder = ["y"];
    expect(el.columnOrder).toEqual(["y", "x"]);
    expect(cells(el.rowElement(0))).toEqual(["row_1", "b", "20"]);
    expect(() => {
      el.columnOrder = ["row"];
    }).toThrow('"row" isn\'t a column that can be moved');
    expect(() => {
      el.columnOrder = ["x", "x"];
    }).toThrow('"x" is given twice');
    el.columnOrder = [];
    expect(el.columnOrder).toEqual(["x", "y"]);
    expect(views).toEqual([]);
  });

  it("moves a column only among those next to it under the same spanners and on the same side", async () => {
    const alone = await mountTable(GROUPED, { columns: { y: { reorderable: true } }, controls: { bar: true } });
    expect(alone.reorderableColumns).toEqual([]);
    expect(toggle(alone)).toBeNull();
    const pinned = await mountTable(GROUPED, { columns: { x: { reorderable: true, pin: "start" }, y: { reorderable: true } } });
    expect(pinned.reorderableColumns).toEqual([]);
    const split = await mountTable(GROUPED, {
      columns: BOTH,
      thead:
        `<tr class="gt_col_headings gt_spanner_row"><th class="gt_col_heading" rowspan="2"></th>` +
        `<th class="gt_column_spanner_outer" id="t-s"><span class="gt_column_spanner">S</span></th>` +
        `<th class="gt_column_spanner_outer"></th></tr>` +
        `<tr class="gt_col_headings"><th class="gt_col_heading" id="t-x">x</th><th class="gt_col_heading" id="t-y">y</th></tr>`,
      spanners: [{ id: "s", level: 1, columns: ["x"], header: "t-s" }],
    });
    expect(split.reorderableColumns).toEqual([]);
  });

  it("moves the cells under a spanner over the run, which stays", async () => {
    const { el } = await mountOrder({
      thead:
        `<tr class="gt_col_headings gt_spanner_row"><th class="gt_col_heading" rowspan="2"></th>` +
        `<th class="gt_column_spanner_outer" colspan="2" id="t-s"><span class="gt_column_spanner">Values</span></th></tr>` +
        `<tr class="gt_col_headings"><th class="gt_col_heading" id="t-x">x</th><th class="gt_col_heading" id="t-y">y</th></tr>`,
      spanners: [{ id: "s", level: 1, columns: ["x", "y"], header: "t-s" }],
      columns: { x: { reorderable: true, hideable: true }, y: { reorderable: true, hideable: true } },
    });
    expect(toggle(el)?.getAttribute("aria-label")).toBe("Show, hide or reorder columns");
    el.columnOrder = ["y", "x"];
    expect(labels(el)).toEqual(["", "Values", "y", "x"]);
    toggle(el)?.click();
    expect(Array.from(panel(el).querySelectorAll("label"), (label) => label.textContent)).toEqual(["Values – y", "Values – x"]);
    later(el, "y").click();
    expect(live(el)).toBe("Values – y moved after x");
    // (A column hidden is passed over, and can't be moved past)
    el.hiddenColumns = ["x"];
    expect([earlier(el, "y"), later(el, "y")].map((b) => b.getAttribute("aria-disabled"))).toEqual(["true", "true"]);
    expect(cells(el.rowElement(0))).toEqual(["row_1", "b"]);
    el.hiddenColumns = [];
    expect(cells(el.rowElement(0))).toEqual(["row_1", "20", "b"]);
    expect(header(el, "s").colSpan).toBe(2);
  });

  it("keeps the search, filters, sort and export on the columns as moved", async () => {
    const { el } = await mountOrder({
      controls: { search: true },
      filters: [{ column: "y", type: "facet", values: ["a", "b", "c"] }],
      export: { formats: ["csv"] },
      columns: { x: { reorderable: true }, y: { reorderable: true, searchable: false } },
    });
    el.columnOrder = ["y", "x"];
    el.search = "b";
    expect(visible(el)).toEqual(["grand:Max"]);
    el.search = "10";
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
    el.search = "";
    el.filter = { and: [{ col: "y", op: "in", value: ["c"] }] };
    expect(visible(el)).toEqual(["group:a", 2, "grand:Max"]);
    el.filter = null;
    el.sort = [{ column: "x", descending: false }];
    expect(cells(el.rowElement(1))).toEqual(["row_2", "a", "5"]);
    expect(el.toCSV().split("\r\n")[0]).toBe(",row,y,x");
    expect(el.toCSV().split("\r\n")[1]).toBe("b,row_1,b,20");
  });

  it("moves the cells with the groups as a column, and a selection column", async () => {
    const body: BodyRow[] = [{ group: "b" }, 3, 0, { group: "a" }, 1, 2];
    const el = await mountTable(body, {
      columns: BOTH,
      groupsAsColumn: true,
      controls: { selection: "multiple" },
      thead:
        `<tr class="gt_col_headings"><th class="gt_col_heading" colspan="2"></th>` +
        `<th class="gt_col_heading" id="t-x">x</th><th class="gt_col_heading" id="t-y">y</th></tr>`,
    });
    el.columnOrder = ["y", "x"];
    const first = el.querySelector(".gt_row_group_first") as HTMLTableRowElement;
    expect(cells(first).slice(1)).toEqual(["b", "row_4", "a", ""]);
    expect(cells(el.rowElement(0)).slice(1)).toEqual(["row_1", "b", "20"]);
    expect(labels(el).slice(-2)).toEqual(["y", "x"]);
    el.sort = [{ column: "y", descending: false }];
    expect(cells(el.querySelector(".gt_row_group_first")).slice(1)).toEqual(["b", "row_4", "a", ""]);
  });

  it("keeps the order in the view: reset, undone and restored from the URL", async () => {
    history.replaceState(null, "", "/page?t1.order=y&t1.order=nope");
    const warn = vi.spyOn(console, "warn").mockImplementation(() => {});
    const el = await mountTable(GROUPED, {
      columns: BOTH,
      viewState: { url: true, storage: false, key: "t1", undo: true },
      controls: { bar: true },
    });
    expect(el.columnOrder).toEqual(["y", "x"]);
    expect(warn.mock.calls.map(([message]) => String(message)).join()).toContain('"nope" is left out of its order');
    el.resetView();
    expect(el.columnOrder).toEqual(["x", "y"]);
    expect(location.search).toBe("");
    toggle(el)?.click();
    later(el, "x").click();
    expect(location.search).toBe("?t1.order=y&t1.order=x");
    (el.querySelector('.gt-i-bar [data-gti-bar="undo"]') as HTMLButtonElement).click();
    expect(el.columnOrder).toEqual(["x", "y"]);
    expect(location.search).toBe("");
    history.replaceState(null, "", "/");
  });
});
