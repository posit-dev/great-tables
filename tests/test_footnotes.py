import polars as pl
import re
from great_tables import GT, loc


def _create_test_data():
    # Create DataFrame with potential for stub and two row groups
    return pl.DataFrame(
        {
            "group": ["A", "A", "A", "B", "B", "B"],
            "row_id": ["r1", "r2", "r3", "r4", "r5", "r6"],
            "col1": [10, 20, 30, 40, 50, 60],
            "col2": [100, 200, 300, 400, 500, 600],
            "col3": [1000, 2000, 3000, 4000, 5000, 6000],
        }
    )


def _create_base_gt():
    df = _create_test_data()
    return (
        GT(df, rowname_col="row_id", groupname_col="group")
        .tab_header(title="Test Title", subtitle="Test Subtitle")
        .tab_spanner(label="Spanner", columns=["col1", "col2"])
    )


def test_tab_footnote_basic():
    # Test basic footnote creation and HTML rendering
    gt_table = _create_base_gt().tab_footnote(
        footnote="Test footnote", locations=loc.body(columns="col1", rows=[0])
    )

    html = gt_table._render_as_html()

    # Check that footnote appears in footer
    assert "Test footnote" in html
    # Check that footnote mark appears in cell
    assert re.search(r"10<span[^>]*>1</span>", html)


def test_tab_footnote_numeric_marks():
    # Test numeric footnote marks (default type of marks)
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="First note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Second note", locations=loc.body(columns="col2", rows=[1]))
        .tab_footnote(footnote="Third note", locations=loc.body(columns="col3", rows=[2]))
    )

    html = gt_table._render_as_html()

    # Check that marks appear in the correct order
    assert re.search(r"10<span[^>]*>1</span>", html)  # First cell
    assert re.search(r"200<span[^>]*>2</span>", html)  # Second cell
    assert re.search(r"3000<span[^>]*>3</span>", html)  # Third cell


def test_tab_footnote_mark_coalescing():
    # Test that multiple footnotes on same location show up as comma-separated marks
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="First note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Second note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Third note", locations=loc.body(columns="col2", rows=[1]))
    )

    html = gt_table._render_as_html()

    # First cell should have coalesced marks "1,2"
    assert re.search(r"10<span[^>]*>1,2</span>", html)
    # Second cell should have single mark "3"
    assert re.search(r"200<span[^>]*>3</span>", html)


def test_tab_footnote_ordering():
    # Test that footnotes are ordered left-to-right, top-to-bottom
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="Body note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Header note", locations=loc.column_labels(columns="col1"))
        .tab_footnote(footnote="Later body note", locations=loc.body(columns="col2", rows=[1]))
    )

    html = gt_table._render_as_html()

    # Header should get mark 1 (comes before body)
    assert re.search(r">col1<span[^>]*>1</span>", html)
    # First body cell should get mark 2
    assert re.search(r"10<span[^>]*>2</span>", html)
    # Later body cell should get mark 3
    assert re.search(r"200<span[^>]*>3</span>", html)


def test_tab_footnote_all_locations():
    # Test that footnotes can be placed in all major locations
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="Title note", locations=loc.title())
        .tab_footnote(footnote="Subtitle note", locations=loc.subtitle())
        .tab_footnote(footnote="Spanner note", locations=loc.spanner_labels(ids=["Spanner"]))
        .tab_footnote(footnote="Column note", locations=loc.column_labels(columns="col1"))
        .tab_footnote(footnote="Body note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Stub note", locations=loc.stub(rows=[0]))
        .tab_footnote(footnote="Row group note", locations=loc.row_groups(rows=[0]))
    )

    html = gt_table._render_as_html()

    # All footnotes should appear in footer
    for note in [
        "Title note",
        "Subtitle note",
        "Spanner note",
        "Column note",
        "Body note",
        "Stub note",
        "Row group note",
    ]:
        assert note in html

    # Check that the footnote marks in the title and subtitle appear
    assert re.search(r"Test Title<span[^>]*>1</span>", html)  # Title
    assert re.search(r"Test Subtitle<span[^>]*>2</span>", html)  # Subtitle


def test_tab_footnote_symbol_marks_standard():
    # Test "standard" symbol marks
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="First note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Second note", locations=loc.body(columns="col2", rows=[1]))
        .tab_footnote(footnote="Third note", locations=loc.body(columns="col3", rows=[2]))
        .tab_footnote(footnote="Fourth note", locations=loc.body(columns="col1", rows=[1]))
        .opt_footnote_marks("standard")
    )

    html = gt_table._render_as_html()

    # Check standard symbols appear in visual reading order
    assert re.search(r"10<span[^>]*>\*</span>", html)
    assert re.search(r"20<span[^>]*>†</span>", html)
    assert re.search(r"200<span[^>]*>‡</span>", html)
    assert re.search(r"3000<span[^>]*>§</span>", html)


