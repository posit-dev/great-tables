"""Tests for `opt_interactive()` tables: GT tables rendered as `<gt-table>` elements.

(How the options map to the spec is tested in test_gti.py; GTI tables, in test_gti_class.py.)
"""

from __future__ import annotations

import json
import re
import warnings

import pandas as pd
import polars as pl
import pyarrow as pa
import pyarrow.compute as pc
import pytest

from great_tables import GT, GTI, loc, style
from great_tables._gti._render import _load_runtime, page_html
from great_tables._tbl_data import _re_version
from great_tables.data import exibble


@pytest.fixture()
def gt_mini() -> GT:
    df = pl.from_pandas(exibble[["num", "char", "currency"]]).head(5)
    return GT(df, id="mini")


def spec_in(html: str) -> dict:
    """The spec in a `<gt-table>` element's HTML."""
    found = re.search(r"<script type=\"application/json\" data-gti-spec>(.*?)</script>", html)
    assert found is not None, "no spec in the HTML"
    return json.loads(found.group(1))


def table_in(html: str) -> str:
    """The `<gt-table>` element's HTML (its table and spec), without the runtime after it."""
    element, _, _ = html.partition("</gt-table>\n")
    assert element.startswith("<gt-table")
    return element


# opt_interactive() stores its options ----


class TestOptInteractiveOptions:
    def test_active_default_false(self, gt_mini: GT):
        assert gt_mini._options.ihtml_active.value is False

    def test_active_set_true(self, gt_mini: GT):
        assert gt_mini.opt_interactive()._options.ihtml_active.value is True

    def test_active_explicit_false(self, gt_mini: GT):
        assert gt_mini.opt_interactive(active=False)._options.ihtml_active.value is False

    def test_options_stored(self, gt_mini: GT):
        options = gt_mini.opt_interactive(
            page_size_default=25,
            page_size_values=[5, 10, 20],
            use_search=True,
            use_filters=True,
            pagination_type="simple",
            height="400px",
        )._options
        assert options.ihtml_page_size_default.value == 25
        assert options.ihtml_page_size_values.value == [5, 10, 20]
        assert options.ihtml_use_search.value is True
        assert options.ihtml_use_filters.value is True
        assert options.ihtml_pagination_type.value == "simple"
        assert options.ihtml_height.value == "400px"

    def test_chaining_returns_gt(self, gt_mini: GT):
        result = gt_mini.opt_interactive(use_search=True).opt_interactive(page_size_default=20)
        assert type(result) is GT
        assert result._options.ihtml_page_size_default.value == 20


# The static table is unchanged without it ----


class TestStaticPathUnchanged:
    def test_static_html_not_interactive(self, gt_mini: GT):
        html = gt_mini.as_raw_html()
        assert "gt_table" in html
        assert "<gt-table" not in html

    def test_active_false_static(self, gt_mini: GT):
        html = gt_mini.opt_interactive(active=False).as_raw_html()
        assert html == gt_mini.as_raw_html()


# as_raw_html() renders a <gt-table> ----


