import { afterEach, describe, expect, it } from "vitest";
import { CELL, collapse, ROW, ROW_GROUP, TABLE, TableBorders } from "../src/borders";

const border = (width: number, style = "solid", color = "red", origin = CELL) => ({ width, style, color, origin });

describe("collapse()", () => {
  it("is none without borders, or with a hidden one", () => {
    expect(collapse([])).toBeNull();
    expect(collapse([undefined, border(0), border(3, "none")])).toBeNull();
    expect(collapse([border(3), border(1, "hidden", "red", TABLE)])).toBeNull();
  });

  it("takes the widest border", () => {
    expect(collapse([border(1, "double"), border(3, "dotted", "blue")])).toEqual({
      width: 3,
      style: "dotted",
      color: "blue",
    });
  });

  it("takes the strongest style of borders as wide", () => {
    expect(collapse([border(2, "dashed"), border(2, "solid", "blue"), border(2, "inset", "green")])).toEqual({
      width: 2,
      style: "solid",
      color: "blue",
    });
    expect(collapse([border(2, "solid"), border(2, "double", "blue")])?.style).toBe("double");
  });

  it("takes the border from the most specific origin, then the first", () => {
    const row = border(2, "solid", "row", ROW);
    const group = border(2, "solid", "group", ROW_GROUP);
    expect(collapse([group, row, border(2, "solid", "cell")])?.color).toBe("cell");
    expect(collapse([group, row])?.color).toBe("row");
    expect(collapse([border(2, "solid", "above"), border(2, "solid", "below")])?.color).toBe("above");
  });
});

describe("TableBorders", () => {
  afterEach(() => {
    document.body.innerHTML = "";
  });

  // A table of the rows given (with their borders inline)
  const make = (html: string) => {
    document.body.innerHTML = `<table>${html}</table>`;
    return document.querySelector("table") as HTMLTableElement;
  };
  const cells = (table: HTMLTableElement) => Array.from(table.querySelectorAll<HTMLTableCellElement>("th, td"));
  const drawn = (cell: HTMLTableCellElement) =>
    ["top", "right", "bottom", "left"].map((side) => cell.style.getPropertyValue(`border-${side}-style`));

  it("separates the table's borders", () => {
    const table = make(`<tbody><tr><td>a</td></tr></tbody>`);
    new TableBorders(table, () => false);
    expect(table.style.borderCollapse).toBe("separate");
    expect(table.style.borderSpacing).toBe("0");
  });

  it("draws each edge once, on the cell below it unless the row above holds it", () => {
    const table = make(
      `<thead><tr><th style="border-bottom: 2px solid red">h1</th><th>h2</th></tr></thead>` +
        `<tbody><tr><td style="border-top: 1px solid blue">a</td><td style="border-top: 1px solid blue">b</td></tr>` +
        `<tr><td style="border-top: 1px solid green">c</td><td>d</td></tr></tbody>`,
    );
    const borders = new TableBorders(table, (tr) => tr.parentElement?.tagName === "THEAD");
    borders.redraw();
    const [h1, h2, a, b, c, d] = cells(table) as HTMLTableCellElement[];
    // The header's bottom edge: the wider border under h1, the body's under h2; drawn by the header
    expect(borders.drawnBorder(h1 as HTMLTableCellElement, "bottom")).toEqual({ width: 2, style: "solid", color: "red" });
    expect(borders.drawnBorder(h2 as HTMLTableCellElement, "bottom")).toEqual({ width: 1, style: "solid", color: "blue" });
    expect(drawn(a as HTMLTableCellElement)[0]).toBe("none");
    expect(drawn(b as HTMLTableCellElement)[0]).toBe("none");
    // Between the body rows, the row below draws it
    expect(borders.drawnBorder(c as HTMLTableCellElement, "top")).toEqual({ width: 1, style: "solid", color: "green" });
    expect(borders.drawnBorder(a as HTMLTableCellElement, "bottom")).toBeNull();
    expect(borders.drawnBorder(d as HTMLTableCellElement, "top")).toBeNull();
  });

  it("draws the edges between columns on the cell after them, and the row's end on its last", () => {
    const table = make(
      `<tbody><tr><td style="border-right: 2px solid red">a</td><td style="border-left: 1px solid blue; border-right: 3px dashed green">b</td></tr></tbody>`,
    );
    const borders = new TableBorders(table, () => false);
    borders.redraw();
    const [a, b] = cells(table) as HTMLTableCellElement[];
    expect(borders.drawnBorder(a as HTMLTableCellElement, "right")).toBeNull();
    expect(borders.drawnBorder(b as HTMLTableCellElement, "left")).toEqual({ width: 2, style: "solid", color: "red" });
    expect(borders.drawnBorder(b as HTMLTableCellElement, "right")).toEqual({ width: 3, style: "dashed", color: "green" });
  });

  it("gives a cell spanning rows the edges along its side", () => {
    const table = make(
      `<tbody><tr><td rowspan="2" style="border-right: 1px solid red">g</td><td>a</td></tr>` +
        `<tr><td style="border-top: 2px solid blue">b</td></tr>` +
        `<tr><td style="border-top: 1px solid green">h</td><td>c</td></tr></tbody>`,
    );
    const borders = new TableBorders(table, () => false);
    borders.redraw();
    const [g, a, b, h] = cells(table) as HTMLTableCellElement[];
    expect(borders.drawnBorder(a as HTMLTableCellElement, "left")).toEqual({ width: 1, style: "solid", color: "red" });
    expect(borders.drawnBorder(b as HTMLTableCellElement, "top")).toEqual({ width: 2, style: "solid", color: "blue" });
    // (None across the merged cell)
    expect(borders.drawnBorder(g as HTMLTableCellElement, "bottom")).toBeNull();
    expect(borders.drawnBorder(h as HTMLTableCellElement, "top")).toEqual({ width: 1, style: "solid", color: "green" });
  });

  it("draws only the rows shown", () => {
    const table = make(
      `<tbody><tr><td>a</td></tr><tr hidden><td style="border-top: 2px solid red">b</td></tr>` +
        `<tr><td style="border-top: 1px solid blue">c</td></tr></tbody>`,
    );
    const borders = new TableBorders(table, () => false);
    borders.redraw();
    const [, b, c] = cells(table) as HTMLTableCellElement[];
    expect(borders.drawnBorder(b as HTMLTableCellElement, "top")).toBeNull();
    expect(borders.drawnBorder(c as HTMLTableCellElement, "top")).toEqual({ width: 1, style: "solid", color: "blue" });
    // Shown again, its edge is drawn
    (table.rows[1] as HTMLTableRowElement).hidden = false;
    borders.redraw();
    expect(borders.drawnBorder(b as HTMLTableCellElement, "top")).toEqual({ width: 2, style: "solid", color: "red" });
  });

  it("restores a row's own borders when told to forget them", () => {
    const table = make(`<tbody><tr><td>a</td></tr><tr><td style="border-top: 2px solid red">b</td></tr></tbody>`);
    const borders = new TableBorders(table, () => false);
    borders.redraw();
    const b = cells(table)[1] as HTMLTableCellElement;
    expect(b.style.getPropertyValue("border-bottom-style")).toBe("none");
    borders.forget(table.rows[1] as HTMLTableRowElement);
    expect(b.style.getPropertyValue("border-top-width")).toBe("2px");
    expect(b.style.getPropertyValue("border-bottom-style")).toBe("");
    expect(borders.drawnBorder(b, "top")).toBeNull();
  });
});
