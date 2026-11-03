import { describe, expect, it } from "vitest";
import type { FilterQuery } from "../src/filter";
import {
  paramsText,
  readParams,
  readView,
  type View,
  type ViewLimits,
  type ViewParams,
  type ViewPart,
  viewParams,
  writeParams,
} from "../src/state";

const BASE: View = {
  filter: { and: [{ col: "population_2021", op: "gte", value: 10000 }] },
  sort: [{ column: "population_2021", descending: true }],
  search: "",
  page: 1,
  pageSize: 10,
  hidden: [],
  order: ["a", "b", "c", "d", "e f"],
};

const RANKS = { name: [0], status: [0], population_2021: [0], "-x": [0] };

const LIMITS: ViewLimits = { ranks: RANKS, search: true, sizes: [10, 25, 50], hideable: ["status", "area", "a b&c"], runs: [["a", "b", "c"], ["d", "e f"]] };

const FILTER: FilterQuery = {
  and: [
    { col: "status", op: "in", value: ["single-tier", null] },
    { col: "Name of town", op: "contains", value: 'Côte "St" & =' },
  ],
};

// A view kept as a URL's parameters (for table `towny`), and read back
function roundTrip(view: View, { base = BASE, limits = LIMITS }: { base?: View; limits?: ViewLimits } = {}) {
  const warnings: string[] = [];
  const query = writeParams("", "towny", viewParams(view, base));
  const params = readParams(query, "towny") ?? [];
  return { query, view: readView(params, base, limits, (message) => warnings.push(message)), warnings };
}

describe("viewParams", () => {
  it("has the parts that differ from the author's view", () => {
    expect(viewParams(BASE, BASE)).toEqual([]);
    expect(viewParams({ ...BASE, search: "ville", page: 3 }, BASE)).toEqual([
      ["search", "ville"],
      ["page", "3"],
    ]);
    expect(
      viewParams({ ...BASE, filter: null, sort: [{ column: "status", descending: false }, { column: "name", descending: true }], pageSize: 25 }, BASE),
    ).toEqual([
      ["filter", ""],
      ["sort", "status"],
      ["sort", "-name"],
      ["size", "25"],
    ]);
  });

  it("has no sort as one empty sort", () => {
    expect(viewParams({ ...BASE, sort: [] }, BASE)).toEqual([["sort", ""]]);
    expect(viewParams(BASE, { ...BASE, sort: [] })).toEqual([["sort", "-population_2021"]]);
  });

  it("has each hidden column, or no hidden column as one empty one", () => {
    expect(viewParams({ ...BASE, hidden: ["status", "area"] }, BASE)).toEqual([
      ["hidden", "status"],
      ["hidden", "area"],
    ]);
    expect(viewParams(BASE, { ...BASE, hidden: ["area"] })).toEqual([["hidden", ""]]);
    expect(viewParams({ ...BASE, hidden: ["area"] }, { ...BASE, hidden: ["area"] })).toEqual([]);
  });

  it("leaves out every row on one page", () => {
    expect(viewParams({ ...BASE, pageSize: null }, BASE)).toEqual([]);
  });
});

describe("parameters", () => {
  it("are named after the table, in a query string", () => {
    const params = viewParams({ ...BASE, search: "a b", page: 2 }, BASE);
    expect(paramsText(params, "towny")).toBe("towny.search=a+b&towny.page=2");
    expect(paramsText(params)).toBe("search=a+b&page=2");
    expect(writeParams("", "towny", [["filter", "population_2021 >= 10000"]])).toBe(
      "?towny.filter=population_2021+%3E%3D+10000",
    );
  });

  it("are read back, for the table's name only", () => {
    expect(readParams("?towny.search=a+b&towny.page=2&other.page=3&page=4&towny.x=1", "towny")).toEqual([
      ["search", "a b"],
      ["page", "2"],
    ]);
    expect(readParams("search=a%20b&page=2")).toEqual([
      ["search", "a b"],
      ["page", "2"],
    ]);
    expect(readParams("?other.page=3", "towny")).toBeNull();
    expect(readParams("", "towny")).toBeNull();
    // (A part without a value is empty; text that isn't encoded is read as it is)
    expect(readParams("?towny.filter&towny.search=%E2%9C%93%ZZ", "towny")).toEqual([
      ["filter", ""],
      ["search", "✓%ZZ"],
    ]);
  });

  it("replace the table's in the URL, keeping the others as they are", () => {
    const query = "?utm_source=a%20b&towny.page=2&flag&other.page=3&towny.search=x";
    expect(writeParams(query, "towny", [["sort", "name"]])).toBe("?utm_source=a%20b&flag&other.page=3&towny.sort=name");
    expect(writeParams(query, "towny", [])).toBe("?utm_source=a%20b&flag&other.page=3");
    expect(writeParams("?towny.page=2", "towny", [])).toBe("");
    // (A key with characters a query string has its own way of writing)
    expect(writeParams("", "a&b c", [["page", "2"]])).toBe("?a%26b+c.page=2");
    expect(readParams("?a%26b+c.page=2", "a&b c")).toEqual([["page", "2"]]);
  });
});

