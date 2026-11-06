import { describe, expect, it } from "vitest";
import { checkPattern, formatPattern, type PatternError, patternCode, patternRegExp, readPattern } from "../src/pattern";

const error = (value: string) => {
  try {
    checkPattern(value);
  } catch (err) {
    expect(err).toBeInstanceOf(SyntaxError);
    return [(err as Error).message, (err as PatternError).at];
  }
  throw new Error(`${JSON.stringify(value)} is a pattern`);
};

const matches = (value: string, text: string) => patternRegExp(checkPattern(value)).test(text);

describe("checkPattern", () => {
  it("takes a pattern, as a query has it", () => {
    for (const value of ["a", "^st\\.", "(?i)[a-z]+$", "\\d\\D\\w\\W\\s\\S", "[\\d_]", "a{2}b{2,}?c{2,5}", "(?:a)|(b)*?", "[-a-]", "😀{2}", "[😀-😂]", "\\n\\t\\r\\f\\v"]) {
      expect(checkPattern(value)).toBe(value);
    }
  });

  it("takes escapes before a slash out (only a query's text needs them)", () => {
    expect(checkPattern("a\\/b[\\/]")).toBe("a/b[/]");
    expect(checkPattern("(?i)\\\\/")).toBe("(?i)\\\\/");
  });

  it("says what's wrong, and where", () => {
    expect(error("")).toEqual(["expected a pattern", 0]);
    expect(error("(?i)")).toEqual(["expected a pattern", 4]);
    expect(error("a\\")).toEqual(['expected a character after "\\"', 1]);
    expect(error("[\\D]")).toEqual(['"\\D" can\'t be in a class', 1]);
    expect(error("(?i)a\\b")).toEqual([
      '"\\b" isn\'t an escape a pattern can have (\\d, \\w, \\s, \\D, \\W, \\S, \\n, \\t, \\r, \\f, \\v, or \\ before punctuation)',
      5,
    ]);
    expect(error("\\é")[0]).toMatch(/^"\\é" isn't an escape/);
    expect(error("[]")).toEqual(['a class can\'t be empty (a "]" in it must be escaped: "\\]")', 1]);
    expect(error("[^]")).toEqual(['a class can\'t be empty (a "]" in it must be escaped: "\\]")', 2]);
    expect(error("[a")).toEqual(['expected "]"', 2]);
    expect(error("[[]")).toEqual(['"[" in a class must be escaped: "\\["', 1]);
    expect(error("[a-[]")).toEqual(['"[" in a class must be escaped: "\\["', 3]);
    expect(error("[z-a]")).toEqual(['the range "z-a" is out of order', 1]);
    expect(error("[a-\\d]")).toEqual(['"\\d" can\'t be in a range', 3]);
    expect(error("[\\w-z]")).toEqual(['"\\w" can\'t be in a range', 1]);
    const brace = '"{" must start a repeat, as in {2}, {2,} or {2,5} (or be escaped: "\\{")';
    expect(error("a{2")).toEqual([brace, 1]);
    expect(error("a{,2}")).toEqual([brace, 1]);
    expect(error("{")).toEqual([brace, 0]);
    const bound = "a repeat can be at most 1000, and its first number no more than its second";
    expect(error("a{2,1}")).toEqual([bound, 1]);
    expect(error("a{1001}")).toEqual([bound, 1]);
    expect(error("a{0,1001}")).toEqual([bound, 1]);
    expect(error("*")).toEqual(['"*" must follow something to repeat', 0]);
    expect(error("a**")).toEqual(['"*" must follow something to repeat', 2]);
    expect(error("(+)")).toEqual(['"+" must follow something to repeat', 1]);
    expect(error("a|?")).toEqual(['"?" must follow something to repeat', 2]);
    expect(error("^{2}")).toEqual(['"{" must follow something to repeat', 1]);
    expect(error("a???")).toEqual(['"?" must follow something to repeat', 3]);
    const group = '"(?" must be "(?:" (a pattern can\'t have lookarounds, named groups or flags)';
    expect(error("(?=a)")).toEqual([group, 0]);
    expect(error("a(?i)")).toEqual([group, 1]);
    expect(error("(?i)(?i)a")).toEqual([group, 4]);
    expect(error(")")).toEqual(['")" must close a "(" (or be escaped: "\\)")', 0]);
    expect(error("]")).toEqual(['"]" must be escaped: "\\]"', 0]);
    expect(error("a}")).toEqual(['"}" must be escaped: "\\}"', 1]);
    expect(error("(a")).toEqual(['expected ")"', 2]);
  });

  it("counts UTF-16 code units", () => {
    expect(error("😀)")).toEqual(['")" must close a "(" (or be escaped: "\\)")', 2]);
  });
});

describe("readPattern", () => {
  it("reads a query's pattern, with whether it ignores case", () => {
    expect(readPattern("a\\/b", false)).toBe("a/b");
    expect(readPattern("a", true)).toBe("(?i)a");
    // (A query's text has the flag i, not (?i))
    expect(() => readPattern("(?i)a", false)).toThrow(SyntaxError);
  });
});

describe("patternRegExp", () => {
  it("finds a match anywhere, with case", () => {
    expect(matches("st\\.", "Rue st. Denis")).toBe(true);
    expect(matches("St\\.", "Rue st. Denis")).toBe(false);
    expect(matches("(?i)St\\.", "Rue st. Denis")).toBe(true);
    expect(matches("^Rue", "Rue st. Denis")).toBe(true);
    expect(matches("^st", "Rue st. Denis")).toBe(false);
    expect(matches("Denis$", "Rue st. Denis")).toBe(true);
    // (Not before a line break at the end)
    expect(matches("Denis$", "Rue st. Denis\n")).toBe(false);
  });

  it("has ASCII's digits, word characters and white space", () => {
    expect(matches("^\\d+$", "123")).toBe(true);
    expect(matches("\\d", "١")).toBe(false);
    expect(matches("^\\w+$", "a_Z9")).toBe(true);
    expect(matches("\\w", "é")).toBe(false);
    expect(matches("\\W", "é")).toBe(true);
    expect(matches("^\\s+$", " \t\n\v\f\r")).toBe(true);
    expect(matches("\\s", "\u00a0")).toBe(false);
    expect(matches("[^\\s\\d]", " 1")).toBe(false);
  });

  it("has . match any character but a line break, and whole characters", () => {
    expect(matches("a.b", "a\rb")).toBe(true);
    expect(matches("a.b", "a\nb")).toBe(false);
    expect(matches("^.$", "😀")).toBe(true);
    expect(matches("^[😀-😂]{2}$", "😁😂")).toBe(true);
  });

  it("ignores case as Python does, with (?i)", () => {
    expect(matches("(?i)^[a-z]+$", "ABC")).toBe(true);
    expect(matches("(?i)^k$", "\u212a")).toBe(true);
    expect(matches("(?i)^é$", "É")).toBe(true);
  });

  it("has characters that are syntax elsewhere as themselves in a class", () => {
    expect(matches("^[&~|]+$", "&~|")).toBe(true);
    expect(matches("^[-a-]+$", "-a-")).toBe(true);
    expect(matches("^[\\^\\]\\\\]+$", "^]\\")).toBe(true);
    expect(matches("^[/]$", "/")).toBe(true);
  });
});

describe("patternCode", () => {
  it("writes a pattern for Polars, pandas and PyArrow", () => {
    expect(patternCode("(?i)^st\\.")).toBe("(?i)^st\\.");
    expect(patternCode("a.\\d\\S")).toBe("a.[0-9][^\\t\\n\\v\\f\\r ]");
    expect(patternCode("[\\w&~|-]")).toBe("[0-9A-Z_a-z\\&\\~\\|\\-]");
    expect(patternCode("(a)\\/")).toBe("(?:a)/");
  });
});

describe("formatPattern", () => {
  it("writes a pattern between slashes, with the flag i, escaping a slash", () => {
    expect(formatPattern("^st\\.")).toBe("/^st\\./");
    expect(formatPattern("(?i)a/b[/]")).toBe("/a\\/b[\\/]/i");
    expect(formatPattern("\\\\/")).toBe("/\\\\\\//");
    for (const value of ["a/b", "(?i)[/]", "\\\\/", "\\/"]) {
      const [, source = "", flags] = /^\/(.*)\/(i?)$/s.exec(formatPattern(value)) as RegExpExecArray;
      expect(readPattern(source, flags === "i")).toBe(checkPattern(value));
    }
  });
});
