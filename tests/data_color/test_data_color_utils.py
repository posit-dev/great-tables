import math

import numpy as np
import pandas as pd
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


def test_ideal_fgnd_color_dark_contrast():
    bgnd_color = "#FFFFFF"  # White background color
    fgnd_color = _ideal_fgnd_color(bgnd_color)
    assert fgnd_color == "#000000"  # Expected dark foreground color


def test_ideal_fgnd_color_light_contrast():
    bgnd_color = "#000000"  # Black background color
    fgnd_color = _ideal_fgnd_color(bgnd_color)
    assert fgnd_color == "#FFFFFF"  # Expected light foreground color


def test_ideal_fgnd_color_custom_contrast():
    bgnd_color = "#FF0000"  # Red background color
    light_color = "#00FF00"  # Green light color
    dark_color = "#0000FF"  # Blue dark color
    fgnd_color = _ideal_fgnd_color(bgnd_color, light=light_color, dark=dark_color)
    assert fgnd_color == "#00FF00"  # Expected custom light foreground color


def test_ideal_fgnd_color_custom_contrast_with_alpha():
    bgnd_color = "#FF0000FF"  # Red background color with alpha
    light_color = "#00FF00"  # Green light color
    dark_color = "#0000FF"  # Blue dark color
    fgnd_color = _ideal_fgnd_color(bgnd_color, light=light_color, dark=dark_color)
    assert fgnd_color == "#00FF00"  # Expected custom light foreground color


def test_ideal_fgnd_color_custom_contrast_with_custom_colors():
    bgnd_color = "#FF0000"  # Red background color
    light_color = "#00FF00"  # Green light color
    dark_color = "#0000FF"  # Blue dark color
    fgnd_color = _ideal_fgnd_color(bgnd_color, light=light_color, dark=dark_color)
    assert fgnd_color == "#00FF00"  # Expected custom light foreground color


def test_ideal_fgnd_color_custom_contrast_with_custom_colors_and_alpha():
    bgnd_color = "#FF0000FF"  # Red background color with alpha
    light_color = "#00FF00"  # Green light color
    dark_color = "#0000FF"  # Blue dark color
    fgnd_color = _ideal_fgnd_color(bgnd_color, light=light_color, dark=dark_color)
    assert fgnd_color == "#00FF00"  # Expected custom light foreground color


def test_get_wcag_contrast_ratio():
    color_1 = "#FFFFFF"  # White color
    color_2 = "#000000"  # Black color
    contrast_ratio = _get_wcag_contrast_ratio(color_1, color_2)
    assert contrast_ratio == 21.0  # Expected high contrast ratio


def test_get_wcag_contrast_ratio_custom_colors():
    color_1 = "#FF0000"  # Red color
    color_2 = "#00FF00"  # Green color
    contrast_ratio = _get_wcag_contrast_ratio(color_1, color_2)
    assert contrast_ratio == 2.9139375476009137  # Expected low contrast ratio


def test_get_wcag_contrast_ratio_custom_colors_with_alpha():
    color_1 = "#FF0000FF"  # Red color with alpha
    color_2 = "#00FF00"  # Green color
    contrast_ratio = _get_wcag_contrast_ratio(color_1, color_2)
    assert contrast_ratio == 2.9139375476009137  # Contrast ratio unchanged with alpha


def test_get_wcag_contrast_ratio_same_color():
    color_1 = "#FF0000"  # Red color
    color_2 = "#FF0000"  # Red color
    contrast_ratio = _get_wcag_contrast_ratio(color_1, color_2)
    assert contrast_ratio == 1.0  # Contrast ratio always 1.0 for same color


def test_get_wcag_contrast_ratio_same_color_with_alpha():
    color_1 = "#FF0000FF"  # Red color with alpha
    color_2 = "#FF0000FF"  # Red color with alpha
    contrast_ratio = _get_wcag_contrast_ratio(color_1, color_2)
    assert contrast_ratio == 1.0  # Contrast ratio unchanged with alpha


