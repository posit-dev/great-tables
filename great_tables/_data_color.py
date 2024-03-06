from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    Union,
    List,
    Optional,
)
from great_tables._constants import DEFAULT_PALETTE, ALL_PALETTES
from great_tables._tbl_data import is_na, DataFrameLike
from great_tables.style import fill, text
from great_tables.loc import body
import numpy as np
from mizani.palettes import gradient_n_pal

if TYPE_CHECKING:
    from great_tables._types import GTSelf


def data_color(
    self: GTSelf,
    columns: Union[str, List[str], None] = None,
    palette: Union[str, List[str], None] = None,
    domain: Union[List[str], List[float], List[int], None] = None,
    na_color: Optional[str] = None,
    alpha: Optional[Union[int, float]] = None,
    reverse: bool = False,
    autocolor_text: bool = True,
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
    - text autocoloring: `data_color()` will automatically recolor the foreground text to provide
    the best contrast (can be deactivated with `autocolor_text=False`)

    Parameters
    ----------
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.
    palette
        The color palette to use. This should be a list of colors (e.g., `["#FF0000", "#00FF00",
        "#0000FF"]`). A ColorBrewer palette could also be used, just supply the name (reference
        available in the *Color palette access from ColorBrewer* section). If `None`, then a default
        palette will be used.
    domain
        The domain of values to use for the color scheme. This can be a list of floats, integers, or
        strings. If `None`, then the domain will be inferred from the data values.
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

    Returns
    -------
    GT
        The GT object is returned. This is the same object that the method is called on so that we
        can facilitate method chaining.

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

    Examples
    --------
    The `data_color()` method can be used without any supplied arguments to colorize a table. Let's
    do this with the `exibble` dataset:

    ```{python}
    import great_tables as gt

    gt.GT(gt.data.exibble).data_color()
    ```

    What's happened is that `data_color()` applies background colors to all cells of every column
    with the palette of eight colors. Numeric columns will use 'numeric' methodology for color
    scaling whereas string-based columns will use the 'factor' methodology. The text color undergoes
    an automatic modification that maximizes contrast (since `autocolor_text=True` by default).

    We can target specific colors and apply color to just those columns. Let's do that and also
    supply `palette=` values of `"red"` and `"green"`.

    ```{python}

    gt.GT(gt.data.exibble).data_color(
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
    gt.GT(gt.data.exibble).data_color(
        columns="currency",
        palette=["red", "green"],
        domain=[0, 50],
        na_color="lightgray"
    )
    ```
    """

    from great_tables._utils_color import _html_color, _ideal_fgnd_color

    # If no color is provided to `na_color`, use a light gray color as a default
    if na_color is None:
        na_color = "#808080"
    else:
        na_color = _html_color(colors=[na_color], alpha=alpha)[0]

    # If palette is not provided, use a default palette
    if palette is None:
        palette = DEFAULT_PALETTE
    elif isinstance(palette, str):
        # Check if the `palette` value refers to a ColorBrewer or viridis palette
        # and, if it is, then convert it to a list of hexadecimal color values; otherwise,
        # convert it to a list (this assumes that the value is a single color)
        if palette in ALL_PALETTES:
            palette = ALL_PALETTES[palette]
        else:
            palette = [palette]

    # Reverse the palette if `reverse` is set to `True`
    if reverse:
        palette = palette[::-1]

    # Standardize values in `palette` to hexadecimal color values
    palette = _html_color(colors=palette, alpha=alpha)

    # Set a flag to indicate whether or not the domain should be calculated automatically
    if domain is None:
        autocalc_domain = True
    else:
        autocalc_domain = False

    # Get the internal data table
    data_table = self._tbl_data

    # If `columns` is a single value, convert it to a list; if it is None then
    # get a list of all columns in the table body
    columns_resolved: List[str]

    if isinstance(columns, str):
        columns_resolved = [columns]
    elif columns is None:
        columns_resolved = data_table.columns
    else:
        columns_resolved = columns

    gt_obj = self

    # For each column targeted, get the data values as a new list object
    for col in columns_resolved:
        column_vals = data_table[col].to_list()

        # Filter out NA values from `column_vals`
        filtered_column_vals = [x for x in column_vals if not is_na(data_table, x)]

        # The methodology for domain calculation and rescaling depends on column values being:
        # (1) numeric (integers or floats), then the method should be 'numeric'
        # (2) strings, then the method should be 'factor'
        if len(filtered_column_vals) and all(
            isinstance(x, (int, float)) for x in filtered_column_vals
        ):
            # If `domain` is not provided, then infer it from the data values
            if autocalc_domain:
                domain = _get_domain_numeric(df=data_table, vals=column_vals)

            # Rescale only the non-NA values in `column_vals` to the range [0, 1]
            scaled_vals = _rescale_numeric(df=data_table, vals=column_vals, domain=domain)

        elif all(isinstance(x, str) for x in filtered_column_vals):
            # If `domain` is not provided, then infer it from the data values
            if autocalc_domain:
                domain = _get_domain_factor(df=data_table, vals=column_vals)

            # Rescale only the non-NA values in `column_vals` to the range [0, 1]
            scaled_vals = _rescale_factor(
                df=data_table, vals=column_vals, domain=domain, palette=palette
            )

        else:
            raise ValueError(
                f"Invalid column type provided ({col}). Please ensure that all columns are either numeric or strings."
            )

        # Replace NA values in `scaled_vals` with `None`
        scaled_vals = [np.nan if is_na(data_table, x) else x for x in scaled_vals]

        # Create a color scale function from the palette
        color_scale_fn = gradient_n_pal(colors=palette)

        # Call the color scale function on the scaled values to get a list of colors
        color_vals = color_scale_fn(scaled_vals)

        # Replace 'None' and 'np.nan' values in `color_vals` with the `na_color=` color
        color_vals = [na_color if is_na(data_table, x) else x for x in color_vals]

        # for every color value in color_vals, apply a fill to the corresponding cell
        # by using `tab_style()`
        for i, _ in enumerate(color_vals):
            if autocolor_text:
                fgnd_color = _ideal_fgnd_color(bgnd_color=color_vals[i])

                gt_obj = gt_obj.tab_style(
                    style=[text(color=fgnd_color), fill(color=color_vals[i])],
                    locations=body(columns=col, rows=[i]),
                )

            else:
                gt_obj = gt_obj.tab_style(
                    style=fill(color=color_vals[i]), locations=body(columns=col, rows=[i])
                )
    return gt_obj


def _rescale_numeric(
    df: DataFrameLike, vals: List[Union[int, float]], domain: List[float]
) -> List[float]:
    """
    Rescale numeric values

    Rescale the numeric values in `vals=` to the range [0, 1] using the domain provided.
    """

    # Get the minimum and maximum values from `domain`
    domain_min = domain[0]
    domain_max = domain[1]

    # Get the range of values in `domain`
    domain_range = domain_max - domain_min

    if domain_range == 0:
        # In the case where the domain range is 0, all scaled values in `vals` will be `0`
        scaled_vals = [0.0 if not is_na(df, x) else x for x in vals]
    else:
        # Rescale the values in `vals` to the range [0, 1], pass through NA values
        scaled_vals = [(x - domain_min) / domain_range if not is_na(df, x) else x for x in vals]

    # Add NA values to any values in `scaled_vals` that are not in the [0, 1] range
    scaled_vals = [x if not is_na(df, x) and (x >= 0 and x <= 1) else np.nan for x in scaled_vals]

    return scaled_vals


def _rescale_factor(
    df: DataFrameLike, vals: List[Union[int, float]], domain: List[float], palette: List[str]
) -> List[float]:
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
        vals=[domain.index(x) if x in domain else np.nan for x in vals],
        domain=[0, domain_length],
    )

    return scaled_vals


def _get_domain_numeric(df: DataFrameLike, vals: List[Union[int, float]]) -> List[float]:
    """
    Get the domain of numeric values.

    Get the domain of numeric values in `vals=` as a list of two values: the min and max values.
    """

    # Exclude any NA values from `vals`
    vals = [x for x in vals if not is_na(df, x)]

    # Get the minimum and maximum values from `vals`
    domain_min = min(vals)
    domain_max = max(vals)

    # Create the domain
    domain = [domain_min, domain_max]

    return domain


def _get_domain_factor(df: DataFrameLike, vals: List[str]) -> List[str]:
    """
    Get the domain of factor values.

    Get the domain of factor values in `vals=` as a list of the unique values in the order provided.
    """

    # Exclude any NA values from `vals`
    vals = [x for x in vals if not is_na(df, x)]

    # Create the domain by getting the unique values in `vals` in order provided
    unique_list: List[str] = []
    seen: List[str] = []

    for item in vals:
        if item not in seen:
            unique_list.append(item)
            seen.append(item)

    return seen
