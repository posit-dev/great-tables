/**
 * Queries as text: a small language for the filters' query (see `filter.ts`), which reads and
 * writes it without loss.
 *
 *   status in ("single-tier", null) and population >= 10000 and `Name of town` contains "ville"
 *   and founded <= "1900-12-31"
 *
 * A query is clauses joined by `and` and `or`, each of them after `not` if wanted, and grouped in
 * parentheses as wanted; `not` binds tighter than `and`, and `and` tighter than `or`:
 *
 *   region in ("east") and not (population >= 10000 or status in ("city"))
 *
 * A clause is a column, then `contains` and a string, `matches` and a pattern (a regular
 * expression between slashes, with the flag `i` to ignore case, as in `/^st\./i`; see
 * `pattern.ts`), `in` and values in parentheses, `>=`, `<=`, `>` or `<` and a number or a date (a
 * string of ISO 8601 text, as `filter.ts` has it), or `is null`; `x not in (...)`, `x not contains "..."`,
 * `x not matches /.../` and `x is not null` are `not` and those. A column is a name of letters,
 * digits and underscores (not starting with a digit), or any name in backticks (a backtick in it
 * doubled); `not` before an op is a column's name. Strings and numbers are written as in JSON; the other values are `true`,
 * `false` and `null` (a missing value). Keywords can be in any case. Empty text is no query.
 *
 * Great Tables reads and writes the same language (`great_tables/_gti/_query.py`), with the same
 * errors.
 *
 * For a query being typed, `readQuery()` reads as much as it can of text that isn't (yet) a query,
 * saying what each part is, for highlighting, and `queryContext()` what can go where the caret is,
 * for suggestions.
 */

import { type ColumnFilter, type FilterClause, type FilterItem, type FilterQuery, isClause } from "./filter";
import { formatPattern, type PatternError, readPattern } from "./pattern";
import { fold } from "./search";
import type { FilterValue } from "./spec";

/** A query's text that isn't a query: what's wrong, and where (in UTF-16 code units, to mark it). */
export interface QuerySyntaxError extends SyntaxError {
  from: number;
  to: number;
}

