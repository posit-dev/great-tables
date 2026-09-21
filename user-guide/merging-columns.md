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
#bxavjepjld table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bxavjepjld thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bxavjepjld p { margin: 0; padding: 0; }
 #bxavjepjld .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bxavjepjld .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bxavjepjld .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bxavjepjld .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bxavjepjld .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bxavjepjld .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bxavjepjld .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bxavjepjld .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bxavjepjld .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bxavjepjld .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bxavjepjld .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bxavjepjld .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bxavjepjld .gt_spanner_row { border-bottom-style: hidden; }
 #bxavjepjld .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bxavjepjld .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bxavjepjld .gt_from_md> :first-child { margin-top: 0; }
 #bxavjepjld .gt_from_md> :last-child { margin-bottom: 0; }
 #bxavjepjld .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bxavjepjld .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bxavjepjld .gt_indent_1 { text-indent: 5px; }
 #bxavjepjld .gt_indent_2 { text-indent: calc(5px * 2); }
 #bxavjepjld .gt_indent_3 { text-indent: calc(5px * 3); }
 #bxavjepjld .gt_indent_4 { text-indent: calc(5px * 4); }
 #bxavjepjld .gt_indent_5 { text-indent: calc(5px * 5); }
 #bxavjepjld .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bxavjepjld .gt_row_group_first td { border-top-width: 2px; }
 #bxavjepjld .gt_row_group_first th { border-top-width: 2px; }
 #bxavjepjld .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bxavjepjld .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bxavjepjld .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bxavjepjld .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bxavjepjld .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bxavjepjld .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bxavjepjld .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bxavjepjld .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bxavjepjld .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bxavjepjld .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bxavjepjld .gt_left { text-align: left; }
 #bxavjepjld .gt_center { text-align: center; }
 #bxavjepjld .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bxavjepjld .gt_font_normal { font-weight: normal; }
 #bxavjepjld .gt_font_bold { font-weight: bold; }
 #bxavjepjld .gt_font_italic { font-style: italic; }
 #bxavjepjld .gt_super { font-size: 65%; }
 #bxavjepjld .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bxavjepjld .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bxavjepjld .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bxavjepjld .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bxavjepjld .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bxavjepjld .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | measurement | uncertainty | low  | high | n_obs | pct  |
