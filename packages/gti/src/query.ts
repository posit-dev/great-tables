/**
 * Queries as text: a small language for the filters' query (see `filter.ts`), which reads and
 * writes it without loss.
 *
 *   status in ("single-tier", null) and population >= 10000 and `Name of town` contains "ville"
 *   and founded <= "1900-12-31"
 *
 * A query is clauses joined by `and`; a clause is a column, then `contains` and a string, `in` and
 * values in parentheses, or `>=` or `<=` and a number or a date (a string of ISO 8601 text, as
 * `filter.ts` has it). A column is a name of letters, digits and
 * underscores (not starting with a digit), or any name in backticks (a backtick in it doubled).
 * Strings and numbers are written as in JSON; the other values are `true`, `false` and `null` (a
 * missing value). Keywords can be in any case. Empty text is no query.
 *
 * Great Tables reads and writes the same language (`great_tables/_gti/_query.py`), with the same
 * errors.
 *
 * For a query being typed, `readQuery()` reads as much as it can of text that isn't (yet) a query,
 * saying what each part is, for highlighting, and `queryContext()` what can go where the caret is,
 * for suggestions.
 */

import type { ColumnFilter, FilterClause, FilterQuery } from "./filter";
import type { FilterValue } from "./spec";

/** A query's text that isn't a query: what's wrong, and where (in UTF-16 code units, to mark it). */
export interface QuerySyntaxError extends SyntaxError {
  from: number;
  to: number;
}

const NAME = /^[A-Za-z_][A-Za-z0-9_]*$/;
const WORD = /[A-Za-z_][A-Za-z0-9_]*/y;
// (A string or a name in backticks can be left open, as it's typed)
const QUOTED = /`(?:[^`]|``)*(`?)/y;
const STRING = /"(?:[^"\\]|\\[^])*("?)/y;
const NUMBER = /-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?/y;
const SPACE = /[ \t\n\r]*/y;

type Token =
  | { kind: "name"; text: string; at: number }
  | { kind: "quoted"; text: string; at: number }
  | { kind: "string"; value: string; at: number }
  | { kind: "number"; value: number; at: number }
  | { kind: "symbol"; text: string; at: number }
  | { kind: "end"; at: number };

const match = (re: RegExp, text: string, at: number): string | null => {
  re.lastIndex = at;
  return re.exec(text)?.[0] ?? null;
};

const json = (text: string): unknown => {
  try {
    return JSON.parse(text);
  } catch {
    return undefined;
  }
};

// The text's part after a place (and any space), read loosely; `null` at the end
function scan(text: string, at: number): Pick<QueryPart, "kind" | "text" | "from" | "to" | "open"> | null {
  const from = at + (match(SPACE, text, at) as string).length;
  const char = text[from];
  if (char === undefined) {
    return null;
  }
  let kind: QueryPart["kind"] = "symbol";
  let open = false;
  let piece = match(WORD, text, from);
  if (piece !== null) {
    kind = "name";
  } else if (char === "`" || char === '"') {
    const re = char === "`" ? QUOTED : STRING;
    re.lastIndex = from;
    const found = re.exec(text) as RegExpExecArray;
    [piece] = found;
    kind = char === "`" ? "quoted" : "string";
    open = found[1] === "";
  } else if ((piece = match(NUMBER, text, from)) !== null) {
    kind = "number";
  } else {
    // (A whole character, to mark it)
    piece =
      text.startsWith(">=", from) || text.startsWith("<=", from)
        ? text.slice(from, from + 2)
        : String.fromCodePoint(text.codePointAt(from) as number);
  }
  return { kind, text: piece, from, to: from + piece.length, open };
}

