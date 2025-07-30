import math
from contextlib import nullcontext
from typing import Any

import narwhals.stable.v2 as nw
import numpy as np
import pytest
from great_tables._data_color.base import (
    _add_alpha,
    _color_name_to_hex,
    _expand_short_hex,
    _float_to_hex,
    _get_domain_factor,
    _get_domain_numeric,
    _get_wcag_contrast_ratio,
    _hex_to_rgb,
    _html_color,
    _ideal_fgnd_color,
    _is_hex_col,
    _is_short_hex,
    _is_standard_hex_col,
    _relative_luminance,
    _remove_alpha,
    _rescale_numeric,
    _srgb,
)
from great_tables._data_color.palettes import GradientPalette

from tests.utils import SeriesConstructor, assert_series_equal


@pytest.mark.parametrize(
    ("bgnd_color", "fgnd_color"),
    [
        ("#FFFFFF", "#000000"),  # White background color -> Expected dark foreground color
        ("#000000", "#FFFFFF"),  # Black background color -> Expected light foreground color
    ],
)
def test_ideal_fgnd_color_contrast(bgnd_color: str, fgnd_color: str) -> None:
    assert _ideal_fgnd_color(bgnd_color) == fgnd_color


@pytest.mark.parametrize(
    ("bgnd_color", "light_color", "dark_color", "fgnd_color"),
    [
        (
            "#FF0000",  # Red background color
            "#00FF00",  # Green light color
            "#0000FF",  # Blue dark color
            "#00FF00",  # Expected custom light foreground color
        ),
        (
            "#FF0000FF",  # Red background color with alpha
            "#00FF00",  # Green light color
            "#0000FF",  # Blue dark color
            "#00FF00",  # Expected custom light foreground color
        ),
        (
            "#FF0000",  # Red background color
            "#00FF00",  # Green light color
            "#0000FF",  # Blue dark color
            "#00FF00",  # Expected custom light foreground color
        ),
        (
            "#FF0000FF",  # Red background color with alpha
            "#00FF00",  # Green light color
            "#0000FF",  # Blue dark color
            "#00FF00",  # Expected custom light foreground color
        ),
    ],
)
def test_ideal_fgnd_color_custom_contrast(
    bgnd_color: str, fgnd_color: str, light_color: str, dark_color: str
) -> None:
    assert _ideal_fgnd_color(bgnd_color, light=light_color, dark=dark_color) == fgnd_color


@pytest.mark.parametrize(
    ("color_1", "color_2", "contrast_ratio"),
    [
        ("#FFFFFF", "#000000", 21.0),  # Colors: (White, Black) -> high contrast ratio
        ("#FF0000", "#00FF00", 2.9139375476009137),  # colors: (Red, Green) -> low contrast ratio
        (
            "#FF0000FF",
            "#00FF00",
            2.9139375476009137,
        ),  # colors: (Red with alpha, Green) -> Contrast ratio unchanged with alpha
        (
            "#FF0000",
            "#FF0000",
            1.0,
        ),  # colors: (Red, Red) -> Contrast ratio always 1.0 for same color
        (
            "#FF0000FF",
            "#FF0000FF",
            1.0,
        ),  # colors: (Red with alpha, Red with alpha) -> Contrast ratio unchanged with alpha
    ],
)
def test_get_wcag_contrast_ratio(color_1: str, color_2: str, contrast_ratio: float) -> None:
    assert _get_wcag_contrast_ratio(color_1, color_2) == contrast_ratio


@pytest.mark.parametrize(
    ("hex_color", "rgb"),
    [
        ("#FF0000", (255, 0, 0)),  # Red color
        ("#00FF00", (0, 255, 0)),  # Green color
        ("#0000FF", (0, 0, 255)),  # Blue color
        ("#FFFFFF", (255, 255, 255)),  # White color
        ("#000000", (0, 0, 0)),  # Black color
        ("#FF0000FF", (255, 0, 0)),  # Red color with alpha
        ("#00FF00FF", (0, 255, 0)),  # Green color with alpha
        ("#0000FFFF", (0, 0, 255)),  # Blue color with alpha
        ("#FFFFFFFF", (255, 255, 255)),  # White color with alpha
        ("#000000FF", (0, 0, 0)),  # Black color with alpha
    ],
)
def test_hex_to_rgb(hex_color: str, rgb: tuple[int, int, int]) -> None:
    assert _hex_to_rgb(hex_color) == rgb


