from __future__ import annotations

from typing import TYPE_CHECKING
from .utils_render_common import get_row_reorder_df
from ._tbl_data import reorder


if TYPE_CHECKING:
    from ._gt_data import Body, RowGroups, Stub, Boxhead


def body_reassemble(body: Body, row_groups: RowGroups, stub_df: Stub, boxhead: Boxhead) -> Body:
    cols = [col_info.var for col_info in boxhead]

    start_final = get_row_reorder_df(row_groups, stub_df)
    rows = [final for _, final in start_final]

    # TODO: once body is just a DataFrame, we can call reorder directly on it
    return body.__class__(reorder(body.body, rows, cols))
