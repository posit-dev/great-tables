import pandas as pd
import polars as pl
import polars.testing
import pytest

from gt._tbl_data import _get_cell, _get_column_dtype, _set_cell, get_column_names, DataFrameLike


params_frames = [
    pytest.param(pd.DataFrame, id="pandas"),
    pytest.param(pl.DataFrame, id="polars")
]

@pytest.fixture(params=params_frames, scope="function")
def df(request) -> pd.DataFrame:
    return request.param({
        'col1': [1, 2, 3],
        'col2': ['a', 'b', 'c'],
        'col3': [4.0, 5.0, 6.0]
    })


def assert_frame_equal(src, target):
    if isinstance(src, pd.DataFrame):
        pd.testing.assert_frame_equal(src, target)
    elif isinstance(src, pl.DataFrame):
        pl.testing.assert_frame_equal(src, target)
    else:
        raise NotImplementedError(f"Unsupported data type: {type(src)}")


def test_get_column_names(df: DataFrameLike):
    expected = ['col1', 'col2', 'col3']
    assert get_column_names(df) == expected


def test_get_column_dtypes(df: DataFrameLike):
    assert _get_column_dtype(df, "col1") == df["col1"].dtype


def test_get_cell(df: DataFrameLike):
    assert _get_cell(df, 1, 'col2') == 'b'


def test_set_cell(df: DataFrameLike):
    expected = df.__class__({
        'col1': [1, 2, 3],
        'col2': ['a', 'x', 'c'],
        'col3': [4.0, 5.0, 6.0]
    })
    _set_cell(df, 1, 'col2', 'x')
    assert_frame_equal(df, expected)
