from __future__ import annotations

from great_tables._text import _latex_escape, escape_pattern_str_latex


def test_process_text_latex():

    assert _latex_escape("a & b") == "a \\& b"
    assert _latex_escape("a & b & c") == "a \\& b \\& c"
    assert _latex_escape("\\a_\\d") == "\\\\a\\_\\\\d"


def test_escape_pattern_str_latex():

    assert escape_pattern_str_latex("{x}") == "{x}"
    assert escape_pattern_str_latex("a $_{1} %ab {2}") == "a \\$\\_{1} \\%ab {2}"
    assert escape_pattern_str_latex("a{b}c") == "a\\{b\\}c"
