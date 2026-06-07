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
