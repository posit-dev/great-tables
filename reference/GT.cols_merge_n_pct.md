# GT.cols_merge_n_pct()


Merge two columns to combine counts and percentages.


Usage

``` python
GT.cols_merge_n_pct(
    col_n,
    col_pct,
    rows=None,
    autohide=True,
)
```


[cols_merge_n_pct()](GT.cols_merge_n_pct.md#great_tables.GT.cols_merge_n_pct) is a specialized variant of [cols_merge()](GT.cols_merge.md#great_tables.GT.cols_merge). It operates by taking two columns that constitute both a count (`col_n`) and a fraction of the total population (`col_pct`) and merges them into a single column. What results is a column containing both counts and their associated percentages (e.g., `12 (23.2%)`). The column specified in `col_pct` is dropped from the output table.


## Parameters


`col_n: SelectExpr`  
The column that contains values for the count component. While column selection expressions can be used, it's recommended that a single column name be used to ensure that exactly one column is provided here.

`col_pct: SelectExpr`  
The column that contains values for the percentage component. While column selection expressions can be used, it's recommended that a single column name be used to ensure that exactly one column is provided here. This column should be formatted such that percentages are displayed (e.g., with `fmt_percent()`).

`rows: RowSelectExpr = None`  
In conjunction with `col_n`, we can specify which rows should participate in the merging process. The default is all rows. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`autohide: bool = ``True`  
An option to automatically hide the column specified as `col_pct`. Any columns with their state changed to hidden will behave the same as before, they just won't be displayed in the finalized table. Defaults to `True`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Details


### Specialized NA and zero-value handling

This function employs specialized semantics for missing value and zero-value handling:

1.  Missing values in `col_n` result in missing values for the merged column (e.g., `NA` + `10.2%` = `NA`)
2.  Missing values in `col_pct` (but not `col_n`) result in base values only for the merged column (e.g., `13` + `NA` = `13`)
3.  Missing values in both `col_n` and `col_pct` result in missing values for the merged column (e.g., `NA` + `NA` = `NA`)
4.  If a zero (`0`) value is in `col_n` then the formatted output will be `"0"` (i.e., no percentage will be shown)

It is the responsibility of the user to ensure that values are correct in both the `col_n` and `col_pct` columns (this function neither generates nor recalculates values in either). Formatting of each column can be done independently in separate `fmt_number()` and `fmt_percent()` calls.


## Examples

Create a simple table with counts and percentages, then merge them.


``` python
from great_tables import GT
import polars as pl

df = pl.DataFrame({
    "category": ["A", "B", "C"],
    "n": [10, 20, 30],
    "pct": [0.167, 0.333, 0.500],
})

(
    GT(df)
    .fmt_percent(columns="pct")
    .cols_merge_n_pct(col_n="n", col_pct="pct")
    .cols_label(n="Count (%)")
)
```


<style>
#qwxippezeg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qwxippezeg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qwxippezeg p { margin: 0; padding: 0; }
 #qwxippezeg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qwxippezeg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qwxippezeg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qwxippezeg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qwxippezeg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qwxippezeg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qwxippezeg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qwxippezeg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qwxippezeg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qwxippezeg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qwxippezeg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qwxippezeg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qwxippezeg .gt_spanner_row { border-bottom-style: hidden; }
 #qwxippezeg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qwxippezeg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qwxippezeg .gt_from_md> :first-child { margin-top: 0; }
 #qwxippezeg .gt_from_md> :last-child { margin-bottom: 0; }
 #qwxippezeg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qwxippezeg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qwxippezeg .gt_indent_1 { text-indent: 5px; }
 #qwxippezeg .gt_indent_2 { text-indent: calc(5px * 2); }
 #qwxippezeg .gt_indent_3 { text-indent: calc(5px * 3); }
 #qwxippezeg .gt_indent_4 { text-indent: calc(5px * 4); }
 #qwxippezeg .gt_indent_5 { text-indent: calc(5px * 5); }
 #qwxippezeg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qwxippezeg .gt_row_group_first td { border-top-width: 2px; }
 #qwxippezeg .gt_row_group_first th { border-top-width: 2px; }
 #qwxippezeg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qwxippezeg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qwxippezeg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qwxippezeg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qwxippezeg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qwxippezeg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qwxippezeg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qwxippezeg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qwxippezeg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qwxippezeg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qwxippezeg .gt_left { text-align: left; }
 #qwxippezeg .gt_center { text-align: center; }
 #qwxippezeg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qwxippezeg .gt_font_normal { font-weight: normal; }
 #qwxippezeg .gt_font_bold { font-weight: bold; }
 #qwxippezeg .gt_font_italic { font-style: italic; }
 #qwxippezeg .gt_super { font-size: 65%; }
 #qwxippezeg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qwxippezeg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qwxippezeg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qwxippezeg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qwxippezeg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qwxippezeg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| category | Count (%)   |
|----------|-------------|
| A        | 10 (16.70%) |
| B        | 20 (33.30%) |
| C        | 30 (50.00%) |


Zero values in the count column suppress the percentage display. Missing values in the percentage column result in just the count being shown, and missing counts produce empty cells.


``` python
df = pl.DataFrame({
    "item": ["Alpha", "Beta", "Gamma", "Delta"],
    "count": [15, 0, 8, None],
    "frac": [0.375, 0.0, None, 0.125],
})

(
    GT(df)
    .fmt_percent(columns="frac", decimals=1)
    .cols_merge_n_pct(col_n="count", col_pct="frac")
    .cols_label(count="N (%)")
)
```


<style>
#vukyoyceiz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vukyoyceiz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vukyoyceiz p { margin: 0; padding: 0; }
 #vukyoyceiz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vukyoyceiz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vukyoyceiz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vukyoyceiz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vukyoyceiz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vukyoyceiz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vukyoyceiz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vukyoyceiz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vukyoyceiz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vukyoyceiz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vukyoyceiz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vukyoyceiz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vukyoyceiz .gt_spanner_row { border-bottom-style: hidden; }
 #vukyoyceiz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vukyoyceiz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vukyoyceiz .gt_from_md> :first-child { margin-top: 0; }
 #vukyoyceiz .gt_from_md> :last-child { margin-bottom: 0; }
 #vukyoyceiz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vukyoyceiz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vukyoyceiz .gt_indent_1 { text-indent: 5px; }
 #vukyoyceiz .gt_indent_2 { text-indent: calc(5px * 2); }
 #vukyoyceiz .gt_indent_3 { text-indent: calc(5px * 3); }
 #vukyoyceiz .gt_indent_4 { text-indent: calc(5px * 4); }
 #vukyoyceiz .gt_indent_5 { text-indent: calc(5px * 5); }
 #vukyoyceiz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vukyoyceiz .gt_row_group_first td { border-top-width: 2px; }
 #vukyoyceiz .gt_row_group_first th { border-top-width: 2px; }
 #vukyoyceiz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vukyoyceiz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vukyoyceiz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vukyoyceiz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vukyoyceiz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vukyoyceiz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vukyoyceiz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vukyoyceiz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vukyoyceiz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vukyoyceiz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vukyoyceiz .gt_left { text-align: left; }
 #vukyoyceiz .gt_center { text-align: center; }
 #vukyoyceiz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vukyoyceiz .gt_font_normal { font-weight: normal; }
 #vukyoyceiz .gt_font_bold { font-weight: bold; }
 #vukyoyceiz .gt_font_italic { font-style: italic; }
 #vukyoyceiz .gt_super { font-size: 65%; }
 #vukyoyceiz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vukyoyceiz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vukyoyceiz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vukyoyceiz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vukyoyceiz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vukyoyceiz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| item  | N (%)      |
|-------|------------|
| Alpha | 15 (37.5%) |
| Beta  | 0          |
| Gamma | 8          |
| Delta |            |
