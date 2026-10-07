from __future__ import annotations

from bisect import bisect_right
from collections.abc import Callable
from decimal import Decimal
from math import isinf, isnan
from typing import TYPE_CHECKING, Any, Literal, TypeAlias

from great_tables._locations import RowSelectExpr, resolve_cols_c, resolve_rows_i
from great_tables._tab_create_modify import tab_style
from great_tables._tbl_data import (
    DataFrameLike,
    SelectExpr,
    _get_column_levels,
    get_column_names,
    get_rows,
    is_na,
    to_list,
)
from great_tables.loc import body
from great_tables.style import fill, text

from .constants import ALL_PALETTES, COLOR_NAME_TO_HEX, DEFAULT_PALETTE

if TYPE_CHECKING:
    from great_tables._types import GTSelf


RGBColor: TypeAlias = tuple[int, int, int]
ContrastAlgo: TypeAlias = Literal["apca", "wcag"]

# Coefficients for the SAPC APCA (Accessible Perceptual Contrast Algorithm); these values are
# current as of Beta 0.0.98G-4g (Oct 1, 2021)
_APCA_COEFFS = {
    "mainTRC": 2.4,
    "sRco": 0.2126729,
    "sGco": 0.7151522,
    "sBco": 0.0721750,
    "normBG": 0.56,
    "normTXT": 0.57,
    "revTXT": 0.62,
    "revBG": 0.65,
    "blkThrs": 0.022,
    "blkClmp": 1.414,
    "scaleBoW": 1.14,
    "scaleWoB": 1.14,
    "loBoWoffset": 0.027,
    "deltaYmin": 0.0005,
}


