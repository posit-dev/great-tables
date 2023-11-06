from __future__ import annotations

from dataclasses import dataclass, fields
from functools import singledispatch
from typing import TYPE_CHECKING, Literal, get_origin, get_type_hints

# note that types like Spanners are only used in annotations for concretes of the
# resolve generic, but we need to import at runtime, due to singledispatch looking
# up annotations
from ._gt_data import GTData, Spanners


# Locations ============================================================================
# TODO: these are called cells_* in gt. I prefixed them with Loc just to keep things
# straight while going through helpers.R, but no strong opinion on naming!


@dataclass
class Loc:
    """A location."""


@dataclass
class LocTitle(Loc):
    """A location for targeting the table title and subtitle."""

    groups: Literal["title", "subtitle"]


@dataclass
class LocStubhead(Loc):
    groups: Literal["stubhead"] = "stubhead"


@dataclass
class LocColumnSpanners(Loc):
    """A location for column spanners."""

    # TODO: these can also be tidy selectors
    ids: list[str]


@dataclass
class LocColumnLabels(Loc):
    # TODO: these can be tidyselectors
    columns: list[str]


@dataclass
class LocRowGroups(Loc):
    # TODO: these can be tidyselectors
    groups: list[str]


@dataclass
class LocStub(Loc):
    # TODO: these can be tidyselectors
    # TODO: can this take integers?
    rows: list[str]


@dataclass
class LocBody(Loc):
    # TODO: these can be tidyselectors
    columns: list[str]
    rows: list[str]


@dataclass
class LocSummary(Loc):
    # TODO: these can be tidyselectors
    groups: list[str]
    columns: list[str]
    rows: list[str]


@dataclass
class LocGrandSummary(Loc):
    # TODO: these can be tidyselectors
    columns: list[str]
    rows: list[str]


@dataclass
class LocStubSummary(Loc):
    # TODO: these can be tidyselectors
    groups: list[str]
    rows: list[str]


@dataclass
class LocStubGrandSummary(Loc):
    rows: list[str]


@dataclass
class LocFootnotes(Loc):
    groups: Literal["footnotes"] = "footnotes"


@dataclass
class LocSourceNotes(Loc):
    # This dataclass in R has a `groups` field, which is a literal value.
    # In python, we can use an isinstance check to determine we're seeing an
    # instance of this class
    groups: Literal["source_notes"] = "source_notes"


# Utils ================================================================================


def resolve_vector_i(expr: list[str], candidates: list[str], item_label: str) -> list[int]:
    """Return list of indices for candidates, selected by expr."""

    mask = resolve_vector_l(expr, candidates, item_label)
    return [ii for ii, val in enumerate(mask) if val]


def resolve_vector_l(expr: list[str], candidates: list[str], item_label: str) -> list[bool]:
    """Return list of logical index for candidates, selected by expr."""

    if not (isinstance(expr, list) and all(isinstance(x, str) for x in expr)):
        raise NotImplementedError("Selecting entries currently requires a list of strings.")

    set_expr = set(expr)
    if set_expr - set(candidates):
        missing = set_expr - set(candidates)
        raise ValueError(f"Cannot find these entries: {missing}")

    return [candidate in set_expr for candidate in candidates]


# Resolve generic ======================================================================


@singledispatch
def resolve(loc: Loc, *args, **kwargs) -> Loc:
    """Return a copy of location with lookups resolved (e.g. tidyselect on columns)."""
    raise NotImplementedError(f"Unsupported location type: {type(loc)}")


@resolve.register
def _(loc: LocColumnSpanners, spanners: Spanners) -> LocColumnSpanners:
    # unique labels (with order preserved)
    spanner_ids = [span.spanner_id for span in spanners]

    resolved_spanners_idx = resolve_vector_i(loc.ids, spanner_ids, item_label="spanner")
    resolved_spanners = [spanner_ids[idx] for idx in resolved_spanners_idx]

    # Create a list object
    return LocColumnSpanners(ids=resolved_spanners)
