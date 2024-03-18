import numpy as np
from great_tables._utils_nanoplots import _normalize_vals, _normalize_to_dict

# TODO: need tests of all utils_nanoplot functions


def test_normalize_vals():
    # Test case 1: Normalization with no missing values
    x = [1, 2, 3, 4, 5]
    expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert _normalize_vals(x) == expected_output

    # Test case 2: Normalization with missing values
    x = [1, np.nan, 3, 4, np.nan]
    expected_output = [0.0, np.nan, 0.6666666666666666, 1.0, np.nan]
    assert _normalize_vals(x) == expected_output

    # Test case 3: Normalization with all missing values
    x = [np.nan, np.nan, np.nan]
    expected_output = [np.nan, np.nan, np.nan]
    assert _normalize_vals(x) == expected_output

    # Test case 4: Normalization with negative values
    x = [-5, -3, -1, 0, 2, 4]
    expected_output = [
        0.0,
        0.2222222222222222,
        0.4444444444444444,
        0.5555555555555556,
        0.7777777777777778,
        1.0,
    ]
    assert _normalize_vals(x) == expected_output


def test_normalize_to_dict():
    # Test case 1: Normalization with no missing values
    assert _normalize_to_dict(a=3.5, b=-0.3) == {"a": [1.0], "b": [0.0]}

    # Test case 2: Normalization with missing values
    assert _normalize_to_dict(a=3.5, b=np.nan, c=4.0) == {"a": [0.0], "b": [np.nan], "c": [1.0]}

    # Test case 3: Normalization with negative values
    assert _normalize_to_dict(a=3.5, b=np.nan, c=4.0, werwdf=-5) == {
        "a": [0.9444444444444444],
        "b": [np.nan],
        "c": [1.0],
        "werwdf": [0.0],
    }

    # Test case 4: Normalization with non-unique values
    res = _normalize_to_dict(a=5, b=5, c=5)

    # Get values from res into a list and sort them
    res = sorted(list(res.values()))

    assert res[0][0] == 0.0
    assert res[1][0] > 0.0 and res[1][0] < 1.0
    assert res[2][0] == 1.0
