import { describe, expect, it, vi } from "vitest";
import { MISSING } from "../src/filter";
import { CellText } from "../src/search";
import { LocalSource, type RowQuery } from "../src/source";
import type { Spec } from "../src/spec";

// Five rows: a name, a number (one missing), a kind, and a note that isn't searchable, with a
// column only for querying (`code`)
const NAMES = ["apricot", "banana", "coconut", "durian", "fig"];
const NUMS = ["3", "1", "", "5", "2"];
const KINDS = ["one", "two", "one", "three", "two"];
const NOTES = ["sweet", "soft", "hard", "smelly", "sweet"];

const SPEC = {
  nrows: 5,
  columns: [
    { id: "name", role: "data", kind: "string", align: "left", header: "h-name" },
    { id: "num", role: "data", kind: "number", align: "right", header: "h-num" },
    { id: "kind", role: "data", kind: "string", align: "left", header: "h-kind" },
    { id: "note", role: "data", kind: "string", align: "left", header: "h-note", searchable: false },
  ],
  query_columns: [{ id: "code", kind: "string", label: "Code", texts: ["AP", "BA", "CO", "DU", "FI"] }],
  ranks: {
    name: [0, 1, 2, 3, 4],
    num: [2, 0, null, 3, 1],
    kind: [0, 2, 0, 1, 2],
    code: [0, 1, 2, 3, 4],
  },
  filters: [
    { column: "name", type: "text", values: null },
    { column: "num", type: "range", values: [1, 2, 3, 5] },
    { column: "kind", type: "facet", values: ["one", "three", "two"] },
    { column: "code", type: "text", values: null },
    // (Not one of its columns, and a second on a column)
    { column: "nope", type: "text", values: null },
    { column: "kind", type: "text", values: null },
  ],
  link: { group: "g", on: "kind", name: null, label: "Kind", keys: KINDS },
} as unknown as Spec;

const cellTexts = () =>
  NAMES.map((_, row) =>
    [NAMES, NUMS, KINDS, NOTES].map((column) => {
      const td = document.createElement("td");
      td.textContent = column[row] as string;
      return new CellText(td);
    }),
  );

const query = (parts: Partial<RowQuery> = {}): RowQuery => ({ search: "", hidden: [], filter: null, links: [], ...parts });

// The rows a query keeps, by number, and their count
function kept(source: LocalSource, parts: Partial<RowQuery>) {
  const { matched, count } = source.rows(query(parts));
  return { rows: Array.from(matched ?? [], (on, row) => (on === 1 ? [row] : [])).flat(), count };
}

describe("LocalSource", () => {
  it("keeps every row without a search, filters or linked selections", () => {
    expect(kept(new LocalSource(SPEC, cellTexts), {})).toEqual({ rows: [0, 1, 2, 3, 4], count: 5 });
  });

  it("searches the columns that are searchable and not hidden", () => {
    const source = new LocalSource(SPEC, cellTexts);
    expect(kept(source, { search: "an" })).toEqual({ rows: [1, 3], count: 2 });
    expect(kept(source, { search: "sweet" }).rows).toEqual([]);
    expect(kept(source, { search: "one" }).rows).toEqual([0, 2]);
    expect(kept(source, { search: "one", hidden: ["kind"] }).rows).toEqual([]);
    // (Each term in some cell: "co" in apricot's and coconut's names)
    expect(kept(source, { search: "co one" }).rows).toEqual([0, 2]);
    expect(kept(source, { search: "co two" }).rows).toEqual([]);
  });

  it("filters by a query, with its groups", () => {
    const source = new LocalSource(SPEC, cellTexts);
    expect(kept(source, { filter: { and: [{ col: "kind", op: "in", value: ["two"] }] } }).rows).toEqual([1, 4]);
    expect(kept(source, { filter: { and: [{ col: "num", op: "gte", value: 2 }, { col: "name", op: "contains", value: "an" }] } }).rows).toEqual([3]);
    expect(kept(source, { filter: { and: [{ col: "code", op: "contains", value: "u" }] } }).rows).toEqual([3]);
    expect(
      kept(source, { filter: { and: [{ or: [{ col: "num", op: "is_null" }, { col: "name", op: "contains", value: "fig" }] }] } }).rows,
    ).toEqual([2, 4]);
    // (Each query on its own: the one before is gone)
    expect(kept(source, { filter: null }).count).toBe(5);
  });

  it("keeps the rows with the keys of each linked selection", () => {
    const source = new LocalSource(SPEC, cellTexts);
    expect(kept(source, { links: [["one", "three"]] }).rows).toEqual([0, 2, 3]);
    expect(kept(source, { links: [["one", "three"], ["three", "two"]] }).rows).toEqual([3]);
  });

  it("makes the cells' text only when a query needs it", () => {
    const texts = vi.fn(cellTexts);
    const source = new LocalSource(SPEC, texts);
    kept(source, { filter: { and: [{ col: "kind", op: "in", value: ["one"] }] }, links: [["one"]] });
    kept(source, { filter: { and: [{ col: "num", op: "is_null" }] } });
    expect(texts).not.toHaveBeenCalled();
    kept(source, { search: "a" });
    kept(source, { filter: { and: [{ col: "name", op: "contains", value: "a" }] } });
    expect(texts).toHaveBeenCalledTimes(2);
  });

  it("counts the rows a query keeps of each of a facet's values", () => {
    const source = new LocalSource(SPEC, cellTexts);
    expect(source.facet(query(), "kind")).toEqual(new Map([[0, 2], [2, 2], [1, 1]]));
    expect(source.facet(query({ search: "an" }), "kind")).toEqual(new Map([[2, 1], [1, 1]]));
    // (A missing value's, as `MISSING`)
    expect(source.facet(query({ filter: { and: [{ col: "kind", op: "in", value: ["one"] }] } }), "num")).toEqual(
      new Map([[2, 1], [MISSING, 1]]),
    );
  });

  it("throws for a query on a column that can't be filtered", () => {
    const source = new LocalSource(SPEC, cellTexts);
    expect(() => source.rows(query({ filter: { and: [{ col: "nope", op: "contains", value: "a" }] } }))).toThrow(
      /"nope" isn't a column that can be filtered/,
    );
  });
});