describe("readView", () => {
  it("reads back the view the parameters keep", () => {
    const view: View = {
      filter: FILTER,
      sort: [
        { column: "status", descending: false },
        { column: "name", descending: true },
      ],
      search: "  Côte & co ",
      page: 4,
      pageSize: 50,
      hidden: ["status", "a b&c"],
      order: ["b", "a", "c", "e f", "d"],
    };
    const { query, view: read, warnings } = roundTrip(view);
    expect(query).toContain("towny.sort=status&towny.sort=-name");
    expect(read).toEqual(view);
    expect(warnings).toEqual([]);
    // (A view that has none of the author's)
    expect(roundTrip({ ...view, filter: null, sort: [] }).view).toEqual({ ...view, filter: null, sort: [] });
  });

  it("has the author's view for the parts the parameters don't have", () => {
    const { query, view } = roundTrip(BASE);
    expect(query).toBe("");
    expect(view).toEqual(BASE);
    expect(view.sort).not.toBe(BASE.sort);
    expect(readView([["page", "2"]], BASE, LIMITS, () => {})).toEqual({ ...BASE, page: 2 });
  });

  it("reads the hidden columns, in column order", () => {
    const { query, view } = roundTrip({ ...BASE, hidden: ["status", "a b&c"] });
    expect(query).toBe("?towny.hidden=status&towny.hidden=a+b%26c");
    expect(readView([["hidden", "a b&c"], ["hidden", "status"]], BASE, LIMITS, () => {}).hidden).toEqual([
      "status",
      "a b&c",
    ]);
    // (Once empty, for none, over the author's)
    const base = { ...BASE, hidden: ["area"] };
    expect(roundTrip(BASE, { base }).view.hidden).toEqual([]);
    expect(readView([["page", "2"]], base, LIMITS, () => {}).hidden).toEqual(["area"]);
  });

  it("leaves out a column it can't hide, with a warning, keeping the others", () => {
    const warnings: string[] = [];
    const params: ViewParams = [
      ["hidden", "name"],
      ["hidden", "area"],
    ];
    const view = readView(params, BASE, LIMITS, (message) => warnings.push(message));
    expect(view).toEqual({ ...BASE, hidden: ["area"] });
    expect(warnings).toEqual(['the saved view\'s hidden column "name" is left out (it isn\'t one the reader can hide)']);
  });

  it("reads the columns' order, each run in it in that order, with the columns it leaves out after", () => {
    const { query, view } = roundTrip({ ...BASE, order: ["c", "a", "b", "e f", "d"] });
    expect(query).toBe("?towny.order=c&towny.order=a&towny.order=b&towny.order=e+f&towny.order=d");
    expect(view.order).toEqual(["c", "a", "b", "e f", "d"]);
    // (Only when it isn't the author's)
    expect(roundTrip(BASE).query).toBe("");
    const order = (...ids: string[]) => readView(ids.map((id) => ["order", id]), BASE, LIMITS, () => {}).order;
    expect(order("b")).toEqual(["b", "a", "c", "d", "e f"]);
    expect(order("e f", "c", "b")).toEqual(["c", "b", "a", "e f", "d"]);
    expect(order("c", "c", "a")).toEqual(["c", "a", "b", "d", "e f"]);
  });

  it("leaves out of the order a column readers can't move, with a warning", () => {
    const warnings: string[] = [];
    const params: ViewParams = [
      ["order", "status"],
      ["order", "c"],
    ];
    expect(readView(params, BASE, LIMITS, (message) => warnings.push(message)).order).toEqual(["c", "a", "b", "d", "e f"]);
    expect(warnings).toEqual([
      'the saved view\'s column "status" is left out of its order (it isn\'t one the reader can move)',
    ]);
  });

  it("reads a column that starts with - as sorted", () => {
    expect(roundTrip({ ...BASE, sort: [{ column: "-x", descending: true }] }).view.sort).toEqual([{ column: "-x", descending: true }]);
    expect(roundTrip({ ...BASE, sort: [{ column: "-x", descending: false }] }).view.sort).toEqual([{ column: "-x", descending: false }]);
  });

  it.each<[ViewPart, ViewParams, string]>([
    ["filter", [["filter", "population_2021 >="]], "expected a number"],
    ["sort", [["sort", "name"], ["sort", "area"]], '"area" isn\'t a sortable column'],
    ["sort", [["sort", "-name"], ["sort", "name"]], '"name" is in the sort more than once'],
    ["page", [["page", "0"]], '"0" isn\'t a page number'],
    ["page", [["page", "2.5"]], '"2.5" isn\'t a page number'],
    ["size", [["size", "20"]], '"20" isn\'t a page size the table has'],
  ])("leaves out a %s it can't have, with a warning", (part, params, why) => {
    const warnings: string[] = [];
    const view = readView(
      [...params, ["search", "kept"]],
      BASE,
      LIMITS,
      (message) => warnings.push(message),
    );
    expect(view).toEqual({ ...BASE, search: "kept" });
    expect(warnings).toHaveLength(1);
    expect(warnings[0]).toMatch(`the saved view's ${part} is left out (`);
    expect(warnings[0]).toContain(why);
  });

  it("leaves out what the table doesn't let readers change", () => {
    const warnings: string[] = [];
    const params = readParams("sort=name&search=x&page=2&size=25") ?? [];
    const view = readView(params, BASE, { ranks: null, search: false, sizes: [], hideable: [], runs: [] }, (message) => warnings.push(message));
    expect(view).toEqual(BASE);
    expect(warnings).toEqual([
      "the saved view's search is left out (the table can't be searched)",
      "the saved view's page is left out (the table has no pages)",
      "the saved view's size is left out (the table has no pages)",
      "the saved view's sort is left out (the table can't be sorted)",
    ]);
  });
});