|---------|-------------|-------------|------|------|-------|------|
| Trial 1 | 12.45       | 0.32        | 10.5 | 14.2 | 120   | 34.2 |
| Trial 2 | 8.92        | 0.15        | 7.8  | 10.1 | 85    | 24.3 |
| Trial 3 | 15.03       | 0.48        | 13.2 | 16.8 | 200   | 57.1 |
| Trial 4 |             |             | 9.1  | 12.5 | 0     | 0.0  |


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
#atxzcfyfdy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#atxzcfyfdy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#atxzcfyfdy p { margin: 0; padding: 0; }
 #atxzcfyfdy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #atxzcfyfdy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #atxzcfyfdy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #atxzcfyfdy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #atxzcfyfdy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #atxzcfyfdy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #atxzcfyfdy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #atxzcfyfdy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #atxzcfyfdy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #atxzcfyfdy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #atxzcfyfdy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #atxzcfyfdy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #atxzcfyfdy .gt_spanner_row { border-bottom-style: hidden; }
 #atxzcfyfdy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #atxzcfyfdy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #atxzcfyfdy .gt_from_md> :first-child { margin-top: 0; }
 #atxzcfyfdy .gt_from_md> :last-child { margin-bottom: 0; }
 #atxzcfyfdy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #atxzcfyfdy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #atxzcfyfdy .gt_indent_1 { text-indent: 5px; }
 #atxzcfyfdy .gt_indent_2 { text-indent: calc(5px * 2); }
 #atxzcfyfdy .gt_indent_3 { text-indent: calc(5px * 3); }
 #atxzcfyfdy .gt_indent_4 { text-indent: calc(5px * 4); }
 #atxzcfyfdy .gt_indent_5 { text-indent: calc(5px * 5); }
 #atxzcfyfdy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #atxzcfyfdy .gt_row_group_first td { border-top-width: 2px; }
 #atxzcfyfdy .gt_row_group_first th { border-top-width: 2px; }
 #atxzcfyfdy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #atxzcfyfdy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #atxzcfyfdy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #atxzcfyfdy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #atxzcfyfdy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #atxzcfyfdy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #atxzcfyfdy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #atxzcfyfdy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #atxzcfyfdy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #atxzcfyfdy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #atxzcfyfdy .gt_left { text-align: left; }
 #atxzcfyfdy .gt_center { text-align: center; }
 #atxzcfyfdy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #atxzcfyfdy .gt_font_normal { font-weight: normal; }
 #atxzcfyfdy .gt_font_bold { font-weight: bold; }
 #atxzcfyfdy .gt_font_italic { font-style: italic; }
 #atxzcfyfdy .gt_super { font-size: 65%; }
 #atxzcfyfdy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #atxzcfyfdy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #atxzcfyfdy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #atxzcfyfdy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #atxzcfyfdy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #atxzcfyfdy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wkwyagoyqe table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wkwyagoyqe thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wkwyagoyqe p { margin: 0; padding: 0; }
 #wkwyagoyqe .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wkwyagoyqe .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wkwyagoyqe .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wkwyagoyqe .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wkwyagoyqe .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wkwyagoyqe .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wkwyagoyqe .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wkwyagoyqe .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wkwyagoyqe .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wkwyagoyqe .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wkwyagoyqe .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wkwyagoyqe .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wkwyagoyqe .gt_spanner_row { border-bottom-style: hidden; }
 #wkwyagoyqe .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wkwyagoyqe .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wkwyagoyqe .gt_from_md> :first-child { margin-top: 0; }
 #wkwyagoyqe .gt_from_md> :last-child { margin-bottom: 0; }
 #wkwyagoyqe .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wkwyagoyqe .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wkwyagoyqe .gt_indent_1 { text-indent: 5px; }
 #wkwyagoyqe .gt_indent_2 { text-indent: calc(5px * 2); }
 #wkwyagoyqe .gt_indent_3 { text-indent: calc(5px * 3); }
 #wkwyagoyqe .gt_indent_4 { text-indent: calc(5px * 4); }
 #wkwyagoyqe .gt_indent_5 { text-indent: calc(5px * 5); }
 #wkwyagoyqe .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wkwyagoyqe .gt_row_group_first td { border-top-width: 2px; }
 #wkwyagoyqe .gt_row_group_first th { border-top-width: 2px; }
 #wkwyagoyqe .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wkwyagoyqe .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wkwyagoyqe .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wkwyagoyqe .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wkwyagoyqe .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wkwyagoyqe .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wkwyagoyqe .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wkwyagoyqe .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wkwyagoyqe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wkwyagoyqe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wkwyagoyqe .gt_left { text-align: left; }
 #wkwyagoyqe .gt_center { text-align: center; }
 #wkwyagoyqe .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wkwyagoyqe .gt_font_normal { font-weight: normal; }
 #wkwyagoyqe .gt_font_bold { font-weight: bold; }
 #wkwyagoyqe .gt_font_italic { font-style: italic; }
 #wkwyagoyqe .gt_super { font-size: 65%; }
 #wkwyagoyqe .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wkwyagoyqe .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wkwyagoyqe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wkwyagoyqe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wkwyagoyqe .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wkwyagoyqe .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#chrijadlah table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#chrijadlah thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#chrijadlah p { margin: 0; padding: 0; }
 #chrijadlah .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #chrijadlah .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #chrijadlah .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #chrijadlah .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #chrijadlah .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #chrijadlah .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #chrijadlah .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #chrijadlah .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #chrijadlah .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #chrijadlah .gt_column_spanner_outer:first-child { padding-left: 0; }
 #chrijadlah .gt_column_spanner_outer:last-child { padding-right: 0; }
 #chrijadlah .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #chrijadlah .gt_spanner_row { border-bottom-style: hidden; }
 #chrijadlah .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #chrijadlah .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #chrijadlah .gt_from_md> :first-child { margin-top: 0; }
 #chrijadlah .gt_from_md> :last-child { margin-bottom: 0; }
 #chrijadlah .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #chrijadlah .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #chrijadlah .gt_indent_1 { text-indent: 5px; }
 #chrijadlah .gt_indent_2 { text-indent: calc(5px * 2); }
 #chrijadlah .gt_indent_3 { text-indent: calc(5px * 3); }
 #chrijadlah .gt_indent_4 { text-indent: calc(5px * 4); }
 #chrijadlah .gt_indent_5 { text-indent: calc(5px * 5); }
 #chrijadlah .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #chrijadlah .gt_row_group_first td { border-top-width: 2px; }
 #chrijadlah .gt_row_group_first th { border-top-width: 2px; }
 #chrijadlah .gt_striped { color: #333333; background-color: #F4F4F4; }
 #chrijadlah .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #chrijadlah .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #chrijadlah .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #chrijadlah .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #chrijadlah .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #chrijadlah .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #chrijadlah .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #chrijadlah .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #chrijadlah .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #chrijadlah .gt_left { text-align: left; }
 #chrijadlah .gt_center { text-align: center; }
 #chrijadlah .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #chrijadlah .gt_font_normal { font-weight: normal; }
 #chrijadlah .gt_font_bold { font-weight: bold; }
 #chrijadlah .gt_font_italic { font-style: italic; }
 #chrijadlah .gt_super { font-size: 65%; }
 #chrijadlah .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #chrijadlah .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #chrijadlah .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #chrijadlah .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #chrijadlah .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #chrijadlah .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#phgutkokss table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#phgutkokss thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#phgutkokss p { margin: 0; padding: 0; }
 #phgutkokss .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #phgutkokss .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #phgutkokss .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #phgutkokss .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #phgutkokss .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #phgutkokss .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #phgutkokss .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #phgutkokss .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #phgutkokss .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #phgutkokss .gt_column_spanner_outer:first-child { padding-left: 0; }
 #phgutkokss .gt_column_spanner_outer:last-child { padding-right: 0; }
 #phgutkokss .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #phgutkokss .gt_spanner_row { border-bottom-style: hidden; }
 #phgutkokss .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #phgutkokss .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #phgutkokss .gt_from_md> :first-child { margin-top: 0; }
 #phgutkokss .gt_from_md> :last-child { margin-bottom: 0; }
 #phgutkokss .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #phgutkokss .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #phgutkokss .gt_indent_1 { text-indent: 5px; }
 #phgutkokss .gt_indent_2 { text-indent: calc(5px * 2); }
 #phgutkokss .gt_indent_3 { text-indent: calc(5px * 3); }
 #phgutkokss .gt_indent_4 { text-indent: calc(5px * 4); }
 #phgutkokss .gt_indent_5 { text-indent: calc(5px * 5); }
 #phgutkokss .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #phgutkokss .gt_row_group_first td { border-top-width: 2px; }
 #phgutkokss .gt_row_group_first th { border-top-width: 2px; }
 #phgutkokss .gt_striped { color: #333333; background-color: #F4F4F4; }
 #phgutkokss .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #phgutkokss .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #phgutkokss .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #phgutkokss .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #phgutkokss .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #phgutkokss .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #phgutkokss .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #phgutkokss .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #phgutkokss .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #phgutkokss .gt_left { text-align: left; }
 #phgutkokss .gt_center { text-align: center; }
 #phgutkokss .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #phgutkokss .gt_font_normal { font-weight: normal; }
 #phgutkokss .gt_font_bold { font-weight: bold; }
 #phgutkokss .gt_font_italic { font-style: italic; }
 #phgutkokss .gt_super { font-size: 65%; }
 #phgutkokss .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #phgutkokss .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #phgutkokss .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #phgutkokss .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #phgutkokss .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #phgutkokss .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#iccxdwuqok table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iccxdwuqok thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iccxdwuqok p { margin: 0; padding: 0; }
 #iccxdwuqok .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #iccxdwuqok .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iccxdwuqok .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iccxdwuqok .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iccxdwuqok .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iccxdwuqok .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iccxdwuqok .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iccxdwuqok .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iccxdwuqok .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iccxdwuqok .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iccxdwuqok .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iccxdwuqok .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iccxdwuqok .gt_spanner_row { border-bottom-style: hidden; }
 #iccxdwuqok .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iccxdwuqok .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #iccxdwuqok .gt_from_md> :first-child { margin-top: 0; }
 #iccxdwuqok .gt_from_md> :last-child { margin-bottom: 0; }
 #iccxdwuqok .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #iccxdwuqok .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #iccxdwuqok .gt_indent_1 { text-indent: 5px; }
 #iccxdwuqok .gt_indent_2 { text-indent: calc(5px * 2); }
 #iccxdwuqok .gt_indent_3 { text-indent: calc(5px * 3); }
 #iccxdwuqok .gt_indent_4 { text-indent: calc(5px * 4); }
 #iccxdwuqok .gt_indent_5 { text-indent: calc(5px * 5); }
 #iccxdwuqok .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iccxdwuqok .gt_row_group_first td { border-top-width: 2px; }
 #iccxdwuqok .gt_row_group_first th { border-top-width: 2px; }
 #iccxdwuqok .gt_striped { color: #333333; background-color: #F4F4F4; }
 #iccxdwuqok .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iccxdwuqok .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iccxdwuqok .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #iccxdwuqok .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iccxdwuqok .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iccxdwuqok .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iccxdwuqok .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iccxdwuqok .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iccxdwuqok .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iccxdwuqok .gt_left { text-align: left; }
 #iccxdwuqok .gt_center { text-align: center; }
 #iccxdwuqok .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iccxdwuqok .gt_font_normal { font-weight: normal; }
 #iccxdwuqok .gt_font_bold { font-weight: bold; }
 #iccxdwuqok .gt_font_italic { font-style: italic; }
 #iccxdwuqok .gt_super { font-size: 65%; }
 #iccxdwuqok .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iccxdwuqok .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #iccxdwuqok .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iccxdwuqok .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iccxdwuqok .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iccxdwuqok .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | measurement | uncertainty | low       | n_obs | pct  |
