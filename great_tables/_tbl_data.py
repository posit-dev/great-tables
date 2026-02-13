from __future__ import annotations

import re
import warnings
from functools import singledispatch
from typing import TYPE_CHECKING, Any, Callable, Optional, Union

from typing_extensions import TypeAlias

from ._databackend import AbstractBackend

# Define databackend types ----
# These are resolved lazily (e.g. on isinstance checks) when run dynamically,
# or imported directly during type checking.

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd
    import polars as pl
    import pyarrow as pa

    # backwards compatible import of polars Selector type
    try:
        from polars.selectors import Selector
    except ImportError:
        from polars.selectors import _selector_proxy_ as Selector

    PdDataFrame = pd.DataFrame
    PlDataFrame = pl.DataFrame
    PyArrowTable = pa.Table

    PlSelectExpr = Selector
    PlExpr = pl.Expr

    PdSeries = pd.Series
    PlSeries = pl.Series
    PyArrowArray = pa.Array
    PyArrowChunkedArray = pa.ChunkedArray

    PdNA = pd.NA
    PlNull = pl.Null

    NpNan = np.nan
    NpInteger = np.integer

    DataFrameLike = Union[PdDataFrame, PlDataFrame, PyArrowTable]
    SeriesLike = Union[PdSeries, PlSeries, PyArrowArray, PyArrowChunkedArray]
    TblData = DataFrameLike

else:
    from abc import ABC

    # we just need this as a static type hint, but singledispatch tries to resolve
    # any hints at runtime. So we need some value for it.
    from typing import Any as Selector

    class PdDataFrame(AbstractBackend):
        _backends = [("pandas", "DataFrame")]

    class PlDataFrame(AbstractBackend):
        _backends = [("polars", "DataFrame")]

    class PyArrowTable(AbstractBackend):
        _backends = [("pyarrow", "Table")]

    class PlSelectExpr(AbstractBackend):
        _backends = [("polars.selectors", "_selector_proxy_"), ("polars.selectors", "Selector")]
        _strict = False

    class PlExpr(AbstractBackend):
        _backends = [("polars", "Expr")]

    class PdSeries(AbstractBackend):
        _backends = [("pandas", "Series")]

    class PlSeries(AbstractBackend):
        _backends = [("polars", "Series")]

    class PyArrowArray(AbstractBackend):
        _backends = [("pyarrow", "Array")]

    class PyArrowChunkedArray(AbstractBackend):
        _backends = [("pyarrow", "ChunkedArray")]

    class PdNA(AbstractBackend):
        _backends = [("pandas", "NA")]

    class PlNull(AbstractBackend):
        _backends = [("polars", "Null")]

    class NpNan(AbstractBackend):
        _backends = [("numpy", "nan")]

    class NpInteger(AbstractBackend):
        _backends = [("numpy", "integer")]

    # TODO: these types are imported throughout gt, so we need to either put
    # those imports under TYPE_CHECKING, or continue to make available dynamically here.
    class DataFrameLike(ABC):
        """Represent some DataFrame"""

    class SeriesLike(ABC):
        """Represent some Series"""

    DataFrameLike.register(PdDataFrame)
    DataFrameLike.register(PlDataFrame)
    DataFrameLike.register(PyArrowTable)
    SeriesLike.register(PdSeries)
    SeriesLike.register(PlSeries)
    SeriesLike.register(PyArrowArray)
    SeriesLike.register(PyArrowChunkedArray)

    TblData = DataFrameLike


# utils ----


def _raise_not_implemented(data: Any):
    raise NotImplementedError(f"Unsupported data type: {type(data)}")


def _raise_pandas_required(msg: Any):
    raise ImportError(msg)


def _re_version(raw_version: str) -> tuple[int, int, int]:
    """Return a semver-like version string as a 3-tuple of integers.

    Note two important caveats: (1) separators like dev are dropped (e.g. "3.2.1dev3" -> (3, 2, 1)),
    and (2) it simply integer converts parts (e.g. "3.2.0001" -> (3,2,1)).
    """

    # Note two major caveats
    regex = r"(?P<major>\d+)\.(?P<minor>\d+).(?P<patch>\d+)"
    return tuple(map(int, re.match(regex, raw_version).groups()))


class Agnostic:
    """This class dispatches a generic in a DataFrame agnostic way.

    It is available for generics like is_na.
    """


# generic functions ----


