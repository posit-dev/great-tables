import pandas as pd
import polars as pl
import polars.testing
import pytest

from great_tables._tbl_data import (
    _get_cell,
    _get_column_dtype,
    _set_cell,
    get_column_names,
    DataFrameLike,
    reorder,
    eval_select,
    create_empty_frame,
    validate_frame,
)


params_frames = [pytest.param(pd.DataFrame, id="pandas"), pytest.param(pl.DataFrame, id="polars")]


@pytest.fixture(params=params_frames, scope="function")
def df(request) -> pd.DataFrame:
    return request.param({"col1": [1, 2, 3], "col2": ["a", "b", "c"], "col3": [4.0, 5.0, 6.0]})


def assert_frame_equal(src, target):
    if isinstance(src, pd.DataFrame):
        pd.testing.assert_frame_equal(src, target)
    elif isinstance(src, pl.DataFrame):
        pl.testing.assert_frame_equal(src, target)
    else:
        raise NotImplementedError(f"Unsupported data type: {type(src)}")


def test_get_column_names(df: DataFrameLike):
    expected = ["col1", "col2", "col3"]
    assert get_column_names(df) == expected


def test_get_column_dtypes(df: DataFrameLike):
    assert _get_column_dtype(df, "col1") == df["col1"].dtype


def test_get_cell(df: DataFrameLike):
    assert _get_cell(df, 1, "col2") == "b"


def test_set_cell(df: DataFrameLike):
    expected = df.__class__({"col1": [1, 2, 3], "col2": ["a", "x", "c"], "col3": [4.0, 5.0, 6.0]})
    _set_cell(df, 1, "col2", "x")
    assert_frame_equal(df, expected)


def test_reorder(df: DataFrameLike):
    res = reorder(df, [0, 2], ["col2"])
    dst = df.__class__({"col2": ["a", "c"]})

    if isinstance(dst, pd.DataFrame):
        dst.index = pd.Index([0, 2])

    assert_frame_equal(res, dst)


def test_eval_select_with_list(df: DataFrameLike):
    sel = eval_select(df, ["col2", "col1"])
    assert sel == [("col2", 1), ("col1", 0)]


def test_create_empty_frame(df: DataFrameLike):
    res = create_empty_frame(df)
    col = [None] * 3

    if isinstance(res, pd.DataFrame):
        dst = pd.DataFrame({"col1": col, "col2": col, "col3": col}, dtype="string")
    else:
        dst = pl.DataFrame({"col1": col, "col2": col, "col3": col}).cast(pl.Utf8)

    assert_frame_equal(res, dst)


def test_validate_frame_dupe_cols():
    df = pd.DataFrame([[1, 2, 3]], columns=["x", "x", "y"])

    with pytest.raises(ValueError) as exc_info:
        validate_frame(df)

    assert "Column names must be unique" in str(exc_info.value.args[0])


def test_validate_frame_multi_index():
    df = pd.DataFrame(
        [[1, 2, 3]], columns=pd.MultiIndex.from_tuples([("a", "x"), ("a", "y"), ("b", "x")])
    )

    with pytest.raises(ValueError) as exc_info:
        validate_frame(df)

    assert "MultiIndex columns are not supported" in str(exc_info.value.args[0])


def test_validate_frame_non_str_cols_warning(snapshot):
    df = pd.DataFrame({"x": [1], 55: [2], "y": [3], 99: [4]})

    with pytest.warns(UserWarning) as record:
        validate_frame(df)

    assert len(record) == 1
    assert snapshot == record[0].message.args[0]


def test_validate_frame_non_str_cols_result():
    df = pd.DataFrame({"x": [1], 55: [2], "y": [3], 99: [4]})

    with pytest.warns(UserWarning):
        res = validate_frame(df)

    assert list(res.columns) == ["x", "55", "y", "99"]
