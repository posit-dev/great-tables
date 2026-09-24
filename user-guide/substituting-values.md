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
#vhjgknzlko table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vhjgknzlko thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vhjgknzlko p { margin: 0; padding: 0; }
 #vhjgknzlko .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vhjgknzlko .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vhjgknzlko .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vhjgknzlko .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vhjgknzlko .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vhjgknzlko .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vhjgknzlko .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vhjgknzlko .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vhjgknzlko .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vhjgknzlko .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vhjgknzlko .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vhjgknzlko .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vhjgknzlko .gt_spanner_row { border-bottom-style: hidden; }
 #vhjgknzlko .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vhjgknzlko .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vhjgknzlko .gt_from_md> :first-child { margin-top: 0; }
 #vhjgknzlko .gt_from_md> :last-child { margin-bottom: 0; }
 #vhjgknzlko .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vhjgknzlko .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vhjgknzlko .gt_indent_1 { text-indent: 5px; }
 #vhjgknzlko .gt_indent_2 { text-indent: calc(5px * 2); }
 #vhjgknzlko .gt_indent_3 { text-indent: calc(5px * 3); }
 #vhjgknzlko .gt_indent_4 { text-indent: calc(5px * 4); }
 #vhjgknzlko .gt_indent_5 { text-indent: calc(5px * 5); }
 #vhjgknzlko .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vhjgknzlko .gt_row_group_first td { border-top-width: 2px; }
 #vhjgknzlko .gt_row_group_first th { border-top-width: 2px; }
 #vhjgknzlko .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vhjgknzlko .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vhjgknzlko .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vhjgknzlko .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vhjgknzlko .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vhjgknzlko .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vhjgknzlko .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vhjgknzlko .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vhjgknzlko .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vhjgknzlko .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vhjgknzlko .gt_left { text-align: left; }
 #vhjgknzlko .gt_center { text-align: center; }
 #vhjgknzlko .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vhjgknzlko .gt_font_normal { font-weight: normal; }
 #vhjgknzlko .gt_font_bold { font-weight: bold; }
 #vhjgknzlko .gt_font_italic { font-style: italic; }
 #vhjgknzlko .gt_super { font-size: 65%; }
 #vhjgknzlko .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vhjgknzlko .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vhjgknzlko .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vhjgknzlko .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vhjgknzlko .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vhjgknzlko .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#yhtsxztgjj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#yhtsxztgjj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#yhtsxztgjj p { margin: 0; padding: 0; }
 #yhtsxztgjj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #yhtsxztgjj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #yhtsxztgjj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #yhtsxztgjj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #yhtsxztgjj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yhtsxztgjj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yhtsxztgjj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yhtsxztgjj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #yhtsxztgjj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #yhtsxztgjj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #yhtsxztgjj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #yhtsxztgjj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #yhtsxztgjj .gt_spanner_row { border-bottom-style: hidden; }
 #yhtsxztgjj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #yhtsxztgjj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #yhtsxztgjj .gt_from_md> :first-child { margin-top: 0; }
 #yhtsxztgjj .gt_from_md> :last-child { margin-bottom: 0; }
 #yhtsxztgjj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #yhtsxztgjj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #yhtsxztgjj .gt_indent_1 { text-indent: 5px; }
 #yhtsxztgjj .gt_indent_2 { text-indent: calc(5px * 2); }
 #yhtsxztgjj .gt_indent_3 { text-indent: calc(5px * 3); }
 #yhtsxztgjj .gt_indent_4 { text-indent: calc(5px * 4); }
 #yhtsxztgjj .gt_indent_5 { text-indent: calc(5px * 5); }
 #yhtsxztgjj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #yhtsxztgjj .gt_row_group_first td { border-top-width: 2px; }
 #yhtsxztgjj .gt_row_group_first th { border-top-width: 2px; }
 #yhtsxztgjj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #yhtsxztgjj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yhtsxztgjj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yhtsxztgjj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #yhtsxztgjj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yhtsxztgjj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yhtsxztgjj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #yhtsxztgjj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #yhtsxztgjj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yhtsxztgjj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yhtsxztgjj .gt_left { text-align: left; }
 #yhtsxztgjj .gt_center { text-align: center; }
 #yhtsxztgjj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #yhtsxztgjj .gt_font_normal { font-weight: normal; }
 #yhtsxztgjj .gt_font_bold { font-weight: bold; }
 #yhtsxztgjj .gt_font_italic { font-style: italic; }
 #yhtsxztgjj .gt_super { font-size: 65%; }
 #yhtsxztgjj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yhtsxztgjj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #yhtsxztgjj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yhtsxztgjj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yhtsxztgjj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #yhtsxztgjj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#luslcutony table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#luslcutony thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#luslcutony p { margin: 0; padding: 0; }
 #luslcutony .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #luslcutony .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #luslcutony .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #luslcutony .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #luslcutony .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #luslcutony .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #luslcutony .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #luslcutony .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #luslcutony .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #luslcutony .gt_column_spanner_outer:first-child { padding-left: 0; }
 #luslcutony .gt_column_spanner_outer:last-child { padding-right: 0; }
 #luslcutony .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #luslcutony .gt_spanner_row { border-bottom-style: hidden; }
 #luslcutony .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #luslcutony .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #luslcutony .gt_from_md> :first-child { margin-top: 0; }
 #luslcutony .gt_from_md> :last-child { margin-bottom: 0; }
 #luslcutony .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #luslcutony .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #luslcutony .gt_indent_1 { text-indent: 5px; }
 #luslcutony .gt_indent_2 { text-indent: calc(5px * 2); }
 #luslcutony .gt_indent_3 { text-indent: calc(5px * 3); }
 #luslcutony .gt_indent_4 { text-indent: calc(5px * 4); }
 #luslcutony .gt_indent_5 { text-indent: calc(5px * 5); }
 #luslcutony .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #luslcutony .gt_row_group_first td { border-top-width: 2px; }
 #luslcutony .gt_row_group_first th { border-top-width: 2px; }
 #luslcutony .gt_striped { color: #333333; background-color: #F4F4F4; }
 #luslcutony .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #luslcutony .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #luslcutony .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #luslcutony .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #luslcutony .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #luslcutony .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #luslcutony .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #luslcutony .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #luslcutony .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #luslcutony .gt_left { text-align: left; }
 #luslcutony .gt_center { text-align: center; }
 #luslcutony .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #luslcutony .gt_font_normal { font-weight: normal; }
 #luslcutony .gt_font_bold { font-weight: bold; }
 #luslcutony .gt_font_italic { font-style: italic; }
 #luslcutony .gt_super { font-size: 65%; }
 #luslcutony .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #luslcutony .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #luslcutony .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #luslcutony .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #luslcutony .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #luslcutony .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#mwcoxofdmp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mwcoxofdmp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mwcoxofdmp p { margin: 0; padding: 0; }
 #mwcoxofdmp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mwcoxofdmp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mwcoxofdmp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mwcoxofdmp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mwcoxofdmp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mwcoxofdmp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mwcoxofdmp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mwcoxofdmp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mwcoxofdmp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mwcoxofdmp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mwcoxofdmp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mwcoxofdmp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mwcoxofdmp .gt_spanner_row { border-bottom-style: hidden; }
 #mwcoxofdmp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mwcoxofdmp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mwcoxofdmp .gt_from_md> :first-child { margin-top: 0; }
 #mwcoxofdmp .gt_from_md> :last-child { margin-bottom: 0; }
 #mwcoxofdmp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mwcoxofdmp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mwcoxofdmp .gt_indent_1 { text-indent: 5px; }
 #mwcoxofdmp .gt_indent_2 { text-indent: calc(5px * 2); }
 #mwcoxofdmp .gt_indent_3 { text-indent: calc(5px * 3); }
 #mwcoxofdmp .gt_indent_4 { text-indent: calc(5px * 4); }
 #mwcoxofdmp .gt_indent_5 { text-indent: calc(5px * 5); }
 #mwcoxofdmp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mwcoxofdmp .gt_row_group_first td { border-top-width: 2px; }
 #mwcoxofdmp .gt_row_group_first th { border-top-width: 2px; }
 #mwcoxofdmp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mwcoxofdmp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mwcoxofdmp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mwcoxofdmp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mwcoxofdmp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mwcoxofdmp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mwcoxofdmp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mwcoxofdmp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mwcoxofdmp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mwcoxofdmp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mwcoxofdmp .gt_left { text-align: left; }
 #mwcoxofdmp .gt_center { text-align: center; }
 #mwcoxofdmp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mwcoxofdmp .gt_font_normal { font-weight: normal; }
 #mwcoxofdmp .gt_font_bold { font-weight: bold; }
 #mwcoxofdmp .gt_font_italic { font-style: italic; }
 #mwcoxofdmp .gt_super { font-size: 65%; }
 #mwcoxofdmp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mwcoxofdmp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mwcoxofdmp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mwcoxofdmp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mwcoxofdmp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mwcoxofdmp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#nooehbgntq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nooehbgntq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nooehbgntq p { margin: 0; padding: 0; }
 #nooehbgntq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nooehbgntq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nooehbgntq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nooehbgntq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nooehbgntq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nooehbgntq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nooehbgntq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nooehbgntq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nooehbgntq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nooehbgntq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nooehbgntq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nooehbgntq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nooehbgntq .gt_spanner_row { border-bottom-style: hidden; }
 #nooehbgntq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nooehbgntq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nooehbgntq .gt_from_md> :first-child { margin-top: 0; }
 #nooehbgntq .gt_from_md> :last-child { margin-bottom: 0; }
 #nooehbgntq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nooehbgntq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nooehbgntq .gt_indent_1 { text-indent: 5px; }
 #nooehbgntq .gt_indent_2 { text-indent: calc(5px * 2); }
 #nooehbgntq .gt_indent_3 { text-indent: calc(5px * 3); }
 #nooehbgntq .gt_indent_4 { text-indent: calc(5px * 4); }
 #nooehbgntq .gt_indent_5 { text-indent: calc(5px * 5); }
 #nooehbgntq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nooehbgntq .gt_row_group_first td { border-top-width: 2px; }
 #nooehbgntq .gt_row_group_first th { border-top-width: 2px; }
 #nooehbgntq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nooehbgntq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nooehbgntq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nooehbgntq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nooehbgntq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nooehbgntq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nooehbgntq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nooehbgntq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nooehbgntq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nooehbgntq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nooehbgntq .gt_left { text-align: left; }
 #nooehbgntq .gt_center { text-align: center; }
 #nooehbgntq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nooehbgntq .gt_font_normal { font-weight: normal; }
 #nooehbgntq .gt_font_bold { font-weight: bold; }
 #nooehbgntq .gt_font_italic { font-style: italic; }
 #nooehbgntq .gt_super { font-size: 65%; }
 #nooehbgntq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nooehbgntq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nooehbgntq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nooehbgntq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nooehbgntq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nooehbgntq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ufnrhxtrjd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ufnrhxtrjd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ufnrhxtrjd p { margin: 0; padding: 0; }
 #ufnrhxtrjd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ufnrhxtrjd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ufnrhxtrjd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ufnrhxtrjd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ufnrhxtrjd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ufnrhxtrjd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ufnrhxtrjd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ufnrhxtrjd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ufnrhxtrjd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ufnrhxtrjd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ufnrhxtrjd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ufnrhxtrjd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ufnrhxtrjd .gt_spanner_row { border-bottom-style: hidden; }
 #ufnrhxtrjd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ufnrhxtrjd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ufnrhxtrjd .gt_from_md> :first-child { margin-top: 0; }
 #ufnrhxtrjd .gt_from_md> :last-child { margin-bottom: 0; }
 #ufnrhxtrjd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ufnrhxtrjd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ufnrhxtrjd .gt_indent_1 { text-indent: 5px; }
 #ufnrhxtrjd .gt_indent_2 { text-indent: calc(5px * 2); }
 #ufnrhxtrjd .gt_indent_3 { text-indent: calc(5px * 3); }
 #ufnrhxtrjd .gt_indent_4 { text-indent: calc(5px * 4); }
 #ufnrhxtrjd .gt_indent_5 { text-indent: calc(5px * 5); }
 #ufnrhxtrjd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ufnrhxtrjd .gt_row_group_first td { border-top-width: 2px; }
 #ufnrhxtrjd .gt_row_group_first th { border-top-width: 2px; }
 #ufnrhxtrjd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ufnrhxtrjd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ufnrhxtrjd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ufnrhxtrjd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ufnrhxtrjd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ufnrhxtrjd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ufnrhxtrjd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ufnrhxtrjd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ufnrhxtrjd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ufnrhxtrjd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ufnrhxtrjd .gt_left { text-align: left; }
 #ufnrhxtrjd .gt_center { text-align: center; }
 #ufnrhxtrjd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ufnrhxtrjd .gt_font_normal { font-weight: normal; }
 #ufnrhxtrjd .gt_font_bold { font-weight: bold; }
 #ufnrhxtrjd .gt_font_italic { font-style: italic; }
 #ufnrhxtrjd .gt_super { font-size: 65%; }
 #ufnrhxtrjd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ufnrhxtrjd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ufnrhxtrjd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ufnrhxtrjd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ufnrhxtrjd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ufnrhxtrjd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#yyekkbfaau table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#yyekkbfaau thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#yyekkbfaau p { margin: 0; padding: 0; }
 #yyekkbfaau .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #yyekkbfaau .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #yyekkbfaau .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #yyekkbfaau .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #yyekkbfaau .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yyekkbfaau .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yyekkbfaau .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yyekkbfaau .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #yyekkbfaau .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #yyekkbfaau .gt_column_spanner_outer:first-child { padding-left: 0; }
 #yyekkbfaau .gt_column_spanner_outer:last-child { padding-right: 0; }
 #yyekkbfaau .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #yyekkbfaau .gt_spanner_row { border-bottom-style: hidden; }
 #yyekkbfaau .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #yyekkbfaau .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #yyekkbfaau .gt_from_md> :first-child { margin-top: 0; }
 #yyekkbfaau .gt_from_md> :last-child { margin-bottom: 0; }
 #yyekkbfaau .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #yyekkbfaau .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #yyekkbfaau .gt_indent_1 { text-indent: 5px; }
 #yyekkbfaau .gt_indent_2 { text-indent: calc(5px * 2); }
 #yyekkbfaau .gt_indent_3 { text-indent: calc(5px * 3); }
 #yyekkbfaau .gt_indent_4 { text-indent: calc(5px * 4); }
 #yyekkbfaau .gt_indent_5 { text-indent: calc(5px * 5); }
 #yyekkbfaau .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #yyekkbfaau .gt_row_group_first td { border-top-width: 2px; }
 #yyekkbfaau .gt_row_group_first th { border-top-width: 2px; }
 #yyekkbfaau .gt_striped { color: #333333; background-color: #F4F4F4; }
 #yyekkbfaau .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yyekkbfaau .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yyekkbfaau .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #yyekkbfaau .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yyekkbfaau .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yyekkbfaau .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #yyekkbfaau .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #yyekkbfaau .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yyekkbfaau .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yyekkbfaau .gt_left { text-align: left; }
 #yyekkbfaau .gt_center { text-align: center; }
 #yyekkbfaau .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #yyekkbfaau .gt_font_normal { font-weight: normal; }
 #yyekkbfaau .gt_font_bold { font-weight: bold; }
 #yyekkbfaau .gt_font_italic { font-style: italic; }
 #yyekkbfaau .gt_super { font-size: 65%; }
 #yyekkbfaau .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yyekkbfaau .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #yyekkbfaau .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yyekkbfaau .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yyekkbfaau .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #yyekkbfaau .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|          | count | rate  | revenue          |
