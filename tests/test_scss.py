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
