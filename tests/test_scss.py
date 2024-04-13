import pytest
import pandas as pd

from great_tables import GT
from great_tables._scss import font_color, css_add, compile_scss


@pytest.mark.parametrize(
    "src,dst,table_font_color,table_font_color_light",
    [
        ("#FFFFFF", "#000000", "#000000", "#FFFFFF"),
        ("#000000", "#FFFFFF", "black", "white"),
        ("white", "#000000", "#000000", "#FFFFFF"),
        ("black", "#FFFFFF", "black", "white"),
        ("silver", "#000000", "#000000", "#FFFFFF"),
        ("transparent", "#000000", "#000000", "#FFFFFF"),
        ("transparent", "black", "black", "white"),
        ("currentcolor", "currentcolor", "#000000", "#FFFFFF"),
        ("currentColor", "currentcolor", "black", "white"),
    ],
)
def test_font_color(src, dst, table_font_color, table_font_color_light):
    res = font_color(src, table_font_color, table_font_color_light)
    assert res == dst



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