|----------|-------|-------|------------------|
| Widget A | 150.0 | 0.003 | 4500.0           |
| Widget B | 0.0   | 0.0   | 0.0              |
| Widget C | 42.0  | 0.542 | \>=10000000000.0 |
| Widget D | None  | 0.871 | 75.5             |
| Widget E | 3.0   | None  | None             |


The value `1e13` in the `revenue` column is now shown as `">=10000000000.0"` rather than displaying the full number. You can customize the pattern with the `large_pattern=` argument.


``` python
gt_tbl.sub_large_vals(columns="revenue", threshold=1e10, large_pattern="OVER {x}")
```


<style>
#loqygznwis table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#loqygznwis thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#loqygznwis p { margin: 0; padding: 0; }
 #loqygznwis .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #loqygznwis .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #loqygznwis .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #loqygznwis .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #loqygznwis .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #loqygznwis .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #loqygznwis .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #loqygznwis .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #loqygznwis .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #loqygznwis .gt_column_spanner_outer:first-child { padding-left: 0; }
 #loqygznwis .gt_column_spanner_outer:last-child { padding-right: 0; }
 #loqygznwis .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #loqygznwis .gt_spanner_row { border-bottom-style: hidden; }
 #loqygznwis .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #loqygznwis .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #loqygznwis .gt_from_md> :first-child { margin-top: 0; }
 #loqygznwis .gt_from_md> :last-child { margin-bottom: 0; }
 #loqygznwis .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #loqygznwis .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #loqygznwis .gt_indent_1 { text-indent: 5px; }
 #loqygznwis .gt_indent_2 { text-indent: calc(5px * 2); }
 #loqygznwis .gt_indent_3 { text-indent: calc(5px * 3); }
 #loqygznwis .gt_indent_4 { text-indent: calc(5px * 4); }
 #loqygznwis .gt_indent_5 { text-indent: calc(5px * 5); }
 #loqygznwis .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #loqygznwis .gt_row_group_first td { border-top-width: 2px; }
 #loqygznwis .gt_row_group_first th { border-top-width: 2px; }
 #loqygznwis .gt_striped { color: #333333; background-color: #F4F4F4; }
 #loqygznwis .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #loqygznwis .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #loqygznwis .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #loqygznwis .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #loqygznwis .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #loqygznwis .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #loqygznwis .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #loqygznwis .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #loqygznwis .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #loqygznwis .gt_left { text-align: left; }
 #loqygznwis .gt_center { text-align: center; }
 #loqygznwis .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #loqygznwis .gt_font_normal { font-weight: normal; }
 #loqygznwis .gt_font_bold { font-weight: bold; }
 #loqygznwis .gt_font_italic { font-style: italic; }
 #loqygznwis .gt_super { font-size: 65%; }
 #loqygznwis .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #loqygznwis .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #loqygznwis .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #loqygznwis .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #loqygznwis .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #loqygznwis .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|          | count | rate  | revenue            |