# copy_data ----
@singledispatch
def copy_data(data: DataFrameLike) -> DataFrameLike:
    """Copy the stored table data"""
    _raise_not_implemented(data)


@copy_data.register(PdDataFrame)
def _(data: PdDataFrame):
    return data.copy()


@copy_data.register(PlDataFrame)
def _(data: PlDataFrame):
    return data.clone()


@copy_data.register(PyArrowTable)
def _(data: PyArrowTable):
    import pyarrow as pa

    return pa.table(data)


# get_column_names ----
@singledispatch
def get_column_names(data: DataFrameLike) -> list[str]:
    """Get a list of column names from the input data table"""
    _raise_not_implemented(data)


@get_column_names.register(PdDataFrame)
def _(data: PdDataFrame):
    return data.columns.tolist()


@get_column_names.register(PlDataFrame)
def _(data: PlDataFrame):
    return data.columns


@get_column_names.register(PyArrowTable)
def _(data: PyArrowTable):
    return data.column_names


# n_rows ----


@singledispatch
def n_rows(data: DataFrameLike) -> int:
    """Get the number of rows from the input data table"""
    raise _raise_not_implemented(data)


@n_rows.register(PdDataFrame)
@n_rows.register(PlDataFrame)
def _(data: Any) -> int:
    return len(data)


@n_rows.register(PyArrowTable)
def _(data: PyArrowTable) -> int:
    return data.num_rows


# _get_cell ----


@singledispatch
def _get_cell(data: DataFrameLike, row: int, column: str) -> Any:
    """Get the content from a single cell in the input data table"""

    _raise_not_implemented(data)


@_get_cell.register(PlDataFrame)
def _(data: Any, row: int, column: str) -> Any:
    import polars as pl

    # if container dtype, convert pl.Series to list
    if isinstance(data[column].dtype, (pl.List, pl.Array)):
        return data[column][row].to_list()

    return data[column][row]


@_get_cell.register(PdDataFrame)
def _(data: Any, row: int, col: str) -> Any:
    col_ii = data.columns.get_loc(col)

    if not isinstance(col_ii, int):
        raise ValueError("Column named " + col + " matches multiple columns.")

    return data.iloc[row, col_ii]


@_get_cell.register(PyArrowTable)
def _(data: PyArrowTable, row: int, column: str) -> Any:
    return data.column(column)[row].as_py()


# _set_cell ----


@singledispatch
def _set_cell(data: DataFrameLike, row: int, column: str, value: Any):
    _raise_not_implemented(data)


@_set_cell.register(PdDataFrame)
def _(data, row: int, column: str, value: Any) -> None:
    # TODO: This assumes column names are unique
    # if this is violated, get_loc will return a mask
    col_indx = data.columns.get_loc(column)
    data.iloc[row, col_indx] = value


@_set_cell.register(PlDataFrame)
def _(data, row: int, column: str, value: Any) -> None:
    data[row, column] = value


@_set_cell.register(PyArrowTable)
def _(data: PyArrowTable, row: int, column: str, value: Any) -> PyArrowTable:
    import pyarrow as pa

    colindex = data.column_names.index(column)
    col = data.column(column)
    pylist = col.to_pylist()
    pylist[row] = value
    data = data.set_column(colindex, column, pa.array(pylist))
    return data


# _get_column_dtype ----


@singledispatch
def _get_column_dtype(data: DataFrameLike, column: str) -> Any:
    """Get the data type for a single column in the input data table"""
    return data[column].dtype


@_get_column_dtype.register(PyArrowTable)
def _(data: PyArrowTable, column: str) -> Any:
    return data.column(column).type


# reorder ----


@singledispatch
def reorder(data: DataFrameLike, rows: list[int], columns: list[str]) -> DataFrameLike:
    """Return a re-ordered DataFrame."""
    _raise_not_implemented(data)


@reorder.register
def _(data: PdDataFrame, rows: list[int], columns: list[str]) -> PdDataFrame:
    # note that because loc is label based, we need
    # reset index to allow us to use integer indexing on the rows
    # note that this means the index is not preserved when reordering pandas
    return data.iloc[rows, :].loc[:, columns]


@reorder.register
def _(data: PlDataFrame, rows: list[int], columns: list[str]) -> PlDataFrame:
    return data[rows, columns]


@reorder.register
def _(data: PyArrowTable, rows: list[int], columns: list[str]) -> PyArrowTable:
    return data.select(columns).take(rows)


