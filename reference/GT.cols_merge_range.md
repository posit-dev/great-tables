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
#izkzmbplzb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#izkzmbplzb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#izkzmbplzb p { margin: 0; padding: 0; }
 #izkzmbplzb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #izkzmbplzb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #izkzmbplzb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #izkzmbplzb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #izkzmbplzb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #izkzmbplzb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #izkzmbplzb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #izkzmbplzb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #izkzmbplzb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #izkzmbplzb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #izkzmbplzb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #izkzmbplzb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #izkzmbplzb .gt_spanner_row { border-bottom-style: hidden; }
 #izkzmbplzb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #izkzmbplzb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #izkzmbplzb .gt_from_md> :first-child { margin-top: 0; }
 #izkzmbplzb .gt_from_md> :last-child { margin-bottom: 0; }
 #izkzmbplzb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #izkzmbplzb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #izkzmbplzb .gt_indent_1 { text-indent: 5px; }
 #izkzmbplzb .gt_indent_2 { text-indent: calc(5px * 2); }
 #izkzmbplzb .gt_indent_3 { text-indent: calc(5px * 3); }
 #izkzmbplzb .gt_indent_4 { text-indent: calc(5px * 4); }
 #izkzmbplzb .gt_indent_5 { text-indent: calc(5px * 5); }
 #izkzmbplzb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #izkzmbplzb .gt_row_group_first td { border-top-width: 2px; }
 #izkzmbplzb .gt_row_group_first th { border-top-width: 2px; }
 #izkzmbplzb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #izkzmbplzb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #izkzmbplzb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #izkzmbplzb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #izkzmbplzb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #izkzmbplzb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #izkzmbplzb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #izkzmbplzb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #izkzmbplzb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #izkzmbplzb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #izkzmbplzb .gt_left { text-align: left; }
 #izkzmbplzb .gt_center { text-align: center; }
 #izkzmbplzb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #izkzmbplzb .gt_font_normal { font-weight: normal; }
 #izkzmbplzb .gt_font_bold { font-weight: bold; }
 #izkzmbplzb .gt_font_italic { font-style: italic; }
 #izkzmbplzb .gt_super { font-size: 65%; }
 #izkzmbplzb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #izkzmbplzb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #izkzmbplzb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #izkzmbplzb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #izkzmbplzb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #izkzmbplzb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hjaqgsojqm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hjaqgsojqm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hjaqgsojqm p { margin: 0; padding: 0; }
 #hjaqgsojqm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hjaqgsojqm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hjaqgsojqm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hjaqgsojqm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hjaqgsojqm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hjaqgsojqm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjaqgsojqm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hjaqgsojqm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hjaqgsojqm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hjaqgsojqm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hjaqgsojqm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hjaqgsojqm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hjaqgsojqm .gt_spanner_row { border-bottom-style: hidden; }
 #hjaqgsojqm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hjaqgsojqm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hjaqgsojqm .gt_from_md> :first-child { margin-top: 0; }
 #hjaqgsojqm .gt_from_md> :last-child { margin-bottom: 0; }
 #hjaqgsojqm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hjaqgsojqm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hjaqgsojqm .gt_indent_1 { text-indent: 5px; }
 #hjaqgsojqm .gt_indent_2 { text-indent: calc(5px * 2); }
 #hjaqgsojqm .gt_indent_3 { text-indent: calc(5px * 3); }
 #hjaqgsojqm .gt_indent_4 { text-indent: calc(5px * 4); }
 #hjaqgsojqm .gt_indent_5 { text-indent: calc(5px * 5); }
 #hjaqgsojqm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hjaqgsojqm .gt_row_group_first td { border-top-width: 2px; }
 #hjaqgsojqm .gt_row_group_first th { border-top-width: 2px; }
 #hjaqgsojqm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hjaqgsojqm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjaqgsojqm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hjaqgsojqm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hjaqgsojqm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjaqgsojqm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hjaqgsojqm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hjaqgsojqm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hjaqgsojqm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjaqgsojqm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hjaqgsojqm .gt_left { text-align: left; }
 #hjaqgsojqm .gt_center { text-align: center; }
 #hjaqgsojqm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hjaqgsojqm .gt_font_normal { font-weight: normal; }
 #hjaqgsojqm .gt_font_bold { font-weight: bold; }
 #hjaqgsojqm .gt_font_italic { font-style: italic; }
 #hjaqgsojqm .gt_super { font-size: 65%; }
 #hjaqgsojqm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjaqgsojqm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hjaqgsojqm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjaqgsojqm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hjaqgsojqm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hjaqgsojqm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| city | Temp. Range (°F) |
|------|------------------|
| NYC  | 28 to 35         |
| LA   | 55               |
| CHI  | 50               |
| HOU  | 45 to 60         |
