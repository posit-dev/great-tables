import { describe, expect, it } from "vitest";
import { RowData, type RowsPayload } from "../src/rows";
import { SpecError } from "../src/spec";

// Rows 3 and 4, then row 1, of a table of 5 rows of 2 columns (a stub with the row's key, and a
// column with HTML): with one `<tr>` tag for every row, a key by the row's index, and a column's
// values by index
const NUL = String.fromCharCode(0);
const PAYLOAD: RowsPayload = {
  rows: [3, 2, 1, 1],
  tr: { v: ["<tr>"] },
  key: { prefix: "t-stub-", offset: 1 },
  cells: [
    { tag: { v: [`<th id="${NUL}" class="gt_row gt_stub">`] }, html: { v: ["row_4", "row_5", "row_2"] } },
    { tag: { v: [`<td headers="${NUL} t-x" class="gt_row">`] }, html: { v: ["<b>a</b> &amp; b", "plain"], i: [0, 1, 0] } },
  ],
};

describe("RowData", () => {
  it("has the rows of its runs", () => {
    const data = new RowData(PAYLOAD, 5, 2, true);
    expect(data.rows).toEqual([3, 4, 1]);
    expect([0, 1, 2, 3, 4].map((row) => data.has(row))).toEqual([false, true, false, true, true]);
    expect(data.payload).toBe(PAYLOAD);
  });

  it("builds each row's HTML, with its key in its cells' tags", () => {
    const data = new RowData(PAYLOAD, 5, 2, true);
    expect(data.html([4, 1])).toBe(
      '<tr><th id="t-stub-5" class="gt_row gt_stub">row_5</th><td headers="t-stub-5 t-x" class="gt_row">plain</td></tr>' +
        '<tr><th id="t-stub-2" class="gt_row gt_stub">row_2</th><td headers="t-stub-2 t-x" class="gt_row"><b>a</b> &amp; b</td></tr>',
    );
    // (A key as a column, or none)
    const keyed = new RowData({ ...PAYLOAD, key: { v: ["k3", "k4", "k1"] } }, 5, 2, true);
    expect(keyed.html([1])).toContain('id="k1"');
    const unkeyed = new RowData({ ...PAYLOAD, key: null }, 5, 2, true);
    expect(unkeyed.html([3])).toContain('<th id="" class');
  });

  it("makes each column's cells once, a cell for each value, out of the page", () => {
    const data = new RowData(PAYLOAD, 5, 2, true);
    const cells = data.column(1);
    expect(cells.map((cell) => cell.innerHTML)).toEqual(["<b>a</b> &amp; b", "plain"]);
    expect(cells[0]?.ownerDocument).not.toBe(document);
    expect(data.column(1)).toBe(cells);
    expect(data.cell(1, 1)).toBe(cells[0]);
    expect(data.cell(4, 1)).toBe(cells[1]);
    expect(data.cell(0, 1)).toBeUndefined();
    expect(data.value(4, 1)).toBe(1);
    // (The rows with a value share its text, as the search has it)
    expect(data.cellTexts(3)[1]).toBe(data.cellTexts(1)[1]);
    expect(data.cellTexts(4)[0]).not.toBe(data.cellTexts(3)[0]);
  });

  it("makes a column's cells one by one if their HTML runs into each other's", () => {
    const payload = { ...PAYLOAD, cells: [PAYLOAD.cells[0], { tag: { v: ["<td>"] }, html: { v: ["<table><tr><td>in", "x &lt; y", "z"] } }] };
    const cells = new RowData(payload, 5, 2, true).column(1);
    expect(cells).toHaveLength(3);
    expect(cells[1]?.textContent).toBe("x < y");
    expect(cells[2]?.textContent).toBe("z");
  });

  it("parses rows' cells, as each row has them", () => {
    const made = new RowData(PAYLOAD, 5, 2, true).parse([1, 4]);
    expect([...made.keys()]).toEqual([1, 4]);
    expect(made.get(1)?.map((cell) => cell.id)).toEqual(["t-stub-2", ""]);
    expect(made.get(4)?.[1]?.textContent).toBe("plain");
  });

  it("takes its payload later, with its rows alone first", () => {
    const data = new RowData({ rows: PAYLOAD.rows }, 5, 2, false);
    expect(data.rows).toEqual([3, 4, 1]);
    expect(data.payload).toBeNull();
    expect(data.cell(3, 0)).toBeUndefined();
    data.take(PAYLOAD);
    expect(data.payload).toBe(PAYLOAD);
  });

  it.each([
    ["no runs", { ...PAYLOAD, rows: [3] }],
    ["a row the table hasn't", { ...PAYLOAD, rows: [4, 2] }],
    ["a row twice", { ...PAYLOAD, rows: [3, 2, 4, 1] }],
  ])("throws a SpecError with %s", (_, json) => {
    expect(() => new RowData(json, 5, 2, true)).toThrow(SpecError);
  });

  it.each([
    ["too few values", { ...PAYLOAD, tr: { v: ["<tr>", "<tr>"] } }],
    ["an index past its values", { ...PAYLOAD, cells: [PAYLOAD.cells[0], { tag: { v: ["<td>"] }, html: { v: ["a"], i: [0, 1, 0] } }] }],
    ["a cell for another table's columns", { ...PAYLOAD, cells: PAYLOAD.cells.slice(1) }],
    ["a key that isn't one", { ...PAYLOAD, key: { prefix: 1 } }],
  ])("throws a SpecError with a payload of %s", (_, json) => {
    expect(() => new RowData(json, 5, 2, true)).toThrow(SpecError);
  });
});
