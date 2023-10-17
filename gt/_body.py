from typing import Union, List, Literal, Any
import pandas as pd
from ._tbl_data import DataFrameLike, TblData, _get_cell, _set_cell, copy_data
from ._formats import FormatInfo

Context = Literal["html", "default"]


class Body:
    body: TblData
    data: Any

    def __init__(self, body: Union[pd.DataFrame, TblData], data: Any = None):
        if isinstance(body, DataFrameLike):
            self.body = pd.DataFrame(
                pd.NA, index=body.index, columns=body.columns, dtype="string"
            )
        else:
            raise NotImplementedError()
        self.data = data

    def render_formats(
        self, data_tbl: TblData, formats: List[FormatInfo], context: Context
    ):
        for fmt in formats:
            eval_func = getattr(fmt.func, context, fmt.func.default)
            if eval_func is None:
                raise Exception("Internal Error")
            for col, row in fmt.cells.resolve():
                result = eval_func(_get_cell(data_tbl, row, col))
                # TODO: I think that this is very inefficient with polars, so
                # we could either accumulate results and set them per column, or
                # could always use a pandas DataFrame inside Body?
                _set_cell(self.body, row, col, result)

        return self


class BodyAPI:
    _body: Body

    def __init__(self, data: Any):
        self._body = Body(data, data)
