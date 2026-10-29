from typing import Callable

import pandas as pd
import polars as pl
import pyarrow as pa
import pyarrow.compute as pc
import pytest

from great_tables import GT, loc, style, vals
from great_tables._utils_render_html import create_body_component_h
from tests.utils import DataFrameConstructor, assert_parity, assert_rendered_body, by_backend


def render_only_body(gt) -> str:
    built = gt._build_data("html")
    body = create_body_component_h(built)

    return body


def mean_expr(df: pd.DataFrame):
    return df.mean(numeric_only=True)


def min_expr(df: pd.DataFrame):
    return df.min(numeric_only=True)


def max_expr(df: pd.DataFrame):
    return df.max(numeric_only=True)


def pyarrow_summary(
    fn: Callable[[pa.ChunkedArray], pa.Scalar], columns: list[str]
) -> Callable[[pa.Table], pa.Table]:
    # pyarrow has no expressions, so a summary function returns a one-row table
    return lambda tbl: pa.table({col: [fn(tbl[col]).as_py()] for col in columns})


def test_row_group_order(snapshot):
    gt = GT(pd.DataFrame({"g": ["a", "b"], "x": [1, 2], "y": [3, 4]}), groupname_col="g")

    assert_rendered_body(snapshot, gt.row_group_order(["b", "a"]))


def test_with_groupname_col(frame_constructor: DataFrameConstructor):
    gt = GT(frame_constructor({"g": ["b", "a"], "x": [1, 2], "y": [3, 4]}))

    new_gt = gt.tab_stub(groupname_col="g")
    group_rows = new_gt._stub.group_rows

    assert list(grp.group_id for grp in group_rows) == ["b", "a"]
    assert [grp.indices for grp in group_rows] == [[0], [1]]


def test_with_groupname_col_undo_spanner_style():
    SPAN_COLS = ["g", "x"]
    STYLE_COLS = ["g", "y"]

    gt = (
        GT(pd.DataFrame({"g": ["b"], "x": [1], "y": [3]}))
        .tab_spanner("A", SPAN_COLS)
        .tab_style(style.fill("red"), loc.body(columns=STYLE_COLS))
    )

    assert gt._spanners[0].vars == SPAN_COLS
    assert len(gt._styles) == 2
    assert {style.colname for style in gt._styles} == set(STYLE_COLS)

    new_gt = gt.tab_stub(groupname_col="g")

    # grouping col dropped from spanner vars
    assert len(new_gt._spanners) == 1
    assert new_gt._spanners[0].vars == ["x"]

    # grouping col dropped from body styles
    assert len(new_gt._styles) == 1
    assert new_gt._styles[0].colname == "y"


def test_with_groupname_col_unset():
    gt = GT(
        pd.DataFrame({"g": ["b"], "row": ["one"], "x": [1], "y": [3]}),
        rowname_col="row",
        groupname_col="g",
    )

    assert gt._boxhead._get_row_group_column().var == "g"
    assert len(gt._stub.group_rows) == 1

    new_gt = gt.tab_stub(rowname_col="row")

    # check row unchanged ----
    assert new_gt._boxhead._get_stub_column().var == "row"
    assert new_gt._stub.rows[0].rowname == "one"

    # check group col removed ----
    assert new_gt._boxhead._get_row_group_column() is None
    assert len(new_gt._stub.group_rows) == 0


def test_with_rowname_col(frame_constructor: DataFrameConstructor):
    gt = GT(frame_constructor({"g": ["b", "a"], "x": [1, 2], "y": [3, 4]}))

    new_gt = gt.tab_stub(rowname_col="g")
    rows = new_gt._stub.rows

    assert [row.rowname for row in rows] == ["b", "a"]


def test_with_rowname_col_undo_spanner_style():
    SPAN_COLS = ["g", "x"]
    STYLE_COLS = ["g", "y"]

    gt = (
        GT(pd.DataFrame({"g": ["b"], "x": [1], "y": [3]}))
        .tab_spanner("A", SPAN_COLS)
        .tab_style(style.fill("red"), loc.body(columns=STYLE_COLS))
    )

    assert gt._spanners[0].vars == SPAN_COLS
    assert len(gt._styles) == 2
    assert {style.colname for style in gt._styles} == set(STYLE_COLS)

    new_gt = gt.tab_stub(rowname_col="g")

    # rowname col dropped from spanner vars
    assert len(new_gt._spanners) == 1
    assert new_gt._spanners[0].vars == ["x"]

    # rowname col *kept* in body styles
    assert len(new_gt._styles) == 2


