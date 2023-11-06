from __future__ import annotations

from ._gt_data import GTData
from ._locations import Loc

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
