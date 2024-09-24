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
    LocColumnLabels as column_labels,
    LocSpannerLabel as spanner_label,
    LocColumnLabel as column_label,
    #
    # Stub ----
    LocStub as stub,
    LocRowGroupLabel as row_group_label,
    LocRowLabel as row_label,
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
    "column_labels",
    "spanner_label",
    "column_label",
    "stub",
    "row_group_label",
    "row_label",
    "summary_label",
    "body",
    "summary",
    "footer",
    "footnotes",
    "source_notes",
)
