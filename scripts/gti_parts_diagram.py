"""Draw the "parts of a GTI table" diagram for the User Guide.

    python scripts/gti_parts_diagram.py          # write both themes, then lint
    python scripts/gti_parts_diagram.py --lint   # lint only, nonzero exit on issues

Writes `assets/gti_parts_of_a_table.light.svg` and `.dark.svg`; the docs' lightbox shows the dark
one in dark mode. The figure is built from structured elements (rects, lines, text) rather than
SVG strings, so that the same geometry can be written for both themes and linted for text that
runs off the canvas, text that overlaps text, leaders that cross text, and off-scale font sizes.
The design system (canvas width, strokes, fonts, text sizes) follows EdgeCase's doc graphics.
"""

from __future__ import annotations

import argparse
import html
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
SLUG = "gti_parts_of_a_table"

# --- canvas & typography ---------------------------------------------------

W, H = 760, 384
MARGIN = 12

STROKE = 1.5
THIN = 1.0

FONT_SANS = "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', sans-serif"
FONT_MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

# The only allowed text sizes. Linted.
SIZE_LABEL = 13  # part names
SIZE_CAPTION = 12  # method captions (code)
SIZE_NOTE = 11  # cells, status line, tokens
SIZE_BADGE = 10  # dtype badges, row numbers
TEXT_SIZES = {SIZE_LABEL, SIZE_CAPTION, SIZE_NOTE, SIZE_BADGE}

TITLE = "The parts of a GTI table"
ALT = (
    "A schematic GTI table with its parts labelled. The table GT made (column labels and body) is "
    "drawn in gray; the parts GTI adds are in teal: the status line above the table, the column "
    "controls and column profiles under the labels, the row numbers, the height handle at the foot "
    "of the body, the filter tokens, and the control bar below the table with its search, keyboard "
    "shortcuts, page controls and counter, filters-as-text button, panels, and undo and redo."
)

# --- theme -----------------------------------------------------------------


@dataclass(frozen=True)
class Theme:
    suffix: Literal["light", "dark"]
    ink: str
    paper: str
    accent: str  # the site's teal, darkened (light) or lightened (dark) for contrast


LIGHT = Theme("light", ink="#1f2328", paper="#ffffff", accent="#0b7a64")
DARK = Theme("dark", ink="#e6edf3", paper="#0d1117", accent="#3fd8b4")
THEMES = (LIGHT, DARK)


