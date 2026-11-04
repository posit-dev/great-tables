import { describe, expect, it } from "vitest";
import { ColumnFilter, dateKey, type FilterGroup, type FilterQuery, filterQuery, MISSING, setFilterQuery } from "../src/filter";
import { CellText } from "../src/search";

// Five rows: `x` is 20, 5, 10, missing, 20; `y` is "b", "a", "c", "a", "a"; `z` is text
const x = () => new ColumnFilter({ column: "x", type: "range", values: [5, 10, 20] }, 1, [2, 0, 1, null, 2]);
const y = () => new ColumnFilter({ column: "y", type: "facet", values: ["a", "b", "c"] }, 2, [1, 0, 2, 0, 0]);
const z = () => new ColumnFilter({ column: "z", type: "text", values: null }, 3, []);
// `d` is 2015-06-15, 2015-01-01, missing, 2015-12-31, 2015-06-15; `t` is dates and times
const d = () =>
  new ColumnFilter(
    { column: "d", type: "date", values: ["2015-01-01", "2015-06-15", "2015-12-31"] },
    4,
    [1, 0, null, 2, 1],
    null,
    "date",
  );
const t = () =>
  new ColumnFilter(
    { column: "t", type: "date", values: ["2015-06-14T23:59:59.999999999", "2015-06-15T00:00:00", "2015-06-15T09:30:00.5"] },
    5,
    [0, 1, 2, null, 2],
    null,
    "datetime",
  );

const cell = (text: string) => {
  const td = document.createElement("td");
  td.innerHTML = text;
  return new CellText(td);
};

const kept = (filter: ColumnFilter, cells: CellText[] = []) =>
  [0, 1, 2, 3, 4].filter((row) => filter.keeps(row, cells[row]));

describe("ColumnFilter", () => {
  it("keeps every row until it's set", () => {
    for (const filter of [x(), y(), z()]) {
      expect(filter.active).toBe(false);
      expect(kept(filter)).toEqual([0, 1, 2, 3, 4]);
      expect(filter.clauses()).toEqual([]);
    }
  });

  it("keeps the rows within a range's bounds, either of which can be open", () => {
    const filter = x();
    filter.min = 10;
    expect(filter.active).toBe(true);
    expect(kept(filter)).toEqual([0, 2, 4]);
    expect(filter.clauses()).toEqual([{ col: "x", op: "gte", value: 10 }]);
    filter.max = 10;
    expect(kept(filter)).toEqual([2]);
    expect(filter.clauses()).toEqual([
      { col: "x", op: "gte", value: 10 },
      { col: "x", op: "lte", value: 10 },
    ]);
    // (Never a missing value)
    filter.min = null;
    filter.max = 1000;
    expect(kept(filter)).toEqual([0, 1, 2, 4]);
  });

  it("keeps the rows with a facet's values chosen, a missing one too", () => {
    const filter = y();
    filter.chosen = new Set([2, 1]);
    expect(kept(filter)).toEqual([0, 2]);
    // (In the values' order)
    expect(filter.clauses()).toEqual([{ col: "y", op: "in", value: ["b", "c"] }]);

    const facet = new ColumnFilter({ column: "x", type: "facet", values: [5, 10, 20] }, 1, [2, 0, 1, null, 2]);
    facet.chosen = new Set([MISSING, 0]);
    expect(kept(facet)).toEqual([1, 3]);
    expect(facet.clauses()).toEqual([{ col: "x", op: "in", value: [5, null] }]);
  });

  it("keeps the rows whose cell has a text filter's text, ignoring case and accents", () => {
    const filter = z();
    const cells = ["Crème brûlée", "apple", "CREAM", "<b>cr</b>eme", ""].map(cell);
    filter.setText("  creme ");
    expect(filter.active).toBe(true);
    expect(kept(filter, cells)).toEqual([0, 3]);
    expect(filter.clauses()).toEqual([{ col: "z", op: "contains", value: "creme" }]);
    // (Blank text is no filter)
    filter.setText("   ");
    expect(filter.active).toBe(false);
    expect(kept(filter, cells)).toEqual([0, 1, 2, 3, 4]);
  });

  it("matches the texts of a column only for querying, which has no cells", () => {
    const texts = ["Crème brûlée", "apple", "CREAM", "pie\ncream", ""];
    const filter = new ColumnFilter({ column: "q", type: "text", values: null }, -1, [], texts);
    filter.setText("CREME");
    expect(kept(filter)).toEqual([0]);
    // (What a cell wouldn't show, too)
    filter.setText("cream");
    expect(kept(filter, ["x", "x", "x", "x", "x"].map(cell))).toEqual([2, 3]);
    expect(filter.clauses()).toEqual([{ col: "q", op: "contains", value: "cream" }]);
  });

  it("clears", () => {
    const filter = x();
    filter.min = 1;
    filter.clear();
    expect(filter.active).toBe(false);
  });
});

