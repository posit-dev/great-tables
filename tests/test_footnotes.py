import polars as pl
import re
from great_tables import GT, loc, md, html
from great_tables._gt_data import FootnotePlacement, FootnoteInfo
from great_tables._text import Text
from great_tables._utils_render_html import (
    create_body_component_h,
    _apply_footnote_placement,
    _create_footnote_mark_html,
    _get_column_index,
    _get_footnote_mark_string,
    _get_spanner_leftmost_column_index,
    _is_numeric_content,
)


def assert_rendered_body(snapshot, gt):
    built = gt._build_data("html")
    body = create_body_component_h(built)

    assert snapshot == body


def assert_complete_html_without_style(snapshot, gt):
    import re

    html = gt.as_raw_html()
    html_without_style = re.sub(r"<style>.*?</style>", "", html, flags=re.DOTALL)

    assert snapshot == html_without_style


def _create_test_data():
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
    gt_table = _create_base_gt().tab_footnote(
        footnote="Test footnote", locations=loc.body(columns="col1", rows=[0])
    )

    html = gt_table._render_as_html()

    # Check that footnote appears in footer
    assert "Test footnote" in html
    # Check that footnote mark appears in cell (left placement for numbers with auto)
    assert re.search(r"<span[^>]*>1</span> 10", html)


def test_tab_footnote_numeric_marks():
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="First note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Second note", locations=loc.body(columns="col2", rows=[1]))
        .tab_footnote(footnote="Third note", locations=loc.body(columns="col3", rows=[2]))
    )

    html = gt_table._render_as_html()

    # Check that marks appear in the correct order (left placement for numbers with auto)
    assert re.search(r"<span[^>]*>1</span> 10", html)  # First cell
    assert re.search(r"<span[^>]*>2</span> 200", html)  # Second cell
    assert re.search(r"<span[^>]*>3</span> 3000", html)  # Third cell


def test_tab_footnote_mark_coalescing():
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="First note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Second note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Third note", locations=loc.body(columns="col2", rows=[1]))
    )

    html = gt_table._render_as_html()

    # First cell should have coalesced marks "1,2" (left placement for numbers with auto)
    assert re.search(r"<span[^>]*>1,2</span> 10", html)
    # Second cell should have single mark "3" (left placement for numbers with auto)
    assert re.search(r"<span[^>]*>3</span> 200", html)


def test_tab_footnote_ordering():
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="Body note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Header note", locations=loc.column_labels(columns="col1"))
        .tab_footnote(footnote="Later body note", locations=loc.body(columns="col2", rows=[1]))
    )

    html = gt_table._render_as_html()

    # Header should get mark 1 (comes before body); text gets right placement
    assert re.search(r">col1<span[^>]*>1</span>", html)
    # First body cell should get mark 2; numbers get left placement with auto
    assert re.search(r"<span[^>]*>2</span> 10", html)
    # Later body cell should get mark 3; numbers get left placement with auto
    assert re.search(r"<span[^>]*>3</span> 200", html)


def test_tab_footnote_all_locations():
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
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="First note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Second note", locations=loc.body(columns="col2", rows=[1]))
        .tab_footnote(footnote="Third note", locations=loc.body(columns="col3", rows=[2]))
        .tab_footnote(footnote="Fourth note", locations=loc.body(columns="col1", rows=[1]))
        .opt_footnote_marks("standard")
    )

    html = gt_table._render_as_html()

    # Check standard symbols appear in visual reading order (left placement for numbers with auto)
    assert re.search(r"<span[^>]*>\*</span> 10", html)
    assert re.search(r"<span[^>]*>†</span> 20", html)
    assert re.search(r"<span[^>]*>‡</span> 200", html)
    assert re.search(r"<span[^>]*>§</span> 3000", html)


def test_tab_footnote_symbol_marks_extended():
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
    # Numbers get left placement with auto
    symbols = ["*", "†", "‡", "§", "‖", "¶"]
    values = [10, 100, 1000, 20, 200, 2000]

    for symbol, value in zip(symbols, values):
        escaped_symbol = re.escape(symbol)
        assert re.search(f"<span[^>]*>{escaped_symbol}</span> {value}", html)


