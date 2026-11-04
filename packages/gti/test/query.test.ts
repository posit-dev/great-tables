import { describe, expect, it } from "vitest";
import { ColumnFilter, type FilterClause, type FilterQuery } from "../src/filter";
import {
  formatQuery,
  parseQuery,
  type QuerySyntaxError,
  queryContext,
  queryProblem,
  readQuery,
} from "../src/query";

const error = (text: string) => {
  try {
    parseQuery(text);
  } catch (err) {
    expect(err).toBeInstanceOf(SyntaxError);
    return (err as Error).message;
  }
  throw new Error(`${JSON.stringify(text)} parsed`);
};

describe("parseQuery", () => {
  it("reads every kind of clause, joined by and", () => {
    expect(
      parseQuery('population_2021 >= 10000 and status in ("single-tier", "city") and name contains "cote" and x <= -1.5e3'),
    ).toEqual({
      and: [
        { col: "population_2021", op: "gte", value: 10000 },
        { col: "status", op: "in", value: ["single-tier", "city"] },
        { col: "name", op: "contains", value: "cote" },
        { col: "x", op: "lte", value: -1500 },
      ],
    });
  });

  it("reads no query from empty text", () => {
    expect(parseQuery("")).toBeNull();
    expect(parseQuery(" \t\n ")).toBeNull();
  });

  it("reads keywords in any case, and any spacing", () => {
    expect(parseQuery('a IN(1,TRUE , False,NULL)AND b Contains"x"')).toEqual({
      and: [
        { col: "a", op: "in", value: [1, true, false, null] },
        { col: "b", op: "contains", value: "x" },
      ],
    });
  });

  it("reads any column name in backticks, with backticks doubled", () => {
    expect(parseQuery('`Name of town` contains "x" and `a``b` >= 1 and `` <= 2 and `and` in (null)')).toEqual({
      and: [
        { col: "Name of town", op: "contains", value: "x" },
        { col: "a`b", op: "gte", value: 1 },
        { col: "", op: "lte", value: 2 },
        { col: "and", op: "in", value: [null] },
      ],
    });
    // (Keywords are column names where a column goes)
    expect(parseQuery("in in (1)")).toEqual({ and: [{ col: "in", op: "in", value: [1] }] });
  });

  it("reads dates as bounds, as strings", () => {
    expect(parseQuery('d >= "2015-06-15" and d <= "2015-06-15T09:30"')).toEqual({
      and: [
        { col: "d", op: "gte", value: "2015-06-15" },
        { col: "d", op: "lte", value: "2015-06-15T09:30" },
      ],
    });
  });

  it("reads strings as JSON does", () => {
    expect(parseQuery(String.raw`a contains "q\"\\\/\b\f\n\r\té😀 Côté"`)).toEqual({
      and: [{ col: "a", op: "contains", value: 'q"\\/\b\f\n\r\té😀 Côté' }],
    });
  });

  it("doesn't check what the clauses mean", () => {
    // (The table does that, or Great Tables)
    expect(parseQuery('a >= 1 and a >= 2 and b contains ""')?.and).toHaveLength(3);
  });

  it("says what's wrong, and where", () => {
    expect(error("a")).toBe('expected "contains", "in", ">=" or "<=", at the end');
    expect(error("a = 1")).toBe('expected "contains", "in", ">=" or "<=", at character 3');
    expect(error(">= 1")).toBe("expected a column name, at character 1");
    expect(error("a >= x")).toBe("expected a number, or a date in double quotes, at character 6");
    expect(error("a >= (")).toBe("expected a number, or a date in double quotes, at character 6");
    expect(error("a contains x")).toBe("expected a string in double quotes, at character 12");
    expect(error("a in 1")).toBe('expected "(", at character 6');
    expect(error("a in ()")).toBe(
      "expected a value: a string in double quotes, a number, true, false or null, at character 7",
    );
    expect(error("a in (1 2)")).toBe('expected "," or ")", at character 9');
    expect(error("a in (1,")).toBe(
      "expected a value: a string in double quotes, a number, true, false or null, at the end",
    );
    expect(error("a >= 1 b")).toBe('expected "and", "or" or the end of the query, at character 8');
    expect(error("a >= 1 and")).toBe("expected a column name, at the end");
    expect(error("a >= 1e999")).toBe("the number 1e999 is too large, at character 6");
    expect(error('a contains "x')).toBe("a string must end with a double quote (with escapes as in JSON), at character 12");
    expect(error('a contains "\\x"')).toBe(
      "a string must end with a double quote (with escapes as in JSON), at character 12",
    );
    expect(error("`a")).toBe("a column name in backticks must end with a backtick, at the end");
    // (Numbers as JSON has them)
    expect(error("a >= .5")).toBe("expected a number, or a date in double quotes, at character 6");
    expect(error("a >= 01")).toBe('expected "and", "or" or the end of the query, at character 7');
  });

  it("counts characters, not UTF-16 code units", () => {
    expect(error('`😀` contains "😀" x')).toBe('expected "and", "or" or the end of the query, at character 18');
  });
});

