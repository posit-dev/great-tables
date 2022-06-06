from gt import *
import pandas as pd


def test_gt_object():
    data = [{"a": 5, "b": 15}, {"a": 15, "b": 2000}]
    pd_data = pd.DataFrame(data)
    gt_tbl = gt.GT(pd_data)
    assert type(gt_tbl).__name__ == "GT"
