from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING
from ._databackend import AbstractBackend
from functools import singledispatch

import pandas as pd


if TYPE_CHECKING:
    import pandas as pd
    import polars as pl

    PdDataFrame = pd.DataFrame
    PlDataFrame = pl.DataFrame

    DataFrameLike = Union[PdDataFrame, PlDataFrame]
    TblData = DataFrameLike

else:
    from abc import ABC

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


@_get_cell.register(PdDataFrame)
@_get_cell.register(PlDataFrame)
def _(data, row: int, column: str):
    return data[column][row]


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