const NAME = /^[A-Za-z_][A-Za-z0-9_]*$/;
// (The ops that are words)
const OP_WORD = /^(?:in|contains|matches|is)$/i;
/** The ops that can be after `not`, as in `x not in (...)`. */
export const NEGATED = ["contains", "matches", "in"];
type Comparison = "gte" | "lte" | "gt" | "lt";
// (The ops that compare to a bound, by their symbols, and the symbols by the ops)
const COMPARISONS = new Map<string | null, Comparison>([
  [">=", "gte"],
  ["<=", "lte"],
  [">", "gt"],
  ["<", "lt"],
]);
const SYMBOLS: Record<Comparison, string> = { gte: ">=", lte: "<=", gt: ">", lt: "<" };
const WORD = /[A-Za-z_][A-Za-z0-9_]*/y;
// (A string or a name in backticks can be left open, as it's typed)
const QUOTED = /`(?:[^`]|``)*(`?)/y;
const STRING = /"(?:[^"\\]|\\[^])*("?)/y;
// (A pattern, on one line: escapes, and classes, where a slash needn't be escaped; then its flags)
const PATTERN = /\/(?:[^\\/[\n\r]|\\[^\n\r]|\[(?:[^\\\]\n\r]|\\[^\n\r])*\]?)*(\/?)([A-Za-z0-9_]*)/y;
const NUMBER = /-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?/y;
const SPACE = /[ \t\n\r]*/y;

type Token =
  | { kind: "name"; text: string; at: number }
  | { kind: "quoted"; text: string; at: number }
  | { kind: "string"; value: string; at: number }
  | { kind: "regex"; value: string; at: number }
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
  } else if (char === "`" || char === '"' || char === "/") {
    const re = char === "`" ? QUOTED : char === '"' ? STRING : PATTERN;
    re.lastIndex = from;
    const found = re.exec(text) as RegExpExecArray;
    [piece] = found;
    kind = char === "`" ? "quoted" : char === '"' ? "string" : "regex";
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
    if (kind === "regex") {
      if (open) {
        fail("a pattern must end with a slash", { kind: "symbol", text: "/", at: from });
      }
      const flags = (/[A-Za-z0-9_]*$/.exec(piece) as RegExpExecArray)[0];
      // (Where its closing slash is)
      const end = at - flags.length - 1;
      if (flags !== "" && flags !== "i") {
        fail('a pattern can have only the flag "i"', { kind: "symbol", text: flags, at: end + 1 });
      }
      try {
        return { kind, value: readPattern(text.slice(from + 1, end), flags === "i"), at: from };
      } catch (err) {
        const where = from + 1 + (err as PatternError).at;
        fail((err as Error).message, { kind: "symbol", text: String.fromCodePoint(text.codePointAt(where) as number), at: where });
      }
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

  function clause(): FilterItem {
    if (token.kind !== "name" && token.kind !== "quoted") {
      fail("expected a column name");
    }
    const col = (token as { text: string }).text;
    token = next();
    if (isWord("is")) {
      token = next();
      const not = isWord("not");
      if (not) {
        token = next();
      }
      if (!isWord("null")) {
        fail(not ? 'expected "null"' : 'expected "null" or "not null"');
      }
      token = next();
      const clause: FilterClause = { col, op: "is_null" };
      return not ? { not: clause } : clause;
    }
    // (`not` before `contains`, `matches` or `in` is a `not` of the clause)
    if (isWord("not")) {
      token = next();
      if (!NEGATED.some(isWord)) {
        fail('expected "contains", "matches" or "in"');
      }
      return { not: opClause(col) };
    }
    return opClause(col);
  }

  // A clause's op and what's after it
  function opClause(col: string): FilterClause {
    if (isWord("contains")) {
      token = next();
      const t = token;
      if (t.kind !== "string") {
        return fail("expected a string in double quotes");
      }
      token = next();
      return { col, op: "contains", value: t.value };
    }
    if (isWord("matches")) {
      token = next();
      const t = token;
      if (t.kind !== "regex") {
        return fail("expected a pattern between slashes, as in /^st\\./");
      }
      token = next();
      return { col, op: "matches", value: t.value };
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
    const op = token.kind === "symbol" ? COMPARISONS.get(token.text) : undefined;
    if (op !== undefined) {
      token = next();
      const t = token;
      if (t.kind !== "number" && t.kind !== "string") {
        return fail("expected a number, or a date in double quotes");
      }
      token = next();
      return { col, op, value: t.value };
    }
    return fail('expected "contains", "matches", "in", "not", ">=", "<=", ">", "<" or "is"');
  }

  // Whether the token is the keyword `not` (rather than a column's name, before an op)
  function isNot(): boolean {
    if (!isWord("not")) {
      return false;
    }
    const was = at;
    const after = next();
    at = was;
    const word = after.kind === "name" ? after.text.toLowerCase() : null;
    const symbol = after.kind === "symbol" ? after.text : null;
    return !OP_WORD.test(word ?? "") && !COMPARISONS.has(symbol);
  }

  // Parts joined by `or` or `and` (one part on its own; and the parts of a group of the same kind
  // spliced in)
  const group = (kind: "or" | "and", items: FilterItem[]): FilterItem =>
    items.length === 1
      ? (items[0] as FilterItem)
      : ({
          [kind]: items.flatMap((item) => (kind in item ? (item as Record<string, FilterItem[]>)[kind] : [item])),
        } as FilterItem);

  function unary(): FilterItem {
    if (isNot()) {
      token = next();
      return { not: unary() };
    }
    if (isSymbol("(")) {
      token = next();
      const item = or();
      if (!isSymbol(")")) {
        fail('expected "and", "or" or ")"');
      }
      token = next();
      return item;
    }
    return clause();
  }

  function and(): FilterItem {
    const items = [unary()];
    while (isWord("and")) {
      token = next();
      items.push(unary());
    }
    return group("and", items);
  }

  function or(): FilterItem {
    const items = [and()];
    while (isWord("or")) {
      token = next();
      items.push(and());
    }
    return group("or", items);
  }

  token = next();
  if (token.kind === "end") {
    return null;
  }
  const item = or();
  if ((token as Token).kind !== "end") {
    fail('expected "and", "or" or the end of the query');
  }
  return { and: "and" in item ? item.and : [item] };
}

/**
 * A column's name as a query has it: in backticks, unless it's letters, digits and underscores
 * (and not `in`, `contains`, `matches` or `is`, which are ops after `not`).
 */
export const formatColumn = (name: string) =>
  NAME.test(name) && !OP_WORD.test(name) ? name : `\`${name.replace(/`/g, "``")}\``;

/** A value as a query has it. */
export const formatValue = (value: FilterValue) =>
  typeof value === "number" ? String(value) : JSON.stringify(value);

// A clause's op and what's after it, as text
function formatOp(clause: FilterClause): string {
  switch (clause.op) {
    case "contains":
      return `contains ${JSON.stringify(clause.value)}`;
    case "matches":
      return `matches ${formatPattern(clause.value)}`;
    case "in":
      return `in (${clause.value.map(formatValue).join(", ")})`;
    case "is_null":
      return "is null";
    default:
      return `${SYMBOLS[clause.op]} ${formatValue(clause.value)}`;
  }
}

