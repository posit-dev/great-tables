# GT.cols_width()


Set the widths of columns.


Usage

``` python
GT.cols_width(
    cases=None,
    **kwargs,
)
```


Manual specifications of column widths can be performed using the [cols_width()](GT.cols_width.md#great_tables.GT.cols_width) method. We choose which columns get specific widths. This can be in units of pixels or as percentages. Width assignments are supplied inside of a dictionary where columns are the keys and the corresponding width is the value.


## Parameters


`cases: dict[str, str] | None = None`  
A dictionary where the keys are column names and the values are the widths. Widths can be specified in pixels (e.g., `"50px"`) or as percentages (e.g., `"20%"`). Use the `stub` sentinel as a key to set the width of the stub column without risk of collision with a data column named `"stub"`, or `stub(n)` to set one level of a hierarchical stub (counting from the right).

`**kwargs: str`  
Keyword arguments to specify column widths. Each keyword corresponds to a column name, with its value indicating the width in pixels or percentages.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use select columns from the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a new table. We can specify the widths of columns with [cols_width()](GT.cols_width.md#great_tables.GT.cols_width). This is done by specifying the exact widths for table columns in a dictionary. In this example, we'll set the width of the `num` column to `"150px"`, the `char` column to `"100px"`, the `date` column to `"300px"`. All other columns won't be affected (their widths will be automatically set by their content).


``` python
import warnings
from great_tables import GT, exibble

warnings.filterwarnings("ignore")
exibble_mini = exibble[["num", "char", "date", "datetime", "row"]].head(5)

(
    GT(exibble_mini)
    .cols_width(
        cases={
            "num": "150px",
            "char": "100px",
            "date": "300px"
        }
    )
)
```


<style>
#rvjuxmffpq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rvjuxmffpq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rvjuxmffpq p { margin: 0; padding: 0; }
 #rvjuxmffpq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rvjuxmffpq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rvjuxmffpq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rvjuxmffpq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rvjuxmffpq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rvjuxmffpq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rvjuxmffpq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rvjuxmffpq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rvjuxmffpq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rvjuxmffpq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rvjuxmffpq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rvjuxmffpq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rvjuxmffpq .gt_spanner_row { border-bottom-style: hidden; }
 #rvjuxmffpq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rvjuxmffpq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rvjuxmffpq .gt_from_md> :first-child { margin-top: 0; }
 #rvjuxmffpq .gt_from_md> :last-child { margin-bottom: 0; }
 #rvjuxmffpq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rvjuxmffpq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rvjuxmffpq .gt_indent_1 { text-indent: 5px; }
 #rvjuxmffpq .gt_indent_2 { text-indent: calc(5px * 2); }
 #rvjuxmffpq .gt_indent_3 { text-indent: calc(5px * 3); }
 #rvjuxmffpq .gt_indent_4 { text-indent: calc(5px * 4); }
 #rvjuxmffpq .gt_indent_5 { text-indent: calc(5px * 5); }
 #rvjuxmffpq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rvjuxmffpq .gt_row_group_first td { border-top-width: 2px; }
 #rvjuxmffpq .gt_row_group_first th { border-top-width: 2px; }
 #rvjuxmffpq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rvjuxmffpq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rvjuxmffpq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rvjuxmffpq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rvjuxmffpq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rvjuxmffpq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rvjuxmffpq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rvjuxmffpq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rvjuxmffpq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rvjuxmffpq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rvjuxmffpq .gt_left { text-align: left; }
 #rvjuxmffpq .gt_center { text-align: center; }
 #rvjuxmffpq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rvjuxmffpq .gt_font_normal { font-weight: normal; }
 #rvjuxmffpq .gt_font_bold { font-weight: bold; }
 #rvjuxmffpq .gt_font_italic { font-style: italic; }
 #rvjuxmffpq .gt_super { font-size: 65%; }
 #rvjuxmffpq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rvjuxmffpq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rvjuxmffpq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rvjuxmffpq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rvjuxmffpq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rvjuxmffpq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | date       | datetime         | row   |
|--------|---------|------------|------------------|-------|
| 0.1111 | apricot | 2015-01-15 | 2018-01-01 02:22 | row_1 |
| 2.222  | banana  | 2015-02-15 | 2018-02-02 14:33 | row_2 |
| 33.33  | coconut | 2015-03-15 | 2018-03-03 03:44 | row_3 |
| 444.4  | durian  | 2015-04-15 | 2018-04-04 15:55 | row_4 |
| 5550.0 | None    | 2015-05-15 | 2018-05-05 04:00 | row_5 |


We can also specify the widths of columns as percentages. In this example, we'll set the width of the `num` column to `"20%"`, the `char` column to `"10%"`, and the `date` column to `"30%"`. Note that the percentages are relative and don't need to sum to 100%.


``` python
(
    GT(exibble_mini)
    .cols_width(
        cases={
            "num": "20%",
            "char": "10%",
            "date": "30%"
        }
    )
)
```


<style>
#qvascqxkyq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qvascqxkyq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qvascqxkyq p { margin: 0; padding: 0; }
 #qvascqxkyq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qvascqxkyq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qvascqxkyq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qvascqxkyq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qvascqxkyq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qvascqxkyq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qvascqxkyq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qvascqxkyq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qvascqxkyq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qvascqxkyq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qvascqxkyq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qvascqxkyq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qvascqxkyq .gt_spanner_row { border-bottom-style: hidden; }
 #qvascqxkyq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qvascqxkyq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qvascqxkyq .gt_from_md> :first-child { margin-top: 0; }
 #qvascqxkyq .gt_from_md> :last-child { margin-bottom: 0; }
 #qvascqxkyq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qvascqxkyq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qvascqxkyq .gt_indent_1 { text-indent: 5px; }
 #qvascqxkyq .gt_indent_2 { text-indent: calc(5px * 2); }
 #qvascqxkyq .gt_indent_3 { text-indent: calc(5px * 3); }
 #qvascqxkyq .gt_indent_4 { text-indent: calc(5px * 4); }
 #qvascqxkyq .gt_indent_5 { text-indent: calc(5px * 5); }
 #qvascqxkyq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qvascqxkyq .gt_row_group_first td { border-top-width: 2px; }
 #qvascqxkyq .gt_row_group_first th { border-top-width: 2px; }
 #qvascqxkyq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qvascqxkyq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qvascqxkyq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qvascqxkyq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qvascqxkyq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qvascqxkyq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qvascqxkyq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qvascqxkyq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qvascqxkyq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qvascqxkyq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qvascqxkyq .gt_left { text-align: left; }
 #qvascqxkyq .gt_center { text-align: center; }
 #qvascqxkyq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qvascqxkyq .gt_font_normal { font-weight: normal; }
 #qvascqxkyq .gt_font_bold { font-weight: bold; }
 #qvascqxkyq .gt_font_italic { font-style: italic; }
 #qvascqxkyq .gt_super { font-size: 65%; }
 #qvascqxkyq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qvascqxkyq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qvascqxkyq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qvascqxkyq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qvascqxkyq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qvascqxkyq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | date       | datetime         | row   |
|--------|---------|------------|------------------|-------|
| 0.1111 | apricot | 2015-01-15 | 2018-01-01 02:22 | row_1 |
| 2.222  | banana  | 2015-02-15 | 2018-02-02 14:33 | row_2 |
| 33.33  | coconut | 2015-03-15 | 2018-03-03 03:44 | row_3 |
| 444.4  | durian  | 2015-04-15 | 2018-04-04 15:55 | row_4 |
| 5550.0 | None    | 2015-05-15 | 2018-05-05 04:00 | row_5 |


We can also mix and match pixel and percentage widths. In this example, we'll set the width of the `num` column to `"150px"`, the `char` column to `"10%"`, and the `date` column to `"30%"`.


``` python
(
    GT(exibble_mini)
    .cols_width(
        cases={
            "num": "150px",
            "char": "10%",
            "date": "30%"
        }
    )
)
```


<style>
#kvtnlkmbhz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kvtnlkmbhz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kvtnlkmbhz p { margin: 0; padding: 0; }
 #kvtnlkmbhz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kvtnlkmbhz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kvtnlkmbhz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kvtnlkmbhz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kvtnlkmbhz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kvtnlkmbhz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kvtnlkmbhz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kvtnlkmbhz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kvtnlkmbhz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kvtnlkmbhz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kvtnlkmbhz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kvtnlkmbhz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kvtnlkmbhz .gt_spanner_row { border-bottom-style: hidden; }
 #kvtnlkmbhz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kvtnlkmbhz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kvtnlkmbhz .gt_from_md> :first-child { margin-top: 0; }
 #kvtnlkmbhz .gt_from_md> :last-child { margin-bottom: 0; }
 #kvtnlkmbhz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kvtnlkmbhz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kvtnlkmbhz .gt_indent_1 { text-indent: 5px; }
 #kvtnlkmbhz .gt_indent_2 { text-indent: calc(5px * 2); }
 #kvtnlkmbhz .gt_indent_3 { text-indent: calc(5px * 3); }
 #kvtnlkmbhz .gt_indent_4 { text-indent: calc(5px * 4); }
 #kvtnlkmbhz .gt_indent_5 { text-indent: calc(5px * 5); }
 #kvtnlkmbhz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kvtnlkmbhz .gt_row_group_first td { border-top-width: 2px; }
 #kvtnlkmbhz .gt_row_group_first th { border-top-width: 2px; }
 #kvtnlkmbhz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kvtnlkmbhz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kvtnlkmbhz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kvtnlkmbhz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kvtnlkmbhz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kvtnlkmbhz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kvtnlkmbhz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kvtnlkmbhz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kvtnlkmbhz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kvtnlkmbhz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kvtnlkmbhz .gt_left { text-align: left; }
 #kvtnlkmbhz .gt_center { text-align: center; }
 #kvtnlkmbhz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kvtnlkmbhz .gt_font_normal { font-weight: normal; }
 #kvtnlkmbhz .gt_font_bold { font-weight: bold; }
 #kvtnlkmbhz .gt_font_italic { font-style: italic; }
 #kvtnlkmbhz .gt_super { font-size: 65%; }
 #kvtnlkmbhz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kvtnlkmbhz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kvtnlkmbhz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kvtnlkmbhz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kvtnlkmbhz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kvtnlkmbhz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | date       | datetime         | row   |
|--------|---------|------------|------------------|-------|
| 0.1111 | apricot | 2015-01-15 | 2018-01-01 02:22 | row_1 |
| 2.222  | banana  | 2015-02-15 | 2018-02-02 14:33 | row_2 |
| 33.33  | coconut | 2015-03-15 | 2018-03-03 03:44 | row_3 |
| 444.4  | durian  | 2015-04-15 | 2018-04-04 15:55 | row_4 |
| 5550.0 | None    | 2015-05-15 | 2018-05-05 04:00 | row_5 |


If we set the width of all columns, the table will be forced to use the specified widths (i.e., a column width less than the content width will be honored). In this next example, we'll set widths for all columns. This is a good way to ensure that the widths you specify are fully respected (and not overridden by automatic width calculations).


``` python
(
    GT(exibble_mini)
    .cols_width(
        cases={
            "num": "30px",
            "char": "100px",
            "date": "100px",
            "datetime": "200px",
            "row": "50px"
        }
    )
)
```


<style>
#wsrkabenhz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wsrkabenhz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wsrkabenhz p { margin: 0; padding: 0; }
 #wsrkabenhz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wsrkabenhz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wsrkabenhz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wsrkabenhz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wsrkabenhz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wsrkabenhz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wsrkabenhz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wsrkabenhz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wsrkabenhz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wsrkabenhz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wsrkabenhz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wsrkabenhz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wsrkabenhz .gt_spanner_row { border-bottom-style: hidden; }
 #wsrkabenhz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wsrkabenhz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wsrkabenhz .gt_from_md> :first-child { margin-top: 0; }
 #wsrkabenhz .gt_from_md> :last-child { margin-bottom: 0; }
 #wsrkabenhz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wsrkabenhz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wsrkabenhz .gt_indent_1 { text-indent: 5px; }
 #wsrkabenhz .gt_indent_2 { text-indent: calc(5px * 2); }
 #wsrkabenhz .gt_indent_3 { text-indent: calc(5px * 3); }
 #wsrkabenhz .gt_indent_4 { text-indent: calc(5px * 4); }
 #wsrkabenhz .gt_indent_5 { text-indent: calc(5px * 5); }
 #wsrkabenhz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wsrkabenhz .gt_row_group_first td { border-top-width: 2px; }
 #wsrkabenhz .gt_row_group_first th { border-top-width: 2px; }
 #wsrkabenhz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wsrkabenhz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wsrkabenhz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wsrkabenhz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wsrkabenhz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wsrkabenhz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wsrkabenhz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wsrkabenhz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wsrkabenhz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wsrkabenhz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wsrkabenhz .gt_left { text-align: left; }
 #wsrkabenhz .gt_center { text-align: center; }
 #wsrkabenhz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wsrkabenhz .gt_font_normal { font-weight: normal; }
 #wsrkabenhz .gt_font_bold { font-weight: bold; }
 #wsrkabenhz .gt_font_italic { font-style: italic; }
 #wsrkabenhz .gt_super { font-size: 65%; }
 #wsrkabenhz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wsrkabenhz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wsrkabenhz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wsrkabenhz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wsrkabenhz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wsrkabenhz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | date       | datetime         | row   |
|--------|---------|------------|------------------|-------|
| 0.1111 | apricot | 2015-01-15 | 2018-01-01 02:22 | row_1 |
| 2.222  | banana  | 2015-02-15 | 2018-02-02 14:33 | row_2 |
| 33.33  | coconut | 2015-03-15 | 2018-03-03 03:44 | row_3 |
| 444.4  | durian  | 2015-04-15 | 2018-04-04 15:55 | row_4 |
| 5550.0 | None    | 2015-05-15 | 2018-05-05 04:00 | row_5 |


Notice that in the above example, the `num` column is very small (only `30px`) and the content overflows. When not specifying the width of all columns, the table will automatically adjust the column widths based on the content (and you wouldn't get the overflowing behavior seen in the previous example).

When a table has a stub (row labels), use the `stub` sentinel to set its width. This avoids any ambiguity with a data column that happens to be named `"stub"`. With a hierarchical stub, [stub](loc.stub.md#great_tables.loc.stub) sets the width of every stub column, and `stub(n)` sets the width of a single level, counting from the right (`stub(1)` is the column holding the row labels).


``` python
from great_tables import GT, stub
from great_tables.data import gtcars

gtcars_mini = gtcars[["model", "year", "hp", "msrp"]].head(6)

(
    GT(gtcars_mini, rowname_col="model")
    .cols_width(
        cases={
            stub: "200px",
            "year": "60px",
            "hp": "60px",
            "msrp": "120px",
        }
    )
)
```


<style>
#rykzhdkpcn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rykzhdkpcn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rykzhdkpcn p { margin: 0; padding: 0; }
 #rykzhdkpcn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rykzhdkpcn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rykzhdkpcn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rykzhdkpcn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rykzhdkpcn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rykzhdkpcn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rykzhdkpcn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rykzhdkpcn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rykzhdkpcn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rykzhdkpcn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rykzhdkpcn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rykzhdkpcn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rykzhdkpcn .gt_spanner_row { border-bottom-style: hidden; }
 #rykzhdkpcn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rykzhdkpcn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rykzhdkpcn .gt_from_md> :first-child { margin-top: 0; }
 #rykzhdkpcn .gt_from_md> :last-child { margin-bottom: 0; }
 #rykzhdkpcn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rykzhdkpcn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rykzhdkpcn .gt_indent_1 { text-indent: 5px; }
 #rykzhdkpcn .gt_indent_2 { text-indent: calc(5px * 2); }
 #rykzhdkpcn .gt_indent_3 { text-indent: calc(5px * 3); }
 #rykzhdkpcn .gt_indent_4 { text-indent: calc(5px * 4); }
 #rykzhdkpcn .gt_indent_5 { text-indent: calc(5px * 5); }
 #rykzhdkpcn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rykzhdkpcn .gt_row_group_first td { border-top-width: 2px; }
 #rykzhdkpcn .gt_row_group_first th { border-top-width: 2px; }
 #rykzhdkpcn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rykzhdkpcn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rykzhdkpcn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rykzhdkpcn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rykzhdkpcn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rykzhdkpcn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rykzhdkpcn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rykzhdkpcn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rykzhdkpcn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rykzhdkpcn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rykzhdkpcn .gt_left { text-align: left; }
 #rykzhdkpcn .gt_center { text-align: center; }
 #rykzhdkpcn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rykzhdkpcn .gt_font_normal { font-weight: normal; }
 #rykzhdkpcn .gt_font_bold { font-weight: bold; }
 #rykzhdkpcn .gt_font_italic { font-style: italic; }
 #rykzhdkpcn .gt_super { font-size: 65%; }
 #rykzhdkpcn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rykzhdkpcn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rykzhdkpcn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rykzhdkpcn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rykzhdkpcn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rykzhdkpcn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|              | year | hp    | msrp     |
|--------------|------|-------|----------|
| GT           | 2017 | 647.0 | 447000.0 |
| 458 Speciale | 2015 | 597.0 | 291744.0 |
| 458 Spider   | 2015 | 562.0 | 263553.0 |
| 458 Italia   | 2014 | 562.0 | 233509.0 |
| 488 GTB      | 2016 | 661.0 | 245400.0 |
| California   | 2015 | 553.0 | 198973.0 |


Here's a hierarchical stub with a different width for each level.


``` python
(
    GT(gtcars[["mfr", "model", "year", "hp"]].head(6), rowname_col=["mfr", "model"])
    .cols_width(cases={stub(2): "120px", stub(1): "200px", "year": "60px", "hp": "60px"})
)
```


<style>
#cncbjcmwzc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cncbjcmwzc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cncbjcmwzc p { margin: 0; padding: 0; }
 #cncbjcmwzc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cncbjcmwzc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cncbjcmwzc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cncbjcmwzc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cncbjcmwzc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cncbjcmwzc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cncbjcmwzc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cncbjcmwzc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cncbjcmwzc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cncbjcmwzc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cncbjcmwzc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cncbjcmwzc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cncbjcmwzc .gt_spanner_row { border-bottom-style: hidden; }
 #cncbjcmwzc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cncbjcmwzc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cncbjcmwzc .gt_from_md> :first-child { margin-top: 0; }
 #cncbjcmwzc .gt_from_md> :last-child { margin-bottom: 0; }
 #cncbjcmwzc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cncbjcmwzc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cncbjcmwzc .gt_indent_1 { text-indent: 5px; }
 #cncbjcmwzc .gt_indent_2 { text-indent: calc(5px * 2); }
 #cncbjcmwzc .gt_indent_3 { text-indent: calc(5px * 3); }
 #cncbjcmwzc .gt_indent_4 { text-indent: calc(5px * 4); }
 #cncbjcmwzc .gt_indent_5 { text-indent: calc(5px * 5); }
 #cncbjcmwzc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cncbjcmwzc .gt_row_group_first td { border-top-width: 2px; }
 #cncbjcmwzc .gt_row_group_first th { border-top-width: 2px; }
 #cncbjcmwzc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cncbjcmwzc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cncbjcmwzc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cncbjcmwzc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cncbjcmwzc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cncbjcmwzc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cncbjcmwzc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cncbjcmwzc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cncbjcmwzc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cncbjcmwzc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cncbjcmwzc .gt_left { text-align: left; }
 #cncbjcmwzc .gt_center { text-align: center; }
 #cncbjcmwzc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cncbjcmwzc .gt_font_normal { font-weight: normal; }
 #cncbjcmwzc .gt_font_bold { font-weight: bold; }
 #cncbjcmwzc .gt_font_italic { font-style: italic; }
 #cncbjcmwzc .gt_super { font-size: 65%; }
 #cncbjcmwzc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cncbjcmwzc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cncbjcmwzc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cncbjcmwzc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cncbjcmwzc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cncbjcmwzc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" style="table-layout: fixed;; width: 0px" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th colspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" scope="colgroup"></th>
<th id="year" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">year</th>
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th id="stub-1-1" class="gt_row gt_left gt_stub" scope="row">Ford</th>
<th id="stub-1-2" class="gt_row gt_left gt_stub" scope="row">GT</th>
<td class="gt_row gt_right" headers="stub-1-1 stub-1-2 year">2017</td>
<td class="gt_row gt_right" headers="stub-1-1 stub-1-2 hp">647.0</td>
</tr>
<tr>
<th rowspan="5" id="stub-2-1" class="gt_row gt_left gt_stub" scope="rowgroup">Ferrari</th>
<th id="stub-2-2" class="gt_row gt_left gt_stub" scope="row">458 Speciale</th>
<td class="gt_row gt_right" headers="stub-2-1 stub-2-2 year">2015</td>
<td class="gt_row gt_right" headers="stub-2-1 stub-2-2 hp">597.0</td>
</tr>
<tr>
<th id="stub-3-2" class="gt_row gt_left gt_stub" scope="row">458 Spider</th>
<td class="gt_row gt_right" headers="stub-2-1 stub-3-2 year">2015</td>
<td class="gt_row gt_right" headers="stub-2-1 stub-3-2 hp">562.0</td>
</tr>
<tr>
<th id="stub-4-2" class="gt_row gt_left gt_stub" scope="row">458 Italia</th>
<td class="gt_row gt_right" headers="stub-2-1 stub-4-2 year">2014</td>
<td class="gt_row gt_right" headers="stub-2-1 stub-4-2 hp">562.0</td>
</tr>
<tr>
<th id="stub-5-2" class="gt_row gt_left gt_stub" scope="row">488 GTB</th>
<td class="gt_row gt_right" headers="stub-2-1 stub-5-2 year">2016</td>
<td class="gt_row gt_right" headers="stub-2-1 stub-5-2 hp">661.0</td>
</tr>
<tr>
<th id="stub-6-2" class="gt_row gt_left gt_stub" scope="row">California</th>
<td class="gt_row gt_right" headers="stub-2-1 stub-6-2 year">2015</td>
<td class="gt_row gt_right" headers="stub-2-1 stub-6-2 hp">553.0</td>
</tr>
</tbody>
</table>
