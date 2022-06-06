from typing import Optional
from enum import Enum

from ._base_api import BaseAPI
from ._tbl_data import TblData


class ColumnAlignment(Enum):
    Left = 1
    Center = 2
    Right = 3
    Justify = 4


class ColInfo:
    # TODO: Make var readonly
    var: str
    column_label: str
    visible: bool
    column_align: Optional[ColumnAlignment]
    column_width: Optional[str]

    # The components of the boxhead are:
    # `var` (obtained from column names)
    # `column_label` (obtained from column names)
    # `visible` = True
    # `column_align` = None
    # `column_width` = None

    def __init__(
        self,
        var: str,
        column_label: Optional[str] = None,
        visible: bool = True,
        column_align: Optional[ColumnAlignment] = None,
        column_width: Optional[str] = None,
    ):
        self.var = var
        self.column_label = column_label or var
        self.visible = visible
        self.column_align = column_align
        self.column_width = column_width


class Boxhead:
    def __init__(self, data: TblData):

        # Obtain the column names from the data and initialize the
        # `_boxhead` from that
        column_names = data.columns
        self._boxhead: list[ColInfo] = [ColInfo(col) for col in column_names]


class BoxheadAPI(BaseAPI):
    _boxhead: Boxhead

    def __init__(self):
        self._boxhead = Boxhead(self._data)
