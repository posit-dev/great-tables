import pandas as pd
import pytest

from great_tables import GT
from great_tables._gt_data import Body, GroupRowInfo, GroupRows, Stub, RowInfo


@pytest.fixture
def grouped_gt():
    """A GT table with a groupname column and two groups."""
    df = pd.DataFrame(
        {
            "group": ["A", "A", "B", "B"],
            "value": [1, 2, 3, 4],
        }
    )
    return GT(df, groupname_col="group")


@pytest.fixture
def numeric_grouped_gt():
    """A GT table with a numeric groupname column and two groups."""
    df = pd.DataFrame(
        {
            "group": [1000, 1000, 2000, 2000],
            "value": [1, 2, 3, 4],
        }
    )
    return GT(df, groupname_col="group")


def test_update_group_row_labels_uses_formatted_value(numeric_grouped_gt: GT):
    """When a formatter has been applied, group labels should reflect the formatted value."""
    gt_fmt = numeric_grouped_gt.fmt_number(columns="group", decimals=0)

    built = gt_fmt._render_formats("html")
    labels = [gr.defaulted_label() for gr in built._stub.group_rows]

    assert labels == ["1,000", "2,000"]


def test_update_group_row_labels_falls_back_to_original(grouped_gt: GT):
    """When no formatter is applied, group labels should use the original data value."""
    built = grouped_gt._render_formats("html")
    labels = [gr.defaulted_label() for gr in built._stub.group_rows]

    assert labels == ["A", "B"]


def test_update_group_row_labels_no_groups():
    """When there is no groupname column, the stub is returned unchanged."""
    df = pd.DataFrame({"value": [1, 2, 3]})
    gt_tbl = GT(df)

    built = gt_tbl._render_formats("html")

    # No group rows should exist
    assert len(built._stub.group_rows) == 0


def test_formatted_group_label_in_html(numeric_grouped_gt: GT):
    """Formatted group labels should appear in the rendered HTML output."""
    html = numeric_grouped_gt.fmt_number(columns="group", decimals=0).as_raw_html()

    assert ">1,000</th>" in html
    assert ">2,000</th>" in html


def test_markdown_link_in_group_label_renders_as_anchor():
    """Markdown links in group labels should render as <a> tags in HTML output."""
    df = pd.DataFrame(
        {
            "group": [
                "[Google](https://google.com)",
                "[Google](https://google.com)",
                "[GitHub](https://github.com)",
                "[GitHub](https://github.com)",
            ],
            "value": [1, 2, 3, 4],
        }
    )
    html = GT(df, groupname_col="group").fmt_markdown(columns="group").as_raw_html()

    assert '<a href="https://google.com">Google</a>' in html
    assert '<a href="https://github.com">GitHub</a>' in html
