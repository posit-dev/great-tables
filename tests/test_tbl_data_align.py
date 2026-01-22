"""Tests for dtype classification and auto-alignment."""

import pandas as pd
import polars as pl
import pytest

from great_tables._tbl_data_align import (
    ALIGNMENT_MAP,
    classify_dtype_for_alignment,
    is_number_like_column,
)
import great_tables as gt


class TestClassifyDtypePandas:
    """Test dtype classification for pandas."""

    @pytest.mark.parametrize(
        "dtype,expected",
        [
            ("int64", "numeric"),
            ("int32", "numeric"),
            ("float64", "numeric"),
            ("float32", "numeric"),
        ],
    )
    def test_numeric_types(self, dtype, expected):
        df = pd.DataFrame({"col": pd.array([1, 2, 3], dtype=dtype)})
        assert classify_dtype_for_alignment(df, "col") == expected

    def test_str_type_classified_as_string(self):
        # Pandas 3.x uses "str" dtype for string columns, which is in STRING_DTYPES
        df = pd.DataFrame({"col": ["a", "b", "c"]})
        assert classify_dtype_for_alignment(df, "col") == "string"

    def test_bool_type(self):
        df = pd.DataFrame({"col": [True, False, True]})
        assert classify_dtype_for_alignment(df, "col") == "other"

    def test_datetime_type(self):
        df = pd.DataFrame({"col": pd.to_datetime(["2024-01-01", "2024-01-02"])})
        assert classify_dtype_for_alignment(df, "col") == "numeric"


class TestClassifyDtypePolars:
    """Test dtype classification for polars."""

    @pytest.mark.parametrize(
        "dtype,expected",
        [
            (pl.Int64, "numeric"),
            (pl.Int32, "numeric"),
            (pl.UInt8, "numeric"),
            (pl.UInt64, "numeric"),
            (pl.Float64, "numeric"),
            (pl.Float32, "numeric"),
        ],
    )
    def test_numeric_types(self, dtype, expected):
        df = pl.DataFrame({"col": pl.Series([1, 2, 3]).cast(dtype)})
        assert classify_dtype_for_alignment(df, "col") == expected

    def test_string_type(self):
        df = pl.DataFrame({"col": ["a", "b", "c"]})
        # Polars "String" dtype lowercases to "string" which is in STRING_DTYPES
        assert classify_dtype_for_alignment(df, "col") == "string"

    def test_bool_type(self):
        df = pl.DataFrame({"col": [True, False, True]})
        assert classify_dtype_for_alignment(df, "col") == "other"

    def test_date_type(self):
        df = pl.DataFrame({"col": pl.Series(["2024-01-01", "2024-01-02"]).str.to_date()})
        assert classify_dtype_for_alignment(df, "col") == "numeric"

    def test_datetime_type(self):
        df = pl.DataFrame({"col": pl.Series(["2024-01-01", "2024-01-02"]).str.to_datetime()})
        assert classify_dtype_for_alignment(df, "col") == "numeric"


class TestNumberLikeDetection:
    """Tests for is_number_like_column() function."""

    def test_date_like_strings(self):
        df = pd.DataFrame({"col": ["2024-01-15", "2024-02-20", "2024-03-25"]})
        assert is_number_like_column(df, "col") is True

    def test_time_like_strings(self):
        df = pd.DataFrame({"col": ["10:30:00", "14:45:30", "23:59:59"]})
        assert is_number_like_column(df, "col") is True

    def test_mixed_text_not_number_like(self):
        df = pd.DataFrame({"col": ["abc", "123", "def"]})
        assert is_number_like_column(df, "col") is False

    def test_pure_text_not_number_like(self):
        df = pd.DataFrame({"col": ["hello", "world", "test"]})
        assert is_number_like_column(df, "col") is False

    def test_numeric_strings(self):
        df = pd.DataFrame({"col": ["123", "456", "789"]})
        assert is_number_like_column(df, "col") is True

    def test_empty_strings(self):
        # NOTE: Empty strings match the current pattern (^[0-9 -/:\\.]*$)
        # This documents current behavior
        df = pd.DataFrame({"col": ["", "", ""]})
        assert is_number_like_column(df, "col") is True

    def test_polars_number_like(self):
        # Polars string columns work with number-like detection
        df_str = pl.DataFrame({"col": ["2024-01-15", "2024-02-20"]})
        assert is_number_like_column(df_str, "col") is True


class TestAlignmentMap:
    """Tests for ALIGNMENT_MAP constant."""

    def test_numeric_maps_to_right(self):
        assert ALIGNMENT_MAP["numeric"] == "right"

    def test_string_maps_to_left(self):
        assert ALIGNMENT_MAP["string"] == "left"

    def test_other_maps_to_center(self):
        assert ALIGNMENT_MAP["other"] == "center"


class TestAutoAlignIntegration:
    """Integration tests verifying GT auto-alignment behavior."""

    def test_pandas_auto_align(self):
        df = pd.DataFrame({"num": [1, 2], "text": ["a", "b"]})
        gt_tbl = gt.GT(df)
        aligns = [col.column_align for col in gt_tbl._boxhead._d]
        assert aligns == ["right", "left"]  # int -> right, str -> left

    def test_polars_auto_align(self):
        df = pl.DataFrame({"num": [1, 2], "text": ["a", "b"]})
        gt_tbl = gt.GT(df)
        aligns = [col.column_align for col in gt_tbl._boxhead._d]
        assert aligns == ["right", "left"]  # int -> right, String -> left

    def test_auto_align_disabled(self):
        df = pd.DataFrame({"num": [1, 2], "text": ["a", "b"]})
        gt_tbl = gt.GT(df, auto_align=False)
        aligns = [col.column_align for col in gt_tbl._boxhead._d]
        # When auto_align=False, columns keep default alignment (None)
        assert aligns == [None, None]

    def test_pandas_date_strings_right_align(self):
        # String columns with number-like content (dates) get right-aligned
        df = pd.DataFrame({"dates": ["2024-01-15", "2024-02-20", "2024-03-25"]})
        gt_tbl = gt.GT(df)
        aligns = [col.column_align for col in gt_tbl._boxhead._d]
        assert aligns == ["right"]  # number-like strings -> right

    def test_pandas_mixed_text_left_align(self):
        # String columns with non-number-like content get left-aligned
        df = pd.DataFrame({"mixed": ["hello", "123", "world"]})
        gt_tbl = gt.GT(df)
        aligns = [col.column_align for col in gt_tbl._boxhead._d]
        assert aligns == ["left"]  # mixed text -> left
