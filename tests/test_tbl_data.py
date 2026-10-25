import builtins
import math
from datetime import date, datetime, time, timedelta, timezone
from decimal import Decimal
from typing import Any, Callable, TypeVar
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import polars as pl
import pyarrow as pa
import pytest
from syrupy.assertion import SnapshotAssertion

from great_tables import GT, loc
from great_tables._tbl_data import (
    Agnostic,
    DataFrameLike,
    SeriesLike,
    _get_cell,
    _get_column_dtype,
    _get_column_levels,
    _is_numeric_dtype,
    _re_version,
    _set_cell,
    _set_cells,
    _validate_selector_list,
    cast_frame_to_string,
    copy_data,
    copy_frame,
    create_empty_frame,
    eval_aggregate,
    eval_select,
    eval_transform,
    get_column_names,
    get_rows,
    group_splits,
    is_na,
    is_series,
    n_rows,
    reorder,
    replace_null_frame,
    to_frame,
    to_list,
    validate_frame,
)
from great_tables._tbl_data_align import classify_dtype_for_alignment
from great_tables._utils_render_html import create_body_component_h
from tests.utils import (
    Backend,
    DataFrameConstructor,
    DataLike,
    SeriesConstructor,
    assert_frame_equal,
    native_backend,
)

params_pl_container_dtypes = [
    pytest.param(pl.List, id="list"),
    pytest.param(pl.Array, id="array"),
]

pandas_ge_v3 = _re_version(pd.__version__) >= (3, 0, 0)

FrameT = TypeVar("FrameT", bound=DataFrameLike)

# One column per dtype, each ending with a missing value. The float column needs a non-integral
# value, or the pandas nullable and pyarrow-backed constructors make it an integer column.
DTYPE_MATRIX: DataLike = {
    "int": [1, 2, None],
    "float": [1.5, -0.0, None],
    "str": ["a", "b", None],
    "bool": [True, False, None],
    "date": [date(2024, 1, 1), date(2024, 2, 29), None],
    "datetime": [datetime(2024, 1, 1, 12, 30), datetime(2024, 2, 29), None],
    "datetime_tz": [
        datetime(2024, 1, 1, 12, 30, tzinfo=timezone.utc),
        datetime(2024, 2, 29, tzinfo=timezone.utc),
        None,
    ],
    "duration": [timedelta(hours=1), timedelta(days=2), None],
    "decimal": [Decimal("1.50"), Decimal("-2.25"), None],
    "list": [[1, 2], [3], None],
}

MATRIX_COLUMNS = [*DTYPE_MATRIX, "categorical", "categorical_ordered"]

IS_NA_SCALARS: dict[str, Any] = {
    "None": None,
    "nan": math.nan,
    "np.float64(nan)": np.float64("nan"),
    "pd.NA": pd.NA,
    "pd.NaT": pd.NaT,
    "0": 0,
    "1.5": 1.5,
    "empty str": "",
    "str": "a",
    "False": False,
    "date": date(2024, 1, 1),
    "Decimal": Decimal("1.5"),
    "list": [1, 2],
    "np.array": np.array([1, 2]),
    "np.array([nan])": np.array([math.nan]),
}

params_set_cells_values: list[dict[int, str | None]] = [
    {1: "x"},
    {2: "z", 0: "x", 1: "y"},
    {0: None, 2: "z"},
    {},
]


def _cast_to_categorical(df: DataFrameLike, column: str, *, ordered: bool) -> DataFrameLike:
    # Python values can't build categorical columns. Ordered categories follow first appearance.
    if isinstance(df, pd.DataFrame):
        categories = df[column].dropna().unique()
        categorical = pd.Categorical(df[column], categories=categories, ordered=ordered)
        return df.assign(**{column: categorical})

    if isinstance(df, pl.DataFrame):
        categories = df[column].drop_nulls().unique(maintain_order=True)
        return df.with_columns(
            pl.col(column).cast(pl.Enum(categories) if ordered else pl.Categorical)
        )

    encoded = df[column].dictionary_encode()
    if ordered:
        encoded = encoded.cast(
            pa.dictionary(encoded.type.index_type, encoded.type.value_type, ordered=True)
        )
    return df.set_column(df.column_names.index(column), column, encoded)


def _column_cells(df: DataFrameLike, column: str) -> list[Any]:
    return [_get_cell(df, row, column) for row in range(n_rows(df))]


def _is_na_or_error(df: Any, x: Any) -> bool | str:
    try:
        return is_na(df, x)
    except Exception as e:
        return type(e).__name__


def _describe(value: Any) -> str:
    # Type name and `str()` hold across library versions, unlike reprs. numpy 2 names its bool
    # scalar "bool", so numpy types get a prefix to tell them from Python's.
    prefix = "np." if isinstance(value, np.generic) else ""
    return f"{prefix}{type(value).__name__}: {value}"


def _describe_column(
    column: str, values: list[Any], constructor: DataFrameConstructor | SeriesConstructor
) -> list[str]:
    described = [_describe(value) for value in values]

    # A missing value in a plain pandas text column is None on pandas 2 (object dtype) and nan on
    # pandas 3 (str dtype), so it's checked here and the snapshot holds on both majors
    plain_pandas = constructor.__name__ in ("pandas_constructor", "pandas_series_constructor")
    if column == "str" and plain_pandas:
        assert described[-1] == ("float: nan" if pandas_ge_v3 else "NoneType: None")
        described[-1] = "None (pandas 2) or nan (pandas 3)"

    return described


