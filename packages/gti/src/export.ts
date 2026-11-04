/**
 * Writing a table's rows out: as CSV (RFC 4180, as spreadsheets read it), as tab-separated text
 * (for the clipboard, with an HTML table, and for a download), and as records (objects, and their
 * JSON).
 */

// A cell a spreadsheet would read as a formula: one starting with `=`, `+`, `-`, `@`, a tab or a
// carriage return; but not a number (as "-1,234.5" or "+5%" are)
const FORMULA = /^[=+\-@\t\r]/;
const NUMBER = /^[-+][\d.,\s]*\d[\d.,\s]*%?$/;

// A cell's text, after a `'` if a spreadsheet would read it as a formula
const guarded = (text: string) => (FORMULA.test(text) && !NUMBER.test(text) ? `'${text}` : text);

/**
 * A cell as CSV has it: in double quotes if it has a comma, a double quote or a line break; and
 * (with `guard`) after a `'` if a spreadsheet would read it as a formula.
 */
export function csvCell(text: string, guard = true): string {
  if (guard) {
    text = guarded(text);
  }
  return /[",\r\n]/.test(text) ? `"${text.replace(/"/g, '""')}"` : text;
}

/** Rows of cells as CSV, each line ending in CRLF (see `csvCell()` for `guard`). */
export function toCSV(rows: readonly (readonly string[])[], guard = true): string {
  return rows.map((row) => `${row.map((cell) => csvCell(cell, guard)).join(",")}\r\n`).join("");
}

/**
 * Rows of cells as tab-separated text, with the cells' tabs and line breaks as spaces; and (with
 * `guard`) a cell a spreadsheet would read as a formula after a `'`.
 */
export function toTSV(rows: readonly (readonly string[])[], guard = false): string {
  return rows
    .map((row) =>
      row
        .map((cell) => {
          const text = cell.replace(/[\t\r\n]/g, " ");
          return guard ? guarded(text) : text;
        })
        .join("\t"),
    )
    .join("\n");
}

/** Rows of cells as records: an object for each row, with each of its cells under its column's key. */
export function toRecords(keys: readonly string[], rows: readonly (readonly string[])[]): Record<string, string>[] {
  return rows.map((row) => Object.fromEntries(keys.map((key, i) => [key, row[i] ?? ""])));
}

/**
 * Rows of cells as JSON records, as `JSON.stringify()` indents them, but with the keys in their
 * columns' order (which an object doesn't keep for keys like "2020"), and a line break at the end.
 */
export function recordsJSON(keys: readonly string[], rows: readonly (readonly string[])[]): string {
  if (rows.length === 0) {
    return "[]\n";
  }
  const names = keys.map((key) => JSON.stringify(key));
  const records = rows.map((row) =>
    names.length === 0
      ? "  {}"
      : `  {${names.map((name, i) => `\n    ${name}: ${JSON.stringify(row[i] ?? "")}`).join(",")}\n  }`,
  );
  return `[\n${records.join(",\n")}\n]\n`;
}
