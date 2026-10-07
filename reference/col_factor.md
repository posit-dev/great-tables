# col_factor()


Create a color-mapping function for categorical values.


Usage

``` python
col_factor(
    palette=None,
    domain=None,
    na_color=None,
    reverse=False,
)
```


The [col_factor()](col_factor.md#great_tables.col_factor) helper returns a function that gives each distinct value (or level) its own color. If the palette has at least as many colors as there are levels, then the levels take the palette colors in order; otherwise, colors are interpolated along the palette. The returned function is designed to be passed to the `fn=` argument of <a href="../reference/GT.data_color.html#great_tables.GT.data_color" class="gdls-link"><code>data_color()</code></a>, but it can be called on any list of values.


## Parameters


`palette: str | list[str] | None = None`  
The colors to use. This can be a list of colors (as hexadecimal values or color names) or the name of a ColorBrewer or viridis palette (see <a href="../reference/GT.data_color.html#great_tables.GT.data_color" class="gdls-link"><code>data_color()</code></a> for the available names). If `None`, then a default palette will be used.

`domain: list[Any] | None = None`  
The levels to map to colors, in order. Values that aren't in the domain receive the missing-value color. If `None`, then the levels are the distinct (non-missing) values supplied to the returned function each time it is called, in their order of appearance.

`na_color: str | None = None`  
The color to use for missing values and values not in the domain. If `None`, then the returned function gives `None` for those values, which lets [data_color()](GT.data_color.md#great_tables.GT.data_color) apply its own `na_color=` color.

`reverse: bool = ``False`  
Should the order of the palette colors be reversed?


## Returns


`Callable[[list[Any]], list[str | None]]`  
A function that takes a list of values and returns a list of hexadecimal colors.


## Examples

Setting the `domain=` fixes the color of each level, no matter which levels are present in the column or in what order they appear:


``` python
import pandas as pd
from great_tables import GT, col_factor

df = pd.DataFrame(
    {
        "ticket": [101, 102, 103, 104, 105],
        "priority": ["low", "high", "medium", "high", "urgent"],
    }
)

GT(df).data_color(
    columns="priority",
    fn=col_factor(
        palette=["#FEF0D9", "#FDCC8A", "#FC8D59"],
        domain=["low", "medium", "high"],
        na_color="#D7301F",
    ),
)
```


<style>
#oifbzvnwsu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oifbzvnwsu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oifbzvnwsu p { margin: 0; padding: 0; }
 #oifbzvnwsu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oifbzvnwsu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oifbzvnwsu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oifbzvnwsu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oifbzvnwsu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oifbzvnwsu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oifbzvnwsu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oifbzvnwsu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oifbzvnwsu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oifbzvnwsu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oifbzvnwsu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oifbzvnwsu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oifbzvnwsu .gt_spanner_row { border-bottom-style: hidden; }
 #oifbzvnwsu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oifbzvnwsu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #oifbzvnwsu .gt_from_md> :first-child { margin-top: 0; }
 #oifbzvnwsu .gt_from_md> :last-child { margin-bottom: 0; }
 #oifbzvnwsu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #oifbzvnwsu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #oifbzvnwsu .gt_indent_1 { text-indent: 5px; }
 #oifbzvnwsu .gt_indent_2 { text-indent: calc(5px * 2); }
 #oifbzvnwsu .gt_indent_3 { text-indent: calc(5px * 3); }
 #oifbzvnwsu .gt_indent_4 { text-indent: calc(5px * 4); }
 #oifbzvnwsu .gt_indent_5 { text-indent: calc(5px * 5); }
 #oifbzvnwsu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oifbzvnwsu .gt_row_group_first td { border-top-width: 2px; }
 #oifbzvnwsu .gt_row_group_first th { border-top-width: 2px; }
 #oifbzvnwsu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oifbzvnwsu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oifbzvnwsu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oifbzvnwsu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oifbzvnwsu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oifbzvnwsu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oifbzvnwsu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oifbzvnwsu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oifbzvnwsu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oifbzvnwsu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oifbzvnwsu .gt_left { text-align: left; }
 #oifbzvnwsu .gt_center { text-align: center; }
 #oifbzvnwsu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oifbzvnwsu .gt_font_normal { font-weight: normal; }
 #oifbzvnwsu .gt_font_bold { font-weight: bold; }
 #oifbzvnwsu .gt_font_italic { font-style: italic; }
 #oifbzvnwsu .gt_super { font-size: 65%; }
 #oifbzvnwsu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oifbzvnwsu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oifbzvnwsu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oifbzvnwsu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oifbzvnwsu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oifbzvnwsu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| ticket | priority |
|--------|----------|
| 101    | low      |
| 102    | high     |
| 103    | medium   |
| 104    | high     |
| 105    | urgent   |