@pytest.mark.parametrize(
    ("rgb", "luminance"),
    [
        ((255, 255, 255), 1.0),  # White color
        ((0, 0, 0), 0.0),  # Black color
        ((255, 0, 0), 0.2126),  # Red color
        ((0, 255, 0), 0.7152),  # Green color
        ((0, 0, 255), 0.0722),  # Blue color
    ],
)
def test_relative_luminance(rgb: tuple[int, int, int], luminance: float) -> None:
    assert _relative_luminance(rgb) == luminance


@pytest.mark.parametrize(
    ("x", "srgb"),
    [
        (0, 0.0),
        (255, 1.0),
        (128, 0.21586050011389926),
        (100, 0.12743768043564743),
        (200, 0.5775804404296506),
    ],
)
def test_srgb(x: int, srgb: float) -> None:
    assert _srgb(x) == srgb


@pytest.mark.parametrize(
    ("colors", "alpha", "result"),
    [
        (["#FF0000", "#00FF00", "#0000FF"], None, ["#FF0000", "#00FF00", "#0000FF"]),
        (["red", "green", "blue"], None, ["#FF0000", "#008000", "#0000FF"]),
        (["#FF0000", "green", "#0000FF"], None, ["#FF0000", "#008000", "#0000FF"]),
        (["#FF0000", "#00FF00", "#0000FF"], 0.5, ["#FF00007F", "#00FF007F", "#0000FF7F"]),
        (["red", "green", "blue"], 0.5, ["#FF00007F", "#0080007F", "#0000FF7F"]),
        (["#FF0000", "green", "#0000FF"], 0.5, ["#FF00007F", "#0080007F", "#0000FF7F"]),
    ],
)
def test_html_color_hex_colors(colors: list[str], alpha: float | None, result: list[str]) -> None:
    assert _html_color(colors, alpha=alpha) == result


@pytest.mark.parametrize(
    ("alpha", "context"),
    [
        (0.5, nullcontext()),
        (
            1.5,
            pytest.raises(
                ValueError,
                match=r"Invalid alpha value provided \(1.5\). Please ensure that alpha is a value between 0 and 1.",
            ),
        ),
    ],
)
def test_add_alpha_float_alpha(alpha: float, context: Any) -> None:
    colors = ["#FF0000", "#00FF00", "#0000FF"]

    with context:
        result = _add_alpha(colors, alpha)
        assert result == ["#FF00007F", "#00FF007F", "#0000FF7F"]


@pytest.mark.parametrize(
    ("colors", "result"),
    [
        (["#FF0000FF", "#00FF00FF", "#0000FFFF"], ["#FF0000", "#00FF00", "#0000FF"]),
        (["#FF000080", "#00FF0080", "#0000FF80"], ["#FF0000", "#00FF00", "#0000FF"]),
        (["#FF0000", "#00FF00", "#0000FF"], ["#FF0000", "#00FF00", "#0000FF"]),
    ],
)
def test_remove_alpha(colors: list[str], result: list[str]) -> None:
    assert _remove_alpha(colors) == result


@pytest.mark.parametrize(
    ("x", "hex"),
    [
        (0.0, "00"),  # Test case 1: x = 0.0
        (1.0, "FF"),  # Test case 2: x = 1.0
        (0.5, "7F"),  # Test case 3: x = 0.5
        (0.25, "3F"),  # Test case 4: x = 0.25
        (0.75, "BF"),  # Test case 5: x = 0.75
        (0.125, "1F"),  # Test case 6: x = 0.125
    ],
)
def test_float_to_hex(x: float, hex: str) -> None:
    assert _float_to_hex(x) == hex


