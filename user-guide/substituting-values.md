# Substituting Values

Real-world data often contains missing values, zeros, or extreme numbers that can look awkward or misleading when displayed directly in a table. The `sub_*()` family of methods lets you replace these problematic values with more meaningful text, improving readability without altering your underlying data.

It is worth noting that substitution is about communication, not data cleaning. The underlying DataFrame is unchanged--what changes is how problematic values are *presented* to the reader. A `None` displayed as "N/A" or an em dash is immediately understood as intentionally missing, whereas a raw `None` can look like a bug or an incomplete pipeline. Similarly, replacing a zero with "none" or capping an extreme value with "\>10B" tells the reader that you've accounted for these cases deliberately.


# Setting Up the Example Data

For the examples on this page, we will use a small DataFrame with a mix of values that includes missing data, zeros, and both very small and very large numbers.


``` python
import pandas as pd
from great_tables import GT

df = pd.DataFrame({
    "item": ["Widget A", "Widget B", "Widget C", "Widget D", "Widget E"],
    "count": [150, 0, 42, None, 3],
    "rate": [0.003, 0.0, 0.542, 0.871, None],
    "revenue": [4500.00, 0.00, 1e13, 75.50, None],
})

gt_tbl = GT(df, rowname_col="item")
gt_tbl
```


<style>
#mvgueyyrlf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mvgueyyrlf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mvgueyyrlf p { margin: 0; padding: 0; }
 #mvgueyyrlf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mvgueyyrlf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mvgueyyrlf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mvgueyyrlf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mvgueyyrlf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mvgueyyrlf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mvgueyyrlf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mvgueyyrlf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mvgueyyrlf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mvgueyyrlf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mvgueyyrlf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mvgueyyrlf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mvgueyyrlf .gt_spanner_row { border-bottom-style: hidden; }
 #mvgueyyrlf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mvgueyyrlf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mvgueyyrlf .gt_from_md> :first-child { margin-top: 0; }
 #mvgueyyrlf .gt_from_md> :last-child { margin-bottom: 0; }
 #mvgueyyrlf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mvgueyyrlf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mvgueyyrlf .gt_indent_1 { text-indent: 5px; }
 #mvgueyyrlf .gt_indent_2 { text-indent: calc(5px * 2); }
 #mvgueyyrlf .gt_indent_3 { text-indent: calc(5px * 3); }
 #mvgueyyrlf .gt_indent_4 { text-indent: calc(5px * 4); }
 #mvgueyyrlf .gt_indent_5 { text-indent: calc(5px * 5); }
 #mvgueyyrlf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mvgueyyrlf .gt_row_group_first td { border-top-width: 2px; }
 #mvgueyyrlf .gt_row_group_first th { border-top-width: 2px; }
 #mvgueyyrlf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mvgueyyrlf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mvgueyyrlf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mvgueyyrlf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mvgueyyrlf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mvgueyyrlf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mvgueyyrlf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mvgueyyrlf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mvgueyyrlf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mvgueyyrlf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mvgueyyrlf .gt_left { text-align: left; }
 #mvgueyyrlf .gt_center { text-align: center; }
 #mvgueyyrlf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mvgueyyrlf .gt_font_normal { font-weight: normal; }
 #mvgueyyrlf .gt_font_bold { font-weight: bold; }
 #mvgueyyrlf .gt_font_italic { font-style: italic; }
 #mvgueyyrlf .gt_super { font-size: 65%; }
 #mvgueyyrlf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mvgueyyrlf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mvgueyyrlf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mvgueyyrlf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mvgueyyrlf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mvgueyyrlf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|          | count | rate  | revenue          |
|----------|-------|-------|------------------|
| Widget A | 150.0 | 0.003 | 4500.0           |
| Widget B | 0.0   | 0.0   | 0.0              |
| Widget C | 42.0  | 0.542 | 10000000000000.0 |
| Widget D | None  | 0.871 | 75.5             |
| Widget E | 3.0   | None  | None             |


Notice how the table displays `None` values and raw numbers in a way that may not be ideal for a presentation table. The `sub_*()` methods let us address each of these cases.


# Substituting Missing Values

