import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from gt import GT


@pytest.mark.xfail(reason="Don't have a method to get formatted values as list")
def test_fmt_number_basic():
    df = pd.DataFrame({"x": [1.234, 2.345], "y": [3.456, 4.567]})
    gt = GT(df).fmt_number(columns="x", decimals=2)

    # TODO: is 2.35 below the intended result?
    res = gt._build_data("html")._body.body
    dst = df.assign(x=["1.23", "2.35"])

    assert_frame_equal(res, dst)
