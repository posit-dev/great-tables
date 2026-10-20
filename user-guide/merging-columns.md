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
#hlrkaudxpm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hlrkaudxpm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hlrkaudxpm p { margin: 0; padding: 0; }
 #hlrkaudxpm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hlrkaudxpm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hlrkaudxpm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hlrkaudxpm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hlrkaudxpm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hlrkaudxpm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hlrkaudxpm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hlrkaudxpm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hlrkaudxpm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hlrkaudxpm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hlrkaudxpm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hlrkaudxpm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hlrkaudxpm .gt_spanner_row { border-bottom-style: hidden; }
 #hlrkaudxpm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hlrkaudxpm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hlrkaudxpm .gt_from_md> :first-child { margin-top: 0; }
 #hlrkaudxpm .gt_from_md> :last-child { margin-bottom: 0; }
 #hlrkaudxpm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hlrkaudxpm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hlrkaudxpm .gt_indent_1 { text-indent: 5px; }
 #hlrkaudxpm .gt_indent_2 { text-indent: calc(5px * 2); }
 #hlrkaudxpm .gt_indent_3 { text-indent: calc(5px * 3); }
 #hlrkaudxpm .gt_indent_4 { text-indent: calc(5px * 4); }
 #hlrkaudxpm .gt_indent_5 { text-indent: calc(5px * 5); }
 #hlrkaudxpm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hlrkaudxpm .gt_row_group_first td { border-top-width: 2px; }
 #hlrkaudxpm .gt_row_group_first th { border-top-width: 2px; }
 #hlrkaudxpm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hlrkaudxpm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hlrkaudxpm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hlrkaudxpm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hlrkaudxpm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hlrkaudxpm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hlrkaudxpm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hlrkaudxpm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hlrkaudxpm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hlrkaudxpm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hlrkaudxpm .gt_left { text-align: left; }
 #hlrkaudxpm .gt_center { text-align: center; }
 #hlrkaudxpm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hlrkaudxpm .gt_font_normal { font-weight: normal; }
 #hlrkaudxpm .gt_font_bold { font-weight: bold; }
 #hlrkaudxpm .gt_font_italic { font-style: italic; }
 #hlrkaudxpm .gt_super { font-size: 65%; }
 #hlrkaudxpm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hlrkaudxpm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hlrkaudxpm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hlrkaudxpm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hlrkaudxpm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hlrkaudxpm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xczuhndjyf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xczuhndjyf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xczuhndjyf p { margin: 0; padding: 0; }
 #xczuhndjyf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xczuhndjyf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xczuhndjyf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xczuhndjyf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xczuhndjyf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xczuhndjyf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xczuhndjyf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xczuhndjyf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xczuhndjyf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xczuhndjyf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xczuhndjyf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xczuhndjyf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xczuhndjyf .gt_spanner_row { border-bottom-style: hidden; }
 #xczuhndjyf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xczuhndjyf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xczuhndjyf .gt_from_md> :first-child { margin-top: 0; }
 #xczuhndjyf .gt_from_md> :last-child { margin-bottom: 0; }
 #xczuhndjyf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xczuhndjyf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xczuhndjyf .gt_indent_1 { text-indent: 5px; }
 #xczuhndjyf .gt_indent_2 { text-indent: calc(5px * 2); }
 #xczuhndjyf .gt_indent_3 { text-indent: calc(5px * 3); }
 #xczuhndjyf .gt_indent_4 { text-indent: calc(5px * 4); }
 #xczuhndjyf .gt_indent_5 { text-indent: calc(5px * 5); }
 #xczuhndjyf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xczuhndjyf .gt_row_group_first td { border-top-width: 2px; }
 #xczuhndjyf .gt_row_group_first th { border-top-width: 2px; }
 #xczuhndjyf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xczuhndjyf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xczuhndjyf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xczuhndjyf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xczuhndjyf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xczuhndjyf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xczuhndjyf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xczuhndjyf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xczuhndjyf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xczuhndjyf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xczuhndjyf .gt_left { text-align: left; }
 #xczuhndjyf .gt_center { text-align: center; }
 #xczuhndjyf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xczuhndjyf .gt_font_normal { font-weight: normal; }
 #xczuhndjyf .gt_font_bold { font-weight: bold; }
 #xczuhndjyf .gt_font_italic { font-style: italic; }
 #xczuhndjyf .gt_super { font-size: 65%; }
 #xczuhndjyf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xczuhndjyf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xczuhndjyf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xczuhndjyf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xczuhndjyf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xczuhndjyf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ereclyiepk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ereclyiepk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ereclyiepk p { margin: 0; padding: 0; }
 #ereclyiepk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ereclyiepk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ereclyiepk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ereclyiepk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ereclyiepk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ereclyiepk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ereclyiepk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ereclyiepk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ereclyiepk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ereclyiepk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ereclyiepk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ereclyiepk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ereclyiepk .gt_spanner_row { border-bottom-style: hidden; }
 #ereclyiepk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ereclyiepk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ereclyiepk .gt_from_md> :first-child { margin-top: 0; }
 #ereclyiepk .gt_from_md> :last-child { margin-bottom: 0; }
 #ereclyiepk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ereclyiepk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ereclyiepk .gt_indent_1 { text-indent: 5px; }
 #ereclyiepk .gt_indent_2 { text-indent: calc(5px * 2); }
 #ereclyiepk .gt_indent_3 { text-indent: calc(5px * 3); }
 #ereclyiepk .gt_indent_4 { text-indent: calc(5px * 4); }
 #ereclyiepk .gt_indent_5 { text-indent: calc(5px * 5); }
 #ereclyiepk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ereclyiepk .gt_row_group_first td { border-top-width: 2px; }
 #ereclyiepk .gt_row_group_first th { border-top-width: 2px; }
 #ereclyiepk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ereclyiepk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ereclyiepk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ereclyiepk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ereclyiepk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ereclyiepk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ereclyiepk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ereclyiepk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ereclyiepk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ereclyiepk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ereclyiepk .gt_left { text-align: left; }
 #ereclyiepk .gt_center { text-align: center; }
 #ereclyiepk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ereclyiepk .gt_font_normal { font-weight: normal; }
 #ereclyiepk .gt_font_bold { font-weight: bold; }
 #ereclyiepk .gt_font_italic { font-style: italic; }
 #ereclyiepk .gt_super { font-size: 65%; }
 #ereclyiepk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ereclyiepk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ereclyiepk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ereclyiepk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ereclyiepk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ereclyiepk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#kxngkhmayr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kxngkhmayr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kxngkhmayr p { margin: 0; padding: 0; }
 #kxngkhmayr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kxngkhmayr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kxngkhmayr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kxngkhmayr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kxngkhmayr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kxngkhmayr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kxngkhmayr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kxngkhmayr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kxngkhmayr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kxngkhmayr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kxngkhmayr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kxngkhmayr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kxngkhmayr .gt_spanner_row { border-bottom-style: hidden; }
 #kxngkhmayr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kxngkhmayr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kxngkhmayr .gt_from_md> :first-child { margin-top: 0; }
 #kxngkhmayr .gt_from_md> :last-child { margin-bottom: 0; }
 #kxngkhmayr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kxngkhmayr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kxngkhmayr .gt_indent_1 { text-indent: 5px; }
 #kxngkhmayr .gt_indent_2 { text-indent: calc(5px * 2); }
 #kxngkhmayr .gt_indent_3 { text-indent: calc(5px * 3); }
 #kxngkhmayr .gt_indent_4 { text-indent: calc(5px * 4); }
 #kxngkhmayr .gt_indent_5 { text-indent: calc(5px * 5); }
 #kxngkhmayr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kxngkhmayr .gt_row_group_first td { border-top-width: 2px; }
 #kxngkhmayr .gt_row_group_first th { border-top-width: 2px; }
 #kxngkhmayr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kxngkhmayr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kxngkhmayr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kxngkhmayr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kxngkhmayr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kxngkhmayr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kxngkhmayr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kxngkhmayr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kxngkhmayr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kxngkhmayr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kxngkhmayr .gt_left { text-align: left; }
 #kxngkhmayr .gt_center { text-align: center; }
 #kxngkhmayr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kxngkhmayr .gt_font_normal { font-weight: normal; }
 #kxngkhmayr .gt_font_bold { font-weight: bold; }
 #kxngkhmayr .gt_font_italic { font-style: italic; }
 #kxngkhmayr .gt_super { font-size: 65%; }
 #kxngkhmayr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kxngkhmayr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kxngkhmayr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kxngkhmayr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kxngkhmayr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kxngkhmayr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#thopbkxjcp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#thopbkxjcp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#thopbkxjcp p { margin: 0; padding: 0; }
 #thopbkxjcp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #thopbkxjcp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #thopbkxjcp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #thopbkxjcp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #thopbkxjcp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #thopbkxjcp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #thopbkxjcp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #thopbkxjcp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #thopbkxjcp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #thopbkxjcp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #thopbkxjcp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #thopbkxjcp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #thopbkxjcp .gt_spanner_row { border-bottom-style: hidden; }
 #thopbkxjcp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #thopbkxjcp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #thopbkxjcp .gt_from_md> :first-child { margin-top: 0; }
 #thopbkxjcp .gt_from_md> :last-child { margin-bottom: 0; }
 #thopbkxjcp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #thopbkxjcp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #thopbkxjcp .gt_indent_1 { text-indent: 5px; }
 #thopbkxjcp .gt_indent_2 { text-indent: calc(5px * 2); }
 #thopbkxjcp .gt_indent_3 { text-indent: calc(5px * 3); }
 #thopbkxjcp .gt_indent_4 { text-indent: calc(5px * 4); }
 #thopbkxjcp .gt_indent_5 { text-indent: calc(5px * 5); }
 #thopbkxjcp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #thopbkxjcp .gt_row_group_first td { border-top-width: 2px; }
 #thopbkxjcp .gt_row_group_first th { border-top-width: 2px; }
 #thopbkxjcp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #thopbkxjcp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #thopbkxjcp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #thopbkxjcp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #thopbkxjcp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #thopbkxjcp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #thopbkxjcp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #thopbkxjcp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #thopbkxjcp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #thopbkxjcp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #thopbkxjcp .gt_left { text-align: left; }
 #thopbkxjcp .gt_center { text-align: center; }
 #thopbkxjcp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #thopbkxjcp .gt_font_normal { font-weight: normal; }
 #thopbkxjcp .gt_font_bold { font-weight: bold; }
 #thopbkxjcp .gt_font_italic { font-style: italic; }
 #thopbkxjcp .gt_super { font-size: 65%; }
 #thopbkxjcp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #thopbkxjcp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #thopbkxjcp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #thopbkxjcp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #thopbkxjcp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #thopbkxjcp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#yakifinqmi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#yakifinqmi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#yakifinqmi p { margin: 0; padding: 0; }
 #yakifinqmi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #yakifinqmi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #yakifinqmi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #yakifinqmi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #yakifinqmi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yakifinqmi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yakifinqmi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yakifinqmi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #yakifinqmi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #yakifinqmi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #yakifinqmi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #yakifinqmi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #yakifinqmi .gt_spanner_row { border-bottom-style: hidden; }
 #yakifinqmi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #yakifinqmi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #yakifinqmi .gt_from_md> :first-child { margin-top: 0; }
 #yakifinqmi .gt_from_md> :last-child { margin-bottom: 0; }
 #yakifinqmi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #yakifinqmi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #yakifinqmi .gt_indent_1 { text-indent: 5px; }
 #yakifinqmi .gt_indent_2 { text-indent: calc(5px * 2); }
 #yakifinqmi .gt_indent_3 { text-indent: calc(5px * 3); }
 #yakifinqmi .gt_indent_4 { text-indent: calc(5px * 4); }
 #yakifinqmi .gt_indent_5 { text-indent: calc(5px * 5); }
 #yakifinqmi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #yakifinqmi .gt_row_group_first td { border-top-width: 2px; }
 #yakifinqmi .gt_row_group_first th { border-top-width: 2px; }
 #yakifinqmi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #yakifinqmi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yakifinqmi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yakifinqmi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #yakifinqmi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yakifinqmi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yakifinqmi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #yakifinqmi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #yakifinqmi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yakifinqmi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yakifinqmi .gt_left { text-align: left; }
 #yakifinqmi .gt_center { text-align: center; }
 #yakifinqmi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #yakifinqmi .gt_font_normal { font-weight: normal; }
 #yakifinqmi .gt_font_bold { font-weight: bold; }
 #yakifinqmi .gt_font_italic { font-style: italic; }
 #yakifinqmi .gt_super { font-size: 65%; }
 #yakifinqmi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yakifinqmi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #yakifinqmi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yakifinqmi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yakifinqmi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #yakifinqmi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tsnnqfeqkz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tsnnqfeqkz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tsnnqfeqkz p { margin: 0; padding: 0; }
 #tsnnqfeqkz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tsnnqfeqkz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tsnnqfeqkz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tsnnqfeqkz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tsnnqfeqkz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tsnnqfeqkz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tsnnqfeqkz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tsnnqfeqkz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tsnnqfeqkz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tsnnqfeqkz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tsnnqfeqkz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tsnnqfeqkz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tsnnqfeqkz .gt_spanner_row { border-bottom-style: hidden; }
 #tsnnqfeqkz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tsnnqfeqkz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tsnnqfeqkz .gt_from_md> :first-child { margin-top: 0; }
 #tsnnqfeqkz .gt_from_md> :last-child { margin-bottom: 0; }
 #tsnnqfeqkz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tsnnqfeqkz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tsnnqfeqkz .gt_indent_1 { text-indent: 5px; }
 #tsnnqfeqkz .gt_indent_2 { text-indent: calc(5px * 2); }
 #tsnnqfeqkz .gt_indent_3 { text-indent: calc(5px * 3); }
 #tsnnqfeqkz .gt_indent_4 { text-indent: calc(5px * 4); }
 #tsnnqfeqkz .gt_indent_5 { text-indent: calc(5px * 5); }
 #tsnnqfeqkz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tsnnqfeqkz .gt_row_group_first td { border-top-width: 2px; }
 #tsnnqfeqkz .gt_row_group_first th { border-top-width: 2px; }
 #tsnnqfeqkz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tsnnqfeqkz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tsnnqfeqkz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tsnnqfeqkz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tsnnqfeqkz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tsnnqfeqkz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tsnnqfeqkz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tsnnqfeqkz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tsnnqfeqkz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tsnnqfeqkz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tsnnqfeqkz .gt_left { text-align: left; }
 #tsnnqfeqkz .gt_center { text-align: center; }
 #tsnnqfeqkz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tsnnqfeqkz .gt_font_normal { font-weight: normal; }
 #tsnnqfeqkz .gt_font_bold { font-weight: bold; }
 #tsnnqfeqkz .gt_font_italic { font-style: italic; }
 #tsnnqfeqkz .gt_super { font-size: 65%; }
 #tsnnqfeqkz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tsnnqfeqkz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tsnnqfeqkz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tsnnqfeqkz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tsnnqfeqkz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tsnnqfeqkz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jkfwjijuew table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jkfwjijuew thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jkfwjijuew p { margin: 0; padding: 0; }
 #jkfwjijuew .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jkfwjijuew .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jkfwjijuew .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jkfwjijuew .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jkfwjijuew .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jkfwjijuew .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jkfwjijuew .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jkfwjijuew .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jkfwjijuew .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jkfwjijuew .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jkfwjijuew .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jkfwjijuew .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jkfwjijuew .gt_spanner_row { border-bottom-style: hidden; }
 #jkfwjijuew .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jkfwjijuew .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jkfwjijuew .gt_from_md> :first-child { margin-top: 0; }
 #jkfwjijuew .gt_from_md> :last-child { margin-bottom: 0; }
 #jkfwjijuew .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jkfwjijuew .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jkfwjijuew .gt_indent_1 { text-indent: 5px; }
 #jkfwjijuew .gt_indent_2 { text-indent: calc(5px * 2); }
 #jkfwjijuew .gt_indent_3 { text-indent: calc(5px * 3); }
 #jkfwjijuew .gt_indent_4 { text-indent: calc(5px * 4); }
 #jkfwjijuew .gt_indent_5 { text-indent: calc(5px * 5); }
 #jkfwjijuew .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jkfwjijuew .gt_row_group_first td { border-top-width: 2px; }
 #jkfwjijuew .gt_row_group_first th { border-top-width: 2px; }
 #jkfwjijuew .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jkfwjijuew .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jkfwjijuew .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jkfwjijuew .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jkfwjijuew .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jkfwjijuew .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jkfwjijuew .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jkfwjijuew .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jkfwjijuew .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jkfwjijuew .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jkfwjijuew .gt_left { text-align: left; }
 #jkfwjijuew .gt_center { text-align: center; }
 #jkfwjijuew .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jkfwjijuew .gt_font_normal { font-weight: normal; }
 #jkfwjijuew .gt_font_bold { font-weight: bold; }
 #jkfwjijuew .gt_font_italic { font-style: italic; }
 #jkfwjijuew .gt_super { font-size: 65%; }
 #jkfwjijuew .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jkfwjijuew .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jkfwjijuew .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jkfwjijuew .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jkfwjijuew .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jkfwjijuew .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#lvlkksduge table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lvlkksduge thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lvlkksduge p { margin: 0; padding: 0; }
 #lvlkksduge .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lvlkksduge .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lvlkksduge .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lvlkksduge .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lvlkksduge .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lvlkksduge .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lvlkksduge .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lvlkksduge .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lvlkksduge .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lvlkksduge .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lvlkksduge .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lvlkksduge .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lvlkksduge .gt_spanner_row { border-bottom-style: hidden; }
 #lvlkksduge .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lvlkksduge .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lvlkksduge .gt_from_md> :first-child { margin-top: 0; }
 #lvlkksduge .gt_from_md> :last-child { margin-bottom: 0; }
 #lvlkksduge .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lvlkksduge .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lvlkksduge .gt_indent_1 { text-indent: 5px; }
 #lvlkksduge .gt_indent_2 { text-indent: calc(5px * 2); }
 #lvlkksduge .gt_indent_3 { text-indent: calc(5px * 3); }
 #lvlkksduge .gt_indent_4 { text-indent: calc(5px * 4); }
 #lvlkksduge .gt_indent_5 { text-indent: calc(5px * 5); }
 #lvlkksduge .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lvlkksduge .gt_row_group_first td { border-top-width: 2px; }
 #lvlkksduge .gt_row_group_first th { border-top-width: 2px; }
 #lvlkksduge .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lvlkksduge .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lvlkksduge .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lvlkksduge .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lvlkksduge .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lvlkksduge .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lvlkksduge .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lvlkksduge .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lvlkksduge .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lvlkksduge .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lvlkksduge .gt_left { text-align: left; }
 #lvlkksduge .gt_center { text-align: center; }
 #lvlkksduge .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lvlkksduge .gt_font_normal { font-weight: normal; }
 #lvlkksduge .gt_font_bold { font-weight: bold; }
 #lvlkksduge .gt_font_italic { font-style: italic; }
 #lvlkksduge .gt_super { font-size: 65%; }
 #lvlkksduge .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lvlkksduge .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lvlkksduge .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lvlkksduge .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lvlkksduge .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lvlkksduge .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | Result     | Range     | Observations |
|---------|------------|-----------|--------------|
| Trial 1 | 12.4 ± 0.3 | 10.5-14.2 | 120 (34.2)   |
| Trial 2 | 8.9 ± 0.1  | 7.8-10.1  | 85 (24.3)    |
| Trial 3 | 15.0 ± 0.5 | 13.2-16.8 | 200 (57.1)   |
| Trial 4 |            | 9.1-12.5  | 0            |


By merging three pairs of columns, we reduced the table from six data columns down to three, each conveying the same information in a more compact form.

Column merging is a powerful technique for building information-dense tables. By combining related values into unified columns, you reduce visual clutter and help readers process the data more efficiently. The specialized [cols_merge_uncert()](../reference/GT.cols_merge_uncert.md#great_tables.GT.cols_merge_uncert), [cols_merge_range()](../reference/GT.cols_merge_range.md#great_tables.GT.cols_merge_range), and [cols_merge_n_pct()](../reference/GT.cols_merge_n_pct.md#great_tables.GT.cols_merge_n_pct) methods handle the most common patterns, while [cols_merge()](../reference/GT.cols_merge.md#great_tables.GT.cols_merge) with its pattern syntax gives you full flexibility for any custom arrangement.
