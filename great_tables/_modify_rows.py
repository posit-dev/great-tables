from __future__ import annotations

from statistics import quantiles
from typing import TYPE_CHECKING, Any, Literal

from great_tables._locations import resolve_cols_c

from ._gt_data import (
    GRAND_SUMMARY_GROUP,
    FormatFn,
    GTData,
    Locale,
    RowGroups,
    Styles,
    SummaryFn,
    SummaryRowInfo,
)
from ._tbl_data import (
    SelectExpr,
    to_list,
)

if TYPE_CHECKING:
    from ._types import GTSelf


def row_group_order(self: GTSelf, groups: RowGroups) -> GTSelf:
    new_stub = self._stub.order_groups(groups)

    return self._replace(_stub=new_stub)


def _remove_from_body_styles(styles: Styles, column: str) -> Styles:
    # TODO: refactor
    from ._locations import LocBody
    from ._utils_render_html import _is_loc

    new_styles = [
        info for info in styles if not (_is_loc(info.locname, LocBody) and info.colname == column)
    ]

    return new_styles


def _remove_from_group_styles(styles: Styles, column: str):
    # TODO(#341): once group styles are supported, will need to wire this up.
    return list(styles)


def tab_stub(
    self: GTSelf, rowname_col: str | None = None, groupname_col: str | None = None
) -> GTSelf:
    """Add a table stub, to emphasize row and group information.

    Parameters
    ----------
    rowname_col:
        The column to use for row names. By default, no row names added.
    groupname_col:
        The column to use for group names. By default no group names added.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------

    By default, all data is together in the body of the table.

    ```{python}
    from great_tables import GT, exibble

    GT(exibble)
    ```

    The table stub separates row names with a vertical line, and puts group names
    on their own line.

    ```{python}
    GT(exibble).tab_stub(rowname_col="row", groupname_col="group")
    ```
    """
    # old columns ----
    _info = self._boxhead._get_row_group_column()
    old_groupname_col = _info.var if _info is not None else None

    styles = self._styles

    # remove group styles ----
    if old_groupname_col is not None and old_groupname_col != groupname_col:
        styles = _remove_from_group_styles(styles, old_groupname_col)

    # remove table body styles ----
    # they no longer apply to groupname_col
    if groupname_col is not None:
        styles = _remove_from_body_styles(self._styles, groupname_col)

    self = self._replace(_styles=styles)

    # remove from spanners ----
    if groupname_col is not None:
        self = self._replace(_spanners=self._spanners.remove_column(groupname_col))

    if rowname_col is not None:
        self = self._replace(_spanners=self._spanners.remove_column(rowname_col))

    # set new row and group name cols ----
    stub, boxhead = self._stub._set_cols(self._tbl_data, self._boxhead, rowname_col, groupname_col)

    return self._replace(_stub=stub, _boxhead=boxhead)


def with_locale(self: GTSelf, locale: str | None = None) -> GTSelf:
    """Set a column to be the default locale.

    Setting a default locale affects formatters like `fmt_number()`, and `fmt_date()`,
    by having them default to locale-specific features (e.g. representing one thousand
    as 1.000,00)

    Parameters
    ----------
    locale
        An optional locale identifier that can be used for formatting values according the locale's
        rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's create a table and set its `locale=` to `"ja"` for Japan. Then, we call `fmt_currency()`
    to format the `"currency"` column. Since we didn't specify a `locale=` for `fmt_currency()`,
    it will adopt the globally set `"ja"` locale.

    ```{python}
    from great_tables import GT, exibble


    (
        GT(exibble)
        .with_locale("ja")
        .fmt_currency(
            columns="currency",
            decimals=3,
            use_seps=False
        )
    )
    ```
    **Great Tables** internally supports many locale options. You can find the available locales in
    the following table:

    ```{python}
    from great_tables.data import __x_locales

    columns = ["locale", "lang_name", "lang_desc", "territory_name", "territory_desc"]
    GT(__x_locales.loc[:, columns]).cols_align("right")
    ```
    """

    return self._replace(_locale=Locale(locale))


def with_id(self: GTSelf, id: str | None = None) -> GTSelf:
    """Set the id for this table.

    Note that this is a shortcut for the `table_id=` argument in `GT.tab_options()`.

    Parameters
    ----------
    id
        By default (with `None`) the table ID will be a random, ten-letter string as generated
        through internal use of the `random_id()` function. A custom table ID can be used here by
        providing a string.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    The use of `with_id` is straightforward—simply pass a string to `id=` to set the table ID:
    ```{python}
    from great_tables import GT, exibble

    GT(exibble).with_id("your-table-id")
    ```
    """
    return self._replace(_options=self._options._set_option_value("table_id", id))


