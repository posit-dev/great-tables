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

    The font stacks and the individual fonts used by platform
    ---------------------------------------------------------
    ### System UI (`"system-ui"`)

    ```css
    font-family: system-ui, sans-serif;
    ```

    The operating system interface's default typefaces are known as system UI fonts. They contain a
    variety of font weights, are quite readable at small sizes, and are perfect for UI elements.
    These typefaces serve as a great starting point for text in data tables and so this font stack
    is the default for **Great Tables**.

    ### Transitional (`"transitional"`)

    ```css
    font-family: Charter, 'Bitstream Charter', 'Sitka Text', Cambria, serif;
    ```

    The Enlightenment saw the development of transitional typefaces, which combine Old Style and
    Modern typefaces. *Times New Roman*, a transitional typeface created for the Times of London
    newspaper, is among the most well-known instances of this style.

    ### Old Style (`"old-style"`)

    ```css
    font-family: 'Iowan Old Style', 'Palatino Linotype', 'URW Palladio L', P052, serif;
    ```

    Old style typefaces were created during the Renaissance and are distinguished by diagonal
    stress, a lack of contrast between thick and thin strokes, and rounded serifs. *Garamond* is
    among the most well-known instances of an antique typeface.

    ### Humanist (`"humanist"`)

    ```css
    font-family: Seravek, 'Gill Sans Nova', Ubuntu, Calibri, 'DejaVu Sans', source-sans-pro, sans-serif;
    ```

    Low contrast between thick and thin strokes and organic, calligraphic forms are traits of
    humanist typefaces. These typefaces, which draw their inspiration from Renaissance calligraphy,
    are frequently regarded as being more readable and easier to read than other sans serif
    typefaces.

    ### Geometric Humanist (`"geometric-humanist"`)

    ```css
    font-family: Avenir, Montserrat, Corbel, 'URW Gothic', source-sans-pro, sans-serif;
    ```

    Clean, geometric forms and consistent stroke widths are characteristics of geometric humanist
    typefaces. These typefaces, which are frequently used for headlines and other display purposes,
    are frequently thought to be contemporary and slick in appearance. A well-known example of this
    classification is *Futura*.

    ### Classical Humanist (`"classical-humanist"`)

    ```css
    font-family: Optima, Candara, 'Noto Sans', source-sans-pro, sans-serif;
    ```

    The way the strokes gradually widen as they approach the stroke terminals without ending in a
    serif is what distinguishes classical humanist typefaces. The stone carving on Renaissance-era
    tombstones and classical Roman capitals served as inspiration for these typefaces.

    ### Neo-Grotesque (`"neo-grotesque"`)

    ```css
    font-family: Inter, Roboto, 'Helvetica Neue', 'Arial Nova', 'Nimbus Sans', Arial, sans-serif;
    ```

    Neo-grotesque typefaces are a form of sans serif that originated in the late 19th and early 20th
    centuries. They are distinguished by their crisp, geometric shapes and regular stroke widths.
    *Helvetica* is among the most well-known examples of a Neo-grotesque typeface.

    ### Monospace Slab Serif (`"monospace-slab-serif"`)

    ```css
    font-family: 'Nimbus Mono PS', 'Courier New', monospace;
    ```

    Monospace slab serif typefaces are distinguished by their fixed-width letters, which are the
    same width irrespective of their shape, and their straightforward, geometric forms. For reports,
    tabular work, and technical documentation, this technique is used to simulate typewriter output.

    ### Monospace Code (`"monospace-code"`)

    ```css
    font-family: ui-monospace, 'Cascadia Code', 'Source Code Pro', Menlo, Consolas, 'DejaVu Sans Mono', monospace;
    ```

    Specifically created for use in programming and other technical applications, monospace code
    typefaces are used in these fields. These typefaces are distinguished by their clear, readable
    forms and monospaced design, which ensures that all letters and characters are the same width.

    ### Industrial (`"industrial"`)

    ```css
    font-family: Bahnschrift, 'DIN Alternate', 'Franklin Gothic Medium', 'Nimbus Sans Narrow', sans-serif-condensed, sans-serif;
    ```

    The development of industrial typefaces began in the late 19th century and was greatly
    influenced by the industrial and technological advancements of the time. Industrial typefaces
    are distinguished by their strong sans serif letterforms, straightforward appearance, and use of
    geometric shapes and straight lines.

    ### Rounded Sans (`"rounded-sans"`)

    ```css
    font-family: ui-rounded, 'Hiragino Maru Gothic ProN', Quicksand, Comfortaa, Manjari, 'Arial Rounded MT', 'Arial Rounded MT Bold', Calibri, source-sans-pro, sans-serif;
    ```

    The rounded, curved letterforms that define rounded typefaces give them a softer, friendlier
    appearance. The typeface's rounded edges give it a more natural and playful feel, making it
    appropriate for use in casual or kid-friendly designs. Since the 1950s, the rounded sans-serif
    design has gained popularity and is still frequently used in branding, graphic design, and other
    fields.

    ### Slab Serif (`"slab-serif"`)

    ```css
    font-family: Rockwell, 'Rockwell Nova', 'Roboto Slab', 'DejaVu Serif', 'Sitka Small', serif;
    ```

    Slab Serif typefaces are distinguished by the thick, block-like serifs that appear at the ends
    of each letterform. Typically, these serifs are unbracketed, which means that they do not have
    any curved or tapered transitions to the letter's main stroke.

    ### Antique (`"antique"`)

    ```css
    font-family: Superclarendon, 'Bookman Old Style', 'URW Bookman', 'URW Bookman L', 'Georgia Pro', Georgia, serif;
    ```

    Serif typefaces that were popular in the 19th century include antique typefaces, also referred
    to as Egyptians. They are distinguished by their thick, uniform stroke weight and block-like
    serifs. The typeface *Clarendon* is a highly regarded example of this style and *Superclarendon*
    is a modern take on that revered typeface.

    ### Didone (`"didone"`)

    ```css
    font-family: Didot, 'Bodoni MT', 'Noto Serif Display', 'URW Palladio L', P052, Sylfaen, serif;
    ```

    Didone typefaces, also referred to as Modern typefaces, are distinguished by their vertical
    stress, sharp contrast between thick and thin strokes, and hairline serifs without bracketing.
    The Didone style first appeared in the late 18th century and became well-known in the early
    19th century. *Bodoni* and *Didot* are two of the most well-known typefaces in this category.

    ### Handwritten (`"handwritten"`)

    ```css
    font-family: 'Segoe Print', 'Bradley Hand', Chilanka, TSCu_Comic, casual, cursive;
    ```

    The appearance and feel of handwriting are replicated by handwritten typefaces. Although there
    are a wide variety of handwriting styles, this font stack tends to use a more casual and
    commonplace style. In regards to these types of fonts in tables, one can say that any table
    having a handwritten font will evoke a feeling of gleefulness.

    Examples
    --------
    Using select columns from the `exibble` dataset, let's create a table with a number of
    components added. Following that, we'll set a font for the entire table using the
    `tab_options()` method with the `table_font_names` parameter. Instead of passing a list of font
    names, we'll use the `system_fonts()` helper function to get a font stack. In this case, we'll
    use the `"industrial"` font stack.

    ```{python}
    from great_tables import GT, exibble, md, system_fonts

    (
      GT(
        exibble[["num", "char", "currency", "row", "group"]],
        rowname_col="row",
        groupname_col="group"
      )
      .tab_header(
        title=md("Data listing from **exibble**"),
        subtitle=md("`exibble` is a **Great Tables** dataset.")
      )
      .fmt_number(columns="num")
      .fmt_currency(columns="currency")
      .tab_source_note(source_note="This is only a subset of the dataset.")
      .opt_align_table_header(align="left")
      .tab_options(table_font_names=system_fonts("industrial"))
    )
    ```

    Invoking the `system_fonts()` helper function with the `"industrial"` argument will return a
    list of font names that make up the font stack. This is exactly the type of input that the
    `table_font_names` parameter requires.
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
