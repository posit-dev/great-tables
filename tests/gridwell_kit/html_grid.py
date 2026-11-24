"""The L1 grid of a table as gt or Great Tables draws it, read from its own HTML.

`gridwell conformance normalize --tier L1` writes the grid an emitter's IR gives;
this writes the grid the package's `as_raw_html()` shows, so the two can be
compared without trusting either emitter. The expected L1 grids in `expected/`
come from here (see make.py).

It reads the HTML gt and Great Tables write (their `gt_*` classes), not HTML in
general, and only what L1 checks: the stub, the header lines, the head rows and
their spans, the groups and their labels, the data and summary rows and the text
of every cell, footnote and source note. Footnote marks aren't text, so they're
left out. A group whose label is in a row group column (`row_group_as_column`)
starts at that stub cell, and has no label.

The head is written as the IR's rule 4 has it: a label spanning several head rows
in the HTML (a column without a spanner above it) is the bottom row's, with empty
cells above it.

Run it on a file to print the grid:

    python conformance/html_grid.py harness/gt-reference/demographics.gt.html
"""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser

FORMAT = "gridwell-conformance-grid/1"

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "wbr"}
# Elements a browser starts a line for (the ones a label's HTML might hold).
BLOCKS = set(
    "address article aside blockquote dd div dl dt figcaption figure footer h1 h2 h3 h4 h5 h6 "
    "header hr li main nav ol p pre section table tr ul".split()
)
# Where a block starts or ends, in text() (a line break if text comes before and after).
BLOCK_EDGE = "\x00"
# A row group's label in the stub (`row_group_as_column`): a stub cell, spanning
# the group's rows, that starts the group (which has no label row then).
STUB_GROUP = "gt_stub_row_group"
# The Unicode superscript and subscript characters, as gridwell's writers draw
# `<sup>` and `<sub>` (`gridwell_layout::text`).
SCRIPTS = {
    "sup": dict(zip(
        "0123456789+-−=()abcdefghijklmnoprstuvwxyz",
        "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁼⁽⁾ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻ",
    )),
    "sub": dict(zip(
        "0123456789+-−=()aehijklmnoprstuvx",
        "₀₁₂₃₄₅₆₇₈₉₊₋₋₌₍₎ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ",
    )),
}


class Element:
    def __init__(self, tag: str, attrs: dict[str, str]):
        self.tag = tag
        self.attrs = attrs
        self.children: list[Element | str] = []

    @property
    def classes(self) -> set[str]:
        return set(self.attrs.get("class", "").split())

    def elements(self, *tags: str):
        """Child elements (with one of `tags`, if given), in document order."""
        return [c for c in self.children if isinstance(c, Element) and (not tags or c.tag in tags)]

    def find_all(self, pred):
        """Descendant elements matching `pred`, in document order."""
        for c in self.children:
            if isinstance(c, Element):
                if pred(c):
                    yield c
                yield from c.find_all(pred)


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Element("#root", {})
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        el = Element(tag, {k: v or "" for k, v in attrs})
        self.stack[-1].children.append(el)
        if tag not in VOID:
            self.stack.append(el)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Element(tag, {k: v or "" for k, v in attrs}))

    def handle_endtag(self, tag):
        # Close up to the matching element; a stray end tag closes nothing.
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def parse(html: str) -> Element:
    builder = TreeBuilder()
    builder.feed(html)
    builder.close()
    return builder.root


