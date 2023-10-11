from typing import Any, List, Union, cast, TYPE_CHECKING
from ._databackend import AbstractBackend
from functools import singledispatch

import pandas as pd


if TYPE_CHECKING:
    import pandas as pd
    import polars as pl

    PdDataFrame = pd.DataFrame
    PlDataFrame = pl.DataFrame


else:

    class PdDataFrame(AbstractBackend):
        _backends = [("pandas", "DataFrame")]

    class PlDataFrame(AbstractBackend):
        _backends = [("polars", "DataFrame")]


DataFrameLike = Union[PdDataFrame, PlDataFrame]


# utils ----

def _raise_not_implemented(data):
    raise NotImplementedError(f"Unsupported data type: {type(data)}")


def register_tbl_data(f):
    """Registers a concrete that dispatches on underlying TblData DataFrame

    This is a temporary patch until TblData is removed in favor of the underlying
    DataFrame type itself.
    """
    f.register(TblData, lambda d, *args, **kwargs: f(d._tbl_data, *args, **kwargs))

    return f


# classes ----

class TblData:
    _tbl_data: pd.DataFrame

    def __init__(self, data: Any):

        # Transform incoming data to a pandas DataFrame
        pd_data = pd.DataFrame(data).copy()

        # The tabular data stored as a pandas DataFrame
        self._tbl_data = pd_data


class TblDataAPI:
    _tbl_data: TblData

    def __init__(self, data: Any):
        self._tbl_data = TblData(data)


# generic functions ----

# get_column_names ----

@register_tbl_data
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

@register_tbl_data
@singledispatch
def n_rows(data: DataFrameLike) -> int:
    """Get the number of rows from the input data table"""
    raise _raise_not_implemented(data)


@n_rows.register(PdDataFrame)
@n_rows.register(PlDataFrame)
def _(data):
    return len(data)


# _get_cell ----

@register_tbl_data
@singledispatch
def _get_cell(data: DataFrameLike, row: int, column: str) -> Any:
    """Get the content from a single cell in the input data table"""

    _raise_not_implemented(data)

@_get_cell.register(PdDataFrame)
@_get_cell.register(PlDataFrame)
def _(data, row: int, column: str):
    return data[column][row]


# _set_cell ----

@register_tbl_data
@singledispatch
def _set_cell(data: DataFrameLike, row: int, column: str, value: Any):
    _raise_not_implemented(data)


@_set_cell.register(PdDataFrame)
def _(data, row: int, column: str, value: Any):
    data[column][row] = value


# _get_column_dtype ----

@register_tbl_data
@singledispatch
def _get_column_dtype(data: DataFrameLike, column: str) -> str:
    """Get the data type for a single column in the input data table"""
    return data[column].dtypes

