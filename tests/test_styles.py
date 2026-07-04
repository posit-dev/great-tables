import pandas as pd
import polars as pl
from great_tables._styles import CellStyleText, CellStyleBorders, FromColumn
from great_tables._helpers import GoogleFont


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


def test_cell_style_text_with_google_font():
    style = CellStyleText(font=GoogleFont("Roboto"), color="red")

    res = style._to_html_style()

    assert res == "color: red;font-family: Roboto;"


def test_cell_style_text_google_font_no_spaces():
    style = CellStyleText(font=GoogleFont("Inter"))

    result = style._to_html_style()

    assert result == "font-family: Inter;"


def test_cell_style_text_google_font_has_spaces():
    style = CellStyleText(font=GoogleFont("Open Sans"), size="14px")

    result = style._to_html_style()

    assert "font-family: Open Sans;" in result
    assert "font-size: 14px;" in result


def test_cell_style_text_multiple_properties_with_google_font():
    style = CellStyleText(
        font=GoogleFont("IBM Plex Mono"),
        color="#333333",
        size="16px",
        weight="bold",
        align="center",
    )

    res = style._to_html_style()

    # Check that all defined CSS properties are present
    assert "font-family: IBM Plex Mono;" in res
    assert "color: #333333;" in res
    assert "font-size: 16px;" in res
    assert "font-weight: bold;" in res
    assert "text-align: center;" in res


def test_cell_style_text_invalid_font_type():
    style = CellStyleText(font=object())

    try:
        style._to_html_style()
    except ValueError as err:
        assert "Invalid font type" in str(err)
    else:
        raise AssertionError("Expected ValueError")


def test_tab_style_spanner_id_differs_from_label():
    # Regression test for #829: a style targeting a spanner by its `id` should be
    # applied to the spanner header cell, even when the `id` differs from the
    # displayed `label`.
    from great_tables import GT, loc, style

    df = pl.DataFrame({"a": [1], "b": [2]})
    gt_table = (
        GT(df)
        .tab_spanner(label="Displayed Group", id="internal_id", columns=["a", "b"])
        .tab_style(style=style.text(color="red"), locations=loc.spanner_labels(ids=["internal_id"]))
    )

    html = gt_table.as_raw_html()

    assert "color: red" in html


def test_tab_style_multilevel_spanner_id_differs_from_label():
    # Regression test for #829 covering higher-level (nested) spanners.
    from great_tables import GT, loc, style

    df = pl.DataFrame({"a": [1], "b": [2]})
    gt_table = (
        GT(df)
        .tab_spanner(label="Inner", id="inner_id", columns=["a", "b"])
        .tab_spanner(label="Outer", id="outer_id", columns=["a", "b"])
        .tab_style(style=style.text(color="red"), locations=loc.spanner_labels(ids=["outer_id"]))
    )

    html = gt_table.as_raw_html()

    assert "color: red" in html
