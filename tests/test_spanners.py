import pandas as pd
import polars as pl
import polars.selectors as cs
import pytest
from great_tables import GT
from great_tables._gt_data import Boxhead, ColInfo, ColInfoTypeEnum, SpannerInfo, Spanners
from great_tables._spanners import (
    cols_hide,
    cols_move,
    cols_move_to_end,
    cols_move_to_start,
    empty_spanner_matrix,
    spanners_print_matrix,
    tab_spanner,
)

PandasDataFrame = pd.DataFrame
PolarsDataFrame = pl.DataFrame


@pytest.fixture
def spanners() -> Spanners:
    return Spanners(
        [
            SpannerInfo(spanner_id="a", spanner_level=0, vars=["col1"], built="A"),
            SpannerInfo(spanner_id="b", spanner_level=1, vars=["col2"], built="B"),
        ]
    )


@pytest.fixture
def boxhead() -> Boxhead:
    return Boxhead(
        [
            ColInfo(var="col1"),
            ColInfo(var="col2"),
            ColInfo(var="col3"),
            ColInfo(var="col4", type=ColInfoTypeEnum.hidden),
        ]
    )


def test_spanners_next_level_above_first(spanners: Spanners):
    assert spanners.next_level(["col1"]) == 1


def test_spanners_next_level_above_second(spanners: Spanners):
    assert spanners.next_level(["col2"]) == 2


def test_spanners_next_level_unique(spanners: Spanners):
    assert spanners.next_level(["col3"]) == 0


def test_spanners_print_matrix(spanners: Spanners, boxhead: Boxhead):
    mat, vars = spanners_print_matrix(spanners, boxhead)
    assert vars == ["col1", "col2", "col3"]
    assert mat == [
        {"col1": None, "col2": "B", "col3": None},
        {"col1": "A", "col2": None, "col3": None},
        {"col1": "col1", "col2": "col2", "col3": "col3"},
    ]


def test_spanners_print_matrix_arg_omit_columns_row(spanners: Spanners, boxhead: Boxhead):
    mat, vars = spanners_print_matrix(spanners, boxhead, omit_columns_row=True)
    assert vars == ["col1", "col2", "col3"]
    assert mat == [
        {"col1": None, "col2": "B", "col3": None},
        {"col1": "A", "col2": None, "col3": None},
    ]


def test_spanners_print_matrix_arg_include_hidden(spanners: Spanners, boxhead: Boxhead):
    mat, vars = spanners_print_matrix(spanners, boxhead, include_hidden=True)
    assert vars == ["col1", "col2", "col3", "col4"]
    assert mat == [
        {"col1": None, "col2": "B", "col3": None, "col4": None},
        {"col1": "A", "col2": None, "col3": None, "col4": None},
        {"col1": "col1", "col2": "col2", "col3": "col3", "col4": "col4"},
    ]


def test_spanners_print_matrix_exclude_stub():
    """spanners_print_matrix omits a selected column if it's in the stub."""
    info = SpannerInfo(spanner_id="a", spanner_level=0, vars=["x", "y"], built="A")
    spanners = Spanners([info])
    boxh = Boxhead([ColInfo(var="x"), ColInfo(var="y", type=ColInfoTypeEnum.stub)])

    mat, vars = spanners_print_matrix(spanners, boxh, omit_columns_row=True)
    assert vars == ["x"]
    assert mat == [{"x": "A"}]


def test_empty_spanner_matrix():
    mat, vars = empty_spanner_matrix(["a", "b"], omit_columns_row=False)

    assert vars == ["a", "b"]
    assert mat == [{"a": "a", "b": "b"}]


def test_empty_spanner_matrix_arg_omit_columns_row():
    mat, vars = empty_spanner_matrix(["a", "b"], omit_columns_row=True)

    assert vars == ["a", "b"]
    assert mat == []


def test_tab_spanners_with_columns():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
    src_gt = GT(df)

    dst_span = SpannerInfo("a_spanner", 0, "a_spanner", vars=["b", "a"])

    new_gt = tab_spanner(src_gt, "a_spanner", columns=["b", "a"], gather=False)
    assert len(new_gt._spanners)
    assert new_gt._spanners[0] == dst_span


