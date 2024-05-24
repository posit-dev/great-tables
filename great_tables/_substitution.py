from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Literal

from ._formats import fmt
from ._gt_data import FormatterSkipElement
from ._helpers import html
from ._tbl_data import DataFrameLike, SelectExpr, is_na
from ._text import Text, _process_text

if TYPE_CHECKING:
    from ._types import GTSelf


def _convert_missing(context: Literal["html"], el: str):
    """Convert el to a context specific representation."""

    # TODO: how is context passed? Could use a literal string (e.g. "html") for now?
    # TODO: detect if el has some kind of AsIs feature specified
    # which indicates it should not be converted

    # If a table row has all empty cells, they collapse. So add a single line break.
    # See https://stackoverflow.com/q/2789372/1144523
    if context == "html" and el == "":
        return "<br />"

    return el


def sub_missing(
    self: GTSelf,
    columns: SelectExpr = None,
    rows: int | list[int] | None = None,
    missing_text: str | Text | None = None,
) -> GTSelf:
    """
    Substitute missing values in the table body.

    Wherever there is missing data (i.e., `None` values) customizable content may present better
    than the standard representation of missing values that would otherwise appear. The
    `sub_missing()` method allows for this replacement through its `missing_text=` argument.
    And by not supplying anything to `missing_text=`, an em dash will serve as a default indicator
    of missingness.

    Parameters
    ----------
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.
    rows
        In conjunction with `columns=`, we can specify which of their rows should be scanned for
        missing values. The default is all rows, resulting in all rows in all targeted columns being
        considered for this substitution. Alternatively, we can supply a list of row indices.
    missing_text
        The text to be used in place of missing values in the rendered table. We can optionally use
        the [`md()`](`great_tables.md`) or [`html()`](`great_tables.html`) helper functions to style
        the text as Markdown or to retain HTML elements in the text.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Using a subset of the `exibble` dataset, let's create a new table. The missing values in two
    selections of columns will be given different variations of replacement text (across two
    separate calls of `sub_missing()`).

    ```{python}
    from great_tables import GT, md, html, exibble
    import polars as pl
    import polars.selectors as cs

    exibble_mini = pl.from_pandas(exibble).drop("row", "group", "fctr").slice(4, 8)

    (
        GT(exibble_mini)
        .sub_missing(
            columns=["num", "char"],
            missing_text="missing"
        )
        .sub_missing(
            columns=cs.contains(("date", "time")) | cs.by_name("currency"),
            missing_text="nothing"
        )
    )
    ```
    """

    subber = SubMissing(self._tbl_data, missing_text)
    return fmt(self, fns=subber.to_html, columns=columns, rows=rows, is_substitution=True)


def sub_zero(
    self: GTSelf,
    columns: SelectExpr = None,
    rows: int | list[int] | None = None,
    zero_text: str = "nil",
) -> GTSelf:
    """
    Substitute zero values in the table body.

    Wherever there is numerical data that are zero in value, replacement text may be better for
    explanatory purposes. The `sub_zero()` function allows for this replacement through its
    `zero_text=` argument.

    Parameters
    ----------
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.
    rows
        In conjunction with `columns=`, we can specify which of their rows should be scanned for
        zeros. The default is all rows, resulting in all rows in all targeted columns being
        considered for this substitution. Alternatively, we can supply a list of row indices.
    zero_text
        The text to be used in place of zero values in the rendered table. We can optionally use the
        [`md()`](`great_tables.md`) or [`html()`](`great_tables.html`) functions to style the text
        as Markdown or to retain HTML elements in the text.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's generate a simple table that contains an assortment of values that could potentially
    undergo some substitution via the `sub_zero()` method (i.e., there are two `0` values). The
    ordering of the [`fmt_scientific()`](`great_tables.GT.fmt_scientific`) and `sub_zero()` calls
    in the example below doesn't affect the final result since any `sub_*()` method won't interfere
    with the formatting of the table.

    ```{python}
    from great_tables import GT
    import polars as pl

    single_vals_df = pl.DataFrame(
        {
            "i": range(1, 8),
            "numbers": [2.75, 0, -3.2, 8, 1e-10, 0, 2.6e9]
        }
    )

    GT(single_vals_df).fmt_scientific(columns="numbers").sub_zero()
    ```
    """

    subber = SubZero(zero_text)
    return fmt(self, fns=subber.to_html, columns=columns, rows=rows, is_substitution=True)


@dataclass
class SubMissing:
    dispatch_frame: DataFrameLike
    missing_text: str | Text | None

    def __post_init__(self):
        # TODO: we should use an alternative to html(), once we support formats like latex
        if self.missing_text is None:
            self.missing_text = html("&mdash;")

    def to_html(self, x: Any) -> str | FormatterSkipElement:
        if is_na(self.dispatch_frame, x):
            return _process_text(self.missing_text)

        return FormatterSkipElement()


@dataclass
class SubZero:
    zero_text: str | Text

    def to_html(self, x: Any) -> str | FormatterSkipElement:
        if x == 0:
            return _process_text(self.zero_text)

        return FormatterSkipElement()
