from typing import Union
import pandas as pd
import polars as pl
import pytest
import re

from great_tables import GT
from great_tables.data import exibble
from great_tables.gt import _get_column_of_values
from great_tables._data_color.base import _html_color
from great_tables._utils_render_html import create_body_component_h
from great_tables._formats import (
    _format_number_fixed_decimals,
    _expand_exponential_to_full_string,
    fmt,
    FmtImage,
)
from great_tables._locations import RowSelectExpr


def assert_rendered_body(snapshot, gt):
    built = gt._build_data("html")
    body = create_body_component_h(built)

    assert snapshot == body


def assert_repr_html(snapshot, gt):
    body = gt._repr_html_()
    body = re.sub(r"^.*?<table (.*?)</table>.*$", r"\1", body, flags=re.DOTALL)

    assert snapshot == body


def test_format_fns():
    df = pd.DataFrame({"x": [1, 2]})
    gt = GT(df)
    new_gt = fmt(gt, fns=lambda x: str(x + 1), columns=["x"])

    formats_fn = new_gt._formats[0]

    res = list(map(formats_fn.func.default, df["x"]))
    assert res == ["2", "3"]


def test_format_snap(snapshot):
    new_gt = (
        GT(exibble)
        .fmt_currency(columns="currency")
        .fmt_scientific(columns="num")
        .fmt_date(columns="date", date_style="day_month_year")
    )

    assert_rendered_body(snapshot, new_gt)


def test_format_repr_snap(snapshot):
    new_gt = (
        GT(exibble)
        .fmt_currency(columns="currency")
        .fmt_scientific(columns="num")
        .fmt_date(columns="date", date_style="day_month_year")
    )

    assert_repr_html(snapshot, new_gt)


@pytest.mark.parametrize(
    "expr",
    [
        [1, 2],
        pl.col("x") > 0,
        lambda D: D["x"] > 0,
    ],
)
def test_format_row_selection(expr):
    df = pd.DataFrame({"x": [0, 1, 2]})

    if isinstance(expr, pl.Expr):
        gt = GT(pl.from_pandas(df))
    else:
        gt = GT(df)

    res = gt.fmt(lambda x: x, columns=[], rows=expr)
    assert len(res._formats) == 1
    assert res._formats[0].cells.rows == [1, 2]


@pytest.mark.parametrize(
    "scale_values, placement, incl_space, force_sign, x_out",
    [
        (
            True,
            "right",
            False,
            False,
            [
                "0.05%",
                "0.46%",
                "4.56%",
                "45.60%",
                "456.00%",
                "4,560.00%",
                "45,600.00%",
                "\u2212" + "4.68%",
                "0.00%",
            ],
        ),
        (
            False,
            "right",
            False,
            False,
            [
                "0.00%",
                "0.00%",
                "0.05%",
                "0.46%",
                "4.56%",
                "45.60%",
                "456.00%",
                "\u2212" + "0.05%",
                "0.00%",
            ],
        ),
        (
            False,
            "left",
            False,
            False,
            [
                "%0.00",
                "%0.00",
                "%0.05",
                "%0.46",
                "%4.56",
                "%45.60",
                "%456.00",
                "\u2212" + "%0.05",
                "%0.00",
            ],
        ),
        (
            False,
            "right",
            True,
            False,
            [
                "0.00 %",
                "0.00 %",
                "0.05 %",
                "0.46 %",
                "4.56 %",
                "45.60 %",
                "456.00 %",
                "\u2212" + "0.05 %",
                "0.00 %",
            ],
        ),
        (
            False,
            "left",
            True,
            False,
            [
                "% 0.00",
                "% 0.00",
                "% 0.05",
                "% 0.46",
                "% 4.56",
                "% 45.60",
                "% 456.00",
                "\u2212" + "% 0.05",
                "% 0.00",
            ],
        ),
        (
            False,
            "left",
            True,
            True,
            [
                "+% 0.00",
                "+% 0.00",
                "+% 0.05",
                "+% 0.46",
                "+% 4.56",
                "+% 45.60",
                "+% 456.00",
                "\u2212" + "% 0.05",
                "% 0.00",
            ],
        ),
        (
            False,
            "left",
            False,
            True,
            [
                "+%0.00",
                "+%0.00",
                "+%0.05",
                "+%0.46",
                "+%4.56",
                "+%45.60",
                "+%456.00",
                "\u2212" + "%0.05",
                "%0.00",
            ],
        ),
        (
            False,
            "right",
            True,
            True,
            [
                "+0.00 %",
                "+0.00 %",
                "+0.05 %",
                "+0.46 %",
                "+4.56 %",
                "+45.60 %",
                "+456.00 %",
                "\u2212" + "0.05 %",
                "0.00 %",
            ],
        ),
        (
            False,
            "right",
            False,
            True,
            [
                "+0.00%",
                "+0.00%",
                "+0.05%",
                "+0.46%",
                "+4.56%",
                "+45.60%",
                "+456.00%",
                "\u2212" + "0.05%",
                "0.00%",
            ],
        ),
    ],
)
def test_fmt_percent_basic_0(
    scale_values: bool, placement: str, incl_space: bool, force_sign: bool, x_out: str
):
    df = pd.DataFrame({"x": [0.000456, 0.00456, 0.0456, 0.456, 4.56, 45.6, 456, -0.0468, 0]})

    # Expect that values in `x` are formatted correctly when varying the
    # number of fixed decimal places (`decimals`)
    gt = GT(df).fmt_percent(
        columns="x",
        scale_values=scale_values,
        force_sign=force_sign,
        placement=placement,
        incl_space=incl_space,
    )
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == x_out


