# Tests to be run with pandas uninstalled.

import pytest
from great_tables._formats_vals import _make_one_col_table

# mark file as nopandas
pytestmark = pytest.mark.no_pandas


def test_no_pandas_import_fails():
    with pytest.raises(ModuleNotFoundError):
        import pandas


def test_no_pandas_import_exibble_raises():
    with pytest.raises(ModuleNotFoundError):
        from great_tables import exibble


def test_no_pandas_import():
    from great_tables import GT


def test_one_column_table_no_lib() -> None:
    vals = [1, 2, 3]

    _make_one_col_table(vals=vals)