def _mix(c1: str, c2: str, t: float) -> str:
    """Blend hex c1 toward c2 by t (0 = c1, 1 = c2)."""
    a = [int(c1[i : i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i : i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * t):02x}" for x, y in zip(a, b))


# Colors are named by role and resolved per theme.
Color = Literal["ink", "muted", "faint", "accent", "tint", "bar", "paper"]


def _color(theme: Theme, c: Color) -> str:
    return {
        "ink": theme.ink,
        "muted": _mix(theme.ink, theme.paper, 0.45),
        "faint": _mix(theme.ink, theme.paper, 0.88),
        "accent": theme.accent,
        "tint": _mix(theme.accent, theme.paper, 0.86),
        "bar": _mix(theme.accent, theme.paper, 0.45),
        "paper": theme.paper,
    }[c]


# --- elements --------------------------------------------------------------

BBox = tuple[float, float, float, float]  # x0, y0, x1, y1


@dataclass
class Text:
    x: float
    y: float  # baseline
    s: str
    size: int = SIZE_LABEL
    color: Color = "ink"
    anchor: Literal["start", "middle", "end"] = "start"
    mono: bool = False
    bold: bool = False

    def bbox(self) -> BBox:
        w = text_width(self.s, self.size, self.mono, self.bold)
        x0 = {"start": self.x, "middle": self.x - w / 2, "end": self.x - w}[self.anchor]
        return (x0, self.y - self.size * 0.78, x0 + w, self.y + self.size * 0.22)


@dataclass
class Rect:
    x0: float
    y0: float
    x1: float
    y1: float
    stroke: Color | None = None
    fill: Color | None = None
    rx: float = 0
    width: float = STROKE


@dataclass
class Line:
    pts: list[tuple[float, float]]
    color: Color = "ink"
    width: float = STROKE
    leader: bool = False  # a label's leader: linted against the text it passes
    dot: bool = False  # a dot at the last point (where a leader meets its part)
    fill: Color | None = None  # closed and filled (glyphs)


@dataclass
class Circle:
    cx: float
    cy: float
    r: float
    stroke: Color | None = None
    fill: Color | None = None


@dataclass
class Path:
    d: str
    color: Color = "accent"
    width: float = STROKE


def text_width(s: str, size: float, mono: bool = False, bold: bool = False) -> float:
    if mono:
        return len(s) * size * 0.61
    # Rough proportional-font estimate, deliberately on the wide side.
    w = 0.0
    for ch in s:
        if ch in "il.,:;|!' ":
            w += 0.3
        elif ch in "mwMW":
            w += 0.85
        elif ch.isupper() or ch.isdigit():
            w += 0.66
        else:
            w += 0.56
    return w * size * (1.05 if bold else 1.0)


@dataclass
class Scene:
    texts: list[Text] = field(default_factory=list)
    shapes: list[Rect | Line | Circle | Path] = field(default_factory=list)

    def text(self, *args, **kwargs) -> Text:
        t = Text(*args, **kwargs)
        self.texts.append(t)
        return t

    def add(self, shape):
        self.shapes.append(shape)
        return shape

    def label(self, x, y, name, captions=(), anchor="start", color: Color = "accent"):
        """A part's name in bold, with its methods (as code) under it."""
        self.text(
            x, y, name, SIZE_LABEL, "ink" if color == "accent" else "muted", anchor, bold=True
        )
        for i, cap in enumerate(captions, start=1):
            self.text(x, y + 14 * i, cap, SIZE_CAPTION, color, anchor, mono=True)

    def leader(self, *pts, color: Color = "accent"):
        self.add(Line(list(pts), color, THIN, leader=True, dot=True))


# --- the figure ------------------------------------------------------------

# The table: a row-number gutter and four columns.
TX0, TX1 = 190, 570
GUTTER = 214
COLS = [  # name, x0, x1, dtype, right-aligned
    ("mfr", GUTTER, 300, "str", False),
    ("model", 300, 400, "str", False),
    ("year", 400, 470, "i64", True),
    ("hp", 470, TX1, "f64", True),
]
ROWS = [  # row number, then the values, as the table is filtered and sorted
    ("9", "Ferrari", "LaFerrari", "2015", "949.0"),
    ("8", "Ferrari", "F12Berlinetta", "2015", "731.0"),
    ("12", "Lamborghini", "Aventador", "2015", "700.0"),
    ("6", "Ferrari", "GTC4Lusso", "2017", "680.0"),
]

Y_STATUS = 38  # status line baseline
Y_LABELS = (50, 74)
Y_CONTROLS = (74, 92)
Y_PROFILES = (92, 128)
Y_BODY = 132
ROW_H = 25
Y_BODY_END = Y_BODY + ROW_H * len(ROWS)
Y_TOKEN = (246, 266)
Y_BAR = (276, 304)
BAR_Y = (Y_BAR[0] + Y_BAR[1]) / 2

# Control bar buttons, by their centers.
BAR_X = {
    "search": 206,
    "keys": 230,
    "first": 316,
    "prev": 338,
    "counter": 366,
    "next": 394,
    "last": 416,
    "query": 448,
    "columns": 472,
    "export": 494,
    "undo": 516,
    "redo": 536,
    "info": 556,
}

# Labels sit in the margins: ending at LEFT on the left, starting at RIGHT on the right.
LEFT, RIGHT = 176, 584

# Profile bars (heights 0..1) for each column, from left to right.
PROFILES = {
    "mfr": [1.0, 0.22, 0, 0, 0, 0, 0.12, 0.12],
    "model": [0.12] * 9,
    "year": [0.18, 0.3, 0.55, 1.0, 0.45, 0.2],
    "hp": [0.25, 0.6, 1.0, 0.7, 0.35, 0.15, 0, 0.12, 0, 0, 0.1],
}


def chevron(x, y, direction: int) -> Line:
    """A page arrow pointing left (-1) or right (1)."""
    return Line(
        [(x - 2.5 * direction, y - 5), (x + 2.5 * direction, y), (x - 2.5 * direction, y + 5)],
        "accent",
    )


def build() -> Scene:
    sc = Scene()

    # Legend.
    sc.add(Rect(RIGHT, 12, RIGHT + 10, 22, fill="muted", rx=2))
    sc.text(RIGHT + 16, 21, "The table GT made", SIZE_NOTE, "ink")
    sc.add(Rect(RIGHT, 28, RIGHT + 10, 38, fill="accent", rx=2))
    sc.text(RIGHT + 16, 37, "Added by GTI", SIZE_NOTE, "ink")

    # Status line.
    sc.text(TX0, Y_STATUS, "Polars DataFrame · 12 of 47 rows × 4 columns", SIZE_NOTE, "accent")
    sc.label(LEFT, 30, "Status line", ["i_inspect()"], anchor="end")
    sc.leader((LEFT + 4, 34), (TX0 - 4, 34))

    # Column labels (GT's), with a rule above and below.
    sc.add(Rect(TX0, Y_LABELS[0], TX1, Y_LABELS[1], fill="faint"))
    for name, x0, x1, _, right in COLS:
        sc.text(
            x1 - 8 if right else x0 + 6,
            Y_LABELS[1] - 8,
            name,
            SIZE_NOTE,
            "ink",
            "end" if right else "start",
        )
    sc.label(RIGHT, 66, "Column labels", color="muted")
    sc.leader((RIGHT - 4, 62), (TX1 - 2, 62), color="muted")

    # Column controls: a dtype badge, sort arrows and a filter button for each column.
    cy = sum(Y_CONTROLS) / 2
    for name, x0, x1, dtype, right in COLS:
        bw = text_width(dtype, SIZE_BADGE, mono=True) + 6
        bx = x1 - 8 - bw - 30 if right else x0 + 6
        sc.add(Rect(bx, cy - 6, bx + bw, cy + 6, fill="tint", rx=2))
        sc.text(bx + bw / 2, cy + 3.5, dtype, SIZE_BADGE, "accent", "middle", mono=True)
        ax = bx + bw + 9
        down = name == "hp"  # sorted by hp, descending
        sc.add(Line([(ax - 3, cy - 1.5), (ax, cy - 5), (ax + 3, cy - 1.5)], "accent", THIN))
        sc.add(
            Line(
                [(ax - 3, cy + 1.5), (ax, cy + 5), (ax + 3, cy + 1.5)],
                "accent",
                THIN,
                fill="accent" if down else None,
            )
        )
        fx = ax + 13
        funnel = [
            (fx - 4.5, cy - 4.5),
            (fx + 4.5, cy - 4.5),
            (fx + 1, cy),
            (fx + 1, cy + 4.5),
            (fx - 1, cy + 4.5),
            (fx - 1, cy),
        ]
        sc.add(Line(funnel + [funnel[0]], "accent", THIN, fill="accent" if name == "mfr" else None))
    sc.label(LEFT, 78, "Column controls", ["i_sorting()", "i_cols_filter()"], anchor="end")
    sc.leader((LEFT + 4, 74), (GUTTER + 4, cy))

    # Column profiles.
    for name, x0, x1, _, _ in COLS:
        bars = PROFILES[name]
        step = (x1 - x0 - 12) / len(bars)
        for i, h in enumerate(bars):
            if h:
                bx = x0 + 6 + i * step
                sc.add(
                    Rect(
                        bx, Y_PROFILES[1] - 6 - 26 * h, bx + step - 2, Y_PROFILES[1] - 6, fill="bar"
                    )
                )
    sc.add(Line([(TX0, Y_PROFILES[1] + 2), (TX1, Y_PROFILES[1] + 2)], "muted", THIN))
    sc.label(LEFT, 128, "Column profiles", ["i_cols_profile()"], anchor="end")
    sc.leader((LEFT + 4, 124), (GUTTER + 4, 112))

    # Body (GT's), with the row numbers in the gutter.
    for i, (num, *values) in enumerate(ROWS):
        y = Y_BODY + ROW_H * i
        base = y + ROW_H / 2 + 4
        sc.text(GUTTER - 6, base, num, SIZE_BADGE, "accent", "end")
        for (_, x0, x1, _, right), v in zip(COLS, values):
            sc.text(
                x1 - 8 if right else x0 + 6, base, v, SIZE_NOTE, "ink", "end" if right else "start"
            )
        if i:
            sc.add(Line([(TX0, y), (TX1, y)], "faint", THIN))
    sc.add(Line([(TX0, Y_BODY_END), (TX1, Y_BODY_END)], "muted", THIN))
    sc.label(LEFT, 180, "Row numbers", ["i_inspect()"], anchor="end")
    sc.leader((LEFT + 4, 176), (TX0 + 2, 169))
    sc.label(RIGHT, 186, "Table body", color="muted")
    sc.leader((RIGHT - 4, 182), (TX1 - 2, 182), color="muted")

    # Height handle, at the foot of the body.
    hx = (TX0 + TX1) / 2
    sc.add(Rect(hx - 12, Y_BODY_END + 2, hx + 12, Y_BODY_END + 6, fill="accent", rx=2))
    sc.label(RIGHT, 232, "Height handle", ["i_scroll()"])
    sc.leader((RIGHT - 4, 228), (hx + 16, Y_BODY_END + 4))

    # Filter token.
    token = "mfr: Ferrari, Lamborghini"
    tw = text_width(token, SIZE_NOTE)
    sc.add(Rect(TX0, Y_TOKEN[0], TX0 + tw + 34, Y_TOKEN[1], "accent", "tint", rx=10, width=THIN))
    sc.text(TX0 + 10, Y_TOKEN[1] - 6, token, SIZE_NOTE, "ink")
    kx, ky = TX0 + tw + 22, sum(Y_TOKEN) / 2
    sc.add(Line([(kx - 3, ky - 3), (kx + 3, ky + 3)], "accent", THIN))
    sc.add(Line([(kx - 3, ky + 3), (kx + 3, ky - 3)], "accent", THIN))
    sc.label(LEFT, 260, "Filter tokens", anchor="end")
    sc.leader((LEFT + 4, 256), (TX0 - 2, 256))

    # Control bar, and its buttons.
    sc.add(Rect(TX0, Y_BAR[0], TX1, Y_BAR[1], "accent", "paper", rx=14))
    b, y = BAR_X, BAR_Y
    sc.add(Circle(b["search"] - 1.5, y - 1.5, 4.5, "accent"))
    sc.add(Line([(b["search"] + 1.8, y + 1.8), (b["search"] + 5, y + 5)], "accent"))
    sc.add(Rect(b["keys"] - 7, y - 5, b["keys"] + 7, y + 5, "accent", rx=1.5, width=THIN))
    sc.add(Line([(b["keys"] - 3.5, y + 2), (b["keys"] + 3.5, y + 2)], "accent", THIN))
    sc.add(Line([(b["first"] - 4, y - 5), (b["first"] - 4, y + 5)], "accent"))
    sc.add(chevron(b["first"] + 1, y, -1))
    sc.add(chevron(b["prev"], y, -1))
    sc.text(b["counter"], y + 4, "1 / 2", SIZE_NOTE, "ink", "middle")
    sc.add(chevron(b["next"], y, 1))
    sc.add(chevron(b["last"] - 1, y, 1))
    sc.add(Line([(b["last"] + 4, y - 5), (b["last"] + 4, y + 5)], "accent"))
    sc.text(b["query"], y + 4, "{ }", SIZE_CAPTION, "accent", "middle", mono=True)
    sc.add(Rect(b["columns"] - 6, y - 5, b["columns"] + 6, y + 5, "accent", width=THIN))
    for dx in (-2, 2):
        sc.add(Line([(b["columns"] + dx, y - 5), (b["columns"] + dx, y + 5)], "accent", THIN))
    sc.add(Line([(b["export"], y - 6), (b["export"], y + 2)], "accent"))
    sc.add(
        Line(
            [(b["export"] - 3.5, y - 1.5), (b["export"], y + 2), (b["export"] + 3.5, y - 1.5)],
            "accent",
        )
    )
    sc.add(Line([(b["export"] - 5, y + 6), (b["export"] + 5, y + 6)], "accent"))
    for name, d in (("undo", -1), ("redo", 1)):
        x = b[name]
        # A hooked arrow: its head points left (undo) or right (redo).
        sweep = 1 if d < 0 else 0
        sc.add(
            Path(f"M {x + 5 * d} {y - 2} H {x - d} A 4 4 0 0 {sweep} {x - d} {y + 6} H {x + 2 * d}")
        )
        sc.add(Line([(x + 2 * d, y - 5), (x + 5 * d, y - 2), (x + 2 * d, y + 1)], "accent"))
    sc.add(Circle(b["info"], y, 6.5, "accent"))
    sc.add(Line([(b["info"], y - 0.5), (b["info"], y + 3.5)], "accent"))
    sc.add(Circle(b["info"], y - 3, 0.9, fill="accent"))
    sc.label(RIGHT, 294, "Control bar")
    sc.leader((RIGHT - 4, 290), (TX1 + 2, 290))

    # The control bar's parts: in the margin, above the bar, and in two tiers below it.
    sc.label(LEFT, 294, "Search", anchor="end")
    sc.leader((LEFT + 4, 290), (TX0 + 6, 290))
    sc.label(LEFT, 334, "Keyboard shortcuts", anchor="end")
    sc.leader((LEFT + 4, 330), (b["keys"], 330), (b["keys"], y + 7))
    sc.label(510, 262, "Panels", anchor="middle")
    for name in ("columns", "export", "info"):
        sc.leader((510 + (b[name] - 510) * 0.15, 266), (b[name], y - 8))

    yb = Y_BAR[1] + 6  # brackets under groups of buttons
    sc.add(
        Line(
            [
                (b["first"] - 8, yb - 3),
                (b["first"] - 8, yb),
                (b["last"] + 8, yb),
                (b["last"] + 8, yb - 3),
            ],
            "accent",
            THIN,
        )
    )
    sc.add(
        Line(
            [
                (b["undo"] - 8, yb - 3),
                (b["undo"] - 8, yb),
                (b["redo"] + 8, yb),
                (b["redo"] + 8, yb - 3),
            ],
            "accent",
            THIN,
        )
    )
    tier1, tier2 = 338, 368
    sc.label(b["counter"], tier1, "Page counter", anchor="middle")
    sc.leader((b["counter"], tier1 - 14), (b["counter"], y + 11))
    sc.label(b["first"] - 8, tier2, "Page controls", anchor="middle")
    sc.leader((b["first"] - 8, tier2 - 14), (b["first"] - 8, yb))
    sc.label(b["query"], tier2, "Filters as text", anchor="middle")
    sc.leader((b["query"], tier2 - 14), (b["query"], y + 11))
    undo_x = (b["undo"] + b["redo"]) / 2
    sc.label(undo_x, tier1, "Undo / redo", anchor="middle")
    sc.leader((undo_x, tier1 - 14), (undo_x, yb))
    return sc


# --- svg -------------------------------------------------------------------


def _attrs(**kw) -> str:
    return " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in kw.items() if v is not None)


def to_svg(sc: Scene, theme: Theme) -> str:
    def c(name: Color | None) -> str | None:
        return None if name is None else _color(theme, name)

    out = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
            f'height="{H}" role="img" xml:space="preserve">'
        ),
        f"<title>{html.escape(TITLE)}</title>",
        f"<desc>{html.escape(ALT)}</desc>",
        f'<rect width="{W}" height="{H}" fill="{theme.paper}"/>',
    ]
    for s in sc.shapes:
        if isinstance(s, Rect):
            a = _attrs(
                x=s.x0,
                y=s.y0,
                width=round(s.x1 - s.x0, 2),
                height=round(s.y1 - s.y0, 2),
                rx=s.rx or None,
                fill=c(s.fill) or "none",
                stroke=c(s.stroke),
                stroke_width=s.width if s.stroke else None,
            )
            out.append(f"<rect {a}/>")
        elif isinstance(s, Line):
            pts = " ".join(f"{round(x, 2)},{round(y, 2)}" for x, y in s.pts)
            tag = "polygon" if s.fill else "polyline"
            a = _attrs(
                points=pts,
                fill=c(s.fill) or "none",
                stroke=c(s.color),
                stroke_width=s.width,
                stroke_linecap="round",
                stroke_linejoin="round",
                stroke_opacity=0.7 if s.leader else None,
            )
            out.append(f"<{tag} {a}/>")
            if s.dot:
                x, y = s.pts[-1]
                out.append(f'<circle cx="{x}" cy="{y}" r="2" fill="{c(s.color)}"/>')
        elif isinstance(s, Circle):
            a = _attrs(
                cx=s.cx,
                cy=s.cy,
                r=s.r,
                fill=c(s.fill) or "none",
                stroke=c(s.stroke),
                stroke_width=STROKE if s.stroke else None,
            )
            out.append(f"<circle {a}/>")
        elif isinstance(s, Path):
            a = _attrs(
                d=s.d, fill="none", stroke=c(s.color), stroke_width=s.width, stroke_linecap="round"
            )
            out.append(f"<path {a}/>")
    for t in sc.texts:
        a = _attrs(
            x=round(t.x, 2),
            y=round(t.y, 2),
            font_family=FONT_MONO if t.mono else FONT_SANS,
            font_size=t.size,
            font_weight=600 if t.bold else None,
            fill=c(t.color),
            text_anchor=t.anchor if t.anchor != "start" else None,
        )
        out.append(f"<text {a}>{html.escape(t.s)}</text>")
    out.append("</svg>")
    return "\n".join(out) + "\n"


