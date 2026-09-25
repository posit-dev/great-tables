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
#rkzwtdwrpk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rkzwtdwrpk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rkzwtdwrpk p { margin: 0; padding: 0; }
 #rkzwtdwrpk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rkzwtdwrpk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rkzwtdwrpk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rkzwtdwrpk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rkzwtdwrpk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rkzwtdwrpk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rkzwtdwrpk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rkzwtdwrpk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rkzwtdwrpk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rkzwtdwrpk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rkzwtdwrpk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rkzwtdwrpk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rkzwtdwrpk .gt_spanner_row { border-bottom-style: hidden; }
 #rkzwtdwrpk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rkzwtdwrpk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rkzwtdwrpk .gt_from_md> :first-child { margin-top: 0; }
 #rkzwtdwrpk .gt_from_md> :last-child { margin-bottom: 0; }
 #rkzwtdwrpk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rkzwtdwrpk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rkzwtdwrpk .gt_indent_1 { text-indent: 5px; }
 #rkzwtdwrpk .gt_indent_2 { text-indent: calc(5px * 2); }
 #rkzwtdwrpk .gt_indent_3 { text-indent: calc(5px * 3); }
 #rkzwtdwrpk .gt_indent_4 { text-indent: calc(5px * 4); }
 #rkzwtdwrpk .gt_indent_5 { text-indent: calc(5px * 5); }
 #rkzwtdwrpk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rkzwtdwrpk .gt_row_group_first td { border-top-width: 2px; }
 #rkzwtdwrpk .gt_row_group_first th { border-top-width: 2px; }
 #rkzwtdwrpk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rkzwtdwrpk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rkzwtdwrpk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rkzwtdwrpk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rkzwtdwrpk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rkzwtdwrpk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rkzwtdwrpk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rkzwtdwrpk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rkzwtdwrpk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rkzwtdwrpk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rkzwtdwrpk .gt_left { text-align: left; }
 #rkzwtdwrpk .gt_center { text-align: center; }
 #rkzwtdwrpk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rkzwtdwrpk .gt_font_normal { font-weight: normal; }
 #rkzwtdwrpk .gt_font_bold { font-weight: bold; }
 #rkzwtdwrpk .gt_font_italic { font-style: italic; }
 #rkzwtdwrpk .gt_super { font-size: 65%; }
 #rkzwtdwrpk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rkzwtdwrpk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rkzwtdwrpk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rkzwtdwrpk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rkzwtdwrpk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rkzwtdwrpk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#engtehcnse table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#engtehcnse thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#engtehcnse p { margin: 0; padding: 0; }
 #engtehcnse .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #engtehcnse .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #engtehcnse .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #engtehcnse .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #engtehcnse .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #engtehcnse .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #engtehcnse .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #engtehcnse .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #engtehcnse .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #engtehcnse .gt_column_spanner_outer:first-child { padding-left: 0; }
 #engtehcnse .gt_column_spanner_outer:last-child { padding-right: 0; }
 #engtehcnse .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #engtehcnse .gt_spanner_row { border-bottom-style: hidden; }
 #engtehcnse .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #engtehcnse .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #engtehcnse .gt_from_md> :first-child { margin-top: 0; }
 #engtehcnse .gt_from_md> :last-child { margin-bottom: 0; }
 #engtehcnse .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #engtehcnse .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #engtehcnse .gt_indent_1 { text-indent: 5px; }
 #engtehcnse .gt_indent_2 { text-indent: calc(5px * 2); }
 #engtehcnse .gt_indent_3 { text-indent: calc(5px * 3); }
 #engtehcnse .gt_indent_4 { text-indent: calc(5px * 4); }
 #engtehcnse .gt_indent_5 { text-indent: calc(5px * 5); }
 #engtehcnse .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #engtehcnse .gt_row_group_first td { border-top-width: 2px; }
 #engtehcnse .gt_row_group_first th { border-top-width: 2px; }
 #engtehcnse .gt_striped { color: #333333; background-color: #F4F4F4; }
 #engtehcnse .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #engtehcnse .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #engtehcnse .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #engtehcnse .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #engtehcnse .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #engtehcnse .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #engtehcnse .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #engtehcnse .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #engtehcnse .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #engtehcnse .gt_left { text-align: left; }
 #engtehcnse .gt_center { text-align: center; }
 #engtehcnse .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #engtehcnse .gt_font_normal { font-weight: normal; }
 #engtehcnse .gt_font_bold { font-weight: bold; }
 #engtehcnse .gt_font_italic { font-style: italic; }
 #engtehcnse .gt_super { font-size: 65%; }
 #engtehcnse .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #engtehcnse .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #engtehcnse .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #engtehcnse .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #engtehcnse .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #engtehcnse .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Measurement |
|-------------|
| 12.5 ± 0.20 |
| 8.3         |
| 15.0 ± 0.50 |
| 9.7         |
