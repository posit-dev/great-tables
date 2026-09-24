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
#bpdhgagfqa table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bpdhgagfqa thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bpdhgagfqa p { margin: 0; padding: 0; }
 #bpdhgagfqa .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bpdhgagfqa .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bpdhgagfqa .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bpdhgagfqa .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bpdhgagfqa .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bpdhgagfqa .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpdhgagfqa .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bpdhgagfqa .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bpdhgagfqa .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bpdhgagfqa .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bpdhgagfqa .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bpdhgagfqa .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bpdhgagfqa .gt_spanner_row { border-bottom-style: hidden; }
 #bpdhgagfqa .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bpdhgagfqa .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bpdhgagfqa .gt_from_md> :first-child { margin-top: 0; }
 #bpdhgagfqa .gt_from_md> :last-child { margin-bottom: 0; }
 #bpdhgagfqa .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bpdhgagfqa .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bpdhgagfqa .gt_indent_1 { text-indent: 5px; }
 #bpdhgagfqa .gt_indent_2 { text-indent: calc(5px * 2); }
 #bpdhgagfqa .gt_indent_3 { text-indent: calc(5px * 3); }
 #bpdhgagfqa .gt_indent_4 { text-indent: calc(5px * 4); }
 #bpdhgagfqa .gt_indent_5 { text-indent: calc(5px * 5); }
 #bpdhgagfqa .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bpdhgagfqa .gt_row_group_first td { border-top-width: 2px; }
 #bpdhgagfqa .gt_row_group_first th { border-top-width: 2px; }
 #bpdhgagfqa .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bpdhgagfqa .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpdhgagfqa .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bpdhgagfqa .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bpdhgagfqa .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpdhgagfqa .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bpdhgagfqa .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bpdhgagfqa .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bpdhgagfqa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpdhgagfqa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bpdhgagfqa .gt_left { text-align: left; }
 #bpdhgagfqa .gt_center { text-align: center; }
 #bpdhgagfqa .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bpdhgagfqa .gt_font_normal { font-weight: normal; }
 #bpdhgagfqa .gt_font_bold { font-weight: bold; }
 #bpdhgagfqa .gt_font_italic { font-style: italic; }
 #bpdhgagfqa .gt_super { font-size: 65%; }
 #bpdhgagfqa .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpdhgagfqa .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bpdhgagfqa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpdhgagfqa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bpdhgagfqa .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bpdhgagfqa .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#npmugkjvwx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#npmugkjvwx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#npmugkjvwx p { margin: 0; padding: 0; }
 #npmugkjvwx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #npmugkjvwx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #npmugkjvwx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #npmugkjvwx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #npmugkjvwx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #npmugkjvwx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #npmugkjvwx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #npmugkjvwx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #npmugkjvwx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #npmugkjvwx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #npmugkjvwx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #npmugkjvwx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #npmugkjvwx .gt_spanner_row { border-bottom-style: hidden; }
 #npmugkjvwx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #npmugkjvwx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #npmugkjvwx .gt_from_md> :first-child { margin-top: 0; }
 #npmugkjvwx .gt_from_md> :last-child { margin-bottom: 0; }
 #npmugkjvwx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #npmugkjvwx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #npmugkjvwx .gt_indent_1 { text-indent: 5px; }
 #npmugkjvwx .gt_indent_2 { text-indent: calc(5px * 2); }
 #npmugkjvwx .gt_indent_3 { text-indent: calc(5px * 3); }
 #npmugkjvwx .gt_indent_4 { text-indent: calc(5px * 4); }
 #npmugkjvwx .gt_indent_5 { text-indent: calc(5px * 5); }
 #npmugkjvwx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #npmugkjvwx .gt_row_group_first td { border-top-width: 2px; }
 #npmugkjvwx .gt_row_group_first th { border-top-width: 2px; }
 #npmugkjvwx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #npmugkjvwx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #npmugkjvwx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #npmugkjvwx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #npmugkjvwx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #npmugkjvwx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #npmugkjvwx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #npmugkjvwx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #npmugkjvwx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #npmugkjvwx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #npmugkjvwx .gt_left { text-align: left; }
 #npmugkjvwx .gt_center { text-align: center; }
 #npmugkjvwx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #npmugkjvwx .gt_font_normal { font-weight: normal; }
 #npmugkjvwx .gt_font_bold { font-weight: bold; }
 #npmugkjvwx .gt_font_italic { font-style: italic; }
 #npmugkjvwx .gt_super { font-size: 65%; }
 #npmugkjvwx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #npmugkjvwx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #npmugkjvwx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #npmugkjvwx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #npmugkjvwx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #npmugkjvwx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#almwslkpcp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#almwslkpcp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#almwslkpcp p { margin: 0; padding: 0; }
 #almwslkpcp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #almwslkpcp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #almwslkpcp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #almwslkpcp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #almwslkpcp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #almwslkpcp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #almwslkpcp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #almwslkpcp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #almwslkpcp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #almwslkpcp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #almwslkpcp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #almwslkpcp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #almwslkpcp .gt_spanner_row { border-bottom-style: hidden; }
 #almwslkpcp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #almwslkpcp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #almwslkpcp .gt_from_md> :first-child { margin-top: 0; }
 #almwslkpcp .gt_from_md> :last-child { margin-bottom: 0; }
 #almwslkpcp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #almwslkpcp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #almwslkpcp .gt_indent_1 { text-indent: 5px; }
 #almwslkpcp .gt_indent_2 { text-indent: calc(5px * 2); }
 #almwslkpcp .gt_indent_3 { text-indent: calc(5px * 3); }
 #almwslkpcp .gt_indent_4 { text-indent: calc(5px * 4); }
 #almwslkpcp .gt_indent_5 { text-indent: calc(5px * 5); }
 #almwslkpcp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #almwslkpcp .gt_row_group_first td { border-top-width: 2px; }
 #almwslkpcp .gt_row_group_first th { border-top-width: 2px; }
 #almwslkpcp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #almwslkpcp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #almwslkpcp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #almwslkpcp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #almwslkpcp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #almwslkpcp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #almwslkpcp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #almwslkpcp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #almwslkpcp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #almwslkpcp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #almwslkpcp .gt_left { text-align: left; }
 #almwslkpcp .gt_center { text-align: center; }
 #almwslkpcp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #almwslkpcp .gt_font_normal { font-weight: normal; }
 #almwslkpcp .gt_font_bold { font-weight: bold; }
 #almwslkpcp .gt_font_italic { font-style: italic; }
 #almwslkpcp .gt_super { font-size: 65%; }
 #almwslkpcp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #almwslkpcp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #almwslkpcp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #almwslkpcp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #almwslkpcp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #almwslkpcp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| **date**   | open      | high      | low     | close     | volume       | **adj_close** |
|------------|-----------|-----------|---------|-----------|--------------|---------------|
| 2015-12-31 | 2060.5901 | 2062.54   | 2043.62 | 2043.9399 | 2655330000.0 | 2043.9399     |
| 2015-12-30 | 2077.3401 | 2077.3401 | 2061.97 | 2063.3601 | 2367430000.0 | 2063.3601     |
| 2015-12-29 | 2060.54   | 2081.5601 | 2060.54 | 2078.3601 | 2542000000.0 | 2078.3601     |
| 2015-12-28 | 2057.77   | 2057.77   | 2044.2  | 2056.5    | 2492510000.0 | 2056.5        |
| 2015-12-24 | 2063.52   | 2067.3601 | 2058.73 | 2060.99   | 1411860000.0 | 2060.99       |