def _recorder(calls: list[Any], returns: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def record(arg: Any) -> Any:
        calls.append(arg)
        return returns(arg)

    return record


@pytest.fixture
def df(frame_constructor: DataFrameConstructor) -> DataFrameLike:
    return frame_constructor({"col1": [1, 2, 3], "col2": ["a", "b", "c"], "col3": [4.0, 5.0, 6.0]})


@pytest.fixture
def matrix_df(frame_constructor: DataFrameConstructor) -> DataFrameLike:
    text = DTYPE_MATRIX["str"]
    df = frame_constructor({**DTYPE_MATRIX, "categorical": text, "categorical_ordered": text})
    df = _cast_to_categorical(df, "categorical", ordered=False)
    return _cast_to_categorical(df, "categorical_ordered", ordered=True)


@pytest.fixture
def offset_index_df(pandas_frame_constructor: DataFrameConstructor) -> pd.DataFrame:
    # Index labels that aren't row positions, as after filtering rows
    df = pandas_frame_constructor(
        {"col1": [1, 2, 3], "col2": ["a", "b", "c"], "col3": [4.0, 5.0, 6.0]}
    )
    assert isinstance(df, pd.DataFrame)
    df.index = [3, 7, 9]
    return df


@pytest.fixture(params=params_pl_container_dtypes, scope="function")
def df_container_dtypes(request):
    dtype_constructor = request.param

    if dtype_constructor == pl.List:
        return pl.DataFrame(
            {"col1": [1, 2, 3], "col2": [[1, 2, 3], [4, 5], None], "col3": ["a", "b", "c"]}
        )
    # return a pl df with pl.Array columns
    else:
        col2_as_array = pl.col("col2").cast(pl.Array(pl.Int32, shape=(3,)))
        return pl.DataFrame(
            {
                "col1": [1, 2, 3],
                "col2": [[1, 2, 3], [4, 5, 6], None],
                "col3": ["a", "b", "c"],
            }
        ).with_columns(col2_as_array)


@pytest.fixture
def ser(series_constructor: SeriesConstructor) -> SeriesLike:
    return series_constructor([1.0, 2.0, None])


def test_get_column_names(df: DataFrameLike):
    expected = ["col1", "col2", "col3"]
    assert get_column_names(df) == expected


def test_get_column_names_empty_frame(frame_constructor: DataFrameConstructor):
    assert get_column_names(frame_constructor({"x": []})) == ["x"]


@pytest.mark.parametrize("data, expected", [({"x": [1, 2, 3]}, 3), ({"x": []}, 0)])
def test_n_rows(frame_constructor: DataFrameConstructor, data: DataLike, expected: int):
    assert n_rows(frame_constructor(data)) == expected


def test_get_column_dtypes(df: DataFrameLike):
    col1 = df["col1"]
    assert _get_column_dtype(df, "col1") == getattr(col1, "dtype", getattr(col1, "type", None))


def test_is_numeric_dtype_dtype_matrix(matrix_df: DataFrameLike, snapshot: SnapshotAssertion):
    # `opt_interactive()` passes the values of numeric columns to `float()`, and
    # `cols_align_decimal()` aligns only numeric columns
    # TODO(Unassigned): Update the snapshot once #1020 and #1028 are fixed
    assert snapshot == {col: _is_numeric_dtype(matrix_df, col) for col in MATRIX_COLUMNS}


@pytest.mark.parametrize(
    ("column", "numeric_on", "reason"),
    [
        pytest.param(
            "list",
            {"polars", "pyarrow"},
            "https://github.com/posit-dev/great-tables/issues/1020",
            id="list",
        ),
        pytest.param(
            "categorical",
            {"pyarrow"},
            "https://github.com/posit-dev/great-tables/issues/1028",
            id="categorical",
        ),
    ],
)
def test_is_numeric_dtype_nested_types(
    matrix_df: DataFrameLike,
    column: str,
    numeric_on: set[str],
    reason: str,
    request: pytest.FixtureRequest,
):
    # The dtype name includes the element or index type, e.g. "list(int64)" or
    # "dictionary<values=string, indices=int32, ordered=0>", so it matches "int" and
    # `opt_interactive()` crashes
    if native_backend(matrix_df) in numeric_on:
        request.applymarker(pytest.mark.xfail(strict=True, raises=AssertionError, reason=reason))

    assert not _is_numeric_dtype(matrix_df, column)


def test_is_numeric_dtype_missing_column(df: DataFrameLike):
    assert _is_numeric_dtype(df, "missing") is False


def test_get_column_levels(frame_constructor: DataFrameConstructor):
    # `data_color()` colors an ordered categorical column by its declared levels, not sorted ones
    text = ["b", "a", None]
    df = frame_constructor({"text": text, "unordered": text, "ordered": text})
    df = _cast_to_categorical(df, "unordered", ordered=False)
    df = _cast_to_categorical(df, "ordered", ordered=True)

    levels = {col: _get_column_levels(df, col) for col in get_column_names(df)}
    assert levels == {"text": None, "unordered": None, "ordered": ["b", "a"]}


def test_get_column_levels_pyarrow_chunked():
    # Levels are the non-null union of the chunk dictionaries, in first-seen order
    chunks = [
        pa.DictionaryArray.from_arrays(
            pa.array(indices, pa.int32()), pa.array(dictionary), ordered=True
        )
        for indices, dictionary in [([1, 0], ["b", "a"]), ([0], ["c", None])]
    ]
    df = pa.table({"x": pa.chunked_array(chunks)})
    empty = pa.table({"x": pa.chunked_array([], chunks[0].type)})

    assert _get_column_levels(df, "x") == ["b", "a", "c"]
    assert _get_column_levels(empty, "x") == []


def test_classify_dtype_for_alignment_dtype_matrix(
    matrix_df: DataFrameLike, snapshot: SnapshotAssertion
):
    # GT also right-aligns text columns whose strings all look like numbers, and object columns
    # without strings (#1024), so the final alignment is pinned too
    # TODO(Unassigned): Update the snapshot once #1021 and #1024 are fixed
    result = {
        "classification": {
            col: classify_dtype_for_alignment(matrix_df, col) for col in MATRIX_COLUMNS
        },
        "alignment": {col.var: col.column_align for col in GT(matrix_df)._boxhead._d},
    }

    assert snapshot == result


def test_get_cell_dtype_matrix(
    matrix_df: DataFrameLike, frame_constructor: DataFrameConstructor, snapshot: SnapshotAssertion
):
    # Unformatted cells render as `str()` of these values
    result = {
        col: _describe_column(col, _column_cells(matrix_df, col), frame_constructor)
        for col in get_column_names(matrix_df)
    }

    assert snapshot == result


def test_get_cell_offset_index(offset_index_df: pd.DataFrame):
    # Rows are positions, not index labels
    assert _column_cells(offset_index_df, "col2") == ["a", "b", "c"]


def test_get_cell_container_dtypes(df_container_dtypes: pl.DataFrame):
    "Checks that container dtype entries in polars dfs are returned as lists"
    assert isinstance(_get_cell(df_container_dtypes, 0, "col2"), list)
    assert _get_cell(df_container_dtypes, 2, "col2") is None


def test_set_cell(df: DataFrameLike, frame_constructor: DataFrameConstructor):
    expected_data = {"col1": [1, 2, 3], "col2": ["a", "x", "c"], "col3": [4.0, 5.0, 6.0]}
    expected = frame_constructor(expected_data)

    new_df = _set_cell(df, 1, "col2", "x")
    if new_df is None:
        # Some implementations do in-place modifications
        new_df = df
    assert_frame_equal(new_df, expected)


def _set_cells_with_set_cell(df: FrameT, column: str, values: dict[int, Any]) -> FrameT:
    for row, value in values.items():
        new_df = _set_cell(df, row, column, value)
        if new_df is not None:
            df = new_df
    return df


def test_set_cell_offset_index(offset_index_df: pd.DataFrame):
    # Rows are positions, not index labels
    res = _set_cells_with_set_cell(offset_index_df, "col2", {1: "x"})

    assert _column_cells(res, "col2") == ["a", "x", "c"]
    assert list(res.index) == [3, 7, 9]


@pytest.mark.parametrize("values", params_set_cells_values)
def test_set_cells(df: DataFrameLike, values: dict[int, str | None]):
    expected = _set_cells_with_set_cell(create_empty_frame(df), "col2", values)
    res = _set_cells(create_empty_frame(df), "col2", values)

    assert_frame_equal(res, expected)
    # Unset rows and None stay missing
    cells = _column_cells(res, "col2")
    assert [None if is_na(res, cell) else cell for cell in cells] == [
        values.get(i) for i in range(3)
    ]


@pytest.mark.parametrize("values", params_set_cells_values)
def test_set_cells_offset_index(offset_index_df: pd.DataFrame, values: dict[int, str | None]):
    expected = _set_cells_with_set_cell(create_empty_frame(offset_index_df), "col2", values)

    assert_frame_equal(_set_cells(create_empty_frame(offset_index_df), "col2", values), expected)


@pytest.mark.parametrize("value", [5, 1.5, True])
def test_set_cells_non_strings_as_set_cell(df: DataFrameLike, value):
    # Values that aren't strings are set as `_set_cell()` sets them, which differs by backend
    # (polars casts them to strings, pandas raises for most and PyArrow infers a new dtype)
    values = {0: "x", 2: value}

    try:
        expected = _set_cells_with_set_cell(create_empty_frame(df), "col2", values)
    except Exception as e:
        with pytest.raises(type(e)):
            _set_cells(create_empty_frame(df), "col2", values)
    else:
        assert_frame_equal(_set_cells(create_empty_frame(df), "col2", values), expected)


def test_reorder(df: DataFrameLike, frame_constructor: DataFrameConstructor):
    res = reorder(df, [2, 0], ["col3", "col1"])

    dst = frame_constructor({"col3": [6.0, 4.0], "col1": [3, 1]})

    if isinstance(dst, pd.DataFrame):
        dst.index = pd.Index([2, 0])

    assert_frame_equal(res, dst)


def test_reorder_no_rows(df: DataFrameLike):
    res = reorder(df, [], ["col2"])

    assert n_rows(res) == 0
    assert get_column_names(res) == ["col2"]
    assert _get_column_dtype(res, "col2") == _get_column_dtype(df, "col2")


def test_reorder_offset_index(offset_index_df: pd.DataFrame):
    # Rows are positions, and their index labels move with them
    res = reorder(offset_index_df, [2, 0], ["col2"])

    assert _column_cells(res, "col2") == ["c", "a"]
    assert list(res.index) == [9, 3]


@pytest.mark.parametrize("expr", [["col2", "col1"], [1, 0], ["col2", 0], [1, "col1"]])
def test_eval_select_with_list(df: DataFrameLike, expr):
    sel = eval_select(df, expr)
    assert sel == [("col2", 1), ("col1", 0)]


def test_eval_select_with_callable(df: DataFrameLike):
    def expr(col):
        return col == "col2"

    sel = eval_select(df, expr)
    assert sel == [("col2", 1)]


@pytest.mark.parametrize(
    ("expr", "expected"), [(-1, [("col3", 2)]), ([-1, 0], [("col3", 2), ("col1", 0)])]
)
def test_eval_select_negative_int(
    df: DataFrameLike, expr: int | list[int], expected: list[tuple[str, int]]
):
    assert eval_select(df, expr) == expected


@pytest.mark.parametrize(("expr", "expected"), [("x", []), (["col1", "x"], [("col1", 0)])])
def test_eval_select_unknown_name(
    df: DataFrameLike, expr: str | list[str], expected: list[tuple[str, int]]
):
    # pandas and pyarrow skip names that aren't columns, polars raises
    if native_backend(df) == "polars":
        with pytest.raises(pl.exceptions.ColumnNotFoundError):
            eval_select(df, expr)
    else:
        assert eval_select(df, expr) == expected


def test_polars_columns_callable_in_public_api():
    df = pl.DataFrame({"x1": [1.5], "x2": [2.5], "z": ["a"]})

    html = GT(df).fmt_number(columns=lambda col: col.startswith("x")).as_raw_html()

    assert ">1.50<" in html
    assert ">2.50<" in html
    assert ">a<" in html


def test_polars_columns_callable_keeps_selectors_working():
    df = pl.DataFrame({"x1": [1.5], "z": ["a"]})

    assert eval_select(df, pl.selectors.numeric()) == [("x1", 0)]
    assert eval_select(df, pl.col("z")) == [("z", 1)]


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


@pytest.mark.parametrize(
    "keys, expected",
    [
        (["b", "a", "b", "c"], {"a": [1], "b": [0, 2], "c": [3]}),
        ([2, 1, 2], {1: [1], 2: [0, 2]}),
        ([True, False, True], {False: [1], True: [0, 2]}),
    ],
)
def test_group_splits(
    frame_constructor: DataFrameConstructor, keys: list[Any], expected: dict[Any, list[int]]
):
    splits = group_splits(frame_constructor({"g": keys}), "g")

    # Compared as dicts: polars doesn't keep the group order, and GT orders groups itself
    assert splits == expected
    # A dict can't tell True from 1, and GT labels each group with `str()` of its key
    assert sorted(map(str, splits)) == sorted(map(str, expected))


@pytest.mark.parametrize(
    "keys, expected",
    [
        (["b", None, "a", None], {"a": [2], "b": [0], None: [1, 3]}),
        ([None, None], {None: [0, 1]}),
    ],
)
@pytest.mark.parametrize("categorical", [False, True])
def test_group_splits_null_keys(
    frame_constructor: DataFrameConstructor,
    keys: list[Any],
    expected: dict[Any, list[int]],
    categorical: bool,
    request: pytest.FixtureRequest,
):
    df = frame_constructor({"g": keys})
    if categorical:
        df = _cast_to_categorical(df, "g", ordered=False)

    if categorical and native_backend(df) == "pandas":
        # groupby(dropna=False).indices drops the NaN group of a categorical key
        reason = "pandas drops the rows with a null categorical key"
        request.applymarker(pytest.mark.xfail(strict=True, raises=AssertionError, reason=reason))

    # pandas spells the missing key NaN or NA, which `test_group_splits_null_key_is_none` pins
    splits = {None if is_na(df, key) else key: rows for key, rows in group_splits(df, "g").items()}
    assert splits == expected


def test_render_body_null_group_keys(
    frame_constructor: DataFrameConstructor, request: pytest.FixtureRequest
):
    values = [11, 12, 13, 14, 15]
    df = frame_constructor({"g": ["b", None, "a", None, "b"], "x": values})

    # The missing key breaks rendering on pandas 2 (TypeError) and on pandas 3 nullable dtypes
    # (KeyError on <NA>), while a pandas 3 `str` column spells it nan and renders
    plain_pandas_3 = pandas_ge_v3 and frame_constructor.__name__ == "pandas_constructor"
    if native_backend(df) == "pandas" and not plain_pandas_3:
        reason = "https://github.com/posit-dev/great-tables/issues/1003"
        request.applymarker(
            pytest.mark.xfail(strict=True, raises=(TypeError, KeyError), reason=reason)
        )

    body = create_body_component_h(GT(df, groupname_col="g")._build_data("html"))

    assert [value for value in values if f">{value}<" not in body] == []


def test_render_null_group_keys_pyarrow_matches_polars():
    data = {"g": ["b", None, "a", None, "b"], "x": [1, 2, 3, 4, 5]}

    # The table id is random unless pinned
    html_pa = GT(pa.table(data), groupname_col="g", id="t").as_raw_html()
    html_pl = GT(pl.DataFrame(data), groupname_col="g", id="t").as_raw_html()

    assert html_pa == html_pl


@pytest.mark.xfail(
    strict=True,
    raises=AssertionError,
    reason="https://github.com/posit-dev/great-tables/issues/1003",
    # TODO(Unassigned): Remove entire test once the issue is fixed
)
def test_group_splits_null_key_is_none(pandas_frame_constructor: DataFrameConstructor):
    assert None in group_splits(pandas_frame_constructor({"g": ["b", None]}), "g")


def test_group_splits_offset_index(offset_index_df: pd.DataFrame):
    # Rows are positions, not index labels
    assert group_splits(offset_index_df, "col2") == {"a": [0], "b": [1], "c": [2]}


def test_group_splits_pd_na():
    df = pd.DataFrame({"g": ["b", "a", None]})

    splits = group_splits(df, "g")
    assert len(splits.keys()) == 3
    nan_key = [k for k in splits if isinstance(k, float) and math.isnan(k)][0]

    assert splits[nan_key] == [2]


def test_validate_selector_list_strict_raises():
    with pytest.raises(TypeError) as exc_info:
        _validate_selector_list([pl.col("a")])

    msg = "entry 0 is a polars Expr, which is only supported for polars versions >= 0.20.30."
    assert msg in str(exc_info.value.args[0])


@pytest.mark.parametrize("row_count", [3, 0])
def test_create_empty_frame(df: DataFrameLike, row_count: int):
    res = create_empty_frame(df[:row_count])
    col = [None] * row_count

    if isinstance(res, pd.DataFrame):
        dst = pd.DataFrame({"col1": col, "col2": col, "col3": col}, dtype="string")
    elif isinstance(res, pl.DataFrame):
        dst = pl.DataFrame({"col1": col, "col2": col, "col3": col}).cast(pl.Utf8)
    elif isinstance(res, pa.Table):
        dst = pa.table(
            {"col1": col, "col2": col, "col3": col},
            schema=pa.schema(
                (
                    pa.field("col1", pa.string()),
                    pa.field("col2", pa.string()),
                    pa.field("col3", pa.string()),
                )
            ),
        )
    else:
        raise ValueError(f"Unsupported data type: {type(res)}")

    assert_frame_equal(res, dst)


def test_create_empty_frame_offset_index(offset_index_df: pd.DataFrame):
    assert list(create_empty_frame(offset_index_df).index) == [3, 7, 9]


def test_replace_null_frame(matrix_df: DataFrameLike):
    # GT fills the body cells that no formatter set with the original data cast to strings
    str_data = cast_frame_to_string(matrix_df)
    body = _set_cells(create_empty_frame(matrix_df), "str", {0: "x", 2: "z"})

    res = replace_null_frame(body, str_data)

    expected = {col: to_list(str_data[col]) for col in MATRIX_COLUMNS}
    expected["str"] = ["x", "b", "z"]
    assert {col: to_list(res[col]) for col in MATRIX_COLUMNS} == expected


def test_replace_null_frame_offset_index(offset_index_df: pd.DataFrame):
    # pandas fills by index label, which works because GT builds both frames from the same data
    body = _set_cells(create_empty_frame(offset_index_df), "col2", {0: "x"})

    res = replace_null_frame(body, cast_frame_to_string(offset_index_df))

    assert _column_cells(res, "col2") == ["x", "b", "c"]
    assert list(res.index) == [3, 7, 9]


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


def test_validate_frame_passthrough(df: DataFrameLike, recwarn: pytest.WarningsRecorder):
    assert validate_frame(df) is df

    is_pyarrow = native_backend(df) == "pyarrow"
    expected = ["PyArrow Table support is currently experimental."] if is_pyarrow else []
    assert [str(w.message) for w in recwarn] == expected


def test_is_series(ser: SeriesLike):
    assert is_series(ser)


def test_is_series_false():
    assert not is_series(1)


def test_to_list_dtype_matrix(series_constructor: SeriesConstructor, snapshot: SnapshotAssertion):
    # `data_color(fn=...)` gets these values
    result = {
        col: _describe_column(col, to_list(series_constructor(values)), series_constructor)
        for col, values in DTYPE_MATRIX.items()
    }

    assert snapshot == result


@pytest.mark.parametrize("column", list(DTYPE_MATRIX))
def test_to_frame_dtype_matrix(
    series_constructor: SeriesConstructor,
    paired_frame_constructor: DataFrameConstructor,
    column: str,
):
    # A series makes the same frame as its values would
    values = DTYPE_MATRIX[column]
    expected = paired_frame_constructor({column: values})

    assert_frame_equal(to_frame(series_constructor(values), name=column), expected)


@pytest.mark.parametrize("indexes, expected", [([2, 0], [3.5, 1.5]), ([], [])])
def test_get_rows(series_constructor: SeriesConstructor, indexes: list[int], expected: list[float]):
    ser = series_constructor([1.5, 2.5, 3.5])
    assert to_list(get_rows(ser, indexes)) == expected


def test_get_rows_offset_index(offset_index_df: pd.DataFrame):
    # Rows are positions, not index labels
    assert to_list(get_rows(offset_index_df["col2"], [2, 0])) == ["c", "a"]


def test_cast_frame_to_string_polars_list_col():
    df = pl.DataFrame({"x": [[1, 2], [3]], "y": [1, None], "z": [{"a": 1}, {"a": 2}]})
    new_df = cast_frame_to_string(df)

    assert new_df["x"].dtype.is_(pl.String)
    assert new_df["y"].dtype.is_(pl.String)
    assert new_df["z"].dtype.is_(pl.String)


def test_cast_frame_to_string_list_col(frame_constructor: DataFrameConstructor):
    """List cells are spelled as Python spells them, whichever backend built the table."""
    df = frame_constructor({"x": [[1, 2], [3], None]})

    assert to_list(cast_frame_to_string(df)["x"]) == ["[1, 2]", "[3]", None]


def test_cast_frame_to_string_dtype_matrix(matrix_df: DataFrameLike, snapshot: SnapshotAssertion):
    # Only body cells still missing at render time get these strings; unformatted cells already
    # hold `str()` of their value
    res = cast_frame_to_string(matrix_df)

    assert snapshot == {col: to_list(res[col]) for col in get_column_names(res)}


def test_cast_frame_to_string_nan(
    frame_constructor: DataFrameConstructor, snapshot: SnapshotAssertion
):
    # polars and pyarrow keep NaN apart from null, so GT renders the string NaN gets here
    df = frame_constructor({"x": [1.5, math.nan, None]})

    assert snapshot == to_list(cast_frame_to_string(df)["x"])


def test_cast_frame_to_string_pyarrow_struct_col():
    # pyarrow can't cast nested types to strings. polars spells structs "{1}" instead
    df = pa.table({"x": [{"a": 1}, {"a": 2}, None]})

    assert cast_frame_to_string(df)["x"].to_pylist() == ["{'a': 1}", "{'a': 2}", None]


@pytest.mark.parametrize("column", MATRIX_COLUMNS)
def test_is_na_dtype_matrix(matrix_df: DataFrameLike, column: str):
    # `is_na()` must recognize each backend's own missing value (None, nan, NaT or NA) in every dtype
    cells = _column_cells(matrix_df, column)

    assert [is_na(matrix_df, cell) for cell in cells] == [False, False, True]


def test_is_na_scalars(df: DataFrameLike, snapshot: SnapshotAssertion):
    # A cell holding an array or a list isn't missing, even if its elements are. pandas scalars
    # can't come out of a polars or pyarrow frame: polars says they aren't missing, pyarrow raises
    assert snapshot == {name: _is_na_or_error(df, x) for name, x in IS_NA_SCALARS.items()}


def test_is_na_agnostic(snapshot: SnapshotAssertion):
    assert snapshot == {name: _is_na_or_error(Agnostic(), x) for name, x in IS_NA_SCALARS.items()}


def test_values_handed_to_user_callables(
    frame_constructor: DataFrameConstructor, snapshot: SnapshotAssertion
):
    # User functions get the backend's own scalars, missing ones included (pandas NaN, NaT and NA,
    # polars and pyarrow None); changing them breaks user code, e.g. `x < 100` raises on None
    data = {
        "int": [1, None],
        "float": [1.5, None],
        "str": ["a", None],
        "datetime": [datetime(2024, 1, 1, 12, 30), None],
    }
    gt = GT(frame_constructor(data))

    result: dict[str, dict[str, list[str]]] = {"fmt": {}, "data_color": {}, "text_transform": {}}
    for col in data:
        fmt_args: list[Any] = []
        color_args: list[Any] = []
        text_args: list[Any] = []

        gt.fmt(_recorder(fmt_args, lambda x: ""), columns=col).as_raw_html()
        gt.data_color(
            columns=col, fn=_recorder(color_args, lambda xs: [None] * len(xs))
        ).as_raw_html()
        gt.text_transform(loc.body(columns=col), _recorder(text_args, lambda x: x)).as_raw_html()

        # `data_color()` calls `fn` once, with the whole column as a list
        [column_values] = color_args
        assert type(column_values) is list

        result["fmt"][col] = _describe_column(col, fmt_args, frame_constructor)
        result["data_color"][col] = _describe_column(col, column_values, frame_constructor)
        # `text_transform()` gets the rendered text of non-missing cells
        result["text_transform"][col] = [_describe(arg) for arg in text_args]

    assert snapshot == result


def test_pandas_array_cells_render():
    df = pd.DataFrame({"x": [np.array([1, 2]), np.array([3])], "y": [[1, 2], [3]]})

    html = GT(df).as_raw_html()
    assert ">[1 2]</td>" in html
    assert ">[1, 2]</td>" in html

    assert "[1 2] & [1, 2]" in GT(df).as_latex()


def test_frame_rendering(df: DataFrameLike, snapshot):
    gt = GT(df).fmt_number(columns="col3", decimals=0).fmt_currency(columns="col1")
    assert create_body_component_h(gt._build_data("html")) == snapshot


@pytest.mark.parametrize("copy", [copy_data, copy_frame])
def test_copy_keeps_dtypes(
    matrix_df: DataFrameLike, copy: Callable[[DataFrameLike], DataFrameLike]
):
    if copy is copy_frame and isinstance(matrix_df, pa.Table):
        # pa.array() can't rebuild a chunked list column holding a null.
        # NOTE: GT never calls copy_frame()
        with pytest.raises(TypeError):
            copy_frame(matrix_df)
        matrix_df = matrix_df.drop_columns("list")

    res = copy(matrix_df)

    assert res is not matrix_df
    assert_frame_equal(res, matrix_df)


@pytest.mark.parametrize("copy", [copy_data, copy_frame])
def test_copy_is_independent(df: DataFrameLike, copy: Callable[[DataFrameLike], DataFrameLike]):
    # GT sets formatted cells on a copy of the body, in place for pandas and polars
    body = create_empty_frame(df)

    _set_cells(copy(body), "col2", {0: "x"})

    assert all(is_na(body, cell) for cell in _column_cells(body, "col2"))


def test_eval_aggregate_pandas(df: DataFrameLike):
    def expr(df):
        return pd.Series({"col1_sum": sum(df["col1"]), "col3_max": max(df["col3"])})

    # Only pandas supports callable aggregation expressions
    if isinstance(df, pl.DataFrame):
        with pytest.raises(TypeError) as exc_info:
            eval_aggregate(df, expr)
        assert "cannot create expression literal for value of type function" in str(
            exc_info.value.args[0]
        )
        return

    if isinstance(df, pa.Table):
        with pytest.raises(TypeError) as exc_info:
            eval_aggregate(df, expr)
        assert "unsupported operand type(s)" in str(exc_info.value.args[0])
        return

    result = eval_aggregate(df, expr)
    assert result == {"col1_sum": 6, "col3_max": 6.0}


@pytest.mark.parametrize(
    "expr,expected",
    [
        (pl.col("col1").sum(), {"col1": 6}),
        (pl.col("col2").first(), {"col2": "a"}),
        (pl.col("col3").max(), {"col3": 6.0}),
    ],
)
def test_eval_aggregate_polars(df: DataFrameLike, expr, expected):
    # Only polars supports polars expression aggregations
    if not isinstance(df, pl.DataFrame):
        with pytest.raises(TypeError) as exc_info:
            eval_aggregate(df, expr)
        assert "'Expr' object is not callable" in str(exc_info.value.args[0])
        return

    result = eval_aggregate(df, expr)
    assert result == expected


def test_eval_aggregate_with_nulls(frame_constructor: DataFrameConstructor):
    df = frame_constructor({"a": [1, None, 3]})

    if isinstance(df, pd.DataFrame):

        def expr(df):
            return pd.Series({"a": df["a"].sum()})

    if isinstance(df, pl.DataFrame):
        expr = pl.col("a").sum()

    if isinstance(df, pa.Table):

        def expr(tbl):
            s = pa.compute.sum(tbl.column("a"))
            return pa.table({"a": [s.as_py()]})

    result = eval_aggregate(df, expr)
    assert result == {"a": 4}


def test_eval_aggregate_pandas_raises():
    df = pd.DataFrame({"a": [1, 2, 3]})

    def expr(df):
        return {"a": df["a"].sum()}

    with pytest.raises(ValueError) as exc_info:
        eval_aggregate(df, expr)
    assert "Result must be a pandas Series" in str(exc_info.value)


def test_eval_aggregate_polars_raises():
    df = pl.DataFrame({"a": [1, 2, 3]})
    expr = pl.col("a")

    with pytest.raises(ValueError) as exc_info:
        eval_aggregate(df, expr)
    assert "Expression must produce exactly 1 row" in str(exc_info.value)


def test_eval_aggregate_pyarrow_raises1():
    df = pa.table({"a": [1, 2, 3]})

    def expr(tbl):
        s = pa.compute.sum(tbl.column("a"))
        return {"a": [s.as_py()]}

    with pytest.raises(ValueError) as exc_info:
        eval_aggregate(df, expr)
    assert "Result must be a PyArrow Table" in str(exc_info.value)


def test_eval_aggregate_pyarrow_raises2():
    df = pa.table({"a": [1, 2, 3]})

    def expr(tbl):
        return pa.table({"a": tbl.column("a")})

    with pytest.raises(ValueError) as exc_info:
        eval_aggregate(df, expr)
    assert "Expression must produce exactly 1 row (aggregation)" in str(exc_info.value)


def test_eval_transform(df: DataFrameLike):
    if isinstance(df, pd.DataFrame):

        def expr(df):
            return df["col1"] > 1

    if isinstance(df, pl.DataFrame):
        expr = pl.col("col1") > 1

    if isinstance(df, pa.Table):

        def expr(tbl):
            # a ChunkedArray, since Table columns are chunked
            return pa.compute.greater(tbl["col1"], 1)

    assert eval_transform(df, expr) == [False, True, True]


def test_eval_transform_pyarrow_array():
    df = pa.table({"a": [1, 2, 3]})

    def expr(tbl):
        return pa.compute.greater(tbl["a"], 1).combine_chunks()

    assert eval_transform(df, expr) == [False, True, True]


def test_eval_transform_wrong_type_raises(df: DataFrameLike):
    # polars evaluates the list as one literal expression per item, all named "literal"
    expected_error: dict[Backend, tuple[type[Exception], str]] = {
        "pandas": (ValueError, "Result must be a pandas Series"),
        "polars": (pl.exceptions.DuplicateError, "literal"),
        "pyarrow": (ValueError, "Result must be an Arrow Array or ChunkedArray"),
    }
    error_type, pattern = expected_error[native_backend(df)]

    with pytest.raises(error_type, match=pattern):
        eval_transform(df, lambda _: [False, True, True])


def test_eval_transform_wrong_length_raises(df: DataFrameLike):
    with pytest.raises(ValueError, match=r"Input data: 3\.\nResult: 2\."):
        eval_transform(df, lambda data: data["col1"][:2])


def test_eval_transform_polars_multiple_columns_raises():
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

    with pytest.raises(ValueError, match="Result must be a single column. Received 2 columns."):
        eval_transform(df, pl.col("a", "b") > 1)


def test_is_na_singledispatch_fallback_raises():
    fallback = is_na.dispatch(object)
    with pytest.raises(NotImplementedError, match="Unsupported type"):
        fallback("not_a_dataframe", None)


def test_eval_select_singledispatch_fallback_raises():
    fallback = eval_select.dispatch(object)
    with pytest.raises(NotImplementedError, match="Unsupported type"):
        fallback("not_a_dataframe", ["col"])


def test_pyarrow_validate_frame_duplicate_columns_raises():
    # ValueError when PyArrow table has duplicate column names
    import pyarrow as pa

    tbl = pa.table({"x": [1, 2], "y": [3, 4]})

    # Manually create a table with duplicate column names (PyArrow allows this)
    dup_tbl = pa.table([pa.array([1, 2]), pa.array([3, 4])], names=["x", "x"])
    with pytest.raises(ValueError, match="Column names must be unique"):
        validate_frame(dup_tbl)


def test_to_frame_list_without_name_raises():
    # ValueError when converting list to frame without specifying name
    with pytest.raises(ValueError, match="name must be specified"):
        to_frame([1, 2, 3], name=None)


_UTC_M5 = timezone(timedelta(hours=-5))
_NEW_YORK = ZoneInfo("America/New_York")
_TOKYO = ZoneInfo("Asia/Tokyo")


@pytest.mark.parametrize(
    "vals, dtype",
    [
        ([1, 2], pl.Int64),
        ([1, 2.5], pl.Float64),
        ([1.0, float("nan")], pl.Float64),
        ([1.5, None], pl.Float64),
        ([2**64], pl.Int128),
        (["a", None], pl.String),
        ([date(2000, 2, 29)], pl.Date),
        ([datetime(2000, 2, 29, 23, 30)], pl.Datetime("us")),
        ([datetime(2000, 2, 29, 23, 30, tzinfo=timezone.utc)], pl.Datetime("us", "UTC")),
        ([datetime(2000, 2, 29, 23, 30, tzinfo=_NEW_YORK)], pl.Datetime("us", "America/New_York")),
        ([time(14, 35)], pl.Time),
    ],
)
def test_to_frame_list_keeps_inferred_dtype(vals, dtype):
    df = to_frame(vals, name="x")

    assert df.schema["x"] == dtype


@pytest.mark.parametrize(
    "vals",
    [
        # too big for any integer type (polars makes them null)
        pytest.param([10**40], id="big-int"),
        pytest.param([1, 10**40], id="int-and-big-int"),
        # a fixed UTC offset (polars converts it to UTC)
        pytest.param([datetime(2000, 2, 29, 23, 30, tzinfo=_UTC_M5)], id="fixed-offset"),
        # datetimes in different time zones, or naive and aware ones (polars raises)
        pytest.param(
            [datetime(2000, 2, 29, 23, 30, tzinfo=_NEW_YORK), datetime(2000, 2, 29, tzinfo=_TOKYO)],
            id="two-zones",
        ),
        pytest.param(
            [datetime(2000, 2, 29), datetime(2000, 2, 29, tzinfo=timezone.utc)],
            id="naive-and-aware",
        ),
        # an aware time (polars drops the zone)
        pytest.param([time(14, 35, tzinfo=_UTC_M5)], id="aware-time"),
        # numbers that are changed by the type they're given
        pytest.param([True, 2], id="bool-and-int"),
        pytest.param([np.int64(3), np.float64(1.5)], id="numpy-int-and-float"),
        pytest.param([0.25, Decimal("0.1")], id="float-and-decimal"),
        pytest.param([1.5, "a"], id="float-and-str"),
    ],
)
def test_to_frame_list_keeps_values_polars(vals):
    df = to_frame(vals, name="x")

    assert isinstance(df, pl.DataFrame)
    assert df.schema["x"] == pl.Object
    assert df["x"].to_list() == vals


@pytest.fixture
def no_polars_import(monkeypatch: pytest.MonkeyPatch):
    # polars stays loaded for the data backends; only `import polars` in `to_frame()` fails
    real_import = builtins.__import__

    def fake_import(name, *args, **kwargs):
        if name == "polars":
            raise ImportError(name)
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", fake_import)


@pytest.mark.parametrize(
    "vals, dtype",
    [
        ([1, 2], "int64"),
        ([1.5, None], "float64"),
        ([datetime(2000, 2, 29), None], "datetime64[us]"),
        ([datetime(2000, 2, 29, 23, 30, tzinfo=_UTC_M5)], "datetime64[us, UTC-05:00]"),
        ([10**40], "object"),
        ([True, 2], "object"),
        ([datetime(2000, 2, 29), datetime(2000, 2, 29, tzinfo=timezone.utc)], "object"),
    ],
)
@pytest.mark.usefixtures("no_polars_import")
def test_to_frame_list_keeps_values_pandas(vals, dtype):
    df = to_frame(vals, name="x")

    assert isinstance(df, pd.DataFrame)
    # pandas 3 stores datetimes in microseconds, and pandas 2 (the last for Python 3.10) in
    # nanoseconds
    assert str(df["x"].dtype).replace("[ns", "[us") == dtype

    if dtype == "object":
        assert df["x"].tolist() == vals


def test_cast_frame_to_string_is_consistent_across_backends(
    frame_constructor: DataFrameConstructor,
):
    """A cell must read the same no matter which dataframe library built the table.

    pandas spelled missing values `<NA>` while polars and pyarrow spelled them `None`,
    and polars and pyarrow spelled booleans `true`/`false` while pandas spelled them
    `True`/`False`. See #875.
    """
    df = frame_constructor({"flag": [True, False, None], "txt": ["true", "false", None]})

    res = cast_frame_to_string(df)

    assert to_list(res["flag"]) == ["True", "False", None]
    # a string column that happens to spell "true" is left alone
    assert to_list(res["txt"]) == ["true", "false", None]


def test_cast_frame_to_string_drops_the_sign_on_zero(frame_constructor: DataFrameConstructor):
    """-0.0 is a floating point detail that should not reach a rendered table."""
    df = frame_constructor({"x": [-0.0, 0.0, -1.5]})

    res = cast_frame_to_string(df)
    col = to_list(res["x"])

    assert not col[0].startswith("-")
    assert col[0] == col[1]
    # a genuinely negative value keeps its sign
    assert col[2].startswith("-")


def test_render_body_is_consistent_across_backends(frame_constructor: DataFrameConstructor):
    """The rendered cells for booleans and missing values do not depend on the backend."""
    gt = GT(frame_constructor({"flag": [True, False, None]}))

    body = create_body_component_h(gt._build_data("html"))

    assert ">True<" in body
    assert ">False<" in body
    assert ">None<" in body
    assert "<NA>" not in body


def test_render_body_list_column(frame_constructor: DataFrameConstructor):
    """List cells render as Python spells them, whichever backend built the table."""
    gt = GT(frame_constructor({"l": [[1, 2], [3], None]}))

    body = create_body_component_h(gt._build_data("html"))

    assert ">[1, 2]<" in body
    assert ">[3]<" in body
    assert ">None<" in body


@pytest.mark.parametrize(
    "dtype, expected",
    [("Int64", ["1", None, "0"]), ("Float64", ["1.0", None, "0.0"])],
)
def test_cast_frame_to_string_pandas_nullable_missing(dtype: str, expected: list):
    """Missing values in nullable pandas columns must not be rendered as zero."""
    df = pd.DataFrame({"x": pd.array([1, None, 0], dtype=dtype)})

    res = cast_frame_to_string(df)

    assert to_list(res["x"]) == expected


@pytest.mark.parametrize(
    "fmt", ["fmt_number", "fmt_integer", "fmt_percent", "fmt_scientific", "fmt_currency"]
)
def test_pyarrow_nan_in_formatted_float_column(fmt: str):
    """A NaN (not null) in a float column used to raise ArrowTypeError when the formatter output was set."""
    gt = GT(pa.table({"x": pa.array([1.0, float("nan"), 2.5])}))

    html = getattr(gt, fmt)("x").as_raw_html()

    # the NaN is shown as polars shows it, and the other cells are still formatted
    assert ">NaN<" in html
    assert html.count("NaN") == 1


def test_pyarrow_set_cells_nan_in_a_string_column():
    data = pa.table({"x": pa.array(["a", "b", "c"])})

    res = _set_cells(data, "x", {0: "1.00", 1: float("nan"), 2: None})

    assert res.column("x").to_pylist() == ["1.00", "NaN", None]
