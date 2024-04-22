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
