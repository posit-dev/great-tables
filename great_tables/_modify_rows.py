from __future__ import annotations

from statistics import quantiles
from typing import TYPE_CHECKING, Literal

from great_tables._locations import resolve_cols_c

from ._gt_data import Locale, RowGroups, Styles
from ._tbl_data import (
    SelectExpr,
    copy_data,
    get_column_names,
    insert_row,
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


# def grand_summary_rows(
#     self: GTSelf,
#     fns: list[Literal["min", "max", "mean", "median"]] | Literal["min", "max", "mean", "median"],
#     columns: SelectExpr = None,
#     side: Literal["bottom", "top"] = "bottom",
# ) -> GTSelf:
#     new_body = self._body.copy()
#     new_tbl_data = new_body.body


#     new_body.append()

#     self._replace(_body=new_body)

#     return self


def grand_summary_rows(
    self: GTSelf,
    fns: list[Literal["min", "max", "mean", "median"]] | Literal["min", "max", "mean", "median"],
    columns: SelectExpr = None,
    side: Literal["bottom", "top"] = "bottom",
    missing_text: str = "---",
) -> GTSelf:
    if isinstance(fns, str):
        fns = [fns]

    tbl_data = self._tbl_data
    new_tbl_data = copy_data(tbl_data)

    original_column_names = get_column_names(tbl_data)

    summary_col_names = resolve_cols_c(data=self, expr=columns)

    # Create summary rows DataFrame
    for fn_name in fns:
        summary_row = []

        for col in original_column_names:
            if col in summary_col_names:
                col_data = to_list(tbl_data[col])

                if fn_name == "min":
                    new_cell = [min(col_data)]
                elif fn_name == "max":
                    new_cell = [max(col_data)]
                elif fn_name == "mean":
                    new_cell = [sum(col_data) / len(col_data)]
                elif fn_name == "median":
                    new_cell = [quantiles(col_data, n=2)]
                else:
                    # Should never get here
                    new_cell = ["hi"]
            else:
                new_cell = [None]

            summary_row += new_cell

        new_tbl_data = insert_row(new_tbl_data, summary_row, 0)

    # Concatenate based on side parameter
    # if side == "bottom":
    #     new_data = concat_frames(tbl_data, summary_df)
    # else:  # top
    #     new_data = concat_frames(summary_df, tbl_data)

    self = self._replace(_tbl_data=new_tbl_data)

    _row_group_info = self._boxhead._get_row_group_column()
    groupname_col = _row_group_info.var if _row_group_info is not None else None

    _row_name_info = self._boxhead._get_stub_column()
    rowname_col = _row_name_info.var if _row_name_info is not None else None

    stub, boxhead = self._stub._set_cols(self._tbl_data, self._boxhead, rowname_col, groupname_col)

    self._body.body = new_tbl_data

    return self._replace(_stub=stub, _boxhead=boxhead)
