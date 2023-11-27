from great_tables._gt_data import RowGroups, Stub, RowInfo
from great_tables.utils_render_common import get_row_reorder_df
import pytest


def test_get_row_reorder_df_simple():
    groups = ["b", "a"]
    stub = Stub([RowInfo(0, "a"), RowInfo(1, "b"), RowInfo(2, "a")])

    start_end = get_row_reorder_df(groups, stub)

    assert start_end == [(0, 1), (1, 0), (2, 2)]


def test_get_row_reorder_df_no_groups():
    groups = []
    stub = Stub([RowInfo(0, "a"), RowInfo(1, "b")])

    with pytest.raises(ValueError):
        get_row_reorder_df(groups, stub)
