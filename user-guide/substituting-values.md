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
#cjkzukwouc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cjkzukwouc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cjkzukwouc p { margin: 0; padding: 0; }
 #cjkzukwouc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cjkzukwouc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cjkzukwouc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cjkzukwouc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cjkzukwouc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cjkzukwouc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cjkzukwouc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cjkzukwouc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cjkzukwouc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cjkzukwouc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cjkzukwouc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cjkzukwouc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cjkzukwouc .gt_spanner_row { border-bottom-style: hidden; }
 #cjkzukwouc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cjkzukwouc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cjkzukwouc .gt_from_md> :first-child { margin-top: 0; }
 #cjkzukwouc .gt_from_md> :last-child { margin-bottom: 0; }
 #cjkzukwouc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cjkzukwouc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cjkzukwouc .gt_indent_1 { text-indent: 5px; }
 #cjkzukwouc .gt_indent_2 { text-indent: calc(5px * 2); }
 #cjkzukwouc .gt_indent_3 { text-indent: calc(5px * 3); }
 #cjkzukwouc .gt_indent_4 { text-indent: calc(5px * 4); }
 #cjkzukwouc .gt_indent_5 { text-indent: calc(5px * 5); }
 #cjkzukwouc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cjkzukwouc .gt_row_group_first td { border-top-width: 2px; }
 #cjkzukwouc .gt_row_group_first th { border-top-width: 2px; }
 #cjkzukwouc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cjkzukwouc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cjkzukwouc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cjkzukwouc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cjkzukwouc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cjkzukwouc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cjkzukwouc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cjkzukwouc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cjkzukwouc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cjkzukwouc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cjkzukwouc .gt_left { text-align: left; }
 #cjkzukwouc .gt_center { text-align: center; }
 #cjkzukwouc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cjkzukwouc .gt_font_normal { font-weight: normal; }
 #cjkzukwouc .gt_font_bold { font-weight: bold; }
 #cjkzukwouc .gt_font_italic { font-style: italic; }
 #cjkzukwouc .gt_super { font-size: 65%; }
 #cjkzukwouc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cjkzukwouc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cjkzukwouc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cjkzukwouc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cjkzukwouc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cjkzukwouc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#mzntlszbbb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mzntlszbbb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mzntlszbbb p { margin: 0; padding: 0; }
 #mzntlszbbb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mzntlszbbb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mzntlszbbb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mzntlszbbb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mzntlszbbb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mzntlszbbb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mzntlszbbb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mzntlszbbb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mzntlszbbb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mzntlszbbb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mzntlszbbb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mzntlszbbb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mzntlszbbb .gt_spanner_row { border-bottom-style: hidden; }
 #mzntlszbbb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mzntlszbbb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mzntlszbbb .gt_from_md> :first-child { margin-top: 0; }
 #mzntlszbbb .gt_from_md> :last-child { margin-bottom: 0; }
 #mzntlszbbb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mzntlszbbb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mzntlszbbb .gt_indent_1 { text-indent: 5px; }
 #mzntlszbbb .gt_indent_2 { text-indent: calc(5px * 2); }
 #mzntlszbbb .gt_indent_3 { text-indent: calc(5px * 3); }
 #mzntlszbbb .gt_indent_4 { text-indent: calc(5px * 4); }
 #mzntlszbbb .gt_indent_5 { text-indent: calc(5px * 5); }
 #mzntlszbbb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mzntlszbbb .gt_row_group_first td { border-top-width: 2px; }
 #mzntlszbbb .gt_row_group_first th { border-top-width: 2px; }
 #mzntlszbbb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mzntlszbbb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mzntlszbbb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mzntlszbbb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mzntlszbbb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mzntlszbbb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mzntlszbbb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mzntlszbbb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mzntlszbbb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mzntlszbbb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mzntlszbbb .gt_left { text-align: left; }
 #mzntlszbbb .gt_center { text-align: center; }
 #mzntlszbbb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mzntlszbbb .gt_font_normal { font-weight: normal; }
 #mzntlszbbb .gt_font_bold { font-weight: bold; }
 #mzntlszbbb .gt_font_italic { font-style: italic; }
 #mzntlszbbb .gt_super { font-size: 65%; }
 #mzntlszbbb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mzntlszbbb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mzntlszbbb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mzntlszbbb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mzntlszbbb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mzntlszbbb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bytzdlekvj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bytzdlekvj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bytzdlekvj p { margin: 0; padding: 0; }
 #bytzdlekvj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bytzdlekvj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bytzdlekvj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bytzdlekvj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bytzdlekvj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bytzdlekvj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bytzdlekvj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bytzdlekvj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bytzdlekvj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bytzdlekvj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bytzdlekvj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bytzdlekvj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bytzdlekvj .gt_spanner_row { border-bottom-style: hidden; }
 #bytzdlekvj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bytzdlekvj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bytzdlekvj .gt_from_md> :first-child { margin-top: 0; }
 #bytzdlekvj .gt_from_md> :last-child { margin-bottom: 0; }
 #bytzdlekvj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bytzdlekvj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bytzdlekvj .gt_indent_1 { text-indent: 5px; }
 #bytzdlekvj .gt_indent_2 { text-indent: calc(5px * 2); }
 #bytzdlekvj .gt_indent_3 { text-indent: calc(5px * 3); }
 #bytzdlekvj .gt_indent_4 { text-indent: calc(5px * 4); }
 #bytzdlekvj .gt_indent_5 { text-indent: calc(5px * 5); }
 #bytzdlekvj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bytzdlekvj .gt_row_group_first td { border-top-width: 2px; }
 #bytzdlekvj .gt_row_group_first th { border-top-width: 2px; }
 #bytzdlekvj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bytzdlekvj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bytzdlekvj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bytzdlekvj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bytzdlekvj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bytzdlekvj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bytzdlekvj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bytzdlekvj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bytzdlekvj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bytzdlekvj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bytzdlekvj .gt_left { text-align: left; }
 #bytzdlekvj .gt_center { text-align: center; }
 #bytzdlekvj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bytzdlekvj .gt_font_normal { font-weight: normal; }
 #bytzdlekvj .gt_font_bold { font-weight: bold; }
 #bytzdlekvj .gt_font_italic { font-style: italic; }
 #bytzdlekvj .gt_super { font-size: 65%; }
 #bytzdlekvj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bytzdlekvj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bytzdlekvj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bytzdlekvj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bytzdlekvj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bytzdlekvj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vwmdeyiezi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vwmdeyiezi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vwmdeyiezi p { margin: 0; padding: 0; }
 #vwmdeyiezi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vwmdeyiezi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vwmdeyiezi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vwmdeyiezi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vwmdeyiezi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vwmdeyiezi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vwmdeyiezi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vwmdeyiezi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vwmdeyiezi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vwmdeyiezi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vwmdeyiezi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vwmdeyiezi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vwmdeyiezi .gt_spanner_row { border-bottom-style: hidden; }
 #vwmdeyiezi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vwmdeyiezi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vwmdeyiezi .gt_from_md> :first-child { margin-top: 0; }
 #vwmdeyiezi .gt_from_md> :last-child { margin-bottom: 0; }
 #vwmdeyiezi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vwmdeyiezi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vwmdeyiezi .gt_indent_1 { text-indent: 5px; }
 #vwmdeyiezi .gt_indent_2 { text-indent: calc(5px * 2); }
 #vwmdeyiezi .gt_indent_3 { text-indent: calc(5px * 3); }
 #vwmdeyiezi .gt_indent_4 { text-indent: calc(5px * 4); }
 #vwmdeyiezi .gt_indent_5 { text-indent: calc(5px * 5); }
 #vwmdeyiezi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vwmdeyiezi .gt_row_group_first td { border-top-width: 2px; }
 #vwmdeyiezi .gt_row_group_first th { border-top-width: 2px; }
 #vwmdeyiezi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vwmdeyiezi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vwmdeyiezi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vwmdeyiezi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vwmdeyiezi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vwmdeyiezi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vwmdeyiezi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vwmdeyiezi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vwmdeyiezi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vwmdeyiezi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vwmdeyiezi .gt_left { text-align: left; }
 #vwmdeyiezi .gt_center { text-align: center; }
 #vwmdeyiezi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vwmdeyiezi .gt_font_normal { font-weight: normal; }
 #vwmdeyiezi .gt_font_bold { font-weight: bold; }
 #vwmdeyiezi .gt_font_italic { font-style: italic; }
 #vwmdeyiezi .gt_super { font-size: 65%; }
 #vwmdeyiezi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vwmdeyiezi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vwmdeyiezi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vwmdeyiezi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vwmdeyiezi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vwmdeyiezi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wfeafihsdj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wfeafihsdj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wfeafihsdj p { margin: 0; padding: 0; }
 #wfeafihsdj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wfeafihsdj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wfeafihsdj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wfeafihsdj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wfeafihsdj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wfeafihsdj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wfeafihsdj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wfeafihsdj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wfeafihsdj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wfeafihsdj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wfeafihsdj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wfeafihsdj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wfeafihsdj .gt_spanner_row { border-bottom-style: hidden; }
 #wfeafihsdj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wfeafihsdj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wfeafihsdj .gt_from_md> :first-child { margin-top: 0; }
 #wfeafihsdj .gt_from_md> :last-child { margin-bottom: 0; }
 #wfeafihsdj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wfeafihsdj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wfeafihsdj .gt_indent_1 { text-indent: 5px; }
 #wfeafihsdj .gt_indent_2 { text-indent: calc(5px * 2); }
 #wfeafihsdj .gt_indent_3 { text-indent: calc(5px * 3); }
 #wfeafihsdj .gt_indent_4 { text-indent: calc(5px * 4); }
 #wfeafihsdj .gt_indent_5 { text-indent: calc(5px * 5); }
 #wfeafihsdj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wfeafihsdj .gt_row_group_first td { border-top-width: 2px; }
 #wfeafihsdj .gt_row_group_first th { border-top-width: 2px; }
 #wfeafihsdj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wfeafihsdj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wfeafihsdj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wfeafihsdj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wfeafihsdj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wfeafihsdj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wfeafihsdj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wfeafihsdj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wfeafihsdj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wfeafihsdj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wfeafihsdj .gt_left { text-align: left; }
 #wfeafihsdj .gt_center { text-align: center; }
 #wfeafihsdj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wfeafihsdj .gt_font_normal { font-weight: normal; }
 #wfeafihsdj .gt_font_bold { font-weight: bold; }
 #wfeafihsdj .gt_font_italic { font-style: italic; }
 #wfeafihsdj .gt_super { font-size: 65%; }
 #wfeafihsdj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wfeafihsdj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wfeafihsdj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wfeafihsdj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wfeafihsdj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wfeafihsdj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#retxxpxaez table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#retxxpxaez thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#retxxpxaez p { margin: 0; padding: 0; }
 #retxxpxaez .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #retxxpxaez .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #retxxpxaez .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #retxxpxaez .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #retxxpxaez .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #retxxpxaez .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #retxxpxaez .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #retxxpxaez .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #retxxpxaez .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #retxxpxaez .gt_column_spanner_outer:first-child { padding-left: 0; }
 #retxxpxaez .gt_column_spanner_outer:last-child { padding-right: 0; }
 #retxxpxaez .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #retxxpxaez .gt_spanner_row { border-bottom-style: hidden; }
 #retxxpxaez .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #retxxpxaez .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #retxxpxaez .gt_from_md> :first-child { margin-top: 0; }
 #retxxpxaez .gt_from_md> :last-child { margin-bottom: 0; }
 #retxxpxaez .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #retxxpxaez .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #retxxpxaez .gt_indent_1 { text-indent: 5px; }
 #retxxpxaez .gt_indent_2 { text-indent: calc(5px * 2); }
 #retxxpxaez .gt_indent_3 { text-indent: calc(5px * 3); }
 #retxxpxaez .gt_indent_4 { text-indent: calc(5px * 4); }
 #retxxpxaez .gt_indent_5 { text-indent: calc(5px * 5); }
 #retxxpxaez .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #retxxpxaez .gt_row_group_first td { border-top-width: 2px; }
 #retxxpxaez .gt_row_group_first th { border-top-width: 2px; }
 #retxxpxaez .gt_striped { color: #333333; background-color: #F4F4F4; }
 #retxxpxaez .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #retxxpxaez .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #retxxpxaez .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #retxxpxaez .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #retxxpxaez .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #retxxpxaez .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #retxxpxaez .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #retxxpxaez .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #retxxpxaez .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #retxxpxaez .gt_left { text-align: left; }
 #retxxpxaez .gt_center { text-align: center; }
 #retxxpxaez .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #retxxpxaez .gt_font_normal { font-weight: normal; }
 #retxxpxaez .gt_font_bold { font-weight: bold; }
 #retxxpxaez .gt_font_italic { font-style: italic; }
 #retxxpxaez .gt_super { font-size: 65%; }
 #retxxpxaez .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #retxxpxaez .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #retxxpxaez .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #retxxpxaez .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #retxxpxaez .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #retxxpxaez .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tgeikbvxmx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tgeikbvxmx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tgeikbvxmx p { margin: 0; padding: 0; }
 #tgeikbvxmx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tgeikbvxmx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tgeikbvxmx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tgeikbvxmx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tgeikbvxmx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tgeikbvxmx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tgeikbvxmx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tgeikbvxmx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tgeikbvxmx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tgeikbvxmx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tgeikbvxmx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tgeikbvxmx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tgeikbvxmx .gt_spanner_row { border-bottom-style: hidden; }
 #tgeikbvxmx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tgeikbvxmx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tgeikbvxmx .gt_from_md> :first-child { margin-top: 0; }
 #tgeikbvxmx .gt_from_md> :last-child { margin-bottom: 0; }
 #tgeikbvxmx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tgeikbvxmx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tgeikbvxmx .gt_indent_1 { text-indent: 5px; }
 #tgeikbvxmx .gt_indent_2 { text-indent: calc(5px * 2); }
 #tgeikbvxmx .gt_indent_3 { text-indent: calc(5px * 3); }
 #tgeikbvxmx .gt_indent_4 { text-indent: calc(5px * 4); }
 #tgeikbvxmx .gt_indent_5 { text-indent: calc(5px * 5); }
 #tgeikbvxmx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tgeikbvxmx .gt_row_group_first td { border-top-width: 2px; }
 #tgeikbvxmx .gt_row_group_first th { border-top-width: 2px; }
 #tgeikbvxmx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tgeikbvxmx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tgeikbvxmx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tgeikbvxmx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tgeikbvxmx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tgeikbvxmx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tgeikbvxmx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tgeikbvxmx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tgeikbvxmx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tgeikbvxmx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tgeikbvxmx .gt_left { text-align: left; }
 #tgeikbvxmx .gt_center { text-align: center; }
 #tgeikbvxmx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tgeikbvxmx .gt_font_normal { font-weight: normal; }
 #tgeikbvxmx .gt_font_bold { font-weight: bold; }
 #tgeikbvxmx .gt_font_italic { font-style: italic; }
 #tgeikbvxmx .gt_super { font-size: 65%; }
 #tgeikbvxmx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tgeikbvxmx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tgeikbvxmx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tgeikbvxmx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tgeikbvxmx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tgeikbvxmx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zqmmmmhgjs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zqmmmmhgjs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zqmmmmhgjs p { margin: 0; padding: 0; }
 #zqmmmmhgjs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zqmmmmhgjs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zqmmmmhgjs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zqmmmmhgjs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zqmmmmhgjs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zqmmmmhgjs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zqmmmmhgjs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zqmmmmhgjs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zqmmmmhgjs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zqmmmmhgjs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zqmmmmhgjs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zqmmmmhgjs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zqmmmmhgjs .gt_spanner_row { border-bottom-style: hidden; }
 #zqmmmmhgjs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zqmmmmhgjs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zqmmmmhgjs .gt_from_md> :first-child { margin-top: 0; }
 #zqmmmmhgjs .gt_from_md> :last-child { margin-bottom: 0; }
 #zqmmmmhgjs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zqmmmmhgjs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zqmmmmhgjs .gt_indent_1 { text-indent: 5px; }
 #zqmmmmhgjs .gt_indent_2 { text-indent: calc(5px * 2); }
 #zqmmmmhgjs .gt_indent_3 { text-indent: calc(5px * 3); }
 #zqmmmmhgjs .gt_indent_4 { text-indent: calc(5px * 4); }
 #zqmmmmhgjs .gt_indent_5 { text-indent: calc(5px * 5); }
 #zqmmmmhgjs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zqmmmmhgjs .gt_row_group_first td { border-top-width: 2px; }
 #zqmmmmhgjs .gt_row_group_first th { border-top-width: 2px; }
 #zqmmmmhgjs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zqmmmmhgjs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zqmmmmhgjs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zqmmmmhgjs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zqmmmmhgjs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zqmmmmhgjs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zqmmmmhgjs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zqmmmmhgjs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zqmmmmhgjs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zqmmmmhgjs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zqmmmmhgjs .gt_left { text-align: left; }
 #zqmmmmhgjs .gt_center { text-align: center; }
 #zqmmmmhgjs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zqmmmmhgjs .gt_font_normal { font-weight: normal; }
 #zqmmmmhgjs .gt_font_bold { font-weight: bold; }
 #zqmmmmhgjs .gt_font_italic { font-style: italic; }
 #zqmmmmhgjs .gt_super { font-size: 65%; }
 #zqmmmmhgjs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zqmmmmhgjs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zqmmmmhgjs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zqmmmmhgjs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zqmmmmhgjs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zqmmmmhgjs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#illsoaatrc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#illsoaatrc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#illsoaatrc p { margin: 0; padding: 0; }
 #illsoaatrc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #illsoaatrc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #illsoaatrc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #illsoaatrc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #illsoaatrc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #illsoaatrc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #illsoaatrc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #illsoaatrc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #illsoaatrc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #illsoaatrc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #illsoaatrc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #illsoaatrc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #illsoaatrc .gt_spanner_row { border-bottom-style: hidden; }
 #illsoaatrc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #illsoaatrc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #illsoaatrc .gt_from_md> :first-child { margin-top: 0; }
 #illsoaatrc .gt_from_md> :last-child { margin-bottom: 0; }
 #illsoaatrc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #illsoaatrc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #illsoaatrc .gt_indent_1 { text-indent: 5px; }
 #illsoaatrc .gt_indent_2 { text-indent: calc(5px * 2); }
 #illsoaatrc .gt_indent_3 { text-indent: calc(5px * 3); }
 #illsoaatrc .gt_indent_4 { text-indent: calc(5px * 4); }
 #illsoaatrc .gt_indent_5 { text-indent: calc(5px * 5); }
 #illsoaatrc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #illsoaatrc .gt_row_group_first td { border-top-width: 2px; }
 #illsoaatrc .gt_row_group_first th { border-top-width: 2px; }
 #illsoaatrc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #illsoaatrc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #illsoaatrc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #illsoaatrc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #illsoaatrc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #illsoaatrc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #illsoaatrc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #illsoaatrc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #illsoaatrc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #illsoaatrc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #illsoaatrc .gt_left { text-align: left; }
 #illsoaatrc .gt_center { text-align: center; }
 #illsoaatrc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #illsoaatrc .gt_font_normal { font-weight: normal; }
 #illsoaatrc .gt_font_bold { font-weight: bold; }
 #illsoaatrc .gt_font_italic { font-style: italic; }
 #illsoaatrc .gt_super { font-size: 65%; }
 #illsoaatrc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #illsoaatrc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #illsoaatrc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #illsoaatrc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #illsoaatrc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #illsoaatrc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#nhssswgmcc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nhssswgmcc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nhssswgmcc p { margin: 0; padding: 0; }
 #nhssswgmcc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nhssswgmcc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nhssswgmcc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nhssswgmcc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nhssswgmcc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nhssswgmcc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nhssswgmcc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nhssswgmcc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nhssswgmcc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nhssswgmcc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nhssswgmcc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nhssswgmcc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nhssswgmcc .gt_spanner_row { border-bottom-style: hidden; }
 #nhssswgmcc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nhssswgmcc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nhssswgmcc .gt_from_md> :first-child { margin-top: 0; }
 #nhssswgmcc .gt_from_md> :last-child { margin-bottom: 0; }
 #nhssswgmcc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nhssswgmcc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nhssswgmcc .gt_indent_1 { text-indent: 5px; }
 #nhssswgmcc .gt_indent_2 { text-indent: calc(5px * 2); }
 #nhssswgmcc .gt_indent_3 { text-indent: calc(5px * 3); }
 #nhssswgmcc .gt_indent_4 { text-indent: calc(5px * 4); }
 #nhssswgmcc .gt_indent_5 { text-indent: calc(5px * 5); }
 #nhssswgmcc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nhssswgmcc .gt_row_group_first td { border-top-width: 2px; }
 #nhssswgmcc .gt_row_group_first th { border-top-width: 2px; }
 #nhssswgmcc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nhssswgmcc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nhssswgmcc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nhssswgmcc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nhssswgmcc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nhssswgmcc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nhssswgmcc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nhssswgmcc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nhssswgmcc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nhssswgmcc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nhssswgmcc .gt_left { text-align: left; }
 #nhssswgmcc .gt_center { text-align: center; }
 #nhssswgmcc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nhssswgmcc .gt_font_normal { font-weight: normal; }
 #nhssswgmcc .gt_font_bold { font-weight: bold; }
 #nhssswgmcc .gt_font_italic { font-style: italic; }
 #nhssswgmcc .gt_super { font-size: 65%; }
 #nhssswgmcc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nhssswgmcc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nhssswgmcc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nhssswgmcc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nhssswgmcc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nhssswgmcc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ajghdcicxe table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ajghdcicxe thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ajghdcicxe p { margin: 0; padding: 0; }
 #ajghdcicxe .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ajghdcicxe .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ajghdcicxe .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ajghdcicxe .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ajghdcicxe .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ajghdcicxe .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ajghdcicxe .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ajghdcicxe .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ajghdcicxe .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ajghdcicxe .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ajghdcicxe .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ajghdcicxe .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ajghdcicxe .gt_spanner_row { border-bottom-style: hidden; }
 #ajghdcicxe .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ajghdcicxe .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ajghdcicxe .gt_from_md> :first-child { margin-top: 0; }
 #ajghdcicxe .gt_from_md> :last-child { margin-bottom: 0; }
 #ajghdcicxe .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ajghdcicxe .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ajghdcicxe .gt_indent_1 { text-indent: 5px; }
 #ajghdcicxe .gt_indent_2 { text-indent: calc(5px * 2); }
 #ajghdcicxe .gt_indent_3 { text-indent: calc(5px * 3); }
 #ajghdcicxe .gt_indent_4 { text-indent: calc(5px * 4); }
 #ajghdcicxe .gt_indent_5 { text-indent: calc(5px * 5); }
 #ajghdcicxe .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ajghdcicxe .gt_row_group_first td { border-top-width: 2px; }
 #ajghdcicxe .gt_row_group_first th { border-top-width: 2px; }
 #ajghdcicxe .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ajghdcicxe .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ajghdcicxe .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ajghdcicxe .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ajghdcicxe .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ajghdcicxe .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ajghdcicxe .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ajghdcicxe .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ajghdcicxe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ajghdcicxe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ajghdcicxe .gt_left { text-align: left; }
 #ajghdcicxe .gt_center { text-align: center; }
 #ajghdcicxe .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ajghdcicxe .gt_font_normal { font-weight: normal; }
 #ajghdcicxe .gt_font_bold { font-weight: bold; }
 #ajghdcicxe .gt_font_italic { font-style: italic; }
 #ajghdcicxe .gt_super { font-size: 65%; }
 #ajghdcicxe .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ajghdcicxe .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ajghdcicxe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ajghdcicxe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ajghdcicxe .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ajghdcicxe .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#epqmcoivbp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#epqmcoivbp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#epqmcoivbp p { margin: 0; padding: 0; }
 #epqmcoivbp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #epqmcoivbp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #epqmcoivbp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #epqmcoivbp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #epqmcoivbp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #epqmcoivbp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #epqmcoivbp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #epqmcoivbp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #epqmcoivbp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #epqmcoivbp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #epqmcoivbp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #epqmcoivbp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #epqmcoivbp .gt_spanner_row { border-bottom-style: hidden; }
 #epqmcoivbp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #epqmcoivbp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #epqmcoivbp .gt_from_md> :first-child { margin-top: 0; }
 #epqmcoivbp .gt_from_md> :last-child { margin-bottom: 0; }
 #epqmcoivbp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #epqmcoivbp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #epqmcoivbp .gt_indent_1 { text-indent: 5px; }
 #epqmcoivbp .gt_indent_2 { text-indent: calc(5px * 2); }
 #epqmcoivbp .gt_indent_3 { text-indent: calc(5px * 3); }
 #epqmcoivbp .gt_indent_4 { text-indent: calc(5px * 4); }
 #epqmcoivbp .gt_indent_5 { text-indent: calc(5px * 5); }
 #epqmcoivbp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #epqmcoivbp .gt_row_group_first td { border-top-width: 2px; }
 #epqmcoivbp .gt_row_group_first th { border-top-width: 2px; }
 #epqmcoivbp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #epqmcoivbp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #epqmcoivbp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #epqmcoivbp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #epqmcoivbp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #epqmcoivbp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #epqmcoivbp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #epqmcoivbp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #epqmcoivbp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #epqmcoivbp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #epqmcoivbp .gt_left { text-align: left; }
 #epqmcoivbp .gt_center { text-align: center; }
 #epqmcoivbp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #epqmcoivbp .gt_font_normal { font-weight: normal; }
 #epqmcoivbp .gt_font_bold { font-weight: bold; }
 #epqmcoivbp .gt_font_italic { font-style: italic; }
 #epqmcoivbp .gt_super { font-size: 65%; }
 #epqmcoivbp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #epqmcoivbp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #epqmcoivbp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #epqmcoivbp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #epqmcoivbp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #epqmcoivbp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
