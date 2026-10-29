"""Tests for the interactive HTML table rendering path."""

from __future__ import annotations

import json
import re

import pandas as pd
import polars as pl
import pyarrow as pa
import pyarrow.compute as pc
import pytest

from great_tables import GT, html, md, style, loc
from great_tables.data import exibble
from tests.utils import DataFrameConstructor


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def gt_mini() -> GT:
    df = pl.from_pandas(exibble[["num", "char", "currency"]]).head(5)
    return GT(df)


@pytest.fixture()
def gt_with_header(gt_mini: GT) -> GT:
    return gt_mini.tab_header(title="Title", subtitle="Subtitle")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _extract_props(html: str) -> dict:
    """Extract the props dict from rendered HTML."""
    m = re.search(r"const _props = (\{.*?\});\n", html, re.DOTALL)
    assert m, "Could not find props JSON in HTML"
    return json.loads(m.group(1))


# ---------------------------------------------------------------------------
# opt_interactive stores options correctly
# ---------------------------------------------------------------------------


class TestOptInteractiveOptions:
    def test_active_default_false(self, gt_mini: GT):
        assert gt_mini._options.ihtml_active.value is False

    def test_active_set_true(self, gt_mini: GT):
        t = gt_mini.opt_interactive()
        assert t._options.ihtml_active.value is True

    def test_active_explicit_false(self, gt_mini: GT):
        t = gt_mini.opt_interactive(active=False)
        assert t._options.ihtml_active.value is False

    def test_page_size_stored(self, gt_mini: GT):
        t = gt_mini.opt_interactive(page_size_default=25)
        assert t._options.ihtml_page_size_default.value == 25

    def test_page_size_values_stored(self, gt_mini: GT):
        t = gt_mini.opt_interactive(page_size_values=[5, 10, 20])
        assert t._options.ihtml_page_size_values.value == [5, 10, 20]

    def test_use_search_stored(self, gt_mini: GT):
        t = gt_mini.opt_interactive(use_search=True)
        assert t._options.ihtml_use_search.value is True

    def test_use_filters_stored(self, gt_mini: GT):
        t = gt_mini.opt_interactive(use_filters=True)
        assert t._options.ihtml_use_filters.value is True

    def test_pagination_type_stored(self, gt_mini: GT):
        t = gt_mini.opt_interactive(pagination_type="simple")
        assert t._options.ihtml_pagination_type.value == "simple"

    def test_height_stored(self, gt_mini: GT):
        t = gt_mini.opt_interactive(height="400px")
        assert t._options.ihtml_height.value == "400px"

    def test_chaining_returns_gt(self, gt_mini: GT):
        result = gt_mini.opt_interactive(use_search=True).opt_interactive(page_size_default=20)
        assert isinstance(result, GT)
        assert result._options.ihtml_page_size_default.value == 20


# ---------------------------------------------------------------------------
# Static path is unchanged when opt_interactive is not called
# ---------------------------------------------------------------------------


class TestStaticPathUnchanged:
    def test_static_html_no_interactive(self, gt_mini: GT):
        html = gt_mini.as_raw_html()
        assert "gt_table" in html
        assert "Reactable2" not in html

    def test_active_false_static(self, gt_mini: GT):
        html = gt_mini.opt_interactive(active=False).as_raw_html()
        assert "gt_table" in html
        assert "Reactable2" not in html


# ---------------------------------------------------------------------------
# Interactive rendering produces valid output
# ---------------------------------------------------------------------------


