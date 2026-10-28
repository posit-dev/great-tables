import re

import pandas as pd
import polars as pl
import pytest
from great_tables import GT
from great_tables._boxhead import _align_to_char
from great_tables.gt import _get_column_labels
from great_tables._helpers import UnitStr
from tests.utils import DataFrameConstructor, assert_rendered_columns


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


def test_cols_label_invalid_type_raises():
    import polars as pl

    with pytest.raises(ValueError, match="Column labels must be strings or BaseText objects"):
        GT(pl.DataFrame({"x": [1]})).cols_label(x=42)


def test_cols_align_single_col_raises():
    df = pd.DataFrame({"x": [1], "y": [2]})
    with pytest.raises(AssertionError):
        GT(df).cols_align(columns="nope")


def test_cols_align_list_with_invalid_col_raises():
    # A single invalid column name already raised; a list containing one should too
    # (previously the invalid name was silently dropped instead of raising).
    df = pd.DataFrame({"x": [1], "y": [2]})
    with pytest.raises(AssertionError):
        GT(df).cols_align(columns=["x", "nope"])


def test_cols_label_with_list_with_invalid_col_raises():
    df = pd.DataFrame({"x": [1], "y": [2]})
    with pytest.raises(AssertionError):
        GT(df).cols_label_with(columns=["x", "nope"], fn=str.upper)


@pytest.mark.parametrize(
    "values, expected",
    [
        # inputs and outputs from the snapshot tests of cols_align_decimal() in the R gt package
        (
            [
                "1.2",
                "\u221233.52",
                "9,023.2",
                "\u2212283.527",
                "NA",
                "0.401",
                "\u2212123.1",
                "NA",
                "41",
            ],
            [
                "\u2007\u2007\u2007\u20071.2\u2007\u2007",
                "\u2007\u2007\u221233.52\u2007",
                "9,023.2\u2007\u2007",
                "\u2007\u2212283.527",
                "NA",
                "\u2007\u2007\u2007\u20070.401",
                "\u2007\u2212123.1\u2007\u2007",
                "NA",
                "\u2007\u2007\u200741 \u2007\u2007\u2007",
            ],
        ),
        (
            [
                "1.2",
                "\u221233.52",
                "9,023.2",
                "\u2212283.527",
                "NA",
                "0.401",
                "\u2212123.1",
                "NA",
                "41.",
            ],
            [
                "\u2007\u2007\u2007\u20071.2\u2007\u2007",
                "\u2007\u2007\u221233.52\u2007",
                "9,023.2\u2007\u2007",
                "\u2007\u2212283.527",
                "NA",
                "\u2007\u2007\u2007\u20070.401",
                "\u2007\u2212123.1\u2007\u2007",
                "NA",
                "\u2007\u2007\u200741.\u2007\u2007\u2007",
            ],
        ),
        (
            [
                "1.2%",
                "\u221233.52%",
                "9,023.2%",
                "\u2212283.527%",
                "NA",
                "0.401%",
                "\u2212123.1%",
                "NA",
                "41%",
            ],
            [
                "\u2007\u2007\u2007\u20071.2%\u2007\u2007",
                "\u2007\u2007\u221233.52%\u2007",
                "9,023.2%\u2007\u2007",
                "\u2007\u2212283.527%",
                "NA",
                "\u2007\u2007\u2007\u20070.401%",
                "\u2007\u2212123.1%\u2007\u2007",
                "NA",
                "\u2007\u200741 %\u2007\u2007\u2007",
            ],
        ),
        (
            [
                "1.2 ppm",
                "\u221233.52 ppm",
                "9,023.2 ppm",
                "\u2212283.527 ppm",
                "NA",
                "0.401 ppm",
                "\u2212123.1 ppm",
                "NA",
                "41 ppm",
            ],
            [
                "\u2007\u2007\u2007\u2007\u20071.2 ppm\u2007\u2007",
                "\u2007\u2007\u2007\u221233.52 ppm\u2007",
                "\u20079,023.2 ppm\u2007\u2007",
                "\u2007\u2007\u2212283.527 ppm",
                "NA",
                "\u2007\u2007\u2007\u2007\u20070.401 ppm",
                "\u2007\u2007\u2212123.1 ppm\u2007\u2007",
                "NA",
                "41  ppm\u2007\u2007\u2007",
            ],
        ),
        (
            ["1.2", "(33.52)", "9,023.2", "(283.527)", "NA", "0.401", "(123.1)", "NA", "41."],
            [
                "\u2007\u2007\u2007\u20071.2\u2007\u2007\u2007",
                "\u2007\u2007(33.52)\u2007\xa0",
                "9,023.2\u2007\u2007\u2007",
                "\u2007(283.527)\xa0",
                "NA",
                "\u2007\u2007\u2007\u20070.401\u2007",
                "\u2007(123.1)\u2007\u2007\xa0",
                "NA",
                "\u2007\u2007\u200741.\u2007\u2007\u2007\u2007",
            ],
        ),
        (
            ["$1", "($34)", "$9,023", "($284)", "NA", "$0", "($123)", "NA", "$41"],
            [
                "\u2007\u2007\u2007\u2007$1\xa0",
                "\u2007($34)",
                "$9,023\xa0",
                "($284)",
                "NA",
                "\u2007\u2007\u2007\u2007$0\xa0",
                "($123)",
                "NA",
                "\u2007\u2007\u2007$41\xa0",
            ],
        ),
    ],
)
def test_align_to_char_matches_r_gt(values: list[str], expected: list[str]):
    assert _align_to_char(values) == expected