describe("parseQuery, with or, not and parentheses", () => {
  const a = { col: "a", op: "gte", value: 1 } as const;
  const b = { col: "b", op: "gte", value: 2 } as const;
  const c = { col: "c", op: "contains", value: "x" } as const;

  it("binds not tighter than and, and and tighter than or", () => {
    expect(parseQuery('a >= 1 or b >= 2 and not c contains "x"')).toEqual({
      and: [{ or: [a, { and: [b, { not: c }] }] }],
    });
    expect(parseQuery('not a >= 1 and b >= 2 OR c contains "x"')).toEqual({
      and: [{ or: [{ and: [{ not: a }, b] }, c] }],
    });
  });

  it("groups in parentheses, splicing a group into one of its kind", () => {
    expect(parseQuery('(a >= 1 or b >= 2) and c contains "x"')).toEqual({ and: [{ or: [a, b] }, c] });
    expect(parseQuery('a >= 1 or (b >= 2 or c contains "x")')).toEqual({ and: [{ or: [a, b, c] }] });
    expect(parseQuery('(a >= 1 and b >= 2) and (c contains "x")')).toEqual({ and: [a, b, c] });
    expect(parseQuery("((a >= 1))")).toEqual({ and: [a] });
    expect(parseQuery("not (a >= 1 and b >= 2)")).toEqual({ and: [{ not: { and: [a, b] } }] });
    expect(parseQuery("not not a >= 1")).toEqual({ and: [{ not: { not: a } }] });
  });

  it("reads not before an op as a column's name", () => {
    expect(parseQuery("not >= 1")).toEqual({ and: [{ col: "not", op: "gte", value: 1 }] });
    expect(parseQuery('NOT contains "x" or not in (1)')).toEqual({
      and: [{ or: [{ col: "NOT", op: "contains", value: "x" }, { col: "not", op: "in", value: [1] }] }],
    });
    expect(parseQuery("not not <= 1")).toEqual({ and: [{ not: { col: "not", op: "lte", value: 1 } }] });
    expect(parseQuery("or >= 1 or and >= 2")).toEqual({
      and: [{ or: [{ col: "or", op: "gte", value: 1 }, { col: "and", op: "gte", value: 2 }] }],
    });
  });

  it("says what's wrong, and where", () => {
    expect(error("(a >= 1")).toBe('expected "and", "or" or ")", at the end');
    expect(error("(a >= 1 b")).toBe('expected "and", "or" or ")", at character 9');
    expect(error("a >= 1)")).toBe('expected "and", "or" or the end of the query, at character 7');
    expect(error("()")).toBe("expected a column name, at character 2");
    expect(error("not")).toBe("expected a column name, at the end");
    expect(error("a >= 1 or")).toBe("expected a column name, at the end");
    expect(error("a >= 1 or not")).toBe("expected a column name, at the end");
    expect(error('not "x')).toBe("a string must end with a double quote (with escapes as in JSON), at character 5");
  });
});