def test_tab_footnote_symbol_marks_letters():
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="Note A", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Note B", locations=loc.body(columns="col2", rows=[0]))
        .tab_footnote(footnote="Note C", locations=loc.body(columns="col3", rows=[0]))
        .opt_footnote_marks("letters")
    )

    html = gt_table._render_as_html()

    # Check that the letter marks appear (left placement for numbers with auto)
    assert re.search(r"<span[^>]*>a</span> 10", html)
    assert re.search(r"<span[^>]*>b</span> 100", html)
    assert re.search(r"<span[^>]*>c</span> 1000", html)


def test_tab_footnote_symbol_marks_uppercase_letters():
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="Note A", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Note B", locations=loc.body(columns="col2", rows=[0]))
        .tab_footnote(footnote="Note C", locations=loc.body(columns="col3", rows=[0]))
        .opt_footnote_marks("LETTERS")
    )

    html = gt_table._render_as_html()

    # Check that the uppercase letter marks appear (left placement for numbers with auto)
    assert re.search(r"<span[^>]*>A</span> 10", html)
    assert re.search(r"<span[^>]*>B</span> 100", html)
    assert re.search(r"<span[^>]*>C</span> 1000", html)


def test_tab_footnote_custom_symbol_marks():
    custom_marks = ["❶", "❷", "❸", "❹"]  # using circled numbers
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="Note 3", locations=loc.body(columns="col3", rows=[0]))
        .tab_footnote(footnote="Note 2", locations=loc.body(columns="col2", rows=[0]))
        .tab_footnote(footnote="Note 1", locations=loc.body(columns="col1", rows=[0]))
        .opt_footnote_marks(custom_marks)
    )

    html = gt_table._render_as_html()

    # Check that the custom marks appear (in the right order, left placement for numbers with auto)
    assert re.search(r"<span[^>]*>❶</span> 10", html)
    assert re.search(r"<span[^>]*>❷</span> 100", html)
    assert re.search(r"<span[^>]*>❸</span> 1000", html)


def test_tab_footnote_symbol_cycling():
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

    # Check the cycling behavior (left placement for numbers with auto)
    assert re.search(r"<span[^>]*>\*</span> 10", html)
    assert re.search(r"<span[^>]*>†</span> 100", html)
    assert re.search(r"<span[^>]*>‡</span> 1000", html)
    assert re.search(r"<span[^>]*>§</span> 20", html)
    assert re.search(r"<span[^>]*>\*\*</span> 200", html)


def test_tab_footnote_symbol_coalescing():
    gt_table = (
        _create_base_gt()
        .tab_footnote(footnote="First note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Second note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Third note", locations=loc.body(columns="col2", rows=[0]))
        .opt_footnote_marks("standard")
    )

    html = gt_table._render_as_html()

    # The first cell should have a coalesced symbol marks (left placement for numbers with auto)
    assert re.search(r"<span[^>]*>\*,†</span> 10", html)

    # The second cell should have a single symbol mark (left placement for numbers with auto)
    assert re.search(r"<span[^>]*>‡</span> 100", html)


def test_tab_footnote_multiple_rows():
    gt_table = _create_base_gt().tab_footnote(
        footnote="Multiple rows note", locations=loc.body(columns="col1", rows=[0, 1, 2])
    )

    html = gt_table._render_as_html()

    # All three cells should have the same footnote mark (left placement for numbers with auto)
    assert re.search(r"<span[^>]*>1</span> 10", html)
    assert re.search(r"<span[^>]*>1</span> 20", html)
    assert re.search(r"<span[^>]*>1</span> 30", html)


def test_tab_footnote_multiple_columns():
    gt_table = _create_base_gt().tab_footnote(
        footnote="Multiple columns note", locations=loc.body(columns=["col1", "col2"], rows=[0])
    )

    html = gt_table._render_as_html()

    # Both cells in the first row should have the same footnote mark (left placement for numbers with auto)
    assert re.search(r"<span[^>]*>1</span> 10", html)
    assert re.search(r"<span[^>]*>1</span> 100", html)


