# GT.cols_align_decimal()


Align all numeric values in a column along the decimal mark.


Usage

``` python
GT.cols_align_decimal(
    columns=None,
    dec_mark=".",
    locale=None,
)
```


For numeric columns that contain values with more than one decimal place, it can be helpful to align them on the decimal mark so they are easier to scan and compare. The [cols_align_decimal()](GT.cols_align_decimal.md#great_tables.GT.cols_align_decimal) method does this by padding the formatted values with figure spaces (which are as wide as a digit) so that the decimal marks line up, and right-aligning the columns. This happens after formatting, so it works with values formatted by the `fmt_*()` methods, including ones with a `%` or other suffix. Only numeric columns are aligned, any other columns that are targeted are left unchanged.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list. If `None`, all numeric columns are targeted.

`dec_mark: str = ``"."`  
The character used as the decimal mark in the formatted values. This is ignored if a `locale` is supplied.

`locale: str | None = None`  
An optional locale identifier that can be used to obtain the decimal mark. If not set, the locale set in `GT(locale=...)`, if any, is used.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's put some numbers with different numbers of decimal places in a table, format them with `fmt_number()` and align them on the decimal mark.


``` python
import polars as pl
from great_tables import GT

df = pl.DataFrame({"num": [1.2, -33.52, 9023.2, -283.527, None, 0.401, 41.0]})

(
    GT(df)
    .fmt_number(columns="num", decimals=3, drop_trailing_zeros=True)
    .cols_align_decimal()
)
```


<style>
#xyfgtczpbo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xyfgtczpbo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xyfgtczpbo p { margin: 0; padding: 0; }
 #xyfgtczpbo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xyfgtczpbo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xyfgtczpbo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xyfgtczpbo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xyfgtczpbo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xyfgtczpbo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xyfgtczpbo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xyfgtczpbo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xyfgtczpbo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xyfgtczpbo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xyfgtczpbo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xyfgtczpbo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xyfgtczpbo .gt_spanner_row { border-bottom-style: hidden; }
 #xyfgtczpbo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xyfgtczpbo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xyfgtczpbo .gt_from_md> :first-child { margin-top: 0; }
 #xyfgtczpbo .gt_from_md> :last-child { margin-bottom: 0; }
 #xyfgtczpbo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xyfgtczpbo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xyfgtczpbo .gt_indent_1 { text-indent: 5px; }
 #xyfgtczpbo .gt_indent_2 { text-indent: calc(5px * 2); }
 #xyfgtczpbo .gt_indent_3 { text-indent: calc(5px * 3); }
 #xyfgtczpbo .gt_indent_4 { text-indent: calc(5px * 4); }
 #xyfgtczpbo .gt_indent_5 { text-indent: calc(5px * 5); }
 #xyfgtczpbo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xyfgtczpbo .gt_row_group_first td { border-top-width: 2px; }
 #xyfgtczpbo .gt_row_group_first th { border-top-width: 2px; }
 #xyfgtczpbo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xyfgtczpbo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xyfgtczpbo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xyfgtczpbo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xyfgtczpbo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xyfgtczpbo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xyfgtczpbo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xyfgtczpbo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xyfgtczpbo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xyfgtczpbo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xyfgtczpbo .gt_left { text-align: left; }
 #xyfgtczpbo .gt_center { text-align: center; }
 #xyfgtczpbo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xyfgtczpbo .gt_font_normal { font-weight: normal; }
 #xyfgtczpbo .gt_font_bold { font-weight: bold; }
 #xyfgtczpbo .gt_font_italic { font-style: italic; }
 #xyfgtczpbo .gt_super { font-size: 65%; }
 #xyfgtczpbo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xyfgtczpbo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xyfgtczpbo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xyfgtczpbo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xyfgtczpbo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xyfgtczpbo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num       |
|-----------|
|     1.2   |
|   −33.52  |
| 9,023.2   |
|  −283.527 |
| None      |
|     0.401 |
|    41     |