class TestRenderAsIhtml:
    def test_returns_string(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        assert isinstance(html, str)
        assert len(html) > 1000

    def test_contains_init(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        assert "Reactable2" in html

    def test_contains_importmap(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        assert 'type="importmap"' in html
        assert "esm.sh/react" in html

    def test_contains_module_script(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        assert 'type="module"' in html

    def test_no_meta_charset(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        assert "<meta charset" not in html

    def test_mount_id_present(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        assert "gt-ihtml-" in html

    def test_unique_ids_across_tables(self):
        df = pl.from_pandas(exibble[["num"]].head(3))
        html_a = GT(df).opt_interactive().as_raw_html()
        html_b = GT(df).opt_interactive().as_raw_html()
        ids_a = re.findall(r'id="(gt-ihtml-[^"]+)"', html_a)
        ids_b = re.findall(r'id="(gt-ihtml-[^"]+)"', html_b)
        assert ids_a and ids_b
        assert ids_a[0] != ids_b[0]

    def test_all_columns_in_props(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive().as_raw_html())
        col_ids = [c["id"] for c in props["columns"]]
        for col in ["num", "char", "currency"]:
            assert col in col_ids

    def test_columnar_data_in_props(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive().as_raw_html())
        assert isinstance(props["data"], dict)
        for col in ["num", "char", "currency"]:
            assert col in props["data"]
            assert isinstance(props["data"][col], list)


# ---------------------------------------------------------------------------
# Feature flags map to props
# ---------------------------------------------------------------------------


class TestFeatureFlags:
    def test_search_disabled_by_default(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive().as_raw_html())
        assert props["searchable"] is False

    def test_search_enabled(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive(use_search=True).as_raw_html())
        assert props["searchable"] is True

    def test_sorting_enabled_by_default(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive().as_raw_html())
        assert props["sortable"] is True

    def test_sorting_disabled(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive(use_sorting=False).as_raw_html())
        assert props["sortable"] is False

    def test_pagination_enabled_by_default(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive().as_raw_html())
        assert props["pagination"] is True

    def test_pagination_disabled(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive(use_pagination=False).as_raw_html())
        assert props["pagination"] is False

    def test_filter_enabled(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive(use_filters=True).as_raw_html())
        assert props["filterable"] is True

    def test_filter_disabled_by_default(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive().as_raw_html())
        assert props["filterable"] is False

    def test_page_info_enabled_by_default(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive().as_raw_html())
        assert props["showPageInfo"] is True

    def test_page_size_default(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive(page_size_default=25).as_raw_html())
        assert props["defaultPageSize"] == 25

    def test_page_size_values(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive(page_size_values=[5, 10]).as_raw_html())
        assert props["pageSizeOptions"] == [5, 10]

    def test_pagination_type_numbers(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive(pagination_type="numbers").as_raw_html())
        assert props["paginationType"] == "numbers"

    def test_pagination_type_simple(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive(pagination_type="simple").as_raw_html())
        assert props["paginationType"] == "simple"

    def test_height_set(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive(height="400px").as_raw_html())
        assert props["height"] == "400px"

    def test_height_auto_not_in_props(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive(height="auto").as_raw_html())
        assert "height" not in props

    def test_compact_disabled_by_default(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive().as_raw_html())
        assert props["compact"] is False

    def test_compact_enabled(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive(use_compact_mode=True).as_raw_html())
        assert props["compact"] is True


# ---------------------------------------------------------------------------
# Header / footer passthrough
# ---------------------------------------------------------------------------


class TestHeaderFooter:
    def test_title_rendered(self, gt_with_header: GT):
        html = gt_with_header.opt_interactive().as_raw_html()
        assert "gt-ihtml-title" in html
        assert "Title" in html

    def test_subtitle_rendered(self, gt_with_header: GT):
        html = gt_with_header.opt_interactive().as_raw_html()
        assert "gt-ihtml-subtitle" in html
        assert "Subtitle" in html

    def test_source_note_rendered(self, gt_mini: GT):
        html = gt_mini.tab_source_note("My note").opt_interactive().as_raw_html()
        assert "gt-ihtml-source-note" in html
        assert "My note" in html

    def test_no_header_when_absent(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        assert '<div class="gt-ihtml-header">' not in html


# ---------------------------------------------------------------------------
# tab_style() integration — loc.body() and loc.column_labels()
# ---------------------------------------------------------------------------


class TestTabStyle:
    @pytest.fixture()
    def gt_styled(self) -> GT:
        df = pl.DataFrame({"a": [1, 2, 3], "b": [10, 20, 30]})
        return (
            GT(df)
            .tab_style(
                style=style.fill(color="yellow"),
                locations=loc.body(columns="a", rows=pl.col("a") == 2),
            )
            .tab_style(
                style=style.text(color="red", weight="bold"),
                locations=loc.body(columns="b", rows=pl.col("b") == 30),
            )
            .tab_style(
                style=style.fill(color="#abc"),
                locations=loc.column_labels(columns="b"),
            )
            .opt_interactive()
        )

    def test_body_fill_style_in_col_def(self, gt_styled: GT):
        props = _extract_props(gt_styled.as_raw_html())
        col_a = next(c for c in props["columns"] if c["id"] == "a")
        assert "style" in col_a
        # style is a {code: "..."} JS callback for sort-stability
        assert "code" in col_a["style"]
        # row index 1 is where a==2 — check the lookup table embedded in the code
        assert '"1"' in col_a["style"]["code"]
        assert "yellow" in col_a["style"]["code"]

    def test_body_text_style_in_col_def(self, gt_styled: GT):
        props = _extract_props(gt_styled.as_raw_html())
        col_b = next(c for c in props["columns"] if c["id"] == "b")
        assert "style" in col_b
        # row index 2 is where b==30
        assert '"2"' in col_b["style"]["code"]
        assert "red" in col_b["style"]["code"]
        assert "bold" in col_b["style"]["code"]

    def test_unstyles_rows_absent_from_lookup(self, gt_styled: GT):
        props = _extract_props(gt_styled.as_raw_html())
        col_a = next(c for c in props["columns"] if c["id"] == "a")
        code = col_a["style"]["code"]
        # rows 0 and 2 (a==1 and a==3) have no style — their keys absent from lookup
        import json, re

        m = re.search(r"var s=(\{.*?\});", code)
        lookup = json.loads(m.group(1))
        assert "0" not in lookup
        assert "2" not in lookup

    def test_col_label_style_in_header_style(self, gt_styled: GT):
        props = _extract_props(gt_styled.as_raw_html())
        col_b = next(c for c in props["columns"] if c["id"] == "b")
        assert "headerStyle" in col_b
        assert "abc" in col_b["headerStyle"].get("backgroundColor", "")

    def test_no_style_fn_when_no_tab_style(self):
        df = pl.DataFrame({"x": [1, 2]})
        props = _extract_props(GT(df).opt_interactive().as_raw_html())
        for col_def in props["columns"]:
            assert "style" not in col_def

    def test_data_color_produces_style_fn(self):
        df = pl.DataFrame({"a": [10, 50, 100], "b": ["x", "y", "z"]})
        props = _extract_props(
            GT(df)
            .data_color(columns="a", palette=["#ffffff", "#ff0000"])
            .opt_interactive()
            .as_raw_html()
        )
        col_a = next(c for c in props["columns"] if c["id"] == "a")
        assert "style" in col_a
        assert "code" in col_a["style"]
        # All 3 rows get a background color — keys "0", "1", "2" in the lookup
        import json, re

        m = re.search(r"var s=(\{.*?\});", col_a["style"]["code"])
        lookup = json.loads(m.group(1))
        assert len(lookup) == 3
        for s in lookup.values():
            assert "backgroundColor" in s

    def test_unsupported_location_does_not_crash(self):
        df = pl.DataFrame({"x": [1, 2]})
        html = (
            GT(df)
            .tab_header(title="T")
            .tab_style(style=style.fill(color="blue"), locations=loc.header())
            .opt_interactive()
            .as_raw_html()
        )
        assert "Reactable2" in html


# ---------------------------------------------------------------------------
# Column width pre-sizing
# ---------------------------------------------------------------------------


class TestColumnWidths:
    def test_every_column_has_min_width(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive().as_raw_html())
        for col_def in props["columns"]:
            assert "minWidth" in col_def, f"column {col_def.get('id')} missing 'minWidth'"

    def test_min_width_is_integer(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive().as_raw_html())
        for col_def in props["columns"]:
            assert isinstance(col_def["minWidth"], int)

    def test_markup_and_entities_not_counted(self):
        # `1.50 × 10³` is written with `&nbsp;` and a `<sup>`, but is 10 characters wide, like
        # `1.50 x 103` written as plain text
        df = pl.DataFrame({"sci": [1500.0], "plain": ["1.50 x 103"]})
        props = _extract_props(GT(df).fmt_scientific("sci").opt_interactive().as_raw_html())
        min_widths = {c["id"]: c["minWidth"] for c in props["columns"]}

        assert min_widths["sci"] == min_widths["plain"] == int(10 * 14 * 0.6 + 20 + 24)

    def test_label_lines_measured_separately(self):
        df = pl.DataFrame({"x": ["a"]})
        gt = GT(df).cols_label(x=html("Speed<br>(km/h)"))
        props = _extract_props(gt.opt_interactive().as_raw_html())

        # The widest line is `(km/h)` (6 characters)
        assert props["columns"][0]["minWidth"] == int(6 * 14 * 0.6 + 20 + 24)

    def test_nanoplot_width_from_view_box(self):
        df = pl.DataFrame({"np": ["1 2 3 4 5"]})
        props = _extract_props(GT(df).fmt_nanoplot("np").opt_interactive().as_raw_html())

        # The nanoplot SVG is 2em high (at 14px) with a 350 x 130 `viewBox`, so ~75px wide; its
        # markup (thousands of characters, including `<text>` elements) isn't counted
        assert props["columns"][0]["minWidth"] == int(2 * 14 * 350 / 130 + 20 + 24)


class TestHtmlWidthPx:
    @pytest.mark.parametrize(
        "html_str,width_px",
        [
            ("abc", 3 * 8.4),
            ("a&nbsp;&amp;&nbsp;b", 5 * 8.4),
            ("<strong>bold</strong> text", 9 * 8.4),
            ("ab<br>abcd<br/>a", 4 * 8.4),
            # Images and inline SVGs: their own width, else height times the aspect ratio
            ('<img src="x.png" style="height: 20px;width: 50px;">', 50),
            ('<img src="x.png" style="height: 3em;vertical-align: middle;">', 3 * 14),
            ('<img src="x.png">', 2 * 14),
            ('<svg viewBox="0 0 200 100" style="height: 1em;"><text>long label</text></svg>', 28),
            ('ab <span><svg width="10" height="20"></svg></span>', 3 * 8.4 + 10),
        ],
    )
    def test_width(self, html_str: str, width_px: float):
        from great_tables._ihtml import _html_width_px

        assert _html_width_px(html_str, font_size_px=14, char_width_px=8.4) == pytest.approx(
            width_px
        )


class TestCellHtml:
    @pytest.fixture()
    def props(self) -> dict:
        df = pl.DataFrame(
            {"md": ["**bold** & more", "plain"], "text": ["a & <b>", "c"], "k": ["x", "y"]}
        )
        return _extract_props(GT(df).fmt_markdown("md").opt_interactive().as_raw_html())

    def test_every_column_is_html(self, props: dict):
        assert all(c["html"] is True for c in props["columns"])

    def test_cells_shown_as_formatted_html(self, props: dict):
        cols = {c["id"]: c for c in props["columns"]}

        assert cols["md"]["cell"] == ["<strong>bold</strong> &amp; more", "plain"]
        # Unformatted text is escaped, as in the static table
        assert cols["text"]["cell"] == ["a &amp; &lt;b&gt;", "c"]
        # A column without markup or entities doesn't need `cell`
        assert "cell" not in cols["k"]

    def test_data_holds_visible_text(self, props: dict):
        # Searching, sorting and filtering use the text that is shown
        assert props["data"] == {
            "md": ["bold & more", "plain"],
            "text": ["a & <b>", "c"],
            "k": ["x", "y"],
        }


class TestColumnLabelHtml:
    def test_labels_are_html(self):
        df = pl.DataFrame({"a": [1.0], "b": ["x"], "c": ["y"], "d": ["z"]})
        gt = GT(df).cols_label(a=html("Speed<br>(km/h)"), b=md("**Bold** & co"), c="A <b> B")
        props = _extract_props(gt.opt_interactive().as_raw_html())

        assert [c.get("header") for c in props["columns"]] == [
            "Speed<br>(km/h)",
            "<strong>Bold</strong> &amp; co",
            "A &lt;b&gt; B",
            None,
        ]

    def test_names_are_label_text(self):
        # reactable puts `name` in the sort and filter aria-labels ("Sort {name}")
        df = pl.DataFrame({"a": [1.0], "b": ["x"], "c": ["y"], "d": ["z"]})
        gt = GT(df).cols_label(a=html("Speed<br>(km/h)"), b=md("**Bold** & co"), c="A <b> B")
        props = _extract_props(gt.opt_interactive().as_raw_html())

        assert [c["name"] for c in props["columns"]] == [
            "Speed (km/h)",
            "Bold & co",
            "A <b> B",
            "d",
        ]


# ---------------------------------------------------------------------------
# Row striping
# ---------------------------------------------------------------------------


class TestRowStriping:
    def test_striped_false_by_default(self, gt_mini: GT):
        props = _extract_props(gt_mini.opt_interactive().as_raw_html())
        assert props["striped"] is False

    def test_striped_true_when_option_enabled(self, gt_mini: GT):
        props = _extract_props(
            gt_mini.tab_options(row_striping_include_table_body=True)
            .opt_interactive()
            .as_raw_html()
        )
        assert props["striped"] is True


# ---------------------------------------------------------------------------
# CSS conversion helper
# ---------------------------------------------------------------------------


class TestCssToReactStyle:
    def test_background_color(self):
        from great_tables._ihtml import _css_str_to_react_style

        result = _css_str_to_react_style("background-color: yellow;")
        assert result == {"backgroundColor": "yellow"}

    def test_font_weight_and_color(self):
        from great_tables._ihtml import _css_str_to_react_style

        result = _css_str_to_react_style("color:red;font-weight:bold;")
        assert result["color"] == "red"
        assert result["fontWeight"] == "bold"

    def test_important_stripped(self):
        from great_tables._ihtml import _css_str_to_react_style

        result = _css_str_to_react_style("background-color: blue !important;")
        assert result["backgroundColor"] == "blue"

    def test_empty_string(self):
        from great_tables._ihtml import _css_str_to_react_style

        assert _css_str_to_react_style("") == {}


# ---------------------------------------------------------------------------
# ihtml helper functions
# ---------------------------------------------------------------------------


class TestColLabel:
    def test_label_set_returns_label(self):
        from great_tables._ihtml import _col_label
        from great_tables._gt_data import ColInfo, ColInfoTypeEnum

        col = ColInfo(var="my_col", type=ColInfoTypeEnum.default, column_label="Display Name")
        assert _col_label(col) == "Display Name"

    def test_label_equals_var_when_not_set(self):
        from great_tables._ihtml import _col_label
        from great_tables._gt_data import ColInfo, ColInfoTypeEnum

        col = ColInfo(var="my_col", type=ColInfoTypeEnum.default)
        # ColInfo sets column_label = var when not supplied, so label is the var name
        assert _col_label(col) == "my_col"


class TestParsePx:
    def test_none_returns_default(self):
        from great_tables._ihtml import _parse_px

        assert _parse_px(None) == 16.0

    def test_empty_string_returns_default(self):
        from great_tables._ihtml import _parse_px

        assert _parse_px("") == 16.0

    def test_px_value_parsed(self):
        from great_tables._ihtml import _parse_px

        assert _parse_px("14px") == 14.0

    def test_invalid_value_returns_default(self):
        from great_tables._ihtml import _parse_px

        assert _parse_px("not-a-number") == 16.0

    def test_custom_default(self):
        from great_tables._ihtml import _parse_px

        assert _parse_px(None, default=12.0) == 12.0


class TestIhtmlWarnings:
    def test_summary_rows_warn_in_interactive(self):
        import pandas as pd

        df = pd.DataFrame({"grp": ["A", "A", "B"], "x": [1, 2, 3]})
        gt = (
            GT(df, groupname_col="grp")
            .summary_rows(groups="A", fns={"sum": lambda x: x.sum()})
            .opt_interactive()
        )
        with pytest.warns(UserWarning, match="summary_rows"):
            gt.as_raw_html()

    def test_spanners_warn_in_interactive(self):
        df = pl.DataFrame({"a": [1], "b": [2], "c": [3]})
        gt = GT(df).tab_spanner(label="Group", columns=["a", "b"]).opt_interactive()
        with pytest.warns(UserWarning, match="tab_spanner"):
            gt.as_raw_html()

    def test_column_width_px_used_in_interactive(self):
        df = pl.DataFrame({"a": [1, 2], "b": [3, 4]})
        gt = GT(df).cols_width({"a": "120px"}).opt_interactive()
        html = gt.as_raw_html()
        # The column width should influence the rendered output in some way
        assert "120" in html


# ---------------------------------------------------------------------------
# Numeric column sorting
# ---------------------------------------------------------------------------


class TestNumericSorting:
    """Numeric columns should use numeric sort order, not lexicographic."""

    def test_list_columns_are_not_numeric(self, frame_constructor: DataFrameConstructor):
        df = frame_constructor({"items": [[1, 2], [3], [], None], "num": [1.5, 22.25, 3.0, None]})
        props = _extract_props(GT(df).opt_interactive().as_raw_html())
        col_map = {c["id"]: c for c in props["columns"]}

        assert "type" not in col_map["items"]
        assert props["data"]["items"] == ["[1, 2]", "[3]", "[]", ""]
        assert col_map["num"]["type"] == "numeric"
        assert props["data"]["num"] == [1.5, 22.25, 3.0, None]

    @pytest.mark.parametrize(
        "make_frame, expected",
        [
            pytest.param(
                lambda: pl.DataFrame(
                    {"x": ["point", "line", "point"]}, schema={"x": pl.Enum(["point", "line"])}
                ),
                ["point", "line", "point"],
                id="polars-enum",
            ),
            pytest.param(
                lambda: pd.DataFrame({"x": pd.interval_range(0, 3)}),
                ["(0, 1]", "(1, 2]", "(2, 3]"],
                id="pandas-interval",
            ),
            pytest.param(
                lambda: pa.table({"x": pc.run_end_encode(pa.array(["a", "a", "b"]))}),
                ["a", "a", "b"],
                id="pyarrow-run_end_encoded",
            ),
        ],
    )
    def test_parameterized_dtypes_are_not_numeric(self, make_frame, expected):
        # These dtypes name their parameters, so their values used to go through `float()` (#1045)
        props = _extract_props(GT(make_frame()).opt_interactive().as_raw_html())
        col_map = {c["id"]: c for c in props["columns"]}

        assert "type" not in col_map["x"]
        assert props["data"]["x"] == expected

    def test_numeric_columns_have_type_numeric(self):
        df = pl.DataFrame({"symbol": ["A", "B", "C"], "price": [227.5, 431.2, 118.9]})
        html = GT(df).opt_interactive().as_raw_html()
        props = _extract_props(html)
        col_map = {c["id"]: c for c in props["columns"]}
        assert col_map["price"]["type"] == "numeric"
        assert "type" not in col_map["symbol"]

    def test_numeric_data_contains_numbers(self):
        df = pl.DataFrame({"name": ["X", "Y"], "value": [51230, 302100]})
        html = GT(df).opt_interactive().as_raw_html()
        props = _extract_props(html)
        assert props["data"]["value"] == [51230.0, 302100.0]
        assert props["data"]["name"] == ["X", "Y"]

    def test_numeric_columns_have_cell_display_values(self):
        df = pl.DataFrame({"a": ["x"], "b": [42]})
        html = GT(df).opt_interactive().as_raw_html()
        props = _extract_props(html)
        col_map = {c["id"]: c for c in props["columns"]}
        assert "cell" in col_map["b"]
        assert col_map["b"]["html"] is True
        assert "cell" not in col_map["a"]

    def test_formatted_numeric_uses_display_in_cell(self):
        df = pl.DataFrame({"val": [1234.5]})
        html = GT(df).fmt_number("val", decimals=2).opt_interactive().as_raw_html()
        props = _extract_props(html)
        col_map = {c["id"]: c for c in props["columns"]}
        assert col_map["val"]["cell"] == ["1,234.50"]
        assert props["data"]["val"] == [1234.5]

    def test_missing_numeric_values_are_null(self, frame_constructor: DataFrameConstructor):
        df = frame_constructor({"x": [1.5, None, float("nan")], "n": [1, None, 3]})
        html = GT(df).opt_interactive().as_raw_html()
        props = _extract_props(html)
        assert props["data"] == {"x": [1.5, None, None], "n": [1.0, None, 3.0]}
        assert [c["cell"][1] for c in props["columns"]] == ["", ""]

    def test_integer_column_detected_as_numeric(self):
        df = pl.DataFrame({"n": [10, 20, 30]})
        html = GT(df).opt_interactive().as_raw_html()
        props = _extract_props(html)
        col_map = {c["id"]: c for c in props["columns"]}
        assert col_map["n"]["type"] == "numeric"

    def test_pandas_numeric_columns(self):
        import pandas as pd

        df = pd.DataFrame({"label": ["a", "b"], "amount": [100, 200]})
        html = GT(df).opt_interactive().as_raw_html()
        props = _extract_props(html)
        col_map = {c["id"]: c for c in props["columns"]}
        assert col_map["amount"]["type"] == "numeric"
        assert "type" not in col_map["label"]
