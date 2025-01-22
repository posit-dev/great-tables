import pandas as pd
import polars as pl
import pytest
from great_tables import GT, style, loc, google_font, from_column
from great_tables._locations import LocBody
from great_tables._styles import CellStyleFill
from great_tables._tab_create_modify import tab_style
from polars import selectors as cs


@pytest.fixture
def gt():
    return GT(pd.DataFrame({"x": [1, 2], "y": [4, 5]}))


@pytest.fixture
def gt2():
    return GT(pl.DataFrame({"x": [1, 2], "y": [4, 5]}))


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


def test_tab_style_loc_body_mask(gt2: GT):
    style = CellStyleFill(color="blue")
    new_gt = tab_style(gt2, style, LocBody(mask=cs.numeric().gt(1.5)))

    assert len(gt2._styles) == 0
    assert len(new_gt._styles) == 3

    xy_0y, xy_1x, xy_1y = new_gt._styles

    assert xy_0y.styles[0] is style
    assert xy_1x.styles[0] is style
    assert xy_1y.styles[0] is style

    assert xy_0y.rownum == 0
    assert xy_0y.colname == "y"

    assert xy_1x.rownum == 1
    assert xy_1x.colname == "x"

    assert xy_1y.rownum == 1
    assert xy_1y.colname == "y"


def test_tab_style_loc_body_raises(gt2: GT):
    style = CellStyleFill(color="blue")
    mask = cs.numeric().gt(1.5)
    err_msg = "Cannot specify the `mask` argument along with `columns` or `rows` in `loc.body()`."

    with pytest.raises(ValueError) as exc_info:
        tab_style(gt2, style, LocBody(columns=["x"], mask=mask))
    assert err_msg in exc_info.value.args[0]

    with pytest.raises(ValueError) as exc_info:
        tab_style(gt2, style, LocBody(rows=[0], mask=mask))

    assert err_msg in exc_info.value.args[0]


def test_tab_style_loc_body_mask_not_polars_expression_raises(gt2: GT):
    style = CellStyleFill(color="blue")
    mask = "fake expression"
    err_msg = "Only Polars expressions can be passed to the `mask` argument."

    with pytest.raises(ValueError) as exc_info:
        tab_style(gt2, style, LocBody(mask=mask))
    assert err_msg in exc_info.value.args[0]


def test_tab_style_loc_body_mask_columns_not_inside_raises(gt2: GT):
    style = CellStyleFill(color="blue")
    mask = pl.len()
    err_msg = (
        "The `mask` expression produces extra columns, with names not in the original DataFrame."
    )

    with pytest.raises(ValueError) as exc_info:
        tab_style(gt2, style, LocBody(mask=mask))
    assert err_msg in exc_info.value.args[0]


def test_tab_style_loc_body_mask_rows_not_equal_raises(gt2: GT):
    style = CellStyleFill(color="blue")
    mask = pl.len().alias("x")
    err_msg = "The DataFrame length after applying `mask` differs from the original."

    with pytest.raises(ValueError) as exc_info:
        tab_style(gt2, style, LocBody(mask=mask))
    assert err_msg in exc_info.value.args[0]
