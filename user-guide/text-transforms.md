# Text Transforms

Sometimes the final step in preparing a table involves modifying the text content of cells after all formatting has been applied. The `text_*()` methods operate on the already-rendered text in cells, giving you a post-processing layer for tasks like replacing abbreviations, applying conditional labels, or inserting custom HTML. These methods complement the `fmt_*()` methods, which work on raw data values.

To clarify the distinction: `fmt_*()` methods work on raw data values *before* they become text. Text transforms work on the *already-rendered text* after formatting. This means you can use `fmt_number()` to get consistent decimal places, and then use [text_transform()](../reference/GT.text_transform.md#great_tables.GT.text_transform) to wrap the result in custom HTML or append a unit label. The two layers complement each other, where formatting handles the numeric conversion, and text transforms handle the final presentation touches.


# Setting Up the Example Data


``` python
import polars as pl
from great_tables import GT, loc, md

status_df = pl.DataFrame({
    "task": ["Data collection", "Analysis", "Report writing", "Peer review"],
    "status": ["DONE", "IN_PROGRESS", "NOT_STARTED", "DONE"],
    "priority": ["high", "high", "medium", "low"],
    "progress": [100, 65, 0, 100],
})

gt_tbl = GT(status_df, rowname_col="task")
gt_tbl
```


<style>
#dzsnbhlhap table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dzsnbhlhap thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dzsnbhlhap p { margin: 0; padding: 0; }
 #dzsnbhlhap .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dzsnbhlhap .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dzsnbhlhap .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dzsnbhlhap .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dzsnbhlhap .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dzsnbhlhap .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dzsnbhlhap .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dzsnbhlhap .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dzsnbhlhap .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dzsnbhlhap .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dzsnbhlhap .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dzsnbhlhap .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dzsnbhlhap .gt_spanner_row { border-bottom-style: hidden; }
 #dzsnbhlhap .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dzsnbhlhap .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dzsnbhlhap .gt_from_md> :first-child { margin-top: 0; }
 #dzsnbhlhap .gt_from_md> :last-child { margin-bottom: 0; }
 #dzsnbhlhap .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dzsnbhlhap .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dzsnbhlhap .gt_indent_1 { text-indent: 5px; }
 #dzsnbhlhap .gt_indent_2 { text-indent: calc(5px * 2); }
 #dzsnbhlhap .gt_indent_3 { text-indent: calc(5px * 3); }
 #dzsnbhlhap .gt_indent_4 { text-indent: calc(5px * 4); }
 #dzsnbhlhap .gt_indent_5 { text-indent: calc(5px * 5); }
 #dzsnbhlhap .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dzsnbhlhap .gt_row_group_first td { border-top-width: 2px; }
 #dzsnbhlhap .gt_row_group_first th { border-top-width: 2px; }
 #dzsnbhlhap .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dzsnbhlhap .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dzsnbhlhap .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dzsnbhlhap .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dzsnbhlhap .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dzsnbhlhap .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dzsnbhlhap .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dzsnbhlhap .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dzsnbhlhap .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dzsnbhlhap .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dzsnbhlhap .gt_left { text-align: left; }
 #dzsnbhlhap .gt_center { text-align: center; }
 #dzsnbhlhap .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dzsnbhlhap .gt_font_normal { font-weight: normal; }
 #dzsnbhlhap .gt_font_bold { font-weight: bold; }
 #dzsnbhlhap .gt_font_italic { font-style: italic; }
 #dzsnbhlhap .gt_super { font-size: 65%; }
 #dzsnbhlhap .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dzsnbhlhap .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dzsnbhlhap .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dzsnbhlhap .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dzsnbhlhap .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dzsnbhlhap .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | status      | priority | progress |
|-----------------|-------------|----------|----------|
| Data collection | DONE        | high     | 100      |
| Analysis        | IN_PROGRESS | high     | 65       |
| Report writing  | NOT_STARTED | medium   | 0        |
| Peer review     | DONE        | low      | 100      |


This produces a basic table with coded status values and numeric progress, which we will transform using the text methods below.


# Custom Text Transformations

The [text_transform()](../reference/GT.text_transform.md#great_tables.GT.text_transform) method is the most flexible of the text methods. It takes a location specifier and a function that receives a cell's text content as a string and returns the transformed string. The transformation runs after all `fmt_*()` methods have been applied.


``` python
(
    gt_tbl
    .text_transform(
        locations=loc.body(columns="status"),
        fn=lambda text: text.replace("_", " ").title()
    )
)
```


<style>
#uavmcnadrr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uavmcnadrr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uavmcnadrr p { margin: 0; padding: 0; }
 #uavmcnadrr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #uavmcnadrr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uavmcnadrr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uavmcnadrr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uavmcnadrr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uavmcnadrr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uavmcnadrr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uavmcnadrr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uavmcnadrr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uavmcnadrr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uavmcnadrr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uavmcnadrr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uavmcnadrr .gt_spanner_row { border-bottom-style: hidden; }
 #uavmcnadrr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uavmcnadrr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #uavmcnadrr .gt_from_md> :first-child { margin-top: 0; }
 #uavmcnadrr .gt_from_md> :last-child { margin-bottom: 0; }
 #uavmcnadrr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #uavmcnadrr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #uavmcnadrr .gt_indent_1 { text-indent: 5px; }
 #uavmcnadrr .gt_indent_2 { text-indent: calc(5px * 2); }
 #uavmcnadrr .gt_indent_3 { text-indent: calc(5px * 3); }
 #uavmcnadrr .gt_indent_4 { text-indent: calc(5px * 4); }
 #uavmcnadrr .gt_indent_5 { text-indent: calc(5px * 5); }
 #uavmcnadrr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uavmcnadrr .gt_row_group_first td { border-top-width: 2px; }
 #uavmcnadrr .gt_row_group_first th { border-top-width: 2px; }
 #uavmcnadrr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uavmcnadrr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uavmcnadrr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uavmcnadrr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uavmcnadrr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uavmcnadrr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uavmcnadrr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uavmcnadrr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uavmcnadrr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uavmcnadrr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uavmcnadrr .gt_left { text-align: left; }
 #uavmcnadrr .gt_center { text-align: center; }
 #uavmcnadrr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uavmcnadrr .gt_font_normal { font-weight: normal; }
 #uavmcnadrr .gt_font_bold { font-weight: bold; }
 #uavmcnadrr .gt_font_italic { font-style: italic; }
 #uavmcnadrr .gt_super { font-size: 65%; }
 #uavmcnadrr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uavmcnadrr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uavmcnadrr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uavmcnadrr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uavmcnadrr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uavmcnadrr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | status      | priority | progress |
|-----------------|-------------|----------|----------|
| Data collection | Done        | high     | 100      |
| Analysis        | In Progress | high     | 65       |
| Report writing  | Not Started | medium   | 0        |
| Peer review     | Done        | low      | 100      |


The underscores in status values are replaced with spaces and the text is converted to title case. This is useful when your data contains coded values that need to be made more readable.

You can also return HTML from the transform function to add visual elements to cells.


``` python
def add_progress_indicator(text):
    value = int(text)
    color = "green" if value == 100 else "orange" if value > 0 else "gray"
    bar = f'<div style="background:{color};width:{value}%;height:8px;border-radius:4px;"></div>'
    return f'{text}%<br>{bar}'

(
    gt_tbl
    .text_transform(
        locations=loc.body(columns="progress"),
        fn=add_progress_indicator
    )
)
```


<style>
#xdublymuwz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xdublymuwz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xdublymuwz p { margin: 0; padding: 0; }
 #xdublymuwz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xdublymuwz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xdublymuwz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xdublymuwz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xdublymuwz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xdublymuwz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xdublymuwz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xdublymuwz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xdublymuwz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xdublymuwz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xdublymuwz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xdublymuwz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xdublymuwz .gt_spanner_row { border-bottom-style: hidden; }
 #xdublymuwz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xdublymuwz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xdublymuwz .gt_from_md> :first-child { margin-top: 0; }
 #xdublymuwz .gt_from_md> :last-child { margin-bottom: 0; }
 #xdublymuwz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xdublymuwz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xdublymuwz .gt_indent_1 { text-indent: 5px; }
 #xdublymuwz .gt_indent_2 { text-indent: calc(5px * 2); }
 #xdublymuwz .gt_indent_3 { text-indent: calc(5px * 3); }
 #xdublymuwz .gt_indent_4 { text-indent: calc(5px * 4); }
 #xdublymuwz .gt_indent_5 { text-indent: calc(5px * 5); }
 #xdublymuwz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xdublymuwz .gt_row_group_first td { border-top-width: 2px; }
 #xdublymuwz .gt_row_group_first th { border-top-width: 2px; }
 #xdublymuwz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xdublymuwz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xdublymuwz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xdublymuwz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xdublymuwz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xdublymuwz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xdublymuwz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xdublymuwz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xdublymuwz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xdublymuwz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xdublymuwz .gt_left { text-align: left; }
 #xdublymuwz .gt_center { text-align: center; }
 #xdublymuwz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xdublymuwz .gt_font_normal { font-weight: normal; }
 #xdublymuwz .gt_font_bold { font-weight: bold; }
 #xdublymuwz .gt_font_italic { font-style: italic; }
 #xdublymuwz .gt_super { font-size: 65%; }
 #xdublymuwz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xdublymuwz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xdublymuwz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xdublymuwz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xdublymuwz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xdublymuwz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="status" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">status</th>
<th id="priority" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">priority</th>
<th id="progress" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">progress</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">Data collection</th>
<td class="gt_row gt_left">DONE</td>
<td class="gt_row gt_left">high</td>
<td class="gt_row gt_right">100%<br />


</div></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Analysis</th>
<td class="gt_row gt_left">IN_PROGRESS</td>
<td class="gt_row gt_left">high</td>
<td class="gt_row gt_right">65%<br />


</div></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Report writing</th>
<td class="gt_row gt_left">NOT_STARTED</td>
<td class="gt_row gt_left">medium</td>
<td class="gt_row gt_right">0%<br />


</div></td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">Peer review</th>
<td class="gt_row gt_left">DONE</td>
<td class="gt_row gt_left">low</td>
<td class="gt_row gt_right">100%<br />


</div></td>
</tr>
</tbody>
</table>


Each progress cell now displays both the numeric percentage and a colored bar beneath it. Returning raw HTML from the function lets you embed rich visual elements directly in table cells.


# Text Replacement with Regex

The [text_replace()](../reference/GT.text_replace.md#great_tables.GT.text_replace) method performs regex-based find-and-replace on cell content. It is a simpler alternative to [text_transform()](../reference/GT.text_transform.md#great_tables.GT.text_transform) when you just need pattern matching.


``` python
(
    gt_tbl
    .text_replace(
        pattern=r"_",
        replacement=" ",
        locations=loc.body(columns="status")
    )
)
```


<style>
#zglsaelmeq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zglsaelmeq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zglsaelmeq p { margin: 0; padding: 0; }
 #zglsaelmeq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zglsaelmeq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zglsaelmeq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zglsaelmeq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zglsaelmeq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zglsaelmeq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zglsaelmeq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zglsaelmeq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zglsaelmeq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zglsaelmeq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zglsaelmeq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zglsaelmeq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zglsaelmeq .gt_spanner_row { border-bottom-style: hidden; }
 #zglsaelmeq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zglsaelmeq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zglsaelmeq .gt_from_md> :first-child { margin-top: 0; }
 #zglsaelmeq .gt_from_md> :last-child { margin-bottom: 0; }
 #zglsaelmeq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zglsaelmeq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zglsaelmeq .gt_indent_1 { text-indent: 5px; }
 #zglsaelmeq .gt_indent_2 { text-indent: calc(5px * 2); }
 #zglsaelmeq .gt_indent_3 { text-indent: calc(5px * 3); }
 #zglsaelmeq .gt_indent_4 { text-indent: calc(5px * 4); }
 #zglsaelmeq .gt_indent_5 { text-indent: calc(5px * 5); }
 #zglsaelmeq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zglsaelmeq .gt_row_group_first td { border-top-width: 2px; }
 #zglsaelmeq .gt_row_group_first th { border-top-width: 2px; }
 #zglsaelmeq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zglsaelmeq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zglsaelmeq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zglsaelmeq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zglsaelmeq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zglsaelmeq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zglsaelmeq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zglsaelmeq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zglsaelmeq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zglsaelmeq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zglsaelmeq .gt_left { text-align: left; }
 #zglsaelmeq .gt_center { text-align: center; }
 #zglsaelmeq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zglsaelmeq .gt_font_normal { font-weight: normal; }
 #zglsaelmeq .gt_font_bold { font-weight: bold; }
 #zglsaelmeq .gt_font_italic { font-style: italic; }
 #zglsaelmeq .gt_super { font-size: 65%; }
 #zglsaelmeq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zglsaelmeq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zglsaelmeq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zglsaelmeq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zglsaelmeq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zglsaelmeq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | status      | priority | progress |
|-----------------|-------------|----------|----------|
| Data collection | DONE        | high     | 100      |
| Analysis        | IN PROGRESS | high     | 65       |
| Report writing  | NOT STARTED | medium   | 0        |
| Peer review     | DONE        | low      | 100      |


All underscores in the `status` column are replaced with spaces. The `pattern=` argument accepts full Python regex syntax, so you can use capture groups and backreferences in the `replacement=` string.


``` python
(
    gt_tbl
    .text_replace(
        pattern=r"(\w+)_(\w+)",
        replacement=r"\1 \2",
        locations=loc.body(columns="status")
    )
)
```


<style>
#cutzxsxjin table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cutzxsxjin thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cutzxsxjin p { margin: 0; padding: 0; }
 #cutzxsxjin .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cutzxsxjin .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cutzxsxjin .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cutzxsxjin .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cutzxsxjin .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cutzxsxjin .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cutzxsxjin .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cutzxsxjin .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cutzxsxjin .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cutzxsxjin .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cutzxsxjin .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cutzxsxjin .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cutzxsxjin .gt_spanner_row { border-bottom-style: hidden; }
 #cutzxsxjin .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cutzxsxjin .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cutzxsxjin .gt_from_md> :first-child { margin-top: 0; }
 #cutzxsxjin .gt_from_md> :last-child { margin-bottom: 0; }
 #cutzxsxjin .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cutzxsxjin .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cutzxsxjin .gt_indent_1 { text-indent: 5px; }
 #cutzxsxjin .gt_indent_2 { text-indent: calc(5px * 2); }
 #cutzxsxjin .gt_indent_3 { text-indent: calc(5px * 3); }
 #cutzxsxjin .gt_indent_4 { text-indent: calc(5px * 4); }
 #cutzxsxjin .gt_indent_5 { text-indent: calc(5px * 5); }
 #cutzxsxjin .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cutzxsxjin .gt_row_group_first td { border-top-width: 2px; }
 #cutzxsxjin .gt_row_group_first th { border-top-width: 2px; }
 #cutzxsxjin .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cutzxsxjin .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cutzxsxjin .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cutzxsxjin .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cutzxsxjin .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cutzxsxjin .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cutzxsxjin .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cutzxsxjin .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cutzxsxjin .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cutzxsxjin .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cutzxsxjin .gt_left { text-align: left; }
 #cutzxsxjin .gt_center { text-align: center; }
 #cutzxsxjin .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cutzxsxjin .gt_font_normal { font-weight: normal; }
 #cutzxsxjin .gt_font_bold { font-weight: bold; }
 #cutzxsxjin .gt_font_italic { font-style: italic; }
 #cutzxsxjin .gt_super { font-size: 65%; }
 #cutzxsxjin .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cutzxsxjin .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cutzxsxjin .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cutzxsxjin .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cutzxsxjin .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cutzxsxjin .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | status      | priority | progress |
|-----------------|-------------|----------|----------|
| Data collection | DONE        | high     | 100      |
| Analysis        | IN PROGRESS | high     | 65       |
| Report writing  | NOT STARTED | medium   | 0        |
| Peer review     | DONE        | low      | 100      |


The regex captures the two words separated by an underscore and reconstructs them with a space in between. This technique is especially handy when your data has structured codes with consistent delimiters.


# Case Matching

The [text_case_match()](../reference/GT.text_case_match.md#great_tables.GT.text_case_match) method provides a switch-like mechanism for replacing cell text. You supply tuples of `(old_text, new_text)` and the method matches cell content against each case in order.


``` python
(
    gt_tbl
    .text_case_match(
        ("DONE", "Complete ✓"),
        ("IN_PROGRESS", "In Progress"),
        ("NOT_STARTED", "Not Started"),
        locations=loc.body(columns="status")
    )
)
```


<style>
#lkywamglhw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lkywamglhw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lkywamglhw p { margin: 0; padding: 0; }
 #lkywamglhw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lkywamglhw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lkywamglhw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lkywamglhw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lkywamglhw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lkywamglhw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lkywamglhw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lkywamglhw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lkywamglhw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lkywamglhw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lkywamglhw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lkywamglhw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lkywamglhw .gt_spanner_row { border-bottom-style: hidden; }
 #lkywamglhw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lkywamglhw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lkywamglhw .gt_from_md> :first-child { margin-top: 0; }
 #lkywamglhw .gt_from_md> :last-child { margin-bottom: 0; }
 #lkywamglhw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lkywamglhw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lkywamglhw .gt_indent_1 { text-indent: 5px; }
 #lkywamglhw .gt_indent_2 { text-indent: calc(5px * 2); }
 #lkywamglhw .gt_indent_3 { text-indent: calc(5px * 3); }
 #lkywamglhw .gt_indent_4 { text-indent: calc(5px * 4); }
 #lkywamglhw .gt_indent_5 { text-indent: calc(5px * 5); }
 #lkywamglhw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lkywamglhw .gt_row_group_first td { border-top-width: 2px; }
 #lkywamglhw .gt_row_group_first th { border-top-width: 2px; }
 #lkywamglhw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lkywamglhw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lkywamglhw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lkywamglhw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lkywamglhw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lkywamglhw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lkywamglhw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lkywamglhw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lkywamglhw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lkywamglhw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lkywamglhw .gt_left { text-align: left; }
 #lkywamglhw .gt_center { text-align: center; }
 #lkywamglhw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lkywamglhw .gt_font_normal { font-weight: normal; }
 #lkywamglhw .gt_font_bold { font-weight: bold; }
 #lkywamglhw .gt_font_italic { font-style: italic; }
 #lkywamglhw .gt_super { font-size: 65%; }
 #lkywamglhw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lkywamglhw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lkywamglhw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lkywamglhw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lkywamglhw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lkywamglhw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | status      | priority | progress |
|-----------------|-------------|----------|----------|
| Data collection | Complete ✓  | high     | 100      |
| Analysis        | In Progress | high     | 65       |
| Report writing  | Not Started | medium   | 0        |
| Peer review     | Complete ✓  | low      | 100      |


Each status code is mapped to a more readable label. By default, [text_case_match()](../reference/GT.text_case_match.md#great_tables.GT.text_case_match) compares the entire cell text (i.e., `replace="all"`). You can set `replace="partial"` to match substrings instead.

When you have a known, finite set of values to map (like status codes, country abbreviations, or category labels) [text_case_match()](../reference/GT.text_case_match.md#great_tables.GT.text_case_match) is more readable and self-documenting than a [text_transform()](../reference/GT.text_transform.md#great_tables.GT.text_transform) call with a lambda containing if/elif chains. The mapping is declared as data rather than buried in control flow. Reserve [text_transform()](../reference/GT.text_transform.md#great_tables.GT.text_transform) for open-ended transformations where the logic can't be expressed as a simple lookup table.


## Matching Multiple Values to One Replacement

The first element of each case tuple can be a list of strings, allowing you to map multiple values to the same replacement.


``` python
(
    gt_tbl
    .text_case_match(
        (["DONE", "IN_PROGRESS"], "Active"),
        ("NOT_STARTED", "Pending"),
        locations=loc.body(columns="status")
    )
)
```


<style>
#rpiotptjtf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rpiotptjtf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rpiotptjtf p { margin: 0; padding: 0; }
 #rpiotptjtf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rpiotptjtf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rpiotptjtf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rpiotptjtf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rpiotptjtf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rpiotptjtf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rpiotptjtf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rpiotptjtf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rpiotptjtf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rpiotptjtf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rpiotptjtf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rpiotptjtf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rpiotptjtf .gt_spanner_row { border-bottom-style: hidden; }
 #rpiotptjtf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rpiotptjtf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rpiotptjtf .gt_from_md> :first-child { margin-top: 0; }
 #rpiotptjtf .gt_from_md> :last-child { margin-bottom: 0; }
 #rpiotptjtf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rpiotptjtf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rpiotptjtf .gt_indent_1 { text-indent: 5px; }
 #rpiotptjtf .gt_indent_2 { text-indent: calc(5px * 2); }
 #rpiotptjtf .gt_indent_3 { text-indent: calc(5px * 3); }
 #rpiotptjtf .gt_indent_4 { text-indent: calc(5px * 4); }
 #rpiotptjtf .gt_indent_5 { text-indent: calc(5px * 5); }
 #rpiotptjtf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rpiotptjtf .gt_row_group_first td { border-top-width: 2px; }
 #rpiotptjtf .gt_row_group_first th { border-top-width: 2px; }
 #rpiotptjtf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rpiotptjtf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rpiotptjtf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rpiotptjtf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rpiotptjtf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rpiotptjtf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rpiotptjtf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rpiotptjtf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rpiotptjtf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rpiotptjtf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rpiotptjtf .gt_left { text-align: left; }
 #rpiotptjtf .gt_center { text-align: center; }
 #rpiotptjtf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rpiotptjtf .gt_font_normal { font-weight: normal; }
 #rpiotptjtf .gt_font_bold { font-weight: bold; }
 #rpiotptjtf .gt_font_italic { font-style: italic; }
 #rpiotptjtf .gt_super { font-size: 65%; }
 #rpiotptjtf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rpiotptjtf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rpiotptjtf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rpiotptjtf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rpiotptjtf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rpiotptjtf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | status  | priority | progress |
|-----------------|---------|----------|----------|
| Data collection | Active  | high     | 100      |
| Analysis        | Active  | high     | 65       |
| Report writing  | Pending | medium   | 0        |
| Peer review     | Active  | low      | 100      |


Both `"DONE"` and `"IN_PROGRESS"` map to `"Active"`, reducing several statuses down to fewer categories. This is convenient when you want to simplify grouped labels for presentation.


## Providing a Default

If some cell values do not match any case, they remain unchanged by default. You can set a fallback value with the `default=` argument.


``` python
(
    gt_tbl
    .text_case_match(
        ("DONE", "Complete"),
        default="Other",
        locations=loc.body(columns="status")
    )
)
```


<style>
#ltyhncfxme table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ltyhncfxme thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ltyhncfxme p { margin: 0; padding: 0; }
 #ltyhncfxme .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ltyhncfxme .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ltyhncfxme .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ltyhncfxme .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ltyhncfxme .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ltyhncfxme .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ltyhncfxme .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ltyhncfxme .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ltyhncfxme .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ltyhncfxme .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ltyhncfxme .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ltyhncfxme .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ltyhncfxme .gt_spanner_row { border-bottom-style: hidden; }
 #ltyhncfxme .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ltyhncfxme .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ltyhncfxme .gt_from_md> :first-child { margin-top: 0; }
 #ltyhncfxme .gt_from_md> :last-child { margin-bottom: 0; }
 #ltyhncfxme .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ltyhncfxme .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ltyhncfxme .gt_indent_1 { text-indent: 5px; }
 #ltyhncfxme .gt_indent_2 { text-indent: calc(5px * 2); }
 #ltyhncfxme .gt_indent_3 { text-indent: calc(5px * 3); }
 #ltyhncfxme .gt_indent_4 { text-indent: calc(5px * 4); }
 #ltyhncfxme .gt_indent_5 { text-indent: calc(5px * 5); }
 #ltyhncfxme .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ltyhncfxme .gt_row_group_first td { border-top-width: 2px; }
 #ltyhncfxme .gt_row_group_first th { border-top-width: 2px; }
 #ltyhncfxme .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ltyhncfxme .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ltyhncfxme .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ltyhncfxme .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ltyhncfxme .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ltyhncfxme .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ltyhncfxme .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ltyhncfxme .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ltyhncfxme .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ltyhncfxme .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ltyhncfxme .gt_left { text-align: left; }
 #ltyhncfxme .gt_center { text-align: center; }
 #ltyhncfxme .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ltyhncfxme .gt_font_normal { font-weight: normal; }
 #ltyhncfxme .gt_font_bold { font-weight: bold; }
 #ltyhncfxme .gt_font_italic { font-style: italic; }
 #ltyhncfxme .gt_super { font-size: 65%; }
 #ltyhncfxme .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ltyhncfxme .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ltyhncfxme .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ltyhncfxme .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ltyhncfxme .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ltyhncfxme .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | status   | priority | progress |
|-----------------|----------|----------|----------|
| Data collection | Complete | high     | 100      |
| Analysis        | Other    | high     | 65       |
| Report writing  | Other    | medium   | 0        |
| Peer review     | Complete | low      | 100      |


Cells containing `"IN_PROGRESS"` and `"NOT_STARTED"` both become `"Other"` since they did not match the single case provided.


# Conditional Text Replacement

The [text_case_when()](../reference/GT.text_case_when.md#great_tables.GT.text_case_when) method gives you predicate-based replacement logic. Each case is a tuple of `(predicate_function, replacement_text)`, where the predicate receives the cell text as a string and returns `True` or `False`. The first matching predicate determines the replacement.


``` python
(
    gt_tbl
    .text_case_when(
        (lambda x: x == "100", "Complete"),
        (lambda x: int(x) > 0, "In Progress"),
        (lambda x: x == "0", "Not Started"),
        locations=loc.body(columns="progress")
    )
)
```


<style>
#hjmaxdckvo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hjmaxdckvo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hjmaxdckvo p { margin: 0; padding: 0; }
 #hjmaxdckvo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hjmaxdckvo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hjmaxdckvo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hjmaxdckvo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hjmaxdckvo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hjmaxdckvo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjmaxdckvo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hjmaxdckvo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hjmaxdckvo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hjmaxdckvo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hjmaxdckvo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hjmaxdckvo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hjmaxdckvo .gt_spanner_row { border-bottom-style: hidden; }
 #hjmaxdckvo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hjmaxdckvo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hjmaxdckvo .gt_from_md> :first-child { margin-top: 0; }
 #hjmaxdckvo .gt_from_md> :last-child { margin-bottom: 0; }
 #hjmaxdckvo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hjmaxdckvo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hjmaxdckvo .gt_indent_1 { text-indent: 5px; }
 #hjmaxdckvo .gt_indent_2 { text-indent: calc(5px * 2); }
 #hjmaxdckvo .gt_indent_3 { text-indent: calc(5px * 3); }
 #hjmaxdckvo .gt_indent_4 { text-indent: calc(5px * 4); }
 #hjmaxdckvo .gt_indent_5 { text-indent: calc(5px * 5); }
 #hjmaxdckvo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hjmaxdckvo .gt_row_group_first td { border-top-width: 2px; }
 #hjmaxdckvo .gt_row_group_first th { border-top-width: 2px; }
 #hjmaxdckvo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hjmaxdckvo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjmaxdckvo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hjmaxdckvo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hjmaxdckvo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjmaxdckvo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hjmaxdckvo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hjmaxdckvo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hjmaxdckvo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjmaxdckvo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hjmaxdckvo .gt_left { text-align: left; }
 #hjmaxdckvo .gt_center { text-align: center; }
 #hjmaxdckvo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hjmaxdckvo .gt_font_normal { font-weight: normal; }
 #hjmaxdckvo .gt_font_bold { font-weight: bold; }
 #hjmaxdckvo .gt_font_italic { font-style: italic; }
 #hjmaxdckvo .gt_super { font-size: 65%; }
 #hjmaxdckvo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjmaxdckvo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hjmaxdckvo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjmaxdckvo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hjmaxdckvo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hjmaxdckvo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | status      | priority | progress    |
|-----------------|-------------|----------|-------------|
| Data collection | DONE        | high     | Complete    |
| Analysis        | IN_PROGRESS | high     | In Progress |
| Report writing  | NOT_STARTED | medium   | Not Started |
| Peer review     | DONE        | low      | Complete    |


This approach is particularly powerful when your replacement logic depends on the value itself (such as numeric thresholds) rather than exact string matching.

The key difference from [text_case_match()](../reference/GT.text_case_match.md#great_tables.GT.text_case_match) is that [text_case_when()](../reference/GT.text_case_when.md#great_tables.GT.text_case_when) is predicate-based: each case is a function that can express numeric thresholds, string containment tests, length checks, or any other boolean logic. Use it when your replacement logic goes beyond exact string matching. If you find yourself writing predicates that are just `lambda x: x == "some_value"`, that's a sign you should use [text_case_match()](../reference/GT.text_case_match.md#great_tables.GT.text_case_match) instead.


# Targeting Different Locations

All text methods support the `locations=` argument, which defaults to [loc.body()](../reference/loc.body.md#great_tables.loc.body) when not specified. You can target other parts of the table as well.


## Transforming Row Group Labels


``` python
df_grouped = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "team": ["team_alpha", "team_alpha", "team_beta", "team_beta"],
    "score": [92, 87, 95, 78],
})

(
    GT(df_grouped, rowname_col="name", groupname_col="team")
    .text_replace(
        pattern=r"team_(\w+)",
        replacement=r"Team \1",
        locations=loc.row_groups()
    )
)
```


<style>
#lvlbmmuwys table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lvlbmmuwys thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lvlbmmuwys p { margin: 0; padding: 0; }
 #lvlbmmuwys .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lvlbmmuwys .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lvlbmmuwys .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lvlbmmuwys .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lvlbmmuwys .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lvlbmmuwys .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lvlbmmuwys .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lvlbmmuwys .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lvlbmmuwys .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lvlbmmuwys .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lvlbmmuwys .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lvlbmmuwys .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lvlbmmuwys .gt_spanner_row { border-bottom-style: hidden; }
 #lvlbmmuwys .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lvlbmmuwys .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lvlbmmuwys .gt_from_md> :first-child { margin-top: 0; }
 #lvlbmmuwys .gt_from_md> :last-child { margin-bottom: 0; }
 #lvlbmmuwys .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lvlbmmuwys .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lvlbmmuwys .gt_indent_1 { text-indent: 5px; }
 #lvlbmmuwys .gt_indent_2 { text-indent: calc(5px * 2); }
 #lvlbmmuwys .gt_indent_3 { text-indent: calc(5px * 3); }
 #lvlbmmuwys .gt_indent_4 { text-indent: calc(5px * 4); }
 #lvlbmmuwys .gt_indent_5 { text-indent: calc(5px * 5); }
 #lvlbmmuwys .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lvlbmmuwys .gt_row_group_first td { border-top-width: 2px; }
 #lvlbmmuwys .gt_row_group_first th { border-top-width: 2px; }
 #lvlbmmuwys .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lvlbmmuwys .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lvlbmmuwys .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lvlbmmuwys .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lvlbmmuwys .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lvlbmmuwys .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lvlbmmuwys .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lvlbmmuwys .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lvlbmmuwys .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lvlbmmuwys .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lvlbmmuwys .gt_left { text-align: left; }
 #lvlbmmuwys .gt_center { text-align: center; }
 #lvlbmmuwys .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lvlbmmuwys .gt_font_normal { font-weight: normal; }
 #lvlbmmuwys .gt_font_bold { font-weight: bold; }
 #lvlbmmuwys .gt_font_italic { font-style: italic; }
 #lvlbmmuwys .gt_super { font-size: 65%; }
 #lvlbmmuwys .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lvlbmmuwys .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lvlbmmuwys .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lvlbmmuwys .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lvlbmmuwys .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lvlbmmuwys .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="score" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">score</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="2" class="gt_group_heading">Team alpha</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">Alice</td>
<td class="gt_row gt_right">92</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Bob</td>
<td class="gt_row gt_right">87</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading">Team beta</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Charlie</td>
<td class="gt_row gt_right">95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Diana</td>
<td class="gt_row gt_right">78</td>
</tr>
</tbody>
</table>


The row group labels are transformed from `"team_alpha"` and `"team_beta"` to `"Team alpha"` and `"Team beta"`. This keeps the source data unchanged while presenting a polished label in the table.


## Transforming Column Labels


``` python
(
    gt_tbl
    .text_transform(
        locations=loc.column_labels(columns="progress"),
        fn=lambda text: text.upper()
    )
)
```


<style>
#cejpoaqdjs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cejpoaqdjs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cejpoaqdjs p { margin: 0; padding: 0; }
 #cejpoaqdjs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cejpoaqdjs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cejpoaqdjs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cejpoaqdjs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cejpoaqdjs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cejpoaqdjs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cejpoaqdjs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cejpoaqdjs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cejpoaqdjs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cejpoaqdjs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cejpoaqdjs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cejpoaqdjs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cejpoaqdjs .gt_spanner_row { border-bottom-style: hidden; }
 #cejpoaqdjs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cejpoaqdjs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cejpoaqdjs .gt_from_md> :first-child { margin-top: 0; }
 #cejpoaqdjs .gt_from_md> :last-child { margin-bottom: 0; }
 #cejpoaqdjs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cejpoaqdjs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cejpoaqdjs .gt_indent_1 { text-indent: 5px; }
 #cejpoaqdjs .gt_indent_2 { text-indent: calc(5px * 2); }
 #cejpoaqdjs .gt_indent_3 { text-indent: calc(5px * 3); }
 #cejpoaqdjs .gt_indent_4 { text-indent: calc(5px * 4); }
 #cejpoaqdjs .gt_indent_5 { text-indent: calc(5px * 5); }
 #cejpoaqdjs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cejpoaqdjs .gt_row_group_first td { border-top-width: 2px; }
 #cejpoaqdjs .gt_row_group_first th { border-top-width: 2px; }
 #cejpoaqdjs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cejpoaqdjs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cejpoaqdjs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cejpoaqdjs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cejpoaqdjs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cejpoaqdjs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cejpoaqdjs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cejpoaqdjs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cejpoaqdjs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cejpoaqdjs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cejpoaqdjs .gt_left { text-align: left; }
 #cejpoaqdjs .gt_center { text-align: center; }
 #cejpoaqdjs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cejpoaqdjs .gt_font_normal { font-weight: normal; }
 #cejpoaqdjs .gt_font_bold { font-weight: bold; }
 #cejpoaqdjs .gt_font_italic { font-style: italic; }
 #cejpoaqdjs .gt_super { font-size: 65%; }
 #cejpoaqdjs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cejpoaqdjs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cejpoaqdjs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cejpoaqdjs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cejpoaqdjs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cejpoaqdjs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | status      | priority | PROGRESS |
|-----------------|-------------|----------|----------|
| Data collection | DONE        | high     | 100      |
| Analysis        | IN_PROGRESS | high     | 65       |
| Report writing  | NOT_STARTED | medium   | 0        |
| Peer review     | DONE        | low      | 100      |


The `"progress"` column label is converted to uppercase. You can target any combination of column labels using the `columns=` argument within [loc.column_labels()](../reference/loc.column_labels.md#great_tables.loc.column_labels).


# Combining Text Methods

You can chain multiple text methods together. They are applied in the order specified, each operating on the result of the previous transformation.


``` python
(
    gt_tbl
    .text_case_match(
        ("DONE", "Complete"),
        ("IN_PROGRESS", "In Progress"),
        ("NOT_STARTED", "Not Started"),
        locations=loc.body(columns="status")
    )
    .text_case_match(
        ("high", "High ●"),
        ("medium", "Medium ●"),
        ("low", "Low ●"),
        locations=loc.body(columns="priority")
    )
)
```


<style>
#rfhwvkezeg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rfhwvkezeg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rfhwvkezeg p { margin: 0; padding: 0; }
 #rfhwvkezeg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rfhwvkezeg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rfhwvkezeg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rfhwvkezeg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rfhwvkezeg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rfhwvkezeg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rfhwvkezeg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rfhwvkezeg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rfhwvkezeg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rfhwvkezeg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rfhwvkezeg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rfhwvkezeg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rfhwvkezeg .gt_spanner_row { border-bottom-style: hidden; }
 #rfhwvkezeg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rfhwvkezeg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rfhwvkezeg .gt_from_md> :first-child { margin-top: 0; }
 #rfhwvkezeg .gt_from_md> :last-child { margin-bottom: 0; }
 #rfhwvkezeg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rfhwvkezeg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rfhwvkezeg .gt_indent_1 { text-indent: 5px; }
 #rfhwvkezeg .gt_indent_2 { text-indent: calc(5px * 2); }
 #rfhwvkezeg .gt_indent_3 { text-indent: calc(5px * 3); }
 #rfhwvkezeg .gt_indent_4 { text-indent: calc(5px * 4); }
 #rfhwvkezeg .gt_indent_5 { text-indent: calc(5px * 5); }
 #rfhwvkezeg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rfhwvkezeg .gt_row_group_first td { border-top-width: 2px; }
 #rfhwvkezeg .gt_row_group_first th { border-top-width: 2px; }
 #rfhwvkezeg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rfhwvkezeg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rfhwvkezeg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rfhwvkezeg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rfhwvkezeg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rfhwvkezeg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rfhwvkezeg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rfhwvkezeg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rfhwvkezeg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rfhwvkezeg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rfhwvkezeg .gt_left { text-align: left; }
 #rfhwvkezeg .gt_center { text-align: center; }
 #rfhwvkezeg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rfhwvkezeg .gt_font_normal { font-weight: normal; }
 #rfhwvkezeg .gt_font_bold { font-weight: bold; }
 #rfhwvkezeg .gt_font_italic { font-style: italic; }
 #rfhwvkezeg .gt_super { font-size: 65%; }
 #rfhwvkezeg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rfhwvkezeg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rfhwvkezeg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rfhwvkezeg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rfhwvkezeg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rfhwvkezeg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | status      | priority | progress |
|-----------------|-------------|----------|----------|
| Data collection | Complete    | High ●   | 100      |
| Analysis        | In Progress | High ●   | 65       |
| Report writing  | Not Started | Medium ● | 0        |
| Peer review     | Complete    | Low ●    | 100      |


The text transformation methods provide a final layer of control over how your table content appears. Whether you need simple find-and-replace, switch-like mappings, or complex conditional logic, these methods let you shape the text to match your exact presentation needs.