def test_tab_footnote_footer_rendering():
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
    # Test a footnote with the Text object
    gt_table = _create_base_gt().tab_footnote(
        footnote=Text("Bold text"), locations=loc.body(columns="col1", rows=[0])
    )

    html = gt_table._render_as_html()

    # Check that the footnote mark appears (left placement for numbers with auto)
    assert re.search(r"<span[^>]*>1</span> 10", html)

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
        .tab_footnote(footnote="Note A", locations=loc.column_labels(columns="col1"))
        .tab_footnote(footnote="Note A", locations=loc.column_labels(columns="col2"))
        .tab_footnote(footnote="Note A", locations=loc.column_labels(columns="col3"))
        .tab_footnote(footnote="Note B", locations=loc.column_labels(columns="col2"))
        .tab_footnote(footnote="Note B", locations=loc.column_labels(columns="col4"))
        .tab_footnote(footnote="Note C", locations=loc.column_labels(columns="col1"))
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

    # Check footnote text and marks
    footnote_dict = {mark.rstrip("."): text.strip() for mark, text in footer_matches}
    assert footnote_dict["1"] == "Note A"  # Appears on visible columns
    assert footnote_dict["2"] == "Note C"  # Appears on visible column
    assert "Note B" not in html  # Should not appear anywhere since only targets hidden columns


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


def test_tab_footnote_stub_body_ordering_snapshot(snapshot):
    df = pl.DataFrame(
        {
            "name": ["A", "B"],
            "value": ["Y", "Z"],
        }
    )

    gt_table = (
        GT(df, rowname_col="name", id="test_stub_body_footnotes")
        .tab_footnote(
            footnote="Body note.",
            locations=loc.body(columns="value", rows=[1]),
        )
        .tab_footnote(
            footnote="Stub note.",
            locations=loc.stub(rows=[0]),
        )
    )

    # Use assert_rendered_body to create a smaller, focused snapshot
    assert_rendered_body(snapshot, gt_table)


def test_tab_footnote_complete_ordering_snapshot(snapshot):
    df = pl.DataFrame(
        {
            "name": ["Row1"],
            "col1": [10],
            "col2": [20],
        }
    )

    gt_table = (
        GT(df, rowname_col="name", id="test_complete_footnote_ordering")
        .tab_header(title="Title", subtitle="Subtitle")
        .tab_stubhead(label="Stubhead")
        .tab_spanner(label="Spanner A", columns=["col1"])
        .tab_spanner(label="Spanner B", columns=["col2"])
        .tab_footnote(footnote="Subtitle note", locations=loc.subtitle())
        .tab_footnote(footnote="Spanner B note", locations=loc.spanner_labels(ids=["Spanner B"]))
        .tab_footnote(footnote="Spanner A note", locations=loc.spanner_labels(ids=["Spanner A"]))
        .tab_footnote(footnote="Title note", locations=loc.title())
        .tab_footnote(footnote="Col2 note", locations=loc.column_labels(columns="col2"))
        .tab_footnote(footnote="Col1 note", locations=loc.column_labels(columns="col1"))
        .tab_footnote(footnote="Body note", locations=loc.body(columns="col1", rows=[0]))
        .tab_footnote(footnote="Stub note", locations=loc.stub(rows=[0]))
        .tab_footnote(footnote="Stubhead note", locations=loc.stubhead())
    )

    # Use `assert_complete_html_without_style()` to capture all footnote marks in the table (and
    # the footnotes in the footer section)
    assert_complete_html_without_style(snapshot, gt_table)


def test_tab_footnote_md_with_unit_notation():
    df = pl.DataFrame({"area": [100, 200], "value": [10, 20]})

    gt_table = GT(df).tab_footnote(
        footnote=md("**Area** is measured in {{km^2}}."),
        locations=loc.body(columns="area", rows=[0]),
    )

    html_output = gt_table._render_as_html()

    assert (
        '<strong>Area</strong> is measured in km<span style="white-space:nowrap;"><sup style="line-height:0;">2</sup></span>'
        in html_output
    )


def test_tab_footnote_html_with_unit_notation():
    # Test that html() footnotes also support unit notation like {{km^2}}
    df = pl.DataFrame({"area": [100, 200], "value": [10, 20]})

    gt_table = GT(df).tab_footnote(
        footnote=html("<strong>Area</strong> is measured in {{km^2}}."),
        locations=loc.body(columns="area", rows=[0]),
    )

    html_output = gt_table._render_as_html()

    assert (
        '<strong>Area</strong> is measured in km<span style="white-space:nowrap;"><sup style="line-height:0;">2</sup></span>'
        in html_output
    )


