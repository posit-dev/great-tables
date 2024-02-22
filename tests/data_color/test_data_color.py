from great_tables import GT, style
from great_tables.data import exibble
from great_tables._utils_render_html import create_body_component_h
from great_tables._gt_data import StyleInfo, CellStyle
from typing import Type, TypeVar

import numpy as np
import pandas as pd
import polars as pl
import pytest
from great_tables._tbl_data import DataFrameLike


T_CellStyle = TypeVar("T_CellStyle", bound=CellStyle)

params_frames = [pytest.param(pd.DataFrame, id="pandas"), pytest.param(pl.DataFrame, id="polars")]


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


def test_data_color_simple_df_snap(snapshot):
    df = pd.DataFrame(
        {
            "A": [1, 2, 3],
            "B": [10, 9, 8],
            "C": ["one", "two", "three"],
        }
    )

    new_gt = GT(df).data_color()

    assert_rendered_body(snapshot, new_gt)


def test_data_color_simple_exibble_snap(snapshot, df: DataFrameLike):
    gt = GT(df).data_color()

    assert_rendered_body(snapshot, gt)


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


def test_data_color_domain_na_color_snap(snapshot, df: DataFrameLike):
    """`data_color` works with `domain` and `na_color`."""
    gt = GT(df).data_color(
        columns="currency", palette=["red", "green"], domain=[0, 50], na_color="blue"
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_domain_na_color_reverse_snap(snapshot, df: DataFrameLike):
    """`data_color` works with `domain`, `na_color`, and `reverse`."""
    gt = GT(df).data_color(
        columns="currency", palette=["red", "green"], domain=[0, 50], na_color="blue", reverse=True
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_overlapping_domain(snapshot, df: DataFrameLike):
    """`data_color` works with overlapping `domain` (RHS domain extends outside the data range)."""
    gt = GT(df).data_color(
        columns="currency",
        palette=["yellow", "rebeccapurple"],
        domain=[1000, 65555],
        na_color="red",
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_subset_domain(snapshot, df: DataFrameLike):
    """`data_color` works with subset `domain`."""
    gt = GT(df).data_color(
        columns="currency",
        palette=["yellow", "rebeccapurple"],
        domain=[1000, 60000],
        na_color="red",
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_autocolor_text_false(snapshot, df: DataFrameLike):
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


def test_data_color_colorbrewer_snap(snapshot):
    df = pd.DataFrame(
        {
            "A": [1, 2, 3, 4, 5],
            "B": [10, 9, 8, 7, 6],
            "C": ["one", "two", "three", "four", "five"],
        }
    )

    new_gt = GT(df).data_color(columns=["A", "B"], palette="Greens")

    assert_rendered_body(snapshot, new_gt)


def test_data_color_viridis_snap(snapshot):
    df = pd.DataFrame(
        {
            "A": [1, 2, 3, 4, 5],
            "B": [10, 9, 8, 7, 6],
            "C": ["one", "two", "three", "four", "five"],
        }
    )

    new_gt = GT(df).data_color(columns=["A", "B"], palette="viridis")

    assert_rendered_body(snapshot, new_gt)
