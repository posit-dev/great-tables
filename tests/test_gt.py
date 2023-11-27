import pytest

from great_tables import GT
from great_tables._gt_data import RowGroups
import pandas as pd

# Generate a gt Table object for assertion testing
data = [{"a": 5, "b": 15}, {"a": 15, "b": 2000}]
pd_data = pd.DataFrame(data)


@pytest.fixture
def gt_tbl():
    return GT(pd_data)


def test_gt_replace(gt_tbl: GT):
    row_groups = ["x"]
    new_gt_tbl = gt_tbl._replace(_row_groups=row_groups)

    assert new_gt_tbl._row_groups is row_groups


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
    assert isinstance(gt_tbl._row_groups, list)
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