describe("formatQuery", () => {
  it("writes a query as text", () => {
    expect(
      formatQuery({
        and: [
          { col: "population_2021", op: "gte", value: 10000 },
          { col: "status", op: "in", value: ["single-tier", null, true, 1.5] },
          { col: "Name of town", op: "contains", value: 'a "b"' },
          { col: "a`b", op: "lte", value: -0.25 },
        ],
      }),
    ).toBe(
      'population_2021 >= 10000 and status in ("single-tier", null, true, 1.5) and `Name of town` contains "a \\"b\\"" and `a``b` <= -0.25',
    );
    expect(formatQuery(null)).toBe("");
  });

  it("writes groups with the parentheses they need", () => {
    const a: FilterClause = { col: "a", op: "gte", value: 1 };
    const b: FilterClause = { col: "b", op: "in", value: [2] };
    const c: FilterClause = { col: "c", op: "contains", value: "x" };
    expect(formatQuery({ and: [{ or: [a, { and: [b, c] }] }] })).toBe('a >= 1 or b in (2) and c contains "x"');
    expect(formatQuery({ and: [a, { or: [b, c] }] })).toBe('a >= 1 and (b in (2) or c contains "x")');
    expect(formatQuery({ and: [{ not: { or: [a, b] } }] })).toBe("not (a >= 1 or b in (2))");
    expect(formatQuery({ and: [{ not: { and: [a, b] } }, c] })).toBe('not (a >= 1 and b in (2)) and c contains "x"');
    expect(formatQuery({ and: [{ not: { not: a } }] })).toBe("not not a >= 1");
    // (A column named as a keyword that goes after a column, in backticks)
    expect(formatQuery({ and: [{ col: "in", op: "in", value: [1] }, { col: "Contains", op: "gte", value: 1 }] })).toBe(
      "`in` in (1) and `Contains` >= 1",
    );
  });

  it("writes what parseQuery reads back", () => {
    const queries: FilterQuery[] = [
      { and: [{ col: "", op: "contains", value: "" }] },
      { and: [{ col: "``", op: "in", value: ["\n", "\u0000", "é", 1e21, 5e-7] }] },
      { and: [{ col: "1a", op: "gte", value: -1 }, { col: "_", op: "lte", value: 0 }] },
      { and: [{ col: "and", op: "in", value: [false] }] },
      { and: [{ col: "d", op: "gte", value: "2015-06-15" }, { col: "d", op: "lte", value: "2015-06-15T09:30:00.5" }] },
      { and: [{ col: "in", op: "in", value: [1] }, { not: { col: "contains", op: "contains", value: "x" } }] },
      { and: [{ not: { col: "not", op: "gte", value: 1 } }, { or: [{ col: "or", op: "lte", value: 1 }, { col: "and", op: "in", value: [null] }] }] },
      {
        and: [
          { col: "a", op: "gte", value: 1 },
          { or: [{ and: [{ col: "b", op: "in", value: [1] }, { not: { or: [{ col: "c", op: "lte", value: 2 }, { not: { col: "d", op: "contains", value: "y" } }] } }] }, { col: "e", op: "gte", value: 3 }] },
          { not: { and: [{ col: "f", op: "gte", value: 0 }, { col: "g", op: "lte", value: 0 }] } },
        ],
      },
      { and: [{ or: [{ col: "a", op: "gte", value: 1 }, { col: "b", op: "gte", value: 2 }] }] },
    ];
    for (const query of queries) {
      expect(parseQuery(formatQuery(query))).toEqual(query);
    }
  });
});

describe("syntax errors", () => {
  const where = (text: string) => {
    try {
      parseQuery(text);
    } catch (err) {
      const { from, to } = err as QuerySyntaxError;
      return text.slice(from, to);
    }
    throw new Error(`${JSON.stringify(text)} parsed`);
  };

  it("say where the token that's wrong is, to mark it", () => {
    expect(where("a >= x")).toBe("x");
    expect(where("a in (1, ) ")).toBe(")");
    expect(where('a contains "x" b')).toBe("b");
    expect(where('(a contains "x" b')).toBe("b");
    expect(where('a contains "x')).toBe('"');
    expect(where("a >= 1e999")).toBe("1e999");
    expect(where("😀 >= 1")).toBe("😀");
    // (Nothing, for one at the end)
    expect(where("a >= ")).toBe("");
    expect(where("`a")).toBe("");
  });
});

