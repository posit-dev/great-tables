from typing import Any, List, Dict, cast
import pandas as pd
from pandas._typing import Column


class TblData:
    _tbl_data: pd.DataFrame

    def __init__(self, data: Any):

        # Transform incoming data to a pandas DataFrame
        pd_data = pd.DataFrame(data).copy()

        # The tabular data stored as a pandas DataFrame
        self._tbl_data = pd_data

    def get_column_names(self) -> List[str]:
        """Get a list of column names from the input data table"""
        data_column_index: pd.Index = self._tbl_data.columns
        return list(data_column_index)

    def n_rows(self) -> int:
        """Get the number of rows from the input data table"""
        return len(self._tbl_data)

    def _get_cell(self, row: int, column: str) -> Any:
        """Get the content from a single cell in the input data table"""
        return cast(Any, self._tbl_data[column][row])

    def _get_column_dtype(self, column: str) -> str:
        """Get the data type for a single column in the input data table"""
        return self._tbl_data[column].dtypes

    def _make_empty_df(self):
        """Create an empty DataFrame variant of the input data table"""
        column_list = list(self._tbl_data.columns)
        rowidx_list = list(range(len(self._tbl_data)))
        return pd.DataFrame(columns=column_list, index=rowidx_list)

    def _make_empty_table_dict(self) -> Dict[Column, Any]:
        """Create an empty DataFrame variant of the input data table"""
        column_list = list(self._tbl_data.columns)
        rowidx_list = list(range(len(self._tbl_data)))
        df = pd.DataFrame(columns=column_list, index=rowidx_list)
        df = df.reset_index().to_dict(orient="list")
        idx_key = list(df.keys())[0]
        df.pop(idx_key, None)
        return df

    def _pd_to_dict(self):
        """Transform the input data table from a DataFrame to a dictionary"""
        return self._tbl_data.reset_index().to_dict(orient="list")


class TblDataAPI:
    _tbl_data: TblData

    def __init__(self, data: Any):
        self._tbl_data = TblData(data)
