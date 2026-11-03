import { describe, expect, it } from "vitest";
import { csvCell, toCSV, toTSV } from "../src/export";

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
});