def text(el: Element) -> str:
    """What a reader sees, as the normalizer writes L1 text: footnote marks left
    out, `<br>` a line break, a block (`<p>`, `<div>`, ...) on lines of its own,
    a superscript or subscript in Unicode characters when every character has one
    (`m<sup>2</sup>` is `m²`), an SVG not text, white space runs one space, lines
    and the whole trimmed."""
    out: list[str] = []

    def walk(node, out):
        for c in node.children:
            if isinstance(c, str):
                # Line breaks in the source are spaces; only <br> and blocks break a line.
                out.append(re.sub(r"[\s\x00]+", " ", c))
            elif c.tag == "br":
                out.append("\n")
            elif c.tag in SCRIPTS:
                inner: list[str] = []
                walk(c, inner)
                s = "".join(inner)
                chars = SCRIPTS[c.tag]
                if all(ch in chars or ch == " " for ch in s):
                    s = "".join(chars.get(ch, ch) for ch in s)
                out.append(s)
            elif (
                c.tag not in ("style", "script", "svg")
                and "gt_footnote_marks" not in c.classes
            ):
                edge = [BLOCK_EDGE] if c.tag in BLOCKS else []
                out.extend(edge)
                walk(c, out)
                out.extend(edge)

    walk(el, out)
    # A block edge breaks the line when the line has text and more text or a <br>
    # follows (so `<p>a</p><p>b</p>` is two lines, and an empty block is nothing).
    joined, pending, has_text = [], False, False
    for piece in re.split(f"(\n|{BLOCK_EDGE})", "".join(out)):
        if piece == "\n":
            # After a block, a <br> is a line of its own.
            joined.append("\n\n" if pending else piece)
            pending = has_text = False
        elif piece == BLOCK_EDGE:
            pending = pending or has_text
        elif piece.strip():
            if pending:
                joined.append("\n")
                pending = False
            joined.append(piece)
            has_text = True
        else:
            joined.append(piece)
    lines = "".join(joined).split("\n")
    return "\n".join(" ".join(line.split()) for line in lines).strip()


def span(el: Element, name: str) -> int:
    try:
        return max(1, int(el.attrs.get(name, "1")))
    except ValueError:
        return 1


def place(rows: list[list[Element]]) -> list[list[tuple[int, Element]]]:
    """Each row's cells with the grid column they start in (HTML's table model:
    a cell takes the first column no cell from above still covers)."""
    covered: dict[tuple[int, int], bool] = {}
    placed = []
    for r, cells in enumerate(rows):
        col = 0
        out = []
        for cell in cells:
            while covered.get((r, col)):
                col += 1
            cs, rs = span(cell, "colspan"), span(cell, "rowspan")
            for dr in range(rs):
                for dc in range(cs):
                    covered[(r + dr, col + dc)] = True
            out.append((col, cell))
            col += cs
        placed.append(out)
    return placed


def cell_entry(col: int, cell: Element, *, stub: bool = False, rowspan: int = 1) -> dict:
    entry: dict = {"col": col}
    cs = span(cell, "colspan")
    if cs > 1:
        entry["colspan"] = cs
    if rowspan > 1:
        entry["rowspan"] = rowspan
    if stub:
        entry["stub"] = True
    entry["text"] = text(cell)
    return entry


def head_rows(rows: list[Element]) -> list[dict]:
    """The column-label rows in rule 4's shape: spanner rows top level first, then
    the column labels, every position filled, no label spanning rows."""
    cells = [r.elements("th", "td") for r in rows]
    placed = place(cells)
    n = len(rows)
    grid: list[list[dict]] = [[] for _ in range(n)]
    for r, row in enumerate(placed):
        for col, cell in row:
            rs = min(span(cell, "rowspan"), n - r)
            # A label spanning rows sits in the last; the rows above are empty there.
            for above in range(r, r + rs - 1):
                for dc in range(span(cell, "colspan")):
                    grid[above].append({"col": col + dc, "text": ""})
            grid[r + rs - 1].append(cell_entry(col, cell))
    out = []
    for r, row in enumerate(rows):
        role = "spanner_label" if "gt_spanner_row" in row.classes else "column_label"
        out.append({"cells": sorted(grid[r], key=lambda c: c["col"]), "role": role})
    return out


