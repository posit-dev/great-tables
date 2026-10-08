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
#eyulfdszlf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eyulfdszlf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eyulfdszlf p { margin: 0; padding: 0; }
 #eyulfdszlf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eyulfdszlf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eyulfdszlf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eyulfdszlf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eyulfdszlf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eyulfdszlf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eyulfdszlf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eyulfdszlf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eyulfdszlf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eyulfdszlf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eyulfdszlf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eyulfdszlf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eyulfdszlf .gt_spanner_row { border-bottom-style: hidden; }
 #eyulfdszlf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eyulfdszlf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eyulfdszlf .gt_from_md> :first-child { margin-top: 0; }
 #eyulfdszlf .gt_from_md> :last-child { margin-bottom: 0; }
 #eyulfdszlf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eyulfdszlf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eyulfdszlf .gt_indent_1 { text-indent: 5px; }
 #eyulfdszlf .gt_indent_2 { text-indent: calc(5px * 2); }
 #eyulfdszlf .gt_indent_3 { text-indent: calc(5px * 3); }
 #eyulfdszlf .gt_indent_4 { text-indent: calc(5px * 4); }
 #eyulfdszlf .gt_indent_5 { text-indent: calc(5px * 5); }
 #eyulfdszlf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eyulfdszlf .gt_row_group_first td { border-top-width: 2px; }
 #eyulfdszlf .gt_row_group_first th { border-top-width: 2px; }
 #eyulfdszlf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eyulfdszlf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eyulfdszlf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eyulfdszlf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eyulfdszlf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eyulfdszlf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eyulfdszlf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eyulfdszlf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eyulfdszlf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eyulfdszlf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eyulfdszlf .gt_left { text-align: left; }
 #eyulfdszlf .gt_center { text-align: center; }
 #eyulfdszlf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eyulfdszlf .gt_font_normal { font-weight: normal; }
 #eyulfdszlf .gt_font_bold { font-weight: bold; }
 #eyulfdszlf .gt_font_italic { font-style: italic; }
 #eyulfdszlf .gt_super { font-size: 65%; }
 #eyulfdszlf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eyulfdszlf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eyulfdszlf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eyulfdszlf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eyulfdszlf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eyulfdszlf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pfwtqdokfj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pfwtqdokfj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pfwtqdokfj p { margin: 0; padding: 0; }
 #pfwtqdokfj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pfwtqdokfj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pfwtqdokfj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pfwtqdokfj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pfwtqdokfj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pfwtqdokfj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pfwtqdokfj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pfwtqdokfj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pfwtqdokfj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pfwtqdokfj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pfwtqdokfj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pfwtqdokfj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pfwtqdokfj .gt_spanner_row { border-bottom-style: hidden; }
 #pfwtqdokfj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pfwtqdokfj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pfwtqdokfj .gt_from_md> :first-child { margin-top: 0; }
 #pfwtqdokfj .gt_from_md> :last-child { margin-bottom: 0; }
 #pfwtqdokfj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pfwtqdokfj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pfwtqdokfj .gt_indent_1 { text-indent: 5px; }
 #pfwtqdokfj .gt_indent_2 { text-indent: calc(5px * 2); }
 #pfwtqdokfj .gt_indent_3 { text-indent: calc(5px * 3); }
 #pfwtqdokfj .gt_indent_4 { text-indent: calc(5px * 4); }
 #pfwtqdokfj .gt_indent_5 { text-indent: calc(5px * 5); }
 #pfwtqdokfj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pfwtqdokfj .gt_row_group_first td { border-top-width: 2px; }
 #pfwtqdokfj .gt_row_group_first th { border-top-width: 2px; }
 #pfwtqdokfj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pfwtqdokfj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pfwtqdokfj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pfwtqdokfj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pfwtqdokfj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pfwtqdokfj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pfwtqdokfj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pfwtqdokfj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pfwtqdokfj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pfwtqdokfj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pfwtqdokfj .gt_left { text-align: left; }
 #pfwtqdokfj .gt_center { text-align: center; }
 #pfwtqdokfj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pfwtqdokfj .gt_font_normal { font-weight: normal; }
 #pfwtqdokfj .gt_font_bold { font-weight: bold; }
 #pfwtqdokfj .gt_font_italic { font-style: italic; }
 #pfwtqdokfj .gt_super { font-size: 65%; }
 #pfwtqdokfj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pfwtqdokfj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pfwtqdokfj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pfwtqdokfj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pfwtqdokfj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pfwtqdokfj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fnvhvzepnb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fnvhvzepnb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fnvhvzepnb p { margin: 0; padding: 0; }
 #fnvhvzepnb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fnvhvzepnb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fnvhvzepnb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fnvhvzepnb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fnvhvzepnb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fnvhvzepnb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fnvhvzepnb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fnvhvzepnb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fnvhvzepnb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fnvhvzepnb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fnvhvzepnb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fnvhvzepnb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fnvhvzepnb .gt_spanner_row { border-bottom-style: hidden; }
 #fnvhvzepnb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fnvhvzepnb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fnvhvzepnb .gt_from_md> :first-child { margin-top: 0; }
 #fnvhvzepnb .gt_from_md> :last-child { margin-bottom: 0; }
 #fnvhvzepnb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fnvhvzepnb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fnvhvzepnb .gt_indent_1 { text-indent: 5px; }
 #fnvhvzepnb .gt_indent_2 { text-indent: calc(5px * 2); }
 #fnvhvzepnb .gt_indent_3 { text-indent: calc(5px * 3); }
 #fnvhvzepnb .gt_indent_4 { text-indent: calc(5px * 4); }
 #fnvhvzepnb .gt_indent_5 { text-indent: calc(5px * 5); }
 #fnvhvzepnb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fnvhvzepnb .gt_row_group_first td { border-top-width: 2px; }
 #fnvhvzepnb .gt_row_group_first th { border-top-width: 2px; }
 #fnvhvzepnb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fnvhvzepnb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fnvhvzepnb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fnvhvzepnb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fnvhvzepnb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fnvhvzepnb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fnvhvzepnb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fnvhvzepnb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fnvhvzepnb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fnvhvzepnb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fnvhvzepnb .gt_left { text-align: left; }
 #fnvhvzepnb .gt_center { text-align: center; }
 #fnvhvzepnb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fnvhvzepnb .gt_font_normal { font-weight: normal; }
 #fnvhvzepnb .gt_font_bold { font-weight: bold; }
 #fnvhvzepnb .gt_font_italic { font-style: italic; }
 #fnvhvzepnb .gt_super { font-size: 65%; }
 #fnvhvzepnb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fnvhvzepnb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fnvhvzepnb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fnvhvzepnb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fnvhvzepnb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fnvhvzepnb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fbbmxvbobm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fbbmxvbobm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fbbmxvbobm p { margin: 0; padding: 0; }
 #fbbmxvbobm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fbbmxvbobm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fbbmxvbobm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fbbmxvbobm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fbbmxvbobm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fbbmxvbobm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fbbmxvbobm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fbbmxvbobm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fbbmxvbobm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fbbmxvbobm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fbbmxvbobm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fbbmxvbobm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fbbmxvbobm .gt_spanner_row { border-bottom-style: hidden; }
 #fbbmxvbobm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fbbmxvbobm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fbbmxvbobm .gt_from_md> :first-child { margin-top: 0; }
 #fbbmxvbobm .gt_from_md> :last-child { margin-bottom: 0; }
 #fbbmxvbobm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fbbmxvbobm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fbbmxvbobm .gt_indent_1 { text-indent: 5px; }
 #fbbmxvbobm .gt_indent_2 { text-indent: calc(5px * 2); }
 #fbbmxvbobm .gt_indent_3 { text-indent: calc(5px * 3); }
 #fbbmxvbobm .gt_indent_4 { text-indent: calc(5px * 4); }
 #fbbmxvbobm .gt_indent_5 { text-indent: calc(5px * 5); }
 #fbbmxvbobm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fbbmxvbobm .gt_row_group_first td { border-top-width: 2px; }
 #fbbmxvbobm .gt_row_group_first th { border-top-width: 2px; }
 #fbbmxvbobm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fbbmxvbobm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fbbmxvbobm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fbbmxvbobm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fbbmxvbobm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fbbmxvbobm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fbbmxvbobm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fbbmxvbobm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fbbmxvbobm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fbbmxvbobm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fbbmxvbobm .gt_left { text-align: left; }
 #fbbmxvbobm .gt_center { text-align: center; }
 #fbbmxvbobm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fbbmxvbobm .gt_font_normal { font-weight: normal; }
 #fbbmxvbobm .gt_font_bold { font-weight: bold; }
 #fbbmxvbobm .gt_font_italic { font-style: italic; }
 #fbbmxvbobm .gt_super { font-size: 65%; }
 #fbbmxvbobm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fbbmxvbobm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fbbmxvbobm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fbbmxvbobm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fbbmxvbobm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fbbmxvbobm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wkajlyqyiu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wkajlyqyiu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wkajlyqyiu p { margin: 0; padding: 0; }
 #wkajlyqyiu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wkajlyqyiu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wkajlyqyiu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wkajlyqyiu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wkajlyqyiu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wkajlyqyiu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wkajlyqyiu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wkajlyqyiu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wkajlyqyiu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wkajlyqyiu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wkajlyqyiu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wkajlyqyiu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wkajlyqyiu .gt_spanner_row { border-bottom-style: hidden; }
 #wkajlyqyiu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wkajlyqyiu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wkajlyqyiu .gt_from_md> :first-child { margin-top: 0; }
 #wkajlyqyiu .gt_from_md> :last-child { margin-bottom: 0; }
 #wkajlyqyiu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wkajlyqyiu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wkajlyqyiu .gt_indent_1 { text-indent: 5px; }
 #wkajlyqyiu .gt_indent_2 { text-indent: calc(5px * 2); }
 #wkajlyqyiu .gt_indent_3 { text-indent: calc(5px * 3); }
 #wkajlyqyiu .gt_indent_4 { text-indent: calc(5px * 4); }
 #wkajlyqyiu .gt_indent_5 { text-indent: calc(5px * 5); }
 #wkajlyqyiu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wkajlyqyiu .gt_row_group_first td { border-top-width: 2px; }
 #wkajlyqyiu .gt_row_group_first th { border-top-width: 2px; }
 #wkajlyqyiu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wkajlyqyiu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wkajlyqyiu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wkajlyqyiu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wkajlyqyiu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wkajlyqyiu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wkajlyqyiu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wkajlyqyiu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wkajlyqyiu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wkajlyqyiu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wkajlyqyiu .gt_left { text-align: left; }
 #wkajlyqyiu .gt_center { text-align: center; }
 #wkajlyqyiu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wkajlyqyiu .gt_font_normal { font-weight: normal; }
 #wkajlyqyiu .gt_font_bold { font-weight: bold; }
 #wkajlyqyiu .gt_font_italic { font-style: italic; }
 #wkajlyqyiu .gt_super { font-size: 65%; }
 #wkajlyqyiu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wkajlyqyiu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wkajlyqyiu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wkajlyqyiu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wkajlyqyiu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wkajlyqyiu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#muptqvedyv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#muptqvedyv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#muptqvedyv p { margin: 0; padding: 0; }
 #muptqvedyv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #muptqvedyv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #muptqvedyv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #muptqvedyv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #muptqvedyv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #muptqvedyv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muptqvedyv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #muptqvedyv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #muptqvedyv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #muptqvedyv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #muptqvedyv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #muptqvedyv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #muptqvedyv .gt_spanner_row { border-bottom-style: hidden; }
 #muptqvedyv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #muptqvedyv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #muptqvedyv .gt_from_md> :first-child { margin-top: 0; }
 #muptqvedyv .gt_from_md> :last-child { margin-bottom: 0; }
 #muptqvedyv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #muptqvedyv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #muptqvedyv .gt_indent_1 { text-indent: 5px; }
 #muptqvedyv .gt_indent_2 { text-indent: calc(5px * 2); }
 #muptqvedyv .gt_indent_3 { text-indent: calc(5px * 3); }
 #muptqvedyv .gt_indent_4 { text-indent: calc(5px * 4); }
 #muptqvedyv .gt_indent_5 { text-indent: calc(5px * 5); }
 #muptqvedyv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #muptqvedyv .gt_row_group_first td { border-top-width: 2px; }
 #muptqvedyv .gt_row_group_first th { border-top-width: 2px; }
 #muptqvedyv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #muptqvedyv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muptqvedyv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #muptqvedyv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #muptqvedyv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #muptqvedyv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #muptqvedyv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #muptqvedyv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #muptqvedyv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muptqvedyv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #muptqvedyv .gt_left { text-align: left; }
 #muptqvedyv .gt_center { text-align: center; }
 #muptqvedyv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #muptqvedyv .gt_font_normal { font-weight: normal; }
 #muptqvedyv .gt_font_bold { font-weight: bold; }
 #muptqvedyv .gt_font_italic { font-style: italic; }
 #muptqvedyv .gt_super { font-size: 65%; }
 #muptqvedyv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muptqvedyv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #muptqvedyv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #muptqvedyv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #muptqvedyv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #muptqvedyv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tpubshyeuq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tpubshyeuq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tpubshyeuq p { margin: 0; padding: 0; }
 #tpubshyeuq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tpubshyeuq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tpubshyeuq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tpubshyeuq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tpubshyeuq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tpubshyeuq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tpubshyeuq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tpubshyeuq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tpubshyeuq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tpubshyeuq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tpubshyeuq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tpubshyeuq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tpubshyeuq .gt_spanner_row { border-bottom-style: hidden; }
 #tpubshyeuq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tpubshyeuq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tpubshyeuq .gt_from_md> :first-child { margin-top: 0; }
 #tpubshyeuq .gt_from_md> :last-child { margin-bottom: 0; }
 #tpubshyeuq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tpubshyeuq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tpubshyeuq .gt_indent_1 { text-indent: 5px; }
 #tpubshyeuq .gt_indent_2 { text-indent: calc(5px * 2); }
 #tpubshyeuq .gt_indent_3 { text-indent: calc(5px * 3); }
 #tpubshyeuq .gt_indent_4 { text-indent: calc(5px * 4); }
 #tpubshyeuq .gt_indent_5 { text-indent: calc(5px * 5); }
 #tpubshyeuq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tpubshyeuq .gt_row_group_first td { border-top-width: 2px; }
 #tpubshyeuq .gt_row_group_first th { border-top-width: 2px; }
 #tpubshyeuq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tpubshyeuq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tpubshyeuq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tpubshyeuq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tpubshyeuq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tpubshyeuq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tpubshyeuq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tpubshyeuq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tpubshyeuq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tpubshyeuq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tpubshyeuq .gt_left { text-align: left; }
 #tpubshyeuq .gt_center { text-align: center; }
 #tpubshyeuq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tpubshyeuq .gt_font_normal { font-weight: normal; }
 #tpubshyeuq .gt_font_bold { font-weight: bold; }
 #tpubshyeuq .gt_font_italic { font-style: italic; }
 #tpubshyeuq .gt_super { font-size: 65%; }
 #tpubshyeuq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tpubshyeuq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tpubshyeuq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tpubshyeuq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tpubshyeuq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tpubshyeuq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xytqnbsfck table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xytqnbsfck thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xytqnbsfck p { margin: 0; padding: 0; }
 #xytqnbsfck .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xytqnbsfck .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xytqnbsfck .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xytqnbsfck .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xytqnbsfck .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xytqnbsfck .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xytqnbsfck .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xytqnbsfck .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xytqnbsfck .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xytqnbsfck .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xytqnbsfck .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xytqnbsfck .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xytqnbsfck .gt_spanner_row { border-bottom-style: hidden; }
 #xytqnbsfck .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xytqnbsfck .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xytqnbsfck .gt_from_md> :first-child { margin-top: 0; }
 #xytqnbsfck .gt_from_md> :last-child { margin-bottom: 0; }
 #xytqnbsfck .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xytqnbsfck .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xytqnbsfck .gt_indent_1 { text-indent: 5px; }
 #xytqnbsfck .gt_indent_2 { text-indent: calc(5px * 2); }
 #xytqnbsfck .gt_indent_3 { text-indent: calc(5px * 3); }
 #xytqnbsfck .gt_indent_4 { text-indent: calc(5px * 4); }
 #xytqnbsfck .gt_indent_5 { text-indent: calc(5px * 5); }
 #xytqnbsfck .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xytqnbsfck .gt_row_group_first td { border-top-width: 2px; }
 #xytqnbsfck .gt_row_group_first th { border-top-width: 2px; }
 #xytqnbsfck .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xytqnbsfck .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xytqnbsfck .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xytqnbsfck .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xytqnbsfck .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xytqnbsfck .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xytqnbsfck .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xytqnbsfck .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xytqnbsfck .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xytqnbsfck .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xytqnbsfck .gt_left { text-align: left; }
 #xytqnbsfck .gt_center { text-align: center; }
 #xytqnbsfck .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xytqnbsfck .gt_font_normal { font-weight: normal; }
 #xytqnbsfck .gt_font_bold { font-weight: bold; }
 #xytqnbsfck .gt_font_italic { font-style: italic; }
 #xytqnbsfck .gt_super { font-size: 65%; }
 #xytqnbsfck .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xytqnbsfck .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xytqnbsfck .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xytqnbsfck .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xytqnbsfck .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xytqnbsfck .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#izwstwklkb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#izwstwklkb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#izwstwklkb p { margin: 0; padding: 0; }
 #izwstwklkb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #izwstwklkb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #izwstwklkb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #izwstwklkb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #izwstwklkb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #izwstwklkb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #izwstwklkb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #izwstwklkb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #izwstwklkb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #izwstwklkb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #izwstwklkb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #izwstwklkb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #izwstwklkb .gt_spanner_row { border-bottom-style: hidden; }
 #izwstwklkb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #izwstwklkb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #izwstwklkb .gt_from_md> :first-child { margin-top: 0; }
 #izwstwklkb .gt_from_md> :last-child { margin-bottom: 0; }
 #izwstwklkb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #izwstwklkb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #izwstwklkb .gt_indent_1 { text-indent: 5px; }
 #izwstwklkb .gt_indent_2 { text-indent: calc(5px * 2); }
 #izwstwklkb .gt_indent_3 { text-indent: calc(5px * 3); }
 #izwstwklkb .gt_indent_4 { text-indent: calc(5px * 4); }
 #izwstwklkb .gt_indent_5 { text-indent: calc(5px * 5); }
 #izwstwklkb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #izwstwklkb .gt_row_group_first td { border-top-width: 2px; }
 #izwstwklkb .gt_row_group_first th { border-top-width: 2px; }
 #izwstwklkb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #izwstwklkb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #izwstwklkb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #izwstwklkb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #izwstwklkb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #izwstwklkb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #izwstwklkb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #izwstwklkb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #izwstwklkb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #izwstwklkb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #izwstwklkb .gt_left { text-align: left; }
 #izwstwklkb .gt_center { text-align: center; }
 #izwstwklkb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #izwstwklkb .gt_font_normal { font-weight: normal; }
 #izwstwklkb .gt_font_bold { font-weight: bold; }
 #izwstwklkb .gt_font_italic { font-style: italic; }
 #izwstwklkb .gt_super { font-size: 65%; }
 #izwstwklkb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #izwstwklkb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #izwstwklkb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #izwstwklkb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #izwstwklkb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #izwstwklkb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#sqsskzuznk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sqsskzuznk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sqsskzuznk p { margin: 0; padding: 0; }
 #sqsskzuznk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sqsskzuznk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sqsskzuznk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sqsskzuznk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sqsskzuznk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sqsskzuznk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sqsskzuznk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sqsskzuznk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sqsskzuznk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sqsskzuznk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sqsskzuznk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sqsskzuznk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sqsskzuznk .gt_spanner_row { border-bottom-style: hidden; }
 #sqsskzuznk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sqsskzuznk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sqsskzuznk .gt_from_md> :first-child { margin-top: 0; }
 #sqsskzuznk .gt_from_md> :last-child { margin-bottom: 0; }
 #sqsskzuznk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sqsskzuznk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sqsskzuznk .gt_indent_1 { text-indent: 5px; }
 #sqsskzuznk .gt_indent_2 { text-indent: calc(5px * 2); }
 #sqsskzuznk .gt_indent_3 { text-indent: calc(5px * 3); }
 #sqsskzuznk .gt_indent_4 { text-indent: calc(5px * 4); }
 #sqsskzuznk .gt_indent_5 { text-indent: calc(5px * 5); }
 #sqsskzuznk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sqsskzuznk .gt_row_group_first td { border-top-width: 2px; }
 #sqsskzuznk .gt_row_group_first th { border-top-width: 2px; }
 #sqsskzuznk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sqsskzuznk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sqsskzuznk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sqsskzuznk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sqsskzuznk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sqsskzuznk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sqsskzuznk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sqsskzuznk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sqsskzuznk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sqsskzuznk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sqsskzuznk .gt_left { text-align: left; }
 #sqsskzuznk .gt_center { text-align: center; }
 #sqsskzuznk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sqsskzuznk .gt_font_normal { font-weight: normal; }
 #sqsskzuznk .gt_font_bold { font-weight: bold; }
 #sqsskzuznk .gt_font_italic { font-style: italic; }
 #sqsskzuznk .gt_super { font-size: 65%; }
 #sqsskzuznk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sqsskzuznk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sqsskzuznk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sqsskzuznk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sqsskzuznk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sqsskzuznk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qrvqrikoce table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qrvqrikoce thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qrvqrikoce p { margin: 0; padding: 0; }
 #qrvqrikoce .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qrvqrikoce .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qrvqrikoce .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qrvqrikoce .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qrvqrikoce .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qrvqrikoce .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qrvqrikoce .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qrvqrikoce .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qrvqrikoce .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qrvqrikoce .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qrvqrikoce .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qrvqrikoce .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qrvqrikoce .gt_spanner_row { border-bottom-style: hidden; }
 #qrvqrikoce .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qrvqrikoce .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qrvqrikoce .gt_from_md> :first-child { margin-top: 0; }
 #qrvqrikoce .gt_from_md> :last-child { margin-bottom: 0; }
 #qrvqrikoce .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qrvqrikoce .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qrvqrikoce .gt_indent_1 { text-indent: 5px; }
 #qrvqrikoce .gt_indent_2 { text-indent: calc(5px * 2); }
 #qrvqrikoce .gt_indent_3 { text-indent: calc(5px * 3); }
 #qrvqrikoce .gt_indent_4 { text-indent: calc(5px * 4); }
 #qrvqrikoce .gt_indent_5 { text-indent: calc(5px * 5); }
 #qrvqrikoce .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qrvqrikoce .gt_row_group_first td { border-top-width: 2px; }
 #qrvqrikoce .gt_row_group_first th { border-top-width: 2px; }
 #qrvqrikoce .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qrvqrikoce .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qrvqrikoce .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qrvqrikoce .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qrvqrikoce .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qrvqrikoce .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qrvqrikoce .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qrvqrikoce .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qrvqrikoce .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qrvqrikoce .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qrvqrikoce .gt_left { text-align: left; }
 #qrvqrikoce .gt_center { text-align: center; }
 #qrvqrikoce .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qrvqrikoce .gt_font_normal { font-weight: normal; }
 #qrvqrikoce .gt_font_bold { font-weight: bold; }
 #qrvqrikoce .gt_font_italic { font-style: italic; }
 #qrvqrikoce .gt_super { font-size: 65%; }
 #qrvqrikoce .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qrvqrikoce .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qrvqrikoce .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qrvqrikoce .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qrvqrikoce .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qrvqrikoce .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#cdqyigykoh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cdqyigykoh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cdqyigykoh p { margin: 0; padding: 0; }
 #cdqyigykoh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cdqyigykoh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cdqyigykoh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cdqyigykoh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cdqyigykoh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cdqyigykoh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cdqyigykoh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cdqyigykoh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cdqyigykoh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cdqyigykoh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cdqyigykoh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cdqyigykoh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cdqyigykoh .gt_spanner_row { border-bottom-style: hidden; }
 #cdqyigykoh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cdqyigykoh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cdqyigykoh .gt_from_md> :first-child { margin-top: 0; }
 #cdqyigykoh .gt_from_md> :last-child { margin-bottom: 0; }
 #cdqyigykoh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cdqyigykoh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cdqyigykoh .gt_indent_1 { text-indent: 5px; }
 #cdqyigykoh .gt_indent_2 { text-indent: calc(5px * 2); }
 #cdqyigykoh .gt_indent_3 { text-indent: calc(5px * 3); }
 #cdqyigykoh .gt_indent_4 { text-indent: calc(5px * 4); }
 #cdqyigykoh .gt_indent_5 { text-indent: calc(5px * 5); }
 #cdqyigykoh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cdqyigykoh .gt_row_group_first td { border-top-width: 2px; }
 #cdqyigykoh .gt_row_group_first th { border-top-width: 2px; }
 #cdqyigykoh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cdqyigykoh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cdqyigykoh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cdqyigykoh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cdqyigykoh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cdqyigykoh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cdqyigykoh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cdqyigykoh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cdqyigykoh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cdqyigykoh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cdqyigykoh .gt_left { text-align: left; }
 #cdqyigykoh .gt_center { text-align: center; }
 #cdqyigykoh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cdqyigykoh .gt_font_normal { font-weight: normal; }
 #cdqyigykoh .gt_font_bold { font-weight: bold; }
 #cdqyigykoh .gt_font_italic { font-style: italic; }
 #cdqyigykoh .gt_super { font-size: 65%; }
 #cdqyigykoh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cdqyigykoh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cdqyigykoh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cdqyigykoh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cdqyigykoh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cdqyigykoh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
