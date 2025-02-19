import commonmark
import html
import pytest
import re
from dataclasses import (
    dataclass,
)
from great_tables._text import (
    BaseText,
    Html,
    Md,
    Text,
    _html_escape,
    _latex_escape,
    _md_html,
    _md_latex,
    _process_text,
    _process_text_id,
    escape_pattern_str_latex,
    process_string,
)
from typing import (
    Callable,
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
    assert (
        _process_text(Md("**a** & <b>"), context="html")
        == "<strong>a</strong> &amp; <b>"
    )
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
        _process_text(1, context="html")
    assert "Invalid type: <class 'int'>" in exc_info.value.args[0]


def test_process_text_id():
    """Test that _process_text_id replaces spaces with dashes after processing text.

    This covers the scenario when the input is a plain string, a Text instance, and a string
    that involves HTML escaping.
    """
    assert _process_text_id("Hello World") == "Hello-World"
    text_obj = Text("Make me an id")
    assert _process_text_id(text_obj) == "Make-me-an-id"
    assert _process_text_id("A & B") == "A-&amp;-B"


def test_process_string():
    """
    Test that process_string applies the given function only to segments that do not match a regex pattern,
    covering various scenarios including patterns at the beginning and no matches at all.
    """
    pattern = "(\\d+)"
    fn = lambda s: f"<{s}>"
    input_str = "Hello123World456!"
    expected = "<Hello>" + "123" + "<World>" + "456" + "<!>"
    result = process_string(input_str, pattern, fn)
    assert result == expected
    input_str2 = "123Hello"
    expected2 = "<>" + "123" + "<Hello>"
    result2 = process_string(input_str2, pattern, fn)
    assert result2 == expected2
    input_str3 = "abc"
    expected3 = "<abc>"
    result3 = process_string(input_str3, pattern, fn)
    assert result3 == expected3


def test_process_text_with_unexpected_context():
    """
    Test that _process_text applies LaTeX escaping when the context is not 'html'.
    In this case, a context value other than "html" (e.g., "unexpected") should trigger
    the latex escaping branch.
    """
    input_str = "a & b"
    expected = _latex_escape(input_str)
    result = _process_text(input_str, context="unexpected")
    assert result == expected


def test_md_to_latex_not_implemented():
    """
    Test that _md_latex raises NotImplementedError when attempting
    to convert Markdown to LaTeX, as this functionality is not implemented.
    """
    with pytest.raises(NotImplementedError) as exc_info:
        _md_latex("**Markdown**")
    assert "Markdown to LaTeX conversion is not supported yet" in str(exc_info.value)


def test_process_string_non_capturing():
    """
    Test that process_string correctly handles a regex pattern with no capturing groups.
    In this scenario, since the pattern does not capture the matched segments, those parts
    are omitted from the output. This test demonstrates that behavior.
    """
    pattern = "\\d+"
    fn = lambda s: f"[{s}]"
    input_str = "abc123def"
    expected = "[abc][def]"
    result = process_string(input_str, pattern, fn)
    assert result == expected


def test_process_text_custom_base_text():
    """
    Test that _process_text correctly calls the to_html and to_latex methods
    on a custom subclass of BaseText. This ensures that when using a non-built-in
    BaseText subclass, _process_text behaves as expected.
    """

    class Dummy(BaseText):

        def to_html(self) -> str:
            return "dummy html"

        def to_latex(self) -> str:
            return "dummy latex"

    dummy_instance = Dummy()
    assert _process_text(dummy_instance, context="html") == "dummy html"
    assert _process_text(dummy_instance, context="latex") == "dummy latex"


def test_process_string_with_adjacent_matches():
    """
    Test process_string behavior for the scenario when
    the regex pattern with a capturing group matches the entire string.
    Since re.split returns a single match (["", "123123", ""]),
    the expected result becomes "<>123123<>", not "<>123<>123<>".
    """
    pattern = "(\\d+)"
    fn = lambda s: f"<{s}>"
    input_str = "123123"
    expected = "<>123123<>"
    result = process_string(input_str, pattern, fn)
    assert result == expected


def test_html_escape_directly():
    """
    Test that _html_escape correctly escapes HTML special characters.
    This ensures that the helper function produces the expected results.
    """
    test_input = '<div class="example">& "special" \'characters\'</div>'
    expected_output = html.escape(test_input)
    result = _html_escape(test_input)
    assert result == expected_output


def test_md_html_strips_paragraph_tags():
    """
       Test that _md_html correctly removes the wrapping <p> and </p>
    from
       the HTML output produced by commonmark, including handling an empty string.
       This ensures that the markdown to HTML helper function processes the text
       as expected.
    """
    md_input = "Hello, world!"
    expected_normal = "Hello, world!"
    result_normal = _md_html(md_input)
    assert (
        result_normal == expected_normal
    ), f"Expected '{expected_normal}', got '{result_normal}'"
    md_empty = ""
    expected_empty = ""
    result_empty = _md_html(md_empty)
    assert (
        result_empty == expected_empty
    ), f"Expected empty string, got '{result_empty}'"


def test_latex_escape_extra_chars():
    """
    Test that _latex_escape correctly escapes all LaTeX special characters,
    including tilde (~) and caret (^), producing the expected output.
    """
    special_chars = "\\&%$#_{}~^"
    result = _latex_escape(special_chars)
    expected = "".join(("\\" + ch for ch in special_chars))
    assert result == expected
