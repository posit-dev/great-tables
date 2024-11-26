import pytest

from great_tables._text import (
    BaseText,
    Text,
    Md,
    Html,
    _latex_escape,
    escape_pattern_str_latex,
    _process_text,
)


def test_base_text_class():
    with pytest.raises(NotImplementedError):
        BaseText().to_html()

    with pytest.raises(NotImplementedError):
        BaseText().to_latex()


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


def test_process_text_html():
    assert _process_text("a & <b>", context="html") == "a &amp; &lt;b&gt;"
    assert _process_text(Text("a & <b>"), context="html") == "a & <b>"
    assert _process_text(Md("**a** & <b>"), context="html") == "<strong>a</strong> &amp; <b>"
    assert _process_text(Html("**a** & <b>"), context="html") == "**a** & <b>"
    assert _process_text(None, context="html") == ""


def test_process_text_latex():
    assert _process_text("a & _b_", context="latex") == "a \\& \\_b\\_"
    assert _process_text(Text("\\_\\$"), context="latex") == "\\_\\$"
    assert _process_text(Html("**a** & <b>"), context="latex") == "**a** \\& <b>"
    assert _process_text(None, context="latex") == ""

    with pytest.raises(NotImplementedError) as exc_info:
        _process_text(Md("**a** & <b>"), context="latex")

    assert "Markdown to LaTeX conversion is not supported yet" in exc_info.value.args[0]


def test_process_text_raises():
    with pytest.raises(TypeError) as exc_info:
        _process_text(1, context="html")  # type: ignore

    assert "Invalid type: <class 'int'>" in exc_info.value.args[0]
