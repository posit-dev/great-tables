from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, ClassVar, Literal, TypedDict, TypeVar, cast

from ._gt_data import GTData, Locale, Options, RowGroups, Spanners, Stub, Boxhead, Styles

if TYPE_CHECKING:
    from ._types import GTSelf


def row_group_order(self: GTSelf, groups: RowGroups):
    new_stub = self._stub.order_groups(groups)

    return self._replace(_stub=new_stub)


def _remove_from_body_styles(styles: Styles, column: str) -> Styles:
    new_styles = [
        info for info in styles if not (info.locname == "data" and info.colname == column)
    ]

    return new_styles


def _remove_from_group_styles(styles: Styles, column: str):
    # TODO(#341): once group styles are supported, will need to wire this up.
    return list(styles)


def with_rowname_col(self: GTSelf, column: str | None = None):
    """Set a column to be the rownames in the table stub."""

    # in case it was the groupname_col, need to remove group styles ----
    if column is not None:
        self = self._replace(_styles=_remove_from_group_styles(self._styles, column))

    # remove from spanners ----
    if column is not None:
        self = self._replace(_spanners=self._spanners.remove_column(column))

    # get existing groupname column ----
    _info = self._boxhead._get_row_group_column()
    groupname_col = _info.var if _info is not None else None

    stub, boxhead = self._stub._set_cols(self._tbl_data, self._boxhead, column, groupname_col)

    return self._replace(_stub=stub, _boxhead=boxhead)


def with_groupname_col(self: GTSelf, column: str = None):
    """Set a column to be the groupnames in the table stub."""

    # remove any table body styles ----
    if column is not None:
        self = self._replace(_styles=_remove_from_body_styles(self._styles, column))

    # remove from spanners ----
    if column is not None:
        self = self._replace(_spanners=self._spanners.remove_column(column))

    # get existing rowname column ----
    _info = self._boxhead._get_stub_column()
    rowname_col = _info.var if _info is not None else None

    stub, boxhead = self._stub._set_cols(self._tbl_data, self._boxhead, rowname_col, column)

    return self._replace(_stub=stub, _boxhead=boxhead)


def with_locale(self: GTSelf, locale: str | None = None):
    """Set a column to be the locale."""

    return self._replace(_locale=Locale(locale))


def with_id(self: GTSelf, id: str | None = None):
    return self._replace(_options=self._options._set_option_value("table_id", id))