// A part of a query as text, in what it's a part of (`null` for the whole query): in parentheses
// only where it needs them (`not` binding tighter than `and`, and `and` tighter than `or`)
function formatItem(item: FilterItem, inside: "or" | "and" | "not" | null): string {
  if (isClause(item)) {
    return `${formatColumn(item.col)} ${formatOp(item)}`;
  }
  if ("not" in item) {
    const part = item.not;
    return isClause(part) && part.op === "is_null"
      ? `${formatColumn(part.col)} is not null`
      : isClause(part) && NEGATED.includes(part.op)
        ? `${formatColumn(part.col)} not ${formatOp(part)}`
        : `not ${formatItem(part, "not")}`;
  }
  const kind = "or" in item ? "or" : "and";
  const text = ("or" in item ? item.or : item.and).map((part) => formatItem(part, kind)).join(` ${kind} `);
  return inside === null || (kind === "and" && inside === "or") ? text : `(${text})`;
}

/**
 * Write a query as text (`""` for `null`), which `parseQuery()` reads back as the same query (as
 * `setFilterQuery()` writes it: with no `and` in an `and`, or `or` in an `or`, nor groups of one).
 */
export function formatQuery(query: FilterQuery | null): string {
  const items = query?.and ?? [];
  return items.length === 1
    ? formatItem(items[0] as FilterItem, null)
    : items.map((item) => formatItem(item, "and")).join(" and ");
}

/** What a part of a query's text is (for highlighting it), or `null` where it doesn't fit. */
export type QueryRole = "column" | "keyword" | "string" | "number" | "literal" | "punct";

/**
 * What goes next in a query: a column (or `not`, or `(`), an op, an op that can be after `not`
 * (after a column and `not`), a string (after `contains`), a pattern (after `matches`), `(` (after
 * `in`), a value or `,` or `)` (in the parentheses), a bound (a number or a date, after `>=`,
 * `<=`, `>` or `<`), `null` or `not` (after `is`), `null` (after `is not`), or `and` (or `or`, or a `)` closing
 * a group); `null` where the text doesn't fit.
 */
export type QueryExpect =
  | "column"
  | "op"
  | "negated"
  | "string"
  | "pattern"
  | "("
  | "value"
  | ",)"
  | "bound"
  | "is"
  | "null"
  | "and"
  | null;

export interface QueryState {
  expect: QueryExpect;
  /** The clause's column, once it has one. */
  col: string | null;
  /** The values in the parentheses so far (after `in`). */
  values: FilterValue[];
  /** How many groups' parentheses are open. */
  depth: number;
}

export interface QueryPart {
  kind: "name" | "quoted" | "string" | "regex" | "number" | "symbol";
  text: string;
  /** Where it is in the text (in UTF-16 code units). */
  from: number;
  to: number;
  /** A string, a pattern or a name in backticks without its closing quote (or slash). */
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
  { expect, depth }: QueryState,
  { kind, text, open }: QueryPart,
  word: string | null,
  symbol: string | null,
): [QueryExpect, QueryRole] | null {
  switch (expect) {
    case "column":
      return word === "not" || symbol === "("
        ? ["column", word === null ? "punct" : "keyword"]
        : kind === "name" || kind === "quoted"
          ? ["op", "column"]
          : null;
    case "op":
    case "negated":
      return word === "contains"
        ? ["string", "keyword"]
        : word === "matches"
          ? ["pattern", "keyword"]
          : word === "in"
            ? ["(", "keyword"]
            : expect === "negated"
              ? null
              : word === "not"
                ? ["negated", "keyword"]
                : word === "is"
                  ? ["is", "keyword"]
                  : COMPARISONS.has(symbol)
                    ? ["bound", "keyword"]
                    : null;
    case "is":
    case "null":
      return word === "null" ? ["and", "literal"] : word === "not" && expect === "is" ? ["null", "keyword"] : null;
    case "string":
      return kind === "string" ? ["and", "string"] : null;
    case "pattern":
      return kind === "regex" ? ["and", "string"] : null;
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
      return word === "and" || word === "or"
        ? ["column", "keyword"]
        : symbol === ")" && depth > 0
          ? ["and", "punct"]
          : null;
    default:
      return null;
  }
}

