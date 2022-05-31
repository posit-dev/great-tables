from typing import Any
import pandas as pd


class TblData:
    def __init__(self, data: Any):

        # Transform incoming data to a pandas DataFrame
        pd_data = pd.DataFrame(data)

        # The tabular data stored as a pandas DataFrame
        self._tbl_data: pd.DataFrame = pd_data


class TblDataAPI:
    _tbl_data: TblData

    def __init__(self, data: Any):
        self._tbl_data = TblData(data)