def data_color(
    self: GTSelf,
    columns: SelectExpr = None,
    rows: RowSelectExpr = None,
    palette: str | list[str] | None = None,
    domain: list[str] | list[int] | list[float] | None = None,
    midpoint: int | float | None = None,
    na_color: str | None = None,
    alpha: float | None = None,
    reverse: bool = False,
    autocolor_text: bool = True,
    contrast_algo: ContrastAlgo = "apca",
    truncate: bool = False,
    fn: Callable[[list[Any]], list[str | None]] | None = None,
) -> GTSelf:
    """
    Perform data cell colorization.

    It's possible to add color to data cells according to their values with the `data_color()`
    method. There is a multitude of ways to perform data cell colorizing here:

    - targeting: we can constrain which columns should receive the colorization treatment through
    the `columns=` argument)
    - color palettes: with `palette=` we could supply a list of colors composed of hexadecimal
    values or color names
    - value domain: we can either opt to have the range of values define the domain, or, specify
    one explicitly with the `domain=` argument
    - color-mapping function: for complete control over the mapping of values to colors, a
    function can be supplied to `fn=`
    - text autocoloring: `data_color()` will automatically recolor the foreground text to provide
    the best contrast (can be deactivated with `autocolor_text=False`)

    Parameters
    ----------
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.
    rows
        In conjunction with `columns=`, we can specify which rows should be colored. By default,
        all rows in the targeted columns will be colored. Alternatively, we can provide a list
        of row indices.
    palette
        The color palette to use. This should be a list of colors (e.g., `["#FF0000", "#00FF00",
        "#0000FF"]`). A ColorBrewer palette could also be used, just supply the name (reference
        available in the *Color palette access from ColorBrewer* section). If `None`, then a default
        palette will be used.
    domain
        The domain of values to use for the color scheme. This can be a list of floats, integers, or
        strings. If `None`, then the domain will be inferred from the data values (see the
        *How column values are mapped to colors* section for details).
    midpoint
        A value to center the color scale on, for numeric columns (e.g., `0` for values that
        represent a change). The midpoint receives the color at the center of the palette, which
        makes this most useful with a diverging palette like `["red", "white", "green"]` or
        `"RdBu"`. If `domain=` is `None`, then the domain is made symmetric around the midpoint so
        that values equally far from it on either side are equally strong in color. If `domain=`
        is supplied, then each side of the midpoint is scaled separately to its end of the domain
        (and the midpoint must lie within the domain). See the *Centering colors on a midpoint*
        section for details.
    na_color
        The color to use for missing values. If `None`, then the default color (`"#808080"`) will be
        used.
    alpha
        An optional, fixed alpha transparency value that will be applied to all color palette
        values.
    reverse
        Should the colors computed operate in the reverse order? If `True` then colors that normally
        change from red to blue will change in the opposite direction.
    autocolor_text
        Whether or not to automatically color the text of the data values. If `True`, then the text
        will be colored according to the background color of the cell.
    contrast_algo
        The color contrast algorithm to use when `autocolor_text=True`. By default this is
        `"apca"` (Accessible Perceptual Contrast Algorithm) and the alternative to this is
        `"wcag"` (Web Content Accessibility Guidelines). The chosen algorithm determines whether
        light or dark text provides better contrast against each cell's background color.
    truncate
        If `True`, then any values that fall outside of the domain will be truncated to the
        minimum or maximum value of the domain (will have the same color). If `False`, then any
        values that fall outside of the domain will be set to `NaN` and will follow the `na_color=`
        color.
    fn
        A color-mapping function. The function should take a list of data values (from a single
        column) as input and return a list of colors of the same length. Each color may be a
        hexadecimal color value (e.g., `"#FF0000"`) or a color name (e.g., `"red"`). All values are
        passed to the function, including missing values, so the function must handle those
        itself. Any position where the function returns `None` receives the `na_color=` color. If
        a function is supplied, then the `palette=`, `domain=`, `reverse=`, `truncate=`, and
        `midpoint=` arguments are ignored. The `alpha=`, `autocolor_text=`, and `contrast_algo=`
        arguments still apply to the returned colors. The
        [`col_numeric()`](`great_tables.col_numeric`), [`col_bin()`](`great_tables.col_bin`), and
        [`col_factor()`](`great_tables.col_factor`) helpers create ready-made color-mapping
        functions that can be supplied here.

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

    How column values are mapped to colors
    --------------------------------------
    Without `fn=`, each targeted column is mapped to colors in one of two ways, depending on the
    values it contains (missing values are set aside first):

    - numeric values (integers, floats, and `Decimal` values) are spread along the palette as a
    continuous gradient, from the lowest value in the domain to the highest
    - string values (including categorical columns) are treated as categories, with each one
    taking its own position along the palette

    Columns of any other type (e.g., dates) or with a mix of types will raise an error. To color
    these, supply a color-mapping function to `fn=` (see the *Custom color-mapping functions*
    section). Some further details on how values are handled:

    - missing values (`None`, `NaN`, and `pd.NA`) always receive the `na_color=` color
    - booleans are treated as numbers, so `True` takes the high end of the palette and `False` the
    low end
    - an inferred numeric domain spans the finite values only; any infinite values are given the
    color at the matching end of the palette (with a supplied `domain=`, infinite values are treated
    like any other value outside of the domain, following the `truncate=` setting)
    - an inferred categorical domain lists the categories in the order they first appear in the
    column, except for ordered categorical columns (an ordered Pandas `Categorical` or a Polars
    `Enum`), where the declared levels are used in their declared order (this includes any levels
    that don't appear in the data, so colors stay consistent no matter which `rows=` are colored)

    Supplying `domain=` overrides any of the inferred domains described above.

    Centering colors on a midpoint
    ------------------------------
    For numeric values that are naturally centered on some value (changes centered on `0`, ratios
    centered on `1`, scores centered on a target), the `midpoint=` argument pins that value to the
    center color of the palette. How the rest of the values map to colors depends on whether
    `domain=` is supplied. As an example, suppose a column spans from `-2` to `10` and we use
    `palette=["red", "white", "green"]` with `midpoint=0`:

    - without `domain=`, the domain becomes symmetric around the midpoint (here, `[-10, 10]`), so
    `10` is fully green while `-2` is only a pale red: the strength of a color reflects the distance
    from the midpoint, the same on both sides
    - with `domain=[-2, 10]`, each side of the midpoint is scaled separately, so `-2` is fully red
    and `10` is fully green (this is how three-color scales work in spreadsheet software, where both
    sides always use their full range of colors)

    For finer control (such as pinning every palette color to a specific value, or to a percentage
    of the way through the range of values), use `fn=col_numeric(stops=...)` (see
    [`col_numeric()`](`great_tables.col_numeric`)).

    Color palette access from ColorBrewer and viridis
    -------------------------------------------------
    All palettes from the ColorBrewer package can be accessed by providing the palette name in
    `palette=`. There are 35 available palettes:

    |    | Palette Name      | Colors  | Category    | Colorblind Friendly |
    |----|-------------------|---------|-------------|---------------------|
    | 1  | `"BrBG"`          | 11      | Diverging   | Yes                 |
    | 2  | `"PiYG"`          | 11      | Diverging   | Yes                 |
    | 3  | `"PRGn"`          | 11      | Diverging   | Yes                 |
    | 4  | `"PuOr"`          | 11      | Diverging   | Yes                 |
    | 5  | `"RdBu"`          | 11      | Diverging   | Yes                 |
    | 6  | `"RdYlBu"`        | 11      | Diverging   | Yes                 |
    | 7  | `"RdGy"`          | 11      | Diverging   | No                  |
    | 8  | `"RdYlGn"`        | 11      | Diverging   | No                  |
    | 9  | `"Spectral"`      | 11      | Diverging   | No                  |
    | 10 | `"Dark2"`         | 8       | Qualitative | Yes                 |
    | 11 | `"Paired"`        | 12      | Qualitative | Yes                 |
    | 12 | `"Set1"`          | 9       | Qualitative | No                  |
    | 13 | `"Set2"`          | 8       | Qualitative | Yes                 |
    | 14 | `"Set3"`          | 12      | Qualitative | No                  |
    | 15 | `"Accent"`        | 8       | Qualitative | No                  |
    | 16 | `"Pastel1"`       | 9       | Qualitative | No                  |
    | 17 | `"Pastel2"`       | 8       | Qualitative | No                  |
    | 18 | `"Blues"`         | 9       | Sequential  | Yes                 |
    | 19 | `"BuGn"`          | 9       | Sequential  | Yes                 |
    | 20 | `"BuPu"`          | 9       | Sequential  | Yes                 |
    | 21 | `"GnBu"`          | 9       | Sequential  | Yes                 |
    | 22 | `"Greens"`        | 9       | Sequential  | Yes                 |
    | 23 | `"Greys"`         | 9       | Sequential  | Yes                 |
    | 24 | `"Oranges"`       | 9       | Sequential  | Yes                 |
    | 25 | `"OrRd"`          | 9       | Sequential  | Yes                 |
    | 26 | `"PuBu"`          | 9       | Sequential  | Yes                 |
    | 27 | `"PuBuGn"`        | 9       | Sequential  | Yes                 |
    | 28 | `"PuRd"`          | 9       | Sequential  | Yes                 |
    | 29 | `"Purples"`       | 9       | Sequential  | Yes                 |
    | 30 | `"RdPu"`          | 9       | Sequential  | Yes                 |
    | 31 | `"Reds"`          | 9       | Sequential  | Yes                 |
    | 32 | `"YlGn"`          | 9       | Sequential  | Yes                 |
    | 33 | `"YlGnBu"`        | 9       | Sequential  | Yes                 |
    | 34 | `"YlOrBr"`        | 9       | Sequential  | Yes                 |
    | 35 | `"YlOrRd"`        | 9       | Sequential  | Yes                 |

    We can also use the *viridis* and associated color palettes by providing to `palette=` any of
    the following string values: `"viridis"`, `"plasma"`, `"inferno"`, `"magma"`, or `"cividis"`.

    Custom color-mapping functions
    ------------------------------
    When the built-in mapping (a palette spread across a domain) isn't what you need, you can
    supply your own color-mapping function to `fn=`. This gives complete control over how values
    become colors. Here's how such a function is used:

    - it's called once per targeted column, receiving a list of that column's values (only for the
    rows selected by `rows=`, in table order)
    - it must return a list of colors of the same length, where each color is a hexadecimal value
    (`"#RRGGBB"`, `"#RRGGBBAA"`, or the short `"#RGB"` form) or a CSS/X11 color name
    - missing values are included in the list, so the function must handle them: with pandas they
    usually arrive as `NaN` (or `None`/`pd.NA`, depending on the column type), and with Polars and
    PyArrow they arrive as `None`; `pd.isna()` catches all of these
    - returning `None` at any position gives that cell the `na_color=` color, which is the easiest
    way to deal with missing values
    - columns of any type can be colored (e.g., booleans or dates), since the numeric-or-string
    requirement of the built-in mapping doesn't apply

    When `fn=` is used, the `palette=`, `domain=`, `reverse=`, `truncate=`, and `midpoint=` arguments
    are ignored because the function takes over their roles. The `na_color=`, `alpha=`,
    `autocolor_text=`, and `contrast_algo=` arguments still apply to the colors that the function
    returns.

    Rather than writing a function from scratch, you can create one with these helpers (modeled on
    the color-mapping functions of the R **scales** package, which are commonly used with gt):

    - [`col_numeric()`](`great_tables.col_numeric`): a continuous gradient across a numeric domain,
    optionally with each palette color pinned to a specific value (or a percentage of the way
    through the range of values) with `stops=`
    - [`col_bin()`](`great_tables.col_bin`): numeric values cut into bins, with one color per bin
    - [`col_factor()`](`great_tables.col_factor`): one color per category, optionally with a fixed
    set of levels so colors stay consistent across tables

    Each helper accepts a palette in the same forms as `palette=` here (including ColorBrewer and
    viridis palette names). The numeric helpers also have their own `domain=` and `truncate=`
    arguments. Missing values, and values outside of the domain, give `None` by default, so the
    `na_color=` value given to `data_color()` is used for those cells. Because the helpers return
    ordinary functions, they can also be called inside your own function, for instance to compute a
    domain from the data before mapping it.

    Examples
    --------
    The `data_color()` method can be used without any supplied arguments to colorize a table. Let's
    do this with the `exibble` dataset:

    ```{python}
    from great_tables import GT
    from great_tables.data import exibble

    GT(exibble).data_color()
    ```

    What's happened is that `data_color()` applies background colors to all cells of every column
    with the palette of eight colors. Numeric columns will use 'numeric' methodology for color
    scaling whereas string-based columns will use the 'factor' methodology. The text color undergoes
    an automatic modification that maximizes contrast (since `autocolor_text=True` by default).

    We can target specific colors and apply color to just those columns. Let's do that and also
    supply `palette=` values of `"red"` and `"green"`.

    ```{python}
    GT(exibble).data_color(
        columns=["num", "currency"],
        palette=["red", "green"]
    )
    ```

    With those options in place we see that only the numeric columns `num` and `currency` received
    color treatments. Moreover, the palette colors were mapped to the lower and upper limits of the
    data in each column; interpolated colors were used for the values in between the numeric limits
    of the two columns.

    We can manually set the limits of the data with the `domain=` argument (which is preferable in
    most cases). Let's colorize just the currency column and set `domain=[0, 50]`. Any values that
    are either missing or lie outside of the domain will be colorized with the `na_color=` color
    (so we'll set that to `"lightgray"`).

    ```{python}
    GT(exibble).data_color(
        columns="currency",
        palette=["red", "green"],
        domain=[0, 50],
        na_color="lightgray"
    )
    ```

    For complete control over how values map to colors, we can supply a function to `fn=`. The
    function receives the list of values in a column (missing values included) and must return a
    list of colors of the same length. Here, values in the `num` column are colored according to
    whether they are below or above `100`. Returning `None` for the missing value means that it
    gets the `na_color=` color:

    ```{python}
    import pandas as pd

    def above_below_100(vals):
        return [None if pd.isna(x) else "lightblue" if x < 100 else "orange" for x in vals]

    GT(exibble).data_color(
        columns="num",
        fn=above_below_100,
        na_color="lightgray"
    )
    ```

    A color-mapping function is also useful for highlighting the sign of values. Here, positive
    changes are colored green, negative changes orange, and zero values are left white. Because
    the function assigns its own color to the missing value, `na_color=` isn't needed:

    ```{python}
    df = pd.DataFrame(
        {
            "region": ["North", "South", "East", "West", "Central"],
            "change": [12.5, -8.1, 0.0, 3.2, None],
        }
    )

    def sign_colors(vals):
        return [
            "#E0E0E0" if pd.isna(x) else "#1B9E77" if x > 0 else "#D95F02" if x < 0 else "#FFFFFF"
            for x in vals
        ]

    (
        GT(df)
        .data_color(columns="change", fn=sign_colors)
        .fmt_number(columns="change", decimals=1, force_sign=True)
    )
    ```

    For a gradient that's centered on zero, rather than fixed colors, we can use `midpoint=0` with a
    diverging palette. Negative changes become increasingly red and positive changes increasingly
    green, the further they are from zero. Because no `domain=` is given, the domain is made
    symmetric around zero, so the largest decrease (`-8.1`) is a less intense red than the largest
    increase (`12.5`) is green:

    ```{python}
    (
        GT(df)
        .data_color(columns="change", palette=["#D7191C", "white", "#1A9641"], midpoint=0)
        .fmt_number(columns="change", decimals=1, force_sign=True)
    )
    ```

    The midpoint doesn't have to be zero, and it doesn't have to sit in the middle of the domain.
    Here, sales are shown as a fraction of a target, so the midpoint is `1`. Supplying a `domain=`
    means that each side of the midpoint is scaled separately: the colors go from red to white over
    the wide range from 50% of the target up to the target, and from white to green over the
    narrower range from the target up to 120% of it:

    ```{python}
    sales_df = pd.DataFrame(
        {
            "rep": ["Ana", "Ben", "Cai", "Dee", "Eli"],
            "pct_of_target": [0.62, 0.88, 1.0, 1.08, 1.17],
        }
    )

    (
        GT(sales_df)
        .data_color(
            columns="pct_of_target",
            palette=["#D7191C", "white", "#1A9641"],
            domain=[0.5, 1.2],
            midpoint=1,
        )
        .fmt_percent(columns="pct_of_target", decimals=0)
    )
    ```

    To pin more than the midpoint, we can build the function with
    [`col_numeric()`](`great_tables.col_numeric`) and its `stops=` argument, which gives a value
    for each palette color. A stop can be a data value or a percentage of the way through the range
    of values in the column. Here, the lowest value is red, zero is white, and the highest value is
    green, so both sides use their full range of colors:

    ```{python}
    from great_tables import col_numeric

    (
        GT(df)
        .data_color(
            columns="change",
            fn=col_numeric(palette=["#D7191C", "white", "#1A9641"], stops=["0%", 0, "100%"]),
        )
        .fmt_number(columns="change", decimals=1, force_sign=True)
    )
    ```
    """

    # TODO: there is a circular import in palettes (which imports functions from this module)
    from great_tables._data_color.palettes import GradientPalette

    _validate_contrast_algo(contrast_algo)

    # If no color is provided to `na_color`, use a light gray color as a default
    if na_color is None:
        na_color = "#808080"
    else:
        na_color = _html_color(colors=[na_color], alpha=alpha)[0]

    # Resolve the palette to a list of hexadecimal color values
    palette = _resolve_palette(palette=palette, reverse=reverse, alpha=alpha)

    # Set a flag to indicate whether or not the domain should be calculated automatically
    autocalc_domain = domain is None

    if midpoint is not None and fn is None:
        _validate_midpoint(midpoint, domain=domain)

    # Get the internal data table
    data_table = self._tbl_data

    # If `columns` is a single value, convert it to a list; if it is None then
    # get a list of all columns in the table body
    columns_resolved: list[str]

    if columns is None:
        columns_resolved = get_column_names(data_table)
    else:
        columns_resolved = resolve_cols_c(data=self, expr=columns)

    row_res = resolve_rows_i(self, rows)
    row_pos = [name_pos[1] for name_pos in row_res]

    gt_obj = self

    # For each column targeted, get the data values as a new list object
    for col in columns_resolved:
        # This line handles both pandas and polars dataframes
        column_vals = to_list(get_rows(data_table[col], indexes=row_pos))

        # If a color-mapping function is provided, it determines the colors directly (bypassing
        # the palette, domain, and rescaling logic below)
        if fn is not None:
            color_vals = _apply_color_fn(
                fn=fn,
                col=col,
                vals=column_vals,
                na_color=na_color,
                alpha=alpha,
            )

            gt_obj = _apply_data_color_styles(
                gt_obj,
                col=col,
                row_pos=row_pos,
                color_vals=color_vals,
                autocolor_text=autocolor_text,
                contrast_algo=contrast_algo,
            )

            continue

        # Convert any `Decimal` values to floats so that they can be scaled like other numbers
        column_vals = [float(x) if isinstance(x, Decimal) else x for x in column_vals]

        # Filter out NA values from `column_vals`
        filtered_column_vals = [x for x in column_vals if not is_na(data_table, x)]

        # The methodology for domain calculation and rescaling depends on column values being:
        # (1) numeric (integers or floats), then the method should be 'numeric'
        # (2) strings, then the method should be 'factor'
        if len(filtered_column_vals) and all(
            isinstance(x, (int, float)) for x in filtered_column_vals
        ):
            if midpoint is not None:
                # Pin the midpoint to the center of the palette (an inferred domain is made
                # symmetric around the midpoint, a supplied one is scaled separately on each side)
                present_vals = [None if is_na(data_table, x) else x for x in column_vals]
                stops, positions = _midpoint_stops(midpoint, domain=domain, vals=present_vals)
                scaled_vals = _rescale_stops(
                    present_vals, stops=stops, positions=positions, truncate=truncate
                )

            else:
                # If `domain` is not provided, then infer it from the data values
                if autocalc_domain:
                    domain = _get_domain_numeric(df=data_table, vals=column_vals)

                # Rescale only the non-NA values in `column_vals` to the range [0, 1]
                scaled_vals = _rescale_numeric(
                    df=data_table, vals=column_vals, domain=domain, truncate=truncate
                )

            # Infinite values are left out of an inferred domain, so place them at either end of it
            if autocalc_domain:
                scaled_vals = [
                    (1.0 if x > 0 else 0.0) if _is_infinite(x) else scaled
                    for x, scaled in zip(column_vals, scaled_vals)
                ]

        elif all(isinstance(x, str) for x in filtered_column_vals):
            # (an all-missing column also lands here, and that's fine to color with `na_color=`)
            if midpoint is not None and filtered_column_vals:
                raise ValueError(
                    f"`midpoint=` can only be used with numeric columns, but column '{col}' "
                    "contains string values."
                )

            # If `domain` is not provided, then infer it from the data values
            # (for ordered categorical columns, use the declared levels instead)
            if autocalc_domain:
                domain = _get_column_levels(data_table, col) or _get_domain_factor(
                    df=data_table, vals=column_vals
                )

            # Rescale only the non-NA values in `column_vals` to the range [0, 1]
            scaled_vals = _rescale_factor(
                df=data_table, vals=column_vals, domain=domain, palette=palette
            )

        else:
            raise ValueError(
                f"Invalid column type provided ({col}). Please ensure that all columns are either numeric or strings."
            )

        # Replace NA values in `scaled_vals` with `None`
        scaled_vals = [None if is_na(data_table, x) else x for x in scaled_vals]

        # Create a color scale function from the palette
        color_scale_fn = GradientPalette(colors=palette)

        # Call the color scale function on the scaled values to get a list of colors
        color_vals = color_scale_fn(scaled_vals)

        # `GradientPalette` interpolates using RGB tuples, which have no alpha channel, so the
        # `alpha=` value baked into `palette` above is lost here; reapply it to the interpolated
        # colors (skipping `None` entries, which stand in for NA values)
        if alpha is not None:
            not_na_idx = [i for i, x in enumerate(color_vals) if x is not None]
            not_na_colors = [x for x in color_vals if x is not None]
            not_na_vals = _html_color(colors=not_na_colors, alpha=alpha)
            for i, val in zip(not_na_idx, not_na_vals):
                color_vals[i] = val

        # Replace 'None' values in `color_vals` with the `na_color=` color
        color_vals = [na_color if x is None else x for x in color_vals]

        gt_obj = _apply_data_color_styles(
            gt_obj,
            col=col,
            row_pos=row_pos,
            color_vals=color_vals,
            autocolor_text=autocolor_text,
            contrast_algo=contrast_algo,
        )

    return gt_obj