def test_tab_spanners_with_spanner_ids():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
    src_gt = GT(df)

    # we'll be testing for this second spanner added
    dst_span = SpannerInfo("b_spanner", 1, "b_spanner", vars=["c", "b", "a"])

    gt_with_span = tab_spanner(src_gt, "a_spanner", columns=["b", "a"], gather=False)

    new_gt = tab_spanner(gt_with_span, "b_spanner", spanners="a_spanner", columns=["c"])

    assert len(new_gt._spanners) == 2
    assert new_gt._spanners[1] == dst_span


def test_tab_spanners_overlap():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
    src_gt = GT(df)

    # we'll be testing for this second spanner added
    dst_span = SpannerInfo("b_spanner", 0, "b_spanner", vars=["b"])

    new_gt = src_gt.tab_spanner("a_spanner", columns=["a"], gather=False).tab_spanner(
        "b_spanner", columns=["b"]
    )

    assert len(new_gt._spanners) == 2
    assert new_gt._spanners[1] == dst_span


def test_tab_spanners_with_gather():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
    src_gt = GT(df)

    new_gt = tab_spanner(src_gt, "a_spanner", columns=["a", "c"], gather=True)

    assert len(new_gt._spanners) == 1
    assert [col.var for col in new_gt._boxhead] == ["a", "c", "b"]


def test_cols_width_partial_set():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
    gt_tbl = GT(df).cols_width({"a": "10px"})

    assert gt_tbl._boxhead[0].column_width == "10px"
    assert gt_tbl._boxhead[1].column_width == None
    assert gt_tbl._boxhead[2].column_width == None


def test_cols_width_fully_set():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
    gt_tbl = GT(df).cols_width({"a": "10px", "b": "20px", "c": "30px"})

    assert gt_tbl._boxhead[0].column_width == "10px"
    assert gt_tbl._boxhead[1].column_width == "20px"
    assert gt_tbl._boxhead[2].column_width == "30px"


def test_cols_width_partial_set_pct():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
    gt_tbl = GT(df).cols_width({"a": "20%"})

    assert gt_tbl._boxhead[0].column_width == "20%"
    assert gt_tbl._boxhead[1].column_width == None
    assert gt_tbl._boxhead[2].column_width == None


def test_cols_width_fully_set_pct():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
    gt_tbl = GT(df).cols_width({"a": "20%", "b": "20%", "c": "60%"})

    assert gt_tbl._boxhead[0].column_width == "20%"
    assert gt_tbl._boxhead[1].column_width == "20%"
    assert gt_tbl._boxhead[2].column_width == "60%"


def test_cols_width_fully_set_pct_2():
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
    gt_tbl = GT(df).cols_width({"a": "10%", "b": "10%", "c": "40%"})

    assert gt_tbl._boxhead[0].column_width == "10%"
    assert gt_tbl._boxhead[1].column_width == "10%"
    assert gt_tbl._boxhead[2].column_width == "40%"


@pytest.mark.parametrize(
    "DF, columns",
    [
        (PandasDataFrame, "a"),
        (PolarsDataFrame, cs.starts_with("a")),
        (PolarsDataFrame, pl.col("a")),
    ],
)
def test_cols_move_single_col(DF, columns):
    df = DF({"a": [1, 2], "b": [3, 4], "c": [5, 6], "d": [7, 8]})
    src_gt = GT(df)
    new_gt = cols_move(src_gt, columns=columns, after="b")
    assert [col.var for col in new_gt._boxhead] == ["b", "a", "c", "d"]


@pytest.mark.parametrize(
    "DF, columns",
    [
        (PandasDataFrame, ["a", "d"]),
        (PolarsDataFrame, cs.starts_with("a") | cs.ends_with("d")),
        (PolarsDataFrame, pl.col("a", "d")),
    ],
)
def test_cols_move_multi_cols(DF, columns):
    df = DF({"a": [1, 2], "b": [3, 4], "c": [5, 6], "d": [7, 8]})
    src_gt = GT(df)
    new_gt = cols_move(src_gt, columns=columns, after="b")
    assert [col.var for col in new_gt._boxhead] == ["b", "a", "d", "c"]


@pytest.mark.parametrize(
    "DF, columns",
    [
        (PandasDataFrame, "c"),
        (PolarsDataFrame, cs.starts_with("c")),
        (PolarsDataFrame, pl.col("c")),
    ],
)
def test_cols_move_to_start_single_col(DF, columns):
    df = DF({"a": [1, 2], "b": [3, 4], "c": [5, 6], "d": [7, 8]})
    src_gt = GT(df)
    new_gt = cols_move_to_start(src_gt, columns=columns)
    assert [col.var for col in new_gt._boxhead] == ["c", "a", "b", "d"]


