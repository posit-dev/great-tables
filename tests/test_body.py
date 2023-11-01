from great_tables._gt_data import Body, Stub, Boxhead
from great_tables._body import body_reassemble
import pandas as pd
from pandas.testing import assert_frame_equal


df = pd.DataFrame(
    {"col1": [1, 2, 3, 4], "col2": ["b", "a", "b", "a"], "col3": [4.0, 5.0, 6.0, 7.0]}
)


def test_body_reassemble():
    body = Body(df)
    boxhead = Boxhead(df)
    stub_df = Stub(df, groupname_col="col2")

    row_groups = stub_df._to_row_groups()

    body_reassembled = body_reassemble(body, row_groups, stub_df, boxhead)

    compare_df = df.iloc[[0, 2, 1, 3],]

    assert_frame_equal(body_reassembled.body, compare_df)
