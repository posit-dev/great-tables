import pandas as pd
import polars as pl
import pytest
from great_tables._formats_vals import _make_one_col_table
from great_tables._tbl_data import to_list


@pytest.mark.parametrize("src", [1, [1], (1,), pd.Series([1]), pl.Series([1])])
def test_roundtrip(src):
    gt = _make_one_col_table(src)

    assert to_list(gt._tbl_data["x"]) == [1]
