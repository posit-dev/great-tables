from great_tables._helpers import (
    LETTERS,
    letters,
    pct,
    px,
    random_id,
    _get_font_stack,
    define_units,
    FONT_STACKS,
    _generate_tokens_list,
    _units_to_subscript,
    _units_to_superscript,
    _units_html_sub_super,
    _replace_units_symbol,
    _units_symbol_replacements,
)
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


@pytest.mark.parametrize(
    "units, x_out",
    [
        ("x10^7 m s^-1", ["x10^7", "m", "s^-1"]),
        (
            "-20 kg^2 m_12 m[_0^2] g/L %C6H12O6% x10^-3",
            ["-20", "kg^2", "m_12", "m[_0^2]", "g/L", "%C6H12O6%", "x10^-3"],
        ),
    ],
)
def assert_generate_tokens_list(units: str, x_out: str):

    x = _generate_tokens_list(units_notation=units)
    assert x == x_out


@pytest.mark.parametrize(
    "content, x_out",
    [
        ("2"),
        (""),
    ],
)
def assert_units_to_subscript(content: str):
    x = _units_to_subscript(content=content)
    assert (
        x == f'<span style="white-space:nowrap;"><sub style="line-height:0;>{content}</sub></span>'
    )


@pytest.mark.parametrize(
    "content",
    [
        ("2"),
        (""),
    ],
)
def assert_units_to_superscript(content: str):
    x = _units_to_superscript(content=content)
    assert (
        x == f'<span style="white-space:nowrap;"><sup style="line-height:0;>{content}</sup></span>'
    )


@pytest.mark.parametrize(
    "content_sub, content_sup",
    [
        (
            "*2i*",
            "3.23517",
        ),
        (
            "0",
            "e2.7",
        ),
    ],
)
def assert_units_html_sub_super(content_sub: str, content_sup: str):
    x = _units_html_sub_super(content_sub=content_sub, content_sup=content_sup)
    assert (
        x
        == f'<span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">{content_sup}<br>{content_sub}</span>'
    )


@pytest.mark.parametrize(
    "text, detect, pattern, replace, x_out",
    [
        ("-10^-5", "^-", "^-", "&minus;", "&minus10^-5"),
        ("uL", "^uL$", "uL", "&micro;L", "&micro;L"),
        ("umol_0", "^umol", "^umol", "&micro;mol", "&micro;mol_0"),
    ],
)
def assert_replace_units_symbol(text: str, detect: str, pattern: str, replace: str, x_out: str):
    x = _replace_units_symbol(text=text, detect=detect, pattern=pattern, replace=replace)
    assert x == x_out


@pytest.mark.parametrize(
    "text, x_out",
    [
        ("um", "&micro;m"),
        (":Omicron:", "&Omicron;"),
    ],
)
def assert_units_symbol_replacements(text: str, x_out: str):
    x = _units_symbol_replacements(text=text)
    assert x == x_out


@pytest.mark.parametrize(
    "units_notation, x_out",
    [
        # unit with superscript
        (
            "m^2",
            'm<span style="white-space:nowrap;"><sup style="line-height:0;">2</sup></span>',
        ),
        # unit with subscript
        (
            "h_0",
            'h<span style="white-space:nowrap;"><sub style="line-height:0;">0</sub></span>',
        ),
        # unit with superscript and subscript
        (
            "h_0^3",
            'h<span style="white-space:nowrap;"><sub style="line-height:0;">0</sub></span><span style="white-space:nowrap;"><sup style="line-height:0;">3</sup></span>',
        ),
        # unit with superscript and subscript (using overstriking)
        (
            "h[_0^3]",
            'h<span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">3<br>0</span>',
        ),
        # slashed-unit shorthand for a '-1' exponent
        (
            "/s",
            's<span style="white-space:nowrap;"><sup style="line-height:0;">&minus;1</sup></span>',
        ),
        # slashes between units normalized
        (
            "t_0 / t_n",
            't<span style="white-space:nowrap;"><sub style="line-height:0;">0</sub></span>/t<span style="white-space:nowrap;"><sub style="line-height:0;">n</sub></span>',
        ),
        # multiple inline units, separating by a space
        (
            "kg^2 m^-1",
            'kg<span style="white-space:nowrap;"><sup style="line-height:0;">2</sup></span> m<span style="white-space:nowrap;"><sup style="line-height:0;">&minus;1</sup></span>',
        ),
        # use of a number allowed with previous rules
        (
            "10^3 kg^2 m^-1",
            '10<span style="white-space:nowrap;"><sup style="line-height:0;">3</sup></span> kg<span style="white-space:nowrap;"><sup style="line-height:0;">2</sup></span> m<span style="white-space:nowrap;"><sup style="line-height:0;">&minus;1</sup></span>',
        ),
        # "use of 'x' preceding number to form scalar multiplier
        (
            "x10^3 kg^2 m^-1",
            '&times;10<span style="white-space:nowrap;"><sup style="line-height:0;">3</sup></span> kg<span style="white-space:nowrap;"><sup style="line-height:0;">2</sup></span> m<span style="white-space:nowrap;"><sup style="line-height:0;">&minus;1</sup></span>',
        ),
        # hyphen is transformed to minus sign when preceding a unit
        (
            "-h^2",
            '&minus;h<span style="white-space:nowrap;"><sup style="line-height:0;">2</sup></span>',
        ),
        # italicization of base unit
        (
            "*m*^2",
            '<em>m</em><span style="white-space:nowrap;"><sup style="line-height:0;">2</sup></span>',
        ),
        # emboldening of base unit
        (
            "**m**^2",
            '<strong>m</strong><span style="white-space:nowrap;"><sup style="line-height:0;">2</sup></span>',
        ),
        # italicizing and emboldening of base unit
        (
            "_**m**_^2",
            '<em><strong>m</strong></em><span style="white-space:nowrap;"><sup style="line-height:0;">2</sup></span>',
        ),
        # styling of subscripts and superscripts
        (
            "h_*0*^**3**",
            'h<span style="white-space:nowrap;"><sub style="line-height:0;"><em>0</em></sub></span><span style="white-space:nowrap;"><sup style="line-height:0;"><strong>3</strong></sup></span>',
        ),
        # transformation of common units from ASCII to preferred form
        (
            "ug",
            "&micro;g",
        ),
        # insertion of common symbols and Greek letters via `:[symbol name]:`
        (
            ":angstrom:",
            "&#8491;",
        ),
        # use of chemical formulas via `%[chemical formula]%`
        (
            "%C6H12O6%",
            'C<span style="white-space:nowrap;"><sub>6</sub></span>H<span style="white-space:nowrap;"><sub>12</sub></span>O<span style="white-space:nowrap;"><sub>6</sub></span>',
        ),
    ],
)
def assert_define_units_html_superscript():
    x = define_units(units_notation="m^2").to_html()
    assert x == 'm<span style="white-space:nowrap;"><sup style="line-height:0;">2</sup></span>'
