from typing import Union, List, Literal, Any
import pandas as pd
from ._tbl_data import TblData
from ._formats import FormatInfo

Context = Literal["html", "default"]


class Body:
    body: TblData
    data: Any

    def __init__(self, body: Union[pd.DataFrame, TblData], data: Any = None):
        if isinstance(body, pd.DataFrame):
            self.body = TblData(body)
        else:
            self.body = body
        self.data = data

    def render_formats(
        self, data_tbl: TblData, formats: List[FormatInfo], context: Context
    ):
        for fmt in formats:
            eval_func = getattr(fmt.func, context, fmt.func.default)
            if eval_func is None:
                raise Exception("Internal Error")
            for col, row in fmt.cells.resolve():
                result = eval_func(data_tbl._get_cell(row, col))
                self.body._set_cell(row, col, result)

        return self


class BodyAPI:
    _body: Body

    def __init__(self, data: Any):
        self._body = Body(data, self)