def _resolve_palette(
    palette: str | list[str] | None,
    reverse: bool = False,
    alpha: float | None = None,
) -> list[str]:
    """
    Resolve a palette specification to a list of hexadecimal color values.

    A value of `None` gives the default palette. A string is first checked against the names of
    the ColorBrewer and viridis palettes; if it isn't one of those, it's treated as a single color.
    """

    # If palette is not provided, use a default palette
    if palette is None:
        palette = DEFAULT_PALETTE
    elif isinstance(palette, str):
        # Check if the `palette` value refers to a ColorBrewer or viridis palette
        # and, if it is, then convert it to a list of hexadecimal color values; otherwise,
        # convert it to a list (this assumes that the value is a single color)
        palette = ALL_PALETTES.get(palette, [palette])

    # Reverse the palette if `reverse` is set to `True`
    if reverse:
        palette = palette[::-1]

    # Standardize values in `palette` to hexadecimal color values
    return _html_color(colors=list(palette), alpha=alpha)


def _apply_data_color_styles(
    gt_obj: GTSelf,
    col: str,
    row_pos: list[int],
    color_vals: list[str],
    autocolor_text: bool,
    contrast_algo: ContrastAlgo,
) -> GTSelf:
    # For every color value in `color_vals`, apply a fill to the corresponding cell
    # by using `tab_style()`
    for i, color_val in zip(row_pos, color_vals):
        if autocolor_text:
            fgnd_color = _ideal_fgnd_color(bgnd_color=color_val, algo=contrast_algo)

            gt_obj = tab_style(
                gt_obj,
                style=[text(color=fgnd_color), fill(color=color_val)],
                locations=body(columns=col, rows=[i]),
            )

        else:
            gt_obj = tab_style(
                gt_obj, style=fill(color=color_val), locations=body(columns=col, rows=[i])
            )

    return gt_obj