def test_with_rowname_col_unset():
    gt = GT(
        pd.DataFrame({"g": ["b"], "row": ["one"], "x": [1], "y": [3]}),
        rowname_col="row",
        groupname_col="g",
    )

    assert gt._boxhead._get_stub_column().var == "row"
    assert gt._stub.rows[0].rowname == "one"

    new_gt = gt.tab_stub(groupname_col="g")

    # check row removed ----
    assert new_gt._boxhead._get_stub_column() is None
    assert new_gt._stub.rows[0].rowname is None

    # check group col unchanged ----
    assert new_gt._boxhead._get_row_group_column().var == "g"
    assert len(new_gt._stub.group_rows) == 1


def test_with_locale():
    gt = GT(pd.DataFrame({"x": [1]}), locale="es")

    assert gt._locale._locale == "es"

    assert gt.with_locale("de")._locale._locale == "de"


def test_with_locale_unset():
    gt = GT(pd.DataFrame({"x": [1]}), locale="es")

    assert gt._locale._locale == "es"

    assert gt.with_locale()._locale._locale is None


def test_with_id():
    gt = GT(pd.DataFrame({"x": [1]}), id="abc")

    assert gt._options.table_id.value == "abc"

    assert gt.with_id("zzz")._options.table_id.value == "zzz"


def test_with_id_unset():
    gt = GT(pd.DataFrame({"x": [1]}), id="abc")

    assert gt._options.table_id.value == "abc"

    assert gt.with_id()._options.table_id.value is None


def test_with_id_preserves_other_options():
    gt = GT(pd.DataFrame({"x": [1]})).tab_options(container_width="20px")

    assert gt._options.container_width.value == "20px"

    new_gt = gt.with_id("zzz")
    assert new_gt._options.table_id.value == "zzz"
    assert new_gt._options.container_width.value == "20px"


def test_grand_summary_rows_snap(snapshot, all_frame_constructors: list[DataFrameConstructor]):
    def render(constructor: DataFrameConstructor) -> str:
        df = constructor({"a": [1, 2, 3], "b": [4, 5, 6]})
        fns = by_backend(
            df,
            pandas={"Average": mean_expr, "Maximum": max_expr},
            polars={"Average": pl.all().mean(), "Maximum": pl.all().max()},
            pyarrow={
                "Average": pyarrow_summary(pc.mean, ["a", "b"]),
                "Maximum": pyarrow_summary(pc.max, ["a", "b"]),
            },
        )
        return render_only_body(GT(df).grand_summary_rows(fns=fns))

    assert_parity(snapshot, all_frame_constructors, render)


def test_grand_summary_rows_with_rowname_snap(snapshot):
    df = pd.DataFrame({"a": [1, 2], "b": [4, 5], "row": ["x", "y"]})

    res = GT(df, rowname_col="row").grand_summary_rows(fns={"Average": mean_expr})

    assert_rendered_body(snapshot, res)


def test_grand_summary_rows_with_group_as_col_snap(snapshot):
    df = pd.DataFrame({"a": [1, 2], "b": [4, 5], "group": ["x", "y"]})

    res = (
        GT(df, groupname_col="group")
        .grand_summary_rows(fns={"Average": mean_expr})
        .tab_options(row_group_as_column=True)
    )

    assert_rendered_body(snapshot, res)


def test_grand_summary_rows_with_rowname_and_groupname():
    df = pd.DataFrame({"a": [1, 2], "group": ["x", "x"], "row": ["row1", "row2"]})

    res = (
        GT(df, rowname_col="row", groupname_col="group")
        .grand_summary_rows(fns={"Average": mean_expr})
        .tab_options(row_group_as_column=True)
    )
    html = res.as_raw_html()

    assert 'rowspan="2" scope="rowgroup" id="x">x</th>' in html
    assert (
        '<th class="gt_row gt_left gt_stub gt_grand_summary_row gt_first_grand_summary_row_bottom" colspan="2" scope="row" id="grand-summary-Average">Average</th>'
        in html
    )


def test_grand_summary_rows_with_missing():
    df = pd.DataFrame({"a": [1, 2], "non_numeric": ["x", "y"]})

    res = GT(df).grand_summary_rows(
        fns={"Average": mean_expr},
        missing_text="missing_text",
    )
    html = res.as_raw_html()

    assert "missing_text" in html


