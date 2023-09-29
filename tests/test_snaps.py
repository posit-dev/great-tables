from gt import *
import pandas as pd


def test_render_doc_module(snapshot):
    pd_data = pd.DataFrame([{"a": 5.23, "b": 15}, {"a": 15, "b": 2000}])

    res = gt.GT(pd_data)._repr_html_()

    assert res == snapshot
