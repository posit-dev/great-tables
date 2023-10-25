from typing import Union
import pandas as pd
import pytest

from gt import GT
from gt.gt import _get_column_of_values
from gt._formats import (
    _format_number_with_separator,
    _expand_exponential_to_full_string,
)


@pytest.mark.parametrize(
    "decimals, outcome",
    [(2, ["1.23", "2.35"]), (5, ["1.23400", "2.34500"]), (0, ["1", "2"])],
)
def test_fmt_number_basic(decimals: int, outcome: str):
    df = pd.DataFrame({"x": [1.234, 2.345], "y": [3.456, 4.567]})

    # Expect that values in `x` are formatted to 2 decimal places
    gt = GT(df).fmt_number(columns="x", decimals=decimals)
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == outcome


# TODO: parameterize this as above
def test_fmt_number_drop_trailing():
    df = pd.DataFrame({"x": [1.23, 2.345], "y": [3.456, 4.567]})

    gt = GT(df).fmt_number(
        columns="x",
        decimals=0,
        drop_trailing_zeros=False,
        drop_trailing_dec_mark=True,
    )
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == ["1", "2"]

    gt = GT(df).fmt_number(
        columns="x",
        decimals=0,
        drop_trailing_zeros=False,
        drop_trailing_dec_mark=False,
    )
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == ["1.", "2."]

    gt = GT(df).fmt_number(
        columns="x",
        decimals=4,
        drop_trailing_zeros=True,
        drop_trailing_dec_mark=False,
    )
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == ["1.23", "2.345"]

    gt = GT(df).fmt_number(
        columns="x",
        decimals=4,
        drop_trailing_zeros=False,
        drop_trailing_dec_mark=True,
    )
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == ["1.2300", "2.3450"]


# Test `_format_number_with_separator()` util function
@pytest.mark.parametrize(
    "number, x_out",
    [
        (8234252645325, "8,234,252,645,325"),
        (234252645325, "234,252,645,325"),
        (34252645325, "34,252,645,325"),
        (4252645325, "4,252,645,325"),
        (252645325, "252,645,325"),
        (52645325, "52,645,325"),
        (2645325, "2,645,325"),
        (645325, "645,325"),
        (45325, "45,325"),
        (5325, "5,325"),
        (325, "325"),
        (25, "25"),
        (5, "5"),
        (0, "0"),
        (2645325.234523, "2,645,325.234523"),
        (645325.234523, "645,325.234523"),
        (45325.234523, "45,325.234523"),
        (5325.234523, "5,325.234523"),
        (325.234523, "325.234523"),
        (25.234523, "25.234523"),
        (5.234523, "5.234523"),
        (0, "0"),
        (0.1, "0.1"),
        (0.01, "0.01"),
        (0.00023, "0.00023"),
        (0.000033, "0.000033"),
        # (0.00000000446453, "0.00000000446453"), <- doesn't work
        ("8234324.23", "8,234,324.23"),
        (
            "82534563535234324.233535303503503530530535",
            "82,534,563,535,234,324.233535303503503530530535",
        ),
    ],
)
def test_format_number_with_separator(number: Union[int, float, str], x_out: str):
    x = _format_number_with_separator(number=number, separator=",")
    assert x == x_out


# @pytest.mark.xfail("Doesn't work as well as imagined, we need a better implementation")
@pytest.mark.parametrize(
    "str_number, x_out",
    [
        ("1e-5", "0.00001"),
        ("1.5e-5", "0.000015"),
        ("-1e-5", "-0.00001"),
        ("-1.5e-5", "-0.000015"),
        ("1E-5", "0.00001"),
        ("1.5E-5", "0.000015"),
        ("-1E-5", "-0.00001"),
        ("-1.5E-5", "-0.000015"),
        # ("1E+5", "100000"),  # <- doesn't work
        # ("1.5E+5", "150000"),  # <- doesn't work
        ("150000", "150000"),
    ],
)
def test_expand_exponential_to_full_string(str_number: str, x_out: str):
    x = _expand_exponential_to_full_string(str_number=str_number)
    assert x == x_out
