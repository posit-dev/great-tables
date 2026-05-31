import math

import pandas as pd
import polars as pl
import pytest
from great_tables import GT
from great_tables._cols_merge import ColMergeInfo, merge_pattern


@pytest.fixture
def simple_df():
    return pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})


@pytest.fixture
def missing_df():
    return pd.DataFrame(
        {
            "number": ["Three", "Four", "Five"],
            "val1": [10, 20, 30],
            "val2": [15.0, 25.0, None],
            "val3": [5.0, None, None],
        }
    )


class TestReplaceNa:
    """Tests for the ColMergeInfo.replace_na() static method."""

    def test_replace_na_with_none(self):
        """Test that None values are replaced with None."""
        result = ColMergeInfo.replace_na("hello", None, "world")
        assert result == ("hello", None, "world")

    def test_replace_na_with_nan(self):
        """Test that NaN values are replaced with None."""
        result = ColMergeInfo.replace_na("hello", math.nan, "world")
        assert result == ("hello", None, "world")

    def test_replace_na_with_float_nan(self):
        """Test that float('nan') values are replaced with None."""
        result = ColMergeInfo.replace_na(10, float("nan"), 30)
        assert result[0] == 10
        assert result[1] is None
        assert result[2] == 30

    def test_replace_na_preserves_non_missing(self):
        """Test that non-missing values are preserved."""
        result = ColMergeInfo.replace_na("a", "b", "c", 1, 2, 3)
        assert result == ("a", "b", "c", 1, 2, 3)

    def test_replace_na_empty(self):
        """Test replace_na with no arguments."""
        result = ColMergeInfo.replace_na()
        assert result == ()

    def test_replace_na_single_value(self):
        """Test replace_na with single value."""
        assert ColMergeInfo.replace_na(42) == (42,)
        assert ColMergeInfo.replace_na(None) == (None,)
        assert ColMergeInfo.replace_na(math.nan) == (None,)

    def test_replace_na_all_missing(self):
        """Test replace_na when all values are missing."""
        result = ColMergeInfo.replace_na(None, math.nan, float("nan"))
        assert result == (None, None, None)


class TestMergePattern:
    """Tests for the merge_pattern() convenience function."""

    def test_simple_merge(self):
        """Test basic merge pattern."""
        result = merge_pattern("{0} {1}", "John", "Doe")
        assert result == "John Doe"

    def test_merge_with_separator(self):
        """Test merge pattern with em dash separator."""
        result = merge_pattern("{0}—{1}", 10, 20)
        assert result == "10—20"

    def test_merge_with_none_value(self):
        """Test merge pattern with None value in conditional section."""
        result = merge_pattern("{0}<< ({1})>>", "John", None)
        assert result == "John"

    def test_merge_with_all_present(self):
        """Test merge pattern with all values present."""
        result = merge_pattern("{0}<< ({1})>>", "John", "123-456")
        assert result == "John (123-456)"

    def test_nested_conditionals(self):
        """Test merge pattern with nested conditional sections."""
        result = merge_pattern("{0}<< to {1}<< to {2}>>>>", 10, 20, None)
        assert result == "10 to 20"

        result2 = merge_pattern("{0}<< to {1}<< to {2}>>>>", 10, None, None)
        assert result2 == "10"

        result3 = merge_pattern("{0}<< to {1}<< to {2}>>>>", 10, 20, 30)
        assert result3 == "10 to 20 to 30"

    def test_merge_three_columns(self):
        """Test merge pattern with three values."""
        result = merge_pattern("{0} {1} {2}", "A", "B", "C")
        assert result == "A B C"


