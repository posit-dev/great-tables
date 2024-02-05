import pandas as pd
import pytest
from great_tables import GT
from great_tables._scss import compile_scss




def test_options_no_mutate():
    df = pd.DataFrame({"x": [1, 2, 3]})
    gt = GT(df)

    gt2 = gt.tab_options(container_width="100px")
    gt3 = gt.tab_options(container_width="999px")

    assert gt2._options.container_width.value == "100px"
    assert gt3._options.container_width.value == "999px"