/** Read a query's text into a query, or `null` for empty text. @throws {SyntaxError} */
export function parseQuery(text: string): FilterQuery | null {
  let at = 0;
  let token: Token;
  function fail(message: string, where: Token = token): never {
    // (Counted in characters, not UTF-16 code units, as Python counts them)
    const place = where.kind === "end" ? "the end" : `character ${Array.from(text.slice(0, where.at)).length + 1}`;
    // (The current token ends where reading is; one made for the error, after its text)
    const to = where === token ? at : where.at + (where.kind === "symbol" ? where.text.length : 0);
    throw Object.assign(new SyntaxError(`${message}, at ${place}`), { from: where.at, to });
  }

  function next(): Token {
    const part = scan(text, at);
    if (part === null) {
      at = text.length;
      return { kind: "end", at };
    }
    const { kind, text: piece, from, open } = part;
    at = part.to;
    if (kind === "quoted") {
      if (open) {
        fail("a column name in backticks must end with a backtick", { kind: "end", at });
      }
      return { kind, text: piece.slice(1, -1).replace(/``/g, "`"), at: from };
    }
    if (kind === "string") {
      // (As JSON has them: escapes, and no control characters)
      const value = open ? null : json(piece);
      if (typeof value !== "string") {
        fail("a string must end with a double quote (with escapes as in JSON)", { kind: "symbol", text: '"', at: from });
      }
      return { kind, value: value as string, at: from };
    }
    if (kind === "number") {
      const value = Number(piece);
      if (!Number.isFinite(value)) {
        fail(`the number ${piece} is too large`, { kind: "symbol", text: piece, at: from });
      }
      return { kind, value, at: from };
    }
    return { kind, text: piece, at: from };
  }

  const isWord = (word: string) => token.kind === "name" && token.text.toLowerCase() === word;
  const isSymbol = (symbol: string) => token.kind === "symbol" && token.text === symbol;

  function value(): FilterValue {
    const t = token;
    if (t.kind === "string" || t.kind === "number") {
      token = next();
      return t.value;
    }
    for (const [word, v] of [
      ["true", true],
      ["false", false],
      ["null", null],
    ] as const) {
      if (isWord(word)) {
        token = next();
        return v;
      }
    }
    return fail("expected a value: a string in double quotes, a number, true, false or null");
  }

  function clause(): FilterClause {
    if (token.kind !== "name" && token.kind !== "quoted") {
      fail("expected a column name");
    }
    const col = (token as { text: string }).text;
    token = next();
    if (isWord("contains")) {
      token = next();
      const t = token;
      if (t.kind !== "string") {
        return fail("expected a string in double quotes");
      }
      token = next();
      return { col, op: "contains", value: t.value };
    }
    if (isWord("in")) {
      token = next();
      if (!isSymbol("(")) {
        fail('expected "("');
      }
      token = next();
      const values = [value()];
      while (!isSymbol(")")) {
        if (!isSymbol(",")) {
          fail('expected "," or ")"');
        }
        token = next();
        values.push(value());
      }
      token = next();
      return { col, op: "in", value: values };
    }
    if (isSymbol(">=") || isSymbol("<=")) {
      const op = (token as { text: string }).text === ">=" ? "gte" : "lte";
      token = next();
      const t = token;
      if (t.kind !== "number" && t.kind !== "string") {
        return fail("expected a number, or a date in double quotes");
      }
      token = next();
      return { col, op, value: t.value };
    }
    return fail('expected "contains", "in", ">=" or "<="');
  }

  token = next();
  if (token.kind === "end") {
    return null;
  }
  const clauses = [clause()];
  while (token.kind !== "end") {
    if (!isWord("and")) {
      fail('expected "and" or the end of the query');
    }
    token = next();
    clauses.push(clause());
  }
  return { and: clauses };
}

/** A column's name as a query has it: in backticks, unless it's letters, digits and underscores. */
export const formatColumn = (name: string) => (NAME.test(name) ? name : `\`${name.replace(/`/g, "``")}\``);

/** A value as a query has it. */
export const formatValue = (value: FilterValue) =>
  typeof value === "number" ? String(value) : JSON.stringify(value);

/** Write a query as text (`""` for `null`), which `parseQuery()` reads back as the same query. */
export function formatQuery(query: FilterQuery | null): string {
  return (query?.and ?? [])
    .map((clause) => {
      const col = formatColumn(clause.col);
      switch (clause.op) {
        case "contains":
          return `${col} contains ${JSON.stringify(clause.value)}`;
        case "in":
          return `${col} in (${clause.value.map(formatValue).join(", ")})`;
        default:
          return `${col} ${clause.op === "gte" ? ">=" : "<="} ${formatValue(clause.value)}`;
      }
    })
    .join(" and ");
}