class TestColMergeInfoUnit:
    """Unit tests for ColMergeInfo that don't require full table rendering."""

    def test_creation(self):
        """Test basic ColMergeInfo creation."""
        info = ColMergeInfo(vars=["a", "b"], rows=[0, 1, 2], type="merge", pattern="{0} {1}")

        assert info.vars == ["a", "b"]
        assert info.rows == [0, 1, 2]
        assert info.type == "merge"
        assert info.pattern == "{0} {1}"

    def test_pattern_columns_extraction(self):
        """Test pattern_columns property extracts column references correctly."""
        info = ColMergeInfo(vars=["a", "b", "c"], rows=[0], type="merge", pattern="{0}—{1}—{2}")
        assert info.pattern_columns == ["0", "1", "2"]

        # Test with duplicate references
        info2 = ColMergeInfo(vars=["a", "b"], rows=[0], type="merge", pattern="{0} {1} {0}")
        assert info2.pattern_columns == ["0", "1"]

    def test_validate_pattern_success(self):
        """Test validate_pattern with valid patterns."""
        info = ColMergeInfo(vars=["a", "b"], rows=[0], type="merge", pattern="{0} {1}")
        # Should not raise
        info.validate_pattern()

        # Test with subset of columns referenced
        info2 = ColMergeInfo(vars=["a", "b", "c"], rows=[0], type="merge", pattern="{0} {2}")
        info2.validate_pattern()

    def test_validate_pattern_zero_index_valid(self):
        """Test validate_pattern accepts 0-based indexing."""
        info = ColMergeInfo(vars=["a", "b"], rows=[0], type="merge", pattern="{0}-{1}")
        # Should not raise with 0-based indexing
        info.validate_pattern()

    def test_validate_pattern_out_of_range_raises(self):
        """Test validate_pattern raises when pattern references non-existent column."""
        info = ColMergeInfo(vars=["a", "b"], rows=[0], type="merge", pattern="{0} {1} {2}")
        with pytest.raises(ValueError, match="Pattern references column"):
            info.validate_pattern()

    # Tests for the merge() method
    def test_merge_simple(self):
        """Test merge() with simple patterns."""
        info = ColMergeInfo(vars=["a", "b"], rows=[0], type="merge", pattern="{0} {1}")
        result = info.merge("Hello", "World")
        assert result == "Hello World"

    def test_merge_with_separator(self):
        """Test merge() with different separators."""
        info = ColMergeInfo(vars=["a", "b"], rows=[0], type="merge", pattern="{0}—{1}")
        result = info.merge(10, 20)
        assert result == "10—20"

    def test_merge_conditional_missing(self):
        """Test merge() with conditional sections and missing values."""
        info = ColMergeInfo(vars=["a", "b"], rows=[0], type="merge", pattern="{0}<< ({1})>>")

        # Non-missing: include the conditional section
        result1 = info.merge(10, 20)
        assert result1 == "10 (20)"

        # Missing value (None): remove the conditional section
        result2 = info.merge(10, None)
        assert result2 == "10"

    def test_merge_nested_conditionals(self):
        """Test merge() with nested conditional sections."""
        info = ColMergeInfo(
            vars=["a", "b", "c"], rows=[0], type="merge", pattern="{0}<< ({1}-<<{2}>>)>>"
        )

        # All present
        result1 = info.merge(10, 15, 5)
        assert result1 == "10 (15-5)"

        # Third missing
        result2 = info.merge(10, 15, None)
        assert result2 == "10 (15-)"

        # Second missing (and third)
        result3 = info.merge(10, None, None)
        assert result3 == "10"

    def test_merge_three_values(self):
        """Test merge() with three values."""
        info = ColMergeInfo(vars=["a", "b", "c"], rows=[0], type="merge", pattern="{0} {1} {2}")
        result = info.merge("A", "B", "C")
        assert result == "A B C"

    def test_merge_column_subset_in_pattern(self):
        """Test merge() when pattern only uses a subset of columns."""
        info = ColMergeInfo(vars=["a", "b", "c"], rows=[0], type="merge", pattern="{0} {2}")
        result = info.merge("First", "Second", "Third")
        assert result == "First Third"


# =============================================================================
# Integration Tests (require GT rendering)
# =============================================================================


