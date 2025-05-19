import pandas as pd
import polars as pl
import pytest
from great_tables._formats_vals import _make_one_col_table
from great_tables._tbl_data import to_list
import sys


@pytest.mark.parametrize("src", [1, [1], (1,), pd.Series([1]), pl.Series([1])])
def test_roundtrip(src):
    gt = _make_one_col_table(src)

    assert to_list(gt._tbl_data["x"]) == [1]


def test_one_column_table_no_lib() -> None:
    sys.modules["pandas"] = None

    with pytest.raises(ModuleNotFoundError):
        import pandas

    vals = [1, 2, 3]

    _make_one_col_table(vals=vals)
    raise


test_one_column_table_no_lib()