def test_footer_structure_combined():
    df = pl.DataFrame({"area": [100, 200], "value": [10, 20]})

    gt_table = (
        GT(df)
        .tab_source_note("Source: Test data.")
        .tab_footnote(
            footnote="Area footnote.",
            locations=loc.body(columns="area", rows=[0]),
        )
        .tab_footnote(
            footnote="Value footnote.",
            locations=loc.body(columns="value", rows=[1]),
        )
    )

    html_output = gt_table._render_as_html()

    # Check that there is only a single <tfoot> container
    assert html_output.count("<tfoot") == 1
    assert html_output.count("</tfoot>") == 1

    # Check that both source notes and footnotes are present
    assert "gt_sourcenote" in html_output
    assert html_output.count("gt_footnote") >= 2

    # Check proper class structure (should use the `gt_footnotes` class)
    assert 'class="gt_footnotes"' in html_output

    # Check that footnote marks are present
    assert "gt_footnote_marks" in html_output


def test_tab_footnote_complex_spanner_ordering():
    df = pl.DataFrame(
        {
            "region": ["North", "South", "East", "West"],
            "q1_sales": [100, 110, 95, 105],
            "q1_profit": [20, 25, 18, 22],
            "q2_sales": [120, 130, 115, 125],
            "q2_profit": [25, 30, 22, 28],
            "q3_sales": [140, 150, 135, 145],
            "q3_profit": [30, 35, 27, 32],
        }
    )

    gt_table = (
        GT(df, rowname_col="region")
        .tab_header(title="Quarterly Performance", subtitle="By Region")
        .tab_stubhead(label="Region")
        .tab_spanner(label="Q1 Performance", columns=["q1_sales", "q1_profit"])
        .tab_spanner(label="Q2 Performance", columns=["q2_sales", "q2_profit"])
        .tab_spanner(label="Q3 Performance", columns=["q3_sales", "q3_profit"])
        .tab_spanner(label="Sales Data", columns=["q1_sales", "q2_sales", "q3_sales"])
        .tab_spanner(label="Profit Data", columns=["q1_profit", "q2_profit", "q3_profit"])
        .cols_label(
            q1_sales="Sales",
            q1_profit="Profit",
            q2_sales="Sales",
            q2_profit="Profit",
            q3_sales="Sales",
            q3_profit="Profit",
        )
        .tab_footnote(footnote="Title footnote", locations=loc.title())
        .tab_footnote(footnote="Subtitle footnote", locations=loc.subtitle())
        .tab_footnote(footnote="Stubhead footnote", locations=loc.stubhead())
        .tab_footnote(
            footnote="Sales Data spanner footnote", locations=loc.spanner_labels(ids=["Sales Data"])
        )
        .tab_footnote(
            footnote="Profit Data spanner footnote",
            locations=loc.spanner_labels(ids=["Profit Data"]),
        )
        .tab_footnote(
            footnote="Q1 Performance spanner footnote",
            locations=loc.spanner_labels(ids=["Q1 Performance"]),
        )
        .tab_footnote(
            footnote="Q2 Performance spanner footnote",
            locations=loc.spanner_labels(ids=["Q2 Performance"]),
        )
        .tab_footnote(
            footnote="Q3 Performance spanner footnote",
            locations=loc.spanner_labels(ids=["Q3 Performance"]),
        )
        .tab_footnote(
            footnote="Q1 Sales column footnote", locations=loc.column_labels(columns="q1_sales")
        )
        .tab_footnote(
            footnote="Q1 Profit column footnote", locations=loc.column_labels(columns="q1_profit")
        )
        .tab_footnote(footnote="North region footnote", locations=loc.stub(rows=[0]))
        .tab_footnote(footnote="South region footnote", locations=loc.stub(rows=[1]))
        .tab_footnote(
            footnote="Cell footnote (North Q1 Sales)",
            locations=loc.body(columns="q1_sales", rows=[0]),
        )
        .tab_footnote(
            footnote="Cell footnote (South Q2 Profit)",
            locations=loc.body(columns="q2_profit", rows=[1]),
        )
    )

    html = gt_table._render_as_html()

    # Check that all footnotes appear in footer
    expected_footnotes = [
        "Title footnote",
        "Subtitle footnote",
        "Stubhead footnote",
        "Sales Data spanner footnote",
        "Profit Data spanner footnote",
        "Q1 Performance spanner footnote",
        "Q2 Performance spanner footnote",
        "Q3 Performance spanner footnote",
        "Q1 Sales column footnote",
        "Q1 Profit column footnote",
        "North region footnote",
        "South region footnote",
        "Cell footnote (North Q1 Sales)",
        "Cell footnote (South Q2 Profit)",
    ]

    for footnote in expected_footnotes:
        assert footnote in html

    #
    # Check that footnote marks appear in the expected locations
    #

    # Title should have mark 1
    assert re.search(r"Quarterly Performance<span[^>]*>1</span>", html)

    # Subtitle should have mark 2
    assert re.search(r"By Region<span[^>]*>2</span>", html)

    # Stubhead should have mark 3
    assert re.search(r"Region<span[^>]*>3</span>", html)

    # Test that spanner marks are present by looking for any spanner with footnote marks
    spanner_marks = re.findall(
        r'<span class="gt_column_spanner">[^<]*<span[^>]*class="gt_footnote_marks"[^>]*>([^<]+)</span>',
        html,
    )
    assert len(spanner_marks) > 0

    #
    # Test that marks are ordered sequentially (1, 2, 3, ...)
    #

    # Extract all footnote marks from the HTML
    mark_pattern = r'<span[^>]*class="gt_footnote_marks"[^>]*>([^<]+)</span>'
    all_marks = re.findall(mark_pattern, html)

    # Convert marks to individual numbers (handle comma-separated marks like "1,2")
    mark_numbers = []
    for mark in all_marks:
        for single_mark in mark.split(","):
            if single_mark.strip().isdigit():
                mark_numbers.append(int(single_mark.strip()))

    # Check they include sequential numbers starting from 1
    if mark_numbers:
        unique_marks = sorted(list(set(mark_numbers)))
        assert 1 in unique_marks
        assert len(unique_marks) >= 3


