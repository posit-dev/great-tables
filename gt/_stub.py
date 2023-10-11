from typing import Optional

from ._base_api import BaseAPI
from ._tbl_data import TblData, n_rows


class RowInfo:
    # TODO: Make `rownum_i` readonly
    rownum_i: int
    group_id: Optional[str]
    rowname: Optional[str]
    group_label: Optional[str]
    built: bool = False

    # The components of the stub are:
    # `rownum_i` (The initial row indices for the table at ingest time)
    # `group_id` = None
    # `rowname` = None
    # `group_label` = None
    # `built` = False

    def __init__(
        self,
        rownum_i: int,
        group_id: Optional[str] = None,
        rowname: Optional[str] = None,
        group_label: Optional[str] = None,
        built: bool = False,
    ):
        self.rownum_i = rownum_i
        self.group_id = group_id
        self.rowname = rowname
        self.group_label = group_label
        self.built = built


class Stub:
    def __init__(self, data: TblData):

        # Obtain a list of row indices from the data and initialize
        # the `_stub` from that
        row_indices = list(range(n_rows(data)))

        # Obtain the column names from the data and initialize the
        # `_boxhead` from that
        self._stub: list[RowInfo] = [RowInfo(col) for col in row_indices]


class StubAPI(BaseAPI):
    _stub: Stub

    def __init__(self):
        self._stub = Stub(self._get_tbl_data())
