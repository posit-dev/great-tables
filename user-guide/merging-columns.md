# Merging Columns

Tables often contain related data spread across multiple columns that would be better presented as a single, combined value. For example, a measurement and its uncertainty, a low and high bound forming a range, or a count with its corresponding percentage. The `cols_merge*()` family of methods combines the content of two or more columns into one, giving you a more compact and readable table.

Merging works best when two columns are conceptually a single value: a measurement and its uncertainty, a low and high bound forming a range, or a count paired with its percentage. In these cases, presenting the values separately forces the reader to mentally combine them anyway. If, however, the columns represent independent quantities that a reader might want to compare on their own (say, revenue and profit), keep them as separate columns so each value can be scanned independently.


# Setting Up the Example Data

We will use a small dataset that includes a measurement with uncertainty, a range, and a count with a percentage.


``` python
import pandas as pd
from great_tables import GT

experiment_df = pd.DataFrame({
    "trial": ["Trial 1", "Trial 2", "Trial 3", "Trial 4"],
    "measurement": [12.45, 8.92, 15.03, None],
    "uncertainty": [0.32, 0.15, 0.48, None],
    "low": [10.5, 7.8, 13.2, 9.1],
    "high": [14.2, 10.1, 16.8, 12.5],
    "n_obs": [120, 85, 200, 0],
    "pct": [34.2, 24.3, 57.1, 0.0],
})

gt_tbl = GT(experiment_df, rowname_col="trial")
gt_tbl
```


<style>
#ayhosgsxta table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ayhosgsxta thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ayhosgsxta p { margin: 0; padding: 0; }
 #ayhosgsxta .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ayhosgsxta .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ayhosgsxta .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ayhosgsxta .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ayhosgsxta .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ayhosgsxta .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ayhosgsxta .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ayhosgsxta .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ayhosgsxta .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ayhosgsxta .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ayhosgsxta .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ayhosgsxta .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ayhosgsxta .gt_spanner_row { border-bottom-style: hidden; }
 #ayhosgsxta .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ayhosgsxta .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ayhosgsxta .gt_from_md> :first-child { margin-top: 0; }
 #ayhosgsxta .gt_from_md> :last-child { margin-bottom: 0; }
 #ayhosgsxta .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ayhosgsxta .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ayhosgsxta .gt_indent_1 { text-indent: 5px; }
 #ayhosgsxta .gt_indent_2 { text-indent: calc(5px * 2); }
 #ayhosgsxta .gt_indent_3 { text-indent: calc(5px * 3); }
 #ayhosgsxta .gt_indent_4 { text-indent: calc(5px * 4); }
 #ayhosgsxta .gt_indent_5 { text-indent: calc(5px * 5); }
 #ayhosgsxta .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ayhosgsxta .gt_row_group_first td { border-top-width: 2px; }
 #ayhosgsxta .gt_row_group_first th { border-top-width: 2px; }
 #ayhosgsxta .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ayhosgsxta .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ayhosgsxta .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ayhosgsxta .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ayhosgsxta .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ayhosgsxta .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ayhosgsxta .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ayhosgsxta .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ayhosgsxta .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ayhosgsxta .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ayhosgsxta .gt_left { text-align: left; }
 #ayhosgsxta .gt_center { text-align: center; }
 #ayhosgsxta .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ayhosgsxta .gt_font_normal { font-weight: normal; }
 #ayhosgsxta .gt_font_bold { font-weight: bold; }
 #ayhosgsxta .gt_font_italic { font-style: italic; }
 #ayhosgsxta .gt_super { font-size: 65%; }
 #ayhosgsxta .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ayhosgsxta .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ayhosgsxta .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ayhosgsxta .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ayhosgsxta .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ayhosgsxta .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | measurement | uncertainty | low  | high | n_obs | pct  |
