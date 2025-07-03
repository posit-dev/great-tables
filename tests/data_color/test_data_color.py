from typing import Type, TypeVar

import numpy as np
import pandas as pd
import polars as pl
import pytest

from great_tables import GT, style
from great_tables._gt_data import CellStyle, StyleInfo
from great_tables._tbl_data import DataFrameLike
from great_tables._utils_render_html import create_body_component_h
from great_tables.data import exibble

T_CellStyle = TypeVar("T_CellStyle", bound=CellStyle)

params_frames = [
    pytest.param(pd.DataFrame, id="pandas"),
    pytest.param(pl.DataFrame, id="polars"),
]


@pytest.fixture(params=params_frames, scope="function")
def df(request) -> DataFrameLike:
    return request.param(exibble[["num", "char", "currency"]].head(4))


def assert_rendered_body(snapshot, gt):
    built = gt._build_data("html")
    body = create_body_component_h(built)

    assert snapshot == body


def get_first_style(obj: StyleInfo, cls: Type[T_CellStyle]) -> Type[T_CellStyle]:
    for cell_style in obj.styles:
        if isinstance(cell_style, cls):
            return cell_style

    raise KeyError(f"No style entry of type {cls} found.")


def test_data_color_simple_df_snap(snapshot: str):
    df = pd.DataFrame(
        {
            "A": [1, 2, 3],
            "B": [10, 9, 8],
            "C": ["one", "two", "three"],
        }
    )

    new_gt = GT(df).data_color()

    assert_rendered_body(snapshot, new_gt)


def test_data_color_simple_exibble_snap(snapshot: str, df: DataFrameLike):
    gt = GT(df).data_color()

    assert_rendered_body(snapshot, gt)


def test_data_color_pd_cols_rows_snap(snapshot: str):
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5, 200], "b": [51, 52, 53, 54, 55, 200]})
    new_gt = GT(df).data_color(columns=["a"], rows=[0, 1, 2, 3, 4])
    assert_rendered_body(snapshot, new_gt)
    new_gt2 = GT(df).data_color(columns=["a"], rows=lambda df_: df_["a"].lt(60))
    assert create_body_component_h(new_gt._build_data("html")) == create_body_component_h(
        new_gt2._build_data("html")
    )


def test_data_color_pl_cols_rows_snap(snapshot: str):
    import polars.selectors as cs

    df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 200], "b": [51, 52, 53, 54, 55, 200]})
    new_gt = GT(df).data_color(columns=["b"], rows=[0, 1, 2, 3, 4])
    assert_rendered_body(snapshot, new_gt)
    new_gt2 = GT(df).data_color(columns=cs.starts_with("b"), rows=pl.col("b").lt(60))
    assert create_body_component_h(new_gt._build_data("html")) == create_body_component_h(
        new_gt2._build_data("html")
    )


@pytest.mark.parametrize("none_val", [None, np.nan, float("nan"), pd.NA])
@pytest.mark.parametrize("df_cls", [pd.DataFrame, pl.DataFrame])
def test_data_color_missing_value(df_cls, none_val):
    from great_tables import GT

    # skip the case where pd.NA would be passed to polars
    # since it raises an error on DataFrame construction
    if df_cls is pl.DataFrame and none_val is pd.NA:
        pytest.skip()

    df = df_cls({"x": [1.0, 2.0, none_val], "y": [3, 4, 5]})
    new_gt = GT(df).data_color("x", na_color="#FFFFF0")
    assert len(new_gt._styles) == 3
    assert get_first_style(new_gt._styles[-1], style.fill).color == "#FFFFF0"


def test_data_color_palette_snap(snapshot, df: DataFrameLike):
    gt = GT(df).data_color(columns=["num", "currency"], palette=["red", "green"])

    assert_rendered_body(snapshot, gt)


