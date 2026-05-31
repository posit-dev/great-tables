from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable, Literal

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


def sub_small_vals(
    self: GTSelf,
    columns: SelectExpr = None,
    rows: int | list[int] | None = None,
    threshold: int | float = 0.01,
    small_pattern: str | None = None,
    sign: str = "+",
) -> GTSelf:
    """
    Substitute small values in the table body.

    Wherever there is numerical data that are very small in value, replacement text may be better
    for explanatory purposes. The `sub_small_vals()` method allows for this replacement through
    specification of a `threshold`, a `small_pattern`, and the sign of the values to be considered.
    The substitution will occur for those values found to be between `0` and the threshold value.
    This is possible for small positive and small negative values (this can be explicitly set by the
    `sign` option). Note that the interval does not include the `0` or the `threshold` value.
    Should you need to include zero values, use `sub_zero()`.

    Parameters
    ----------
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.
    rows
        In conjunction with `columns=`, we can specify which of their rows should be scanned for
        small values. The default is all rows, resulting in all rows in all targeted columns being
        considered for this substitution. Alternatively, we can supply a list of row indices.
    threshold
        The threshold value with which values should be considered small enough for replacement.
    small_pattern
        The pattern text to be used in place of the suitably small values in the rendered table.
        The `{x}` placeholder within the pattern will be replaced with the threshold value. If not
        provided, the default is `"<{x}"` for positive values and `">-{x}"` for negative values.
    sign
        The sign of the numbers to be considered in the replacement. By default, we only consider
        positive values (`"+"`). The other option (`"-"`) can be used to consider only negative
        values.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's generate a simple, single-column table that contains an assortment of values that could
    potentially undergo some substitution via `sub_small_vals()`.

    ```{python}
    from great_tables import GT
    import polars as pl

    single_vals_df = pl.DataFrame(
        {
            "i": range(1, 8),
            "numbers": [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0]
        }
    )

    GT(single_vals_df).fmt_number(columns="numbers").sub_small_vals()
    ```

    We can also target small negative values by setting `sign="-"` and use a custom
    `small_pattern` to provide alternative replacement text.

    ```{python}
    from great_tables import GT
    import polars as pl

    neg_vals_df = pl.DataFrame(
        {
            "i": range(1, 6),
            "numbers": [-0.0001, -0.005, -0.05, -1.0, -100.0]
        }
    )

    (
        GT(neg_vals_df)
        .fmt_number(columns="numbers")
        .sub_small_vals(sign="-", threshold=0.01, small_pattern="~0")
    )
    ```
    """

    if sign not in ("+", "-"):
        raise ValueError('The `sign` option should be either "+" or "-".')

    threshold = abs(threshold)

    if small_pattern is None:
        if sign == "+":
            small_pattern = "<{x}"
        else:
            small_pattern = ">-{x}"

    subber = SubSmallVals(threshold=threshold, small_pattern=small_pattern, sign=sign)
    return fmt(self, fns=subber.to_html, columns=columns, rows=rows, is_substitution=True)


def sub_large_vals(
    self: GTSelf,
    columns: SelectExpr = None,
    rows: int | list[int] | None = None,
    threshold: int | float = 1e12,
    large_pattern: str = ">={x}",
    sign: str = "+",
) -> GTSelf:
    """
    Substitute large values in the table body.

    Wherever there are numerical data that are very large in value, replacement text may be better
    for explanatory purposes. The `sub_large_vals()` method allows for this replacement through
    specification of a `threshold`, a `large_pattern`, and the sign (positive or negative) of the
    values to be considered.

    Parameters
    ----------
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.
    rows
        In conjunction with `columns=`, we can specify which of their rows should be scanned for
        large values. The default is all rows, resulting in all rows in all targeted columns being
        considered for this substitution. Alternatively, we can supply a list of row indices.
    threshold
        The threshold value with which values should be considered large enough for replacement.
    large_pattern
        The pattern text to be used in place of the suitably large values in the rendered table.
        The `{x}` placeholder within the pattern will be replaced with the threshold value.
    sign
        The sign of the numbers to be considered in the replacement. By default, we only consider
        positive values (`"+"`). The other option (`"-"`) can be used to consider only negative
        values. Note that when `sign="-"` and the default `large_pattern=">={x}"` is used, the
        `">="` is automatically changed to `"<="`.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's generate a simple, single-column table that contains an assortment of values that could
    potentially undergo some substitution via `sub_large_vals()`.

    ```{python}
    from great_tables import GT
    import polars as pl

    single_vals_df = pl.DataFrame(
        {
            "i": range(1, 8),
            "numbers": [0.0, 10.0, 1e8, 1e9, 1e10, 1e11, 1e12]
        }
    )

    GT(single_vals_df).fmt_number(columns="numbers").sub_large_vals(threshold=1e10)
    ```

    Large negative values can also be targeted with `sign="-"`. Notice the `">="` in the default
    pattern is automatically changed to `"<="` when dealing with negative values.

    ```{python}
    from great_tables import GT
    import polars as pl

    neg_vals_df = pl.DataFrame(
        {
            "i": range(1, 5),
            "numbers": [-10.0, -500.0, -1e6, -1e12]
        }
    )

    (
        GT(neg_vals_df)
        .fmt_number(columns="numbers")
        .sub_large_vals(threshold=1000, sign="-")
    )
    ```
    """

    if sign not in ("+", "-"):
        raise ValueError('The `sign` option should be either "+" or "-".')

    threshold = abs(threshold)

    subber = SubLargeVals(threshold=threshold, large_pattern=large_pattern, sign=sign)
    return fmt(self, fns=subber.to_html, columns=columns, rows=rows, is_substitution=True)


