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
    "decimals, x_out",
    [
        (0, ["1", "1", "1", "1", "1", "1", "1", "1", "1"]),
        (1, ["1.0", "1.2", "1.2", "1.2", "1.2", "1.2", "1.2", "1.2", "1.2"]),
        (2, ["1.00", "1.20", "1.23", "1.23", "1.23", "1.23", "1.23", "1.23", "1.23"]),
        (
            3,
            [
                "1.000",
                "1.200",
                "1.230",
                "1.234",
                "1.234",
                "1.235",
                "1.235",
                "1.235",
                "1.235",
            ],
        ),
        (
            4,
            [
                "1.0000",
                "1.2000",
                "1.2300",
                "1.2340",
                "1.2345",
                "1.2346",
                "1.2346",
                "1.2346",
                "1.2346",
            ],
        ),
        (
            5,
            [
                "1.00000",
                "1.20000",
                "1.23000",
                "1.23400",
                "1.23450",
                "1.23456",
                "1.23457",
                "1.23457",
                "1.23457",
            ],
        ),
        (
            6,
            [
                "1.000000",
                "1.200000",
                "1.230000",
                "1.234000",
                "1.234500",
                "1.234560",
                "1.234567",
                "1.234568",
                "1.234568",
            ],
        ),
        (
            7,
            [
                "1.0000000",
                "1.2000000",
                "1.2300000",
                "1.2340000",
                "1.2345000",
                "1.2345600",
                "1.2345670",
                "1.2345678",
                "1.2345679",
            ],
        ),
        (
            8,
            [
                "1.00000000",
                "1.20000000",
                "1.23000000",
                "1.23400000",
                "1.23450000",
                "1.23456000",
                "1.23456700",
                "1.23456780",
                "1.23456789",
            ],
        ),
        (
            9,
            [
                "1.000000000",
                "1.200000000",
                "1.230000000",
                "1.234000000",
                "1.234500000",
                "1.234560000",
                "1.234567000",
                "1.234567800",
                "1.234567890",
            ],
        ),
    ],
)
def test_fmt_number_basic_0(decimals: int, x_out: str):
    df = pd.DataFrame(
        {
            "x": [
                1,
                1.2,
                1.23,
                1.234,
                1.2345,
                1.23456,
                1.234567,
                1.2345678,
                1.23456789,
            ]
        }
    )

    # Expect that values in `x` are formatted to 2 decimal places
    gt = GT(df).fmt_number(columns="x", decimals=decimals)
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == x_out


