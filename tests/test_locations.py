import pandas as pd
import polars as pl
import polars.selectors as cs
import pytest
from great_tables import GT, stub
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
    LocGrandSummaryStub,
    LocGrandSummary,
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


@pytest.mark.parametrize(
    "rows, res",
    [
        (0, {0}),
        ("min", {1}),
        (["min"], {1}),
        (["min", 0], {0, 1}),
        (["min", -1], {1}),
    ],
)
def test_resolve_loc_grand_summary_stub(rows, res):
    df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
    gt = (
        GT(df)
        .grand_summary_rows(fns={"min": lambda x: x.min()}, side="bottom")
        .grand_summary_rows(fns={"max": lambda x: x.max()}, side="top")
    )

    cells = resolve(LocGrandSummaryStub(rows), gt)

    assert cells == res


@pytest.mark.parametrize(
    "cols, rows, resolved_subset, length",
    [
        (["x"], ["max"], CellPos(column=0, row=0, colname="x", rowname=None), 1),
        ([1], ["min"], CellPos(column=1, row=1, colname="y", rowname=None), 1),
        ([-1], [0, 1], CellPos(column=1, row=0, colname="y", rowname=None), 2),
        ([-1, "x"], ["max", 1], CellPos(column=0, row=0, colname="x", rowname=None), 4),
    ],
)
def test_resolve_loc_grand_summary(cols, rows, resolved_subset, length):
    df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
    gt = (
        GT(df)
        .grand_summary_rows(fns={"min": lambda x: x.min()}, side="bottom")
        .grand_summary_rows(fns={"max": lambda x: x.max()}, side="top")
    )

    cells = resolve(LocGrandSummary(columns=cols, rows=rows), gt)

    assert isinstance(cells, list)
    assert len(cells) == length
    assert resolved_subset in cells


def test_set_style_singledispatch_fallback_raises():
    fallback = set_style.dispatch(object)
    with pytest.raises(NotImplementedError, match="Unsupported location type"):
        fallback("not_a_loc", None, [])


def test_resolve_unknown_loc_type_raises():
    # singledispatch fallback raises NotImplementedError for unknown Loc type
    class UnknownLoc:
        pass

    fallback = resolve.dispatch(object)
    with pytest.raises(NotImplementedError, match="Unsupported location type"):
        fallback(UnknownLoc())


def test_resolve_grand_summary_with_mask_raises():
    # NotImplementedError when mask is provided for LocGrandSummary
    import polars as pl

    df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
    gt = GT(df).grand_summary_rows(fns={"total": lambda df: df.sum()})
    built = gt._build_data("html")
    loc_gs = LocGrandSummary(mask=pl.col("x") > 0)
    with pytest.raises(NotImplementedError, match="Masked selection is not yet implemented"):
        resolve(loc_gs, built)


def test_resolve_grand_summary_columns_and_mask_raises():
    # ValueError when both columns/rows and mask specified for LocGrandSummary
    import polars as pl

    df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
    gt = GT(df).grand_summary_rows(fns={"total": lambda df: df.sum()})
    built = gt._build_data("html")
    loc_gs = LocGrandSummary(columns="x", mask=pl.col("x") > 0)
    with pytest.raises(ValueError, match="Cannot specify.*mask.*along with.*columns.*rows"):
        resolve(loc_gs, built)


def test_resolve_cols_i_stub_expr():
    # Resolve_cols_i with "stub()" in expr list returns stub column
    gt = GT(pd.DataFrame({"x": [1, 2], "y": [3, 4]}), rowname_col="x")
    built = gt._build_data("html")

    # The stub column is excluded by default, like a stub column given by name
    assert resolve_cols_i(built, ["stub()"]) == []
    assert resolve_cols_i(built, ["stub()"], excl_stub=False) == [("x", 0)]


def test_resolve_cols_i_null_means_nothing():
    # Resolve_cols_i with expr=None and null_means="nothing" returns []
    gt = GT(pd.DataFrame({"x": [1, 2], "y": [3, 4]}))
    built = gt._build_data("html")
    result = resolve_cols_i(built, None, null_means="nothing")

    assert result == []


# Stub and row group columns in column selections ----------------------------------------------


def _stub_gt():
    from great_tables import GT

    df = pl.DataFrame(
        {
            "a": ["A", "A", "B"],
            "b": ["x", "y", "z"],
            "g": ["G", "G", "H"],
            "n1": [1.5, 2.5, 3.5],
            "n2": [4, 5, 6],
        }
    )
    return GT(df, rowname_col=["a", "b"], groupname_col="g")


@pytest.mark.parametrize("columns", ["b", ["a", "n1"], stub, stub(2)])
def test_loc_body_stub_columns_raise(columns):
    from great_tables import loc, style

    with pytest.raises(ValueError, match="can't target stub columns.*loc.stub"):
        _stub_gt().tab_style(style.fill("red"), loc.body(columns=columns))


def test_loc_body_stub_column_footnote_raises():
    # A footnote on a stub cell via `loc.body()` used to be listed with no mark in the table
    from great_tables import loc

    with pytest.raises(ValueError, match="can't target stub columns"):
        _stub_gt().tab_footnote("note", loc.body(columns="b", rows=[0]))


def test_loc_body_group_column_raises():
    from great_tables import loc, style

    with pytest.raises(ValueError, match="can't target the row group column.*loc.row_groups"):
        _stub_gt().tab_style(style.fill("red"), loc.body(columns="g"))


