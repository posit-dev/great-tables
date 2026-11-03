/**
 * The code for a view: Python that filters and sorts a table's data (`df`) as the view's filters
 * and sort do (and drops the columns it hides), for Polars, pandas, or Narwhals, as Great Tables' `query_code()` writes it
 * (great_tables/_gti/_query.py), character for character.
 *
 * It goes by what the spec's `export.code` has of the columns: their types, as the code needs
 * them, and a facet's values as Python (the code's values are the data's, not the text shown).
 */

import type { FilterQuery } from "./filter";
import { fold } from "./search";
import type { SortKey } from "./sort";
import type { CodeBackend, CodeSpec, FilterSpec } from "./spec";

// (Python's `json.dumps(ensure_ascii=False)`)
const str = (text: string) => JSON.stringify(text);
const list = (items: readonly string[]) => `[${items.join(", ")}]`;
const py = (flag: boolean) => (flag ? "True" : "False");

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
  const terms: string[] = [];
  for (const clause of query?.and ?? []) {
    const name = str(clause.col);
    const column = spec.columns[clause.col];
    const col = pandas ? `df[${name}]` : `${ns}.col(${name})`;
    if (clause.op === "contains") {
      const needle = str(fold(clause.value.trim()));
      if (needle === '""') {
        continue;
      }
      const text = column?.dtype === "string" ? col : pandas ? `${col}.astype(str)` : `${col}.cast(${ns}.String)`;
      terms.push(
        pandas
          ? `${text}.str.contains(${needle}, case=False, regex=False, na=False)`
          : `${text}.str.to_lowercase().str.contains(${needle}, literal=True)`,
      );
    } else if (clause.op === "in") {
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
      let term = missing;
      if (present.length > 0) {
        // (A category as its text; and with Narwhals, both zeros of floats, which PyArrow tells apart)
        const keys =
          !pandas && column?.dtype === "categorical" && present.every((value) => typeof value === "string")
            ? `${col}.cast(${ns}.String)`
            : col;
        const zeros = backend === "narwhals" && column?.dtype === "float" && present.includes(0);
        const items = zeros ? [...literals.filter((_, i) => present[i] !== 0), "-0.0", "0.0"] : literals;
        term = `${keys}.${pandas ? "isin" : "is_in"}(${list(items)})`;
        if (present.length < clause.value.length) {
          term += ` | ${missing}`;
        }
      }
      terms.push(term);
    } else if (typeof clause.value === "string") {
      imports.add("import datetime");
      const term = `${col} ${clause.op === "gte" ? ">=" : "<="} ${pyDate(clause.value, column?.dtype === "datetime")}`;
      terms.push(pandas && column?.nullable ? `(${term}).fillna(False)` : term);
    } else {
      let term = `${col} ${clause.op === "gte" ? ">=" : "<="} ${pyNumber(clause.value)}`;
      // (A float's NaN and infinities aren't kept)
      if (column?.dtype === "float") {
        if (pandas) {
          imports.add("import numpy as np");
        }
        term = `(${term}) & ${pandas ? `np.isfinite(${col})` : `${col}.is_finite()`}`;
      }
      terms.push(pandas && column?.nullable ? `(${term}).fillna(False)` : term);
    }
  }

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
