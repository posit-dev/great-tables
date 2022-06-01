import pandas as pd
import numpy as np


class Stub:
    def __init__(self, data: pd.DataFrame):

        # Transform incoming data to a pandas DataFrame
        # TODO: use already stored data in `_tbl_data` in `GT()`
        pd_data = pd.DataFrame(data)

        row_indices = list(range(len(pd_data)))

        # The `stub` DataFrame is used to handle row indices,
        # row labels, any associated groups, and built labels
        # for the output context

        # 0: rownum_i = obtained from length of DF
        # 1: group_id = np.nan
        # 2: rowname = np.nan
        # 3: group_label = np.nan
        # 4: built = np.nan

        self._stub: pd.DataFrame = pd.DataFrame(
            {
                "rownum_i": row_indices,
                "group_id": np.nan,
                "rowname": np.nan,
                "group_label": np.nan,
                "built": np.nan,
            }
        )


class StubAPI:
    _stub: Stub

    def __init__(self, data: pd.DataFrame):
        self._stub = Stub(data)