/** What a part of a query's text is (for highlighting it), or `null` where it doesn't fit. */
export type QueryRole = "column" | "keyword" | "string" | "number" | "literal" | "punct";

/**
 * What goes next in a query: a column, an op, a string (after `contains`), `(` (after `in`), a
 * value or `,` or `)` (in the parentheses), a bound (a number or a date, after `>=` or `<=`), or
 * `and`; `null` where the text doesn't fit.
 */
export type QueryExpect = "column" | "op" | "string" | "(" | "value" | ",)" | "bound" | "and" | null;

export interface QueryState {
  expect: QueryExpect;
  /** The clause's column, once it has one. */
  col: string | null;
  /** The values in the parentheses so far (after `in`). */
  values: FilterValue[];
}

export interface QueryPart {
  kind: "name" | "quoted" | "string" | "number" | "symbol";
  text: string;
  /** Where it is in the text (in UTF-16 code units). */
  from: number;
  to: number;
  /** A string or a name in backticks without its closing quote. */
  open: boolean;
  role: QueryRole | null;
  /** The state before it. */
  state: QueryState;
}

export interface QueryReading {
  parts: QueryPart[];
  /** Where each whole clause is (in the clauses' order). */
  clauses: [number, number][];
  /** The state after the text. */
  end: QueryState;
}

// A part as a value (`undefined` if it isn't one, or isn't finished)
function partValue({ kind, text, open }: Pick<QueryPart, "kind" | "text" | "open">): FilterValue | undefined {
  if (kind === "number") {
    return Number(text);
  }
  if (kind === "string" && !open) {
    return json(text) as FilterValue | undefined;
  }
  const word = kind === "name" ? text.toLowerCase() : "";
  return word === "true" ? true : word === "false" ? false : word === "null" ? null : undefined;
}

// What a part can be after a state: the state after it, and its role (`null` if it doesn't fit)
function step(
  expect: QueryExpect,
  { kind, text, open }: QueryPart,
  word: string | null,
  symbol: string | null,
): [QueryExpect, QueryRole] | null {
  switch (expect) {
    case "column":
      return kind === "name" || kind === "quoted" ? ["op", "column"] : null;
    case "op":
      return word === "contains"
        ? ["string", "keyword"]
        : word === "in"
          ? ["(", "keyword"]
          : symbol === ">=" || symbol === "<="
            ? ["bound", "keyword"]
            : null;
    case "string":
      return kind === "string" ? ["and", "string"] : null;
    case "(":
      return symbol === "(" ? ["value", "punct"] : null;
    case "value":
      // (A string being typed is one, too)
      return kind === "string" || kind === "number"
        ? [",)", kind]
        : partValue({ kind, text, open }) !== undefined
          ? [",)", "literal"]
          : null;
    case ",)":
      return symbol === "," ? ["value", "punct"] : symbol === ")" ? ["and", "punct"] : null;
    case "bound":
      return kind === "number" || kind === "string" ? ["and", kind] : null;
    case "and":
      return word === "and" ? ["column", "keyword"] : null;
    default:
      return null;
  }
}

