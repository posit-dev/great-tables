import pandas as pd
from great_tables import GT


def test_heading_no_mutate():
    df = pd.DataFrame({"x": [1, 2, 3]})
    gt = GT(df)

    gt2 = gt.tab_header(title="First")

    assert gt2 is not gt
    assert gt._heading.title is None
    assert gt2._heading.title == "First"
