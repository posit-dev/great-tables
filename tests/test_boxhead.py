import pandas as pd
from great_tables import GT
from great_tables.gt import _get_column_labels


def test_cols_label():
    df = pd.DataFrame({"x": [1.234, 2.345], "y": [3.456, 4.567]})
    gt = GT(df).cols_label(x="ex", y="why")

    x = _get_column_labels(gt=gt, context="html")
    y = ["ex", "why"]
    assert x == y