def sub_values(
    self: GTSelf,
    columns: SelectExpr = None,
    rows: int | list[int] | None = None,
    values: list[Any] | Any | None = None,
    pattern: str | None = None,
    fn: Callable[..., bool] | None = None,
    replacement: str | int | float | None = None,
) -> GTSelf:
    """
    Substitute targeted values in the table body.

    Should you need to replace specific cell values with custom text, `sub_values()` can be a good
    choice. We can target cells for replacement through value, regex, and custom matching rules.

    Parameters
    ----------
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.
    rows
        In conjunction with `columns=`, we can specify which of their rows should be targeted for
        substitution. The default is all rows, resulting in all rows in all targeted columns being
        considered for this substitution. Alternatively, we can supply a list of row indices.
    values
        The specific value or values that should be replaced with a `replacement` value. If
        `pattern` is also supplied then `values` will be ignored.
    pattern
        A regex pattern that can target solely those values in character-based columns. If `values`
        is also supplied, `pattern` will take precedence.
    fn
        A supplied function that operates on each cell value `x` and should return a boolean
        indicating whether that value should be replaced. If either of `values` or `pattern` is also
        supplied, `fn` will take precedence.
    replacement
        The replacement value for any cell values matched by either `values`, `pattern`, or `fn`.
        Must be a string or numeric value.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's create an input table with three columns containing an assortment of values that could
    potentially undergo some substitution via `sub_values()`.

    ```{python}
    from great_tables import GT
    import polars as pl

    tbl = pl.DataFrame(
        {
            "num_1": [-0.01, 74.0, None, 0.0, 500.0, 0.001, 84.3],
            "int_1": [1, -100000, 800, 5, None, 1, -32],
            "lett": ["A", "B", "C", "D", "E", "F", "G"],
        }
    )

    GT(tbl).sub_values(values=[74, 500], replacement="—")
    ```

    For the most flexibility, use the `fn` argument. The function you provide should accept a cell
    value and return a boolean indicating whether it should be replaced.

    ```{python}
    from great_tables import GT
    import polars as pl

    tbl = pl.DataFrame(
        {
            "num_1": [-0.01, 74.0, None, 0.0, 500.0, 0.001, 84.3],
            "int_1": [1, -100000, 800, 5, None, 1, -32],
            "lett": ["A", "B", "C", "D", "E", "F", "G"],
        }
    )

    (
        GT(tbl)
        .sub_values(
            fn=lambda x: isinstance(x, (int, float)) and x >= 0 and x < 50,
            replacement="small"
        )
    )
    ```
    """

    if values is None and pattern is None and fn is None:
        raise ValueError("One of `values`, `pattern`, or `fn` must be supplied to `sub_values()`.")

    if replacement is None:
        raise ValueError("A `replacement` value must be provided.")

    if fn is not None and not callable(fn):
        raise TypeError("A function must be provided to the `fn` argument.")

    subber = SubValues(values=values, pattern=pattern, fn=fn, replacement=replacement)
    return fmt(self, fns=subber.to_html, columns=columns, rows=rows, is_substitution=True)


@dataclass
class SubSmallVals:
    threshold: float
    small_pattern: str
    sign: str

    def to_html(self, x: Any) -> str | FormatterSkipElement:
        # Only operate on numeric values
        if not isinstance(x, (int, float)):
            return FormatterSkipElement()

        # Skip NA/NaN values
        if x != x:  # NaN check
            return FormatterSkipElement()

        # Skip zero values
        if x == 0:
            return FormatterSkipElement()

        if self.sign == "+":
            # Value must be positive and less than threshold
            if x > 0 and x < self.threshold:
                return self._format_text()
        else:
            # Value must be negative and greater than -threshold (closer to zero)
            if x < 0 and x > -self.threshold:
                return self._format_text()

        return FormatterSkipElement()

    def _format_text(self) -> str:
        text = self.small_pattern.replace("{x}", str(self.threshold))
        return _process_text(text)


@dataclass
class SubLargeVals:
    threshold: float
    large_pattern: str
    sign: str

    def to_html(self, x: Any) -> str | FormatterSkipElement:
        # Only operate on numeric values
        if not isinstance(x, (int, float)):
            return FormatterSkipElement()

        # Skip NA/NaN values
        if x != x:  # NaN check
            return FormatterSkipElement()

        if self.sign == "+":
            # Value must be >= threshold
            if x >= self.threshold:
                return self._format_text()
        else:
            # Value must be <= -threshold
            if x <= -self.threshold:
                return self._format_text()

        return FormatterSkipElement()

    def _format_text(self) -> str:
        pattern = self.large_pattern

        # When sign is "-", flip ">=" to "<=" in the pattern
        if self.sign == "-":
            pattern = pattern.replace(">=", "<=")

        text = pattern.replace("{x}", str(self.threshold))
        return _process_text(text)


@dataclass
class SubValues:
    values: list[Any] | Any | None
    pattern: str | None
    fn: Callable[..., bool] | None
    replacement: str | int | float

    def to_html(self, x: Any) -> str | FormatterSkipElement:
        if self._is_match(x):
            return _process_text(str(self.replacement))

        return FormatterSkipElement()

    def _is_match(self, x: Any) -> bool:
        # Skip NA/None values
        if x is None:
            return False

        # Priority: fn > pattern > values
        if self.fn is not None:
            try:
                result = self.fn(x)
                return bool(result)
            except (TypeError, ValueError):
                return False

        if self.pattern is not None:
            # Pattern matching only works on string values
            if not isinstance(x, str):
                return False
            return bool(re.search(self.pattern, x))

        if self.values is not None:
            match_values = self.values if isinstance(self.values, list) else [self.values]
            return x in match_values

        return False