def test_loc_body_selector_skips_stub_and_group_columns():
    from great_tables import loc, style

    gt = _stub_gt().tab_style(style.fill("red"), loc.body(columns=cs.all()))
    assert sorted({x.colname for x in gt._styles}) == ["n1", "n2"]


@pytest.mark.parametrize(
    "columns,x_out",
    [
        (stub, [("a", 0), ("b", 1)]),
        (stub(1), [("b", 1)]),
        (stub(2), [("a", 0)]),
        ([stub(1), "n2"], [("b", 1), ("n2", 4)]),
        (["stub()"], [("a", 0), ("b", 1)]),
    ],
)
def test_resolve_cols_i_stub_selectors(columns, x_out):
    built = _stub_gt()._build_data("html")
    assert resolve_cols_i(built, columns, excl_stub=False) == x_out

    # Like stub column names, stub selectors are excluded unless `excl_stub=False`
    assert [x for x in resolve_cols_i(built, columns) if x[0] in ("a", "b")] == []


def test_resolve_cols_i_stub_selector_level_too_large():
    built = _stub_gt()._build_data("html")
    with pytest.raises(ValueError, match="stub level 3"):
        resolve_cols_i(built, stub(3), excl_stub=False)


def test_resolve_cols_i_excludes_stub_and_group_by_default():
    built = _stub_gt()._build_data("html")

    assert resolve_cols_i(built, ["a", "g", "n1"]) == [("n1", 3)]
    assert resolve_cols_i(built, ["a", "g", "n1"], excl_stub=False) == [("a", 0), ("n1", 3)]
    assert resolve_cols_i(built, ["a", "g", "n1"], excl_group=False) == [("g", 2), ("n1", 3)]


def test_fmt_can_target_stub_columns():
    from great_tables.gt import _get_column_of_values

    gt = _stub_gt().fmt(lambda x: x.upper(), columns=stub(1)).fmt(lambda x: f"<{x}>", columns="a")
    assert _get_column_of_values(gt, column_name="b", context="html") == ["X", "Y", "Z"]
    assert _get_column_of_values(gt, column_name="a", context="html") == ["<A>", "<A>", "<B>"]


def test_tab_spanner_excludes_stub_columns():
    gt = _stub_gt().tab_spanner("S", columns=["a", "n1"])
    assert [x.vars for x in gt._spanners] == [["n1"]]


@pytest.mark.parametrize(
    "method,kwargs,arg",
    [
        ("cols_move_to_start", dict(columns="a"), "columns"),
        ("cols_move_to_end", dict(columns=["n1", "b"]), "columns"),
        ("cols_move", dict(columns="n2", after="b"), "after"),
        ("cols_move", dict(columns="g", after="n1"), "columns"),
    ],
)
def test_cols_move_stub_or_group_columns_raise(method: str, kwargs: dict, arg: str):
    with pytest.raises(ValueError, match=f"`{arg}=` can't include stub or row group columns"):
        getattr(_stub_gt(), method)(**kwargs)


def test_cols_hide_and_unhide_stub_column():
    gt = _stub_gt().cols_hide("a")
    assert [x.var for x in gt._boxhead if not x.visible] == ["a"]

    gt = gt.cols_unhide("a")
    assert [x.var for x in gt._boxhead if not x.visible] == []


@pytest.mark.parametrize("rows,x_out", [("A", [0, 1]), ("y", [1]), (["B", "x"], [0, 2])])
def test_loc_stub_row_names_match_any_stub_column(rows, x_out: list[int]):
    # Without `columns=`, row names are matched against every stub column (as in R gt)
    from great_tables import loc, style

    gt = _stub_gt().tab_style(style.fill("red"), loc.stub(rows=rows))
    assert sorted({x.rownum for x in gt._styles}) == x_out


def test_tab_style_body_match_in_stub_column():
    # A match in a stub column styles the stub (with `extents="stub"`), never a body cell for
    # the stub column
    from great_tables import style

    gt = _stub_gt().tab_style_body(
        style=style.fill("red"),
        columns=["b", "n1"],
        values=["y"],
        targets="row",
        extents=["body", "stub"],
    )
    cells = sorted((type(x.locname).__name__, x.colname, x.rownum) for x in gt._styles)
    assert cells == [("LocBody", "n1", 1), ("LocStub", None, 1)]


def test_default_columns_exclude_stub_and_group():
    # With no `columns=`, methods that can target the stub still only select the body columns
    # (e.g., `fmt_integer()` mustn't try to format a string stub or group column)
    from great_tables.gt import _get_column_of_values

    gt = _stub_gt().fmt_integer()
    assert _get_column_of_values(gt, column_name="n1", context="html") == ["2", "2", "4"]
    assert _get_column_of_values(gt, column_name="a", context="html") == ["A", "A", "B"]

    built = _stub_gt()._build_data("html")
    expected = [("n1", 3), ("n2", 4)]
    assert resolve_cols_i(built, None, excl_stub=False, excl_group=False) == expected


def test_data_color_default_columns_exclude_stub():
    # As in R gt, `data_color()` with no `columns=` colors the body cells only
    gt = _stub_gt().data_color()
    assert sorted({x.colname for x in gt._styles}) == ["n1", "n2"]
