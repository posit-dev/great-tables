from typing import Union, List
import random

from ._text import Text


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


def md(text: str) -> Text:
    """Interpret input text as Markdown-formatted text.

    Markdown! It's a wonderful thing. We can use it in certain places (e.g.,
    footnotes, source notes, the table title, etc.) and expect it to render to
    HTML as Markdown does. There is the `html()` helper that allows you to ferry
    in HTML but this function `md()`... it's almost like a two-for-one deal (you
    get to use Markdown plus any HTML fragments at the same time).

    Args:
        text (str): The text that is understood to contain Markdown
        formatting.

    Returns:
        Text: An instance of the Text class is returned, where the text
        `type` is 'markdown'.
    """
    return Text(text=text, type="markdown")


def html(text: str) -> Text:
    """Interpret input text as HTML-formatted text.

    For certain pieces of text (like in column labels or table headings) we may
    want to express them as raw HTML. In fact, with HTML, anything goes so it
    can be much more than just text. The `html()` function will guard the input
    HTML against escaping, so, your HTML tags will come through as HTML when
    rendered... to HTML.

    Args:
        text (str): The text that is understood to contain HTML formatting.

    Returns:
        Text: An instance of the Text class is returned, where the text
        `type` is 'html'.
    """
    return Text(text=text, type="html")


def random_id(n: int = 10) -> str:
    """Helper for creating a random `id` for a gt table

    Args:
        n (int, optional): The number of lowercase letters to use in the random
        ID string. Defaults to 10.

    Returns:
        str: A string that constitutes a random ID value.
    """
    return "".join(random.choices(letters(), k=n))
