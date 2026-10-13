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
#pditspofce table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pditspofce thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pditspofce p { margin: 0; padding: 0; }
 #pditspofce .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pditspofce .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pditspofce .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pditspofce .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pditspofce .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pditspofce .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pditspofce .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pditspofce .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pditspofce .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pditspofce .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pditspofce .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pditspofce .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pditspofce .gt_spanner_row { border-bottom-style: hidden; }
 #pditspofce .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pditspofce .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pditspofce .gt_from_md> :first-child { margin-top: 0; }
 #pditspofce .gt_from_md> :last-child { margin-bottom: 0; }
 #pditspofce .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pditspofce .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pditspofce .gt_indent_1 { text-indent: 5px; }
 #pditspofce .gt_indent_2 { text-indent: calc(5px * 2); }
 #pditspofce .gt_indent_3 { text-indent: calc(5px * 3); }
 #pditspofce .gt_indent_4 { text-indent: calc(5px * 4); }
 #pditspofce .gt_indent_5 { text-indent: calc(5px * 5); }
 #pditspofce .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pditspofce .gt_row_group_first td { border-top-width: 2px; }
 #pditspofce .gt_row_group_first th { border-top-width: 2px; }
 #pditspofce .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pditspofce .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pditspofce .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pditspofce .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pditspofce .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pditspofce .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pditspofce .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pditspofce .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pditspofce .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pditspofce .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pditspofce .gt_left { text-align: left; }
 #pditspofce .gt_center { text-align: center; }
 #pditspofce .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pditspofce .gt_font_normal { font-weight: normal; }
 #pditspofce .gt_font_bold { font-weight: bold; }
 #pditspofce .gt_font_italic { font-style: italic; }
 #pditspofce .gt_super { font-size: 65%; }
 #pditspofce .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pditspofce .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pditspofce .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pditspofce .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pditspofce .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pditspofce .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qeiakrsyok table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qeiakrsyok thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qeiakrsyok p { margin: 0; padding: 0; }
 #qeiakrsyok .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qeiakrsyok .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qeiakrsyok .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qeiakrsyok .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qeiakrsyok .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qeiakrsyok .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qeiakrsyok .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qeiakrsyok .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qeiakrsyok .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qeiakrsyok .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qeiakrsyok .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qeiakrsyok .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qeiakrsyok .gt_spanner_row { border-bottom-style: hidden; }
 #qeiakrsyok .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qeiakrsyok .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qeiakrsyok .gt_from_md> :first-child { margin-top: 0; }
 #qeiakrsyok .gt_from_md> :last-child { margin-bottom: 0; }
 #qeiakrsyok .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qeiakrsyok .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qeiakrsyok .gt_indent_1 { text-indent: 5px; }
 #qeiakrsyok .gt_indent_2 { text-indent: calc(5px * 2); }
 #qeiakrsyok .gt_indent_3 { text-indent: calc(5px * 3); }
 #qeiakrsyok .gt_indent_4 { text-indent: calc(5px * 4); }
 #qeiakrsyok .gt_indent_5 { text-indent: calc(5px * 5); }
 #qeiakrsyok .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qeiakrsyok .gt_row_group_first td { border-top-width: 2px; }
 #qeiakrsyok .gt_row_group_first th { border-top-width: 2px; }
 #qeiakrsyok .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qeiakrsyok .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qeiakrsyok .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qeiakrsyok .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qeiakrsyok .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qeiakrsyok .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qeiakrsyok .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qeiakrsyok .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qeiakrsyok .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qeiakrsyok .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qeiakrsyok .gt_left { text-align: left; }
 #qeiakrsyok .gt_center { text-align: center; }
 #qeiakrsyok .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qeiakrsyok .gt_font_normal { font-weight: normal; }
 #qeiakrsyok .gt_font_bold { font-weight: bold; }
 #qeiakrsyok .gt_font_italic { font-style: italic; }
 #qeiakrsyok .gt_super { font-size: 65%; }
 #qeiakrsyok .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qeiakrsyok .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qeiakrsyok .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qeiakrsyok .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qeiakrsyok .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qeiakrsyok .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jgvbjlhkvz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jgvbjlhkvz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jgvbjlhkvz p { margin: 0; padding: 0; }
 #jgvbjlhkvz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jgvbjlhkvz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jgvbjlhkvz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jgvbjlhkvz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jgvbjlhkvz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jgvbjlhkvz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jgvbjlhkvz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jgvbjlhkvz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jgvbjlhkvz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jgvbjlhkvz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jgvbjlhkvz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jgvbjlhkvz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jgvbjlhkvz .gt_spanner_row { border-bottom-style: hidden; }
 #jgvbjlhkvz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jgvbjlhkvz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jgvbjlhkvz .gt_from_md> :first-child { margin-top: 0; }
 #jgvbjlhkvz .gt_from_md> :last-child { margin-bottom: 0; }
 #jgvbjlhkvz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jgvbjlhkvz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jgvbjlhkvz .gt_indent_1 { text-indent: 5px; }
 #jgvbjlhkvz .gt_indent_2 { text-indent: calc(5px * 2); }
 #jgvbjlhkvz .gt_indent_3 { text-indent: calc(5px * 3); }
 #jgvbjlhkvz .gt_indent_4 { text-indent: calc(5px * 4); }
 #jgvbjlhkvz .gt_indent_5 { text-indent: calc(5px * 5); }
 #jgvbjlhkvz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jgvbjlhkvz .gt_row_group_first td { border-top-width: 2px; }
 #jgvbjlhkvz .gt_row_group_first th { border-top-width: 2px; }
 #jgvbjlhkvz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jgvbjlhkvz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jgvbjlhkvz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jgvbjlhkvz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jgvbjlhkvz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jgvbjlhkvz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jgvbjlhkvz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jgvbjlhkvz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jgvbjlhkvz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jgvbjlhkvz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jgvbjlhkvz .gt_left { text-align: left; }
 #jgvbjlhkvz .gt_center { text-align: center; }
 #jgvbjlhkvz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jgvbjlhkvz .gt_font_normal { font-weight: normal; }
 #jgvbjlhkvz .gt_font_bold { font-weight: bold; }
 #jgvbjlhkvz .gt_font_italic { font-style: italic; }
 #jgvbjlhkvz .gt_super { font-size: 65%; }
 #jgvbjlhkvz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jgvbjlhkvz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jgvbjlhkvz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jgvbjlhkvz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jgvbjlhkvz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jgvbjlhkvz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hsffmydhfx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hsffmydhfx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hsffmydhfx p { margin: 0; padding: 0; }
 #hsffmydhfx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hsffmydhfx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hsffmydhfx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hsffmydhfx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hsffmydhfx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hsffmydhfx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hsffmydhfx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hsffmydhfx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hsffmydhfx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hsffmydhfx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hsffmydhfx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hsffmydhfx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hsffmydhfx .gt_spanner_row { border-bottom-style: hidden; }
 #hsffmydhfx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hsffmydhfx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hsffmydhfx .gt_from_md> :first-child { margin-top: 0; }
 #hsffmydhfx .gt_from_md> :last-child { margin-bottom: 0; }
 #hsffmydhfx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hsffmydhfx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hsffmydhfx .gt_indent_1 { text-indent: 5px; }
 #hsffmydhfx .gt_indent_2 { text-indent: calc(5px * 2); }
 #hsffmydhfx .gt_indent_3 { text-indent: calc(5px * 3); }
 #hsffmydhfx .gt_indent_4 { text-indent: calc(5px * 4); }
 #hsffmydhfx .gt_indent_5 { text-indent: calc(5px * 5); }
 #hsffmydhfx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hsffmydhfx .gt_row_group_first td { border-top-width: 2px; }
 #hsffmydhfx .gt_row_group_first th { border-top-width: 2px; }
 #hsffmydhfx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hsffmydhfx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hsffmydhfx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hsffmydhfx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hsffmydhfx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hsffmydhfx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hsffmydhfx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hsffmydhfx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hsffmydhfx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hsffmydhfx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hsffmydhfx .gt_left { text-align: left; }
 #hsffmydhfx .gt_center { text-align: center; }
 #hsffmydhfx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hsffmydhfx .gt_font_normal { font-weight: normal; }
 #hsffmydhfx .gt_font_bold { font-weight: bold; }
 #hsffmydhfx .gt_font_italic { font-style: italic; }
 #hsffmydhfx .gt_super { font-size: 65%; }
 #hsffmydhfx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hsffmydhfx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hsffmydhfx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hsffmydhfx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hsffmydhfx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hsffmydhfx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rqagrcufnm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rqagrcufnm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rqagrcufnm p { margin: 0; padding: 0; }
 #rqagrcufnm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rqagrcufnm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rqagrcufnm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rqagrcufnm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rqagrcufnm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rqagrcufnm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rqagrcufnm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rqagrcufnm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rqagrcufnm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rqagrcufnm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rqagrcufnm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rqagrcufnm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rqagrcufnm .gt_spanner_row { border-bottom-style: hidden; }
 #rqagrcufnm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rqagrcufnm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rqagrcufnm .gt_from_md> :first-child { margin-top: 0; }
 #rqagrcufnm .gt_from_md> :last-child { margin-bottom: 0; }
 #rqagrcufnm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rqagrcufnm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rqagrcufnm .gt_indent_1 { text-indent: 5px; }
 #rqagrcufnm .gt_indent_2 { text-indent: calc(5px * 2); }
 #rqagrcufnm .gt_indent_3 { text-indent: calc(5px * 3); }
 #rqagrcufnm .gt_indent_4 { text-indent: calc(5px * 4); }
 #rqagrcufnm .gt_indent_5 { text-indent: calc(5px * 5); }
 #rqagrcufnm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rqagrcufnm .gt_row_group_first td { border-top-width: 2px; }
 #rqagrcufnm .gt_row_group_first th { border-top-width: 2px; }
 #rqagrcufnm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rqagrcufnm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rqagrcufnm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rqagrcufnm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rqagrcufnm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rqagrcufnm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rqagrcufnm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rqagrcufnm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rqagrcufnm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rqagrcufnm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rqagrcufnm .gt_left { text-align: left; }
 #rqagrcufnm .gt_center { text-align: center; }
 #rqagrcufnm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rqagrcufnm .gt_font_normal { font-weight: normal; }
 #rqagrcufnm .gt_font_bold { font-weight: bold; }
 #rqagrcufnm .gt_font_italic { font-style: italic; }
 #rqagrcufnm .gt_super { font-size: 65%; }
 #rqagrcufnm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rqagrcufnm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rqagrcufnm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rqagrcufnm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rqagrcufnm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rqagrcufnm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#lidxqhxixy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lidxqhxixy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lidxqhxixy p { margin: 0; padding: 0; }
 #lidxqhxixy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lidxqhxixy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lidxqhxixy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lidxqhxixy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lidxqhxixy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lidxqhxixy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lidxqhxixy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lidxqhxixy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lidxqhxixy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lidxqhxixy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lidxqhxixy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lidxqhxixy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lidxqhxixy .gt_spanner_row { border-bottom-style: hidden; }
 #lidxqhxixy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lidxqhxixy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lidxqhxixy .gt_from_md> :first-child { margin-top: 0; }
 #lidxqhxixy .gt_from_md> :last-child { margin-bottom: 0; }
 #lidxqhxixy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lidxqhxixy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lidxqhxixy .gt_indent_1 { text-indent: 5px; }
 #lidxqhxixy .gt_indent_2 { text-indent: calc(5px * 2); }
 #lidxqhxixy .gt_indent_3 { text-indent: calc(5px * 3); }
 #lidxqhxixy .gt_indent_4 { text-indent: calc(5px * 4); }
 #lidxqhxixy .gt_indent_5 { text-indent: calc(5px * 5); }
 #lidxqhxixy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lidxqhxixy .gt_row_group_first td { border-top-width: 2px; }
 #lidxqhxixy .gt_row_group_first th { border-top-width: 2px; }
 #lidxqhxixy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lidxqhxixy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lidxqhxixy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lidxqhxixy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lidxqhxixy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lidxqhxixy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lidxqhxixy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lidxqhxixy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lidxqhxixy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lidxqhxixy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lidxqhxixy .gt_left { text-align: left; }
 #lidxqhxixy .gt_center { text-align: center; }
 #lidxqhxixy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lidxqhxixy .gt_font_normal { font-weight: normal; }
 #lidxqhxixy .gt_font_bold { font-weight: bold; }
 #lidxqhxixy .gt_font_italic { font-style: italic; }
 #lidxqhxixy .gt_super { font-size: 65%; }
 #lidxqhxixy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lidxqhxixy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lidxqhxixy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lidxqhxixy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lidxqhxixy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lidxqhxixy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#avkxibrkpe table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#avkxibrkpe thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#avkxibrkpe p { margin: 0; padding: 0; }
 #avkxibrkpe .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #avkxibrkpe .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #avkxibrkpe .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #avkxibrkpe .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #avkxibrkpe .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #avkxibrkpe .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #avkxibrkpe .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #avkxibrkpe .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #avkxibrkpe .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #avkxibrkpe .gt_column_spanner_outer:first-child { padding-left: 0; }
 #avkxibrkpe .gt_column_spanner_outer:last-child { padding-right: 0; }
 #avkxibrkpe .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #avkxibrkpe .gt_spanner_row { border-bottom-style: hidden; }
 #avkxibrkpe .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #avkxibrkpe .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #avkxibrkpe .gt_from_md> :first-child { margin-top: 0; }
 #avkxibrkpe .gt_from_md> :last-child { margin-bottom: 0; }
 #avkxibrkpe .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #avkxibrkpe .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #avkxibrkpe .gt_indent_1 { text-indent: 5px; }
 #avkxibrkpe .gt_indent_2 { text-indent: calc(5px * 2); }
 #avkxibrkpe .gt_indent_3 { text-indent: calc(5px * 3); }
 #avkxibrkpe .gt_indent_4 { text-indent: calc(5px * 4); }
 #avkxibrkpe .gt_indent_5 { text-indent: calc(5px * 5); }
 #avkxibrkpe .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #avkxibrkpe .gt_row_group_first td { border-top-width: 2px; }
 #avkxibrkpe .gt_row_group_first th { border-top-width: 2px; }
 #avkxibrkpe .gt_striped { color: #333333; background-color: #F4F4F4; }
 #avkxibrkpe .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #avkxibrkpe .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #avkxibrkpe .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #avkxibrkpe .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #avkxibrkpe .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #avkxibrkpe .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #avkxibrkpe .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #avkxibrkpe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #avkxibrkpe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #avkxibrkpe .gt_left { text-align: left; }
 #avkxibrkpe .gt_center { text-align: center; }
 #avkxibrkpe .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #avkxibrkpe .gt_font_normal { font-weight: normal; }
 #avkxibrkpe .gt_font_bold { font-weight: bold; }
 #avkxibrkpe .gt_font_italic { font-style: italic; }
 #avkxibrkpe .gt_super { font-size: 65%; }
 #avkxibrkpe .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #avkxibrkpe .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #avkxibrkpe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #avkxibrkpe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #avkxibrkpe .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #avkxibrkpe .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#nihdynhjse table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nihdynhjse thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nihdynhjse p { margin: 0; padding: 0; }
 #nihdynhjse .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nihdynhjse .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nihdynhjse .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nihdynhjse .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nihdynhjse .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nihdynhjse .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nihdynhjse .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nihdynhjse .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nihdynhjse .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nihdynhjse .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nihdynhjse .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nihdynhjse .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nihdynhjse .gt_spanner_row { border-bottom-style: hidden; }
 #nihdynhjse .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nihdynhjse .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nihdynhjse .gt_from_md> :first-child { margin-top: 0; }
 #nihdynhjse .gt_from_md> :last-child { margin-bottom: 0; }
 #nihdynhjse .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nihdynhjse .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nihdynhjse .gt_indent_1 { text-indent: 5px; }
 #nihdynhjse .gt_indent_2 { text-indent: calc(5px * 2); }
 #nihdynhjse .gt_indent_3 { text-indent: calc(5px * 3); }
 #nihdynhjse .gt_indent_4 { text-indent: calc(5px * 4); }
 #nihdynhjse .gt_indent_5 { text-indent: calc(5px * 5); }
 #nihdynhjse .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nihdynhjse .gt_row_group_first td { border-top-width: 2px; }
 #nihdynhjse .gt_row_group_first th { border-top-width: 2px; }
 #nihdynhjse .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nihdynhjse .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nihdynhjse .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nihdynhjse .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nihdynhjse .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nihdynhjse .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nihdynhjse .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nihdynhjse .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nihdynhjse .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nihdynhjse .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nihdynhjse .gt_left { text-align: left; }
 #nihdynhjse .gt_center { text-align: center; }
 #nihdynhjse .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nihdynhjse .gt_font_normal { font-weight: normal; }
 #nihdynhjse .gt_font_bold { font-weight: bold; }
 #nihdynhjse .gt_font_italic { font-style: italic; }
 #nihdynhjse .gt_super { font-size: 65%; }
 #nihdynhjse .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nihdynhjse .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nihdynhjse .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nihdynhjse .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nihdynhjse .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nihdynhjse .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ahzhagvcva table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ahzhagvcva thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ahzhagvcva p { margin: 0; padding: 0; }
 #ahzhagvcva .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ahzhagvcva .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ahzhagvcva .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ahzhagvcva .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ahzhagvcva .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ahzhagvcva .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ahzhagvcva .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ahzhagvcva .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ahzhagvcva .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ahzhagvcva .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ahzhagvcva .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ahzhagvcva .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ahzhagvcva .gt_spanner_row { border-bottom-style: hidden; }
 #ahzhagvcva .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ahzhagvcva .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ahzhagvcva .gt_from_md> :first-child { margin-top: 0; }
 #ahzhagvcva .gt_from_md> :last-child { margin-bottom: 0; }
 #ahzhagvcva .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ahzhagvcva .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ahzhagvcva .gt_indent_1 { text-indent: 5px; }
 #ahzhagvcva .gt_indent_2 { text-indent: calc(5px * 2); }
 #ahzhagvcva .gt_indent_3 { text-indent: calc(5px * 3); }
 #ahzhagvcva .gt_indent_4 { text-indent: calc(5px * 4); }
 #ahzhagvcva .gt_indent_5 { text-indent: calc(5px * 5); }
 #ahzhagvcva .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ahzhagvcva .gt_row_group_first td { border-top-width: 2px; }
 #ahzhagvcva .gt_row_group_first th { border-top-width: 2px; }
 #ahzhagvcva .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ahzhagvcva .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ahzhagvcva .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ahzhagvcva .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ahzhagvcva .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ahzhagvcva .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ahzhagvcva .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ahzhagvcva .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ahzhagvcva .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ahzhagvcva .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ahzhagvcva .gt_left { text-align: left; }
 #ahzhagvcva .gt_center { text-align: center; }
 #ahzhagvcva .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ahzhagvcva .gt_font_normal { font-weight: normal; }
 #ahzhagvcva .gt_font_bold { font-weight: bold; }
 #ahzhagvcva .gt_font_italic { font-style: italic; }
 #ahzhagvcva .gt_super { font-size: 65%; }
 #ahzhagvcva .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ahzhagvcva .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ahzhagvcva .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ahzhagvcva .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ahzhagvcva .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ahzhagvcva .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#cuuxwlqahj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cuuxwlqahj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cuuxwlqahj p { margin: 0; padding: 0; }
 #cuuxwlqahj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cuuxwlqahj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cuuxwlqahj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cuuxwlqahj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cuuxwlqahj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cuuxwlqahj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cuuxwlqahj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cuuxwlqahj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cuuxwlqahj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cuuxwlqahj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cuuxwlqahj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cuuxwlqahj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cuuxwlqahj .gt_spanner_row { border-bottom-style: hidden; }
 #cuuxwlqahj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cuuxwlqahj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cuuxwlqahj .gt_from_md> :first-child { margin-top: 0; }
 #cuuxwlqahj .gt_from_md> :last-child { margin-bottom: 0; }
 #cuuxwlqahj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cuuxwlqahj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cuuxwlqahj .gt_indent_1 { text-indent: 5px; }
 #cuuxwlqahj .gt_indent_2 { text-indent: calc(5px * 2); }
 #cuuxwlqahj .gt_indent_3 { text-indent: calc(5px * 3); }
 #cuuxwlqahj .gt_indent_4 { text-indent: calc(5px * 4); }
 #cuuxwlqahj .gt_indent_5 { text-indent: calc(5px * 5); }
 #cuuxwlqahj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cuuxwlqahj .gt_row_group_first td { border-top-width: 2px; }
 #cuuxwlqahj .gt_row_group_first th { border-top-width: 2px; }
 #cuuxwlqahj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cuuxwlqahj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cuuxwlqahj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cuuxwlqahj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cuuxwlqahj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cuuxwlqahj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cuuxwlqahj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cuuxwlqahj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cuuxwlqahj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cuuxwlqahj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cuuxwlqahj .gt_left { text-align: left; }
 #cuuxwlqahj .gt_center { text-align: center; }
 #cuuxwlqahj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cuuxwlqahj .gt_font_normal { font-weight: normal; }
 #cuuxwlqahj .gt_font_bold { font-weight: bold; }
 #cuuxwlqahj .gt_font_italic { font-style: italic; }
 #cuuxwlqahj .gt_super { font-size: 65%; }
 #cuuxwlqahj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cuuxwlqahj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cuuxwlqahj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cuuxwlqahj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cuuxwlqahj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cuuxwlqahj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pmtjlqzixa table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pmtjlqzixa thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pmtjlqzixa p { margin: 0; padding: 0; }
 #pmtjlqzixa .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pmtjlqzixa .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pmtjlqzixa .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pmtjlqzixa .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pmtjlqzixa .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pmtjlqzixa .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pmtjlqzixa .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pmtjlqzixa .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pmtjlqzixa .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pmtjlqzixa .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pmtjlqzixa .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pmtjlqzixa .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pmtjlqzixa .gt_spanner_row { border-bottom-style: hidden; }
 #pmtjlqzixa .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pmtjlqzixa .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pmtjlqzixa .gt_from_md> :first-child { margin-top: 0; }
 #pmtjlqzixa .gt_from_md> :last-child { margin-bottom: 0; }
 #pmtjlqzixa .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pmtjlqzixa .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pmtjlqzixa .gt_indent_1 { text-indent: 5px; }
 #pmtjlqzixa .gt_indent_2 { text-indent: calc(5px * 2); }
 #pmtjlqzixa .gt_indent_3 { text-indent: calc(5px * 3); }
 #pmtjlqzixa .gt_indent_4 { text-indent: calc(5px * 4); }
 #pmtjlqzixa .gt_indent_5 { text-indent: calc(5px * 5); }
 #pmtjlqzixa .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pmtjlqzixa .gt_row_group_first td { border-top-width: 2px; }
 #pmtjlqzixa .gt_row_group_first th { border-top-width: 2px; }
 #pmtjlqzixa .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pmtjlqzixa .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pmtjlqzixa .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pmtjlqzixa .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pmtjlqzixa .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pmtjlqzixa .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pmtjlqzixa .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pmtjlqzixa .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pmtjlqzixa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pmtjlqzixa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pmtjlqzixa .gt_left { text-align: left; }
 #pmtjlqzixa .gt_center { text-align: center; }
 #pmtjlqzixa .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pmtjlqzixa .gt_font_normal { font-weight: normal; }
 #pmtjlqzixa .gt_font_bold { font-weight: bold; }
 #pmtjlqzixa .gt_font_italic { font-style: italic; }
 #pmtjlqzixa .gt_super { font-size: 65%; }
 #pmtjlqzixa .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pmtjlqzixa .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pmtjlqzixa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pmtjlqzixa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pmtjlqzixa .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pmtjlqzixa .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#auknvcirwe table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#auknvcirwe thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#auknvcirwe p { margin: 0; padding: 0; }
 #auknvcirwe .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #auknvcirwe .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #auknvcirwe .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #auknvcirwe .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #auknvcirwe .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #auknvcirwe .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #auknvcirwe .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #auknvcirwe .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #auknvcirwe .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #auknvcirwe .gt_column_spanner_outer:first-child { padding-left: 0; }
 #auknvcirwe .gt_column_spanner_outer:last-child { padding-right: 0; }
 #auknvcirwe .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #auknvcirwe .gt_spanner_row { border-bottom-style: hidden; }
 #auknvcirwe .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #auknvcirwe .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #auknvcirwe .gt_from_md> :first-child { margin-top: 0; }
 #auknvcirwe .gt_from_md> :last-child { margin-bottom: 0; }
 #auknvcirwe .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #auknvcirwe .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #auknvcirwe .gt_indent_1 { text-indent: 5px; }
 #auknvcirwe .gt_indent_2 { text-indent: calc(5px * 2); }
 #auknvcirwe .gt_indent_3 { text-indent: calc(5px * 3); }
 #auknvcirwe .gt_indent_4 { text-indent: calc(5px * 4); }
 #auknvcirwe .gt_indent_5 { text-indent: calc(5px * 5); }
 #auknvcirwe .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #auknvcirwe .gt_row_group_first td { border-top-width: 2px; }
 #auknvcirwe .gt_row_group_first th { border-top-width: 2px; }
 #auknvcirwe .gt_striped { color: #333333; background-color: #F4F4F4; }
 #auknvcirwe .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #auknvcirwe .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #auknvcirwe .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #auknvcirwe .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #auknvcirwe .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #auknvcirwe .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #auknvcirwe .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #auknvcirwe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #auknvcirwe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #auknvcirwe .gt_left { text-align: left; }
 #auknvcirwe .gt_center { text-align: center; }
 #auknvcirwe .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #auknvcirwe .gt_font_normal { font-weight: normal; }
 #auknvcirwe .gt_font_bold { font-weight: bold; }
 #auknvcirwe .gt_font_italic { font-style: italic; }
 #auknvcirwe .gt_super { font-size: 65%; }
 #auknvcirwe .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #auknvcirwe .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #auknvcirwe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #auknvcirwe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #auknvcirwe .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #auknvcirwe .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
