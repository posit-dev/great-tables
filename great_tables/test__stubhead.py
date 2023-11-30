import great_tables as gt
import pandas as pd


def test_tab_stubhead():
    # Create a GTData object with row labels
    df = pd.DataFrame({"model": ["Toyota", "Honda", "Ford"], "year": [2020, 2021, 2019]})
    gt_data = gt.GT(df, rowname_col="model")

    # Test adding a stubhead label
    result = gt_data.tab_stubhead(label="Car")
    assert result._stubhead == "Car"

    # Test adding a stubhead label with Markdown formatting
    result = gt_data.tab_stubhead(label=gt.md("*Car*"))
    assert result._stubhead == "*Car*"
