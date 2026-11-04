/**
 * Patterns: the regular expressions of a query's `matches` clauses.
 *
 * A pattern is in the part of regular expressions' syntax that JavaScript (the runtime), Python's
 * `re` (Great Tables' `view_rows()`, and pandas), Rust's `regex` (Polars) and RE2 (PyArrow) read
 * alike, and is translated for each of them so that it means the same:
 *
 * - characters, with `\` before punctuation for the character itself, and `\n`, `\t`, `\r`, `\f`
 *   and `\v`; `.`, any character but a line break (`\n`); `^` and `$`, the start and the end of
 *   the text;
 * - classes, as `[a-z_]` and `[^0-9]`; and `\d`, `\w` and `\s` (or `\D`, `\W` and `\S`, not in a
 *   class), ASCII's digits, word characters and white space, `[0-9]`, `[0-9A-Z_a-z]` and
 *   `[\t\n\v\f\r ]`;
 * - groups, `(...)` or `(?:...)`, and `|`;
 * - repeats: `*`, `+`, `?`, `{n}`, `{n,}` and `{n,m}` (up to 1000), each lazy with a `?` after it.
 *
 * A pattern that starts with `(?i)` ignores case (as each of them does, alike for ASCII's
 * letters); in a query's text, that's the flag `i`, as in `/^st\./i`.
 *
 * Great Tables reads and translates patterns the same way (`great_tables/_gti/_pattern.py`), with
 * the same errors.
 */

/** A pattern that can't be read: what's wrong, and where (in UTF-16 code units). */
export interface PatternError extends SyntaxError {
  at: number;
}

const SYNTAX = "^$\\.*+?()[]{}|";
const CLASSES: Record<string, string> = { d: "0-9", w: "0-9A-Z_a-z", s: "\\t\\n\\v\\f\\r " };
const PUNCT = /^[!-/:-@[-`{-~]$/;
const REPEAT = /^\{([0-9]+)(,([0-9]*))?\}/;
const CASE = "(?i)";

/**
 * A pattern (without its `(?i)`) translated for JavaScript's `RegExp` (with the `u` flag), or
 * for the code (Polars', pandas' and PyArrow's regexes).
 *
 * @throws {SyntaxError} (a `PatternError`) for a pattern that isn't one.
 */
function translate(source: string, js: boolean): string {
  let i = 0;
  let depth = 0;
  let out = "";
  // What's before: something to repeat, a repeat (which only `?` can follow), or neither
  let last: "atom" | "repeat" | null = null;
  const fail = (message: string, at = i): never => {
    throw Object.assign(new SyntaxError(message), { at });
  };
  const peek = () => (i < source.length ? String.fromCodePoint(source.codePointAt(i) as number) : "");

  // A character (after a `\`, it's escaped), or a class's escape, as `\d`
  function atom(inClass: boolean): string {
    const at = i;
    const c = peek();
    i += c.length;
    if (c !== "\\") {
      return c;
    }
    const e = peek();
    if (e === "") {
      fail('expected a character after "\\"', at);
    }
    i += e.length;
    if ("dDwWsS".includes(e)) {
      if (inClass && e !== e.toLowerCase()) {
        fail(`"\\${e}" can't be in a class`, at);
      }
      return `\\${e}`;
    }
    const k = "nrtfv".indexOf(e);
    if (k < 0 && !PUNCT.test(e)) {
      fail(`"\\${e}" isn't an escape a pattern can have (\\d, \\w, \\s, \\D, \\W, \\S, \\n, \\t, \\r, \\f, \\v, or \\ before punctuation)`, at);
    }
    return k < 0 ? e : ("\n\r\t\f\v"[k] as string);
  }

  const isSet = (a: string) => a.length === 2 && a[0] === "\\";
  // A character or a class's escape, in a class or not
  const item = (a: string, inClass: boolean): string => {
    if (isSet(a)) {
      const letter = a[1] as string;
      const body = CLASSES[letter.toLowerCase()] as string;
      return inClass ? body : `[${letter === letter.toLowerCase() ? "" : "^"}${body}]`;
    }
    const escaped = inClass ? (js ? "\\]^-[" : "\\]^-[&~|") : SYNTAX;
    return escaped.includes(a) ? `\\${a}` : a;
  };

  function klass(): string {
    let body = peek() === "^" ? "^" : "";
    i += body.length;
    if (peek() === "]") {
      fail('a class can\'t be empty (a "]" in it must be escaped: "\\]")');
    }
    for (;;) {
      const c = peek();
      if (c === "") {
        fail('expected "]"');
      }
      if (c === "]") {
        i++;
        return `[${body}]`;
      }
      if (c === "[") {
        fail('"[" in a class must be escaped: "\\["');
      }
      const at = i;
      const a = atom(true);
      if (peek() !== "-" || i + 1 >= source.length || source[i + 1] === "]") {
        body += item(a, true);
        continue;
      }
      i++;
      if (peek() === "[") {
        fail('"[" in a class must be escaped: "\\["');
      }
      const to = i;
      const b = atom(true);
      if (isSet(a) || isSet(b)) {
        fail(`"${isSet(a) ? a : b}" can't be in a range`, isSet(a) ? at : to);
      }
      if ((a.codePointAt(0) as number) > (b.codePointAt(0) as number)) {
        fail(`the range "${source.slice(at, i)}" is out of order`, at);
      }
      body += `${item(a, true)}-${item(b, true)}`;
    }
  }

  if (source === "") {
    fail("expected a pattern");
  }
  while (i < source.length) {
    const at = i;
    const c = peek();
    if ("*+?{".includes(c)) {
      let repeat = c;
      if (c === "{") {
        const found = REPEAT.exec(source.slice(i));
        if (found === null) {
          fail('"{" must start a repeat, as in {2}, {2,} or {2,5} (or be escaped: "\\{")');
        }
        const [whole, low, , high = ""] = found as RegExpExecArray as string[];
        if (+(low as string) > 1000 || (high !== "" && (+high > 1000 || +high < +(low as string)))) {
          fail("a repeat can be at most 1000, and its first number no more than its second");
        }
        repeat = whole as string;
      }
      if (last !== "atom") {
        fail(`"${c}" must follow something to repeat`);
      }
      i += repeat.length;
      if (peek() === "?") {
        repeat += "?";
        i++;
      }
      out += repeat;
      last = "repeat";
      continue;
    }
    i += c.length;
    last = "atom";
    if (c === "(") {
      if (peek() === "?") {
        if (source[i + 1] !== ":") {
          fail('"(?" must be "(?:" (a pattern can\'t have lookarounds, named groups or flags)', at);
        }
        i += 2;
      }
      depth++;
      out += "(?:";
      last = null;
    } else if (c === ")") {
      if (depth === 0) {
        fail('")" must close a "(" (or be escaped: "\\)")', at);
      }
      depth--;
      out += ")";
    } else if (c === "|" || c === "^" || c === "$") {
      out += c;
      last = null;
    } else if (c === "]" || c === "}") {
      fail(`"${c}" must be escaped: "\\${c}"`, at);
    } else if (c === ".") {
      out += js ? "[^\\n]" : ".";
    } else if (c === "[") {
      out += klass();
    } else {
      i = at;
      out += item(atom(false), false);
    }
  }
  if (depth > 0) {
    fail('expected ")"');
  }
  return out;
}