def test_align_to_char_without_alignable_values():
    values = ["NA", "\u2014", "n/a"]
    assert _align_to_char(values) == values


def _body_cells(html: str, align: str = "right") -> list[str]:
    return re.findall(rf'<td(?: headers="[^"]*")? class="gt_row gt_{align}">(.*?)</td>', html)


def test_cols_align_decimal():
    df = pl.DataFrame({"num": [1.5, 22.25, 3.0]})
    html = (
        GT(df)
        .fmt_number(columns="num", decimals=2, drop_trailing_zeros=True)
        .cols_align_decimal()
        .as_raw_html()
    )

    assert _body_cells(html) == ["\u20071.5\u2007", "22.25", "\u20073 \u2007\u2007"]


def test_cols_align_decimal_skips_non_numeric_columns():
    df = pl.DataFrame({"char": ["a.b", "c"], "num": [1.5, 22.25]})
    gt = GT(df).cols_align_decimal()

    assert [col.column_align for col in gt._boxhead] == ["left", "right"]
    assert _body_cells(gt.as_raw_html(), align="left") == ["a.b", "c"]


def test_cols_align_decimal_no_numeric_columns():
    gt = GT(pl.DataFrame({"char": ["a.b", "c"]}))
    res = gt.cols_align_decimal()

    assert [col.column_align for col in res._boxhead] == ["left"]
    assert res._transforms == gt._transforms


def test_cols_align_decimal_skips_list_columns(frame_constructor: DataFrameConstructor):
    df = frame_constructor({"items": [[1, 2], [3], [], None], "num": [1.5, 22.25, 3.0, None]})
    gt = GT(df)
    res = gt.cols_align_decimal()

    # The list column keeps its default alignment (it differs by backend) and isn't padded
    before = [col.column_align for col in gt._boxhead]
    assert [col.column_align for col in res._boxhead] == [before[0], "right"]
    assert [t.loc.columns for t in res._transforms] == [["num"]]


def test_cols_align_decimal_locale():
    df = pl.DataFrame({"num": [1.5, 22.25, 3.0]})
    html = (
        GT(df, locale="de")
        .fmt_number(columns="num", decimals=2, drop_trailing_zeros=True)
        .cols_align_decimal()
        .as_raw_html()
    )

    assert _body_cells(html) == ["\u20071,5\u2007", "22,25", "\u20073 \u2007\u2007"]


def test_cols_align_decimal_missing_values():
    df = pl.DataFrame({"num": [1.5, None, 22.25]})
    formatted = GT(df).fmt_number(columns="num", decimals=2, drop_trailing_zeros=True)

    aligned = _body_cells(formatted.cols_align_decimal().as_raw_html())
    unaligned = _body_cells(formatted.as_raw_html())

    assert aligned[1] == unaligned[1]
    assert [aligned[0], aligned[2]] == ["\u20071.5\u2007", "22.25"]
