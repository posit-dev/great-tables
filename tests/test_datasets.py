import pandas as pd
import polars as pl
import pyarrow as pa
import pytest

from great_tables import data
from great_tables.data import Dataset


@pytest.mark.parametrize(
    "name",
    [
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
    ],
)
def test_datasets(name: str):
    df = getattr(data, name)
    assert isinstance(df, pd.DataFrame)

    dataset = getattr(Dataset, name)
    assert isinstance(dataset.to_pandas(), pd.DataFrame)
    assert isinstance(dataset.to_polars(), pl.DataFrame)
    assert isinstance(dataset.to_pyarrow(), pa.Table)
