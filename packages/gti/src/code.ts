/**
 * The code for a view: Python that filters and sorts a table's data (`df`) as the view's filters
 * and sort do (and drops the columns it hides), for Polars, pandas, or Narwhals, as Great Tables' `query_code()` writes it
 * (great_tables/_gti/_query.py), character for character.
 *
 * It goes by what the spec's `export.code` has of the columns: their types, as the code needs
 * them, and a facet's values as Python (the code's values are the data's, not the text shown).
 */

import { type FilterClause, type FilterItem, type FilterQuery, isClause } from "./filter";
import { patternCode } from "./pattern";
import { fold } from "./search";
import type { SortKey } from "./sort";
import type { CodeBackend, CodeSpec, FilterSpec } from "./spec";

// (Python's `json.dumps(ensure_ascii=False)`)
const str = (text: string) => JSON.stringify(text);
const list = (items: readonly string[]) => `[${items.join(", ")}]`;
const py = (flag: boolean) => (flag ? "True" : "False");
// (The comparisons' operators)
const OPERATORS = { gte: ">=", lte: "<=", gt: ">", lt: "<" };

// A term of the code's filter, and how tightly it binds, as Python's operators do: a comparison,
// an `|`, an `&`, a `~`, or an atom (a call, or in parentheses)
type Term = [string, number];
const COMPARE = 0;
const OR = 1;
const AND = 2;
const NOT = 3;
const ATOM = 4;

/** A bound, as Python writes it: an integer if it's whole, or else as `repr()` writes a float. */
export function pyNumber(value: number): string {
  if (Number.isInteger(value)) {
    return BigInt(value).toString();
  }
  // (As JavaScript does, but in exponent notation below 1e-4: 1e-05)
  const [digits, exponent] = value.toExponential().split("e") as [string, string];
  return +exponent < -4 ? `${digits}e-${exponent.slice(1).padStart(2, "0")}` : String(value);
}

/**
 * A date bound (ISO 8601 text, as `filter.ts` has it), as Python's `repr()` writes it: a
 * `datetime.date`, or for a column of dates and times, a `datetime.datetime` (a date as its
 * midnight).
 */
export function pyDate(text: string, times: boolean): string {
  const [date = "", time = ""] = text.split("T");
  const [year, month, day] = date.split("-").map(Number);
  if (!times) {
    return `datetime.date(${year}, ${month}, ${day})`;
  }
  const [clock = "", fraction = ""] = time.split(".");
  const [hour = 0, minute = 0, second = 0] = clock === "" ? [] : clock.split(":").map(Number);
  const micro = Number(fraction.padEnd(6, "0"));
  const parts = [year, month, day, hour, minute];
  if (second !== 0 || micro !== 0) {
    parts.push(second);
  }
  if (micro !== 0) {
    parts.push(micro);
  }
  return `datetime.datetime(${parts.join(", ")})`;
}

/**
 * The code for a view (its query, as the `filter` property has it, its sort, and the columns it
 * hides, in column order), with its imports, for `backend`.
 *
 * @throws {RangeError} for a facet's value that can't be written as Python (a duration).
 */
