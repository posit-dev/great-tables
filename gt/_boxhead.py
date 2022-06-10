from typing import Optional, List
from enum import Enum, auto

from ._base_api import BaseAPI
from ._tbl_data import TblData


class ColumnAlignment(Enum):
    Left = auto()
    Center = auto()
    Right = auto()
    Justify = auto()


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

    # Get a list of visible columns in
    def _get_visible_columns(self) -> List[str]:

        visible_columns = [x.var for x in self._boxhead if x.visible is True]
        return visible_columns

    # Get the number of columns for the visible (not hidden) data; this
    # excludes the number of columns required for the table stub
    def _get_number_of_visible_data_columns(self) -> int:
        return len(self._get_visible_columns())

    # Obtain the number of visible columns in the built table; this should
    # account for the size of the stub in the final, built table
    def _get_effective_number_of_columns(self) -> int:

        n_data_cols = self._get_number_of_visible_data_columns()

        # TODO: Once the stub is defined in the package, we need to account
        # for the width of the stub at build time to fully obtain the number
        # of visible columns in the built table
        # n_data_cols = n_data_cols + len(get_stub_layout(data=data))

        return n_data_cols


class BoxheadAPI(BaseAPI):
    _boxhead: Boxhead

    def __init__(self):
        self._boxhead = Boxhead(self._data)
