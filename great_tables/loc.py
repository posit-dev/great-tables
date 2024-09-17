from __future__ import annotations

from ._locations import (
    # Header ----
    LocHeader as header,
    LocTitle as title,
    LocSubTitle as subtitle,
    #
    # Stubhead ----
    LocStubhead as stubhead,
    LocStubheadLabel as stubhead_label,
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
    LocSummaryLabel as summary_label,
    #
    # Body ----
    LocBody as body,
    LocSummary as summary,
    #
    # Footer ----
    LocFooter as footer,
    LocFootnotes as footnotes,
    LocSourceNotes as source_notes,
)

__all__ = (
    "header",
    "title",
    "subtitle",
    "stubhead",
    "stubhead_label",
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