def test_hex_to_rgb():
    hex_color = "#FF0000"  # Red color
    rgb = _hex_to_rgb(hex_color)
    assert rgb == (255, 0, 0)

    hex_color = "#00FF00"  # Green color
    rgb = _hex_to_rgb(hex_color)
    assert rgb == (0, 255, 0)

    hex_color = "#0000FF"  # Blue color
    rgb = _hex_to_rgb(hex_color)
    assert rgb == (0, 0, 255)

    hex_color = "#FFFFFF"  # White color
    rgb = _hex_to_rgb(hex_color)
    assert rgb == (255, 255, 255)

    hex_color = "#000000"  # Black color
    rgb = _hex_to_rgb(hex_color)
    assert rgb == (0, 0, 0)

    hex_color = "#FF0000FF"  # Red color with alpha
    rgb = _hex_to_rgb(hex_color)
    assert rgb == (255, 0, 0)

    hex_color = "#00FF00FF"  # Green color with alpha
    rgb = _hex_to_rgb(hex_color)
    assert rgb == (0, 255, 0)

    hex_color = "#0000FFFF"  # Blue color with alpha
    rgb = _hex_to_rgb(hex_color)
    assert rgb == (0, 0, 255)

    hex_color = "#FFFFFFFF"  # White color with alpha
    rgb = _hex_to_rgb(hex_color)
    assert rgb == (255, 255, 255)

    hex_color = "#000000FF"  # Black color with alpha
    rgb = _hex_to_rgb(hex_color)
    assert rgb == (0, 0, 0)


def test_relative_luminance():
    rgb = (255, 255, 255)  # White color
    luminance = _relative_luminance(rgb)
    assert luminance == 1.0

    rgb = (0, 0, 0)  # Black color
    luminance = _relative_luminance(rgb)
    assert luminance == 0.0

    rgb = (255, 0, 0)  # Red color
    luminance = _relative_luminance(rgb)
    assert luminance == 0.2126

    rgb = (0, 255, 0)  # Green color
    luminance = _relative_luminance(rgb)
    assert luminance == 0.7152

    rgb = (0, 0, 255)  # Blue color
    luminance = _relative_luminance(rgb)
    assert luminance == 0.0722


def test_srgb():
    x = 0
    result = _srgb(x)
    assert result == 0.0

    x = 255
    result = _srgb(x)
    assert result == 1.0

    x = 128
    result = _srgb(x)
    assert result == 0.21586050011389926

    x = 100
    result = _srgb(x)
    assert result == 0.12743768043564743

    x = 200
    result = _srgb(x)
    assert result == 0.5775804404296506


def test_html_color_hex_colors():
    colors = ["#FF0000", "#00FF00", "#0000FF"]
    result = _html_color(colors)
    assert result == ["#FF0000", "#00FF00", "#0000FF"]


def test_html_color_named_colors():
    colors = ["red", "green", "blue"]
    result = _html_color(colors)
    assert result == ["#FF0000", "#008000", "#0000FF"]


def test_html_color_mixed_colors():
    colors = ["#FF0000", "green", "#0000FF"]
    result = _html_color(colors)
    assert result == ["#FF0000", "#008000", "#0000FF"]


def test_html_color_hex_colors_with_alpha():
    colors = ["#FF0000", "#00FF00", "#0000FF"]
    alpha = 0.5
    result = _html_color(colors, alpha)
    assert result == ["#FF00007F", "#00FF007F", "#0000FF7F"]


def test_html_color_named_colors_with_alpha():
    colors = ["red", "green", "blue"]
    alpha = 0.5
    result = _html_color(colors, alpha)
    assert result == ["#FF00007F", "#0080007F", "#0000FF7F"]


def test_html_color_mixed_colors_with_alpha():
    colors = ["#FF0000", "green", "#0000FF"]
    alpha = 0.5
    result = _html_color(colors, alpha)
    assert result == ["#FF00007F", "#0080007F", "#0000FF7F"]


