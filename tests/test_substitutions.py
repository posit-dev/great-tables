from math import nan

import numpy as np
import pandas as pd
import polars as pl
import pyarrow as pa
import polars.testing
import pytest
from great_tables import GT
from great_tables._gt_data import FormatterSkipElement
from great_tables._substitution import SubMissing, SubZero, SubSmallVals, SubLargeVals, SubValues
from great_tables._tbl_data import DataFrameLike, to_list

params_frames = [
    pytest.param(pd.DataFrame, id="pandas"),
    pytest.param(pl.DataFrame, id="polars"),
    pytest.param(pa.table, id="arrow"),
]


@pytest.fixture(params=params_frames, scope="function")
def df(request) -> DataFrameLike:
    return request.param({"col1": [None, nan, 0]})


@pytest.fixture(params=params_frames, scope="function")
def df_empty(request) -> DataFrameLike:
    return request.param({})


def assert_frame_equal(src: DataFrameLike, target: DataFrameLike):
    if isinstance(src, pd.DataFrame):
        pd.testing.assert_frame_equal(src, target)
    elif isinstance(src, pl.DataFrame):
        pl.testing.assert_frame_equal(src, target)
    else:
        raise NotImplementedError(f"Unsupported data type: {type(src)}")


def assert_series_equals(src, target: list):
    # polars is kind and converts its null type to None, but
    # pandas needs the NA -> None to be done manually.
    fixed = [None if x is pd.NA else x for x in to_list(src)]
    assert fixed == target


@pytest.mark.parametrize("el", [None, nan, np.nan])
def test_sub_missing_el(df_empty: DataFrameLike, el):
    # df just being used as constructor
    assert SubMissing(df_empty, "---").to_html(el) == "---"


def test_sub_missing_el_skip(df_empty: DataFrameLike):
    assert isinstance(SubMissing(df_empty, "---").to_html(0), FormatterSkipElement)


def test_sub_missing_meth(df):
    new_gt = GT(df).sub_missing("col1", missing_text="--")._render_formats("html")
    assert_series_equals(new_gt._body.body["col1"], ["--", "--", None])


def test_sub_missing_meth_implicit_columns(df):
    # Drive by: https://github.com/posit-dev/great-tables/issues/667
    new_gt = GT(df).sub_missing(missing_text="--")._render_formats("html")
    assert_series_equals(new_gt._body.body["col1"], ["--", "--", None])


@pytest.mark.parametrize("el", [0, 0.0])
def test_sub_zero_el(el):
    assert SubZero("--").to_html(el) == "--"


def test_sub_zero_el_skip():
    assert isinstance(SubZero("--").to_html(1), FormatterSkipElement)


def test_sub_zero_meth(df):
    new_gt = GT(df).sub_zero("col1", zero_text="no")._render_formats("html")
    assert_series_equals(new_gt._body.body["col1"], [None, None, "no"])


# =============================================================================
# sub_small_vals() tests
# =============================================================================