/** Read text as far as it's a query, saying what each part is and where the clauses are. */
export function readQuery(text: string): QueryReading {
  const parts: QueryPart[] = [];
  const clauses: [number, number][] = [];
  let state: QueryState = { expect: "column", col: null, values: [] };
  let start = 0;
  for (let at = 0; ; ) {
    const found = scan(text, at);
    if (found === null) {
      return { parts, clauses, end: state };
    }
    const { kind, text: piece, open } = found;
    const part: QueryPart = { ...found, role: null, state };
    at = part.to;
    const word = kind === "name" ? piece.toLowerCase() : null;
    const symbol = kind === "symbol" ? piece : null;
    const value = partValue(part);
    let { col, values } = state;
    let [expect, role] = step(state.expect, part, word, symbol) ?? [null, null];
    if (role === "column") {
      col = kind === "name" ? piece : piece.slice(1, open ? undefined : -1).replace(/``/g, "`");
      start = part.from;
    } else if (state.expect === "(" && role !== null) {
      values = [];
    } else if (state.expect === "value" && value !== undefined) {
      values = [...values, value];
    }
    // (Past what doesn't fit, reading picks up again at an `and`)
    if (role === null && word === "and") {
      [expect, role] = ["column", "keyword"];
    }
    if (expect === "and" && state.expect !== "and") {
      clauses.push([start, part.to]);
    }
    part.role = role;
    parts.push(part);
    state = { expect, col: expect === null ? null : col, values };
  }
}

/** What can go at the caret: a part to replace (from `from` to `to`) and its text so far, if any. */
export interface QueryContext extends QueryState {
  from: number;
  to: number;
  prefix: string;
}

/** What can go at a place in text being typed as a query (in UTF-16 code units). */
export function queryContext(text: string, caret: number): QueryContext {
  const { parts, end } = readQuery(text);
  const at = (state: QueryState, from = caret, to = caret): QueryContext => ({
    ...state,
    from,
    to,
    prefix: text.slice(from, caret),
  });
  for (const part of parts) {
    if (part.from >= caret) {
      return at(part.state);
    }
    // (A word, a string or a partial `>=` or `<=` at the caret is replaced; inside anything else,
    // nothing goes)
    const word = part.kind === "name" || part.kind === "quoted" || part.kind === "string";
    if (caret <= part.to && (word || part.text === ">" || part.text === "<")) {
      return at(part.state, part.from, part.to);
    }
    if (caret < part.to) {
      return at({ ...part.state, expect: null });
    }
  }
  return at(end);
}

const OPS = { text: ["contains"], facet: ["in"], range: [">=", "<="], date: [">=", "<="] };

/**
 * The first clause of a query (by its index) that filters can't have, and why, in the query's
 * terms; `null` if they can have them all.
 */
export function queryProblem(
  filters: readonly ColumnFilter[],
  query: FilterQuery | null,
): { clause: number; message: string } | null {
  const seen = new Set<string>();
  const clauses = query?.and ?? [];
  for (let i = 0; i < clauses.length; i++) {
    const clause = clauses[i] as FilterClause;
    const { col } = clause;
    const op = clause.op === "gte" ? ">=" : clause.op === "lte" ? "<=" : clause.op;
    const name = formatColumn(col);
    const filter = filters.find((f) => f.column === col);
    const key = JSON.stringify([col, op]);
    const bad =
      clause.op === "in" && filter !== undefined
        ? clause.value.find((value) => value !== null && filter.rankOf(value) === undefined)
        : undefined;
    const bound = clause.op === "gte" || clause.op === "lte" ? clause.value : undefined;
    const message =
      filter === undefined
        ? `${name} isn't a column with a filter`
        : !OPS[filter.type].includes(op)
          ? `${name} has a ${filter.type} filter: use ${OPS[filter.type].join(" or ")}`
          : seen.has(key)
            ? `${name} has more than one ${op} clause`
            : bad !== undefined
              ? `${formatValue(bad)} isn't a value of ${name}`
              : filter.type === "range" && typeof bound === "string"
                ? `${name} has a range filter: give a number`
                : filter.type === "date" && typeof bound === "number"
                  ? `${name} has a date filter: give a date in double quotes ("YYYY-MM-DD")`
                  : filter.type === "date" && typeof bound === "string" && !filter.isDateBound(bound)
                    ? filter.times
                      ? `${formatValue(bound)} isn't a date ("YYYY-MM-DD") or date and time ("YYYY-MM-DDTHH:MM:SS")`
                      : `${formatValue(bound)} isn't a date ("YYYY-MM-DD"), and ${name} has dates without times`
                    : null;
    if (message !== null) {
      return { clause: i, message };
    }
    seen.add(key);
  }
  return null;
}
