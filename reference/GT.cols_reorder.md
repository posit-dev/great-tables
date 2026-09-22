# GT.cols_reorder()


Reorder all columns in a specified order.


Usage

``` python
GT.cols_reorder(columns)
```


The [cols_reorder()](GT.cols_reorder.md#great_tables.GT.cols_reorder) method allows you to completely rearrange the column order of a table. Provide all column names in the exact order you want them to appear. This is useful when you need full control over the column layout and want to express the entire ordering in a single call, rather than using multiple [cols_move()](GT.cols_move.md#great_tables.GT.cols_move), [cols_move_to_start()](GT.cols_move_to_start.md#great_tables.GT.cols_move_to_start), or [cols_move_to_end()](GT.cols_move_to_end.md#great_tables.GT.cols_move_to_end) calls.

Every column in the table must appear exactly once in the `columns=` list. If any columns are missing or extra names are provided, a `ValueError` will be raised.


## Parameters


`columns: SelectExpr`  
A list of all column names in the desired display order. This can be a list of column name strings or a column selection expression (e.g., Polars selectors). All columns in the table must be included exactly once.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Raises


`ValueError`  
If the provided columns do not match all columns in the table (e.g., missing columns, extra columns, or duplicates).


## Examples

Let's use a subset of columns from the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a table.


``` python
from great_tables import GT
from great_tables.data import exibble

exibble_mini = exibble[["num", "char", "fctr", "date", "time"]]

GT(exibble_mini)
```


<style>
#abjbknbooc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#abjbknbooc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#abjbknbooc p { margin: 0; padding: 0; }
 #abjbknbooc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #abjbknbooc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #abjbknbooc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #abjbknbooc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #abjbknbooc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #abjbknbooc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #abjbknbooc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #abjbknbooc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #abjbknbooc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #abjbknbooc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #abjbknbooc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #abjbknbooc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #abjbknbooc .gt_spanner_row { border-bottom-style: hidden; }
 #abjbknbooc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #abjbknbooc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #abjbknbooc .gt_from_md> :first-child { margin-top: 0; }
 #abjbknbooc .gt_from_md> :last-child { margin-bottom: 0; }
 #abjbknbooc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #abjbknbooc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #abjbknbooc .gt_indent_1 { text-indent: 5px; }
 #abjbknbooc .gt_indent_2 { text-indent: calc(5px * 2); }
 #abjbknbooc .gt_indent_3 { text-indent: calc(5px * 3); }
 #abjbknbooc .gt_indent_4 { text-indent: calc(5px * 4); }
 #abjbknbooc .gt_indent_5 { text-indent: calc(5px * 5); }
 #abjbknbooc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #abjbknbooc .gt_row_group_first td { border-top-width: 2px; }
 #abjbknbooc .gt_row_group_first th { border-top-width: 2px; }
 #abjbknbooc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #abjbknbooc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #abjbknbooc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #abjbknbooc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #abjbknbooc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #abjbknbooc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #abjbknbooc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #abjbknbooc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #abjbknbooc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #abjbknbooc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #abjbknbooc .gt_left { text-align: left; }
 #abjbknbooc .gt_center { text-align: center; }
 #abjbknbooc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #abjbknbooc .gt_font_normal { font-weight: normal; }
 #abjbknbooc .gt_font_bold { font-weight: bold; }
 #abjbknbooc .gt_font_italic { font-style: italic; }
 #abjbknbooc .gt_super { font-size: 65%; }
 #abjbknbooc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #abjbknbooc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #abjbknbooc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #abjbknbooc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #abjbknbooc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #abjbknbooc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num       | char       | fctr  | date       | time  |
|-----------|------------|-------|------------|-------|
| 0.1111    | apricot    | one   | 2015-01-15 | 13:35 |
| 2.222     | banana     | two   | 2015-02-15 | 14:40 |
| 33.33     | coconut    | three | 2015-03-15 | 15:45 |
| 444.4     | durian     | four  | 2015-04-15 | 16:50 |
| 5550.0    | None       | five  | 2015-05-15 | 17:55 |
| None      | fig        | six   | 2015-06-15 | None  |
| 777000.0  | grapefruit | seven | None       | 19:10 |
| 8880000.0 | honeydew   | eight | 2015-08-15 | 20:20 |


Now, let's reorder the columns so that `fctr` and `date` come first, followed by the remaining columns in a custom order:


``` python
(
    GT(exibble_mini)
    .cols_reorder(["fctr", "date", "time", "char", "num"])
)
```


<style>
#jcvojxorkw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jcvojxorkw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jcvojxorkw p { margin: 0; padding: 0; }
 #jcvojxorkw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jcvojxorkw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jcvojxorkw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jcvojxorkw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jcvojxorkw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jcvojxorkw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jcvojxorkw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jcvojxorkw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jcvojxorkw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jcvojxorkw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jcvojxorkw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jcvojxorkw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jcvojxorkw .gt_spanner_row { border-bottom-style: hidden; }
 #jcvojxorkw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jcvojxorkw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jcvojxorkw .gt_from_md> :first-child { margin-top: 0; }
 #jcvojxorkw .gt_from_md> :last-child { margin-bottom: 0; }
 #jcvojxorkw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jcvojxorkw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jcvojxorkw .gt_indent_1 { text-indent: 5px; }
 #jcvojxorkw .gt_indent_2 { text-indent: calc(5px * 2); }
 #jcvojxorkw .gt_indent_3 { text-indent: calc(5px * 3); }
 #jcvojxorkw .gt_indent_4 { text-indent: calc(5px * 4); }
 #jcvojxorkw .gt_indent_5 { text-indent: calc(5px * 5); }
 #jcvojxorkw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jcvojxorkw .gt_row_group_first td { border-top-width: 2px; }
 #jcvojxorkw .gt_row_group_first th { border-top-width: 2px; }
 #jcvojxorkw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jcvojxorkw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jcvojxorkw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jcvojxorkw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jcvojxorkw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jcvojxorkw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jcvojxorkw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jcvojxorkw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jcvojxorkw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jcvojxorkw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jcvojxorkw .gt_left { text-align: left; }
 #jcvojxorkw .gt_center { text-align: center; }
 #jcvojxorkw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jcvojxorkw .gt_font_normal { font-weight: normal; }
 #jcvojxorkw .gt_font_bold { font-weight: bold; }
 #jcvojxorkw .gt_font_italic { font-style: italic; }
 #jcvojxorkw .gt_super { font-size: 65%; }
 #jcvojxorkw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jcvojxorkw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jcvojxorkw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jcvojxorkw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jcvojxorkw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jcvojxorkw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| fctr  | date       | time  | char       | num       |
|-------|------------|-------|------------|-----------|
| one   | 2015-01-15 | 13:35 | apricot    | 0.1111    |
| two   | 2015-02-15 | 14:40 | banana     | 2.222     |
| three | 2015-03-15 | 15:45 | coconut    | 33.33     |
| four  | 2015-04-15 | 16:50 | durian     | 444.4     |
| five  | 2015-05-15 | 17:55 | None       | 5550.0    |
| six   | 2015-06-15 | None  | fig        | None      |
| seven | None       | 19:10 | grapefruit | 777000.0  |
| eight | 2015-08-15 | 20:20 | honeydew   | 8880000.0 |


For tables with many columns, you can use Python's iterable unpacking to build the column list programmatically. Here we use the full [exibble](data.exibble.md#great_tables.data.exibble) dataset (9 columns) and move `fctr` to the front while pushing `num` and `char` to the end--without typing every column name in between:


``` python
# Unpack the first three column names and capture all remaining ones in `rest`
# exibble.columns is: ["num", "char", "fctr", "date", "time", "datetime", "currency", "row", "group"]
num, char, fctr, *rest = exibble.columns

# Build the new order: fctr first, then all middle columns in their
# original order, and finally char and num moved to the end
(
    GT(exibble)
    .cols_reorder([fctr, *rest, char, num])
)
```


<style>
#pqehtdrujz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pqehtdrujz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pqehtdrujz p { margin: 0; padding: 0; }
 #pqehtdrujz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pqehtdrujz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pqehtdrujz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pqehtdrujz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pqehtdrujz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pqehtdrujz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pqehtdrujz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pqehtdrujz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pqehtdrujz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pqehtdrujz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pqehtdrujz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pqehtdrujz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pqehtdrujz .gt_spanner_row { border-bottom-style: hidden; }
 #pqehtdrujz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pqehtdrujz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pqehtdrujz .gt_from_md> :first-child { margin-top: 0; }
 #pqehtdrujz .gt_from_md> :last-child { margin-bottom: 0; }
 #pqehtdrujz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pqehtdrujz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pqehtdrujz .gt_indent_1 { text-indent: 5px; }
 #pqehtdrujz .gt_indent_2 { text-indent: calc(5px * 2); }
 #pqehtdrujz .gt_indent_3 { text-indent: calc(5px * 3); }
 #pqehtdrujz .gt_indent_4 { text-indent: calc(5px * 4); }
 #pqehtdrujz .gt_indent_5 { text-indent: calc(5px * 5); }
 #pqehtdrujz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pqehtdrujz .gt_row_group_first td { border-top-width: 2px; }
 #pqehtdrujz .gt_row_group_first th { border-top-width: 2px; }
 #pqehtdrujz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pqehtdrujz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pqehtdrujz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pqehtdrujz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pqehtdrujz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pqehtdrujz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pqehtdrujz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pqehtdrujz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pqehtdrujz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pqehtdrujz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pqehtdrujz .gt_left { text-align: left; }
 #pqehtdrujz .gt_center { text-align: center; }
 #pqehtdrujz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pqehtdrujz .gt_font_normal { font-weight: normal; }
 #pqehtdrujz .gt_font_bold { font-weight: bold; }
 #pqehtdrujz .gt_font_italic { font-style: italic; }
 #pqehtdrujz .gt_super { font-size: 65%; }
 #pqehtdrujz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pqehtdrujz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pqehtdrujz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pqehtdrujz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pqehtdrujz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pqehtdrujz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| fctr | date | time | datetime | currency | row | group | char | num |
|----|----|----|----|----|----|----|----|----|
| one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a | apricot | 0.1111 |
| two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a | banana | 2.222 |
| three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a | coconut | 33.33 |
| four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a | durian | 444.4 |
| five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b | None | 5550.0 |
| six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | row_6 | grp_b | fig | None |
| seven | None | 19:10 | 2018-07-07 05:22 | None | row_7 | grp_b | grapefruit | 777000.0 |
| eight | 2015-08-15 | 20:20 | None | 0.44 | row_8 | grp_b | honeydew | 8880000.0 |


This unpacking technique is especially handy for wide tables where you want to pin a few columns to the start or end without manually listing every column in between. The `*rest` variable automatically adapts if columns are added to or removed from the dataset, making your table code more resilient to upstream schema changes.