def test_tab_footnote_spanner_specific_functionality():
    df = pl.DataFrame({"col1": [1, 2], "col2": [3, 4], "col3": [5, 6], "col4": [7, 8]})

    gt_table = (
        GT(df)
        .tab_spanner(label="Group A", columns=["col1", "col2"])
        .tab_spanner(label="Group B", columns=["col3", "col4"])
        .tab_footnote(footnote="First spanner note", locations=loc.spanner_labels(ids=["Group A"]))
        .tab_footnote(footnote="Second spanner note", locations=loc.spanner_labels(ids=["Group A"]))
        .tab_footnote(footnote="Group B note", locations=loc.spanner_labels(ids=["Group B"]))
    )

    html = gt_table._render_as_html()

    # Check that all spanner footnotes appear
    assert "First spanner note" in html
    assert "Second spanner note" in html
    assert "Group B note" in html

    #
    # Check that spanner labels get footnote marks
    #

    # Group A should have marks for both footnotes
    group_a_marks = re.findall(
        r'Group A<span[^>]*class="gt_footnote_marks"[^>]*>([^<]+)</span>', html
    )
    assert len(group_a_marks) >= 1

    # Group B should have its own mark
    group_b_marks = re.findall(
        r'Group B<span[^>]*class="gt_footnote_marks"[^>]*>([^<]+)</span>', html
    )
    assert len(group_b_marks) >= 1


# ===========================================================================================
# Tests for utility functions
# ===========================================================================================


