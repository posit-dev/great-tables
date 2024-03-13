import pytest
from great_tables._utils_units_notation import (
    _generate_tokens_list,
    _units_to_subscript,
    _units_to_superscript,
    _units_html_sub_super,
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
