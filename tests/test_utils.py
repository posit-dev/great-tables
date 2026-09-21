from collections.abc import Generator
import re
import pytest


from great_tables import GT, exibble
from great_tables._utils import (
    _assert_list_is_subset,
    _assert_str_in_set,
    _assert_str_list,
    _assert_str_scalar,
    _collapse_list_elements,
    _insert_into_list,
    _match_arg,
    OrderedSet,
    _str_detect,
    _str_scalar_to_list,
    is_valid_http_schema,
    heading_has_subtitle,
    heading_has_title,
    seq_groups,
)


def test_heading_has_title():
    assert heading_has_title("title")
    assert not heading_has_title(None)


def test_heading_has_subtitle():
    assert heading_has_subtitle("subtitle")
    assert not heading_has_subtitle(None)


def test_match_arg():
    assert _match_arg("x", ["a", "b", "c", "x"]) == "x"


def test_match_arg_raises():
    with pytest.raises(ValueError) as exc_info:
        _match_arg("x", [])

    assert "The `lst` object must contain at least one element." in exc_info.value.args[0]

    with pytest.raises(ValueError) as exc_info:
        _match_arg("x", [1])

    assert "All elements in the `lst` object must be strings." in exc_info.value.args[0]

    with pytest.raises(ValueError) as exc_info:
        _match_arg("x", ["a", "a"])

    assert "The `lst` object must contain unique elements." in exc_info.value.args[0]

    with pytest.raises(ValueError) as exc_info:
        _match_arg("x", ["a"])

    assert "is not an allowed option." in exc_info.value.args[0]


def test_assert_str_scalar():
    _assert_str_scalar("a")


def test_assert_str_scalar_raises():
    with pytest.raises(AssertionError) as exc_info:
        _assert_str_scalar(1)

    assert "is not a string." in exc_info.value.args[0]


def test_assert_str_list():
    _assert_str_list(["a"])


def test_assert_str_list_raises():
    with pytest.raises(AssertionError) as exc_info:
        _assert_str_list(1)

    assert "is not a list." in exc_info.value.args[0]

    with pytest.raises(AssertionError) as exc_info:
        _assert_str_list([1])

    assert "Not all elements of the supplied list are strings." in exc_info.value.args[0]


def test_assert_str_in_set():
    _assert_str_in_set("a", ["a", "b", "c"])


def test_assert_str_in_set_raises():
    with pytest.raises(AssertionError) as exc_info:
        _assert_str_in_set("x", ["a", "b", "c"])

    assert "is not part of the defined `set`." in exc_info.value.args[0]


def test_assert_list_is_subset():
    _assert_list_is_subset([1, 2], [1, 2, 3])


def test_assert_list_is_subset_raises():
    with pytest.raises(AssertionError) as exc_info:
        _assert_list_is_subset([1, 2], [2, 3, 4])

    assert "The columns provided are not present in the table." in exc_info.value.args[0]


def test_str_scalar_to_list():
    x = _str_scalar_to_list("x")
    assert isinstance(x, list)
    assert x[0] == "x"


def test_orderedSet():
    o = OrderedSet([1, 2, "x", "y", 1, 2])

    assert all(x in o for x in [1, 2, "x", "y"])
    assert len(o) == 4
    assert list(o) == [1, 2, "x", "y"]
    assert o.as_list() == [1, 2, "x", "y"]
    assert o.as_set() == {1, 2, "x", "y"}
    assert o.as_dict() == {1: True, 2: True, "x": True, "y": True}
    assert repr(o) == "OrderedSet([1, 2, 'x', 'y'])"


@pytest.mark.parametrize(
    "iterable, ordered_list",
    [
        (["1", "2", "3"], ["1", "2", "3"]),
        (["1", "3", "2", "3", "1"], ["1", "3", "2"]),
        ((1, 3, 2, 3, 1, 1, 3, 2, 2), [1, 3, 2]),
        (iter("223311"), ["2", "3", "1"]),
    ],
)
def test_create_ordered_list(iterable, ordered_list):
    assert OrderedSet(iterable).as_list() == ordered_list


