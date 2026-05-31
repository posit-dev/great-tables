"""Comprehensive snapshot tests for summary_rows() and grand_summary_rows().

Tests cover the structural combinations that can affect HTML and LaTeX rendering:
- Row labels (with/without rowname_col)
- Row groups as spanning header vs. as column in stub
- Group summary only, grand summary only, both combined
- Different sides (top, bottom, both)
- Empty groups (groups with no data)
- Multiple summary functions
- Formatted vs. unformatted values
"""

import pandas as pd
import polars as pl
import pytest

from great_tables import GT, vals
from great_tables._utils_render_html import create_body_component_h
from great_tables._utils_render_latex import _render_as_latex, create_body_component_l


# --- Test data fixtures ---


@pytest.fixture
def df_groups_pd():
    """Pandas DataFrame with two groups and numeric data."""
    return pd.DataFrame(
        {
            "group": ["A", "A", "A", "B", "B", "B"],
            "row": ["r1", "r2", "r3", "r4", "r5", "r6"],
            "x": [1, 2, 3, 4, 5, 6],
            "y": [10, 20, 30, 40, 50, 60],
        }
    )


@pytest.fixture
def df_groups_pl():
    """Polars DataFrame with two groups and numeric data."""
    return pl.DataFrame(
        {
            "group": ["A", "A", "A", "B", "B", "B"],
            "row": ["r1", "r2", "r3", "r4", "r5", "r6"],
            "x": [1, 2, 3, 4, 5, 6],
            "y": [10, 20, 30, 40, 50, 60],
        }
    )


@pytest.fixture
def df_three_groups_pd():
    """Pandas DataFrame with three groups (including one with single row)."""
    return pd.DataFrame(
        {
            "group": ["A", "A", "B", "B", "C"],
            "row": ["r1", "r2", "r3", "r4", "r5"],
            "x": [1, 2, 3, 4, 5],
            "y": [10, 20, 30, 40, 50],
        }
    )


# --- Helper functions ---


def render_html_body(gt) -> str:
    built = gt._build_data("html")
    return create_body_component_h(built)


def render_latex_body(gt) -> str:
    built = gt._build_data("latex")
    return create_body_component_l(built)


def render_full_latex(gt) -> str:
    built = gt._build_data("latex")
    return _render_as_latex(data=built)


def pd_sum(df):
    return df.sum(numeric_only=True)


def pd_mean(df):
    return df.mean(numeric_only=True)


def pd_min(df):
    return df.min(numeric_only=True)


def pd_max(df):
    return df.max(numeric_only=True)


# ===========================================================================
# HTML SNAPSHOT TESTS
# ===========================================================================


