# GT.data_color()


Perform data cell colorization.


Usage

``` python
GT.data_color(
    columns=None,
    rows=None,
    palette=None,
    domain=None,
    midpoint=None,
    na_color=None,
    alpha=None,
    reverse=False,
    autocolor_text=True,
    contrast_algo="apca",
    truncate=False,
    fn=None,
)
```


It's possible to add color to data cells according to their values with the [data_color()](GT.data_color.md#great_tables.GT.data_color) method. There is a multitude of ways to perform data cell colorizing here:

- targeting: we can constrain which columns should receive the colorization treatment through the `columns=` argument)
- color palettes: with `palette=` we could supply a list of colors composed of hexadecimal values or color names
- value domain: we can either opt to have the range of values define the domain, or, specify one explicitly with the `domain=` argument
- color-mapping function: for complete control over the mapping of values to colors, a function can be supplied to `fn=`
- text autocoloring: [data_color()](GT.data_color.md#great_tables.GT.data_color) will automatically recolor the foreground text to provide the best contrast (can be deactivated with `autocolor_text=False`)


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which rows should be colored. By default, all rows in the targeted columns will be colored. Alternatively, we can provide a list of row indices.

`palette: str | list[str] | None = None`  
The color palette to use. This should be a list of colors (e.g., `["#FF0000", "#00FF00", "#0000FF"]`). A ColorBrewer palette could also be used, just supply the name (reference available in the *Color palette access from ColorBrewer* section). If `None`, then a default palette will be used.

`domain: list[str] | list[int] | list[float] | None = None`  
The domain of values to use for the color scheme. This can be a list of floats, integers, or strings. If `None`, then the domain will be inferred from the data values (see the *How column values are mapped to colors* section for details).

`midpoint: int | float | None = None`  
A value to center the color scale on, for numeric columns (e.g., `0` for values that represent a change). The midpoint receives the color at the center of the palette, which makes this most useful with a diverging palette like `["red", "white", "green"]` or `"RdBu"`. If `domain=` is `None`, then the domain is made symmetric around the midpoint so that values equally far from it on either side are equally strong in color. If `domain=` is supplied, then each side of the midpoint is scaled separately to its end of the domain (and the midpoint must lie within the domain). See the *Centering colors on a midpoint* section for details.

`na_color: str | None = None`  
The color to use for missing values. If `None`, then the default color (`"#808080"`) will be used.

`alpha: float | None = None`  
An optional, fixed alpha transparency value that will be applied to all color palette values.

`reverse: bool = ``False`  
Should the colors computed operate in the reverse order? If `True` then colors that normally change from red to blue will change in the opposite direction.

`autocolor_text: bool = ``True`  
Whether or not to automatically color the text of the data values. If `True`, then the text will be colored according to the background color of the cell.

`contrast_algo: ContrastAlgo = ``"apca"`  
The color contrast algorithm to use when `autocolor_text=True`. By default this is `"apca"` (Accessible Perceptual Contrast Algorithm) and the alternative to this is `"wcag"` (Web Content Accessibility Guidelines). The chosen algorithm determines whether light or dark text provides better contrast against each cell's background color.

`truncate: bool = ``False`  
If `True`, then any values that fall outside of the domain will be truncated to the minimum or maximum value of the domain (will have the same color). If `False`, then any values that fall outside of the domain will be set to `NaN` and will follow the `na_color=` color.

`fn: Callable[[list[Any]], list[str | None]] | None = None`  
A color-mapping function. The function should take a list of data values (from a single column) as input and return a list of colors of the same length. Each color may be a hexadecimal color value (e.g., `"#FF0000"`) or a color name (e.g., `"red"`). All values are passed to the function, including missing values, so the function must handle those itself. Any position where the function returns `None` receives the `na_color=` color. If a function is supplied, then the `palette=`, `domain=`, `reverse=`, `truncate=`, and `midpoint=` arguments are ignored. The `alpha=`, `autocolor_text=`, and `contrast_algo=` arguments still apply to the returned colors. The <a href="../reference/col_numeric.html#great_tables.col_numeric" class="gdls-link"><code>col_numeric()</code></a>, <a href="../reference/col_bin.html#great_tables.col_bin" class="gdls-link"><code>col_bin()</code></a>, and <a href="../reference/col_factor.html#great_tables.col_factor" class="gdls-link"><code>col_factor()</code></a> helpers create ready-made color-mapping functions that can be supplied here.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## How Column Values Are Mapped To Colors

Without `fn=`, each targeted column is mapped to colors in one of two ways, depending on the values it contains (missing values are set aside first):

- numeric values (integers, floats, and `Decimal` values) are spread along the palette as a continuous gradient, from the lowest value in the domain to the highest
- string values (including categorical columns) are treated as categories, with each one taking its own position along the palette

Columns of any other type (e.g., dates) or with a mix of types will raise an error. To color these, supply a color-mapping function to `fn=` (see the *Custom color-mapping functions* section). Some further details on how values are handled:

- missing values (`None`, `NaN`, and `pd.NA`) always receive the `na_color=` color
- booleans are treated as numbers, so `True` takes the high end of the palette and `False` the low end
- an inferred numeric domain spans the finite values only; any infinite values are given the color at the matching end of the palette (with a supplied `domain=`, infinite values are treated like any other value outside of the domain, following the `truncate=` setting)
- an inferred categorical domain lists the categories in the order they first appear in the column, except for ordered categorical columns (an ordered Pandas `Categorical` or a Polars `Enum`), where the declared levels are used in their declared order (this includes any levels that don't appear in the data, so colors stay consistent no matter which `rows=` are colored)

Supplying `domain=` overrides any of the inferred domains described above.


## Centering Colors On A Midpoint

For numeric values that are naturally centered on some value (changes centered on `0`, ratios centered on `1`, scores centered on a target), the `midpoint=` argument pins that value to the center color of the palette. How the rest of the values map to colors depends on whether `domain=` is supplied. As an example, suppose a column spans from `-2` to `10` and we use `palette=["red", "white", "green"]` with `midpoint=0`:

- without `domain=`, the domain becomes symmetric around the midpoint (here, `[-10, 10]`), so `10` is fully green while `-2` is only a pale red: the strength of a color reflects the distance from the midpoint, the same on both sides
- with `domain=[-2, 10]`, each side of the midpoint is scaled separately, so `-2` is fully red and `10` is fully green (this is how three-color scales work in spreadsheet software, where both sides always use their full range of colors)

For finer control (such as pinning every palette color to a specific value, or to a percentage of the way through the range of values), use `fn=col_numeric(stops=...)` (see <a href="../reference/col_numeric.html#great_tables.col_numeric" class="gdls-link"><code>col_numeric()</code></a>).


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


## Custom Color-Mapping Functions

When the built-in mapping (a palette spread across a domain) isn't what you need, you can supply your own color-mapping function to `fn=`. This gives complete control over how values become colors. Here's how such a function is used:

- it's called once per targeted column, receiving a list of that column's values (only for the rows selected by `rows=`, in table order)
- it must return a list of colors of the same length, where each color is a hexadecimal value (`"#RRGGBB"`, `"#RRGGBBAA"`, or the short `"#RGB"` form) or a CSS/X11 color name
- missing values are included in the list, so the function must handle them: with pandas they usually arrive as `NaN` (or `None`/`pd.NA`, depending on the column type), and with Polars and PyArrow they arrive as `None`; `pd.isna()` catches all of these
- returning `None` at any position gives that cell the `na_color=` color, which is the easiest way to deal with missing values
- columns of any type can be colored (e.g., booleans or dates), since the numeric-or-string requirement of the built-in mapping doesn't apply

When `fn=` is used, the `palette=`, `domain=`, `reverse=`, `truncate=`, and `midpoint=` arguments are ignored because the function takes over their roles. The `na_color=`, `alpha=`, `autocolor_text=`, and `contrast_algo=` arguments still apply to the colors that the function returns.

Rather than writing a function from scratch, you can create one with these helpers (modeled on the color-mapping functions of the R **scales** package, which are commonly used with gt):

- <a href="../reference/col_numeric.html#great_tables.col_numeric" class="gdls-link"><code>col_numeric()</code></a>: a continuous gradient across a numeric domain, optionally with each palette color pinned to a specific value (or a percentage of the way through the range of values) with `stops=`
- <a href="../reference/col_bin.html#great_tables.col_bin" class="gdls-link"><code>col_bin()</code></a>: numeric values cut into bins, with one color per bin
- <a href="../reference/col_factor.html#great_tables.col_factor" class="gdls-link"><code>col_factor()</code></a>: one color per category, optionally with a fixed set of levels so colors stay consistent across tables

Each helper accepts a palette in the same forms as `palette=` here (including ColorBrewer and viridis palette names). The numeric helpers also have their own `domain=` and `truncate=` arguments. Missing values, and values outside of the domain, give `None` by default, so the `na_color=` value given to [data_color()](GT.data_color.md#great_tables.GT.data_color) is used for those cells. Because the helpers return ordinary functions, they can also be called inside your own function, for instance to compute a domain from the data before mapping it.


## Examples

The [data_color()](GT.data_color.md#great_tables.GT.data_color) method can be used without any supplied arguments to colorize a table. Let's do this with the [exibble](data.exibble.md#great_tables.data.exibble) dataset:


``` python
from great_tables import GT
from great_tables.data import exibble

GT(exibble).data_color()
```


<style>
#bnheddzaxm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bnheddzaxm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bnheddzaxm p { margin: 0; padding: 0; }
 #bnheddzaxm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bnheddzaxm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bnheddzaxm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bnheddzaxm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bnheddzaxm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bnheddzaxm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bnheddzaxm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bnheddzaxm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bnheddzaxm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bnheddzaxm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bnheddzaxm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bnheddzaxm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bnheddzaxm .gt_spanner_row { border-bottom-style: hidden; }
 #bnheddzaxm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bnheddzaxm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bnheddzaxm .gt_from_md> :first-child { margin-top: 0; }
 #bnheddzaxm .gt_from_md> :last-child { margin-bottom: 0; }
 #bnheddzaxm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bnheddzaxm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bnheddzaxm .gt_indent_1 { text-indent: 5px; }
 #bnheddzaxm .gt_indent_2 { text-indent: calc(5px * 2); }
 #bnheddzaxm .gt_indent_3 { text-indent: calc(5px * 3); }
 #bnheddzaxm .gt_indent_4 { text-indent: calc(5px * 4); }
 #bnheddzaxm .gt_indent_5 { text-indent: calc(5px * 5); }
 #bnheddzaxm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bnheddzaxm .gt_row_group_first td { border-top-width: 2px; }
 #bnheddzaxm .gt_row_group_first th { border-top-width: 2px; }
 #bnheddzaxm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bnheddzaxm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bnheddzaxm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bnheddzaxm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bnheddzaxm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bnheddzaxm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bnheddzaxm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bnheddzaxm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bnheddzaxm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bnheddzaxm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bnheddzaxm .gt_left { text-align: left; }
 #bnheddzaxm .gt_center { text-align: center; }
 #bnheddzaxm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bnheddzaxm .gt_font_normal { font-weight: normal; }
 #bnheddzaxm .gt_font_bold { font-weight: bold; }
 #bnheddzaxm .gt_font_italic { font-style: italic; }
 #bnheddzaxm .gt_super { font-size: 65%; }
 #bnheddzaxm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bnheddzaxm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bnheddzaxm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bnheddzaxm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bnheddzaxm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bnheddzaxm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
| None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | row_8 | grp_b |


What's happened is that [data_color()](GT.data_color.md#great_tables.GT.data_color) applies background colors to all cells of every column with the palette of eight colors. Numeric columns will use 'numeric' methodology for color scaling whereas string-based columns will use the 'factor' methodology. The text color undergoes an automatic modification that maximizes contrast (since `autocolor_text=True` by default).

We can target specific colors and apply color to just those columns. Let's do that and also supply `palette=` values of `"red"` and `"green"`.


``` python
GT(exibble).data_color(
    columns=["num", "currency"],
    palette=["red", "green"]
)
```


<style>
#muocgpghuk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#muocgpghuk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#muocgpghuk p { margin: 0; padding: 0; }
 #muocgpghuk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #muocgpghuk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #muocgpghuk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #muocgpghuk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #muocgpghuk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #muocgpghuk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muocgpghuk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #muocgpghuk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #muocgpghuk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #muocgpghuk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #muocgpghuk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #muocgpghuk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #muocgpghuk .gt_spanner_row { border-bottom-style: hidden; }
 #muocgpghuk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #muocgpghuk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #muocgpghuk .gt_from_md> :first-child { margin-top: 0; }
 #muocgpghuk .gt_from_md> :last-child { margin-bottom: 0; }
 #muocgpghuk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #muocgpghuk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #muocgpghuk .gt_indent_1 { text-indent: 5px; }
 #muocgpghuk .gt_indent_2 { text-indent: calc(5px * 2); }
 #muocgpghuk .gt_indent_3 { text-indent: calc(5px * 3); }
 #muocgpghuk .gt_indent_4 { text-indent: calc(5px * 4); }
 #muocgpghuk .gt_indent_5 { text-indent: calc(5px * 5); }
 #muocgpghuk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #muocgpghuk .gt_row_group_first td { border-top-width: 2px; }
 #muocgpghuk .gt_row_group_first th { border-top-width: 2px; }
 #muocgpghuk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #muocgpghuk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muocgpghuk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #muocgpghuk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #muocgpghuk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muocgpghuk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #muocgpghuk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #muocgpghuk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #muocgpghuk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muocgpghuk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #muocgpghuk .gt_left { text-align: left; }
 #muocgpghuk .gt_center { text-align: center; }
 #muocgpghuk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #muocgpghuk .gt_font_normal { font-weight: normal; }
 #muocgpghuk .gt_font_bold { font-weight: bold; }
 #muocgpghuk .gt_font_italic { font-style: italic; }
 #muocgpghuk .gt_super { font-size: 65%; }
 #muocgpghuk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muocgpghuk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #muocgpghuk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muocgpghuk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #muocgpghuk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #muocgpghuk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
| None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | row_8 | grp_b |


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


<style>
#fduwyibktn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fduwyibktn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fduwyibktn p { margin: 0; padding: 0; }
 #fduwyibktn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fduwyibktn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fduwyibktn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fduwyibktn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fduwyibktn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fduwyibktn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fduwyibktn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fduwyibktn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fduwyibktn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fduwyibktn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fduwyibktn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fduwyibktn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fduwyibktn .gt_spanner_row { border-bottom-style: hidden; }
 #fduwyibktn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fduwyibktn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fduwyibktn .gt_from_md> :first-child { margin-top: 0; }
 #fduwyibktn .gt_from_md> :last-child { margin-bottom: 0; }
 #fduwyibktn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fduwyibktn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fduwyibktn .gt_indent_1 { text-indent: 5px; }
 #fduwyibktn .gt_indent_2 { text-indent: calc(5px * 2); }
 #fduwyibktn .gt_indent_3 { text-indent: calc(5px * 3); }
 #fduwyibktn .gt_indent_4 { text-indent: calc(5px * 4); }
 #fduwyibktn .gt_indent_5 { text-indent: calc(5px * 5); }
 #fduwyibktn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fduwyibktn .gt_row_group_first td { border-top-width: 2px; }
 #fduwyibktn .gt_row_group_first th { border-top-width: 2px; }
 #fduwyibktn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fduwyibktn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fduwyibktn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fduwyibktn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fduwyibktn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fduwyibktn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fduwyibktn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fduwyibktn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fduwyibktn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fduwyibktn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fduwyibktn .gt_left { text-align: left; }
 #fduwyibktn .gt_center { text-align: center; }
 #fduwyibktn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fduwyibktn .gt_font_normal { font-weight: normal; }
 #fduwyibktn .gt_font_bold { font-weight: bold; }
 #fduwyibktn .gt_font_italic { font-style: italic; }
 #fduwyibktn .gt_super { font-size: 65%; }
 #fduwyibktn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fduwyibktn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fduwyibktn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fduwyibktn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fduwyibktn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fduwyibktn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
| None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | row_8 | grp_b |


For complete control over how values map to colors, we can supply a function to `fn=`. The function receives the list of values in a column (missing values included) and must return a list of colors of the same length. Here, values in the `num` column are colored according to whether they are below or above `100`. Returning `None` for the missing value means that it gets the `na_color=` color:


``` python
import pandas as pd

def above_below_100(vals):
    return [None if pd.isna(x) else "lightblue" if x < 100 else "orange" for x in vals]

GT(exibble).data_color(
    columns="num",
    fn=above_below_100,
    na_color="lightgray"
)
```


<style>
#sppuegufnt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sppuegufnt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sppuegufnt p { margin: 0; padding: 0; }
 #sppuegufnt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sppuegufnt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sppuegufnt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sppuegufnt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sppuegufnt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sppuegufnt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sppuegufnt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sppuegufnt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sppuegufnt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sppuegufnt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sppuegufnt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sppuegufnt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sppuegufnt .gt_spanner_row { border-bottom-style: hidden; }
 #sppuegufnt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sppuegufnt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sppuegufnt .gt_from_md> :first-child { margin-top: 0; }
 #sppuegufnt .gt_from_md> :last-child { margin-bottom: 0; }
 #sppuegufnt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sppuegufnt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sppuegufnt .gt_indent_1 { text-indent: 5px; }
 #sppuegufnt .gt_indent_2 { text-indent: calc(5px * 2); }
 #sppuegufnt .gt_indent_3 { text-indent: calc(5px * 3); }
 #sppuegufnt .gt_indent_4 { text-indent: calc(5px * 4); }
 #sppuegufnt .gt_indent_5 { text-indent: calc(5px * 5); }
 #sppuegufnt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sppuegufnt .gt_row_group_first td { border-top-width: 2px; }
 #sppuegufnt .gt_row_group_first th { border-top-width: 2px; }
 #sppuegufnt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sppuegufnt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sppuegufnt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sppuegufnt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sppuegufnt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sppuegufnt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sppuegufnt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sppuegufnt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sppuegufnt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sppuegufnt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sppuegufnt .gt_left { text-align: left; }
 #sppuegufnt .gt_center { text-align: center; }
 #sppuegufnt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sppuegufnt .gt_font_normal { font-weight: normal; }
 #sppuegufnt .gt_font_bold { font-weight: bold; }
 #sppuegufnt .gt_font_italic { font-style: italic; }
 #sppuegufnt .gt_super { font-size: 65%; }
 #sppuegufnt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sppuegufnt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sppuegufnt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sppuegufnt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sppuegufnt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sppuegufnt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
| None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | row_8 | grp_b |


A color-mapping function is also useful for highlighting the sign of values. Here, positive changes are colored green, negative changes orange, and zero values are left white. Because the function assigns its own color to the missing value, `na_color=` isn't needed:


``` python
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


<style>
#gwlxpapykb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gwlxpapykb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gwlxpapykb p { margin: 0; padding: 0; }
 #gwlxpapykb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gwlxpapykb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gwlxpapykb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gwlxpapykb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gwlxpapykb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gwlxpapykb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gwlxpapykb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gwlxpapykb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gwlxpapykb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gwlxpapykb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gwlxpapykb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gwlxpapykb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gwlxpapykb .gt_spanner_row { border-bottom-style: hidden; }
 #gwlxpapykb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gwlxpapykb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gwlxpapykb .gt_from_md> :first-child { margin-top: 0; }
 #gwlxpapykb .gt_from_md> :last-child { margin-bottom: 0; }
 #gwlxpapykb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gwlxpapykb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gwlxpapykb .gt_indent_1 { text-indent: 5px; }
 #gwlxpapykb .gt_indent_2 { text-indent: calc(5px * 2); }
 #gwlxpapykb .gt_indent_3 { text-indent: calc(5px * 3); }
 #gwlxpapykb .gt_indent_4 { text-indent: calc(5px * 4); }
 #gwlxpapykb .gt_indent_5 { text-indent: calc(5px * 5); }
 #gwlxpapykb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gwlxpapykb .gt_row_group_first td { border-top-width: 2px; }
 #gwlxpapykb .gt_row_group_first th { border-top-width: 2px; }
 #gwlxpapykb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gwlxpapykb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gwlxpapykb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gwlxpapykb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gwlxpapykb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gwlxpapykb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gwlxpapykb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gwlxpapykb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gwlxpapykb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gwlxpapykb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gwlxpapykb .gt_left { text-align: left; }
 #gwlxpapykb .gt_center { text-align: center; }
 #gwlxpapykb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gwlxpapykb .gt_font_normal { font-weight: normal; }
 #gwlxpapykb .gt_font_bold { font-weight: bold; }
 #gwlxpapykb .gt_font_italic { font-style: italic; }
 #gwlxpapykb .gt_super { font-size: 65%; }
 #gwlxpapykb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gwlxpapykb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gwlxpapykb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gwlxpapykb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gwlxpapykb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gwlxpapykb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | +12.5  |
| South   | −8.1   |
| East    | 0.0    |
| West    | +3.2   |
| Central | None   |


For a gradient that's centered on zero, rather than fixed colors, we can use `midpoint=0` with a diverging palette. Negative changes become increasingly red and positive changes increasingly green, the further they are from zero. Because no `domain=` is given, the domain is made symmetric around zero, so the largest decrease (`-8.1`) is a less intense red than the largest increase (`12.5`) is green:


``` python
(
    GT(df)
    .data_color(columns="change", palette=["#D7191C", "white", "#1A9641"], midpoint=0)
    .fmt_number(columns="change", decimals=1, force_sign=True)
)
```


<style>
#bjbshtjyoe table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bjbshtjyoe thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bjbshtjyoe p { margin: 0; padding: 0; }
 #bjbshtjyoe .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bjbshtjyoe .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bjbshtjyoe .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bjbshtjyoe .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bjbshtjyoe .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bjbshtjyoe .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bjbshtjyoe .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bjbshtjyoe .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bjbshtjyoe .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bjbshtjyoe .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bjbshtjyoe .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bjbshtjyoe .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bjbshtjyoe .gt_spanner_row { border-bottom-style: hidden; }
 #bjbshtjyoe .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bjbshtjyoe .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bjbshtjyoe .gt_from_md> :first-child { margin-top: 0; }
 #bjbshtjyoe .gt_from_md> :last-child { margin-bottom: 0; }
 #bjbshtjyoe .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bjbshtjyoe .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bjbshtjyoe .gt_indent_1 { text-indent: 5px; }
 #bjbshtjyoe .gt_indent_2 { text-indent: calc(5px * 2); }
 #bjbshtjyoe .gt_indent_3 { text-indent: calc(5px * 3); }
 #bjbshtjyoe .gt_indent_4 { text-indent: calc(5px * 4); }
 #bjbshtjyoe .gt_indent_5 { text-indent: calc(5px * 5); }
 #bjbshtjyoe .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bjbshtjyoe .gt_row_group_first td { border-top-width: 2px; }
 #bjbshtjyoe .gt_row_group_first th { border-top-width: 2px; }
 #bjbshtjyoe .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bjbshtjyoe .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bjbshtjyoe .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bjbshtjyoe .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bjbshtjyoe .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bjbshtjyoe .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bjbshtjyoe .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bjbshtjyoe .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bjbshtjyoe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bjbshtjyoe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bjbshtjyoe .gt_left { text-align: left; }
 #bjbshtjyoe .gt_center { text-align: center; }
 #bjbshtjyoe .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bjbshtjyoe .gt_font_normal { font-weight: normal; }
 #bjbshtjyoe .gt_font_bold { font-weight: bold; }
 #bjbshtjyoe .gt_font_italic { font-style: italic; }
 #bjbshtjyoe .gt_super { font-size: 65%; }
 #bjbshtjyoe .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bjbshtjyoe .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bjbshtjyoe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bjbshtjyoe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bjbshtjyoe .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bjbshtjyoe .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | +12.5  |
| South   | −8.1   |
| East    | 0.0    |
| West    | +3.2   |
| Central | None   |


The midpoint doesn't have to be zero, and it doesn't have to sit in the middle of the domain. Here, sales are shown as a fraction of a target, so the midpoint is `1`. Supplying a `domain=` means that each side of the midpoint is scaled separately: the colors go from red to white over the wide range from 50% of the target up to the target, and from white to green over the narrower range from the target up to 120% of it:


``` python
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


<style>
#epnacnchxk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#epnacnchxk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#epnacnchxk p { margin: 0; padding: 0; }
 #epnacnchxk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #epnacnchxk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #epnacnchxk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #epnacnchxk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #epnacnchxk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #epnacnchxk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #epnacnchxk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #epnacnchxk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #epnacnchxk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #epnacnchxk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #epnacnchxk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #epnacnchxk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #epnacnchxk .gt_spanner_row { border-bottom-style: hidden; }
 #epnacnchxk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #epnacnchxk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #epnacnchxk .gt_from_md> :first-child { margin-top: 0; }
 #epnacnchxk .gt_from_md> :last-child { margin-bottom: 0; }
 #epnacnchxk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #epnacnchxk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #epnacnchxk .gt_indent_1 { text-indent: 5px; }
 #epnacnchxk .gt_indent_2 { text-indent: calc(5px * 2); }
 #epnacnchxk .gt_indent_3 { text-indent: calc(5px * 3); }
 #epnacnchxk .gt_indent_4 { text-indent: calc(5px * 4); }
 #epnacnchxk .gt_indent_5 { text-indent: calc(5px * 5); }
 #epnacnchxk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #epnacnchxk .gt_row_group_first td { border-top-width: 2px; }
 #epnacnchxk .gt_row_group_first th { border-top-width: 2px; }
 #epnacnchxk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #epnacnchxk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #epnacnchxk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #epnacnchxk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #epnacnchxk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #epnacnchxk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #epnacnchxk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #epnacnchxk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #epnacnchxk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #epnacnchxk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #epnacnchxk .gt_left { text-align: left; }
 #epnacnchxk .gt_center { text-align: center; }
 #epnacnchxk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #epnacnchxk .gt_font_normal { font-weight: normal; }
 #epnacnchxk .gt_font_bold { font-weight: bold; }
 #epnacnchxk .gt_font_italic { font-style: italic; }
 #epnacnchxk .gt_super { font-size: 65%; }
 #epnacnchxk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #epnacnchxk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #epnacnchxk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #epnacnchxk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #epnacnchxk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #epnacnchxk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| rep | pct_of_target |
|-----|---------------|
| Ana | 62%           |
| Ben | 88%           |
| Cai | 100%          |
| Dee | 108%          |
| Eli | 117%          |


To pin more than the midpoint, we can build the function with <a href="../reference/col_numeric.html#great_tables.col_numeric" class="gdls-link"><code>col_numeric()</code></a> and its `stops=` argument, which gives a value for each palette color. A stop can be a data value or a percentage of the way through the range of values in the column. Here, the lowest value is red, zero is white, and the highest value is green, so both sides use their full range of colors:


``` python
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


<style>
#zfhqkaedgg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zfhqkaedgg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zfhqkaedgg p { margin: 0; padding: 0; }
 #zfhqkaedgg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zfhqkaedgg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zfhqkaedgg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zfhqkaedgg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zfhqkaedgg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zfhqkaedgg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zfhqkaedgg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zfhqkaedgg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zfhqkaedgg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zfhqkaedgg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zfhqkaedgg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zfhqkaedgg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zfhqkaedgg .gt_spanner_row { border-bottom-style: hidden; }
 #zfhqkaedgg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zfhqkaedgg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zfhqkaedgg .gt_from_md> :first-child { margin-top: 0; }
 #zfhqkaedgg .gt_from_md> :last-child { margin-bottom: 0; }
 #zfhqkaedgg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zfhqkaedgg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zfhqkaedgg .gt_indent_1 { text-indent: 5px; }
 #zfhqkaedgg .gt_indent_2 { text-indent: calc(5px * 2); }
 #zfhqkaedgg .gt_indent_3 { text-indent: calc(5px * 3); }
 #zfhqkaedgg .gt_indent_4 { text-indent: calc(5px * 4); }
 #zfhqkaedgg .gt_indent_5 { text-indent: calc(5px * 5); }
 #zfhqkaedgg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zfhqkaedgg .gt_row_group_first td { border-top-width: 2px; }
 #zfhqkaedgg .gt_row_group_first th { border-top-width: 2px; }
 #zfhqkaedgg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zfhqkaedgg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zfhqkaedgg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zfhqkaedgg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zfhqkaedgg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zfhqkaedgg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zfhqkaedgg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zfhqkaedgg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zfhqkaedgg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zfhqkaedgg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zfhqkaedgg .gt_left { text-align: left; }
 #zfhqkaedgg .gt_center { text-align: center; }
 #zfhqkaedgg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zfhqkaedgg .gt_font_normal { font-weight: normal; }
 #zfhqkaedgg .gt_font_bold { font-weight: bold; }
 #zfhqkaedgg .gt_font_italic { font-style: italic; }
 #zfhqkaedgg .gt_super { font-size: 65%; }
 #zfhqkaedgg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zfhqkaedgg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zfhqkaedgg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zfhqkaedgg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zfhqkaedgg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zfhqkaedgg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | +12.5  |
| South   | −8.1   |
| East    | 0.0    |
| West    | +3.2   |
| Central | None   |