class TestColsMergeIntegration:
    """Integration tests that verify cols_merge works correctly with full GT rendering."""

    def test_basic(self, simple_df: pd.DataFrame):
        gt = GT(simple_df).cols_merge(columns=["a", "b"])

        # Check that merge was registered
        assert len(gt._col_merge) == 1
        assert gt._col_merge[0].vars == ["a", "b"]
        assert gt._col_merge[0].pattern == "{0} {1}"
        assert gt._col_merge[0].type == "merge"

        # Check rendered output
        html = gt.as_raw_html()
        assert "1 4" in html
        assert "2 5" in html
        assert "3 6" in html

    def test_custom_pattern(self, simple_df: pd.DataFrame):
        gt = GT(simple_df).cols_merge(columns=["a", "b"], pattern="{0}—{1}")

        assert gt._col_merge[0].pattern == "{0}—{1}"

        # Check rendered output with em dash
        html = gt.as_raw_html()
        assert "1—4" in html
        assert "2—5" in html
        assert "3—6" in html

    def test_three_columns(self, simple_df: pd.DataFrame):
        gt = GT(simple_df).cols_merge(columns=["a", "b", "c"])

        assert gt._col_merge[0].vars == ["a", "b", "c"]
        assert gt._col_merge[0].pattern == "{0} {1} {2}"

        # Check rendered output with three columns
        html = gt.as_raw_html()
        assert "1 4 7" in html
        assert "2 5 8" in html
        assert "3 6 9" in html

    def test_subset_of_columns(self, simple_df: pd.DataFrame):
        # Provide three columns but only use first two in the pattern
        gt1 = GT(simple_df).cols_merge(columns=["a", "b", "c"], pattern="{0} {1}")

        html1 = gt1.as_raw_html()
        assert "1 4" in html1
        assert "2 5" in html1
        assert "3 6" in html1

        # Provide three columns but only use first and third in the pattern
        gt2 = GT(simple_df).cols_merge(columns=["a", "b", "c"], pattern="{0} {2}")

        html2 = gt2.as_raw_html()
        assert "1 7" in html2
        assert "2 8" in html2
        assert "3 9" in html2

        # Provide three columns but only use the third in the pattern
        gt3 = GT(simple_df).cols_merge(columns=["a", "b", "c"], pattern="Value: {2}")

        html3 = gt3.as_raw_html()
        assert "Value: 7" in html3
        assert "Value: 8" in html3
        assert "Value: 9" in html3

    def test_hiding_default(self, simple_df: pd.DataFrame):
        gt = GT(simple_df).cols_merge(columns=["a", "b", "c"])

        built = gt._build_data(context="html")

        # Check visibility in boxhead
        col_a = [col for col in built._boxhead if col.var == "a"][0]
        col_b = [col for col in built._boxhead if col.var == "b"][0]
        col_c = [col for col in built._boxhead if col.var == "c"][0]

        assert col_a.visible
        assert not col_b.visible
        assert not col_c.visible

    def test_hiding_false(self, simple_df: pd.DataFrame):
        gt = GT(simple_df).cols_merge(columns=["a", "b"], hide_columns=False)

        built = gt._build_data(context="html")

        col_a = [col for col in built._boxhead if col.var == "a"][0]
        col_b = [col for col in built._boxhead if col.var == "b"][0]

        assert col_a.visible
        assert col_b.visible

    def test_specific_rows(self, simple_df: pd.DataFrame):
        gt = GT(simple_df).cols_merge(columns=["a", "b"], rows=[0, 2], pattern="{0}-{1}")

        assert gt._col_merge[0].rows == [0, 2]

        html = gt.as_raw_html()

        # Check that only rows 0 and 2 are merged
        assert "1-4" in html  # Row 0
        assert "2-5" not in html  # Row 1 (not merged)
        assert "3-6" in html  # Row 2

    def test_multiple_operations(self, simple_df: pd.DataFrame):
        gt = (
            GT(simple_df)
            .cols_merge(columns=["a", "b"], pattern="{0}+{1}")
            .cols_merge(columns=["a", "c"], pattern="{0}*{1}")
        )

        assert len(gt._col_merge) == 2
        assert gt._col_merge[0].pattern == "{0}+{1}"
        assert gt._col_merge[1].pattern == "{0}*{1}"

        html = gt.as_raw_html()

        # Check that the second merge uses the result of the first merge
        assert "1+4*7" in html
        assert "2+5*8" in html
        assert "3+6*9" in html

    def test_with_missing_values(self, missing_df: pd.DataFrame):
        gt = GT(missing_df).cols_merge(columns=["val1", "val2"], pattern="{0}<< ({1})>>")

        html = gt.as_raw_html()
        assert "10 (15.0)" in html or "10.0 (15.0)" in html
        assert "20 (25.0)" in html or "20.0 (25.0)" in html
        assert "30<" in html or "30.0<" in html  # The '<' is part of the closing tag (missing val2)

    def test_nested_conditionals(self, missing_df: pd.DataFrame):
        gt = GT(missing_df).cols_merge(
            columns=["val1", "val2", "val3"], pattern="{0}<< ({1}-<<{2}>>)>>"
        )

        html = gt.as_raw_html()

        assert "10 (15.0-5.0)" in html or "10.0 (15.0-5.0)" in html
        assert "20 (25.0-)" in html or "20.0 (25.0-)" in html
        assert "30<" in html or "30.0<" in html

    def test_minimum_columns_error(self, simple_df: pd.DataFrame):
        with pytest.raises(ValueError, match="At least two columns"):
            GT(simple_df).cols_merge(columns=["a"])

    def test_invalid_pattern_reference(self, simple_df: pd.DataFrame):
        gt = GT(simple_df).cols_merge(columns=["a", "b"], pattern="{0} {1} {2}")

        with pytest.raises(ValueError, match="Pattern references column"):
            gt._repr_html_()

    def test_zero_based_indexing(self, simple_df: pd.DataFrame):
        """Test that 0-based indexing works correctly in patterns."""
        gt = GT(simple_df).cols_merge(columns=["a", "b"], pattern="{0}-{1}")

        html = gt.as_raw_html()
        assert "1-4" in html
        assert "2-5" in html
        assert "3-6" in html

    def test_preserves_formatting(self, simple_df: pd.DataFrame):
        gt = (
            GT(simple_df)
            .fmt_number(columns="a", decimals=3)
            .cols_merge(columns=["a", "b"], pattern="{0}+{1}")
        )

        html = gt.as_raw_html()

        assert "1.000+4" in html
        assert "2.000+5" in html
        assert "3.000+6" in html

    def test_with_sub_missing(self, missing_df: pd.DataFrame):
        """Test that sub_missing() replacements are NOT treated as missing.

        In R's gt, sub_missing() replacements mean the value is no longer considered
        NA for cols_merge() purposes. The "--" replacement should appear in the
        merged output, not cause the conditional section to be omitted.
        """
        # calling sub_missing() before cols_merge()
        gt_1 = (
            GT(missing_df)
            .sub_missing(columns=["val2", "val3"], missing_text="--")
            .cols_merge(columns=["val1", "val2", "val3"], pattern="{0}<< to {1}<< to {2}>>>>")
        )

        # calling sub_missing() after cols_merge()
        gt_2 = (
            GT(missing_df)
            .cols_merge(columns=["val1", "val2", "val3"], pattern="{0}<< to {1}<< to {2}>>>>")
            .sub_missing(columns=["val2", "val3"], missing_text="--")
        )

        # From both approaches, we should get the same output
        html_1 = gt_1.as_raw_html()
        html_2 = gt_2.as_raw_html()

        # Row 0: All values are present (none are missing values)
        assert "10 to 15.0 to 5.0" in html_1
        assert "10 to 15.0 to 5.0" in html_2

        # Row 1: val3 was None, but sub_missing() replaced it with "--" so that "--"
        # should be included (it's treated as a non-missing value because of sub_missing())
        assert "20 to 25.0 to --" in html_1
        assert "20 to 25.0 to --" in html_2

        # Row 2: val2 and val3 were None, both replaced with "--" by sub_missing() so both of
        # the "--" values should be included in the output
        assert "30 to -- to --" in html_1
        assert "30 to -- to --" in html_2

    def test_with_formatted_values(self):
        df = pl.DataFrame({"a": [1, 2, None], "b": [10, None, 30], "c": [100, 200, 300]})

        gt = (
            GT(df)
            .cols_merge(columns=["a", "b"], pattern="{0}<< ({1})>>")
            .fmt_integer(columns=["a", "b", "c"])
        )

        html = gt.as_raw_html()

        assert "1 (10)" in html or "1(10)" in html
        assert "2<" in html  # The < is from the closing tag, not from the pattern


