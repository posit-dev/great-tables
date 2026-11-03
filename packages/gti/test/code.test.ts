import { describe, expect, it } from "vitest";
import { pyNumber, viewCode } from "../src/code";
import type { FilterQuery } from "../src/filter";
import type { SortKey } from "../src/sort";
import type { CodeBackend, CodeColumnSpec, CodeSpec, FilterSpec } from "../src/spec";

// (As tests/test_gti_query.py has them, for `query_code()`: a pandas frame of `name`, `num`, a
// float column with a missing value, `few`, and `flag`)
const FILTERS: FilterSpec[] = [
  { column: "name", type: "text", values: null },
  { column: "num", type: "range", values: [1.5, 2.0, 3.0] },
  { column: "few", type: "facet", values: ["x", "y"] },
  { column: "flag", type: "facet", values: [false, true] },
];

const column = (dtype: CodeColumnSpec["dtype"], literals: (string | null)[] | null = null, nullable = false) => ({
  dtype,
  nullable,
  literals,
});

const SPEC: CodeSpec = {
  backend: "pandas",
  columns: {
    name: column("string"),
    num: column("float"),
    few: column("string", ['"x"', '"y"']),
    flag: column("other", ["False", "True"]),
  },
};

const code = (
  query: FilterQuery | null,
  sort: SortKey[],
  backend: CodeBackend,
  { filters = FILTERS, spec = SPEC, hidden = [] }: { filters?: FilterSpec[]; spec?: CodeSpec; hidden?: string[] } = {},
) => viewCode(query, sort, hidden, filters, spec, backend);

describe("pyNumber", () => {
  it("writes whole numbers as integers", () => {
    expect(pyNumber(10000)).toBe("10000");
    expect(pyNumber(-3)).toBe("-3");
    expect(pyNumber(-0)).toBe("0");
    // (Every digit, as Python's `int()` of the double has them)
    expect(pyNumber(2 ** 60)).toBe("1152921504606846976");
    expect(pyNumber(1e30)).toBe("1000000000000000019884624838656");
  });

  it("writes other numbers as Python's `repr()` of a float does", () => {
    expect(pyNumber(1.5)).toBe("1.5");
    expect(pyNumber(-0.25)).toBe("-0.25");
    expect(pyNumber(0.1 + 0.2)).toBe("0.30000000000000004");
    expect(pyNumber(0.0001)).toBe("0.0001");
    expect(pyNumber(0.00012)).toBe("0.00012");
    expect(pyNumber(1e-5)).toBe("1e-05");
    expect(pyNumber(-1.5e-7)).toBe("-1.5e-07");
    expect(pyNumber(5e-324)).toBe("5e-324");
    expect(pyNumber(123456.789)).toBe("123456.789");
  });
});

