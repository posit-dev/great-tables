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
#kctklqawdd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kctklqawdd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kctklqawdd p { margin: 0; padding: 0; }
 #kctklqawdd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kctklqawdd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kctklqawdd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kctklqawdd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kctklqawdd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kctklqawdd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kctklqawdd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kctklqawdd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kctklqawdd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kctklqawdd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kctklqawdd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kctklqawdd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kctklqawdd .gt_spanner_row { border-bottom-style: hidden; }
 #kctklqawdd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kctklqawdd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kctklqawdd .gt_from_md> :first-child { margin-top: 0; }
 #kctklqawdd .gt_from_md> :last-child { margin-bottom: 0; }
 #kctklqawdd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kctklqawdd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kctklqawdd .gt_indent_1 { text-indent: 5px; }
 #kctklqawdd .gt_indent_2 { text-indent: calc(5px * 2); }
 #kctklqawdd .gt_indent_3 { text-indent: calc(5px * 3); }
 #kctklqawdd .gt_indent_4 { text-indent: calc(5px * 4); }
 #kctklqawdd .gt_indent_5 { text-indent: calc(5px * 5); }
 #kctklqawdd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kctklqawdd .gt_row_group_first td { border-top-width: 2px; }
 #kctklqawdd .gt_row_group_first th { border-top-width: 2px; }
 #kctklqawdd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kctklqawdd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kctklqawdd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kctklqawdd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kctklqawdd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kctklqawdd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kctklqawdd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kctklqawdd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kctklqawdd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kctklqawdd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kctklqawdd .gt_left { text-align: left; }
 #kctklqawdd .gt_center { text-align: center; }
 #kctklqawdd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kctklqawdd .gt_font_normal { font-weight: normal; }
 #kctklqawdd .gt_font_bold { font-weight: bold; }
 #kctklqawdd .gt_font_italic { font-style: italic; }
 #kctklqawdd .gt_super { font-size: 65%; }
 #kctklqawdd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kctklqawdd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kctklqawdd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kctklqawdd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kctklqawdd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kctklqawdd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jyvtxxtbke table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jyvtxxtbke thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jyvtxxtbke p { margin: 0; padding: 0; }
 #jyvtxxtbke .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jyvtxxtbke .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jyvtxxtbke .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jyvtxxtbke .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jyvtxxtbke .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jyvtxxtbke .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jyvtxxtbke .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jyvtxxtbke .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jyvtxxtbke .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jyvtxxtbke .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jyvtxxtbke .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jyvtxxtbke .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jyvtxxtbke .gt_spanner_row { border-bottom-style: hidden; }
 #jyvtxxtbke .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jyvtxxtbke .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jyvtxxtbke .gt_from_md> :first-child { margin-top: 0; }
 #jyvtxxtbke .gt_from_md> :last-child { margin-bottom: 0; }
 #jyvtxxtbke .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jyvtxxtbke .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jyvtxxtbke .gt_indent_1 { text-indent: 5px; }
 #jyvtxxtbke .gt_indent_2 { text-indent: calc(5px * 2); }
 #jyvtxxtbke .gt_indent_3 { text-indent: calc(5px * 3); }
 #jyvtxxtbke .gt_indent_4 { text-indent: calc(5px * 4); }
 #jyvtxxtbke .gt_indent_5 { text-indent: calc(5px * 5); }
 #jyvtxxtbke .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jyvtxxtbke .gt_row_group_first td { border-top-width: 2px; }
 #jyvtxxtbke .gt_row_group_first th { border-top-width: 2px; }
 #jyvtxxtbke .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jyvtxxtbke .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jyvtxxtbke .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jyvtxxtbke .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jyvtxxtbke .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jyvtxxtbke .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jyvtxxtbke .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jyvtxxtbke .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jyvtxxtbke .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jyvtxxtbke .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jyvtxxtbke .gt_left { text-align: left; }
 #jyvtxxtbke .gt_center { text-align: center; }
 #jyvtxxtbke .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jyvtxxtbke .gt_font_normal { font-weight: normal; }
 #jyvtxxtbke .gt_font_bold { font-weight: bold; }
 #jyvtxxtbke .gt_font_italic { font-style: italic; }
 #jyvtxxtbke .gt_super { font-size: 65%; }
 #jyvtxxtbke .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jyvtxxtbke .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jyvtxxtbke .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jyvtxxtbke .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jyvtxxtbke .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jyvtxxtbke .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fhkurilkgl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fhkurilkgl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fhkurilkgl p { margin: 0; padding: 0; }
 #fhkurilkgl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fhkurilkgl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fhkurilkgl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fhkurilkgl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fhkurilkgl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fhkurilkgl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fhkurilkgl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fhkurilkgl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fhkurilkgl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fhkurilkgl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fhkurilkgl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fhkurilkgl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fhkurilkgl .gt_spanner_row { border-bottom-style: hidden; }
 #fhkurilkgl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fhkurilkgl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fhkurilkgl .gt_from_md> :first-child { margin-top: 0; }
 #fhkurilkgl .gt_from_md> :last-child { margin-bottom: 0; }
 #fhkurilkgl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fhkurilkgl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fhkurilkgl .gt_indent_1 { text-indent: 5px; }
 #fhkurilkgl .gt_indent_2 { text-indent: calc(5px * 2); }
 #fhkurilkgl .gt_indent_3 { text-indent: calc(5px * 3); }
 #fhkurilkgl .gt_indent_4 { text-indent: calc(5px * 4); }
 #fhkurilkgl .gt_indent_5 { text-indent: calc(5px * 5); }
 #fhkurilkgl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fhkurilkgl .gt_row_group_first td { border-top-width: 2px; }
 #fhkurilkgl .gt_row_group_first th { border-top-width: 2px; }
 #fhkurilkgl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fhkurilkgl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fhkurilkgl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fhkurilkgl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fhkurilkgl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fhkurilkgl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fhkurilkgl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fhkurilkgl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fhkurilkgl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fhkurilkgl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fhkurilkgl .gt_left { text-align: left; }
 #fhkurilkgl .gt_center { text-align: center; }
 #fhkurilkgl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fhkurilkgl .gt_font_normal { font-weight: normal; }
 #fhkurilkgl .gt_font_bold { font-weight: bold; }
 #fhkurilkgl .gt_font_italic { font-style: italic; }
 #fhkurilkgl .gt_super { font-size: 65%; }
 #fhkurilkgl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fhkurilkgl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fhkurilkgl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fhkurilkgl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fhkurilkgl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fhkurilkgl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#djxpwduzik table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#djxpwduzik thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#djxpwduzik p { margin: 0; padding: 0; }
 #djxpwduzik .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #djxpwduzik .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #djxpwduzik .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #djxpwduzik .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #djxpwduzik .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #djxpwduzik .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #djxpwduzik .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #djxpwduzik .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #djxpwduzik .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #djxpwduzik .gt_column_spanner_outer:first-child { padding-left: 0; }
 #djxpwduzik .gt_column_spanner_outer:last-child { padding-right: 0; }
 #djxpwduzik .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #djxpwduzik .gt_spanner_row { border-bottom-style: hidden; }
 #djxpwduzik .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #djxpwduzik .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #djxpwduzik .gt_from_md> :first-child { margin-top: 0; }
 #djxpwduzik .gt_from_md> :last-child { margin-bottom: 0; }
 #djxpwduzik .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #djxpwduzik .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #djxpwduzik .gt_indent_1 { text-indent: 5px; }
 #djxpwduzik .gt_indent_2 { text-indent: calc(5px * 2); }
 #djxpwduzik .gt_indent_3 { text-indent: calc(5px * 3); }
 #djxpwduzik .gt_indent_4 { text-indent: calc(5px * 4); }
 #djxpwduzik .gt_indent_5 { text-indent: calc(5px * 5); }
 #djxpwduzik .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #djxpwduzik .gt_row_group_first td { border-top-width: 2px; }
 #djxpwduzik .gt_row_group_first th { border-top-width: 2px; }
 #djxpwduzik .gt_striped { color: #333333; background-color: #F4F4F4; }
 #djxpwduzik .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #djxpwduzik .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #djxpwduzik .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #djxpwduzik .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #djxpwduzik .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #djxpwduzik .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #djxpwduzik .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #djxpwduzik .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #djxpwduzik .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #djxpwduzik .gt_left { text-align: left; }
 #djxpwduzik .gt_center { text-align: center; }
 #djxpwduzik .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #djxpwduzik .gt_font_normal { font-weight: normal; }
 #djxpwduzik .gt_font_bold { font-weight: bold; }
 #djxpwduzik .gt_font_italic { font-style: italic; }
 #djxpwduzik .gt_super { font-size: 65%; }
 #djxpwduzik .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #djxpwduzik .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #djxpwduzik .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #djxpwduzik .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #djxpwduzik .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #djxpwduzik .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qepamfaqch table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qepamfaqch thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qepamfaqch p { margin: 0; padding: 0; }
 #qepamfaqch .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qepamfaqch .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qepamfaqch .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qepamfaqch .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qepamfaqch .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qepamfaqch .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qepamfaqch .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qepamfaqch .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qepamfaqch .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qepamfaqch .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qepamfaqch .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qepamfaqch .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qepamfaqch .gt_spanner_row { border-bottom-style: hidden; }
 #qepamfaqch .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qepamfaqch .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qepamfaqch .gt_from_md> :first-child { margin-top: 0; }
 #qepamfaqch .gt_from_md> :last-child { margin-bottom: 0; }
 #qepamfaqch .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qepamfaqch .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qepamfaqch .gt_indent_1 { text-indent: 5px; }
 #qepamfaqch .gt_indent_2 { text-indent: calc(5px * 2); }
 #qepamfaqch .gt_indent_3 { text-indent: calc(5px * 3); }
 #qepamfaqch .gt_indent_4 { text-indent: calc(5px * 4); }
 #qepamfaqch .gt_indent_5 { text-indent: calc(5px * 5); }
 #qepamfaqch .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qepamfaqch .gt_row_group_first td { border-top-width: 2px; }
 #qepamfaqch .gt_row_group_first th { border-top-width: 2px; }
 #qepamfaqch .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qepamfaqch .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qepamfaqch .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qepamfaqch .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qepamfaqch .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qepamfaqch .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qepamfaqch .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qepamfaqch .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qepamfaqch .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qepamfaqch .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qepamfaqch .gt_left { text-align: left; }
 #qepamfaqch .gt_center { text-align: center; }
 #qepamfaqch .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qepamfaqch .gt_font_normal { font-weight: normal; }
 #qepamfaqch .gt_font_bold { font-weight: bold; }
 #qepamfaqch .gt_font_italic { font-style: italic; }
 #qepamfaqch .gt_super { font-size: 65%; }
 #qepamfaqch .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qepamfaqch .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qepamfaqch .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qepamfaqch .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qepamfaqch .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qepamfaqch .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | 12.5   |
| South   | -8.1   |
| East    | 0.0    |
| West    | 3.2    |
| Central | -1.0   |
