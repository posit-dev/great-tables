/**
 * Rows as data: the data rows a large table of pages has past its first page, which its HTML
 * leaves out, for the table to build as they're shown (see `off_page_rows()` in Great Tables).
 * They're in a `<script type="application/json" data-gti-rows>` in the element, as columns (see
 * `RowsPayload`); or, with `data-gti-rows-src`, the script has only which rows they are, and the
 * rest is in a JSON file at that URL.
 */

import { CellText } from "./search";
import { SpecError } from "./spec";

/**
 * Values, one for each row, as a column: its distinct values (`v`) and each row's index into
 * them (`i`); or, without `i`, each row's value, or one value for every row.
 */
export interface RowsColumn {
  v: string[];
  i?: number[];
}

/** The rows, as Great Tables' `rows_payload()` writes them. */
export interface RowsPayload {
  /** The rows (by index in the data), in the body's order, as runs: each one's first row and how many there are. */
  rows: number[];
  /** Their `<tr>` tags. */
  tr: RowsColumn;
  /**
   * The ID of each row's cells (its stub's), which their tags have as `\u0000`: as a prefix
   * before the row's index plus an offset, as a column, or `null` without one.
   */
  key: { prefix: string; offset: number } | RowsColumn | null;
  /** Each cell's start tag and its HTML, in the order of the spec's columns. */
  cells: { tag: RowsColumn; html: RowsColumn }[];
}

const isColumn = (x: unknown, n: number): x is RowsColumn => {
  const { v, i } = (x ?? {}) as Partial<RowsColumn>;
  return (
    Array.isArray(v) &&
    v.every((value) => typeof value === "string") &&
    (i === undefined
      ? v.length === n || v.length === 1
      : Array.isArray(i) && i.length === n && i.every((k) => Number.isInteger(k) && k >= 0 && k < v.length))
  );
};

// A row's value in a column (by the row's place among the rows), as an index into its values
const at = (column: RowsColumn, j: number): number => column.i?.[j] ?? (column.v.length === 1 ? 0 : j);

const valueOf = (column: RowsColumn, j: number): string => column.v[at(column, j)] as string;

export class RowData {
  /** The rows (by index in the data), in the body's order. */
  readonly rows: number[] = [];
  /** The payload, once it's come (from `data-gti-rows-src`). */
  payload: RowsPayload | null = null;
  // Each row's place among the rows (by its index in the data), or -1
  private readonly places: Int32Array;
  // Each column's cells, one for each of its values (see `column()`), and their text
  private readonly made: Element[][] = [];
  private readonly texts: CellText[][] = [];
  private doc: Document | null = null;

  /**
   * The rows of `json` (a payload, or, with `whole` false, its `rows` alone), of a table of
   * `nrows` data rows and `ncells` columns.
   *
   * @throws {SpecError} if they aren't rows of the table.
   */
  constructor(
    json: unknown,
    nrows: number,
    private readonly ncells: number,
    whole: boolean,
  ) {
    const runs = (json as Partial<RowsPayload> | null)?.rows;
    this.places = new Int32Array(nrows).fill(-1);
    if (!Array.isArray(runs) || runs.length % 2 !== 0) {
      throw new SpecError("the rows as data have no runs");
    }
    for (let r = 0; r < runs.length; r += 2) {
      const [first, count] = runs.slice(r, r + 2) as number[];
      for (let row = first as number; row < (first as number) + (count as number); row++) {
        if (!Number.isInteger(row) || this.places[row] !== -1) {
          throw new SpecError(`the rows as data have a row ${row} the table can't have`);
        }
        this.places[row] = this.rows.push(row) - 1;
      }
    }
    if (whole) {
      this.take(json);
    }
  }