# --- lint ------------------------------------------------------------------


def _overlap(a: BBox, b: BBox, gap: float = 0) -> bool:
    return a[0] < b[2] + gap and b[0] < a[2] + gap and a[1] < b[3] + gap and b[1] < a[3] + gap


def _seg_hits_box(p, q, b: BBox, gap: float = 2) -> bool:
    x0, y0, x1, y1 = b[0] - gap, b[1] - gap, b[2] + gap, b[3] + gap
    n = max(2, int(max(abs(q[0] - p[0]), abs(q[1] - p[1])) / 1.5))
    for i in range(n + 1):
        x, y = p[0] + (q[0] - p[0]) * i / n, p[1] + (q[1] - p[1]) * i / n
        if x0 <= x <= x1 and y0 <= y <= y1:
            return True
    return False


def lint(sc: Scene) -> list[str]:
    issues = []
    if not ALT.strip():
        issues.append("[alt] the figure needs alt text")
    boxes = [(t, t.bbox()) for t in sc.texts]
    for t, b in boxes:
        if t.size not in TEXT_SIZES:
            issues.append(f"[size] {t.s!r} is {t.size}px, not one of {sorted(TEXT_SIZES)}")
        if b[0] < MARGIN or b[2] > W - MARGIN or b[1] < MARGIN / 2 or b[3] > H - MARGIN / 2:
            issues.append(f"[bounds] {t.s!r} runs off the canvas: {tuple(round(v) for v in b)}")
    for i, (t1, b1) in enumerate(boxes):
        for t2, b2 in boxes[i + 1 :]:
            if _overlap(b1, b2, gap=1):
                issues.append(f"[overlap] {t1.s!r} and {t2.s!r}")
    for s in sc.shapes:
        if not (isinstance(s, Line) and s.leader):
            continue
        # A leader starts beside (or just under) its own label, which it may touch.
        own = [b for _, b in boxes if _seg_hits_box(s.pts[0], s.pts[0], b, gap=6)]
        for p, q in zip(s.pts, s.pts[1:]):
            for t, b in boxes:
                if b not in own and _seg_hits_box(p, q, b):
                    issues.append(f"[leader] the leader from {s.pts[0]} crosses {t.s!r}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--lint", action="store_true", help="lint only; don't write the SVGs")
    args = parser.parse_args()

    sc = build()
    issues = lint(sc)
    if not args.lint:
        for theme in THEMES:
            path = OUT / f"{SLUG}.{theme.suffix}.svg"
            path.write_text(to_svg(sc, theme))
            print(f"wrote {path.relative_to(ROOT)}")
    for issue in issues:
        print(issue, file=sys.stderr)
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
