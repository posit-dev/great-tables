# GT.cols_merge_uncert()


Merge columns to a value-with-uncertainty column.


Usage

``` python
GT.cols_merge_uncert(
    col_val,
    col_uncert,
    rows=None,
    sep=" +/- ",
    autohide=True,
)
```


[cols_merge_uncert()](GT.cols_merge_uncert.md#great_tables.GT.cols_merge_uncert) is a specialized variant of [cols_merge()](GT.cols_merge.md#great_tables.GT.cols_merge). It takes as input a base value column (`col_val`) and either: (1) a single uncertainty column, or (2) two columns representing lower and upper uncertainty bounds. These columns will be essentially merged into a single column (that of `col_val`). What results is a column with values and associated uncertainties, and any columns specified in `col_uncert` are hidden from appearing in the output table.


## Parameters


`col_val: SelectExpr`  
The column that contains values for the base measurement. While column selection expressions can be used, it's recommended that a single column name be used to ensure that exactly one column is provided here.

`col_uncert: SelectExpr`  
The column or columns that contain uncertainty values. The most common case involves supplying a single column with uncertainties; these values will be combined with those in `col_val`. Less commonly, the lower and upper uncertainty bounds may be different. For that case, two columns representing the lower and upper uncertainty values away from `col_val`, respectively, should be provided as a list.

`rows: int | list[int] | None = None`  
In conjunction with `col_val`, we can specify which rows should participate in the merging process. The default is all rows. Alternatively, we can supply a list of row indices.

`sep: str = ``" +/- "`  
The separator text that contains the uncertainty mark for a single uncertainty value. The default value of `" +/- "` indicates that an appropriate plus/minus mark will be used depending on the output context. The plus/minus symbol (±) is used in HTML output.

`autohide: bool = ``True`  
An option to automatically hide any columns specified in `col_uncert`. Any columns with their state changed to hidden will behave the same as before, they just won't be displayed in the finalized table. Defaults to `True`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Details


### Specialized NA handling

This function employs specialized semantics for missing value handling that differ from the generic [cols_merge()](GT.cols_merge.md#great_tables.GT.cols_merge):

1.  Missing values in `col_val` result in missing values for the merged column (e.g., `NA` + `0.1` = `NA`)
2.  Missing values in `col_uncert` (but not `col_val`) result in base values only for the merged column (e.g., `12.0` + `NA` = `12.0`)
3.  Missing values in both `col_val` and `col_uncert` result in missing values for the merged column (e.g., `NA` + `NA` = `NA`)


## Examples

Use the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a simple, two-column table. Merge the `currency` and `num` columns together as a value with uncertainty.


``` python
from great_tables import GT
from great_tables.data import exibble
import polars as pl

exibble_mini = (
    pl.from_pandas(exibble)
    .select("num", "currency")
    .slice(0, 7)
)

(
    GT(exibble_mini)
    .fmt_number(columns="num", decimals=3, use_seps=False)
    .cols_merge_uncert(col_val="currency", col_uncert="num")
    .cols_label(currency="value + uncert.")
)
```


<style>
#casskmtoxv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#casskmtoxv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#casskmtoxv p { margin: 0; padding: 0; }
 #casskmtoxv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #casskmtoxv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #casskmtoxv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #casskmtoxv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #casskmtoxv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #casskmtoxv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #casskmtoxv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #casskmtoxv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #casskmtoxv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #casskmtoxv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #casskmtoxv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #casskmtoxv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #casskmtoxv .gt_spanner_row { border-bottom-style: hidden; }
 #casskmtoxv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #casskmtoxv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #casskmtoxv .gt_from_md> :first-child { margin-top: 0; }
 #casskmtoxv .gt_from_md> :last-child { margin-bottom: 0; }
 #casskmtoxv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #casskmtoxv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #casskmtoxv .gt_indent_1 { text-indent: 5px; }
 #casskmtoxv .gt_indent_2 { text-indent: calc(5px * 2); }
 #casskmtoxv .gt_indent_3 { text-indent: calc(5px * 3); }
 #casskmtoxv .gt_indent_4 { text-indent: calc(5px * 4); }
 #casskmtoxv .gt_indent_5 { text-indent: calc(5px * 5); }
 #casskmtoxv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #casskmtoxv .gt_row_group_first td { border-top-width: 2px; }
 #casskmtoxv .gt_row_group_first th { border-top-width: 2px; }
 #casskmtoxv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #casskmtoxv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #casskmtoxv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #casskmtoxv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #casskmtoxv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #casskmtoxv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #casskmtoxv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #casskmtoxv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #casskmtoxv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #casskmtoxv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #casskmtoxv .gt_left { text-align: left; }
 #casskmtoxv .gt_center { text-align: center; }
 #casskmtoxv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #casskmtoxv .gt_font_normal { font-weight: normal; }
 #casskmtoxv .gt_font_bold { font-weight: bold; }
 #casskmtoxv .gt_font_italic { font-style: italic; }
 #casskmtoxv .gt_super { font-size: 65%; }
 #casskmtoxv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #casskmtoxv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #casskmtoxv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #casskmtoxv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #casskmtoxv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #casskmtoxv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| value + uncert.    |
|--------------------|
| 49.95 ± 0.111      |
| 17.95 ± 2.222      |
| 1.39 ± 33.330      |
| 65100.0 ± 444.400  |
| 1325.81 ± 5550.000 |
| 13.255             |
|                    |


When there are missing values in the uncertainty column, the merged result shows only the base value. When the base value itself is missing, the entire merged cell is empty.


``` python
df = pl.DataFrame({
    "measurement": [12.5, 8.3, 15.0, 9.7],
    "error": [0.2, None, 0.5, None],
})

(
    GT(df)
    .fmt_number(columns="error", decimals=2)
    .cols_merge_uncert(col_val="measurement", col_uncert="error")
    .cols_label(measurement="Measurement")
)
```


<style>
#eiymxndyfa table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eiymxndyfa thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eiymxndyfa p { margin: 0; padding: 0; }
 #eiymxndyfa .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eiymxndyfa .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eiymxndyfa .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eiymxndyfa .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eiymxndyfa .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eiymxndyfa .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eiymxndyfa .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eiymxndyfa .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eiymxndyfa .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eiymxndyfa .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eiymxndyfa .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eiymxndyfa .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eiymxndyfa .gt_spanner_row { border-bottom-style: hidden; }
 #eiymxndyfa .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eiymxndyfa .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eiymxndyfa .gt_from_md> :first-child { margin-top: 0; }
 #eiymxndyfa .gt_from_md> :last-child { margin-bottom: 0; }
 #eiymxndyfa .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eiymxndyfa .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eiymxndyfa .gt_indent_1 { text-indent: 5px; }
 #eiymxndyfa .gt_indent_2 { text-indent: calc(5px * 2); }
 #eiymxndyfa .gt_indent_3 { text-indent: calc(5px * 3); }
 #eiymxndyfa .gt_indent_4 { text-indent: calc(5px * 4); }
 #eiymxndyfa .gt_indent_5 { text-indent: calc(5px * 5); }
 #eiymxndyfa .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eiymxndyfa .gt_row_group_first td { border-top-width: 2px; }
 #eiymxndyfa .gt_row_group_first th { border-top-width: 2px; }
 #eiymxndyfa .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eiymxndyfa .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eiymxndyfa .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eiymxndyfa .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eiymxndyfa .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eiymxndyfa .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eiymxndyfa .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eiymxndyfa .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eiymxndyfa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eiymxndyfa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eiymxndyfa .gt_left { text-align: left; }
 #eiymxndyfa .gt_center { text-align: center; }
 #eiymxndyfa .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eiymxndyfa .gt_font_normal { font-weight: normal; }
 #eiymxndyfa .gt_font_bold { font-weight: bold; }
 #eiymxndyfa .gt_font_italic { font-style: italic; }
 #eiymxndyfa .gt_super { font-size: 65%; }
 #eiymxndyfa .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eiymxndyfa .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eiymxndyfa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eiymxndyfa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eiymxndyfa .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eiymxndyfa .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Measurement |
|-------------|
| 12.5 ± 0.20 |
| 8.3         |
| 15.0 ± 0.50 |
| 9.7         |
