import pandas as pd
import pytest
from great_tables._body import body_reassemble
from great_tables._gt_data import Body, Boxhead, Stub
from pandas.testing import assert_frame_equal


df = pd.DataFrame(
    {"col1": [1, 2, 3, 4], "col2": ["b", "a", "b", "a"], "col3": [4.0, 5.0, 6.0, 7.0]}
)
