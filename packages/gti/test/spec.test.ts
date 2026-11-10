import { describe, expect, it } from "vitest";
import { parseSpec, SPEC_VERSION, SpecError } from "../src/index";

const valid = {
  version: SPEC_VERSION,
  nrows: 2,
  columns: [{ id: "x", role: "data", kind: "number", align: "right", header: "t-x" }],
  spanners: [],
  stub: { columns: [], groups_as_column: false },
  groups: [],
  body: [{ group: "a" }, 1, 0, { summary: "Total", group: "a", side: "bottom" }],
  ranks: { x: [1, null] },
  striping: { stub: false, body: true },
  controls: { sorting: true, search: false, resizing: false, selection: null },
  pagination: { enabled: true, page_size: 10, page_sizes: [10, 25], size_select: false, info: true, type: "numbers" },
  display: { highlight: false, compact: false, wrap: true },
  layout: { height: null, responsive: "scroll" },
};

const pagination = (fields: object) => JSON.stringify({ ...valid, pagination: { ...valid.pagination, ...fields } });

const parse = (spec: object) => parseSpec(JSON.stringify(spec));

const filters = (list: unknown) => JSON.stringify({ ...valid, filters: list });

const view = (value: unknown) => JSON.stringify({ ...valid, view: value });

const queries = (list: unknown) => JSON.stringify({ ...valid, query_columns: list });

const exports = (value: unknown) => JSON.stringify({ ...valid, export: value });

const viewState = (value: unknown) => JSON.stringify({ ...valid, view_state: value });

const details = (value: unknown) => JSON.stringify({ ...valid, details: value });

const profiles = (list: unknown) => JSON.stringify({ ...valid, profiles: list });

