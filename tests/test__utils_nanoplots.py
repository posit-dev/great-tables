import pytest
import numpy as np
from great_tables._utils_nanoplots import (
    _val_is_numeric,
    _val_is_str,
    _is_integerlike,
    _normalize_vals,
    _normalize_to_dict,
    calc_ref_value,
    _format_number_compactly,
)
from typing import Union

# TODO: need tests of all utils_nanoplot functions


def test_val_is_numeric():
    # Test case 1: Numeric values
    assert _val_is_numeric(1)
    assert _val_is_numeric(-1)
    assert _val_is_numeric(1.0)
    assert _val_is_numeric(-1.0)
    assert _val_is_numeric(1.0e-10)
    assert _val_is_numeric(-1.0e-10)
    assert _val_is_numeric(1.0e10)
    assert _val_is_numeric(-1.0e10)
    assert _val_is_numeric(1.0e-10)
    assert _val_is_numeric(-1.0e-10)

    # Test case 2: Non-numeric values
    assert not _val_is_numeric("a")
    assert not _val_is_numeric("1")
    assert not _val_is_numeric("1.0")
    assert not _val_is_numeric("1.0e-10")
    assert not _val_is_numeric("1.0e10")
    assert not _val_is_numeric(None)


@pytest.mark.xfail
def test_val_is_numeric_fails_list_input():
    with pytest.raises(ValueError):
        _val_is_numeric([1, 2, 3])


def test_val_is_str():
    # Test case 1: String values
    assert _val_is_str("a")
    assert _val_is_str("1")
    assert _val_is_str("1.0")
    assert _val_is_str("1.0e-10")
    assert _val_is_str("1.0e10")

    # Test case 2: Non-string values
    assert not _val_is_str(1)
    assert not _val_is_str(-1)
    assert not _val_is_str(1.0)
    assert not _val_is_str(-1.0)
    assert not _val_is_str(1.0e-10)
    assert not _val_is_str(-1.0e-10)
    assert not _val_is_str(1.0e10)
    assert not _val_is_str(-1.0e10)
    assert not _val_is_str(None)


@pytest.mark.xfail
def test_val_is_str_fails_list_input():
    with pytest.raises(ValueError):
        _val_is_str(["a", "b", "c"])


# TODO: add tests for _val_is_missing()


def test_is_integerlike():
    # Test case 1: Integer-like values
    assert _is_integerlike([1])
    assert _is_integerlike([-1])
    assert _is_integerlike([0])
    # assert _is_integerlike([1.0, 2.0, 3.0, 6.0]) # TODO: this should pass
    # assert _is_integerlike([-1.0]) # TODO: this should pass
    # assert _is_integerlike([2e15]) # TODO: this should pass
    # assert _is_integerlike([3.2343e15]) # TODO: this should pass
    assert _is_integerlike([0, 79])
    assert _is_integerlike([-234234, 0, 2343, 6342379])

    # Test case 2: Non-integer-like values
    assert not _is_integerlike([1.1])
    assert not _is_integerlike([1e-5])
    assert not _is_integerlike([-3, 4, 5.4])
    assert not _is_integerlike([])


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


@pytest.mark.parametrize(
    "name,dst",
    [
        ("min", 1),
        ("max", 4),
        ("median", 2.5),
        ("mean", 2.5),
    ],
)
def test_calc_ref_value(name: str, dst: float):
    res = calc_ref_value(name, [3, 1, 4, 2])
    assert res == dst


