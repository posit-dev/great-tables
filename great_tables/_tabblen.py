"""Tabblen, the Great Tables mascot, drawn in a terminal.

`render()` draws him, with box-drawing characters (and ANSI colors where the terminal has them),
in any of the moods and arm poses of the web version (`assets/tabblen.js`), with text in the cells
of his body. Every drawing is the same size, so a TUI can redraw him in place to animate him;
`python -m great_tables._tabblen` shows how.
"""

from __future__ import annotations

import os
import re
import sys
import time
from collections.abc import Iterator, Mapping, Sequence
from typing import IO, TypeAlias

__all__ = ["ARMS", "HEIGHT", "MOODS", "WIDTH", "render"]

# The drawing: 31 columns by 11 lines, with the body in columns 3 to 27 (its four cells, five
# characters wide, between the lines at columns 3, 9, 15, 21 and 27) and room for the arms on
# either side.
WIDTH = 31
HEIGHT = 11

_BODY = [
    "   ┌───────────────────────┐   ",
    "   │                       │   ",
    "   │                       │   ",
    "   ├─────┬─────┬─────┬─────┤   ",
    "   │     │     │     │     │   ",
    "   ├─────┼─────┼─────┼─────┤   ",
    "   │     │     │     │     │   ",
    "   ├─────┼─────┼─────┼─────┤   ",
    "   │     │     │     │     │   ",
    "  ╭┴─────┴────╮│╭────┴─────┴╮  ",
    "  ╰───────────╯ ╰───────────╯  ",
]

_EYES = {
    "open": "◉",
    "wide": "◎",
    "happy": "◠",
    "closed": "‿",
    "heart": "♥",
    "blink": "─",
}

_MOUTHS = {
    "smile": "╰───╯",
    "grin": "╰▄▄▄╯",
    "flat": " ─── ",
    "frown": "╭───╮",
    "o": "  ○  ",
    "smirk": " ───╯",
    "small": "  ‿  ",
    "soft": " ╰─╯ ",
    "wavy": " ~~~ ",
    "talk": " ╭─╮ ",
}

# Each mood is a pair of eyes and a mouth, as in the web version.
MOODS: dict[str, tuple[str, str, str]] = {
    "happy": ("open", "open", "smile"),
    "grin": ("happy", "happy", "grin"),
    "neutral": ("open", "open", "flat"),
    "sad": ("open", "open", "frown"),
    "surprised": ("wide", "wide", "o"),
    "wink": ("open", "happy", "smirk"),
    "sleepy": ("closed", "closed", "small"),
    "zen": ("closed", "closed", "soft"),
    "love": ("heart", "heart", "smile"),
    "thinking": ("open", "open", "wavy"),
}

# The arm poses, each as the (line, column, character)s of the left arm and then the right one.
_ARMS: dict[str, tuple[tuple[tuple[int, int, str], ...], tuple[tuple[int, int, str], ...]]] = {
    "rest": (((5, 1, "⎛"), (6, 1, "⎜"), (7, 1, "⎝")), ((5, 29, "⎞"), (6, 29, "⎟"), (7, 29, "⎠"))),
    "open": (((4, 0, "╰"), (4, 1, "─")), ((4, 29, "─"), (4, 30, "╯"))),
    "up": (((2, 0, "╲"), (3, 1, "╲")), ((2, 30, "╱"), (3, 29, "╱"))),
    "point": (((4, 0, "─"), (4, 1, "─")), ((4, 29, "─"), (4, 30, "─"))),
    # (Halfway through a wave)
    "wave": (((2, 1, "│"), (3, 1, "│")), ((2, 29, "│"), (3, 29, "│"))),
}
ARMS = tuple(_ARMS)

_LOOKS = {"left": -1, "center": 0, "right": 1}

_INK = "\x1b[38;5;244m"
_ACCENT = "\x1b[38;5;199m"
_BOLD = "\x1b[1m"
_RESET = "\x1b[0m"
_ANSI = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]")

Cell: TypeAlias = "str | int | float | None | Mapping[str, object]"


