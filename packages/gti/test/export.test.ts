import { describe, expect, it } from "vitest";
import { csvCell, recordsJSON, toCSV, toRecords, toTSV } from "../src/export";

describe("csvCell", () => {
  it("quotes cells with commas, double quotes or line breaks", () => {
    expect(csvCell("plain text")).toBe("plain text");
    expect(csvCell("")).toBe("");
    expect(csvCell("a,b")).toBe('"a,b"');
    expect(csvCell('say "hi"')).toBe('"say ""hi"""');
    expect(csvCell("one\ntwo")).toBe('"one\ntwo"');
    expect(csvCell("one\r\ntwo")).toBe('"one\r\ntwo"');
  });

  it("guards cells a spreadsheet would read as a formula", () => {
    expect(csvCell("=SUM(A1:A9)")).toBe("'=SUM(A1:A9)");
    expect(csvCell("+cmd")).toBe("'+cmd");
    expect(csvCell("-cmd")).toBe("'-cmd");
    expect(csvCell("@SUM(A1)")).toBe("'@SUM(A1)");
    expect(csvCell("\tx")).toBe("'\tx");
    expect(csvCell("\rx")).toBe("\"'\rx\"");
    // (Then quotes them as any other)
    expect(csvCell('=HYPERLINK("x","y")')).toBe('"\'=HYPERLINK(""x"",""y"")"');
    // (Not a formula character later on)
    expect(csvCell("a=b")).toBe("a=b");
  });

  it("doesn't guard numbers with a sign", () => {
    expect(csvCell("-1")).toBe("-1");
    expect(csvCell("+5%")).toBe("+5%");
    expect(csvCell("-0.25")).toBe("-0.25");
    expect(csvCell("-1,234.5")).toBe('"-1,234.5"');
    expect(csvCell("- 1 234,5")).toBe('"- 1 234,5"');
    // (But does a sign without digits, or with more than a number)
    expect(csvCell("-")).toBe("'-");
    expect(csvCell("-1+1")).toBe("'-1+1");
    expect(csvCell("+1)")).toBe("'+1)");
  });

  it("doesn't guard without `guard`", () => {
    expect(csvCell("=SUM(A1)", false)).toBe("=SUM(A1)");
    expect(csvCell("=a,b", false)).toBe('"=a,b"');
  });
});

describe("toCSV", () => {
  it("writes rows of cells, each line ending in CRLF", () => {
    expect(
      toCSV([
        ["name", "value"],
        ["a, b", "=1+1"],
        ["", "-2"],
      ]),
    ).toBe('name,value\r\n"a, b",\'=1+1\r\n,-2\r\n');
    expect(toCSV([["=1"]], false)).toBe("=1\r\n");
    expect(toCSV([])).toBe("");
  });
});

describe("toTSV", () => {
  it("writes rows of cells, with their tabs and line breaks as spaces", () => {
    expect(
      toTSV([
        ["name", "value"],
        ["a\tb", "one\r\ntwo"],
        ["=1", 'say "hi"'],
      ]),
    ).toBe('name\tvalue\na b\tone  two\n=1\tsay "hi"');
    expect(toTSV([])).toBe("");
  });
  it("guards cells a spreadsheet would read as a formula, with `guard`", () => {
    expect(toTSV([["=1", "-2", "@x", "a=b"]], true)).toBe("'=1\t-2\t'@x\ta=b");
    // (A tab or line break first is a space by then)
    expect(toTSV([["\t=1", "\rx"]], true)).toBe(" =1\t x");
  });
});

describe("toRecords", () => {
  it("makes an object of each row, its cells under their keys, in order", () => {
    const records = toRecords(["a", "b"], [["1", "2"], ["3"]]);
    expect(records).toEqual([
      { a: "1", b: "2" },
      { a: "3", b: "" },
    ]);
    expect(Object.keys(records[0] as object)).toEqual(["a", "b"]);
    // (A key that's an object's own property, too)
    expect(JSON.stringify(toRecords(["__proto__", "constructor"], [["x", "y"]]))).toBe('[{"__proto__":"x","constructor":"y"}]');
    expect(toRecords(["a"], [])).toEqual([]);
  });
});

describe("recordsJSON", () => {
  it("writes records as JSON.stringify() indents them, with their keys in order", () => {
    const keys = ["name", "2021", "say \"hi\""];
    const rows = [
      ["a\nb", "1", "é"],
      ["", "2", "\u2028"],
    ];
    const text = recordsJSON(keys, rows);
    expect(text).toBe(
      '[\n  {\n    "name": "a\\nb",\n    "2021": "1",\n    "say \\"hi\\"": "é"\n  },\n' +
        '  {\n    "name": "",\n    "2021": "2",\n    "say \\"hi\\"": "\u2028"\n  }\n]\n',
    );
    expect(JSON.parse(text)).toEqual(toRecords(keys, rows));
    // (As JSON.stringify() has them, but the keys' order)
    expect(recordsJSON(["a", "b"], [["1", "2"]])).toBe(`${JSON.stringify([{ a: "1", b: "2" }], null, 2)}\n`);
    expect(recordsJSON(["a"], [])).toBe("[]\n");
    expect(recordsJSON([], [[]])).toBe(`${JSON.stringify([{}], null, 2)}\n`);
  });
});