# group_splits ----
@singledispatch
def group_splits(data: DataFrameLike, group_key: str) -> dict[Any, list[int]]:
    raise NotImplementedError(f"Unsupported data type: {type(data)}")


@group_splits.register
def _(data: PdDataFrame, group_key: str) -> dict[Any, list[int]]:
    g_df = data.groupby(group_key, dropna=False)
    return {k: list(v) for k, v in g_df.indices.items()}


@group_splits.register
def _(data: PlDataFrame, group_key: str) -> dict[Any, list[int]]:
    # TODO: should ensure row count name isn't already in data
    import polars as pl

    # with_row_index supersedes with_row_count
    meth_row_number = getattr(data, "with_row_index", None)
    if not meth_row_number:
        meth_row_number = data.with_row_count

    groups = meth_row_number("__row_count__").group_by(group_key).agg(pl.col("__row_count__"))

    res = dict(zip(groups[group_key].to_list(), groups["__row_count__"].to_list()))
    return res


@group_splits.register
def _(data: PyArrowTable, group_key: str) -> dict[Any, list[int]]:
    import pyarrow.compute as pc

    group_col = data.column(group_key)
    encoded = group_col.dictionary_encode().combine_chunks()

    d = {}
    for idx, group_key in enumerate(encoded.dictionary):
        mask = pc.equal(encoded.indices, idx)
        d[group_key.as_py()] = pc.indices_nonzero(mask).to_pylist()
    return d


# eval_select ----

SelectExpr: TypeAlias = Union[
    str,
    list[str],
    int,
    list[int],
    list["str | int"],
    PlSelectExpr,
    list[PlSelectExpr],
    Callable[[str], bool],
    None,
]
_NamePos: TypeAlias = list[tuple[str, int]]


@singledispatch
def eval_select(data: DataFrameLike, expr: SelectExpr, strict: bool = True) -> _NamePos:
    """Return a list of column names selected by expr."""

    raise NotImplementedError(f"Unsupported type: {type(expr)}")


@eval_select.register
def _(
    data: PdDataFrame,
    expr: Union[list[Union[str, int]], Callable[[str], bool]],
    strict: bool = True,
) -> _NamePos:
    if isinstance(expr, (str, int)):
        expr = [expr]

    if isinstance(expr, list):
        return _eval_select_from_list(list(data.columns), expr)
    elif callable(expr):
        # TODO: currently, we call on each string, but we could be calling on
        # pd.DataFrame.columns instead (which would let us use pandas .str methods)
        col_pos = {k: ii for ii, k in enumerate(list(data.columns))}
        return [(col, col_pos[col]) for col in data.columns if expr(col)]

    raise NotImplementedError(f"Unsupported selection expr: {expr}")


@eval_select.register
def _(data: PlDataFrame, expr: Union[list[str], PlSelectExpr], strict: bool = True) -> _NamePos:
    import polars as pl
    import polars.selectors as cs
    from polars import Expr

    from ._utils import OrderedSet

    pl_version = _re_version(pl.__version__)
    expand_opts = {"strict": False} if pl_version >= (0, 20, 30) else {}

    if isinstance(expr, (str, int)):
        expr = [expr]

    if isinstance(expr, list):
        # convert str and int entries to selectors ----
        all_selectors = [
            cs.by_name(x) if isinstance(x, str) else cs.by_index(x) if isinstance(x, int) else x
            for x in expr
        ]

        # validate all entries ----
        _validate_selector_list(all_selectors, **expand_opts)

        # this should be equivalent to reducing selectors using an "or" operator,
        # which isn't possible when there are selectors mixed with expressions
        # like pl.col("some_col")
        final_columns = OrderedSet(
            col_name
            for sel in all_selectors
            for col_name in cs.expand_selector(data, sel, **expand_opts)
        ).as_list()
    else:
        if not isinstance(expr, (PlSelectExpr, Expr)):
            raise TypeError(f"Unsupported selection expr type: {type(expr)}")

        final_columns = cs.expand_selector(data, expr, **expand_opts)

    col_pos = {k: ii for ii, k in enumerate(data.columns)}

    # I don't think there's a way to get the columns w/o running the selection
    return [(col, col_pos[col]) for col in final_columns]


@eval_select.register
def _(data: PyArrowTable, expr: Union[list[str], PlSelectExpr], strict: bool = True) -> _NamePos:
    if isinstance(expr, (str, int)):
        expr = [expr]

    if isinstance(expr, list):
        return _eval_select_from_list(data.column_names, expr)
    elif callable(expr):
        col_pos = {k: ii for ii, k in enumerate(data.column_names)}
        return [(col, col_pos[col]) for col in data.column_names if expr(col)]

    raise NotImplementedError(f"Unsupported selection expr: {expr}")


