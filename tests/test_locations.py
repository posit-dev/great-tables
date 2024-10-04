import pandas as pd
import polars as pl
import polars.selectors as cs
import pytest
from great_tables import GT
from great_tables._gt_data import Spanners
from great_tables._locations import (
    CellPos,
    LocBody,
    LocColumnLabels,
    LocSpannerLabels,
    LocRowGroups,
    LocSpannerLabels,
    LocStub,
    LocTitle,
    resolve,
    resolve_cols_i,
    resolve_rows_i,
    resolve_vector_i,
    set_style,
)
from great_tables._styles import CellStyleText, FromColumn


def test_resolve_vector_i():
    assert resolve_vector_i(["x", "a"], ["a", "b", "x"], "") == [0, 2]


def test_resolve_vector_i_raises():
    with pytest.raises(NotImplementedError) as exc_info:
        resolve_vector_i([1, 2], ["a", "b", "x"], "")

    assert "Selecting entries currently requires a list of strings." in exc_info.value.args[0]


def test_resolve_cols_i_gt_data():
    gt = GT(pd.DataFrame(columns=["a", "b", "x"]))
    assert resolve_cols_i(gt, ["x", "a"]) == [("x", 2), ("a", 0)]


def test_resolve_cols_i_polars_in_list():
    gt = GT(pl.DataFrame({"a": [], "b": [], "x": []}))
    assert resolve_cols_i(gt, [pl.col("x"), "a"]) == [("x", 2), ("a", 0)]


def test_resolve_cols_i_strings():
    df = pd.DataFrame(columns=["a", "b", "x"])
    assert resolve_cols_i(df, ["x", "a"]) == [("x", 2), ("a", 0)]


def test_resolve_cols_i_ints():
    df = pd.DataFrame(columns=["a", "b", "x"])
    assert resolve_cols_i(df, [-1, 0]) == [("x", 2), ("a", 0)]


def test_resolve_cols_i_raises():
    df = pd.DataFrame(columns=["a", "b", "x"])
    assert resolve_cols_i(df, [-1, 0]) == [("x", 2), ("a", 0)]


def test_resolve_rows_i_gt_data():
    gt = GT(pd.DataFrame({"x": ["a", "b", "c"]}), rowname_col="x")
    assert resolve_rows_i(gt, ["b", "a"]) == [("a", 0), ("b", 1)]


def test_resolve_rows_i_gt_data_nothing():
    gt = GT(pd.DataFrame({"x": ["a", "b", "c"]}), rowname_col="x")
    assert resolve_rows_i(gt, null_means="nothing") == []


@pytest.mark.parametrize("s, resolved", [("x", [("x", 1)]), ("a", [("a", 0), ("a", 2)])])
def test_resolve_rows_i_string(s, resolved):
    assert resolve_rows_i(["a", "x", "a", "b"], s) == resolved


def test_resolve_rows_i_strings():
    assert resolve_rows_i(["a", "x", "a", "b"], ["x", "a"]) == [("a", 0), ("x", 1), ("a", 2)]


@pytest.mark.parametrize("i, resolved", [(0, [("a", 0)]), (-1, [("b", 3)])])
def test_resolve_rows_i_int(i, resolved):
    assert resolve_rows_i(["a", "x", "a", "b"], i) == resolved


def test_resolve_rows_i_ints():
    assert resolve_rows_i(["a", "x", "a", "b"], [0, -1]) == [("a", 0), ("b", 3)]


def test_resolve_rows_i_polars_expr():
    gt = GT(pl.DataFrame({"x": ["a", "b", "c"]}), rowname_col="x")
    assert resolve_rows_i(gt, pl.col("x").is_in(["a", "b"])) == [("a", 0), ("b", 1)]


def test_resolve_rows_i_func_expr():
    gt = GT(pd.DataFrame({"x": ["a", "b", "c"]}), rowname_col="x")
    assert resolve_rows_i(gt, lambda D: D["x"].isin(["a", "b"])) == [("a", 0), ("b", 1)]


def test_resolve_rows_i_func_expr_return_non_bool_pd_series():
    gt = GT(pd.DataFrame({"x": ["a", "b", "c"]}), rowname_col="x")
    with pytest.raises(ValueError) as exc_info:
        resolve_rows_i(gt, lambda D: pd.Series([4, 5, 6]))

    assert (
        "If you select rows using a callable, it must take a DataFrame, "
        + "and return a boolean Series."
        in exc_info.value.args[0]
    )