def test_data_color_domain_na_color_snap(snapshot: str, df: DataFrameLike):
    """`data_color` works with `domain` and `na_color`."""
    gt = GT(df).data_color(
        columns="currency", palette=["red", "green"], domain=[0, 50], na_color="blue"
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_domain_na_color_reverse_snap(snapshot: str, df: DataFrameLike):
    """`data_color` works with `domain`, `na_color`, and `reverse`."""
    gt = GT(df).data_color(
        columns="currency",
        palette=["red", "green"],
        domain=[0, 50],
        na_color="blue",
        reverse=True,
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_overlapping_domain(snapshot: str, df: DataFrameLike):
    """`data_color` works with overlapping `domain` (RHS domain extends outside the data range)."""
    gt = GT(df).data_color(
        columns="currency",
        palette=["yellow", "rebeccapurple"],
        domain=[1000, 65555],
        na_color="red",
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_subset_domain(snapshot: str, df: DataFrameLike):
    """`data_color` works with subset `domain`."""
    gt = GT(df).data_color(
        columns="currency",
        palette=["yellow", "rebeccapurple"],
        domain=[1000, 60000],
        na_color="red",
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_autocolor_text_false(snapshot: str, df: DataFrameLike):
    """`data_color` works with `autocolor_text=False`."""
    gt = GT(df).data_color(
        columns="currency",
        palette=["red", "green"],
        domain=[0, 50],
        na_color="blue",
        reverse=True,
        autocolor_text=False,
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_colorbrewer_palettes(df: DataFrameLike):
    palettes = [
        "Accent",
        "Blues",
        "BrBG",
        "BuGn",
        "BuPu",
        "Dark2",
        "GnBu",
        "Greens",
        "Greys",
        "OrRd",
        "Oranges",
        "PRGn",
        "Paired",
        "Pastel1",
        "Pastel2",
        "PiYG",
        "PuBu",
        "PuBuGn",
        "PuOr",
        "PuRd",
        "Purples",
        "RdBu",
        "RdGy",
        "RdPu",
        "RdYlBu",
        "RdYlGn",
        "Reds",
        "Set1",
        "Set2",
        "Set3",
        "Spectral",
        "YlGn",
        "YlGnBu",
        "YlOrBr",
        "YlOrRd",
    ]

    for palette in palettes:
        gt = GT(df).data_color(columns=["num", "currency"], palette=palette)
        assert isinstance(gt, GT)


def test_data_color_viridis_palettes(df: DataFrameLike):
    palettes = [
        "viridis",
        "plasma",
        "inferno",
        "magma",
        "cividis",
    ]

    for palette in palettes:
        gt = GT(df).data_color(columns=["num", "currency"], palette=palette)
        assert isinstance(gt, GT)


def test_data_color_colorbrewer_snap(snapshot: str):
    df = pd.DataFrame(
        {
            "A": [1, 2, 3, 4, 5],
            "B": [10, 9, 8, 7, 6],
            "C": ["one", "two", "three", "four", "five"],
        }
    )

    new_gt = GT(df).data_color(columns=["A", "B"], palette="Greens")

    assert_rendered_body(snapshot, new_gt)


def test_data_color_viridis_snap(snapshot: str):
    df = pd.DataFrame(
        {
            "A": [1, 2, 3, 4, 5],
            "B": [10, 9, 8, 7, 6],
            "C": ["one", "two", "three", "four", "five"],
        }
    )

    new_gt = GT(df).data_color(columns=["A", "B"], palette="viridis")

    assert_rendered_body(snapshot, new_gt)


# Pandas: Single value -- single color; uses first color from palette
def test_single_value_pd(snapshot: str):
    df = pd.DataFrame({"x": [1], "y": [3]})
    new_gt = GT(df).data_color("x", palette=["green", "blue"], na_color="red")

    assert_rendered_body(snapshot, new_gt)


# Pandas: Single value -- multiple rows (rest of the rows are missing); uses first color
# from palette and applies `na_color=` to the missing rows
def test_single_value_from_multiple_rows_pd(snapshot: str):
    df = pd.DataFrame({"x": [1, None], "y": [3, 4]})
    new_gt = GT(df).data_color("x", palette=["green", "blue"], na_color="red")

    assert_rendered_body(snapshot, new_gt)


# Pandas: Multiple rows in a column but all are missing; applies `na_color=` to all rows
def test_all_missing_from_multiple_rows_pd(snapshot: str):
    df = pd.DataFrame({"x": [None, None], "y": [3, 6]})
    new_gt = GT(df).data_color("x", palette=["green", "blue"], na_color="red")

    assert_rendered_body(snapshot, new_gt)


# Pandas: Single missing value from a single row; applies `na_color=` to the missing value
def test_single_value_and_missing_pd(snapshot: str):
    df = pd.DataFrame({"x": [None], "y": [3]})
    new_gt = GT(df).data_color("x", palette=["green", "blue"], na_color="red")

    assert_rendered_body(snapshot, new_gt)


# Pandas: Non-missing values have a domain range of 0; applies `na_color=` to the missing values
def test_all_values_have_zero_range_domain_pd(snapshot: str):
    df = pd.DataFrame({"x": [2, 2, None, None], "y": [3, 4, 5, 6]})
    new_gt = GT(df).data_color("x", palette=["green", "blue"], domain=[0, 0])

    assert_rendered_body(snapshot, new_gt)


# Polars: Single value -- single color; uses first color from palette
def test_single_value_pl(snapshot: str):
    df = pl.DataFrame({"x": [1], "y": [3]})
    new_gt = GT(df).data_color("x", palette=["green", "blue"], na_color="red")

    assert_rendered_body(snapshot, new_gt)


# Polars: Single value -- multiple rows (rest of the rows are missing); uses first color
# from palette and applies `na_color=` to the missing rows
def test_single_value_from_multiple_rows_pl(snapshot: str):
    df = pl.DataFrame({"x": [1, None], "y": [3, 4]})
    new_gt = GT(df).data_color("x", palette=["green", "blue"], na_color="red")

    assert_rendered_body(snapshot, new_gt)


# Polars: Multiple rows in a column but all are missing; applies `na_color=` to all rows
def test_all_missing_from_multiple_rows_pl(snapshot: str):
    df = pl.DataFrame({"x": [None, None], "y": [3, 6]})
    new_gt = GT(df).data_color("x", palette=["green", "blue"], na_color="red")

    assert_rendered_body(snapshot, new_gt)


# Polars: Single missing value from a single row; applies `na_color=` to the missing value
def test_single_value_and_missing_pl(snapshot: str):
    df = pl.DataFrame({"x": [None], "y": [3]})
    new_gt = GT(df).data_color("x", palette=["green", "blue"], na_color="red")

    assert_rendered_body(snapshot, new_gt)


# Polars: Non-missing values have a domain range of 0; applies `na_color=` to the missing values
def test_all_values_have_zero_range_domain_pl(snapshot: str):
    df = pl.DataFrame({"x": [2, 2, None, None], "y": [3, 4, 5, 6]})
    new_gt = GT(df).data_color("x", palette=["green", "blue"], domain=[0, 0])

    assert_rendered_body(snapshot, new_gt)


# test for data_color with truncate=True
def test_data_color_truncate(df: DataFrameLike):
    new_gt = GT(df).data_color(
        columns=["num", "currency"],
        domain=[10, 40],
        palette=["#654321", "white", "#123456"],
        truncate=True,
    )

    # check if all cells are colored
    assert len(new_gt._styles) == 8
    # check if the last cell (out of range of domain) is colored with the last color in the palette
    assert get_first_style(new_gt._styles[-1], style.fill).color == "#123456"
    # check if the first cell (out of range of domain) is colored with the first color in the palette
    assert get_first_style(new_gt._styles[0], style.fill).color == "#654321"
