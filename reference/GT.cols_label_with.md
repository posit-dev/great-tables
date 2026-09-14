# GT.cols_label_with()


Relabel one or more columns using a function.


Usage

``` python
GT.cols_label_with(
    columns=None,
    fn=None,
)
```


The [cols_label_with()](GT.cols_label_with.md#great_tables.GT.cols_label_with) function allows for modification of column labels through a supplied function. By default, the function will be invoked on all column labels but this can be limited to a subset via the `columns` parameter.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`fn: Callable[[str], str] | None = None`  
A function that accepts a column name as input and returns a label as output.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Notes

GT always selects columns using their name in the underlying data. This means that a column's label is purely for final presentation.


## Examples

Let's use a subset of the [sp500](data.sp500.md#great_tables.data.sp500) dataset to create a gt table.


``` python
from great_tables import GT, md
from great_tables.data import sp500

gt = GT(sp500.head())
gt
```


<style>
#asnjszpsib table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#asnjszpsib thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#asnjszpsib p { margin: 0; padding: 0; }
 #asnjszpsib .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #asnjszpsib .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #asnjszpsib .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #asnjszpsib .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #asnjszpsib .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #asnjszpsib .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #asnjszpsib .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #asnjszpsib .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #asnjszpsib .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #asnjszpsib .gt_column_spanner_outer:first-child { padding-left: 0; }
 #asnjszpsib .gt_column_spanner_outer:last-child { padding-right: 0; }
 #asnjszpsib .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #asnjszpsib .gt_spanner_row { border-bottom-style: hidden; }
 #asnjszpsib .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #asnjszpsib .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #asnjszpsib .gt_from_md> :first-child { margin-top: 0; }
 #asnjszpsib .gt_from_md> :last-child { margin-bottom: 0; }
 #asnjszpsib .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #asnjszpsib .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #asnjszpsib .gt_indent_1 { text-indent: 5px; }
 #asnjszpsib .gt_indent_2 { text-indent: calc(5px * 2); }
 #asnjszpsib .gt_indent_3 { text-indent: calc(5px * 3); }
 #asnjszpsib .gt_indent_4 { text-indent: calc(5px * 4); }
 #asnjszpsib .gt_indent_5 { text-indent: calc(5px * 5); }
 #asnjszpsib .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #asnjszpsib .gt_row_group_first td { border-top-width: 2px; }
 #asnjszpsib .gt_row_group_first th { border-top-width: 2px; }
 #asnjszpsib .gt_striped { color: #333333; background-color: #F4F4F4; }
 #asnjszpsib .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #asnjszpsib .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #asnjszpsib .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #asnjszpsib .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #asnjszpsib .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #asnjszpsib .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #asnjszpsib .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #asnjszpsib .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #asnjszpsib .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #asnjszpsib .gt_left { text-align: left; }
 #asnjszpsib .gt_center { text-align: center; }
 #asnjszpsib .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #asnjszpsib .gt_font_normal { font-weight: normal; }
 #asnjszpsib .gt_font_bold { font-weight: bold; }
 #asnjszpsib .gt_font_italic { font-style: italic; }
 #asnjszpsib .gt_super { font-size: 65%; }
 #asnjszpsib .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #asnjszpsib .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #asnjszpsib .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #asnjszpsib .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #asnjszpsib .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #asnjszpsib .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | open      | high      | low     | close     | volume       | adj_close |
|------------|-----------|-----------|---------|-----------|--------------|-----------|
| 2015-12-31 | 2060.5901 | 2062.54   | 2043.62 | 2043.9399 | 2655330000.0 | 2043.9399 |
| 2015-12-30 | 2077.3401 | 2077.3401 | 2061.97 | 2063.3601 | 2367430000.0 | 2063.3601 |
| 2015-12-29 | 2060.54   | 2081.5601 | 2060.54 | 2078.3601 | 2542000000.0 | 2078.3601 |
| 2015-12-28 | 2057.77   | 2057.77   | 2044.2  | 2056.5    | 2492510000.0 | 2056.5    |
| 2015-12-24 | 2063.52   | 2067.3601 | 2058.73 | 2060.99   | 1411860000.0 | 2060.99   |


We can pass `str.upper` to the `fn` parameter to convert all column labels to uppercase.


``` python
gt.cols_label_with(fn=str.upper)
```


<style>
#etjuvcvqvq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#etjuvcvqvq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#etjuvcvqvq p { margin: 0; padding: 0; }
 #etjuvcvqvq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #etjuvcvqvq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #etjuvcvqvq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #etjuvcvqvq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #etjuvcvqvq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #etjuvcvqvq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #etjuvcvqvq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #etjuvcvqvq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #etjuvcvqvq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #etjuvcvqvq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #etjuvcvqvq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #etjuvcvqvq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #etjuvcvqvq .gt_spanner_row { border-bottom-style: hidden; }
 #etjuvcvqvq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #etjuvcvqvq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #etjuvcvqvq .gt_from_md> :first-child { margin-top: 0; }
 #etjuvcvqvq .gt_from_md> :last-child { margin-bottom: 0; }
 #etjuvcvqvq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #etjuvcvqvq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #etjuvcvqvq .gt_indent_1 { text-indent: 5px; }
 #etjuvcvqvq .gt_indent_2 { text-indent: calc(5px * 2); }
 #etjuvcvqvq .gt_indent_3 { text-indent: calc(5px * 3); }
 #etjuvcvqvq .gt_indent_4 { text-indent: calc(5px * 4); }
 #etjuvcvqvq .gt_indent_5 { text-indent: calc(5px * 5); }
 #etjuvcvqvq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #etjuvcvqvq .gt_row_group_first td { border-top-width: 2px; }
 #etjuvcvqvq .gt_row_group_first th { border-top-width: 2px; }
 #etjuvcvqvq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #etjuvcvqvq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #etjuvcvqvq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #etjuvcvqvq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #etjuvcvqvq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #etjuvcvqvq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #etjuvcvqvq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #etjuvcvqvq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #etjuvcvqvq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #etjuvcvqvq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #etjuvcvqvq .gt_left { text-align: left; }
 #etjuvcvqvq .gt_center { text-align: center; }
 #etjuvcvqvq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #etjuvcvqvq .gt_font_normal { font-weight: normal; }
 #etjuvcvqvq .gt_font_bold { font-weight: bold; }
 #etjuvcvqvq .gt_font_italic { font-style: italic; }
 #etjuvcvqvq .gt_super { font-size: 65%; }
 #etjuvcvqvq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #etjuvcvqvq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #etjuvcvqvq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #etjuvcvqvq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #etjuvcvqvq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #etjuvcvqvq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| DATE       | OPEN      | HIGH      | LOW     | CLOSE     | VOLUME       | ADJ_CLOSE |
|------------|-----------|-----------|---------|-----------|--------------|-----------|
| 2015-12-31 | 2060.5901 | 2062.54   | 2043.62 | 2043.9399 | 2655330000.0 | 2043.9399 |
| 2015-12-30 | 2077.3401 | 2077.3401 | 2061.97 | 2063.3601 | 2367430000.0 | 2063.3601 |
| 2015-12-29 | 2060.54   | 2081.5601 | 2060.54 | 2078.3601 | 2542000000.0 | 2078.3601 |
| 2015-12-28 | 2057.77   | 2057.77   | 2044.2  | 2056.5    | 2492510000.0 | 2056.5    |
| 2015-12-24 | 2063.52   | 2067.3601 | 2058.73 | 2060.99   | 1411860000.0 | 2060.99   |


One useful use case is using [md()](md.md#great_tables.md), provided by **Great Tables**, to format column labels. For example, the following code demonstrates how to make the `date` and `adj_close` column labels bold using markdown syntax.


``` python
gt.cols_label_with(["date", "adj_close"], lambda x: md(f"**{x}**"))
```


<style>
#wbrqwkaqnr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wbrqwkaqnr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wbrqwkaqnr p { margin: 0; padding: 0; }
 #wbrqwkaqnr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wbrqwkaqnr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wbrqwkaqnr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wbrqwkaqnr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wbrqwkaqnr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wbrqwkaqnr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wbrqwkaqnr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wbrqwkaqnr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wbrqwkaqnr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wbrqwkaqnr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wbrqwkaqnr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wbrqwkaqnr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wbrqwkaqnr .gt_spanner_row { border-bottom-style: hidden; }
 #wbrqwkaqnr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wbrqwkaqnr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wbrqwkaqnr .gt_from_md> :first-child { margin-top: 0; }
 #wbrqwkaqnr .gt_from_md> :last-child { margin-bottom: 0; }
 #wbrqwkaqnr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wbrqwkaqnr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wbrqwkaqnr .gt_indent_1 { text-indent: 5px; }
 #wbrqwkaqnr .gt_indent_2 { text-indent: calc(5px * 2); }
 #wbrqwkaqnr .gt_indent_3 { text-indent: calc(5px * 3); }
 #wbrqwkaqnr .gt_indent_4 { text-indent: calc(5px * 4); }
 #wbrqwkaqnr .gt_indent_5 { text-indent: calc(5px * 5); }
 #wbrqwkaqnr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wbrqwkaqnr .gt_row_group_first td { border-top-width: 2px; }
 #wbrqwkaqnr .gt_row_group_first th { border-top-width: 2px; }
 #wbrqwkaqnr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wbrqwkaqnr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wbrqwkaqnr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wbrqwkaqnr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wbrqwkaqnr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wbrqwkaqnr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wbrqwkaqnr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wbrqwkaqnr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wbrqwkaqnr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wbrqwkaqnr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wbrqwkaqnr .gt_left { text-align: left; }
 #wbrqwkaqnr .gt_center { text-align: center; }
 #wbrqwkaqnr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wbrqwkaqnr .gt_font_normal { font-weight: normal; }
 #wbrqwkaqnr .gt_font_bold { font-weight: bold; }
 #wbrqwkaqnr .gt_font_italic { font-style: italic; }
 #wbrqwkaqnr .gt_super { font-size: 65%; }
 #wbrqwkaqnr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wbrqwkaqnr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wbrqwkaqnr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wbrqwkaqnr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wbrqwkaqnr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wbrqwkaqnr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| **date**   | open      | high      | low     | close     | volume       | **adj_close** |
|------------|-----------|-----------|---------|-----------|--------------|---------------|
| 2015-12-31 | 2060.5901 | 2062.54   | 2043.62 | 2043.9399 | 2655330000.0 | 2043.9399     |
| 2015-12-30 | 2077.3401 | 2077.3401 | 2061.97 | 2063.3601 | 2367430000.0 | 2063.3601     |
| 2015-12-29 | 2060.54   | 2081.5601 | 2060.54 | 2078.3601 | 2542000000.0 | 2078.3601     |
| 2015-12-28 | 2057.77   | 2057.77   | 2044.2  | 2056.5    | 2492510000.0 | 2056.5        |
| 2015-12-24 | 2063.52   | 2067.3601 | 2058.73 | 2060.99   | 1411860000.0 | 2060.99       |