def test_is_numeric_content():
    # Test basic numbers
    assert _is_numeric_content("123") == True
    assert _is_numeric_content("123.45") == True
    assert _is_numeric_content("0") == True
    assert _is_numeric_content("0.0") == True

    # Test formatted numbers
    assert _is_numeric_content("1,234") == True
    assert _is_numeric_content("1,234.56") == True
    assert _is_numeric_content("$123") == True
    assert _is_numeric_content("$1,234.56") == True
    assert _is_numeric_content("123%") == True
    assert _is_numeric_content("(123)") == True
    assert _is_numeric_content("€1,234.56") == True
    assert _is_numeric_content("£1,234.56") == True
    assert _is_numeric_content("¥1,234") == True

    # Test numbers with various formatting
    assert _is_numeric_content("  123  ") == True
    assert _is_numeric_content("+123") == True
    assert _is_numeric_content("-123") == True
    assert _is_numeric_content("−123") == True

    # Test with HTML tags
    assert _is_numeric_content("<span>123</span>") == True
    assert _is_numeric_content("<b>$1,234.56</b>") == True
    assert _is_numeric_content('<div class="number">123.45</div>') == True

    # Test non-numeric content
    assert _is_numeric_content("Hello") == False
    assert _is_numeric_content("Text123") == False
    assert _is_numeric_content("123Text") == False
    assert _is_numeric_content("A") == False
    assert _is_numeric_content("NA") == False
    assert _is_numeric_content("NULL") == False
    assert _is_numeric_content("") == False
    assert _is_numeric_content("   ") == False

    # Test mixed content with HTML
    assert _is_numeric_content("<span>Hello</span>") == False
    assert _is_numeric_content("<b>Text Content</b>") == False

    # Test edge cases
    assert _is_numeric_content("$") == False
    assert _is_numeric_content("%") == False
    assert _is_numeric_content("()") == False
    assert _is_numeric_content(",") == False
    assert _is_numeric_content(".") == False
    assert _is_numeric_content("..") == False


def test_apply_footnote_placement():
    text = "123"
    marks_html = '<span class="gt_footnote_marks">1</span>'

    # Test left placement
    result = _apply_footnote_placement(text, marks_html, FootnotePlacement.left)
    expected = '<span class="gt_footnote_marks">1</span> 123'
    assert result == expected

    # Test right placement
    result = _apply_footnote_placement(text, marks_html, FootnotePlacement.right)
    expected = '123<span class="gt_footnote_marks">1</span>'
    assert result == expected

    # Test auto placement with numeric content
    result = _apply_footnote_placement("123", marks_html, FootnotePlacement.auto)
    expected = '<span class="gt_footnote_marks">1</span> 123'  # Should go left for numbers
    assert result == expected

    # Test auto placement with text content
    result = _apply_footnote_placement("Hello", marks_html, FootnotePlacement.auto)
    expected = 'Hello<span class="gt_footnote_marks">1</span>'  # Should go right for text
    assert result == expected

    # Test auto placement with formatted numbers
    result = _apply_footnote_placement("$1,234.56", marks_html, FootnotePlacement.auto)
    expected = (
        '<span class="gt_footnote_marks">1</span> $1,234.56'  # Should go left for formatted numbers
    )
    assert result == expected

    # Test None placement (should default to auto)
    result = _apply_footnote_placement("123", marks_html, None)
    expected = '<span class="gt_footnote_marks">1</span> 123'  # Should go left for numbers
    assert result == expected

    # Test with HTML content
    html_text = "<b>456</b>"
    result = _apply_footnote_placement(html_text, marks_html, FootnotePlacement.auto)
    expected = (
        '<span class="gt_footnote_marks">1</span> <b>456</b>'  # Should go left for numbers in HTML
    )
    assert result == expected

    html_text = "<b>Hello</b>"
    result = _apply_footnote_placement(html_text, marks_html, FootnotePlacement.auto)
    expected = (
        '<b>Hello</b><span class="gt_footnote_marks">1</span>'  # Should go right for text in HTML
    )
    assert result == expected


def test_footnote_placement_snapshot_different_types(snapshot):
    import pandas as pd

    # Create test data with different value types
    df = pd.DataFrame(
        {
            "integers": [42],
            "floats": [123.45],
            "currency": ["$1,234.56"],
            "percentages": ["85.5%"],
            "text": ["Hello"],
            "mixed": ["ABC123"],
            "formatted_num": ["(1,000)"],
            "scientific": ["1.23e-4"],
        }
    )

    # Test with auto placement (default)
    gt_auto = (
        GT(df, id="test_auto_placement")
        .tab_header(title="Auto Placement Test")
        .tab_footnote("Integer footnote", locations=loc.body(columns="integers", rows=[0]))
        .tab_footnote("Float footnote", locations=loc.body(columns="floats", rows=[0]))
        .tab_footnote("Currency footnote", locations=loc.body(columns="currency", rows=[0]))
        .tab_footnote("Percentage footnote", locations=loc.body(columns="percentages", rows=[0]))
        .tab_footnote("Text footnote", locations=loc.body(columns="text", rows=[0]))
        .tab_footnote("Mixed footnote", locations=loc.body(columns="mixed", rows=[0]))
        .tab_footnote(
            "Formatted number footnote", locations=loc.body(columns="formatted_num", rows=[0])
        )
        .tab_footnote("Scientific footnote", locations=loc.body(columns="scientific", rows=[0]))
    )

    assert_complete_html_without_style(snapshot, gt_auto)


