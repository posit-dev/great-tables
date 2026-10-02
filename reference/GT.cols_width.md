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
#ostnkybkvk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ostnkybkvk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ostnkybkvk p { margin: 0; padding: 0; }
 #ostnkybkvk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ostnkybkvk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ostnkybkvk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ostnkybkvk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ostnkybkvk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ostnkybkvk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ostnkybkvk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ostnkybkvk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ostnkybkvk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ostnkybkvk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ostnkybkvk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ostnkybkvk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ostnkybkvk .gt_spanner_row { border-bottom-style: hidden; }
 #ostnkybkvk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ostnkybkvk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ostnkybkvk .gt_from_md> :first-child { margin-top: 0; }
 #ostnkybkvk .gt_from_md> :last-child { margin-bottom: 0; }
 #ostnkybkvk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ostnkybkvk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ostnkybkvk .gt_indent_1 { text-indent: 5px; }
 #ostnkybkvk .gt_indent_2 { text-indent: calc(5px * 2); }
 #ostnkybkvk .gt_indent_3 { text-indent: calc(5px * 3); }
 #ostnkybkvk .gt_indent_4 { text-indent: calc(5px * 4); }
 #ostnkybkvk .gt_indent_5 { text-indent: calc(5px * 5); }
 #ostnkybkvk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ostnkybkvk .gt_row_group_first td { border-top-width: 2px; }
 #ostnkybkvk .gt_row_group_first th { border-top-width: 2px; }
 #ostnkybkvk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ostnkybkvk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ostnkybkvk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ostnkybkvk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ostnkybkvk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ostnkybkvk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ostnkybkvk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ostnkybkvk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ostnkybkvk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ostnkybkvk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ostnkybkvk .gt_left { text-align: left; }
 #ostnkybkvk .gt_center { text-align: center; }
 #ostnkybkvk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ostnkybkvk .gt_font_normal { font-weight: normal; }
 #ostnkybkvk .gt_font_bold { font-weight: bold; }
 #ostnkybkvk .gt_font_italic { font-style: italic; }
 #ostnkybkvk .gt_super { font-size: 65%; }
 #ostnkybkvk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ostnkybkvk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ostnkybkvk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ostnkybkvk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ostnkybkvk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ostnkybkvk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#kkwvhsnvwt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kkwvhsnvwt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kkwvhsnvwt p { margin: 0; padding: 0; }
 #kkwvhsnvwt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kkwvhsnvwt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kkwvhsnvwt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kkwvhsnvwt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kkwvhsnvwt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kkwvhsnvwt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkwvhsnvwt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kkwvhsnvwt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kkwvhsnvwt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kkwvhsnvwt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kkwvhsnvwt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kkwvhsnvwt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kkwvhsnvwt .gt_spanner_row { border-bottom-style: hidden; }
 #kkwvhsnvwt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kkwvhsnvwt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kkwvhsnvwt .gt_from_md> :first-child { margin-top: 0; }
 #kkwvhsnvwt .gt_from_md> :last-child { margin-bottom: 0; }
 #kkwvhsnvwt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kkwvhsnvwt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kkwvhsnvwt .gt_indent_1 { text-indent: 5px; }
 #kkwvhsnvwt .gt_indent_2 { text-indent: calc(5px * 2); }
 #kkwvhsnvwt .gt_indent_3 { text-indent: calc(5px * 3); }
 #kkwvhsnvwt .gt_indent_4 { text-indent: calc(5px * 4); }
 #kkwvhsnvwt .gt_indent_5 { text-indent: calc(5px * 5); }
 #kkwvhsnvwt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kkwvhsnvwt .gt_row_group_first td { border-top-width: 2px; }
 #kkwvhsnvwt .gt_row_group_first th { border-top-width: 2px; }
 #kkwvhsnvwt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kkwvhsnvwt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkwvhsnvwt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kkwvhsnvwt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kkwvhsnvwt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkwvhsnvwt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kkwvhsnvwt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kkwvhsnvwt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kkwvhsnvwt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkwvhsnvwt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kkwvhsnvwt .gt_left { text-align: left; }
 #kkwvhsnvwt .gt_center { text-align: center; }
 #kkwvhsnvwt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kkwvhsnvwt .gt_font_normal { font-weight: normal; }
 #kkwvhsnvwt .gt_font_bold { font-weight: bold; }
 #kkwvhsnvwt .gt_font_italic { font-style: italic; }
 #kkwvhsnvwt .gt_super { font-size: 65%; }
 #kkwvhsnvwt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkwvhsnvwt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kkwvhsnvwt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkwvhsnvwt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kkwvhsnvwt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kkwvhsnvwt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#aqbcblxqkj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#aqbcblxqkj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#aqbcblxqkj p { margin: 0; padding: 0; }
 #aqbcblxqkj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #aqbcblxqkj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #aqbcblxqkj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #aqbcblxqkj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #aqbcblxqkj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aqbcblxqkj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aqbcblxqkj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aqbcblxqkj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #aqbcblxqkj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #aqbcblxqkj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #aqbcblxqkj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #aqbcblxqkj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #aqbcblxqkj .gt_spanner_row { border-bottom-style: hidden; }
 #aqbcblxqkj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #aqbcblxqkj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #aqbcblxqkj .gt_from_md> :first-child { margin-top: 0; }
 #aqbcblxqkj .gt_from_md> :last-child { margin-bottom: 0; }
 #aqbcblxqkj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #aqbcblxqkj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #aqbcblxqkj .gt_indent_1 { text-indent: 5px; }
 #aqbcblxqkj .gt_indent_2 { text-indent: calc(5px * 2); }
 #aqbcblxqkj .gt_indent_3 { text-indent: calc(5px * 3); }
 #aqbcblxqkj .gt_indent_4 { text-indent: calc(5px * 4); }
 #aqbcblxqkj .gt_indent_5 { text-indent: calc(5px * 5); }
 #aqbcblxqkj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #aqbcblxqkj .gt_row_group_first td { border-top-width: 2px; }
 #aqbcblxqkj .gt_row_group_first th { border-top-width: 2px; }
 #aqbcblxqkj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #aqbcblxqkj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aqbcblxqkj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aqbcblxqkj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #aqbcblxqkj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aqbcblxqkj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aqbcblxqkj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #aqbcblxqkj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #aqbcblxqkj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aqbcblxqkj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aqbcblxqkj .gt_left { text-align: left; }
 #aqbcblxqkj .gt_center { text-align: center; }
 #aqbcblxqkj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #aqbcblxqkj .gt_font_normal { font-weight: normal; }
 #aqbcblxqkj .gt_font_bold { font-weight: bold; }
 #aqbcblxqkj .gt_font_italic { font-style: italic; }
 #aqbcblxqkj .gt_super { font-size: 65%; }
 #aqbcblxqkj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aqbcblxqkj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #aqbcblxqkj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aqbcblxqkj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aqbcblxqkj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #aqbcblxqkj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rhxlgpqpvw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rhxlgpqpvw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rhxlgpqpvw p { margin: 0; padding: 0; }
 #rhxlgpqpvw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rhxlgpqpvw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rhxlgpqpvw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rhxlgpqpvw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rhxlgpqpvw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rhxlgpqpvw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rhxlgpqpvw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rhxlgpqpvw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rhxlgpqpvw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rhxlgpqpvw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rhxlgpqpvw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rhxlgpqpvw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rhxlgpqpvw .gt_spanner_row { border-bottom-style: hidden; }
 #rhxlgpqpvw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rhxlgpqpvw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rhxlgpqpvw .gt_from_md> :first-child { margin-top: 0; }
 #rhxlgpqpvw .gt_from_md> :last-child { margin-bottom: 0; }
 #rhxlgpqpvw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rhxlgpqpvw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rhxlgpqpvw .gt_indent_1 { text-indent: 5px; }
 #rhxlgpqpvw .gt_indent_2 { text-indent: calc(5px * 2); }
 #rhxlgpqpvw .gt_indent_3 { text-indent: calc(5px * 3); }
 #rhxlgpqpvw .gt_indent_4 { text-indent: calc(5px * 4); }
 #rhxlgpqpvw .gt_indent_5 { text-indent: calc(5px * 5); }
 #rhxlgpqpvw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rhxlgpqpvw .gt_row_group_first td { border-top-width: 2px; }
 #rhxlgpqpvw .gt_row_group_first th { border-top-width: 2px; }
 #rhxlgpqpvw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rhxlgpqpvw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rhxlgpqpvw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rhxlgpqpvw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rhxlgpqpvw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rhxlgpqpvw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rhxlgpqpvw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rhxlgpqpvw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rhxlgpqpvw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rhxlgpqpvw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rhxlgpqpvw .gt_left { text-align: left; }
 #rhxlgpqpvw .gt_center { text-align: center; }
 #rhxlgpqpvw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rhxlgpqpvw .gt_font_normal { font-weight: normal; }
 #rhxlgpqpvw .gt_font_bold { font-weight: bold; }
 #rhxlgpqpvw .gt_font_italic { font-style: italic; }
 #rhxlgpqpvw .gt_super { font-size: 65%; }
 #rhxlgpqpvw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rhxlgpqpvw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rhxlgpqpvw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rhxlgpqpvw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rhxlgpqpvw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rhxlgpqpvw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ocpklwzdcx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ocpklwzdcx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ocpklwzdcx p { margin: 0; padding: 0; }
 #ocpklwzdcx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ocpklwzdcx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ocpklwzdcx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ocpklwzdcx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ocpklwzdcx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ocpklwzdcx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ocpklwzdcx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ocpklwzdcx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ocpklwzdcx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ocpklwzdcx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ocpklwzdcx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ocpklwzdcx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ocpklwzdcx .gt_spanner_row { border-bottom-style: hidden; }
 #ocpklwzdcx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ocpklwzdcx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ocpklwzdcx .gt_from_md> :first-child { margin-top: 0; }
 #ocpklwzdcx .gt_from_md> :last-child { margin-bottom: 0; }
 #ocpklwzdcx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ocpklwzdcx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ocpklwzdcx .gt_indent_1 { text-indent: 5px; }
 #ocpklwzdcx .gt_indent_2 { text-indent: calc(5px * 2); }
 #ocpklwzdcx .gt_indent_3 { text-indent: calc(5px * 3); }
 #ocpklwzdcx .gt_indent_4 { text-indent: calc(5px * 4); }
 #ocpklwzdcx .gt_indent_5 { text-indent: calc(5px * 5); }
 #ocpklwzdcx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ocpklwzdcx .gt_row_group_first td { border-top-width: 2px; }
 #ocpklwzdcx .gt_row_group_first th { border-top-width: 2px; }
 #ocpklwzdcx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ocpklwzdcx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ocpklwzdcx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ocpklwzdcx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ocpklwzdcx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ocpklwzdcx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ocpklwzdcx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ocpklwzdcx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ocpklwzdcx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ocpklwzdcx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ocpklwzdcx .gt_left { text-align: left; }
 #ocpklwzdcx .gt_center { text-align: center; }
 #ocpklwzdcx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ocpklwzdcx .gt_font_normal { font-weight: normal; }
 #ocpklwzdcx .gt_font_bold { font-weight: bold; }
 #ocpklwzdcx .gt_font_italic { font-style: italic; }
 #ocpklwzdcx .gt_super { font-size: 65%; }
 #ocpklwzdcx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ocpklwzdcx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ocpklwzdcx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ocpklwzdcx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ocpklwzdcx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ocpklwzdcx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|              | year | hp    | msrp     |
|--------------|------|-------|----------|
| GT           | 2017 | 647.0 | 447000.0 |
| 458 Speciale | 2015 | 597.0 | 291744.0 |
| 458 Spider   | 2015 | 562.0 | 263553.0 |
| 458 Italia   | 2014 | 562.0 | 233509.0 |
| 488 GTB      | 2016 | 661.0 | 245400.0 |
| California   | 2015 | 553.0 | 198973.0 |
