import pandas as pd
import polars as pl
import pytest
from great_tables import (
    GT,
    exibble,
    html,
    loc,
    md,
    style,
)
from great_tables._utils_render_html import (
    create_body_component_h,
    create_columns_component_h,
    create_heading_component_h,
    create_source_notes_component_h,
    rtl_modern_unicode_charset,
)
from htmltools import (
    TagList,
)

small_exibble = exibble[["num", "char"]].head(3)


def assert_rendered_source_notes(snapshot, gt):
    built = gt._build_data("html")
    source_notes = create_source_notes_component_h(built)
    assert snapshot == source_notes


def assert_rendered_heading(snapshot, gt):
    built = gt._build_data("html")
    heading = create_heading_component_h(built)
    assert snapshot == heading


def assert_rendered_columns(snapshot, gt):
    built = gt._build_data("html")
    columns = create_columns_component_h(built)
    assert snapshot == str(columns)


def assert_rendered_body(snapshot, gt):
    built = gt._build_data("html")
    body = create_body_component_h(built)
    assert snapshot == body


def test_source_notes_snap(snapshot):
    new_gt = (
        GT(exibble)
        .tab_source_note(md("An **important** note."))
        .tab_source_note(md("Another *important* note."))
        .tab_source_note("A plain note.")
        .tab_source_note(html("An <strong>HTML heavy</strong> note."))
    )
    assert_rendered_source_notes(snapshot, new_gt)


def test_render_groups_reordered(snapshot):
    df = pd.DataFrame(
        {"row": [0, 1, 2, 3], "g": ["A", "B", "A", "B"], "x": ["00", "11", "22", "33"]}
    )
    new_gt = GT(df, rowname_col="row", groupname_col="g")
    assert_rendered_body(snapshot, new_gt)


def test_body_multiple_locations(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style.fill(color="red"),
        locations=[
            loc.body(columns="num", rows=[0, 2]),
            loc.body(columns="char", rows=[1]),
        ],
    )
    assert_rendered_body(snapshot, new_gt)


def test_body_multiple_styles(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style=[style.fill(color="red"), style.borders("left")],
        locations=loc.body(columns="num", rows=[0]),
    )
    assert_rendered_body(snapshot, new_gt)


def test_styling_data_01(snapshot):
    new_gt = GT(small_exibble).tab_style(style.text(color="red"), locations=loc.body())
    assert_rendered_body(snapshot, new_gt)


def test_styling_data_02(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style.text(color="red"), locations=loc.body(columns=["char"])
    )
    assert_rendered_body(snapshot, new_gt)


def test_styling_data_03(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style.text(color="red"), locations=loc.body(columns="char", rows=[0, 2])
    )
    assert_rendered_body(snapshot, new_gt)


def test_styling_data_04(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style.text(color="red"), locations=loc.body(columns=[], rows=[0, 2])
    )
    assert_rendered_body(snapshot, new_gt)


def test_styling_data_05(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style.text(color="red"), locations=loc.body(columns="char", rows=[])
    )
    assert_rendered_body(snapshot, new_gt)


def test_styling_data_06(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style.text(color="red"), locations=loc.body(columns=[], rows=[])
    )
    assert_rendered_body(snapshot, new_gt)


def test_styling_data_07(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style.borders(sides="left"), locations=loc.body(columns="char", rows=[0, 2])
    )
    assert_rendered_body(snapshot, new_gt)


def test_styling_data_08(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style.borders(sides=["left"]), locations=loc.body(columns="char", rows=[0, 2])
    )
    assert_rendered_body(snapshot, new_gt)


def test_styling_data_09(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style.borders(sides=["left", "right"]),
        locations=loc.body(columns="char", rows=[0, 2]),
    )
    assert_rendered_body(snapshot, new_gt)


def test_styling_data_10(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style.borders(sides="all"), locations=loc.body(columns="char", rows=[0, 2])
    )
    assert_rendered_body(snapshot, new_gt)


def test_render_polars_list_col(snapshot):
    gt = GT(pl.DataFrame({"x": [[1, 2]]}))
    assert_rendered_body(snapshot, gt)


