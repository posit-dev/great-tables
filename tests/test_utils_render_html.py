from typing import Union

import re

from great_tables import GT, exibble, md, html
from great_tables._utils_render_html import create_source_notes_component_h
from great_tables._source_notes import tab_source_note


def assert_rendered_source_notes(snapshot, gt):
    built = gt._build_data("html")
    source_notes = create_source_notes_component_h(built)

    assert snapshot == source_notes


def test_format_snap(snapshot):
    new_gt = (
        GT(exibble)
        .tab_source_note(md("An **important** note."))
        .tab_source_note(md("Another *important* note."))
        .tab_source_note("A plain note.")
        .tab_source_note(html("An <strong>HTML heavy</strong> note."))
    )

    assert_rendered_source_notes(snapshot, new_gt)