def test_tab_footnote_symbol_marks_extended():
    # Test "extended" symbol marks
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="Note 1", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Note 2", locations=loc.body(columns="col2", rows=[0]))
        .tab_footnote(footnote="Note 3", locations=loc.body(columns="col3", rows=[0]))
        .tab_footnote(footnote="Note 4", locations=loc.body(columns="col1", rows=[1]))
        .tab_footnote(footnote="Note 5", locations=loc.body(columns="col2", rows=[1]))
        .tab_footnote(footnote="Note 6", locations=loc.body(columns="col3", rows=[1]))
        .opt_footnote_marks("extended")
    )

    html = gt_table._render_as_html()

    # Check extended symbols appear in reading order (left-to-right, top-to-bottom)
    symbols = ["*", "†", "‡", "§", "‖", "¶"]
    values = [10, 100, 1000, 20, 200, 2000]

    for symbol, value in zip(symbols, values):
        escaped_symbol = re.escape(symbol)
        assert re.search(f"{value}<span[^>]*>{escaped_symbol}</span>", html)


def test_tab_footnote_symbol_marks_letters():
    # Test letter-based marks ("letters")
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="Note A", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Note B", locations=loc.body(columns="col2", rows=[0]))
        .tab_footnote(footnote="Note C", locations=loc.body(columns="col3", rows=[0]))
        .opt_footnote_marks("letters")
    )

    html = gt_table._render_as_html()

    # Check that the letter marks appear
    assert re.search(r"10<span[^>]*>a</span>", html)
    assert re.search(r"100<span[^>]*>b</span>", html)
    assert re.search(r"1000<span[^>]*>c</span>", html)


def test_tab_footnote_symbol_marks_uppercase_letters():
    # Test uppercase letter marks ("LETTERS")
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="Note A", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Note B", locations=loc.body(columns="col2", rows=[0]))
        .tab_footnote(footnote="Note C", locations=loc.body(columns="col3", rows=[0]))
        .opt_footnote_marks("LETTERS")
    )

    html = gt_table._render_as_html()

    # Check that the uppercase letter marks appear
    assert re.search(r"10<span[^>]*>A</span>", html)
    assert re.search(r"100<span[^>]*>B</span>", html)
    assert re.search(r"1000<span[^>]*>C</span>", html)


def test_tab_footnote_custom_symbol_marks():
    # Test custom symbol marks
    custom_marks = ["❶", "❷", "❸", "❹"]  # using circled numbers
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="Note 3", locations=loc.body(columns="col3", rows=[0]))
        .tab_footnote(footnote="Note 2", locations=loc.body(columns="col2", rows=[0]))
        .tab_footnote(footnote="Note 1", locations=loc.body(columns="col1", rows=[0]))
        .opt_footnote_marks(custom_marks)
    )

    html = gt_table._render_as_html()

    # Check that the custom marks appear (in the right order)
    assert re.search(r"10<span[^>]*>❶</span>", html)
    assert re.search(r"100<span[^>]*>❷</span>", html)
    assert re.search(r"1000<span[^>]*>❸</span>", html)


def test_tab_footnote_symbol_cycling():
    # Test the symbol cycling feature (when there are more footnotes than symbols)
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="Note 1", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Note 2", locations=loc.body(columns="col2", rows=[0]))
        .tab_footnote(footnote="Note 3", locations=loc.body(columns="col3", rows=[0]))
        .tab_footnote(
            footnote="Note 4", locations=loc.body(columns="col1", rows=[1])
        )  # Should cycle to **
        .tab_footnote(
            footnote="Note 5", locations=loc.body(columns="col2", rows=[1])
        )  # Should cycle to ††
        .opt_footnote_marks("standard")
    )

    html = gt_table._render_as_html()

    # Check the cycling behavior
    assert re.search(r"10<span[^>]*>\*</span>", html)
    assert re.search(r"100<span[^>]*>†</span>", html)
    assert re.search(r"1000<span[^>]*>‡</span>", html)
    assert re.search(r"20<span[^>]*>§</span>", html)
    assert re.search(r"200<span[^>]*>\*\*</span>", html)


def test_tab_footnote_symbol_coalescing():
    # Test symbol mark coalescing with commas
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="First note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Second note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Third note", locations=loc.body(columns="col2", rows=[0]))
        .opt_footnote_marks("standard")
    )

    html = gt_table._render_as_html()

    # The first cell should have a coalesced symbol marks
    assert re.search(r"10<span[^>]*>\*,†</span>", html)
    # The second cell should have a single symbol mark
    assert re.search(r"100<span[^>]*>‡</span>", html)


def test_tab_footnote_multiple_rows():
    # Test a single footnote targeting multiple rows
    gt_table = _create_base_gt().tab_footnote(
        footnote="Multiple rows note", locations=loc.body(columns="col1", rows=[0, 1, 2])
    )

    html = gt_table._render_as_html()

    # All three cells should have the same footnote mark
    assert re.search(r"10<span[^>]*>1</span>", html)
    assert re.search(r"20<span[^>]*>1</span>", html)
    assert re.search(r"30<span[^>]*>1</span>", html)


def test_tab_footnote_multiple_columns():
    # Test footnote targeting multiple columns
    gt_table = _create_base_gt().tab_footnote(
        footnote="Multiple columns note", locations=loc.body(columns=["col1", "col2"], rows=[0])
    )

    html = gt_table._render_as_html()

    # Both cells in the first row should have the same footnote mark
    assert re.search(r"10<span[^>]*>1</span>", html)
    assert re.search(r"100<span[^>]*>1</span>", html)


