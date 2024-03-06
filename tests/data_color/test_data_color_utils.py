import pandas as pd
import numpy as np
from great_tables._data_color import (
    _rescale_numeric,
    _get_domain_numeric,
    _get_domain_factor,
)


def test_rescale_numeric():
    # Test case 1: Rescale values within the domain range
    df = pd.DataFrame({"col": [1, 2, 3, 4, 5]})
    vals = [2, 3, 4]
    domain = [1, 5]
    expected_result = [0.25, 0.5, 0.75]
    result = _rescale_numeric(df, vals, domain)
    assert result == expected_result

    # Test case 2: Rescale values outside the domain range
    df = pd.DataFrame({"col": [1, 2, 3, 4, 5]})
    vals = [0, 6]
    domain = [1, 5]
    expected_result = [np.nan, np.nan]
    result = _rescale_numeric(df, vals, domain)
    assert result == expected_result

    # Test case 3: Rescale values with NA values
    df = pd.DataFrame({"col": [1, 2, np.nan, 4, 5]})
    vals = [2, np.nan, 4]
    domain = [1, 5]
    expected_result = [0.25, np.nan, 0.75]
    result = _rescale_numeric(df, vals, domain)
    assert result == expected_result


def test_get_domain_numeric():
    df = pd.DataFrame({"col1": [1, 2, 3, 4, 5], "col2": [6, 7, 8, 9, 10]})
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    domain = _get_domain_numeric(df, vals)
    assert domain == [1, 10]

    df = pd.DataFrame({"col1": [1, 2, 3, 4, 5], "col2": [6, 7, 8, 9, 10]})
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, np.nan]
    domain = _get_domain_numeric(df, vals)
    assert domain == [1, 10]

    df = pd.DataFrame({"col1": [1, 2, 3, 4, 5], "col2": [6, 7, 8, 9, 10]})
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, np.nan, np.nan]
    domain = _get_domain_numeric(df, vals)
    assert domain == [1, 10]


def test_get_domain_factor():
    # Test case 1: Empty DataFrame
    df = pd.DataFrame()
    vals = []
    result = _get_domain_factor(df, vals)
    assert result == []

    # Test case 2: DataFrame with factor values
    df = pd.DataFrame({"col1": ["A", "B", "A", "C", "B"]})
    vals = ["A", "B", "C"]
    result = _get_domain_factor(df, vals)
    assert result == ["A", "B", "C"]

    # Test case 3: DataFrame with factor values and NA values
    df = pd.DataFrame({"col1": ["A", "B", np.nan, "C", "B"]})
    vals = ["A", "B", "C"]
    result = _get_domain_factor(df, vals)
    assert result == ["A", "B", "C"]

    # Test case 4: DataFrame with factor values and NA values in `vals`
    df = pd.DataFrame({"col1": ["A", "B", "C"]})
    vals = ["A", "B", np.nan, "C"]
    result = _get_domain_factor(df, vals)
    assert result == ["A", "B", "C"]

    # Test case 5: DataFrame with factor values and duplicate values in `vals`
    df = pd.DataFrame({"col1": ["A", "B", "C"]})
    vals = ["A", "B", "B", "C"]
    result = _get_domain_factor(df, vals)
    assert result == ["A", "B", "C"]