export function viewCode(
  query: FilterQuery | null,
  sort: readonly SortKey[],
  hidden: readonly string[],
  filters: readonly FilterSpec[],
  spec: CodeSpec,
  backend: CodeBackend,
): string {
  const pandas = backend === "pandas";
  const ns = backend === "polars" ? "pl" : "nw";
  const imports = new Set<string>();
  if (!pandas) {
    imports.add(`import ${backend} as ${ns}`);
  }
  // A clause's term (`null` for a `contains` without text, which keeps every row)
  const clauseTerm = (clause: FilterClause): Term | null => {
    const name = str(clause.col);
    const column = spec.columns[clause.col];
    const col = pandas ? `df[${name}]` : `${ns}.col(${name})`;
    const text = column?.dtype === "string" ? col : pandas ? `${col}.astype(str)` : `${col}.cast(${ns}.String)`;
    if (clause.op === "matches") {
      const pattern = str(patternCode(clause.value));
      return [pandas ? `${text}.str.contains(${pattern}, regex=True, na=False)` : `${text}.str.contains(${pattern})`, ATOM];
    }
    if (clause.op === "contains") {
      const needle = str(fold(clause.value.trim()));
      if (needle === '""') {
        return null;
      }
      return [
        pandas
          ? `${text}.str.contains(${needle}, case=False, regex=False, na=False)`
          : `${text}.str.to_lowercase().str.contains(${needle}, literal=True)`,
        ATOM,
      ];
    }
    if (clause.op === "is_null") {
      // (A float's NaN is missing too, as pandas has it already)
      return pandas
        ? [`${col}.isna()`, ATOM]
        : column?.dtype === "float"
          ? [`${col}.is_null() | ${col}.is_nan()`, OR]
          : [`${col}.is_null()`, ATOM];
    }
    if (clause.op === "in") {
      const values = filters.find((filter) => filter.column === clause.col)?.values ?? [];
      const present = clause.value.filter((value) => value !== null);
      const literals = present.map((value) => {
        const literal = column?.literals?.[values.indexOf(value)];
        if (literal == null) {
          throw new RangeError(`the filter on ${name} can't be written as code`);
        }
        if (literal.startsWith("datetime.")) {
          imports.add("import datetime");
        }
        return literal;
      });
      const missing = pandas ? `${col}.isna()` : `${col}.is_null()`;
      if (present.length === 0) {
        return [missing, ATOM];
      }
      // (A category as its text; and with Narwhals, both zeros of floats, which PyArrow tells apart)
      const keys =
        !pandas && column?.dtype === "categorical" && present.every((value) => typeof value === "string")
          ? `${col}.cast(${ns}.String)`
          : col;
      const zeros = backend === "narwhals" && column?.dtype === "float" && present.includes(0);
      const items = zeros ? [...literals.filter((_, i) => present[i] !== 0), "-0.0", "0.0"] : literals;
      const term = `${keys}.${pandas ? "isin" : "is_in"}(${list(items)})`;
      return present.length < clause.value.length ? [`${term} | ${missing}`, OR] : [term, ATOM];
    }
    if (clause.op === "top_n" || clause.op === "bottom_n") {
      // (Ranked among all the rows, ties with the n-th kept; a float's NaN and infinities aren't
      // ranked)
      const top = clause.op === "top_n";
      let ranked = col;
      if (column?.dtype === "float") {
        if (pandas) {
          imports.add("import numpy as np");
        }
        ranked = pandas ? `${col}.where(np.isfinite(${col}))` : `${ns}.when(${col}.is_finite()).then(${col})`;
      }
      const rank = pandas
        ? `${ranked}.rank(method="min"${top ? ", ascending=False" : ""})`
        : `${ranked}.rank("min"${top ? ", descending=True" : ""})`;
      return [`${rank} <= ${clause.value}`, COMPARE];
    }
    let term: Term;
    const op = OPERATORS[clause.op];
    if (typeof clause.value === "string") {
      imports.add("import datetime");
      term = [`${col} ${op} ${pyDate(clause.value, column?.dtype === "datetime")}`, COMPARE];
    } else {
      term = [`${col} ${op} ${pyNumber(clause.value)}`, COMPARE];
      // (A float's NaN and infinities aren't kept)
      if (column?.dtype === "float") {
        if (pandas) {
          imports.add("import numpy as np");
        }
        term = [`(${term[0]}) & ${pandas ? `np.isfinite(${col})` : `${col}.is_finite()`}`, AND];
      }
    }
    return pandas && column?.nullable ? [`(${term[0]}).fillna(False)`, ATOM] : term;
  };

  // A part of the query's term: a group's parts joined by `|` or `&` (each in parentheses unless
  // it's an atom, a `~`, or of the same kind); and a `not`'s part after `~`, a clause that leaves
  // out a row with a missing value keeping it (as pandas' terms do already, filling them)
  const itemTerm = (item: FilterItem): Term => {
    if (isClause(item)) {
      return clauseTerm(item) as Term;
    }
    if ("not" in item) {
      const [code, rank] = itemTerm(item.not);
      return pandas
        ? [`~${rank >= NOT ? code : `(${code})`}`, NOT]
        : [`~${rank === ATOM ? code : `(${code})`}.fill_null(False)`, NOT];
    }
    const [parts, rank, joint] = "or" in item ? [item.or, OR, " | "] : [item.and, AND, " & "];
    const codes = parts.map(itemTerm).map(([code, r]) => (r >= NOT || r === rank ? code : `(${code})`));
    return [codes.join(joint), rank];
  };
  const terms = (query?.and ?? []).flatMap((item) => {
    const found = isClause(item) ? clauseTerm(item) : itemTerm(item);
    return found === null ? [] : [found[0]];
  });

  const names = sort.map((key) => str(key.column));
  const drop = list(hidden.map(str));
  let code = "df";
  if (pandas) {
    if (terms.length > 0) {
      code = `df[\n    ${terms.map((term) => (terms.length > 1 ? `(${term})` : term)).join("\n    & ")}\n]`;
    }
    if (sort.length > 0) {
      code += `.sort_values(${list(names)}, ascending=${list(sort.map((key) => py(!key.descending)))}, na_position="last", kind="stable")`;
    }
    if (hidden.length > 0) {
      code += `.drop(columns=${drop})`;
    }
  } else if (backend === "polars") {
    if (terms.length > 0) {
      code += `.filter(\n${terms.map((term) => `    ${term},\n`).join("")})`;
    }
    if (sort.length > 0) {
      code += `.sort(${list(names)}, descending=${list(sort.map((key) => py(key.descending)))}, nulls_last=True, maintain_order=True)`;
    }
    if (hidden.length > 0) {
      code += `.drop(${drop})`;
    }
  } else {
    const lines = ["nw.from_native(df)"];
    if (terms.length > 0) {
      lines.push(`.filter(\n${terms.map((term) => `        ${term},\n`).join("")}    )`);
    }
    if (sort.length > 0) {
      // (Narwhals' sort mightn't keep ties in order, so the rows' order is the last key; and NaN
      // is first in descending order, as with Polars)
      lines.push('.with_row_index("_row")');
      const by: string[] = [];
      const flags: boolean[] = [];
      const extra = ['"_row"'];
      sort.forEach(({ column, descending }, i) => {
        if (descending && spec.columns[column]?.dtype === "float") {
          const nan = str(`_nan_${column}`);
          const col = `nw.col(${names[i]})`;
          lines.push(`.with_columns((${col}.is_nan() & ~${col}.is_null()).fill_null(False).alias(${nan}))`);
          by.push(nan);
          flags.push(true);
          extra.push(nan);
        }
        by.push(names[i] as string);
        flags.push(descending);
      });
      lines.push(`.sort(${list([...by, '"_row"'])}, descending=${list([...flags, false].map(py))}, nulls_last=True)`);
      lines.push(`.drop(${list(extra)})`);
    }
    if (hidden.length > 0) {
      lines.push(`.drop(${drop})`);
    }
    lines.push(".to_native()");
    code = `(\n    ${lines.join("\n    ")}\n)`;
  }
  const header = Array.from(imports).sort().join("\n");
  return header ? `${header}\n\n${code}\n` : `${code}\n`;
}