@pytest.mark.parametrize("bad_expr", [(4, 5, 6), {7, 8, 9}, {"col1": 1, "col2": 2, "col3": 3}])
def test_resolve_rows_i_raises(bad_expr):
    gt = GT(pd.DataFrame({"x": ["a", "b", "c"]}), rowname_col="x")
    with pytest.raises(NotImplementedError) as exc_info:
        resolve_rows_i(gt, bad_expr)

    expected = exc_info.value.args[0]
    assert "Currently, rows can only be selected using these approaches:" in expected
    assert "a list of integers" in expected
    assert "a polars expression" in expected
    assert "a callable that takes a DataFrame and returns a boolean Series" in expected


# Resolve Loc tests --------------------------------------------------------------------------------


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


@pytest.mark.xfail
def test_resolve_loc_spanners_label_single():
    spanners = Spanners.from_ids(["a", "b"])
    loc = LocSpannerLabels(ids="a")

    new_loc = resolve(loc, spanners)

    assert new_loc.ids == ["a"]


@pytest.mark.parametrize(
    "expr",
    [
        ["a", "c"],
        pytest.param(cs.by_name("a", "c"), marks=pytest.mark.xfail),
    ],
)
def test_resolve_loc_spanners_label(expr):
    # note that this essentially a no-op
    ids = ["a", "b", "c"]

    spanners = Spanners.from_ids(ids)
    loc = LocSpannerLabels(ids=expr)

    new_loc = resolve(loc, spanners)

    assert new_loc.ids == ["a", "c"]


def test_resolve_loc_spanner_label_error_missing():
    # note that this essentially a no-op
    ids = ["a", "b", "c"]

    spanners = Spanners.from_ids(ids)
    loc = LocSpannerLabels(ids=["a", "d"])

    with pytest.raises(ValueError):
        resolve(loc, spanners)


@pytest.mark.parametrize(
    "rows, res",
    [
        (2, {"b"}),
        ([2], {"b"}),
        ("b", {"b"}),
        (["a", "c"], {"a", "c"}),
        ([0, 1], {"a"}),
        (None, {"a", "b", "c"}),
        (pl.col("group") == "b", {"b"}),
    ],
)
def test_resolve_loc_row_groups(rows, res):
    df = pl.DataFrame({"group": ["a", "a", "b", "c"]})
    loc = LocRowGroups(rows=rows)
    new_loc = resolve(loc, GT(df, groupname_col="group"))

    assert isinstance(new_loc, set)
    assert new_loc == res


@pytest.mark.parametrize(
    "rows, res",
    [
        (2, {2}),
        ([2], {2}),
        ("b", {2}),
        (["a", "c"], {0, 1, 3}),
        ([0, 1], {0, 1}),
        (pl.col("row") == "a", {0, 1}),
    ],
)
def test_resolve_loc_stub(rows, res):
    df = pl.DataFrame({"row": ["a", "a", "b", "c"]})
    loc = LocStub(rows=rows)
    new_loc = resolve(loc, GT(df, rowname_col="row"))

    assert isinstance(new_loc, set)
    assert new_loc == res


@pytest.mark.parametrize(
    "cols, res",
    [
        (["b"], [("b", 1)]),
        ([0, 2], [("a", 0), ("c", 2)]),
        (cs.by_name("a"), [("a", 0)]),
    ],
)
def test_resolve_loc_column_labels(cols, res):
    df = pl.DataFrame({"a": [0], "b": [1], "c": [2]})
    loc = LocColumnLabels(columns=cols)

    selected = resolve(loc, GT(df))
    assert selected == res


@pytest.mark.parametrize(
    "ids, res",
    [
        (["b"], ["b"]),
        (["a", "b"], ["a", "b"]),
        pytest.param(cs.by_name("a"), ["a"], marks=pytest.mark.xfail),
    ],
)
def test_resolve_loc_spanner_labels(ids, res):
    df = pl.DataFrame({"x": [0], "y": [1], "z": [2]})
    gt = GT(df).tab_spanner("a", ["x", "y"]).tab_spanner("b", ["z"])
    loc = LocSpannerLabels(ids=ids)

    new_loc = resolve(loc, gt._spanners)
    assert new_loc.ids == res


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
    loc = LocTitle()
    style = CellStyleText(color=FromColumn("color"))

    with pytest.raises(TypeError) as exc_info:
        set_style(loc, gt_df, [style])

    assert snapshot == exc_info.value.args[0]
