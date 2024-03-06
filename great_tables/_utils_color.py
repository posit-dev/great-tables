# Utility functions for color handling


from typing import List, Optional, Tuple, Union
from great_tables._constants import COLOR_NAME_TO_HEX


def _ideal_fgnd_color(bgnd_color: str, light: str = "#FFFFFF", dark: str = "#000000") -> str:
    # Remove alpha value from hexadecimal color value in `bgnd_color=`
    bgnd_color = _remove_alpha(colors=[bgnd_color])[0]

    contrast_dark = _get_wcag_contrast_ratio(color_1=dark, color_2=bgnd_color)
    contrast_light = _get_wcag_contrast_ratio(color_1=light, color_2=bgnd_color)

    fgnd_color = dark if abs(contrast_dark) > abs(contrast_light) else light

    return fgnd_color


def _get_wcag_contrast_ratio(color_1: str, color_2: str) -> float:
    """
    Calculate the WCAG contrast ratio between two colors.

    Parameters
    ----------
    color_1
        The first color.
    color_2
        The second color.

    Returns
    -------
    float
        The WCAG contrast ratio between the two colors.
    """

    # Convert the colors to RGB values
    rgb_1 = _hex_to_rgb(hex_color=color_1)
    rgb_2 = _hex_to_rgb(hex_color=color_2)

    # Calculate the relative luminance values for each color
    l_1 = _relative_luminance(rgb=rgb_1)
    l_2 = _relative_luminance(rgb=rgb_2)

    # Calculate the contrast ratio between the two colors
    contrast_ratio = (max(l_1, l_2) + 0.05) / (min(l_1, l_2) + 0.05)

    return contrast_ratio


def _hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """
    Convert a hexadecimal color value to RGB.

    Parameters
    ----------
    hex_color
        The hexadecimal color value.

    Returns
    -------
    Tuple[int, int, int]
        The RGB values.
    """

    # If the hexadecimal color value is in the #RRGGBBAA format, then we need to remove the
    # alpha value from it before converting it to RGB
    if len(hex_color) == 9:
        hex_color = hex_color[:-2]

    # Convert the hexadecimal color value to RGB
    rgb = tuple(int(hex_color[i : i + 2], 16) for i in (1, 3, 5))

    return rgb


def _relative_luminance(rgb: Tuple[int, int, int]) -> float:
    """
    Calculate the relative luminance of an RGB color.

    Parameters
    ----------
    rgb
        The RGB color.

    Returns
    -------
    float
        The relative luminance.
    """

    # Convert the RGB values to the sRGB color space
    srgb = [_srgb(x=x) for x in rgb]

    # Calculate the relative luminance
    relative_luminance = 0.2126 * srgb[0] + 0.7152 * srgb[1] + 0.0722 * srgb[2]

    return relative_luminance


def _srgb(x: int) -> float:
    """
    Convert an integer to the sRGB color space.

    Parameters
    ----------
    x
        The integer to convert.

    Returns
    -------
    float
        The converted value.
    """

    x_frac = x / 255

    if x_frac <= 0.03928:
        x_frac = x_frac / 12.92
    else:
        x_frac = ((x_frac + 0.055) / 1.055) ** 2.4

    return x_frac


def _html_color(colors: List[str], alpha: Optional[Union[int, float]] = None) -> List[str]:
    """
    Normalize HTML colors.

    Input colors can be color names (e.g., `"green"`, `"steelblue"`, etc.) or colors in hexadecimal
    format with or without an alpha component (either #RRGGBB or #RRGGBBAA). Output will be a list
    of hexadecimal colors of the same length as the input but it will contain #RRGGBB and #RRGGBBAA
    colors.
    """

    # Expand any shorthand hexadecimal color values to the `RRGGBB` form
    colors = [_expand_short_hex(hex_color=color) for color in colors]

    # If not classified as hexadecimal, assume other values are named colors to be handled separately
    all_hex_colors = all(_is_hex_col(colors=colors))

    if not all_hex_colors:
        # Ensure that all color names are in the set of X11/R color names or CSS color names
        _check_named_colors(colors=colors)

        # Translate named colors to hexadecimal values
        colors = _color_name_to_hex(colors=colors)

    # If `alpha` is not None, then we need to add the alpha value to the
    # color value but only if it doesn't already exist
    if alpha is not None:
        colors = _add_alpha(colors=colors, alpha=alpha)

    return colors