class TestSummaryRowsHtmlSnap:
    """HTML snapshot tests for group summary rows with different table structures."""

    def test_groups_only_no_stub(self, snapshot, df_groups_pd):
        """Groups spanning (no rowname_col), group summary rows."""
        gt = GT(df_groups_pd, groupname_col="group").summary_rows(fns={"Sum": pd_sum})
        assert snapshot == render_html_body(gt)

    def test_groups_with_rowname(self, snapshot, df_groups_pd):
        """Groups + row labels, group summary rows."""
        gt = GT(df_groups_pd, rowname_col="row", groupname_col="group").summary_rows(
            fns={"Sum": pd_sum, "Mean": pd_mean}
        )
        assert snapshot == render_html_body(gt)

    def test_groups_as_column_no_rowname(self, snapshot, df_groups_pd):
        """Groups as column in stub (no rowname_col), group summary rows."""
        gt = (
            GT(df_groups_pd, groupname_col="group")
            .tab_options(row_group_as_column=True)
            .summary_rows(fns={"Sum": pd_sum})
        )
        assert snapshot == render_html_body(gt)

    def test_groups_as_column_with_rowname(self, snapshot, df_groups_pd):
        """Groups as column + row labels, group summary rows."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .tab_options(row_group_as_column=True)
            .summary_rows(fns={"Sum": pd_sum, "Mean": pd_mean})
        )
        assert snapshot == render_html_body(gt)

    def test_summary_side_top(self, snapshot, df_groups_pd):
        """Group summary rows placed at the top."""
        gt = GT(df_groups_pd, rowname_col="row", groupname_col="group").summary_rows(
            fns={"Sum": pd_sum}, side="top"
        )
        assert snapshot == render_html_body(gt)

    def test_summary_side_both(self, snapshot, df_groups_pd):
        """Group summary rows on both top and bottom (via two calls)."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .summary_rows(fns={"Min": pd_min}, side="top")
            .summary_rows(fns={"Max": pd_max}, side="bottom")
        )
        assert snapshot == render_html_body(gt)

    def test_summary_with_fmt(self, snapshot, df_groups_pd):
        """Group summary rows with formatting applied."""
        gt = GT(df_groups_pd, rowname_col="row", groupname_col="group").summary_rows(
            fns={"Mean": pd_mean}, fmt=vals.fmt_number
        )
        assert snapshot == render_html_body(gt)

    def test_summary_selective_groups(self, snapshot, df_three_groups_pd):
        """Summary rows only for specific groups."""
        gt = GT(df_three_groups_pd, rowname_col="row", groupname_col="group").summary_rows(
            fns={"Sum": pd_sum}, groups=["A", "C"]
        )
        assert snapshot == render_html_body(gt)

    def test_summary_with_missing_text(self, snapshot):
        """Summary rows where some columns produce no numeric result."""
        df = pd.DataFrame(
            {
                "group": ["A", "A", "B", "B"],
                "row": ["r1", "r2", "r3", "r4"],
                "x": [1, 2, 3, 4],
                "label": ["foo", "bar", "baz", "qux"],
            }
        )
        gt = GT(df, rowname_col="row", groupname_col="group").summary_rows(
            fns={"Sum": pd_sum}, missing_text="--"
        )
        assert snapshot == render_html_body(gt)

    def test_summary_three_groups(self, snapshot, df_three_groups_pd):
        """Three groups including one with a single row."""
        gt = GT(df_three_groups_pd, rowname_col="row", groupname_col="group").summary_rows(
            fns={"Sum": pd_sum, "Mean": pd_mean}
        )
        assert snapshot == render_html_body(gt)


class TestGrandSummaryRowsHtmlSnap:
    """HTML snapshot tests for grand summary rows with different table structures."""

    def test_grand_no_groups_no_stub(self, snapshot):
        """Grand summary, no groups, no row stub."""
        df = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
        gt = GT(df).grand_summary_rows(fns={"Sum": pd_sum, "Mean": pd_mean})
        assert snapshot == render_html_body(gt)

    def test_grand_with_rowname(self, snapshot):
        """Grand summary with row labels."""
        df = pd.DataFrame({"row": ["a", "b", "c"], "x": [1, 2, 3], "y": [10, 20, 30]})
        gt = GT(df, rowname_col="row").grand_summary_rows(fns={"Sum": pd_sum})
        assert snapshot == render_html_body(gt)

    def test_grand_with_groups_spanning(self, snapshot, df_groups_pd):
        """Grand summary with groups as spanning rows."""
        gt = GT(df_groups_pd, rowname_col="row", groupname_col="group").grand_summary_rows(
            fns={"Sum": pd_sum}
        )
        assert snapshot == render_html_body(gt)

    def test_grand_with_groups_as_column(self, snapshot, df_groups_pd):
        """Grand summary with groups as column."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .tab_options(row_group_as_column=True)
            .grand_summary_rows(fns={"Sum": pd_sum})
        )
        assert snapshot == render_html_body(gt)

    def test_grand_side_top(self, snapshot, df_groups_pd):
        """Grand summary at top."""
        gt = GT(df_groups_pd, rowname_col="row", groupname_col="group").grand_summary_rows(
            fns={"Sum": pd_sum}, side="top"
        )
        assert snapshot == render_html_body(gt)

    def test_grand_side_both(self, snapshot, df_groups_pd):
        """Grand summary at both top and bottom."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .grand_summary_rows(fns={"Min": pd_min}, side="top")
            .grand_summary_rows(fns={"Max": pd_max}, side="bottom")
        )
        assert snapshot == render_html_body(gt)