def _validate_selector_list(selectors: list, strict=True):
    from polars import Expr
    from polars.selectors import is_selector

    for ii, sel in enumerate(selectors):
        if isinstance(sel, Expr):
            if strict:
                raise TypeError(
                    f"Expected a list of selectors, but entry {ii} is a polars Expr, which is only "
                    "supported for polars versions >= 0.20.30."
                )
        elif not is_selector(sel):
            raise TypeError(f"Expected a list of selectors, but entry {ii} is type: {type(sel)}.")


def _eval_select_from_list(
    columns: list[str], expr: list[Union[str, int]]
) -> list[tuple[str, int]]:
    col_pos = {k: ii for ii, k in enumerate(columns)}

    # TODO: should prohibit duplicate names in expr?
    res: list[tuple[str, int]] = []
    n_cols = len(columns)
    for col in expr:
        if isinstance(col, str):
            if col in col_pos:
                res.append((col, col_pos[col]))
        elif isinstance(col, int):
            _pos = col if col >= 0 else n_cols + col
            res.append((columns[col], _pos))
        else:
            raise TypeError(
                f"eval_select received a list with object of type {type(col)}."
                " Only int and str are supported."
            )
    return res


# create_empty ----


@singledispatch
def create_empty_frame(df: DataFrameLike) -> DataFrameLike:
    """Return a DataFrame with the same shape, but all nan string columns"""
    raise NotImplementedError(f"Unsupported type: {type(df)}")


@create_empty_frame.register
def _(df: PdDataFrame):
    import pandas as pd

    return pd.DataFrame(pd.NA, index=df.index, columns=df.columns, dtype="string")


@create_empty_frame.register
def _(df: PlDataFrame):
    import polars as pl

    return df.clear(len(df)).cast(pl.Utf8)


@create_empty_frame.register
def _(df: PyArrowTable):
    import pyarrow as pa

    return pa.table({col: pa.nulls(df.num_rows, type=pa.string()) for col in df.column_names})


@singledispatch
def copy_frame(df: DataFrameLike) -> DataFrameLike:
    """Return a copy of the input DataFrame"""
    raise NotImplementedError(f"Unsupported type: {type(df)}")


@copy_frame.register
def _(df: PdDataFrame):
    return df.copy()


@copy_frame.register
def _(df: PlDataFrame):
    return df.clone()


@copy_frame.register
def _(df: PyArrowTable):
    import pyarrow as pa

    return pa.table({col: pa.array(df.column(col)) for col in df.column_names})


# cast_frame_to_string ----


@singledispatch
def cast_frame_to_string(df: DataFrameLike) -> DataFrameLike:
    """Return a copy of the input DataFrame with all columns cast to string"""
    raise NotImplementedError(f"Unsupported type: {type(df)}")


@cast_frame_to_string.register
def _(df: PdDataFrame):
    return df.astype("string")


@cast_frame_to_string.register
def _(df: PlDataFrame):
    import polars as pl
    import polars.selectors as cs

    list_cols = [
        name for name, dtype in df.schema.items() if issubclass(dtype.base_type(), pl.List)
    ]

    return df.with_columns(
        cs.by_name(list_cols).map_elements(lambda x: str(x.to_list()), return_dtype=pl.String),
        cs.all().exclude(list_cols).cast(pl.Utf8),
    )


@cast_frame_to_string.register
def _(df: PyArrowTable):
    import pyarrow as pa

    return pa.table({col: pa.array(df.column(col).cast(pa.string())) for col in df.column_names})


# replace_null_frame ----


@singledispatch
def replace_null_frame(df: DataFrameLike, replacement: DataFrameLike) -> DataFrameLike:
    """Return a copy of the input DataFrame with all null values replaced with replacement"""
    raise NotImplementedError(f"Unsupported type: {type(df)}")


@replace_null_frame.register
def _(df: PdDataFrame, replacement: DataFrameLike):
    return df.fillna(replacement)


@replace_null_frame.register
def _(df: PlDataFrame, replacement: PlDataFrame):
    import polars as pl

    exprs = [pl.col(name).fill_null(replacement[name]) for name in df.columns]
    return df.select(exprs)