def test_footnote_placement_snapshot_left_placement(snapshot):
    import pandas as pd

    df = pd.DataFrame({"integers": [42], "text": ["Hello"], "currency": ["$1,234.56"]})

    # Test with explicit left placement
    gt_left = (
        GT(df, id="test_left_placement")
        .tab_header(title="Left Placement Test")
        .tab_footnote(
            "Integer footnote", locations=loc.body(columns="integers", rows=[0]), placement="left"
        )
        .tab_footnote(
            "Text footnote", locations=loc.body(columns="text", rows=[0]), placement="left"
        )
        .tab_footnote(
            "Currency footnote", locations=loc.body(columns="currency", rows=[0]), placement="left"
        )
    )

    assert_complete_html_without_style(snapshot, gt_left)


def test_footnote_placement_snapshot_right_placement(snapshot):
    import pandas as pd

    df = pd.DataFrame({"integers": [42], "text": ["Hello"], "currency": ["$1,234.56"]})

    # Test with explicit right placement
    gt_right = (
        GT(df, id="test_right_placement")
        .tab_header(title="Right Placement Test")
        .tab_footnote(
            "Integer footnote", locations=loc.body(columns="integers", rows=[0]), placement="right"
        )
        .tab_footnote(
            "Text footnote", locations=loc.body(columns="text", rows=[0]), placement="right"
        )
        .tab_footnote(
            "Currency footnote", locations=loc.body(columns="currency", rows=[0]), placement="right"
        )
    )

    assert_complete_html_without_style(snapshot, gt_right)


def test_source_notes_single_line_with_footnotes():
    import pandas as pd

    df = pd.DataFrame({"values": [42, 123]})

    # Create a table with source notes in single-line mode and footnotes
    gt_table = (
        GT(df)
        .tab_header(title="Table with Source Notes and Footnotes")
        .tab_source_note("First source note")
        .tab_source_note("Second source note")
        .tab_source_note("Third source note")
        .tab_footnote("Value footnote", locations=loc.body(columns="values", rows=[0]))
        .tab_options(source_notes_multiline=False)
    )

    html = gt_table._render_as_html()

    # Check that source notes are in single line (joined by separator)
    # The default separator should be used to join the notes
    assert "First source note" in html
    assert "Second source note" in html
    assert "Third source note" in html

    # Check that footnotes are also present
    assert "Value footnote" in html

    # Verify the HTML structure: source notes should be in a single row
    import re

    # Look for source notes in a single <td> with the `gt_sourcenote` class
    source_note_pattern = r'<tr class="gt_sourcenotes"><td class="gt_sourcenote"[^>]*><span class="gt_from_md">[^<]*First source note[^<]*Second source note[^<]*Third source note[^<]*</span></td></tr>'
    assert re.search(source_note_pattern, html)


def test_source_notes_multiline_with_footnotes():
    import pandas as pd

    df = pd.DataFrame({"values": [42, 123]})

    # Create a table with source notes in multiline mode and footnotes
    gt_table = (
        GT(df)
        .tab_header(title="Table with Multiline Source Notes and Footnotes")
        .tab_source_note("First source note")
        .tab_source_note("Second source note")
        .tab_source_note("Third source note")
        .tab_footnote("Value footnote", locations=loc.body(columns="values", rows=[0]))
        .tab_options(source_notes_multiline=True)
    )

    html = gt_table._render_as_html()

    # Check that source notes are present
    assert "First source note" in html
    assert "Second source note" in html
    assert "Third source note" in html

    # Check that footnotes are also present
    assert "Value footnote" in html

    # Verify the HTML structure: each source note should be in its own row
    import re

    # Look for multiple source note rows
    source_note_rows = re.findall(
        r'<tr class="gt_sourcenotes"><td class="gt_sourcenote"[^>]*>', html
    )
    assert len(source_note_rows) >= 3


