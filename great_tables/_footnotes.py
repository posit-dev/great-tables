from __future__ import annotations

from typing import TYPE_CHECKING

from ._locations import Loc, PlacementOptions, set_footnote
from ._text import Text

if TYPE_CHECKING:
    from ._types import GTSelf


def tab_footnote(
    self: GTSelf,
    footnote: str | Text,
    locations: Loc | None | list[Loc | None] = None,
    placement: PlacementOptions = "auto",
) -> GTSelf:
    """
    Add a table footnote.

    `tab_footnote()` can make it a painless process to add a footnote to a
    **Great Tables** table. There are commonly two components to a footnote:
    (1) a footnote mark that is attached to the targeted cell content, and (2)
    the footnote text itself that is placed in the table's footer area. Each unit
    of footnote text in the footer is linked to an element of text or otherwise
    through the footnote mark.

    The footnote system in **Great Tables** presents footnotes in a way that matches
    the usual expectations, where:

    1. footnote marks have a sequence, whether they are symbols, numbers, or letters
    2. multiple footnotes can be applied to the same content (and marks are
       always presented in an ordered fashion)
    3. footnote text in the footer is never exactly repeated, **Great Tables** reuses
       footnote marks where needed throughout the table
    4. footnote marks are ordered across the table in a consistent manner (left
       to right, top to bottom)

    Each call of `tab_footnote()` will either add a different footnote to the
    footer or reuse existing footnote text therein. One or more cells outside of
    the footer are targeted using location classes from the `loc` module (e.g.,
    `loc.body()`, `loc.column_labels()`, etc.). You can choose to *not* attach
    a footnote mark by simply not specifying anything in the `locations` argument.

    By default, **Great Tables** will choose which side of the text to place the
    footnote mark via the `placement="auto"` option. You are, however, always free
    to choose the placement of the footnote mark (either to the `"left"` or `"right"`
    of the targeted cell content).

    Parameters
    ----------
    footnote
        The text to be used in the footnote. We can optionally use
        [`md()`](`great_tables.md`) or [`html()`](`great_tables.html`) to style
        the text as Markdown or to retain HTML elements in the footnote text.
    locations
        The cell or set of cells to be associated with the footnote. Supplying any
        of the location classes from the `loc` module is a useful way to target the
        location cells that are associated with the footnote text. These location
        classes are: `loc.title`, `loc.stubhead`, `loc.spanner_labels`,
        `loc.column_labels`, `loc.row_groups`, `loc.stub`, `loc.body`, etc.
        Additionally, we can enclose several location calls within a `list()` if we
        wish to link the footnote text to different types of locations (e.g., body
        cells, row group labels, the table title, etc.).
    placement
        Where to affix footnote marks to the table content. Two options for this
        are `"left"` or `"right"`, where the placement is either to the absolute
        left or right of the cell content. By default, however, this option is set
        to `"auto"` whereby **Great Tables** will choose a preferred left-or-right
        placement depending on the alignment of the cell content.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called
        on so that we can facilitate method chaining.

    Examples
    --------
    See [`GT.tab_footnote()`](`great_tables.GT.tab_footnote`) for examples.
    """

    # Convert footnote to string if it's a Text object
    if hasattr(footnote, "__str__"):
        footnote_str = str(footnote)
    else:
        footnote_str = footnote

    # Handle None locations (footnote without mark)
    if locations is None:
        return set_footnote(None, self, footnote_str, placement)  # type: ignore

    # Ensure locations is a list
    if not isinstance(locations, list):
        locations = [locations]

    # Apply footnote to each location
    result = self
    for loc in locations:
        result = set_footnote(loc, result, footnote_str, placement)  # type: ignore

    return result  # type: ignore
