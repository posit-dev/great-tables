"""Row details: what each data row shows under it when the reader opens it (`GTI.i_row_details()`).

Each row's details are rendered here, as HTML, which the table's `<gt-table>` element has in a
`<template>` per row (inert until it's opened, and not shown without the runtime); the spec says
which rows have them.
"""

from __future__ import annotations

import math
from typing import TYPE_CHECKING, Any

from .._gt_data import ColInfoTypeEnum
from .._tbl_data import _get_column_values, get_column_names
from .._text import BaseText, _process_text
from ._settings import settings_of

if TYPE_CHECKING:
    from .._gt_data import GTData
    from ..gt import GT


def render_details(data: GTData) -> dict[int, str]:
    """Each data row's details, as HTML, by the row's index (rows without any are left out)."""
    content = settings_of(data).row_details
    if content is None:
        return {}
    tbl_data = data._tbl_data
    if isinstance(content, str):
        made = enumerate(_get_column_values(tbl_data, content))
    else:
        # (Each row's values as the data has them, by column, as the function gets them)
        names = get_column_names(tbl_data)
        columns = [_get_column_values(tbl_data, name) for name in names]
        rows = [dict(zip(names, cells)) for cells in zip(*columns)] if names else []
        made = enumerate(content(values) for values in rows)

    details: dict[int, str] = {}
    for row, value in made:
        html = _details_html(value, row, content)
        if html is not None:
            details[row] = html
    return details


def details_template(row: int, html: str) -> str:
    return f'<template data-gti-details="{row}">{html}</template>\n'


def leave_out_details_column(gt: GT) -> GT:
    """Leave the column holding the rows' details (if they're in one) out of the table, as
    `cols_hide()` does."""
    column = settings_of(gt).row_details
    if not isinstance(column, str):
        return gt
    boxhead = gt._boxhead
    for kind in (ColInfoTypeEnum.stub, ColInfoTypeEnum.row_group):
        if column in boxhead.vars_from_type(kind):
            raise ValueError(
                f"The stub and the row group column can't hold the rows' details, as they're in "
                f"the table, so `i_row_details()` can't have {column!r}."
            )
    boxhead = boxhead.set_cols_hidden([column])
    if not boxhead._get_default_columns() and not boxhead._get_stub_columns():
        raise ValueError(
            f"A table without a stub needs a column other than the one with the rows' details "
            f"({column!r}), which is left out of it."
        )
    return gt._replace(_boxhead=boxhead)


def _details_html(value: Any, row: int, content: Any) -> str | None:
    """A row's details as HTML, or `None` for none: a table (`GT`), text (`html()`, `md()`, or a
    string, shown as text), or nothing (`None`, a missing value, or an empty string)."""
    from ..gt import GT
    from ..gti import GTI

    if _is_missing(value) or (isinstance(value, str) and value == ""):
        return None
    if isinstance(value, GT):
        if isinstance(value, GTI) or value._options.ihtml_active.value:
            raise ValueError(
                f"Row {row}'s details are an interactive table, which can't be in a row's "
                "details: use a `GT` table, without `opt_interactive()`."
            )
        return value._build_data(context="html")._render_as_html()
    if isinstance(value, (str, BaseText)):
        return _process_text(value)
    source = (
        f"The `{content}` column" if isinstance(content, str) else "The `i_row_details()` function"
    )
    raise TypeError(
        f"{source} gave {type(value).__name__!r} for row {row}'s details, which must be a `GT` "
        "table, `html()` or `md()` text, a string, or `None` (no details)."
    )


def _is_missing(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, float):
        return math.isnan(value)
    # (pandas' NA and NaT)
    return type(value).__name__ in ("NAType", "NaTType")
