# GT.sub_small_vals()


Substitute small values in the table body.


Usage

``` python
GT.sub_small_vals(
    columns=None,
    rows=None,
    threshold=0.01,
    small_pattern=None,
    sign="+",
)
```


Wherever there is numerical data that are very small in value, replacement text may be better for explanatory purposes. The [sub_small_vals()](GT.sub_small_vals.md#great_tables.GT.sub_small_vals) method allows for this replacement through specification of a `threshold`, a `small_pattern`, and the sign of the values to be considered. The substitution will occur for those values found to be between `0` and the threshold value. This is possible for small positive and small negative values (this can be explicitly set by the `sign` option). Note that the interval does not include the `0` or the `threshold` value. Should you need to include zero values, use [sub_zero()](GT.sub_zero.md#great_tables.GT.sub_zero).


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should be scanned for small values. The default is all rows, resulting in all rows in all targeted columns being considered for this substitution. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`threshold: int | float = ``0.01`  
The threshold value with which values should be considered small enough for replacement.

`small_pattern: str | None = None`  
The pattern text to be used in place of the suitably small values in the rendered table. The `{x}` placeholder within the pattern will be replaced with the threshold value (written compactly, e.g., `0.01` or `1e-04`). If not provided, the default is `"<{x}"` for positive values and `">-{x}"` for negative values.

`sign: str = ``"+"`  
The sign of the numbers to be considered in the replacement. By default, we only consider positive values (`"+"`). The other option (`"-"`) can be used to consider only negative values.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's generate a simple, single-column table that contains an assortment of values that could potentially undergo some substitution via [sub_small_vals()](GT.sub_small_vals.md#great_tables.GT.sub_small_vals).


``` python
from great_tables import GT
import polars as pl

single_vals_df = pl.DataFrame(
    {
        "i": range(1, 8),
        "numbers": [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0]
    }
)

GT(single_vals_df).fmt_number(columns="numbers").sub_small_vals()
```


<style>
#czpbemlvuj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#czpbemlvuj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#czpbemlvuj p { margin: 0; padding: 0; }
 #czpbemlvuj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #czpbemlvuj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #czpbemlvuj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #czpbemlvuj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #czpbemlvuj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #czpbemlvuj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #czpbemlvuj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #czpbemlvuj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #czpbemlvuj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #czpbemlvuj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #czpbemlvuj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #czpbemlvuj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #czpbemlvuj .gt_spanner_row { border-bottom-style: hidden; }
 #czpbemlvuj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #czpbemlvuj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #czpbemlvuj .gt_from_md> :first-child { margin-top: 0; }
 #czpbemlvuj .gt_from_md> :last-child { margin-bottom: 0; }
 #czpbemlvuj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #czpbemlvuj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #czpbemlvuj .gt_indent_1 { text-indent: 5px; }
 #czpbemlvuj .gt_indent_2 { text-indent: calc(5px * 2); }
 #czpbemlvuj .gt_indent_3 { text-indent: calc(5px * 3); }
 #czpbemlvuj .gt_indent_4 { text-indent: calc(5px * 4); }
 #czpbemlvuj .gt_indent_5 { text-indent: calc(5px * 5); }
 #czpbemlvuj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #czpbemlvuj .gt_row_group_first td { border-top-width: 2px; }
 #czpbemlvuj .gt_row_group_first th { border-top-width: 2px; }
 #czpbemlvuj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #czpbemlvuj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #czpbemlvuj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #czpbemlvuj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #czpbemlvuj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #czpbemlvuj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #czpbemlvuj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #czpbemlvuj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #czpbemlvuj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #czpbemlvuj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #czpbemlvuj .gt_left { text-align: left; }
 #czpbemlvuj .gt_center { text-align: center; }
 #czpbemlvuj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #czpbemlvuj .gt_font_normal { font-weight: normal; }
 #czpbemlvuj .gt_font_bold { font-weight: bold; }
 #czpbemlvuj .gt_font_italic { font-style: italic; }
 #czpbemlvuj .gt_super { font-size: 65%; }
 #czpbemlvuj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #czpbemlvuj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #czpbemlvuj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #czpbemlvuj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #czpbemlvuj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #czpbemlvuj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| i   | numbers |
|-----|---------|
| 1   | \<0.01  |
| 2   | \<0.01  |
| 3   | 0.01    |
| 4   | 0.10    |
| 5   | 1.00    |
| 6   | 10.00   |
| 7   | 100.00  |


We can also target small negative values by setting `sign="-"` and use a custom `small_pattern` to provide alternative replacement text.


``` python
from great_tables import GT
import polars as pl

neg_vals_df = pl.DataFrame(
    {
        "i": range(1, 6),
        "numbers": [-0.0001, -0.005, -0.05, -1.0, -100.0]
    }
)

(
    GT(neg_vals_df)
    .fmt_number(columns="numbers")
    .sub_small_vals(sign="-", threshold=0.01, small_pattern="~0")
)
```


<style>
#ululuxzmqw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ululuxzmqw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ululuxzmqw p { margin: 0; padding: 0; }
 #ululuxzmqw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ululuxzmqw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ululuxzmqw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ululuxzmqw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ululuxzmqw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ululuxzmqw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ululuxzmqw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ululuxzmqw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ululuxzmqw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ululuxzmqw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ululuxzmqw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ululuxzmqw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ululuxzmqw .gt_spanner_row { border-bottom-style: hidden; }
 #ululuxzmqw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ululuxzmqw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ululuxzmqw .gt_from_md> :first-child { margin-top: 0; }
 #ululuxzmqw .gt_from_md> :last-child { margin-bottom: 0; }
 #ululuxzmqw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ululuxzmqw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ululuxzmqw .gt_indent_1 { text-indent: 5px; }
 #ululuxzmqw .gt_indent_2 { text-indent: calc(5px * 2); }
 #ululuxzmqw .gt_indent_3 { text-indent: calc(5px * 3); }
 #ululuxzmqw .gt_indent_4 { text-indent: calc(5px * 4); }
 #ululuxzmqw .gt_indent_5 { text-indent: calc(5px * 5); }
 #ululuxzmqw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ululuxzmqw .gt_row_group_first td { border-top-width: 2px; }
 #ululuxzmqw .gt_row_group_first th { border-top-width: 2px; }
 #ululuxzmqw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ululuxzmqw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ululuxzmqw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ululuxzmqw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ululuxzmqw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ululuxzmqw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ululuxzmqw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ululuxzmqw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ululuxzmqw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ululuxzmqw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ululuxzmqw .gt_left { text-align: left; }
 #ululuxzmqw .gt_center { text-align: center; }
 #ululuxzmqw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ululuxzmqw .gt_font_normal { font-weight: normal; }
 #ululuxzmqw .gt_font_bold { font-weight: bold; }
 #ululuxzmqw .gt_font_italic { font-style: italic; }
 #ululuxzmqw .gt_super { font-size: 65%; }
 #ululuxzmqw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ululuxzmqw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ululuxzmqw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ululuxzmqw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ululuxzmqw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ululuxzmqw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| i   | numbers |
|-----|---------|
| 1   | ~0      |
| 2   | ~0      |
| 3   | −0.05   |
| 4   | −1.00   |
| 5   | −100.00 |
