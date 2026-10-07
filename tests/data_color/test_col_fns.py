import numpy as np
import pandas as pd
import polars as pl
import pytest

from great_tables import GT, col_bin, col_factor, col_numeric, style
from great_tables._data_color.col_fns import _is_missing


def fill_colors(gt: GT) -> list[str]:
    return [next(s for s in info.styles if isinstance(s, style.fill)).color for info in gt._styles]


# col_numeric ------------------------------------------------------------------------------------


def test_col_numeric_diverging_domain():
    fn = col_numeric(palette=["red", "white", "green"], domain=[-10, 10])

    assert fn([-10, -5, 0, 5, 10]) == ["#FF0000", "#FF8080", "#FFFFFF", "#80C080", "#008000"]


def test_col_numeric_domain_from_data():
    fn = col_numeric(palette=["#000000", "#FFFFFF"])

    assert fn([10, 15, 20]) == ["#000000", "#808080", "#FFFFFF"]
    # The domain is recomputed on every call
    assert fn([0, 100]) == ["#000000", "#FFFFFF"]


def test_col_numeric_missing_and_out_of_domain_give_none():
    fn = col_numeric(palette=["red", "green"], domain=[0, 10])

    assert fn([None, float("nan"), np.nan, pd.NA, -1, 11]) == [None] * 6


def test_col_numeric_na_color():
    fn = col_numeric(palette=["red", "green"], domain=[0, 10], na_color="gray")

    assert fn([None, 11, 0]) == ["#BEBEBE", "#BEBEBE", "#FF0000"]


def test_col_numeric_named_palette_and_reverse():
    assert col_numeric(palette="viridis")([0, 1]) == ["#440154", "#FDE725"]
    assert col_numeric(palette="viridis", reverse=True)([0, 1]) == ["#FDE725", "#440154"]


def test_col_numeric_zero_range_and_all_missing():
    fn = col_numeric(palette=["red", "green"])

    assert fn([5, 5]) == ["#FF0000", "#FF0000"]
    assert fn([None, None]) == [None, None]
    assert fn([]) == []


def test_col_numeric_single_color_palette():
    assert col_numeric(palette="red")([1, 2, None]) == ["#FF0000", "#FF0000", None]


@pytest.mark.parametrize("domain", [[0], [0, 1, 2], [10, 0]])
def test_col_numeric_invalid_domain_raises(domain):
    with pytest.raises(ValueError, match="domain"):
        col_numeric(domain=domain)


@pytest.mark.parametrize("val", ["a", True])
def test_col_numeric_non_numeric_raises(val):
    with pytest.raises(TypeError, match="requires numeric values"):
        col_numeric()([1, val])


def test_col_numeric_infinite_raises():
    with pytest.raises(ValueError, match="infinite"):
        col_numeric()([1, float("inf")])


def test_col_numeric_truncate():
    fn = col_numeric(palette=["red", "white", "green"], domain=[-10, 10], truncate=True)

    assert fn([-50, -10, 0, 10, 50, None]) == [
        "#FF0000",
        "#FF0000",
        "#FFFFFF",
        "#008000",
        "#008000",
        None,
    ]


def test_col_numeric_truncate_zero_range_domain():
    fn = col_numeric(palette=["red", "green"], domain=[5, 5], truncate=True)

    assert fn([0, 5, 10]) == ["#FF0000"] * 3


RWG = ["red", "white", "green"]


def test_col_numeric_midpoint_symmetric_domain():
    fn = col_numeric(palette=RWG, midpoint=0)

    assert fn([-2, 0, 10, None]) == ["#FFCCCC", "#FFFFFF", "#008000", None]


def test_col_numeric_midpoint_with_domain_is_piecewise():
    fn = col_numeric(palette=RWG, midpoint=0, domain=[-2, 10])

    assert fn([-2, -1, 0, 5, 10]) == ["#FF0000", "#FF8080", "#FFFFFF", "#80C080", "#008000"]


@pytest.mark.parametrize("domain", [[0, 10], [-10, 0]])
def test_col_numeric_midpoint_at_domain_end_keeps_center_color(domain):
    fn = col_numeric(palette=RWG, midpoint=0, domain=domain)

    assert fn([0]) == ["#FFFFFF"]


def test_col_numeric_midpoint_all_values_at_midpoint():
    assert col_numeric(palette=RWG, midpoint=5)([5, 5]) == ["#FFFFFF", "#FFFFFF"]


