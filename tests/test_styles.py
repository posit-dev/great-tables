import pandas as pd
import polars as pl
from great_tables._styles import CellStyleText, CellStyleBorders, FromColumn


def test_from_column_replace():
    """FromColumn is replaced by the specified column's value in a row of data"""

    df = pd.DataFrame({"x": [1, 2], "color": ["red", "blue"]})
    from_col = FromColumn("color")

    style = CellStyleText(color=from_col)
    new_style = style._from_row(df, 0)

    assert style.color is from_col
    assert new_style.color == "red"


def test_from_column_fn():
    df = pd.DataFrame({"x": [1, 2], "color": ["red", "blue"]})
    from_col = FromColumn("color", fn=lambda x: x.upper())

    style = CellStyleText(color=from_col)
    new_style = style._from_row(df, 0)

    assert new_style.color == "RED"


def test_cell_value_from_function():
    df = pd.DataFrame({"x": [1, 2], "color": ["red", "blue"]})

    style = CellStyleText(color=lambda D: D["color"].str.upper())
    new_style = style._evaluate_expressions(df)._from_row(df, 0)

    assert new_style.color == "RED"


def test_cell_value_from_polars_expr():
    df = pl.DataFrame({"x": [1, 2], "color": ["red", "blue"]})

    style = CellStyleText(color=pl.col("color").str.to_uppercase())
    new_style = style._evaluate_expressions(df)._from_row(df, 0)

    assert new_style.color == "RED"


def test_cell_style_borders_all():
    res = CellStyleBorders(sides=["all"], color="blue")._to_html_style()
    assert res.split(";") == [
        "border-top: 1px solid blue",
        "border-bottom: 1px solid blue",
        "border-left: 1px solid blue",
        "border-right: 1px solid blue",
        "",
    ]