def test_footnote_and_source_note_integration():
    import pandas as pd

    df = pd.DataFrame({"numbers": [100, 200], "text": ["Alpha", "Beta"]})

    # Create a comprehensive table with both footnotes and source notes
    gt_table = (
        GT(df)
        .tab_header(title="Integration Test: Footnotes and Source Notes")
        .tab_footnote("Number footnote", locations=loc.body(columns="numbers", rows=[0]))
        .tab_footnote("Text footnote", locations=loc.body(columns="text", rows=[1]))
        .tab_source_note("Data source: Example dataset")
        .tab_source_note("Analysis performed in 2025")
        .tab_options(source_notes_multiline=False)
    )

    html = gt_table._render_as_html()

    # Verify footnotes are applied with correct placement
    import re

    # Numbers should get left placement, text should get right placement
    assert re.search(r"<span[^>]*>1</span> 100", html), "Number footnote should be left-placed"
    assert re.search(r"Beta<span[^>]*>2</span>", html), "Text footnote should be right-placed"

    # Verify footnotes appear in footer
    assert "Number footnote" in html
    assert "Text footnote" in html

    # Verify source notes appear in footer in single line
    assert "Data source: Example dataset" in html
    assert "Analysis performed in 2025" in html

    # Check that both footnotes and source notes are in the footer section
    footer_match = re.search(r"<tfoot>(.*?)</tfoot>", html, re.DOTALL)
    assert footer_match

    # Footer should contain both source notes and footnotes
    footer_content = footer_match.group(1)
    assert "Data source: Example dataset" in footer_content
    assert "Number footnote" in footer_content
    assert "Text footnote" in footer_content


def test_create_footnote_mark_html_edge_cases():
    # Test that empty mark should return an empty string
    result = _create_footnote_mark_html(mark="")
    assert result == ""


def test_footnote_mark_string_edge_cases():
    # Test with empty GTData (no footnotes)
    empty_gt = GT(pl.DataFrame({"col": [1]}))
    footnote_info = FootnoteInfo(locname="body", rownum=0, colname="col", footnotes=["test"])

    # Should return mark "1" when no existing footnotes
    result = _get_footnote_mark_string(empty_gt._build_data("footnote_test"), footnote_info)
    assert result == "1"

    # Test with footnote_info having no footnotes
    footnote_info_empty = FootnoteInfo(locname="body", rownum=0, colname="col", footnotes=[])
    result = _get_footnote_mark_string(empty_gt._build_data("footnote_test"), footnote_info_empty)
    assert result == "1"


def test_get_column_index_edge_cases():
    df = pl.DataFrame({"col1": [1], "col2": [2], "col3": [3]})
    gt_table = GT(df)
    data = gt_table._build_data("test")

    # Test situation where colname is None or empty
    result = _get_column_index(data, None)
    assert result == 0

    result = _get_column_index(data, "")
    assert result == 0

    # Test situation where the column name is not found
    result = _get_column_index(data, "nonexistent_column")
    assert result == 0

    # Tests of normal cases where the column provided exists
    result = _get_column_index(data, "col1")
    assert result == 0

    result = _get_column_index(data, "col2")
    assert result == 1

    result = _get_column_index(data, "col3")
    assert result == 2


def test_get_spanner_leftmost_column_index_edge_cases():
    df = pl.DataFrame({"col1": [1], "col2": [2], "col3": [3]})
    gt_table = GT(df).tab_spanner(label="Test Spanner", columns=["col2", "col3"])
    data = gt_table._build_data("test")

    # Test case 1: `spanner_grpname` is None
    result = _get_spanner_leftmost_column_index(data, None)
    assert result == 0

    # Test case 2: `spanner_grpname` is empty string
    result = _get_spanner_leftmost_column_index(data, "")
    assert result == 0

    # Test case 3: `spanner_grpname` doesn't exist
    result = _get_spanner_leftmost_column_index(data, "Nonexistent Spanner")
    assert result == 0

    # Test normal case: existing spanner should return leftmost column index;
    # col2 is at index 1, col3 at index 2, so leftmost is 1
    result = _get_spanner_leftmost_column_index(data, "Test Spanner")
    assert result == 1