@replace_null_frame.register
def _(df: PyArrowTable, replacement: PyArrowTable):
    import pyarrow as pa
    import pyarrow.compute as pc

    return pa.table(
        {
            col: pc.if_else(pc.is_null(df.column(col)), replacement.column(col), df.column(col))
            for col in df.column_names
        }
    )


@singledispatch
def to_list(ser: SeriesLike) -> list[Any]:
    raise NotImplementedError(f"Unsupported type: {type(ser)}")


@to_list.register
def _(ser: PdSeries) -> list[Any]:
    return ser.tolist()


@to_list.register
def _(ser: PlSeries) -> list[Any]:
    return ser.to_list()


@to_list.register
def _(ser: PyArrowArray) -> list[Any]:
    return ser.to_pylist()


@to_list.register
def _(ser: PyArrowChunkedArray) -> list[Any]:
    return ser.to_pylist()


# is_series ----


@singledispatch
def is_series(ser: Any) -> bool:
    return False


@is_series.register
def _(ser: PdSeries) -> bool:
    return True


@is_series.register
def _(ser: PlSeries) -> bool:
    return True


@is_series.register
def _(ser: PyArrowArray) -> bool:
    return True


@is_series.register
def _(ser: PyArrowChunkedArray) -> bool:
    return True


# mutate ----


@singledispatch
def eval_transform(df: DataFrameLike, expr: Any) -> list[Any]:
    raise NotImplementedError(f"Unsupported type: {type(df)}")


@eval_transform.register
def _(df: PdDataFrame, expr: Callable[[PdDataFrame], PdSeries]) -> list[Any]:
    res = expr(df)

    if not isinstance(res, PdSeries):
        raise ValueError(f"Result must be a pandas Series. Received {type(res)}")
    elif not len(res) == len(df):
        raise ValueError(
            f"Result must be same length as input data. Observed different lengths."
            f"\n\nInput data: {len(df)}.\nResult: {len(res)}."
        )

    return res.to_list()


@eval_transform.register
def _(df: PlDataFrame, expr: PlExpr) -> list[Any]:
    df_res = df.select(expr)

    if len(df_res.columns) > 1:
        raise ValueError(f"Result must be a single column. Received {len(df_res.columns)} columns.")
    else:
        res = df_res[df_res.columns[0]]

    if not isinstance(res, PlSeries):
        raise ValueError(f"Result must be a polars Series. Received {type(res)}")
    elif not len(res) == len(df):
        raise ValueError(
            f"Result must be same length as input data. Observed different lengths."
            f"\n\nInput data: {len(df)}.\nResult: {len(res)}."
        )

    return res.to_list()


@eval_transform.register
def _(df: PyArrowTable, expr: Callable[[PyArrowTable], PyArrowArray]) -> list[Any]:
    res = expr(df)

    if not isinstance(res, PyArrowArray):
        raise ValueError(f"Result must be an Arrow Array. Received {type(res)}")
    elif not len(res) == len(df):
        raise ValueError(
            f"Result must be same length as input data. Observed different lengths."
            f"\n\nInput data: {df.num_rows}.\nResult: {len(res)}."
        )

    return res.to_pylist()


@singledispatch
def is_na(df: DataFrameLike, x: Any) -> bool:
    raise NotImplementedError(f"Unsupported type: {type(df)}")


@is_na.register
def _(df: PdDataFrame, x: Any) -> bool:
    import pandas as pd

    return pd.isna(x)


@is_na.register(Agnostic)
@is_na.register
def _(df: PlDataFrame, x: Any) -> bool:
    from math import isnan

    import polars as pl

    return x is None or isinstance(x, pl.Null) or (isinstance(x, float) and isnan(x))


@is_na.register
def _(df: PyArrowTable, x: Any) -> bool:
    import pyarrow as pa

    arr = pa.array([x])
    return arr.is_null().to_pylist()[0] or arr.is_nan().to_pylist()[0]


@singledispatch
def validate_frame(df: DataFrameLike) -> DataFrameLike:
    """Raises an error if a DataFrame is not supported by Great Tables.

    Note that this is only relevant for pandas, which allows duplicate names
    on DataFrames, and multi-index columns (and probably other things).
    """
    raise NotImplementedError(f"Unsupported type: {type(df)}")