describe("readQuery", () => {
  const roles = (text: string) => readQuery(text).parts.map((part) => [part.text, part.role]);

  it("says what each part of a query is", () => {
    expect(roles('`a b` in ("x", null) and c >= -1 AND d contains "y"')).toEqual([
      ["`a b`", "column"],
      ["in", "keyword"],
      ["(", "punct"],
      ['"x"', "string"],
      [",", "punct"],
      ["null", "literal"],
      [")", "punct"],
      ["and", "keyword"],
      ["c", "column"],
      [">=", "keyword"],
      ["-1", "number"],
      ["AND", "keyword"],
      ["d", "column"],
      ["contains", "keyword"],
      ['"y"', "string"],
    ]);
    expect(roles('d >= "2015-06-15"')).toEqual([
      ["d", "column"],
      [">=", "keyword"],
      ['"2015-06-15"', "string"],
    ]);
  });

  it("reads strings and names in backticks being typed", () => {
    expect(roles('a contains "x y')).toEqual([
      ["a", "column"],
      ["contains", "keyword"],
      ['"x y', "string"],
    ]);
    const { parts } = readQuery("`a ``b");
    expect(parts.map((part) => [part.text, part.open])).toEqual([["`a ``b", true]]);
  });

  it("reads on from an and, past what doesn't fit", () => {
    expect(roles("a >= x and b >= 1")).toEqual([
      ["a", "column"],
      [">=", "keyword"],
      ["x", null],
      ["and", "keyword"],
      ["b", "column"],
      [">=", "keyword"],
      ["1", "number"],
    ]);
  });

  it("says where each clause is", () => {
    const text = 'a in (1, 2) and  b contains "and" and c <= 3';
    expect(readQuery(text).clauses.map(([from, to]) => text.slice(from, to))).toEqual([
      "a in (1, 2)",
      'b contains "and"',
      "c <= 3",
    ]);
  });

  it("reads groups, and not before an op as a column", () => {
    expect(roles("not (a >= 1 or b in (2)) and c >= 3")).toEqual([
      ["not", "keyword"],
      ["(", "punct"],
      ["a", "column"],
      [">=", "keyword"],
      ["1", "number"],
      ["or", "keyword"],
      ["b", "column"],
      ["in", "keyword"],
      ["(", "punct"],
      ["2", "number"],
      [")", "punct"],
      [")", "punct"],
      ["and", "keyword"],
      ["c", "column"],
      [">=", "keyword"],
      ["3", "number"],
    ]);
    expect(roles("not not in (1)")).toEqual([
      ["not", "keyword"],
      ["not", "column"],
      ["in", "keyword"],
      ["(", "punct"],
      ["1", "number"],
      [")", "punct"],
    ]);
    // (A ")" without a group to close doesn't fit)
    expect(roles("a >= 1)")).toEqual([
      ["a", "column"],
      [">=", "keyword"],
      ["1", "number"],
      [")", null],
    ]);
  });

  it("reads on from an or, past what doesn't fit, and says where each clause in a group is", () => {
    expect(roles("a >= x or b >= 1").map(([, role]) => role)).toEqual(["column", "keyword", null, "keyword", "column", "keyword", "number"]);
    const text = '(a in (1) or not b <= 2) and c contains "or"';
    expect(readQuery(text).clauses.map(([from, to]) => text.slice(from, to))).toEqual([
      "a in (1)",
      "b <= 2",
      'c contains "or"',
    ]);
    expect(readQuery("not >= 1").clauses).toEqual([[0, 8]]);
  });
});

