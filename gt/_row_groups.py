from typing import Optional


class RowGroups:
    row_groups: Optional[str]

    def __init__(self):
        pass


class RowGroupsAPI:
    _row_groups: RowGroups

    def __init__(self):
        self._row_groups = RowGroups()
