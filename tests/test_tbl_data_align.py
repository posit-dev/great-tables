"""Tests for dtype classification and auto-alignment."""

from collections.abc import Callable
from datetime import date, datetime, time
from decimal import Decimal
from typing import Any

import pandas as pd
import polars as pl
import pyarrow as pa
import pytest

from great_tables._tbl_data import DataFrameLike, _re_version
from great_tables._tbl_data_align import (
    ALIGNMENT_MAP,
    classify_dtype_for_alignment,
    is_number_like_column,
)
import great_tables as gt
from tests.utils import DataFrameConstructor

pandas_ge_v3 = _re_version(pd.__version__) >= (3, 0, 0)


class TestClassifyDtype:
    """Test dtype classification on every backend.

    `test_classify_dtype_for_alignment_dtype_matrix` in test_tbl_data.py covers the other dtypes,
    with missing values.
    """

    @pytest.mark.parametrize(
        "values, expected",
        [
            pytest.param([1, 2, 3], "numeric", id="int"),
            pytest.param([1.5, 2.5, 3.5], "numeric", id="float"),
            pytest.param(["a", "b", "c"], "string", id="str"),
            pytest.param([True, False, True], "other", id="bool"),
        ],
    )
    def test_types(self, frame_constructor: DataFrameConstructor, values: list[Any], expected: str):
        df = frame_constructor({"col": values})
        assert classify_dtype_for_alignment(df, "col") == expected

    def test_date_type(self, frame_constructor: DataFrameConstructor):
        df = frame_constructor({"col": [date(2024, 1, 1), date(2024, 1, 2)]})

        # pandas keeps dates in an object column, which is classified by its values (#1024)
        assert classify_dtype_for_alignment(df, "col") == "numeric"
        assert [col.column_align for col in gt.GT(df)._boxhead._d] == ["right"]

    def test_datetime_type(self, frame_constructor: DataFrameConstructor):
        df = frame_constructor({"col": [datetime(2024, 1, 1, 12, 30), datetime(2024, 1, 2)]})
        assert classify_dtype_for_alignment(df, "col") == "numeric"


# Dtypes that Python values can't build


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

    @pytest.mark.parametrize(
        "values, expected",
        [
            pytest.param([True, None], "other", id="bool-with-missing"),
            pytest.param([time(12, 30), None], "other", id="time"),
            pytest.param([Decimal("1.5"), None], "other", id="decimal"),
            pytest.param([[1, 2], [3]], "other", id="list"),
            pytest.param([None, None], "other", id="all-missing"),
            pytest.param([date(2024, 1, 1), None], "numeric", id="date"),
            pytest.param([datetime(2024, 1, 1, 12, 30), None], "numeric", id="datetime"),
            pytest.param([1, 2.5, None], "numeric", id="numbers"),
            pytest.param(["1.5", None], "string", id="number-like-str"),
            pytest.param(["a", 1], "string", id="mixed-with-str"),
        ],
    )
    def test_object_column_classified_by_values(self, values: list[Any], expected: str):
        # polars and pyarrow type these columns; pandas keeps them as `object`, so they are
        # classified by their values to align the same way (#1024)
        df = pd.DataFrame({"col": pd.Series(values, dtype=object)})
        assert str(df["col"].dtype) == "object"
        assert classify_dtype_for_alignment(df, "col") == expected


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


class TestClassifyDtypePyArrow:
    """Test dtype classification for PyArrow."""

    @pytest.mark.parametrize(
        "pyarrow_type,expected",
        [
            (pa.int64(), "numeric"),
            (pa.int32(), "numeric"),
            (pa.uint8(), "numeric"),
            (pa.float64(), "numeric"),
            (pa.float32(), "numeric"),
        ],
    )
    def test_numeric_types(self, pyarrow_type, expected):
        table = pa.table({"col": pa.array([1, 2, 3], type=pyarrow_type)})
        assert classify_dtype_for_alignment(table, "col") == expected

    def test_utf8_type(self):
        # utf8 is an alias for string in PyArrow
        table = pa.table({"col": pa.array(["a", "b", "c"], type=pa.utf8())})
        assert classify_dtype_for_alignment(table, "col") == "string"