class TestCombinedSummaryHtmlSnap:
    """HTML snapshot tests for combined group + grand summary rows."""

    def test_both_summary_and_grand(self, snapshot, df_groups_pd):
        """Both group and grand summary rows."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .summary_rows(fns={"Group Sum": pd_sum})
            .grand_summary_rows(fns={"Grand Sum": pd_sum})
        )
        assert snapshot == render_html_body(gt)

    def test_both_summary_and_grand_groups_as_column(self, snapshot, df_groups_pd):
        """Both group and grand summary, groups as column."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .tab_options(row_group_as_column=True)
            .summary_rows(fns={"Group Sum": pd_sum})
            .grand_summary_rows(fns={"Grand Sum": pd_sum})
        )
        assert snapshot == render_html_body(gt)

    def test_both_summary_top_grand_bottom(self, snapshot, df_groups_pd):
        """Group summary on top, grand summary on bottom."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .summary_rows(fns={"Group Min": pd_min}, side="top")
            .grand_summary_rows(fns={"Grand Max": pd_max}, side="bottom")
        )
        assert snapshot == render_html_body(gt)

    def test_both_summary_bottom_grand_top(self, snapshot, df_groups_pd):
        """Group summary on bottom, grand summary on top."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .summary_rows(fns={"Group Max": pd_max}, side="bottom")
            .grand_summary_rows(fns={"Grand Min": pd_min}, side="top")
        )
        assert snapshot == render_html_body(gt)

    def test_multiple_fns_both_levels(self, snapshot, df_groups_pd):
        """Multiple summary functions at both levels."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .summary_rows(fns={"Min": pd_min, "Max": pd_max, "Mean": pd_mean})
            .grand_summary_rows(fns={"Overall Min": pd_min, "Overall Max": pd_max})
        )
        assert snapshot == render_html_body(gt)

    def test_with_formatting_both_levels(self, snapshot, df_groups_pd):
        """Formatting applied at both group and grand levels."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .summary_rows(fns={"Mean": pd_mean}, fmt=vals.fmt_number)
            .grand_summary_rows(fns={"Grand Mean": pd_mean}, fmt=vals.fmt_number)
        )
        assert snapshot == render_html_body(gt)


class TestSummaryRowsPolarsHtmlSnap:
    """HTML snapshot tests using Polars expressions."""

    def test_polars_basic(self, snapshot, df_groups_pl):
        """Polars expressions for group summary."""
        gt = GT(df_groups_pl, rowname_col="row", groupname_col="group").summary_rows(
            fns={"Sum": pl.col("x", "y").sum(), "Mean": pl.col("x", "y").mean()}
        )
        assert snapshot == render_html_body(gt)

    def test_polars_groups_as_column(self, snapshot, df_groups_pl):
        """Polars with groups as column."""
        gt = (
            GT(df_groups_pl, rowname_col="row", groupname_col="group")
            .tab_options(row_group_as_column=True)
            .summary_rows(fns={"Sum": pl.col("x", "y").sum()}, fmt=vals.fmt_integer)
        )
        assert snapshot == render_html_body(gt)

    def test_polars_combined(self, snapshot, df_groups_pl):
        """Polars with both group and grand summary."""
        gt = (
            GT(df_groups_pl, rowname_col="row", groupname_col="group")
            .summary_rows(fns={"Group Sum": pl.col("x", "y").sum()}, fmt=vals.fmt_integer)
            .grand_summary_rows(fns={"Grand Sum": pl.col("x", "y").sum()}, fmt=vals.fmt_integer)
        )
        assert snapshot == render_html_body(gt)


# ===========================================================================
# LATEX SNAPSHOT TESTS
# ===========================================================================


