import pandas as pd
import polars as pl
import pytest

from great_tables import GT, vals
from great_tables._formats import _group_integer_digits
from great_tables.gt import _get_column_of_values

INF = float("inf")


@pytest.mark.parametrize(
    "integer_part, intl, ind",
    [
        ("0", "0", "0"),
        ("999", "999", "999"),
        ("1000", "1,000", "1,000"),
        ("12345", "12,345", "12,345"),
        ("123456", "123,456", "1,23,456"),
        ("1234567", "1,234,567", "12,34,567"),
        ("12345678", "12,345,678", "1,23,45,678"),
        ("123456789", "123,456,789", "12,34,56,789"),
        ("1234567890", "1,234,567,890", "1,23,45,67,890"),
    ],
)
def test_group_integer_digits(integer_part: str, intl: str, ind: str):
    assert _group_integer_digits(integer_part, sep_mark=",") == intl
    assert _group_integer_digits(integer_part, sep_mark=",", system="intl") == intl
    assert _group_integer_digits(integer_part, sep_mark=",", system="ind") == ind


class TestFmtNumberInd:
    def test_digit_lengths(self):
        values = [0.0, 999, 1000, 12345, 123456, 1234567, 12345678, 123456789, 1234567890]
        assert vals.fmt_number(values, system="ind") == [
            "0.00",
            "999.00",
            "1,000.00",
            "12,345.00",
            "1,23,456.00",
            "12,34,567.00",
            "1,23,45,678.00",
            "12,34,56,789.00",
            "1,23,45,67,890.00",
        ]

    def test_negative_and_fractional_values(self):
        assert vals.fmt_number([-1234567.89, 0.5, 99999.995], system="ind") == [
            "−12,34,567.89",
            "0.50",
            "99,999.99",
        ]

    def test_intl_is_default(self):
        values = [1234567.89, -1234567890]
        assert vals.fmt_number(values) == vals.fmt_number(values, system="intl")
        assert vals.fmt_number(values) == ["1,234,567.89", "−1,234,567,890.00"]

    def test_n_sigfig(self):
        assert vals.fmt_number([12345, 123456, 1234567], system="ind", n_sigfig=3) == [
            "12,300",
            "1,23,000",
            "12,30,000",
        ]

    def test_decimals_and_drop_trailing_zeros(self):
        assert vals.fmt_number([1234567.5], system="ind", decimals=3) == ["12,34,567.500"]
        assert vals.fmt_number([1234567.5], system="ind", drop_trailing_zeros=True) == [
            "12,34,567.5"
        ]

    def test_force_sign_and_accounting(self):
        assert vals.fmt_number([1234567], system="ind", force_sign=True) == ["+12,34,567.00"]
        assert vals.fmt_number([-1234567.89], system="ind", accounting=True) == ["(12,34,567.89)"]

    def test_scale_by_and_pattern(self):
        assert vals.fmt_number([1234.567], system="ind", scale_by=1000, pattern="₹{x}") == [
            "₹12,34,567.00"
        ]

    def test_marks_are_respected(self):
        assert vals.fmt_number([1234567.5], system="ind", sep_mark=" ", dec_mark=",") == [
            "12 34 567,50"
        ]
        assert vals.fmt_number([1234567.5], system="ind", locale="de") == ["12.34.567,50"]
        assert vals.fmt_number([1234567.5], system="ind", use_seps=False) == ["1234567.50"]

    def test_min_sep_threshold(self):
        assert vals.fmt_number([1234, 12345, 123456], system="ind", min_sep_threshold=2) == [
            "1234.00",
            "12,345.00",
            "1,23,456.00",
        ]

    def test_infinite_values(self):
        assert vals.fmt_number([INF, -INF], system="ind") == vals.fmt_number([INF, -INF])


class TestFmtIntegerInd:
    def test_values(self):
        assert vals.fmt_integer([123456, -1234567.89, 99999.995], system="ind") == [
            "1,23,456",
            "−12,34,568",
            "1,00,000",
        ]

    def test_intl_is_default(self):
        assert vals.fmt_integer([1234567]) == vals.fmt_integer([1234567], system="intl")
        assert vals.fmt_integer([1234567]) == ["1,234,567"]

    def test_marks_are_respected(self):
        assert vals.fmt_integer([1234567], system="ind", sep_mark=".") == ["12.34.567"]
        assert vals.fmt_integer([1234567], system="ind", locale="fr") == ["12 34 567"]
        assert vals.fmt_integer([1234567], system="ind", use_seps=False) == ["1234567"]

    def test_force_sign_and_accounting(self):
        assert vals.fmt_integer([1234567], system="ind", force_sign=True) == ["+12,34,567"]
        assert vals.fmt_integer([-1234567], system="ind", accounting=True) == ["(12,34,567)"]


