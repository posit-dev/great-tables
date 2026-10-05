from typing import Type, TypeVar

import numpy as np
import pandas as pd
import polars as pl
import pyarrow as pa
import pytest

from great_tables import GT, style
from great_tables._gt_data import CellStyle, StyleInfo
from great_tables._tbl_data import DataFrameLike
from great_tables._utils_render_html import create_body_component_h
from great_tables.data import exibble
from tests.utils import assert_rendered_body

T_CellStyle = TypeVar("T_CellStyle", bound=CellStyle)

params_frames = [
    pytest.param(pd.DataFrame, id="pandas"),
    pytest.param(pl.DataFrame, id="polars"),
    pytest.param(pa.table, id="pyarrow"),
]


@pytest.fixture(params=params_frames, scope="function")
def df(request) -> DataFrameLike:
    return request.param(exibble[["num", "char", "currency"]].head(4))


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


def test_data_color_contrast_algo(df: DataFrameLike):
    """`contrast_algo=` controls how autocolored text is chosen."""

    def text_color(algo: str) -> str:
        gt = GT(df).data_color(columns="num", palette=["red", "red"], contrast_algo=algo)
        return get_first_style(gt._styles[0], style.text).color

    assert text_color("apca") == "#FFFFFF"
    assert text_color("wcag") == "#000000"


def test_data_color_contrast_algo_invalid(df: DataFrameLike):
    with pytest.raises(ValueError, match="contrast_algo"):
        GT(df).data_color(contrast_algo="foo")  # type: ignore[arg-type]


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


def test_data_color_alpha_gradient_palette():
    """`data_color` applies `alpha=` to colors interpolated from a gradient palette (#711)."""
    df = pd.DataFrame({"x": [0, 50, 100]})
    new_gt = GT(df).data_color(columns="x", palette=["#FF0000", "#0000FF"], alpha=0.5)

    colors = [get_first_style(s, style.fill).color.lower() for s in new_gt._styles]
    assert colors == ["#ff00007f", "#8000807f", "#0000ff7f"]


def test_data_color_alpha_factor_palette():
    """`data_color` applies `alpha=` to colors interpolated for a factor (categorical) column."""
    df = pd.DataFrame({"x": ["a", "b", "c"]})
    new_gt = GT(df).data_color(columns="x", palette=["#FF0000", "#0000FF"], alpha=0.5)

    colors = [get_first_style(s, style.fill).color for s in new_gt._styles]
    assert all(len(c) == 9 and c.lower().endswith("7f") for c in colors)


def test_data_color_alpha_na_color_not_double_applied():
    """`alpha=` is applied once to `na_color=`, not compounded by the gradient-palette fix."""
    df = pd.DataFrame({"x": [1.0, 2.0, None]})
    new_gt = GT(df).data_color(columns="x", palette=["red", "blue"], alpha=0.5, na_color="#00FF00")

    na_style_color = get_first_style(new_gt._styles[-1], style.fill).color.lower()
    assert na_style_color == "#00ff007f"


def test_data_color_invalid_column_type_raises():
    """data_color raises ValueError for mixed-type (non-numeric, non-string) columns."""
    df = pd.DataFrame({"x": [1, "two", 3]})
    with pytest.raises(ValueError, match="Invalid column type"):
        GT(df).data_color(columns="x").as_raw_html()


def test_data_color_fn(df: DataFrameLike):
    """`fn=` maps column values directly to colors."""
    new_gt = GT(df).data_color(
        columns="num",
        fn=lambda vals: ["red" if x < 1 else "#00F" for x in vals],
        autocolor_text=False,
    )

    colors = [get_first_style(s, style.fill).color for s in new_gt._styles]
    assert colors == ["#FF0000", "#0000FF", "#0000FF", "#0000FF"]


