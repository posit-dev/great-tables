import pandas as pd

from great_tables._styles import FromColumn, CellStyleText


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
