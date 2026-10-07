# GT.cols_merge_range()


Merge two columns to a value range column.


Usage

``` python
GT.cols_merge_range(
    col_begin,
    col_end,
    rows=None,
    sep=None,
    autohide=True,
    locale=None,
)
```


[cols_merge_range()](GT.cols_merge_range.md#great_tables.GT.cols_merge_range) is a specialized variant of [cols_merge()](GT.cols_merge.md#great_tables.GT.cols_merge). It operates by taking two columns that constitute a range of values (`col_begin` and `col_end`) and merges them into a single column. What results is a column containing both values separated by an en dash (or a custom separator). The column specified in `col_end` is dropped from the output table.


## Parameters


`col_begin: SelectExpr`  
The column that contains values for the start of the range. While column selection expressions can be used, it's recommended that a single column name be used to ensure that exactly one column is provided here.

`col_end: SelectExpr`  
The column that contains values for the end of the range. While column selection expressions can be used, it's recommended that a single column name be used to ensure that exactly one column is provided here.

`rows: RowSelectExpr = None`  
In conjunction with `col_begin`, we can specify which rows should participate in the merging process. The default is all rows. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`sep: str | None = None`  
The separator text that indicates the values are ranged. If not provided, an en dash (`"-"`) will be used. You can use `"--"` for an en dash or `"---"` for an em dash.

`autohide: bool = ``True`  
An option to automatically hide the column specified as `col_end`. Any columns with their state changed to hidden will behave the same as before, they just won't be displayed in the finalized table. Defaults to `True`.

`locale: str | None = None`  
An optional locale identifier that can be used for applying a separator pattern specific to a locale's rules. Currently reserved for future use.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Details


### Specialized NA handling

This function employs specialized semantics for missing value handling that differ from the generic [cols_merge()](GT.cols_merge.md#great_tables.GT.cols_merge):

1.  Missing values in `col_begin` (but not `col_end`) result in a display of only the `col_end` value
2.  Missing values in `col_end` (but not `col_begin`) result in a display of only the `col_begin` value
3.  Missing values in both `col_begin` and `col_end` result in missing values for the merged column


## Examples

Use a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset to create a table. Merge the `mpg_c` and `mpg_h` columns together as a range.


``` python
from great_tables import GT
from great_tables.data import gtcars
import polars as pl

gtcars_mini = (
    pl.from_pandas(gtcars)
    .select("model", "mpg_c", "mpg_h")
    .slice(0, 8)
)

(
    GT(gtcars_mini)
    .cols_merge_range(col_begin="mpg_c", col_end="mpg_h")
    .cols_label(mpg_c="MPG")
)
```


<style>
#rckztatksc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rckztatksc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rckztatksc p { margin: 0; padding: 0; }
 #rckztatksc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rckztatksc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rckztatksc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rckztatksc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rckztatksc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rckztatksc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rckztatksc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rckztatksc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rckztatksc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rckztatksc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rckztatksc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rckztatksc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rckztatksc .gt_spanner_row { border-bottom-style: hidden; }
 #rckztatksc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rckztatksc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rckztatksc .gt_from_md> :first-child { margin-top: 0; }
 #rckztatksc .gt_from_md> :last-child { margin-bottom: 0; }
 #rckztatksc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rckztatksc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rckztatksc .gt_indent_1 { text-indent: 5px; }
 #rckztatksc .gt_indent_2 { text-indent: calc(5px * 2); }
 #rckztatksc .gt_indent_3 { text-indent: calc(5px * 3); }
 #rckztatksc .gt_indent_4 { text-indent: calc(5px * 4); }
 #rckztatksc .gt_indent_5 { text-indent: calc(5px * 5); }
 #rckztatksc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rckztatksc .gt_row_group_first td { border-top-width: 2px; }
 #rckztatksc .gt_row_group_first th { border-top-width: 2px; }
 #rckztatksc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rckztatksc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rckztatksc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rckztatksc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rckztatksc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rckztatksc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rckztatksc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rckztatksc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rckztatksc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rckztatksc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rckztatksc .gt_left { text-align: left; }
 #rckztatksc .gt_center { text-align: center; }
 #rckztatksc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rckztatksc .gt_font_normal { font-weight: normal; }
 #rckztatksc .gt_font_bold { font-weight: bold; }
 #rckztatksc .gt_font_italic { font-style: italic; }
 #rckztatksc .gt_super { font-size: 65%; }
 #rckztatksc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rckztatksc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rckztatksc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rckztatksc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rckztatksc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rckztatksc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| model        | MPG       |
|--------------|-----------|
| GT           | 11.0-18.0 |
| 458 Speciale | 13.0-17.0 |
| 458 Spider   | 13.0-17.0 |
| 458 Italia   | 13.0-17.0 |
| 488 GTB      | 15.0-22.0 |
| California   | 16.0-23.0 |
| GTC4Lusso    | 12.0-17.0 |
| FF           | 11.0-16.0 |


When there are missing values, the merged result gracefully degrades: if only one side is missing, the other value is shown alone (without a separator). A custom separator can be provided via the `sep=` argument.


``` python
df = pl.DataFrame({
    "city": ["NYC", "LA", "CHI", "HOU"],
    "temp_low": [28, 55, None, 45],
    "temp_high": [35, None, 50, 60],
})

(
    GT(df)
    .cols_merge_range(col_begin="temp_low", col_end="temp_high", sep=" to ")
    .cols_label(temp_low="Temp. Range (°F)")
)
```


<style>
#jpsdzhwwyn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jpsdzhwwyn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jpsdzhwwyn p { margin: 0; padding: 0; }
 #jpsdzhwwyn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jpsdzhwwyn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jpsdzhwwyn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jpsdzhwwyn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jpsdzhwwyn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jpsdzhwwyn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jpsdzhwwyn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jpsdzhwwyn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jpsdzhwwyn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jpsdzhwwyn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jpsdzhwwyn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jpsdzhwwyn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jpsdzhwwyn .gt_spanner_row { border-bottom-style: hidden; }
 #jpsdzhwwyn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jpsdzhwwyn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jpsdzhwwyn .gt_from_md> :first-child { margin-top: 0; }
 #jpsdzhwwyn .gt_from_md> :last-child { margin-bottom: 0; }
 #jpsdzhwwyn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jpsdzhwwyn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jpsdzhwwyn .gt_indent_1 { text-indent: 5px; }
 #jpsdzhwwyn .gt_indent_2 { text-indent: calc(5px * 2); }
 #jpsdzhwwyn .gt_indent_3 { text-indent: calc(5px * 3); }
 #jpsdzhwwyn .gt_indent_4 { text-indent: calc(5px * 4); }
 #jpsdzhwwyn .gt_indent_5 { text-indent: calc(5px * 5); }
 #jpsdzhwwyn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jpsdzhwwyn .gt_row_group_first td { border-top-width: 2px; }
 #jpsdzhwwyn .gt_row_group_first th { border-top-width: 2px; }
 #jpsdzhwwyn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jpsdzhwwyn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jpsdzhwwyn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jpsdzhwwyn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jpsdzhwwyn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jpsdzhwwyn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jpsdzhwwyn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jpsdzhwwyn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jpsdzhwwyn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jpsdzhwwyn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jpsdzhwwyn .gt_left { text-align: left; }
 #jpsdzhwwyn .gt_center { text-align: center; }
 #jpsdzhwwyn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jpsdzhwwyn .gt_font_normal { font-weight: normal; }
 #jpsdzhwwyn .gt_font_bold { font-weight: bold; }
 #jpsdzhwwyn .gt_font_italic { font-style: italic; }
 #jpsdzhwwyn .gt_super { font-size: 65%; }
 #jpsdzhwwyn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jpsdzhwwyn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jpsdzhwwyn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jpsdzhwwyn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jpsdzhwwyn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jpsdzhwwyn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| city | Temp. Range (°F) |
|------|------------------|
| NYC  | 28 to 35         |
| LA   | 55               |
| CHI  | 50               |
| HOU  | 45 to 60         |