def test_grand_summary_rows_bottom_and_top():
    df = pd.DataFrame({"a": [1, 2]})

    res = (
        GT(df)
        .grand_summary_rows(fns={"Top": min_expr}, side="top")
        .grand_summary_rows(fns={"Bottom": max_expr}, side="bottom")
    )

    html = render_only_body(res)

    assert (
        'gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">Bottom</th>'
        in html
    )
    assert (
        'gt_last_grand_summary_row_top gt_row gt_left gt_stub gt_grand_summary_row">Top</th>'
        in html
    )


def test_grand_summary_rows_overwritten_row_maintains_location():
    df = pd.DataFrame({"a": [1, 2], "row": ["x", "y"]})

    res = (
        GT(df)
        .grand_summary_rows(fns={"Overwritten": min_expr}, side="top")
        .grand_summary_rows(fns={"Overwritten": max_expr}, side="bottom")
    )
    html = render_only_body(res)

    assert '"gt_last_grand_summary_row_top' in html
    assert '"gt_first_grand_summary_row_bottom' not in html

    assert 'gt_grand_summary_row">1</td>' not in html
    assert 'gt_grand_summary_row">2</td>' in html


def test_grand_summary_rows_with_fmt(frame_constructor: DataFrameConstructor):
    df = frame_constructor({"a": [1, 3], "row": ["x", "y"]})
    average = by_backend(
        df, pandas=mean_expr, polars=pl.col("a").mean(), pyarrow=pyarrow_summary(pc.mean, ["a"])
    )

    res = GT(df).grand_summary_rows(fns={"Average": average}, fmt=vals.fmt_integer)
    html = render_only_body(res)

    assert 'gt_grand_summary_row">2</td>' in html
    assert 'gt_grand_summary_row">2.0</td>' not in html


def test_grand_summary_rows_raises_columns_not_implemented():
    df = pd.DataFrame({"a": [1, 2], "row": ["x", "y"]})

    with pytest.raises(NotImplementedError) as exc_info:
        GT(df).grand_summary_rows(fns={"Minimum": min_expr}, columns="b")

    assert (
        "Currently, grand_summary_rows() does not support column selection."
        in exc_info.value.args[0]
    )


# summary_rows tests ----


def test_summary_rows_snap(snapshot, all_frame_constructors: list[DataFrameConstructor]):
    def render(constructor: DataFrameConstructor) -> str:
        df = constructor({"group": ["A", "A", "B", "B"], "x": [1, 2, 3, 4], "y": [10, 20, 30, 40]})
        fns = by_backend(
            df,
            pandas={"Sum": lambda df: df.sum(numeric_only=True), "Average": mean_expr},
            polars={"Sum": pl.col("x", "y").sum(), "Average": pl.col("x", "y").mean()},
            pyarrow={
                "Sum": pyarrow_summary(pc.sum, ["x", "y"]),
                "Average": pyarrow_summary(pc.mean, ["x", "y"]),
            },
        )
        return render_only_body(GT(df, groupname_col="group").summary_rows(fns=fns))

    assert_parity(snapshot, all_frame_constructors, render)


def test_summary_rows_with_rowname_snap(snapshot):
    df = pd.DataFrame(
        {"group": ["A", "A", "B", "B"], "row": ["a1", "a2", "b1", "b2"], "x": [1, 2, 3, 4]}
    )

    res = GT(df, rowname_col="row", groupname_col="group").summary_rows(
        fns={"Sum": lambda df: df.sum(numeric_only=True)}
    )

    assert_rendered_body(snapshot, res)


def test_summary_rows_with_groups_param():
    df = pd.DataFrame(
        {
            "group": ["A", "A", "B", "B", "C", "C"],
            "x": [1, 2, 3, 4, 5, 6],
        }
    )

    res = GT(df, groupname_col="group").summary_rows(
        fns={"Sum": lambda df: df.sum(numeric_only=True)},
        groups=["A", "C"],
    )
    html = render_only_body(res)

    # Group A and C should have summary rows
    assert html.count("gt_summary_row") > 0
    # Should not have summary row values for group B (sum would be 7)
    assert "gt_first_summary_row" in html


