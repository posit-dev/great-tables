from __future__ import annotations

from typing import TYPE_CHECKING

from typing_extensions import TypeAlias

if TYPE_CHECKING:
    from ._gt_data import RowGroups, Stub


TupleStartFinal: TypeAlias = tuple[int, int]


def get_row_reorder_df(stub_df: Stub, groups: RowGroups | None = None) -> list[TupleStartFinal]:
    # TODO: this function should be removed, since the stub generates indices directly.

    if groups is None:
        groups = stub_df.group_ids

    # Get the number of non-None entries in the `groupname_col`
    n_stub_entries = len([entry for entry in stub_df.rows if entry.group_id is not None])

    # Raise a ValueError if there are row group entries but no RowGroups
    if n_stub_entries and not len(groups):
        raise ValueError(f"Detected {n_stub_entries} but only {len(groups)} row groups.")

    # If there aren't any row groups then return a list of tuples that don't lead
    # to any resorting later on (e.g., `[(0, 0), (1, 1), (2, 2) ... (n, n)]`)
    if not len(groups):
        indices = range(len(stub_df.rows))

        # TODO: is this used in indexing? If so, we may need to use
        # ii + 1 for the final part?
        return [(ii, ii) for ii in indices]

    # where in the group each element is
    # TODO: this doesn't yield consistent values
    groups_pos = [
        groups.index(row.group_id) if row.group_id is not None else -1 for row in stub_df.rows
    ]

    # From running test_body_reassemble():
    # print(groups_pos)
    # [0, 1, 0, 1] <- correct
    # [1, 0, 1, 0] <- wrong

    # the index that when used on the rows will sort them by the order in groups
    start_pos = range(len(groups_pos))
    sort_indx = sorted(start_pos, key=lambda ii: groups_pos[ii])

    # From running test_body_reassemble():
    # [(0, 0), (1, 2), (2, 1), (3, 3)] <- correct
    # [(0, 1), (1, 3), (2, 0), (3, 2)] <- wrong
    return list(zip(start_pos, sort_indx))
