import pytest
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
    assert result._stubhead.text == "*Car*"

    # Test adding a stubhead label with HTML formatting
    result = gt_data.tab_stubhead(label=gt.html("<strong>Car</strong>"))
    assert result._stubhead.text == "<strong>Car</strong>"



def _two_level_gt():
    df = pd.DataFrame(
        {
            "sector": ["Tech", "Tech", "Finance"],
            "ticker": ["AAPL", "MSFT", "JPM"],
            "price": [189.30, 415.20, 198.47],
        }
    )
    return gt.GT(df, rowname_col=["sector", "ticker"])


def test_tab_stubhead_list_stores_labels():
    result = _two_level_gt().tab_stubhead(label=["Sector", "Ticker"])
    assert result._stubhead == ["Sector", "Ticker"]


def test_tab_stubhead_list_length_mismatch_raises():
    with pytest.raises(ValueError, match="stub has 2 column"):
        _two_level_gt().tab_stubhead(label=["OnlyOne"])


def test_tab_stubhead_list_renders_separate_th_cells():
    html = _two_level_gt().tab_stubhead(label=["Sector", "Ticker"]).as_raw_html()
    # Both labels should appear as separate <th> cells (not merged)
    assert "Sector" in html
    assert "Ticker" in html
    # colspan=1 means they appear individually — no colspan=2 for stub header
    # The stub header area should NOT have colspan="2" when labels are split
    assert 'colspan="2"' not in html.split("gt_col_heading")[1].split("gt_col_heading")[0]


def test_tab_stubhead_list_three_level():
    df = pd.DataFrame(
        {
            "region": ["North", "North", "South"],
            "sector": ["Tech", "Finance", "Tech"],
            "ticker": ["AAPL", "JPM", "NVDA"],
            "price": [189.30, 198.47, 875.40],
        }
    )
    result = gt.GT(df, rowname_col=["region", "sector", "ticker"]).tab_stubhead(
        label=["Region", "Sector", "Ticker"]
    )
    assert result._stubhead == ["Region", "Sector", "Ticker"]
    html = result.as_raw_html()
    assert "Region" in html
    assert "Sector" in html
    assert "Ticker" in html


def test_tab_stubhead_list_wrong_length_three_level_raises():
    df = pd.DataFrame(
        {
            "region": ["North"],
            "sector": ["Tech"],
            "ticker": ["AAPL"],
            "price": [189.30],
        }
    )
    with pytest.raises(ValueError, match="3 column"):
        gt.GT(df, rowname_col=["region", "sector", "ticker"]).tab_stubhead(
            label=["Region", "Sector"]
        )
