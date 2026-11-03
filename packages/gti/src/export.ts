/**
 * Writing a table's rows out: as CSV (RFC 4180, as spreadsheets read it), and as tab-separated
 * text (for the clipboard, with an HTML table).
 */

// A cell a spreadsheet would read as a formula: one starting with `=`, `+`, `-`, `@`, a tab or a
// carriage return; but not a number (as "-1,234.5" or "+5%" are)
const FORMULA = /^[=+\-@\t\r]/;
const NUMBER = /^[-+][\d.,\s]*\d[\d.,\s]*%?$/;

/**
 * A cell as CSV has it: in double quotes if it has a comma, a double quote or a line break; and
 * (with `guard`) after a `'` if a spreadsheet would read it as a formula.
 */
export function csvCell(text: string, guard = true): string {
  if (guard && FORMULA.test(text) && !NUMBER.test(text)) {
    text = `'${text}`;
  }
  return /[",\r\n]/.test(text) ? `"${text.replace(/"/g, '""')}"` : text;
}

/** Rows of cells as CSV, each line ending in CRLF (see `csvCell()` for `guard`). */
export function toCSV(rows: readonly (readonly string[])[], guard = true): string {
  return rows.map((row) => `${row.map((cell) => csvCell(cell, guard)).join(",")}\r\n`).join("");
}

/** Rows of cells as tab-separated text, with the cells' tabs and line breaks as spaces. */
export function toTSV(rows: readonly (readonly string[])[]): string {
  return rows.map((row) => row.map((cell) => cell.replace(/[\t\r\n]/g, " ")).join("\t")).join("\n");
}