@pytest.mark.parametrize(
    "decimals, x_out",
    [
        (0, ["0", "0", "0", "0", "0", "0", "0", "0", "0"]),
        (1, ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0"]),
        (2, ["0.00", "0.00", "0.00", "0.00", "0.00", "0.00", "0.00", "0.00", "0.00"]),
        (
            3,
            [
                "0.000",
                "0.000",
                "0.000",
                "0.000",
                "0.000",
                "0.000",
                "0.000",
                "0.000",
                "0.000",
            ],
        ),
        (
            4,
            [
                "0.0000",
                "0.0000",
                "0.0000",
                "0.0000",
                "0.0000",
                "0.0000",
                "0.0000",
                "0.0000",
                "0.0000",
            ],
        ),
        (
            5,
            [
                "0.00000",
                "0.00000",
                "0.00000",
                "0.00000",
                "0.00000",
                "0.00000",
                "0.00000",
                "0.00000",
                "0.00000",
            ],
        ),
        (
            6,
            [
                "0.000001",
                "0.000001",
                "0.000001",
                "0.000001",
                "0.000001",
                "0.000001",
                "0.000001",
                "0.000001",
                "0.000001",
            ],
        ),
        (
            7,
            [
                "0.0000010",
                "0.0000012",
                "0.0000012",
                "0.0000012",
                "0.0000012",
                "0.0000012",
                "0.0000012",
                "0.0000012",
                "0.0000012",
            ],
        ),
        (
            8,
            [
                "0.00000100",
                "0.00000120",
                "0.00000123",
                "0.00000123",
                "0.00000123",
                "0.00000123",
                "0.00000123",
                "0.00000123",
                "0.00000123",
            ],
        ),
        (
            9,
            [
                "0.000001000",
                "0.000001200",
                "0.000001230",
                "0.000001234",
                "0.000001234",
                "0.000001235",
                "0.000001235",
                "0.000001235",
                "0.000001235",
            ],
        ),
    ],
)
def test_fmt_number_basic_1(decimals: int, x_out: str):
    df = pd.DataFrame(
        {
            "x": [
                0.000001,
                0.0000012,
                0.00000123,
                0.000001234,
                0.0000012345,
                0.00000123456,
                0.000001234567,
                0.0000012345678,
                0.00000123456789,
            ]
        }
    )

    # Expect that values in `x` are formatted to 2 decimal places
    gt = GT(df).fmt_number(columns="x", decimals=decimals)
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == x_out


@pytest.mark.parametrize(
    "decimals, drop_trailing_zeros, drop_trailing_dec_mark, x_out",
    [
        (0, False, False, ["1.", "2."]),
        (0, False, True, ["1", "2"]),
        (0, True, False, ["1.", "2."]),
        (0, True, True, ["1", "2"]),
        (1, False, False, ["1.2", "2.3"]),
        (1, False, True, ["1.2", "2.3"]),
        (1, True, False, ["1.2", "2.3"]),
        (1, True, True, ["1.2", "2.3"]),
        (2, False, False, ["1.23", "2.35"]),
        (2, False, True, ["1.23", "2.35"]),
        (2, True, False, ["1.23", "2.35"]),
        (2, True, True, ["1.23", "2.35"]),
        (3, False, False, ["1.230", "2.345"]),
        (3, False, True, ["1.230", "2.345"]),
        (3, True, False, ["1.23", "2.345"]),
        (3, True, True, ["1.23", "2.345"]),
        (4, False, False, ["1.2300", "2.3450"]),
        (4, False, True, ["1.2300", "2.3450"]),
        (4, True, False, ["1.23", "2.345"]),
        (4, True, True, ["1.23", "2.345"]),
        (5, False, False, ["1.23000", "2.34500"]),
        (5, False, True, ["1.23000", "2.34500"]),
        (5, True, False, ["1.23", "2.345"]),
        (5, True, True, ["1.23", "2.345"]),
        (10, False, False, ["1.2300000000", "2.3450000000"]),
        (10, False, True, ["1.2300000000", "2.3450000000"]),
        (10, True, False, ["1.23", "2.345"]),
        (10, True, True, ["1.23", "2.345"]),
        # (20, False, False, ["1.23000000000000000000", "2.34500000000000000000"]), # <- doesn't work
        # (20, False, True, ["1.23000000000000000000", "2.34500000000000000000"]), # <- doesn't work
        # (20, True, False, ["1.23", "2.345"]), # <- doesn't work
        # (20, True, True, ["1.23", "2.345"]), # <- doesn't work
    ],
)
def test_fmt_number_drop_trailing(
    decimals: int, drop_trailing_zeros: bool, drop_trailing_dec_mark: bool, x_out: str
):
    df = pd.DataFrame({"x": [1.23, 2.345]})

    gt = GT(df).fmt_number(
        columns="x",
        decimals=decimals,
        drop_trailing_zeros=drop_trailing_zeros,
        drop_trailing_dec_mark=drop_trailing_dec_mark,
    )
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == x_out


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
        (0.00000000446453, "0.00000000446453"),
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
        ("4.46453E-9", "0.00000000446453"),
        ("1E+5", "100000"),
        ("1.5E+5", "150000"),
        ("150000", "150000"),
    ],
)
def test_expand_exponential_to_full_string(str_number: str, x_out: str):
    x = _expand_exponential_to_full_string(str_number=str_number)
    assert x == x_out


def test_format_number_with_sigfig():
    df = pd.DataFrame({"x": [1.23, 2.345]})
    gt = GT(df).fmt_number(
        columns="x",
        n_sigfig=2,
        drop_trailing_zeros=True,
        drop_trailing_dec_mark=False,
    )
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == ["1.2", "2.3"]


def test_format_number_with_sigfig_2():
    df = pd.DataFrame({"x": [0.000000000000000534, 9.123]})
    gt = GT(df).fmt_number(
        columns="x",
        n_sigfig=2,
        drop_trailing_zeros=True,
        drop_trailing_dec_mark=False,
    )
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == ["0.00000000000000053", "9.1"]
