import pandas as pd

from gt._gt_data import Stub, RowInfo
from gt._gt_data import RowGroups


def test_stub_construct_manual():
    stub = Stub([RowInfo(0), RowInfo(1)])
    assert stub[0] == RowInfo(0)


def test_stub_construct_df():
    stub = Stub(pd.DataFrame({"x": [8, 9]}))

    assert len(stub) == 2
    assert stub[0] == RowInfo(0)
    assert stub[1] == RowInfo(1)


def test_row_groups_construct_manual():
    groups = RowGroups(["a", "b"])

    assert len(groups) == 2
    assert groups[0] == "a"
    assert groups[1] == "b"

    assert isinstance(groups[:], RowGroups)
