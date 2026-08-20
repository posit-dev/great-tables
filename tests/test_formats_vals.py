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


def test_val_fmt_engineering_single():
    result = vals.fmt_engineering(1234.5, decimals=2)
    assert result == ["1.23 × 10<sup style='font-size: 65%;'>3</sup>"]


def test_val_fmt_engineering_multiple():
    result = vals.fmt_engineering([1234.5, 0.000123, 1e6], decimals=2)
    assert result == [
        "1.23 × 10<sup style='font-size: 65%;'>3</sup>",
        "123.00 × 10<sup style='font-size: 65%;'>−6</sup>",
        "1.00 × 10<sup style='font-size: 65%;'>6</sup>",
    ]


def test_val_fmt_to_expression():
    expr = vals.fmt_integer(pl.col("x"))
    assert isinstance(expr, pl.Expr)

    res = pl.DataFrame({"x": [1.23]}).select(expr)
    assert res[0, "x"] == "1"


def test_val_fmt_number():
    assert vals.fmt_number(1234.567, decimals=3) == ["1,234.567"]
    assert vals.fmt_number([0, 1000000], decimals=0) == ["0", "1,000,000"]


def test_val_fmt_integer():
    assert vals.fmt_integer(42) == ["42"]
    assert vals.fmt_integer([0, -5, 1000]) == ["0", "−5", "1,000"]


def test_val_fmt_scientific():
    result = vals.fmt_scientific(12345.678, decimals=3)
    assert len(result) == 1
    assert "×" in result[0]


def test_val_fmt_percent():
    assert vals.fmt_percent(0.25) == ["25.00%"]
    assert vals.fmt_percent([0.1, 0.5], decimals=0) == ["10%", "50%"]


def test_val_fmt_partsper():
    result = vals.fmt_partsper(0.001, to_units="per-mille")
    assert len(result) == 1


def test_val_fmt_currency():
    result = vals.fmt_currency(9.99, currency="USD")
    assert "$" in result[0]
    assert "9.99" in result[0]


def test_val_fmt_roman():
    assert vals.fmt_roman(4) == ["IV"]
    assert vals.fmt_roman([1, 10, 50]) == ["I", "X", "L"]


def test_val_fmt_bytes():
    result = vals.fmt_bytes(1024)
    assert len(result) == 1
    assert "B" in result[0]


def test_val_fmt_duration():
    result = vals.fmt_duration(3661, input_units="seconds")
    assert len(result) == 1


def test_val_fmt_date():
    result = vals.fmt_date("2023-06-15")
    assert result == ["2023-06-15"]


def test_val_fmt_time():
    result = vals.fmt_time("14:30:00")
    assert result == ["14:30:00"]


def test_val_fmt_markdown():
    result = vals.fmt_markdown("**bold**")
    assert result == ["<strong>bold</strong>"]


def test_val_fmt_number_si():
    result = vals.fmt_number_si(1500)
    assert "k" in result[0] or "1" in result[0]