class TestAsRawHtml:
    def test_is_a_gt_table_with_its_runtime(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        js, css = _load_runtime()
        # (No control bar, nor stacking in a narrow container: it scrolls)
        assert html.startswith("<gt-table>\n<div id=")
        assert html.endswith(f"<style>\n{css}</style>\n<script>\n{js}</script>\n")

    def test_has_the_static_table(self, gt_mini: GT):
        gt = gt_mini.opt_interactive()
        assert gt._render_as_html() in table_in(gt.as_raw_html())

    def test_needs_no_network(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        assert "importmap" not in html
        assert 'type="module"' not in html
        assert not re.search(r"""(src|href)=["']https?://""", html)

    def test_is_a_fragment(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        assert "<!DOCTYPE" not in html and "<meta" not in html

    def test_make_page(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html(make_page=True)
        assert html.startswith('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8"/>')
        assert '<meta name="viewport" content="width=device-width, initial-scale=1"/>' in html
        assert "<body>\n<gt-table>\n" in html
        assert html.endswith("</body>\n</html>\n")

    def test_make_page_as_gti_does(self):
        gt = GT(pl.DataFrame({"x": [1]}), id="t").opt_interactive()
        assert gt.as_raw_html(make_page=True) == page_html(gt.as_raw_html())

    def test_all_important(self):
        gt = GT(pl.DataFrame({"x": [1]}), id="t").opt_interactive()
        assert "!important" not in table_in(gt.as_raw_html())
        assert re.search(r"#t \.gt_row {[^}]*?!important", gt.as_raw_html(all_important=True))

    def test_inline_css_is_ignored(self, gt_mini: GT):
        gt = gt_mini.opt_interactive()
        assert gt.as_raw_html(inline_css=True) == gt.as_raw_html()

    def test_unique_ids_across_tables(self):
        df = pl.DataFrame({"x": [1, 2]})
        html_a, html_b = (GT(df).opt_interactive().as_raw_html() for _ in range(2))
        id_a = re.match(r'<gt-table>\n<div id="([^"]+)"', html_a)
        id_b = re.match(r'<gt-table>\n<div id="([^"]+)"', html_b)
        assert id_a and id_b and id_a.group(1) != id_b.group(1)

    def test_spec_has_every_column(self, gt_mini: GT):
        spec = spec_in(gt_mini.opt_interactive().as_raw_html())
        assert [c["id"] for c in spec["columns"]] == ["num", "char", "currency"]
        assert spec["nrows"] == 5

    def test_options_in_spec(self, gt_mini: GT):
        html = gt_mini.opt_interactive(
            use_search=True,
            use_sorting=False,
            use_resizers=True,
            use_page_size_select=True,
            page_size_default=2,
            page_size_values=[2, 4],
            pagination_type="full",
            use_compact_mode=True,
            use_highlight=True,
            selection_mode="multiple",
        ).as_raw_html()
        spec = spec_in(html)
        assert spec["controls"] == {
            "sorting": False,
            "search": True,
            "resizing": True,
            "selection": "multiple",
            "bar": False,
        }
        assert spec["pagination"] == {
            "enabled": True,
            "page_size": 2,
            "page_sizes": [2, 4],
            "size_select": True,
            "info": True,
            "type": "full",
        }
        assert spec["display"] == {
            "highlight": True,
            "compact": True,
            "wrap": True,
            "monospace": False,
            "row_numbers": False,
            "row_start": 0,
            "dimensions": False,
            "data_kind": None,
        }

    @pytest.mark.parametrize(
        "height, expected",
        [("400px", "400px"), (400, "400px"), ("50vh", "50vh"), ("auto", None)],
    )
    def test_height(self, gt_mini: GT, height, expected):
        html = gt_mini.opt_interactive(height=height).as_raw_html()
        assert spec_in(html)["layout"]["height"] == expected
        if expected is None:
            assert html.startswith("<gt-table>\n")
        else:
            assert html.startswith(f'<gt-table data-gti-scroll style="--gt-i-height: {expected}">')

    def test_text_wrapping_off_marks_the_element(self, gt_mini: GT):
        html = gt_mini.opt_interactive(use_text_wrapping=False).as_raw_html()
        assert html.startswith("<gt-table data-gti-nowrap>\n")


# use_filters= ----


class TestUseFilters:
    def test_off_by_default(self, gt_mini: GT):
        assert spec_in(gt_mini.opt_interactive().as_raw_html())["filters"] == []

    def test_every_column_filtered_by_its_type(self):
        df = pl.DataFrame(
            {
                "name": [f"n{i}" for i in range(30)],
                "num": [i * 1.5 for i in range(30)],
                "few": ["a", "b", "c"] * 10,
                "flag": [True, False] * 15,
            }
        )
        spec = spec_in(GT(df).opt_interactive(use_filters=True).as_raw_html())
        assert [(f["column"], f["type"]) for f in spec["filters"]] == [
            ("name", "text"),
            ("num", "range"),
            ("few", "facet"),
            ("flag", "bool"),
        ]

    def test_not_the_stub_nor_the_groups(self):
        df = pl.DataFrame({"g": ["a", "b"], "r": ["x", "y"], "n": [1, 2]})
        gt = GT(df, rowname_col="r", groupname_col="g").opt_interactive(use_filters=True)
        assert [f["column"] for f in spec_in(gt.as_raw_html())["filters"]] == ["n"]

    def test_as_in_a_gti_made_from_it(self, gt_mini: GT):
        gt = gt_mini.opt_interactive(use_filters=True)
        assert (
            spec_in(gt.as_raw_html())["filters"]
            == spec_in(GTI.from_gt(gt).as_raw_html())["filters"]
        )


# The table's structure and styles are kept ----


class TestStructure:
    def test_header_and_footer(self, gt_mini: GT):
        gt = (
            gt_mini.tab_header(title="The Title", subtitle="The Subtitle")
            .tab_source_note("My note")
            .tab_footnote("A footnote", locations=loc.column_labels(columns="num"))
            .opt_interactive()
        )
        element = table_in(gt.as_raw_html())
        for text in ("The Title", "The Subtitle", "My note", "A footnote"):
            assert text in element

    def test_stub_groups_spanners_and_summary_rows(self):
        df = pl.DataFrame({"g": ["a", "a", "b"], "r": ["x", "y", "z"], "n": [1, 2, 3]})
        gt = (
            GT(df, rowname_col="r", groupname_col="g")
            .tab_spanner("Values", ["n"])
            .summary_rows(groups="a", fns={"Sum": pl.col("n").sum()})
            .opt_interactive()
        )
        # (The reactable renderer warned that it dropped spanners and summary rows)
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            html = gt.as_raw_html()
        spec = spec_in(html)
        assert [c["role"] for c in spec["columns"]] == ["stub", "data"]
        assert [s["header"] for s in spec["spanners"]] == ["Values"]
        assert [g["id"] for g in spec["groups"]] == ["a", "b"]
        assert "gt_summary_row" in table_in(html)

    def test_styles_in_the_table(self):
        df = pl.DataFrame({"a": [1, 2, 3], "b": [10, 20, 30]})
        gt = (
            GT(df)
            .tab_style(
                style=style.fill(color="yellow"),
                locations=loc.body(columns="a", rows=pl.col("a") == 2),
            )
            .tab_style(style=style.fill(color="#abc"), locations=loc.column_labels(columns="b"))
            .data_color(columns="b", palette=["#ffffff", "#ff0000"])
            .opt_interactive()
        )
        element = table_in(gt.as_raw_html())
        assert element.count("background-color: yellow;") == 1
        assert "background-color: #abc;" in element
        assert element.count("background-color: #ff0000;") == 1

    def test_formatted_values_shown_and_sorted_by_value(self):
        df = pl.DataFrame({"val": [1234.5, 99.0, None]})
        html = GT(df).fmt_number("val", decimals=2).sub_missing().opt_interactive().as_raw_html()
        assert "1,234.50" in table_in(html)
        spec = spec_in(html)
        assert spec["columns"][0]["kind"] == "number"
        assert spec["ranks"]["val"][1] < spec["ranks"]["val"][0]

    def test_column_widths(self):
        gt = GT(pl.DataFrame({"a": [1], "b": [2]})).cols_width({"a": "120px"}).opt_interactive()
        assert "width:120px;" in table_in(gt.as_raw_html()).replace(" ", "")


# Parameterized dtypes ----


@pytest.mark.parametrize(
    "make_frame, kind",
    [
        pytest.param(
            lambda: pl.DataFrame(
                {"x": ["point", "line", "point"]}, schema={"x": pl.Enum(["point", "line"])}
            ),
            "category",
            id="polars-enum",
        ),
        pytest.param(lambda: pd.DataFrame({"x": pd.interval_range(0, 3)}), "other", id="interval"),
        pytest.param(
            lambda: pa.table({"x": pc.run_end_encode(pa.array(["a", "a", "b"]))}),
            "other",
            id="pyarrow-run_end_encoded",
            marks=pytest.mark.skipif(
                _re_version(pa.__version__) < (26, 0, 0),
                reason="pyarrow < 26 can't cast run-end-encoded arrays to string",
            ),
        ),
        pytest.param(
            lambda: pa.table({"x": pa.array([10, 9, 10]).dictionary_encode()}),
            "category",
            id="pyarrow-dictionary-numbers",
        ),
        pytest.param(
            lambda: pa.table(
                {
                    "x": pa.UnionArray.from_sparse(
                        pa.array([0, 1, 0], pa.int8()),
                        [pa.array([1, 0, 3]), pa.array(["", "y", ""])],
                    )
                }
            ),
            "other",
            id="pyarrow-sparse_union",
        ),
        pytest.param(lambda: pl.DataFrame({"x": [[1, 2], [3], [], None]}), "other", id="list"),
    ],
)
def test_parameterized_dtypes_are_not_numbers(make_frame, kind: str):
    # (A numeric type in a dtype's parameters made reactable's renderer take the values as numbers:
    # #1045, #1028)
    spec = spec_in(GT(make_frame()).opt_interactive(use_filters=True).as_raw_html())
    assert spec["columns"][0]["kind"] == kind
    assert spec["filters"][0]["type"] != "range"