|---------|-------------|-------------|------|------|-------|------|
| Trial 1 | 12.45       | 0.32        | 10.5 | 14.2 | 120   | 34.2 |
| Trial 2 | 8.92        | 0.15        | 7.8  | 10.1 | 85    | 24.3 |
| Trial 3 | 15.03       | 0.48        | 13.2 | 16.8 | 200   | 57.1 |
| Trial 4 | None        | None        | 9.1  | 12.5 | 0     | 0.0  |


With six data columns, this table is quite wide. Let's reduce the column count by merging related pairs together.


# Merging with a Pattern

The most general method is [cols_merge()](../reference/GT.cols_merge.md#great_tables.GT.cols_merge). It takes a `columns=` list where the first column becomes the target (the one that receives the merged content), and a `pattern=` string that controls how column values are combined. In the pattern, `{0}` refers to the first column, `{1}` to the second, and so on.


``` python
(
    GT(experiment_df, rowname_col="trial")
    .cols_merge(
        columns=["measurement", "uncertainty"],
        pattern="{0} ± {1}"
    )
)
```


<style>
#cnwbbfptvm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cnwbbfptvm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cnwbbfptvm p { margin: 0; padding: 0; }
 #cnwbbfptvm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cnwbbfptvm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cnwbbfptvm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cnwbbfptvm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cnwbbfptvm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cnwbbfptvm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cnwbbfptvm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cnwbbfptvm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cnwbbfptvm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cnwbbfptvm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cnwbbfptvm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cnwbbfptvm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cnwbbfptvm .gt_spanner_row { border-bottom-style: hidden; }
 #cnwbbfptvm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cnwbbfptvm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cnwbbfptvm .gt_from_md> :first-child { margin-top: 0; }
 #cnwbbfptvm .gt_from_md> :last-child { margin-bottom: 0; }
 #cnwbbfptvm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cnwbbfptvm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cnwbbfptvm .gt_indent_1 { text-indent: 5px; }
 #cnwbbfptvm .gt_indent_2 { text-indent: calc(5px * 2); }
 #cnwbbfptvm .gt_indent_3 { text-indent: calc(5px * 3); }
 #cnwbbfptvm .gt_indent_4 { text-indent: calc(5px * 4); }
 #cnwbbfptvm .gt_indent_5 { text-indent: calc(5px * 5); }
 #cnwbbfptvm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cnwbbfptvm .gt_row_group_first td { border-top-width: 2px; }
 #cnwbbfptvm .gt_row_group_first th { border-top-width: 2px; }
 #cnwbbfptvm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cnwbbfptvm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cnwbbfptvm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cnwbbfptvm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cnwbbfptvm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cnwbbfptvm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cnwbbfptvm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cnwbbfptvm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cnwbbfptvm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cnwbbfptvm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cnwbbfptvm .gt_left { text-align: left; }
 #cnwbbfptvm .gt_center { text-align: center; }
 #cnwbbfptvm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cnwbbfptvm .gt_font_normal { font-weight: normal; }
 #cnwbbfptvm .gt_font_bold { font-weight: bold; }
 #cnwbbfptvm .gt_font_italic { font-style: italic; }
 #cnwbbfptvm .gt_super { font-size: 65%; }
 #cnwbbfptvm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cnwbbfptvm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cnwbbfptvm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cnwbbfptvm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cnwbbfptvm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cnwbbfptvm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | measurement  | low  | high | n_obs | pct  |
|---------|--------------|------|------|-------|------|
| Trial 1 | 12.45 ± 0.32 | 10.5 | 14.2 | 120   | 34.2 |
| Trial 2 | 8.92 ± 0.15  | 7.8  | 10.1 | 85    | 24.3 |
| Trial 3 | 15.03 ± 0.48 | 13.2 | 16.8 | 200   | 57.1 |
| Trial 4 | NA ± NA      | 9.1  | 12.5 | 0     | 0.0  |


The `measurement` column now contains the merged text and the `uncertainty` column is automatically hidden. This hiding behavior can be controlled with the `hide_columns=` argument.


## Conditional Content with `<<>>`

Sometimes a column value may be missing, and you want the merged text to adapt gracefully. Wrapping part of the pattern in double angle brackets (`<<...>>`) makes that section conditional: it will be omitted entirely if any referenced column value inside is missing.


``` python
(
    GT(experiment_df, rowname_col="trial")
    .cols_merge(
        columns=["measurement", "uncertainty"],
        pattern="{0}<< ± {1}>>"
    )
)
```


<style>
#yklzagiquk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#yklzagiquk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#yklzagiquk p { margin: 0; padding: 0; }
 #yklzagiquk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #yklzagiquk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #yklzagiquk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #yklzagiquk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #yklzagiquk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yklzagiquk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yklzagiquk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yklzagiquk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #yklzagiquk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #yklzagiquk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #yklzagiquk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #yklzagiquk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #yklzagiquk .gt_spanner_row { border-bottom-style: hidden; }
 #yklzagiquk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #yklzagiquk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #yklzagiquk .gt_from_md> :first-child { margin-top: 0; }
 #yklzagiquk .gt_from_md> :last-child { margin-bottom: 0; }
 #yklzagiquk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #yklzagiquk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #yklzagiquk .gt_indent_1 { text-indent: 5px; }
 #yklzagiquk .gt_indent_2 { text-indent: calc(5px * 2); }
 #yklzagiquk .gt_indent_3 { text-indent: calc(5px * 3); }
 #yklzagiquk .gt_indent_4 { text-indent: calc(5px * 4); }
 #yklzagiquk .gt_indent_5 { text-indent: calc(5px * 5); }
 #yklzagiquk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #yklzagiquk .gt_row_group_first td { border-top-width: 2px; }
 #yklzagiquk .gt_row_group_first th { border-top-width: 2px; }
 #yklzagiquk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #yklzagiquk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yklzagiquk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yklzagiquk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #yklzagiquk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yklzagiquk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yklzagiquk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #yklzagiquk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #yklzagiquk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yklzagiquk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yklzagiquk .gt_left { text-align: left; }
 #yklzagiquk .gt_center { text-align: center; }
 #yklzagiquk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #yklzagiquk .gt_font_normal { font-weight: normal; }
 #yklzagiquk .gt_font_bold { font-weight: bold; }
 #yklzagiquk .gt_font_italic { font-style: italic; }
 #yklzagiquk .gt_super { font-size: 65%; }
 #yklzagiquk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yklzagiquk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #yklzagiquk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yklzagiquk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yklzagiquk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #yklzagiquk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | measurement  | low  | high | n_obs | pct  |
|---------|--------------|------|------|-------|------|
| Trial 1 | 12.45 ± 0.32 | 10.5 | 14.2 | 120   | 34.2 |
| Trial 2 | 8.92 ± 0.15  | 7.8  | 10.1 | 85    | 24.3 |
| Trial 3 | 15.03 ± 0.48 | 13.2 | 16.8 | 200   | 57.1 |
| Trial 4 | NA           | 9.1  | 12.5 | 0     | 0.0  |


In this example, Trial 4 has missing values for both columns. The conditional section `<< ± {1}>>` is dropped when `uncertainty` is missing, producing a cleaner result than showing placeholder text.

Handling missing values gracefully matters because real-world data is rarely complete: not every row will have values for every field. Without the `<<>>` syntax, the merged cell might display awkward artifacts like " ± " with nothing around it. Conditional sections let the pattern degrade naturally, showing only the parts that have actual data behind them.


# Merging Value and Uncertainty

The [cols_merge_uncert()](../reference/GT.cols_merge_uncert.md#great_tables.GT.cols_merge_uncert) method is a convenience wrapper specifically designed for the common pattern of a measurement paired with its uncertainty. It handles missing values automatically and renders the separator as a proper plus-minus sign.


``` python
(
    GT(experiment_df, rowname_col="trial")
    .cols_merge_uncert(col_val="measurement", col_uncert="uncertainty")
)
```


<style>
#bswevlrxeb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bswevlrxeb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bswevlrxeb p { margin: 0; padding: 0; }
 #bswevlrxeb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bswevlrxeb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bswevlrxeb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bswevlrxeb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bswevlrxeb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bswevlrxeb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bswevlrxeb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bswevlrxeb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bswevlrxeb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bswevlrxeb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bswevlrxeb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bswevlrxeb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bswevlrxeb .gt_spanner_row { border-bottom-style: hidden; }
 #bswevlrxeb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bswevlrxeb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bswevlrxeb .gt_from_md> :first-child { margin-top: 0; }
 #bswevlrxeb .gt_from_md> :last-child { margin-bottom: 0; }
 #bswevlrxeb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bswevlrxeb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bswevlrxeb .gt_indent_1 { text-indent: 5px; }
 #bswevlrxeb .gt_indent_2 { text-indent: calc(5px * 2); }
 #bswevlrxeb .gt_indent_3 { text-indent: calc(5px * 3); }
 #bswevlrxeb .gt_indent_4 { text-indent: calc(5px * 4); }
 #bswevlrxeb .gt_indent_5 { text-indent: calc(5px * 5); }
 #bswevlrxeb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bswevlrxeb .gt_row_group_first td { border-top-width: 2px; }
 #bswevlrxeb .gt_row_group_first th { border-top-width: 2px; }
 #bswevlrxeb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bswevlrxeb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bswevlrxeb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bswevlrxeb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bswevlrxeb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bswevlrxeb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bswevlrxeb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bswevlrxeb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bswevlrxeb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bswevlrxeb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bswevlrxeb .gt_left { text-align: left; }
 #bswevlrxeb .gt_center { text-align: center; }
 #bswevlrxeb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bswevlrxeb .gt_font_normal { font-weight: normal; }
 #bswevlrxeb .gt_font_bold { font-weight: bold; }
 #bswevlrxeb .gt_font_italic { font-style: italic; }
 #bswevlrxeb .gt_super { font-size: 65%; }
 #bswevlrxeb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bswevlrxeb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bswevlrxeb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bswevlrxeb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bswevlrxeb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bswevlrxeb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | measurement  | low  | high | n_obs | pct  |
|---------|--------------|------|------|-------|------|
| Trial 1 | 12.45 ± 0.32 | 10.5 | 14.2 | 120   | 34.2 |
| Trial 2 | 8.92 ± 0.15  | 7.8  | 10.1 | 85    | 24.3 |
| Trial 3 | 15.03 ± 0.48 | 13.2 | 16.8 | 200   | 57.1 |
| Trial 4 |              | 9.1  | 12.5 | 0     | 0.0  |


The `sep=` argument controls the text between the value and uncertainty (defaulting to `" ± "`). You can combine this with [fmt_number()](../reference/GT.fmt_number.md#great_tables.GT.fmt_number) to control the decimal precision of the merged values.


``` python
(
    GT(experiment_df, rowname_col="trial")
    .fmt_number(columns=["measurement", "uncertainty"], decimals=1)
    .cols_merge_uncert(col_val="measurement", col_uncert="uncertainty")
)
```


<style>
#budtagqnwr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#budtagqnwr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#budtagqnwr p { margin: 0; padding: 0; }
 #budtagqnwr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #budtagqnwr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #budtagqnwr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #budtagqnwr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #budtagqnwr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #budtagqnwr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #budtagqnwr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #budtagqnwr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #budtagqnwr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #budtagqnwr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #budtagqnwr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #budtagqnwr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #budtagqnwr .gt_spanner_row { border-bottom-style: hidden; }
 #budtagqnwr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #budtagqnwr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #budtagqnwr .gt_from_md> :first-child { margin-top: 0; }
 #budtagqnwr .gt_from_md> :last-child { margin-bottom: 0; }
 #budtagqnwr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #budtagqnwr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #budtagqnwr .gt_indent_1 { text-indent: 5px; }
 #budtagqnwr .gt_indent_2 { text-indent: calc(5px * 2); }
 #budtagqnwr .gt_indent_3 { text-indent: calc(5px * 3); }
 #budtagqnwr .gt_indent_4 { text-indent: calc(5px * 4); }
 #budtagqnwr .gt_indent_5 { text-indent: calc(5px * 5); }
 #budtagqnwr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #budtagqnwr .gt_row_group_first td { border-top-width: 2px; }
 #budtagqnwr .gt_row_group_first th { border-top-width: 2px; }
 #budtagqnwr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #budtagqnwr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #budtagqnwr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #budtagqnwr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #budtagqnwr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #budtagqnwr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #budtagqnwr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #budtagqnwr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #budtagqnwr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #budtagqnwr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #budtagqnwr .gt_left { text-align: left; }
 #budtagqnwr .gt_center { text-align: center; }
 #budtagqnwr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #budtagqnwr .gt_font_normal { font-weight: normal; }
 #budtagqnwr .gt_font_bold { font-weight: bold; }
 #budtagqnwr .gt_font_italic { font-style: italic; }
 #budtagqnwr .gt_super { font-size: 65%; }
 #budtagqnwr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #budtagqnwr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #budtagqnwr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #budtagqnwr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #budtagqnwr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #budtagqnwr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | measurement | low  | high | n_obs | pct  |
|---------|-------------|------|------|-------|------|
| Trial 1 | 12.4 ± 0.3  | 10.5 | 14.2 | 120   | 34.2 |
| Trial 2 | 8.9 ± 0.1   | 7.8  | 10.1 | 85    | 24.3 |
| Trial 3 | 15.0 ± 0.5  | 13.2 | 16.8 | 200   | 57.1 |
| Trial 4 |             | 9.1  | 12.5 | 0     | 0.0  |


Formatting should be applied before merging, since the merge operates on the already-formatted text content.


# Merging a Range

The [cols_merge_range()](../reference/GT.cols_merge_range.md#great_tables.GT.cols_merge_range) method combines two columns into a range display, separated by an en dash by default. This is ideal for confidence intervals, date ranges, or any pair of low/high bounds.


``` python
(
    GT(experiment_df, rowname_col="trial")
    .cols_merge_range(col_begin="low", col_end="high")
)
```


<style>
#kzqeegbmyy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kzqeegbmyy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kzqeegbmyy p { margin: 0; padding: 0; }
 #kzqeegbmyy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kzqeegbmyy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kzqeegbmyy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kzqeegbmyy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kzqeegbmyy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kzqeegbmyy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kzqeegbmyy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kzqeegbmyy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kzqeegbmyy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kzqeegbmyy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kzqeegbmyy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kzqeegbmyy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kzqeegbmyy .gt_spanner_row { border-bottom-style: hidden; }
 #kzqeegbmyy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kzqeegbmyy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kzqeegbmyy .gt_from_md> :first-child { margin-top: 0; }
 #kzqeegbmyy .gt_from_md> :last-child { margin-bottom: 0; }
 #kzqeegbmyy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kzqeegbmyy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kzqeegbmyy .gt_indent_1 { text-indent: 5px; }
 #kzqeegbmyy .gt_indent_2 { text-indent: calc(5px * 2); }
 #kzqeegbmyy .gt_indent_3 { text-indent: calc(5px * 3); }
 #kzqeegbmyy .gt_indent_4 { text-indent: calc(5px * 4); }
 #kzqeegbmyy .gt_indent_5 { text-indent: calc(5px * 5); }
 #kzqeegbmyy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kzqeegbmyy .gt_row_group_first td { border-top-width: 2px; }
 #kzqeegbmyy .gt_row_group_first th { border-top-width: 2px; }
 #kzqeegbmyy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kzqeegbmyy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kzqeegbmyy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kzqeegbmyy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kzqeegbmyy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kzqeegbmyy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kzqeegbmyy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kzqeegbmyy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kzqeegbmyy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kzqeegbmyy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kzqeegbmyy .gt_left { text-align: left; }
 #kzqeegbmyy .gt_center { text-align: center; }
 #kzqeegbmyy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kzqeegbmyy .gt_font_normal { font-weight: normal; }
 #kzqeegbmyy .gt_font_bold { font-weight: bold; }
 #kzqeegbmyy .gt_font_italic { font-style: italic; }
 #kzqeegbmyy .gt_super { font-size: 65%; }
 #kzqeegbmyy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kzqeegbmyy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kzqeegbmyy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kzqeegbmyy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kzqeegbmyy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kzqeegbmyy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | measurement | uncertainty | low       | n_obs | pct  |
|---------|-------------|-------------|-----------|-------|------|
| Trial 1 | 12.45       | 0.32        | 10.5-14.2 | 120   | 34.2 |
| Trial 2 | 8.92        | 0.15        | 7.8-10.1  | 85    | 24.3 |
| Trial 3 | 15.03       | 0.48        | 13.2-16.8 | 200   | 57.1 |
| Trial 4 | None        | None        | 9.1-12.5  | 0     | 0.0  |


You can customize the separator with `sep=`. The special values `"--"` and `"---"` are automatically rendered as an en dash and em dash, respectively. Any other string is used literally.


``` python
(
    GT(experiment_df, rowname_col="trial")
    .cols_merge_range(col_begin="low", col_end="high", sep=" to ")
)
```


<style>
#lhfquzsyea table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lhfquzsyea thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lhfquzsyea p { margin: 0; padding: 0; }
 #lhfquzsyea .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lhfquzsyea .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lhfquzsyea .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lhfquzsyea .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lhfquzsyea .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lhfquzsyea .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lhfquzsyea .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lhfquzsyea .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lhfquzsyea .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lhfquzsyea .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lhfquzsyea .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lhfquzsyea .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lhfquzsyea .gt_spanner_row { border-bottom-style: hidden; }
 #lhfquzsyea .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lhfquzsyea .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lhfquzsyea .gt_from_md> :first-child { margin-top: 0; }
 #lhfquzsyea .gt_from_md> :last-child { margin-bottom: 0; }
 #lhfquzsyea .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lhfquzsyea .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lhfquzsyea .gt_indent_1 { text-indent: 5px; }
 #lhfquzsyea .gt_indent_2 { text-indent: calc(5px * 2); }
 #lhfquzsyea .gt_indent_3 { text-indent: calc(5px * 3); }
 #lhfquzsyea .gt_indent_4 { text-indent: calc(5px * 4); }
 #lhfquzsyea .gt_indent_5 { text-indent: calc(5px * 5); }
 #lhfquzsyea .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lhfquzsyea .gt_row_group_first td { border-top-width: 2px; }
 #lhfquzsyea .gt_row_group_first th { border-top-width: 2px; }
 #lhfquzsyea .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lhfquzsyea .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lhfquzsyea .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lhfquzsyea .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lhfquzsyea .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lhfquzsyea .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lhfquzsyea .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lhfquzsyea .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lhfquzsyea .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lhfquzsyea .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lhfquzsyea .gt_left { text-align: left; }
 #lhfquzsyea .gt_center { text-align: center; }
 #lhfquzsyea .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lhfquzsyea .gt_font_normal { font-weight: normal; }
 #lhfquzsyea .gt_font_bold { font-weight: bold; }
 #lhfquzsyea .gt_font_italic { font-style: italic; }
 #lhfquzsyea .gt_super { font-size: 65%; }
 #lhfquzsyea .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lhfquzsyea .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lhfquzsyea .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lhfquzsyea .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lhfquzsyea .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lhfquzsyea .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | measurement | uncertainty | low          | n_obs | pct  |
|---------|-------------|-------------|--------------|-------|------|
| Trial 1 | 12.45       | 0.32        | 10.5 to 14.2 | 120   | 34.2 |
| Trial 2 | 8.92        | 0.15        | 7.8 to 10.1  | 85    | 24.3 |
| Trial 3 | 15.03       | 0.48        | 13.2 to 16.8 | 200   | 57.1 |
| Trial 4 | None        | None        | 9.1 to 12.5  | 0     | 0.0  |


# Merging Count and Percentage

When you have a count column alongside a pre-computed percentage column, [cols_merge_n_pct()](../reference/GT.cols_merge_n_pct.md#great_tables.GT.cols_merge_n_pct) merges them into a format like `"120 (34.2%)"`. This is a common pattern in statistical tables and survey results.


``` python
(
    GT(experiment_df, rowname_col="trial")
    .cols_merge_n_pct(col_n="n_obs", col_pct="pct")
)
```


<style>
#sxqfevlzrr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sxqfevlzrr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sxqfevlzrr p { margin: 0; padding: 0; }
 #sxqfevlzrr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sxqfevlzrr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sxqfevlzrr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sxqfevlzrr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sxqfevlzrr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sxqfevlzrr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sxqfevlzrr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sxqfevlzrr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sxqfevlzrr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sxqfevlzrr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sxqfevlzrr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sxqfevlzrr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sxqfevlzrr .gt_spanner_row { border-bottom-style: hidden; }
 #sxqfevlzrr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sxqfevlzrr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sxqfevlzrr .gt_from_md> :first-child { margin-top: 0; }
 #sxqfevlzrr .gt_from_md> :last-child { margin-bottom: 0; }
 #sxqfevlzrr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sxqfevlzrr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sxqfevlzrr .gt_indent_1 { text-indent: 5px; }
 #sxqfevlzrr .gt_indent_2 { text-indent: calc(5px * 2); }
 #sxqfevlzrr .gt_indent_3 { text-indent: calc(5px * 3); }
 #sxqfevlzrr .gt_indent_4 { text-indent: calc(5px * 4); }
 #sxqfevlzrr .gt_indent_5 { text-indent: calc(5px * 5); }
 #sxqfevlzrr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sxqfevlzrr .gt_row_group_first td { border-top-width: 2px; }
 #sxqfevlzrr .gt_row_group_first th { border-top-width: 2px; }
 #sxqfevlzrr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sxqfevlzrr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sxqfevlzrr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sxqfevlzrr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sxqfevlzrr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sxqfevlzrr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sxqfevlzrr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sxqfevlzrr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sxqfevlzrr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sxqfevlzrr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sxqfevlzrr .gt_left { text-align: left; }
 #sxqfevlzrr .gt_center { text-align: center; }
 #sxqfevlzrr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sxqfevlzrr .gt_font_normal { font-weight: normal; }
 #sxqfevlzrr .gt_font_bold { font-weight: bold; }
 #sxqfevlzrr .gt_font_italic { font-style: italic; }
 #sxqfevlzrr .gt_super { font-size: 65%; }
 #sxqfevlzrr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sxqfevlzrr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sxqfevlzrr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sxqfevlzrr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sxqfevlzrr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sxqfevlzrr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | measurement | uncertainty | low  | high | n_obs      |
|---------|-------------|-------------|------|------|------------|
| Trial 1 | 12.45       | 0.32        | 10.5 | 14.2 | 120 (34.2) |
| Trial 2 | 8.92        | 0.15        | 7.8  | 10.1 | 85 (24.3)  |
| Trial 3 | 15.03       | 0.48        | 13.2 | 16.8 | 200 (57.1) |
| Trial 4 | None        | None        | 9.1  | 12.5 | 0          |


Notice that Trial 4 shows `"0"` without a percentage. This is intentional: when the count is zero, showing `"0 (0.0%)"` would be redundant, so the method displays only the count.


# Combining Multiple Merges

You can apply several merge operations in the same table to consolidate all related column pairs at once.


``` python
(
    GT(experiment_df, rowname_col="trial")
    .fmt_number(columns=["measurement", "uncertainty", "low", "high"], decimals=1)
    .cols_merge_uncert(col_val="measurement", col_uncert="uncertainty")
    .cols_merge_range(col_begin="low", col_end="high")
    .cols_merge_n_pct(col_n="n_obs", col_pct="pct")
    .cols_label(
        measurement="Result",
        low="Range",
        n_obs="Observations"
    )
)
```


<style>
#gsiqpvkwee table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gsiqpvkwee thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gsiqpvkwee p { margin: 0; padding: 0; }
 #gsiqpvkwee .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gsiqpvkwee .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gsiqpvkwee .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gsiqpvkwee .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gsiqpvkwee .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gsiqpvkwee .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gsiqpvkwee .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gsiqpvkwee .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gsiqpvkwee .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gsiqpvkwee .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gsiqpvkwee .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gsiqpvkwee .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gsiqpvkwee .gt_spanner_row { border-bottom-style: hidden; }
 #gsiqpvkwee .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gsiqpvkwee .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gsiqpvkwee .gt_from_md> :first-child { margin-top: 0; }
 #gsiqpvkwee .gt_from_md> :last-child { margin-bottom: 0; }
 #gsiqpvkwee .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gsiqpvkwee .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gsiqpvkwee .gt_indent_1 { text-indent: 5px; }
 #gsiqpvkwee .gt_indent_2 { text-indent: calc(5px * 2); }
 #gsiqpvkwee .gt_indent_3 { text-indent: calc(5px * 3); }
 #gsiqpvkwee .gt_indent_4 { text-indent: calc(5px * 4); }
 #gsiqpvkwee .gt_indent_5 { text-indent: calc(5px * 5); }
 #gsiqpvkwee .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gsiqpvkwee .gt_row_group_first td { border-top-width: 2px; }
 #gsiqpvkwee .gt_row_group_first th { border-top-width: 2px; }
 #gsiqpvkwee .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gsiqpvkwee .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gsiqpvkwee .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gsiqpvkwee .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gsiqpvkwee .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gsiqpvkwee .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gsiqpvkwee .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gsiqpvkwee .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gsiqpvkwee .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gsiqpvkwee .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gsiqpvkwee .gt_left { text-align: left; }
 #gsiqpvkwee .gt_center { text-align: center; }
 #gsiqpvkwee .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gsiqpvkwee .gt_font_normal { font-weight: normal; }
 #gsiqpvkwee .gt_font_bold { font-weight: bold; }
 #gsiqpvkwee .gt_font_italic { font-style: italic; }
 #gsiqpvkwee .gt_super { font-size: 65%; }
 #gsiqpvkwee .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gsiqpvkwee .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gsiqpvkwee .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gsiqpvkwee .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gsiqpvkwee .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gsiqpvkwee .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | Result     | Range     | Observations |
|---------|------------|-----------|--------------|
| Trial 1 | 12.4 ± 0.3 | 10.5-14.2 | 120 (34.2)   |
| Trial 2 | 8.9 ± 0.1  | 7.8-10.1  | 85 (24.3)    |
| Trial 3 | 15.0 ± 0.5 | 13.2-16.8 | 200 (57.1)   |
| Trial 4 |            | 9.1-12.5  | 0            |


By merging three pairs of columns, we reduced the table from six data columns down to three, each conveying the same information in a more compact form.

Column merging is a powerful technique for building information-dense tables. By combining related values into unified columns, you reduce visual clutter and help readers process the data more efficiently. The specialized [cols_merge_uncert()](../reference/GT.cols_merge_uncert.md#great_tables.GT.cols_merge_uncert), [cols_merge_range()](../reference/GT.cols_merge_range.md#great_tables.GT.cols_merge_range), and [cols_merge_n_pct()](../reference/GT.cols_merge_n_pct.md#great_tables.GT.cols_merge_n_pct) methods handle the most common patterns, while [cols_merge()](../reference/GT.cols_merge.md#great_tables.GT.cols_merge) with its pattern syntax gives you full flexibility for any custom arrangement.
