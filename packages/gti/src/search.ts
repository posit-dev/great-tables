/**
 * Search: matching rows by the text their cells show.
 *
 * Matching ignores case and accents ("cafe" finds "Café"). A search is split into terms at
 * whitespace, and a row matches when every term is in one of its cells. The text of each cell is
 * kept with a map back to the cell's text nodes, so that matches can be highlighted.
 */

// Removes combining marks once characters are decomposed (NFD)
const MARKS = /\p{M}/gu;
const ASCII = /^[\x00-\x7f]*$/;

/** Text folded for matching: decomposed, without combining marks, lowercased. */
export function fold(text: string): string {
  return ASCII.test(text) ? text.toLowerCase() : foldMapped(text).folded;
}

/**
 * Fold text one character at a time, keeping where each folded character came from (folding can
 * change the length: a decomposed Hangul syllable is longer, an accented letter may be shorter).
 */
function foldMapped(text: string): { folded: string; starts: number[]; ends: number[] } {
  let folded = "";
  const starts: number[] = [];
  const ends: number[] = [];
  let i = 0;
  for (const char of text) {
    const out = char.normalize("NFD").replace(MARKS, "").toLowerCase();
    folded += out;
    for (let k = 0; k < out.length; k++) {
      starts.push(i);
      ends.push(i + char.length);
    }
    i += char.length;
  }
  return { folded, starts, ends };
}

/** The terms of a search, folded; empty for a blank search. */
export function searchTerms(search: string): string[] {
  return fold(search).split(/\s+/).filter((term) => term !== "");
}

/** Where a range of a cell's text is: a start and an end in its text nodes. */
export interface TextRange {
  startNode: Text;
  startOffset: number;
  endNode: Text;
  endOffset: number;
}

/** The searchable text of one cell. */
export class CellText {
  /** The folded text: the shown text, then (after a newline) text that isn't shown, like `alt`. */
  readonly folded: string;
  private readonly nodes: Text[];
  /** Where each node starts in the shown text. */
  private readonly offsets: number[];
  /** How much of `folded` is the shown text. */
  private readonly shownLength: number;
  /** For text that isn't ASCII: where each folded character starts and ends in the shown text. */
  private readonly starts: number[] | null;
  private readonly ends: number[] | null;

  constructor(cell: Element) {
    const nodes: Text[] = [];
    const extra: string[] = [];
    collect(cell, nodes, extra);

    const offsets: number[] = [];
    let shown = "";
    for (const node of nodes) {
      offsets.push(shown.length);
      shown += node.data;
    }
    this.nodes = nodes;
    this.offsets = offsets;

    if (ASCII.test(shown)) {
      this.starts = null;
      this.ends = null;
      this.shownLength = shown.length;
      this.folded = shown.toLowerCase();
    } else {
      const mapped = foldMapped(shown);
      this.starts = mapped.starts;
      this.ends = mapped.ends;
      this.shownLength = mapped.folded.length;
      this.folded = mapped.folded;
    }
    if (extra.length > 0) {
      this.folded += `\n${fold(extra.join("\n"))}`;
    }
  }

  /** Where `terms` are in the shown text (not in text that isn't shown). */
  find(terms: readonly string[]): TextRange[] {
    const found: TextRange[] = [];
    const shown = this.folded.slice(0, this.shownLength);
    for (const term of terms) {
      for (let at = shown.indexOf(term); at >= 0; at = shown.indexOf(term, at + term.length)) {
        const last = at + term.length - 1;
        const start = this.starts === null ? at : (this.starts[at] as number);
        const end = this.ends === null ? last + 1 : (this.ends[last] as number);
        const [startNode, startOffset] = this.position(start, false);
        const [endNode, endOffset] = this.position(end, true);
        found.push({ startNode, startOffset, endNode, endOffset });
      }
    }
    return found;
  }

  // The text node and offset of a position in the shown text. At a boundary between two nodes, a
  // start is at the beginning of the second and an end at the end of the first.
  private position(offset: number, isEnd: boolean): [Text, number] {
    let i = this.nodes.length - 1;
    while (i > 0) {
      const start = this.offsets[i] as number;
      if (isEnd ? start < offset : start <= offset) {
        break;
      }
      i--;
    }
    return [this.nodes[i] as Text, offset - (this.offsets[i] as number)];
  }
}

// Footnote marks aren't part of a cell's value
const SKIPPED = "gt_footnote_marks";

function collect(node: Node, nodes: Text[], extra: string[]): void {
  for (const child of node.childNodes) {
    if (child.nodeType === Node.TEXT_NODE) {
      nodes.push(child as Text);
    } else if (child.nodeType === Node.ELEMENT_NODE) {
      const el = child as Element;
      const tag = el.localName;
      if (tag === "svg") {
        // Icons, flags and plots: only the name (a flag's <title>), not the plot's text
        const title = el.querySelector(":scope > title")?.textContent?.trim();
        if (title) {
          extra.push(title);
        }
      } else if (tag === "img") {
        const alt = el.getAttribute("alt")?.trim();
        if (alt) {
          extra.push(alt);
        }
      } else if (tag !== "script" && tag !== "style" && tag !== "template" && !el.classList.contains(SKIPPED)) {
        collect(el, nodes, extra);
      }
    }
  }
}

/** Whether a row (the text of its cells) has every term in one of its cells. */
export function rowMatches(cells: readonly CellText[], terms: readonly string[]): boolean {
  return terms.every((term) => cells.some((cell) => cell.folded.includes(term)));
}
