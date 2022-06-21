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
        """Get a list of column names from the input data table"""
        data_column_index: pd.Index = self._tbl_data.columns
        return list(data_column_index)

    @property
    def rows(self) -> int:
        """Get the number of rows from the input data table"""
        return len(self._tbl_data)

    def get_cell(self, row: int, column: str) -> Any:
        """Get the content from a single cell in the input data table"""
        return cast(Any, self._tbl_data[column][row])

    def pd_to_dict(self):
        """Transform the input data table from a DataFrame to a dictionary"""
        return self._tbl_data.reset_index().to_dict(orient="list")

    def get_column_dtype(self, column: str) -> str:
        """Get the data type for a single column in the input data table"""
        return self._tbl_data[column].dtypes


class TblDataAPI:
    _tbl_data: TblData

    def __init__(self, data: Any):
        self._tbl_data = TblData(data)