def test_collapse_list_elements():
    lst = ["a", "b", "c"]
    assert _collapse_list_elements(lst) == "abc"
    assert _collapse_list_elements(lst, "#") == "a#b#c"


def test_insert_into_list():
    lst = ["b", "c"]
    assert _insert_into_list(lst, "a") == ["a", "b", "c"]


@pytest.mark.parametrize(
    "seq, grouped",
    [
        ("a", [("a", 1)]),
        ("abc", [("a", 1), ("b", 1), ("c", 1)]),
        ("aabbcc", [("a", 2), ("b", 2), ("c", 2)]),
        ("aabbccd", [("a", 2), ("b", 2), ("c", 2), ("d", 1)]),
        (("a", "b", "c"), [("a", 1), ("b", 1), ("c", 1)]),
        (("aa", "bb", "cc"), [("aa", 1), ("bb", 1), ("cc", 1)]),
        (iter("xyyzzz"), [("x", 1), ("y", 2), ("z", 3)]),
        ((i for i in "333221"), [("3", 3), ("2", 2), ("1", 1)]),
        (["a", "a", "b", None, "c"], [("a", 2), ("b", 1), (None, 1), ("c", 1)]),
        (["a", "a", "b", None, None, "c"], [("a", 2), ("b", 1), (None, 1), (None, 1), ("c", 1)]),
        ([None, "a", "a", "b"], [(None, 1), ("a", 2), ("b", 1)]),
        ([None, None, "a", "a", "b"], [(None, 1), (None, 1), ("a", 2), ("b", 1)]),
        ([None, None, None, "a", "a", "b"], [(None, 1), (None, 1), (None, 1), ("a", 2), ("b", 1)]),
        ([None, None, None], [(None, 1), (None, 1), (None, 1)]),
    ],
)
def test_seq_groups(seq, grouped):
    g = seq_groups(seq)
    assert isinstance(g, Generator)
    assert list(g) == grouped


def test_seq_groups_raises():
    """
    https://stackoverflow.com/questions/66566960/pytest-raises-does-not-catch-stopiteration-error
    """
    with pytest.raises(RuntimeError) as exc_info:
        next(seq_groups([]))
    assert "StopIteration" in str(exc_info.value)


def test_migrate_unformatted_to_output_latex():
    gt_tbl = GT(exibble.head(2)).fmt_number(columns="num", decimals=3)

    # _render_formats escapes unformatted cells for the output context;
    # after rendering, the 'char' column should contain the original values
    # escaped for LaTeX (plain text like "apricot" is unchanged)
    rendered = gt_tbl._render_formats(context="latex")

    assert rendered._body.body["char"].tolist() == ["apricot", "banana"]


def test_migrate_unformatted_to_output_html():
    gt_tbl = GT(exibble.head(2)).fmt_number(columns="num", decimals=3)

    # _render_formats escapes unformatted cells for the output context;
    # after rendering, the 'char' column should contain the original values
    # escaped for HTML (plain text like "apricot" is unchanged)
    rendered = gt_tbl._render_formats(context="html")

    assert rendered._body.body["char"].tolist() == ["apricot", "banana"]


