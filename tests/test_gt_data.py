import pandas as pd
from great_tables._gt_data import Boxhead, ColInfo, RowInfo, Stub


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
