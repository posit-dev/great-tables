import pandas as pd
import pytest

from great_tables._locations import (
    LocColumnSpanners,
    LocBody,
    CellPos,
    resolve,
    resolve_vector_i,
    resolve_cols_i,
    resolve_rows_i,
)
from great_tables._gt_data import Spanners, SpannerInfo
from great_tables import GT


def test_resolve_vector_i():
    assert resolve_vector_i(["x", "a"], ["a", "b", "x"], "") == [0, 2]


def test_resolve_cols_i_gt_data():
    gt = GT(pd.DataFrame(columns=["a", "b", "x"]))
    assert resolve_cols_i(["x", "a"], gt) == [("x", 2), ("a", 0)]


def test_resolve_cols_i_strings():
    df = pd.DataFrame(columns=["a", "b", "x"])
    assert resolve_cols_i(["x", "a"], df) == [("x", 2), ("a", 0)]


def test_resolve_cols_i_ints():
    df = pd.DataFrame(columns=["a", "b", "x"])
    assert resolve_cols_i([-1, 0], df) == [("x", 2), ("a", 0)]


def test_resolve_rows_i_gt_data():
    gt = GT(pd.DataFrame({"x": ["a", "b", "c"]}), rowname_col="x")
    assert resolve_rows_i(["b", "a"], gt) == [("a", 0), ("b", 1)]


def test_resolve_rows_i_strings():
    assert resolve_rows_i(["x", "a"], ["a", "x", "a", "b"]) == [("a", 0), ("x", 1), ("a", 2)]


def test_resolve_rows_i_ints():
    assert resolve_rows_i([0, -1], ["a", "x", "a", "b"]) == [("a", 0), ("b", 3)]


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