@pytest.mark.parametrize(
    "DF, columns",
    [
        (PandasDataFrame, ["c", "d"]),
        (PolarsDataFrame, cs.starts_with("c") | cs.ends_with("d")),
        (PolarsDataFrame, pl.col("c", "d")),
    ],
)
def test_cols_move_to_start_multi_cols(DF, columns):
    df = DF({"a": [1, 2], "b": [3, 4], "c": [5, 6], "d": [7, 8]})
    src_gt = GT(df)
    new_gt = cols_move_to_start(src_gt, columns=columns)
    assert [col.var for col in new_gt._boxhead] == ["c", "d", "a", "b"]


@pytest.mark.parametrize(
    "DF, columns",
    [
        (PandasDataFrame, "c"),
        (PolarsDataFrame, cs.starts_with("c")),
        (PolarsDataFrame, pl.col("c")),
    ],
)
def test_cols_move_to_end_single_col(DF, columns):
    df = DF({"a": [1, 2], "b": [3, 4], "c": [5, 6], "d": [7, 8]})
    src_gt = GT(df)
    new_gt = cols_move_to_end(src_gt, columns=columns)
    assert [col.var for col in new_gt._boxhead] == ["a", "b", "d", "c"]


@pytest.mark.parametrize(
    "DF, columns",
    [
        (PandasDataFrame, ["a", "c"]),
        (PolarsDataFrame, cs.starts_with("a") | cs.ends_with("c")),
        (PolarsDataFrame, pl.col("a", "c")),
    ],
)
def test_cols_move_to_end_multi_cols(DF, columns):
    df = DF({"a": [1, 2], "b": [3, 4], "c": [5, 6], "d": [7, 8]})
    src_gt = GT(df)
    new_gt = cols_move_to_end(src_gt, columns=columns)
    assert [col.var for col in new_gt._boxhead] == ["b", "d", "a", "c"]


@pytest.mark.parametrize(
    "DF, columns",
    [
        (PandasDataFrame, "c"),
        (PolarsDataFrame, cs.starts_with("c")),
        (PolarsDataFrame, pl.col("c")),
    ],
)
def test_cols_hide_single_col(DF, columns):
    df = DF({"a": [1, 2], "b": [3, 4], "c": [5, 6], "d": [7, 8]})
    src_gt = GT(df)
    new_gt = cols_hide(src_gt, columns=columns)
    assert [col.var for col in new_gt._boxhead if col.visible] == ["a", "b", "d"]


@pytest.mark.parametrize(
    "DF, columns",
    [
        (PandasDataFrame, ["a", "d"]),
        (PolarsDataFrame, cs.starts_with("a") | cs.ends_with("d")),
        (PolarsDataFrame, pl.col("a", "d")),
    ],
)
def test_cols_hide_multi_cols(DF, columns):
    df = DF({"a": [1, 2], "b": [3, 4], "c": [5, 6], "d": [7, 8]})
    src_gt = GT(df)
    new_gt = cols_hide(src_gt, columns=columns)
    assert [col.var for col in new_gt._boxhead if col.visible] == ["b", "c"]


@pytest.mark.parametrize(
    "columns",
    [
        pl.col("c").add(100),
        pl.col("c").cast(pl.Utf8).str.to_lowercase(),
        pl.col("c").add(pl.col("d")),
    ],
)
def test_weird_pl_expr_single_col(columns):
    df = pl.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6], "d": [7, 8]})
    src_gt = GT(df)
    new_gt = cols_hide(src_gt, columns=columns)
    assert [col.var for col in new_gt._boxhead if col.visible] == ["a", "b", "d"]


@pytest.mark.parametrize(
    "columns",
    [
        pl.col("a", "d").add(100),
        pl.col("a", "d").cast(pl.Utf8).str.to_lowercase(),
        pl.col("a", "d").add(pl.col("b")),
    ],
)
def test_weird_pl_expr_multi_cols(columns):
    df = pl.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6], "d": [7, 8]})
    src_gt = GT(df)
    new_gt = cols_hide(src_gt, columns=columns)
    assert [col.var for col in new_gt._boxhead if col.visible] == ["b", "c"]