|----------|-------|-------|--------------------|
| Widget A | 150.0 | 0.003 | 4500.0             |
| Widget B | 0.0   | 0.0   | 0.0                |
| Widget C | 42.0  | 0.542 | OVER 10000000000.0 |
| Widget D | None  | 0.871 | 75.5               |
| Widget E | 3.0   | None  | None               |


The `{x}` placeholder in the pattern is replaced with the threshold value, giving you full control over how the capped text reads.


# General Value Substitution

For more flexible replacement logic, [sub_values()](../reference/GT.sub_values.md#great_tables.GT.sub_values) provides three modes of matching: by exact value, by regex pattern, or by a custom function.


## Matching by Value

You can supply a specific value (or list of values) to match against. Any cell containing that value gets replaced.


``` python
GT(df, rowname_col="item").sub_values(columns="count", values=0, replacement="zero")
```


<style>
#yextyemyrg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#yextyemyrg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#yextyemyrg p { margin: 0; padding: 0; }
 #yextyemyrg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #yextyemyrg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #yextyemyrg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #yextyemyrg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #yextyemyrg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yextyemyrg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yextyemyrg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yextyemyrg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #yextyemyrg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #yextyemyrg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #yextyemyrg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #yextyemyrg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #yextyemyrg .gt_spanner_row { border-bottom-style: hidden; }
 #yextyemyrg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #yextyemyrg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #yextyemyrg .gt_from_md> :first-child { margin-top: 0; }
 #yextyemyrg .gt_from_md> :last-child { margin-bottom: 0; }
 #yextyemyrg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #yextyemyrg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #yextyemyrg .gt_indent_1 { text-indent: 5px; }
 #yextyemyrg .gt_indent_2 { text-indent: calc(5px * 2); }
 #yextyemyrg .gt_indent_3 { text-indent: calc(5px * 3); }
 #yextyemyrg .gt_indent_4 { text-indent: calc(5px * 4); }
 #yextyemyrg .gt_indent_5 { text-indent: calc(5px * 5); }
 #yextyemyrg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #yextyemyrg .gt_row_group_first td { border-top-width: 2px; }
 #yextyemyrg .gt_row_group_first th { border-top-width: 2px; }
 #yextyemyrg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #yextyemyrg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yextyemyrg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yextyemyrg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #yextyemyrg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yextyemyrg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yextyemyrg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #yextyemyrg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #yextyemyrg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yextyemyrg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yextyemyrg .gt_left { text-align: left; }
 #yextyemyrg .gt_center { text-align: center; }
 #yextyemyrg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #yextyemyrg .gt_font_normal { font-weight: normal; }
 #yextyemyrg .gt_font_bold { font-weight: bold; }
 #yextyemyrg .gt_font_italic { font-style: italic; }
 #yextyemyrg .gt_super { font-size: 65%; }
 #yextyemyrg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yextyemyrg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #yextyemyrg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yextyemyrg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yextyemyrg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #yextyemyrg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ujmnpwlhdb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ujmnpwlhdb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ujmnpwlhdb p { margin: 0; padding: 0; }
 #ujmnpwlhdb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ujmnpwlhdb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ujmnpwlhdb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ujmnpwlhdb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ujmnpwlhdb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ujmnpwlhdb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ujmnpwlhdb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ujmnpwlhdb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ujmnpwlhdb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ujmnpwlhdb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ujmnpwlhdb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ujmnpwlhdb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ujmnpwlhdb .gt_spanner_row { border-bottom-style: hidden; }
 #ujmnpwlhdb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ujmnpwlhdb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ujmnpwlhdb .gt_from_md> :first-child { margin-top: 0; }
 #ujmnpwlhdb .gt_from_md> :last-child { margin-bottom: 0; }
 #ujmnpwlhdb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ujmnpwlhdb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ujmnpwlhdb .gt_indent_1 { text-indent: 5px; }
 #ujmnpwlhdb .gt_indent_2 { text-indent: calc(5px * 2); }
 #ujmnpwlhdb .gt_indent_3 { text-indent: calc(5px * 3); }
 #ujmnpwlhdb .gt_indent_4 { text-indent: calc(5px * 4); }
 #ujmnpwlhdb .gt_indent_5 { text-indent: calc(5px * 5); }
 #ujmnpwlhdb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ujmnpwlhdb .gt_row_group_first td { border-top-width: 2px; }
 #ujmnpwlhdb .gt_row_group_first th { border-top-width: 2px; }
 #ujmnpwlhdb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ujmnpwlhdb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ujmnpwlhdb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ujmnpwlhdb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ujmnpwlhdb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ujmnpwlhdb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ujmnpwlhdb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ujmnpwlhdb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ujmnpwlhdb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ujmnpwlhdb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ujmnpwlhdb .gt_left { text-align: left; }
 #ujmnpwlhdb .gt_center { text-align: center; }
 #ujmnpwlhdb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ujmnpwlhdb .gt_font_normal { font-weight: normal; }
 #ujmnpwlhdb .gt_font_bold { font-weight: bold; }
 #ujmnpwlhdb .gt_font_italic { font-style: italic; }
 #ujmnpwlhdb .gt_super { font-size: 65%; }
 #ujmnpwlhdb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ujmnpwlhdb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ujmnpwlhdb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ujmnpwlhdb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ujmnpwlhdb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ujmnpwlhdb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qqpdwzirjh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qqpdwzirjh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qqpdwzirjh p { margin: 0; padding: 0; }
 #qqpdwzirjh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qqpdwzirjh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qqpdwzirjh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qqpdwzirjh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qqpdwzirjh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qqpdwzirjh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qqpdwzirjh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qqpdwzirjh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qqpdwzirjh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qqpdwzirjh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qqpdwzirjh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qqpdwzirjh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qqpdwzirjh .gt_spanner_row { border-bottom-style: hidden; }
 #qqpdwzirjh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qqpdwzirjh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qqpdwzirjh .gt_from_md> :first-child { margin-top: 0; }
 #qqpdwzirjh .gt_from_md> :last-child { margin-bottom: 0; }
 #qqpdwzirjh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qqpdwzirjh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qqpdwzirjh .gt_indent_1 { text-indent: 5px; }
 #qqpdwzirjh .gt_indent_2 { text-indent: calc(5px * 2); }
 #qqpdwzirjh .gt_indent_3 { text-indent: calc(5px * 3); }
 #qqpdwzirjh .gt_indent_4 { text-indent: calc(5px * 4); }
 #qqpdwzirjh .gt_indent_5 { text-indent: calc(5px * 5); }
 #qqpdwzirjh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qqpdwzirjh .gt_row_group_first td { border-top-width: 2px; }
 #qqpdwzirjh .gt_row_group_first th { border-top-width: 2px; }
 #qqpdwzirjh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qqpdwzirjh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qqpdwzirjh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qqpdwzirjh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qqpdwzirjh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qqpdwzirjh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qqpdwzirjh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qqpdwzirjh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qqpdwzirjh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qqpdwzirjh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qqpdwzirjh .gt_left { text-align: left; }
 #qqpdwzirjh .gt_center { text-align: center; }
 #qqpdwzirjh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qqpdwzirjh .gt_font_normal { font-weight: normal; }
 #qqpdwzirjh .gt_font_bold { font-weight: bold; }
 #qqpdwzirjh .gt_font_italic { font-style: italic; }
 #qqpdwzirjh .gt_super { font-size: 65%; }
 #qqpdwzirjh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qqpdwzirjh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qqpdwzirjh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qqpdwzirjh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qqpdwzirjh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qqpdwzirjh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dxdhrgctyg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dxdhrgctyg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dxdhrgctyg p { margin: 0; padding: 0; }
 #dxdhrgctyg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dxdhrgctyg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dxdhrgctyg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dxdhrgctyg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dxdhrgctyg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dxdhrgctyg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxdhrgctyg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dxdhrgctyg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dxdhrgctyg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dxdhrgctyg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dxdhrgctyg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dxdhrgctyg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dxdhrgctyg .gt_spanner_row { border-bottom-style: hidden; }
 #dxdhrgctyg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dxdhrgctyg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dxdhrgctyg .gt_from_md> :first-child { margin-top: 0; }
 #dxdhrgctyg .gt_from_md> :last-child { margin-bottom: 0; }
 #dxdhrgctyg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dxdhrgctyg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dxdhrgctyg .gt_indent_1 { text-indent: 5px; }
 #dxdhrgctyg .gt_indent_2 { text-indent: calc(5px * 2); }
 #dxdhrgctyg .gt_indent_3 { text-indent: calc(5px * 3); }
 #dxdhrgctyg .gt_indent_4 { text-indent: calc(5px * 4); }
 #dxdhrgctyg .gt_indent_5 { text-indent: calc(5px * 5); }
 #dxdhrgctyg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dxdhrgctyg .gt_row_group_first td { border-top-width: 2px; }
 #dxdhrgctyg .gt_row_group_first th { border-top-width: 2px; }
 #dxdhrgctyg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dxdhrgctyg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxdhrgctyg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dxdhrgctyg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dxdhrgctyg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxdhrgctyg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dxdhrgctyg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dxdhrgctyg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dxdhrgctyg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxdhrgctyg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dxdhrgctyg .gt_left { text-align: left; }
 #dxdhrgctyg .gt_center { text-align: center; }
 #dxdhrgctyg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dxdhrgctyg .gt_font_normal { font-weight: normal; }
 #dxdhrgctyg .gt_font_bold { font-weight: bold; }
 #dxdhrgctyg .gt_font_italic { font-style: italic; }
 #dxdhrgctyg .gt_super { font-size: 65%; }
 #dxdhrgctyg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxdhrgctyg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dxdhrgctyg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxdhrgctyg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dxdhrgctyg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dxdhrgctyg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