|---------|-------------|-------------|-----------|-------|------|
| Trial 1 | 12.45       | 0.32        | 10.5-14.2 | 120   | 34.2 |
| Trial 2 | 8.92        | 0.15        | 7.8-10.1  | 85    | 24.3 |
| Trial 3 | 15.03       | 0.48        | 13.2-16.8 | 200   | 57.1 |
| Trial 4 |             |             | 9.1-12.5  | 0     | 0.0  |


You can customize the separator with `sep=`. The special values `"--"` and `"---"` are automatically rendered as an en dash and em dash, respectively. Any other string is used literally.


``` python
(
    GT(experiment_df, rowname_col="trial")
    .cols_merge_range(col_begin="low", col_end="high", sep=" to ")
)
```


<style>
#jxwbsgxban table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jxwbsgxban thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jxwbsgxban p { margin: 0; padding: 0; }
 #jxwbsgxban .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jxwbsgxban .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jxwbsgxban .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jxwbsgxban .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jxwbsgxban .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jxwbsgxban .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jxwbsgxban .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jxwbsgxban .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jxwbsgxban .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jxwbsgxban .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jxwbsgxban .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jxwbsgxban .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jxwbsgxban .gt_spanner_row { border-bottom-style: hidden; }
 #jxwbsgxban .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jxwbsgxban .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jxwbsgxban .gt_from_md> :first-child { margin-top: 0; }
 #jxwbsgxban .gt_from_md> :last-child { margin-bottom: 0; }
 #jxwbsgxban .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jxwbsgxban .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jxwbsgxban .gt_indent_1 { text-indent: 5px; }
 #jxwbsgxban .gt_indent_2 { text-indent: calc(5px * 2); }
 #jxwbsgxban .gt_indent_3 { text-indent: calc(5px * 3); }
 #jxwbsgxban .gt_indent_4 { text-indent: calc(5px * 4); }
 #jxwbsgxban .gt_indent_5 { text-indent: calc(5px * 5); }
 #jxwbsgxban .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jxwbsgxban .gt_row_group_first td { border-top-width: 2px; }
 #jxwbsgxban .gt_row_group_first th { border-top-width: 2px; }
 #jxwbsgxban .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jxwbsgxban .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jxwbsgxban .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jxwbsgxban .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jxwbsgxban .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jxwbsgxban .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jxwbsgxban .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jxwbsgxban .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jxwbsgxban .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jxwbsgxban .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jxwbsgxban .gt_left { text-align: left; }
 #jxwbsgxban .gt_center { text-align: center; }
 #jxwbsgxban .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jxwbsgxban .gt_font_normal { font-weight: normal; }
 #jxwbsgxban .gt_font_bold { font-weight: bold; }
 #jxwbsgxban .gt_font_italic { font-style: italic; }
 #jxwbsgxban .gt_super { font-size: 65%; }
 #jxwbsgxban .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jxwbsgxban .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jxwbsgxban .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jxwbsgxban .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jxwbsgxban .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jxwbsgxban .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | measurement | uncertainty | low          | n_obs | pct  |
