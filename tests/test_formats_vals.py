import base64
import polars as pl
from pathlib import Path
from importlib_resources import files

import pytest
from great_tables import vals


@pytest.fixture
def img_paths():
    return files("great_tables") / "data/metro_images"


def test_locate_val_fmt_image(img_paths: Path):
    imgs = vals.fmt_image("1", path=img_paths, file_pattern="metro_{}.svg")
    with open(img_paths / "metro_1.svg", "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    assert encoded in imgs[0]


def test_val_fmt_image_single(img_paths: Path):
    imgs = vals.fmt_image("1", path=img_paths, file_pattern="metro_{}.svg")
    assert 'img src="data:image/svg+xml;base64' in imgs[0]


def test_val_fmt_image_multiple(img_paths: Path):
    img1, img2 = vals.fmt_image(["1", "2"], path=img_paths, file_pattern="metro_{}.svg")

    assert 'img src="data:image/svg+xml;base64' in img1
    assert 'img src="data:image/svg+xml;base64' in img2


def test_val_fmt_to_expression():
    expr = vals.fmt_integer(pl.col("x"))
    assert isinstance(expr, pl.Expr)

    res = pl.DataFrame({"x": [1.23]}).select(expr)
    assert res[0, "x"] == "1"