@pytest.mark.parametrize(
    ("colors", "result"),
    [
        # Test case 1: All colors are already in hexadecimal format
        (["#FF0000", "#00FF00", "#0000FF"], ["#FF0000", "#00FF00", "#0000FF"]),
        # Test case 2: Some colors are in color name format
        (["red", "green", "blue"], ["#FF0000", "#008000", "#0000FF"]),
        # Test case 3: All colors are in color name format
        (["red", "green", "blue"], ["#FF0000", "#008000", "#0000FF"]),
        # Test case 4: Empty list of colors []
        ([], []),
        # Test case 5: Colors with mixed formats
        (["#FF0000", "green", "#0000FF"], ["#FF0000", "#008000", "#0000FF"]),
    ],
)
def test_color_name_to_hex(colors: list[str], result: list[str]) -> None:
    assert _color_name_to_hex(colors) == result


def test_color_name_to_hex_invalid() -> None:
    # Test case 6: Colors with invalid names
    colors = ["#FF0000", "green", "invalid"]
    with pytest.raises(ValueError) as e:
        _color_name_to_hex(colors)

    assert "Invalid color name provided (invalid)" in e.value.args[0]


@pytest.mark.parametrize(
    ("color", "is_short_hex"),
    [
        ("#F00", True),
        ("#0F0", True),
        ("#00F", True),
        ("#123", True),
        ("#FF0000", False),
        ("#00FF00", False),
        ("#0000FF", False),
        ("#123456", False),
    ],
)
def test_is_short_hex(color: str, is_short_hex: bool) -> None:
    assert _is_short_hex(color) is is_short_hex


@pytest.mark.parametrize(
    ("colors", "is_valid"),
    [
        (["#FF0000", "#00FF00", "#0000FF"], [True, True, True]),
        (["#123456", "#ABCDEF", "#abcdef"], [True, True, True]),
        (["#F00", "#0F0", "#00F"], [False, False, False]),
        (["#FF0000FF", "#00FF00FF", "#0000FFFF"], [True, True, True]),
        (["#FF000", "#00FF00F", "#0000FFG"], [False, False, False]),
        (["#12345", "#ABCDEF1", "#abcdefg"], [False, False, False]),
        (["#F0", "#0F00", "#00FG"], [False, False, False]),
        (["#FF0000F", "#00FF00F", "#0000FFG"], [False, False, False]),
    ],
)
def test_is_hex_col_valid_hex_colors(colors: list[str], is_valid: list[bool]) -> None:
    assert _is_hex_col(colors) == is_valid


@pytest.mark.parametrize(
    ("colors", "result"),
    [
        (["#FF0000", "#00FF00", "#0000FF"], [True, True, True]),
        (["#F00", "#0F0", "#00F"], [False, False, False]),
        (["#123456", "#ABCDEF", "#abcdef"], [True, True, True]),
        (["#123", "#abc", "#ABC"], [False, False, False]),
        (
            [
                "#FF0000",
                "#00FF00",
                "#0000FF",
                "#F00",
                "#0F0",
                "#00F",
                "#123456",
                "#ABCDEF",
                "#abcdef",
                "#123",
                "#abc",
                "#ABC",
            ],
            [True, True, True, False, False, False, True, True, True, False, False, False],
        ),
    ],
)
def test_is_standard_hex_col(colors: list[str], result: list[bool]) -> None:
    assert _is_standard_hex_col(colors) == result


@pytest.mark.parametrize(
    ("hex_color", "expanded"),
    [
        ("#F00", "#FF0000"),
        ("#0F0", "#00FF00"),
        ("#00F", "#0000FF"),
        ("#123", "#112233"),
    ],
)
def test_expand_short_hex_valid_short_hex(hex_color: str, expanded: str) -> None:
    assert _expand_short_hex(hex_color) == expanded


@pytest.mark.parametrize(
    ("vals", "expected_vals"),
    [
        ([2, 3, 4], [0.25, 0.5, 0.75]),  # Rescale values within the domain range
        ([0, 6], [float("nan"), float("nan")]),  # Rescale values outside the domain range
        ([2.0, float("nan"), 4.0], [0.25, float("nan"), 0.75]),  # Rescale values with NA values
    ],
)
def test_rescale_numeric(
    series_constructor: SeriesConstructor, vals: list[float], expected_vals: list[float]
):
    domain = [1, 5]
    nw_vals = nw.from_native(series_constructor(vals), series_only=True)
    expected = nw.from_native(series_constructor(expected_vals), series_only=True)
    result = _rescale_numeric(vals=nw_vals, domain=domain)
    assert_series_equal(result, expected)


