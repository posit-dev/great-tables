from .gt import GT
from typing import Literal

Context = Literal["html", "default"]


def render_formats(data: GT, context: Context):
    body = data._body
    data_tbl = data._tbl_data
    formats = data._formats

    for fmt in formats:
        eval_func = getattr(fmt.func, context, fmt.func.default)
        if eval_func is None:
            raise Exception("Internal Error")
        for col, row in fmt.cells.resolve():
            result = eval_func(data_tbl._get_cell(row, col))
            body.body._set_cell(row, col, result)
