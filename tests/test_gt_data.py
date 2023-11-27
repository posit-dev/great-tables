import pandas as pd

from great_tables._gt_data import Stub, RowInfo, Boxhead, ColInfo
from great_tables._gt_data import RowGroups


def test_stub_construct_manual():
    stub = Stub([RowInfo(0), RowInfo(1)])
    assert stub[0] == RowInfo(0)


def test_stub_construct_df():
    stub = Stub(pd.DataFrame({"x": [8, 9]}))

    assert len(stub) == 2
    assert stub[0] == RowInfo(0)
    assert stub[1] == RowInfo(1)


def test_stub_construct_df_rowname():
    # TODO: remove groupname_col from here
    stub = Stub(pd.DataFrame({"x": [8, 9], "y": [1, 2]}), rowname_col="x", groupname_col=None)


def test_boxhead_reorder():
    boxh = Boxhead([ColInfo("a"), ColInfo("b"), ColInfo("c")])
    new_boxh = boxh.reorder(["b", "a", "c"])

    assert new_boxh == Boxhead([ColInfo("b"), ColInfo("a"), ColInfo("c")])