def render(
    mood: str = "happy",
    *,
    arms: str | tuple[str, str] = "rest",
    look: str | int = "center",
    eyes: str | tuple[str, str] | None = None,
    mouth: str | None = None,
    cells: str | Sequence[Sequence[Cell]] | None = None,
    color: bool | None = None,
) -> str:
    """Draw Tabblen.

    Parameters
    ----------
    mood
        One of the `MOODS`, which sets his eyes and mouth.
    arms
        One of the `ARMS` poses for both arms, or a pose for each (left, right).
    look
        Where he looks: `"left"`, `"center"` or `"right"` (or -1, 0 or 1).
    eyes
        Eyes in place of the mood's: `"open"`, `"wide"`, `"happy"`, `"closed"`, `"heart"` or
        `"blink"`, for both eyes or for each (left, right).
    mouth
        A mouth in place of the mood's: `"smile"`, `"grin"`, `"flat"`, `"frown"`, `"o"`,
        `"smirk"`, `"small"`, `"soft"`, `"wavy"` or `"talk"`.
    cells
        What's in his body's 3 rows of 4 cells. Either rows of cells, each one text (cut to five
        characters) or a mapping with `"text"` and a `"fill"` color (as `"#rrggbb"`), or a string,
        with a character in each cell.
    color
        Whether to use ANSI colors. By default, they're used if standard output is a terminal and
        the `NO_COLOR` environment variable isn't set.

    Returns
    -------
    str
        The drawing, `HEIGHT` lines of `WIDTH` characters each.
    """

    if mood not in MOODS:
        raise ValueError(f"`mood` must be one of {', '.join(MOODS)}, not {mood!r}.")
    left_eye, right_eye, mood_mouth = MOODS[mood]
    if eyes is not None:
        left_eye, right_eye = (eyes, eyes) if isinstance(eyes, str) else eyes
    mouth = mood_mouth if mouth is None else mouth
    for eye in (left_eye, right_eye):
        if eye not in _EYES:
            raise ValueError(f"Eyes must be one of {', '.join(_EYES)}, not {eye!r}.")
    if mouth not in _MOUTHS:
        raise ValueError(f"`mouth` must be one of {', '.join(_MOUTHS)}, not {mouth!r}.")
    left_arm, right_arm = (arms, arms) if isinstance(arms, str) else arms
    for arm in (left_arm, right_arm):
        if arm not in _ARMS:
            raise ValueError(f"`arms` must be one of {', '.join(_ARMS)}, not {arm!r}.")
    shift = _LOOKS.get(look, look) if isinstance(look, str) else look
    if shift not in (-1, 0, 1):
        raise ValueError(
            f"`look` must be one of {', '.join(_LOOKS)} (or -1, 0 or 1), not {look!r}."
        )
    if color is None:
        color = _use_color(sys.stdout)

    # The drawing, as a grid of characters, each with its style
    grid: list[list[list[str]]] = [[[ch, _INK] for ch in line] for line in _BODY]

    def put(line: int, col: int, text: str, style: str = _INK) -> None:
        for i, ch in enumerate(text):
            grid[line][col + i] = [ch, style]

    for col, eye in ((11 + int(shift), left_eye), (19 + int(shift), right_eye)):
        put(1, col, _EYES[eye], _ACCENT if eye == "heart" else _INK)
    put(2, 13, _MOUTHS[mouth])
    for line, col, ch in _ARMS[left_arm][0] + _ARMS[right_arm][1]:
        put(line, col, ch)

    for r, row in enumerate(_cell_rows(cells)):
        for c, cell in enumerate(row[:4]):
            text, fill = _cell_spec(cell)
            style = _BOLD + (_on(fill) if fill else "")
            put(4 + 2 * r, 4 + 6 * c, _fit(text).center(5), style)

    lines: list[str] = []
    for line in grid:
        if not color:
            lines.append("".join(ch for ch, _ in line))
            continue
        out: list[str] = []
        style = None
        for ch, st in line:
            if st != style:
                out.append(_RESET + st)
                style = st
            out.append(ch)
        lines.append("".join(out) + _RESET)
    return "\n".join(lines)


def _use_color(stream: IO[str]) -> bool:
    if os.environ.get("NO_COLOR") or os.environ.get("TERM") == "dumb":
        return False
    return hasattr(stream, "isatty") and stream.isatty()


