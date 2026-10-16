import pandas as pd

from great_tables import GT
from great_tables._tbl_data import to_list


def test_sub_values_skips_pandas_na():
    df = pd.DataFrame({"x": pd.Series([1, None, 2], dtype="Int64")})

    gt = GT(df).sub_values(columns="x", values=[1], replacement="one")
    body = to_list(gt._render_formats("html")._body.body["x"])

    assert body[0] == "one"
    assert body[1] is pd.NA
    assert body[2] == "2"
