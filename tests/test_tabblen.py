import io
import re

import pytest

from great_tables._tabblen import (
    ARMS,
    HEIGHT,
    MOODS,
    WIDTH,
    _demo,
    _demo_frames,
    _strip,
    _use_color,
    render,
)


DEFAULT = "\n".join(
    [
        "   ┌───────────────────────┐   ",
        "   │       ◉       ◉       │   ",
        "   │         ╰───╯         │   ",
        "   ├─────┬─────┬─────┬─────┤   ",
        "   │     │     │     │     │   ",
        " ⎛ ├─────┼─────┼─────┼─────┤ ⎞ ",
        " ⎜ │     │     │     │     │ ⎟ ",
        " ⎝ ├─────┼─────┼─────┼─────┤ ⎠ ",
        "   │     │     │     │     │   ",
        "  ╭┴─────┴────╮│╭────┴─────┴╮  ",
        "  ╰───────────╯ ╰───────────╯  ",
    ]
)


def test_render_default():
    assert render(color=False) == DEFAULT


@pytest.mark.parametrize("mood", MOODS)
@pytest.mark.parametrize("arms", ARMS)
def test_render_size(mood: str, arms: str):
    lines = render(mood, arms=arms, color=False).split("\n")
    assert len(lines) == HEIGHT
    assert {len(line) for line in lines} == {WIDTH}


def test_render_color_is_plain_drawing_with_styles():
    kwargs = dict(
        mood="love", arms=("open", "wave"), cells=[["a", {"text": "b", "fill": "#f900c3"}]]
    )
    colored = render(color=True, **kwargs)
    assert "\x1b[" in colored
    assert _strip(colored) == render(color=False, **kwargs)


def test_render_moods_and_parts():
    assert render("surprised", color=False).split("\n")[1] == "   │       ◎       ◎       │   "
    assert render("surprised", color=False).split("\n")[2] == "   │           ○           │   "
    assert render("wink", color=False).split("\n")[1] == "   │       ◉       ◠       │   "
    # Eyes and a mouth in place of the mood's
    line_1, line_2 = render(eyes=("closed", "heart"), mouth="frown", color=False).split("\n")[1:3]
    assert line_1 == "   │       ‿       ♥       │   "
    assert line_2 == "   │         ╭───╮         │   "


@pytest.mark.parametrize(
    "look, col", [("left", 10), (-1, 10), ("center", 11), ("right", 12), (1, 12)]
)
def test_render_look(look: "str | int", col: int):
    line = render(look=look, color=False).split("\n")[1]
    assert line.index("◉") == col
    assert line.index("◉", col + 1) == col + 8


def test_render_arms_each_side():
    lines = render(arms=("up", "point"), color=False).split("\n")
    assert lines[2][0] == "╲" and lines[3][1] == "╲"
    assert lines[4][29:] == "──"
    assert lines[5][1] == " " and lines[5][29] == " "


def test_render_cells():
    lines = render(cells=[["ab", 1.5, None, "toolong"], [], [{"text": 42}]], color=False).split(
        "\n"
    )
    assert lines[4] == "   │  ab │ 1.5 │     │tool…│   "
    assert lines[6] == " ⎜ │     │     │     │     │ ⎟ "
    assert lines[8] == "   │  42 │     │     │     │   "


def test_render_cells_string():
    lines = render(cells="GREAT TABLES and more", color=False).split("\n")
    assert [re.sub(r"[│ ]", "", lines[n][3:28]) for n in (4, 6, 8)] == ["GREA", "TTA", "BLES"]


def test_render_cell_fills():
    light = render(cells=[[{"text": "x", "fill": "#fff0fa"}]], color=True)
    dark = render(cells=[[{"fill": "f900c3"}]], color=True)
    assert "\x1b[48;2;255;240;250m\x1b[38;5;16m" in light
    assert "\x1b[48;2;249;0;195m\x1b[38;5;231m" in dark


@pytest.mark.parametrize(
    "kwargs, match",
    [
        (dict(mood="angry"), "`mood` must be one of"),
        (dict(eyes="square"), "Eyes must be one of"),
        (dict(eyes=("open", "x")), "Eyes must be one of"),
        (dict(mouth="pout"), "`mouth` must be one of"),
        (dict(arms="akimbo"), "`arms` must be one of"),
        (dict(arms=("rest", "akimbo")), "`arms` must be one of"),
        (dict(look="up"), "`look` must be one of"),
        (dict(look=2), "`look` must be one of"),
        (dict(cells=[[{"fill": "pink"}]], color=True), "Cell fills must be colors"),
    ],
)
def test_render_raises(kwargs: dict, match: str):
    with pytest.raises(ValueError, match=match):
        render(**kwargs)


class _Stream(io.StringIO):
    def __init__(self, tty: bool):
        super().__init__()
        self.tty = tty

    def isatty(self) -> bool:
        return self.tty


def test_use_color(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv("NO_COLOR", raising=False)
    monkeypatch.setenv("TERM", "xterm-256color")
    assert _use_color(_Stream(tty=True))
    assert not _use_color(_Stream(tty=False))

    monkeypatch.setenv("NO_COLOR", "1")
    assert not _use_color(_Stream(tty=True))

    monkeypatch.delenv("NO_COLOR")
    monkeypatch.setenv("TERM", "dumb")
    assert not _use_color(_Stream(tty=True))


def test_render_color_default_follows_stdout(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("NO_COLOR", "1")
    assert render() == DEFAULT


def test_demo_frames_have_room_to_hop():
    frames = list(_demo_frames())
    assert frames
    for drawing, seconds in frames:
        lines = _strip(drawing).split("\n")
        assert len(lines) == HEIGHT + 1
        assert sum(line == "" for line in lines) == 1
        assert seconds > 0


def test_demo(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("great_tables._tabblen.time.sleep", lambda seconds: None)
    stream = _Stream(tty=True)
    _demo(stream)
    out = stream.getvalue()
    n_frames = len(list(_demo_frames()))
    assert out.startswith("\x1b[?25l") and out.endswith("\x1b[?25h")
    assert out.count(f"\x1b[{HEIGHT + 1}A") == n_frames - 1