// A pattern's source, and whether it ignores case
const split = (value: string): [string, boolean] =>
  value.startsWith(CASE) ? [value.slice(CASE.length), true] : [value, false];

/**
 * A pattern from a query's text (between its slashes), with whether it ignores case (its flag
 * `i`), as a query has it: without escapes before a slash (which only the text needs).
 *
 * @throws {SyntaxError} (a `PatternError`) for a pattern that isn't one.
 */
export function readPattern(source: string, ignoreCase: boolean): string {
  translate(source, true);
  return (ignoreCase ? CASE : "") + source.replace(/\\[^]/g, (escape) => (escape === "\\/" ? "/" : escape));
}

/**
 * A query's pattern, checked, as `readPattern()` writes it.
 *
 * @throws {SyntaxError} (a `PatternError`, where in `value`) for a pattern that isn't one.
 */
export function checkPattern(value: string): string {
  const [source, ignoreCase] = split(value);
  try {
    return readPattern(source, ignoreCase);
  } catch (err) {
    (err as PatternError).at += value.length - source.length;
    throw err;
  }
}

/** A (checked) pattern as JavaScript's `RegExp`. */
export function patternRegExp(value: string): RegExp {
  const [source, ignoreCase] = split(value);
  return new RegExp(translate(source, true), ignoreCase ? "iu" : "u");
}

/** A (checked) pattern for the code: a regex as Polars, pandas and PyArrow read it. */
export function patternCode(value: string): string {
  const [source, ignoreCase] = split(value);
  return (ignoreCase ? CASE : "") + translate(source, false);
}

// (A query's text can't have a line break in a pattern, but the escape for it means the same)
const ESCAPES: Record<string, string> = { "/": "\\/", "\n": "\\n", "\r": "\\r" };

/** A (checked) pattern as a query's text has it: between slashes, with the flag `i` to ignore case. */
export function formatPattern(value: string): string {
  const [source, ignoreCase] = split(value);
  return `/${source.replace(/\\[^]|[/\n\r]/g, (part) => ESCAPES[part] ?? part)}/${ignoreCase ? "i" : ""}`;
}
