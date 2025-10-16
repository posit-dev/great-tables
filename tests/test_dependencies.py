# Tests to be run with pandas uninstalled.

import pytest

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


def test_no_pandas_vals_funcs_polars():
    from great_tables import vals
    import polars as pl

    assert vals.fmt_percent(pl.Series([0.11, 0.22]), decimals=0) == ["11%", "22%"]