def _cell_rows(cells: str | Sequence[Sequence[Cell]] | None) -> list[Sequence[Cell]]:
    if cells is None:
        return []
    if isinstance(cells, str):
        chars = list(cells[:12])
        return [chars[i : i + 4] for i in range(0, len(chars), 4)]
    return list(cells)[:3]


def _cell_spec(cell: Cell) -> tuple[str, str | None]:
    if isinstance(cell, Mapping):
        text = cell.get("text")
        fill = cell.get("fill")
        return ("" if text is None else str(text)), (None if fill is None else str(fill))
    return ("" if cell is None else str(cell)), None


def _fit(text: str) -> str:
    return text if len(text) <= 5 else text[:4] + "…"


def _on(fill: str) -> str:
    """The ANSI style for text on a fill color (in black or white, whichever reads better)"""
    hex_ = fill.lstrip("#")
    if not re.fullmatch(r"[0-9a-fA-F]{6}", hex_):
        raise ValueError(f"Cell fills must be colors like '#f900c3', not {fill!r}.")
    r, g, b = (int(hex_[i : i + 2], 16) for i in range(0, 6, 2))
    light = 0.2126 * r + 0.7152 * g + 0.0722 * b > 150
    return f"\x1b[48;2;{r};{g};{b}m\x1b[38;5;{16 if light else 231}m"


def _strip(text: str) -> str:
    return _ANSI.sub("", text)


def _demo_frames() -> Iterator[tuple[str, float]]:
    """The frames of a short show (each with how long it stays up, in seconds)"""

    def frame(seconds: float = 0.12, lift: bool = False, **kwargs: object) -> tuple[str, float]:
        drawing = render(color=True, **kwargs)  # type: ignore[arg-type]
        # (He hops by a line, so the frames have one to spare)
        return (drawing + "\n" if lift else "\n" + drawing), seconds

    yield frame(0.9)
    yield frame(eyes="blink")
    yield frame(0.7)
    yield frame(0.5, look="left")
    yield frame(0.5, look="right")
    yield frame(0.4)
    for _ in range(3):
        yield frame(0.22, arms=("rest", "up"))
        yield frame(0.22, arms=("rest", "wave"))
    yield frame(0.3, mood="grin", arms=("rest", "up"))
    title = "GREAT TABLES"
    for n in range(1, len(title) + 1):
        yield frame(0.09, mood="happy", arms="open", cells=title[:n])
    yield frame(0.8, mood="grin", arms="up", cells=title)
    for _ in range(2):
        yield frame(0.16, mood="grin", arms="up", cells=title, lift=True)
        yield frame(0.16, mood="grin", arms="up", cells=title)
    pinks = ["#fff0fa", "#fcc2ec", "#fb94de", "#fa66d0", "#f933c9", "#f900c3"]
    filled: list[list[Cell]] = []
    for n in range(13):
        filled = [
            [
                {"text": "", "fill": pinks[min(5, (4 * r + c) // 2)]} if 4 * r + c < n else ""
                for c in range(4)
            ]
            for r in range(3)
        ]
        yield frame(0.07, mood="surprised", arms="open", cells=filled)
    yield frame(1.0, mood="love", arms="open", cells=filled)
    yield frame(0.12, mood="zen", arms="open")
    yield frame(1.4, mood="zen", arms="open", mouth="soft")
    yield frame(1.0, mood="wink", arms=("rest", "point"))


def _demo(stream: IO[str] = sys.stdout) -> None:
    """Play the show in a terminal, redrawing in place"""
    height = HEIGHT + 1
    stream.write("\x1b[?25l")
    try:
        first = True
        for drawing, seconds in _demo_frames():
            if not first:
                stream.write(f"\x1b[{height}A\r")
            stream.write(drawing.replace("\n", "\x1b[K\n") + "\x1b[K\n")
            stream.flush()
            first = False
            time.sleep(seconds)
    except KeyboardInterrupt:
        pass
    finally:
        stream.write("\x1b[?25h")
        stream.flush()


if __name__ == "__main__":
    if _use_color(sys.stdout):
        _demo()
    else:
        print(render(color=False))
