from __future__ import annotations

from dataclasses import dataclass
from functools import singledispatch
from typing import Optional, Literal


# Cell Styles ==========================================================================
# TODO: stubbed out the styles in helpers.R as dataclasses while I was reading it,
# but have no worked on any runtime validation, etc..


# TODO: what goes into CellStyle?
class CellStyle:
    """A style specification."""

    def _to_html_style(self) -> str:
        raise NotImplementedError


@dataclass
class CellStyleText(CellStyle):
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
    ] | None = None
    decorate: Literal["overline", "line-through", "underline", "underline overline"] | None = None
    transform: Literal["uppercase", "lowercase", "capitalize"] | None = None
    whitespace: Literal[
        "normal", "nowrap", "pre", "pre-wrap", "pre-line", "break-spaces"
    ] | None = None

    def _to_html_style(self) -> str:
        rendered = f""

        if self.color:
            rendered = rendered.join(f"color: {self.color};")
        if self.font:
            rendered = rendered.join(f"font-family: {self.font};")
        if self.size:
            rendered = rendered.join(f"font-size: {self.size};")

        return rendered


@dataclass
class CellStyleFill(CellStyle):
    """A style specification for the background fill of targeted cells."""

    color: str
    alpha: Optional[float] = None

    def _to_html_style(self) -> str:
        return f"background-color: {self.color};"


@dataclass
class CellStyleBorders(CellStyle):
    sides: Literal["all", "top", "bottom", "left", "right"]
    color: str
    style: str
    # TODO: this can include objects like px(1)
    weight: str