def test_tab_footnote_footer_rendering():
    # Test that the footnotes section is properly rendered
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="First footnote text", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Second footnote text", locations=loc.body(columns="col2", rows=[1]))
        .opt_footnote_marks("standard")
    )

    html = gt_table._render_as_html()

    # Check footnotes appear in footer with correct marks
    footer_match = re.search(r"<tfoot[^>]*>.*?</tfoot>", html, re.DOTALL)
    assert footer_match is not None
    footer_html = footer_match.group(0)

    assert re.search(r"<span[^>]*>\*</span>\s*First footnote text", footer_html)
    assert re.search(r"<span[^>]*>†</span>\s*Second footnote text", footer_html)


def test_tab_footnote_with_text_object():
    # Test a footnote with the Text object (not using a basic string)
    from great_tables._text import Text

    gt_table = _create_base_gt().tab_footnote(
        footnote=Text("Bold text"), locations=loc.body(columns="col1", rows=[0])
    )

    html = gt_table._render_as_html()

    # Check that the footnote mark appears
    assert re.search(r"10<span[^>]*>1</span>", html)
    # Check that the text object content should appear in the footer
    assert "Bold text" in html


def test_tab_footnote_hidden_columns():
    df = pl.DataFrame(
        {
            "col1": [10],
            "col2": [100],  # Will be hidden
            "col3": [1000],
            "col4": [10000],  # Will be hidden
        }
    )

    gt_table = (
        GT(df)
        .tab_footnote(footnote="Note A", locations=loc.column_labels(columns="col1"))  # Visible
        .tab_footnote(
            footnote="Note A", locations=loc.column_labels(columns="col2")
        )  # Hidden (same text)
        .tab_footnote(
            footnote="Note A", locations=loc.column_labels(columns="col3")
        )  # Visible (same text)
        .tab_footnote(footnote="Note B", locations=loc.column_labels(columns="col2"))  # Hidden only
        .tab_footnote(
            footnote="Note B", locations=loc.column_labels(columns="col4")
        )  # Hidden only (same text)
        .tab_footnote(footnote="Note C", locations=loc.column_labels(columns="col1"))  # Visible
        .cols_hide(columns=["col2", "col4"])
    )

    html = gt_table._render_as_html()

    # Extract footnote marks from visible column headers
    col1_match = re.search(r'id="col1"[^>]*>([^<]*(?:<[^>]*>[^<]*)*)</th>', html)
    col3_match = re.search(r'id="col3"[^>]*>([^<]*(?:<[^>]*>[^<]*)*)</th>', html)

    assert col1_match is not None
    assert col3_match is not None

    col1_marks_match = re.search(
        r'<span class="gt_footnote_marks"[^>]*>([^<]*)</span>', col1_match.group(1)
    )
    col3_marks_match = re.search(
        r'<span class="gt_footnote_marks"[^>]*>([^<]*)</span>', col3_match.group(1)
    )

    # col1 should have marks 1,2 (Note A and Note C)
    assert col1_marks_match is not None
    assert col1_marks_match.group(1) == "1,2"

    # col3 should have mark 1 only (Note A)
    assert col3_marks_match is not None
    assert col3_marks_match.group(1) == "1"

    # Extract footer footnotes
    footer_matches = re.findall(
        r'<span class="gt_footnote_marks"[^>]*>([^<]*)</span>\s*([^<]+?)(?=</td>)', html
    )

    # Should only show 2 footnotes in footer (Note A and Note C)
    # Note B should not appear because it only targets hidden columns
    assert len(footer_matches) == 2

    # Check footnote texts and marks
    footnote_dict = {mark.rstrip("."): text.strip() for mark, text in footer_matches}
    assert footnote_dict["1"] == "Note A"  # Appears on visible columns
    assert footnote_dict["2"] == "Note C"  # Appears on visible column
    assert "Note B" not in html  # Should not appear anywhere since only targets hidden columns

    # Verify that duplicate footnote text gets same mark number
    # Note A appears on both col1 and col3 but should use the same mark (1)


def test_tab_footnote_mixed_locations_hidden():
    df = pl.DataFrame({"visible_col": [10], "hidden_col": [100]})

    gt_table = (
        GT(df)
        .tab_footnote(
            footnote="Mixed location note",
            locations=[
                loc.column_labels(columns="visible_col"),
                loc.column_labels(columns="hidden_col"),
            ],
        )
        .cols_hide(columns="hidden_col")
    )

    html = gt_table._render_as_html()

    # Footnote should appear because it targets at least one visible location
    assert "Mixed location note" in html

    # Mark should appear on visible column
    visible_match = re.search(r'id="visible_col"[^>]*>([^<]*(?:<[^>]*>[^<]*)*)</th>', html)
    assert visible_match is not None

    marks_match = re.search(
        r'<span class="gt_footnote_marks"[^>]*>([^<]*)</span>', visible_match.group(1)
    )
    assert marks_match is not None
    assert marks_match.group(1) == "1"