@pytest.mark.parametrize(
    "num,dst",
    [
        (1e-23, "1.0E−23"),
        (1.2363423e-23, "1.2E−23"),
        (1.9001e-20, "1.9E−20"),
        (1.243234e-10, "1.2E−10"),
        (0.002345322, "2.3E−30"),
        (0.074234, "0.074"),
        (0.32923, "0.33"),
        (0.3, "0.30"),
        (0.1, "0.10"),
        (0.99, "0.99"),
        (0.999999991, "1.0"),
        (0, "0"),
        (0.0000, "0"),
        (1, "1.00"),
        (1.2, "1.20"),
        (23.34, "23.3"),
        (999.823, "1,000"),
        (1002.62, "1.00K"),
        (56256.99345, "56.3K"),
        (262456.632, "262K"),
        (838238.123, "838K"),
        (9237442.4, "9.24M"),
        (23425521.8, "23.4M"),
        (682378385.0, "682M"),
        (7453473217.4, "7.45B"),
        (890236897525, "890B"),
        (3324986945826, "3.32T"),
        (367353689054245, "367T"),
        (8923749826567834, "8.9E15"),
        (90872346782346451237345, "9.1E22"),
        (-1.243234e-10, "−1.2E−10"),
        (-93456734587347958, "−9.3E16"),
    ],
)
def test_format_number_compactly_basic(num: float, dst: str):
    res = _format_number_compactly(val=num)
    assert res == dst


@pytest.mark.parametrize(
    "num,dst",
    [
        (1e-23, "1.0E−23"),
        (1.2363423e-23, "1.2E−23"),
        (1.9001e-20, "1.9E−20"),
        (1.243234e-10, "1.2E−10"),
        (0.002345322, "2.3E−30"),
        (0.074234, "0"),
        (0.32923, "0"),
        (0.3, "0"),
        (0.1, "0"),
        (0.99, "1"),
        (0.999999991, "1"),
        (0, "0"),
        (0.0000, "0"),
        (1, "1"),
        (1.2, "1"),
        (23.34, "23"),
        (999.823, "1,000"),
        (1002.62, "1.00K"),
        (56256.99345, "56.3K"),
        (262456.632, "262K"),
        (838238.123, "838K"),
        (9237442.4, "9.24M"),
        (23425521.8, "23.4M"),
        (682378385.0, "682M"),
        (7453473217.4, "7.45B"),
        (890236897525, "890B"),
        (3324986945826, "3.32T"),
        (367353689054245, "367T"),
        (8923749826567834, "8.9E15"),
        (90872346782346451237345, "9.1E22"),
        (-1.243234e-10, "−1.2E−10"),
        (-93456734587347958, "−9.3E16"),
    ],
)
def test_format_number_compactly_integer(num: float, dst: str):
    res = _format_number_compactly(val=num, as_integer=True)
    assert res == dst


@pytest.mark.parametrize(
    "num,currency,dst",
    [
        (1.243234e-10, "USD", "$0.00"),
        (0.002345322, "USD", "$0.00"),
        (0.074234, "USD", "$0.07"),
        (0.32923, "USD", "$0.33"),
        (0.3, "USD", "$0.30"),
        (0.1, "USD", "$0.10"),
        (0.99, "USD", "$0.99"),
        (0.999999991, "USD", "$1.00"),
        (0, "USD", "0"),
        (0.0000, "USD", "0"),
        (1, "USD", "$1.00"),
        (1.2, "USD", "$1.20"),
        (23.34, "USD", "$23.34"),
        (999.823, "USD", "$999.82"),
        (1002.62, "USD", "$1,002.62"),
        (56256.99345, "USD", "$56,257.0"),
        (262456.632, "USD", "$262,457"),
        (838238.123, "USD", "$838,238"),
        (9237442.4, "USD", "$9,237,442.4"),
        (23425521.8, "USD", "$23,425,521.8"),
        (682378385.0, "USD", "$682,378,385.0"),
        (7453473217.4, "USD", "$7,453,473,217.4"),
        (890236897525, "USD", "$890,236,897,525.0"),
        (3324986945826, "USD", "$3,324,986,945,826.0"),
        (367353689054245, "USD", "$367,353,689,054,245.0"),
        (8923749826567834, "USD", ">"),
        (90872346782346451237345, "USD", ">"),
        (-1.243234e-10, "USD", "−$0.00"),
        (-93456734587347958, "USD", ">"),
        (-642.34, "USD", "−$642.34"),
        (23534, "EUR", "&#8364;23,534.0"),
        (556.325, "KRW", "&#8361;556"),
        (82.63, "HKD", "HK$82.63"),
        (838238.123, None, "838K"),
    ],
)
def test_format_number_compactly_currency(num: float, currency: Union[str, None], dst: str):
    res = _format_number_compactly(val=num, currency=currency)
    assert res == dst