class TestSubSmallVals:
    """Tests for sub_small_vals()."""

    def test_basic_positive_default_threshold(self):
        """Values between 0 and 0.01 (exclusive) are substituted."""
        subber = SubSmallVals(threshold=0.01, small_pattern="<{x}", sign="+")
        assert subber.to_html(0.001) == "&lt;0.01"
        assert subber.to_html(0.009) == "&lt;0.01"

    def test_threshold_excluded(self):
        """The threshold value itself is NOT substituted."""
        subber = SubSmallVals(threshold=0.01, small_pattern="<{x}", sign="+")
        assert isinstance(subber.to_html(0.01), FormatterSkipElement)

    def test_zero_excluded(self):
        """Zero is NOT substituted (use sub_zero for that)."""
        subber = SubSmallVals(threshold=0.01, small_pattern="<{x}", sign="+")
        assert isinstance(subber.to_html(0), FormatterSkipElement)
        assert isinstance(subber.to_html(0.0), FormatterSkipElement)

    def test_large_positive_skipped(self):
        """Values >= threshold are not substituted."""
        subber = SubSmallVals(threshold=0.01, small_pattern="<{x}", sign="+")
        assert isinstance(subber.to_html(0.1), FormatterSkipElement)
        assert isinstance(subber.to_html(1.0), FormatterSkipElement)
        assert isinstance(subber.to_html(100), FormatterSkipElement)

    def test_negative_values_skipped_with_positive_sign(self):
        """Negative values are not substituted when sign='+'."""
        subber = SubSmallVals(threshold=0.01, small_pattern="<{x}", sign="+")
        assert isinstance(subber.to_html(-0.001), FormatterSkipElement)

    def test_negative_sign(self):
        """With sign='-', small negative values (between -threshold and 0) are substituted."""
        subber = SubSmallVals(threshold=0.01, small_pattern=">-{x}", sign="-")
        assert subber.to_html(-0.001) == "&gt;-0.01"
        assert subber.to_html(-0.009) == "&gt;-0.01"

    def test_negative_sign_threshold_excluded(self):
        """The negative threshold value itself is NOT substituted."""
        subber = SubSmallVals(threshold=0.01, small_pattern=">-{x}", sign="-")
        assert isinstance(subber.to_html(-0.01), FormatterSkipElement)

    def test_negative_sign_zero_excluded(self):
        """Zero is NOT substituted with sign='-'."""
        subber = SubSmallVals(threshold=0.01, small_pattern=">-{x}", sign="-")
        assert isinstance(subber.to_html(0), FormatterSkipElement)

    def test_negative_sign_positive_values_skipped(self):
        """Positive values are not substituted when sign='-'."""
        subber = SubSmallVals(threshold=0.01, small_pattern=">-{x}", sign="-")
        assert isinstance(subber.to_html(0.001), FormatterSkipElement)

    def test_non_numeric_skipped(self):
        """Non-numeric values are not substituted."""
        subber = SubSmallVals(threshold=0.01, small_pattern="<{x}", sign="+")
        assert isinstance(subber.to_html("hello"), FormatterSkipElement)
        assert isinstance(subber.to_html(None), FormatterSkipElement)

    def test_nan_skipped(self):
        """NaN values are not substituted."""
        subber = SubSmallVals(threshold=0.01, small_pattern="<{x}", sign="+")
        assert isinstance(subber.to_html(float("nan")), FormatterSkipElement)

    def test_custom_pattern(self):
        """Custom pattern without {x} placeholder works."""
        subber = SubSmallVals(threshold=0.01, small_pattern="smol", sign="+")
        assert subber.to_html(0.001) == "smol"

    def test_custom_threshold(self):
        """Custom threshold value works."""
        subber = SubSmallVals(threshold=0.5, small_pattern="<{x}", sign="+")
        assert subber.to_html(0.3) == "&lt;0.5"
        assert isinstance(subber.to_html(0.5), FormatterSkipElement)
        assert isinstance(subber.to_html(0.7), FormatterSkipElement)

    def test_method_integration(self):
        """End-to-end test using the GT method."""
        df = pl.DataFrame({"val": [0.001, 0.01, 0.1, 1.0, 0.0]})
        gt = GT(df).sub_small_vals(columns="val")
        result = gt._render_formats("html")
        body = [x for x in to_list(result._body.body["val"])]
        assert body == ["&lt;0.01", None, None, None, None]

    def test_method_sign_validation(self):
        """Invalid sign raises ValueError."""
        df = pl.DataFrame({"val": [1.0]})
        with pytest.raises(ValueError, match="sign"):
            GT(df).sub_small_vals(columns="val", sign="x")

    def test_method_default_pattern_positive(self):
        """Default pattern for positive sign is '<{x}'."""
        df = pl.DataFrame({"val": [0.005]})
        gt = GT(df).sub_small_vals(columns="val")
        result = gt._render_formats("html")
        body = [x for x in to_list(result._body.body["val"])]
        assert body == ["&lt;0.01"]

    def test_method_default_pattern_negative(self):
        """Default pattern for negative sign is '>-{x}'."""
        df = pl.DataFrame({"val": [-0.005]})
        gt = GT(df).sub_small_vals(columns="val", sign="-")
        result = gt._render_formats("html")
        body = [x for x in to_list(result._body.body["val"])]
        assert body == ["&gt;-0.01"]

    def test_ordering_independence_with_fmt(self):
        """sub_small_vals() works regardless of order with fmt_number()."""
        df = pl.DataFrame({"val": [0.001, 0.01, 0.1, 1.0]})
        # fmt then sub
        result1 = GT(df).fmt_number(columns="val").sub_small_vals(columns="val")
        body1 = [x for x in to_list(result1._render_formats("html")._body.body["val"])]
        # sub then fmt
        result2 = GT(df).sub_small_vals(columns="val").fmt_number(columns="val")
        body2 = [x for x in to_list(result2._render_formats("html")._body.body["val"])]
        assert body1 == body2

    def test_non_numeric_column_unaffected(self):
        """Applying sub_small_vals to a character column has no effect."""
        df = pl.DataFrame({"lett": ["A", "B", "C"]})
        gt = GT(df).sub_small_vals(columns="lett")
        result = gt._render_formats("html")
        body = [x for x in to_list(result._body.body["lett"])]
        assert body == [None, None, None]

    def test_negative_threshold_same_as_positive(self):
        """Negative threshold is treated as abs(threshold)."""
        df = pl.DataFrame({"val": [0.005, 0.05]})
        result1 = GT(df).sub_small_vals(columns="val", threshold=0.01)
        body1 = [x for x in to_list(result1._render_formats("html")._body.body["val"])]
        result2 = GT(df).sub_small_vals(columns="val", threshold=-0.01)
        body2 = [x for x in to_list(result2._render_formats("html")._body.body["val"])]
        assert body1 == body2


