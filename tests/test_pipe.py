import polars as pl
from great_tables import GT, loc, style


def test_pipe():
    columns = ["x", "y"]
    colors = ["lightgray", "lightblue"]
    df = pl.DataFrame(dict(zip(columns, [[1, 2, 3], [3, 2, 1]])))

    gt1 = (
        GT(df)
        .tab_style(
            style=style.fill(color=colors[0]),
            locations=loc.body(
                columns=columns[0], rows=pl.col(columns[0]).eq(pl.col(columns[0]).max())
            ),
        )
        .tab_style(
            style=style.fill(color=colors[1]),
            locations=loc.body(
                columns=columns[1], rows=pl.col(columns[1]).eq(pl.col(columns[1]).max())
            ),
        )
    )

    def tbl_style(gtbl: GT, columns: list[str], colors: list[str]) -> GT:
        for column, color in zip(columns, colors):
            gtbl = gtbl.tab_style(
                style=style.fill(color=color),
                locations=loc.body(columns=column, rows=pl.col(column).eq(pl.col(column).max())),
            )
        return gtbl

    gt2 = GT(df).pipe(tbl_style, columns, colors)  # check *args
    gt3 = GT(df).pipe(tbl_style, columns=columns, colors=colors)  # check **kwargs

    assert gt1._styles == gt2._styles == gt3._styles
