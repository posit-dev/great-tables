from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ._gt_data import GroupRows
from ._tbl_data import _get_cell, is_na

if TYPE_CHECKING:
    from ._gt_data import Body, ColInfo, Stub, TblData


def update_group_row_labels(
    stub: Stub,
    body: Body,
    tbl_data: TblData,
    rowgroup_var: ColInfo,
) -> Stub:
    """Update group row labels in `stub` using formatted values from `body`.

    For each group in `stub.group_rows`, the formatted cell value for the
    first row of the group is looked up in `body`. If the cell was not
    formatted (i.e., it is still NA), the original value from `tbl_data` is
    used instead. A new `Stub` with updated `group_rows` is returned and the
    original `stub` is not mutated.

    Parameters
    ----------
    stub
        The current stub containing group row information.
    body
        The rendered body whose cells may contain formatted values.
    tbl_data
        The original (unformatted) source data.
    rowgroup_var
        Column metadata identifying the row-group column.

    Returns
    -------
    Stub
        A copy of ``stub`` with group labels replaced by formatted values.
    """
    new_group_rows: list[Any] = []

    for group_row in stub.group_rows:
        first_index = group_row.indices[0]
        cell_content = _get_cell(body.body, first_index, rowgroup_var.var)

        # When no formatter was applied, the cell is still NA -- fall back to the
        # original data value.
        if is_na(tbl_data, cell_content):
            cell_content = _get_cell(tbl_data, first_index, rowgroup_var.var)

        new_group_rows.append(group_row.with_group_label(cell_content))

    stub.group_rows = GroupRows(new_group_rows)
    return stub
