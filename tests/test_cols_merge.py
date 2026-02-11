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
