# col_bin()


Create a color-mapping function for numeric values cut into bins.


Usage

``` python
col_bin(
    palette=None,
    domain=None,
    bins=7,
    na_color=None,
    right=False,
    reverse=False,
    truncate=False,
)
```


The [col_bin()](col_bin.md#great_tables.col_bin) helper returns a function that divides numeric values into bins and gives every value in a bin the same color. The bin colors are spaced evenly along the palette. The returned function is designed to be passed to the `fn=` argument of <a href="../reference/GT.data_color.html#great_tables.GT.data_color" class="gdls-link"><code>data_color()</code></a>, but it can be called on any list of values.


## Parameters


`palette: str | list[str] | None = None`  
The colors to use. This can be a list of colors (as hexadecimal values or color names) or the name of a ColorBrewer or viridis palette (see <a href="../reference/GT.data_color.html#great_tables.GT.data_color" class="gdls-link"><code>data_color()</code></a> for the available names). If `None`, then a default palette will be used.

`domain: list[int] | list[float] | None = None`  
The range of values to divide into bins, given as `[min, max]`. This is only used when `bins=` is an integer. If `None`, then the domain is taken from the range of the (non-missing) values supplied to the returned function each time it is called.

`bins: int | list[int] | list[float] = ``7`  
Either the number of equal-width bins to cut the domain into, or a list of two or more bin boundaries (e.g., `[0, 10, 50, 100]`). Values outside of the outermost boundaries receive the missing-value color (unless `truncate=True`).

`na_color: str | None = None`  
The color to use for missing values and values outside of the bins. If `None`, then the returned function gives `None` for those values, which lets [data_color()](GT.data_color.md#great_tables.GT.data_color) apply its own `na_color=` color.

`right: bool = ``False`  
Should the bins be closed on the right (and open on the left)? By default, bins include their lower boundary but not their upper one (the last bin includes both). With `right=True`, bins include their upper boundary but not their lower one (the first bin includes both).

`reverse: bool = ``False`  
Should the order of the palette colors be reversed?

`truncate: bool = ``False`  
If `True`, then values below the lowest boundary are placed in the first bin and values above the highest boundary are placed in the last bin. If `False` (the default), then they receive the missing-value color.


## Returns


`Callable[[list[Any]], list[str | None]]`  
A function that takes a list of numeric values and returns a list of hexadecimal colors.


## Examples

Let's color the `currency` column of the [exibble](data.exibble.md#great_tables.data.exibble) dataset in three bins with explicit boundaries:


``` python
from great_tables import GT, col_bin
from great_tables.data import exibble

GT(exibble[["currency", "char"]]).data_color(
    columns="currency",
    fn=col_bin(palette="Blues", bins=[0, 10, 1000, 100000]),
    na_color="lightgray",
)
```


<style>
#pevppoonhi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pevppoonhi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pevppoonhi p { margin: 0; padding: 0; }
 #pevppoonhi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pevppoonhi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pevppoonhi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pevppoonhi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pevppoonhi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pevppoonhi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pevppoonhi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pevppoonhi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pevppoonhi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pevppoonhi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pevppoonhi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pevppoonhi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pevppoonhi .gt_spanner_row { border-bottom-style: hidden; }
 #pevppoonhi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pevppoonhi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pevppoonhi .gt_from_md> :first-child { margin-top: 0; }
 #pevppoonhi .gt_from_md> :last-child { margin-bottom: 0; }
 #pevppoonhi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pevppoonhi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pevppoonhi .gt_indent_1 { text-indent: 5px; }
 #pevppoonhi .gt_indent_2 { text-indent: calc(5px * 2); }
 #pevppoonhi .gt_indent_3 { text-indent: calc(5px * 3); }
 #pevppoonhi .gt_indent_4 { text-indent: calc(5px * 4); }
 #pevppoonhi .gt_indent_5 { text-indent: calc(5px * 5); }
 #pevppoonhi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pevppoonhi .gt_row_group_first td { border-top-width: 2px; }
 #pevppoonhi .gt_row_group_first th { border-top-width: 2px; }
 #pevppoonhi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pevppoonhi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pevppoonhi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pevppoonhi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pevppoonhi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pevppoonhi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pevppoonhi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pevppoonhi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pevppoonhi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pevppoonhi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pevppoonhi .gt_left { text-align: left; }
 #pevppoonhi .gt_center { text-align: center; }
 #pevppoonhi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pevppoonhi .gt_font_normal { font-weight: normal; }
 #pevppoonhi .gt_font_bold { font-weight: bold; }
 #pevppoonhi .gt_font_italic { font-style: italic; }
 #pevppoonhi .gt_super { font-size: 65%; }
 #pevppoonhi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pevppoonhi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pevppoonhi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pevppoonhi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pevppoonhi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pevppoonhi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| currency | char       |
|----------|------------|
| 49.95    | apricot    |
| 17.95    | banana     |
| 1.39     | coconut    |
| 65100.0  | durian     |
| 1325.81  | None       |
| 13.255   | fig        |
| None     | grapefruit |
| 0.44     | honeydew   |
