from typing import Union, List, Literal
import random
from typing_extensions import TypeAlias
from ._text import Text


FontStackName: TypeAlias = Literal[
    "system-ui",
    "transitional",
    "old-style",
    "humanist",
    "geometric-humanist",
    "classical-humanist",
    "neo-grotesque",
    "monospace-slab-serif",
    "monospace-code",
    "industrial",
    "rounded-sans",
    "slab-serif",
    "antique",
    "didone",
    "handwritten",
]


def px(x: Union[int, float]) -> str:
    """
    Helper for providing a CSS length value in pixels.

    For certain parameters, a length value is required. Examples include the setting of font sizes
    (e.g., in `cell_text()`) and thicknesses of lines (e.g., in `cell_borders()`). Setting a length
    in pixels with `px()` allows for an absolute definition of size as opposed to the analogous
    helper function `pct()`.

    Parameters
    ----------
    x : Union[int, float]
        The integer or float value to format as a string (e.g., `"12px"`) for some arguments that
        can take values as units of pixels.

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

    A percentage value acts as a length value that is relative to an initial state. For instance an
    80% value for something will size the target to 80% the size of its 'previous' value. This type
    of sizing is useful for sizing up or down a length value with an intuitive measure. This helper
    function can be used for the setting of font sizes (e.g., in `cell_text()`) and altering the
    thicknesses of lines (e.g., in `cell_borders()`. Should a more exact definition of size be
    required, the analogous helper function `pct()` will be more useful.

    Parameters
    ----------
    x : Union[int, float]
        The integer or float value to format as a string-based percentage value for some arguments
        that can take percentage values.

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

    Markdown can be used in certain places (e.g., source notes, table title/subtitle, etc.) and we
    can expect it to render to HTML. There is also the [`html()`](`great_tables.html`) helper
    function that allows you to use raw HTML text.

    Parameters
    ----------
    text : str
        The text that is understood to contain Markdown formatting.

    Returns
    -------
    Text
        An instance of the Text class is returned, where the text `type` is `"from_markdown"`.
    """
    return Text(text=text, type="from_markdown")


def html(text: str) -> Text:
    """Interpret input text as HTML-formatted text.

    For certain pieces of text (like in column labels or table headings) we may want to express them
    as raw HTML. In fact, with HTML, anything goes so it can be much more than just text. The
    `html()` function will guard the input HTML against escaping, so, your HTML tags will come
    through as HTML when rendered.

    Parameters
    ----------
    text : str
        The text that is understood to contain HTML formatting.

    Returns
    -------
    Text
        An instance of the Text class is returned, where the text `type` is `"html"`.
    """
    return Text(text=text, type="html")


def random_id(n: int = 10) -> str:
    """Helper for creating a random `id` for an output table

    Parameters
    ----------
    n : int
        The number of lowercase letters to use in the random ID string. Defaults to 10.

    Returns
    -------
    str
        A string that constitutes a random ID value.
    """
    return "".join(random.choices(letters(), k=n))


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


def system_fonts(name: FontStackName = "system-ui") -> List[str]:
    """Get a themed font stack that works well across systems.

    A font stack can be obtained from `system_fonts()` using one of various keywords such as
    `"system-ui"`, `"old-style"`, and `"humanist"` (there are 15 in total) representing a themed set
    of fonts. These sets comprise a font family that has been tested to work across a wide range of
    computer systems.

    Parameters
    ----------
    name : FontStackName, optional
        The name of a font stack. Must be drawn from the set of `"system-ui"` (the default),
        `"transitional"`, `"old-style"`, `"humanist"`, `"geometric-humanist"`,
        `"classical-humanist"`, `"neo-grotesque"`, `"monospace-slab-serif"`, `"monospace-code"`,
        `"industrial"`, `"rounded-sans"`, `"slab-serif"`, `"antique"`, `"didone"`, and
        `"handwritten"`.

    Returns
    -------
    List[str]
        A list of font names that make up the font stack.
    """
    return _get_font_stack(name)


def _get_font_stack(name: FontStackName = "system-ui", add_emoji=True) -> List[str]:
    font_stack_names = [
        "system-ui",
        "transitional",
        "old-style",
        "humanist",
        "geometric-humanist",
        "classical-humanist",
        "neo-grotesque",
        "monospace-slab-serif",
        "monospace-code",
        "industrial",
        "rounded-sans",
        "slab-serif",
        "antique",
        "didone",
        "handwritten",
    ]

    if name not in font_stack_names:
        raise ValueError(f"Invalid font stack name: {name}")

    if name == "system-ui":
        font_stack = ["system-ui", "sans-serif"]
    elif name == "transitional":
        font_stack = ["Charter", "Bitstream Charter", "Sitka Text", "Cambria", "serif"]
    elif name == "old-style":
        font_stack = ["Iowan Old Style", "Palatino Linotype", "URW Palladio L", "P052", "serif"]
    elif name == "humanist":
        font_stack = [
            "Seravek",
            "Gill Sans Nova",
            "Ubuntu",
            "Calibri",
            "DejaVu Sans",
            "source-sans-pro",
            "sans-serif",
        ]
    elif name == "geometric-humanist":
        font_stack = [
            "Avenir",
            "Montserrat",
            "Corbel",
            "URW Gothic",
            "source-sans-pro",
            "sans-serif",
        ]
    elif name == "classical-humanist":
        font_stack = ["Optima", "Candara", "Noto Sans", "source-sans-pro", "sans-serif"]
    elif name == "neo-grotesque":
        font_stack = [
            "Inter",
            "Roboto",
            "Helvetica Neue",
            "Arial Nova",
            "Nimbus Sans",
            "Arial",
            "sans-serif",
        ]
    elif name == "monospace-slab-serif":
        font_stack = ["Nimbus Mono PS", "Courier New", "monospace"]
    elif name == "monospace-code":
        font_stack = [
            "ui-monospace",
            "Cascadia Code",
            "Source Code Pro",
            "Menlo",
            "Consolas",
            "DejaVu Sans Mono",
            "monospace",
        ]
    elif name == "industrial":
        font_stack = [
            "Bahnschrift",
            "DIN Alternate",
            "Franklin Gothic Medium",
            "Nimbus Sans Narrow",
            "sans-serif-condensed",
            "sans-serif",
        ]
    elif name == "rounded-sans":
        font_stack = [
            "ui-rounded",
            "Hiragino Maru Gothic ProN",
            "Quicksand",
            "Comfortaa",
            "Manjari",
            "Arial Rounded MT",
            "Arial Rounded MT Bold",
            "Calibri",
            "source-sans-pro",
            "sans-serif",
        ]
    elif name == "slab-serif":
        font_stack = [
            "Rockwell",
            "Rockwell Nova",
            "Roboto Slab",
            "DejaVu Serif",
            "Sitka Small",
            "serif",
        ]
    elif name == "antique":
        font_stack = [
            "Superclarendon",
            "Bookman Old Style",
            "URW Bookman",
            "URW Bookman L",
            "Georgia Pro",
            "Georgia",
            "serif",
        ]
    elif name == "didone":
        font_stack = [
            "Didot",
            "Bodoni MT",
            "Noto Serif Display",
            "URW Palladio L",
            "P052",
            "Sylfaen",
            "serif",
        ]
    elif name == "handwritten":
        font_stack = ["Segoe Print", "Bradley Hand", "Chilanka", "TSCu_Comic", "casual", "cursive"]

    if add_emoji:
        font_stack.extend(
            ["Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"]
        )

    return font_stack