class TestHtmlEscaping:
    """Regression tests for HTML escaping of unformatted body cells (XSS prevention)."""

    def test_body_cells_are_escaped(self):
        import pandas as pd

        df = pd.DataFrame({"x": ["<img src=x onerror=alert(1)>", "<script>alert(1)</script>"]})
        html = GT(df).as_raw_html()

        assert "<img src=x onerror=alert(1)>" not in html
        assert "<script>alert(1)</script>" not in html
        assert "&lt;img src=x onerror=alert(1)&gt;" in html
        assert "&lt;script&gt;alert(1)&lt;/script&gt;" in html

    def test_ampersand_and_angle_brackets_escaped(self):
        import pandas as pd

        df = pd.DataFrame({"x": ["x & y", "a < b", "c > d"]})
        html = GT(df).as_raw_html()

        assert "x &amp; y" in html
        assert "a &lt; b" in html
        assert "c &gt; d" in html

    def test_formatted_cells_preserve_html(self):
        import pandas as pd
        from great_tables import html as gt_html

        df = pd.DataFrame({"x": ["hello"]})
        html = GT(df).fmt(columns="x", fns=lambda x: gt_html("<b>bold</b>").to_html()).as_raw_html()

        assert "<b>bold</b>" in html

    def test_mixed_formatted_and_unformatted(self):
        import pandas as pd

        df = pd.DataFrame({"x": ["<b>not bold</b>", "safe"], "y": [1, 2]})
        html = GT(df).fmt_number(columns="y", decimals=1).as_raw_html()

        assert "&lt;b&gt;not bold&lt;/b&gt;" in html
        assert ">safe<" in html
        assert ">1.0<" in html

    def test_group_label_escaped_without_groupname_col(self):
        import pandas as pd

        df = pd.DataFrame({"x": [1, 2], "grp": ["<script>xss</script>", "<script>xss</script>"]})
        html = GT(df, groupname_col="grp").as_raw_html()

        assert "<script>xss</script>" not in html
        assert "&lt;script&gt;xss&lt;/script&gt;" in html

    def test_summary_stub_label_escaped(self):
        import pandas as pd
        from great_tables import GT

        df = pd.DataFrame({"x": [1, 2], "grp": ["a", "a"]})
        gt_tbl = GT(df, groupname_col="grp", rowname_col="x").summary_rows(
            fns={"<b>mean</b>": lambda df: df.mean(numeric_only=True)}
        )
        html = gt_tbl.as_raw_html()

        assert "<b>mean</b>" not in html
        assert "&lt;b&gt;mean&lt;/b&gt;" in html


