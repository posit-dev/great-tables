from great_tables._helpers import LETTERS, letters, pct, px, random_id, _get_font_stack, FONT_STACKS
import pytest


@pytest.fixture
def font_stack_names():
    yield {
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
    }


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


def test_get_font_stack_raises():
    name = "fake_name"
    with pytest.raises(ValueError) as exc_info:
        _get_font_stack(name)

    assert f"Invalid font stack name: {name}" in exc_info.value.args[0]


def test_get_font_stack_add_emoji_false(font_stack_names):
    assert all(
        _get_font_stack(name, add_emoji=False) == FONT_STACKS[name] for name in font_stack_names
    )


def test_get_font_stack_add_emoji_true(font_stack_names):
    extended_emoji = {"Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"}
    assert all(
        extended_emoji.issubset(_get_font_stack(name, add_emoji=True)) for name in font_stack_names
    )