def test_multiple_spanners_pads_for_stubhead_label(snapshot):
    gt = (
        GT(exibble, rowname_col="row", groupname_col="group")
        .tab_spanner("A", ["num", "char", "fctr"])
        .tab_spanner("B", ["fctr"])
        .tab_spanner("C", ["num", "char"])
        .tab_spanner("D", ["fctr", "date", "time"])
        .tab_spanner("E", spanners=["B", "C"])
        .tab_stubhead(label="Group")
    )
    assert_rendered_columns(snapshot, gt)


def test_loc_column_labels():
    """Test that column label styling applied via loc.column_labels works correctly."""
    gt = GT(pl.DataFrame({"x": [1], "y": [2]}))
    new_gt = gt.tab_style(style.fill("yellow"), loc.column_labels(columns=["x"]))
    el = create_columns_component_h(new_gt._build_data("html"))
    if not hasattr(el, "name") and isinstance(el, (list, TagList)):
        for item in el:
            if hasattr(item, "name") and item.name == "tr":
                el = item
                break
    assert hasattr(el, "name"), "Returned element does not have a 'name' attribute"
    assert el.name == "tr"
    assert "style" in el.children[0].attrs, "Expected style attribute in first child"
    style_val = el.children[0].attrs["style"].strip()
    assert (
        style_val == "background-color: yellow;"
    ), f"Expected 'background-color: yellow;', got '{style_val}'"
    assert "style" not in el.children[1].attrs


def test_loc_kitchen_sink(snapshot):
    gt = (
        GT(exibble.loc[[0], ["num", "char", "fctr", "row", "group"]])
        .tab_header("title", "subtitle")
        .tab_stub(rowname_col="row", groupname_col="group")
        .tab_source_note("yo")
        .tab_spanner("spanner", ["char", "fctr"])
        .tab_stubhead("stubhead")
    )
    new_gt = (
        gt.tab_style(style.css("BODY"), loc.body())
        .tab_style(style.css("COLUMN_LABEL"), loc.column_labels(columns="num"))
        .tab_style(style.css("COLUMN_HEADER"), loc.column_header())
        .tab_style(style.css("SPANNER_LABEL"), loc.spanner_labels(ids=["spanner"]))
        .tab_style(style.css("HEADER"), loc.header())
        .tab_style(style.css("SUBTITLE"), loc.subtitle())
        .tab_style(style.css("TITLE"), loc.title())
        .tab_style(style.css("FOOTER"), loc.footer())
        .tab_style(style.css("SOURCE_NOTES"), loc.source_notes())
        .tab_style(style.css("GROUP_LABEL"), loc.row_groups())
        .tab_style(style.css("STUB"), loc.stub())
        .tab_style(style.css("ROW_LABEL"), loc.stub(rows=[0]))
        .tab_style(style.css("STUBHEAD"), loc.stubhead())
    )
    html_output = new_gt.as_raw_html()
    cleaned = html_output[html_output.index("<table") :]
    assert cleaned == snapshot


def test_table_id_used_in_headers(snapshot):
    new_gt = GT(
        pl.DataFrame(
            {
                "Count": [1, 2, 3, 4],
                "Group Label": ["label a", "label b", "label c", "label d"],
            }
        )
    ).with_id("test_id")
    assert_rendered_columns(snapshot, new_gt)


def test_rtl_modern_unicode_charset():
    """
    Test that rtl_modern_unicode_charset returns a regex pattern that includes
    the expected Unicode ranges for RTL scripts (Hebrew, Arabic, etc.).
    """
    pattern = rtl_modern_unicode_charset()
    assert "[\\u0590-\\u05FF]" in pattern, "Hebrew Unicode range not found in pattern."
    assert "[\\u0600-\\u06FF]" in pattern, "Arabic Unicode range not found in pattern."
    assert "[\\u0700-\\u074F]" in pattern, "Syriac Unicode range not found in pattern."
    assert "[\\u0780-\\u07BF]" in pattern, "Thaana Unicode range not found in pattern."
    assert (
        "[\\u0800-\\u083F]" in pattern
    ), "Samaritan Unicode range not found in pattern."
    assert "[\\u0840-\\u085F]" in pattern, "Mandaic Unicode range not found in pattern."