def grand_summary_rows(
    self: GTSelf,
    fns: str | list[str] | list[SummaryFn] | dict[str, str] | dict[str, SummaryFn],
    fmt: FormatFn | None = None,
    columns: SelectExpr = None,
    side: Literal["bottom", "top"] = "bottom",
    missing_text: str = "---",
) -> GTSelf:
    """Add grand summary rows to the table.

    Add grand summary rows by using the table data and any suitable aggregation functions. With
    grand summary rows, all of the available data in the gt table is incorporated (regardless of
    whether some of the data are part of row groups). Multiple grand summary rows can be added via
    expressions given to fns. You can selectively format the values in the resulting grand summary
    cells by use of formatting expressions in fmt.

    Parameters
    ----------

    fns
        TODO text
    fmt
        TODO text
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.
    side
        Should the grand summary rows be placed at the `"bottom"` (the default) or the `"top"` of
        the table?
    missing_text
        The text to be used in summary cells with no data outputs.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    TODO Explanation
    ```{python}

    ```

    """
    # Computes summary rows immediately but stores them separately from main data.
    normalized_fns = _normalize_fns_to_tuples(fns)

    for label, fn_callable in normalized_fns:
        row_values_dict = _calculate_summary_row(
            self, fn_callable, fmt, columns, missing_text, group_id=None
        )

        summary_row_info = SummaryRowInfo(
            id=label,
            label=label,
            values=row_values_dict,  # TODO: revisit type
            side=side,
            group=GRAND_SUMMARY_GROUP,
        )

        self._summary_rows.add_summary_row(summary_row_info)

    return self


def _normalize_fns_to_tuples(
    fns: str | list[str] | list[SummaryFn] | dict[str, str] | dict[str, SummaryFn],
) -> list[tuple[str, SummaryFn]]:
    """Convert all fns formats to a list of (label, callable) tuples."""

    # Case 1: Single string -> convert to list
    if isinstance(fns, str):
        fns = [fns]

    # Case 2: List of strings
    if isinstance(fns, list) and all(isinstance(fn, str) for fn in fns):
        return [(fn_name, _get_builtin_function(fn_name)) for fn_name in fns]

    # Case 3: List of callables -> infer labels from function names
    if isinstance(fns, list) and all(callable(fn) for fn in fns):
        return [(fn.__name__, fn) for fn in fns]

    # Case 4: Dict with string values -> convert strings to callables
    if isinstance(fns, dict) and all(isinstance(v, str) for v in fns.values()):
        return [(label, _get_builtin_function(fn_name)) for label, fn_name in fns.items()]

    # Case 5: Dict with callable values -> everything is given
    if isinstance(fns, dict) and all(callable(v) for v in fns.values()):
        return list(fns.items())

    raise ValueError(f"Unsupported fns format: {type(fns)} or mixed types in collection")


def _get_builtin_function(fn_name: str) -> SummaryFn:
    """Convert string function name to actual callable function."""

    def _mean(values: list[Any]) -> float:
        return sum(values) / len(values)

    def _median(values: list[Any]) -> Any:
        return quantiles(values, n=2)[0]

    builtin_functions: dict[str, SummaryFn] = {
        "min": min,
        "max": max,
        "sum": sum,
        "mean": _mean,
        "median": _median,
    }

    if fn_name not in builtin_functions:
        raise ValueError(f"Unknown function name: {fn_name}")

    return builtin_functions[fn_name]


def _calculate_summary_row(
    data: GTData,
    fn: SummaryFn,
    fmt: FormatFn | None,
    columns: SelectExpr,
    missing_text: str,
    group_id: str | None = None,  # None means grand summary (all data)
) -> dict[str, Any]:
    """Calculate a summary row based on the function and selected columns for a specific group."""
    original_columns = data._boxhead._get_columns()

    summary_col_names = resolve_cols_c(data=data, expr=columns)

    if group_id is None:
        group_id = GRAND_SUMMARY_GROUP.group_id
    else:
        # Future: group-specific logic would go here
        raise NotImplementedError("Group-specific summaries not yet implemented")

    # Create summary row data as dict
    summary_row = {}

    for col in original_columns:
        if col in summary_col_names:
            col_data = to_list(data._tbl_data[col])
            res = fn(col_data)

            if fmt is not None:
                # The vals functions expect a list and return a list
                formatted_list = fmt([res])
                res = formatted_list[0]

            summary_row[col] = res
        else:
            summary_row[col] = missing_text

    return summary_row
