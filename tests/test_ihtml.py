"""Tests for the interactive HTML table rendering path."""

from __future__ import annotations

import json
import re

import pytest
import polars as pl

from great_tables import GT, style, loc
from great_tables.data import exibble


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