describe("dateKey()", () => {
  it("makes dates and times into text that sorts as they do", () => {
    expect(dateKey("2015-06-15")).toBe("2015-06-15T00:00:00.000000000");
    expect(dateKey("2015-06-15T09:30")).toBe("2015-06-15T09:30:00.000000000");
    expect(dateKey("2015-06-15T09:30:05.25")).toBe("2015-06-15T09:30:05.250000000");
    expect(dateKey("0001-01-01T23:59:59.123456789")).toBe("0001-01-01T23:59:59.123456789");
    expect(dateKey("2016-02-29")).not.toBeNull();
    expect(dateKey("2000-02-29")).not.toBeNull();
  });

  it.each([
    "",
    "2015-6-15",
    "2015-06-15 09:30",
    "2015-06-15T09",
    "2015-06-15T09:30Z",
    "2015-06-15T09:30:00+00:00",
    "2015-06-15T09:30:00.",
    "0000-01-01",
    "2015-00-01",
    "2015-13-01",
    "2015-04-31",
    "2015-02-29",
    "1900-02-29",
    "2015-06-15T24:00",
    "2015-06-15T09:60",
    "2015-06-15T09:30:60",
    "２０１５-06-15",
  ])("isn't made of %j", (text) => {
    expect(dateKey(text)).toBeNull();
  });

  it("takes as many digits of a second's fraction as asked", () => {
    expect(dateKey("2015-06-15T09:30:00.1234567", 6)).toBeNull();
    expect(dateKey("2015-06-15T09:30:00.123456", 6)).not.toBeNull();
  });
});

describe("a date filter", () => {
  it("keeps the rows within its bounds, either of which can be open", () => {
    const filter = d();
    expect(filter.active).toBe(false);
    expect(kept(filter)).toEqual([0, 1, 2, 3, 4]);
    filter.min = "2015-06-15";
    expect(filter.active).toBe(true);
    expect(kept(filter)).toEqual([0, 3, 4]);
    expect(filter.clauses()).toEqual([{ col: "d", op: "gte", value: "2015-06-15" }]);
    filter.max = "2015-06-15";
    expect(kept(filter)).toEqual([0, 4]);
    // (Never a missing value)
    filter.min = null;
    filter.max = "2016-01-01";
    expect(kept(filter)).toEqual([0, 1, 3, 4]);
  });

  it("compares dates and times as times, a date as its midnight", () => {
    const filter = t();
    filter.min = "2015-06-15";
    expect(kept(filter)).toEqual([1, 2, 4]);
    filter.min = "2015-06-15T00:00:00.000001";
    expect(kept(filter)).toEqual([2, 4]);
    filter.min = null;
    filter.max = "2015-06-15T09:30:00.5";
    expect(kept(filter)).toEqual([0, 1, 2, 4]);
    filter.max = "2015-06-15T09:30:00.499999";
    expect(kept(filter)).toEqual([0, 1]);
  });

  it("takes bounds that are dates, or for a column with times, dates and times", () => {
    expect(d().parse([{ col: "d", op: "gte", value: "2020-02-29" }]).min).toBe("2020-02-29");
    expect(t().parse([{ col: "t", op: "lte", value: "2015-06-15" }]).max).toBe("2015-06-15");
    expect(t().parse([{ col: "t", op: "lte", value: "2015-06-15T09:30:00.123456" }]).max).toBe(
      "2015-06-15T09:30:00.123456",
    );
    expect(() => d().parse([{ col: "d", op: "gte", value: "2015-06-15T09:30" }])).toThrow(
      '"2015-06-15T09:30" isn\'t a date ("YYYY-MM-DD"), for "d" (of dates, without times)',
    );
    expect(() => t().parse([{ col: "t", op: "gte", value: "2015-06-31" }])).toThrow(
      '"2015-06-31" isn\'t a date ("YYYY-MM-DD") or date and time ("YYYY-MM-DDTHH:MM:SS"), for "t"',
    );
    // (Python's times have six digits of a second's fraction)
    expect(() => t().parse([{ col: "t", op: "gte", value: "2015-06-15T09:30:00.1234567" }])).toThrow(RangeError);
    expect(() => d().parse([{ col: "d", op: "gte", value: 2015 }])).toThrow('"d" has a date filter');
    expect(() => d().parse([{ col: "d", op: "in", value: ["2015-06-15"] }])).toThrow('"d" has a date filter');
  });

  it("finds the value a bound is, as a date or time", () => {
    expect(d().dateRank("2015-06-15")).toBe(1);
    expect(d().dateRank("2015-06-16")).toBeUndefined();
    expect(t().dateRank("2015-06-15T00:00")).toBe(1);
    expect(t().dateRank("2015-06-15")).toBe(1);
    expect(t().dateRank("2015-06-15T09:30:00.500")).toBe(2);
  });
});

