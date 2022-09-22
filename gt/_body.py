from typing import Optional, Union
import pandas as pd
from ._tbl_data import TblData


class Body:
    body: TblData
    data: Optional[int]

    def __init__(self, body: Union[pd.DataFrame, TblData], data: Optional[int] = None):
        if isinstance(body, pd.DataFrame):
            self.body = TblData(body)
        else:
            self.body = body
        self.data = data

    # def _render_formats(self) -> "Body":

    #     self = Body(self.body, self.data)
    #     formats = self.
    #     for fmt in formats:
    #         pass
    #     # for (fmt in formats)  {
    #     #     # Determine if the formatter has a function relevant
    #     #     # to the context; if not, use the `default` function
    #     #     # (which should always be present)
    #     #     if (context %in% names(fmt$func)) {
    #     #     eval_func <- context
    #     #     } else {
    #     #     eval_func <- "default"
    #     #     }
    #     #     for (col in fmt[["cols"]]) {
    #     #     # Perform rendering but only do so if the column is present
    #     #     if (col %in% colnames(data_tbl)) {
    #     #         result <- fmt$func[[eval_func]](data_tbl[[col]][fmt$rows])
    #     #         # If any of the resulting output is `NA`, that
    #     #         # means we want to NOT make changes to those
    #     #         # particular cells' output (i.e. inherit the
    #     #         # results of the previous formatter).
    #     #         body[[col]][fmt$rows][!is.na(result)] <- stats::na.omit(result)
    #     #     }
    #     #     }
    #     # }

    #     return self


class BodyAPI:
    _body: Body

    def __init__(self):
        pass
