from decimal import Decimal
from typing import Any, Type, TypeVar

import numpy as np
import pandas as pd
import polars as pl
import pyarrow as pa
import pyarrow.compute as pc
import pytest
from syrupy.assertion import SnapshotAssertion

from great_tables import GT, style
from great_tables._gt_data import CellStyle, StyleInfo
from great_tables._tbl_data import DataFrameLike, is_na
from great_tables.data import exibble
from tests.utils import (
    INT_UPCAST,
    OBJECT_ALIGNED_RIGHT,
    DataFrameConstructor,
    DataLike,
    Divergent,
    Render,
    assert_parity,
    assert_rendered_body,
    body_html,
    by_backend,
)

T_CellStyle = TypeVar("T_CellStyle", bound=CellStyle)

# plain and nullable pandas keep an all-missing column as `object`, which is right-aligned
PANDAS_ALL_MISSING_ALIGNED_RIGHT = Divergent(
    pandas_constructor=OBJECT_ALIGNED_RIGHT, pandas_nullable_constructor=OBJECT_ALIGNED_RIGHT
)
PANDAS_INT_UPCAST = Divergent(pandas_constructor=INT_UPCAST)

EXIBBLE_DATA = exibble[["num", "char", "currency"]].head(4).to_dict("list")
COLS_ROWS_DATA = {"a": [1, 2, 3, 4, 5, 200], "b": [51, 52, 53, 54, 55, 200]}


@pytest.fixture
def df(frame_constructor: DataFrameConstructor) -> DataFrameLike:
    return frame_constructor(EXIBBLE_DATA)


def _data_color_renderer(data: DataLike, **kwargs: Any) -> Render:
    return lambda constructor: body_html(GT(constructor(data)).data_color(**kwargs))


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


def test_data_color_simple_exibble_snap(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    assert_parity(snapshot, all_frame_constructors, _data_color_renderer(EXIBBLE_DATA))


def test_data_color_cols_rows_snap(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _data_color_renderer(COLS_ROWS_DATA, columns=["a"], rows=[0, 1, 2, 3, 4])
    assert_parity(snapshot, all_frame_constructors, render)


def test_data_color_rows_callable_matches_indices(frame_constructor: DataFrameConstructor):
    df = frame_constructor(COLS_ROWS_DATA)
    a_lt_60 = by_backend(
        df,
        pandas=lambda df_: df_["a"] < 60,
        polars=lambda df_: df_["a"] < 60,
        pyarrow=lambda tbl: pc.less(tbl["a"], 60),
    )

    assert body_html(GT(df).data_color(columns=["a"], rows=a_lt_60)) == body_html(
        GT(df).data_color(columns=["a"], rows=[0, 1, 2, 3, 4])
    )


def test_data_color_pl_cols_rows_snap(snapshot: str):
    import polars.selectors as cs

    df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 200], "b": [51, 52, 53, 54, 55, 200]})
    new_gt = GT(df).data_color(columns=["b"], rows=[0, 1, 2, 3, 4])
    assert_rendered_body(snapshot, new_gt)
    new_gt2 = GT(df).data_color(columns=cs.starts_with("b"), rows=pl.col("b").lt(60))
    assert body_html(new_gt) == body_html(new_gt2)


def test_data_color_no_rows_selected(frame_constructor: DataFrameConstructor):
    """Selecting no rows colors no cells, on every backend (pyarrow raised, see #1005)."""
    new_gt = GT(frame_constructor({"x": [1.5, 2.5, 3.5]})).data_color(columns="x", rows=[])

    assert new_gt._styles == []


@pytest.mark.parametrize("none_val", [None, np.nan, float("nan"), pd.NA])
def test_data_color_missing_value(frame_constructor: DataFrameConstructor, none_val):
    # only pandas can build a column holding pd.NA
    if none_val is pd.NA and not frame_constructor.__name__.startswith("pandas_"):
        pytest.skip()

    # whole floats would become ints on the nullable and pyarrow-backed pandas constructors
    df = frame_constructor({"x": [1.5, 2.5, none_val], "y": [3, 4, 5]})
    new_gt = GT(df).data_color("x", na_color="#FFFFF0")
    assert len(new_gt._styles) == 3
    assert get_first_style(new_gt._styles[-1], style.fill).color == "#FFFFF0"


