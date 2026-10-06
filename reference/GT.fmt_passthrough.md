# GT.fmt_passthrough()


Format values by passing them through, optionally escaping and decorating.


Usage

``` python
GT.fmt_passthrough(
    columns=None,
    rows=None,
    escape=True,
    pattern="{x}",
)
```


The [fmt_passthrough()](GT.fmt_passthrough.md#great_tables.GT.fmt_passthrough) method allows you to mark cells as formatted without transforming them. This is useful in two situations:

- **Escaping**: When `escape=True` (the default), special characters in cell values are escaped for the output context (HTML or LaTeX). This protects against cross-site scripting (XSS) while giving you explicit control over which cells are escaped.
- **Decoration**: The `pattern=` argument lets you wrap values in a text pattern (e.g., `pattern="[{x}]"`) without changing the underlying value.

Since [fmt_passthrough()](GT.fmt_passthrough.md#great_tables.GT.fmt_passthrough) marks cells as formatted, they are no longer subject to the automatic escaping that applies to unformatted cells. Setting `escape=False` is the way to include raw HTML or LaTeX in cell values without using the [html()](html.md#great_tables.html) helper.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`escape: bool = ``True`  
Should the cell values be escaped for the output context? When `True` (the default), HTML special characters like `<`, `>`, and `&` are escaped in HTML output, and LaTeX special characters are escaped in LaTeX output. Set to `False` to pass values through without escaping, which is useful when cell values already contain trusted HTML or LaTeX markup.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using [fmt_passthrough()](GT.fmt_passthrough.md#great_tables.GT.fmt_passthrough) with `escape=True` (the default) to safely render user-supplied data:


``` python
from great_tables import GT
import pandas as pd

df = pd.DataFrame({"input": ["<b>bold</b>", "x & y", "normal text"]})

GT(df).fmt_passthrough(columns="input")
```


<style>
#vcnsptblno table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vcnsptblno thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vcnsptblno p { margin: 0; padding: 0; }
 #vcnsptblno .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vcnsptblno .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vcnsptblno .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vcnsptblno .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vcnsptblno .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vcnsptblno .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vcnsptblno .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vcnsptblno .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vcnsptblno .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vcnsptblno .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vcnsptblno .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vcnsptblno .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vcnsptblno .gt_spanner_row { border-bottom-style: hidden; }
 #vcnsptblno .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vcnsptblno .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vcnsptblno .gt_from_md> :first-child { margin-top: 0; }
 #vcnsptblno .gt_from_md> :last-child { margin-bottom: 0; }
 #vcnsptblno .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vcnsptblno .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vcnsptblno .gt_indent_1 { text-indent: 5px; }
 #vcnsptblno .gt_indent_2 { text-indent: calc(5px * 2); }
 #vcnsptblno .gt_indent_3 { text-indent: calc(5px * 3); }
 #vcnsptblno .gt_indent_4 { text-indent: calc(5px * 4); }
 #vcnsptblno .gt_indent_5 { text-indent: calc(5px * 5); }
 #vcnsptblno .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vcnsptblno .gt_row_group_first td { border-top-width: 2px; }
 #vcnsptblno .gt_row_group_first th { border-top-width: 2px; }
 #vcnsptblno .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vcnsptblno .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vcnsptblno .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vcnsptblno .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vcnsptblno .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vcnsptblno .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vcnsptblno .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vcnsptblno .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vcnsptblno .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vcnsptblno .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vcnsptblno .gt_left { text-align: left; }
 #vcnsptblno .gt_center { text-align: center; }
 #vcnsptblno .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vcnsptblno .gt_font_normal { font-weight: normal; }
 #vcnsptblno .gt_font_bold { font-weight: bold; }
 #vcnsptblno .gt_font_italic { font-style: italic; }
 #vcnsptblno .gt_super { font-size: 65%; }
 #vcnsptblno .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vcnsptblno .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vcnsptblno .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vcnsptblno .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vcnsptblno .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vcnsptblno .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| input           |
|-----------------|
| \<b\>bold\</b\> |
| x & y           |
| normal text     |


Using `pattern=` to decorate values without otherwise changing them:


``` python
from great_tables import GT
import pandas as pd

df = pd.DataFrame({"code": ["ABC", "DEF", "GHI"]})

GT(df).fmt_passthrough(columns="code", pattern="[{x}]")
```


<style>
#dzxsqcstxl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dzxsqcstxl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dzxsqcstxl p { margin: 0; padding: 0; }
 #dzxsqcstxl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dzxsqcstxl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dzxsqcstxl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dzxsqcstxl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dzxsqcstxl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dzxsqcstxl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dzxsqcstxl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dzxsqcstxl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dzxsqcstxl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dzxsqcstxl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dzxsqcstxl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dzxsqcstxl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dzxsqcstxl .gt_spanner_row { border-bottom-style: hidden; }
 #dzxsqcstxl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dzxsqcstxl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dzxsqcstxl .gt_from_md> :first-child { margin-top: 0; }
 #dzxsqcstxl .gt_from_md> :last-child { margin-bottom: 0; }
 #dzxsqcstxl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dzxsqcstxl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dzxsqcstxl .gt_indent_1 { text-indent: 5px; }
 #dzxsqcstxl .gt_indent_2 { text-indent: calc(5px * 2); }
 #dzxsqcstxl .gt_indent_3 { text-indent: calc(5px * 3); }
 #dzxsqcstxl .gt_indent_4 { text-indent: calc(5px * 4); }
 #dzxsqcstxl .gt_indent_5 { text-indent: calc(5px * 5); }
 #dzxsqcstxl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dzxsqcstxl .gt_row_group_first td { border-top-width: 2px; }
 #dzxsqcstxl .gt_row_group_first th { border-top-width: 2px; }
 #dzxsqcstxl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dzxsqcstxl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dzxsqcstxl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dzxsqcstxl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dzxsqcstxl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dzxsqcstxl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dzxsqcstxl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dzxsqcstxl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dzxsqcstxl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dzxsqcstxl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dzxsqcstxl .gt_left { text-align: left; }
 #dzxsqcstxl .gt_center { text-align: center; }
 #dzxsqcstxl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dzxsqcstxl .gt_font_normal { font-weight: normal; }
 #dzxsqcstxl .gt_font_bold { font-weight: bold; }
 #dzxsqcstxl .gt_font_italic { font-style: italic; }
 #dzxsqcstxl .gt_super { font-size: 65%; }
 #dzxsqcstxl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dzxsqcstxl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dzxsqcstxl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dzxsqcstxl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dzxsqcstxl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dzxsqcstxl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| code    |
|---------|
| \[ABC\] |
| \[DEF\] |
| \[GHI\] |


Using `escape=False` to pass through trusted HTML:


``` python
from great_tables import GT
import pandas as pd

df = pd.DataFrame({"content": ["<b>bold</b>", "<em>italic</em>"]})

GT(df).fmt_passthrough(columns="content", escape=False)
```


<style>
#knvgqdxjqc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#knvgqdxjqc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#knvgqdxjqc p { margin: 0; padding: 0; }
 #knvgqdxjqc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #knvgqdxjqc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #knvgqdxjqc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #knvgqdxjqc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #knvgqdxjqc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #knvgqdxjqc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #knvgqdxjqc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #knvgqdxjqc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #knvgqdxjqc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #knvgqdxjqc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #knvgqdxjqc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #knvgqdxjqc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #knvgqdxjqc .gt_spanner_row { border-bottom-style: hidden; }
 #knvgqdxjqc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #knvgqdxjqc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #knvgqdxjqc .gt_from_md> :first-child { margin-top: 0; }
 #knvgqdxjqc .gt_from_md> :last-child { margin-bottom: 0; }
 #knvgqdxjqc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #knvgqdxjqc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #knvgqdxjqc .gt_indent_1 { text-indent: 5px; }
 #knvgqdxjqc .gt_indent_2 { text-indent: calc(5px * 2); }
 #knvgqdxjqc .gt_indent_3 { text-indent: calc(5px * 3); }
 #knvgqdxjqc .gt_indent_4 { text-indent: calc(5px * 4); }
 #knvgqdxjqc .gt_indent_5 { text-indent: calc(5px * 5); }
 #knvgqdxjqc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #knvgqdxjqc .gt_row_group_first td { border-top-width: 2px; }
 #knvgqdxjqc .gt_row_group_first th { border-top-width: 2px; }
 #knvgqdxjqc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #knvgqdxjqc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #knvgqdxjqc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #knvgqdxjqc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #knvgqdxjqc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #knvgqdxjqc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #knvgqdxjqc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #knvgqdxjqc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #knvgqdxjqc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #knvgqdxjqc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #knvgqdxjqc .gt_left { text-align: left; }
 #knvgqdxjqc .gt_center { text-align: center; }
 #knvgqdxjqc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #knvgqdxjqc .gt_font_normal { font-weight: normal; }
 #knvgqdxjqc .gt_font_bold { font-weight: bold; }
 #knvgqdxjqc .gt_font_italic { font-style: italic; }
 #knvgqdxjqc .gt_super { font-size: 65%; }
 #knvgqdxjqc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #knvgqdxjqc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #knvgqdxjqc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #knvgqdxjqc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #knvgqdxjqc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #knvgqdxjqc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| content  |
|----------|
| **bold** |
| *italic* |
