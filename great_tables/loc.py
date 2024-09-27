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
    LocRowGroupLabel as row_group_label,
    # TODO: remove for now
    LocSummaryLabel as summary_label,
    #
    # Body ----
    LocBody as body,
    # TODO: remove for now
    LocSummary as summary,
    #
    # Footer ----
    LocFooter as footer,
    # TODO: remove for now
    LocFootnotes as footnotes,
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
    "row_group_label",
    "summary_label",
    "body",
    "summary",
    "footer",
    "footnotes",
    "source_notes",
)
