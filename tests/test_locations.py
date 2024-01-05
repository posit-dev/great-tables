import pandas as pd
import polars as pl
import pytest

from great_tables._locations import (
    LocColumnSpanners,
    LocBody,
    LocTitle,
    CellPos,
    resolve,
    resolve_vector_i,
    resolve_cols_i,
    resolve_rows_i,
    set_style,
)
from great_tables._styles import CellStyleText, FromColumn
from great_tables._gt_data import Spanners, SpannerInfo
from great_tables import GT


def test_resolve_vector_i():
    assert resolve_vector_i(["x", "a"], ["a", "b", "x"], "") == [0, 2]


def test_resolve_cols_i_gt_data():
    gt = GT(pd.DataFrame(columns=["a", "b", "x"]))
    assert resolve_cols_i(gt, ["x", "a"]) == [("x", 2), ("a", 0)]


def test_resolve_cols_i_strings():
    df = pd.DataFrame(columns=["a", "b", "x"])
    assert resolve_cols_i(df, ["x", "a"]) == [("x", 2), ("a", 0)]


def test_resolve_cols_i_ints():
    df = pd.DataFrame(columns=["a", "b", "x"])
    assert resolve_cols_i(df, [-1, 0]) == [("x", 2), ("a", 0)]


def test_resolve_rows_i_gt_data():
    gt = GT(pd.DataFrame({"x": ["a", "b", "c"]}), rowname_col="x")
    assert resolve_rows_i(gt, ["b", "a"]) == [("a", 0), ("b", 1)]


def test_resolve_rows_i_strings():
    assert resolve_rows_i(["a", "x", "a", "b"], ["x", "a"]) == [("a", 0), ("x", 1), ("a", 2)]


def test_resolve_rows_i_ints():
    assert resolve_rows_i(["a", "x", "a", "b"], [0, -1]) == [("a", 0), ("b", 3)]


def test_resolve_rows_i_polars_expr():
    gt = GT(pl.DataFrame({"x": ["a", "b", "c"]}), rowname_col="x")
    assert resolve_rows_i(gt, pl.col("x").is_in(["a", "b"])) == [("a", 0), ("b", 1)]


def test_resolve_rows_i_func_expr():
    gt = GT(pd.DataFrame({"x": ["a", "b", "c"]}), rowname_col="x")
    assert resolve_rows_i(gt, lambda D: D["x"].isin(["a", "b"])) == [("a", 0), ("b", 1)]


def test_resolve_loc_body():
    gt = GT(pd.DataFrame({"x": [1, 2], "y": [3, 4]}))

    cells = resolve(LocBody(["x"], [-1]), gt)

    assert isinstance(cells, list)
    assert len(cells) == 1
    assert isinstance(cells[0], CellPos)

    pos = cells[0]

    assert pos.column == 0
    assert pos.row == 1
    assert pos.colname == "x"


def test_resolve_column_spanners_simple():
    # note that this essentially a no-op
    ids = ["a", "b", "c"]

    spanners = Spanners.from_ids(ids)
    loc = LocColumnSpanners(ids=["a", "c"])

    new_loc = resolve(loc, spanners)

    assert new_loc == loc
    assert new_loc.ids == ["a", "c"]


def test_resolve_column_spanners_error_missing():
    # note that this essentially a no-op
    ids = ["a", "b", "c"]

    spanners = Spanners.from_ids(ids)
    loc = LocColumnSpanners(ids=["a", "d"])

    with pytest.raises(ValueError):
        resolve(loc, spanners)


@pytest.mark.parametrize(
    "expr",
    [
        FromColumn("color"),
        pl.col("color"),
        pl.col("color").str.to_uppercase().str.to_lowercase(),
    ],
)
def test_set_style_loc_body_from_column(expr):
    df = pd.DataFrame({"x": [1, 2], "color": ["red", "blue"]})

    if isinstance(expr, pl.Expr):
        gt_df = GT(pl.DataFrame(df))
    else:
        gt_df = GT(df)

    loc = LocBody(["x"], [1])
    style = CellStyleText(color=expr)

    new_gt = set_style(loc, gt_df, [style])

    # 1 style info added
    assert len(new_gt._styles) == 1
    cell_info = new_gt._styles[0]

    # style info has single cell style, with new color
    assert len(cell_info.styles) == 1
    assert isinstance(cell_info.styles[0], CellStyleText)
    assert cell_info.styles[0].color == "blue"


def test_set_style_loc_title_from_column_error(snapshot):
    df = pd.DataFrame({"x": [1, 2], "color": ["red", "blue"]})
    gt_df = GT(df)
    loc = LocTitle("title")
    style = CellStyleText(color=FromColumn("color"))

    with pytest.raises(TypeError) as exc_info:
        set_style(loc, gt_df, [style])

    assert snapshot == exc_info.value.args[0]
