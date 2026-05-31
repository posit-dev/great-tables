from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, Literal

from ._gt_data import (
    FormatFn,
    GTData,
    Locale,
    RowGroups,
    Styles,
    SummaryRowInfo,
)
from ._tbl_data import (
    PlExpr,
    SelectExpr,
    TblData,
    eval_aggregate,
    reorder,
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


def summary_rows(
    self: GTSelf,
    *,
    fns: dict[str, PlExpr] | dict[str, Callable[[TblData], Any]],
    fmt: FormatFn | None = None,
    columns: SelectExpr = None,
    groups: list[str] | None = None,
    side: Literal["bottom", "top"] = "bottom",
    missing_text: str = "---",
) -> GTSelf:
    """Add group-wise summary rows to the table.

    Add summary rows by using the table data and any suitable aggregation functions. With
    `summary_rows()`, the data within each row group is aggregated separately and summary rows are
    placed adjacent to each group. Multiple summary rows can be added via expressions given to
    `fns=`. You can selectively format the values in the resulting summary cells by use of
    formatting expressions from the `vals.fmt_*` class of functions.

    Note that currently all arguments are keyword-only, since the final positions may change.

    Parameters
    ----------
    fns
        A dictionary mapping row labels to aggregation expressions. Can be either Polars expressions
        or callable functions that take a DataFrame subset and return aggregated results. Each key
        becomes the label for a summary row within each group.
    fmt
        A formatting function from the `vals.fmt_*` family (e.g., `vals.fmt_number`,
        `vals.fmt_currency`) to apply to the summary row values. If `None`, no formatting is
        applied.
    columns
        Currently, this function does not support selection by columns. If you would like to choose
        which columns to summarize, you can select columns within the functions given to `fns=`.
        See examples below for more explicit cases.
    groups
        The groups to target for summary row insertion. Can be a list of group IDs as strings. By
        default (`None`), summary rows are generated for all groups.
    side
        Should the summary rows be placed at the `"bottom"` (the default) or the `"top"` of each
        group?
    missing_text
        The text to be used in summary cells with no data outputs.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    Examples
    --------
    Let's use a subset of the `gtcars` dataset to create a table with group summary rows. We'll
    group by manufacturer and show min and max values for horsepower and torque columns.

    ```{python}
    import polars as pl
    from great_tables import GT, vals
    from great_tables.data import gtcars

    gtcars_mini = (
        pl.from_pandas(gtcars)
        .select(["mfr", "model", "hp", "trq"])
        .head(12)
    )

    (
        GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
        .summary_rows(
            fns={
                "Min": pl.col("hp", "trq").min(),
                "Max": pl.col("hp", "trq").max(),
            },
            fmt=vals.fmt_integer,
        )
    )
    ```

    We can also target specific groups by using the `groups=` parameter. Here we only show
    summary rows for the `"BMW"` group:

    ```{python}
    (
        GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
        .summary_rows(
            fns={
                "Average": pl.col("hp", "trq").mean(),
            },
            groups=["BMW"],
            fmt=vals.fmt_number,
        )
    )
    ```

    Callable functions work with pandas DataFrames. Each function receives the subset of data
    for that group:

    ```{python}
    from great_tables import GT, vals
    from great_tables.data import gtcars

    (
        GT(
            gtcars[["mfr", "model", "hp", "trq"]].head(12),
            rowname_col="model",
            groupname_col="mfr",
        )
        .summary_rows(
            fns={
                "Min": lambda df: df.min(numeric_only=True),
                "Max": lambda df: df.max(numeric_only=True),
            },
            fmt=vals.fmt_integer,
        )
    )
    ```

    Summary rows can be placed at the top of each group using `side="top"`:

    ```{python}
    import polars as pl
    from great_tables import GT, vals
    from great_tables.data import gtcars

    gtcars_mini = (
        pl.from_pandas(gtcars)
        .select(["mfr", "model", "hp", "trq"])
        .head(12)
    )

    (
        GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
        .summary_rows(
            fns={"Mean": pl.col("hp", "trq").mean()},
            side="top",
            fmt=vals.fmt_number,
        )
    )
    ```

    Combining group summaries with grand summary rows and styling provides a comprehensive
    summary view of the data. Use `loc.summary()` to style all group summary cells:

    ```{python}
    import polars as pl
    from great_tables import GT, vals, style, loc
    from great_tables.data import gtcars

    gtcars_mini = (
        pl.from_pandas(gtcars)
        .select(["mfr", "model", "hp", "trq"])
        .head(12)
    )

    (
        GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
        .summary_rows(
            fns={
                "Min": pl.col("hp", "trq").min(),
                "Max": pl.col("hp", "trq").max(),
            },
            fmt=vals.fmt_integer,
        )
        .grand_summary_rows(
            fns={"Overall Mean": pl.col("hp", "trq").mean()},
            fmt=vals.fmt_number,
        )
        .tab_style(
            style=[style.fill(color="lightyellow")],
            locations=loc.summary(),
        )
        .tab_style(
            style=[style.fill(color="lightblue")],
            locations=loc.grand_summary(),
        )
    )
    ```

    When groups are displayed as a column in the stub (using `row_group_as_column=True`),
    the summary row labels span the stub columns:

    ```{python}
    import polars as pl
    from great_tables import GT, vals
    from great_tables.data import gtcars

    gtcars_mini = (
        pl.from_pandas(gtcars)
        .select(["mfr", "model", "hp", "trq"])
        .head(12)
    )

    (
        GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
        .tab_options(row_group_as_column=True)
        .summary_rows(
            fns={
                "Min": pl.col("hp", "trq").min(),
                "Max": pl.col("hp", "trq").max(),
            },
            fmt=vals.fmt_integer,
        )
    )
    ```

    """
    if columns is not None:
        raise NotImplementedError("Currently, summary_rows() does not support column selection.")

    # Get the group information from the stub
    group_rows = self._stub.group_rows

    if not group_rows._d:
        raise ValueError(
            "summary_rows() requires row groups. Use `groupname_col=` in GT() or "
            "`tab_stub(groupname_col=...)` to define groups."
        )

    # Determine which groups to target
    all_group_ids = [g.group_id for g in group_rows]
    if groups is not None:
        target_group_ids = [gid for gid in groups if gid in all_group_ids]
    else:
        target_group_ids = all_group_ids

    # Get column names for subsetting
    all_columns = [col.var for col in self._boxhead]

    new_summary = self._summary_rows

    for group_info in group_rows:
        if group_info.group_id not in target_group_ids:
            continue

        # Subset the DataFrame to this group's rows
        group_df = reorder(self._tbl_data, group_info.indices, all_columns)

        # Calculate summary for each function
        for label, fn in fns.items():
            row_values_dict = _calculate_summary_row_from_subset(
                group_df, fn, fmt, self._boxhead._get_columns(), missing_text
            )

            summary_row_info = SummaryRowInfo(
                id=label,
                label=label,
                values=row_values_dict,
                side=side,
            )

            new_summary = new_summary.add_summary_row(
                summary_row_info, group_id=group_info.group_id
            )

    return self._replace(_summary_rows=new_summary)


def _calculate_summary_row_from_subset(
    group_df: TblData,
    fn: PlExpr | Callable[[TblData], Any],
    fmt: FormatFn | None,
    original_columns: list[str],
    missing_text: str,
) -> dict[str, Any]:
    """Calculate a summary row from a subset of data (for group summaries)."""
    summary_row = {}

    # Use eval_aggregate to apply the function/expression to the group subset
    result_df = eval_aggregate(group_df, fn)

    # Extract results for each column
    for col in original_columns:
        if col in result_df:
            res = result_df[col]

            if fmt is not None:
                formatted = fmt([res])
                res = formatted[0]

            summary_row[col] = res
        else:
            summary_row[col] = missing_text

    return summary_row


def grand_summary_rows(
    self: GTSelf,
    *,
    fns: dict[str, PlExpr] | dict[str, Callable[[TblData], Any]],
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
    cells by use of formatting expressions from the `vals.fmt_*` class of functions.

    Note that currently all arguments are keyword-only, since the final positions may change.

    Parameters
    ----------
    fns
        A dictionary mapping row labels to aggregation expressions. Can be either Polars
        expressions or callable functions that take the entire DataFrame and return aggregated
        results. Each key becomes the label for a grand summary row.
    fmt
        A formatting function from the `vals.fmt_*` family (e.g., `vals.fmt_number`,
        `vals.fmt_currency`) to apply to the summary row values. If `None`, no formatting
        is applied.
    columns
        Currently, this function does not support selection by columns. If you would like to choose
        which columns to summarize, you can select columns within the functions given to `fns=`.
        See examples below for more explicit cases.
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
    Let's use a subset of the `sp500` dataset to create a table with grand summary rows. We'll
    calculate min, max, and mean values for the numeric columns. Notice the different
    approaches to selecting columns to apply the aggregations to: we can use polars selectors
    or select the columns directly.

    ```{python}
    import polars as pl
    import polars.selectors as cs
    from great_tables import GT, vals, style, loc
    from great_tables.data import sp500

    sp500_mini = (
        pl.from_pandas(sp500)
        .slice(0, 7)
        .drop(["volume", "adj_close"])
    )

    (
        GT(sp500_mini, rowname_col="date")
        .grand_summary_rows(
            fns={
                "Minimum": pl.min("open", "high", "low", "close"),
                "Maximum": pl.col("open", "high", "low", "close").max(),
                "Average": cs.numeric().mean(),
            },
            fmt=vals.fmt_currency,
        )
        .tab_style(
            style=[
                style.text(color="crimson"),
                style.fill(color="lightgray"),
            ],
            locations=loc.grand_summary(),
        )
    )
    ```

    We can also use custom callable functions to create more complex summary calculations.
    Notice here that grand summary rows can be placed at the top of the table and formatted
    with currency notation, by passing a formatter from the `vals.fmt_*` class of functions.

    ```{python}
    from great_tables import GT, style, loc, vals
    from great_tables.data import gtcars

    def pd_median(df):
        return df.median(numeric_only=True)


    (
        GT(
            gtcars[["mfr", "model", "hp", "trq", "mpg_c"]].head(6),
            rowname_col="model",
        )
        .fmt_integer(columns=["hp", "trq", "mpg_c"])
        .grand_summary_rows(
            fns={
                "Min": lambda df: df.min(numeric_only=True),
                "Max": lambda df: df.max(numeric_only=True),
                "Median": pd_median,
            },
            side="top",
            fmt=vals.fmt_integer,
        )
        .tab_style(
            style=[style.text(color="crimson", weight="bold"), style.fill(color="lightgray")],
            locations=loc.grand_summary_stub(),
        )
    )
    ```

    """
    if columns is not None:
        raise NotImplementedError(
            "Currently, grand_summary_rows() does not support column selection."
        )

    # summary_col_names = resolve_cols_c(data=self, expr=columns)

    new_summary = self._summary_rows_grand
    for label, fn in fns.items():
        row_values_dict = _calculate_summary_row(self, fn, fmt, missing_text)

        summary_row_info = SummaryRowInfo(
            id=label,
            label=label,
            values=row_values_dict,
            side=side,
        )

        new_summary = new_summary.add_summary_row(summary_row_info)

    return self._replace(_summary_rows_grand=new_summary)


def _calculate_summary_row(
    data: GTData,
    fn: PlExpr | Callable[[TblData], Any],
    fmt: FormatFn | None,
    # summary_col_names: list[str],
    missing_text: str,
) -> dict[str, Any]:
    """Calculate a summary row using eval_transform."""
    original_columns = data._boxhead._get_columns()
    summary_row = {}

    # Use eval_aggregate to apply the function/expression to the data
    result_df = eval_aggregate(data._tbl_data, fn)

    # Extract results for each column
    for col in original_columns:
        if col in result_df:
            res = result_df[col]

            if fmt is not None:
                formatted = fmt([res])
                res = formatted[0]

            summary_row[col] = res
        else:
            summary_row[col] = missing_text

    return summary_row


# TODO: delegate to group by agg instead (group_by for summary row case)
# TODO: validates after
