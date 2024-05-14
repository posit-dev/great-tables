from great_tables._helpers import LETTERS, letters, pct, px, random_id, _get_font_stack
import pytest


@pytest.fixture
def font_stack_names():
    yield [
        "system-ui",
        "transitional",
        "old-style",
        "humanist",
        "geometric-humanist",
        "classical-humanist",
        "neo-grotesque",
        "monospace-slab-serif",
        "monospace-code",
        "industrial",
        "rounded-sans",
        "slab-serif",
        "antique",
        "didone",
        "handwritten",
    ]


def test_px():
    assert str(px(12)) == "12px"


def test_pct():
    assert str(pct(80)) == "80%"


def test_random_id():
    rid = random_id()
    assert len(rid) == 10
    assert not set(rid).difference(letters())
    assert len(random_id(5)) == 5


def test_lowercases():
    lowercases = letters()
    assert isinstance(lowercases, list)
    assert len(lowercases) == 26

    good_letters = "greattables"
    assert not set(good_letters).difference(lowercases)

    bad_letters = "#$!^%#TABLES"
    assert set(bad_letters).difference(lowercases)


def test_uppercases():
    uppercases = LETTERS()
    assert isinstance(uppercases, list)
    assert len(uppercases) == 26

    good_letters = "GREATTABLES"
    assert not set(good_letters).difference(uppercases)

    bad_letters = "#$!^%#tables"
    assert set(bad_letters).difference(uppercases)


def test_get_font_stack_raises(font_stack_names):
    name = "fake_name"
    with pytest.raises(ValueError) as exc_info:
        _get_font_stack(name)

    assert f"Invalid font stack name: {name}" in exc_info.value.args[0]


@pytest.mark.parametrize(
    "name,font_stack ",
    [
        ("system-ui", ["system-ui", "sans-serif"]),
        ("transitional", ["Charter", "Bitstream Charter", "Sitka Text", "Cambria", "serif"]),
        ("old-style", ["Iowan Old Style", "Palatino Linotype", "URW Palladio L", "P052", "serif"]),
        (
            "humanist",
            [
                "Seravek",
                "Gill Sans Nova",
                "Ubuntu",
                "Calibri",
                "DejaVu Sans",
                "source-sans-pro",
                "sans-serif",
            ],
        ),
        (
            "geometric-humanist",
            [
                "Avenir",
                "Montserrat",
                "Corbel",
                "URW Gothic",
                "source-sans-pro",
                "sans-serif",
            ],
        ),
        ("classical-humanist", ["Optima", "Candara", "Noto Sans", "source-sans-pro", "sans-serif"]),
        (
            "neo-grotesque",
            [
                "Inter",
                "Roboto",
                "Helvetica Neue",
                "Arial Nova",
                "Nimbus Sans",
                "Arial",
                "sans-serif",
            ],
        ),
        ("monospace-slab-serif", ["Nimbus Mono PS", "Courier New", "monospace"]),
        (
            "monospace-code",
            [
                "ui-monospace",
                "Cascadia Code",
                "Source Code Pro",
                "Menlo",
                "Consolas",
                "DejaVu Sans Mono",
                "monospace",
            ],
        ),
        (
            "industrial",
            [
                "Bahnschrift",
                "DIN Alternate",
                "Franklin Gothic Medium",
                "Nimbus Sans Narrow",
                "sans-serif-condensed",
                "sans-serif",
            ],
        ),
        (
            "rounded-sans",
            [
                "ui-rounded",
                "Hiragino Maru Gothic ProN",
                "Quicksand",
                "Comfortaa",
                "Manjari",
                "Arial Rounded MT",
                "Arial Rounded MT Bold",
                "Calibri",
                "source-sans-pro",
                "sans-serif",
            ],
        ),
        (
            "slab-serif",
            [
                "Rockwell",
                "Rockwell Nova",
                "Roboto Slab",
                "DejaVu Serif",
                "Sitka Small",
                "serif",
            ],
        ),
        (
            "antique",
            [
                "Superclarendon",
                "Bookman Old Style",
                "URW Bookman",
                "URW Bookman L",
                "Georgia Pro",
                "Georgia",
                "serif",
            ],
        ),
        (
            "didone",
            [
                "Didot",
                "Bodoni MT",
                "Noto Serif Display",
                "URW Palladio L",
                "P052",
                "Sylfaen",
                "serif",
            ],
        ),
        (
            "handwritten",
            ["Segoe Print", "Bradley Hand", "Chilanka", "TSCu_Comic", "casual", "cursive"],
        ),
    ],
)
def test_get_font_stack_add_emoji_false(name, font_stack):
    assert _get_font_stack(name, add_emoji=False) == font_stack


def test_get_font_stack_add_emoji_true(font_stack_names):
    extended_emoji = set(
        ["Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"]
    )
    assert all(extended_emoji.issubset(_get_font_stack(name)) for name in font_stack_names)
