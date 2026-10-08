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
#hbdnqtpgbj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hbdnqtpgbj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hbdnqtpgbj p { margin: 0; padding: 0; }
 #hbdnqtpgbj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hbdnqtpgbj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hbdnqtpgbj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hbdnqtpgbj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hbdnqtpgbj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hbdnqtpgbj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hbdnqtpgbj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hbdnqtpgbj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hbdnqtpgbj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hbdnqtpgbj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hbdnqtpgbj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hbdnqtpgbj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hbdnqtpgbj .gt_spanner_row { border-bottom-style: hidden; }
 #hbdnqtpgbj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hbdnqtpgbj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hbdnqtpgbj .gt_from_md> :first-child { margin-top: 0; }
 #hbdnqtpgbj .gt_from_md> :last-child { margin-bottom: 0; }
 #hbdnqtpgbj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hbdnqtpgbj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hbdnqtpgbj .gt_indent_1 { text-indent: 5px; }
 #hbdnqtpgbj .gt_indent_2 { text-indent: calc(5px * 2); }
 #hbdnqtpgbj .gt_indent_3 { text-indent: calc(5px * 3); }
 #hbdnqtpgbj .gt_indent_4 { text-indent: calc(5px * 4); }
 #hbdnqtpgbj .gt_indent_5 { text-indent: calc(5px * 5); }
 #hbdnqtpgbj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hbdnqtpgbj .gt_row_group_first td { border-top-width: 2px; }
 #hbdnqtpgbj .gt_row_group_first th { border-top-width: 2px; }
 #hbdnqtpgbj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hbdnqtpgbj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hbdnqtpgbj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hbdnqtpgbj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hbdnqtpgbj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hbdnqtpgbj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hbdnqtpgbj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hbdnqtpgbj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hbdnqtpgbj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hbdnqtpgbj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hbdnqtpgbj .gt_left { text-align: left; }
 #hbdnqtpgbj .gt_center { text-align: center; }
 #hbdnqtpgbj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hbdnqtpgbj .gt_font_normal { font-weight: normal; }
 #hbdnqtpgbj .gt_font_bold { font-weight: bold; }
 #hbdnqtpgbj .gt_font_italic { font-style: italic; }
 #hbdnqtpgbj .gt_super { font-size: 65%; }
 #hbdnqtpgbj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hbdnqtpgbj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hbdnqtpgbj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hbdnqtpgbj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hbdnqtpgbj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hbdnqtpgbj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#gaswldoady table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gaswldoady thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gaswldoady p { margin: 0; padding: 0; }
 #gaswldoady .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gaswldoady .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gaswldoady .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gaswldoady .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gaswldoady .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gaswldoady .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gaswldoady .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gaswldoady .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gaswldoady .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gaswldoady .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gaswldoady .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gaswldoady .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gaswldoady .gt_spanner_row { border-bottom-style: hidden; }
 #gaswldoady .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gaswldoady .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gaswldoady .gt_from_md> :first-child { margin-top: 0; }
 #gaswldoady .gt_from_md> :last-child { margin-bottom: 0; }
 #gaswldoady .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gaswldoady .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gaswldoady .gt_indent_1 { text-indent: 5px; }
 #gaswldoady .gt_indent_2 { text-indent: calc(5px * 2); }
 #gaswldoady .gt_indent_3 { text-indent: calc(5px * 3); }
 #gaswldoady .gt_indent_4 { text-indent: calc(5px * 4); }
 #gaswldoady .gt_indent_5 { text-indent: calc(5px * 5); }
 #gaswldoady .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gaswldoady .gt_row_group_first td { border-top-width: 2px; }
 #gaswldoady .gt_row_group_first th { border-top-width: 2px; }
 #gaswldoady .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gaswldoady .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gaswldoady .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gaswldoady .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gaswldoady .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gaswldoady .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gaswldoady .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gaswldoady .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gaswldoady .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gaswldoady .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gaswldoady .gt_left { text-align: left; }
 #gaswldoady .gt_center { text-align: center; }
 #gaswldoady .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gaswldoady .gt_font_normal { font-weight: normal; }
 #gaswldoady .gt_font_bold { font-weight: bold; }
 #gaswldoady .gt_font_italic { font-style: italic; }
 #gaswldoady .gt_super { font-size: 65%; }
 #gaswldoady .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gaswldoady .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gaswldoady .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gaswldoady .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gaswldoady .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gaswldoady .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#uzywkwykba table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uzywkwykba thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uzywkwykba p { margin: 0; padding: 0; }
 #uzywkwykba .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #uzywkwykba .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uzywkwykba .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uzywkwykba .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uzywkwykba .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uzywkwykba .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uzywkwykba .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uzywkwykba .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uzywkwykba .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uzywkwykba .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uzywkwykba .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uzywkwykba .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uzywkwykba .gt_spanner_row { border-bottom-style: hidden; }
 #uzywkwykba .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uzywkwykba .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #uzywkwykba .gt_from_md> :first-child { margin-top: 0; }
 #uzywkwykba .gt_from_md> :last-child { margin-bottom: 0; }
 #uzywkwykba .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #uzywkwykba .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #uzywkwykba .gt_indent_1 { text-indent: 5px; }
 #uzywkwykba .gt_indent_2 { text-indent: calc(5px * 2); }
 #uzywkwykba .gt_indent_3 { text-indent: calc(5px * 3); }
 #uzywkwykba .gt_indent_4 { text-indent: calc(5px * 4); }
 #uzywkwykba .gt_indent_5 { text-indent: calc(5px * 5); }
 #uzywkwykba .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uzywkwykba .gt_row_group_first td { border-top-width: 2px; }
 #uzywkwykba .gt_row_group_first th { border-top-width: 2px; }
 #uzywkwykba .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uzywkwykba .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uzywkwykba .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uzywkwykba .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uzywkwykba .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uzywkwykba .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uzywkwykba .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uzywkwykba .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uzywkwykba .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uzywkwykba .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uzywkwykba .gt_left { text-align: left; }
 #uzywkwykba .gt_center { text-align: center; }
 #uzywkwykba .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uzywkwykba .gt_font_normal { font-weight: normal; }
 #uzywkwykba .gt_font_bold { font-weight: bold; }
 #uzywkwykba .gt_font_italic { font-style: italic; }
 #uzywkwykba .gt_super { font-size: 65%; }
 #uzywkwykba .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uzywkwykba .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uzywkwykba .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uzywkwykba .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uzywkwykba .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uzywkwykba .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wjholrqihx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wjholrqihx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wjholrqihx p { margin: 0; padding: 0; }
 #wjholrqihx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wjholrqihx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wjholrqihx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wjholrqihx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wjholrqihx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wjholrqihx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjholrqihx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wjholrqihx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wjholrqihx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wjholrqihx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wjholrqihx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wjholrqihx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wjholrqihx .gt_spanner_row { border-bottom-style: hidden; }
 #wjholrqihx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wjholrqihx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wjholrqihx .gt_from_md> :first-child { margin-top: 0; }
 #wjholrqihx .gt_from_md> :last-child { margin-bottom: 0; }
 #wjholrqihx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wjholrqihx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wjholrqihx .gt_indent_1 { text-indent: 5px; }
 #wjholrqihx .gt_indent_2 { text-indent: calc(5px * 2); }
 #wjholrqihx .gt_indent_3 { text-indent: calc(5px * 3); }
 #wjholrqihx .gt_indent_4 { text-indent: calc(5px * 4); }
 #wjholrqihx .gt_indent_5 { text-indent: calc(5px * 5); }
 #wjholrqihx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wjholrqihx .gt_row_group_first td { border-top-width: 2px; }
 #wjholrqihx .gt_row_group_first th { border-top-width: 2px; }
 #wjholrqihx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wjholrqihx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjholrqihx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wjholrqihx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wjholrqihx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjholrqihx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wjholrqihx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wjholrqihx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wjholrqihx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjholrqihx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wjholrqihx .gt_left { text-align: left; }
 #wjholrqihx .gt_center { text-align: center; }
 #wjholrqihx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wjholrqihx .gt_font_normal { font-weight: normal; }
 #wjholrqihx .gt_font_bold { font-weight: bold; }
 #wjholrqihx .gt_font_italic { font-style: italic; }
 #wjholrqihx .gt_super { font-size: 65%; }
 #wjholrqihx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjholrqihx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wjholrqihx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjholrqihx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wjholrqihx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wjholrqihx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hjkogqwudg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hjkogqwudg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hjkogqwudg p { margin: 0; padding: 0; }
 #hjkogqwudg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hjkogqwudg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hjkogqwudg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hjkogqwudg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hjkogqwudg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hjkogqwudg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjkogqwudg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hjkogqwudg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hjkogqwudg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hjkogqwudg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hjkogqwudg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hjkogqwudg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hjkogqwudg .gt_spanner_row { border-bottom-style: hidden; }
 #hjkogqwudg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hjkogqwudg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hjkogqwudg .gt_from_md> :first-child { margin-top: 0; }
 #hjkogqwudg .gt_from_md> :last-child { margin-bottom: 0; }
 #hjkogqwudg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hjkogqwudg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hjkogqwudg .gt_indent_1 { text-indent: 5px; }
 #hjkogqwudg .gt_indent_2 { text-indent: calc(5px * 2); }
 #hjkogqwudg .gt_indent_3 { text-indent: calc(5px * 3); }
 #hjkogqwudg .gt_indent_4 { text-indent: calc(5px * 4); }
 #hjkogqwudg .gt_indent_5 { text-indent: calc(5px * 5); }
 #hjkogqwudg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hjkogqwudg .gt_row_group_first td { border-top-width: 2px; }
 #hjkogqwudg .gt_row_group_first th { border-top-width: 2px; }
 #hjkogqwudg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hjkogqwudg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjkogqwudg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hjkogqwudg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hjkogqwudg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjkogqwudg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hjkogqwudg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hjkogqwudg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hjkogqwudg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjkogqwudg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hjkogqwudg .gt_left { text-align: left; }
 #hjkogqwudg .gt_center { text-align: center; }
 #hjkogqwudg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hjkogqwudg .gt_font_normal { font-weight: normal; }
 #hjkogqwudg .gt_font_bold { font-weight: bold; }
 #hjkogqwudg .gt_font_italic { font-style: italic; }
 #hjkogqwudg .gt_super { font-size: 65%; }
 #hjkogqwudg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjkogqwudg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hjkogqwudg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjkogqwudg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hjkogqwudg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hjkogqwudg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#klppgfiemk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#klppgfiemk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#klppgfiemk p { margin: 0; padding: 0; }
 #klppgfiemk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #klppgfiemk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #klppgfiemk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #klppgfiemk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #klppgfiemk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #klppgfiemk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #klppgfiemk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #klppgfiemk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #klppgfiemk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #klppgfiemk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #klppgfiemk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #klppgfiemk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #klppgfiemk .gt_spanner_row { border-bottom-style: hidden; }
 #klppgfiemk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #klppgfiemk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #klppgfiemk .gt_from_md> :first-child { margin-top: 0; }
 #klppgfiemk .gt_from_md> :last-child { margin-bottom: 0; }
 #klppgfiemk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #klppgfiemk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #klppgfiemk .gt_indent_1 { text-indent: 5px; }
 #klppgfiemk .gt_indent_2 { text-indent: calc(5px * 2); }
 #klppgfiemk .gt_indent_3 { text-indent: calc(5px * 3); }
 #klppgfiemk .gt_indent_4 { text-indent: calc(5px * 4); }
 #klppgfiemk .gt_indent_5 { text-indent: calc(5px * 5); }
 #klppgfiemk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #klppgfiemk .gt_row_group_first td { border-top-width: 2px; }
 #klppgfiemk .gt_row_group_first th { border-top-width: 2px; }
 #klppgfiemk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #klppgfiemk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #klppgfiemk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #klppgfiemk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #klppgfiemk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #klppgfiemk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #klppgfiemk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #klppgfiemk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #klppgfiemk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #klppgfiemk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #klppgfiemk .gt_left { text-align: left; }
 #klppgfiemk .gt_center { text-align: center; }
 #klppgfiemk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #klppgfiemk .gt_font_normal { font-weight: normal; }
 #klppgfiemk .gt_font_bold { font-weight: bold; }
 #klppgfiemk .gt_font_italic { font-style: italic; }
 #klppgfiemk .gt_super { font-size: 65%; }
 #klppgfiemk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #klppgfiemk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #klppgfiemk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #klppgfiemk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #klppgfiemk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #klppgfiemk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th class="gt_row gt_left gt_stub">Ford</th>
<th class="gt_row gt_left gt_stub">GT</th>
<td class="gt_row gt_right">2017</td>
<td class="gt_row gt_right">647.0</td>
</tr>
<tr>
<th rowspan="5" class="gt_row gt_left gt_stub">Ferrari</th>
<th class="gt_row gt_left gt_stub">458 Speciale</th>
<td class="gt_row gt_right">2015</td>
<td class="gt_row gt_right">597.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Spider</th>
<td class="gt_row gt_right">2015</td>
<td class="gt_row gt_right">562.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Italia</th>
<td class="gt_row gt_right">2014</td>
<td class="gt_row gt_right">562.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">488 GTB</th>
<td class="gt_row gt_right">2016</td>
<td class="gt_row gt_right">661.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">California</th>
<td class="gt_row gt_right">2015</td>
<td class="gt_row gt_right">553.0</td>
</tr>
</tbody>
</table>
