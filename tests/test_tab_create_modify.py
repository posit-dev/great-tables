import pandas as pd
import polars as pl
import pytest
from great_tables import GT, style, loc, google_font, from_column
from great_tables._locations import LocBody
from great_tables._styles import CellStyleFill
from great_tables._tab_create_modify import tab_style


@pytest.fixture
def gt():
    return GT(pd.DataFrame({"x": [1, 2], "y": [4, 5]}))


def test_tab_style(gt: GT):
    style = CellStyleFill(color="blue")
    new_gt = tab_style(gt, style, LocBody(["x"], [0]))

    assert len(gt._styles) == 0
    assert len(new_gt._styles) == 1

    assert len(new_gt._styles[0].styles) == 1
    assert new_gt._styles[0].styles[0] is style


def test_tab_style_multiple_columns(gt: GT):
    style = CellStyleFill(color="blue")
    new_gt = tab_style(gt, style, LocBody(["x", "y"], [0]))

    assert len(new_gt._styles) == 2

    assert len(new_gt._styles[0].styles) == 1
    assert new_gt._styles[0].styles[0] is style


def test_tab_style_google_font(gt: GT):

    new_gt = tab_style(
        gt,
        style=style.text(font=google_font(name="IBM Plex Mono")),
        locations=loc.body(columns="x"),
    )

    rendered_html = new_gt.as_raw_html()

    assert rendered_html.find(
        "@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');"
    )
    assert rendered_html.find("font-family: IBM Plex Mono;")


def test_tab_style_font_local(gt: GT):

    new_gt = tab_style(
        gt,
        style=style.text(font="Courier"),
        locations=loc.body(columns="x"),
    )

    rendered_html = new_gt.as_raw_html()

    assert rendered_html.find('<td style="font-family: Courier;" class="gt_row gt_right">1</td>')


def test_tab_style_font_from_column():

    tbl = pl.DataFrame({"x": [1, 2], "font": ["Helvetica", "Courier"]})

    gt_tbl = GT(tbl).tab_style(
        style=style.text(font=from_column(column="font")), locations=loc.body(columns="x")
    )

    rendered_html = gt_tbl.as_raw_html()

    assert rendered_html.find('<td style="font-family: Helvetica;" class="gt_row gt_right">1</td>')
    assert rendered_html.find('<td style="font-family: Courier;" class="gt_row gt_right">2</td>')
