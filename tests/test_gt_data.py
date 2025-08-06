import pandas as pd
import pytest
from great_tables import GT
from great_tables._gt_data import Boxhead, ColInfo, RowInfo, Stub, CellMerges, MergeError


def test_stub_construct_df():
    stub = Stub.from_data(pd.DataFrame({"x": [8, 9]}))

    assert len(stub) == 2
    assert stub[0] == RowInfo(0)
    assert stub[1] == RowInfo(1)


def test_stub_construct_manual():
    stub = Stub.from_data(pd.DataFrame({"x": [8, 9]}))

    stub2 = Stub(stub.rows, stub.group_rows)
    assert stub2[0] == RowInfo(0)


def test_stub_construct_df_rowname():
    # TODO: remove groupname_col from here
    stub = Stub.from_data(
        pd.DataFrame({"x": [8, 9], "y": [1, 2]}), rowname_col="x", groupname_col=None
    )


def test_stub_order_groups():
    stub = Stub.from_data(pd.DataFrame({"g": ["b", "a", "b", "c"]}), groupname_col="g")
    assert stub.group_ids == ["b", "a", "c"]

    stub2 = stub.order_groups(["c", "a", "b"])
    assert stub2.group_ids == ["c", "a", "b"]

    indice_labels = [(ii, info.defaulted_label()) for ii, info in stub2.group_indices_map()]
    assert indice_labels == [(3, "c"), (1, "a"), (0, "b"), (2, "b")]


def test_boxhead_reorder():
    boxh = Boxhead([ColInfo("a"), ColInfo("b"), ColInfo("c")])
    new_boxh = boxh.reorder(["b", "a", "c"])

    assert new_boxh == Boxhead([ColInfo("b"), ColInfo("a"), ColInfo("c")])


def test_google_font_imports_is_set():
    gt_table = GT(pd.DataFrame())
    from great_tables._helpers import GoogleFontImports

    assert isinstance(gt_table._google_font_imports, GoogleFontImports)


def test_cell_merges_from_data_frame():
    data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
    # Default state where all cells are normal (value `1`)
    merges = CellMerges(
        rowspans=[[1, 1, 1], [1, 1, 1], [1, 1, 1]], colspans=[[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    )
    new_merges = merges.from_data_frame(data)

    assert new_merges.rowspans == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert new_merges.colspans == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]


def test_cell_merges_assign_rowspan():
    # 2-cell rowspan: top-left (0,0) merges with left (1,0)
    merges = CellMerges(
        rowspans=[[0, 1, 1], [1, 1, 1], [1, 1, 1]], colspans=[[0, 1, 1], [1, 1, 1], [1, 1, 1]]
    )
    new_merges = merges.assign_rowspan(0, 0, 2)

    assert new_merges.rowspans[0][0] == 2
    assert new_merges.rowspans[1][0] == 0


def test_cell_merges_assign_colspan():
    # 2-cell colspan: top-left (0,0) merges with top (0,1)
    merges = CellMerges(
        rowspans=[[0, 1, 1], [1, 1, 1], [1, 1, 1]], colspans=[[0, 1, 1], [1, 1, 1], [1, 1, 1]]
    )
    new_merges = merges.assign_colspan(0, 0, 2)

    assert new_merges.colspans[0][0] == 2
    assert new_merges.colspans[0][1] == 0


def test_cell_merges_validate_merge_cell_error_rowspan_not_zero():
    # Merging cell is already being merged on from the left (cell_rowspans[0] != 0) raises an error
    merges = CellMerges(
        rowspans=[[1, 1, 1], [1, 1, 1], [1, 1, 1]], colspans=[[0, 1, 1], [1, 1, 1], [1, 1, 1]]
    )

    with pytest.raises(MergeError, match="Merging cell is already being merged on from the left"):
        merges.validate_merge_cell(0, 0, 2)