@validate_frame.register
def _(df: PdDataFrame) -> PdDataFrame:
    import pandas as pd

    # case 1: multi-index columns ----
    if isinstance(df.columns, pd.MultiIndex):
        raise ValueError(
            "pandas DataFrames with MultiIndex columns are not supported."
            " Please use .columns.droplevel() to remove extra column levels,"
            " or combine the levels into a single name per column."
        )

    # case 2: duplicate column names ----
    dupes = df.columns[df.columns.duplicated()]
    if len(dupes):
        raise ValueError(
            f"Column names must be unique. Detected duplicate columns:\n\n {list(dupes)}"
        )

    non_str_cols = [(ii, el) for ii, el in enumerate(df.columns) if not isinstance(el, str)]

    if non_str_cols:
        _col_msg = "\n".join(f"  * Position {ii}: {col}" for ii, col in non_str_cols[:3])
        warnings.warn(
            "pandas DataFrame contains non-string column names. Coercing to strings. "
            "Here are the first few non-string columns:\n\n"
            f"{_col_msg}",
            category=UserWarning,
        )
        new_df = df.copy()
        new_df.columns = [str(el) for el in df.columns]
        return new_df

    return df


@validate_frame.register
def _(df: PlDataFrame) -> PlDataFrame:
    return df


@validate_frame.register
def _(df: PyArrowTable) -> PyArrowTable:
    warnings.warn("PyArrow Table support is currently experimental.")

    if len(set(df.column_names)) != len(df.column_names):
        raise ValueError("Column names must be unique.")

    return df


# to_frame ----


@singledispatch
def to_frame(ser: "list[Any] | SeriesLike", name: Optional[str] = None) -> DataFrameLike:
    # TODO: remove pandas. currently, we support converting a list to a pd.DataFrame
    # in order to support backwards compatibility in the vals.fmt_* functions.

    try:
        import pandas as pd
    except ImportError:
        _raise_pandas_required(
            "Passing a plain list of values currently requires the library pandas. "
            "You can avoid this error by passing a polars Series."
        )

    if not isinstance(ser, list):
        raise NotImplementedError(f"Unsupported type: {type(ser)}")

    if not name:
        raise ValueError("name must be specified, when converting a list to a DataFrame.")

    return pd.DataFrame({name: ser})


@to_frame.register
def _(ser: PdSeries, name: Optional[str] = None) -> PdDataFrame:
    return ser.to_frame(name)


@to_frame.register
def _(ser: PlSeries, name: Optional[str] = None) -> PlDataFrame:
    return ser.to_frame(name)


@to_frame.register
def _(ser: PyArrowArray, name: Optional[str] = None) -> PyArrowTable:
    import pyarrow as pa

    return pa.table({name: ser})


@to_frame.register
def _(ser: PyArrowChunkedArray, name: Optional[str] = None) -> PyArrowTable:
    import pyarrow as pa

    return pa.table({name: ser})


# eval_aggregate ----


@singledispatch
def eval_aggregate(df, expr) -> dict[str, Any]:
    """Evaluate an expression against data and return a single row as a dictionary.

    This is designed for aggregation operations that produce summary statistics.
    The result should be a single row with values for each column.

    Parameters
    ----------
    data
        The input data (DataFrame)
    expr
        The expression to evaluate (Polars expression or callable)

    Returns
    -------
    dict[str, Any]
        A dictionary mapping column names to their aggregated values
    """
    raise NotImplementedError(f"eval_aggregate not implemented for type: {type(df)}")


@eval_aggregate.register
def _(df: PdDataFrame, expr: Callable[[PdDataFrame], PdSeries]) -> dict[str, Any]:
    res = expr(df)

    if not isinstance(res, PdSeries):
        raise ValueError(f"Result must be a pandas Series. Received {type(res)}")

    return res.to_dict()


@eval_aggregate.register
def _(df: PlDataFrame, expr: PlExpr) -> dict[str, Any]:
    res = df.select(expr)

    if len(res) != 1:
        raise ValueError(
            f"Expression must produce exactly 1 row (aggregation). Got {len(res)} rows."
        )

    return res.to_dicts()[0]


@eval_aggregate.register
def _(df: PyArrowTable, expr: Callable[[PyArrowTable], PyArrowTable]) -> dict[str, Any]:
    res = expr(df)

    if not isinstance(res, PyArrowTable):
        raise ValueError(f"Result must be a PyArrow Table. Received {type(res)}")

    if res.num_rows != 1:
        raise ValueError(
            f"Expression must produce exactly 1 row (aggregation). Got {res.num_rows} rows."
        )

    return {col: res.column(col)[0].as_py() for col in res.column_names}