describe("queryContext", () => {
  // (The caret at the `|`)
  const at = (text: string) => {
    const caret = text.indexOf("|");
    const { expect, col, values, prefix, from, to, depth } = queryContext(text.replace("|", ""), caret);
    return { expect, col, values, prefix, from, to, depth };
  };

  it("says what goes at the caret", () => {
    expect(at("|")).toMatchObject({ expect: "column", prefix: "" });
    expect(at("pop|")).toMatchObject({ expect: "column", prefix: "pop", from: 0, to: 3 });
    expect(at("po|p")).toMatchObject({ expect: "column", prefix: "po", from: 0, to: 3 });
    expect(at("`Name o|")).toMatchObject({ expect: "column", prefix: "`Name o" });
    expect(at("pop |")).toMatchObject({ expect: "op", col: "pop", prefix: "" });
    expect(at("`a``b` co|")).toMatchObject({ expect: "op", col: "a`b", prefix: "co" });
    expect(at("pop >|")).toMatchObject({ expect: "op", col: "pop", prefix: ">" });
    expect(at("pop >= |")).toMatchObject({ expect: "bound" });
    expect(at('d >= "2015|"')).toMatchObject({ expect: "bound", col: "d", prefix: '"2015', from: 5, to: 11 });
    expect(at("s in |")).toMatchObject({ expect: "(" });
    expect(at("s in (|")).toMatchObject({ expect: "value", col: "s", values: [] });
    expect(at('s in ("a", nu|')).toMatchObject({ expect: "value", col: "s", values: ["a"], prefix: "nu" });
    expect(at('s in ("a", "b|')).toMatchObject({ expect: "value", values: ["a"], prefix: '"b' });
    expect(at('s in ("a"|')).toMatchObject({ expect: "value", values: [], prefix: '"a"' });
    expect(at('s in ("a" |')).toMatchObject({ expect: ",)", values: ["a"] });
    expect(at("s in (1) |")).toMatchObject({ expect: "and" });
    expect(at("s in (1) an|")).toMatchObject({ expect: "and", prefix: "an" });
    expect(at("s in (1) and |")).toMatchObject({ expect: "column" });
    // (Before the rest of the text)
    expect(at("s |in (1)")).toMatchObject({ expect: "op", prefix: "", from: 2, to: 2 });
  });

  it("says nothing goes inside a number, or where the text doesn't fit", () => {
    expect(at("pop >= 1|0").expect).toBeNull();
    expect(at("pop >= 10|").expect).toBe("and");
    expect(at("pop = |").expect).toBeNull();
    expect(at("pop = 1 and |").expect).toBe("column");
  });

  it("says what goes in and after a group", () => {
    expect(at("(|")).toMatchObject({ expect: "column", depth: 1 });
    expect(at("not |")).toMatchObject({ expect: "column", depth: 0 });
    expect(at("not (not |")).toMatchObject({ expect: "column", depth: 1 });
    expect(at("not >|")).toMatchObject({ expect: "op", col: "not", prefix: ">" });
    expect(at("(a >= 1 |")).toMatchObject({ expect: "and", depth: 1 });
    expect(at("(a >= 1) |")).toMatchObject({ expect: "and", depth: 0 });
    expect(at("a >= 1 o|")).toMatchObject({ expect: "and", prefix: "o" });
    expect(at("a >= 1 or |")).toMatchObject({ expect: "column" });
  });
});

