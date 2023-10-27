from __future__ import annotations

from typing import TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    from ._gt_data import RowGroups, Stub


TupleStartFinal = Tuple[int, int]


def get_row_reorder_df(groups: RowGroups, stub_df: Stub) -> list[TupleStartFinal]:
    if not len(groups):
        indices = range(len(stub_df))

        # TODO: is this used in indexing? If so, we may need to use
        # ii + 1 for the final part?
        return [(ii, ii) for ii in indices]

    # where in the group each element is
    groups_pos = [groups.index(row.group_id) for row in stub_df]
    # the index that when used on the rows will sort them by the order in groups
    start_pos = list(range(len(groups_pos)))
    sort_indx = sorted(start_pos, key=lambda ii: groups_pos[ii])

    return list(zip(start_pos, sort_indx))
