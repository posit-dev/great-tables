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
#iiztmboqqh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iiztmboqqh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iiztmboqqh p { margin: 0; padding: 0; }
 #iiztmboqqh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #iiztmboqqh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iiztmboqqh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iiztmboqqh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iiztmboqqh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iiztmboqqh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iiztmboqqh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iiztmboqqh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iiztmboqqh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iiztmboqqh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iiztmboqqh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iiztmboqqh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iiztmboqqh .gt_spanner_row { border-bottom-style: hidden; }
 #iiztmboqqh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iiztmboqqh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #iiztmboqqh .gt_from_md> :first-child { margin-top: 0; }
 #iiztmboqqh .gt_from_md> :last-child { margin-bottom: 0; }
 #iiztmboqqh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #iiztmboqqh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #iiztmboqqh .gt_indent_1 { text-indent: 5px; }
 #iiztmboqqh .gt_indent_2 { text-indent: calc(5px * 2); }
 #iiztmboqqh .gt_indent_3 { text-indent: calc(5px * 3); }
 #iiztmboqqh .gt_indent_4 { text-indent: calc(5px * 4); }
 #iiztmboqqh .gt_indent_5 { text-indent: calc(5px * 5); }
 #iiztmboqqh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iiztmboqqh .gt_row_group_first td { border-top-width: 2px; }
 #iiztmboqqh .gt_row_group_first th { border-top-width: 2px; }
 #iiztmboqqh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #iiztmboqqh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iiztmboqqh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iiztmboqqh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #iiztmboqqh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iiztmboqqh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iiztmboqqh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iiztmboqqh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iiztmboqqh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iiztmboqqh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iiztmboqqh .gt_left { text-align: left; }
 #iiztmboqqh .gt_center { text-align: center; }
 #iiztmboqqh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iiztmboqqh .gt_font_normal { font-weight: normal; }
 #iiztmboqqh .gt_font_bold { font-weight: bold; }
 #iiztmboqqh .gt_font_italic { font-style: italic; }
 #iiztmboqqh .gt_super { font-size: 65%; }
 #iiztmboqqh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iiztmboqqh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #iiztmboqqh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iiztmboqqh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iiztmboqqh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iiztmboqqh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vqtguejhdi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vqtguejhdi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vqtguejhdi p { margin: 0; padding: 0; }
 #vqtguejhdi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vqtguejhdi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vqtguejhdi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vqtguejhdi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vqtguejhdi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vqtguejhdi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vqtguejhdi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vqtguejhdi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vqtguejhdi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vqtguejhdi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vqtguejhdi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vqtguejhdi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vqtguejhdi .gt_spanner_row { border-bottom-style: hidden; }
 #vqtguejhdi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vqtguejhdi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vqtguejhdi .gt_from_md> :first-child { margin-top: 0; }
 #vqtguejhdi .gt_from_md> :last-child { margin-bottom: 0; }
 #vqtguejhdi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vqtguejhdi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vqtguejhdi .gt_indent_1 { text-indent: 5px; }
 #vqtguejhdi .gt_indent_2 { text-indent: calc(5px * 2); }
 #vqtguejhdi .gt_indent_3 { text-indent: calc(5px * 3); }
 #vqtguejhdi .gt_indent_4 { text-indent: calc(5px * 4); }
 #vqtguejhdi .gt_indent_5 { text-indent: calc(5px * 5); }
 #vqtguejhdi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vqtguejhdi .gt_row_group_first td { border-top-width: 2px; }
 #vqtguejhdi .gt_row_group_first th { border-top-width: 2px; }
 #vqtguejhdi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vqtguejhdi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vqtguejhdi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vqtguejhdi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vqtguejhdi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vqtguejhdi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vqtguejhdi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vqtguejhdi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vqtguejhdi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vqtguejhdi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vqtguejhdi .gt_left { text-align: left; }
 #vqtguejhdi .gt_center { text-align: center; }
 #vqtguejhdi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vqtguejhdi .gt_font_normal { font-weight: normal; }
 #vqtguejhdi .gt_font_bold { font-weight: bold; }
 #vqtguejhdi .gt_font_italic { font-style: italic; }
 #vqtguejhdi .gt_super { font-size: 65%; }
 #vqtguejhdi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vqtguejhdi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vqtguejhdi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vqtguejhdi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vqtguejhdi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vqtguejhdi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jbcrxhtwjf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jbcrxhtwjf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jbcrxhtwjf p { margin: 0; padding: 0; }
 #jbcrxhtwjf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jbcrxhtwjf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jbcrxhtwjf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jbcrxhtwjf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jbcrxhtwjf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jbcrxhtwjf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jbcrxhtwjf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jbcrxhtwjf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jbcrxhtwjf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jbcrxhtwjf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jbcrxhtwjf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jbcrxhtwjf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jbcrxhtwjf .gt_spanner_row { border-bottom-style: hidden; }
 #jbcrxhtwjf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jbcrxhtwjf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jbcrxhtwjf .gt_from_md> :first-child { margin-top: 0; }
 #jbcrxhtwjf .gt_from_md> :last-child { margin-bottom: 0; }
 #jbcrxhtwjf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jbcrxhtwjf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jbcrxhtwjf .gt_indent_1 { text-indent: 5px; }
 #jbcrxhtwjf .gt_indent_2 { text-indent: calc(5px * 2); }
 #jbcrxhtwjf .gt_indent_3 { text-indent: calc(5px * 3); }
 #jbcrxhtwjf .gt_indent_4 { text-indent: calc(5px * 4); }
 #jbcrxhtwjf .gt_indent_5 { text-indent: calc(5px * 5); }
 #jbcrxhtwjf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jbcrxhtwjf .gt_row_group_first td { border-top-width: 2px; }
 #jbcrxhtwjf .gt_row_group_first th { border-top-width: 2px; }
 #jbcrxhtwjf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jbcrxhtwjf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jbcrxhtwjf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jbcrxhtwjf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jbcrxhtwjf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jbcrxhtwjf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jbcrxhtwjf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jbcrxhtwjf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jbcrxhtwjf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jbcrxhtwjf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jbcrxhtwjf .gt_left { text-align: left; }
 #jbcrxhtwjf .gt_center { text-align: center; }
 #jbcrxhtwjf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jbcrxhtwjf .gt_font_normal { font-weight: normal; }
 #jbcrxhtwjf .gt_font_bold { font-weight: bold; }
 #jbcrxhtwjf .gt_font_italic { font-style: italic; }
 #jbcrxhtwjf .gt_super { font-size: 65%; }
 #jbcrxhtwjf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jbcrxhtwjf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jbcrxhtwjf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jbcrxhtwjf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jbcrxhtwjf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jbcrxhtwjf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#sgtfdbsryd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sgtfdbsryd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sgtfdbsryd p { margin: 0; padding: 0; }
 #sgtfdbsryd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sgtfdbsryd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sgtfdbsryd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sgtfdbsryd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sgtfdbsryd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sgtfdbsryd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sgtfdbsryd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sgtfdbsryd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sgtfdbsryd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sgtfdbsryd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sgtfdbsryd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sgtfdbsryd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sgtfdbsryd .gt_spanner_row { border-bottom-style: hidden; }
 #sgtfdbsryd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sgtfdbsryd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sgtfdbsryd .gt_from_md> :first-child { margin-top: 0; }
 #sgtfdbsryd .gt_from_md> :last-child { margin-bottom: 0; }
 #sgtfdbsryd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sgtfdbsryd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sgtfdbsryd .gt_indent_1 { text-indent: 5px; }
 #sgtfdbsryd .gt_indent_2 { text-indent: calc(5px * 2); }
 #sgtfdbsryd .gt_indent_3 { text-indent: calc(5px * 3); }
 #sgtfdbsryd .gt_indent_4 { text-indent: calc(5px * 4); }
 #sgtfdbsryd .gt_indent_5 { text-indent: calc(5px * 5); }
 #sgtfdbsryd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sgtfdbsryd .gt_row_group_first td { border-top-width: 2px; }
 #sgtfdbsryd .gt_row_group_first th { border-top-width: 2px; }
 #sgtfdbsryd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sgtfdbsryd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sgtfdbsryd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sgtfdbsryd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sgtfdbsryd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sgtfdbsryd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sgtfdbsryd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sgtfdbsryd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sgtfdbsryd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sgtfdbsryd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sgtfdbsryd .gt_left { text-align: left; }
 #sgtfdbsryd .gt_center { text-align: center; }
 #sgtfdbsryd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sgtfdbsryd .gt_font_normal { font-weight: normal; }
 #sgtfdbsryd .gt_font_bold { font-weight: bold; }
 #sgtfdbsryd .gt_font_italic { font-style: italic; }
 #sgtfdbsryd .gt_super { font-size: 65%; }
 #sgtfdbsryd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sgtfdbsryd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sgtfdbsryd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sgtfdbsryd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sgtfdbsryd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sgtfdbsryd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jjjneviano table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jjjneviano thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jjjneviano p { margin: 0; padding: 0; }
 #jjjneviano .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jjjneviano .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jjjneviano .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jjjneviano .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jjjneviano .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jjjneviano .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jjjneviano .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jjjneviano .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jjjneviano .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jjjneviano .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jjjneviano .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jjjneviano .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jjjneviano .gt_spanner_row { border-bottom-style: hidden; }
 #jjjneviano .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jjjneviano .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jjjneviano .gt_from_md> :first-child { margin-top: 0; }
 #jjjneviano .gt_from_md> :last-child { margin-bottom: 0; }
 #jjjneviano .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jjjneviano .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jjjneviano .gt_indent_1 { text-indent: 5px; }
 #jjjneviano .gt_indent_2 { text-indent: calc(5px * 2); }
 #jjjneviano .gt_indent_3 { text-indent: calc(5px * 3); }
 #jjjneviano .gt_indent_4 { text-indent: calc(5px * 4); }
 #jjjneviano .gt_indent_5 { text-indent: calc(5px * 5); }
 #jjjneviano .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jjjneviano .gt_row_group_first td { border-top-width: 2px; }
 #jjjneviano .gt_row_group_first th { border-top-width: 2px; }
 #jjjneviano .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jjjneviano .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jjjneviano .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jjjneviano .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jjjneviano .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jjjneviano .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jjjneviano .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jjjneviano .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jjjneviano .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jjjneviano .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jjjneviano .gt_left { text-align: left; }
 #jjjneviano .gt_center { text-align: center; }
 #jjjneviano .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jjjneviano .gt_font_normal { font-weight: normal; }
 #jjjneviano .gt_font_bold { font-weight: bold; }
 #jjjneviano .gt_font_italic { font-style: italic; }
 #jjjneviano .gt_super { font-size: 65%; }
 #jjjneviano .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jjjneviano .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jjjneviano .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jjjneviano .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jjjneviano .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jjjneviano .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| region  | change |
|---------|--------|
| North   | 12.5   |
| South   | -8.1   |
| East    | 0.0    |
| West    | 3.2    |
| Central | -1.0   |