class TestSummaryRowsLatexSnap:
    """LaTeX snapshot tests for group summary rows with different table structures."""

    def test_groups_only_no_stub(self, snapshot, df_groups_pd):
        """Groups spanning (no rowname_col), group summary rows."""
        gt = GT(df_groups_pd, groupname_col="group").summary_rows(fns={"Sum": pd_sum})
        assert snapshot == render_latex_body(gt)

    def test_groups_with_rowname(self, snapshot, df_groups_pd):
        """Groups + row labels, group summary rows."""
        gt = GT(df_groups_pd, rowname_col="row", groupname_col="group").summary_rows(
            fns={"Sum": pd_sum, "Mean": pd_mean}
        )
        assert snapshot == render_latex_body(gt)

    def test_groups_as_column_no_rowname(self, snapshot, df_groups_pd):
        """Groups as column in stub (no rowname_col), group summary rows."""
        gt = (
            GT(df_groups_pd, groupname_col="group")
            .tab_options(row_group_as_column=True)
            .summary_rows(fns={"Sum": pd_sum})
        )
        assert snapshot == render_latex_body(gt)

    def test_groups_as_column_with_rowname(self, snapshot, df_groups_pd):
        """Groups as column + row labels, group summary rows."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .tab_options(row_group_as_column=True)
            .summary_rows(fns={"Sum": pd_sum, "Mean": pd_mean})
        )
        assert snapshot == render_latex_body(gt)

    def test_summary_side_top(self, snapshot, df_groups_pd):
        """Group summary rows placed at the top."""
        gt = GT(df_groups_pd, rowname_col="row", groupname_col="group").summary_rows(
            fns={"Sum": pd_sum}, side="top"
        )
        assert snapshot == render_latex_body(gt)

    def test_summary_side_both(self, snapshot, df_groups_pd):
        """Group summary rows on both sides."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .summary_rows(fns={"Min": pd_min}, side="top")
            .summary_rows(fns={"Max": pd_max}, side="bottom")
        )
        assert snapshot == render_latex_body(gt)

    def test_summary_with_fmt(self, snapshot, df_groups_pd):
        """Group summary rows with formatting."""
        gt = GT(df_groups_pd, rowname_col="row", groupname_col="group").summary_rows(
            fns={"Mean": pd_mean}, fmt=vals.fmt_number
        )
        assert snapshot == render_latex_body(gt)

    def test_summary_selective_groups(self, snapshot, df_three_groups_pd):
        """Summary only for selected groups."""
        gt = GT(df_three_groups_pd, rowname_col="row", groupname_col="group").summary_rows(
            fns={"Sum": pd_sum}, groups=["A", "C"]
        )
        assert snapshot == render_latex_body(gt)

    def test_summary_three_groups(self, snapshot, df_three_groups_pd):
        """Three groups including one with a single row."""
        gt = GT(df_three_groups_pd, rowname_col="row", groupname_col="group").summary_rows(
            fns={"Sum": pd_sum, "Mean": pd_mean}
        )
        assert snapshot == render_latex_body(gt)


class TestGrandSummaryRowsLatexSnap:
    """LaTeX snapshot tests for grand summary rows."""

    def test_grand_no_groups_no_stub(self, snapshot):
        """Grand summary, no groups, no row stub."""
        df = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
        gt = GT(df).grand_summary_rows(fns={"Sum": pd_sum, "Mean": pd_mean})
        assert snapshot == render_latex_body(gt)

    def test_grand_with_rowname(self, snapshot):
        """Grand summary with row labels."""
        df = pd.DataFrame({"row": ["a", "b", "c"], "x": [1, 2, 3], "y": [10, 20, 30]})
        gt = GT(df, rowname_col="row").grand_summary_rows(fns={"Sum": pd_sum})
        assert snapshot == render_latex_body(gt)

    def test_grand_with_groups_spanning(self, snapshot, df_groups_pd):
        """Grand summary with groups as spanning rows."""
        gt = GT(df_groups_pd, rowname_col="row", groupname_col="group").grand_summary_rows(
            fns={"Sum": pd_sum}
        )
        assert snapshot == render_latex_body(gt)

    def test_grand_with_groups_as_column(self, snapshot, df_groups_pd):
        """Grand summary with groups as column."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .tab_options(row_group_as_column=True)
            .grand_summary_rows(fns={"Sum": pd_sum})
        )
        assert snapshot == render_latex_body(gt)

    def test_grand_side_top(self, snapshot, df_groups_pd):
        """Grand summary at top."""
        gt = GT(df_groups_pd, rowname_col="row", groupname_col="group").grand_summary_rows(
            fns={"Sum": pd_sum}, side="top"
        )
        assert snapshot == render_latex_body(gt)

    def test_grand_side_both(self, snapshot, df_groups_pd):
        """Grand summary at both top and bottom."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .grand_summary_rows(fns={"Min": pd_min}, side="top")
            .grand_summary_rows(fns={"Max": pd_max}, side="bottom")
        )
        assert snapshot == render_latex_body(gt)


