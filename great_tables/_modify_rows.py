from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, ClassVar, Literal, TypedDict, TypeVar, cast

from ._gt_data import GTData, Locale, Options, RowGroups, Spanners, Stub, Boxhead, Styles

if TYPE_CHECKING:
    from ._types import GTSelf


def row_group_order(self: GTSelf, groups: RowGroups) -> GTSelf:
    new_stub = self._stub.order_groups(groups)

    return self._replace(_stub=new_stub)


def _remove_from_body_styles(styles: Styles, column: str) -> Styles:
    # TODO: refactor
    from ._utils_render_html import _is_loc
    from ._locations import LocBody

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

    Setting a default locale affects formatters like .fmt_number, and .fmt_date,
    by having them default to locale-specific features (e.g. representing one thousand
    as 1.000,00)
    """

    return self._replace(_locale=Locale(locale))


def with_id(self: GTSelf, id: str | None = None) -> GTSelf:
    """Set the id for this table.

    Note that this is a shortcut for the `table_id=` argument in `GT.tab_options()`.
    """
    return self._replace(_options=self._options._set_option_value("table_id", id))
