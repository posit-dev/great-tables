# col_numeric()


Create a color-mapping function for continuous numeric values.


Usage

``` python
col_numeric(
    palette=None,
    domain=None,
    midpoint=None,
    stops=None,
    na_color=None,
    reverse=False,
    truncate=False,
)
```


The [col_numeric()](col_numeric.md#great_tables.col_numeric) helper returns a function that linearly maps numeric values onto a color palette (interpolating between the palette's colors). The returned function is designed to be passed to the `fn=` argument of <a href="../reference/GT.data_color.html#great_tables.GT.data_color" class="gdls-link"><code>data_color()</code></a>, but it can be called on any list of values.


## Parameters


`palette: str | list[str] | None = None`  
The colors to interpolate between. This can be a list of colors (as hexadecimal values or color names) or the name of a ColorBrewer or viridis palette (see <a href="../reference/GT.data_color.html#great_tables.GT.data_color" class="gdls-link"><code>data_color()</code></a> for the available names). If `None`, then a default palette will be used.

`domain: list[int] | list[float] | None = None`  
The range of values to map onto the palette, given as `[min, max]`. Values outside of this range receive the missing-value color (unless `truncate=True`). If `None`, then the domain is taken from the range of the (non-missing) values supplied to the returned function each time it is called (or, with `midpoint=`, a range made symmetric around the midpoint). This can't be used together with `stops=`.

`midpoint: int | float | None = None`  
A value that receives the color at the center of the palette. If `domain=` is `None`, then the domain is made symmetric around the midpoint, reaching as far as the value furthest from it. If `domain=` is supplied, then each side of the midpoint is scaled separately to its end of the domain (and the midpoint must lie within the domain). This works in the same way as the `midpoint=` argument of <a href="../reference/GT.data_color.html#great_tables.GT.data_color" class="gdls-link"><code>data_color()</code></a> and can't be used together with `stops=`.

`stops: list[int | float | str] | None = None`  
A list giving the value at which each palette color is reached, with one entry per color in the palette (after any ColorBrewer or viridis palette name is expanded). Colors are interpolated between neighboring stops. Each stop can be either a number (a data value) or a percentage string from `"0%"` to `"100%"` (a position within the range of the values supplied to the returned function, extended to include any numeric stops). For example, `stops=["0%", 0, "100%"]` pins the lowest value, zero, and the highest value, whatever the range of the values. Stops must be in non-decreasing order once resolved. A repeated stop creates a sharp change between two colors, with a value exactly at that stop taking the later color. The outermost stops act as the domain, so values beyond them receive the missing-value color (unless `truncate=True`).

`na_color: str | None = None`  
The color to use for missing values and values outside of the domain. If `None`, then the returned function gives `None` for those values, which lets [data_color()](GT.data_color.md#great_tables.GT.data_color) apply its own `na_color=` color.

`reverse: bool = ``False`  
Should the order of the palette colors be reversed? This doesn't affect `stops=`, which apply to the colors in their reversed order.

`truncate: bool = ``False`  
If `True`, then values outside of the domain (or the outermost `stops=`) are treated as the nearest end of it, so they receive the first or last color of the palette. If `False` (the default), then they receive the missing-value color.


## Returns


`Callable[[list[Any]], list[str | None]]`  
A function that takes a list of numeric values and returns a list of hexadecimal colors.


## Examples

A diverging palette with a domain centered on zero colors negative values increasingly red and positive values increasingly green, the further they are from zero:


``` python
import pandas as pd
from great_tables import GT, col_numeric

df = pd.DataFrame(
    {
        "region": ["North", "South", "East", "West", "Central"],
        "change": [12.5, -8.1, 0.0, 3.2, -1.0],
    }
)

GT(df).data_color(
    columns="change",
    fn=col_numeric(palette=["#D7191C", "white", "#1A9641"], domain=[-15, 15]),
)
```


<style>
#txufqndigi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#txufqndigi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#txufqndigi p { margin: 0; padding: 0; }
 #txufqndigi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #txufqndigi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #txufqndigi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #txufqndigi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #txufqndigi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #txufqndigi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #txufqndigi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #txufqndigi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #txufqndigi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #txufqndigi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #txufqndigi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #txufqndigi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #txufqndigi .gt_spanner_row { border-bottom-style: hidden; }
 #txufqndigi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #txufqndigi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #txufqndigi .gt_from_md> :first-child { margin-top: 0; }
 #txufqndigi .gt_from_md> :last-child { margin-bottom: 0; }
 #txufqndigi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #txufqndigi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #txufqndigi .gt_indent_1 { text-indent: 5px; }
 #txufqndigi .gt_indent_2 { text-indent: calc(5px * 2); }
 #txufqndigi .gt_indent_3 { text-indent: calc(5px * 3); }
 #txufqndigi .gt_indent_4 { text-indent: calc(5px * 4); }
 #txufqndigi .gt_indent_5 { text-indent: calc(5px * 5); }
 #txufqndigi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #txufqndigi .gt_row_group_first td { border-top-width: 2px; }
 #txufqndigi .gt_row_group_first th { border-top-width: 2px; }
 #txufqndigi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #txufqndigi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #txufqndigi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #txufqndigi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #txufqndigi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #txufqndigi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #txufqndigi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #txufqndigi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #txufqndigi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #txufqndigi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #txufqndigi .gt_left { text-align: left; }
 #txufqndigi .gt_center { text-align: center; }
 #txufqndigi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #txufqndigi .gt_font_normal { font-weight: normal; }
 #txufqndigi .gt_font_bold { font-weight: bold; }
 #txufqndigi .gt_font_italic { font-style: italic; }
 #txufqndigi .gt_super { font-size: 65%; }
 #txufqndigi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #txufqndigi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #txufqndigi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #txufqndigi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #txufqndigi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #txufqndigi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | 12.5   |
| South   | -8.1   |
| East    | 0.0    |
| West    | 3.2    |
| Central | -1.0   |


Rather than fixing the domain, we can give a `midpoint=`. The domain is then made symmetric around the midpoint, reaching as far as the value furthest from it:


``` python
GT(df).data_color(
    columns="change",
    fn=col_numeric(palette=["#D7191C", "white", "#1A9641"], midpoint=0),
)
```


<style>
#oorpvqlcpg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oorpvqlcpg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oorpvqlcpg p { margin: 0; padding: 0; }
 #oorpvqlcpg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oorpvqlcpg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oorpvqlcpg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oorpvqlcpg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oorpvqlcpg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oorpvqlcpg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oorpvqlcpg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oorpvqlcpg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oorpvqlcpg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oorpvqlcpg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oorpvqlcpg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oorpvqlcpg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oorpvqlcpg .gt_spanner_row { border-bottom-style: hidden; }
 #oorpvqlcpg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oorpvqlcpg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #oorpvqlcpg .gt_from_md> :first-child { margin-top: 0; }
 #oorpvqlcpg .gt_from_md> :last-child { margin-bottom: 0; }
 #oorpvqlcpg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #oorpvqlcpg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #oorpvqlcpg .gt_indent_1 { text-indent: 5px; }
 #oorpvqlcpg .gt_indent_2 { text-indent: calc(5px * 2); }
 #oorpvqlcpg .gt_indent_3 { text-indent: calc(5px * 3); }
 #oorpvqlcpg .gt_indent_4 { text-indent: calc(5px * 4); }
 #oorpvqlcpg .gt_indent_5 { text-indent: calc(5px * 5); }
 #oorpvqlcpg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oorpvqlcpg .gt_row_group_first td { border-top-width: 2px; }
 #oorpvqlcpg .gt_row_group_first th { border-top-width: 2px; }
 #oorpvqlcpg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oorpvqlcpg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oorpvqlcpg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oorpvqlcpg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oorpvqlcpg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oorpvqlcpg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oorpvqlcpg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oorpvqlcpg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oorpvqlcpg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oorpvqlcpg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oorpvqlcpg .gt_left { text-align: left; }
 #oorpvqlcpg .gt_center { text-align: center; }
 #oorpvqlcpg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oorpvqlcpg .gt_font_normal { font-weight: normal; }
 #oorpvqlcpg .gt_font_bold { font-weight: bold; }
 #oorpvqlcpg .gt_font_italic { font-style: italic; }
 #oorpvqlcpg .gt_super { font-size: 65%; }
 #oorpvqlcpg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oorpvqlcpg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oorpvqlcpg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oorpvqlcpg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oorpvqlcpg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oorpvqlcpg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | 12.5   |
| South   | -8.1   |
| East    | 0.0    |
| West    | 3.2    |
| Central | -1.0   |


With `stops=`, every palette color can be pinned to a value. Stops can be data values or percentages of the way through the range of values. Here, the lowest value is fully red, zero is white, and the highest value is fully green, so each side uses its full range of colors:


``` python
GT(df).data_color(
    columns="change",
    fn=col_numeric(palette=["#D7191C", "white", "#1A9641"], stops=["0%", 0, "100%"]),
)
```


<style>
#pmftxcakdz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pmftxcakdz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pmftxcakdz p { margin: 0; padding: 0; }
 #pmftxcakdz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pmftxcakdz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pmftxcakdz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pmftxcakdz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pmftxcakdz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pmftxcakdz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pmftxcakdz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pmftxcakdz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pmftxcakdz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pmftxcakdz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pmftxcakdz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pmftxcakdz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pmftxcakdz .gt_spanner_row { border-bottom-style: hidden; }
 #pmftxcakdz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pmftxcakdz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pmftxcakdz .gt_from_md> :first-child { margin-top: 0; }
 #pmftxcakdz .gt_from_md> :last-child { margin-bottom: 0; }
 #pmftxcakdz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pmftxcakdz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pmftxcakdz .gt_indent_1 { text-indent: 5px; }
 #pmftxcakdz .gt_indent_2 { text-indent: calc(5px * 2); }
 #pmftxcakdz .gt_indent_3 { text-indent: calc(5px * 3); }
 #pmftxcakdz .gt_indent_4 { text-indent: calc(5px * 4); }
 #pmftxcakdz .gt_indent_5 { text-indent: calc(5px * 5); }
 #pmftxcakdz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pmftxcakdz .gt_row_group_first td { border-top-width: 2px; }
 #pmftxcakdz .gt_row_group_first th { border-top-width: 2px; }
 #pmftxcakdz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pmftxcakdz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pmftxcakdz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pmftxcakdz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pmftxcakdz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pmftxcakdz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pmftxcakdz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pmftxcakdz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pmftxcakdz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pmftxcakdz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pmftxcakdz .gt_left { text-align: left; }
 #pmftxcakdz .gt_center { text-align: center; }
 #pmftxcakdz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pmftxcakdz .gt_font_normal { font-weight: normal; }
 #pmftxcakdz .gt_font_bold { font-weight: bold; }
 #pmftxcakdz .gt_font_italic { font-style: italic; }
 #pmftxcakdz .gt_super { font-size: 65%; }
 #pmftxcakdz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pmftxcakdz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pmftxcakdz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pmftxcakdz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pmftxcakdz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pmftxcakdz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | 12.5   |
| South   | -8.1   |
| East    | 0.0    |
| West    | 3.2    |
| Central | -1.0   |


Repeating a stop makes a sharp change in color at that value. Here, values below zero are shades of orange and values from zero up are shades of purple:


``` python
GT(df).data_color(
    columns="change",
    fn=col_numeric(
        palette=["#E66101", "#FDB863", "#B2ABD2", "#5E3C99"],
        stops=["0%", 0, 0, "100%"],
    ),
)
```


<style>
#khbhelckdi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#khbhelckdi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#khbhelckdi p { margin: 0; padding: 0; }
 #khbhelckdi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #khbhelckdi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #khbhelckdi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #khbhelckdi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #khbhelckdi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #khbhelckdi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khbhelckdi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #khbhelckdi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #khbhelckdi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #khbhelckdi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #khbhelckdi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #khbhelckdi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #khbhelckdi .gt_spanner_row { border-bottom-style: hidden; }
 #khbhelckdi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #khbhelckdi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #khbhelckdi .gt_from_md> :first-child { margin-top: 0; }
 #khbhelckdi .gt_from_md> :last-child { margin-bottom: 0; }
 #khbhelckdi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #khbhelckdi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #khbhelckdi .gt_indent_1 { text-indent: 5px; }
 #khbhelckdi .gt_indent_2 { text-indent: calc(5px * 2); }
 #khbhelckdi .gt_indent_3 { text-indent: calc(5px * 3); }
 #khbhelckdi .gt_indent_4 { text-indent: calc(5px * 4); }
 #khbhelckdi .gt_indent_5 { text-indent: calc(5px * 5); }
 #khbhelckdi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #khbhelckdi .gt_row_group_first td { border-top-width: 2px; }
 #khbhelckdi .gt_row_group_first th { border-top-width: 2px; }
 #khbhelckdi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #khbhelckdi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khbhelckdi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #khbhelckdi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #khbhelckdi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khbhelckdi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #khbhelckdi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #khbhelckdi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #khbhelckdi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khbhelckdi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #khbhelckdi .gt_left { text-align: left; }
 #khbhelckdi .gt_center { text-align: center; }
 #khbhelckdi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #khbhelckdi .gt_font_normal { font-weight: normal; }
 #khbhelckdi .gt_font_bold { font-weight: bold; }
 #khbhelckdi .gt_font_italic { font-style: italic; }
 #khbhelckdi .gt_super { font-size: 65%; }
 #khbhelckdi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khbhelckdi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #khbhelckdi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khbhelckdi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #khbhelckdi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #khbhelckdi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | 12.5   |
| South   | -8.1   |
| East    | 0.0    |
| West    | 3.2    |
| Central | -1.0   |


With a narrower domain, `truncate=True` saturates the colors of values beyond its limits rather than leaving them uncolored. Here, anything above `5` is fully green and anything below `-5` is fully red:


``` python
GT(df).data_color(
    columns="change",
    fn=col_numeric(palette=["#D7191C", "white", "#1A9641"], domain=[-5, 5], truncate=True),
)
```


<style>
#ddltsjuqxp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ddltsjuqxp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ddltsjuqxp p { margin: 0; padding: 0; }
 #ddltsjuqxp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ddltsjuqxp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ddltsjuqxp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ddltsjuqxp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ddltsjuqxp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ddltsjuqxp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ddltsjuqxp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ddltsjuqxp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ddltsjuqxp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ddltsjuqxp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ddltsjuqxp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ddltsjuqxp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ddltsjuqxp .gt_spanner_row { border-bottom-style: hidden; }
 #ddltsjuqxp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ddltsjuqxp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ddltsjuqxp .gt_from_md> :first-child { margin-top: 0; }
 #ddltsjuqxp .gt_from_md> :last-child { margin-bottom: 0; }
 #ddltsjuqxp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ddltsjuqxp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ddltsjuqxp .gt_indent_1 { text-indent: 5px; }
 #ddltsjuqxp .gt_indent_2 { text-indent: calc(5px * 2); }
 #ddltsjuqxp .gt_indent_3 { text-indent: calc(5px * 3); }
 #ddltsjuqxp .gt_indent_4 { text-indent: calc(5px * 4); }
 #ddltsjuqxp .gt_indent_5 { text-indent: calc(5px * 5); }
 #ddltsjuqxp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ddltsjuqxp .gt_row_group_first td { border-top-width: 2px; }
 #ddltsjuqxp .gt_row_group_first th { border-top-width: 2px; }
 #ddltsjuqxp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ddltsjuqxp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ddltsjuqxp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ddltsjuqxp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ddltsjuqxp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ddltsjuqxp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ddltsjuqxp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ddltsjuqxp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ddltsjuqxp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ddltsjuqxp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ddltsjuqxp .gt_left { text-align: left; }
 #ddltsjuqxp .gt_center { text-align: center; }
 #ddltsjuqxp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ddltsjuqxp .gt_font_normal { font-weight: normal; }
 #ddltsjuqxp .gt_font_bold { font-weight: bold; }
 #ddltsjuqxp .gt_font_italic { font-style: italic; }
 #ddltsjuqxp .gt_super { font-size: 65%; }
 #ddltsjuqxp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ddltsjuqxp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ddltsjuqxp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ddltsjuqxp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ddltsjuqxp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ddltsjuqxp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | 12.5   |
| South   | -8.1   |
| East    | 0.0    |
| West    | 3.2    |
| Central | -1.0   |