# =============================================================================
# sub_large_vals() tests
# =============================================================================


class TestSubLargeVals:
    """Tests for sub_large_vals()."""

    def test_basic_positive_default_threshold(self):
        """Values >= 1e12 are substituted."""
        subber = SubLargeVals(threshold=1e12, large_pattern=">={x}", sign="+")
        assert subber.to_html(1e12) == "&gt;=1000000000000.0"
        assert subber.to_html(1e13) == "&gt;=1000000000000.0"

    def test_below_threshold_skipped(self):
        """Values below threshold are not substituted."""
        subber = SubLargeVals(threshold=1e12, large_pattern=">={x}", sign="+")
        assert isinstance(subber.to_html(1e11), FormatterSkipElement)
        assert isinstance(subber.to_html(0), FormatterSkipElement)

    def test_negative_values_skipped_with_positive_sign(self):
        """Negative values are not substituted when sign='+'."""
        subber = SubLargeVals(threshold=1e12, large_pattern=">={x}", sign="+")
        assert isinstance(subber.to_html(-1e13), FormatterSkipElement)

    def test_negative_sign(self):
        """With sign='-', large negative values (<= -threshold) are substituted."""
        subber = SubLargeVals(threshold=1e12, large_pattern=">={x}", sign="-")
        assert subber.to_html(-1e12) == "&lt;=1000000000000.0"
        assert subber.to_html(-1e13) == "&lt;=1000000000000.0"

    def test_negative_sign_above_neg_threshold_skipped(self):
        """Values above -threshold are not substituted when sign='-'."""
        subber = SubLargeVals(threshold=1e12, large_pattern=">={x}", sign="-")
        assert isinstance(subber.to_html(-1e11), FormatterSkipElement)
        assert isinstance(subber.to_html(0), FormatterSkipElement)

    def test_negative_sign_positive_values_skipped(self):
        """Positive values are not substituted when sign='-'."""
        subber = SubLargeVals(threshold=1e12, large_pattern=">={x}", sign="-")
        assert isinstance(subber.to_html(1e13), FormatterSkipElement)

    def test_non_numeric_skipped(self):
        """Non-numeric values are not substituted."""
        subber = SubLargeVals(threshold=1e12, large_pattern=">={x}", sign="+")
        assert isinstance(subber.to_html("hello"), FormatterSkipElement)
        assert isinstance(subber.to_html(None), FormatterSkipElement)

    def test_nan_skipped(self):
        """NaN values are not substituted."""
        subber = SubLargeVals(threshold=1e12, large_pattern=">={x}", sign="+")
        assert isinstance(subber.to_html(float("nan")), FormatterSkipElement)

    def test_custom_pattern(self):
        """Custom pattern without {x} placeholder works."""
        subber = SubLargeVals(threshold=1e10, large_pattern="hugemongous", sign="+")
        assert subber.to_html(1e10) == "hugemongous"

    def test_custom_threshold(self):
        """Custom threshold value works."""
        subber = SubLargeVals(threshold=100, large_pattern=">={x}", sign="+")
        assert subber.to_html(100) == "&gt;=100"
        assert subber.to_html(200) == "&gt;=100"
        assert isinstance(subber.to_html(99), FormatterSkipElement)

    def test_sign_flips_pattern(self):
        """When sign='-', '>=' in pattern is auto-flipped to '<='."""
        subber = SubLargeVals(threshold=100, large_pattern=">={x}", sign="-")
        assert subber.to_html(-100) == "&lt;=100"

    def test_method_integration(self):
        """End-to-end test using the GT method."""
        df = pl.DataFrame({"val": [0.0, 100.0, 1e10, 1e12, 1e14]})
        gt = GT(df).sub_large_vals(columns="val")
        result = gt._render_formats("html")
        body = [x for x in to_list(result._body.body["val"])]
        # Only 1e12 and 1e14 are >= 1e12
        assert body == [None, None, None, "&gt;=1000000000000.0", "&gt;=1000000000000.0"]

    def test_method_sign_validation(self):
        """Invalid sign raises ValueError."""
        df = pl.DataFrame({"val": [1.0]})
        with pytest.raises(ValueError, match="sign"):
            GT(df).sub_large_vals(columns="val", sign="x")

    def test_ordering_independence_with_fmt(self):
        """sub_large_vals() works regardless of order with fmt_number()."""
        df = pl.DataFrame({"val": [1.0, 100.0, 1e12, 1e14]})
        # fmt then sub
        result1 = GT(df).fmt_number(columns="val").sub_large_vals(columns="val")
        body1 = [x for x in to_list(result1._render_formats("html")._body.body["val"])]
        # sub then fmt
        result2 = GT(df).sub_large_vals(columns="val").fmt_number(columns="val")
        body2 = [x for x in to_list(result2._render_formats("html")._body.body["val"])]
        assert body1 == body2

    def test_non_numeric_column_unaffected(self):
        """Applying sub_large_vals to a character column has no effect."""
        df = pl.DataFrame({"lett": ["A", "B", "C"]})
        gt = GT(df).sub_large_vals(columns="lett")
        result = gt._render_formats("html")
        body = [x for x in to_list(result._body.body["lett"])]
        assert body == [None, None, None]

    def test_negative_threshold_same_as_positive(self):
        """Negative threshold is treated as abs(threshold)."""
        df = pl.DataFrame({"val": [1e11, 1e12, 1e13]})
        result1 = GT(df).sub_large_vals(columns="val", threshold=1e12)
        body1 = [x for x in to_list(result1._render_formats("html")._body.body["val"])]
        result2 = GT(df).sub_large_vals(columns="val", threshold=-1e12)
        body2 = [x for x in to_list(result2._render_formats("html")._body.body["val"])]
        assert body1 == body2