def body_groups(tbody: Element) -> list[dict]:
    """The groups of a table body: its row groups, then the grand summary (as a
    group of summary rows alone). Summary rows above all of a group's rows are at
    its top (`summary_placement`), and grand summary rows above every group are a
    group of their own at the top, as the emitters write them."""
    groups: list[dict] = []
    grand: dict | None = None
    grand_top: dict | None = None
    # Whether each group (by id) has data rows, and summary rows after them.
    has_rows: dict[int, bool] = {}
    below: dict[int, bool] = {}
    # Rows of cells, with the group (and list) each belongs to, so spans are placed
    # over the whole body as the HTML does.
    rows: list[tuple[list, list[Element], str | None]] = []
    for tr in tbody.elements("tr"):
        cells = tr.elements("th", "td")
        if "gt_group_heading_row" in tr.classes:
            label = text(cells[0]) if cells else ""
            groups.append({"label": {"text": label}, "rows": [], "summary_rows": []})
            continue
        classes = set().union(*(c.classes for c in cells)) | tr.classes
        if "gt_grand_summary_row" in classes:
            if not groups:
                if grand_top is None:
                    grand_top = {
                        "label": None,
                        "rows": [],
                        "summary_placement": "top",
                        "summary_rows": [],
                    }
                rows.append((grand_top["summary_rows"], cells, "grand_summary_row"))
                continue
            if grand is None:
                grand = {"label": None, "rows": [], "summary_rows": []}
            rows.append((grand["summary_rows"], cells, "grand_summary_row"))
            continue
        # A group's label in a row group column (`row_group_as_column`) starts it.
        if not groups or any(STUB_GROUP in c.classes for c in cells):
            groups.append({"label": None, "rows": [], "summary_rows": []})
        g = id(groups[-1])
        if "gt_summary_row" in classes:
            rows.append((groups[-1]["summary_rows"], cells, "summary_row"))
            below[g] = below.get(g, False) or has_rows.get(g, False)
        else:
            rows.append((groups[-1]["rows"], cells, None))
            has_rows[g] = True
    for (target, _, role), placed in zip(rows, place([c for _, c, _ in rows])):
        entries = [
            cell_entry(
                col,
                cell,
                stub=bool({"gt_stub", STUB_GROUP} & cell.classes),
                rowspan=span(cell, "rowspan"),
            )
            for col, cell in placed
        ]
        row: dict = {"cells": entries}
        if role:
            row["role"] = role
        target.append(row)
    for group in groups:
        g = id(group)
        if group["summary_rows"] and has_rows.get(g) and not below.get(g):
            group["summary_placement"] = "top"
    if grand is not None:
        groups.append(grand)
    return ([grand_top] if grand_top is not None else []) + groups


def grid(html: str) -> dict:
    """The L1 grid of the gt or Great Tables table in `html`."""
    root = parse(html)
    tables = list(root.find_all(lambda e: e.tag == "table" and "gt_table" in e.classes))
    if len(tables) != 1:
        raise ValueError(f"expected one gt table (table.gt_table), found {len(tables)}")
    table = tables[0]

    def first(cls):
        return next(table.find_all(lambda e: cls in e.classes), None)

    def line(cls):
        el = first(cls)
        return None if el is None else {"text": text(el)}

    thead = next(iter(table.elements("thead")), None)
    head = []
    if thead is not None:
        head = head_rows([tr for tr in thead.elements("tr") if "gt_col_headings" in tr.classes])
    groups = []
    for tbody in table.elements("tbody"):
        groups.extend(body_groups(tbody))
    if not groups:
        groups = [{"label": None, "rows": [], "summary_rows": []}]

    ncols = max(
        [sum(span(c, "colspan") for c in tr.elements("th", "td"))
         for tr in table.find_all(lambda e: e.tag == "tr" and "gt_col_headings" in e.classes)]
        or [0]
    )
    stub = set()
    for g in groups:
        for row in g["rows"] + g["summary_rows"]:
            ncols = max(ncols, max([c["col"] + c.get("colspan", 1) for c in row["cells"]] or [0]))
            stub.update(c["col"] for c in row["cells"] if c.get("stub"))
    columns = [{"stub": True} if i in stub else {} for i in range(ncols)]

    footnotes = [{"text": text(el)} for el in table.find_all(lambda e: "gt_footnote" in e.classes)]
    notes = [{"text": text(el)} for el in table.find_all(lambda e: "gt_sourcenote" in e.classes)]
    return {
        "format": FORMAT,
        "tier": "L1",
        "grid": {
            "columns": columns,
            "extra_lines": [],
            "footnotes": footnotes,
            "groups": groups,
            "head": head,
            "source_notes": notes,
            "subtitle": line("gt_subtitle"),
            "title": line("gt_title"),
        },
    }


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        print(json.dumps(grid(f.read()), indent=2, ensure_ascii=False, sort_keys=True))
