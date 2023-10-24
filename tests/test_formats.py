import pandas as pd

from gt import GT
from gt.gt import _get_column_of_values


def test_fmt_number_basic():
    df = pd.DataFrame({"x": [1.234, 2.345], "y": [3.456, 4.567]})

    # Expect that values in `x` are formatted to 2 decimal places
    gt = GT(df).fmt_number(columns="x", decimals=2)
    x = _get_column_of_values(gt, column_name="x", context="html")
    y = ["1.23", "2.35"]
    assert x == y

    # TODO: this fails because unformatted values not migrated to body
    # Expect that values in `y` are formatted to 2 decimal places
    # x = _get_column_of_values(gt, column_name="y", context="html")
    # y = ["3.46", "4.57"] # is currently ['<NA>', '<NA>']
    # assert x == y

    # Expect that values in `x` are formatted to 5 decimal places
    gt = GT(df).fmt_number(columns="x", decimals=5)
    x = _get_column_of_values(gt, column_name="x", context="html")
    y = ["1.23400", "2.34500"]
    assert x == y
