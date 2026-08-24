# GT.sub_values()


Substitute targeted values in the table body.


Usage

``` python
GT.sub_values(
    columns=None,
    rows=None,
    values=None,
    pattern=None,
    fn=None,
    replacement=None
)
```


Should you need to replace specific cell values with custom text, [sub_values()](GT.sub_values.md#great_tables.GT.sub_values) can be a good choice. We can target cells for replacement through value, regex, and custom matching rules.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should be targeted for substitution. The default is all rows, resulting in all rows in all targeted columns being considered for this substitution. Alternatively, we can supply a list of row indices.

`values: list[Any] | Any | None = None`  
The specific value or values that should be replaced with a `replacement` value. If `pattern` is also supplied then `values` will be ignored.

`pattern: str | None = None`  
A regex pattern that can target solely those values in character-based columns. If `values` is also supplied, `pattern` will take precedence.

`fn: Callable[…, bool] | None = None`  
A supplied function that operates on each cell value `x` and should return a boolean indicating whether that value should be replaced. If either of `values` or `pattern` is also supplied, `fn` will take precedence.

`replacement: str | int | float | None = None`  
The replacement value for any cell values matched by either `values`, `pattern`, or `fn`. Must be a string or numeric value.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's create an input table with three columns containing an assortment of values that could potentially undergo some substitution via [sub_values()](GT.sub_values.md#great_tables.GT.sub_values).


``` python
from great_tables import GT
import polars as pl

tbl = pl.DataFrame(
    {
        "num_1": [-0.01, 74.0, None, 0.0, 500.0, 0.001, 84.3],
        "int_1": [1, -100000, 800, 5, None, 1, -32],
        "lett": ["A", "B", "C", "D", "E", "F", "G"],
    }
)

GT(tbl).sub_values(values=[74, 500], replacement="--")
```


<style>
#bmdbnhgayj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bmdbnhgayj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bmdbnhgayj p { margin: 0; padding: 0; }
 #bmdbnhgayj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bmdbnhgayj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bmdbnhgayj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bmdbnhgayj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bmdbnhgayj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bmdbnhgayj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bmdbnhgayj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bmdbnhgayj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bmdbnhgayj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bmdbnhgayj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bmdbnhgayj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bmdbnhgayj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bmdbnhgayj .gt_spanner_row { border-bottom-style: hidden; }
 #bmdbnhgayj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bmdbnhgayj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bmdbnhgayj .gt_from_md> :first-child { margin-top: 0; }
 #bmdbnhgayj .gt_from_md> :last-child { margin-bottom: 0; }
 #bmdbnhgayj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bmdbnhgayj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bmdbnhgayj .gt_indent_1 { text-indent: 5px; }
 #bmdbnhgayj .gt_indent_2 { text-indent: calc(5px * 2); }
 #bmdbnhgayj .gt_indent_3 { text-indent: calc(5px * 3); }
 #bmdbnhgayj .gt_indent_4 { text-indent: calc(5px * 4); }
 #bmdbnhgayj .gt_indent_5 { text-indent: calc(5px * 5); }
 #bmdbnhgayj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bmdbnhgayj .gt_row_group_first td { border-top-width: 2px; }
 #bmdbnhgayj .gt_row_group_first th { border-top-width: 2px; }
 #bmdbnhgayj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bmdbnhgayj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bmdbnhgayj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bmdbnhgayj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bmdbnhgayj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bmdbnhgayj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bmdbnhgayj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bmdbnhgayj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bmdbnhgayj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bmdbnhgayj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bmdbnhgayj .gt_left { text-align: left; }
 #bmdbnhgayj .gt_center { text-align: center; }
 #bmdbnhgayj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bmdbnhgayj .gt_font_normal { font-weight: normal; }
 #bmdbnhgayj .gt_font_bold { font-weight: bold; }
 #bmdbnhgayj .gt_font_italic { font-style: italic; }
 #bmdbnhgayj .gt_super { font-size: 65%; }
 #bmdbnhgayj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bmdbnhgayj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bmdbnhgayj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bmdbnhgayj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bmdbnhgayj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bmdbnhgayj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num_1 | int_1   | lett |
|-------|---------|------|
| -0.01 | 1       | A    |
| --     | -100000 | B    |
| None  | 800     | C    |
| 0.0   | 5       | D    |
| --     | None    | E    |
| 0.001 | 1       | F    |
| 84.3  | -32     | G    |


For the most flexibility, use the `fn` argument. The function you provide should accept a cell value and return a boolean indicating whether it should be replaced.


``` python
from great_tables import GT
import polars as pl

tbl = pl.DataFrame(
    {
        "num_1": [-0.01, 74.0, None, 0.0, 500.0, 0.001, 84.3],
        "int_1": [1, -100000, 800, 5, None, 1, -32],
        "lett": ["A", "B", "C", "D", "E", "F", "G"],
    }
)

(
    GT(tbl)
    .sub_values(
        fn=lambda x: isinstance(x, (int, float)) and x >= 0 and x < 50,
        replacement="small"
    )
)
```


<style>
#hpmujsmmcw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hpmujsmmcw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hpmujsmmcw p { margin: 0; padding: 0; }
 #hpmujsmmcw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hpmujsmmcw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hpmujsmmcw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hpmujsmmcw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hpmujsmmcw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hpmujsmmcw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hpmujsmmcw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hpmujsmmcw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hpmujsmmcw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hpmujsmmcw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hpmujsmmcw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hpmujsmmcw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hpmujsmmcw .gt_spanner_row { border-bottom-style: hidden; }
 #hpmujsmmcw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hpmujsmmcw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hpmujsmmcw .gt_from_md> :first-child { margin-top: 0; }
 #hpmujsmmcw .gt_from_md> :last-child { margin-bottom: 0; }
 #hpmujsmmcw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hpmujsmmcw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hpmujsmmcw .gt_indent_1 { text-indent: 5px; }
 #hpmujsmmcw .gt_indent_2 { text-indent: calc(5px * 2); }
 #hpmujsmmcw .gt_indent_3 { text-indent: calc(5px * 3); }
 #hpmujsmmcw .gt_indent_4 { text-indent: calc(5px * 4); }
 #hpmujsmmcw .gt_indent_5 { text-indent: calc(5px * 5); }
 #hpmujsmmcw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hpmujsmmcw .gt_row_group_first td { border-top-width: 2px; }
 #hpmujsmmcw .gt_row_group_first th { border-top-width: 2px; }
 #hpmujsmmcw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hpmujsmmcw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hpmujsmmcw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hpmujsmmcw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hpmujsmmcw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hpmujsmmcw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hpmujsmmcw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hpmujsmmcw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hpmujsmmcw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hpmujsmmcw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hpmujsmmcw .gt_left { text-align: left; }
 #hpmujsmmcw .gt_center { text-align: center; }
 #hpmujsmmcw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hpmujsmmcw .gt_font_normal { font-weight: normal; }
 #hpmujsmmcw .gt_font_bold { font-weight: bold; }
 #hpmujsmmcw .gt_font_italic { font-style: italic; }
 #hpmujsmmcw .gt_super { font-size: 65%; }
 #hpmujsmmcw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hpmujsmmcw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hpmujsmmcw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hpmujsmmcw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hpmujsmmcw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hpmujsmmcw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num_1 | int_1   | lett |
|-------|---------|------|
| -0.01 | small   | A    |
| 74.0  | -100000 | B    |
| None  | 800     | C    |
| small | small   | D    |
| 500.0 | None    | E    |
| small | small   | F    |
| 84.3  | -32     | G    |
