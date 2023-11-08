from __future__ import annotations

from typing import Any, List, Union, Callable, Tuple, TYPE_CHECKING
from ._databackend import AbstractBackend
from functools import singledispatch

import pandas as pd


if TYPE_CHECKING:
    import pandas as pd
    import polars as pl

    # the class behind selectors
    from polars.selectors import _selector_proxy_

    PdDataFrame = pd.DataFrame
    PlDataFrame = pl.DataFrame

    DataFrameLike = Union[PdDataFrame, PlDataFrame]
    TblData = DataFrameLike

else:
    from abc import ABC

    # we just need this as a static type hint, but singledispatch tries to resolve
    # any hints at runtime. So we need some value for it.
    from typing import Any as _selector_proxy_

    class PdDataFrame(AbstractBackend):
        _backends = [("pandas", "DataFrame")]

    class PlDataFrame(AbstractBackend):
        _backends = [("polars", "DataFrame")]

    # TODO: these types are imported throughout gt, so we need to either put
    # those imports under TYPE_CHECKING, or continue to make available dynamically here.
    class DataFrameLike(ABC):
        """Represent some DataFrame"""

    DataFrameLike.register(PdDataFrame)
    DataFrameLike.register(PlDataFrame)

    TblData = DataFrameLike


# utils ----


def _raise_not_implemented(data):
    raise NotImplementedError(f"Unsupported data type: {type(data)}")


# classes ----


class TblDataAPI:
    pass


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


# get_column_names ----
@singledispatch
def get_column_names(data: DataFrameLike) -> List[str]:
    """Get a list of column names from the input data table"""
    _raise_not_implemented(data)


@get_column_names.register(PdDataFrame)
def _(data: PdDataFrame):
    return data.columns.tolist()


@get_column_names.register(PlDataFrame)
def _(data: PlDataFrame):
    return data.columns


# n_rows ----


@singledispatch
def n_rows(data: DataFrameLike) -> int:
    """Get the number of rows from the input data table"""
    raise _raise_not_implemented(data)


@n_rows.register(PdDataFrame)
@n_rows.register(PlDataFrame)
def _(data):
    return len(data)


# _get_cell ----


@singledispatch
def _get_cell(data: DataFrameLike, row: int, column: str) -> Any:
    """Get the content from a single cell in the input data table"""

    _raise_not_implemented(data)


@_get_cell.register(PlDataFrame)
def _(data, row: int, column: str):
    return data[column][row]


@_get_cell.register(PdDataFrame)
def _(data, row, col):
    col_ii = data.columns.get_loc(col)

    if not isinstance(col_ii, int):
        raise ValueError("Column named " + col + " matches multiple columns.")

    return data.iloc[row, col_ii]


# _set_cell ----


@singledispatch
def _set_cell(data: DataFrameLike, row: int, column: str, value: Any):
    _raise_not_implemented(data)


@_set_cell.register(PdDataFrame)
def _(data, row: int, column: str, value: Any):
    # TODO: should this use data.loc?
    data[column][row] = value


@_set_cell.register(PlDataFrame)
def _(data, row: int, column: str, value: Any):
    data[row, column] = value


# _get_column_dtype ----


@singledispatch
def _get_column_dtype(data: DataFrameLike, column: str) -> str:
    """Get the data type for a single column in the input data table"""
    return data[column].dtype


# reorder ----


@singledispatch
def reorder(data: DataFrameLike, rows: List[int], columns: List[str]) -> DataFrameLike:
    """Return a re-ordered DataFrame."""
    _raise_not_implemented(data)


@reorder.register
def _(data: PdDataFrame, rows: List[int], columns: List[str]) -> PdDataFrame:
    # note that because loc is label based, we need
    # reset index to allow us to use integer indexing on the rows
    # note that this means the index is not preserved when reordering pandas
    return data.iloc[rows, :].loc[:, columns]


@reorder.register
def _(data: PlDataFrame, rows: List[int], columns: List[str]) -> PlDataFrame:
    return data[rows, columns]


# eval_select ----

_NamePos = List[Tuple[str, int]]


@singledispatch
def eval_select(data: DataFrameLike, expr: Any, strict: bool = True) -> _NamePos:
    """Return a list of column names selected by expr."""

    raise NotImplementedError(f"Unsupported type: {type(expr)}")


@eval_select.register
def _(data: PdDataFrame, expr: Union[List[str], Callable[[str], bool]], strict=True) -> _NamePos:
    col_pos = {k: ii for ii, k in enumerate(data.columns)}
    if isinstance(expr, list):
        # TODO: should prohibit duplicate names in expr?
        return [(col, col_pos[col]) for col in expr if col in data.columns]
    elif callable(expr):
        # TODO: currently, we call on each string, but we could be calling on
        # pd.DataFrame.columns instead (which would let us use pandas .str methods)
        return [(col, col_pos[col]) for col in data.columns if expr(col)]

    raise NotImplementedError(f"Unsupported selection expr: {expr}")


@eval_select.register
def _(data: PlDataFrame, expr: Union[List[str], _selector_proxy_], strict=True) -> _NamePos:
    # TODO: how to annotate type of a polars selector?
    # Seems to be polars.selectors._selector_proxy_.
    from polars import Expr
    from polars import selectors

    col_pos = {k: ii for ii, k in enumerate(data.columns)}

    # just in case _selector_proxy_ gets renamed or something
    # it inherits from Expr, so we can just use that in a pinch
    cls_selector = getattr(selectors, "_selector_proxy_", Expr)

    if not isinstance(expr, (list, cls_selector)):
        raise TypeError(f"Unsupported selection expr type: {type(expr)}")

    # I don't think there's a way to get the columns w/o running the selection
    return [(col, col_pos[col]) for col in data.select(expr).columns]