  /**
   * Take the payload, with each row's cells.
   *
   * @throws {SpecError} if it isn't one for the rows.
   */
  take(json: unknown): void {
    const n = this.rows.length;
    const { tr, key, cells } = (json ?? {}) as RowsPayload;
    if (
      !isColumn(tr, n) ||
      !(key === null || isColumn(key, n) || (typeof key?.prefix === "string" && Number.isInteger(key.offset))) ||
      !Array.isArray(cells) ||
      cells.length !== this.ncells ||
      !cells.every((cell) => isColumn(cell?.tag, n) && isColumn(cell.html, n))
    ) {
      throw new SpecError("the rows as data aren't the table's");
    }
    this.payload = json as RowsPayload;
  }

  /** Whether a row is one of the rows. */
  has(row: number): boolean {
    return (this.places[row] ?? -1) >= 0;
  }

  /** The HTML of rows (once the payload has come), a `<tr>` each. */
  html(rows: number[]): string {
    const { tr, key, cells } = this.payload as RowsPayload;
    return rows
      .map((row) => {
        const j = this.places[row] as number;
        const id = key === null ? "" : "prefix" in key ? `${key.prefix}${row + key.offset}` : valueOf(key, j);
        const own = cells.map(({ tag, html }) => {
          const start = valueOf(tag, j).replace(/\0/g, () => id);
          return `${start}${valueOf(html, j)}</${start.slice(1, 3)}>`;
        });
        return `${valueOf(tr, j)}${own.join("")}</tr>`;
      })
      .join("");
  }

  /** The index of a row's value in a column's values (by the column's index in the spec). */
  value(row: number, k: number): number {
    return at((this.payload as RowsPayload).cells[k]?.html as RowsColumn, this.places[row] as number);
  }

  /** A row's cell in a column (by its index in the spec), for its contents (see `column()`). */
  cell(row: number, k: number): Element | undefined {
    const j = this.places[row] ?? -1;
    const column = this.payload?.cells[k]?.html;
    return j < 0 || column === undefined ? undefined : this.column(k)[at(column, j)];
  }

  /** The searchable text of a row's cells, each shared by the rows with its value. */
  cellTexts(row: number): CellText[] {
    const j = this.places[row] as number;
    return (this.payload as RowsPayload).cells.map(({ html }, k) => {
      const v = at(html, j);
      const texts = (this.texts[k] ??= []);
      return (texts[v] ??= new CellText(this.column(k)[v] as Element));
    });
  }

  /**
   * A column's cells, one for each of its values (by their index), for their contents: made from
   * their HTML at once, in a document of their own (where images don't load), or from their text
   * alone, when that's all their HTML is.
   */
  column(k: number): Element[] {
    let made = this.made[k];
    if (made === undefined) {
      const doc = (this.doc ??= document.implementation.createHTMLDocument(""));
      const values = (this.payload as RowsPayload).cells[k]?.html.v ?? [];
      const marked = values.filter((value) => /[<&]/.test(value));
      const body = doc.createElement("tbody");
      body.innerHTML = marked.map((value) => `<tr><td>${value}</td></tr>`).join("");
      const parsed = Array.from(body.children, (tr) => tr.firstElementChild as Element);
      // (One by one, if their HTML ran into each other's)
      const whole = parsed.length === marked.length;
      let m = 0;
      made = values.map((value) => {
        const marks = /[<&]/.test(value);
        if (marks && whole) {
          return parsed[m++] as Element;
        }
        const td = doc.createElement("td");
        td[marks ? "innerHTML" : "textContent"] = value;
        return td;
      });
      this.made[k] = made;
    }
    return made;
  }

  /** Rows' cells (once the payload has come), as each row has them, by row, out of the page. */
  parse(rows: number[]): Map<number, Element[]> {
    const doc = (this.doc ??= document.implementation.createHTMLDocument(""));
    const body = doc.createElement("tbody");
    body.innerHTML = this.html(rows);
    return new Map(Array.from(body.children, (tr, i) => [rows[i] as number, Array.from(tr.children)]));
  }
}