The [sub_missing()](../reference/GT.sub_missing.md#great_tables.GT.sub_missing) method replaces `None` (or `NaN`) values with a text string of your choice. By default, it inserts an em dash, but you can provide any replacement text through the `missing_text=` argument.


``` python
gt_tbl.sub_missing(missing_text="N/A")
```


<style>
#gtvannradh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gtvannradh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gtvannradh p { margin: 0; padding: 0; }
 #gtvannradh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gtvannradh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gtvannradh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gtvannradh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gtvannradh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gtvannradh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gtvannradh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gtvannradh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gtvannradh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gtvannradh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gtvannradh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gtvannradh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gtvannradh .gt_spanner_row { border-bottom-style: hidden; }
 #gtvannradh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gtvannradh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gtvannradh .gt_from_md> :first-child { margin-top: 0; }
 #gtvannradh .gt_from_md> :last-child { margin-bottom: 0; }
 #gtvannradh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gtvannradh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gtvannradh .gt_indent_1 { text-indent: 5px; }
 #gtvannradh .gt_indent_2 { text-indent: calc(5px * 2); }
 #gtvannradh .gt_indent_3 { text-indent: calc(5px * 3); }
 #gtvannradh .gt_indent_4 { text-indent: calc(5px * 4); }
 #gtvannradh .gt_indent_5 { text-indent: calc(5px * 5); }
 #gtvannradh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gtvannradh .gt_row_group_first td { border-top-width: 2px; }
 #gtvannradh .gt_row_group_first th { border-top-width: 2px; }
 #gtvannradh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gtvannradh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gtvannradh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gtvannradh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gtvannradh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gtvannradh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gtvannradh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gtvannradh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gtvannradh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gtvannradh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gtvannradh .gt_left { text-align: left; }
 #gtvannradh .gt_center { text-align: center; }
 #gtvannradh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gtvannradh .gt_font_normal { font-weight: normal; }
 #gtvannradh .gt_font_bold { font-weight: bold; }
 #gtvannradh .gt_font_italic { font-style: italic; }
 #gtvannradh .gt_super { font-size: 65%; }
 #gtvannradh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gtvannradh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gtvannradh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gtvannradh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gtvannradh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gtvannradh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|          | count | rate  | revenue          |
|----------|-------|-------|------------------|
| Widget A | 150.0 | 0.003 | 4500.0           |
| Widget B | 0.0   | 0.0   | 0.0              |
| Widget C | 42.0  | 0.542 | 10000000000000.0 |
| Widget D | N/A   | 0.871 | 75.5             |
| Widget E | 3.0   | N/A   | N/A              |


You can also target specific columns, leaving other columns to display their missing values as-is.


``` python
gt_tbl.sub_missing(columns="count", missing_text="not reported")
```


<style>
#hpckjpafmq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hpckjpafmq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hpckjpafmq p { margin: 0; padding: 0; }
 #hpckjpafmq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hpckjpafmq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hpckjpafmq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hpckjpafmq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hpckjpafmq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hpckjpafmq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hpckjpafmq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hpckjpafmq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hpckjpafmq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hpckjpafmq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hpckjpafmq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hpckjpafmq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hpckjpafmq .gt_spanner_row { border-bottom-style: hidden; }
 #hpckjpafmq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hpckjpafmq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hpckjpafmq .gt_from_md> :first-child { margin-top: 0; }
 #hpckjpafmq .gt_from_md> :last-child { margin-bottom: 0; }
 #hpckjpafmq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hpckjpafmq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hpckjpafmq .gt_indent_1 { text-indent: 5px; }
 #hpckjpafmq .gt_indent_2 { text-indent: calc(5px * 2); }
 #hpckjpafmq .gt_indent_3 { text-indent: calc(5px * 3); }
 #hpckjpafmq .gt_indent_4 { text-indent: calc(5px * 4); }
 #hpckjpafmq .gt_indent_5 { text-indent: calc(5px * 5); }
 #hpckjpafmq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hpckjpafmq .gt_row_group_first td { border-top-width: 2px; }
 #hpckjpafmq .gt_row_group_first th { border-top-width: 2px; }
 #hpckjpafmq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hpckjpafmq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hpckjpafmq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hpckjpafmq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hpckjpafmq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hpckjpafmq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hpckjpafmq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hpckjpafmq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hpckjpafmq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hpckjpafmq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hpckjpafmq .gt_left { text-align: left; }
 #hpckjpafmq .gt_center { text-align: center; }
 #hpckjpafmq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hpckjpafmq .gt_font_normal { font-weight: normal; }
 #hpckjpafmq .gt_font_bold { font-weight: bold; }
 #hpckjpafmq .gt_font_italic { font-style: italic; }
 #hpckjpafmq .gt_super { font-size: 65%; }
 #hpckjpafmq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hpckjpafmq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hpckjpafmq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hpckjpafmq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hpckjpafmq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hpckjpafmq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|          | count        | rate  | revenue          |
|----------|--------------|-------|------------------|
| Widget A | 150.0        | 0.003 | 4500.0           |
| Widget B | 0.0          | 0.0   | 0.0              |
| Widget C | 42.0         | 0.542 | 10000000000000.0 |
| Widget D | not reported | 0.871 | 75.5             |
| Widget E | 3.0          | None  | None             |


Only the `count` column has its missing value replaced with our custom text. The `rate` and `revenue` columns still show their default missing representation.


# Substituting Zero Values

When zeros are not meaningful in context (for example, in a column that tracks incidents or errors), you can use [sub_zero()](../reference/GT.sub_zero.md#great_tables.GT.sub_zero) to replace them with explanatory text. The default replacement is `"nil"`, but this is customizable through the `zero_text=` argument.


``` python
gt_tbl.sub_zero(columns="count", zero_text="none")
```


<style>
#qnvdtphhmc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qnvdtphhmc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qnvdtphhmc p { margin: 0; padding: 0; }
 #qnvdtphhmc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qnvdtphhmc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qnvdtphhmc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qnvdtphhmc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qnvdtphhmc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qnvdtphhmc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qnvdtphhmc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qnvdtphhmc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qnvdtphhmc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qnvdtphhmc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qnvdtphhmc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qnvdtphhmc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qnvdtphhmc .gt_spanner_row { border-bottom-style: hidden; }
 #qnvdtphhmc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qnvdtphhmc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qnvdtphhmc .gt_from_md> :first-child { margin-top: 0; }
 #qnvdtphhmc .gt_from_md> :last-child { margin-bottom: 0; }
 #qnvdtphhmc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qnvdtphhmc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qnvdtphhmc .gt_indent_1 { text-indent: 5px; }
 #qnvdtphhmc .gt_indent_2 { text-indent: calc(5px * 2); }
 #qnvdtphhmc .gt_indent_3 { text-indent: calc(5px * 3); }
 #qnvdtphhmc .gt_indent_4 { text-indent: calc(5px * 4); }
 #qnvdtphhmc .gt_indent_5 { text-indent: calc(5px * 5); }
 #qnvdtphhmc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qnvdtphhmc .gt_row_group_first td { border-top-width: 2px; }
 #qnvdtphhmc .gt_row_group_first th { border-top-width: 2px; }
 #qnvdtphhmc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qnvdtphhmc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qnvdtphhmc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qnvdtphhmc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qnvdtphhmc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qnvdtphhmc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qnvdtphhmc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qnvdtphhmc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qnvdtphhmc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qnvdtphhmc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qnvdtphhmc .gt_left { text-align: left; }
 #qnvdtphhmc .gt_center { text-align: center; }
 #qnvdtphhmc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qnvdtphhmc .gt_font_normal { font-weight: normal; }
 #qnvdtphhmc .gt_font_bold { font-weight: bold; }
 #qnvdtphhmc .gt_font_italic { font-style: italic; }
 #qnvdtphhmc .gt_super { font-size: 65%; }
 #qnvdtphhmc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qnvdtphhmc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qnvdtphhmc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qnvdtphhmc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qnvdtphhmc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qnvdtphhmc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|          | count | rate  | revenue          |
|----------|-------|-------|------------------|
| Widget A | 150.0 | 0.003 | 4500.0           |
| Widget B | none  | 0.0   | 0.0              |
| Widget C | 42.0  | 0.542 | 10000000000000.0 |
| Widget D | None  | 0.871 | 75.5             |
| Widget E | 3.0   | None  | None             |


Here the zero in the `count` column now reads as `"none"`, which is clearer for the reader.


# Substituting Small Values

Very small numbers can be distracting in a table, especially when they fall below a meaningful threshold. The [sub_small_vals()](../reference/GT.sub_small_vals.md#great_tables.GT.sub_small_vals) method replaces positive values between zero and a given threshold with indicator text like `"<0.01"`.


``` python
gt_tbl.sub_small_vals(columns="rate", threshold=0.01)
```


<style>
#sobbxaexvj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sobbxaexvj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sobbxaexvj p { margin: 0; padding: 0; }
 #sobbxaexvj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sobbxaexvj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sobbxaexvj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sobbxaexvj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sobbxaexvj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sobbxaexvj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sobbxaexvj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sobbxaexvj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sobbxaexvj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sobbxaexvj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sobbxaexvj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sobbxaexvj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sobbxaexvj .gt_spanner_row { border-bottom-style: hidden; }
 #sobbxaexvj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sobbxaexvj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sobbxaexvj .gt_from_md> :first-child { margin-top: 0; }
 #sobbxaexvj .gt_from_md> :last-child { margin-bottom: 0; }
 #sobbxaexvj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sobbxaexvj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sobbxaexvj .gt_indent_1 { text-indent: 5px; }
 #sobbxaexvj .gt_indent_2 { text-indent: calc(5px * 2); }
 #sobbxaexvj .gt_indent_3 { text-indent: calc(5px * 3); }
 #sobbxaexvj .gt_indent_4 { text-indent: calc(5px * 4); }
 #sobbxaexvj .gt_indent_5 { text-indent: calc(5px * 5); }
 #sobbxaexvj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sobbxaexvj .gt_row_group_first td { border-top-width: 2px; }
 #sobbxaexvj .gt_row_group_first th { border-top-width: 2px; }
 #sobbxaexvj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sobbxaexvj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sobbxaexvj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sobbxaexvj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sobbxaexvj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sobbxaexvj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sobbxaexvj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sobbxaexvj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sobbxaexvj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sobbxaexvj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sobbxaexvj .gt_left { text-align: left; }
 #sobbxaexvj .gt_center { text-align: center; }
 #sobbxaexvj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sobbxaexvj .gt_font_normal { font-weight: normal; }
 #sobbxaexvj .gt_font_bold { font-weight: bold; }
 #sobbxaexvj .gt_font_italic { font-style: italic; }
 #sobbxaexvj .gt_super { font-size: 65%; }
 #sobbxaexvj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sobbxaexvj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sobbxaexvj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sobbxaexvj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sobbxaexvj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sobbxaexvj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|          | count | rate   | revenue          |
|----------|-------|--------|------------------|
| Widget A | 150.0 | \<0.01 | 4500.0           |
| Widget B | 0.0   | 0.0    | 0.0              |
| Widget C | 42.0  | 0.542  | 10000000000000.0 |
| Widget D | None  | 0.871  | 75.5             |
| Widget E | 3.0   | None   | None             |


The value `0.003` in the `rate` column is now displayed as `"<0.01"` since it falls below the threshold. All other values remain unchanged.

You can also handle negative small values by setting `sign="-"`. This substitutes values that are between `0` and the negative of the threshold.


``` python
df_neg = pd.DataFrame({
    "label": ["X", "Y", "Z"],
    "change": [-0.002, -5.3, 0.7],
})

GT(df_neg, rowname_col="label").sub_small_vals(columns="change", threshold=0.01, sign="-")
```


<style>
#muhkrlfkmj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#muhkrlfkmj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#muhkrlfkmj p { margin: 0; padding: 0; }
 #muhkrlfkmj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #muhkrlfkmj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #muhkrlfkmj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #muhkrlfkmj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #muhkrlfkmj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #muhkrlfkmj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muhkrlfkmj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #muhkrlfkmj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #muhkrlfkmj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #muhkrlfkmj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #muhkrlfkmj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #muhkrlfkmj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #muhkrlfkmj .gt_spanner_row { border-bottom-style: hidden; }
 #muhkrlfkmj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #muhkrlfkmj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #muhkrlfkmj .gt_from_md> :first-child { margin-top: 0; }
 #muhkrlfkmj .gt_from_md> :last-child { margin-bottom: 0; }
 #muhkrlfkmj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #muhkrlfkmj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #muhkrlfkmj .gt_indent_1 { text-indent: 5px; }
 #muhkrlfkmj .gt_indent_2 { text-indent: calc(5px * 2); }
 #muhkrlfkmj .gt_indent_3 { text-indent: calc(5px * 3); }
 #muhkrlfkmj .gt_indent_4 { text-indent: calc(5px * 4); }
 #muhkrlfkmj .gt_indent_5 { text-indent: calc(5px * 5); }
 #muhkrlfkmj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #muhkrlfkmj .gt_row_group_first td { border-top-width: 2px; }
 #muhkrlfkmj .gt_row_group_first th { border-top-width: 2px; }
 #muhkrlfkmj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #muhkrlfkmj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muhkrlfkmj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #muhkrlfkmj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #muhkrlfkmj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muhkrlfkmj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #muhkrlfkmj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #muhkrlfkmj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #muhkrlfkmj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muhkrlfkmj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #muhkrlfkmj .gt_left { text-align: left; }
 #muhkrlfkmj .gt_center { text-align: center; }
 #muhkrlfkmj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #muhkrlfkmj .gt_font_normal { font-weight: normal; }
 #muhkrlfkmj .gt_font_bold { font-weight: bold; }
 #muhkrlfkmj .gt_font_italic { font-style: italic; }
 #muhkrlfkmj .gt_super { font-size: 65%; }
 #muhkrlfkmj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muhkrlfkmj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #muhkrlfkmj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muhkrlfkmj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #muhkrlfkmj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #muhkrlfkmj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|     | change  |
|-----|---------|
| X   | \>-0.01 |
| Y   | -5.3    |
| Z   | 0.7     |


The `-0.002` value is replaced since its absolute value falls below the threshold. The `sign="-"` argument tells the method to look for small negative values rather than small positive ones.


# Substituting Large Values

In some datasets, extremely large values can skew the reader's perception of the data. The [sub_large_vals()](../reference/GT.sub_large_vals.md#great_tables.GT.sub_large_vals) method lets you cap the displayed values at a threshold, replacing anything above it with indicator text.


``` python
gt_tbl.sub_large_vals(columns="revenue", threshold=1e10)
```


<style>
#gpqshzpxod table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gpqshzpxod thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gpqshzpxod p { margin: 0; padding: 0; }
 #gpqshzpxod .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gpqshzpxod .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gpqshzpxod .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gpqshzpxod .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gpqshzpxod .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gpqshzpxod .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gpqshzpxod .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gpqshzpxod .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gpqshzpxod .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gpqshzpxod .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gpqshzpxod .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gpqshzpxod .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gpqshzpxod .gt_spanner_row { border-bottom-style: hidden; }
 #gpqshzpxod .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gpqshzpxod .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gpqshzpxod .gt_from_md> :first-child { margin-top: 0; }
 #gpqshzpxod .gt_from_md> :last-child { margin-bottom: 0; }
 #gpqshzpxod .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gpqshzpxod .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gpqshzpxod .gt_indent_1 { text-indent: 5px; }
 #gpqshzpxod .gt_indent_2 { text-indent: calc(5px * 2); }
 #gpqshzpxod .gt_indent_3 { text-indent: calc(5px * 3); }
 #gpqshzpxod .gt_indent_4 { text-indent: calc(5px * 4); }
 #gpqshzpxod .gt_indent_5 { text-indent: calc(5px * 5); }
 #gpqshzpxod .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gpqshzpxod .gt_row_group_first td { border-top-width: 2px; }
 #gpqshzpxod .gt_row_group_first th { border-top-width: 2px; }
 #gpqshzpxod .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gpqshzpxod .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gpqshzpxod .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gpqshzpxod .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gpqshzpxod .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gpqshzpxod .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gpqshzpxod .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gpqshzpxod .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gpqshzpxod .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gpqshzpxod .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gpqshzpxod .gt_left { text-align: left; }
 #gpqshzpxod .gt_center { text-align: center; }
 #gpqshzpxod .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gpqshzpxod .gt_font_normal { font-weight: normal; }
 #gpqshzpxod .gt_font_bold { font-weight: bold; }
 #gpqshzpxod .gt_font_italic { font-style: italic; }
 #gpqshzpxod .gt_super { font-size: 65%; }
 #gpqshzpxod .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gpqshzpxod .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gpqshzpxod .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gpqshzpxod .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gpqshzpxod .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gpqshzpxod .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|          | count | rate  | revenue |
|----------|-------|-------|---------|
| Widget A | 150.0 | 0.003 | 4500.0  |
| Widget B | 0.0   | 0.0   | 0.0     |
| Widget C | 42.0  | 0.542 | ≥1e+10  |
| Widget D | None  | 0.871 | 75.5    |
| Widget E | 3.0   | None  | None    |


The value `1e13` in the `revenue` column is now shown as `"≥1e+10"` rather than displaying the full number. You can customize the pattern with the `large_pattern=` argument.


``` python
gt_tbl.sub_large_vals(columns="revenue", threshold=1e10, large_pattern="OVER {x}")
```


<style>
#ryovwxozyd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ryovwxozyd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ryovwxozyd p { margin: 0; padding: 0; }
 #ryovwxozyd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ryovwxozyd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ryovwxozyd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ryovwxozyd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ryovwxozyd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ryovwxozyd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ryovwxozyd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ryovwxozyd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ryovwxozyd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ryovwxozyd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ryovwxozyd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ryovwxozyd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ryovwxozyd .gt_spanner_row { border-bottom-style: hidden; }
 #ryovwxozyd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ryovwxozyd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ryovwxozyd .gt_from_md> :first-child { margin-top: 0; }
 #ryovwxozyd .gt_from_md> :last-child { margin-bottom: 0; }
 #ryovwxozyd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ryovwxozyd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ryovwxozyd .gt_indent_1 { text-indent: 5px; }
 #ryovwxozyd .gt_indent_2 { text-indent: calc(5px * 2); }
 #ryovwxozyd .gt_indent_3 { text-indent: calc(5px * 3); }
 #ryovwxozyd .gt_indent_4 { text-indent: calc(5px * 4); }
 #ryovwxozyd .gt_indent_5 { text-indent: calc(5px * 5); }
 #ryovwxozyd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ryovwxozyd .gt_row_group_first td { border-top-width: 2px; }
 #ryovwxozyd .gt_row_group_first th { border-top-width: 2px; }
 #ryovwxozyd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ryovwxozyd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ryovwxozyd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ryovwxozyd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ryovwxozyd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ryovwxozyd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ryovwxozyd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ryovwxozyd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ryovwxozyd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ryovwxozyd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ryovwxozyd .gt_left { text-align: left; }
 #ryovwxozyd .gt_center { text-align: center; }
 #ryovwxozyd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ryovwxozyd .gt_font_normal { font-weight: normal; }
 #ryovwxozyd .gt_font_bold { font-weight: bold; }
 #ryovwxozyd .gt_font_italic { font-style: italic; }
 #ryovwxozyd .gt_super { font-size: 65%; }
 #ryovwxozyd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ryovwxozyd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ryovwxozyd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ryovwxozyd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ryovwxozyd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ryovwxozyd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|          | count | rate  | revenue    |
|----------|-------|-------|------------|
| Widget A | 150.0 | 0.003 | 4500.0     |
| Widget B | 0.0   | 0.0   | 0.0        |
| Widget C | 42.0  | 0.542 | OVER 1e+10 |
| Widget D | None  | 0.871 | 75.5       |
| Widget E | 3.0   | None  | None       |


The `{x}` placeholder in the pattern is replaced with the threshold value, giving you full control over how the capped text reads.


# General Value Substitution

For more flexible replacement logic, [sub_values()](../reference/GT.sub_values.md#great_tables.GT.sub_values) provides three modes of matching: by exact value, by regex pattern, or by a custom function.


## Matching by Value

You can supply a specific value (or list of values) to match against. Any cell containing that value gets replaced.


``` python
GT(df, rowname_col="item").sub_values(columns="count", values=0, replacement="zero")
```


<style>
#aoefksneux table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#aoefksneux thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#aoefksneux p { margin: 0; padding: 0; }
 #aoefksneux .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #aoefksneux .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #aoefksneux .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #aoefksneux .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #aoefksneux .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aoefksneux .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aoefksneux .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aoefksneux .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #aoefksneux .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #aoefksneux .gt_column_spanner_outer:first-child { padding-left: 0; }
 #aoefksneux .gt_column_spanner_outer:last-child { padding-right: 0; }
 #aoefksneux .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #aoefksneux .gt_spanner_row { border-bottom-style: hidden; }
 #aoefksneux .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #aoefksneux .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #aoefksneux .gt_from_md> :first-child { margin-top: 0; }
 #aoefksneux .gt_from_md> :last-child { margin-bottom: 0; }
 #aoefksneux .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #aoefksneux .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #aoefksneux .gt_indent_1 { text-indent: 5px; }
 #aoefksneux .gt_indent_2 { text-indent: calc(5px * 2); }
 #aoefksneux .gt_indent_3 { text-indent: calc(5px * 3); }
 #aoefksneux .gt_indent_4 { text-indent: calc(5px * 4); }
 #aoefksneux .gt_indent_5 { text-indent: calc(5px * 5); }
 #aoefksneux .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #aoefksneux .gt_row_group_first td { border-top-width: 2px; }
 #aoefksneux .gt_row_group_first th { border-top-width: 2px; }
 #aoefksneux .gt_striped { color: #333333; background-color: #F4F4F4; }
 #aoefksneux .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aoefksneux .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aoefksneux .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #aoefksneux .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aoefksneux .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aoefksneux .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #aoefksneux .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #aoefksneux .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aoefksneux .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aoefksneux .gt_left { text-align: left; }
 #aoefksneux .gt_center { text-align: center; }
 #aoefksneux .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #aoefksneux .gt_font_normal { font-weight: normal; }
 #aoefksneux .gt_font_bold { font-weight: bold; }
 #aoefksneux .gt_font_italic { font-style: italic; }
 #aoefksneux .gt_super { font-size: 65%; }
 #aoefksneux .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aoefksneux .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #aoefksneux .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aoefksneux .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aoefksneux .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #aoefksneux .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|          | count | rate  | revenue          |
|----------|-------|-------|------------------|
| Widget A | 150.0 | 0.003 | 4500.0           |
| Widget B | zero  | 0.0   | 0.0              |
| Widget C | 42.0  | 0.542 | 10000000000000.0 |
| Widget D | None  | 0.871 | 75.5             |
| Widget E | 3.0   | None  | None             |


Every cell in the `count` column that contains exactly `0` is replaced with the string `"zero"`. You can also pass a list of values to match against multiple targets.


## Matching by Pattern

A regex pattern can target string-based cell content for replacement.


``` python
df_text = pd.DataFrame({
    "code": ["PASS-001", "FAIL-002", "PASS-003"],
    "result": ["ok", "error", "ok"],
})

GT(df_text).sub_values(columns="code", pattern=r"^FAIL.*", replacement="FLAGGED")
```


<style>
#kkykhyrzxn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kkykhyrzxn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kkykhyrzxn p { margin: 0; padding: 0; }
 #kkykhyrzxn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kkykhyrzxn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kkykhyrzxn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kkykhyrzxn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kkykhyrzxn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kkykhyrzxn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkykhyrzxn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kkykhyrzxn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kkykhyrzxn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kkykhyrzxn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kkykhyrzxn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kkykhyrzxn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kkykhyrzxn .gt_spanner_row { border-bottom-style: hidden; }
 #kkykhyrzxn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kkykhyrzxn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kkykhyrzxn .gt_from_md> :first-child { margin-top: 0; }
 #kkykhyrzxn .gt_from_md> :last-child { margin-bottom: 0; }
 #kkykhyrzxn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kkykhyrzxn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kkykhyrzxn .gt_indent_1 { text-indent: 5px; }
 #kkykhyrzxn .gt_indent_2 { text-indent: calc(5px * 2); }
 #kkykhyrzxn .gt_indent_3 { text-indent: calc(5px * 3); }
 #kkykhyrzxn .gt_indent_4 { text-indent: calc(5px * 4); }
 #kkykhyrzxn .gt_indent_5 { text-indent: calc(5px * 5); }
 #kkykhyrzxn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kkykhyrzxn .gt_row_group_first td { border-top-width: 2px; }
 #kkykhyrzxn .gt_row_group_first th { border-top-width: 2px; }
 #kkykhyrzxn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kkykhyrzxn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkykhyrzxn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kkykhyrzxn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kkykhyrzxn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kkykhyrzxn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kkykhyrzxn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kkykhyrzxn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kkykhyrzxn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkykhyrzxn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kkykhyrzxn .gt_left { text-align: left; }
 #kkykhyrzxn .gt_center { text-align: center; }
 #kkykhyrzxn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kkykhyrzxn .gt_font_normal { font-weight: normal; }
 #kkykhyrzxn .gt_font_bold { font-weight: bold; }
 #kkykhyrzxn .gt_font_italic { font-style: italic; }
 #kkykhyrzxn .gt_super { font-size: 65%; }
 #kkykhyrzxn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkykhyrzxn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kkykhyrzxn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kkykhyrzxn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kkykhyrzxn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kkykhyrzxn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| code     | result |
|----------|--------|
| PASS-001 | ok     |
| FLAGGED  | error  |
| PASS-003 | ok     |


The regex matches any cell starting with `"FAIL"` and replaces the entire content with `"FLAGGED"`. This is particularly useful for cleaning up status codes or categorized identifiers.


## Matching by Function

The most flexible approach uses a custom function. The function receives a cell value and should return `True` for values that need to be replaced.


``` python
GT(df, rowname_col="item").sub_values(
    columns="revenue",
    fn=lambda x: x is not None and x > 10000,
    replacement="HIGH"
)
```


<style>
#jwanfeyddx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jwanfeyddx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jwanfeyddx p { margin: 0; padding: 0; }
 #jwanfeyddx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jwanfeyddx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jwanfeyddx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jwanfeyddx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jwanfeyddx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jwanfeyddx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jwanfeyddx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jwanfeyddx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jwanfeyddx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jwanfeyddx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jwanfeyddx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jwanfeyddx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jwanfeyddx .gt_spanner_row { border-bottom-style: hidden; }
 #jwanfeyddx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jwanfeyddx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jwanfeyddx .gt_from_md> :first-child { margin-top: 0; }
 #jwanfeyddx .gt_from_md> :last-child { margin-bottom: 0; }
 #jwanfeyddx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jwanfeyddx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jwanfeyddx .gt_indent_1 { text-indent: 5px; }
 #jwanfeyddx .gt_indent_2 { text-indent: calc(5px * 2); }
 #jwanfeyddx .gt_indent_3 { text-indent: calc(5px * 3); }
 #jwanfeyddx .gt_indent_4 { text-indent: calc(5px * 4); }
 #jwanfeyddx .gt_indent_5 { text-indent: calc(5px * 5); }
 #jwanfeyddx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jwanfeyddx .gt_row_group_first td { border-top-width: 2px; }
 #jwanfeyddx .gt_row_group_first th { border-top-width: 2px; }
 #jwanfeyddx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jwanfeyddx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jwanfeyddx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jwanfeyddx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jwanfeyddx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jwanfeyddx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jwanfeyddx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jwanfeyddx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jwanfeyddx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jwanfeyddx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jwanfeyddx .gt_left { text-align: left; }
 #jwanfeyddx .gt_center { text-align: center; }
 #jwanfeyddx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jwanfeyddx .gt_font_normal { font-weight: normal; }
 #jwanfeyddx .gt_font_bold { font-weight: bold; }
 #jwanfeyddx .gt_font_italic { font-style: italic; }
 #jwanfeyddx .gt_super { font-size: 65%; }
 #jwanfeyddx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jwanfeyddx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jwanfeyddx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jwanfeyddx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jwanfeyddx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jwanfeyddx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|          | count | rate  | revenue |
|----------|-------|-------|---------|
| Widget A | 150.0 | 0.003 | 4500.0  |
| Widget B | 0.0   | 0.0   | 0.0     |
| Widget C | 42.0  | 0.542 | HIGH    |
| Widget D | None  | 0.871 | 75.5    |
| Widget E | 3.0   | None  | None    |


The function evaluates each cell value individually. When it returns `True`, that cell is replaced with the specified text. This mode handles complex logic that cannot be expressed as a simple value match or regex pattern.


# Combining Substitution Methods

You can chain multiple `sub_*()` calls together to handle several cases in a single table. The methods are applied in the order they are called.


``` python
(
    GT(df, rowname_col="item")
    .sub_missing(missing_text="N/A")
    .sub_zero(columns=["count", "rate"], zero_text="none")
    .sub_small_vals(columns="rate", threshold=0.01)
    .sub_large_vals(columns="revenue", threshold=1e10, large_pattern=">10B")
)
```


<style>
#jezdyejehv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jezdyejehv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jezdyejehv p { margin: 0; padding: 0; }
 #jezdyejehv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jezdyejehv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jezdyejehv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jezdyejehv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jezdyejehv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jezdyejehv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jezdyejehv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jezdyejehv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jezdyejehv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jezdyejehv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jezdyejehv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jezdyejehv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jezdyejehv .gt_spanner_row { border-bottom-style: hidden; }
 #jezdyejehv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jezdyejehv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jezdyejehv .gt_from_md> :first-child { margin-top: 0; }
 #jezdyejehv .gt_from_md> :last-child { margin-bottom: 0; }
 #jezdyejehv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jezdyejehv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jezdyejehv .gt_indent_1 { text-indent: 5px; }
 #jezdyejehv .gt_indent_2 { text-indent: calc(5px * 2); }
 #jezdyejehv .gt_indent_3 { text-indent: calc(5px * 3); }
 #jezdyejehv .gt_indent_4 { text-indent: calc(5px * 4); }
 #jezdyejehv .gt_indent_5 { text-indent: calc(5px * 5); }
 #jezdyejehv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jezdyejehv .gt_row_group_first td { border-top-width: 2px; }
 #jezdyejehv .gt_row_group_first th { border-top-width: 2px; }
 #jezdyejehv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jezdyejehv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jezdyejehv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jezdyejehv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jezdyejehv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jezdyejehv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jezdyejehv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jezdyejehv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jezdyejehv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jezdyejehv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jezdyejehv .gt_left { text-align: left; }
 #jezdyejehv .gt_center { text-align: center; }
 #jezdyejehv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jezdyejehv .gt_font_normal { font-weight: normal; }
 #jezdyejehv .gt_font_bold { font-weight: bold; }
 #jezdyejehv .gt_font_italic { font-style: italic; }
 #jezdyejehv .gt_super { font-size: 65%; }
 #jezdyejehv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jezdyejehv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jezdyejehv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jezdyejehv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jezdyejehv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jezdyejehv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|          | count | rate   | revenue |
|----------|-------|--------|---------|
| Widget A | 150.0 | \<0.01 | 4500.0  |
| Widget B | none  | none   | 0.0     |
| Widget C | 42.0  | 0.542  | \>10B   |
| Widget D | N/A   | 0.871  | 75.5    |
| Widget E | 3.0   | N/A    | N/A     |


This combination addresses missing data, zero values, very small numbers, and very large numbers all at once, producing a clean and informative table.

Because substitutions are applied before formatting, you can chain `sub_*()` and `fmt_*()` calls freely. The substitution handles the special cases first--missing values, zeros, outliers--and the formatter handles everything else. This separation keeps your table code clean and predictable: each layer has a single responsibility, and you don't need to write conditional logic inside your formatters to account for edge cases.

The `sub_*()` methods work as a pre-processing step before formatting. This means you can apply `fmt_*()` methods to the same columns and the substituted text will remain in place for cells that were already replaced, while the formatter handles the remaining values.