@pytest.mark.parametrize(
    "vals",
    [
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        (1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10, float("nan")),
        (1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10, float("nan"), float("nan")),
    ],
)
def test_get_domain_numeric(series_constructor: SeriesConstructor, vals: list[float]) -> None:
    nw_vals = nw.from_native(series_constructor(vals), series_only=True).rename("col")
    result = _get_domain_numeric(nw_vals)
    assert result == [1, 10]


@pytest.mark.parametrize(
    ("vals", "expected_vals"),
    [
        ([], []),  # Empty Series
        (["A", "B", "A", "C", "B"], ["A", "B", "C"]),  # Series with factor values
        (["A", "B", None, "C"], ["A", "B", "C"]),  # Series with factor & nan values
        (["A", "B", "B", "C"], ["A", "B", "C"]),  #  Series with duplicate values
    ],
)
def test_get_domain_factor(
    series_constructor: SeriesConstructor, vals: list[str], expected_vals: list[str]
) -> None:
    nw_vals = nw.from_native(series_constructor(vals), series_only=True).rename("col")
    result = _get_domain_factor(nw_vals)
    assert result.to_list() == expected_vals


def test_gradient_n_pal():
    palette = GradientPalette(["red", "blue"])

    res = palette([0, 0.25, 0.5, 0.75, 1])
    assert res == ["#ff0000", "#bf0040", "#800080", "#4000bf", "#0000ff"]


@pytest.mark.parametrize(
    ("src", "dst"), [(0.001, "#ff0000"), (0.004, "#fe0001"), (0.999, "#0000ff"), (0.996, "#0100fe")]
)
def test_gradient_n_pal_rounds(src: float, dst: str) -> None:
    palette = GradientPalette(["red", "blue"])

    res = palette([src])
    assert res == [dst]


@pytest.mark.parametrize(
    ("src", "dst"),
    [
        ([-math.inf, 0, math.nan, 1, math.inf], [None, "#ff0000", None, "#0000ff", None]),
        # same but with numpy
        ([-np.inf, 0, np.nan, 1, np.inf], [None, "#ff0000", None, "#0000ff", None]),
    ],
)
def test_gradient_n_pal_inf(src: list[float], dst: list[str]) -> None:
    palette = GradientPalette(["red", "blue"])

    res = palette(src)
    assert res == dst


def test_gradient_n_pal_symmetric():
    # based on mizani unit tests
    palette = GradientPalette(["red", "blue", "red"], values=[0, 0.5, 1])

    res = palette([0.2, 0.5, 0.8])
    assert res == ["#990066", "#0000ff", "#990066"]


def test_gradient_n_pal_manual_values():
    # note that green1 is #0000ff (and green is not!)
    palette = GradientPalette(["red", "blue", "green1"], values=[0, 0.8, 1])

    res = palette([0, 0.8, 0.9, 1])
    assert res == ["#ff0000", "#0000ff", "#008080", "#00ff00"]


@pytest.mark.parametrize(
    ("colors", "values", "context"),
    [
        (["red"], None, pytest.raises(ValueError, match="only 1 provided")),
        # values must start with 0
        (["red", "blue"], [0.1, 1], pytest.raises(ValueError, match="start with 0")),
        # values must end with 1
        (["red", "blue"], [0, 0.1], pytest.raises(ValueError, match="end with 1")),
        # len(color) != len(values)
        (
            ["red", "blue"],
            [0, 1.1, 1],
            pytest.raises(ValueError, match="Received 3 values and 2 colors"),
        ),
        (
            [(255, 0, 0), (0, 255, 0)],
            None,
            pytest.raises(
                NotImplementedError, match="Currently, rgb tuples can't be passed directly."
            ),
        ),
    ],
)
def test_gradient_n_pal_guard_raises(
    colors: list[str], values: list[float] | None, context: Any
) -> None:
    with context:
        GradientPalette(colors=colors, values=values)


@pytest.mark.parametrize(
    ("data", "msg"),
    [
        ([0, 1.1], "Value: 1.1"),
        ([0, -0.1], "Value: -0.1"),
    ],
)
def test_gradient_n_pal_out_of_bounds_raises(data: list[float], msg: str) -> None:
    palette = GradientPalette(["red", "blue"])

    with pytest.raises(ValueError, match=msg):
        palette(data)