def _apply_color_fn(
    fn: Callable[[list[Any]], list[str | None]],
    col: str,
    vals: list[Any],
    na_color: str,
    alpha: float | None,
) -> list[str]:
    """
    Map column values to colors with a user-supplied color-mapping function.

    All values in `vals=` (including missing values) are passed to `fn=`, as in gt. Any positions
    where `fn=` returns `None` receive the `na_color=` color. All other colors are normalized to
    hexadecimal values (with `alpha=` applied, if provided).
    """

    fn_colors = list(fn(vals))

    if len(fn_colors) != len(vals):
        raise ValueError(
            f"The function supplied to `fn=` returned {len(fn_colors)} colors for column "
            f"'{col}' but {len(vals)} were expected. The function must return a list of "
            "colors with the same length as its input."
        )

    for color in fn_colors:
        if color is not None and not isinstance(color, str):
            raise TypeError(
                "The function supplied to `fn=` must return colors as strings (or `None`), "
                f"but returned a value of type {type(color).__name__} for column '{col}'."
            )

    color_vals = [na_color] * len(vals)

    # Normalize the returned colors (skipping `None` entries, which get the `na_color=` color)
    mapped = [(i, color) for i, color in enumerate(fn_colors) if color is not None]

    if mapped:
        normalized = _html_color(colors=[color for _, color in mapped], alpha=alpha)

        for (i, _), color in zip(mapped, normalized):
            color_vals[i] = color

    return color_vals