class TestNumberLikeDetection:
    """Tests for is_number_like_column() function."""

    @pytest.mark.parametrize(
        ("values", "expected"),
        [
            pytest.param(["2024-01-15", "2024-02-20", "2024-03-25"], True, id="dates"),
            pytest.param(["10:30:00", "14:45:30", "23:59:59"], True, id="times"),
            pytest.param(["123", "456", "789"], True, id="numbers"),
            pytest.param(["", "", ""], True, id="empty strings"),
            pytest.param(["1.5", None], True, id="missing value"),
            pytest.param(["abc", "123", "def"], False, id="mixed text"),
            pytest.param(["hello", "world", "test"], False, id="text"),
            pytest.param([True, None], False, id="no strings"),
        ],
    )
    def test_number_like(
        self, frame_constructor: DataFrameConstructor, values: list[Any], expected: bool
    ):
        df = frame_constructor({"col": values})
        assert is_number_like_column(df, "col") is expected


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

    def test_auto_align(self, frame_constructor: DataFrameConstructor):
        df = frame_constructor(
            {"int": [1, 2], "float": [1.5, 2.5], "str": ["a", "b"], "bool": [True, False]}
        )
        gt_tbl = gt.GT(df)
        aligns = [col.column_align for col in gt_tbl._boxhead._d]
        assert aligns == ["right", "right", "left", "center"]

    def test_auto_align_disabled(self, frame_constructor: DataFrameConstructor):
        df = frame_constructor({"num": [1, 2], "text": ["a", "b"]})
        gt_tbl = gt.GT(df, auto_align=False)
        aligns = [col.column_align for col in gt_tbl._boxhead._d]
        # When auto_align=False, columns keep default alignment (None)
        assert aligns == [None, None]

    def test_number_like_strings_align(self, frame_constructor: DataFrameConstructor):
        df = frame_constructor({"col": ["1.5", "2024-01-01"]})

        if frame_constructor.__name__ == "pandas_constructor":
            # The same strings make a `str` column on pandas 3 and an `object` one on pandas 2
            assert str(df["col"].dtype) == ("str" if pandas_ge_v3 else "object")

        gt_tbl = gt.GT(df)
        aligns = [col.column_align for col in gt_tbl._boxhead._d]
        assert aligns == ["right"]

    @pytest.mark.parametrize(
        "values", [pytest.param([None, None], id="all-null"), pytest.param([], id="zero-rows")]
    )
    @pytest.mark.parametrize(
        "make_frame",
        [
            pytest.param(lambda v: pl.DataFrame({"s": v}, schema={"s": pl.String}), id="polars"),
            pytest.param(lambda v: pa.table({"s": pa.array(v, type=pa.string())}), id="pyarrow"),
            pytest.param(
                lambda v: pd.DataFrame({"s": pd.array(v, dtype="string")}), id="pandas-nullable"
            ),
            pytest.param(
                lambda v: pd.DataFrame({"s": pd.array(v, dtype=pd.ArrowDtype(pa.string()))}),
                id="pandas-pyarrow",
            ),
            pytest.param(
                lambda v: pd.DataFrame({"s": pd.Series(v, dtype="str")}),
                id="pandas-str",
                marks=pytest.mark.skipif(not pandas_ge_v3, reason="`str` is `object` on pandas 2"),
            ),
        ],
    )
    def test_string_column_without_values_left_aligned(
        self, make_frame: Callable[[list[Any]], DataFrameLike], values: list[Any]
    ):
        aligns = [col.column_align for col in gt.GT(make_frame(values))._boxhead._d]
        assert aligns == ["left"]

    def test_mixed_text_left_align(self, frame_constructor: DataFrameConstructor):
        # String columns with non-number-like content get left-aligned
        df = frame_constructor({"mixed": ["hello", "123", None]})
        gt_tbl = gt.GT(df)
        aligns = [col.column_align for col in gt_tbl._boxhead._d]
        assert aligns == ["left"]  # mixed text -> left

    @pytest.mark.parametrize(
        "arrow_str",
        [
            pytest.param("string", id="string"),
            pytest.param("large_string", id="large_string"),
            pytest.param(
                "string_view",
                id="string_view",
                marks=pytest.mark.skipif(
                    not hasattr(pa, "string_view"), reason="requires pyarrow>=16"
                ),
            ),
        ],
    )
    def test_pandas_pyarrow_string_auto_align(self, arrow_str):
        df = pd.DataFrame(
            {
                "num": pd.array([1, 2], dtype=pd.ArrowDtype(pa.int64())),
                "text": pd.array(["a", "b"], dtype=pd.ArrowDtype(getattr(pa, arrow_str)())),
            }
        )
        gt_tbl = gt.GT(df)
        aligns = [col.column_align for col in gt_tbl._boxhead._d]
        assert aligns == ["right", "left"]

    @pytest.mark.parametrize(
        "arrow_str",
        [
            pytest.param("string", id="string"),
            pytest.param("large_string", id="large_string"),
            pytest.param(
                "string_view",
                id="string_view",
                marks=pytest.mark.skipif(
                    not hasattr(pa, "string_view"), reason="requires pyarrow>=16"
                ),
            ),
        ],
    )
    def test_pyarrow_string_types_left_aligned(self, arrow_str):
        table = pa.table(
            {
                "num": pa.array([1, 2], type=pa.int64()),
                "text": pa.array(["a", "b"], type=getattr(pa, arrow_str)()),
            }
        )
        assert classify_dtype_for_alignment(table, "text") == "string"
        gt_tbl = gt.GT(table)
        aligns = [col.column_align for col in gt_tbl._boxhead._d]
        assert aligns == ["right", "left"]

    def test_pandas_pyarrow_string_matches_object(self):
        df = pd.DataFrame(
            {
                "text": ["Row 1", "Row 2"],
                "dates": ["2024-01-15", "2024-02-20"],
                "numbers": ["20 23 6", "2.3 6.8"],
            }
        )
        df_arrow = df.convert_dtypes(dtype_backend="pyarrow")
        assert df_arrow["text"].dtype == pd.ArrowDtype(pa.string())

        expected = [col.column_align for col in gt.GT(df)._boxhead._d]
        result = [col.column_align for col in gt.GT(df_arrow)._boxhead._d]
        assert expected == ["left", "right", "right"]
        assert result == expected