describe("queryProblem", () => {
  const filters = [
    new ColumnFilter({ column: "x", type: "range", values: [5, 10, 20] }, 1, []),
    new ColumnFilter({ column: "y", type: "facet", values: ["a", "b", 1] }, 2, []),
    new ColumnFilter({ column: "z z", type: "text", values: null }, 3, []),
    new ColumnFilter({ column: "d", type: "date", values: ["2015-06-15"] }, 4, [], null, "date"),
    new ColumnFilter({ column: "t", type: "date", values: ["2015-06-15T09:30:00"] }, 5, [], null, "datetime"),
    new ColumnFilter({ column: "b", type: "bool", values: [false, true] }, 6, []),
  ];
  const problem = (text: string) => queryProblem(filters, parseQuery(text));

  it("finds the first clause the filters can't have, and says why", () => {
    expect(problem('x >= 1 and y in ("a", null, 1) and `z z` contains "q"')).toBeNull();
    expect(problem("")).toBeNull();
    expect(problem('x >= 1 and w contains "a"')).toEqual({ clause: 1, message: "w isn't a column with a filter" });
    expect(problem("x in (1)")).toEqual({ clause: 0, message: "x has a range filter: use >= or <=" });
    expect(problem("`z z` >= 1")).toEqual({ clause: 0, message: "`z z` has a text filter: use contains" });
    expect(problem('y contains "a"')).toEqual({ clause: 0, message: "y has a facet filter: use in" });
    expect(problem("x >= 1 and x <= 2 and x >= 3")).toEqual({ clause: 2, message: "x has more than one >= clause" });
    expect(problem('y in ("a", "1")')).toEqual({ clause: 0, message: '"1" isn\'t a value of y' });
  });

  it("checks a range's bounds are numbers, and a date filter's dates", () => {
    expect(problem('d >= "2015-01-01" and t <= "2016-01-01" and t >= "2015-01-01T09:30:00.123456"')).toBeNull();
    expect(problem('x >= "5"')).toEqual({ clause: 0, message: "x has a range filter: give a number" });
    expect(problem("d >= 2015")).toEqual({ clause: 0, message: 'd has a date filter: give a date in double quotes ("YYYY-MM-DD")' });
    expect(problem('d in ("2015-06-15")')).toEqual({ clause: 0, message: "d has a date filter: use >= or <=" });
    expect(problem('d <= "2015-06-15T09:30"')).toEqual({
      clause: 0,
      message: '"2015-06-15T09:30" isn\'t a date ("YYYY-MM-DD"), and d has dates without times',
    });
    expect(problem('t <= "June 15"')).toEqual({
      clause: 0,
      message: '"June 15" isn\'t a date ("YYYY-MM-DD") or date and time ("YYYY-MM-DDTHH:MM:SS")',
    });
  });

  it("takes one value of a bool filter", () => {
    expect(problem("b in (true) and x >= 1")).toBeNull();
    expect(problem("b in (null)")).toBeNull();
    expect(problem("b in (true, false)")).toEqual({ clause: 0, message: "b has a bool filter: give one value, true, false or null" });
    expect(problem('b in ("true")')).toEqual({ clause: 0, message: '"true" isn\'t a value of b' });
    expect(problem("b >= 1")).toEqual({ clause: 0, message: "b has a bool filter: use in" });
  });
  it("checks the clauses in groups, each and on its own", () => {
    expect(problem('x >= 1 or w contains "a"')).toEqual({ clause: 1, message: "w isn't a column with a filter" });
    expect(problem('(x >= 1 and x >= 2) or y in ("a")')).toEqual({ clause: 1, message: "x has more than one >= clause" });
    expect(problem("x >= 1 or x >= 2")).toBeNull();
    expect(problem('x >= 1 and (x >= 2 or y in ("a"))')).toBeNull();
    expect(problem("x >= 1 and not x >= 2")).toBeNull();
    // (An and in parentheses at the top is the query's)
    expect(problem("x >= 1 and (x <= 5 and x >= 2)")).toEqual({ clause: 2, message: "x has more than one >= clause" });
    expect(problem('not y in ("c")')).toEqual({ clause: 0, message: '"c" isn\'t a value of y' });
    expect(problem("not b in (true, false)")).toEqual({ clause: 0, message: "b has a bool filter: give one value, true, false or null" });
  });

  it("takes blank text only outside a group (where it keeps every row)", () => {
    expect(problem('`z z` contains " "')).toBeNull();
    expect(problem('x >= 1 or `z z` contains ""')).toEqual({ clause: 1, message: '`z z` needs text to look for, in an "or" or a "not"' });
    expect(problem('not `z z` contains " "')).toEqual({ clause: 0, message: '`z z` needs text to look for, in an "or" or a "not"' });
  });
});