describe("a bool filter", () => {
  // (`b` is true, false, missing, true, false)
  const b = () => new ColumnFilter({ column: "b", type: "bool", values: [false, true] }, 6, [1, 0, null, 1, 0]);

  it("keeps the rows with the value chosen, or a missing one", () => {
    const filter = b();
    expect(filter.active).toBe(false);
    expect(filter.clauses()).toEqual([]);
    filter.chosen = new Set([1]);
    expect(filter.active).toBe(true);
    expect(kept(filter)).toEqual([0, 3]);
    expect(filter.clauses()).toEqual([{ col: "b", op: "in", value: [true] }]);
    filter.chosen = new Set([MISSING]);
    expect(kept(filter)).toEqual([2]);
    expect(filter.clauses()).toEqual([{ col: "b", op: "in", value: [null] }]);
  });

  it("takes one value", () => {
    expect(b().parse([{ col: "b", op: "in", value: [false] }]).chosen).toEqual(new Set([0]));
    expect(b().parse([{ col: "b", op: "in", value: [null] }]).chosen).toEqual(new Set([MISSING]));
    expect(() => b().parse([{ col: "b", op: "in", value: [true, null] }])).toThrow(
      'the "in" clause on "b" (a bool filter) can have only one value',
    );
    expect(() => b().parse([{ col: "b", op: "in", value: [] }])).toThrow("needs at least one value");
    expect(() => b().parse([{ col: "b", op: "in", value: [1] }])).toThrow('1 isn\'t a value of "b"');
    expect(() => b().parse([{ col: "b", op: "gte", value: 1 }])).toThrow('"b" has a bool filter');
  });
});

