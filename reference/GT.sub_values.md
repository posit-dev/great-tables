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
    replacement=None,
)
```


Should you need to replace specific cell values with custom text, [sub_values()](GT.sub_values.md#great_tables.GT.sub_values) can be a good choice. We can target cells for replacement through value, regex, and custom matching rules.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should be targeted for substitution. The default is all rows, resulting in all rows in all targeted columns being considered for this substitution. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

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
#bxtdwtcikg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bxtdwtcikg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bxtdwtcikg p { margin: 0; padding: 0; }
 #bxtdwtcikg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bxtdwtcikg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bxtdwtcikg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bxtdwtcikg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bxtdwtcikg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bxtdwtcikg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bxtdwtcikg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bxtdwtcikg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bxtdwtcikg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bxtdwtcikg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bxtdwtcikg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bxtdwtcikg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bxtdwtcikg .gt_spanner_row { border-bottom-style: hidden; }
 #bxtdwtcikg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bxtdwtcikg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bxtdwtcikg .gt_from_md> :first-child { margin-top: 0; }
 #bxtdwtcikg .gt_from_md> :last-child { margin-bottom: 0; }
 #bxtdwtcikg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bxtdwtcikg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bxtdwtcikg .gt_indent_1 { text-indent: 5px; }
 #bxtdwtcikg .gt_indent_2 { text-indent: calc(5px * 2); }
 #bxtdwtcikg .gt_indent_3 { text-indent: calc(5px * 3); }
 #bxtdwtcikg .gt_indent_4 { text-indent: calc(5px * 4); }
 #bxtdwtcikg .gt_indent_5 { text-indent: calc(5px * 5); }
 #bxtdwtcikg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bxtdwtcikg .gt_row_group_first td { border-top-width: 2px; }
 #bxtdwtcikg .gt_row_group_first th { border-top-width: 2px; }
 #bxtdwtcikg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bxtdwtcikg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bxtdwtcikg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bxtdwtcikg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bxtdwtcikg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bxtdwtcikg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bxtdwtcikg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bxtdwtcikg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bxtdwtcikg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bxtdwtcikg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bxtdwtcikg .gt_left { text-align: left; }
 #bxtdwtcikg .gt_center { text-align: center; }
 #bxtdwtcikg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bxtdwtcikg .gt_font_normal { font-weight: normal; }
 #bxtdwtcikg .gt_font_bold { font-weight: bold; }
 #bxtdwtcikg .gt_font_italic { font-style: italic; }
 #bxtdwtcikg .gt_super { font-size: 65%; }
 #bxtdwtcikg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bxtdwtcikg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bxtdwtcikg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bxtdwtcikg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bxtdwtcikg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bxtdwtcikg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#mrmgciexbr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mrmgciexbr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mrmgciexbr p { margin: 0; padding: 0; }
 #mrmgciexbr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mrmgciexbr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mrmgciexbr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mrmgciexbr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mrmgciexbr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mrmgciexbr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mrmgciexbr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mrmgciexbr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mrmgciexbr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mrmgciexbr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mrmgciexbr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mrmgciexbr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mrmgciexbr .gt_spanner_row { border-bottom-style: hidden; }
 #mrmgciexbr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mrmgciexbr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mrmgciexbr .gt_from_md> :first-child { margin-top: 0; }
 #mrmgciexbr .gt_from_md> :last-child { margin-bottom: 0; }
 #mrmgciexbr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mrmgciexbr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mrmgciexbr .gt_indent_1 { text-indent: 5px; }
 #mrmgciexbr .gt_indent_2 { text-indent: calc(5px * 2); }
 #mrmgciexbr .gt_indent_3 { text-indent: calc(5px * 3); }
 #mrmgciexbr .gt_indent_4 { text-indent: calc(5px * 4); }
 #mrmgciexbr .gt_indent_5 { text-indent: calc(5px * 5); }
 #mrmgciexbr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mrmgciexbr .gt_row_group_first td { border-top-width: 2px; }
 #mrmgciexbr .gt_row_group_first th { border-top-width: 2px; }
 #mrmgciexbr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mrmgciexbr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mrmgciexbr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mrmgciexbr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mrmgciexbr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mrmgciexbr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mrmgciexbr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mrmgciexbr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mrmgciexbr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mrmgciexbr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mrmgciexbr .gt_left { text-align: left; }
 #mrmgciexbr .gt_center { text-align: center; }
 #mrmgciexbr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mrmgciexbr .gt_font_normal { font-weight: normal; }
 #mrmgciexbr .gt_font_bold { font-weight: bold; }
 #mrmgciexbr .gt_font_italic { font-style: italic; }
 #mrmgciexbr .gt_super { font-size: 65%; }
 #mrmgciexbr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mrmgciexbr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mrmgciexbr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mrmgciexbr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mrmgciexbr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mrmgciexbr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
