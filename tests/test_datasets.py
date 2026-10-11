import pandas as pd
import polars as pl
import pytest

from great_tables import data


_DATASET_NAMES = [
    "countrypops",
    "sza",
    "gtcars",
    "sp500",
    "pizzaplace",
    "exibble",
    "towny",
    "peeps",
    "films",
    "metro",
    "gibraltar",
    "constants",
    "illness",
    "reactions",
    "photolysis",
    "nuclides",
]


@pytest.mark.parametrize("name", _DATASET_NAMES)
def test_datasets(name: str):
    df = getattr(data, name)
    assert isinstance(df, pd.DataFrame)


@pytest.mark.parametrize("name", _DATASET_NAMES)
def test_datasets_pd_namespace(name: str):
    df = getattr(data.pd, name)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0


@pytest.mark.parametrize("name", _DATASET_NAMES)
def test_datasets_pl_namespace(name: str):
    df = getattr(data.pl, name)
    assert isinstance(df, pl.DataFrame)
    assert df.shape[0] > 0


@pytest.mark.parametrize("name", _DATASET_NAMES)
def test_datasets_pd_pl_same_shape(name: str):
    pd_df = getattr(data.pd, name)
    pl_df = getattr(data.pl, name)
    assert pd_df.shape == pl_df.shape


def test_pd_namespace_caches_results():
    df1 = data.pd.exibble
    df2 = data.pd.exibble
    assert df1 is df2


def test_pl_namespace_caches_results():
    df1 = data.pl.exibble
    df2 = data.pl.exibble
    assert df1 is df2


def test_pd_namespace_invalid_dataset():
    with pytest.raises(AttributeError, match="not found"):
        data.pd.nonexistent_dataset


def test_pl_namespace_invalid_dataset():
    with pytest.raises(AttributeError, match="not found"):
        data.pl.nonexistent_dataset


def test_namespace_dir():
    pd_datasets = dir(data.pd)
    pl_datasets = dir(data.pl)
    assert pd_datasets == pl_datasets
    for name in _DATASET_NAMES:
        assert name in pd_datasets


def test_pd_namespace_private_attr_raises():
    """Accessing a private attribute (starts with _) raises AttributeError."""
    with pytest.raises(AttributeError):
        data.pd._private_attr


def test_pl_namespace_private_attr_raises():
    """Accessing a private attribute (starts with _) raises AttributeError."""
    with pytest.raises(AttributeError):
        data.pl._private_attr


def test_all_lists_official_datasets_and_load_dataset():
    from typing import get_args

    from great_tables.data import _DatasetNames

    # `__all__` is a literal list (for static tools), so check it against `load_dataset()`'s names
    assert data.__all__ == [*get_args(_DatasetNames), "load_dataset"]
    assert all(hasattr(data, name) for name in data.__all__)


def test_star_import_keeps_pandas_and_polars_aliases():
    # `from great_tables.data import *` mustn't replace `pd` / `pl` with the backend namespaces
    namespace = {"pd": pd, "pl": pl}
    exec("from great_tables.data import *", namespace)

    assert namespace["pd"] is pd
    assert namespace["pl"] is pl
    assert set(data.__all__) <= set(namespace)
    assert "islands" not in namespace and "airquality" not in namespace


@pytest.mark.parametrize("name,shape", [("islands", (48, 2)), ("airquality", (153, 6))])
def test_deprecated_datasets_warn(name: str, shape: tuple[int, int]):
    # `islands` and `airquality` aren't gt datasets, so they're deprecated (but still load)
    with pytest.warns(FutureWarning, match=f"The `{name}` dataset is deprecated"):
        assert getattr(data, name).shape == shape

    with pytest.warns(FutureWarning, match=f"The `{name}` dataset is deprecated"):
        assert getattr(data.pd, name).shape == shape

    with pytest.warns(FutureWarning, match=f"The `{name}` dataset is deprecated"):
        assert getattr(data.pl, name).shape == shape


def test_deprecated_dataset_from_import_warns_once():
    import warnings

    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        exec("from great_tables.data import islands", {})

    assert [str(w.message)[:31] for w in record] == ["The `islands` dataset is deprec"]


def test_official_datasets_and_star_import_dont_warn():
    import warnings

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        exec("from great_tables.data import *", {})
        _ = data.exibble, data.pl.gtcars


def test_unknown_attribute_raises():
    with pytest.raises(AttributeError, match="has no attribute 'nope'"):
        data.nope
