import pandas as pd
import numpy as np


class Boxhead:
    def __init__(self, data: pd.DataFrame):

        # Transform incoming data to a pandas DataFrame
        # TODO: use already stored data in `_tbl_data` in `GT()`
        pd_data = pd.DataFrame(data)
        column_names = list(pd_data.columns)

        # The `boxhead` DataFrame is used to handle column labels, column
        # ordering, alignments of entire columns, column widths, and
        # column visibility (e.g., displayed/hidden)
        # 0: `var` (obtained from column names)
        # 1: `type` = "default"
        # 2: `column_label` (obtained from column names)
        # 3: `column_align` = "center"
        # 4: `column_width` = np.nan

        self._boxhead: pd.DataFrame = pd.DataFrame(
            {
                "var": column_names,
                "type": "default",
                "column_label": column_names,
                "column_align": "center",
                "column_width": np.nan,
            }
        )


class BoxheadAPI:
    _boxhead: Boxhead

    def __init__(self, data: pd.DataFrame):
        self._boxhead = Boxhead(data)