def _validate_contrast_algo(algo: str) -> None:
    if algo not in ("apca", "wcag"):
        raise ValueError(f'`contrast_algo=` must be either "apca" or "wcag", not {algo!r}.')


def _ideal_fgnd_color(
    bgnd_color: str,
    light: str = "#FFFFFF",
    dark: str = "#000000",
    algo: ContrastAlgo = "apca",
) -> str:
    _validate_contrast_algo(algo)

    # Compose alpha value from hexadecimal color value in `bgnd_color=`
    bgnd_color = _alpha_composite_with_white(bgnd_color)

    if algo == "apca":
        # The APCA contrast value is signed (its sign reflects polarity) so `abs()` is used below
        contrast_dark = _get_apca_contrast(txt_color=dark, bgnd_color=bgnd_color)
        contrast_light = _get_apca_contrast(txt_color=light, bgnd_color=bgnd_color)
    else:
        contrast_dark = _get_wcag_contrast_ratio(color_1=dark, color_2=bgnd_color)
        contrast_light = _get_wcag_contrast_ratio(color_1=light, color_2=bgnd_color)

    fgnd_color = dark if abs(contrast_dark) >= abs(contrast_light) else light

    return fgnd_color


def _alpha_composite_with_white(color: str) -> str:
    """
    Alpha composite a color with white background

    Parameters
    ----------
    color : str
        Hexadecimal color value, either #RRGGBB or #RRGGBBAA format

    Returns
    -------
    str
        Composited color in #RRGGBB format
    """

    # If no alpha channel, return as-is
    if len(color) != 9:
        return color

    # Extract RGB and alpha components
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)
    alpha = int(color[7:9], 16) / 255.0

    # White background (255, 255, 255) with full opacity
    white_r, white_g, white_b = 255, 255, 255

    # Apply alpha compositing formula: cr = cf * af + cb * ab * (1 - af)
    result_r = int(r * alpha + white_r * (1 - alpha))
    result_g = int(g * alpha + white_g * (1 - alpha))
    result_b = int(b * alpha + white_b * (1 - alpha))

    # Clamp values to [0, 255] range
    result_r = max(0, min(255, result_r))
    result_g = max(0, min(255, result_g))
    result_b = max(0, min(255, result_b))

    # Convert back to hex format
    # TODO: After refactor, use rgb_to_hex (now in palettes.py)
    return f"#{result_r:02X}{result_g:02X}{result_b:02X}"


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