# =============================================================================
# Tests for cols_merge_uncert
# =============================================================================


class TestColsMergeUncert:
    """Tests for the cols_merge_uncert() method."""

    def test_basic_symmetric(self):
        """Test basic symmetric uncertainty merge."""
        df = pd.DataFrame({"val": [10.0, 20.0, 30.0], "uncert": [0.5, 1.0, 1.5]})

        gt = GT(df).cols_merge_uncert(col_val="val", col_uncert="uncert")

        assert len(gt._col_merge) == 1
        assert gt._col_merge[0].type == "merge_uncert"
        assert gt._col_merge[0].vars == ["val", "uncert"]

        html = gt.as_raw_html()
        # Should contain the ± symbol
        assert "10.0 \u00b1 0.5" in html
        assert "20.0 \u00b1 1.0" in html
        assert "30.0 \u00b1 1.5" in html

    def test_na_in_val(self):
        """Test that NA in col_val produces empty merged value."""
        df = pl.DataFrame({"val": [10.0, None, 30.0], "uncert": [0.5, 1.0, 1.5]})

        gt = GT(df).cols_merge_uncert(col_val="val", col_uncert="uncert")
        html = gt.as_raw_html()

        # First and third rows should have merged values
        assert "10.0 \u00b1 0.5" in html
        assert "30.0 \u00b1 1.5" in html

    def test_na_in_uncert(self):
        """Test that NA in col_uncert shows only the base value."""
        df = pl.DataFrame({"val": [10.0, 20.0, 30.0], "uncert": [0.5, None, 1.5]})

        gt = GT(df).cols_merge_uncert(col_val="val", col_uncert="uncert")
        html = gt.as_raw_html()

        # Second row: only base value (no ± symbol)
        assert "10.0 \u00b1 0.5" in html
        assert "30.0 \u00b1 1.5" in html
        # 20.0 should appear without ± symbol
        assert "20.0 \u00b1" not in html.replace("10.0 \u00b1 0.5", "").replace(
            "30.0 \u00b1 1.5", ""
        )

    def test_custom_sep(self):
        """Test custom separator."""
        df = pd.DataFrame({"val": [10.0, 20.0], "uncert": [0.5, 1.0]})

        gt = GT(df).cols_merge_uncert(col_val="val", col_uncert="uncert", sep=" ~ ")
        html = gt.as_raw_html()

        assert "10.0 ~ 0.5" in html
        assert "20.0 ~ 1.0" in html

    def test_autohide_true(self):
        """Test that col_uncert is hidden by default."""
        df = pd.DataFrame({"val": [10.0], "uncert": [0.5]})

        gt = GT(df).cols_merge_uncert(col_val="val", col_uncert="uncert")
        html = gt.as_raw_html()

        # "uncert" column header should not appear
        assert ">uncert<" not in html

    def test_autohide_false(self):
        """Test that col_uncert remains visible when autohide=False."""
        df = pd.DataFrame({"val": [10.0], "uncert": [0.5]})

        gt = GT(df).cols_merge_uncert(col_val="val", col_uncert="uncert", autohide=False)
        html = gt.as_raw_html()

        # "uncert" column header should appear
        assert "uncert" in html

    def test_asymmetric_uncertainty(self):
        """Test asymmetric uncertainty with two uncertainty columns."""
        df = pd.DataFrame({"val": [10.0, 20.0], "lower": [0.3, 0.6], "upper": [0.5, 1.0]})

        gt = GT(df).cols_merge_uncert(col_val="val", col_uncert=["lower", "upper"])

        assert gt._col_merge[0].vars == ["val", "lower", "upper"]
        html = gt.as_raw_html()

        # Should contain asymmetric format
        assert "+0.5" in html or "+1.0" in html

    def test_with_polars(self):
        """Test with Polars DataFrame."""
        df = pl.DataFrame({"val": [10.0, 20.0, 30.0], "uncert": [0.5, 1.0, 1.5]})

        gt = GT(df).cols_merge_uncert(col_val="val", col_uncert="uncert")
        html = gt.as_raw_html()

        assert "10.0 \u00b1 0.5" in html

    def test_invalid_col_val(self):
        """Test that multiple columns for col_val raises error."""
        df = pd.DataFrame({"a": [1], "b": [2], "c": [3]})

        with pytest.raises(ValueError, match="exactly one column"):
            GT(df).cols_merge_uncert(col_val=["a", "b"], col_uncert="c")

    def test_with_rows(self):
        """Test with specific rows selected."""
        df = pd.DataFrame({"val": [10.0, 20.0, 30.0], "uncert": [0.5, 1.0, 1.5]})

        gt = GT(df).cols_merge_uncert(col_val="val", col_uncert="uncert", rows=[0, 2])
        html = gt.as_raw_html()

        # Only rows 0 and 2 should be merged
        assert "10.0 \u00b1 0.5" in html
        assert "30.0 \u00b1 1.5" in html

    def test_chaining_two_uncert_merges(self):
        """Test applying cols_merge_uncert twice on different column pairs."""
        df = pl.DataFrame(
            {"val1": [10.0, 20.0], "unc1": [0.5, 1.0], "val2": [30.0, 40.0], "unc2": [1.5, 2.0]}
        )

        gt = (
            GT(df)
            .cols_merge_uncert(col_val="val1", col_uncert="unc1")
            .cols_merge_uncert(col_val="val2", col_uncert="unc2")
        )

        assert len(gt._col_merge) == 2
        assert gt._col_merge[0].vars == ["val1", "unc1"]
        assert gt._col_merge[1].vars == ["val2", "unc2"]

        html = gt.as_raw_html()
        assert "10.0 \u00b1 0.5" in html
        assert "30.0 \u00b1 1.5" in html

    def test_asymmetric_all_na_combinations(self):
        """Test asymmetric uncertainty with all NA combinations (matches R gt behavior)."""
        df = pl.DataFrame(
            {
                "value": [34.5, 29.2, 36.3, 31.6, 28.5, 30.9, None, None],
                "lu": [2.1, 2.4, 2.6, 1.8, None, None, 1.2, None],
                "uu": [1.8, 2.7, 2.6, None, 1.6, None, None, None],
            }
        )

        gt = GT(df).cols_merge_uncert(col_val="value", col_uncert=["lu", "uu"])
        html = gt.as_raw_html()

        # Row 1: both bounds present, asymmetric → val (+upper/−lower)
        assert "+1.8" in html
        assert "\u22122.1" in html  # minus sign

        # Row 3: symmetric (lower == upper == 2.6) → val ± uncert
        assert "36.3 \u00b1 2.6" in html

        # Row 4: upper is NA → val (−lower)
        assert "\u22121.8" in html

        # Row 5: lower is NA → val (+upper)
        assert "+1.6" in html

        # Row 6: both bounds NA but val present → just val
        assert "30.9" in html

        # Row 7 & 8: val is NA → empty (nothing meaningful rendered)

    def test_symmetric_when_bounds_equal(self):
        """Test that when lower == upper, symmetric format (±) is used."""
        df = pl.DataFrame({"val": [100.0], "lower": [2.5], "upper": [2.5]})

        gt = GT(df).cols_merge_uncert(col_val="val", col_uncert=["lower", "upper"])
        html = gt.as_raw_html()

        assert "100.0 \u00b1 2.5" in html


