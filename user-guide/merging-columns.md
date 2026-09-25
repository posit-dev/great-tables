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
#xvlnffzvkz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xvlnffzvkz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xvlnffzvkz p { margin: 0; padding: 0; }
 #xvlnffzvkz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xvlnffzvkz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xvlnffzvkz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xvlnffzvkz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xvlnffzvkz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xvlnffzvkz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xvlnffzvkz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xvlnffzvkz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xvlnffzvkz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xvlnffzvkz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xvlnffzvkz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xvlnffzvkz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xvlnffzvkz .gt_spanner_row { border-bottom-style: hidden; }
 #xvlnffzvkz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xvlnffzvkz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xvlnffzvkz .gt_from_md> :first-child { margin-top: 0; }
 #xvlnffzvkz .gt_from_md> :last-child { margin-bottom: 0; }
 #xvlnffzvkz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xvlnffzvkz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xvlnffzvkz .gt_indent_1 { text-indent: 5px; }
 #xvlnffzvkz .gt_indent_2 { text-indent: calc(5px * 2); }
 #xvlnffzvkz .gt_indent_3 { text-indent: calc(5px * 3); }
 #xvlnffzvkz .gt_indent_4 { text-indent: calc(5px * 4); }
 #xvlnffzvkz .gt_indent_5 { text-indent: calc(5px * 5); }
 #xvlnffzvkz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xvlnffzvkz .gt_row_group_first td { border-top-width: 2px; }
 #xvlnffzvkz .gt_row_group_first th { border-top-width: 2px; }
 #xvlnffzvkz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xvlnffzvkz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xvlnffzvkz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xvlnffzvkz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xvlnffzvkz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xvlnffzvkz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xvlnffzvkz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xvlnffzvkz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xvlnffzvkz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xvlnffzvkz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xvlnffzvkz .gt_left { text-align: left; }
 #xvlnffzvkz .gt_center { text-align: center; }
 #xvlnffzvkz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xvlnffzvkz .gt_font_normal { font-weight: normal; }
 #xvlnffzvkz .gt_font_bold { font-weight: bold; }
 #xvlnffzvkz .gt_font_italic { font-style: italic; }
 #xvlnffzvkz .gt_super { font-size: 65%; }
 #xvlnffzvkz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xvlnffzvkz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xvlnffzvkz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xvlnffzvkz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xvlnffzvkz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xvlnffzvkz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#sepftvssxk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sepftvssxk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sepftvssxk p { margin: 0; padding: 0; }
 #sepftvssxk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sepftvssxk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sepftvssxk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sepftvssxk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sepftvssxk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sepftvssxk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sepftvssxk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sepftvssxk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sepftvssxk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sepftvssxk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sepftvssxk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sepftvssxk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sepftvssxk .gt_spanner_row { border-bottom-style: hidden; }
 #sepftvssxk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sepftvssxk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sepftvssxk .gt_from_md> :first-child { margin-top: 0; }
 #sepftvssxk .gt_from_md> :last-child { margin-bottom: 0; }
 #sepftvssxk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sepftvssxk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sepftvssxk .gt_indent_1 { text-indent: 5px; }
 #sepftvssxk .gt_indent_2 { text-indent: calc(5px * 2); }
 #sepftvssxk .gt_indent_3 { text-indent: calc(5px * 3); }
 #sepftvssxk .gt_indent_4 { text-indent: calc(5px * 4); }
 #sepftvssxk .gt_indent_5 { text-indent: calc(5px * 5); }
 #sepftvssxk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sepftvssxk .gt_row_group_first td { border-top-width: 2px; }
 #sepftvssxk .gt_row_group_first th { border-top-width: 2px; }
 #sepftvssxk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sepftvssxk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sepftvssxk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sepftvssxk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sepftvssxk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sepftvssxk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sepftvssxk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sepftvssxk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sepftvssxk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sepftvssxk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sepftvssxk .gt_left { text-align: left; }
 #sepftvssxk .gt_center { text-align: center; }
 #sepftvssxk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sepftvssxk .gt_font_normal { font-weight: normal; }
 #sepftvssxk .gt_font_bold { font-weight: bold; }
 #sepftvssxk .gt_font_italic { font-style: italic; }
 #sepftvssxk .gt_super { font-size: 65%; }
 #sepftvssxk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sepftvssxk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sepftvssxk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sepftvssxk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sepftvssxk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sepftvssxk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wjsdpouygq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wjsdpouygq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wjsdpouygq p { margin: 0; padding: 0; }
 #wjsdpouygq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wjsdpouygq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wjsdpouygq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wjsdpouygq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wjsdpouygq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wjsdpouygq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjsdpouygq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wjsdpouygq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wjsdpouygq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wjsdpouygq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wjsdpouygq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wjsdpouygq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wjsdpouygq .gt_spanner_row { border-bottom-style: hidden; }
 #wjsdpouygq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wjsdpouygq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wjsdpouygq .gt_from_md> :first-child { margin-top: 0; }
 #wjsdpouygq .gt_from_md> :last-child { margin-bottom: 0; }
 #wjsdpouygq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wjsdpouygq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wjsdpouygq .gt_indent_1 { text-indent: 5px; }
 #wjsdpouygq .gt_indent_2 { text-indent: calc(5px * 2); }
 #wjsdpouygq .gt_indent_3 { text-indent: calc(5px * 3); }
 #wjsdpouygq .gt_indent_4 { text-indent: calc(5px * 4); }
 #wjsdpouygq .gt_indent_5 { text-indent: calc(5px * 5); }
 #wjsdpouygq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wjsdpouygq .gt_row_group_first td { border-top-width: 2px; }
 #wjsdpouygq .gt_row_group_first th { border-top-width: 2px; }
 #wjsdpouygq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wjsdpouygq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjsdpouygq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wjsdpouygq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wjsdpouygq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjsdpouygq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wjsdpouygq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wjsdpouygq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wjsdpouygq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjsdpouygq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wjsdpouygq .gt_left { text-align: left; }
 #wjsdpouygq .gt_center { text-align: center; }
 #wjsdpouygq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wjsdpouygq .gt_font_normal { font-weight: normal; }
 #wjsdpouygq .gt_font_bold { font-weight: bold; }
 #wjsdpouygq .gt_font_italic { font-style: italic; }
 #wjsdpouygq .gt_super { font-size: 65%; }
 #wjsdpouygq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjsdpouygq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wjsdpouygq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjsdpouygq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wjsdpouygq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wjsdpouygq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tderfthugw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tderfthugw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tderfthugw p { margin: 0; padding: 0; }
 #tderfthugw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tderfthugw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tderfthugw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tderfthugw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tderfthugw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tderfthugw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tderfthugw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tderfthugw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tderfthugw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tderfthugw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tderfthugw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tderfthugw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tderfthugw .gt_spanner_row { border-bottom-style: hidden; }
 #tderfthugw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tderfthugw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tderfthugw .gt_from_md> :first-child { margin-top: 0; }
 #tderfthugw .gt_from_md> :last-child { margin-bottom: 0; }
 #tderfthugw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tderfthugw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tderfthugw .gt_indent_1 { text-indent: 5px; }
 #tderfthugw .gt_indent_2 { text-indent: calc(5px * 2); }
 #tderfthugw .gt_indent_3 { text-indent: calc(5px * 3); }
 #tderfthugw .gt_indent_4 { text-indent: calc(5px * 4); }
 #tderfthugw .gt_indent_5 { text-indent: calc(5px * 5); }
 #tderfthugw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tderfthugw .gt_row_group_first td { border-top-width: 2px; }
 #tderfthugw .gt_row_group_first th { border-top-width: 2px; }
 #tderfthugw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tderfthugw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tderfthugw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tderfthugw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tderfthugw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tderfthugw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tderfthugw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tderfthugw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tderfthugw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tderfthugw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tderfthugw .gt_left { text-align: left; }
 #tderfthugw .gt_center { text-align: center; }
 #tderfthugw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tderfthugw .gt_font_normal { font-weight: normal; }
 #tderfthugw .gt_font_bold { font-weight: bold; }
 #tderfthugw .gt_font_italic { font-style: italic; }
 #tderfthugw .gt_super { font-size: 65%; }
 #tderfthugw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tderfthugw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tderfthugw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tderfthugw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tderfthugw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tderfthugw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#krjoxjmxmi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#krjoxjmxmi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#krjoxjmxmi p { margin: 0; padding: 0; }
 #krjoxjmxmi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #krjoxjmxmi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #krjoxjmxmi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #krjoxjmxmi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #krjoxjmxmi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #krjoxjmxmi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #krjoxjmxmi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #krjoxjmxmi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #krjoxjmxmi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #krjoxjmxmi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #krjoxjmxmi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #krjoxjmxmi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #krjoxjmxmi .gt_spanner_row { border-bottom-style: hidden; }
 #krjoxjmxmi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #krjoxjmxmi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #krjoxjmxmi .gt_from_md> :first-child { margin-top: 0; }
 #krjoxjmxmi .gt_from_md> :last-child { margin-bottom: 0; }
 #krjoxjmxmi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #krjoxjmxmi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #krjoxjmxmi .gt_indent_1 { text-indent: 5px; }
 #krjoxjmxmi .gt_indent_2 { text-indent: calc(5px * 2); }
 #krjoxjmxmi .gt_indent_3 { text-indent: calc(5px * 3); }
 #krjoxjmxmi .gt_indent_4 { text-indent: calc(5px * 4); }
 #krjoxjmxmi .gt_indent_5 { text-indent: calc(5px * 5); }
 #krjoxjmxmi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #krjoxjmxmi .gt_row_group_first td { border-top-width: 2px; }
 #krjoxjmxmi .gt_row_group_first th { border-top-width: 2px; }
 #krjoxjmxmi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #krjoxjmxmi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #krjoxjmxmi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #krjoxjmxmi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #krjoxjmxmi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #krjoxjmxmi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #krjoxjmxmi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #krjoxjmxmi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #krjoxjmxmi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #krjoxjmxmi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #krjoxjmxmi .gt_left { text-align: left; }
 #krjoxjmxmi .gt_center { text-align: center; }
 #krjoxjmxmi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #krjoxjmxmi .gt_font_normal { font-weight: normal; }
 #krjoxjmxmi .gt_font_bold { font-weight: bold; }
 #krjoxjmxmi .gt_font_italic { font-style: italic; }
 #krjoxjmxmi .gt_super { font-size: 65%; }
 #krjoxjmxmi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #krjoxjmxmi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #krjoxjmxmi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #krjoxjmxmi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #krjoxjmxmi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #krjoxjmxmi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#mpnqxavoab table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mpnqxavoab thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mpnqxavoab p { margin: 0; padding: 0; }
 #mpnqxavoab .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mpnqxavoab .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mpnqxavoab .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mpnqxavoab .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mpnqxavoab .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mpnqxavoab .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mpnqxavoab .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mpnqxavoab .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mpnqxavoab .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mpnqxavoab .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mpnqxavoab .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mpnqxavoab .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mpnqxavoab .gt_spanner_row { border-bottom-style: hidden; }
 #mpnqxavoab .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mpnqxavoab .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mpnqxavoab .gt_from_md> :first-child { margin-top: 0; }
 #mpnqxavoab .gt_from_md> :last-child { margin-bottom: 0; }
 #mpnqxavoab .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mpnqxavoab .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mpnqxavoab .gt_indent_1 { text-indent: 5px; }
 #mpnqxavoab .gt_indent_2 { text-indent: calc(5px * 2); }
 #mpnqxavoab .gt_indent_3 { text-indent: calc(5px * 3); }
 #mpnqxavoab .gt_indent_4 { text-indent: calc(5px * 4); }
 #mpnqxavoab .gt_indent_5 { text-indent: calc(5px * 5); }
 #mpnqxavoab .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mpnqxavoab .gt_row_group_first td { border-top-width: 2px; }
 #mpnqxavoab .gt_row_group_first th { border-top-width: 2px; }
 #mpnqxavoab .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mpnqxavoab .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mpnqxavoab .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mpnqxavoab .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mpnqxavoab .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mpnqxavoab .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mpnqxavoab .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mpnqxavoab .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mpnqxavoab .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mpnqxavoab .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mpnqxavoab .gt_left { text-align: left; }
 #mpnqxavoab .gt_center { text-align: center; }
 #mpnqxavoab .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mpnqxavoab .gt_font_normal { font-weight: normal; }
 #mpnqxavoab .gt_font_bold { font-weight: bold; }
 #mpnqxavoab .gt_font_italic { font-style: italic; }
 #mpnqxavoab .gt_super { font-size: 65%; }
 #mpnqxavoab .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mpnqxavoab .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mpnqxavoab .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mpnqxavoab .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mpnqxavoab .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mpnqxavoab .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jluefwmmkj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jluefwmmkj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jluefwmmkj p { margin: 0; padding: 0; }
 #jluefwmmkj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jluefwmmkj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jluefwmmkj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jluefwmmkj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jluefwmmkj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jluefwmmkj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jluefwmmkj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jluefwmmkj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jluefwmmkj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jluefwmmkj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jluefwmmkj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jluefwmmkj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jluefwmmkj .gt_spanner_row { border-bottom-style: hidden; }
 #jluefwmmkj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jluefwmmkj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jluefwmmkj .gt_from_md> :first-child { margin-top: 0; }
 #jluefwmmkj .gt_from_md> :last-child { margin-bottom: 0; }
 #jluefwmmkj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jluefwmmkj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jluefwmmkj .gt_indent_1 { text-indent: 5px; }
 #jluefwmmkj .gt_indent_2 { text-indent: calc(5px * 2); }
 #jluefwmmkj .gt_indent_3 { text-indent: calc(5px * 3); }
 #jluefwmmkj .gt_indent_4 { text-indent: calc(5px * 4); }
 #jluefwmmkj .gt_indent_5 { text-indent: calc(5px * 5); }
 #jluefwmmkj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jluefwmmkj .gt_row_group_first td { border-top-width: 2px; }
 #jluefwmmkj .gt_row_group_first th { border-top-width: 2px; }
 #jluefwmmkj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jluefwmmkj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jluefwmmkj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jluefwmmkj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jluefwmmkj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jluefwmmkj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jluefwmmkj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jluefwmmkj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jluefwmmkj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jluefwmmkj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jluefwmmkj .gt_left { text-align: left; }
 #jluefwmmkj .gt_center { text-align: center; }
 #jluefwmmkj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jluefwmmkj .gt_font_normal { font-weight: normal; }
 #jluefwmmkj .gt_font_bold { font-weight: bold; }
 #jluefwmmkj .gt_font_italic { font-style: italic; }
 #jluefwmmkj .gt_super { font-size: 65%; }
 #jluefwmmkj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jluefwmmkj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jluefwmmkj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jluefwmmkj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jluefwmmkj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jluefwmmkj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#iyccogrnol table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iyccogrnol thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iyccogrnol p { margin: 0; padding: 0; }
 #iyccogrnol .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #iyccogrnol .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iyccogrnol .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iyccogrnol .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iyccogrnol .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iyccogrnol .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iyccogrnol .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iyccogrnol .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iyccogrnol .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iyccogrnol .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iyccogrnol .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iyccogrnol .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iyccogrnol .gt_spanner_row { border-bottom-style: hidden; }
 #iyccogrnol .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iyccogrnol .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #iyccogrnol .gt_from_md> :first-child { margin-top: 0; }
 #iyccogrnol .gt_from_md> :last-child { margin-bottom: 0; }
 #iyccogrnol .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #iyccogrnol .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #iyccogrnol .gt_indent_1 { text-indent: 5px; }
 #iyccogrnol .gt_indent_2 { text-indent: calc(5px * 2); }
 #iyccogrnol .gt_indent_3 { text-indent: calc(5px * 3); }
 #iyccogrnol .gt_indent_4 { text-indent: calc(5px * 4); }
 #iyccogrnol .gt_indent_5 { text-indent: calc(5px * 5); }
 #iyccogrnol .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iyccogrnol .gt_row_group_first td { border-top-width: 2px; }
 #iyccogrnol .gt_row_group_first th { border-top-width: 2px; }
 #iyccogrnol .gt_striped { color: #333333; background-color: #F4F4F4; }
 #iyccogrnol .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iyccogrnol .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iyccogrnol .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #iyccogrnol .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iyccogrnol .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iyccogrnol .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iyccogrnol .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iyccogrnol .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iyccogrnol .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iyccogrnol .gt_left { text-align: left; }
 #iyccogrnol .gt_center { text-align: center; }
 #iyccogrnol .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iyccogrnol .gt_font_normal { font-weight: normal; }
 #iyccogrnol .gt_font_bold { font-weight: bold; }
 #iyccogrnol .gt_font_italic { font-style: italic; }
 #iyccogrnol .gt_super { font-size: 65%; }
 #iyccogrnol .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iyccogrnol .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #iyccogrnol .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iyccogrnol .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iyccogrnol .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iyccogrnol .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#owxwxskjlc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#owxwxskjlc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#owxwxskjlc p { margin: 0; padding: 0; }
 #owxwxskjlc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #owxwxskjlc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #owxwxskjlc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #owxwxskjlc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #owxwxskjlc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #owxwxskjlc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #owxwxskjlc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #owxwxskjlc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #owxwxskjlc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #owxwxskjlc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #owxwxskjlc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #owxwxskjlc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #owxwxskjlc .gt_spanner_row { border-bottom-style: hidden; }
 #owxwxskjlc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #owxwxskjlc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #owxwxskjlc .gt_from_md> :first-child { margin-top: 0; }
 #owxwxskjlc .gt_from_md> :last-child { margin-bottom: 0; }
 #owxwxskjlc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #owxwxskjlc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #owxwxskjlc .gt_indent_1 { text-indent: 5px; }
 #owxwxskjlc .gt_indent_2 { text-indent: calc(5px * 2); }
 #owxwxskjlc .gt_indent_3 { text-indent: calc(5px * 3); }
 #owxwxskjlc .gt_indent_4 { text-indent: calc(5px * 4); }
 #owxwxskjlc .gt_indent_5 { text-indent: calc(5px * 5); }
 #owxwxskjlc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #owxwxskjlc .gt_row_group_first td { border-top-width: 2px; }
 #owxwxskjlc .gt_row_group_first th { border-top-width: 2px; }
 #owxwxskjlc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #owxwxskjlc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #owxwxskjlc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #owxwxskjlc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #owxwxskjlc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #owxwxskjlc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #owxwxskjlc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #owxwxskjlc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #owxwxskjlc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #owxwxskjlc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #owxwxskjlc .gt_left { text-align: left; }
 #owxwxskjlc .gt_center { text-align: center; }
 #owxwxskjlc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #owxwxskjlc .gt_font_normal { font-weight: normal; }
 #owxwxskjlc .gt_font_bold { font-weight: bold; }
 #owxwxskjlc .gt_font_italic { font-style: italic; }
 #owxwxskjlc .gt_super { font-size: 65%; }
 #owxwxskjlc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #owxwxskjlc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #owxwxskjlc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #owxwxskjlc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #owxwxskjlc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #owxwxskjlc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | Result     | Range     | Observations |
|---------|------------|-----------|--------------|
| Trial 1 | 12.4 ± 0.3 | 10.5-14.2 | 120 (34.2)   |
| Trial 2 | 8.9 ± 0.1  | 7.8-10.1  | 85 (24.3)    |
| Trial 3 | 15.0 ± 0.5 | 13.2-16.8 | 200 (57.1)   |
| Trial 4 |            | 9.1-12.5  | 0            |


By merging three pairs of columns, we reduced the table from six data columns down to three, each conveying the same information in a more compact form.

Column merging is a powerful technique for building information-dense tables. By combining related values into unified columns, you reduce visual clutter and help readers process the data more efficiently. The specialized [cols_merge_uncert()](../reference/GT.cols_merge_uncert.md#great_tables.GT.cols_merge_uncert), [cols_merge_range()](../reference/GT.cols_merge_range.md#great_tables.GT.cols_merge_range), and [cols_merge_n_pct()](../reference/GT.cols_merge_n_pct.md#great_tables.GT.cols_merge_n_pct) methods handle the most common patterns, while [cols_merge()](../reference/GT.cols_merge.md#great_tables.GT.cols_merge) with its pattern syntax gives you full flexibility for any custom arrangement.
