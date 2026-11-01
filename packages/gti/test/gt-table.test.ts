import { afterEach, describe, expect, it, vi } from "vitest";
import {
  type BodyRow,
  define,
  GtTable,
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
  for (const entry of body) {
    if (typeof entry === "object" && "group" in entry && !("summary" in entry)) {
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
    groups: [],
    body: groupsAsColumn
      ? body.filter((entry) => typeof entry !== "object" || !("group" in entry) || "summary" in entry)
      : body,
    ranks: RANKS,
    striping,
  };
  return { html, spec };
}

async function mountTable(body: BodyRow[] = GROUPED, options: TableOptions = {}) {
  const { html, spec } = gtTable(body, options);
  return mount(`<gt-table>${html}${specScript(spec)}</gt-table>`);
}

/** The body as shown: data row indices, and labels for the structural rows. */
function shown(el: GtTable): (number | string)[] {
  return Array.from(el.querySelectorAll<HTMLTableRowElement>("tbody > tr")).map((tr) => {
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