class TestFmtPassthrough:
    """Tests for fmt_passthrough()."""

    def test_escape_true_escapes_html(self):
        import pandas as pd

        df = pd.DataFrame({"x": ["<b>bold</b>", "x & y"]})
        html = GT(df).fmt_passthrough(columns="x").as_raw_html()

        assert "&lt;b&gt;bold&lt;/b&gt;" in html
        assert "x &amp; y" in html

    def test_escape_false_passes_through_html(self):
        import pandas as pd

        df = pd.DataFrame({"x": ["<b>bold</b>", "x & y"]})
        html = GT(df).fmt_passthrough(columns="x", escape=False).as_raw_html()

        assert "<b>bold</b>" in html
        assert "x & y" in html

    def test_pattern_decorates_values(self):
        import pandas as pd

        df = pd.DataFrame({"x": ["ABC", "DEF"]})
        html = GT(df).fmt_passthrough(columns="x", pattern="[{x}]").as_raw_html()

        assert "[ABC]" in html
        assert "[DEF]" in html

    def test_pattern_with_escape(self):
        import pandas as pd

        df = pd.DataFrame({"x": ["a < b"]})
        html = GT(df).fmt_passthrough(columns="x", pattern="({x})").as_raw_html()

        assert "(a &lt; b)" in html

    def test_escape_true_matches_auto_escaping(self):
        """fmt_passthrough(escape=True) should produce the same result as automatic escaping."""
        import pandas as pd

        df = pd.DataFrame({"x": ["<b>bold</b>", "x & y"]})

        auto_escaped = GT(df).as_raw_html()
        passthrough_escaped = GT(df).fmt_passthrough(columns="x").as_raw_html()

        assert "&lt;b&gt;bold&lt;/b&gt;" in auto_escaped
        assert "&lt;b&gt;bold&lt;/b&gt;" in passthrough_escaped
        assert "x &amp; y" in auto_escaped
        assert "x &amp; y" in passthrough_escaped

    def test_no_double_escape(self):
        """Cells formatted by fmt_passthrough should not be escaped again by the auto-escaping pass."""
        import pandas as pd

        df = pd.DataFrame({"x": ["a & b"]})
        html = GT(df).fmt_passthrough(columns="x").as_raw_html()

        assert "a &amp; b" in html
        assert "a &amp;amp; b" not in html

    def test_ordering_passthrough_then_other_formatter(self):
        """A later fmt_*() call overwrites fmt_passthrough (last-formatted-wins)."""
        import pandas as pd

        df = pd.DataFrame({"x": [1.5]})
        html = (
            GT(df)
            .fmt_passthrough(columns="x", escape=False)
            .fmt_number(columns="x", decimals=2)
            .as_raw_html()
        )

        assert "1.50" in html

    def test_ordering_other_formatter_then_passthrough(self):
        """fmt_passthrough called after another formatter wins (last-formatted-wins)."""
        import pandas as pd

        df = pd.DataFrame({"x": [1.5]})
        html = (
            GT(df)
            .fmt_number(columns="x", decimals=2)
            .fmt_passthrough(columns="x", pattern="({x})")
            .as_raw_html()
        )

        assert "(1.5)" in html

    def test_mixed_columns_escape_and_no_escape(self):
        """Different columns can have different escape settings."""
        import pandas as pd

        df = pd.DataFrame(
            {
                "safe": ["<b>text</b>"],
                "raw": ["<b>text</b>"],
            }
        )
        html = (
            GT(df)
            .fmt_passthrough(columns="safe", escape=True)
            .fmt_passthrough(columns="raw", escape=False)
            .as_raw_html()
        )

        assert "&lt;b&gt;text&lt;/b&gt;" in html
        assert "<b>text</b>" in html


@pytest.mark.parametrize(
    "url",
    [
        "http://posit.co/",
        "http://posit.co",
        "https://posit.co/",
        "https://posit.co",
        # URI schemes are case-insensitive (RFC 3986, Section 3.1)
        "HTTP://posit.co",
        "HTTPS://posit.co",
        "Https://posit.co",
        "hTTpS://posit.co",
    ],
)
def test_is_valid_http_schema(url: str):
    assert is_valid_http_schema(url)


@pytest.mark.parametrize(
    "url", ["posit.co", "ftp://posit.co", "/tmp/http://x.png", "httpx://posit.co", ""]
)
def test_is_valid_http_schema_false(url: str):
    assert not is_valid_http_schema(url)


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("int16", True),
        ("uint8", True),
        ("float32", True),
        ("date", True),
        ("datetime", True),
        ("string", False),
        ("object", False),
        ("utf8", False),
        ("bool", False),
        ("boolean", False),
        ("binary", False),
    ],
)
def test_str_detect_align_right_pattern(string: str, expected: bool) -> None:
    pattern = r"int|uint|float|date"
    assert _str_detect(string, pattern) is expected


def test_match_arg_rejects_non_prefix():
    with pytest.raises(ValueError) as exc_info:
        _match_arg("ight", ["left", "right"])

    assert "is not an allowed option" in exc_info.value.args[0]


def test_match_arg_rejects_empty_string():
    with pytest.raises(ValueError):
        _match_arg("", ["left", "right"])


def test_match_arg_rejects_ambiguous_abbreviation():
    with pytest.raises(ValueError) as exc_info:
        _match_arg("c", ["cyan", "center"])

    assert "ambiguous" in exc_info.value.args[0]


def test_match_arg_accepts_unambiguous_abbreviation():
    assert _match_arg("le", ["left", "right"]) == "left"


def test_match_arg_prefers_exact_match_over_longer_option():
    assert _match_arg("red", ["red", "reddish"]) == "red"
