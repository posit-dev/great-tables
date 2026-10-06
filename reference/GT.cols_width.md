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
A dictionary where the keys are column names and the values are the widths. Widths can be specified in pixels (e.g., `"50px"`) or as percentages (e.g., `"20%"`). Use the `stub` sentinel as a key to set the width of the stub column without risk of collision with a data column named `"stub"`.

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
#zcdazfluzy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zcdazfluzy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zcdazfluzy p { margin: 0; padding: 0; }
 #zcdazfluzy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zcdazfluzy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zcdazfluzy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zcdazfluzy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zcdazfluzy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zcdazfluzy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zcdazfluzy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zcdazfluzy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zcdazfluzy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zcdazfluzy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zcdazfluzy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zcdazfluzy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zcdazfluzy .gt_spanner_row { border-bottom-style: hidden; }
 #zcdazfluzy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zcdazfluzy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zcdazfluzy .gt_from_md> :first-child { margin-top: 0; }
 #zcdazfluzy .gt_from_md> :last-child { margin-bottom: 0; }
 #zcdazfluzy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zcdazfluzy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zcdazfluzy .gt_indent_1 { text-indent: 5px; }
 #zcdazfluzy .gt_indent_2 { text-indent: calc(5px * 2); }
 #zcdazfluzy .gt_indent_3 { text-indent: calc(5px * 3); }
 #zcdazfluzy .gt_indent_4 { text-indent: calc(5px * 4); }
 #zcdazfluzy .gt_indent_5 { text-indent: calc(5px * 5); }
 #zcdazfluzy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zcdazfluzy .gt_row_group_first td { border-top-width: 2px; }
 #zcdazfluzy .gt_row_group_first th { border-top-width: 2px; }
 #zcdazfluzy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zcdazfluzy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zcdazfluzy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zcdazfluzy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zcdazfluzy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zcdazfluzy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zcdazfluzy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zcdazfluzy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zcdazfluzy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zcdazfluzy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zcdazfluzy .gt_left { text-align: left; }
 #zcdazfluzy .gt_center { text-align: center; }
 #zcdazfluzy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zcdazfluzy .gt_font_normal { font-weight: normal; }
 #zcdazfluzy .gt_font_bold { font-weight: bold; }
 #zcdazfluzy .gt_font_italic { font-style: italic; }
 #zcdazfluzy .gt_super { font-size: 65%; }
 #zcdazfluzy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zcdazfluzy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zcdazfluzy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zcdazfluzy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zcdazfluzy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zcdazfluzy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zfplqjyppc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zfplqjyppc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zfplqjyppc p { margin: 0; padding: 0; }
 #zfplqjyppc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zfplqjyppc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zfplqjyppc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zfplqjyppc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zfplqjyppc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zfplqjyppc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zfplqjyppc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zfplqjyppc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zfplqjyppc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zfplqjyppc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zfplqjyppc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zfplqjyppc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zfplqjyppc .gt_spanner_row { border-bottom-style: hidden; }
 #zfplqjyppc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zfplqjyppc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zfplqjyppc .gt_from_md> :first-child { margin-top: 0; }
 #zfplqjyppc .gt_from_md> :last-child { margin-bottom: 0; }
 #zfplqjyppc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zfplqjyppc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zfplqjyppc .gt_indent_1 { text-indent: 5px; }
 #zfplqjyppc .gt_indent_2 { text-indent: calc(5px * 2); }
 #zfplqjyppc .gt_indent_3 { text-indent: calc(5px * 3); }
 #zfplqjyppc .gt_indent_4 { text-indent: calc(5px * 4); }
 #zfplqjyppc .gt_indent_5 { text-indent: calc(5px * 5); }
 #zfplqjyppc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zfplqjyppc .gt_row_group_first td { border-top-width: 2px; }
 #zfplqjyppc .gt_row_group_first th { border-top-width: 2px; }
 #zfplqjyppc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zfplqjyppc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zfplqjyppc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zfplqjyppc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zfplqjyppc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zfplqjyppc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zfplqjyppc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zfplqjyppc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zfplqjyppc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zfplqjyppc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zfplqjyppc .gt_left { text-align: left; }
 #zfplqjyppc .gt_center { text-align: center; }
 #zfplqjyppc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zfplqjyppc .gt_font_normal { font-weight: normal; }
 #zfplqjyppc .gt_font_bold { font-weight: bold; }
 #zfplqjyppc .gt_font_italic { font-style: italic; }
 #zfplqjyppc .gt_super { font-size: 65%; }
 #zfplqjyppc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zfplqjyppc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zfplqjyppc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zfplqjyppc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zfplqjyppc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zfplqjyppc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#mqmjsfgigw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mqmjsfgigw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mqmjsfgigw p { margin: 0; padding: 0; }
 #mqmjsfgigw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mqmjsfgigw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mqmjsfgigw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mqmjsfgigw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mqmjsfgigw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mqmjsfgigw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mqmjsfgigw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mqmjsfgigw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mqmjsfgigw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mqmjsfgigw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mqmjsfgigw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mqmjsfgigw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mqmjsfgigw .gt_spanner_row { border-bottom-style: hidden; }
 #mqmjsfgigw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mqmjsfgigw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mqmjsfgigw .gt_from_md> :first-child { margin-top: 0; }
 #mqmjsfgigw .gt_from_md> :last-child { margin-bottom: 0; }
 #mqmjsfgigw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mqmjsfgigw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mqmjsfgigw .gt_indent_1 { text-indent: 5px; }
 #mqmjsfgigw .gt_indent_2 { text-indent: calc(5px * 2); }
 #mqmjsfgigw .gt_indent_3 { text-indent: calc(5px * 3); }
 #mqmjsfgigw .gt_indent_4 { text-indent: calc(5px * 4); }
 #mqmjsfgigw .gt_indent_5 { text-indent: calc(5px * 5); }
 #mqmjsfgigw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mqmjsfgigw .gt_row_group_first td { border-top-width: 2px; }
 #mqmjsfgigw .gt_row_group_first th { border-top-width: 2px; }
 #mqmjsfgigw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mqmjsfgigw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mqmjsfgigw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mqmjsfgigw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mqmjsfgigw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mqmjsfgigw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mqmjsfgigw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mqmjsfgigw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mqmjsfgigw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mqmjsfgigw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mqmjsfgigw .gt_left { text-align: left; }
 #mqmjsfgigw .gt_center { text-align: center; }
 #mqmjsfgigw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mqmjsfgigw .gt_font_normal { font-weight: normal; }
 #mqmjsfgigw .gt_font_bold { font-weight: bold; }
 #mqmjsfgigw .gt_font_italic { font-style: italic; }
 #mqmjsfgigw .gt_super { font-size: 65%; }
 #mqmjsfgigw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mqmjsfgigw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mqmjsfgigw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mqmjsfgigw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mqmjsfgigw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mqmjsfgigw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dnzqqyxhvo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dnzqqyxhvo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dnzqqyxhvo p { margin: 0; padding: 0; }
 #dnzqqyxhvo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dnzqqyxhvo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dnzqqyxhvo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dnzqqyxhvo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dnzqqyxhvo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dnzqqyxhvo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dnzqqyxhvo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dnzqqyxhvo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dnzqqyxhvo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dnzqqyxhvo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dnzqqyxhvo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dnzqqyxhvo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dnzqqyxhvo .gt_spanner_row { border-bottom-style: hidden; }
 #dnzqqyxhvo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dnzqqyxhvo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dnzqqyxhvo .gt_from_md> :first-child { margin-top: 0; }
 #dnzqqyxhvo .gt_from_md> :last-child { margin-bottom: 0; }
 #dnzqqyxhvo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dnzqqyxhvo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dnzqqyxhvo .gt_indent_1 { text-indent: 5px; }
 #dnzqqyxhvo .gt_indent_2 { text-indent: calc(5px * 2); }
 #dnzqqyxhvo .gt_indent_3 { text-indent: calc(5px * 3); }
 #dnzqqyxhvo .gt_indent_4 { text-indent: calc(5px * 4); }
 #dnzqqyxhvo .gt_indent_5 { text-indent: calc(5px * 5); }
 #dnzqqyxhvo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dnzqqyxhvo .gt_row_group_first td { border-top-width: 2px; }
 #dnzqqyxhvo .gt_row_group_first th { border-top-width: 2px; }
 #dnzqqyxhvo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dnzqqyxhvo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dnzqqyxhvo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dnzqqyxhvo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dnzqqyxhvo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dnzqqyxhvo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dnzqqyxhvo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dnzqqyxhvo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dnzqqyxhvo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dnzqqyxhvo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dnzqqyxhvo .gt_left { text-align: left; }
 #dnzqqyxhvo .gt_center { text-align: center; }
 #dnzqqyxhvo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dnzqqyxhvo .gt_font_normal { font-weight: normal; }
 #dnzqqyxhvo .gt_font_bold { font-weight: bold; }
 #dnzqqyxhvo .gt_font_italic { font-style: italic; }
 #dnzqqyxhvo .gt_super { font-size: 65%; }
 #dnzqqyxhvo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dnzqqyxhvo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dnzqqyxhvo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dnzqqyxhvo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dnzqqyxhvo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dnzqqyxhvo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| num    | char    | date       | datetime         | row   |
