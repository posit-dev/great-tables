import pandas as pd
import pytest
from great_tables import GT, style, loc, google_font
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
        locations=loc.body(columns="time"),
    )

    rendered_html = new_gt.as_raw_html()

    assert rendered_html.find(
        "@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');"
    )
    assert rendered_html.find("font-family: IBM Plex Mono;")