def test_add_alpha_float_alpha():
    colors = ["#FF0000", "#00FF00", "#0000FF"]
    alpha = 0.5
    result = _add_alpha(colors, alpha)
    assert result == ["#FF00007F", "#00FF007F", "#0000FF7F"]


def test_add_alpha_invalid_alpha():
    colors = ["#FF0000", "#00FF00", "#0000FF"]
    alpha = 1.5
    try:
        _add_alpha(colors, alpha)
    except ValueError as e:
        assert (
            str(e)
            == "Invalid alpha value provided (1.5). Please ensure that alpha is a value between 0 and 1."
        )


def test_remove_alpha():
    colors = ["#FF0000FF", "#00FF00FF", "#0000FFFF"]
    result = _remove_alpha(colors)
    assert result == ["#FF0000", "#00FF00", "#0000FF"]

    colors = ["#FF000080", "#00FF0080", "#0000FF80"]
    result = _remove_alpha(colors)
    assert result == ["#FF0000", "#00FF00", "#0000FF"]

    colors = ["#FF0000", "#00FF00", "#0000FF"]
    result = _remove_alpha(colors)
    assert result == ["#FF0000", "#00FF00", "#0000FF"]


def test_float_to_hex():
    # Test case 1: x = 0.0
    x = 0.0
    result = _float_to_hex(x)
    assert result == "00"

    # Test case 2: x = 1.0
    x = 1.0
    result = _float_to_hex(x)
    assert result == "FF"

    # Test case 3: x = 0.5
    x = 0.5
    result = _float_to_hex(x)
    assert result == "7F"

    # Test case 4: x = 0.25
    x = 0.25
    result = _float_to_hex(x)
    assert result == "3F"

    # Test case 5: x = 0.75
    x = 0.75
    result = _float_to_hex(x)
    assert result == "BF"

    # Test case 6: x = 0.125
    x = 0.125
    result = _float_to_hex(x)
    assert result == "1F"


def test_color_name_to_hex():
    # Test case 1: All colors are already in hexadecimal format
    colors = ["#FF0000", "#00FF00", "#0000FF"]
    result = _color_name_to_hex(colors)
    assert result == ["#FF0000", "#00FF00", "#0000FF"]

    # Test case 2: Some colors are in color name format
    colors = ["red", "green", "blue"]
    result = _color_name_to_hex(colors)
    assert result == ["#FF0000", "#008000", "#0000FF"]

    # Test case 3: All colors are in color name format
    colors = ["red", "green", "blue"]
    result = _color_name_to_hex(colors)
    assert result == ["#FF0000", "#008000", "#0000FF"]

    # Test case 4: Empty list of colors
    colors = []
    result = _color_name_to_hex(colors)
    assert result == []

    # Test case 5: Colors with mixed formats
    colors = ["#FF0000", "green", "#0000FF"]
    result = _color_name_to_hex(colors)
    assert result == ["#FF0000", "#008000", "#0000FF"]

    # Test case 6: Colors with invalid names
    colors = ["#FF0000", "green", "invalid"]
    with pytest.raises(ValueError) as e:
        _color_name_to_hex(colors)

    assert "Invalid color name provided (invalid)" in e.value.args[0]


def test_is_short_hex_valid_short_hex():
    color = "#F00"
    result = _is_short_hex(color)
    assert result is True

    color = "#0F0"
    result = _is_short_hex(color)
    assert result is True

    color = "#00F"
    result = _is_short_hex(color)
    assert result is True

    color = "#123"
    result = _is_short_hex(color)
    assert result is True


def test_is_short_hex_valid_long_hex():
    color = "#FF0000"
    result = _is_short_hex(color)
    assert result is False

    color = "#00FF00"
    result = _is_short_hex(color)
    assert result is False

    color = "#0000FF"
    result = _is_short_hex(color)
    assert result is False

    color = "#123456"
    result = _is_short_hex(color)
    assert result is False


