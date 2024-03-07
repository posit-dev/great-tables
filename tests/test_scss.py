import pytest
import pandas as pd

from great_tables import GT
from great_tables._scss import _font_color, _css_add, _compile_scss


@pytest.mark.parametrize(
    "src,dst",
    [
        ("#FFFFFF", "#000000"),
        ("#000000", "#FFFFFF"),
        ("white", "#000000"),
    ],
)
def test_font_color(src, dst):
    res = _font_color(src, "#000000", "#FFFFFF")
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
    res = _css_add(src, 1)
    assert res == dst


def test_scss_default_generated(snapshot):
    # we're using this just to generate the css
    gt = GT(pd.DataFrame({"x": [1, 2, 3]}))

    assert snapshot == _compile_scss(gt, id="abc", compress=False)
