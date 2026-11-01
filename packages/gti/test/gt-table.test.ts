import { afterEach, describe, expect, it, vi } from "vitest";
import {
  type BodyRow,
  type ControlsSpec,
  define,
  GtTable,
  PAGE_EVENT,
  type PageEventDetail,
  type PaginationSpec,
  SEARCH_EVENT,
  type SearchEventDetail,
  SORT_EVENT,
  type SortEventDetail,
  SPEC_VERSION,
  type StripingSpec,
  TAG_NAME,
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
  groupsAsColumn?: boolean;
  yLabel?: string;
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
    `<thead><tr class="gt_col_headings"><th class="gt_col_heading"></th>` +
    `<th class="gt_col_heading gt_right" id="t-x">x</th>` +
    `<th class="gt_col_heading gt_left" id="t-y">${options.yLabel ?? "y"}</th></tr></thead>`;
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
    ],
    spanners: [],
    stub: { columns: ["row"], groups_as_column: groupsAsColumn },
    groups,
    body: groupsAsColumn
      ? body.filter((entry) => typeof entry !== "object" || !("group" in entry) || "summary" in entry)
      : body,
    ranks: RANKS,
    striping,
    controls: { sorting: true, search: false, ...options.controls },
    pagination: {
      enabled: false,
      page_size: 2,
      page_sizes: [2, 4],
      size_select: false,
      info: true,
      type: "numbers",
      ...options.pagination,
    },
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