describe("parseSpec()", () => {
  it("returns a valid spec as it is", () => {
    expect(parse(valid)).toEqual(valid);
  });

  it("takes a height", () => {
    const layout = { height: "min(60vh, 600px)", responsive: "scroll" };
    expect(parse({ ...valid, layout }).layout.height).toBe("min(60vh, 600px)");
  });

  it.each(["stack", "auto"])("takes a %s layout, with a stacking width or without one", (responsive) => {
    expect(parse({ ...valid, layout: { height: null, responsive } }).layout.responsive).toBe(responsive);
    const layout = { height: null, responsive, stack_below: 520.5 };
    expect(parse({ ...valid, layout }).layout).toEqual(layout);
  });

  it("takes a collapse layout", () => {
    expect(parse({ ...valid, layout: { height: null, responsive: "collapse" } }).layout.responsive).toBe("collapse");
  });

  it("takes no responsive layout", () => {
    expect(parse({ ...valid, layout: { height: null, responsive: null } }).layout.responsive).toBeNull();
  });

  it("takes what readers can do with a column, or its absence", () => {
    const column = { ...valid.columns[0], sortable: false, searchable: true, resizable: false };
    expect(parse({ ...valid, columns: [column] }).columns).toEqual([column]);
    expect(parse(valid).columns[0]?.sortable).toBeUndefined();
  });

  it("takes the side a column is pinned to, or its absence", () => {
    for (const pin of ["start", "end", null]) {
      expect(parse({ ...valid, columns: [{ ...valid.columns[0], pin }] }).columns[0]?.pin).toBe(pin);
    }
    expect(parse(valid).columns[0]?.pin).toBeUndefined();
  });

  it("takes a column's priority, or its absence", () => {
    for (const priority of [1, 3, null]) {
      expect(parse({ ...valid, columns: [{ ...valid.columns[0], priority }] }).columns[0]?.priority).toBe(priority);
    }
    expect(parse(valid).columns[0]?.priority).toBeUndefined();
  });

  it("takes a column's dtype and rows with missing values, or their absence", () => {
    const column = { ...valid.columns[0], dtype: "f64", missing: [0, 1] };
    expect(parse({ ...valid, columns: [column] }).columns).toEqual([column]);
    const none = { ...valid.columns[0], dtype: null, missing: null };
    expect(parse({ ...valid, columns: [none] }).columns).toEqual([none]);
    expect(parse(valid).columns[0]?.dtype).toBeUndefined();
  });

  it("takes row numbers and dimensions, or their absence", () => {
    const display = { ...valid.display, row_numbers: true, dimensions: false };
    expect(parse({ ...valid, display }).display).toEqual(display);
    expect(parse(valid).display.row_numbers).toBeUndefined();
  });

  it("takes the control bar, or its absence", () => {
    expect(parse({ ...valid, controls: { ...valid.controls, bar: true } }).controls.bar).toBe(true);
    expect(parse(valid).controls.bar).toBeUndefined();
  });

  it("takes filters, or their absence", () => {
    const list = [
      { column: "x", type: "range", values: [1.5, 3] },
      { column: "y", type: "text", values: null },
    ];
    expect(parse({ ...valid, filters: list }).filters).toEqual(list);
    // (And the rows whose value is missing)
    const missing = [{ column: "y", type: "text", values: null, missing: [1] }];
    expect(parse({ ...valid, filters: missing }).filters).toEqual(missing);
    expect(parse({ ...valid, filters: [{ column: "x", type: "facet", values: [true, "b"] }] }).filters).toHaveLength(1);
    expect(parse({ ...valid, filters: [{ column: "x", type: "date", values: ["2015-06-15", "2015-06-15T09:30:00.123456789"] }] }).filters).toHaveLength(1);
    expect(parse(valid).filters).toBeUndefined();
  });

  it("rejects a date filter with values that aren't dates", () => {
    for (const values of [[1, 2], ["2015-06-15", "June 15"], ["2015-02-30", null]]) {
      expect(() => parse({ ...valid, filters: [{ column: "x", type: "date", values }] })).toThrow(SpecError);
    }
  });

  it("takes a bool filter of booleans, and rejects one of other values", () => {
    expect(parse({ ...valid, filters: [{ column: "x", type: "bool", values: [false, true] }] }).filters).toHaveLength(1);
    for (const values of [[0, 1], ["false", "true"], [false, null]]) {
      expect(() => parse({ ...valid, filters: [{ column: "x", type: "bool", values }] })).toThrow(SpecError);
    }
  });

  it("takes the columns only for querying, or their absence", () => {
    const list = [
      { id: "y", kind: "string", label: "Why", texts: ["a", "b\nalt"] },
      { id: "z", kind: "number", label: "z", texts: null },
    ];
    expect(parse({ ...valid, query_columns: list }).query_columns).toEqual(list);
    expect(parse(valid).query_columns).toBeUndefined();
  });

  it("takes a view, or its absence", () => {
    const view = { filter: { and: [{ col: "x", op: "gte", value: 1 }] }, sort: [{ column: "x", descending: true }] };
    expect(parse({ ...valid, view }).view).toEqual(view);
    expect(parse({ ...valid, view: { filter: null, sort: [] } }).view).toEqual({ filter: null, sort: [] });
    expect(parse(valid).view).toBeUndefined();
  });

  it("takes an export, or its absence", () => {
    const value = { formats: ["csv", "clipboard"], filename: "towny" };
    expect(parse({ ...valid, export: value }).export).toEqual(value);
    expect(parse({ ...valid, export: { formats: [], filename: "table" } }).export?.formats).toEqual([]);
    expect(parse(valid).export).toBeUndefined();
    // (With what the view's code needs, or without it)
    const code = { backend: "pandas", columns: { x: { dtype: "float", nullable: false, literals: null } } };
    const withCode = { formats: ["code"], filename: "table", code };
    expect(parse({ ...valid, export: withCode }).export).toEqual(withCode);
    expect(parse({ ...valid, export: { ...value, code: null } }).export?.code).toBeNull();
  });

  it("takes where the view is kept, and whether it can be undone, or its absence", () => {
    const value = { url: true, storage: true, key: "towny", undo: false };
    expect(parse({ ...valid, view_state: value }).view_state).toEqual(value);
    // (Without a key, kept nowhere)
    expect(parse({ ...valid, view_state: { url: false, storage: false, key: null, undo: true } }).view_state?.key).toBeNull();
    expect(parse(valid).view_state).toBeUndefined();
  });

  it("takes the rows with details, or their absence", () => {
    expect(parse({ ...valid, details: [1, 0] }).details).toEqual([1, 0]);
    expect(parse({ ...valid, details: [] }).details).toEqual([]);
    expect(parse(valid).details).toBeUndefined();
  });

  it("takes the columns' profiles, or their absence", () => {
    const list = [
      { column: "x", plot: "histogram", values: [1.5, 3] },
      { column: "x", plot: "top", values: null },
    ];
    expect(parse({ ...valid, profiles: list }).profiles).toEqual(list);
    // (A histogram's dates and times are ISO 8601 text, and its values JSON can't hold, null)
    const dates = [{ column: "x", plot: "histogram", values: ["2015-06-15", null] }];
    expect(parse({ ...valid, profiles: dates }).profiles).toEqual(dates);
    expect(parse(valid).profiles).toBeUndefined();
  });

  it("ignores fields it doesn't know", () => {
    expect(parse({ ...valid, later: { anything: true } }).nrows).toBe(2);
  });

  it("accepts every kind of body row", () => {
    const body = [
      { grand_summary: "Max", side: "top" },
      { group: null },
      0,
      { summary: "Total", group: null, side: "top" },
      1,
    ];
    expect(parse({ ...valid, body }).body).toEqual(body);
  });

  it.each([
    ["isn't JSON", "{", /valid JSON/],
    ["isn't an object", "[1]", /no version/],
    ["has no version", JSON.stringify({ ...valid, version: undefined }), /no version/],
    ["has another version", JSON.stringify({ ...valid, version: 2 }), /version 2 isn't supported/],
    ["has a bad nrows", JSON.stringify({ ...valid, nrows: -1 }), /nrows/],
    ["has a bad nrows", JSON.stringify({ ...valid, nrows: 1.5 }), /nrows/],
    ["has no body", JSON.stringify({ ...valid, body: undefined }), /`body` must be an array/],
    ["has no ranks", JSON.stringify({ ...valid, ranks: [] }), /`ranks` must be objects/],
    ["has a row out of range", JSON.stringify({ ...valid, body: [0, 2] }), /`body\[1\]`/],
    ["has a negative row", JSON.stringify({ ...valid, body: [-1] }), /`body\[0\]`/],
    ["has an unknown row", JSON.stringify({ ...valid, body: [0, { other: 1 }] }), /`body\[1\]`/],
    ["has a row that isn't a number", JSON.stringify({ ...valid, body: ["0"] }), /`body\[0\]`/],
    ["has short ranks", JSON.stringify({ ...valid, ranks: { x: [1] } }), /`ranks.x`/],
    ["has no striping", JSON.stringify({ ...valid, striping: undefined }), /`striping`/],
    ["has a bad striping", JSON.stringify({ ...valid, striping: { stub: 1, body: true } }), /`striping`/],
    ["has no controls", JSON.stringify({ ...valid, controls: undefined }), /`controls`/],
    ["has a bad controls", JSON.stringify({ ...valid, controls: { sorting: true } }), /`controls`/],
    ["has a bad controls", JSON.stringify({ ...valid, controls: { sorting: 1, search: false } }), /`controls`/],
    [
      "has no resizing flag",
      JSON.stringify({ ...valid, controls: { sorting: true, search: false, selection: null } }),
      /`controls`/,
    ],
    [
      "has no selection mode",
      JSON.stringify({ ...valid, controls: { sorting: true, search: false, resizing: false } }),
      /`controls`/,
    ],
    [
      "has an unknown selection mode",
      JSON.stringify({ ...valid, controls: { ...valid.controls, selection: "all" } }),
      /`controls`/,
    ],
    [
      "has a control bar flag that isn't a boolean",
      JSON.stringify({ ...valid, controls: { ...valid.controls, bar: "yes" } }),
      /`controls.bar`/,
    ],
    ["has no pagination", JSON.stringify({ ...valid, pagination: undefined }), /`pagination`/],
    ["has a page size of 0", pagination({ page_size: 0 }), /`pagination`/],
    ["has a fractional page size", pagination({ page_size: 2.5 }), /`pagination`/],
    ["has a bad page sizes", pagination({ page_sizes: [10, -1] }), /`pagination`/],
    ["has page sizes that aren't an array", pagination({ page_sizes: 10 }), /`pagination`/],
    ["has an unknown pagination type", pagination({ type: "scroll" }), /`pagination`/],
    ["has a bad pagination flag", pagination({ size_select: "yes" }), /`pagination`/],
    ["has no pagination info flag", pagination({ info: undefined }), /`pagination`/],
    ["has no display", JSON.stringify({ ...valid, display: undefined }), /`display`/],
    ["has a bad display flag", JSON.stringify({ ...valid, display: { ...valid.display, wrap: 0 } }), /`display`/],
    ["has no highlight flag", JSON.stringify({ ...valid, display: { compact: false, wrap: true } }), /`display`/],
    ["has a row numbers flag that isn't one", JSON.stringify({ ...valid, display: { ...valid.display, row_numbers: 1 } }), /`display`/],
    ["has a dimensions flag that isn't one", JSON.stringify({ ...valid, display: { ...valid.display, dimensions: "yes" } }), /`display`/],
    ["has no layout", JSON.stringify({ ...valid, layout: undefined }), /`layout`/],
    ["has no height", JSON.stringify({ ...valid, layout: { responsive: null } }), /`layout`/],
    ["has a height that isn't a string", JSON.stringify({ ...valid, layout: { height: 400, responsive: null } }), /`layout`/],
    ["has an empty height", JSON.stringify({ ...valid, layout: { height: " ", responsive: null } }), /`layout`/],
    ["has no responsive layout", JSON.stringify({ ...valid, layout: { height: null } }), /`layout.responsive`/],
    ["has an unknown responsive layout", JSON.stringify({ ...valid, layout: { height: null, responsive: "fold" } }), /`layout.responsive`/],
    ...[0, -10, "420", null, true].map((below): [string, string, RegExp] => [
      `has a stacking width of ${JSON.stringify(below)}`,
      JSON.stringify({ ...valid, layout: { height: null, responsive: "stack", stack_below: below } }),
      /`layout.stack_below`/,
    ]),
    ["has filters that aren't an array", filters({ column: "x" }), /`filters`/],
    ["has a filter without a column", filters([{ type: "text", values: null }]), /`filters\[0\]`/],
    ["has a filter of an unknown type", filters([{ column: "x", type: "date", values: null }]), /`filters\[0\]`/],
    ["has a text filter with values", filters([{ column: "x", type: "text", values: [1] }]), /`filters\[0\]`/],
    ["has a facet without values", filters([{ column: "x", type: "facet", values: null }]), /`filters\[0\]`/],
    ["has a facet on a column without ranks", filters([{ column: "y", type: "facet", values: [1, 2] }]), /`filters\[0\]`/],
    ["has a range without a value for a rank", filters([{ column: "x", type: "range", values: [1] }]), /`filters\[0\]`/],
    ["has a facet with a value that isn't JSON's", filters([{ column: "x", type: "facet", values: [1, {}] }]), /`filters\[0\]`/],
    ["has a filter's missing rows that aren't an array", filters([{ column: "y", type: "text", values: null, missing: 1 }]), /`filters\[0\]\.missing`/],
    ["has a filter's missing row that isn't a data row", filters([{ column: "y", type: "text", values: null, missing: [0, 2] }]), /`filters\[0\]\.missing`/],
    ["has query columns that aren't an array", queries({ id: "y" }), /`query_columns`/],
    ["has a query column without an id", queries([{ kind: "string", label: "y", texts: null }]), /`query_columns`/],
    ["has a query column that's in the table", queries([{ id: "x", kind: "number", label: "x", texts: null }]), /`query_columns`/],
    ["has a query column without a label", queries([{ id: "y", kind: "string", texts: null }]), /`query_columns`/],
    ["has a query column with short texts", queries([{ id: "y", kind: "string", label: "y", texts: ["a"] }]), /`query_columns`/],
    ["has a query column with a text that isn't one", queries([{ id: "y", kind: "string", label: "y", texts: ["a", 1] }]), /`query_columns`/],
    ["has a view that isn't an object", view([]), /`view`/],
    ["has a view without a filter", view({ sort: [] }), /`view`/],
    ["has a view with a filter that isn't a query", view({ filter: [], sort: [] }), /`view`/],
    ["has a view without sort keys", view({ filter: null }), /`view`/],
    ["has a view with a bad sort key", view({ filter: null, sort: [{ column: "x" }] }), /`view`/],
    ["has a view with a sort key that's a name", view({ filter: null, sort: ["x"] }), /`view`/],
    ["has an export that isn't an object", exports(["csv"]), /`export`/],
    ["has an export without formats", exports({ filename: "table" }), /`export`/],
    ["has an export with a format it doesn't know", exports({ formats: ["xlsx"], filename: "table" }), /`export`/],
    ["has an export without a filename", exports({ formats: ["csv"] }), /`export`/],
    ["has an export with a filename that isn't text", exports({ formats: ["csv"], filename: 1 }), /`export`/],
    [
      "has an export with code for a library it doesn't know",
      exports({ formats: ["code"], filename: "table", code: { backend: "duckdb", columns: {} } }),
      /`export`/,
    ],
    [
      "has an export with code without columns",
      exports({ formats: ["code"], filename: "table", code: { backend: "polars" } }),
      /`export`/,
    ],
    ["has a column that isn't an object", JSON.stringify({ ...valid, columns: ["x"] }), /`columns\[0\]`/],
    [
      "has a column that's sortable with a string",
      JSON.stringify({ ...valid, columns: [{ ...valid.columns[0], sortable: "no" }] }),
      /`columns\[0\]`/,
    ],
    [
      "has a column that's resizable with a number",
      JSON.stringify({ ...valid, columns: [valid.columns[0], { ...valid.columns[0], resizable: 0 }] }),
      /`columns\[1\]`/,
    ],
    [
      "has a column pinned to a physical side",
      JSON.stringify({ ...valid, columns: [{ ...valid.columns[0], pin: "left" }] }),
      /`columns\[0\]`.*pinned/,
    ],
    ...[0, 1.5, "1", true].map((priority): [string, string, RegExp] => [
      `has a column with priority ${JSON.stringify(priority)}`,
      JSON.stringify({ ...valid, columns: [{ ...valid.columns[0], priority }] }),
      /`columns\[0\]`.*priority/,
    ]),
    ...[1, true, ["f64"]].map((dtype): [string, string, RegExp] => [
      `has a column with dtype ${JSON.stringify(dtype)}`,
      JSON.stringify({ ...valid, columns: [{ ...valid.columns[0], dtype }] }),
      /`columns\[0\]`.*dtype/,
    ]),
    ...[1, [2], [-1], [0.5], ["0"]].map((missing): [string, string, RegExp] => [
      `has a column with missing values in rows ${JSON.stringify(missing)}`,
      JSON.stringify({ ...valid, columns: [{ ...valid.columns[0], missing }] }),
      /`columns\[0\]`.*missing/,
    ]),
    [
      "has a column pinned with a boolean",
      JSON.stringify({ ...valid, columns: [{ ...valid.columns[0], pin: true }] }),
      /`columns\[0\]`/,
    ],
    ["has a view state that isn't an object", viewState(true), /`view_state`/],
    ["has a view state without storage", viewState({ url: true, key: "t", undo: false }), /`view_state`/],
    ["has a view state kept without a key", viewState({ url: true, storage: false, key: null, undo: false }), /`view_state`/],
    ["has a view state kept with an empty key", viewState({ url: false, storage: true, key: "", undo: false }), /`view_state`/],
    ["has a view state with a key that isn't text", viewState({ url: true, storage: false, key: 1, undo: false }), /`view_state`/],
    ["has a view state without undo", viewState({ url: true, storage: false, key: "t" }), /`view_state`/],
    ["has a view state with an undo that isn't a boolean", viewState({ url: false, storage: false, key: null, undo: 1 }), /`view_state`/],
    ["has details that aren't a list", details(1), /`details`/],
    ["has details for a row it doesn't have", details([0, 2]), /`details`/],
    ["has details for a row that isn't an index", details(["0"]), /`details`/],
    ["has profiles that aren't a list", profiles({}), /`profiles`/],
    ["has a profile of an unknown plot", profiles([{ column: "x", plot: "pie", values: null }]), /`profiles\[0\]`/],
    ["has a profile of a column without ranks", profiles([{ column: "y", plot: "top", values: null }]), /`profiles\[0\]`/],
    ["has a histogram without values", profiles([{ column: "x", plot: "histogram", values: null }]), /`profiles\[0\]`/],
    ["has a histogram without a value for every rank", profiles([{ column: "x", plot: "histogram", values: [1] }]), /`profiles\[0\]`/],
    ["has a histogram of booleans", profiles([{ column: "x", plot: "histogram", values: [true, false] }]), /`profiles\[0\]`/],
    ["has a profile of the most common values with values", profiles([{ column: "x", plot: "top", values: [1, 2] }]), /`profiles\[0\]`/],
  ])("rejects a spec that %s", (_, text, message) => {
    expect(() => parseSpec(text)).toThrow(SpecError);
    expect(() => parseSpec(text)).toThrow(message);
  });
});
