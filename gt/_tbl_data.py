from typing import Any, List, cast
import pandas as pd


class TblData:
    def __init__(self, data: Any):

        # Transform incoming data to a pandas DataFrame
        pd_data = pd.DataFrame(data)

        # The tabular data stored as a pandas DataFrame
        self._tbl_data: pd.DataFrame = pd_data

    @property
    def columns(self) -> List[str]:
        data_column_index: pd.Index = self._tbl_data.columns
        return list(data_column_index)

    @property
    def rows(self) -> int:
        return len(self._tbl_data)

    def get_cell(self, row: int, column: str) -> Any:
        return cast(Any, self._tbl_data[column][row])

    def pd_to_dict(self):
        return self._tbl_data.reset_index().to_dict(orient="list")

    def get_column_dtype(self, column: str) -> str:
        return self._tbl_data[column].dtypes


class TblDataAPI:
    _tbl_data: TblData

    def __init__(self, data: Any):
        self._tbl_data = TblData(data)