def _add_alpha(colors: List[str], alpha: Union[int, float]) -> List[str]:
    # If `alpha` is an integer, then convert it to a float
    if isinstance(alpha, int):
        alpha = float(alpha)

    # If `alpha` is not between 0 and 1, then throw an error
    if alpha < 0 or alpha > 1:
        raise ValueError(
            f"Invalid alpha value provided ({alpha}). Please ensure that alpha is a value between 0 and 1."
        )

    # Loop through the indices of the colors and add the alpha value to each one
    for i in range(len(colors)):
        color = colors[i]
        if color == "#FFFFFF00":
            continue

        # If the color value is already in the `#RRGGBBAA` format, then we need to remove the
        # alpha value from it before adding the new alpha value
        if len(color) == 9:
            color = color[:-2]

        # Add the alpha value to the color value
        colors[i] = color + _float_to_hex(alpha)

    return colors


def _remove_alpha(colors: List[str]) -> List[str]:
    # Loop through the colors and remove the alpha value from each one
    for i in range(len(colors)):
        color = colors[i]
        # If the color value is already in the `#RRGGBB` format, then we need to add the
        # alpha value to it before removing the alpha value
        if _is_standard_hex_col([color])[0]:
            color = color + "FF"

        # Remove the alpha value from the color value
        colors[i] = color[:-2]

    return colors


def _float_to_hex(x: float) -> str:
    """
    Convert a float to a hexadecimal value.

    Parameters
    ----------
    x
        The float value to convert.

    Returns
    -------
    str
        The hexadecimal value.
    """

    # Convert the float to an integer and convert to a hexadecimal value
    x_hex = hex(int(x * 255)).upper()

    # Remove the leading '0x' from the hexadecimal value
    x_hex = x_hex[2:]

    # If the hexadecimal value is only one character long, then add a leading '0'
    if len(x_hex) == 1:
        x_hex = "0" + x_hex

    return x_hex


def _color_name_to_hex(colors: List[str]) -> List[str]:
    # If any of the colors are in the color_name_dict, then replace them with the
    # corresponding hexadecimal value
    i = 0
    while i < len(colors):
        color = colors[i]
        if color.lower() in COLOR_NAME_TO_HEX:
            colors[i] = COLOR_NAME_TO_HEX[color.lower()]
        i += 1

    return colors


def _color_name_list() -> List[str]:
    return list(COLOR_NAME_TO_HEX) + ["transparent", "currentcolor", "currentColor"]


def _check_named_colors(colors: Union[str, List[str]]) -> None:
    # Ensure that all incoming color names are set in lowercase letters since CSS color names
    # are often shown with uppercase letters and X11/R color names are always shown with lowercase
    if isinstance(colors, str):
        colors = [colors]

    valid_color_names = _color_name_list()

    for color in colors:
        if not _is_hex_col(colors=[color]) and color not in valid_color_names:
            raise ValueError(
                f"Invalid color name provided ({color}). Please ensure that all color names are valid."
            )

    return


def _is_short_hex(color: str) -> bool:
    import re

    pattern = r"^#[0-9a-fA-F]{3}([0-9a-fA-F])?$"
    return re.match(pattern, color) is not None


def _is_hex_col(colors: List[str]) -> List[bool]:
    import re

    return [bool(re.match(r"^#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$", color)) for color in colors]


def _is_standard_hex_col(colors: List[str]) -> List[bool]:
    import re

    return [bool(re.match(r"^#[0-9a-fA-F]{6}$", color)) for color in colors]


def _expand_short_hex(hex_color: str) -> str:
    """
    Expands a short hexadecimal color value to the full 6-digit hexadecimal color value.

    Args:
        hex_color (str): The short hexadecimal color value to expand.

    Returns:
        str: The expanded 6-digit hexadecimal color value.
    """
    # If the hex color is not a short hexadecimal color value, return the original value
    if not _is_short_hex(color=hex_color):
        return hex_color

    # Get the hex color without the leading '#'
    hex_color = hex_color[1:]

    # Get the first character of the hex color
    first_char = hex_color[0]

    # Get the second character of the hex color
    second_char = hex_color[1]

    # Get the third character of the hex color
    third_char = hex_color[2]

    # Return the expanded 6-digit hexadecimal color value
    expanded = "#" + first_char + first_char + second_char + second_char + third_char + third_char
    expanded = expanded.upper()
    return expanded
