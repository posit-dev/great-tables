import pandas as pd
import pytest
from great_tables import GT
from great_tables.gt import _get_column_labels
from great_tables._helpers import UnitStr
from tests.test_utils_render_html import assert_rendered_columns


def test_cols_label():
    df = pd.DataFrame({"x": [1.234, 2.345], "y": [3.456, 4.567]})
    gt = GT(df).cols_label(x="ex", y="why")

    x = _get_column_labels(gt=gt, context="html")
    y = ["ex", "why"]
    assert x == y


def test_cols_label_mix_cases_kwargs():
    df = pd.DataFrame({"x": [1.234, 2.345], "y": [3.456, 4.567], "z": [5.678, 6.789]})
    gt = GT(df).cols_label({"x": "ex"}, **{"y": "why"}, z="Zee")

    x = _get_column_labels(gt=gt, context="html")
    y = ["ex", "why", "Zee"]
    assert x == y


def test_cols_label_units_text():
    df = pd.DataFrame({"x": [1.234, 2.345], "y": [3.456, 4.567], "z": [5.678, 6.789]})
    gt = GT(df).cols_label(x="Area ({{m^2}})", y="Density ({{kg / m^3}})", z="Zee")

    x = _get_column_labels(gt=gt, context="text")
    assert isinstance(x[0], UnitStr)
    assert isinstance(x[1], UnitStr)
    assert x[2] == "Zee"


def test_cols_label_rotate(snapshot: str):
    df = pd.DataFrame({"x": [1.234, 2.345], "y": [3.456, 4.567], "z": [5.678, 6.789]})
    gt_tbl = GT(df, id="test").cols_label_rotate(columns=["x", "y"])
    assert_rendered_columns(snapshot, gt_tbl)


def test_cols_label_rotate_align_fails():
    with pytest.raises(ValueError) as exc_info:
        df = pd.DataFrame({"x": [], "y": []})
        GT(df).cols_label_rotate(align="invalid")  # noqa

    assert "Align must be one of" in exc_info.value.args[0]


def test_cols_label_rotate_dir_fails():
    with pytest.raises(ValueError) as exc_info:
        df = pd.DataFrame({"x": [], "y": []})
        GT(df).cols_label_rotate(dir="invalid")  # noqa

    assert "Dir must be one of" in exc_info.value.args[0]


def test_cols_label_rotate_align_default():
    df = pd.DataFrame({"x": [], "y": []})
    gt1 = GT(df).cols_label_rotate(columns=["x"], dir="sideways-rl")
    gt2 = GT(df).cols_label_rotate(columns=["y"], dir="sideways-lr")

    assert "text-align: right;" in gt1._styles[0].styles[0].rule
    assert "text-align: left;" in gt2._styles[0].styles[0].rule


def test_final_columns_stub_move_to_beginning():
    df = pd.DataFrame({"w": [1], "x": [1], "y": [2], "z": [3]})
    gt = GT(df, rowname_col="y")

    options = gt._options
    final_columns = gt._boxhead.final_columns(options=options)
    all_columns = [col.var for col in final_columns]

    assert all_columns == ["y", "w", "x", "z"]


def test_final_columns_hidden_columns_removed():
    df = pd.DataFrame({"w": [1], "x": [1], "y": [2], "z": [3]})
    gt = GT(df).cols_hide(columns=["w", "y"])

    options = gt._options
    final_columns = gt._boxhead.final_columns(options=options)
    all_columns = [col.var for col in final_columns]

    assert all_columns == ["x", "z"]


def test_final_columns_row_and_group_cols_handled():
    df = pd.DataFrame({"w": [1], "x": [1], "y": [2], "z": [3]})

    gt_1 = GT(df, rowname_col="y", groupname_col="x").tab_options(row_group_as_column=True)

    options = gt_1._options
    final_columns = gt_1._boxhead.final_columns(options=options)
    all_columns = [col.var for col in final_columns]

    assert all_columns == ["x", "y", "w", "z"]

    gt_2 = GT(df, rowname_col="y", groupname_col="x").tab_options(row_group_as_column=False)

    options = gt_2._options
    final_columns = gt_2._boxhead.final_columns(options=options)
    all_columns = [col.var for col in final_columns]

    assert all_columns == ["y", "w", "z"]


def test_final_columns_hidden_and_row_group_cols_handled():
    df = pd.DataFrame({"w": [1], "x": [1], "y": [2], "z": [3]})

    gt_1 = (
        GT(df, rowname_col="y", groupname_col="x")
        .tab_options(row_group_as_column=True)
        .cols_hide(columns=["w"])
    )

    options = gt_1._options
    final_columns = gt_1._boxhead.final_columns(options=options)
    all_columns = [col.var for col in final_columns]

    assert all_columns == ["x", "y", "z"]

    gt_2 = (
        GT(df, rowname_col="y", groupname_col="x")
        .tab_options(row_group_as_column=False)
        .cols_hide(columns=["w"])
    )

    options = gt_2._options
    final_columns = gt_2._boxhead.final_columns(options=options)
    all_columns = [col.var for col in final_columns]

    assert all_columns == ["y", "z"]
