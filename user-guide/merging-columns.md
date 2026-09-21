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
#jdcathrpid table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jdcathrpid thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jdcathrpid p { margin: 0; padding: 0; }
 #jdcathrpid .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jdcathrpid .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jdcathrpid .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jdcathrpid .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jdcathrpid .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jdcathrpid .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jdcathrpid .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jdcathrpid .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jdcathrpid .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jdcathrpid .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jdcathrpid .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jdcathrpid .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jdcathrpid .gt_spanner_row { border-bottom-style: hidden; }
 #jdcathrpid .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jdcathrpid .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jdcathrpid .gt_from_md> :first-child { margin-top: 0; }
 #jdcathrpid .gt_from_md> :last-child { margin-bottom: 0; }
 #jdcathrpid .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jdcathrpid .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jdcathrpid .gt_indent_1 { text-indent: 5px; }
 #jdcathrpid .gt_indent_2 { text-indent: calc(5px * 2); }
 #jdcathrpid .gt_indent_3 { text-indent: calc(5px * 3); }
 #jdcathrpid .gt_indent_4 { text-indent: calc(5px * 4); }
 #jdcathrpid .gt_indent_5 { text-indent: calc(5px * 5); }
 #jdcathrpid .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jdcathrpid .gt_row_group_first td { border-top-width: 2px; }
 #jdcathrpid .gt_row_group_first th { border-top-width: 2px; }
 #jdcathrpid .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jdcathrpid .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jdcathrpid .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jdcathrpid .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jdcathrpid .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jdcathrpid .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jdcathrpid .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jdcathrpid .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jdcathrpid .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jdcathrpid .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jdcathrpid .gt_left { text-align: left; }
 #jdcathrpid .gt_center { text-align: center; }
 #jdcathrpid .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jdcathrpid .gt_font_normal { font-weight: normal; }
 #jdcathrpid .gt_font_bold { font-weight: bold; }
 #jdcathrpid .gt_font_italic { font-style: italic; }
 #jdcathrpid .gt_super { font-size: 65%; }
 #jdcathrpid .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jdcathrpid .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jdcathrpid .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jdcathrpid .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jdcathrpid .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jdcathrpid .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zxeprmztyg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zxeprmztyg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zxeprmztyg p { margin: 0; padding: 0; }
 #zxeprmztyg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zxeprmztyg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zxeprmztyg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zxeprmztyg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zxeprmztyg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zxeprmztyg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxeprmztyg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zxeprmztyg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zxeprmztyg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zxeprmztyg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zxeprmztyg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zxeprmztyg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zxeprmztyg .gt_spanner_row { border-bottom-style: hidden; }
 #zxeprmztyg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zxeprmztyg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zxeprmztyg .gt_from_md> :first-child { margin-top: 0; }
 #zxeprmztyg .gt_from_md> :last-child { margin-bottom: 0; }
 #zxeprmztyg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zxeprmztyg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zxeprmztyg .gt_indent_1 { text-indent: 5px; }
 #zxeprmztyg .gt_indent_2 { text-indent: calc(5px * 2); }
 #zxeprmztyg .gt_indent_3 { text-indent: calc(5px * 3); }
 #zxeprmztyg .gt_indent_4 { text-indent: calc(5px * 4); }
 #zxeprmztyg .gt_indent_5 { text-indent: calc(5px * 5); }
 #zxeprmztyg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zxeprmztyg .gt_row_group_first td { border-top-width: 2px; }
 #zxeprmztyg .gt_row_group_first th { border-top-width: 2px; }
 #zxeprmztyg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zxeprmztyg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxeprmztyg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zxeprmztyg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zxeprmztyg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zxeprmztyg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zxeprmztyg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zxeprmztyg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zxeprmztyg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxeprmztyg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zxeprmztyg .gt_left { text-align: left; }
 #zxeprmztyg .gt_center { text-align: center; }
 #zxeprmztyg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zxeprmztyg .gt_font_normal { font-weight: normal; }
 #zxeprmztyg .gt_font_bold { font-weight: bold; }
 #zxeprmztyg .gt_font_italic { font-style: italic; }
 #zxeprmztyg .gt_super { font-size: 65%; }
 #zxeprmztyg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxeprmztyg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zxeprmztyg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zxeprmztyg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zxeprmztyg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zxeprmztyg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#sovcdnkyag table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sovcdnkyag thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sovcdnkyag p { margin: 0; padding: 0; }
 #sovcdnkyag .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sovcdnkyag .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sovcdnkyag .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sovcdnkyag .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sovcdnkyag .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sovcdnkyag .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sovcdnkyag .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sovcdnkyag .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sovcdnkyag .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sovcdnkyag .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sovcdnkyag .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sovcdnkyag .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sovcdnkyag .gt_spanner_row { border-bottom-style: hidden; }
 #sovcdnkyag .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sovcdnkyag .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sovcdnkyag .gt_from_md> :first-child { margin-top: 0; }
 #sovcdnkyag .gt_from_md> :last-child { margin-bottom: 0; }
 #sovcdnkyag .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sovcdnkyag .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sovcdnkyag .gt_indent_1 { text-indent: 5px; }
 #sovcdnkyag .gt_indent_2 { text-indent: calc(5px * 2); }
 #sovcdnkyag .gt_indent_3 { text-indent: calc(5px * 3); }
 #sovcdnkyag .gt_indent_4 { text-indent: calc(5px * 4); }
 #sovcdnkyag .gt_indent_5 { text-indent: calc(5px * 5); }
 #sovcdnkyag .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sovcdnkyag .gt_row_group_first td { border-top-width: 2px; }
 #sovcdnkyag .gt_row_group_first th { border-top-width: 2px; }
 #sovcdnkyag .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sovcdnkyag .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sovcdnkyag .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sovcdnkyag .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sovcdnkyag .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sovcdnkyag .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sovcdnkyag .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sovcdnkyag .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sovcdnkyag .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sovcdnkyag .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sovcdnkyag .gt_left { text-align: left; }
 #sovcdnkyag .gt_center { text-align: center; }
 #sovcdnkyag .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sovcdnkyag .gt_font_normal { font-weight: normal; }
 #sovcdnkyag .gt_font_bold { font-weight: bold; }
 #sovcdnkyag .gt_font_italic { font-style: italic; }
 #sovcdnkyag .gt_super { font-size: 65%; }
 #sovcdnkyag .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sovcdnkyag .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sovcdnkyag .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sovcdnkyag .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sovcdnkyag .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sovcdnkyag .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#sunkszdcss table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sunkszdcss thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sunkszdcss p { margin: 0; padding: 0; }
 #sunkszdcss .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sunkszdcss .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sunkszdcss .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sunkszdcss .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sunkszdcss .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sunkszdcss .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sunkszdcss .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sunkszdcss .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sunkszdcss .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sunkszdcss .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sunkszdcss .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sunkszdcss .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sunkszdcss .gt_spanner_row { border-bottom-style: hidden; }
 #sunkszdcss .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sunkszdcss .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sunkszdcss .gt_from_md> :first-child { margin-top: 0; }
 #sunkszdcss .gt_from_md> :last-child { margin-bottom: 0; }
 #sunkszdcss .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sunkszdcss .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sunkszdcss .gt_indent_1 { text-indent: 5px; }
 #sunkszdcss .gt_indent_2 { text-indent: calc(5px * 2); }
 #sunkszdcss .gt_indent_3 { text-indent: calc(5px * 3); }
 #sunkszdcss .gt_indent_4 { text-indent: calc(5px * 4); }
 #sunkszdcss .gt_indent_5 { text-indent: calc(5px * 5); }
 #sunkszdcss .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sunkszdcss .gt_row_group_first td { border-top-width: 2px; }
 #sunkszdcss .gt_row_group_first th { border-top-width: 2px; }
 #sunkszdcss .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sunkszdcss .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sunkszdcss .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sunkszdcss .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sunkszdcss .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sunkszdcss .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sunkszdcss .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sunkszdcss .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sunkszdcss .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sunkszdcss .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sunkszdcss .gt_left { text-align: left; }
 #sunkszdcss .gt_center { text-align: center; }
 #sunkszdcss .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sunkszdcss .gt_font_normal { font-weight: normal; }
 #sunkszdcss .gt_font_bold { font-weight: bold; }
 #sunkszdcss .gt_font_italic { font-style: italic; }
 #sunkszdcss .gt_super { font-size: 65%; }
 #sunkszdcss .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sunkszdcss .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sunkszdcss .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sunkszdcss .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sunkszdcss .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sunkszdcss .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#gehpcslyto table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gehpcslyto thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gehpcslyto p { margin: 0; padding: 0; }
 #gehpcslyto .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gehpcslyto .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gehpcslyto .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gehpcslyto .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gehpcslyto .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gehpcslyto .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gehpcslyto .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gehpcslyto .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gehpcslyto .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gehpcslyto .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gehpcslyto .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gehpcslyto .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gehpcslyto .gt_spanner_row { border-bottom-style: hidden; }
 #gehpcslyto .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gehpcslyto .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gehpcslyto .gt_from_md> :first-child { margin-top: 0; }
 #gehpcslyto .gt_from_md> :last-child { margin-bottom: 0; }
 #gehpcslyto .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gehpcslyto .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gehpcslyto .gt_indent_1 { text-indent: 5px; }
 #gehpcslyto .gt_indent_2 { text-indent: calc(5px * 2); }
 #gehpcslyto .gt_indent_3 { text-indent: calc(5px * 3); }
 #gehpcslyto .gt_indent_4 { text-indent: calc(5px * 4); }
 #gehpcslyto .gt_indent_5 { text-indent: calc(5px * 5); }
 #gehpcslyto .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gehpcslyto .gt_row_group_first td { border-top-width: 2px; }
 #gehpcslyto .gt_row_group_first th { border-top-width: 2px; }
 #gehpcslyto .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gehpcslyto .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gehpcslyto .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gehpcslyto .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gehpcslyto .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gehpcslyto .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gehpcslyto .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gehpcslyto .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gehpcslyto .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gehpcslyto .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gehpcslyto .gt_left { text-align: left; }
 #gehpcslyto .gt_center { text-align: center; }
 #gehpcslyto .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gehpcslyto .gt_font_normal { font-weight: normal; }
 #gehpcslyto .gt_font_bold { font-weight: bold; }
 #gehpcslyto .gt_font_italic { font-style: italic; }
 #gehpcslyto .gt_super { font-size: 65%; }
 #gehpcslyto .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gehpcslyto .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gehpcslyto .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gehpcslyto .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gehpcslyto .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gehpcslyto .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#gjvlwgqrwi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gjvlwgqrwi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gjvlwgqrwi p { margin: 0; padding: 0; }
 #gjvlwgqrwi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gjvlwgqrwi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gjvlwgqrwi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gjvlwgqrwi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gjvlwgqrwi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gjvlwgqrwi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gjvlwgqrwi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gjvlwgqrwi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gjvlwgqrwi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gjvlwgqrwi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gjvlwgqrwi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gjvlwgqrwi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gjvlwgqrwi .gt_spanner_row { border-bottom-style: hidden; }
 #gjvlwgqrwi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gjvlwgqrwi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gjvlwgqrwi .gt_from_md> :first-child { margin-top: 0; }
 #gjvlwgqrwi .gt_from_md> :last-child { margin-bottom: 0; }
 #gjvlwgqrwi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gjvlwgqrwi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gjvlwgqrwi .gt_indent_1 { text-indent: 5px; }
 #gjvlwgqrwi .gt_indent_2 { text-indent: calc(5px * 2); }
 #gjvlwgqrwi .gt_indent_3 { text-indent: calc(5px * 3); }
 #gjvlwgqrwi .gt_indent_4 { text-indent: calc(5px * 4); }
 #gjvlwgqrwi .gt_indent_5 { text-indent: calc(5px * 5); }
 #gjvlwgqrwi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gjvlwgqrwi .gt_row_group_first td { border-top-width: 2px; }
 #gjvlwgqrwi .gt_row_group_first th { border-top-width: 2px; }
 #gjvlwgqrwi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gjvlwgqrwi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gjvlwgqrwi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gjvlwgqrwi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gjvlwgqrwi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gjvlwgqrwi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gjvlwgqrwi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gjvlwgqrwi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gjvlwgqrwi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gjvlwgqrwi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gjvlwgqrwi .gt_left { text-align: left; }
 #gjvlwgqrwi .gt_center { text-align: center; }
 #gjvlwgqrwi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gjvlwgqrwi .gt_font_normal { font-weight: normal; }
 #gjvlwgqrwi .gt_font_bold { font-weight: bold; }
 #gjvlwgqrwi .gt_font_italic { font-style: italic; }
 #gjvlwgqrwi .gt_super { font-size: 65%; }
 #gjvlwgqrwi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gjvlwgqrwi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gjvlwgqrwi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gjvlwgqrwi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gjvlwgqrwi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gjvlwgqrwi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dovbgikgqy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dovbgikgqy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dovbgikgqy p { margin: 0; padding: 0; }
 #dovbgikgqy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dovbgikgqy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dovbgikgqy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dovbgikgqy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dovbgikgqy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dovbgikgqy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dovbgikgqy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dovbgikgqy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dovbgikgqy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dovbgikgqy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dovbgikgqy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dovbgikgqy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dovbgikgqy .gt_spanner_row { border-bottom-style: hidden; }
 #dovbgikgqy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dovbgikgqy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dovbgikgqy .gt_from_md> :first-child { margin-top: 0; }
 #dovbgikgqy .gt_from_md> :last-child { margin-bottom: 0; }
 #dovbgikgqy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dovbgikgqy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dovbgikgqy .gt_indent_1 { text-indent: 5px; }
 #dovbgikgqy .gt_indent_2 { text-indent: calc(5px * 2); }
 #dovbgikgqy .gt_indent_3 { text-indent: calc(5px * 3); }
 #dovbgikgqy .gt_indent_4 { text-indent: calc(5px * 4); }
 #dovbgikgqy .gt_indent_5 { text-indent: calc(5px * 5); }
 #dovbgikgqy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dovbgikgqy .gt_row_group_first td { border-top-width: 2px; }
 #dovbgikgqy .gt_row_group_first th { border-top-width: 2px; }
 #dovbgikgqy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dovbgikgqy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dovbgikgqy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dovbgikgqy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dovbgikgqy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dovbgikgqy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dovbgikgqy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dovbgikgqy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dovbgikgqy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dovbgikgqy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dovbgikgqy .gt_left { text-align: left; }
 #dovbgikgqy .gt_center { text-align: center; }
 #dovbgikgqy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dovbgikgqy .gt_font_normal { font-weight: normal; }
 #dovbgikgqy .gt_font_bold { font-weight: bold; }
 #dovbgikgqy .gt_font_italic { font-style: italic; }
 #dovbgikgqy .gt_super { font-size: 65%; }
 #dovbgikgqy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dovbgikgqy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dovbgikgqy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dovbgikgqy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dovbgikgqy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dovbgikgqy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pslsrxmkul table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pslsrxmkul thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pslsrxmkul p { margin: 0; padding: 0; }
 #pslsrxmkul .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pslsrxmkul .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pslsrxmkul .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pslsrxmkul .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pslsrxmkul .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pslsrxmkul .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pslsrxmkul .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pslsrxmkul .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pslsrxmkul .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pslsrxmkul .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pslsrxmkul .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pslsrxmkul .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pslsrxmkul .gt_spanner_row { border-bottom-style: hidden; }
 #pslsrxmkul .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pslsrxmkul .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pslsrxmkul .gt_from_md> :first-child { margin-top: 0; }
 #pslsrxmkul .gt_from_md> :last-child { margin-bottom: 0; }
 #pslsrxmkul .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pslsrxmkul .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pslsrxmkul .gt_indent_1 { text-indent: 5px; }
 #pslsrxmkul .gt_indent_2 { text-indent: calc(5px * 2); }
 #pslsrxmkul .gt_indent_3 { text-indent: calc(5px * 3); }
 #pslsrxmkul .gt_indent_4 { text-indent: calc(5px * 4); }
 #pslsrxmkul .gt_indent_5 { text-indent: calc(5px * 5); }
 #pslsrxmkul .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pslsrxmkul .gt_row_group_first td { border-top-width: 2px; }
 #pslsrxmkul .gt_row_group_first th { border-top-width: 2px; }
 #pslsrxmkul .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pslsrxmkul .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pslsrxmkul .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pslsrxmkul .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pslsrxmkul .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pslsrxmkul .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pslsrxmkul .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pslsrxmkul .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pslsrxmkul .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pslsrxmkul .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pslsrxmkul .gt_left { text-align: left; }
 #pslsrxmkul .gt_center { text-align: center; }
 #pslsrxmkul .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pslsrxmkul .gt_font_normal { font-weight: normal; }
 #pslsrxmkul .gt_font_bold { font-weight: bold; }
 #pslsrxmkul .gt_font_italic { font-style: italic; }
 #pslsrxmkul .gt_super { font-size: 65%; }
 #pslsrxmkul .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pslsrxmkul .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pslsrxmkul .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pslsrxmkul .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pslsrxmkul .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pslsrxmkul .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dpituwoxlb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dpituwoxlb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dpituwoxlb p { margin: 0; padding: 0; }
 #dpituwoxlb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dpituwoxlb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dpituwoxlb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dpituwoxlb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dpituwoxlb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dpituwoxlb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dpituwoxlb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dpituwoxlb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dpituwoxlb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dpituwoxlb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dpituwoxlb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dpituwoxlb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dpituwoxlb .gt_spanner_row { border-bottom-style: hidden; }
 #dpituwoxlb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dpituwoxlb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dpituwoxlb .gt_from_md> :first-child { margin-top: 0; }
 #dpituwoxlb .gt_from_md> :last-child { margin-bottom: 0; }
 #dpituwoxlb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dpituwoxlb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dpituwoxlb .gt_indent_1 { text-indent: 5px; }
 #dpituwoxlb .gt_indent_2 { text-indent: calc(5px * 2); }
 #dpituwoxlb .gt_indent_3 { text-indent: calc(5px * 3); }
 #dpituwoxlb .gt_indent_4 { text-indent: calc(5px * 4); }
 #dpituwoxlb .gt_indent_5 { text-indent: calc(5px * 5); }
 #dpituwoxlb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dpituwoxlb .gt_row_group_first td { border-top-width: 2px; }
 #dpituwoxlb .gt_row_group_first th { border-top-width: 2px; }
 #dpituwoxlb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dpituwoxlb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dpituwoxlb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dpituwoxlb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dpituwoxlb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dpituwoxlb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dpituwoxlb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dpituwoxlb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dpituwoxlb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dpituwoxlb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dpituwoxlb .gt_left { text-align: left; }
 #dpituwoxlb .gt_center { text-align: center; }
 #dpituwoxlb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dpituwoxlb .gt_font_normal { font-weight: normal; }
 #dpituwoxlb .gt_font_bold { font-weight: bold; }
 #dpituwoxlb .gt_font_italic { font-style: italic; }
 #dpituwoxlb .gt_super { font-size: 65%; }
 #dpituwoxlb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dpituwoxlb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dpituwoxlb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dpituwoxlb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dpituwoxlb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dpituwoxlb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | Result     | Range     | Observations |
|---------|------------|-----------|--------------|
| Trial 1 | 12.4 ± 0.3 | 10.5-14.2 | 120 (34.2)   |
| Trial 2 | 8.9 ± 0.1  | 7.8-10.1  | 85 (24.3)    |
| Trial 3 | 15.0 ± 0.5 | 13.2-16.8 | 200 (57.1)   |
| Trial 4 |            | 9.1-12.5  | 0            |


By merging three pairs of columns, we reduced the table from six data columns down to three, each conveying the same information in a more compact form.

Column merging is a powerful technique for building information-dense tables. By combining related values into unified columns, you reduce visual clutter and help readers process the data more efficiently. The specialized [cols_merge_uncert()](../reference/GT.cols_merge_uncert.md#great_tables.GT.cols_merge_uncert), [cols_merge_range()](../reference/GT.cols_merge_range.md#great_tables.GT.cols_merge_range), and [cols_merge_n_pct()](../reference/GT.cols_merge_n_pct.md#great_tables.GT.cols_merge_n_pct) methods handle the most common patterns, while [cols_merge()](../reference/GT.cols_merge.md#great_tables.GT.cols_merge) with its pattern syntax gives you full flexibility for any custom arrangement.