/** Read text as far as it's a query, saying what each part is and where the clauses are. */
export function readQuery(text: string): QueryReading {
  const parts: QueryPart[] = [];
  const clauses: [number, number][] = [];
  let state: QueryState = { expect: "column", col: null, values: [], depth: 0 };
  let start = 0;
  for (let at = 0; ; ) {
    const found = scan(text, at);
    if (found === null) {
      return { parts, clauses, end: state };
    }
    const { kind, text: piece, open } = found;
    const word = kind === "name" ? piece.toLowerCase() : null;
    const symbol = kind === "symbol" ? piece : null;
    // (A `not` before an op, or what may be one being typed, is a column's name)
    const last = parts[parts.length - 1];
    if (
      state.expect === "column" &&
      last?.role === "keyword" &&
      last.text.toLowerCase() === "not" &&
      (OP_WORD.test(word ?? "") || COMPARISONS.has(symbol))
    ) {
      last.role = "column";
      start = last.from;
      state = { ...state, expect: "op", col: last.text };
    }
    const part: QueryPart = { ...found, role: null, state };
    at = part.to;
    const value = partValue(part);
    let { col, values, depth } = state;
    let [expect, role] = step(state, part, word, symbol) ?? [null, null];
    if (role === "column") {
      col = kind === "name" ? piece : piece.slice(1, open ? undefined : -1).replace(/``/g, "`");
      start = part.from;
    } else if (state.expect === "(" && role !== null) {
      values = [];
    } else if (state.expect === "value" && value !== undefined) {
      values = [...values, value];
    } else if (role === "punct" && (state.expect === "column" || state.expect === "and")) {
      depth += symbol === "(" ? 1 : -1;
    }
    // (Past what doesn't fit, reading picks up again at an `and` or an `or`)
    if (role === null && (word === "and" || word === "or")) {
      [expect, role] = ["column", "keyword"];
    }
    if (expect === "and" && state.expect !== "and") {
      clauses.push([start, part.to]);
    }
    part.role = role;
    parts.push(part);
    state = { expect, col: expect === null ? null : col, values, depth };
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
    // (A word, a string, a pattern or a `>` or `<` (which may be the start of `>=` or `<=`) at the
    // caret is replaced; inside anything else, nothing goes)
    const word = part.kind === "name" || part.kind === "quoted" || part.kind === "string" || part.kind === "regex";
    if (caret <= part.to && (word || part.text === ">" || part.text === "<")) {
      return at(part.state, part.from, part.to);
    }
    if (caret < part.to) {
      return at({ ...part.state, expect: null });
    }
  }
  return at(end);
}

const BOUNDS = [">=", "<=", ">", "<"];
const OPS = { text: ["contains", "matches"], facet: ["in"], range: BOUNDS, date: BOUNDS, bool: ["in"] };

// Ops as a list, as in "contains or matches" or ">=, <=, > or <"
const opList = (ops: readonly string[]) => `${ops.slice(0, -1).join(", ")}${ops.length > 1 ? " or " : ""}${ops[ops.length - 1]}`;

// A query's clauses, in their order (as the text has them), each with the clauses before it in
// the same `and` (none for one in an `or` or a `not` on its own), and whether it's in a group
function* leaves(
  items: readonly FilterItem[],
  seen: Set<string>,
  grouped: boolean,
): Generator<[FilterClause, Set<string>, boolean]> {
  for (const item of items) {
    if (isClause(item)) {
      yield [item, seen, grouped];
    } else if ("and" in item) {
      yield* leaves(item.and, grouped ? new Set() : seen, grouped);
    } else {
      for (const part of "or" in item ? item.or : [item.not]) {
        yield* leaves([part], new Set(), true);
      }
    }
  }
}

/**
 * The first clause of a query (by its index, in the text's order) that filters can't have, and
 * why, in the query's terms; `null` if they can have them all.
 */
export function queryProblem(
  filters: readonly ColumnFilter[],
  query: FilterQuery | null,
): { clause: number; message: string } | null {
  let i = -1;
  for (const [clause, seen, grouped] of leaves(query?.and ?? [], new Set(), false)) {
    i++;
    const { col } = clause;
    const compares = clause.op === "gte" || clause.op === "lte" || clause.op === "gt" || clause.op === "lt";
    const bound = compares ? clause.value : undefined;
    const op = compares ? SYMBOLS[clause.op] : clause.op === "is_null" ? "is null" : clause.op;
    const name = formatColumn(col);
    const filter = filters.find((f) => f.column === col);
    const key = JSON.stringify([col, op]);
    const bad =
      clause.op === "in" && filter !== undefined
        ? clause.value.find((value) => value !== null && filter.rankOf(value) === undefined)
        : undefined;
    const message =
      filter === undefined
        ? `${name} isn't a column with a filter`
        : op !== "is null" && !OPS[filter.type].includes(op)
          ? `${name} has a ${filter.type} filter: use ${opList(OPS[filter.type])}`
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
                    : filter.type === "bool" && clause.op === "in" && clause.value.length > 1
                      ? `${name} has a bool filter: give one value, true, false or null`
                      : grouped && clause.op === "contains" && fold(clause.value.trim()) === ""
                        ? `${name} needs text to look for, in an "or" or a "not"`
                        : null;
    if (message !== null) {
      return { clause: i, message };
    }
    seen.add(key);
  }
  return null;
}
