import pandas as pd


class Spanners:
    def __init__(self):

        # The `spanners` DataFrame is used to handle spanner ID
        # and text, the spanner level, the association to column names,
        # whether the spanner is to gather columns, and the built
        # form of the spanner label (depending on the output context)
        # 0: `vars` (empty list, str)
        # 1: `spanner_label` (empty list, str)
        # 2: `spanner_id` (empty, str)
        # 3: `spanner_level` (empty, int)
        # 4: `gather` (empty, bool)
        # 5: `built` (empty, str)

        self._spanners: pd.DataFrame = pd.DataFrame(
            columns=[
                "vars",
                "spanner_label",
                "spanner_id",
                "spanner_level",
                "gather",
                "built",
            ]
        )


class SpannersAPI:
    _spanners: Spanners

    def __init__(self):
        self._spanners = Spanners()
