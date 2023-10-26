from __future__ import annotations

from typing import TYPE_CHECKING
from .utils_render_common import get_row_reorder_df


if TYPE_CHECKING:
    from ._gt_data import Body, RowGroups, Stub, Boxhead


def body_reassemble(body: Body, row_groups: RowGroups, stub_df: Stub, boxhead: Boxhead) -> Body:
    cols = [col_info.var for col_info in boxhead]
    start_final = get_row_reorder_df(row_groups, stub_df)