class TestCompactInd:
    def test_fmt_number_suffixes(self):
        values = [12345, 123456, 1234567, 12345678, 123456789, 1234567890, -1234567]
        assert vals.fmt_number(values, system="ind", compact=True) == [
            "12,345.00",
            "1.23 Lac",
            "12.35 Lac",
            "1.23 Cr",
            "12.35 Cr",
            "123.46 Cr",
            "−12.35 Lac",
        ]

    def test_fmt_integer_suffixes(self):
        values = [123456, 1234567, 12345678, 1234567890]
        assert vals.fmt_integer(values, system="ind", compact=True) == [
            "1 Lac",
            "12 Lac",
            "1 Cr",
            "123 Cr",
        ]

    def test_crores_are_the_largest_unit(self):
        # A lakh crore stays in crores, which are grouped in the Indian system as well
        assert vals.fmt_number([1e12, 1e15], system="ind", compact=True) == [
            "1,00,000.00 Cr",
            "10,00,00,000.00 Cr",
        ]

    def test_values_below_a_lakh_have_no_suffix(self):
        assert vals.fmt_number([0, 0.5, 999, 99999.99], system="ind", compact=True) == [
            "0",
            "0.50",
            "999.00",
            "99,999.99",
        ]

    def test_rounding_carries_to_the_next_unit(self):
        # 99,999.995 would otherwise give `1,00,000` without a suffix, and 99,99,999.996 would
        # give `100.00 Lac`
        assert vals.fmt_integer([99999.995, -99999.995], system="ind", compact=True) == [
            "1 Lac",
            "−1 Lac",
        ]
        assert vals.fmt_number([9999999.996], system="ind", compact=True) == ["1.00 Cr"]
        assert vals.fmt_number([9949999, 9999999.4], system="ind", compact=True, decimals=0) == [
            "99 Lac",
            "1 Cr",
        ]
        assert vals.fmt_number([99950], system="ind", compact=True, n_sigfig=3) == ["1.00 Lac"]

    def test_n_sigfig_and_drop_trailing_zeros(self):
        assert vals.fmt_number([1234567], system="ind", compact=True, n_sigfig=2) == ["12 Lac"]
        assert vals.fmt_number(
            [1000000, 12500000], system="ind", compact=True, drop_trailing_zeros=True
        ) == ["10 Lac", "1.25 Cr"]

    def test_marks_are_respected(self):
        assert vals.fmt_number([1234567], system="ind", compact=True, locale="de") == ["12,35 Lac"]
        assert vals.fmt_number([1e12], system="ind", compact=True, sep_mark=" ") == [
            "1 00 000.00 Cr"
        ]

    def test_force_sign_and_accounting(self):
        assert vals.fmt_number([1234567], system="ind", compact=True, force_sign=True) == [
            "+12.35 Lac"
        ]
        assert vals.fmt_number([-1234567], system="ind", compact=True, accounting=True) == [
            "(12.35 Lac)"
        ]

    def test_infinite_values_have_no_suffix(self):
        expected = vals.fmt_number([INF, -INF])
        assert vals.fmt_number([INF, -INF], system="ind", compact=True) == expected
        assert vals.fmt_integer([INF, -INF], system="ind", compact=True) == vals.fmt_integer(
            [INF, -INF]
        )

    def test_intl_suffixes_are_unchanged(self):
        values = [0.5, 999, 999999, 1234567, 1.5e9, -1e16, 1e20]
        assert vals.fmt_number(values, compact=True) == [
            "0.50",
            "999.00",
            "1.00M",
            "1.23M",
            "1.50B",
            "−10.00Q",
            "100,000.00Q",
        ]
        assert vals.fmt_number(values, compact=True) == vals.fmt_number(
            values, compact=True, system="intl"
        )


@pytest.mark.parametrize("frame", [pl.DataFrame, pd.DataFrame])
def test_gt_methods(frame):
    gt = (
        GT(frame({"x": [1234567.0, -12345678.0], "y": [1234567.0, -12345678.0]}))
        .fmt_number(columns="x", system="ind")
        .fmt_integer(columns="y", system="ind", compact=True)
    )

    assert _get_column_of_values(gt, column_name="x", context="html") == [
        "12,34,567.00",
        "−1,23,45,678.00",
    ]
    assert _get_column_of_values(gt, column_name="y", context="html") == [
        "12 Lac",
        "−1 Cr",
    ]


def test_latex_output():
    gt = GT(pl.DataFrame({"x": [1234567.0, -12345678.0]}))

    assert _get_column_of_values(
        gt.fmt_number(columns="x", system="ind"), column_name="x", context="latex"
    ) == ["12,34,567.00", "-1,23,45,678.00"]
    assert _get_column_of_values(
        gt.fmt_number(columns="x", system="ind", compact=True), column_name="x", context="latex"
    ) == ["12.35 Lac", "-1.23 Cr"]


@pytest.mark.parametrize("system", ["foo", "IND", "international", None])
def test_invalid_system_raises(system):
    gt = GT(pl.DataFrame({"x": [1.0]}))

    with pytest.raises(ValueError, match="`system` must be either 'intl' or 'ind'"):
        gt.fmt_number(columns="x", system=system)
    with pytest.raises(ValueError, match="`system` must be either 'intl' or 'ind'"):
        gt.fmt_integer(columns="x", system=system)
    with pytest.raises(ValueError, match="`system` must be either 'intl' or 'ind'"):
        vals.fmt_number([1.0], system=system)
    with pytest.raises(ValueError, match="`system` must be either 'intl' or 'ind'"):
        vals.fmt_integer([1.0], system=system)