def test_summary_rows_side_top():
    df = pd.DataFrame({"group": ["A", "A"], "x": [1, 2]})

    res = GT(df, groupname_col="group").summary_rows(
        fns={"Sum": lambda df: df.sum(numeric_only=True)},
        side="top",
    )
    html = render_only_body(res)

    assert "gt_summary_row" in html
    assert "gt_last_summary_row_top" in html


def test_summary_rows_with_fmt(frame_constructor: DataFrameConstructor):
    df = frame_constructor({"group": ["A", "A"], "x": [1, 3]})
    average = by_backend(
        df, pandas=mean_expr, polars=pl.col("x").mean(), pyarrow=pyarrow_summary(pc.mean, ["x"])
    )

    res = GT(df, groupname_col="group").summary_rows(
        fns={"Average": average},
        fmt=vals.fmt_integer,
    )
    html = render_only_body(res)

    assert 'gt_summary_row">2</td>' in html
    assert 'gt_summary_row">2.0</td>' not in html


def test_summary_rows_with_missing_text():
    df = pd.DataFrame({"group": ["A", "A"], "x": [1, 2], "non_numeric": ["a", "b"]})

    res = GT(df, groupname_col="group").summary_rows(
        fns={"Sum": lambda df: df.sum(numeric_only=True)},
        missing_text="N/A",
    )
    html = render_only_body(res)

    assert "N/A" in html


def test_summary_rows_raises_no_groups():
    df = pd.DataFrame({"x": [1, 2]})

    with pytest.raises(ValueError) as exc_info:
        GT(df).summary_rows(fns={"Sum": lambda df: df.sum(numeric_only=True)})

    assert "requires row groups" in exc_info.value.args[0]


def test_summary_rows_raises_columns_not_implemented():
    df = pd.DataFrame({"group": ["A", "A"], "x": [1, 2]})

    with pytest.raises(NotImplementedError) as exc_info:
        GT(df, groupname_col="group").summary_rows(
            fns={"Sum": lambda df: df.sum(numeric_only=True)},
            columns="x",
        )

    assert "does not support column selection" in exc_info.value.args[0]


def test_summary_rows_with_style():
    df = pd.DataFrame({"group": ["A", "A"], "x": [1, 2], "y": [3, 4]})

    res = (
        GT(df, groupname_col="group")
        .summary_rows(
            fns={"Sum": lambda df: df.sum(numeric_only=True)},
            fmt=vals.fmt_integer,
        )
        .tab_style(
            style=[style.text(color="red")],
            locations=loc.summary(),
        )
    )
    html = render_only_body(res)

    assert "color: red;" in html
    assert "gt_summary_row" in html


def test_summary_rows_with_stub_style():
    df = pd.DataFrame({"group": ["A", "A"], "row": ["r1", "r2"], "x": [1, 2]})

    res = (
        GT(df, rowname_col="row", groupname_col="group")
        .summary_rows(
            fns={"Sum": lambda df: df.sum(numeric_only=True)},
        )
        .tab_style(
            style=[style.text(weight="bold")],
            locations=loc.summary_stub(),
        )
    )
    html = render_only_body(res)

    assert "font-weight: bold;" in html
    assert "gt_summary_row" in html


def test_summary_rows_loc_groups_as_list():
    """loc.summary(groups=[...]) with a list of group names hits the else branch."""
    df = pd.DataFrame(
        {"group": ["A", "A", "B", "B"], "row": ["r1", "r2", "r3", "r4"], "x": [1, 2, 3, 4]}
    )
    res = (
        GT(df, rowname_col="row", groupname_col="group")
        .summary_rows(
            fns={"Sum": lambda df: df.sum(numeric_only=True)},
        )
        .tab_style(
            style=[style.text(color="blue")],
            locations=loc.summary(groups=["A", "B"]),
        )
    )
    html = render_only_body(res)
    assert "color: blue;" in html


def test_summary_stub_loc_groups_as_list():
    """loc.summary_stub(groups=[...]) with a list of group names hits the else branch."""
    df = pd.DataFrame(
        {"group": ["A", "A", "B", "B"], "row": ["r1", "r2", "r3", "r4"], "x": [1, 2, 3, 4]}
    )
    res = (
        GT(df, rowname_col="row", groupname_col="group")
        .summary_rows(
            fns={"Sum": lambda df: df.sum(numeric_only=True)},
        )
        .tab_style(
            style=[style.text(weight="bold")],
            locations=loc.summary_stub(groups=["A", "B"]),
        )
    )
    html = render_only_body(res)
    assert "font-weight: bold;" in html
