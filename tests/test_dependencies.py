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


def test_make_on_col_table_from_list_no_pandas() -> None:
    from great_tables._formats_vals import _make_one_col_table
    import polars as pl
    # TODO: Should paramaterize this to collections in general

    with pytest.raises(ModuleNotFoundError):
        import pandas  # sanity check to make sure it's not available

    l: list[str] = ["a", "b", "c"]
    list_table_html: str = _make_one_col_table(l).as_raw_html()
    assert isinstance(list_table_html, str)

    ser: pl.Series = pl.Series(l)
    ser_table_html: str = _make_one_col_table(ser).as_raw_html()
    assert isinstance(ser_table_html, str)

    # TODO: Need a way to check the equality of the two HTML tables