@pytest.mark.parametrize(
    "decimals, x_out",
    [
        (0, ["1", "1", "1", "1", "1", "1", "1", "1", "1"]),
        (1, ["1.0", "1.2", "1.2", "1.2", "1.2", "1.2", "1.2", "1.2", "1.2"]),
        (2, ["1.00", "1.20", "1.23", "1.23", "1.23", "1.23", "1.23", "1.23", "1.23"]),
        (3, ["1.000", "1.200", "1.230", "1.234", "1.234", "1.235", "1.235", "1.235", "1.235"]),
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

    # Expect that values in `x` are formatted correctly when varying the
    # number of fixed decimal places (`decimals`)
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

    # Expect that the smaller values in `x` are formatted correctly when
    # varying the number of fixed decimal places (`decimals`)
    gt = GT(df).fmt_number(columns="x", decimals=decimals)
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == x_out


@pytest.mark.parametrize(
    "n_sigfig, x_out",
    [
        (
            1,
            [
                "0.000001",
                "0.000001",
                "0.000001",
                "0.000001",
                "0.000001",
                "100,000",
                "100,000",
                "100,000",
                "100,000",
                "100,000",
            ],
        ),
        (
            2,
            [
                "0.0000010",
                "0.0000012",
                "0.0000012",
                "0.0000012",
                "0.0000012",
                "120,000",
                "120,000",
                "120,000",
                "120,000",
                "120,000",
            ],
        ),
        (
            3,
            [
                "0.00000100",
                "0.00000120",
                "0.00000123",
                "0.00000123",
                "0.00000123",
                "123,000",
                "123,000",
                "123,000",
                "123,000",
                "123,000",
            ],
        ),
        (
            4,
            [
                "0.000001000",
                "0.000001200",
                "0.000001230",
                "0.000001234",
                "0.000001234",
                "123,400",
                "123,500",
                "123,500",
                "123,500",
                "123,500",
            ],
        ),
        (
            5,
            [
                "0.0000010000",
                "0.0000012000",
                "0.0000012300",
                "0.0000012340",
                "0.0000012345",
                "123,450",
                "123,460",
                "123,460",
                "123,460",
                "123,460",
            ],
        ),
        (
            6,
            [
                "0.00000100000",
                "0.00000120000",
                "0.00000123000",
                "0.00000123400",
                "0.00000123450",
                "123,450",
                "123,457",
                "123,457",
                "123,457",
                "123,457",
            ],
        ),
        (
            7,
            [
                "0.000001000000",
                "0.000001200000",
                "0.000001230000",
                "0.000001234000",
                "0.000001234500",
                "123,450.0",
                "123,456.7",
                "123,456.8",
                "123,456.8",
                "123,456.8",
            ],
        ),
        (
            8,
            [
                "0.0000010000000",
                "0.0000012000000",
                "0.0000012300000",
                "0.0000012340000",
                "0.0000012345000",
                "123,450.00",
                "123,456.70",
                "123,456.76",
                "123,456.76",
                "123,456.77",
            ],
        ),
        (
            9,
            [
                "0.00000100000000",
                "0.00000120000000",
                "0.00000123000000",
                "0.00000123400000",
                "0.00000123450000",
                "123,450.000",
                "123,456.700",
                "123,456.760",
                "123,456.765",
                "123,456.765",
            ],
        ),
        (
            10,
            [
                "0.000001000000000",
                "0.000001200000000",
                "0.000001230000000",
                "0.000001234000000",
                "0.000001234500000",
                "123,450.0000",
                "123,456.7000",
                "123,456.7600",
                "123,456.7650",
                "123,456.7654",
            ],
        ),
        (
            11,
            [
                "0.0000010000000000",
                "0.0000012000000000",
                "0.0000012300000000",
                "0.0000012340000000",
                "0.0000012345000000",
                "123,450.00000",
                "123,456.70000",
                "123,456.76000",
                "123,456.76500",
                "123,456.76540",
            ],
        ),
        (
            12,
            [
                "0.00000100000000000",
                "0.00000120000000000",
                "0.00000123000000000",
                "0.00000123400000000",
                "0.00000123450000000",
                "123,450.000000",
                "123,456.700000",
                "123,456.760000",
                "123,456.765000",
                "123,456.765400",
            ],
        ),
    ],
)
def test_fmt_number_n_sigfig(n_sigfig: int, x_out: str):
    df = pd.DataFrame(
        {
            "x": [
                0.000001,
                0.0000012,
                0.00000123,
                0.000001234,
                0.0000012345,
                123450,
                123456.7,
                123456.76,
                123456.765,
                123456.7654,
            ]
        }
    )

    # Expect that values in `x` are formatted correctly when varying the
    # number of significant digits (`n_sigfig`)
    gt = GT(df).fmt_number(columns="x", n_sigfig=n_sigfig)
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == x_out


# TODO: Expect that the `drop_trailing_zeros` argument is ignored when formatting
# to a fixed number of signficant digits


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
def test_fmt_number_drop_trailing_00(
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


@pytest.mark.parametrize(
    "n_sigfig, drop_trailing_zeros, drop_trailing_dec_mark, x_out",
    [
        (1, False, False, ["1.", "2."]),
        (1, False, True, ["1", "2"]),
        (1, True, False, ["1.", "2."]),
        (1, True, True, ["1", "2"]),
        (2, False, False, ["1.2", "2.3"]),
        (2, False, True, ["1.2", "2.3"]),
        (2, True, False, ["1.2", "2.3"]),
        (2, True, True, ["1.2", "2.3"]),
        (3, False, False, ["1.23", "2.35"]),
        (3, False, True, ["1.23", "2.35"]),
        (3, True, False, ["1.23", "2.35"]),
        (3, True, True, ["1.23", "2.35"]),
    ],
)
def test_fmt_number_drop_trailing_01(
    n_sigfig: int, drop_trailing_zeros: bool, drop_trailing_dec_mark: bool, x_out: str
):
    df = pd.DataFrame({"x": [1.23, 2.345]})

    gt = GT(df).fmt_number(
        columns="x",
        n_sigfig=n_sigfig,
        drop_trailing_zeros=drop_trailing_zeros,
        drop_trailing_dec_mark=drop_trailing_dec_mark,
    )
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == x_out


@pytest.mark.parametrize(
    "n_sigfig, use_seps, sep_mark, dec_mark, x_out",
    [
        (1, True, ",", ".", ["1,000,000", "\u2212" + "5,000"]),
        (1, True, ".", ",", ["1.000.000", "\u2212" + "5.000"]),
        (1, True, "  ", "/", ["1  000  000", "\u2212" + "5  000"]),
        (1, True, "", "", ["1000000", "\u2212" + "5000"]),
        (1, False, ",", ".", ["1000000", "\u2212" + "5000"]),
        (1, False, ".", ",", ["1000000", "\u2212" + "5000"]),
        (1, False, "  ", "/", ["1000000", "\u2212" + "5000"]),
        (1, False, "", "", ["1000000", "\u2212" + "5000"]),
        (3, True, ",", ".", ["1,230,000", "\u2212" + "5,430"]),
        (3, True, ".", ",", ["1.230.000", "\u2212" + "5.430"]),
        (3, True, "  ", "/", ["1  230  000", "\u2212" + "5  430"]),
        (3, True, "", "", ["1230000", "\u2212" + "5430"]),
        (3, False, ",", ".", ["1230000", "\u2212" + "5430"]),
        (3, False, ".", ",", ["1230000", "\u2212" + "5430"]),
        (3, False, "  ", "/", ["1230000", "\u2212" + "5430"]),
        (3, False, "", "", ["1230000", "\u2212" + "5430"]),
        (5, True, ",", ".", ["1,234,600", "\u2212" + "5,432.4"]),
        (5, True, ".", ",", ["1.234.600", "\u2212" + "5.432,4"]),
        (5, True, "  ", "/", ["1  234  600", "\u2212" + "5  432/4"]),
        (5, True, "", "", ["1234600", "\u2212" + "54324"]),
        (5, False, ",", ".", ["1234600", "\u2212" + "5432.4"]),
        (5, False, ".", ",", ["1234600", "\u2212" + "5432,4"]),
        (5, False, "  ", "/", ["1234600", "\u2212" + "5432/4"]),
        (5, False, "", "", ["1234600", "\u2212" + "54324"]),
        (7, True, ",", ".", ["1,234,567", "\u2212" + "5,432.370"]),
        (7, True, ".", ",", ["1.234.567", "\u2212" + "5.432,370"]),
        (7, True, "  ", "/", ["1  234  567", "\u2212" + "5  432/370"]),
        (7, True, "", "", ["1234567", "\u2212" + "5432370"]),
        (7, False, ",", ".", ["1234567", "\u2212" + "5432.370"]),
        (7, False, ".", ",", ["1234567", "\u2212" + "5432,370"]),
        (7, False, "  ", "/", ["1234567", "\u2212" + "5432/370"]),
        (7, False, "", "", ["1234567", "\u2212" + "5432370"]),
        (9, True, ",", ".", ["1,234,567.00", "\u2212" + "5,432.37000"]),
        (9, True, ".", ",", ["1.234.567,00", "\u2212" + "5.432,37000"]),
        (9, True, "  ", "/", ["1  234  567/00", "\u2212" + "5  432/37000"]),
        (9, True, "", "", ["123456700", "\u2212" + "543237000"]),
        (9, False, ",", ".", ["1234567.00", "\u2212" + "5432.37000"]),
        (9, False, ".", ",", ["1234567,00", "\u2212" + "5432,37000"]),
        (9, False, "  ", "/", ["1234567/00", "\u2212" + "5432/37000"]),
        (9, False, "", "", ["123456700", "\u2212" + "543237000"]),
    ],
)
def test_fmt_number_n_sigfig_seps(
    n_sigfig: int, use_seps: bool, sep_mark: str, dec_mark: str, x_out: str
):
    df = pd.DataFrame({"x": [1234567, -5432.37]})

    gt = GT(df).fmt_number(
        columns="x",
        n_sigfig=n_sigfig,
        use_seps=use_seps,
        sep_mark=sep_mark,
        dec_mark=dec_mark,
    )
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == x_out


@pytest.mark.parametrize(
    "force_sign, x_out",
    [
        (
            False,
            [
                "\u2212" + "234.654",
                "\u2212" + "0.001",
                "\u2212" + "0.100",
                "0.000",
                "12,354.300",
                "9,939,293,923.230",
            ],
        ),
        (
            True,
            [
                "\u2212" + "234.654",
                "\u2212" + "0.001",
                "\u2212" + "0.100",
                "0.000",
                "+12,354.300",
                "+9,939,293,923.230",
            ],
        ),
    ],
)
def test_fmt_number_force_sign(force_sign: bool, x_out: str):
    df = pd.DataFrame({"x": [-234.654, -0.000634, -0.1, 0, 12354.3, 9939293923.23]})

    gt = GT(df).fmt_number(columns="x", decimals=3, force_sign=force_sign)
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == x_out


@pytest.mark.parametrize(
    "pattern, x_out",
    [
        ("{x}", ["\u2212" + "234.65", "0.00", "25,342.00"]),
        ("a{x}b", ["a" + "\u2212" + "234.65b", "a0.00b", "a25,342.00b"]),
        (
            "  a {x} b {x} c  ",
            [
                "  a " + "\u2212" + "234.65 b " + "\u2212" + "234.65 c  ",
                "  a 0.00 b 0.00 c  ",
                "  a 25,342.00 b 25,342.00 c  ",
            ],
        ),
        ("{x}{x}", ["\u2212" + "234.65" + "\u2212" + "234.65", "0.000.00", "25,342.0025,342.00"]),
        (
            "#4$!|-_+%^&$*#{x}",
            [
                "#4$!|-_+%^&$*#" + "\u2212" + "234.65",
                "#4$!|-_+%^&$*#0.00",
                "#4$!|-_+%^&$*#25,342.00",
            ],
        ),
        (
            "{xx}{{x}}{xx}",
            ["{xx}{" + "\u2212" + "234.65}{xx}", "{xx}{0.00}{xx}", "{xx}{25,342.00}{xx}"],
        ),
    ],
)
def test_fmt_number_pattern(pattern: str, x_out: str):
    df = pd.DataFrame({"x": [-234.654, 0, 25342]})

    gt = GT(df).fmt_number(columns="x", decimals=2, pattern=pattern)
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == x_out


# Test `_format_number_fixed_decimals()` util function
@pytest.mark.parametrize(
    "value, x_out",
    [
        (8234252645325, "8,234,252,645,325.00"),
        (234252645325, "234,252,645,325.00"),
        (34252645325, "34,252,645,325.00"),
        (4252645325, "4,252,645,325.00"),
        (252645325, "252,645,325.00"),
        (52645325, "52,645,325.00"),
        (2645325, "2,645,325.00"),
        (645325, "645,325.00"),
        (45325, "45,325.00"),
        (5325, "5,325.00"),
        (325, "325.00"),
        (25, "25.00"),
        (5, "5.00"),
        (0, "0.00"),
        (2645325.234523, "2,645,325.23"),
        (645325.234523, "645,325.23"),
        (45325.234523, "45,325.23"),
        (5325.234523, "5,325.23"),
        (325.234523, "325.23"),
        (25.234523, "25.23"),
        (5.234523, "5.23"),
        (0, "0.00"),
        (0.1, "0.10"),
        (0.01, "0.01"),
        (0.00023, "0.00"),
        (0.000033, "0.00"),
        (0.00000000446453, "0.00"),
    ],
)
def test_format_number_fixed_decimals(value: Union[int, float], x_out: str):
    x = _format_number_fixed_decimals(value=value, decimals=2, sep_mark=",")
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


def test_format_number_with_sep_dec_marks():
    df = pd.DataFrame({"x": [12345678.12345678, 1.0, 0, -12345678.12345678]})
    gt = GT(df).fmt_number(columns="x", decimals=5, sep_mark=".", dec_mark=",")
    x = _get_column_of_values(gt, column_name="x", context="html")
    assert x == ["12.345.678,12346", "1,00000", "0,00000", "\u2212" + "12.345.678,12346"]


# ------------------------------------------------------------------------------
# Test `data_color()` and util functions
# ------------------------------------------------------------------------------


@pytest.fixture
def df_color():
    df = pd.DataFrame(
        {
            "A": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "B": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            "C": ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"],
        }
    )
    return df


@pytest.mark.parametrize(
    "color, x_out",
    [
        ("red", "#FF0000"),
        ("#FFF", "#FFFFFF"),
        ("crimson", "#DC143C"),
        ("SteelBlue", "#4682B4"),
        ("RED", "#FF0000"),
        ("#FFFFFF", "#FFFFFF"),
        ("transparent", "#FFFFFF00"),
    ],
)
def test_html_color(color: str, x_out: str):
    x = _html_color(colors=[color])
    assert x == [x_out]


@pytest.mark.parametrize(
    "color, x_out, alpha",
    [
        ("red", "#FF0000D8", 0.85),
        ("#DEF", "#DDEEFFD8", 0.85),
        ("crimson", "#DC143CD8", 0.85),
        ("SteelBlue", "#4682B4D8", 0.85),
        ("RED", "#FF0000D8", 0.85),
        ("#FFFFFF", "#FFFFFFD8", 0.85),
        ("transparent", "#FFFFFF00", 0.85),
        ("#FFFFFF00", "#FFFFFF00", 0.85),
    ],
)
def test_html_color_with_alpha(color: str, x_out: str, alpha: float):
    x = _html_color(colors=[color], alpha=alpha)
    assert x == [x_out]


def test_fmt_image_single():
    formatter = FmtImage(sep=" ", file_pattern="{}.svg", encode=False)
    res = formatter.to_html("/a")
    dst = formatter.SPAN_TEMPLATE.format('<img src="/a.svg" style="vertical-align: middle;">')

    assert res == dst


def test_fmt_image_multiple():
    formatter = FmtImage(sep="---", file_pattern="{}.svg", encode=False)
    res = formatter.to_html("/a,/b")
    dst = formatter.SPAN_TEMPLATE.format(
        '<img src="/a.svg" style="vertical-align: middle;">'
        "---"
        '<img src="/b.svg" style="vertical-align: middle;">'
    )

    assert res == dst


def test_fmt_image_encode(tmpdir):
    from base64 import b64encode
    from pathlib import Path

    content = "abc"
    p_svg = Path(tmpdir) / "some.svg"
    p_svg.write_text(content)

    formatter = FmtImage(sep=" ", file_pattern="{}.svg", encode=True)
    res = formatter.to_html(f"{tmpdir}/some")

    b64_content = b64encode(content.encode()).decode()
    img_src = f"data: image/svg+xml; base64,{b64_content}"
    dst = formatter.SPAN_TEMPLATE.format(f'<img src="{img_src}" style="vertical-align: middle;">')

    assert res == dst


def test_fmt_image_width_height_str():
    formatter = FmtImage(encode=False, width="20px", height="30px")
    res = formatter.to_html("/a")
    dst_img = '<img src="/a" style="height: 30px;width: 20px;vertical-align: middle;">'
    dst = formatter.SPAN_TEMPLATE.format(dst_img)

    assert res == dst


def test_fmt_image_height_int():
    formatter = FmtImage(encode=False, height=30)
    res = formatter.to_html("/a")
    dst_img = '<img src="/a" style="height: 30px;vertical-align: middle;">'
    dst = formatter.SPAN_TEMPLATE.format(dst_img)

    assert res == dst


def test_fmt_image_width_int():
    formatter = FmtImage(encode=False, width=20)

    with pytest.raises(NotImplementedError):
        formatter.to_html("/a")


def test_fmt_image_path():
    formatter = FmtImage(encode=False, path="/a/b")
    res = formatter.to_html("c")
    assert 'src="/a/b/c"' in res