def test_data_color_fn_ignores_palette_and_domain():
    df = pd.DataFrame({"x": [1, 2, 3]})
    new_gt = GT(df).data_color(
        columns="x",
        palette=["green", "yellow"],
        domain=[100, 200],
        fn=lambda vals: ["#123456"] * len(vals),
    )

    colors = [get_first_style(s, style.fill).color for s in new_gt._styles]
    assert colors == ["#123456"] * 3


@pytest.mark.parametrize("df_cls", [pd.DataFrame, pl.DataFrame])
def test_data_color_fn_receives_missing_values(df_cls):
    """Missing values are passed to `fn=` (as in gt); `None` results get `na_color=`."""
    df = df_cls({"x": [1.0, None, 3.0, 4.0]})
    received = []

    def color_fn(vals):
        received.extend(vals)
        return [None if pd.isna(x) or x == 4.0 else "red" for x in vals]

    new_gt = GT(df).data_color(columns="x", fn=color_fn, na_color="#00FF00")

    assert len(received) == 4
    assert pd.isna(received[1])

    colors = [get_first_style(s, style.fill).color for s in new_gt._styles]
    assert colors == ["#FF0000", "#00FF00", "#FF0000", "#00FF00"]


def test_data_color_fn_can_color_missing_values():
    """`fn=` decides the color of missing values, overriding `na_color=`."""
    df = pd.DataFrame({"x": [1.0, None]})
    new_gt = GT(df).data_color(
        columns="x",
        fn=lambda vals: ["#800080" if pd.isna(x) else "red" for x in vals],
        na_color="#00FF00",
    )

    colors = [get_first_style(s, style.fill).color for s in new_gt._styles]
    assert colors == ["#FF0000", "#800080"]


def test_data_color_fn_alpha_and_autocolor_text():
    df = pd.DataFrame({"x": [1, 2]})
    new_gt = GT(df).data_color(
        columns="x", fn=lambda vals: ["black", "white"], alpha=0.5, contrast_algo="wcag"
    )

    fills = [get_first_style(s, style.fill).color for s in new_gt._styles]
    texts = [get_first_style(s, style.text).color for s in new_gt._styles]
    assert fills == ["#0000007F", "#FFFFFF7F"]
    assert texts == ["#000000", "#000000"]


def test_data_color_fn_with_rows():
    df = pd.DataFrame({"x": [1, 2, 3, 4]})
    received = []

    def color_fn(vals):
        received.extend(vals)
        return ["red"] * len(vals)

    new_gt = GT(df).data_color(columns="x", rows=[1, 3], fn=color_fn)

    assert received == [2, 4]
    assert [s.rownum for s in new_gt._styles] == [1, 3]


def test_data_color_fn_non_numeric_non_string_column():
    """`fn=` bypasses the numeric/string column type requirement."""
    df = pd.DataFrame({"x": [True, False]})
    new_gt = GT(df).data_color(columns="x", fn=lambda vals: ["green" if x else "red" for x in vals])

    colors = [get_first_style(s, style.fill).color for s in new_gt._styles]
    assert colors == ["#008000", "#FF0000"]


def test_data_color_fn_snap(snapshot: str):
    gt = GT(exibble).data_color(
        columns=["num", "char"],
        fn=lambda vals: ["lightblue" if i % 2 else "orange" for i in range(len(vals))],
        na_color="lightgray",
    )

    assert_rendered_body(snapshot, gt)


def test_data_color_fn_wrong_length_raises():
    df = pd.DataFrame({"x": [1, 2, 3]})
    with pytest.raises(ValueError, match="returned 2 colors for column 'x' but 3 were expected"):
        GT(df).data_color(columns="x", fn=lambda vals: ["red", "blue"])


def test_data_color_fn_non_string_raises():
    df = pd.DataFrame({"x": [1, 2]})
    with pytest.raises(TypeError, match="must return colors as strings"):
        GT(df).data_color(columns="x", fn=lambda vals: [1, 2])  # type: ignore[arg-type]
