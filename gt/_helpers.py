from typing import Union, List


def letters() -> List[str]:
    """Lowercase letters of the Roman alphabet

    Returns:
        List[str]: the 26 lowercase letters of the Roman alphabet
    """
    lett = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    return lett


def LETTERS() -> List[str]:
    """Uppercase letters of the Roman alphabet

    Returns:
        List[str]: the 26 uppercase letters of the Roman alphabet
    """
    lett = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    return lett


def px(x: Union[int, float]) -> str:
    """
    Helper for providing a CSS length value in pixels.

    For certain parameters, a length value is required. Examples include the
    setting of font sizes (e.g., in `cell_text()`) and thicknesses of lines
    (e.g., in `cell_borders()`). Setting a length in pixels with `px()` allows
    for an absolute definition of size as opposed to the analogous helper
    function `pct()`.

    Parameters
    ----------
    x (Union[int, float])
        The integer or float value to format as a string (e.g., `"12px"`) for
        some `tab_options()` arguments that can take values as units of
        pixels (e.g., `table_font_size`).

    Examples
    --------
        >>> from gt import *
        >>> x = gt.px(12)
        >>> x
        >>> print(x)
    """
    return f"{x}px"


def pct(x: Union[int, float]) -> str:
    """
    Helper for providing a CSS length value as a percentage.

    A percentage value acts as a length value that is relative to an initial
    state. For instance an 80% value for something will size the target
    to 80% the size of its 'previous' value. This type of sizing is
    useful for sizing up or down a length value with an intuitive measure. This
    helper function can be used for the setting of font sizes (e.g., in
    `cell_text()`) and altering the thicknesses of lines (e.g., in
    `cell_borders()`. Should a more exact definition of size be required, the
    analogous helper function `pct()` will be more useful.

    Parameters
    ----------
    x (Union[int, float])
        The integer or float value to format as a string-based percentage value
        for some `tab_options()` arguments that can take percentage values
        (e.g., `table.width`).

    Examples
    --------
        >>> from gt import *
        >>> x = gt.pct(80)
        >>> x
        >>> print(x)
    """
    return f"{x}%"


class Text:
    def __init__(self, text: str, type: str):
        self.text: str = text
        self.type: str = type

