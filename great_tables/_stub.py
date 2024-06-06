from __future__ import annotations

from ._gt_data import RowGroups, Stub
from .utils_render_common import get_row_reorder_df


def reorder_stub_df(stub_df: Stub) -> Stub:
    """
    Reorders the components of the stub object based on the given row groups.

    Args:
        stub_df (Stub): The stub object to be reordered.
        row_groups (RowGroups): The row groups used for reordering.

    Returns:
        Stub: The reordered stub object.
    """

    # NOTE: the original R package reordered stub rows, and returned a new GT object.
    # However, since the final order is determined by the groups, we use those to
    # determine the final order, just before rendering

    # start_final = get_row_reorder_df(stub_df)
    # stub_df = stub_df.reorder_rows([final for _, final in start_final])

    return stub_df
