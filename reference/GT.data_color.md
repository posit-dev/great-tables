## GT.data_color()


Perform data cell colorization.


Usage

``` python
GT.data_color(
    columns=None,
    rows=None,
    palette=None,
    domain=None,
    na_color=None,
    alpha=None,
    reverse=False,
    autocolor_text=True,
    truncate=False
)
```


It's possible to add color to data cells according to their values with the [data_color()](GT.data_color.md#great_tables.GT.data_color) method. There is a multitude of ways to perform data cell colorizing here:

- targeting: we can constrain which columns should receive the colorization treatment through the `columns=` argument)
- color palettes: with `palette=` we could supply a list of colors composed of hexadecimal values or color names
- value domain: we can either opt to have the range of values define the domain, or, specify one explicitly with the `domain=` argument
- text autocoloring: [data_color()](GT.data_color.md#great_tables.GT.data_color) will automatically recolor the foreground text to provide the best contrast (can be deactivated with `autocolor_text=False`)


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which rows should be colored. By default, all rows in the targeted columns will be colored. Alternatively, we can provide a list of row indices.

`palette: str | list[str] | None = None`  
The color palette to use. This should be a list of colors (e.g., `["#FF0000", "#00FF00", "#0000FF"]`). A ColorBrewer palette could also be used, just supply the name (reference available in the *Color palette access from ColorBrewer* section). If `None`, then a default palette will be used.

`domain: list[str] | list[int] | list[float] | None = None`  
The domain of values to use for the color scheme. This can be a list of floats, integers, or strings. If `None`, then the domain will be inferred from the data values.

`na_color: str | None = None`  
The color to use for missing values. If `None`, then the default color (`"#808080"`) will be used.

`alpha: int | float | None = None`  
An optional, fixed alpha transparency value that will be applied to all color palette values.

`reverse: bool = ``False`  
Should the colors computed operate in the reverse order? If `True` then colors that normally change from red to blue will change in the opposite direction.

`autocolor_text: bool = ``True`  
Whether or not to automatically color the text of the data values. If `True`, then the text will be colored according to the background color of the cell.

`truncate: bool = ``False`  
If `True`, then any values that fall outside of the domain will be truncated to the minimum or maximum value of the domain (will have the same color). If `False`, then any values that fall outside of the domain will be set to `NaN` and will follow the `na_color=` color.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Color Palette Access From Colorbrewer And Viridis

All palettes from the ColorBrewer package can be accessed by providing the palette name in `palette=`. There are 35 available palettes:

|     | Palette Name | Colors | Category    | Colorblind Friendly |
|-----|--------------|--------|-------------|---------------------|
| 1   | `"BrBG"`     | 11     | Diverging   | Yes                 |
| 2   | `"PiYG"`     | 11     | Diverging   | Yes                 |
| 3   | `"PRGn"`     | 11     | Diverging   | Yes                 |
| 4   | `"PuOr"`     | 11     | Diverging   | Yes                 |
| 5   | `"RdBu"`     | 11     | Diverging   | Yes                 |
| 6   | `"RdYlBu"`   | 11     | Diverging   | Yes                 |
| 7   | `"RdGy"`     | 11     | Diverging   | No                  |
| 8   | `"RdYlGn"`   | 11     | Diverging   | No                  |
| 9   | `"Spectral"` | 11     | Diverging   | No                  |
| 10  | `"Dark2"`    | 8      | Qualitative | Yes                 |
| 11  | `"Paired"`   | 12     | Qualitative | Yes                 |
| 12  | `"Set1"`     | 9      | Qualitative | No                  |
| 13  | `"Set2"`     | 8      | Qualitative | Yes                 |
| 14  | `"Set3"`     | 12     | Qualitative | No                  |
| 15  | `"Accent"`   | 8      | Qualitative | No                  |
| 16  | `"Pastel1"`  | 9      | Qualitative | No                  |
| 17  | `"Pastel2"`  | 8      | Qualitative | No                  |
| 18  | `"Blues"`    | 9      | Sequential  | Yes                 |
| 19  | `"BuGn"`     | 9      | Sequential  | Yes                 |
| 20  | `"BuPu"`     | 9      | Sequential  | Yes                 |
| 21  | `"GnBu"`     | 9      | Sequential  | Yes                 |
| 22  | `"Greens"`   | 9      | Sequential  | Yes                 |
| 23  | `"Greys"`    | 9      | Sequential  | Yes                 |
| 24  | `"Oranges"`  | 9      | Sequential  | Yes                 |
| 25  | `"OrRd"`     | 9      | Sequential  | Yes                 |
| 26  | `"PuBu"`     | 9      | Sequential  | Yes                 |
| 27  | `"PuBuGn"`   | 9      | Sequential  | Yes                 |
| 28  | `"PuRd"`     | 9      | Sequential  | Yes                 |
| 29  | `"Purples"`  | 9      | Sequential  | Yes                 |
| 30  | `"RdPu"`     | 9      | Sequential  | Yes                 |
| 31  | `"Reds"`     | 9      | Sequential  | Yes                 |
| 32  | `"YlGn"`     | 9      | Sequential  | Yes                 |
| 33  | `"YlGnBu"`   | 9      | Sequential  | Yes                 |
| 34  | `"YlOrBr"`   | 9      | Sequential  | Yes                 |
| 35  | `"YlOrRd"`   | 9      | Sequential  | Yes                 |

We can also use the *viridis* and associated color palettes by providing to `palette=` any of the following string values: `"viridis"`, `"plasma"`, `"inferno"`, `"magma"`, or `"cividis"`.


## Examples

The [data_color()](GT.data_color.md#great_tables.GT.data_color) method can be used without any supplied arguments to colorize a table. Let's do this with the [exibble](data.exibble.md#great_tables.data.exibble) dataset:


``` python
from great_tables import GT
from great_tables.data import exibble

GT(exibble).data_color()
```


| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 |  | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
|  | fig | six | 2015-06-15 |  | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven |  | 19:10 | 2018-07-07 05:22 |  | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 |  | 0.44 | row_8 | grp_b |


What's happened is that [data_color()](GT.data_color.md#great_tables.GT.data_color) applies background colors to all cells of every column with the palette of eight colors. Numeric columns will use 'numeric' methodology for color scaling whereas string-based columns will use the 'factor' methodology. The text color undergoes an automatic modification that maximizes contrast (since `autocolor_text=True` by default).

We can target specific colors and apply color to just those columns. Let's do that and also supply `palette=` values of `"red"` and `"green"`.


``` python
GT(exibble).data_color(
    columns=["num", "currency"],
    palette=["red", "green"]
)
```


| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 |  | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
|  | fig | six | 2015-06-15 |  | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven |  | 19:10 | 2018-07-07 05:22 |  | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 |  | 0.44 | row_8 | grp_b |


With those options in place we see that only the numeric columns `num` and `currency` received color treatments. Moreover, the palette colors were mapped to the lower and upper limits of the data in each column; interpolated colors were used for the values in between the numeric limits of the two columns.

We can manually set the limits of the data with the `domain=` argument (which is preferable in most cases). Let's colorize just the currency column and set `domain=[0, 50]`. Any values that are either missing or lie outside of the domain will be colorized with the `na_color=` color (so we'll set that to `"lightgray"`).


``` python
GT(exibble).data_color(
    columns="currency",
    palette=["red", "green"],
    domain=[0, 50],
    na_color="lightgray"
)
```


| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 |  | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
|  | fig | six | 2015-06-15 |  | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven |  | 19:10 | 2018-07-07 05:22 |  | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 |  | 0.44 | row_8 | grp_b |