def test_is_hex_col_valid_hex_colors():
    colors = ["#FF0000", "#00FF00", "#0000FF"]
    result = _is_hex_col(colors)
    assert result == [True, True, True]

    colors = ["#123456", "#ABCDEF", "#abcdef"]
    result = _is_hex_col(colors)
    assert result == [True, True, True]

    colors = ["#F00", "#0F0", "#00F"]
    result = _is_hex_col(colors)
    assert result == [False, False, False]

    colors = ["#FF0000FF", "#00FF00FF", "#0000FFFF"]
    result = _is_hex_col(colors)
    assert result == [True, True, True]


def test_is_hex_col_invalid_hex_colors():
    colors = ["#FF000", "#00FF00F", "#0000FFG"]
    result = _is_hex_col(colors)
    assert result == [False, False, False]

    colors = ["#12345", "#ABCDEF1", "#abcdefg"]
    result = _is_hex_col(colors)
    assert result == [False, False, False]

    colors = ["#F0", "#0F00", "#00FG"]
    result = _is_hex_col(colors)
    assert result == [False, False, False]

    colors = ["#FF0000F", "#00FF00F", "#0000FFG"]
    result = _is_hex_col(colors)
    assert result == [False, False, False]


def test_is_standard_hex_col():
    colors = ["#FF0000", "#00FF00", "#0000FF"]
    result = _is_standard_hex_col(colors)
    assert result == [True, True, True]

    colors = ["#F00", "#0F0", "#00F"]
    result = _is_standard_hex_col(colors)
    assert result == [False, False, False]

    colors = ["#123456", "#ABCDEF", "#abcdef"]
    result = _is_standard_hex_col(colors)
    assert result == [True, True, True]

    colors = ["#123", "#abc", "#ABC"]
    result = _is_standard_hex_col(colors)
    assert result == [False, False, False]

    colors = [
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
    ]
    result = _is_standard_hex_col(colors)
    assert result == [True, True, True, False, False, False, True, True, True, False, False, False]


def test_expand_short_hex_valid_short_hex():
    hex_color = "#F00"
    expanded = _expand_short_hex(hex_color)
    assert expanded == "#FF0000"

    hex_color = "#0F0"
    expanded = _expand_short_hex(hex_color)
    assert expanded == "#00FF00"

    hex_color = "#00F"
    expanded = _expand_short_hex(hex_color)
    assert expanded == "#0000FF"

    hex_color = "#123"
    expanded = _expand_short_hex(hex_color)
    assert expanded == "#112233"


def test_rescale_numeric():
    # Test case 1: Rescale values within the domain range
    df = pd.DataFrame({"col": [1, 2, 3, 4, 5]})
    vals = [2, 3, 4]
    domain = [1, 5]
    expected_result = [0.25, 0.5, 0.75]
    result = _rescale_numeric(df, vals, domain)
    assert result == expected_result

    # Test case 2: Rescale values outside the domain range
    df = pd.DataFrame({"col": [1, 2, 3, 4, 5]})
    vals = [0, 6]
    domain = [1, 5]
    expected_result = [np.nan, np.nan]
    result = _rescale_numeric(df, vals, domain)
    assert result == expected_result

    # Test case 3: Rescale values with NA values
    df = pd.DataFrame({"col": [1, 2, np.nan, 4, 5]})
    vals = [2, np.nan, 4]
    domain = [1, 5]
    expected_result = [0.25, np.nan, 0.75]
    result = _rescale_numeric(df, vals, domain)
    assert result == expected_result


def test_get_domain_numeric():
    df = pd.DataFrame({"col1": [1, 2, 3, 4, 5], "col2": [6, 7, 8, 9, 10]})
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    domain = _get_domain_numeric(df, vals)
    assert domain == [1, 10]

    df = pd.DataFrame({"col1": [1, 2, 3, 4, 5], "col2": [6, 7, 8, 9, 10]})
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, np.nan]
    domain = _get_domain_numeric(df, vals)
    assert domain == [1, 10]

    df = pd.DataFrame({"col1": [1, 2, 3, 4, 5], "col2": [6, 7, 8, 9, 10]})
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, np.nan, np.nan]
    domain = _get_domain_numeric(df, vals)
    assert domain == [1, 10]


