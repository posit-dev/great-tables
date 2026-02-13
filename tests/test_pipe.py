from __future__ import annotations

import polars as pl

from great_tables import GT

from great_tables._text import BaseText
from great_tables._tbl_data import SelectExpr


def test_pipe() -> None:
    columns = ["x", "y"]
    label = "a spanner"
    df = pl.DataFrame({"x": [1, 2, 3], "y": [3, 2, 1]})

    def tab_spanner2(gt: GT, label: str | BaseText, columns: SelectExpr) -> GT:
        return gt.tab_spanner(label=label, columns=columns)

    gt1 = GT(df).tab_spanner(label, columns=columns)
    gt2 = GT(df).pipe(tab_spanner2, label, columns=columns)

    assert len(gt1._spanners) == len(gt2._spanners)
