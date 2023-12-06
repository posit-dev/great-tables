import pytest

from great_tables._scss import font_color


@pytest.mark.parametrize(
    "src,dst",
    [
        ("#FFFFFF", "dark"),
        ("#000000", "light"),
        ("white", "dark"),
    ],
)
def test_font_color(src, dst):
    res = font_color(src, "dark", "light")
    assert res == dst