class TestClassifyDtypeFallback:
    """Test the singledispatch fallback for unknown data types."""

    def test_fallback_dispatches_for_unknown_type(self):
        # The singledispatch fallback uses string-based pattern matching.
        # Call it directly via dispatch(object) to test the fallback path.
        fallback_fn = classify_dtype_for_alignment.dispatch(object)
        import pandas as pd

        df = pd.DataFrame({"col": [1, 2, 3]})

        # Calling the fallback directly bypasses the registered pandas handler
        result = fallback_fn(df, "col")

        assert result in ("numeric", "string", "other")

    def test_fallback_numeric_detection(self):
        fallback_fn = classify_dtype_for_alignment.dispatch(object)
        import pandas as pd

        df = pd.DataFrame({"col": pd.array([1.0, 2.0], dtype="float64")})
        result = fallback_fn(df, "col")

        assert result == "numeric"

    def test_fallback_string_detection(self):
        fallback_fn = classify_dtype_for_alignment.dispatch(object)
        import pandas as pd

        df = pd.DataFrame({"col": pd.array(["a", "b"], dtype="object")})
        result = fallback_fn(df, "col")

        assert result == "string"

    def test_fallback_other_detection(self):
        # The "other" branch in the fallback is triggered when dtype is
        # neither numeric nor string (e.g., boolean)
        fallback_fn = classify_dtype_for_alignment.dispatch(object)
        import pandas as pd

        df = pd.DataFrame({"col": pd.array([True, False], dtype="bool")})
        result = fallback_fn(df, "col")

        assert result == "other"