|--------|---------|------------|------------------|-------|
| 0.1111 | apricot | 2015-01-15 | 2018-01-01 02:22 | row_1 |
| 2.222  | banana  | 2015-02-15 | 2018-02-02 14:33 | row_2 |
| 33.33  | coconut | 2015-03-15 | 2018-03-03 03:44 | row_3 |
| 444.4  | durian  | 2015-04-15 | 2018-04-04 15:55 | row_4 |
| 5550.0 | None    | 2015-05-15 | 2018-05-05 04:00 | row_5 |


Notice that in the above example, the `num` column is very small (only `30px`) and the content overflows. When not specifying the width of all columns, the table will automatically adjust the column widths based on the content (and you wouldn't get the overflowing behavior seen in the previous example).

When a table has a stub (row labels), use the `stub` sentinel to set its width. This avoids any ambiguity with a data column that happens to be named `"stub"`.


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
#muzbznjavf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#muzbznjavf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#muzbznjavf p { margin: 0; padding: 0; }
 #muzbznjavf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #muzbznjavf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #muzbznjavf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #muzbznjavf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #muzbznjavf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #muzbznjavf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muzbznjavf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #muzbznjavf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #muzbznjavf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #muzbznjavf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #muzbznjavf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #muzbznjavf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #muzbznjavf .gt_spanner_row { border-bottom-style: hidden; }
 #muzbznjavf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #muzbznjavf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #muzbznjavf .gt_from_md> :first-child { margin-top: 0; }
 #muzbznjavf .gt_from_md> :last-child { margin-bottom: 0; }
 #muzbznjavf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #muzbznjavf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #muzbznjavf .gt_indent_1 { text-indent: 5px; }
 #muzbznjavf .gt_indent_2 { text-indent: calc(5px * 2); }
 #muzbznjavf .gt_indent_3 { text-indent: calc(5px * 3); }
 #muzbznjavf .gt_indent_4 { text-indent: calc(5px * 4); }
 #muzbznjavf .gt_indent_5 { text-indent: calc(5px * 5); }
 #muzbznjavf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #muzbznjavf .gt_row_group_first td { border-top-width: 2px; }
 #muzbznjavf .gt_row_group_first th { border-top-width: 2px; }
 #muzbznjavf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #muzbznjavf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muzbznjavf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #muzbznjavf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #muzbznjavf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muzbznjavf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #muzbznjavf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #muzbznjavf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #muzbznjavf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muzbznjavf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #muzbznjavf .gt_left { text-align: left; }
 #muzbznjavf .gt_center { text-align: center; }
 #muzbznjavf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #muzbznjavf .gt_font_normal { font-weight: normal; }
 #muzbznjavf .gt_font_bold { font-weight: bold; }
 #muzbznjavf .gt_font_italic { font-style: italic; }
 #muzbznjavf .gt_super { font-size: 65%; }
 #muzbznjavf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muzbznjavf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #muzbznjavf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muzbznjavf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #muzbznjavf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #muzbznjavf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|              | year | hp    | msrp     |
|--------------|------|-------|----------|
| GT           | 2017 | 647.0 | 447000.0 |
| 458 Speciale | 2015 | 597.0 | 291744.0 |
| 458 Spider   | 2015 | 562.0 | 263553.0 |
| 458 Italia   | 2014 | 562.0 | 233509.0 |
| 488 GTB      | 2016 | 661.0 | 245400.0 |
| California   | 2015 | 553.0 | 198973.0 |
