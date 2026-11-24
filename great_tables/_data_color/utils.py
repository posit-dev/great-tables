from __future__ import annotations

import re
from typing import TypeAlias

from .constants import COLOR_NAME_TO_HEX

RGBColor: TypeAlias = tuple[int, int, int]


def _hex_to_rgb(hex_color: str) -> RGBColor:
    """
    Convert a hexadecimal color value to RGB.

    Parameters
    ----------
    hex_color
        The hexadecimal color value, in `#RRGGBB` or `#RRGGBBAA` format (any alpha component is
        dropped).

    Returns
    -------
    RGBColor
        The RGB values.
    """

    # If the hexadecimal color value is in the #RRGGBBAA format, then we need to remove the
    # alpha value from it before converting it to RGB
    if len(hex_color) == 9:
        hex_color = hex_color[:-2]

    # Convert the hexadecimal color value to RGB
    rgb = tuple(int(hex_color[i : i + 2], 16) for i in (1, 3, 5))

    return rgb  # type: ignore


def rgb_to_hex(rgb: RGBColor) -> str:
    """
    Convert an RGB tuple to a lowercase hexadecimal color string.

    Parameters
    ----------
    rgb
        An `(r, g, b)` tuple of integers in the range `[0, 255]`.

    Returns
    -------
    str
        The hexadecimal color string in `#rrggbb` format.
    """

    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


def _html_color(colors: list[str], alpha: float | None = None) -> list[str]:
    """
    Normalize HTML colors.

    Input colors can be color names (e.g., `"green"`, `"steelblue"`, etc.) or colors in hexadecimal
    format with or without an alpha component (either #RRGGBB or #RRGGBBAA). Output will be a list
    of hexadecimal colors of the same length as the input but it will contain #RRGGBB and #RRGGBBAA
    colors.

    Parameters
    ----------
    colors
        A list of CSS3/X11 color names or hexadecimal color strings.
    alpha
        An optional alpha transparency value between `0` and `1` to apply to all colors.

    Returns
    -------
    list[str]
        The normalized hexadecimal color strings.

    Raises
    ------
    ValueError
        If a color is neither a hexadecimal color nor a known color name, or if `alpha` is not
        between `0` and `1`.
    """

    # Expand any shorthand hexadecimal color values to the `RRGGBB` form
    colors = [_expand_short_hex(hex_color=color) for color in colors]

    # If not classified as hexadecimal, assume other values are named colors to be handled separately
    all_hex_colors = all(_is_hex_col(colors=colors))

    if not all_hex_colors:
        # Translate named colors to hexadecimal values
        colors = _color_name_to_hex(colors=colors)

    # If `alpha` is not None, then we need to add the alpha value to the
    # color value but only if it doesn't already exist
    if alpha is not None:
        colors = _add_alpha(colors=colors, alpha=alpha)

    return colors


def _add_alpha(colors: list[str], alpha: float) -> list[str]:
    """
    Apply an alpha transparency value to a list of hexadecimal color strings.

    The list is modified in place (and also returned). Any existing alpha component is replaced,
    except in `"#FFFFFF00"` (fully transparent), which is left as it is.

    Parameters
    ----------
    colors
        A list of hexadecimal color strings in `#RRGGBB` or `#RRGGBBAA` format.
    alpha
        The alpha transparency value between `0` and `1`.

    Returns
    -------
    list[str]
        The hexadecimal color strings with the alpha component applied.

    Raises
    ------
    ValueError
        If `alpha` is not between `0` and `1`.
    """

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


def _float_to_hex(x: float) -> str:
    """
    Convert a float to a hexadecimal value.

    Parameters
    ----------
    x
        The float value to convert, between `0` and `1`. It's scaled to `0`-`255` and truncated
        (so `0.5` gives `"7F"`).

    Returns
    -------
    str
        The two-digit, uppercase hexadecimal value.
    """

    # Convert the float to an integer and convert to a hexadecimal value
    x_hex = hex(int(x * 255)).upper()

    # Remove the leading '0x' from the hexadecimal value
    x_hex = x_hex[2:]

    # If the hexadecimal value is only one character long, then add a leading '0'
    if len(x_hex) == 1:
        x_hex = "0" + x_hex

    return x_hex


def _color_name_to_hex(colors: list[str]) -> list[str]:
    """
    Convert CSS3/X11 color names to hexadecimal color strings.

    Parameters
    ----------
    colors
        A list of color names (matched case-insensitively) or hexadecimal color strings, which are
        kept as they are.

    Returns
    -------
    list[str]
        The corresponding hexadecimal color strings.

    Raises
    ------
    ValueError
        If a color is neither a hexadecimal color nor a known color name.
    """

    # If any of the colors are in the color_name_dict, then replace them with the
    # corresponding hexadecimal value

    hex_colors: list[str] = []

    for color in colors:
        if _is_hex_col([color])[0]:
            hex_colors.append(color)
        else:
            try:
                hex_colors.append(COLOR_NAME_TO_HEX[color.lower()])
            except KeyError:
                raise ValueError(
                    f"Invalid color name provided ({color}). Please ensure that all colors are valid CSS3 or X11 color names."
                )

    return hex_colors


def _color_name_list() -> list[str]:
    """
    Return all supported CSS3/X11 color names.

    Returns
    -------
    list[str]
        The list of recognized color names.
    """

    return list(COLOR_NAME_TO_HEX)


def _is_short_hex(color: str) -> bool:
    """
    Check whether a color string is in shorthand `#RGB` or `#RGBA` hex format.

    Parameters
    ----------
    color
        The color string to check.

    Returns
    -------
    bool
        `True` if the string matches `#RGB` or `#RGBA`, otherwise `False`.
    """

    pattern = r"^#[0-9a-fA-F]{3}([0-9a-fA-F])?$"
    return re.match(pattern, color) is not None


def _is_hex_col(colors: list[str]) -> list[bool]:
    """
    Check whether each color string is in `#RRGGBB` or `#RRGGBBAA` hex format.

    Parameters
    ----------
    colors
        The list of color strings to check.

    Returns
    -------
    list[bool]
        A list of booleans indicating whether each color is valid `#RRGGBB` or `#RRGGBBAA`.
    """

    return [bool(re.match(r"^#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$", color)) for color in colors]


def _is_standard_hex_col(colors: list[str]) -> list[bool]:
    """
    Check whether each color string is in standard `#RRGGBB` hex format.

    Parameters
    ----------
    colors
        The list of color strings to check.

    Returns
    -------
    list[bool]
        A list of booleans indicating whether each color is valid `#RRGGBB`.
    """

    return [bool(re.match(r"^#[0-9a-fA-F]{6}$", color)) for color in colors]


def _expand_short_hex(hex_color: str) -> str:
    """
    Expand a short hexadecimal color value to the full 6-digit or 8-digit hexadecimal form.

    Parameters
    ----------
    hex_color
        The short hexadecimal color value to expand.

    Returns
    -------
    str
        The expanded, uppercase hexadecimal color value (`#RGB` becomes `#RRGGBB` and `#RGBA`
        becomes `#RRGGBBAA`), or the original value if it isn't shorthand hex.
    """

    # If the hex color is not a short hexadecimal color value, return the original value
    if not _is_short_hex(color=hex_color):
        return hex_color

    # Get the hex color without the leading '#'
    hex_color = hex_color[1:]

    # Return the expanded 6-digit (or 8-digit) hexadecimal color value
    expanded = "#" + "".join(x * 2 for x in hex_color)
    return expanded.upper()
