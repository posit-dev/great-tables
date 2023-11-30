from __future__ import annotations
from ._gt_data import Stub, RowGroups
from .utils_render_common import get_row_reorder_df


def reorder_stub_df(stub_df: Stub, row_groups: RowGroups) -> Stub:
    """
    Reorders the components of the stub object based on the given row groups.

    Args:
        stub_df (Stub): The stub object to be reordered.
        row_groups (RowGroups): The row groups used for reordering.

    Returns:
        Stub: The reordered stub object.
    """
    start_final = get_row_reorder_df(row_groups, stub_df)

    stub_df = stub_df[[final for _, final in start_final]]

    return stub_df