describe("filterQuery() and setFilterQuery()", () => {
  it("make and read the query of a set of filters", () => {
    const filters = [x(), y(), z()];
    expect(filterQuery(filters)).toBeNull();
    const query = {
      and: [
        { col: "y", op: "in" as const, value: ["a"] },
        { col: "x", op: "lte" as const, value: 15 },
        { col: "z", op: "contains" as const, value: "Fig" },
      ],
    };
    setFilterQuery(filters, query);
    const [range, facet, text] = filters as [ColumnFilter, ColumnFilter, ColumnFilter];
    expect(range.max).toBe(15);
    expect(Array.from(facet.chosen)).toEqual([0]);
    expect(text.text).toBe("Fig");
    // (In the filters' order)
    expect(filterQuery(filters)).toEqual({
      and: [
        { col: "x", op: "lte", value: 15 },
        { col: "y", op: "in", value: ["a"] },
        { col: "z", op: "contains", value: "Fig" },
      ],
    });
    setFilterQuery(filters, null);
    expect(filterQuery(filters)).toBeNull();
  });

  it("takes blank text, which keeps every row", () => {
    const filters = [z()];
    setFilterQuery(filters, { and: [{ col: "z", op: "contains", value: "  " }] });
    expect(filterQuery(filters)).toBeNull();
  });

  it("tells a facet's values apart by type", () => {
    const facet = new ColumnFilter({ column: "v", type: "facet", values: [1, "1", true] }, 1, [0, 1, 2]);
    setFilterQuery([facet], { and: [{ col: "v", op: "in", value: [1.0] }] });
    expect(Array.from(facet.chosen)).toEqual([0]);
    setFilterQuery([facet], { and: [{ col: "v", op: "in", value: ["1", true] }] });
    expect(Array.from(facet.chosen)).toEqual([1, 2]);
  });

  it("takes a missing value in a facet", () => {
    const filters = [y()];
    setFilterQuery(filters, { and: [{ col: "y", op: "in", value: [null, "c"] }] });
    expect(filterQuery(filters)).toEqual({ and: [{ col: "y", op: "in", value: ["c", null] }] });
  });

  // (Each after a good clause, which mustn't apply either)
  const good = { col: "y", op: "in", value: ["a"] };
  it.each([
    ["isn't an object", 3, /`\{and: \[\.\.\.parts\]\}`/],
    ["has no clauses", {}, /`\{and: \[\.\.\.parts\]\}`/],
    ["is on a column without a filter", { and: [good, { col: "w", op: "contains", value: "a" }] }, /"w" isn't a column/],
    ["has a clause that isn't one", { and: [good, null] }, /isn't a column/],
    ["has an op its filter can't have", { and: [good, { col: "x", op: "in", value: [5] }] }, /"x" has a range filter/],
    ["has a bound that isn't a number", { and: [good, { col: "x", op: "gte", value: "5" }] }, /"x" has a range filter/],
    ["has a value that isn't the column's", { and: [{ col: "x", op: "lte", value: 9 }, { col: "y", op: "in", value: ["d"] }] }, /"d" isn't a value of "y"/],
    ["has two clauses with an op", { and: [good, { col: "y", op: "in", value: ["b"] }] }, /"y" has more than one "in" clause/],
    ["has two bounds on one side", { and: [good, { col: "x", op: "gte", value: 1 }, { col: "x", op: "gte", value: 2 }] }, /"x" has more than one "gte" clause/],
    ["has two texts", { and: [good, { col: "z", op: "contains", value: "a" }, { col: "z", op: "contains", value: "b" }] }, /"z" has more than one "contains"/],
    ["has a choice of no values", { and: [{ col: "x", op: "lte", value: 9 }, { col: "y", op: "in", value: [] }] }, /"in" clause on "y" needs at least one value/],
    ["has text that isn't a string", { and: [good, { col: "z", op: "contains", value: 3 }] }, /"z" has a text filter/],
  ])("rejects a query that %s, changing nothing", (_, query, message) => {
    const filters = [x(), y(), z()];
    setFilterQuery(filters, { and: [{ col: "x", op: "gte", value: 1 }] });
    expect(() => setFilterQuery(filters, query as never)).toThrow(RangeError);
    expect(() => setFilterQuery(filters, query as never)).toThrow(message);
    expect(filterQuery(filters)).toEqual({ and: [{ col: "x", op: "gte", value: 1 }] });
  });
});

describe("a query's groups", () => {
  // (Rows' cells by the columns' indexes: `z` is "Fig", "apple", "", "fig jam", missing)
  const cells = ["Fig", "apple", "", "fig jam", null].map((text) => {
    const row: (CellText | undefined)[] = [];
    row[3] = text === null ? undefined : cell(text);
    return row;
  });
  const keptBy = (groups: FilterGroup[]) =>
    [0, 1, 2, 3, 4].filter((row) => groups.every((group) => group.keeps(row, cells[row] ?? [])));
  const set = (query: FilterQuery) => {
    const filters = [x(), y(), z()];
    return { filters, groups: setFilterQuery(filters, query) };
  };

  it("are kept apart from the filters' clauses, which come first", () => {
    const { filters, groups } = set({
      and: [
        { or: [{ col: "x", op: "gte", value: 20 }, { col: "y", op: "in", value: ["c"] }] },
        { col: "y", op: "in", value: ["a", "b"] },
        { not: { col: "z", op: "contains", value: "jam" } },
      ],
    });
    expect(filterQuery(filters)).toEqual({ and: [{ col: "y", op: "in", value: ["a", "b"] }] });
    expect(groups.map((group) => group.item)).toEqual([
      { or: [{ col: "x", op: "gte", value: 20 }, { col: "y", op: "in", value: ["c"] }] },
      { not: { col: "z", op: "contains", value: "jam" } },
    ]);
    expect(filterQuery(filters, groups)).toEqual({
      and: [
        { col: "y", op: "in", value: ["a", "b"] },
        { or: [{ col: "x", op: "gte", value: 20 }, { col: "y", op: "in", value: ["c"] }] },
        { not: { col: "z", op: "contains", value: "jam" } },
      ],
    });
    expect(groups.map((group) => [group.filters.map((filter) => filter.column), group.texts])).toEqual([
      [["x", "y"], false],
      [["z"], true],
    ]);
  });

  it("keep the rows any part, or every part, keeps; or that a part doesn't", () => {
    const or = set({ and: [{ or: [{ col: "x", op: "gte", value: 20 }, { col: "y", op: "in", value: ["c"] }] }] });
    expect(keptBy(or.groups)).toEqual([0, 2, 4]);
    const and = set({
      and: [{ or: [{ and: [{ col: "x", op: "lte", value: 10 }, { col: "y", op: "in", value: ["a"] }] }, { col: "z", op: "contains", value: "FIG" }] }],
    });
    expect(keptBy(and.groups)).toEqual([0, 1, 3]);
    // (A row whose value is missing, which a clause leaves out, is kept by `not`)
    const not = set({ and: [{ not: { col: "x", op: "gte", value: 10 } }] });
    expect(keptBy(not.groups)).toEqual([1, 3]);
    const notText = set({ and: [{ not: { col: "z", op: "contains", value: "fig" } }] });
    expect(keptBy(notText.groups)).toEqual([1, 2, 4]);
    const twice = set({ and: [{ not: { not: { col: "x", op: "gte", value: 10 } } }] });
    expect(keptBy(twice.groups)).toEqual([0, 2, 4]);
  });

  it("are written as the table has them: groups of one part as the part, and like groups spliced in", () => {
    const { filters, groups } = set({
      and: [
        { and: [{ col: "x", op: "gte", value: 5 }] },
        { or: [{ and: [{ col: "z", op: "contains", value: "fig" }] }] },
        { or: [{ col: "y", op: "in", value: [null, "c", "a", "c"] }, { or: [{ col: "x", op: "lte", value: 5 }, { or: [{ col: "x", op: "gte", value: 20 }] }] }] },
        { not: { and: [{ col: "x", op: "lte", value: 5 }, { and: [{ col: "y", op: "in", value: ["a"] }] }] } },
      ],
    });
    expect(filterQuery(filters, groups)).toEqual({
      and: [
        { col: "x", op: "gte", value: 5 },
        { col: "z", op: "contains", value: "fig" },
        {
          or: [
            { col: "y", op: "in", value: ["a", "c", null] },
            { col: "x", op: "lte", value: 5 },
            { col: "x", op: "gte", value: 20 },
          ],
        },
        { not: { and: [{ col: "x", op: "lte", value: 5 }, { col: "y", op: "in", value: ["a"] }] } },
      ],
    });
  });

  it.each([
    ["has an empty group", { and: [{ or: [] }] }, /"or" group needs a list of at least one part/],
    ["has a group that isn't a list", { and: [{ and: { col: "x" } }] }, /"and" group needs a list/],
    ["has a clause in a group on a column without a filter", { and: [{ not: { col: "w", op: "contains", value: "a" } }] }, /"w" isn't a column/],
    ["has a group with another key", { and: [{ or: [], and: [] }] }, /isn't a column/],
    ["has blank text in a group", { and: [{ not: { col: "z", op: "contains", value: " " } }] }, /"contains" clause on "z" needs text, in an "or" or a "not"/],
    ["has two clauses with an op in one and", { and: [{ or: [{ and: [{ col: "x", op: "gte", value: 1 }, { col: "x", op: "gte", value: 2 }] }, { col: "y", op: "in", value: ["a"] }] }] }, /"x" has more than one "gte" clause/],
    ["has two at the top, one in an and", { and: [{ col: "x", op: "gte", value: 1 }, { and: [{ col: "x", op: "gte", value: 2 }] }] }, /"x" has more than one "gte" clause/],
    ["has a bad value in a group", { and: [{ not: { col: "y", op: "in", value: ["d"] } }] }, /"d" isn't a value of "y"/],
  ])("reject a query that %s, changing nothing", (_, query, message) => {
    const filters = [x(), y(), z()];
    setFilterQuery(filters, { and: [{ col: "x", op: "gte", value: 1 }] });
    expect(() => setFilterQuery(filters, query as never)).toThrow(RangeError);
    expect(() => setFilterQuery(filters, query as never)).toThrow(message);
    expect(filterQuery(filters)).toEqual({ and: [{ col: "x", op: "gte", value: 1 }] });
  });

  it("can have the same clause in different parts", () => {
    const { groups } = set({
      and: [{ col: "x", op: "gte", value: 5 }, { or: [{ col: "x", op: "gte", value: 20 }, { not: { col: "x", op: "gte", value: 10 } }] }],
    });
    expect(keptBy(groups)).toEqual([0, 1, 3, 4]);
  });
});

describe("an is_null clause", () => {
  const keptBy = (groups: FilterGroup[]) => [0, 1, 2, 3, 4].filter((row) => groups.every((group) => group.keeps(row, [])));
  // (`n` is a float column's: 1, NaN, missing, 1, missing; NaN has a rank, as Polars has it)
  const n = () => new ColumnFilter({ column: "n", type: "range", values: [1, null], missing: [1, 2, 4] }, 4, [0, 1, null, 0, null]);
  const set = (query: FilterQuery) => {
    const filters = [x(), y(), z(), n()];
    return { filters, groups: setFilterQuery(filters, query) };
  };

  it("keeps the rows whose value is missing, as the spec has them", () => {
    expect(keptBy(set({ and: [{ col: "n", op: "is_null" }] }).groups)).toEqual([1, 2, 4]);
    expect(keptBy(set({ and: [{ not: { col: "n", op: "is_null" } }] }).groups)).toEqual([0, 3]);
    // (Without them, the rows without a rank)
    expect(keptBy(set({ and: [{ col: "x", op: "is_null" }] }).groups)).toEqual([3]);
    expect(keptBy(set({ and: [{ col: "y", op: "is_null" }] }).groups)).toEqual([]);
    expect(keptBy(set({ and: [{ col: "z", op: "is_null" }] }).groups)).toEqual([]);
    expect(keptBy(set({ and: [{ or: [{ col: "x", op: "is_null" }, { col: "n", op: "is_null" }] }] }).groups)).toEqual([1, 2, 3, 4]);
  });

  it("is kept as a group is, in the query's order, after the filters' clauses", () => {
    const { filters, groups } = set({
      and: [
        { col: "n", op: "is_null", value: "ignored" } as never,
        { not: { col: "x", op: "is_null" } },
        { col: "x", op: "gte", value: 5 },
        { and: [{ col: "y", op: "is_null" }] },
      ],
    });
    expect(filterQuery(filters)).toEqual({ and: [{ col: "x", op: "gte", value: 5 }] });
    expect(groups.map((group) => [group.item, group.filters.map((filter) => filter.column), group.texts])).toEqual([
      [{ col: "n", op: "is_null" }, ["n"], false],
      [{ not: { col: "x", op: "is_null" } }, ["x"], false],
      [{ col: "y", op: "is_null" }, ["y"], false],
    ]);
    expect(filterQuery(filters, groups)?.and).toHaveLength(4);
  });

  it.each([
    ["has two at the top", { and: [{ col: "x", op: "is_null" }, { and: [{ col: "x", op: "is_null" }] }] }, /"x" has more than one "is_null" clause/],
    ["has two in an and", { and: [{ not: { and: [{ col: "x", op: "is_null" }, { col: "x", op: "is_null" }] } }] }, /"x" has more than one "is_null" clause/],
    ["is on a column without a filter", { and: [{ col: "w", op: "is_null" }] }, /"w" isn't a column/],
  ])("makes a query that %s bad, changing nothing", (_, query, message) => {
    const filters = [x(), y(), z()];
    setFilterQuery(filters, { and: [{ col: "x", op: "gte", value: 1 }] });
    expect(() => setFilterQuery(filters, query as never)).toThrow(message);
    expect(filterQuery(filters)).toEqual({ and: [{ col: "x", op: "gte", value: 1 }] });
  });

  it("can be beside other clauses on its column", () => {
    const { groups } = set({ and: [{ not: { col: "x", op: "is_null" } }, { not: { col: "x", op: "is_null" } }, { col: "x", op: "lte", value: 5 }] });
    expect(groups).toHaveLength(2);
  });
});

describe("a matches clause", () => {
  // (`z` shows "St. Denis", "st. denis", "Côte", an image of a flag, and nothing; `q` is a column
  // only for querying)
  const cells = [cell("St. Denis"), cell("st. <b>denis</b>"), cell("Côte"), cell('Flag <img alt="Canada">'), cell("")];
  const q = () => new ColumnFilter({ column: "q", type: "text", values: null }, -1, [], ["ab", "AB", "", "a\nb", "b"]);
  const set = (query: FilterQuery) => {
    const filters = [x(), y(), z(), q()];
    return { filters, groups: setFilterQuery(filters, query) };
  };
  const keptBy = (groups: FilterGroup[]) =>
    [0, 1, 2, 3, 4].filter((row) => groups.every((group) => group.keeps(row, [undefined, undefined, undefined, cells[row]])));
  const matching = (value: string, col = "z") => keptBy(set({ and: [{ col, op: "matches", value }] }).groups);

  it("keeps the rows whose text has a match, with case, unless it has (?i)", () => {
    expect(matching("^St\\.")).toEqual([0]);
    expect(matching("(?i)^St\\.")).toEqual([0, 1]);
    expect(matching("Côte")).toEqual([2]);
    expect(matching("Cote")).toEqual([]);
    expect(matching("^$")).toEqual([4]);
  });

  it("matches the text that isn't shown after a line break, as a contains does", () => {
    expect(matching("^Flag \\nCanada$")).toEqual([3]);
    expect(matching("Canada")).toEqual([3]);
  });

  it("matches a column only for querying's texts", () => {
    expect(matching("^a", "q")).toEqual([0, 3]);
    expect(matching("(?i)^a.$", "q")).toEqual([0, 1]);
    expect(keptBy(set({ and: [{ not: { col: "q", op: "matches", value: "b$" } }] }).groups)).toEqual([1, 2]);
  });

  it("is kept as a group is, its pattern as checkPattern() writes it", () => {
    const { filters, groups } = set({
      and: [
        { col: "z", op: "matches", value: "a\\/b" },
        { col: "z", op: "contains", value: "x" },
        { or: [{ col: "q", op: "matches", value: "a" }, { col: "z", op: "is_null" }] },
      ],
    });
    expect(filterQuery(filters)).toEqual({ and: [{ col: "z", op: "contains", value: "x" }] });
    expect(groups.map((group) => [group.item, group.texts])).toEqual([
      [{ col: "z", op: "matches", value: "a/b" }, true],
      [{ or: [{ col: "q", op: "matches", value: "a" }, { col: "z", op: "is_null" }] }, false],
    ]);
  });

  it.each([
    ["has two at the top", { and: [{ col: "z", op: "matches", value: "a" }, { and: [{ col: "z", op: "matches", value: "b" }] }] }, /"z" has more than one "matches" clause/],
    ["has two in an and", { and: [{ not: { and: [{ col: "z", op: "matches", value: "a" }, { col: "z", op: "matches", value: "b" }] } }] }, /"z" has more than one "matches" clause/],
    ["is on a column without a text filter", { and: [{ col: "x", op: "matches", value: "1" }] }, /"x" has a range filter, which can't be/],
    ["has a pattern that isn't a string", { and: [{ col: "z", op: "matches", value: 1 }] }, /"z" has a text filter, which can't be/],
    ["has a pattern that can't be read", { and: [{ col: "z", op: "matches", value: "(?i)a(" }] }, 'the pattern of the "matches" clause on "z" can\'t be read: expected ")", at the end'],
    ["has a pattern that can't be read, in a group", { and: [{ not: { col: "z", op: "matches", value: "😀*)" } }] }, 'the pattern of the "matches" clause on "z" can\'t be read: ")" must close a "(" (or be escaped: "\\)"), at character 3'],
  ])("makes a query that %s bad, changing nothing", (_, query, message) => {
    const filters = [x(), y(), z()];
    setFilterQuery(filters, { and: [{ col: "x", op: "gte", value: 1 }] });
    expect(() => setFilterQuery(filters, query as never)).toThrow(RangeError);
    expect(() => setFilterQuery(filters, query as never)).toThrow(message);
    expect(filterQuery(filters)).toEqual({ and: [{ col: "x", op: "gte", value: 1 }] });
  });

  it("can be beside a matches clause in another part", () => {
    expect(set({ and: [{ col: "z", op: "matches", value: "a" }, { not: { col: "z", op: "matches", value: "a" } }] }).groups).toHaveLength(2);
  });
});