def _get_apca_contrast(txt_color: str, bgnd_color: str) -> float:
    """
    Calculate the APCA lightness contrast (Lc) of text overlaid on a background color.

    Parameters
    ----------
    txt_color
        The text (foreground) color.
    bgnd_color
        The background color.

    Returns
    -------
    float
        The Lc contrast value, which lies roughly in the range of -108 to 106. Positive values
        indicate dark text on a light background whereas negative values indicate light text on a
        dark background.
    """

    txt_lum = _relative_luminance_apca(rgb=_hex_to_rgb(hex_color=txt_color))
    bgnd_lum = _relative_luminance_apca(rgb=_hex_to_rgb(hex_color=bgnd_color))

    return _get_apca_contrast_from_luminance(txt_lum=txt_lum, bgnd_lum=bgnd_lum)


def _get_apca_contrast_from_luminance(txt_lum: float, bgnd_lum: float) -> float:
    c = _APCA_COEFFS

    # If the luminance difference between background and text is nearly the same, treat that
    # as zero contrast
    if abs(bgnd_lum - txt_lum) < c["deltaYmin"]:
        return 0.0

    if bgnd_lum > txt_lum:
        # Normal polarity: dark text on a light background
        ratio = (bgnd_lum ** c["normBG"] - txt_lum ** c["normTXT"]) * c["scaleBoW"]
        ratio = 0.0 if ratio < 0.1 else ratio - c["loBoWoffset"]
    else:
        # Reverse polarity: light text on a dark background
        ratio = (bgnd_lum ** c["revBG"] - txt_lum ** c["revTXT"]) * c["scaleWoB"]
        ratio = 0.0 if ratio > -0.1 else ratio + c["loBoWoffset"]

    return ratio * 100


