from __future__ import annotations

from great_tables._text import _latex_escape


def test_process_text_latex():

    assert _latex_escape("a & b") == "a \\& b"
    assert _latex_escape("a & b & c") == "a \\& b \\& c"
    assert _latex_escape("\\a_\\d") == "\\\\a\\_\\\\d"
