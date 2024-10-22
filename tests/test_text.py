from __future__ import annotations

from great_tables._text import Text, Md, Html, _latex_escape, escape_pattern_str_latex


def test_text_class():

    assert Text("<p>Some Text</p>").to_html() == "<p>Some Text</p>"
    assert Text("__Some Text__").to_latex() == "__Some Text__"


def test_md_class():

    assert Md("**text**").to_html() == "<strong>text</strong>"


def test_html_class():

    assert Html("<strong>text</strong>").to_html() == "<strong>text</strong>"
    assert Html("<strong>text</strong>").to_latex() == "<strong>text</strong>"


def test_latex_escape():

    assert _latex_escape("a & b") == "a \\& b"
    assert _latex_escape("a & b & c") == "a \\& b \\& c"
    assert _latex_escape("\\a_\\d") == "\\\\a\\_\\\\d"


def test_escape_pattern_str_latex():

    assert escape_pattern_str_latex("{x}") == "{x}"
    assert escape_pattern_str_latex("a $_{1} %ab {2}") == "a \\$\\_{1} \\%ab {2}"
    assert escape_pattern_str_latex("a{b}c") == "a\\{b\\}c"