def _relative_luminance_apca(rgb: RGBColor) -> float:
    """
    Calculate the APCA screen luminance (Y) of an RGB color.

    Parameters
    ----------
    rgb
        The RGB color.

    Returns
    -------
    float
        The screen luminance, with a soft clamp applied to very dark colors.
    """

    c = _APCA_COEFFS

    r, g, b = ((x / 255) ** c["mainTRC"] for x in rgb)
    lum = r * c["sRco"] + g * c["sGco"] + b * c["sBco"]

    # Soft clamp near-black colors
    if lum <= c["blkThrs"]:
        lum += (c["blkThrs"] - lum) ** c["blkClmp"]

    return lum


def _hex_to_rgb(hex_color: str) -> RGBColor:
    """
    Convert a hexadecimal color value to RGB.

    Parameters
    ----------
    hex_color
        The hexadecimal color value.

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


def _relative_luminance(rgb: RGBColor) -> float:
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


def _html_color(colors: list[str], alpha: float | None = None) -> list[str]:
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
        # Translate named colors to hexadecimal values
        colors = _color_name_to_hex(colors=colors)

    # If `alpha` is not None, then we need to add the alpha value to the
    # color value but only if it doesn't already exist
    if alpha is not None:
        colors = _add_alpha(colors=colors, alpha=alpha)

    return colors


def _add_alpha(colors: list[str], alpha: float) -> list[str]:
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


def _color_name_to_hex(colors: list[str]) -> list[str]:
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
    return list(COLOR_NAME_TO_HEX)


def _is_short_hex(color: str) -> bool:
    import re

    pattern = r"^#[0-9a-fA-F]{3}([0-9a-fA-F])?$"
    return re.match(pattern, color) is not None


def _is_hex_col(colors: list[str]) -> list[bool]:
    import re

    return [bool(re.match(r"^#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$", color)) for color in colors]


def _is_standard_hex_col(colors: list[str]) -> list[bool]:
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

    # Return the expanded 6-digit hexadecimal color value
    expanded = "#" + "".join(x * 2 for x in hex_color)
    return expanded.upper()


def _rescale_numeric(
    df: DataFrameLike, vals: list[int | float], domain: list[float], truncate: bool = False
) -> list[float | None]:
    """
    Rescale numeric values

    Rescale the numeric values in `vals=` to the range [0, 1] using the domain provided.
    """

    # Get the minimum and maximum values from `domain`
    domain_min, domain_max = domain

    # Get the range of values in `domain`
    domain_range = domain_max - domain_min

    if domain_range == 0:
        # In the case where the domain range is 0, all scaled values in `vals` will be `0`
        return [0.0 if not is_na(df, x) else x for x in vals]

    # Rescale the values in `vals` to the range [0, 1], pass through NA values
    scaled: list[float | None] = [
        None if is_na(df, x) else (x - domain_min) / domain_range for x in vals
    ]

    min_val, max_val = (0, 1) if truncate else (None, None)

    return [None if x is None else min_val if x < 0 else max_val if x > 1 else x for x in scaled]


def _validate_midpoint(midpoint: Any, domain: list[float] | None) -> None:
    if (
        isinstance(midpoint, bool)
        or not isinstance(midpoint, (int, float))
        or isinf(midpoint)
        or isnan(midpoint)
    ):
        raise ValueError(f"`midpoint=` must be a finite number, not {midpoint!r}.")

    if domain is not None and not domain[0] <= midpoint <= domain[1]:
        raise ValueError(
            f"`midpoint=` ({midpoint!r}) must lie within the range of `domain=` ({domain!r})."
        )


def _midpoint_stops(
    midpoint: float, domain: list[float] | None, vals: list[float | None]
) -> tuple[list[float], list[float]]:
    """
    Get the stops (data values) and palette positions for a scale centered on `midpoint=`.

    The midpoint takes the center of the palette (position `0.5`) and the ends of the domain take
    the ends of the palette. Without a `domain=`, the domain is made symmetric around the midpoint,
    reaching as far as the furthest finite value in `vals=` (which may contain `None` values).
    """

    if domain is None:
        finite = [x for x in vals if x is not None and not _is_infinite(x)]
        extent = max((abs(x - midpoint) for x in finite), default=0)
        domain = [midpoint - extent, midpoint + extent]

    stops = [domain[0], midpoint, domain[1]]
    positions = [0.0, 0.5, 1.0]

    # Drop any ends of the domain that coincide with the midpoint, so that the midpoint itself
    # always resolves to the center of the palette
    keep = [i for i in range(3) if i == 1 or stops[i] != midpoint]

    return [stops[i] for i in keep], [positions[i] for i in keep]


def _rescale_stops(
    vals: list[float | None], stops: list[float], positions: list[float], truncate: bool = False
) -> list[float | None]:
    """
    Rescale numeric values to palette positions in the range [0, 1] with piecewise-linear stops.

    Each value in `stops=` (a non-decreasing list of data values) is pinned to the palette position
    at the same index in `positions=`, and values in between are linearly interpolated. A value
    that exactly matches a repeated stop takes the position of the last of those stops. Values
    outside of the outermost stops give `None` (unless `truncate=True`, which moves them to the
    nearest outermost stop), as do `None` values in `vals=`.
    """

    lo, hi = stops[0], stops[-1]

    scaled: list[float | None] = []

    for x in vals:
        if x is None:
            scaled.append(None)
            continue

        if truncate:
            x = min(max(x, lo), hi)

        if x < lo or x > hi:
            scaled.append(None)
            continue

        # The number of stops at or below `x` (at least 1, since `x >= lo`)
        i = bisect_right(stops, x)

        if stops[i - 1] == x:
            scaled.append(positions[i - 1])
        else:
            frac = (x - stops[i - 1]) / (stops[i] - stops[i - 1])
            scaled.append(positions[i - 1] + frac * (positions[i] - positions[i - 1]))

    return scaled


def _rescale_factor(
    df: DataFrameLike, vals: list[int | float], domain: list[float], palette: list[str]
) -> list[float]:
    """
    Rescale factor values

    Rescale the factor values in `vals=` to the range [0, 1] using the domain provided.
    """

    domain_length = len(domain)
    palette_length = len(palette)

    if domain_length <= palette_length:
        # If the length of `domain` is less than or equal to the length of `palette`, then clip the
        # length of `palette` to the length of `domain`
        palette = palette[:domain_length]

    # For each value in `vals`, get the index of the value in `domain` but if not present then
    # use NA; then scale these index values to the range [0, 1]
    scaled_vals = _rescale_numeric(
        df=df,
        vals=[None if is_na(df, x) or x not in domain else domain.index(x) for x in vals],
        domain=[0, domain_length - 1],
    )

    return scaled_vals


def _get_domain_numeric(df: DataFrameLike, vals: list[int | float]) -> list[float]:
    """
    Get the domain of numeric values.

    Get the domain of numeric values in `vals=` as a list of two values: the min and max values.
    """

    # Exclude any NA and infinite values from `vals`
    vals = [x for x in vals if not is_na(df, x) and not _is_infinite(x)]

    # Without any finite values there is no range to infer, so use a zero-width domain
    if not vals:
        return [0, 0]

    # Get the minimum and maximum values from `vals`
    domain_min = min(vals)
    domain_max = max(vals)

    # Create the domain
    domain = [domain_min, domain_max]

    return domain


def _is_infinite(x: Any) -> bool:
    return isinstance(x, float) and isinf(x)


def _get_domain_factor(df: DataFrameLike, vals: list[str]) -> list[str]:
    """
    Get the domain of factor values.

    Get the domain of factor values in `vals=` as a list of the unique values in the order provided.
    """

    # Exclude any NA values from `vals`
    vals = [x for x in vals if not is_na(df, x)]

    # Create the domain by getting the unique values in `vals` in order provided
    seen: list[str] = []

    for item in vals:
        if item not in seen:
            seen.append(item)

    return seen
