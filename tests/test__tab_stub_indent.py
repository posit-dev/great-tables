import pytest
import pandas as pd
import great_tables as gt


@pytest.fixture
def gt_with_stub():
    df = pd.DataFrame(
        {
            "row": ["a", "b", "c", "d"],
            "group": ["x", "x", "y", "y"],
            "val": [1, 2, 3, 4],
        }
    )
    return gt.GT(df, rowname_col="row", groupname_col="group")


def test_tab_stub_indent_rows_true_selects_all(gt_with_stub):
    result = gt_with_stub.tab_stub_indent(rows=True, indent=2)
    assert all(row.indent == 2 for row in result._stub.rows)


def test_tab_stub_indent_rows_false_selects_none(gt_with_stub):
    result = gt_with_stub.tab_stub_indent(rows=False, indent=2)
    assert all(row.indent == 0 for row in result._stub.rows)


def test_tab_stub_indent_integer(gt_with_stub):
    result = gt_with_stub.tab_stub_indent(rows=[0, 1], indent=3)
    assert result._stub.rows[0].indent == 3
    assert result._stub.rows[1].indent == 3
    assert result._stub.rows[2].indent == 0
    assert result._stub.rows[3].indent == 0


def test_tab_stub_indent_increase(gt_with_stub):
    # Start at 0, increase by 1
    result = gt_with_stub.tab_stub_indent(rows=[0], indent="increase")
    assert result._stub.rows[0].indent == 1
    assert result._stub.rows[1].indent == 0

    # Increase again from 1
    result2 = result.tab_stub_indent(rows=[0], indent="increase")
    assert result2._stub.rows[0].indent == 2


def test_tab_stub_indent_decrease(gt_with_stub):
    # Set to 2, then decrease
    result = gt_with_stub.tab_stub_indent(rows=[0], indent=2)
    result2 = result.tab_stub_indent(rows=[0], indent="decrease")
    assert result2._stub.rows[0].indent == 1


def test_tab_stub_indent_clamps_to_zero(gt_with_stub):
    # Decrease from 0 stays at 0
    result = gt_with_stub.tab_stub_indent(rows=[0], indent="decrease")
    assert result._stub.rows[0].indent == 0


def test_tab_stub_indent_clamps_to_five(gt_with_stub):
    # Integer beyond 5 is clamped to 5
    result = gt_with_stub.tab_stub_indent(rows=[0], indent=10)
    assert result._stub.rows[0].indent == 5


def test_tab_stub_indent_increase_at_max(gt_with_stub):
    # Increase from 5 stays at 5
    result = gt_with_stub.tab_stub_indent(rows=[0], indent=5)
    result2 = result.tab_stub_indent(rows=[0], indent="increase")
    assert result2._stub.rows[0].indent == 5


def test_tab_stub_indent_html_output(gt_with_stub):
    result = gt_with_stub.tab_stub_indent(rows=[0], indent=2)
    html = result.as_raw_html()
    assert "gt_indent_2" in html


def test_tab_stub_indent_zero_no_class(gt_with_stub):
    result = gt_with_stub.tab_stub_indent(rows=[0], indent=0)
    html = result.as_raw_html()
    assert "gt_indent_0" not in html


@pytest.mark.parametrize("indent", [1, 2, 3, 4, 5])
def test_tab_stub_indent_css_classes(gt_with_stub, indent):
    result = gt_with_stub.tab_stub_indent(rows=[0], indent=indent)
    html = result.as_raw_html()
    assert f"gt_indent_{indent}" in html