class TestCombinedSummaryLatexSnap:
    """LaTeX snapshot tests for combined group + grand summary rows."""

    def test_both_summary_and_grand(self, snapshot, df_groups_pd):
        """Both group and grand summary rows."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .summary_rows(fns={"Group Sum": pd_sum})
            .grand_summary_rows(fns={"Grand Sum": pd_sum})
        )
        assert snapshot == render_latex_body(gt)

    def test_both_summary_and_grand_groups_as_column(self, snapshot, df_groups_pd):
        """Both group and grand summary, groups as column."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .tab_options(row_group_as_column=True)
            .summary_rows(fns={"Group Sum": pd_sum})
            .grand_summary_rows(fns={"Grand Sum": pd_sum})
        )
        assert snapshot == render_latex_body(gt)

    def test_both_summary_top_grand_bottom(self, snapshot, df_groups_pd):
        """Group summary on top, grand summary on bottom."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .summary_rows(fns={"Group Min": pd_min}, side="top")
            .grand_summary_rows(fns={"Grand Max": pd_max}, side="bottom")
        )
        assert snapshot == render_latex_body(gt)

    def test_multiple_fns_both_levels(self, snapshot, df_groups_pd):
        """Multiple summary functions at both levels."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .summary_rows(fns={"Min": pd_min, "Max": pd_max, "Mean": pd_mean})
            .grand_summary_rows(fns={"Overall Min": pd_min, "Overall Max": pd_max})
        )
        assert snapshot == render_latex_body(gt)

    def test_with_formatting_both_levels(self, snapshot, df_groups_pd):
        """Formatting at both levels."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .summary_rows(fns={"Mean": pd_mean}, fmt=vals.fmt_number)
            .grand_summary_rows(fns={"Grand Mean": pd_mean}, fmt=vals.fmt_number)
        )
        assert snapshot == render_latex_body(gt)


class TestFullLatexRender:
    """Full LaTeX output (not just body) for end-to-end validation."""

    def test_full_latex_summary_rows(self, snapshot, df_groups_pd):
        """Full LaTeX rendering with summary rows."""
        gt = GT(df_groups_pd, rowname_col="row", groupname_col="group").summary_rows(
            fns={"Sum": pd_sum, "Mean": pd_mean}, fmt=vals.fmt_number
        )
        assert snapshot == render_full_latex(gt)

    def test_full_latex_grand_summary_rows(self, snapshot, df_groups_pd):
        """Full LaTeX rendering with grand summary rows."""
        gt = GT(df_groups_pd, rowname_col="row", groupname_col="group").grand_summary_rows(
            fns={"Sum": pd_sum}, fmt=vals.fmt_integer
        )
        assert snapshot == render_full_latex(gt)

    def test_full_latex_both_summaries(self, snapshot, df_groups_pd):
        """Full LaTeX rendering with both group and grand summary."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .summary_rows(fns={"Group Sum": pd_sum}, fmt=vals.fmt_integer)
            .grand_summary_rows(fns={"Grand Sum": pd_sum}, fmt=vals.fmt_integer)
        )
        assert snapshot == render_full_latex(gt)

    def test_full_latex_groups_as_column_both(self, snapshot, df_groups_pd):
        """Full LaTeX with groups-as-column and both summary types."""
        gt = (
            GT(df_groups_pd, rowname_col="row", groupname_col="group")
            .tab_options(row_group_as_column=True)
            .summary_rows(fns={"Group Sum": pd_sum}, fmt=vals.fmt_integer)
            .grand_summary_rows(fns={"Grand Sum": pd_sum}, fmt=vals.fmt_integer)
        )
        assert snapshot == render_full_latex(gt)
