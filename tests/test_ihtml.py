"""Tests for the interactive HTML table rendering path."""

from __future__ import annotations

import json
import re

import pytest
import polars as pl

from great_tables import GT
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
