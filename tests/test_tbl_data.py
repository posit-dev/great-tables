import math
import pandas as pd
import polars as pl
import polars.testing
import pytest
from great_tables._tbl_data import (
    DataFrameLike,
    SeriesLike,
    _get_cell,
    _get_column_dtype,
    _set_cell,
    _validate_selector_list,
    cast_frame_to_string,
    create_empty_frame,
    eval_select,
    get_column_names,
    group_splits,
    is_series,
    reorder,
    to_frame,
    validate_frame,
)

params_frames = [pytest.param(pd.DataFrame, id="pandas"), pytest.param(pl.DataFrame, id="polars")]
params_series = [pytest.param(pd.Series, id="pandas"), pytest.param(pl.Series, id="polars")]


@pytest.fixture(params=params_frames, scope="function")
def df(request) -> pd.DataFrame:
    return request.param({"col1": [1, 2, 3], "col2": ["a", "b", "c"], "col3": [4.0, 5.0, 6.0]})


@pytest.fixture(params=params_series, scope="function")
def ser(request) -> SeriesLike:
    return request.param([1.0, 2.0, None])


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


@pytest.mark.parametrize("expr", [["col2", "col1"], [1, 0], ["col2", 0], [1, "col1"]])
def test_eval_select_with_list(df: DataFrameLike, expr):
    sel = eval_select(df, expr)
    assert sel == [("col2", 1), ("col1", 0)]


@pytest.mark.parametrize(
    "expr",
    [
        pl.selectors.exclude("col3"),
        pl.selectors.starts_with("col1") | pl.selectors.starts_with("col2"),
        [pl.col("col1"), pl.col("col2")],
        [pl.col("col1"), pl.selectors.by_name("col2")],
        pl.col("col1", "col2"),
        pl.all().exclude("col3"),
    ],
)
def test_eval_select_with_list_pl_selector(expr):
    df = pl.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"], "col3": [4.0, 5.0, 6.0]})
    sel = eval_select(df, expr)
    assert sel == [("col1", 0), ("col2", 1)]


@pytest.mark.parametrize("expr", [["col2", 1.2]])
def test_eval_select_pandas_raises1(expr):
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"], "col3": [4.0, 5.0, 6.0]})
    with pytest.raises(TypeError) as exc_info:
        eval_select(df, expr)

    assert "Only int and str are supported." in str(exc_info.value.args[0])


@pytest.mark.parametrize("expr", [3.45, {"col2"}, ("col2",)])
def test_eval_select_pandas_raises2(expr):
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"], "col3": [4.0, 5.0, 6.0]})
    with pytest.raises(NotImplementedError) as exc_info:
        eval_select(df, expr)

    assert "Unsupported selection expr: " in str(exc_info.value.args[0])


@pytest.mark.parametrize("expr", [3.45, {6}, (7.8,)])
def test_eval_select_polars_raises(expr):
    df = pl.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"], "col3": [4.0, 5.0, 6.0]})
    with pytest.raises(TypeError) as exc_info:
        eval_select(df, expr)

    assert "Unsupported selection expr type:" in str(exc_info.value.args[0])


def test_eval_selector_polars_list_raises():
    expr = ["col1", 1.2]
    df = pl.DataFrame({"col1": [], "col2": [], "col3": []})
    with pytest.raises(TypeError) as exc_info:
        eval_select(df, expr)

    assert "entry 1 is type: <class 'float'>" in str(exc_info.value.args[0])


@pytest.mark.parametrize("Frame", [pd.DataFrame, pl.DataFrame])
def test_group_splits_pd(Frame):
    df = Frame({"g": ["b", "a", "b", "c"]})

    splits = group_splits(df, "g")
    assert set(splits.keys()) == {"a", "b", "c"}
    assert splits["b"] == [0, 2]
    assert splits["a"] == [1]
    assert splits["c"] == [3]


def test_group_splits_pd_na():
    df = pd.DataFrame({"g": ["b", "a", None]})

    splits = group_splits(df, "g")
    assert len(splits.keys()) == 3
    nan_key = [k for k in splits if isinstance(k, float) and math.isnan(k)][0]

    assert splits[nan_key] == [2]


def test_group_splits_pl_na():
    df = pl.DataFrame({"g": ["b", "a", None]})

    splits = group_splits(df, "g")
    assert set(splits.keys()) == {"b", "a", None}
    assert splits[None] == [2]


def test_validate_selector_list_strict_raises():
    with pytest.raises(TypeError) as exc_info:
        _validate_selector_list([pl.col("a")])

    msg = "entry 0 is a polars Expr, which is only supported for polars versions >= 0.20.30."
    assert msg in str(exc_info.value.args[0])


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


def test_to_frame(ser: SeriesLike):
    df = to_frame(ser, name="x")

    if isinstance(ser, pl.Series):
        assert_frame_equal(df, pl.DataFrame({"x": [1.0, 2.0, None]}))
    elif isinstance(ser, pd.Series):
        assert_frame_equal(df, pd.DataFrame({"x": [1.0, 2.0, None]}))
    else:
        raise AssertionError(f"Unexpected series type: {type(ser)}")


def test_is_series(ser: SeriesLike):
    assert is_series(ser)


def test_is_series_false():
    assert not is_series(1)


def test_cast_frame_to_string_polars_list_col():
    df = pl.DataFrame({"x": [[1, 2], [3]], "y": [1, None], "z": [{"a": 1}, {"a": 2}]})
    new_df = cast_frame_to_string(df)

    assert new_df["x"].dtype.is_(pl.String)
    assert new_df["y"].dtype.is_(pl.String)
    assert new_df["z"].dtype.is_(pl.String)
