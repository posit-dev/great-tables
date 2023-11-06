from __future__ import annotations

from ._gt_data import GTData

from dataclasses import dataclass
from typing import Optional, Literal


# Cell Styles ==========================================================================
# TODO: stubbed out the styles in helpers.R as dataclasses while I was reading it,
# but have no worked on any runtime validation, etc..


@dataclass
class CellStyle:
    """A style specification."""


@dataclass
class CellText:
    """A style specification for text."""

    color: str
    font: str
    size: str
    align: Literal["center", "left", "right", "justify"]
    # TODO: this can also be a gt_column object?
    v_align: Literal["middle", "top", "bottom"]
    style: Literal["normal", "italic", "oblique"]
    weight: Literal["normal", "bold", "bolder", "lighter"]
    stretch: Literal[
        "normal",
        "condensed",
        "ultra-condensed",
        "extra-condensed",
        "semi-condensed",
        "semi-expanded",
        "expanded",
        "extra-expanded",
        "ultra-expanded",
    ]
    decorate: Literal["overline", "line-through", "underline", "underline overline"]
    transform: Literal["uppercase", "lowercase", "capitalize"]
    whitespace: Literal["normal", "nowrap", "pre", "pre-wrap", "pre-line", "break-spaces"]


@dataclass
class CellStyleFill(CellStyle):
    """A style specification for fill."""

    fill: str
    alpha: Optional[float] = None


@dataclass
class CellStyleBorders(CellStyle):
    sides: Literal["all", "top", "bottom", "left", "right"]
    color: str
    style: str
    # TODO: this can include objects like px(1)
    weight: str


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


def tab_style(data: GTData, style: list[CellStyle] | CellStyle, locations: Loc):
    """Add custom style to one or more cells

    Parameters
    ----------
    style:
        A style specification.
    location:
        A location on the table.
    """

    raise NotImplementedError()