|---------|-------------|-------------|--------------|-------|------|
| Trial 1 | 12.45       | 0.32        | 10.5 to 14.2 | 120   | 34.2 |
| Trial 2 | 8.92        | 0.15        | 7.8 to 10.1  | 85    | 24.3 |
| Trial 3 | 15.03       | 0.48        | 13.2 to 16.8 | 200   | 57.1 |
| Trial 4 |             |             | 9.1 to 12.5  | 0     | 0.0  |


# Merging Count and Percentage

When you have a count column alongside a pre-computed percentage column, [cols_merge_n_pct()](../reference/GT.cols_merge_n_pct.md#great_tables.GT.cols_merge_n_pct) merges them into a format like `"120 (34.2%)"`. This is a common pattern in statistical tables and survey results.


``` python
(
    GT(experiment_df, rowname_col="trial")
    .cols_merge_n_pct(col_n="n_obs", col_pct="pct")
)
```


<style>
#bkwuxbtrsd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bkwuxbtrsd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bkwuxbtrsd p { margin: 0; padding: 0; }
 #bkwuxbtrsd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bkwuxbtrsd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bkwuxbtrsd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bkwuxbtrsd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bkwuxbtrsd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bkwuxbtrsd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bkwuxbtrsd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bkwuxbtrsd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bkwuxbtrsd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bkwuxbtrsd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bkwuxbtrsd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bkwuxbtrsd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bkwuxbtrsd .gt_spanner_row { border-bottom-style: hidden; }
 #bkwuxbtrsd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bkwuxbtrsd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bkwuxbtrsd .gt_from_md> :first-child { margin-top: 0; }
 #bkwuxbtrsd .gt_from_md> :last-child { margin-bottom: 0; }
 #bkwuxbtrsd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bkwuxbtrsd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bkwuxbtrsd .gt_indent_1 { text-indent: 5px; }
 #bkwuxbtrsd .gt_indent_2 { text-indent: calc(5px * 2); }
 #bkwuxbtrsd .gt_indent_3 { text-indent: calc(5px * 3); }
 #bkwuxbtrsd .gt_indent_4 { text-indent: calc(5px * 4); }
 #bkwuxbtrsd .gt_indent_5 { text-indent: calc(5px * 5); }
 #bkwuxbtrsd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bkwuxbtrsd .gt_row_group_first td { border-top-width: 2px; }
 #bkwuxbtrsd .gt_row_group_first th { border-top-width: 2px; }
 #bkwuxbtrsd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bkwuxbtrsd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bkwuxbtrsd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bkwuxbtrsd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bkwuxbtrsd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bkwuxbtrsd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bkwuxbtrsd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bkwuxbtrsd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bkwuxbtrsd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bkwuxbtrsd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bkwuxbtrsd .gt_left { text-align: left; }
 #bkwuxbtrsd .gt_center { text-align: center; }
 #bkwuxbtrsd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bkwuxbtrsd .gt_font_normal { font-weight: normal; }
 #bkwuxbtrsd .gt_font_bold { font-weight: bold; }
 #bkwuxbtrsd .gt_font_italic { font-style: italic; }
 #bkwuxbtrsd .gt_super { font-size: 65%; }
 #bkwuxbtrsd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bkwuxbtrsd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bkwuxbtrsd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bkwuxbtrsd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bkwuxbtrsd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bkwuxbtrsd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | measurement | uncertainty | low  | high | n_obs      |
|---------|-------------|-------------|------|------|------------|
| Trial 1 | 12.45       | 0.32        | 10.5 | 14.2 | 120 (34.2) |
| Trial 2 | 8.92        | 0.15        | 7.8  | 10.1 | 85 (24.3)  |
| Trial 3 | 15.03       | 0.48        | 13.2 | 16.8 | 200 (57.1) |
| Trial 4 |             |             | 9.1  | 12.5 | 0          |


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
#eqgoacrvur table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eqgoacrvur thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eqgoacrvur p { margin: 0; padding: 0; }
 #eqgoacrvur .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eqgoacrvur .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eqgoacrvur .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eqgoacrvur .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eqgoacrvur .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eqgoacrvur .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eqgoacrvur .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eqgoacrvur .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eqgoacrvur .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eqgoacrvur .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eqgoacrvur .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eqgoacrvur .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eqgoacrvur .gt_spanner_row { border-bottom-style: hidden; }
 #eqgoacrvur .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eqgoacrvur .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eqgoacrvur .gt_from_md> :first-child { margin-top: 0; }
 #eqgoacrvur .gt_from_md> :last-child { margin-bottom: 0; }
 #eqgoacrvur .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eqgoacrvur .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eqgoacrvur .gt_indent_1 { text-indent: 5px; }
 #eqgoacrvur .gt_indent_2 { text-indent: calc(5px * 2); }
 #eqgoacrvur .gt_indent_3 { text-indent: calc(5px * 3); }
 #eqgoacrvur .gt_indent_4 { text-indent: calc(5px * 4); }
 #eqgoacrvur .gt_indent_5 { text-indent: calc(5px * 5); }
 #eqgoacrvur .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eqgoacrvur .gt_row_group_first td { border-top-width: 2px; }
 #eqgoacrvur .gt_row_group_first th { border-top-width: 2px; }
 #eqgoacrvur .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eqgoacrvur .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eqgoacrvur .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eqgoacrvur .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eqgoacrvur .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eqgoacrvur .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eqgoacrvur .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eqgoacrvur .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eqgoacrvur .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eqgoacrvur .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eqgoacrvur .gt_left { text-align: left; }
 #eqgoacrvur .gt_center { text-align: center; }
 #eqgoacrvur .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eqgoacrvur .gt_font_normal { font-weight: normal; }
 #eqgoacrvur .gt_font_bold { font-weight: bold; }
 #eqgoacrvur .gt_font_italic { font-style: italic; }
 #eqgoacrvur .gt_super { font-size: 65%; }
 #eqgoacrvur .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eqgoacrvur .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eqgoacrvur .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eqgoacrvur .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eqgoacrvur .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eqgoacrvur .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | Result     | Range     | Observations |
|---------|------------|-----------|--------------|
| Trial 1 | 12.4 ± 0.3 | 10.5-14.2 | 120 (34.2)   |
| Trial 2 | 8.9 ± 0.1  | 7.8-10.1  | 85 (24.3)    |
| Trial 3 | 15.0 ± 0.5 | 13.2-16.8 | 200 (57.1)   |
| Trial 4 |            | 9.1-12.5  | 0            |


By merging three pairs of columns, we reduced the table from six data columns down to three, each conveying the same information in a more compact form.

Column merging is a powerful technique for building information-dense tables. By combining related values into unified columns, you reduce visual clutter and help readers process the data more efficiently. The specialized [cols_merge_uncert()](../reference/GT.cols_merge_uncert.md#great_tables.GT.cols_merge_uncert), [cols_merge_range()](../reference/GT.cols_merge_range.md#great_tables.GT.cols_merge_range), and [cols_merge_n_pct()](../reference/GT.cols_merge_n_pct.md#great_tables.GT.cols_merge_n_pct) methods handle the most common patterns, while [cols_merge()](../reference/GT.cols_merge.md#great_tables.GT.cols_merge) with its pattern syntax gives you full flexibility for any custom arrangement.