# =============================================================================
# Tests for cols_merge_range
# =============================================================================


class TestColsMergeRange:
    """Tests for the cols_merge_range() method."""

    def test_basic(self):
        """Test basic range merge with en dash."""
        df = pd.DataFrame({"low": [10, 20, 30], "high": [15, 25, 35]})

        gt = GT(df).cols_merge_range(col_begin="low", col_end="high")

        assert len(gt._col_merge) == 1
        assert gt._col_merge[0].type == "merge_range"
        assert gt._col_merge[0].vars == ["low", "high"]

        html = gt.as_raw_html()
        # Should contain en dash
        assert "10\u201315" in html
        assert "20\u201325" in html
        assert "30\u201335" in html

    def test_na_in_begin(self):
        """Test that NA in col_begin shows only col_end value."""
        df = pl.DataFrame({"low": [10, None, 30], "high": [15, 25, 35]})

        gt = GT(df).cols_merge_range(col_begin="low", col_end="high")
        html = gt.as_raw_html()

        # Second row should show only the end value
        assert "10\u201315" in html
        assert "30\u201335" in html
        # "25" should appear alone (not as part of a range)
        assert "25" in html

    def test_na_in_end(self):
        """Test that NA in col_end shows only col_begin value."""
        df = pl.DataFrame({"low": [10, 20, 30], "high": [15, None, 35]})

        gt = GT(df).cols_merge_range(col_begin="low", col_end="high")
        html = gt.as_raw_html()

        assert "10\u201315" in html
        assert "30\u201335" in html
        # "20" should appear alone
        assert "20" in html

    def test_na_in_both(self):
        """Test that NA in both columns produces empty result."""
        df = pl.DataFrame({"low": [10, None, 30], "high": [15, None, 35]})

        gt = GT(df).cols_merge_range(col_begin="low", col_end="high")
        html = gt.as_raw_html()

        assert "10\u201315" in html
        assert "30\u201335" in html

    def test_custom_sep(self):
        """Test custom separator."""
        df = pd.DataFrame({"low": [10, 20], "high": [15, 25]})

        gt = GT(df).cols_merge_range(col_begin="low", col_end="high", sep=" to ")
        html = gt.as_raw_html()

        assert "10 to 15" in html
        assert "20 to 25" in html

    def test_sep_en_dash(self):
        """Test that '--' is converted to en dash."""
        df = pd.DataFrame({"low": [10], "high": [15]})

        gt = GT(df).cols_merge_range(col_begin="low", col_end="high", sep="--")
        html = gt.as_raw_html()

        assert "10\u201315" in html

    def test_sep_em_dash(self):
        """Test that '---' is converted to em dash."""
        df = pd.DataFrame({"low": [10], "high": [15]})

        gt = GT(df).cols_merge_range(col_begin="low", col_end="high", sep="---")
        html = gt.as_raw_html()

        assert "10\u201415" in html

    def test_autohide_true(self):
        """Test that col_end is hidden by default."""
        df = pd.DataFrame({"low": [10], "high": [15]})

        gt = GT(df).cols_merge_range(col_begin="low", col_end="high")
        html = gt.as_raw_html()

        # "high" column header should not appear
        assert ">high<" not in html

    def test_autohide_false(self):
        """Test that col_end remains visible when autohide=False."""
        df = pd.DataFrame({"low": [10], "high": [15]})

        gt = GT(df).cols_merge_range(col_begin="low", col_end="high", autohide=False)
        html = gt.as_raw_html()

        # "high" column header should appear
        assert "high" in html

    def test_with_polars(self):
        """Test with Polars DataFrame."""
        df = pl.DataFrame({"low": [10, 20, 30], "high": [15, 25, 35]})

        gt = GT(df).cols_merge_range(col_begin="low", col_end="high")
        html = gt.as_raw_html()

        assert "10\u201315" in html

    def test_invalid_col_begin(self):
        """Test that multiple columns for col_begin raises error."""
        df = pd.DataFrame({"a": [1], "b": [2], "c": [3]})

        with pytest.raises(ValueError, match="exactly one column"):
            GT(df).cols_merge_range(col_begin=["a", "b"], col_end="c")

    def test_with_formatted_values(self):
        """Test that formatting is preserved."""
        df = pl.DataFrame({"mpg_c": [16.0, 18.5], "mpg_h": [20.0, 22.5]})

        gt = (
            GT(df)
            .fmt_number(columns=["mpg_c", "mpg_h"], decimals=1)
            .cols_merge_range(col_begin="mpg_c", col_end="mpg_h")
        )
        html = gt.as_raw_html()

        assert "16.0\u201320.0" in html
        assert "18.5\u201322.5" in html

    def test_chaining_two_range_merges(self):
        """Test applying cols_merge_range twice on different column pairs."""
        df = pl.DataFrame(
            {"col_1": [10, 20], "col_2": [15, 25], "col_3": [100, 200], "col_4": [150, 250]}
        )

        gt = (
            GT(df)
            .cols_merge_range(col_begin="col_1", col_end="col_2")
            .cols_merge_range(col_begin="col_3", col_end="col_4")
        )

        assert len(gt._col_merge) == 2
        assert gt._col_merge[0].vars == ["col_1", "col_2"]
        assert gt._col_merge[1].vars == ["col_3", "col_4"]

        html = gt.as_raw_html()
        assert "10\u201315" in html
        assert "100\u2013150" in html

    def test_equal_values(self):
        """Test range merge when begin and end are the same value."""
        df = pl.DataFrame({"low": [10, 20], "high": [10, 25]})

        gt = GT(df).cols_merge_range(col_begin="low", col_end="high")
        html = gt.as_raw_html()

        # When values are equal, both sides of the dash still appear
        assert "10\u201310" in html
        assert "20\u201325" in html

    def test_with_rows(self):
        """Test with specific rows selected."""
        df = pl.DataFrame({"low": [10, 20, 30], "high": [15, 25, 35]})

        gt = GT(df).cols_merge_range(col_begin="low", col_end="high", rows=[0, 2])
        html = gt.as_raw_html()

        # Only rows 0 and 2 should be merged
        assert "10\u201315" in html
        assert "30\u201335" in html


