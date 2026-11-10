import re

import pytest
import pandas as pd

from great_tables import GT
from great_tables._scss import font_color, css_add, compile_scss


@pytest.mark.parametrize(
    "src,dst",
    [
        ("#FFFFFF", "#000000"),
        ("#000000", "#FFFFFF"),
        ("white", "#000000"),
        ("black", "#FFFFFF"),
        ("silver", "#000000"),
        ("transparent", "#000000"),
        ("currentcolor", "currentcolor"),
        ("currentColor", "currentcolor"),
    ],
)
def test_font_color(src, dst):
    res = font_color(src, "#000000", "#FFFFFF")
    assert res == dst


@pytest.mark.parametrize(
    "src, dst",
    [
        ("transparent", "#000000"),
        ("currentColor", "currentcolor"),
        ("black", "#FFFFFF"),
    ],
)
def test_font_color_normalizes_table_color_names(src, dst):
    assert font_color(src, "black", "white") == dst


@pytest.mark.parametrize(
    "src,dst",
    [
        ("1px", "2px"),
        ("1%", "2%"),
        (1, 2),
    ],
)
def test_css_add(src: "str | int", dst: "str | int"):
    res = css_add(src, 1)
    assert res == dst


def test_scss_default_generated(snapshot):
    # we're using this just to generate the css
    gt = GT(pd.DataFrame({"x": [1, 2, 3]}))

    assert snapshot == compile_scss(gt, id="abc", compress=False)


def test_compile_scss_no_font_names():
    """compile_scss works when table_font_names is None (font_family_attr becomes empty string)."""
    gt = GT(pd.DataFrame({"x": [1, 2]})).tab_options(table_font_names=None)
    css = compile_scss(gt, id="abc", compress=False)
    # Should produce CSS without a font-family rule
    assert isinstance(css, str)
    assert len(css) > 0


def _css_rule(css: str, selector: str) -> str:
    return re.search(rf"{re.escape(selector)} \{{(.*?)\}}", css, re.DOTALL).group(1)


@pytest.mark.parametrize(
    "options, padding_bottom",
    [
        ({}, "6px"),
        ({"column_labels_padding": "20px"}, "21px"),
        ({"heading_padding": "20px"}, "6px"),
    ],
)
def test_column_labels_padding_bottom(options: dict, padding_bottom: str):
    # As in gt, the column labels' bottom padding is `column_labels_padding` plus 1px
    gt = GT(pd.DataFrame({"x": [1, 2]})).tab_options(**options)
    rule = _css_rule(compile_scss(gt, id="abc", compress=False), "#abc .gt_col_heading")

    assert f"padding-bottom: {padding_bottom};" in rule


@pytest.mark.parametrize("background, color", [("#FFFFFF", "#333333"), ("#000000", "#FFFFFF")])
def test_footnotes_font_color(background: str, color: str):
    gt = GT(pd.DataFrame({"x": [1, 2]})).tab_options(table_background_color=background)
    css = compile_scss(gt, id="abc", compress=False)

    assert "font-color(" not in css
    assert f"color: {color};" in _css_rule(css, "#abc .gt_footnotes")
