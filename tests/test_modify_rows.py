import pandas as pd

from great_tables import GT, loc, style
from great_tables._utils_render_html import create_body_component_h


def assert_rendered_body(snapshot, gt):
    built = gt._build_data("html")
    body = create_body_component_h(built)

    assert snapshot == body


def test_row_group_order(snapshot):
    gt = GT(pd.DataFrame({"g": ["a", "b"], "x": [1, 2], "y": [3, 4]}), groupname_col="g")

    assert_rendered_body(snapshot, gt.row_group_order(["b", "a"]))


def test_with_groupname_col():
    gt = GT(pd.DataFrame({"g": ["b", "a"], "x": [1, 2], "y": [3, 4]}))

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


def test_with_rowname_col():
    gt = GT(pd.DataFrame({"g": ["b", "a"], "x": [1, 2], "y": [3, 4]}))

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
