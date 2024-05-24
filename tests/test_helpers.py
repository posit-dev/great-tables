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
        (
            "  -20  _kg_^2      *m*_12  m[_0^2] g/L%C6H12O6% x10^-3",
            ["-20", "_kg_^2", "*m*_12", "m[_0^2]", "g/L%C6H12O6%", "x10^-3"],
        ),
        (
            "m^-3 :cdot: kg :cdot: m[_0^2] *per:space:mille*",
            ["m^-3", ":cdot:", "kg", ":cdot:", "m[_0^2]", "*per:space:mille*"],
        ),
        ("", []),
        (" ", []),
    ],
)
def assert_generate_tokens_list(units: str, x_out: str):

    x = _generate_tokens_list(units_notation=units)
    assert x == x_out


@pytest.mark.parametrize(
    "content, x_out",
    [
        ("2", '<span style="white-space:nowrap;"><sub>2</sub></span>'),
        ("2*e*5", '<span style="white-space:nowrap;"><sub>2*e*5</sub></span>'),
        ("", '<span style="white-space:nowrap;"><sub></sub></span>'),
    ],
)
def assert_units_to_subscript(content: str, x_out: str):
    x = _units_to_subscript(content=content)
    assert x == x_out


@pytest.mark.parametrize(
    "content, x_out",
    [
        ("34.3", '<span style="white-space:nowrap;"><sup>34.3</sup></span>'),
        ("4*d*2", '<span style="white-space:nowrap;"><sup>4*d*2</sup></span>'),
        ("", '<span style="white-space:nowrap;"><sup></sup></span>'),
    ],
)
def assert_units_to_superscript(content: str, x_out: str):
    x = _units_to_superscript(content=content)
    assert x == x_out


@pytest.mark.parametrize(
    "content_sub, content_sup, x_out",
    [
        (
            "*2i*",
            "3.23517",
            '<span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">3.23517<br>*2i*</span>',
        ),
        (
            "0",
            "e2.7",
            '<span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">e2.7<br>0</span>',
        ),
    ],
)
def assert_units_to_superscript(content_sub: str, content_sup: str, x_out: str):
    x = _units_html_sub_super(content_sub=content_sub, content_sup=content_sup)
    assert x == x_out


@pytest.mark.parametrize(
    "text, detect, pattern, replace, x_out",
    [
        ("-10^-5", "^-", "^-", "&minus;", "&minus10^-5"),
        ("um", "^um$", "um", "&micro;m", "&micro;m"),
        ("umlaut", "^um$", "um", "&micro;m", "umlaut"),
        ("3:mp:0.5", ":mp:", ":mp:", "&mnplus;", "3&mnplus;0.5"),
        ("-3.4x10^-2.5 kg", "^-", "^-", "&minus;", "&minus;3.4x10^-2.5 kg"),
        ("uL", "^uL$", "uL", "&micro;L", "&micro;L"),
        ("uLa", "^uL$", "uL", "&micro;L", "uLa"),
        ("0.5uL", "^uL$", "uL", "&micro;L", "0.5La"),
        ("umol_0", "^umol", "^umol", "&micro;mol", "&micro;mol_0"),
        ("uMol", "^umol", "^umol", "&micro;mol", "uMol"),
        ("ug", "^ug$", "ug", "&micro;g", "&micro;g"),
        ("ohm", "^ohm$", "ohm", "&#8486;", "&#8486;"),
        ("uohm", "^ohm$", "ohm", "&#8486;", "uohm"),
    ],
)
def assert_replace_units_symbol(text: str, detect: str, pattern: str, replace: str, x_out: str):
    x = _replace_units_symbol(text=text, detect=detect, pattern=pattern, replace=replace)
    assert x == x_out


@pytest.mark.parametrize(
    "text, x_out",
    [
        ("um", "&micro;m"),
        ("uL", "&micro;L"),
        ("umol", "&micro;mol"),
        ("ug", "&micro;g"),
        ("ohm", "&#8486;"),
        ("degC", "&deg;C"),
        ("degF", "&deg;F"),
        (":cdot:", "&sdot;"),
        (":Omicron:", "&Omicron;"),
    ],
)
def assert_units_symbol_replacements(text: str, x_out: str):
    x = _units_symbol_replacements(text=text)
    assert x == x_out


@pytest.mark.parametrize(
    "units_notation, x_out",
    [
        ("m/s", "m/s"),
        ("m / s", "m/s"),
        ("m s^-1", 'm s<span style="white-space:nowrap;"><sup>&minus;1</sup></span>'),
        ("m /s", 'm s<span style="white-space:nowrap;"><sup>&minus;1</sup></span>'),
        (
            "t_i^2.5",
            't<span style="white-space:nowrap;"><sub>i</sub></span><span style="white-space:nowrap;"><sup>2.5</sup></span>',
        ),
        (
            "m[_0^2]",
            'm<span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">2<br>0</span>',
        ),
        (
            "**m**[_*0*^**2**]",
            '<strong>m</strong><span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;"><strong>2</strong><br><em>0</em></span>',
        ),
        (
            "x10^9 / *L*",
            '&times;10<span style="white-space:nowrap;"><sup>9</sup></span>/<em>L</em>',
        ),
        (
            "x10^9/*L*",
            '&times;10<span style="white-space:nowrap;"><sup>9</sup></span>/<em>L</em>',
        ),
        (
            "x10^9 :space: / :space: *L*",
            '&times;10<span style="white-space:nowrap;"><sup>9</sup></span> &nbsp; / &nbsp; <em>L</em>',
        ),
        (
            "-20 kg^2 m_12 m[_0^2] g/L %C6H12O6% x10^-3",
            '&minus;20 kg<span style="white-space:nowrap;"><sup>2</sup></span> m<span style="white-space:nowrap;"><sub>12</sub></span> m<span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">2<br>0</span> g/L C<span style="white-space:nowrap;"><sub>6</sub></span>H<span style="white-space:nowrap;"><sub>12</sub></span>O<span style="white-space:nowrap;"><sub>6</sub></span> &times;10<span style="white-space:nowrap;"><sup>&minus;3</sup></span>',
        ),
        (
            "m^-3 :cdot: kg :cdot: m[_0^2] *per:space:mille*",
            'm<span style="white-space:nowrap;"><sup>&minus;3</sup></span> &sdot; kg &sdot; m<span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">2<br>0</span> <em>per\xa0mille</em>',
        ),
        (
            "  -20  _kg_^2      *m*_12  m[_0^2] g/L%C6H12O6% x10^-3",
            '&minus;20 _kg_<span style="white-space:nowrap;"><sup>2</sup></span> <em>m</em><span style="white-space:nowrap;"><sub>12</sub></span> m<span style="display:inline-block;line-height:1em;text-align:left;font-size:60%;vertical-align:-0.25em;margin-left:0.1em;">2<br>0</span> g/L%C6H12O6% &times;10<span style="white-space:nowrap;"><sup>&minus;3</sup></span>',
        ),
        (
            "kg :cdot: m :cdot: /s",
            'kg &sdot; m &sdot; s<span style="white-space:nowrap;"><sup>&minus;1</sup></span>',
        ),
    ],
)
def assert_define_units_html(units_notation: str, x_out: str):
    x = define_units(units_notation=units_notation).to_html()
    assert x == x_out
