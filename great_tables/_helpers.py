from __future__ import annotations

import random
import string
from typing import Any, Callable, Literal

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


def px(x: int | float) -> str:
    """
    Helper for providing a CSS length value in pixels.

    For certain parameters, a length value is required. Examples include the setting of font sizes
    (e.g., in `cell_text()`) and thicknesses of lines (e.g., in `cell_borders()`). Setting a length
    in pixels with `px()` allows for an absolute definition of size as opposed to the analogous
    helper function `pct()`.

    Parameters
    ----------
    x
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


def pct(x: int | float) -> str:
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
    x
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
    text
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
    text
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
    n
        The number of lowercase letters to use in the random ID string. Defaults to 10.

    Returns
    -------
    str
        A string that constitutes a random ID value.
    """
    return "".join(random.choices(letters(), k=n))


def letters() -> list[str]:
    """Lowercase letters of the Roman alphabet

    Returns:
        list[str]: the 26 lowercase letters of the Roman alphabet
    """
    return list(string.ascii_lowercase)


def LETTERS() -> list[str]:
    """Uppercase letters of the Roman alphabet

    Returns:
        list[str]: the 26 uppercase letters of the Roman alphabet
    """
    return list(string.ascii_uppercase)


def system_fonts(name: FontStackName = "system-ui") -> list[str]:
    """Get a themed font stack that works well across systems.

    A font stack can be obtained from `system_fonts()` using one of various keywords such as
    `"system-ui"`, `"old-style"`, and `"humanist"` (there are 15 in total) representing a themed set
    of fonts. These sets comprise a font family that has been tested to work across a wide range of
    computer systems.

    Parameters
    ----------
    name
        The name of a font stack. Must be drawn from the set of `"system-ui"` (the default),
        `"transitional"`, `"old-style"`, `"humanist"`, `"geometric-humanist"`,
        `"classical-humanist"`, `"neo-grotesque"`, `"monospace-slab-serif"`, `"monospace-code"`,
        `"industrial"`, `"rounded-sans"`, `"slab-serif"`, `"antique"`, `"didone"`, and
        `"handwritten"`.

    Returns
    -------
    list[str]
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


def _get_font_stack(name: FontStackName = "system-ui", add_emoji: bool = True) -> list[str]:
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


# This could probably be removed and nanoplot_options made into a dataclass
# the built-in dataclass decorator doesn't do any validation / coercion, but
# we could do that in the a __post_init__ hook. (I would switch it over to a
# dataclass and then pair on a post_init hook).
# Check that certain values are either a list or a single value
def _normalize_listable_nanoplot_options(nano_opt: Any, option_type: Any) -> list[Any] | None:

    if nano_opt is None:
        return None

    if not isinstance(nano_opt, (option_type, list)):
        raise ValueError(f"Nanoplot option must be a {option_type} or a list of {option_type}s")

    # If it is a list, check that the values are integers
    if isinstance(nano_opt, list):
        if not all(isinstance(x, int) for x in nano_opt):
            raise ValueError(f"Nanoplot option must be a list of {option_type}s")

    # If it is a single value, convert it to a list
    if not isinstance(nano_opt, list):
        nano_opt = [nano_opt]

    return nano_opt


def nanoplot_options(
    data_point_radius: int | list[int] | None = None,
    data_point_stroke_color: str | list[str] | None = None,
    data_point_stroke_width: int | list[int] | None = None,
    data_point_fill_color: str | list[str] | None = None,
    data_line_type: str | None = None,
    data_line_stroke_color: str | None = None,
    data_line_stroke_width: int | None = None,
    data_area_fill_color: str | None = None,
    data_bar_stroke_color: str | list[str] | None = None,
    data_bar_stroke_width: int | list[int] | None = None,
    data_bar_fill_color: str | list[str] | None = None,
    data_bar_negative_stroke_color: str | None = None,
    data_bar_negative_stroke_width: int | None = None,
    data_bar_negative_fill_color: str | None = None,
    reference_line_color: str | None = None,
    reference_area_fill_color: str | None = None,
    vertical_guide_stroke_color: str | None = None,
    vertical_guide_stroke_width: int | None = None,
    show_data_points: bool | None = None,
    show_data_line: bool | None = None,
    show_data_area: bool | None = None,
    show_reference_line: bool | None = None,
    show_reference_area: bool | None = None,
    show_vertical_guides: bool | None = None,
    show_y_axis_guide: bool | None = None,
    interactive_data_values: bool | None = None,
    y_val_fmt_fn: Callable[..., str] | None = None,
    y_axis_fmt_fn: Callable[..., str] | None = None,
    y_ref_line_fmt_fn: Callable[..., str] | None = None,
    currency: str | None = None,
) -> dict[str, Any]:
    """
    Helper for setting the options for a nanoplot.

    When using `cols_nanoplot()`, the defaults for the generated nanoplots can be modified with
    `nanoplot_options()` within the `options=` argument.

    Parameters
    ----------

    data_point_radius
        The `data_point_radius=` option lets you set the radius for each of the data points. By
        default this is set to `10`. Individual radius values can be set by using a list of numeric
        values; however, the list provided must match the number of data points.
    data_point_stroke_color
        The default stroke color of the data points is `"#FFFFFF"` (`"white"`). This works well when
        there is a visible data line combined with data points with a darker fill color. The stroke
        color can be modified with `data_point_stroke_color=` for all data points by supplying a
        single color value. With a list of colors, each data point's stroke color can be changed
        (ensure that the list length matches the number of data points).
    data_point_stroke_width
        The width of the outside stroke for the data points can be modified with the
        `data_point_stroke_width=` option. By default, a value of `4` (as in '4px') is used.
    data_point_fill_color
        By default, all data points have a fill color of `"#FF0000"` (`"red"`). This can be changed
        for all data points by providing a different color to `data_point_fill_color=`. And, a list
        of different colors can be supplied so long as the length is equal to the number of data
        points; the fill color values will be applied in order of left to right.
    data_line_type
        This can accept either `"curved"` or `"straight"`. Curved lines are recommended when the
        nanoplot has less than 30 points and data points are evenly spaced. In most other cases,
        straight lines might present better.
    data_line_stroke_color
        The color of the data line can be modified from its default `"#4682B4"` (`"steelblue"`)
        color by supplying a color to the `data_line_stroke_color=` option.
    data_line_stroke_width
        The width of the connecting data line can be modified with `data_line_stroke_width=`. By
        default, a value of `4` (as in '4px') is used.
    data_area_fill_color
        The fill color for the area that bounds the data points in line plot. The default is
        `"#FF0000"` (`"red"`) but can be changed by providing a color value to
        `data_area_fill_color=`.
    data_bar_stroke_color
        The color of the stroke used for the data bars can be modified from its default `"#3290CC"`
        color by supplying a color to `data_bar_stroke_color=`.
    data_bar_stroke_width
        The width of the stroke used for the data bars can be modified with the
        `data_bar_stroke_width=` option. By default, a value of `4` (as in '4px') is used.
    data_bar_fill_color
        By default, all data bars have a fill color of `"#3FB5FF"`. This can be changed for all data
        bars by providing a different color to `data_bar_fill_color=`. And, a list of different
        colors can be supplied so long as the length is equal to the number of data bars; the fill
        color values will be applied in order of left to right.
    data_bar_negative_stroke_color
        The color of the stroke used for the data bars that have negative values. The default color
        is `"#CC3243"` but this can be changed by supplying a color value to the
        `data_bar_negative_stroke_color=` option.
    data_bar_negative_stroke_width
        The width of the stroke used for negative value data bars. This has the same default as
        `data_bar_stroke_width=` with a value of `4` (as in '4px'). This can be changed by giving a
        numeric value to the `data_bar_negative_stroke_width=` option.
    data_bar_negative_fill_color
        By default, all negative data bars have a fill color of `"#D75A68"`. This can however be
        changed by providing a color value to `data_bar_negative_fill_color=`.
    reference_line_color
        The reference line will have a color of `"#75A8B0"` if it is set to appear. This color can
        be changed by providing a single color value to `reference_line_color=`.
    reference_area_fill_color
        If a reference area has been defined and is visible it has by default a fill color of
        `"#A6E6F2"`. This can be modified by declaring a color value in the
        `reference_area_fill_color=` option.
    vertical_guide_stroke_color
        Vertical guides appear when hovering in the vicinity of data points. Their default color is
        `"#911EB4"` (a strong magenta color) and a fill opacity value of `0.4` is automatically
        applied to this. However, the base color can be changed with the
        `vertical_guide_stroke_color=` option.
    vertical_guide_stroke_width
        The vertical guide's stroke width, by default, is relatively large at `12` (this is '12px').
        This is modifiable by setting a different value with `vertical_guide_stroke_width=`.
    show_data_points
        By default, all data points in a nanoplot are shown but this layer can be hidden by setting
        `show_data_points=` to `False`.
    show_data_line
        The data line connects data points together and it is shown by default. This data line layer
        can be hidden by setting `show_data_line=` to `False`.
    show_data_area
        The data area layer is adjacent to the data points and the data line. It is shown by default
        but can be hidden with `show_data_area=False`.
    show_reference_line
        The layer with a horizontal reference line appears underneath that of the data points and
        the data line. Like vertical guides, hovering over a reference will show its value. The
        reference line (if available) is shown by default but can be hidden by setting
        `show_reference_line=` to `False`.
    show_reference_area
        The reference area appears at the very bottom of the layer stack, if it is available (i.e.,
        defined in `cols_nanoplot()`). It will be shown in the default case but can be hidden by
        using `show_reference_area=False`.
    show_vertical_guides
        Vertical guides appear when hovering over data points. This hidden layer is active by
        default but can be deactivated by using `show_vertical_guides=False`.
    show_y_axis_guide
        The *y*-axis guide will appear when hovering over the far left side of a nanoplot. This
        hidden layer is active by default but can be deactivated by using `show_y_axis_guide=False`.
    interactive_data_values
        By default, numeric data values will be shown only when the user interacts with certain
        regions of a nanoplot. This is because the values may be numerous (i.e., clutter the display
        when all are visible) and it can be argued that the values themselves are secondary to the
        presentation. However, for some types of plots (like horizontal bar plots), a persistent
        display of values alongside the plot marks may be desirable. By setting
        `interactive_data_values=False` we can opt for always displaying the data values alongside
        the plot components.
    y_val_fmt_fn
        If providing a function to `y_val_fmt_fn=`, customized formatting of the *y* values
        associated with the data points/bars is possible.
    y_axis_fmt_fn
        A function supplied to `y_axis_fmt_fn=` will result in customized formatting of the *y*-axis
        label values.
    y_ref_line_fmt_fn
        Providing a function for `y_ref_line_fmt_fn=` yields customized formatting of the reference
        line (if present).
    currency
        If the values are to be displayed as currency values, supply either: (1) a 3-letter currency
        code (e.g., `"USD"` for U.S. Dollars, `"EUR"` for the Euro currency), or (2) a common
        currency name (e.g., `"dollar"`, `"pound"`, `"yen"`, etc.).
    """

    data_point_radius = _normalize_listable_nanoplot_options(
        nano_opt=data_point_radius, option_type=int
    )
    data_point_stroke_color = _normalize_listable_nanoplot_options(
        nano_opt=data_point_stroke_color, option_type=str
    )
    data_point_stroke_width = _normalize_listable_nanoplot_options(
        nano_opt=data_point_stroke_width, option_type=int
    )
    data_point_fill_color = _normalize_listable_nanoplot_options(
        nano_opt=data_point_fill_color, option_type=str
    )
    data_bar_stroke_color = _normalize_listable_nanoplot_options(
        nano_opt=data_bar_stroke_color, option_type=str
    )
    data_bar_stroke_width = _normalize_listable_nanoplot_options(
        nano_opt=data_bar_stroke_width, option_type=int
    )
    data_bar_fill_color = _normalize_listable_nanoplot_options(
        nano_opt=data_bar_fill_color, option_type=str
    )

    data_point_radius = data_point_radius or 10
    data_point_stroke_color = data_point_stroke_color or "#FFFFFF"
    data_point_stroke_width = data_point_stroke_width or 4
    data_point_fill_color = data_point_fill_color or "#FF0000"

    data_line_type = data_line_type or "curved"
    data_line_stroke_color = data_line_stroke_color or "#4682B4"
    data_line_stroke_width = data_line_stroke_width or 8

    data_area_fill_color = data_area_fill_color or "#FF0000"

    data_bar_stroke_color = data_bar_stroke_color or "#3290CC"
    data_bar_stroke_width = data_bar_stroke_width or 4
    data_bar_fill_color = data_bar_fill_color or "#3FB5FF"

    data_bar_negative_stroke_color = data_bar_negative_stroke_color or "#CC3243"
    data_bar_negative_stroke_width = data_bar_negative_stroke_width or 4
    data_bar_negative_fill_color = data_bar_negative_fill_color or "#D75A68"

    reference_line_color = reference_line_color or "#75A8B0"
    reference_area_fill_color = reference_area_fill_color or "#A6E6F2"

    vertical_guide_stroke_color = vertical_guide_stroke_color or "#911EB4"
    vertical_guide_stroke_width = vertical_guide_stroke_width or 12

    show_data_points = True if show_data_points is None else show_data_points
    show_data_line = True if show_data_line is None else show_data_line
    show_data_area = True if show_data_area is None else show_data_area
    show_reference_line = True if show_reference_line is None else show_reference_line
    show_reference_area = True if show_reference_area is None else show_reference_area
    show_vertical_guides = True if show_vertical_guides is None else show_vertical_guides
    show_y_axis_guide = True if show_y_axis_guide is None else show_y_axis_guide

    interactive_data_values = interactive_data_values or True

    # y_val_fmt_fn, y_axis_fmt_fn, and y_ref_line_fmt_fn
    # are not assigned to a default value

    # currency is also not assigned a default value.

    nanoplot_options_dict = {
        "data_point_radius": data_point_radius,
        "data_point_stroke_color": data_point_stroke_color,
        "data_point_stroke_width": data_point_stroke_width,
        "data_point_fill_color": data_point_fill_color,
        "data_line_type": data_line_type,
        "data_line_stroke_color": data_line_stroke_color,
        "data_line_stroke_width": data_line_stroke_width,
        "data_area_fill_color": data_area_fill_color,
        "data_bar_stroke_color": data_bar_stroke_color,
        "data_bar_stroke_width": data_bar_stroke_width,
        "data_bar_fill_color": data_bar_fill_color,
        "data_bar_negative_stroke_color": data_bar_negative_stroke_color,
        "data_bar_negative_stroke_width": data_bar_negative_stroke_width,
        "data_bar_negative_fill_color": data_bar_negative_fill_color,
        "reference_line_color": reference_line_color,
        "reference_area_fill_color": reference_area_fill_color,
        "vertical_guide_stroke_color": vertical_guide_stroke_color,
        "vertical_guide_stroke_width": vertical_guide_stroke_width,
        "show_data_points": show_data_points,
        "show_data_line": show_data_line,
        "show_data_area": show_data_area,
        "show_reference_line": show_reference_line,
        "show_reference_area": show_reference_area,
        "show_vertical_guides": show_vertical_guides,
        "show_y_axis_guide": show_y_axis_guide,
        "interactive_data_values": interactive_data_values,
        "y_val_fmt_fn": y_val_fmt_fn,
        "y_axis_fmt_fn": y_axis_fmt_fn,
        "y_ref_line_fmt_fn": y_ref_line_fmt_fn,
        "currency": currency,
    }

    return nanoplot_options_dict
