# GT.fmt_roman()


Format values as Roman numerals.


Usage

``` python
GT.fmt_roman(
    columns=None,
    rows=None,
    case="upper",
    pattern="{x}",
)
```


With numeric values in a **gt** table we can transform those to Roman numerals, rounding values as necessary.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`case: str = ``"upper"`  
Should Roman numerals should be rendered as uppercase (`"upper"`) or lowercase (`"lower"`) letters? By default, this is set to `"upper"`.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's first create a DataFrame containing small numeric values and then introduce that to <a href="GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>. We'll then format the `roman` column to appear as Roman numerals with the [fmt_roman()](GT.fmt_roman.md#great_tables.GT.fmt_roman) method.


``` python
import pandas as pd
from great_tables import GT

numbers_tbl = pd.DataFrame({"arabic": [1, 8, 24, 85], "roman": [1, 8, 24, 85]})

(
    GT(numbers_tbl, rowname_col="arabic")
    .fmt_roman(columns="roman")
)
```


<style>
#otpitjtfdt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#otpitjtfdt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#otpitjtfdt p { margin: 0; padding: 0; }
 #otpitjtfdt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #otpitjtfdt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #otpitjtfdt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #otpitjtfdt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #otpitjtfdt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #otpitjtfdt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #otpitjtfdt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #otpitjtfdt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #otpitjtfdt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #otpitjtfdt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #otpitjtfdt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #otpitjtfdt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #otpitjtfdt .gt_spanner_row { border-bottom-style: hidden; }
 #otpitjtfdt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #otpitjtfdt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #otpitjtfdt .gt_from_md> :first-child { margin-top: 0; }
 #otpitjtfdt .gt_from_md> :last-child { margin-bottom: 0; }
 #otpitjtfdt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #otpitjtfdt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #otpitjtfdt .gt_indent_1 { text-indent: 5px; }
 #otpitjtfdt .gt_indent_2 { text-indent: calc(5px * 2); }
 #otpitjtfdt .gt_indent_3 { text-indent: calc(5px * 3); }
 #otpitjtfdt .gt_indent_4 { text-indent: calc(5px * 4); }
 #otpitjtfdt .gt_indent_5 { text-indent: calc(5px * 5); }
 #otpitjtfdt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #otpitjtfdt .gt_row_group_first td { border-top-width: 2px; }
 #otpitjtfdt .gt_row_group_first th { border-top-width: 2px; }
 #otpitjtfdt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #otpitjtfdt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #otpitjtfdt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #otpitjtfdt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #otpitjtfdt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #otpitjtfdt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #otpitjtfdt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #otpitjtfdt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #otpitjtfdt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #otpitjtfdt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #otpitjtfdt .gt_left { text-align: left; }
 #otpitjtfdt .gt_center { text-align: center; }
 #otpitjtfdt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #otpitjtfdt .gt_font_normal { font-weight: normal; }
 #otpitjtfdt .gt_font_bold { font-weight: bold; }
 #otpitjtfdt .gt_font_italic { font-style: italic; }
 #otpitjtfdt .gt_super { font-size: 65%; }
 #otpitjtfdt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #otpitjtfdt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #otpitjtfdt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #otpitjtfdt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #otpitjtfdt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #otpitjtfdt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|     | roman |
|-----|-------|
| 1   | I     |
| 8   | VIII  |
| 24  | XXIV  |
| 85  | LXXXV |
