from __future__ import annotations

from ._tbl_data import DataFrameLike, SelectExpr, is_na
from ._gt_data import FormatterSkipElement, FormatInfo
from ._formats import fmt


from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Type, Union, Literal, List

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
    rows: Union[int, List[int], None] = None,
    missing_text: str = "---",
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
        the `md()` and `html()` helper functions to style the text as Markdown or to retain HTML
        elements in the text.

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
            columns = ["num", "char"],
            missing_text = "missing"
        )
        .sub_missing(
            columns = cs.contains(("date", "time")) | cs.by_name("currency"),
            missing_text = "nothing"
        )
    )
    ```

    """

    subber = SubMissing(self._tbl_data, missing_text)
    return fmt(self, fns=subber.to_html, columns=columns, rows=rows, is_substitution=True)


def sub_zero(
    self: GTSelf,
    columns: SelectExpr = None,
    rows: Union[int, List[int], None] = None,
    zero_text: str = "nil",
) -> GTSelf:
    subber = SubZero(zero_text)
    return fmt(self, fns=subber.to_html, columns=columns, rows=rows, is_substitution=True)


@dataclass
class SubMissing:
    dispatch_frame: DataFrameLike
    missing_text: str

    def to_html(self, x: Any) -> str | FormatterSkipElement:
        return self.missing_text if is_na(self.dispatch_frame, x) else FormatterSkipElement()


@dataclass
class SubZero:
    zero_text: str

    def to_html(self, x: Any) -> str | FormatterSkipElement:
        return self.zero_text if x == 0 else FormatterSkipElement()
