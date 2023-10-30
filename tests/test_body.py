from great_tables._gt_data import Body, RowGroups, Stub, Boxhead
from great_tables._body import body_reassemble
import pandas as pd
from pandas.testing import assert_frame_equal


df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["b", "a", "c"], "col3": [4.0, 5.0, 6.0]})


def test_body_reassemble():
    body = Body(df)
    boxhead = Boxhead(df)
    stub_df = Stub(df, rowname_col="col2")

    group_ids = set(row.group_id for row in stub_df if row.group_id is not None)
    row_groups = RowGroups(list(group_ids))

    body_reassembled = body_reassemble(body, row_groups, stub_df, boxhead)

    compare_df = df.iloc[[1, 0, 2],]

    assert_frame_equal(body_reassembled.body, compare_df)
