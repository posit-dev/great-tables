import pandas as pd
import polars as pl
import pytest
from great_tables import GT, exibble, html, loc, md, style
from great_tables._utils_render_html import (
    create_body_component_h,
    create_columns_component_h,
    create_heading_component_h,
    create_source_notes_component_h,
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


def test_row_group_as_column_with_rowname(snapshot):
    df = pd.DataFrame({"g": ["A", "A", "B"], "x": ["0", "1", "2"], "y": [22, 33, 44]})

    new_gt = GT(df, groupname_col="g", rowname_col="x").tab_options(
        row_group_as_column=True,
    )

    assert_rendered_body(snapshot, new_gt)


def test_row_group_as_column_without_rowname(snapshot):
    df = pd.DataFrame({"g": ["A", "A", "B"], "x": ["0", "1", "2"], "y": [22, 33, 44]})

    new_gt = GT(df, groupname_col="g").tab_options(
        row_group_as_column=True,
    )

    assert_rendered_body(snapshot, new_gt)


def test_groupname_with_no_rowname(snapshot):
    df = pd.DataFrame({"g": ["A", "B"], "x": ["0", "1"], "y": ["22", "33"]})

    new_gt = GT(df, groupname_col="g")

    assert_rendered_body(snapshot, new_gt)


def test_body_multiple_locations(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style=style.fill(color="red"),
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
    new_gt = GT(small_exibble).tab_style(
        style=style.text(color="red"),
        locations=loc.body(),
    )

    assert_rendered_body(snapshot, new_gt)


def test_styling_data_02(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style=style.text(color="red"),
        locations=loc.body(columns=["char"]),
    )

    assert_rendered_body(snapshot, new_gt)


def test_styling_data_03(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style=style.text(color="red"),
        locations=loc.body(columns="char", rows=[0, 2]),
    )

    assert_rendered_body(snapshot, new_gt)


def test_styling_data_04(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style=style.text(color="red"),
        locations=loc.body(columns=[], rows=[0, 2]),
    )

    assert_rendered_body(snapshot, new_gt)


def test_styling_data_05(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style=style.text(color="red"),
        locations=loc.body(columns="char", rows=[]),
    )

    assert_rendered_body(snapshot, new_gt)


def test_styling_data_06(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style=style.text(color="red"),
        locations=loc.body(columns=[], rows=[]),
    )

    assert_rendered_body(snapshot, new_gt)


def test_styling_data_07(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style=style.borders(sides="left"),
        locations=loc.body(columns="char", rows=[0, 2]),
    )

    assert_rendered_body(snapshot, new_gt)


def test_styling_data_08(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style=style.borders(sides=["left"]),
        locations=loc.body(columns="char", rows=[0, 2]),
    )

    assert_rendered_body(snapshot, new_gt)


def test_styling_data_09(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style=style.borders(sides=["left", "right"]),
        locations=loc.body(columns="char", rows=[0, 2]),
    )

    assert_rendered_body(snapshot, new_gt)


def test_styling_data_10(snapshot):
    new_gt = GT(small_exibble).tab_style(
        style=style.borders(sides="all"),
        locations=loc.body(columns="char", rows=[0, 2]),
    )

    assert_rendered_body(snapshot, new_gt)


def test_render_polars_list_col(snapshot):
    gt = GT(pl.DataFrame({"x": [[1, 2]]}))

    assert_rendered_body(snapshot, gt)


def test_multiple_spanners_pads_for_stubhead_label(snapshot):
    # NOTE: see test_spanners.test_multiple_spanners_above_one
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


# Location style rendering -------------------------------------------------------------------------
# these tests focus on location classes being correctly picked up
def test_loc_column_labels():
    gt = GT(pl.DataFrame({"x": [1], "y": [2]}))

    new_gt = gt.tab_style(style.fill("yellow"), loc.column_labels(columns=["x"]))
    el = create_columns_component_h(new_gt._build_data("html"))

    assert el.name == "tr"
    assert el.children[0].attrs["style"] == "background-color: yellow;"
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
        # Columns -----------
        .tab_style(style.css("COLUMN_LABEL"), loc.column_labels(columns="num"))
        .tab_style(style.css("COLUMN_HEADER"), loc.column_header())
        .tab_style(style.css("SPANNER_LABEL"), loc.spanner_labels(ids=["spanner"]))
        # Header -----------
        .tab_style(style.css("HEADER"), loc.header())
        .tab_style(style.css("SUBTITLE"), loc.subtitle())
        .tab_style(style.css("TITLE"), loc.title())
        # Footer -----------
        .tab_style(style.css("FOOTER"), loc.footer())
        .tab_style(style.css("SOURCE_NOTES"), loc.source_notes())
        # .tab_style(style.css("AAA"), loc.footnotes())
        # Stub --------------
        .tab_style(style.css("GROUP_LABEL"), loc.row_groups())
        .tab_style(style.css("STUB"), loc.stub())
        .tab_style(style.css("ROW_LABEL"), loc.stub(rows=[0]))
        .tab_style(style.css("STUBHEAD"), loc.stubhead())
    )

    html = new_gt.as_raw_html()
    cleaned = html[html.index("<table") :]
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


def test_source_notes_non_multiline():
    gt = (
        GT(small_exibble)
        .tab_source_note("Note A")
        .tab_source_note("Note B")
        .tab_options(source_notes_multiline=False, source_notes_sep=" | ")
    )
    built = gt._build_data("html")
    html_out = create_source_notes_component_h(built)

    assert "Note A" in html_out
    assert "Note B" in html_out
    assert " | " in html_out
    assert "<tfoot>" in html_out
    assert "<tr class=" not in html_out.replace('<tr class="gt_sourcenotes">', "")


def test_generate_footnote_mark_numbers():
    from great_tables._utils_render_html import _generate_footnote_mark

    assert _generate_footnote_mark(1, "numbers") == "1"
    assert _generate_footnote_mark(5, "numbers") == "5"


def test_generate_footnote_mark_letters():
    from great_tables._utils_render_html import _generate_footnote_mark

    result = _generate_footnote_mark(1, "letters")

    assert len(result) >= 1


def test_generate_footnote_mark_standard_symbols():
    from great_tables._utils_render_html import _generate_footnote_mark

    result = _generate_footnote_mark(1, "standard")

    assert result == "*"

    result2 = _generate_footnote_mark(2, "standard")

    assert result2 == "†"


def test_generate_footnote_mark_unknown_type_returns_number():
    from great_tables._utils_render_html import _generate_footnote_mark

    result = _generate_footnote_mark(3, "bogus_type")

    assert result == "3"


def test_generate_footnote_mark_list_type():
    from great_tables._utils_render_html import _generate_footnote_mark

    result = _generate_footnote_mark(1, ["A", "B", "C"])

    assert result == "A"

    result2 = _generate_footnote_mark(4, ["A", "B", "C"])

    assert result2 == "AA"


def test_create_footnote_mark_html_empty_mark():
    from great_tables._utils_render_html import _create_footnote_mark_html

    result = _create_footnote_mark_html("")

    assert result == ""


def test_create_footnote_mark_html_with_mark():
    from great_tables._utils_render_html import _create_footnote_mark_html

    result = _create_footnote_mark_html("*")

    assert "gt_footnote_marks" in result
    assert "*" in result


def test_apply_footnote_placement_left():
    from great_tables._utils_render_html import _apply_footnote_placement
    from great_tables._gt_data import FootnotePlacement

    result = _apply_footnote_placement("text", "<mark>", FootnotePlacement.left)

    assert result == "<mark> text"


def test_apply_footnote_placement_right():
    from great_tables._utils_render_html import _apply_footnote_placement
    from great_tables._gt_data import FootnotePlacement

    result = _apply_footnote_placement("text", "<mark>", FootnotePlacement.right)

    assert result == "text<mark>"


def test_apply_footnote_placement_auto_numeric():
    from great_tables._utils_render_html import _apply_footnote_placement

    result = _apply_footnote_placement("42.5", "<mark>", None)

    assert result.startswith("<mark>")


def test_apply_footnote_placement_auto_text():
    from great_tables._utils_render_html import _apply_footnote_placement

    result = _apply_footnote_placement("hello world", "<mark>", None)

    assert result.endswith("<mark>")


def test_is_numeric_content_number():
    from great_tables._utils_render_html import _is_numeric_content

    assert _is_numeric_content("23") is True
    assert _is_numeric_content("3.14") is True


def test_is_numeric_content_text():
    from great_tables._utils_render_html import _is_numeric_content

    assert _is_numeric_content("hello") is False


def test_is_numeric_content_empty():
    from great_tables._utils_render_html import _is_numeric_content

    assert _is_numeric_content("") is False
    assert _is_numeric_content("   ") is False


def test_get_footnote_marks_option_default():
    from great_tables._utils_render_html import _get_footnote_marks_option

    gt = GT(small_exibble)
    built = gt._build_data("html")
    result = _get_footnote_marks_option(built)
    assert result is not None


def test_get_spanners_matrix_height():
    from great_tables._utils_render_html import _get_spanners_matrix_height

    gt = GT(small_exibble)
    built = gt._build_data("html")
    height = _get_spanners_matrix_height(built)

    assert isinstance(height, int)
    assert height >= 1


def test_get_footnote_marks_option_fallback_no_options():
    from great_tables._utils_render_html import _get_footnote_marks_option

    # Test the fallback `return "numbers"` path when data has no _options attribute
    class FakeData:
        pass

    result = _get_footnote_marks_option(FakeData())

    assert result == "numbers"


def test_get_footnote_marks_option_fallback_none_value():
    from great_tables._utils_render_html import _get_footnote_marks_option
    from unittest.mock import MagicMock

    # Test the fallback when marks_value is None
    mock_option = MagicMock()
    mock_option.value = None
    mock_options = MagicMock()
    mock_options.footnotes_marks = mock_option
    mock_data = MagicMock()
    mock_data._options = mock_options
    result = _get_footnote_marks_option(mock_data)

    assert result == "numbers"


def test_get_column_index_invalid_column():
    from great_tables._utils_render_html import _get_column_index

    gt = GT(small_exibble)
    built = gt._build_data("html")

    # Column not found returns 0
    result = _get_column_index(built, "nonexistent_column")

    assert result == 0


def test_get_column_index_no_colname():
    from great_tables._utils_render_html import _get_column_index

    gt = GT(small_exibble)
    built = gt._build_data("html")
    result = _get_column_index(built, None)

    assert result == 0


def test_source_notes_empty_returns_empty_string():
    from great_tables._utils_render_html import create_source_notes_component_h

    gt = GT(small_exibble)  # no source notes
    built = gt._build_data("html")
    result = create_source_notes_component_h(built)

    assert result == ""


def test_footer_empty_returns_empty_string():
    from great_tables._utils_render_html import create_footer_component_h

    gt = GT(small_exibble)  # no source notes or footnotes
    built = gt._build_data("html")
    result = create_footer_component_h(built)

    assert result == ""


def test_get_table_defs_percentage_widths():
    from great_tables._utils_render_html import _get_table_defs

    gt = GT(small_exibble).cols_width(cases={"num": "50%", "char": "50%"})
    built = gt._build_data("html")
    result = _get_table_defs(built)

    # table_width should be set to "100%" when all columns use % widths and table_width is "auto"
    assert result["table_style"] is not None
    assert "100%" in result["table_style"]


def test_heading_subtitle_without_title_raises():
    # ValueError when subtitle is provided without a title
    from great_tables._utils_render_html import create_heading_component_h
    import great_tables._gt_data as gt_data

    gt = GT(small_exibble)
    built = gt._build_data("html")

    # Use GTData._replace() helper to swap in a heading that has subtitle but no title
    heading_no_title = gt_data.Heading(title=None, subtitle="a subtitle")
    built_modified = built._replace(_heading=heading_no_title)
    with pytest.raises(ValueError, match="subtitle was provided without a title"):
        create_heading_component_h(built_modified)


def test_column_labels_hidden_returns_empty_string():
    # Return "" when column_labels_hidden option is True
    from great_tables._utils_render_html import create_columns_component_h

    gt = GT(small_exibble).tab_options(column_labels_hidden=True)
    built = gt._build_data("html")
    result = create_columns_component_h(built)

    assert result == ""


def test_spanner_covering_all_columns_else_branch():
    from great_tables._utils_render_html import create_columns_component_h
    import polars as pl

    df = pl.DataFrame({"a": [1, 2], "b": [3, 4]})
    gt = GT(df).tab_spanner("All", ["a", "b"])
    built = gt._build_data("html")
    result = create_columns_component_h(built)

    assert result is not None
    assert "All" in str(result)