# =============================================================================
# Tests for cols_merge_n_pct
# =============================================================================


class TestColsMergeNPct:
    """Tests for the cols_merge_n_pct() method."""

    def test_basic(self):
        """Test basic count and percentage merge."""
        df = pd.DataFrame({"n": [10, 20, 30], "pct": ["16.7%", "33.3%", "50.0%"]})

        gt = GT(df).cols_merge_n_pct(col_n="n", col_pct="pct")

        assert len(gt._col_merge) == 1
        assert gt._col_merge[0].type == "merge_n_pct"
        assert gt._col_merge[0].vars == ["n", "pct"]

        html = gt.as_raw_html()
        assert "10 (16.7%)" in html
        assert "20 (33.3%)" in html
        assert "30 (50.0%)" in html

    def test_na_in_n(self):
        """Test that NA in col_n produces empty result."""
        df = pl.DataFrame({"n": [10, None, 30], "pct": ["16.7%", "33.3%", "50.0%"]})

        gt = GT(df).cols_merge_n_pct(col_n="n", col_pct="pct")
        html = gt.as_raw_html()

        assert "10 (16.7%)" in html
        assert "30 (50.0%)" in html

    def test_na_in_pct(self):
        """Test that NA in col_pct shows only the count."""
        df = pl.DataFrame({"n": [10, 20, 30], "pct": ["16.7%", None, "50.0%"]})

        gt = GT(df).cols_merge_n_pct(col_n="n", col_pct="pct")
        html = gt.as_raw_html()

        assert "10 (16.7%)" in html
        assert "30 (50.0%)" in html
        # Row 2 should just show "20" without parens
        assert "20 (" not in html.replace("10 (16.7%)", "").replace("30 (50.0%)", "")

    def test_na_in_both(self):
        """Test that NA in both columns produces empty result."""
        df = pl.DataFrame({"n": [10, None, 30], "pct": ["16.7%", None, "50.0%"]})

        gt = GT(df).cols_merge_n_pct(col_n="n", col_pct="pct")
        html = gt.as_raw_html()

        assert "10 (16.7%)" in html
        assert "30 (50.0%)" in html

    def test_zero_in_n(self):
        """Test that zero in col_n shows only '0' without percentage."""
        df = pd.DataFrame({"n": [0, 20, 30], "pct": ["0.0%", "33.3%", "50.0%"]})

        gt = GT(df).cols_merge_n_pct(col_n="n", col_pct="pct")
        html = gt.as_raw_html()

        # Zero should not have percentage
        assert "0 (0.0%)" not in html
        # But should have the zero value
        assert "20 (33.3%)" in html
        assert "30 (50.0%)" in html

    def test_autohide_true(self):
        """Test that col_pct is hidden by default."""
        df = pd.DataFrame({"n": [10], "pct": ["16.7%"]})

        gt = GT(df).cols_merge_n_pct(col_n="n", col_pct="pct")
        html = gt.as_raw_html()

        # "pct" column header should not appear
        assert ">pct<" not in html

    def test_autohide_false(self):
        """Test that col_pct remains visible when autohide=False."""
        df = pd.DataFrame({"n": [10], "pct": ["16.7%"]})

        gt = GT(df).cols_merge_n_pct(col_n="n", col_pct="pct", autohide=False)
        html = gt.as_raw_html()

        assert "pct" in html

    def test_with_polars(self):
        """Test with Polars DataFrame."""
        df = pl.DataFrame({"n": [10, 20, 30], "pct": ["16.7%", "33.3%", "50.0%"]})

        gt = GT(df).cols_merge_n_pct(col_n="n", col_pct="pct")
        html = gt.as_raw_html()

        assert "10 (16.7%)" in html

    def test_with_fmt_percent(self):
        """Test integration with fmt_percent for realistic usage."""
        df = pl.DataFrame({"n": [10, 20, 30], "pct": [0.167, 0.333, 0.500]})

        gt = (
            GT(df).fmt_percent(columns="pct", decimals=1).cols_merge_n_pct(col_n="n", col_pct="pct")
        )
        html = gt.as_raw_html()

        assert "10 (16.7%)" in html
        assert "20 (33.3%)" in html
        assert "30 (50.0%)" in html

    def test_invalid_col_n(self):
        """Test that multiple columns for col_n raises error."""
        df = pd.DataFrame({"a": [1], "b": [2], "c": [3]})

        with pytest.raises(ValueError, match="exactly one column"):
            GT(df).cols_merge_n_pct(col_n=["a", "b"], col_pct="c")

    def test_with_rows(self):
        """Test with specific rows selected."""
        df = pd.DataFrame({"n": [10, 20, 30], "pct": ["16.7%", "33.3%", "50.0%"]})

        gt = GT(df).cols_merge_n_pct(col_n="n", col_pct="pct", rows=[0, 2])
        html = gt.as_raw_html()

        # Only rows 0 and 2 should be merged
        assert "10 (16.7%)" in html
        assert "30 (50.0%)" in html

    def test_comprehensive_na_zero_matrix(self):
        """Test all combinations of NA and zero values (mirrors R gt test matrix).

        R gt expected outputs for this dataset:
        - (1, 0.0714)  → "1 (7.1%)"
        - (5, 0.3571)  → "5 (35.7%)"
        - (0, 0.0)     → "0"           (zero suppresses pct)
        - (2, 0.1429)  → "2 (14.3%)"
        - (NA, NA)     → ""            (NA in col_n)
        - (6, 0.4286)  → "6 (42.9%)"
        - (5, NA)      → "5"           (NA in col_pct only)
        - (NA, 1000)   → ""            (NA in col_n)
        - (0, NA)      → "0"           (zero + NA pct → just zero)
        - (NA, 0)      → ""            (NA in col_n)
        """
        df = pl.DataFrame(
            {
                "a": [1, 5, 0, 2, None, 6, 5, None, 0, None],
                "b": [0.0714, 0.3571, 0.0, 0.1429, None, 0.4286, None, 1000.0, None, 0.0],
            }
        )

        gt = GT(df).fmt_percent(columns="b", decimals=1).cols_merge_n_pct(col_n="a", col_pct="b")
        html = gt.as_raw_html()

        # Positive cases: n with pct
        assert "1 (7.1%)" in html
        assert "5 (35.7%)" in html
        assert "2 (14.3%)" in html
        assert "6 (42.9%)" in html

        # Zero in col_n: no percentage shown
        # We check that "0 (" doesn't appear (zero rows don't get parens)
        # Note: "0" should appear without parentheses for zero rows

        # NA in col_pct only: show just the count
        # Row 7: n=5, pct=NA → "5" (without parens)

        # NA in col_n: empty result (no meaningful content for that cell)

    def test_chaining_n_pct_and_range(self):
        """Test combining cols_merge_n_pct with cols_merge_range."""
        df = pl.DataFrame({"n": [10, 20], "pct": [0.167, 0.333], "low": [5, 10], "high": [15, 25]})

        gt = (
            GT(df)
            .fmt_percent(columns="pct", decimals=1)
            .cols_merge_n_pct(col_n="n", col_pct="pct")
            .cols_merge_range(col_begin="low", col_end="high")
        )

        assert len(gt._col_merge) == 2
        html = gt.as_raw_html()
        assert "10 (16.7%)" in html
        assert "5\u201315" in html