describe("viewCode", () => {
  const query: FilterQuery = {
    and: [
      { col: "num", op: "gte", value: 1.5 },
      { col: "few", op: "in", value: ["x", null] },
    ],
  };
  const sort = [
    { column: "num", descending: true },
    { column: "name", descending: false },
  ];

  it("writes Polars code", () => {
    expect(code(query, sort, "polars")).toBe(
      "import polars as pl\n\n" +
        "df.filter(\n" +
        '    (pl.col("num") >= 1.5) & pl.col("num").is_finite(),\n' +
        '    pl.col("few").is_in(["x"]) | pl.col("few").is_null(),\n' +
        ').sort(["num", "name"], descending=[True, False], nulls_last=True, maintain_order=True)\n',
    );
  });

  it("writes pandas code", () => {
    expect(code(query, sort, "pandas")).toBe(
      "import numpy as np\n\n" +
        "df[\n" +
        '    ((df["num"] >= 1.5) & np.isfinite(df["num"]))\n' +
        '    & (df["few"].isin(["x"]) | df["few"].isna())\n' +
        '].sort_values(["num", "name"], ascending=[False, True], na_position="last", kind="stable")\n',
    );
    // (A term on its own isn't in parentheses)
    expect(code({ and: [{ col: "flag", op: "in", value: [true] }] }, [], "pandas")).toBe(
      'df[\n    df["flag"].isin([True])\n]\n',
    );
  });

  it("writes Narwhals code", () => {
    expect(code(query, sort, "narwhals")).toBe(
      "import narwhals as nw\n\n" +
        "(\n" +
        "    nw.from_native(df)\n" +
        "    .filter(\n" +
        '        (nw.col("num") >= 1.5) & nw.col("num").is_finite(),\n' +
        '        nw.col("few").is_in(["x"]) | nw.col("few").is_null(),\n' +
        "    )\n" +
        '    .with_row_index("_row")\n' +
        '    .with_columns((nw.col("num").is_nan() & ~nw.col("num").is_null()).fill_null(False).alias("_nan_num"))\n' +
        '    .sort(["_nan_num", "num", "name", "_row"], descending=[True, True, False, False], nulls_last=True)\n' +
        '    .drop(["_row", "_nan_num"])\n' +
        "    .to_native()\n" +
        ")\n",
    );
  });

  it("writes the whole table without a view", () => {
    expect(code(null, [], "polars")).toBe("import polars as pl\n\ndf\n");
    expect(code(null, [], "pandas")).toBe("df\n");
    expect(code({ and: [] }, [], "narwhals")).toBe("import narwhals as nw\n\n(\n    nw.from_native(df)\n    .to_native()\n)\n");
  });

  it("drops the columns hidden, after the filter and sort", () => {
    const hidden = ["few", 'a"b'];
    const one: FilterQuery = { and: [{ col: "num", op: "lte", value: 2 }] };
    const by = [{ column: "name", descending: false }];
    expect(code(one, by, "polars", { hidden })).toBe(
      "import polars as pl\n\n" +
        "df.filter(\n" +
        '    (pl.col("num") <= 2) & pl.col("num").is_finite(),\n' +
        ').sort(["name"], descending=[False], nulls_last=True, maintain_order=True).drop(["few", "a\\"b"])\n',
    );
    expect(code(null, [], "pandas", { hidden })).toBe('df.drop(columns=["few", "a\\"b"])\n');
    expect(code(null, by, "narwhals", { hidden })).toBe(
      "import narwhals as nw\n\n" +
        "(\n" +
        "    nw.from_native(df)\n" +
        '    .with_row_index("_row")\n' +
        '    .sort(["name", "_row"], descending=[False, False], nulls_last=True)\n' +
        '    .drop(["_row"])\n' +
        '    .drop(["few", "a\\"b"])\n' +
        "    .to_native()\n" +
        ")\n",
    );
  });

  it("matches text as the column's values, folded, and missing values", () => {
    const text: FilterQuery = {
      and: [
        { col: "name", op: "contains", value: "É" },
        { col: "few", op: "in", value: [null] },
      ],
    };
    expect(code(text, [], "polars")).toBe(
      "import polars as pl\n\n" +
        "df.filter(\n" +
        '    pl.col("name").str.to_lowercase().str.contains("e", literal=True),\n' +
        '    pl.col("few").is_null(),\n' +
        ")\n",
    );
    // (As text, for a column that isn't of strings)
    const other = { ...SPEC, columns: { ...SPEC.columns, name: column("other") } };
    const name: FilterQuery = { and: [{ col: "name", op: "contains", value: 'a"b' }] };
    expect(code(name, [], "pandas", { spec: other })).toBe(
      'df[\n    df["name"].astype(str).str.contains("a\\"b", case=False, regex=False, na=False)\n]\n',
    );
    expect(code(name, [], "narwhals", { spec: other })).toContain(
      'nw.col("name").cast(nw.String).str.to_lowercase().str.contains("a\\"b", literal=True),',
    );
    // (Blank text keeps every row)
    expect(code({ and: [{ col: "name", op: "contains", value: " " }] }, [], "pandas")).toBe("df\n");
  });

  it("writes a facet's values as Python, from the spec", () => {
    const filters: FilterSpec[] = [
      { column: "d", type: "facet", values: ["2020-01-02", "2021-03-04"] },
      { column: "c", type: "facet", values: ["lo", "hi"] },
      { column: "z", type: "facet", values: [-1.5, 0, 2] },
    ];
    const spec: CodeSpec = {
      backend: "polars",
      columns: {
        d: column("other", ["datetime.date(2020, 1, 2)", "datetime.date(2021, 3, 4)"]),
        c: column("categorical", ['"lo"', '"hi"']),
        z: column("float", ["-1.5", "0.0", "2.0"]),
      },
    };
    const query: FilterQuery = {
      and: [
        { col: "d", op: "in", value: ["2021-03-04"] },
        { col: "c", op: "in", value: ["hi", "lo"] },
        { col: "z", op: "in", value: [0, 2] },
      ],
    };
    expect(code(query, [], "polars", { filters, spec })).toBe(
      "import datetime\nimport polars as pl\n\n" +
        "df.filter(\n" +
        '    pl.col("d").is_in([datetime.date(2021, 3, 4)]),\n' +
        '    pl.col("c").cast(pl.String).is_in(["hi", "lo"]),\n' +
        '    pl.col("z").is_in([0.0, 2.0]),\n' +
        ")\n",
    );
    // (Narwhals has both zeros of floats, which PyArrow tells apart; pandas doesn't cast categories)
    expect(code(query, [], "narwhals", { filters, spec })).toContain('nw.col("z").is_in([2.0, -0.0, 0.0]),');
    expect(code(query, [], "pandas", { filters, spec })).toContain('(df["c"].isin(["hi", "lo"]))');
  });

  it("can't write a value the spec has no Python for", () => {
    const filters: FilterSpec[] = [{ column: "t", type: "facet", values: ["1 day, 0:00:00"] }];
    const spec: CodeSpec = { backend: "polars", columns: { t: column("other", [null]) } };
    const query: FilterQuery = { and: [{ col: "t", op: "in", value: ["1 day, 0:00:00"] }] };
    expect(() => code(query, [], "polars", { filters, spec })).toThrow(RangeError);
    // (But a missing value, it can)
    expect(code({ and: [{ col: "t", op: "in", value: [null] }] }, [], "polars", { filters, spec })).toContain(
      'pl.col("t").is_null(),',
    );
  });

  it("keeps pandas' nullable comparisons from being missing", () => {
    const spec = { ...SPEC, columns: { ...SPEC.columns, num: column("other", null, true) } };
    const query: FilterQuery = {
      and: [
        { col: "num", op: "gte", value: 1 },
        { col: "num", op: "lte", value: 2.5 },
      ],
    };
    expect(code(query, [], "pandas", { spec })).toBe(
      'df[\n    ((df["num"] >= 1).fillna(False))\n    & ((df["num"] <= 2.5).fillna(False))\n]\n',
    );
    // (Which Polars and Narwhals don't need)
    expect(code(query, [], "polars", { spec })).toContain('    pl.col("num") >= 1,\n    pl.col("num") <= 2.5,\n');
  });

  it("writes column names as Python strings", () => {
    const filters: FilterSpec[] = [{ column: 'Name "of" town', type: "text", values: null }];
    const spec: CodeSpec = { backend: "polars", columns: { 'Name "of" town': column("string") } };
    const query: FilterQuery = { and: [{ col: 'Name "of" town', op: "contains", value: "Côte" }] };
    expect(code(query, [{ column: 'Name "of" town', descending: false }], "polars", { filters, spec })).toBe(
      "import polars as pl\n\n" +
        "df.filter(\n" +
        '    pl.col("Name \\"of\\" town").str.to_lowercase().str.contains("cote", literal=True),\n' +
        ').sort(["Name \\"of\\" town"], descending=[False], nulls_last=True, maintain_order=True)\n',
    );
  });
});