def test_data_color_palette_snap(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _data_color_renderer(
        EXIBBLE_DATA, columns=["num", "currency"], palette=["red", "green"]
    )
    assert_parity(snapshot, all_frame_constructors, render)


def test_data_color_domain_na_color_snap(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    """`data_color` works with `domain` and `na_color`."""
    render = _data_color_renderer(
        EXIBBLE_DATA, columns="currency", palette=["red", "green"], domain=[0, 50], na_color="blue"
    )
    assert_parity(snapshot, all_frame_constructors, render)


def test_data_color_domain_na_color_reverse_snap(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    """`data_color` works with `domain`, `na_color`, and `reverse`."""
    render = _data_color_renderer(
        EXIBBLE_DATA,
        columns="currency",
        palette=["red", "green"],
        domain=[0, 50],
        na_color="blue",
        reverse=True,
    )
    assert_parity(snapshot, all_frame_constructors, render)


def test_data_color_overlapping_domain(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    """`data_color` works with overlapping `domain` (RHS domain extends outside the data range)."""
    render = _data_color_renderer(
        EXIBBLE_DATA,
        columns="currency",
        palette=["yellow", "rebeccapurple"],
        domain=[1000, 65555],
        na_color="red",
    )
    assert_parity(snapshot, all_frame_constructors, render)


def test_data_color_subset_domain(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    """`data_color` works with subset `domain`."""
    render = _data_color_renderer(
        EXIBBLE_DATA,
        columns="currency",
        palette=["yellow", "rebeccapurple"],
        domain=[1000, 60000],
        na_color="red",
    )
    assert_parity(snapshot, all_frame_constructors, render)


def test_data_color_autocolor_text_false(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    """`data_color` works with `autocolor_text=False`."""
    render = _data_color_renderer(
        EXIBBLE_DATA,
        columns="currency",
        palette=["red", "green"],
        domain=[0, 50],
        na_color="blue",
        reverse=True,
        autocolor_text=False,
    )
    assert_parity(snapshot, all_frame_constructors, render)


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


# Single value, single color: uses the first color from the palette
def test_single_value(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _data_color_renderer(
        {"x": [1], "y": [3]}, columns="x", palette=["green", "blue"], na_color="red"
    )
    assert_parity(snapshot, all_frame_constructors, render)


# Single value in multiple rows (the other rows are missing): uses the first color
# from the palette and applies `na_color=` to the missing rows
def test_single_value_from_multiple_rows(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _data_color_renderer(
        {"x": [1, None], "y": [3, 4]}, columns="x", palette=["green", "blue"], na_color="red"
    )
    assert_parity(snapshot, all_frame_constructors, render, PANDAS_INT_UPCAST)


# Multiple rows in a column but all are missing; applies `na_color=` to all rows
def test_all_missing_from_multiple_rows(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _data_color_renderer(
        {"x": [None, None], "y": [3, 6]}, columns="x", palette=["green", "blue"], na_color="red"
    )
    assert_parity(snapshot, all_frame_constructors, render, PANDAS_ALL_MISSING_ALIGNED_RIGHT)


# Single missing value from a single row; applies `na_color=` to the missing value
def test_single_value_and_missing(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _data_color_renderer(
        {"x": [None], "y": [3]}, columns="x", palette=["green", "blue"], na_color="red"
    )
    assert_parity(snapshot, all_frame_constructors, render, PANDAS_ALL_MISSING_ALIGNED_RIGHT)


# Non-missing values have a domain range of 0; applies `na_color=` to the missing values
def test_all_values_have_zero_range_domain(
    snapshot: SnapshotAssertion, all_frame_constructors: list[DataFrameConstructor]
):
    render = _data_color_renderer(
        {"x": [2, 2, None, None], "y": [3, 4, 5, 6]},
        columns="x",
        palette=["green", "blue"],
        domain=[0, 0],
    )
    assert_parity(snapshot, all_frame_constructors, render, PANDAS_INT_UPCAST)


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
    """`data_color` applies `alpha=` to colors interpolated from a gradient palette."""
    df = pd.DataFrame({"x": [0, 50, 100]})
    new_gt = GT(df).data_color(columns="x", palette=["#FF0000", "#0000FF"], alpha=0.5)

    colors = [get_first_style(s, style.fill).color.lower() for s in new_gt._styles]
    assert colors == ["#ff00007f", "#ca00887f", "#0000ff7f"]


def test_data_color_alpha_factor_palette():
    """`data_color` applies `alpha=` to colors interpolated for a factor (categorical) column."""
    df = pd.DataFrame({"x": ["a", "b", "c"]})
    new_gt = GT(df).data_color(columns="x", palette=["#FF0000", "#0000FF"], alpha=0.5)

    colors = [get_first_style(s, style.fill).color for s in new_gt._styles]
    assert all(len(c) == 9 and c.lower().endswith("7f") for c in colors)


def test_data_color_alpha_na_color_not_double_applied(frame_constructor: DataFrameConstructor):
    """`alpha=` is applied once to `na_color=`, not compounded by the gradient-palette fix."""
    # whole floats would become ints on the nullable and pyarrow-backed pandas constructors
    df = frame_constructor({"x": [1.5, 2.5, None]})
    new_gt = GT(df).data_color(columns="x", palette=["red", "blue"], alpha=0.5, na_color="#00FF00")

    na_style_color = get_first_style(new_gt._styles[-1], style.fill).color.lower()
    assert na_style_color == "#00ff007f"


def test_data_color_midpoint_symmetric_domain(frame_constructor: DataFrameConstructor):
    # whole floats would become ints on the nullable and pyarrow-backed pandas constructors
    df = frame_constructor({"x": [-2.5, 0.0, 12.5, None]})
    new_gt = GT(df).data_color(columns="x", palette=["red", "white", "green"], midpoint=0)

    colors = [get_first_style(s, style.fill).color for s in new_gt._styles]
    assert colors == ["#ffd9cb", "#ffffff", "#008000", "#808080"]


def test_data_color_midpoint_with_domain_is_piecewise():
    df = pd.DataFrame({"x": [-2, 0, 10]})
    new_gt = GT(df).data_color(
        columns="x", palette=["red", "white", "green"], domain=[-2, 10], midpoint=0
    )

    colors = [get_first_style(s, style.fill).color for s in new_gt._styles]
    assert colors == ["#ff0000", "#ffffff", "#008000"]


def test_data_color_midpoint_infinite_values_inferred_domain(
    frame_constructor: DataFrameConstructor,
):
    df = frame_constructor({"x": [-np.inf, 1.0, np.inf]})
    new_gt = GT(df).data_color(columns="x", palette=["red", "white", "green"], midpoint=0)

    colors = [get_first_style(s, style.fill).color for s in new_gt._styles]
    assert colors == ["#ff0000", "#008000", "#008000"]


def test_data_color_midpoint_all_missing_column(frame_constructor: DataFrameConstructor):
    # an `object` column on plain and nullable pandas, a null-typed one elsewhere
    df = frame_constructor({"x": [None, None]})
    new_gt = GT(df).data_color(columns="x", midpoint=0)

    colors = [get_first_style(s, style.fill).color for s in new_gt._styles]
    assert colors == ["#808080", "#808080"]


def test_data_color_midpoint_ignored_with_fn():
    df = pd.DataFrame({"x": ["a", "b"]})
    new_gt = GT(df).data_color(columns="x", midpoint=100, fn=lambda vals: ["#123456"] * len(vals))

    colors = [get_first_style(s, style.fill).color for s in new_gt._styles]
    assert colors == ["#123456"] * 2


def test_data_color_midpoint_string_column_raises(frame_constructor: DataFrameConstructor):
    df = frame_constructor({"x": ["a", "b"]})

    with pytest.raises(ValueError, match="can only be used with numeric columns"):
        GT(df).data_color(columns="x", midpoint=0)


def test_data_color_midpoint_outside_domain_raises():
    df = pd.DataFrame({"x": [1, 2]})

    with pytest.raises(ValueError, match="must lie within the range of `domain=`"):
        GT(df).data_color(columns="x", domain=[0, 10], midpoint=50)


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


def test_data_color_fn_receives_missing_values(frame_constructor: DataFrameConstructor):
    """Missing values are passed to `fn=` (as in gt); `None` results get `na_color=`."""
    # whole floats would become ints on the nullable and pyarrow-backed pandas constructors
    df = frame_constructor({"x": [1.5, None, 3.5, 4.5]})
    received = []

    def color_fn(vals):
        received.extend(vals)
        return [None if is_na(df, x) or x == 4.5 else "red" for x in vals]

    new_gt = GT(df).data_color(columns="x", fn=color_fn, na_color="#00FF00")

    # `fn=` gets each backend's own missing value; whether to unify them is undecided
    missing_str = {
        "pandas_constructor": "nan",
        "pandas_nullable_constructor": "<NA>",
        "pandas_pyarrow_constructor": "<NA>",
    }.get(frame_constructor.__name__, "None")
    assert [str(x) for x in received] == ["1.5", missing_str, "3.5", "4.5"]

    colors = [get_first_style(s, style.fill).color for s in new_gt._styles]
    assert colors == ["#FF0000", "#00FF00", "#FF0000", "#00FF00"]


def test_data_color_fn_can_color_missing_values(frame_constructor: DataFrameConstructor):
    """`fn=` decides the color of missing values, overriding `na_color=`."""
    df = frame_constructor({"x": [1.5, None]})
    new_gt = GT(df).data_color(
        columns="x",
        fn=lambda vals: ["#800080" if is_na(df, x) else "red" for x in vals],
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


def test_data_color_fn_with_rows(frame_constructor: DataFrameConstructor):
    df = frame_constructor({"x": [1, 2, 3, 4]})
    received = []

    def color_fn(vals):
        received.extend(vals)
        return ["red"] * len(vals)

    new_gt = GT(df).data_color(columns="x", rows=[1, 3], fn=color_fn)

    assert received == [2, 4]
    assert [s.rownum for s in new_gt._styles] == [1, 3]


def test_data_color_fn_non_numeric_non_string_column(frame_constructor: DataFrameConstructor):
    """`fn=` bypasses the numeric/string column type requirement."""
    df = frame_constructor({"x": [True, False]})
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


def get_fill_colors(gt: GT) -> list[str]:
    return [get_first_style(s, style.fill).color.lower() for s in gt._styles]


@pytest.mark.parametrize("storage", ["python", "pyarrow"])
def test_data_color_pd_string_dtype_with_na(storage: str):
    """`data_color` handles `pd.NA` in a pandas `string` column rather than raising."""
    df = pd.DataFrame({"x": pd.array(["a", None, "b"], dtype=f"string[{storage}]")})
    new_gt = GT(df).data_color(columns="x", palette=["red", "blue"])

    assert get_fill_colors(new_gt) == ["#ff0000", "#808080", "#0000ff"]


def test_data_color_pd_string_dtype_with_na_and_domain():
    """`pd.NA` gets the `na_color=` color when a factor `domain=` is supplied."""
    df = pd.DataFrame({"x": pd.array(["a", None, "b"], dtype="string")})
    new_gt = GT(df).data_color(columns="x", palette=["red", "blue"], domain=["b", "a"])

    assert get_fill_colors(new_gt) == ["#0000ff", "#808080", "#ff0000"]


@pytest.mark.parametrize(
    "df",
    [
        pytest.param(
            pd.DataFrame(
                {"x": pd.Categorical(["high", "low", "mid"], ["low", "mid", "high"], ordered=True)}
            ),
            id="pandas-ordered-categorical",
        ),
        pytest.param(
            pl.DataFrame(
                {"x": pl.Series(["high", "low", "mid"], dtype=pl.Enum(["low", "mid", "high"]))}
            ),
            id="polars-enum",
        ),
        pytest.param(
            pa.table(
                {
                    "x": pa.DictionaryArray.from_arrays(
                        pa.array([2, 0, 1], pa.int32()),
                        pa.array(["low", "mid", "high"]),
                        ordered=True,
                    )
                }
            ),
            id="pyarrow-ordered-dictionary",
        ),
    ],
)
def test_data_color_ordered_categorical_uses_levels(df: DataFrameLike):
    """An inferred domain follows the declared level order, not the order of appearance."""
    new_gt = GT(df).data_color(columns="x", palette=["red", "blue"])

    assert get_fill_colors(new_gt) == ["#0000ff", "#ff0000", "#ca0088"]


def test_data_color_unordered_categorical_uses_appearance_order():
    """An unordered pandas `Categorical` keeps the order-of-appearance domain."""
    x = pd.Categorical(["high", "low", "mid"], categories=["low", "mid", "high"])
    new_gt = GT(pd.DataFrame({"x": x})).data_color(columns="x", palette=["red", "blue"])

    assert get_fill_colors(new_gt) == ["#ff0000", "#ca0088", "#0000ff"]


@pytest.mark.parametrize(
    "df",
    [
        pytest.param(
            pd.DataFrame({"x": pd.Categorical(["a", "c"], ["a", "b", "c"], ordered=True)}),
            id="pandas-ordered-categorical",
        ),
        pytest.param(
            pl.DataFrame({"x": pl.Series(["a", "c"], dtype=pl.Enum(["a", "b", "c"]))}),
            id="polars-enum",
        ),
        pytest.param(
            pa.table(
                {
                    "x": pa.DictionaryArray.from_arrays(
                        pa.array([0, 2], pa.int32()), pa.array(["a", "b", "c"]), ordered=True
                    )
                }
            ),
            id="pyarrow-ordered-dictionary",
        ),
    ],
)
def test_data_color_enum_unused_levels_and_rows(df: DataFrameLike):
    """Declared levels define the domain even when some are unused or rows are filtered."""
    assert get_fill_colors(GT(df).data_color(columns="x", palette=["red", "blue"])) == [
        "#ff0000",
        "#0000ff",
    ]
    assert get_fill_colors(GT(df).data_color(columns="x", rows=[1], palette=["red", "blue"])) == [
        "#0000ff"
    ]


def test_data_color_enum_explicit_domain_takes_precedence():
    """A supplied `domain=` overrides the declared levels of an ordered column."""
    df = pl.DataFrame(
        {"x": pl.Series(["high", "low", "mid"], dtype=pl.Enum(["low", "mid", "high"]))}
    )
    new_gt = GT(df).data_color(columns="x", palette=["red", "blue"], domain=["mid", "high", "low"])

    assert get_fill_colors(new_gt) == ["#ca0088", "#0000ff", "#ff0000"]


def test_data_color_decimal_values(frame_constructor: DataFrameConstructor):
    """`Decimal` values are scaled as numbers."""
    df = frame_constructor({"x": [Decimal("0"), Decimal("5"), None, Decimal("10")]})
    new_gt = GT(df).data_color(columns="x", palette=["red", "blue"])

    assert get_fill_colors(new_gt) == ["#ff0000", "#ca0088", "#808080", "#0000ff"]


def test_data_color_decimal_values_with_domain():
    """`Decimal` values can be scaled against an integer `domain=`."""
    df = pd.DataFrame({"x": [Decimal("0"), Decimal("5")]})
    new_gt = GT(df).data_color(columns="x", palette=["red", "blue"], domain=[0, 10])

    assert get_fill_colors(new_gt) == ["#ff0000", "#ca0088"]


def test_data_color_fn_receives_decimal_values(frame_constructor: DataFrameConstructor):
    """Values passed to `fn=` are not converted from `Decimal`."""
    seen: list[Any] = []

    def fn(vals: list[Any]) -> list[str]:
        seen.extend(vals)
        return ["red"] * len(vals)

    GT(frame_constructor({"x": [Decimal("1.5")]})).data_color(columns="x", fn=fn)

    assert seen == [Decimal("1.5")] and isinstance(seen[0], Decimal)


def test_data_color_infinite_values_inferred_domain(frame_constructor: DataFrameConstructor):
    """Infinite values are left out of an inferred domain and placed at its ends."""
    df = frame_constructor({"x": [-np.inf, 1.0, 2.0, 3.0, np.inf]})
    new_gt = GT(df).data_color(columns="x", palette=["red", "blue"])

    assert get_fill_colors(new_gt) == ["#ff0000", "#ff0000", "#ca0088", "#0000ff", "#0000ff"]


@pytest.mark.parametrize(
    "vals, expected",
    [
        ([np.inf, -np.inf], ["#0000ff", "#ff0000"]),
        ([2.0, np.inf], ["#ff0000", "#0000ff"]),
    ],
)
def test_data_color_infinite_values_degenerate_domain(vals: list[float], expected: list[str]):
    """Infinite values still take the end colors when there is no finite range to infer."""
    new_gt = GT(pd.DataFrame({"x": vals})).data_color(columns="x", palette=["red", "blue"])

    assert get_fill_colors(new_gt) == expected


@pytest.mark.parametrize("truncate, expected", [(False, "#808080"), (True, "#0000ff")])
def test_data_color_infinite_values_explicit_domain(truncate: bool, expected: str):
    """With a supplied `domain=`, infinite values are handled like any out-of-domain value."""
    df = pd.DataFrame({"x": [1.0, np.inf]})
    new_gt = GT(df).data_color(
        columns="x", palette=["red", "blue"], domain=[0, 2], truncate=truncate
    )

    assert get_fill_colors(new_gt) == ["#ca0088", expected]


def get_fill_colors_by_cell(gt: GT) -> dict[tuple[str, int], str]:
    return {(s.colname, s.rownum): get_first_style(s, style.fill).color.lower() for s in gt._styles}


def test_data_color_direction_row(frame_constructor: DataFrameConstructor):
    """With `direction="row"`, each row is colored across the targeted columns on its own domain."""
    # whole floats would become ints on the nullable and pyarrow-backed pandas constructors
    df = frame_constructor({"a": [1.5, 10.5, 5.5], "b": [2.5, 20.5, None], "c": [3.5, 30.5, 6.5]})
    new_gt = GT(df).data_color(palette=["red", "blue"], direction="row")

    assert get_fill_colors_by_cell(new_gt) == {
        ("a", 0): "#ff0000",
        ("b", 0): "#ca0088",
        ("c", 0): "#0000ff",
        ("a", 1): "#ff0000",
        ("b", 1): "#ca0088",
        ("c", 1): "#0000ff",
        ("a", 2): "#ff0000",
        ("b", 2): "#808080",
        ("c", 2): "#0000ff",
    }


def test_data_color_direction_column_is_default():
    df = pd.DataFrame({"a": [1, 10], "b": [20, 2]})

    assert get_fill_colors(GT(df).data_color(palette=["red", "blue"])) == get_fill_colors(
        GT(df).data_color(palette=["red", "blue"], direction="column")
    )
    assert get_fill_colors_by_cell(GT(df).data_color(palette=["red", "blue"], direction="row")) == {
        ("a", 0): "#ff0000",
        ("b", 0): "#0000ff",
        ("a", 1): "#0000ff",
        ("b", 1): "#ff0000",
    }


def test_data_color_direction_row_columns_and_rows():
    """Only the targeted rows are colored, using the values of the targeted columns."""
    df = pd.DataFrame({"a": [1, 4, 7], "b": [2, 5, 8], "c": [3, 6, 100]})
    new_gt = GT(df).data_color(
        columns=["a", "b"], rows=[0, 2], palette=["red", "blue"], direction="row"
    )

    assert get_fill_colors_by_cell(new_gt) == {
        ("a", 0): "#ff0000",
        ("b", 0): "#0000ff",
        ("a", 2): "#ff0000",
        ("b", 2): "#0000ff",
    }


def test_data_color_direction_row_strings():
    """String values in a row are treated as categories, in the order they appear in the row."""
    df = pd.DataFrame({"a": ["x", "z"], "b": ["y", "x"], "c": ["x", "y"]})
    new_gt = GT(df).data_color(palette=["red", "blue"], direction="row")

    assert get_fill_colors_by_cell(new_gt) == {
        ("a", 0): "#ff0000",
        ("b", 0): "#0000ff",
        ("c", 0): "#ff0000",
        ("a", 1): "#ff0000",
        ("b", 1): "#ca0088",
        ("c", 1): "#0000ff",
    }


def test_data_color_direction_row_fn(frame_constructor: DataFrameConstructor):
    """With `fn=`, the function receives the values of each row."""
    df = frame_constructor({"a": [1, 3], "b": [2, 4]})
    seen = []

    def fn(vals):
        seen.append(vals)
        return ["red" if x == max(vals) else "blue" for x in vals]

    new_gt = GT(df).data_color(fn=fn, direction="row")

    assert seen == [[1, 2], [3, 4]]
    assert get_fill_colors_by_cell(new_gt) == {
        ("a", 0): "#0000ff",
        ("b", 0): "#ff0000",
        ("a", 1): "#0000ff",
        ("b", 1): "#ff0000",
    }


def test_data_color_direction_row_mixed_types_raises():
    df = pd.DataFrame({"a": [1, 2], "b": ["x", "y"]})

    with pytest.raises(ValueError, match="Invalid values in row 0"):
        GT(df).data_color(direction="row")


def test_data_color_direction_invalid_raises():
    df = pd.DataFrame({"a": [1, 2]})

    with pytest.raises(ValueError, match='`direction=` must be either "column" or "row"'):
        GT(df).data_color(direction="rows")  # type: ignore[arg-type]
