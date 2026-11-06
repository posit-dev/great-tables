import { describe, expect, it } from "vitest";
import { normalizeSort, type SortKey, sortRows, toggleSort } from "../src/index";

const ranks = {
  x: [2, 0, 1, null, 2],
  y: [1, 0, 2, 0, 0],
};
const all = [0, 1, 2, 3, 4];
const asc = (column: string): SortKey => ({ column, descending: false });
const desc = (column: string): SortKey => ({ column, descending: true });

describe("sortRows()", () => {
  it("keeps the order without sort keys", () => {
    expect(sortRows([3, 1, 4], [], ranks)).toEqual([3, 1, 4]);
  });

  it("sorts ascending, missing values last and ties in order", () => {
    expect(sortRows(all, [asc("x")], ranks)).toEqual([1, 2, 0, 4, 3]);
    expect(sortRows([4, 3, 0], [asc("x")], ranks)).toEqual([4, 0, 3]);
  });

  it("sorts descending, missing values still last and ties still in order", () => {
    expect(sortRows(all, [desc("x")], ranks)).toEqual([0, 4, 2, 1, 3]);
    expect(sortRows([4, 3, 0], [desc("x")], ranks)).toEqual([4, 0, 3]);
  });

  it("sorts by several keys", () => {
    expect(sortRows(all, [asc("y"), desc("x")], ranks)).toEqual([4, 1, 3, 0, 2]);
    expect(sortRows(all, [desc("y"), asc("x")], ranks)).toEqual([2, 0, 1, 4, 3]);
  });

  it("sorts only the rows it's given", () => {
    expect(sortRows([3, 0, 4], [asc("x")], ranks)).toEqual([0, 4, 3]);
  });

  it("doesn't change its input", () => {
    const rows = [0, 1, 2];
    sortRows(rows, [desc("x")], ranks);
    expect(rows).toEqual([0, 1, 2]);
  });
});

describe("normalizeSort()", () => {
  it("fills in the direction", () => {
    expect(normalizeSort([{ column: "x" }, { column: "y", descending: true }], ranks)).toEqual([
      asc("x"),
      desc("y"),
    ]);
  });

  it("rejects columns that can't be sorted, or that repeat", () => {
    expect(() => normalizeSort([{ column: "z" }], ranks)).toThrow(/"z" isn't a sortable column/);
    expect(() => normalizeSort([{ column: "toString" }], ranks)).toThrow(RangeError);
    expect(() => normalizeSort([{ column: "x" }, { column: "x" }], ranks)).toThrow(/more than once/);
  });
});

describe("toggleSort()", () => {
  it("cycles the only sort column through ascending, descending and unsorted", () => {
    expect(toggleSort([], "x", false)).toEqual([asc("x")]);
    expect(toggleSort([asc("x")], "x", false)).toEqual([desc("x")]);
    expect(toggleSort([desc("x")], "x", false)).toEqual([]);
  });

  it("sorts by another column alone, ascending", () => {
    expect(toggleSort([desc("x")], "y", false)).toEqual([asc("y")]);
    expect(toggleSort([asc("x"), desc("y")], "y", false)).toEqual([asc("y")]);
    expect(toggleSort([asc("x"), desc("y")], "x", false)).toEqual([asc("x")]);
  });

  it("adds a column to the sort, or cycles it in place, when extending", () => {
    expect(toggleSort([], "x", true)).toEqual([asc("x")]);
    expect(toggleSort([desc("x")], "y", true)).toEqual([desc("x"), asc("y")]);
    expect(toggleSort([asc("x"), asc("y")], "x", true)).toEqual([desc("x"), asc("y")]);
    expect(toggleSort([desc("x"), asc("y")], "x", true)).toEqual([asc("y")]);
  });
});
