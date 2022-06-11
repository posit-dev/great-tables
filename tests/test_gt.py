from gt import *
import pandas as pd

# Generate a GT Table object for assertion testing
data = [{"a": 5, "b": 15}, {"a": 15, "b": 2000}]
pd_data = pd.DataFrame(data)
gt_tbl = gt.GT(pd_data)


def test_gt_object_prerender():

    assert type(gt_tbl).__name__ == "GT"

    # Assert that certain private variables exist with a
    # GT object and that they have the expected names
    assert type(gt_tbl._boxhead).__name__ == "Boxhead"
    assert type(gt_tbl._stub).__name__ == "Stub"
    assert type(gt_tbl._row_groups).__name__ == "RowGroups"
    assert type(gt_tbl._spanners).__name__ == "Spanners"
    assert type(gt_tbl._heading).__name__ == "Heading"
    assert type(gt_tbl._stubhead).__name__ == "Stubhead"
    assert type(gt_tbl._source_notes).__name__ == "SourceNotes"
    assert type(gt_tbl._footnotes).__name__ == "Footnotes"
    assert type(gt_tbl._styles).__name__ == "Styles"
    assert type(gt_tbl._locale).__name__ == "Locale"


def test_gt_table_render():

    # Assert that a table render process will generate a string object
    assert type(gt_tbl.render()).__name__ == "str"

    assert (
        type(
            gt_tbl.tab_header(title="Title of Table", subtitle="The Subtitle").render()
        ).__name__
        == "str"
    )

    assert type(gt_tbl.tab_source_note(source_note="Note").render()).__name__ == "str"

    assert (
        type(
            gt_tbl.tab_source_note(source_note="Note 1")
            .tab_source_note(source_note="Note 2")
            .render()
        ).__name__
        == "str"
    )
