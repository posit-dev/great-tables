from __future__ import annotations

from dataclasses import dataclass
from functools import singledispatch
from typing import Optional, Literal


# Cell Styles ==========================================================================
# TODO: stubbed out the styles in helpers.R as dataclasses while I was reading it,
# but have no worked on any runtime validation, etc..


# TODO: what goes into CellStyle?
@dataclass
class CellStyle:
    """A style specification."""


@dataclass
class CellStyleText:
    """A style specification for text."""

    color: str | None = None
    font: str | None = None
    size: str | None = None
    align: Literal["center", "left", "right", "justify"] | None = None
    # TODO: this can also be a gt_column object?
    v_align: Literal["middle", "top", "bottom"] | None = None
    style: Literal["normal", "italic", "oblique"] | None = None
    weight: Literal["normal", "bold", "bolder", "lighter"] | None = None
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
