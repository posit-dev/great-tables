# GT.sub_large_vals()


Substitute large values in the table body.


Usage

``` python
GT.sub_large_vals(
    columns=None,
    rows=None,
    threshold=1000000000000.0,
    large_pattern=">={x}",
    sign="+",
)
```


Wherever there are numerical data that are very large in value, replacement text may be better for explanatory purposes. The [sub_large_vals()](GT.sub_large_vals.md#great_tables.GT.sub_large_vals) method allows for this replacement through specification of a `threshold`, a `large_pattern`, and the sign (positive or negative) of the values to be considered.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should be scanned for large values. The default is all rows, resulting in all rows in all targeted columns being considered for this substitution. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`threshold: int | float = ``1000000000000.0`  
The threshold value with which values should be considered large enough for replacement.

`large_pattern: str = ``">={x}"`  
The pattern text to be used in place of the suitably large values in the rendered table. The `{x}` placeholder within the pattern will be replaced with the threshold value (written compactly, e.g., `1e+12` or `1000`). The default pattern, `">={x}"`, is shown with a `≥` mark (e.g., `≥1e+12`).

`sign: str = ``"+"`  
The sign of the numbers to be considered in the replacement. By default, we only consider positive values (`"+"`). The other option (`"-"`) can be used to consider only negative values. Note that when `sign="-"` and the default `large_pattern=">={x}"` is used, the output is shown with a `≤` mark and the negative threshold (e.g., `≤−1e+12`); in a custom pattern, `">="` is changed to `"<="`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's generate a simple, single-column table that contains an assortment of values that could potentially undergo some substitution via [sub_large_vals()](GT.sub_large_vals.md#great_tables.GT.sub_large_vals).


``` python
from great_tables import GT
import polars as pl

single_vals_df = pl.DataFrame(
    {
        "i": range(1, 8),
        "numbers": [0.0, 10.0, 1e8, 1e9, 1e10, 1e11, 1e12]
    }
)

GT(single_vals_df).fmt_number(columns="numbers").sub_large_vals(threshold=1e10)
```


<style>
#nrawqrfnhv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nrawqrfnhv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nrawqrfnhv p { margin: 0; padding: 0; }
 #nrawqrfnhv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nrawqrfnhv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nrawqrfnhv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nrawqrfnhv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nrawqrfnhv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nrawqrfnhv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nrawqrfnhv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nrawqrfnhv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nrawqrfnhv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nrawqrfnhv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nrawqrfnhv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nrawqrfnhv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nrawqrfnhv .gt_spanner_row { border-bottom-style: hidden; }
 #nrawqrfnhv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nrawqrfnhv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nrawqrfnhv .gt_from_md> :first-child { margin-top: 0; }
 #nrawqrfnhv .gt_from_md> :last-child { margin-bottom: 0; }
 #nrawqrfnhv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nrawqrfnhv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nrawqrfnhv .gt_indent_1 { text-indent: 5px; }
 #nrawqrfnhv .gt_indent_2 { text-indent: calc(5px * 2); }
 #nrawqrfnhv .gt_indent_3 { text-indent: calc(5px * 3); }
 #nrawqrfnhv .gt_indent_4 { text-indent: calc(5px * 4); }
 #nrawqrfnhv .gt_indent_5 { text-indent: calc(5px * 5); }
 #nrawqrfnhv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nrawqrfnhv .gt_row_group_first td { border-top-width: 2px; }
 #nrawqrfnhv .gt_row_group_first th { border-top-width: 2px; }
 #nrawqrfnhv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nrawqrfnhv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nrawqrfnhv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nrawqrfnhv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nrawqrfnhv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nrawqrfnhv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nrawqrfnhv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nrawqrfnhv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nrawqrfnhv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nrawqrfnhv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nrawqrfnhv .gt_left { text-align: left; }
 #nrawqrfnhv .gt_center { text-align: center; }
 #nrawqrfnhv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nrawqrfnhv .gt_font_normal { font-weight: normal; }
 #nrawqrfnhv .gt_font_bold { font-weight: bold; }
 #nrawqrfnhv .gt_font_italic { font-style: italic; }
 #nrawqrfnhv .gt_super { font-size: 65%; }
 #nrawqrfnhv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nrawqrfnhv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nrawqrfnhv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nrawqrfnhv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nrawqrfnhv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nrawqrfnhv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| i   | numbers          |
|-----|------------------|
| 1   | 0.00             |
| 2   | 10.00            |
| 3   | 100,000,000.00   |
| 4   | 1,000,000,000.00 |
| 5   | ≥1e+10           |
| 6   | ≥1e+10           |
| 7   | ≥1e+10           |


Large negative values can also be targeted with `sign="-"`. Notice the default pattern is automatically changed to `"<=-{x}"` when dealing with negative values.


``` python
from great_tables import GT
import polars as pl

neg_vals_df = pl.DataFrame(
    {
        "i": range(1, 5),
        "numbers": [-10.0, -500.0, -1e6, -1e12]
    }
)

(
    GT(neg_vals_df)
    .fmt_number(columns="numbers")
    .sub_large_vals(threshold=1000, sign="-")
)
```


<style>
#iippqwcdmj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iippqwcdmj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iippqwcdmj p { margin: 0; padding: 0; }
 #iippqwcdmj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #iippqwcdmj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iippqwcdmj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iippqwcdmj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iippqwcdmj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iippqwcdmj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iippqwcdmj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iippqwcdmj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iippqwcdmj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iippqwcdmj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iippqwcdmj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iippqwcdmj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iippqwcdmj .gt_spanner_row { border-bottom-style: hidden; }
 #iippqwcdmj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iippqwcdmj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #iippqwcdmj .gt_from_md> :first-child { margin-top: 0; }
 #iippqwcdmj .gt_from_md> :last-child { margin-bottom: 0; }
 #iippqwcdmj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #iippqwcdmj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #iippqwcdmj .gt_indent_1 { text-indent: 5px; }
 #iippqwcdmj .gt_indent_2 { text-indent: calc(5px * 2); }
 #iippqwcdmj .gt_indent_3 { text-indent: calc(5px * 3); }
 #iippqwcdmj .gt_indent_4 { text-indent: calc(5px * 4); }
 #iippqwcdmj .gt_indent_5 { text-indent: calc(5px * 5); }
 #iippqwcdmj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iippqwcdmj .gt_row_group_first td { border-top-width: 2px; }
 #iippqwcdmj .gt_row_group_first th { border-top-width: 2px; }
 #iippqwcdmj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #iippqwcdmj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iippqwcdmj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iippqwcdmj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #iippqwcdmj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iippqwcdmj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iippqwcdmj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iippqwcdmj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iippqwcdmj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iippqwcdmj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iippqwcdmj .gt_left { text-align: left; }
 #iippqwcdmj .gt_center { text-align: center; }
 #iippqwcdmj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iippqwcdmj .gt_font_normal { font-weight: normal; }
 #iippqwcdmj .gt_font_bold { font-weight: bold; }
 #iippqwcdmj .gt_font_italic { font-style: italic; }
 #iippqwcdmj .gt_super { font-size: 65%; }
 #iippqwcdmj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iippqwcdmj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #iippqwcdmj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iippqwcdmj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iippqwcdmj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iippqwcdmj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| i   | numbers |
|-----|---------|
| 1   | −10.00  |
| 2   | −500.00 |
| 3   | ≤−1000  |
| 4   | ≤−1000  |
