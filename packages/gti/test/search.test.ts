import { describe, expect, it } from "vitest";
import { fold, searchTerms } from "../src/index";
import { CellText, rowMatches, type TextRange } from "../src/search";

function cell(html: string): HTMLTableCellElement {
  const tr = document.createElement("tr");
  tr.innerHTML = `<td>${html}</td>`;
  return tr.firstElementChild as HTMLTableCellElement;
}

// The text each range covers (ranges within a cell, in document order)
function covered(ranges: TextRange[]): string[] {
  return ranges.map((r) => {
    const range = document.createRange();
    range.setStart(r.startNode, r.startOffset);
    range.setEnd(r.endNode, r.endOffset);
    return range.toString();
  });
}

describe("fold()", () => {
  it("ignores case and accents", () => {
    expect(fold("Café CRÈME")).toBe("cafe creme");
    expect(fold("İstanbul")).toBe("istanbul");
    expect(fold("Ångström")).toBe("angstrom");
  });

  it("matches decomposed and composed text alike", () => {
    expect(fold("e\u0301")).toBe(fold("\u00e9"));
    expect(fold("한국")).toBe(fold("한국".normalize("NFD")));
  });
});

describe("searchTerms()", () => {
  it("splits a search into folded words", () => {
    expect(searchTerms("  Café   au\tLAIT ")).toEqual(["cafe", "au", "lait"]);
  });

  it("has no terms for a blank search", () => {
    expect(searchTerms("")).toEqual([]);
    expect(searchTerms(" \n ")).toEqual([]);
  });
});

describe("CellText", () => {
  it("folds a cell's text", () => {
    expect(new CellText(cell("Ca<b>fé</b> au lait")).folded).toBe("cafe au lait");
  });

  it("leaves out footnote marks", () => {
    const text = new CellText(cell(`10<span class="gt_footnote_marks">1</span>`));
    expect(text.folded).toBe("10");
  });

  it("searches the names of images and flags, but not the text of plots", () => {
    const html =
      `<img src="x.png" alt="Logo">` +
      `<svg role="img"><title>United States</title><text>US</text></svg>` +
      `<svg aria-label="Line plot"><text>42</text></svg>`;
    const text = new CellText(cell(html));
    expect(text.folded).toBe("\nlogo\nunited states");
    expect(rowMatches([text], ["united"])).toBe(true);
    expect(rowMatches([text], ["42"])).toBe(false);
    // Names aren't shown as text, so there's nothing to highlight
    expect(text.find(["logo"])).toEqual([]);
  });

  it("finds every match, across text nodes", () => {
    const text = new CellText(cell("Ca<b>fé</b> au lait, café"));
    expect(covered(text.find(["fe"]))).toEqual(["fé", "fé"]);
    expect(covered(text.find(["afe"]))).toEqual(["afé", "afé"]);
    expect(covered(text.find(["cafe", "lait"]))).toEqual(["Café", "café", "lait"]);
  });

  it("maps matches back to text whose folded length differs", () => {
    // A decomposed accent is dropped; a Hangul syllable decomposes into several letters
    expect(covered(new CellText(cell("Cafe\u0301 Noir")).find(["noir"]))).toEqual(["Noir"]);
    expect(covered(new CellText(cell("Cafe\u0301")).find(["caf"]))).toEqual(["Caf"]);
    expect(covered(new CellText(cell("서울 한국")).find([fold("한국")]))).toEqual(["한국"]);
    expect(covered(new CellText(cell("İstanbul")).find(["stan"]))).toEqual(["stan"]);
  });

  it("takes the accents after a match's last letter with it", () => {
    expect(covered(new CellText(cell("Cafe\u0301 noir")).find(["cafe"]))).toEqual(["Cafe\u0301"]);
    expect(covered(new CellText(cell("Cafe\u0301\u0327")).find(["e"]))).toEqual(["e\u0301\u0327"]);
    // (In the next text node too)
    expect(covered(new CellText(cell("Cafe<b>\u0301</b>")).find(["afe"]))).toEqual(["afe\u0301"]);
    // (And a match ending before the letter doesn't)
    expect(covered(new CellText(cell("Cafe\u0301")).find(["caf"]))).toEqual(["Caf"]);
  });

  it("keeps the text of a cell's blocks and lines apart, as they're shown", () => {
    const text = new CellText(cell("<div>New</div><div>York</div>"));
    expect(text.folded).toBe("new york");
    expect(text.text).toBe("New York");
    expect(text.find(["wyo"])).toEqual([]);
    expect(rowMatches([text], ["wyo"])).toBe(false);
    expect(covered(text.find(["york", "new"]))).toEqual(["York", "New"]);
    // (A match across them, as a text filter's can be, takes both)
    expect(covered(text.find(["new york"]))).toEqual(["NewYork"]);
    expect(new CellText(cell("one<br>two<p>three</p>four")).folded).toBe("one two three four");
    expect(new CellText(cell("<ul><li>a</li><li>b</li></ul>")).text).toBe("a b");
    // (Inline elements run on, as they're shown: "m²")
    expect(new CellText(cell("m<sup>2</sup> <b>bold</b>er")).folded).toBe("m2 bolder");
  });

  it("finds nothing in an empty cell", () => {
    expect(new CellText(cell("")).find(["a"])).toEqual([]);
  });
});

describe("rowMatches()", () => {
  const row = [new CellText(cell("row_1")), new CellText(cell("20")), new CellText(cell("Bébé"))];

  it("needs every term in one of the row's cells", () => {
    expect(rowMatches(row, ["row_1", "bebe"])).toBe(true);
    expect(rowMatches(row, ["20", "nope"])).toBe(false);
  });

  it("doesn't match a term across cells", () => {
    expect(rowMatches(row, ["120"])).toBe(false);
  });
});