def test_col_numeric_midpoint_truncate():
    fn = col_numeric(palette=RWG, midpoint=0, domain=[-1, 5], truncate=True)

    assert fn([-20, 20]) == ["#FF0000", "#008000"]


@pytest.mark.parametrize("midpoint", [True, "0", float("inf"), float("nan")])
def test_col_numeric_invalid_midpoint_raises(midpoint):
    with pytest.raises(ValueError, match="must be a finite number"):
        col_numeric(midpoint=midpoint)


def test_col_numeric_midpoint_outside_domain_raises():
    with pytest.raises(ValueError, match="must lie within the range of `domain=`"):
        col_numeric(midpoint=20, domain=[0, 10])


def test_col_numeric_stops_numeric():
    fn = col_numeric(palette=RWG, stops=[-10, 0, 30])

    assert fn([-10, -5, 0, 15, 30, 31]) == [
        "#FF0000",
        "#FF8080",
        "#FFFFFF",
        "#80C080",
        "#008000",
        None,
    ]


def test_col_numeric_stops_percent_and_numeric():
    fn = col_numeric(palette=RWG, stops=["0%", 0, "100%"])

    assert fn([-2, 0, 10]) == ["#FF0000", "#FFFFFF", "#008000"]


def test_col_numeric_stops_percent_range_includes_numeric_stops():
    # The range spans [0, 10] (the data plus the `0` stop), so `5` is halfway from white to green
    fn = col_numeric(palette=RWG, stops=["0%", 0, "100%"])

    assert fn([5, 10]) == ["#80C080", "#008000"]


def test_col_numeric_stops_percent_only():
    fn = col_numeric(palette=RWG, stops=["0%", "25%", "100%"])

    assert fn([0, 25, 100]) == ["#FF0000", "#FFFFFF", "#008000"]


def test_col_numeric_stops_repeated_stop_is_sharp_change():
    fn = col_numeric(palette=["black", "white", "red", "lime"], stops=[-1, 0, 0, 1])

    assert fn([-1, 0, 1]) == ["#000000", "#FF0000", "#00FF00"]


def test_col_numeric_stops_truncate():
    fn = col_numeric(palette=RWG, stops=[-10, 0, 10], truncate=True)

    assert fn([-20, 20]) == ["#FF0000", "#008000"]


def test_col_numeric_stops_all_missing():
    assert col_numeric(palette=RWG, stops=["0%", 0, "100%"])([None, None]) == [None, None]


@pytest.mark.parametrize(
    "kwargs,match",
    [
        ({"stops": [0, 1]}, "one value per palette color"),
        ({"stops": [0, "x", 1]}, "must be a percentage"),
        ({"stops": [0, "150%", 1]}, "must be a percentage"),
        ({"stops": [0, True, 1]}, "must be a finite number or a percentage"),
        ({"stops": [2, 1, 3]}, "numbers in `stops=` must be in non-decreasing order"),
        ({"stops": ["50%", "0%", 1]}, "percentages in `stops=` must be in non-decreasing order"),
        ({"stops": [0, 1, 2], "domain": [0, 2]}, "can't be used together"),
        ({"stops": [0, 1, 2], "midpoint": 1}, "can't be used together"),
    ],
)
def test_col_numeric_invalid_stops_raises(kwargs, match):
    with pytest.raises(ValueError, match=match):
        col_numeric(palette=RWG, **kwargs)


def test_col_numeric_stops_unordered_once_resolved_raises():
    fn = col_numeric(palette=RWG, stops=[0, "50%", 10])

    with pytest.raises(ValueError, match="once percentages are resolved"):
        fn([8, 100])


# col_bin ----------------------------------------------------------------------------------------


def test_col_bin_explicit_breaks():
    fn = col_bin(palette=["red", "blue"], bins=[0, 10, 20])

    assert fn([0, 9.9, 10, 20]) == ["#FF0000", "#FF0000", "#0000FF", "#0000FF"]


def test_col_bin_right_closed():
    fn = col_bin(palette=["red", "blue"], bins=[0, 10, 20], right=True)

    assert fn([0, 10, 10.1, 20]) == ["#FF0000", "#FF0000", "#0000FF", "#0000FF"]


def test_col_bin_breaks_are_sorted():
    fn = col_bin(palette=["red", "blue"], bins=[20, 0, 10])

    assert fn([5, 15]) == ["#FF0000", "#0000FF"]


