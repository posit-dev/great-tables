import pytest

from great_tables._text import (
    BaseText,
    Text,
    Md,
    Html,
    _latex_escape,
    escape_pattern_str_latex,
    _process_text,
    _md_latex,
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
    assert Html("<strong>text</strong>").to_latex() == "text"


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
    assert _process_text(Html("**a** & <b>bold</b>"), context="latex") == "**a** \\& bold"
    assert _process_text(Md("**a**"), context="latex") == "\\textbf{a}"
    assert _process_text(None, context="latex") == ""


def test_process_text_raises():
    with pytest.raises(TypeError) as exc_info:
        _process_text(1, context="html")  # type: ignore

    assert "Invalid type: <class 'int'>" in exc_info.value.args[0]


def test_md_latex():
    assert _md_latex("Testing **bold** text") == "Testing \\textbf{bold} text"
    assert _md_latex("Testing *italic* text") == "Testing \\emph{italic} text"
    assert _md_latex("Testing `code` text") == "Testing \\texttt{code} text"
    assert _md_latex("A [link](https://example.com)") == "A \\href{https://example.com}{link}"
    assert _md_latex("~~struck~~") == "\\sout{struck}"
    assert _md_latex("**bold** and *italic*") == "\\textbf{bold} and \\emph{italic}"


def test_md_html():
    assert Md("*italic*").to_html() == "<em>italic</em>"
    assert Md("`code`").to_html() == "<code>code</code>"
    assert Md("[link](http://x.com)").to_html() == '<a href="http://x.com">link</a>'
    assert Md("**bold** and *italic*").to_html() == "<strong>bold</strong> and <em>italic</em>"
    # unsafe=True: raw HTML passes through
    assert Md("<b>raw</b>").to_html() == "<b>raw</b>"


def test_html_to_latex_strips_tags():
    # Tags are stripped, remaining text is LaTeX-escaped
    assert Html("<b>bold</b>").to_latex() == "bold"
    assert Html("<em>italic</em>").to_latex() == "italic"
    assert Html('<a href="http://x.com">link</a>').to_latex() == "link"
    assert Html("<br/>").to_latex() == ""
    assert Html("<span class='x'>text</span>").to_latex() == "text"
    # Nested tags
    assert Html("<b><em>nested</em></b>").to_latex() == "nested"


def test_html_to_latex_escapes_special_chars():
    # Special LaTeX chars in content are escaped after tag stripping
    assert Html("<b>a & b</b>").to_latex() == "a \\& b"
    assert Html("<em>100%</em>").to_latex() == "100\\%"
    assert Html("<b>$10</b>").to_latex() == "\\$10"
    assert Html("a & <b>b</b> & c").to_latex() == "a \\& b \\& c"
