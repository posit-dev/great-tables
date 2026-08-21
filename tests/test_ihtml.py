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
    def test_static_html_no_datatable(self, gt_mini: GT):
        html = gt_mini.as_raw_html()
        assert "gt_table" in html
        assert "DataTable" not in html

    def test_active_false_static(self, gt_mini: GT):
        html = gt_mini.opt_interactive(active=False).as_raw_html()
        assert "gt_table" in html
        assert "DataTable" not in html


# ---------------------------------------------------------------------------
# Interactive rendering produces valid output
# ---------------------------------------------------------------------------


class TestRenderAsIhtml:
    def test_returns_string(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        assert isinstance(html, str)
        assert len(html) > 1000

    def test_contains_datatable_init(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        assert "DataTable(" in html

    def test_contains_vendored_js(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        # DataTables minified JS exports the DataTable symbol
        assert "DataTable" in html

    def test_mount_id_present(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        assert "gt-ihtml-" in html

    def test_unique_ids_across_tables(self):
        df = pl.from_pandas(exibble[["num"]].head(3))
        html_a = GT(df).opt_interactive().as_raw_html()
        html_b = GT(df).opt_interactive().as_raw_html()
        # Extract mount IDs
        ids_a = re.findall(r'id="(gt-ihtml-[^"]+)"', html_a)
        ids_b = re.findall(r'id="(gt-ihtml-[^"]+)"', html_b)
        assert ids_a and ids_b
        assert ids_a[0] != ids_b[0]

    def test_all_columns_in_config(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        # num, char, currency should all appear as column data keys
        for col in ["num", "char", "currency"]:
            assert f'"data": "{col}"' in html or f'"data":"{col}"' in html

    def test_row_data_in_output(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        # The data array must be present in the config JSON
        assert '"data":' in html or '"data": ' in html


# ---------------------------------------------------------------------------
# Feature flags map to DataTables config
# ---------------------------------------------------------------------------


class TestFeatureFlags:
    def _extract_config(self, html: str) -> dict:
        """Extract the DataTables config dict from the rendered HTML."""
        # The config JSON is assigned as: var cfg = {...};
        m = re.search(r"var cfg = (\{.*?\});", html, re.DOTALL)
        assert m, "Could not find DataTables config JSON in HTML"
        return json.loads(m.group(1))

    def test_search_disabled_by_default(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive().as_raw_html())
        assert cfg["searching"] is False

    def test_search_enabled(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive(use_search=True).as_raw_html())
        assert cfg["searching"] is True

    def test_sorting_enabled_by_default(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive().as_raw_html())
        assert cfg["ordering"] is True

    def test_sorting_disabled(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive(use_sorting=False).as_raw_html())
        assert cfg["ordering"] is False

    def test_pagination_enabled_by_default(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive().as_raw_html())
        assert cfg["paging"] is True

    def test_pagination_disabled(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive(use_pagination=False).as_raw_html())
        assert cfg["paging"] is False

    def test_page_info_enabled_by_default(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive().as_raw_html())
        assert cfg["info"] is True

    def test_page_size_default(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive(page_size_default=25).as_raw_html())
        assert cfg["pageLength"] == 25

    def test_page_size_values(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive(page_size_values=[5, 10]).as_raw_html())
        assert cfg["lengthMenu"] == [5, 10]

    def test_pagination_type_numbers(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive(pagination_type="numbers").as_raw_html())
        assert cfg["pagingType"] == "numbers"

    def test_pagination_type_simple(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive(pagination_type="simple").as_raw_html())
        assert cfg["pagingType"] == "simple"

    def test_scroll_y_empty_when_auto_height(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive(height="auto").as_raw_html())
        assert cfg["scrollY"] == ""

    def test_scroll_y_set_when_height_given(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive(height="400px").as_raw_html())
        assert cfg["scrollY"] == "400px"

    def test_filter_init_complete_present(self, gt_mini: GT):
        html = gt_mini.opt_interactive(use_filters=True).as_raw_html()
        assert "initComplete" in html

    def test_filter_init_complete_absent_by_default(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        assert "initComplete" not in html


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

    def test_cell_styles_var_present(self, gt_styled: GT):
        html = gt_styled.as_raw_html()
        assert "_cellStyles" in html

    def test_col_idx_var_present(self, gt_styled: GT):
        html = gt_styled.as_raw_html()
        assert "_colIdx" in html

    def test_created_row_callback_present(self, gt_styled: GT):
        html = gt_styled.as_raw_html()
        assert "createdRow" in html

    def test_body_fill_css_in_cell_styles(self, gt_styled: GT):
        html = gt_styled.as_raw_html()
        m = re.search(r"var _cellStyles = (\{.*?\});", html, re.DOTALL)
        assert m, "_cellStyles not found"
        cell_styles = json.loads(m.group(1))
        # row index 1 is where a==2
        assert "1" in cell_styles
        assert "a" in cell_styles["1"]
        assert "yellow" in cell_styles["1"]["a"]

    def test_body_text_css_in_cell_styles(self, gt_styled: GT):
        html = gt_styled.as_raw_html()
        m = re.search(r"var _cellStyles = (\{.*?\});", html, re.DOTALL)
        assert m, "_cellStyles not found"
        cell_styles = json.loads(m.group(1))
        # row index 2 is where b==30
        assert "2" in cell_styles
        assert "b" in cell_styles["2"]
        css = cell_styles["2"]["b"]
        assert "red" in css
        assert "bold" in css

    def test_col_idx_maps_column_names(self, gt_styled: GT):
        html = gt_styled.as_raw_html()
        m = re.search(r"var _colIdx = (\{.*?\});", html, re.DOTALL)
        assert m, "_colIdx not found"
        col_idx = json.loads(m.group(1))
        assert col_idx["a"] == 0
        assert col_idx["b"] == 1

    def test_col_label_style_on_th(self, gt_styled: GT):
        html = gt_styled.as_raw_html()
        # The <th> for column "b" should carry an inline style
        assert 'style="' in html
        assert "#abc" in html

    def test_no_cell_styles_var_when_no_tab_style(self):
        df = pl.DataFrame({"x": [1, 2]})
        html = GT(df).opt_interactive().as_raw_html()
        assert "_cellStyles" not in html

    def test_unsupported_location_does_not_crash(self):
        df = pl.DataFrame({"x": [1, 2]})
        # loc.header() is unsupported in interactive mode — should render without error
        html = (
            GT(df)
            .tab_header(title="T")
            .tab_style(style=style.fill(color="blue"), locations=loc.header())
            .opt_interactive()
            .as_raw_html()
        )
        assert "DataTable(" in html


# ---------------------------------------------------------------------------
# Column width pre-sizing
# ---------------------------------------------------------------------------


class TestColumnWidths:
    def _extract_config(self, html: str) -> dict:
        m = re.search(r"var cfg = (\{.*?\});", html, re.DOTALL)
        assert m, "Could not find DataTables config JSON in HTML"
        return json.loads(m.group(1))

    def test_auto_width_false(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive().as_raw_html())
        assert cfg["autoWidth"] is False

    def test_every_column_has_width(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive().as_raw_html())
        for col_def in cfg["columns"]:
            assert "width" in col_def, f"column {col_def.get('data')} missing 'width'"

    def test_width_is_px_string(self, gt_mini: GT):
        cfg = self._extract_config(gt_mini.opt_interactive().as_raw_html())
        for col_def in cfg["columns"]:
            assert col_def["width"].endswith("px")


# ---------------------------------------------------------------------------
# Row striping
# ---------------------------------------------------------------------------


class TestRowStriping:
    def test_stripe_not_in_class_name_by_default(self, gt_mini: GT):
        html = gt_mini.opt_interactive().as_raw_html()
        m = re.search(r"var cfg = (\{.*?\});", html, re.DOTALL)
        assert m
        cfg = json.loads(m.group(1))
        assert "stripe" not in cfg.get("className", "")

    def test_stripe_css_absent_by_default(self, gt_mini: GT):
        # Our scoped rule uses "nth-child(odd) > td" with !important.
        # The vendored DataTables CSS also uses nth-child(odd) but never "> td".
        html = gt_mini.opt_interactive().as_raw_html()
        assert "nth-child(odd) > td" not in html

    def test_stripe_css_present_when_option_enabled(self, gt_mini: GT):
        html = (
            gt_mini.tab_options(row_striping_include_table_body=True)
            .opt_interactive()
            .as_raw_html()
        )
        assert "nth-child(odd) > td" in html