def test_get_domain_factor():
    # Test case 1: Empty DataFrame
    df = pd.DataFrame()
    vals = []
    result = _get_domain_factor(df, vals)
    assert result == []

    # Test case 2: DataFrame with factor values
    df = pd.DataFrame({"col1": ["A", "B", "A", "C", "B"]})
    vals = ["A", "B", "C"]
    result = _get_domain_factor(df, vals)
    assert result == ["A", "B", "C"]

    # Test case 3: DataFrame with factor values and NA values
    df = pd.DataFrame({"col1": ["A", "B", np.nan, "C", "B"]})
    vals = ["A", "B", "C"]
    result = _get_domain_factor(df, vals)
    assert result == ["A", "B", "C"]

    # Test case 4: DataFrame with factor values and NA values in `vals`
    df = pd.DataFrame({"col1": ["A", "B", "C"]})
    vals = ["A", "B", np.nan, "C"]
    result = _get_domain_factor(df, vals)
    assert result == ["A", "B", "C"]

    # Test case 5: DataFrame with factor values and duplicate values in `vals`
    df = pd.DataFrame({"col1": ["A", "B", "C"]})
    vals = ["A", "B", "B", "C"]
    result = _get_domain_factor(df, vals)
    assert result == ["A", "B", "C"]


def test_gradient_n_pal():
    palette = GradientPalette(["red", "blue"])

    res = palette([0, 0.25, 0.5, 0.75, 1])
    assert res == ["#ff0000", "#bf0040", "#800080", "#4000bf", "#0000ff"]


@pytest.mark.parametrize(
    "src,dst", [(0.001, "#ff0000"), (0.004, "#fe0001"), (0.999, "#0000ff"), (0.996, "#0100fe")]
)
def test_gradient_n_pal_rounds(src, dst):
    palette = GradientPalette(["red", "blue"])

    res = palette([src])
    assert res == [dst]


def test_gradient_n_pal_inf():
    palette = GradientPalette(["red", "blue"])

    res = palette([-math.inf, 0, math.nan, 1, math.inf])
    assert res == [None, "#ff0000", None, "#0000ff", None]

    # same but with numpy
    res = palette([-np.inf, 0, np.nan, 1, np.inf])
    assert res == [None, "#ff0000", None, "#0000ff", None]


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


def test_gradient_n_pal_guard_raises():
    with pytest.raises(ValueError) as exc_info:
        GradientPalette(["red"])

    assert "only 1 provided" in exc_info.value.args[0]

    # values must start with 0
    with pytest.raises(ValueError) as exc_info:
        GradientPalette(["red", "blue"], values=[0.1, 1])

    assert "start with 0" in exc_info.value.args[0]

    # values must end with 1
    with pytest.raises(ValueError) as exc_info:
        GradientPalette(["red", "blue"], values=[0, 0.1])

    assert "end with 1" in exc_info.value.args[0]

    # len(color) != len(values)
    with pytest.raises(ValueError) as exc_info:
        GradientPalette(["red", "blue"], values=[0, 1.1, 1])

    assert "Received 3 values and 2 colors" in exc_info.value.args[0]

    with pytest.raises(NotImplementedError) as exc_info:
        GradientPalette([(255, 0, 0), (0, 255, 0)])

    assert "Currently, rgb tuples can't be passed directly." in exc_info.value.args[0]


def test_gradient_n_pal_out_of_bounds_raises():
    palette = GradientPalette(["red", "blue"])

    with pytest.raises(ValueError) as exc_info:
        palette([0, 1.1])

    assert "Value: 1.1" in exc_info.value.args[0]

    with pytest.raises(ValueError) as exc_info:
        palette([0, -0.1])

    assert "Value: -0.1" in exc_info.value.args[0]
