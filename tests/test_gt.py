import pandas as pd
import pytest
from great_tables import GT


# Generate a gt Table object for assertion testing
data = [{"a": 5, "b": 15}, {"a": 15, "b": 2000}]
pd_data = pd.DataFrame(data)


@pytest.fixture
def gt_tbl():
    return GT(pd_data)


def test_gt_replace(gt_tbl: GT):
    new_gt_tbl = gt_tbl._replace(_has_built=True)

    assert new_gt_tbl._has_built


def test_gt_groupname_and_rowname_col_equal_raises():
    with pytest.raises(ValueError) as exc_info:
        GT(pd.DataFrame({"g": [1], "row": [1]}), rowname_col="g", groupname_col="g")

    assert "may not be set to the same column." in exc_info.value.args[0]


def test_gt_object_prerender(gt_tbl: GT):
    assert type(gt_tbl).__name__ == "GT"

    # Assert that certain private variables exist with a
    # GT object and that they have the expected names
    assert type(gt_tbl._boxhead).__name__ == "Boxhead"
    assert type(gt_tbl._stub).__name__ == "Stub"
    assert type(gt_tbl._spanners).__name__ == "Spanners"
    assert type(gt_tbl._heading).__name__ == "Heading"
    assert isinstance(gt_tbl._source_notes, list)
    assert isinstance(gt_tbl._footnotes, list)
    assert isinstance(gt_tbl._styles, list)
    assert type(gt_tbl._locale).__name__ == "Locale"


def test_gt_table_render(gt_tbl: GT):
    # Assert that a table render process will generate a string object
    assert type(gt_tbl.render(context="html")).__name__ == "str"

    assert (
        type(
            gt_tbl.tab_header(title="Title of Table", subtitle="The Subtitle").render(
                context="html"
            )
        ).__name__
        == "str"
    )

    assert type(gt_tbl.tab_source_note(source_note="Note").render(context="html")).__name__ == "str"

    assert (
        type(
            gt_tbl.tab_source_note(source_note="Note 1")
            .tab_source_note(source_note="Note 2")
            .render(context="html")
        ).__name__
        == "str"
    )
