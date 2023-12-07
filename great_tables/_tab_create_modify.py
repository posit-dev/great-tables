from __future__ import annotations

from typing import TYPE_CHECKING

from ._locations import Loc, PlacementOptions, set_footnote, set_style
from ._styles import CellStyle


if TYPE_CHECKING:
    from ._types import GTSelf


def tab_style(
    self: GTSelf, style: CellStyle | list[CellStyle], locations: Loc | list[Loc]
) -> GTSelf:
    """Add custom style to one or more cells

    Parameters
    ----------
    style:
        A style specification.
    location:
        A location on the table.
    """

    if not isinstance(style, list):
        style = [style]

    if not isinstance(locations, list):
        locations = [locations]

    new_data = self
    for loc in locations:
        new_data = set_style(loc, self, style)

    return new_data


# TODO: note that this function does not yet render, and rendering
# will likely be implemented down the road (e.g. after basic styling).
# this is just all the machinery to set data in GT._footnotes
def tab_footnote(
    self: GTSelf,
    footnote: str | list[str],
    locations: Loc | None | list[Loc | None],
    placement: PlacementOptions = "auto",
) -> GTSelf:
    """Add a footnote to a table

    Parameters
    ----------
    footnote:
        The footnote text.
    locations:
        The location to place the footnote. If None, then a footnote is created without
        a correesponding marker on the table (TODO: double check this).
    placement:
        Where to affix the footnote marks to the table content.

    """

    if isinstance(footnote, list):
        raise NotImplementedError("Currently, only a single string is supported for footnote.")

    if not isinstance(locations, list):
        locations = [locations]

    new_data = self
    if isinstance(locations, list):
        for loc in locations:
            new_data = set_footnote(loc, self, footnote, placement)

    return new_data
