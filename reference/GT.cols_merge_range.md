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

`rows: int | list[int] | None = None`  
In conjunction with `col_begin`, we can specify which rows should participate in the merging process. The default is all rows. Alternatively, we can supply a list of row indices.

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
#gxudxvusnu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gxudxvusnu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gxudxvusnu p { margin: 0; padding: 0; }
 #gxudxvusnu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gxudxvusnu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gxudxvusnu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gxudxvusnu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gxudxvusnu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gxudxvusnu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gxudxvusnu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gxudxvusnu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gxudxvusnu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gxudxvusnu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gxudxvusnu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gxudxvusnu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gxudxvusnu .gt_spanner_row { border-bottom-style: hidden; }
 #gxudxvusnu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gxudxvusnu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gxudxvusnu .gt_from_md> :first-child { margin-top: 0; }
 #gxudxvusnu .gt_from_md> :last-child { margin-bottom: 0; }
 #gxudxvusnu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gxudxvusnu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gxudxvusnu .gt_indent_1 { text-indent: 5px; }
 #gxudxvusnu .gt_indent_2 { text-indent: calc(5px * 2); }
 #gxudxvusnu .gt_indent_3 { text-indent: calc(5px * 3); }
 #gxudxvusnu .gt_indent_4 { text-indent: calc(5px * 4); }
 #gxudxvusnu .gt_indent_5 { text-indent: calc(5px * 5); }
 #gxudxvusnu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gxudxvusnu .gt_row_group_first td { border-top-width: 2px; }
 #gxudxvusnu .gt_row_group_first th { border-top-width: 2px; }
 #gxudxvusnu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gxudxvusnu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gxudxvusnu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gxudxvusnu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gxudxvusnu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gxudxvusnu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gxudxvusnu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gxudxvusnu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gxudxvusnu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gxudxvusnu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gxudxvusnu .gt_left { text-align: left; }
 #gxudxvusnu .gt_center { text-align: center; }
 #gxudxvusnu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gxudxvusnu .gt_font_normal { font-weight: normal; }
 #gxudxvusnu .gt_font_bold { font-weight: bold; }
 #gxudxvusnu .gt_font_italic { font-style: italic; }
 #gxudxvusnu .gt_super { font-size: 65%; }
 #gxudxvusnu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gxudxvusnu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gxudxvusnu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gxudxvusnu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gxudxvusnu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gxudxvusnu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#irotlvdusf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#irotlvdusf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#irotlvdusf p { margin: 0; padding: 0; }
 #irotlvdusf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #irotlvdusf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #irotlvdusf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #irotlvdusf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #irotlvdusf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #irotlvdusf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #irotlvdusf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #irotlvdusf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #irotlvdusf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #irotlvdusf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #irotlvdusf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #irotlvdusf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #irotlvdusf .gt_spanner_row { border-bottom-style: hidden; }
 #irotlvdusf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #irotlvdusf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #irotlvdusf .gt_from_md> :first-child { margin-top: 0; }
 #irotlvdusf .gt_from_md> :last-child { margin-bottom: 0; }
 #irotlvdusf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #irotlvdusf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #irotlvdusf .gt_indent_1 { text-indent: 5px; }
 #irotlvdusf .gt_indent_2 { text-indent: calc(5px * 2); }
 #irotlvdusf .gt_indent_3 { text-indent: calc(5px * 3); }
 #irotlvdusf .gt_indent_4 { text-indent: calc(5px * 4); }
 #irotlvdusf .gt_indent_5 { text-indent: calc(5px * 5); }
 #irotlvdusf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #irotlvdusf .gt_row_group_first td { border-top-width: 2px; }
 #irotlvdusf .gt_row_group_first th { border-top-width: 2px; }
 #irotlvdusf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #irotlvdusf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #irotlvdusf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #irotlvdusf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #irotlvdusf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #irotlvdusf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #irotlvdusf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #irotlvdusf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #irotlvdusf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #irotlvdusf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #irotlvdusf .gt_left { text-align: left; }
 #irotlvdusf .gt_center { text-align: center; }
 #irotlvdusf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #irotlvdusf .gt_font_normal { font-weight: normal; }
 #irotlvdusf .gt_font_bold { font-weight: bold; }
 #irotlvdusf .gt_font_italic { font-style: italic; }
 #irotlvdusf .gt_super { font-size: 65%; }
 #irotlvdusf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #irotlvdusf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #irotlvdusf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #irotlvdusf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #irotlvdusf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #irotlvdusf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| city | Temp. Range (°F) |
|------|------------------|
| NYC  | 28 to 35         |
| LA   | 55               |
| CHI  | 50               |
| HOU  | 45 to 60         |
