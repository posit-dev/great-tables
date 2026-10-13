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
#sqcdgmxwlb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sqcdgmxwlb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sqcdgmxwlb p { margin: 0; padding: 0; }
 #sqcdgmxwlb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sqcdgmxwlb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sqcdgmxwlb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sqcdgmxwlb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sqcdgmxwlb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sqcdgmxwlb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sqcdgmxwlb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sqcdgmxwlb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sqcdgmxwlb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sqcdgmxwlb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sqcdgmxwlb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sqcdgmxwlb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sqcdgmxwlb .gt_spanner_row { border-bottom-style: hidden; }
 #sqcdgmxwlb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sqcdgmxwlb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sqcdgmxwlb .gt_from_md> :first-child { margin-top: 0; }
 #sqcdgmxwlb .gt_from_md> :last-child { margin-bottom: 0; }
 #sqcdgmxwlb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sqcdgmxwlb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sqcdgmxwlb .gt_indent_1 { text-indent: 5px; }
 #sqcdgmxwlb .gt_indent_2 { text-indent: calc(5px * 2); }
 #sqcdgmxwlb .gt_indent_3 { text-indent: calc(5px * 3); }
 #sqcdgmxwlb .gt_indent_4 { text-indent: calc(5px * 4); }
 #sqcdgmxwlb .gt_indent_5 { text-indent: calc(5px * 5); }
 #sqcdgmxwlb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sqcdgmxwlb .gt_row_group_first td { border-top-width: 2px; }
 #sqcdgmxwlb .gt_row_group_first th { border-top-width: 2px; }
 #sqcdgmxwlb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sqcdgmxwlb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sqcdgmxwlb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sqcdgmxwlb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sqcdgmxwlb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sqcdgmxwlb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sqcdgmxwlb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sqcdgmxwlb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sqcdgmxwlb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sqcdgmxwlb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sqcdgmxwlb .gt_left { text-align: left; }
 #sqcdgmxwlb .gt_center { text-align: center; }
 #sqcdgmxwlb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sqcdgmxwlb .gt_font_normal { font-weight: normal; }
 #sqcdgmxwlb .gt_font_bold { font-weight: bold; }
 #sqcdgmxwlb .gt_font_italic { font-style: italic; }
 #sqcdgmxwlb .gt_super { font-size: 65%; }
 #sqcdgmxwlb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sqcdgmxwlb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sqcdgmxwlb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sqcdgmxwlb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sqcdgmxwlb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sqcdgmxwlb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zhtououlwo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zhtououlwo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zhtououlwo p { margin: 0; padding: 0; }
 #zhtououlwo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zhtououlwo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zhtououlwo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zhtououlwo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zhtououlwo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zhtououlwo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zhtououlwo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zhtououlwo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zhtououlwo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zhtououlwo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zhtououlwo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zhtououlwo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zhtououlwo .gt_spanner_row { border-bottom-style: hidden; }
 #zhtououlwo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zhtououlwo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zhtououlwo .gt_from_md> :first-child { margin-top: 0; }
 #zhtououlwo .gt_from_md> :last-child { margin-bottom: 0; }
 #zhtououlwo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zhtououlwo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zhtououlwo .gt_indent_1 { text-indent: 5px; }
 #zhtououlwo .gt_indent_2 { text-indent: calc(5px * 2); }
 #zhtououlwo .gt_indent_3 { text-indent: calc(5px * 3); }
 #zhtououlwo .gt_indent_4 { text-indent: calc(5px * 4); }
 #zhtououlwo .gt_indent_5 { text-indent: calc(5px * 5); }
 #zhtououlwo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zhtououlwo .gt_row_group_first td { border-top-width: 2px; }
 #zhtououlwo .gt_row_group_first th { border-top-width: 2px; }
 #zhtououlwo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zhtououlwo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zhtououlwo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zhtououlwo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zhtououlwo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zhtououlwo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zhtououlwo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zhtououlwo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zhtououlwo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zhtououlwo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zhtououlwo .gt_left { text-align: left; }
 #zhtououlwo .gt_center { text-align: center; }
 #zhtououlwo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zhtououlwo .gt_font_normal { font-weight: normal; }
 #zhtououlwo .gt_font_bold { font-weight: bold; }
 #zhtououlwo .gt_font_italic { font-style: italic; }
 #zhtououlwo .gt_super { font-size: 65%; }
 #zhtououlwo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zhtououlwo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zhtououlwo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zhtououlwo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zhtououlwo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zhtououlwo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fcvheavjhd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fcvheavjhd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fcvheavjhd p { margin: 0; padding: 0; }
 #fcvheavjhd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fcvheavjhd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fcvheavjhd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fcvheavjhd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fcvheavjhd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fcvheavjhd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fcvheavjhd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fcvheavjhd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fcvheavjhd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fcvheavjhd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fcvheavjhd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fcvheavjhd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fcvheavjhd .gt_spanner_row { border-bottom-style: hidden; }
 #fcvheavjhd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fcvheavjhd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fcvheavjhd .gt_from_md> :first-child { margin-top: 0; }
 #fcvheavjhd .gt_from_md> :last-child { margin-bottom: 0; }
 #fcvheavjhd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fcvheavjhd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fcvheavjhd .gt_indent_1 { text-indent: 5px; }
 #fcvheavjhd .gt_indent_2 { text-indent: calc(5px * 2); }
 #fcvheavjhd .gt_indent_3 { text-indent: calc(5px * 3); }
 #fcvheavjhd .gt_indent_4 { text-indent: calc(5px * 4); }
 #fcvheavjhd .gt_indent_5 { text-indent: calc(5px * 5); }
 #fcvheavjhd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fcvheavjhd .gt_row_group_first td { border-top-width: 2px; }
 #fcvheavjhd .gt_row_group_first th { border-top-width: 2px; }
 #fcvheavjhd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fcvheavjhd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fcvheavjhd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fcvheavjhd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fcvheavjhd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fcvheavjhd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fcvheavjhd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fcvheavjhd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fcvheavjhd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fcvheavjhd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fcvheavjhd .gt_left { text-align: left; }
 #fcvheavjhd .gt_center { text-align: center; }
 #fcvheavjhd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fcvheavjhd .gt_font_normal { font-weight: normal; }
 #fcvheavjhd .gt_font_bold { font-weight: bold; }
 #fcvheavjhd .gt_font_italic { font-style: italic; }
 #fcvheavjhd .gt_super { font-size: 65%; }
 #fcvheavjhd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fcvheavjhd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fcvheavjhd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fcvheavjhd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fcvheavjhd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fcvheavjhd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dvmfqkadik table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dvmfqkadik thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dvmfqkadik p { margin: 0; padding: 0; }
 #dvmfqkadik .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dvmfqkadik .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dvmfqkadik .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dvmfqkadik .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dvmfqkadik .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dvmfqkadik .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dvmfqkadik .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dvmfqkadik .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dvmfqkadik .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dvmfqkadik .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dvmfqkadik .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dvmfqkadik .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dvmfqkadik .gt_spanner_row { border-bottom-style: hidden; }
 #dvmfqkadik .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dvmfqkadik .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dvmfqkadik .gt_from_md> :first-child { margin-top: 0; }
 #dvmfqkadik .gt_from_md> :last-child { margin-bottom: 0; }
 #dvmfqkadik .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dvmfqkadik .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dvmfqkadik .gt_indent_1 { text-indent: 5px; }
 #dvmfqkadik .gt_indent_2 { text-indent: calc(5px * 2); }
 #dvmfqkadik .gt_indent_3 { text-indent: calc(5px * 3); }
 #dvmfqkadik .gt_indent_4 { text-indent: calc(5px * 4); }
 #dvmfqkadik .gt_indent_5 { text-indent: calc(5px * 5); }
 #dvmfqkadik .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dvmfqkadik .gt_row_group_first td { border-top-width: 2px; }
 #dvmfqkadik .gt_row_group_first th { border-top-width: 2px; }
 #dvmfqkadik .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dvmfqkadik .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dvmfqkadik .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dvmfqkadik .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dvmfqkadik .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dvmfqkadik .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dvmfqkadik .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dvmfqkadik .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dvmfqkadik .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dvmfqkadik .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dvmfqkadik .gt_left { text-align: left; }
 #dvmfqkadik .gt_center { text-align: center; }
 #dvmfqkadik .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dvmfqkadik .gt_font_normal { font-weight: normal; }
 #dvmfqkadik .gt_font_bold { font-weight: bold; }
 #dvmfqkadik .gt_font_italic { font-style: italic; }
 #dvmfqkadik .gt_super { font-size: 65%; }
 #dvmfqkadik .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dvmfqkadik .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dvmfqkadik .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dvmfqkadik .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dvmfqkadik .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dvmfqkadik .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jczztsoaoo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jczztsoaoo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jczztsoaoo p { margin: 0; padding: 0; }
 #jczztsoaoo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jczztsoaoo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jczztsoaoo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jczztsoaoo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jczztsoaoo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jczztsoaoo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jczztsoaoo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jczztsoaoo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jczztsoaoo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jczztsoaoo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jczztsoaoo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jczztsoaoo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jczztsoaoo .gt_spanner_row { border-bottom-style: hidden; }
 #jczztsoaoo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jczztsoaoo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jczztsoaoo .gt_from_md> :first-child { margin-top: 0; }
 #jczztsoaoo .gt_from_md> :last-child { margin-bottom: 0; }
 #jczztsoaoo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jczztsoaoo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jczztsoaoo .gt_indent_1 { text-indent: 5px; }
 #jczztsoaoo .gt_indent_2 { text-indent: calc(5px * 2); }
 #jczztsoaoo .gt_indent_3 { text-indent: calc(5px * 3); }
 #jczztsoaoo .gt_indent_4 { text-indent: calc(5px * 4); }
 #jczztsoaoo .gt_indent_5 { text-indent: calc(5px * 5); }
 #jczztsoaoo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jczztsoaoo .gt_row_group_first td { border-top-width: 2px; }
 #jczztsoaoo .gt_row_group_first th { border-top-width: 2px; }
 #jczztsoaoo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jczztsoaoo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jczztsoaoo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jczztsoaoo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jczztsoaoo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jczztsoaoo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jczztsoaoo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jczztsoaoo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jczztsoaoo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jczztsoaoo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jczztsoaoo .gt_left { text-align: left; }
 #jczztsoaoo .gt_center { text-align: center; }
 #jczztsoaoo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jczztsoaoo .gt_font_normal { font-weight: normal; }
 #jczztsoaoo .gt_font_bold { font-weight: bold; }
 #jczztsoaoo .gt_font_italic { font-style: italic; }
 #jczztsoaoo .gt_super { font-size: 65%; }
 #jczztsoaoo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jczztsoaoo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jczztsoaoo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jczztsoaoo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jczztsoaoo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jczztsoaoo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dxdissskvy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dxdissskvy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dxdissskvy p { margin: 0; padding: 0; }
 #dxdissskvy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dxdissskvy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dxdissskvy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dxdissskvy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dxdissskvy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dxdissskvy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxdissskvy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dxdissskvy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dxdissskvy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dxdissskvy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dxdissskvy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dxdissskvy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dxdissskvy .gt_spanner_row { border-bottom-style: hidden; }
 #dxdissskvy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dxdissskvy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dxdissskvy .gt_from_md> :first-child { margin-top: 0; }
 #dxdissskvy .gt_from_md> :last-child { margin-bottom: 0; }
 #dxdissskvy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dxdissskvy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dxdissskvy .gt_indent_1 { text-indent: 5px; }
 #dxdissskvy .gt_indent_2 { text-indent: calc(5px * 2); }
 #dxdissskvy .gt_indent_3 { text-indent: calc(5px * 3); }
 #dxdissskvy .gt_indent_4 { text-indent: calc(5px * 4); }
 #dxdissskvy .gt_indent_5 { text-indent: calc(5px * 5); }
 #dxdissskvy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dxdissskvy .gt_row_group_first td { border-top-width: 2px; }
 #dxdissskvy .gt_row_group_first th { border-top-width: 2px; }
 #dxdissskvy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dxdissskvy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxdissskvy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dxdissskvy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dxdissskvy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxdissskvy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dxdissskvy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dxdissskvy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dxdissskvy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxdissskvy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dxdissskvy .gt_left { text-align: left; }
 #dxdissskvy .gt_center { text-align: center; }
 #dxdissskvy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dxdissskvy .gt_font_normal { font-weight: normal; }
 #dxdissskvy .gt_font_bold { font-weight: bold; }
 #dxdissskvy .gt_font_italic { font-style: italic; }
 #dxdissskvy .gt_super { font-size: 65%; }
 #dxdissskvy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxdissskvy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dxdissskvy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxdissskvy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dxdissskvy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dxdissskvy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th class="gt_row gt_left gt_stub" scope="row">Ford</th>
<th class="gt_row gt_left gt_stub" scope="row">GT</th>
<td class="gt_row gt_right">2017</td>
<td class="gt_row gt_right">647.0</td>
</tr>
<tr>
<th rowspan="5" class="gt_row gt_left gt_stub" scope="rowgroup">Ferrari</th>
<th class="gt_row gt_left gt_stub" scope="row">458 Speciale</th>
<td class="gt_row gt_right">2015</td>
<td class="gt_row gt_right">597.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" scope="row">458 Spider</th>
<td class="gt_row gt_right">2015</td>
<td class="gt_row gt_right">562.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" scope="row">458 Italia</th>
<td class="gt_row gt_right">2014</td>
<td class="gt_row gt_right">562.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" scope="row">488 GTB</th>
<td class="gt_row gt_right">2016</td>
<td class="gt_row gt_right">661.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub" scope="row">California</th>
<td class="gt_row gt_right">2015</td>
<td class="gt_row gt_right">553.0</td>
</tr>
</tbody>
</table>
