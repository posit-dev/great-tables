from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, List, Optional, Union

import pandas as pd
import polars as pl
from matplotlib import colormaps as mpl_colormaps
from matplotlib.colors import Colormap, ListedColormap, Normalize, to_hex

from great_tables._data_color.base import _html_color, _ideal_fgnd_color
from great_tables._data_color.constants import DEFAULT_PALETTE
from great_tables._tbl_data import is_na
from great_tables.loc import body
from great_tables.style import fill, text

if TYPE_CHECKING:
    from great_tables._types import GTSelf


def is_numeric(x: Any) -> bool:
    return isinstance(x, (int, float))


def is_numeric_or_none(x: Any) -> bool:
    return x is None or is_numeric(x)


def data_color_mpl(
    self: GTSelf,
    columns: Union[str, List[str], None] = None,
    cmap: Colormap | str | list[str] | None = None,
    norm: Normalize | Callable[[float], float] | None = None,
    na_color: Optional[str] = None,
    alpha: Union[int, float] = 1.0,
    reverse: bool = False,
    autocolor_text: bool = True,
) -> GTSelf:
    """
    Prototype for matplotlib-based colorization.

    Perform data cell colorization.

    - targeting: we can constrain which columns should receive the colorization treatment through
    the `columns=` argument)
    - colormap: we can specify the colormap to use with the `cmap_name=` argument
    - normalization: we can specify the normalization function to use with the `norm=` argument,
    which is a mapping from the data to the domain of the colormap, i.e. [0, 1]
    - text autocoloring: `data_color()` will automatically recolor the foreground text to provide
    the best contrast (can be deactivated with `autocolor_text=False`)

    Parameters
    ----------
    columns
        The columns to target. Can either be a single column name or a series of column names
        provided in a list.
    cmap
        The name of the colormap to use. This should be a valid matplotlib colormap name (e.g.,
        `"viridis"`, `"plasma"`, `"inferno"`, `"magma"`, etc.). Can also be a
        `matplotlib.colors.Colormap` object or a list of colors which are passed to ListedColormap
        to construct a colormap.
    norm
        The normalization function to use. This can be a `matplotlib.colors.Normalize` object, a
        callable function that takes a single float and returns a single float, or `None`. If `None`,
        then the default normalization linearly scales the data to the range [0, 1].
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
    """

    # If no color is provided to `na_color`, use a light gray color as a default
    if na_color is None:
        na_color = "#808080"
    else:
        na_color = _html_color(colors=[na_color], alpha=alpha)[0]

    colormap = _handle_cmap_arg(cmap, reverse=reverse)

    data_table = self._tbl_data
    columns_resolved: List[str]

    if isinstance(columns, str):
        columns_resolved = [columns]
    elif columns is None:
        columns_resolved = data_table.columns
    else:
        columns_resolved = columns

    # check all columns are numeric
    for col in columns_resolved:
        column_values = data_table[col].to_list()
        if not all(map(is_numeric_or_none, column_values)):
            raise ValueError(
                f"Invalid column type provided ({col}) for data_color. Please ensure that all columns are numeric."
            )

    if norm is None:  # default normalization uses all data to min-max scale
        data_subset = data_table[columns_resolved]
        norm = _get_default_norm(data_subset)

    for col in columns_resolved:
        column_values = data_table[col].to_list()

        color_values = []
        for value in column_values:
            if is_na(data_table, value):
                color_values.append(na_color)
            else:
                scaled_value = norm(value)
                color_no_alpha = colormap(scaled_value)
                color = (*color_no_alpha[:3], alpha)  # in RGBA format last value is alpha
                color = to_hex(color, keep_alpha=True)
                color_values.append(color)

        for i, _ in enumerate(color_values):
            if autocolor_text:
                fgnd_color = _ideal_fgnd_color(bgnd_color=color_values[i])

                self = self.tab_style(
                    style=[text(color=fgnd_color), fill(color=color_values[i])],
                    locations=body(columns=col, rows=[i]),
                )

            else:
                self = self.tab_style(
                    style=fill(color=color_values[i]), locations=body(columns=col, rows=[i])
                )

    return self


def _get_default_norm(data: pl.DataFrame | pd.DataFrame) -> Normalize:
    if isinstance(data, pl.DataFrame):
        vmin = data.min().min_horizontal()[0]
        vmax = data.max().max_horizontal()[0]
    elif isinstance(data, pd.DataFrame):
        vmin = data.min().min()
        vmax = data.max().max()
    else:
        raise ValueError(
            f"Invalid data type provided for data. Expected either a pandas or polars DataFrame but got: {type(data)}."
        )
    norm = Normalize(vmin=vmin, vmax=vmax)
    return norm


def _handle_cmap_arg(cmap, reverse: bool = False) -> Colormap:
    if cmap is None:  # construct data_color's default palette with matplotlib
        colormap = ListedColormap(DEFAULT_PALETTE)
    elif isinstance(cmap, Colormap):
        colormap = cmap
    elif isinstance(cmap, list) and all(isinstance(c, str) for c in cmap):
        colormap = ListedColormap(DEFAULT_PALETTE)
    elif cmap in mpl_colormaps:
        colormap = mpl_colormaps[cmap]
    else:
        raise ValueError(
            f"Invalid colormap provided ({cmap}). Please provide a valid matplotlib colormap name, a "
            f"`matplotlib.colors.Colormap` object, or a list of colors."
        )

    if reverse:
        colormap = colormap.reversed()
    return colormap