# =============================================================================
# sub_values() tests
# =============================================================================


class TestSubValues:
    """Tests for sub_values()."""

    # --- Value matching ---

    def test_match_by_numeric_value(self):
        """Numeric values can be matched."""
        subber = SubValues(values=[74, 500], pattern=None, fn=None, replacement="—")
        assert subber.to_html(74) == "—"
        assert subber.to_html(500) == "—"
        assert isinstance(subber.to_html(100), FormatterSkipElement)

    def test_match_by_string_value(self):
        """String values can be matched."""
        subber = SubValues(values=["B"], pattern=None, fn=None, replacement="Bee")
        assert subber.to_html("B") == "Bee"
        assert isinstance(subber.to_html("A"), FormatterSkipElement)

    def test_match_single_value(self):
        """A single value (non-list) can be matched."""
        subber = SubValues(values=42, pattern=None, fn=None, replacement="answer")
        assert subber.to_html(42) == "answer"
        assert isinstance(subber.to_html(43), FormatterSkipElement)

    def test_none_values_skipped(self):
        """None values are not matched."""
        subber = SubValues(values=[None], pattern=None, fn=None, replacement="x")
        assert isinstance(subber.to_html(None), FormatterSkipElement)

    # --- Pattern matching ---

    def test_match_by_regex_pattern(self):
        """Regex pattern can match string values."""
        subber = SubValues(values=None, pattern="A|C|E", fn=None, replacement="Ace")
        assert subber.to_html("A") == "Ace"
        assert subber.to_html("C") == "Ace"
        assert subber.to_html("E") == "Ace"
        assert isinstance(subber.to_html("B"), FormatterSkipElement)

    def test_pattern_only_matches_strings(self):
        """Pattern matching only works on string columns."""
        subber = SubValues(values=None, pattern="123", fn=None, replacement="x")
        assert isinstance(subber.to_html(123), FormatterSkipElement)

    def test_pattern_takes_precedence_over_values(self):
        """If both pattern and values are supplied, pattern takes precedence."""
        subber = SubValues(values=["X"], pattern="A", fn=None, replacement="matched")
        # Pattern is checked, not values
        assert subber.to_html("A") == "matched"
        assert isinstance(subber.to_html("X"), FormatterSkipElement)

    # --- Function matching ---

    def test_match_by_function(self):
        """Custom function can target values."""
        subber = SubValues(
            values=None,
            pattern=None,
            fn=lambda x: isinstance(x, (int, float)) and x >= 0 and x < 50,
            replacement="small",
        )
        assert subber.to_html(0) == "small"
        assert subber.to_html(49) == "small"
        assert isinstance(subber.to_html(50), FormatterSkipElement)
        assert isinstance(subber.to_html(-1), FormatterSkipElement)

    def test_fn_takes_precedence_over_pattern(self):
        """If fn and pattern are both supplied, fn takes precedence."""
        subber = SubValues(values=None, pattern="A", fn=lambda x: x == "B", replacement="matched")
        assert subber.to_html("B") == "matched"
        assert isinstance(subber.to_html("A"), FormatterSkipElement)

    def test_fn_exception_returns_skip(self):
        """If fn raises TypeError/ValueError, the value is skipped."""
        subber = SubValues(
            values=None,
            pattern=None,
            fn=lambda x: x > 5,  # will raise TypeError for strings
            replacement="big",
        )
        assert isinstance(subber.to_html("hello"), FormatterSkipElement)

    # --- Replacement ---

    def test_numeric_replacement(self):
        """Numeric replacement value is converted to string."""
        subber = SubValues(values=[1], pattern=None, fn=None, replacement=150)
        assert subber.to_html(1) == "150"

    # --- Method integration ---

    def test_method_values_integration(self):
        """End-to-end test using the GT method with values."""
        df = pl.DataFrame({"col": [1, 2, 3, 4, 5]})
        gt = GT(df).sub_values(columns="col", values=[2, 4], replacement="even")
        result = gt._render_formats("html")
        body = [x for x in to_list(result._body.body["col"])]
        assert body == [None, "even", None, "even", None]

    def test_method_pattern_integration(self):
        """End-to-end test using the GT method with pattern."""
        df = pl.DataFrame({"col": ["apple", "banana", "apricot", "cherry"]})
        gt = GT(df).sub_values(columns="col", pattern="^ap", replacement="fruit")
        result = gt._render_formats("html")
        body = [x for x in to_list(result._body.body["col"])]
        assert body == ["fruit", None, "fruit", None]

    def test_method_fn_integration(self):
        """End-to-end test using the GT method with fn."""
        df = pl.DataFrame({"col": [10, 20, 30, 40, 50]})
        gt = GT(df).sub_values(columns="col", fn=lambda x: x > 25, replacement="big")
        result = gt._render_formats("html")
        body = [x for x in to_list(result._body.body["col"])]
        assert body == [None, None, "big", "big", "big"]

    def test_method_requires_matching_arg(self):
        """Must supply one of values, pattern, or fn."""
        df = pl.DataFrame({"col": [1]})
        with pytest.raises(ValueError, match="One of"):
            GT(df).sub_values(columns="col", replacement="x")

    def test_method_requires_replacement(self):
        """Must supply a replacement value."""
        df = pl.DataFrame({"col": [1]})
        with pytest.raises(ValueError, match="replacement"):
            GT(df).sub_values(columns="col", values=[1])

    def test_method_fn_must_be_callable(self):
        """fn must be callable."""
        df = pl.DataFrame({"col": [1]})
        with pytest.raises(TypeError, match="function"):
            GT(df).sub_values(columns="col", fn="not_a_function", replacement="x")

    def test_consecutive_replacements_same_column(self):
        """Consecutive sub_values calls on the same column work (last call wins for overlaps)."""
        df = pl.DataFrame({"col": [0, 74, 500]})
        gt = (
            GT(df)
            .sub_values(columns="col", values=[0], replacement="zero")
            .sub_values(columns="col", values=[74], replacement="seventy-four")
        )
        result = gt._render_formats("html")
        body = [x for x in to_list(result._body.body["col"])]
        assert body == ["zero", "seventy-four", None]

    def test_last_call_wins_for_same_value(self):
        """When the same value is targeted by multiple sub_values, the last one wins."""
        df = pl.DataFrame({"col": [74, 100]})
        gt = (
            GT(df)
            .sub_values(columns="col", values=[74], replacement="first")
            .sub_values(columns="col", values=[74], replacement="second")
        )
        result = gt._render_formats("html")
        body = [x for x in to_list(result._body.body["col"])]
        assert body == ["second", None]

    def test_fn_operates_across_columns(self):
        """fn matching works across numeric and character columns."""
        df = pl.DataFrame({"num": [-1, 0, 5, 50], "lett": ["A", "B", "C", "D"]})
        gt = GT(df).sub_values(
            fn=lambda x: isinstance(x, (int, float)) and x < 0, replacement="neg"
        )
        result = gt._render_formats("html")
        num_body = [x for x in to_list(result._body.body["num"])]
        lett_body = [x for x in to_list(result._body.body["lett"])]
        # Only the negative number is replaced; letters are unaffected
        assert num_body == ["neg", None, None, None]
        assert lett_body == [None, None, None, None]

    def test_pattern_does_not_match_numeric_columns(self):
        """Pattern matching only targets string columns, not numeric."""
        df = pl.DataFrame({"num": [0, 1, 500], "lett": ["A0", "B1", "C2"]})
        gt = GT(df).sub_values(pattern="0", replacement="matched")
        result = gt._render_formats("html")
        num_body = [x for x in to_list(result._body.body["num"])]
        lett_body = [x for x in to_list(result._body.body["lett"])]
        # Pattern should not match numeric column
        assert num_body == [None, None, None]
        # Pattern should match string column containing "0"
        assert lett_body == ["matched", None, None]

    def test_html_escaping_in_replacement(self):
        """Replacement text is HTML-escaped by default."""
        df = pl.DataFrame({"col": ["A", "B"]})
        gt = GT(df).sub_values(values=["A"], replacement="<b>bold</b>")
        result = gt._render_formats("html")
        body = [x for x in to_list(result._body.body["col"])]
        assert body == ["&lt;b&gt;bold&lt;/b&gt;", None]
