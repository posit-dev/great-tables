/**
 * Queries as text: a small language for the filters' query (see `filter.ts`), which reads and
 * writes it without loss.
 *
 *   status in ("single-tier", null) and population >= 10000 and `Name of town` contains "ville"
 *
 * A query is clauses joined by `and`; a clause is a column, then `contains` and a string, `in` and
 * values in parentheses, or `>=` or `<=` and a number. A column is a name of letters, digits and
 * underscores (not starting with a digit), or any name in backticks (a backtick in it doubled).
 * Strings and numbers are written as in JSON; the other values are `true`, `false` and `null` (a
 * missing value). Keywords can be in any case. Empty text is no query.
 *
 * Great Tables reads and writes the same language (`great_tables/_gti/_query.py`), with the same
 * errors.
 */

import type { FilterClause, FilterQuery } from "./filter";
import type { FilterValue } from "./spec";

const NAME = /^[A-Za-z_][A-Za-z0-9_]*$/;
const NAME_START = /[A-Za-z_]/y;
const NAME_REST = /[A-Za-z0-9_]*/y;
const STRING = /"(?:[^"\\\u0000-\u001f]|\\["\\/bfnrt]|\\u[0-9a-fA-F]{4})*"/y;
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

/** Read a query's text into a query, or `null` for empty text. @throws {SyntaxError} */
export function parseQuery(text: string): FilterQuery | null {
  let at = 0;
  let token: Token;
  function fail(message: string, where: Token = token): never {
    // (Counted in characters, not UTF-16 code units, as Python counts them)
    const place = where.kind === "end" ? "the end" : `character ${Array.from(text.slice(0, where.at)).length + 1}`;
    throw new SyntaxError(`${message}, at ${place}`);
  }

  function next(): Token {
    at += (match(SPACE, text, at) as string).length;
    const start = at;
    const char = text[at];
    if (char === undefined) {
      return { kind: "end", at };
    }
    if (match(NAME_START, text, at) !== null) {
      const name = char + match(NAME_REST, text, at + 1);
      at += name.length;
      return { kind: "name", text: name, at: start };
    }
    if (char === "`") {
      let name = "";
      for (at++; ; at++) {
        if (at >= text.length) {
          fail("a column name in backticks must end with a backtick", { kind: "end", at });
        }
        if (text[at] === "`") {
          if (text[at + 1] !== "`") {
            break;
          }
          at++;
        }
        name += text[at];
      }
      at++;
      return { kind: "quoted", text: name, at: start };
    }
    if (char === '"') {
      const string = match(STRING, text, at);
      if (string === null) {
        fail('a string must end with a double quote (with escapes as in JSON)', { kind: "symbol", text: char, at });
      }
      at += (string as string).length;
      return { kind: "string", value: JSON.parse(string as string), at: start };
    }
    const number = match(NUMBER, text, at);
    if (number !== null) {
      const value = Number(number);
      if (!Number.isFinite(value)) {
        fail(`the number ${number} is too large`, { kind: "symbol", text: number, at });
      }
      at += number.length;
      return { kind: "number", value, at: start };
    }
    const symbol = text.startsWith(">=", at) || text.startsWith("<=", at) ? text.slice(at, at + 2) : char;
    at += symbol.length;
    return { kind: "symbol", text: symbol, at: start };
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
      if (t.kind !== "number") {
        return fail("expected a number");
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

const formatColumn = (name: string) => (NAME.test(name) ? name : `\`${name.replace(/`/g, "``")}\``);

const formatValue = (value: FilterValue) => (typeof value === "number" ? String(value) : JSON.stringify(value));

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
