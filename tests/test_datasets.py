import pandas as pd
import pytest

from great_tables import data


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
