from __future__ import annotations

from ._locations import (
    # Header ----
    LocHeader as header,
    LocTitle as title,
    LocSubTitle as subtitle,
    #
    # Stubhead ----
    LocStubhead as stubhead,
    #
    # Column Labels ----
    LocColumnHeader as column_header,
    LocSpannerLabels as spanner_labels,
    LocColumnLabels as column_labels,
    #
    # Stub ----
    LocStub as stub,
    LocRowGroups as row_groups,
    #
    # Body ----
    LocBody as body,
    #
    # Footer ----
    LocFooter as footer,
    LocSourceNotes as source_notes,
)

__all__ = (
    "header",
    "title",
    "subtitle",
    "stubhead",
    "column_header",
    "spanner_labels",
    "column_labels",
    "stub",
    "row_groups",
    "body",
    "footer",
    "source_notes",
)