def test_col_bin_n_bins_samples_palette_evenly():
    fn = col_bin(palette=["#000000", "#FFFFFF"], bins=3)

    assert fn([0, 1.9, 2, 4, 6]) == ["#000000", "#000000", "#808080", "#FFFFFF", "#FFFFFF"]


def test_col_bin_n_bins_with_domain():
    fn = col_bin(palette=["red", "blue"], domain=[0, 100], bins=2)

    assert fn([10, 60, 101]) == ["#FF0000", "#0000FF", None]


def test_col_bin_single_bin():
    assert col_bin(palette=["red", "blue"], bins=1)([1, 2]) == ["#FF0000", "#FF0000"]


def test_col_bin_missing_and_out_of_range():
    fn = col_bin(palette=["red", "blue"], bins=[0, 10], na_color="black")

    assert fn([None, -1, 11, 5]) == ["#000000", "#000000", "#000000", "#FF0000"]


@pytest.mark.parametrize("right", [False, True])
def test_col_bin_truncate(right):
    fn = col_bin(palette=["red", "blue"], bins=[0, 10, 20], truncate=True, right=right)

    assert fn([-5, 0, 20, 25, None]) == ["#FF0000", "#FF0000", "#0000FF", "#0000FF", None]


def test_col_bin_truncate_with_domain():
    fn = col_bin(palette=["red", "blue"], domain=[0, 100], bins=2, truncate=True)

    assert fn([-1, 101]) == ["#FF0000", "#0000FF"]


@pytest.mark.parametrize("bins", [0, [5]])
def test_col_bin_invalid_bins_raises(bins):
    with pytest.raises(ValueError, match="bins"):
        col_bin(bins=bins)


# col_factor -------------------------------------------------------------------------------------


def test_col_factor_levels_in_order_of_appearance():
    fn = col_factor(palette=["red", "green", "blue"])

    assert fn(["b", "a", "b", "c", None]) == ["#FF0000", "#008000", "#FF0000", "#0000FF", None]


def test_col_factor_interpolates_short_palette():
    assert col_factor(palette=["red", "blue"])(["a", "b", "c"]) == [
        "#FF0000",
        "#800080",
        "#0000FF",
    ]


def test_col_factor_domain_fixes_colors():
    fn = col_factor(palette=["red", "green", "blue"], domain=["x", "y", "z"], na_color="black")

    assert fn(["z", "x", "w"]) == ["#0000FF", "#FF0000", "#000000"]


def test_col_factor_non_string_levels():
    assert col_factor(palette=["red", "blue"])([True, False, True]) == [
        "#FF0000",
        "#0000FF",
        "#FF0000",
    ]


def test_col_factor_all_missing():
    assert col_factor()([None, None]) == [None, None]


# integration with data_color(fn=) ---------------------------------------------------------------


@pytest.mark.parametrize("df_cls", [pd.DataFrame, pl.DataFrame])
def test_col_numeric_with_data_color_uses_na_color(df_cls):
    df = df_cls({"x": [-10.0, 0.0, 10.0, None]})
    gt = GT(df).data_color(
        columns="x",
        fn=col_numeric(palette=["red", "white", "green"], domain=[-10, 10]),
        na_color="#123456",
    )

    assert fill_colors(gt) == ["#FF0000", "#FFFFFF", "#008000", "#123456"]


def test_col_factor_with_data_color_and_alpha():
    df = pd.DataFrame({"x": ["a", "b"]})
    gt = GT(df).data_color(columns="x", fn=col_factor(palette=["red", "blue"]), alpha=0.5)

    assert fill_colors(gt) == ["#FF00007F", "#0000FF7F"]


def test_col_bin_with_data_color():
    df = pd.DataFrame({"x": [1, 50, 500]})
    gt = GT(df).data_color(columns="x", fn=col_bin(palette=["red", "blue"], bins=[0, 100, 1000]))

    assert fill_colors(gt) == ["#FF0000", "#FF0000", "#0000FF"]


# helpers ----------------------------------------------------------------------------------------


@pytest.mark.parametrize("val", [None, float("nan"), np.nan, pd.NA, pd.NaT])
def test_is_missing_true(val):
    assert _is_missing(val)


@pytest.mark.parametrize("val", [0, 0.0, "", "NA", False])
def test_is_missing_false(val):
    assert not _is_missing(val)
