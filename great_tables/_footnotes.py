from __future__ import annotations

from typing import TYPE_CHECKING

from ._gt_data import FootnoteInfo, FootnotePlacement
from ._locations import FootnoteEntry, Loc, PlacementOptions, set_style
from ._text import Text, _process_text

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

    `tab_footnote()` can make it a painless process to add a footnote to a table. There are commonly
    two components to a footnote: (1) a footnote mark that is attached to the targeted cell content,
    and (2) the footnote text itself that is placed in the table's footer area. Each unit of
    footnote text in the footer is linked to an element of text or otherwise through the footnote
    mark.

    The footnote system in **Great Tables** presents footnotes in a way that matches the usual
    expectations, where:

    1. footnote marks have a sequence, whether they are symbols, numbers, or letters
    2. multiple footnotes can be applied to the same content (and marks are always presented in an
    ordered fashion)
    3. footnote text in the footer is never exactly repeated, **Great Tables** reuses footnote marks
    where needed throughout the table
    4. footnote marks are ordered across the table in a consistent manner (left to right, top to
    bottom)

    Each call of `tab_footnote()` will either add a different footnote to the footer or reuse
    existing footnote text therein. One or more cells outside of the footer are targeted using
    location classes from the `loc` module (e.g., `loc.body()`, `loc.column_labels()`, etc.). You
    can choose to *not* attach a footnote mark by simply not specifying anything in the `locations`
    argument.

    By default, **Great Tables** will choose which side of the text to place the footnote mark via
    the `placement="auto"` option. You are, however, always free to choose the placement of the
    footnote mark (either to the `"left"` or `"right"` of the targeted cell content).

    Parameters
    ----------
    footnote
        The text to be used in the footnote. We can optionally use [`md()`](`great_tables.md`) or
        [`html()`](`great_tables.html`) to style the text as Markdown or to retain HTML elements in
        the footnote text.
    locations
        The cell or set of cells to be associated with the footnote. Supplying any of the location
        classes from the `loc` module is a useful way to target the location cells that are
        associated with the footnote text. These location classes are: `loc.title`, `loc.stubhead`,
        `loc.spanner_labels`, `loc.column_labels`, `loc.row_groups`, `loc.stub`, `loc.body`, etc.
        Additionally, we can enclose several location calls within a `list()` if we wish to link the
        footnote text to different types of locations (e.g., body cells, row group labels, the table
        title, etc.).
    placement
        Where to affix footnote marks to the table content. Two options for this are `"left"` or
        `"right"`, where the placement is either to the absolute left or right of the cell content.
        By default, however, this option is set to `"auto"` whereby **Great Tables** will choose a
        preferred left-or-right placement depending on the alignment of the cell content.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    This example table will be based on the `towny` dataset. We have a header part, with a title and
    a subtitle. We can choose which of these could be associated with a footnote and in this case it
    is the `"subtitle"`. This table has a stub with row labels and some of those labels are
    associated with a footnote. So long as row labels are unique, they can be easily used as row
    identifiers in `loc.stub()`. The third footnote is placed on the `"Density"` column label. Here,
    changing the order of the `tab_footnote()` calls has no effect on the final table rendering.

    ```{python}
    import polars as pl
    from great_tables import GT, loc, md
    from great_tables.data import towny

    towny_mini = (
        pl.from_pandas(towny)
        .filter(pl.col("csd_type") == "city")
        .select(["name", "density_2021", "population_2021"])
        .top_k(10, by="population_2021")
        .sort("population_2021", descending=True)
    )

    (
        GT(towny_mini, rowname_col="name")
        .tab_header(
            title=md("The 10 Largest Municipalities in `towny`"),
            subtitle="Population values taken from the 2021 census."
        )
        .fmt_integer()
        .cols_label(
            density_2021="Density",
            population_2021="Population"
        )
        .tab_footnote(
            footnote="Part of the Greater Toronto Area.",
            locations=loc.stub(rows=[
                "Toronto", "Mississauga", "Brampton", "Markham", "Vaughan"
            ])
        )
        .tab_footnote(
            footnote=md("Density is in terms of persons per {{km^2}}."),
            locations=loc.column_labels(columns="density_2021")
        )
        .tab_footnote(
            footnote="Census results made public on February 9, 2022.",
            locations=loc.subtitle()
        )
        .tab_source_note(
            source_note=md("Data taken from the `towny` dataset.")
        )
        .opt_footnote_marks(marks="letters")
    )
    ```
    """

    # Store footnote as-is to preserve Text objects for later processing
    footnote_str = footnote

    # Handle None locations (footnote without mark)
    if locations is None:
        # For None location, directly add to footnotes
        place = FootnotePlacement[placement]
        processed_footnote = _process_text(footnote_str)
        info = FootnoteInfo(locname=None, footnotes=[processed_footnote], placement=place)
        return self._replace(_footnotes=self._footnotes + [info])  # type: ignore

    # Ensure locations is a list
    if not isinstance(locations, list):
        locations = [locations]

    # Apply footnote to each location
    result = self
    for loc in locations:
        if loc is None:
            # Handle None in the list
            place = FootnotePlacement[placement]
            processed_footnote = _process_text(footnote_str)
            info = FootnoteInfo(locname=None, footnotes=[processed_footnote], placement=place)
            result = result._replace(_footnotes=result._footnotes + [info])  # type: ignore
        else:
            # Use the new consolidated approach - FootnoteEntry will handle Text conversion internally
            footnote_entry = FootnoteEntry(footnote=footnote_str, placement=placement)
            result = set_style(loc, result, [footnote_entry])  # type: ignore

    return result  # type: ignore
