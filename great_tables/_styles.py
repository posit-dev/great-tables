from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Literal, List


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
    """A style specification for cell text.

    The `style.text()` class is to be used with the `tab_style()` method, which itself allows for
    the setting of custom styles to one or more cells. With it, you can specify the color of the
    text, the font family, the font size, and the horizontal and vertical alignment of the text and
    more.

    Parameters
    ----------
    color : str | None
        The text color can be modified through the `color` argument.
    font : str | None
        The font or collection of fonts (subsequent font names are) used as fallbacks.
    size : str | None
        The size of the font. Can be provided as a number that is assumed to represent `px` values
        (or could be wrapped in the `px()` helper function). We can also use one of the following
        absolute size keywords: `"xx-small"`, `"x-small"`, `"small"`, `"medium"`, `"large"`,
        `"x-large"`, or `"xx-large"`.
    align : Literal["center", "left", "right", "justify"] | None
        The text in a cell can be horizontally aligned though one of the following options:
        `"center"`, `"left"`, `"right"`, or `"justify"`.
    v_align : Literal["middle", "top", "bottom"] | None
        The vertical alignment of the text in the cell can be modified through the options
        `"middle"`, `"top"`, or `"bottom"`.
    style : Literal["normal", "italic", "oblique"] | None
        Can be one of either `"normal"`, `"italic"`, or `"oblique"`.
    weight : Literal["normal", "bold", "bolder", "lighter"] | None)
        The weight of the font can be modified thorough a text-based option such as `"normal"`,
        `"bold"`, `"lighter"`, `"bolder"`, or, a numeric value between `1` and `1000`, inclusive.
        Note that only variable fonts may support the numeric mapping of weight.
    stretch : Literal["normal", "condensed", "ultra-condensed", "extra-condensed", "semi-condensed", "semi-expanded", "expanded", "extra-expanded", "ultra-expanded"] | None
        Allows for text to either be condensed or expanded. We can use one of the following
        text-based keywords to describe the degree of condensation/expansion: `"ultra-condensed"`,
        `"extra-condensed"`, `"condensed"`, `"semi-condensed"`, `"normal"`, `"semi-expanded"`,
        `"expanded"`, `"extra-expanded"`, or `"ultra-expanded"`. Alternatively, we can supply
        percentage values from `0%` to `200%`, inclusive. Negative percentage values are not
        allowed.
    decorate : Literal["overline", "line-through", "underline", "underline overline"] | None
        Allows for text decoration effect to be applied. Here, we can use `"overline"`,
        `"line-through"`, or `"underline"`.
    transform : Literal["uppercase", "lowercase", "capitalize"] | None
        Allows for the transformation of text. Options are `"uppercase"`, `"lowercase"`, or
        `"capitalize"`.
    whitespace : Literal["normal", "nowrap", "pre", "pre-wrap", "pre-line", "break-spaces"] | None
        A white-space preservation option. By default, runs of white-space will be collapsed into
        single spaces but several options exist to govern how white-space is collapsed and how lines
        might wrap at soft-wrap opportunities. The options are `"normal"`, `"nowrap"`, `"pre"`,
        `"pre-wrap"`, `"pre-line"`, and `"break-spaces"`.

    Returns
    -------
    CellStyleText
        A CellStyleText object, which is used for a `styles` argument if specifying any cell text
        properties.
    """

    color: str | None = None
    font: str | None = None
    size: str | None = None
    align: Literal["center", "left", "right", "justify"] | None = None
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
        rendered = ""

        if self.color:
            rendered += f"color: {self.color};"
        if self.font:
            rendered += f"font-family: {self.font};"
        if self.size:
            rendered += f"font-size: {self.size};"
        if self.align:
            rendered += f"text-align: {self.align};"
        if self.v_align:
            rendered += f"vertical-align: {self.v_align};"
        if self.style:
            rendered += f"font-style: {self.style};"
        if self.weight:
            rendered += f"font-weight: {self.weight};"
        if self.stretch:
            rendered += f"font-stretch: {self.stretch};"
        if self.decorate:
            rendered += f"text-decoration: {self.decorate};"
        if self.transform:
            rendered += f"text-transform: {self.transform};"
        if self.whitespace:
            rendered += f"white-space: {self.whitespace};"

        return rendered


@dataclass
class CellStyleFill(CellStyle):
    """A style specification for the background fill of targeted cells.

    The `style.fill()` class is to be used with the `tab_style()` method, which itself allows for
    the setting of custom styles to one or more cells. Specifically, the call to `style.fill()`
    should be bound to the `styles` argument of `tab_style()`.

    Parameters
    ----------
    color : str
        The color to use for the cell background fill. This can be any valid CSS color value, such
        as a hex code, a named color, or an RGB value.

    Returns
    -------
    CellStyleFill
        A CellStyleFill object, which is used for a `styles` argument if specifying a cell fill
        value.
    """

    color: str
    # alpha: Optional[float] = None

    def _to_html_style(self) -> str:
        return f"background-color: {self.color};"


@dataclass
class CellStyleBorders(CellStyle):
    sides: Literal["all", "top", "bottom", "left", "right"]
    color: str = "#000000"
    style: str = "solid"
    # TODO: this can include objects like px(1)
    weight: str = "1px"
    """A style specification for cell borders.

    The `styles.borders()` class is to be used with the `tab_style()` method, which itself allows
    for the setting of custom styles to one or more cells. The `sides` argument is where we define
    which borders should be modified (e.g., `"left"`, `"right"`, etc.). With that selection, the
    `color`, `style`, and `weight` of the selected borders can then be modified.

    Parameters
    ----------
    sides : Literal["all", "top", "bottom", "left", "right"]
        The border sides to be modified. Options include `"left"`, `"right"`, `"top"`, and
        `"bottom"`. For all borders surrounding the selected cells, we can use the `"all"` option.
    color : str
        The border `color` can be defined with any valid CSS color value, such as a hex code, a
        named color, or an RGB value. The default `color` value is `"#000000"` (black).
    style : str
        The border `style` can be one of either `"solid"` (the default), `"dashed"`, `"dotted"`,
        `"hidden"`, or `"double"`.
    weight : str
        The default value for `weight` is `"1px"` and higher values will become more visually
        prominent.

    Returns
    -------
    CellStyleBorders
        A CellStyleBorders object, which is used for a `styles` argument if specifying cell borders.
    """

    def _to_html_style(self) -> str:
        border_css_list: List[str] = []
        for side in self.sides:
            border_css_list.append(f"border-{side}: {self.weight} {self.style} {self.color};")

        border_css = "".join(border_css_list)
        return border_css
