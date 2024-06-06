from __future__ import annotations

from typing import TYPE_CHECKING

from ._tbl_data import copy_data

if TYPE_CHECKING:
    from ._gt_data import Body, Boxhead, RowGroups, Stub


def body_reassemble(body: Body, stub_df: Stub, boxhead: Boxhead) -> Body:
    # Note that this used to order the body based on groupings, but now that occurs in the
    # renderer itself.
    return body.__class__(copy_data(body.body))
