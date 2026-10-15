# Text Transforms

Sometimes the final step in preparing a table involves modifying the text content of cells after all formatting has been applied. The `text_*()` methods operate on the already-rendered text in cells, giving you a post-processing layer for tasks like replacing abbreviations, applying conditional labels, or inserting custom HTML. These methods complement the `fmt_*()` methods, which work on raw data values.

To clarify the distinction: `fmt_*()` methods work on raw data values *before* they become text. Text transforms work on the *already-rendered text* after formatting. This means you can use [fmt_number()](../reference/GT.fmt_number.md#great_tables.GT.fmt_number) to get consistent decimal places, and then use [text_transform()](../reference/GT.text_transform.md#great_tables.GT.text_transform) to wrap the result in custom HTML or append a unit label. The two layers complement each other, where formatting handles the numeric conversion, and text transforms handle the final presentation touches.


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
#dwvyswztgw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dwvyswztgw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dwvyswztgw p { margin: 0; padding: 0; }
 #dwvyswztgw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dwvyswztgw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dwvyswztgw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dwvyswztgw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dwvyswztgw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dwvyswztgw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dwvyswztgw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dwvyswztgw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dwvyswztgw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dwvyswztgw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dwvyswztgw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dwvyswztgw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dwvyswztgw .gt_spanner_row { border-bottom-style: hidden; }
 #dwvyswztgw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dwvyswztgw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dwvyswztgw .gt_from_md> :first-child { margin-top: 0; }
 #dwvyswztgw .gt_from_md> :last-child { margin-bottom: 0; }
 #dwvyswztgw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dwvyswztgw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dwvyswztgw .gt_indent_1 { text-indent: 5px; }
 #dwvyswztgw .gt_indent_2 { text-indent: calc(5px * 2); }
 #dwvyswztgw .gt_indent_3 { text-indent: calc(5px * 3); }
 #dwvyswztgw .gt_indent_4 { text-indent: calc(5px * 4); }
 #dwvyswztgw .gt_indent_5 { text-indent: calc(5px * 5); }
 #dwvyswztgw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dwvyswztgw .gt_row_group_first td { border-top-width: 2px; }
 #dwvyswztgw .gt_row_group_first th { border-top-width: 2px; }
 #dwvyswztgw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dwvyswztgw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dwvyswztgw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dwvyswztgw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dwvyswztgw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dwvyswztgw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dwvyswztgw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dwvyswztgw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dwvyswztgw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dwvyswztgw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dwvyswztgw .gt_left { text-align: left; }
 #dwvyswztgw .gt_center { text-align: center; }
 #dwvyswztgw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dwvyswztgw .gt_font_normal { font-weight: normal; }
 #dwvyswztgw .gt_font_bold { font-weight: bold; }
 #dwvyswztgw .gt_font_italic { font-style: italic; }
 #dwvyswztgw .gt_super { font-size: 65%; }
 #dwvyswztgw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dwvyswztgw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dwvyswztgw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dwvyswztgw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dwvyswztgw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dwvyswztgw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vqjriyelkl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vqjriyelkl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vqjriyelkl p { margin: 0; padding: 0; }
 #vqjriyelkl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vqjriyelkl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vqjriyelkl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vqjriyelkl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vqjriyelkl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vqjriyelkl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vqjriyelkl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vqjriyelkl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vqjriyelkl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vqjriyelkl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vqjriyelkl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vqjriyelkl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vqjriyelkl .gt_spanner_row { border-bottom-style: hidden; }
 #vqjriyelkl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vqjriyelkl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vqjriyelkl .gt_from_md> :first-child { margin-top: 0; }
 #vqjriyelkl .gt_from_md> :last-child { margin-bottom: 0; }
 #vqjriyelkl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vqjriyelkl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vqjriyelkl .gt_indent_1 { text-indent: 5px; }
 #vqjriyelkl .gt_indent_2 { text-indent: calc(5px * 2); }
 #vqjriyelkl .gt_indent_3 { text-indent: calc(5px * 3); }
 #vqjriyelkl .gt_indent_4 { text-indent: calc(5px * 4); }
 #vqjriyelkl .gt_indent_5 { text-indent: calc(5px * 5); }
 #vqjriyelkl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vqjriyelkl .gt_row_group_first td { border-top-width: 2px; }
 #vqjriyelkl .gt_row_group_first th { border-top-width: 2px; }
 #vqjriyelkl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vqjriyelkl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vqjriyelkl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vqjriyelkl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vqjriyelkl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vqjriyelkl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vqjriyelkl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vqjriyelkl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vqjriyelkl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vqjriyelkl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vqjriyelkl .gt_left { text-align: left; }
 #vqjriyelkl .gt_center { text-align: center; }
 #vqjriyelkl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vqjriyelkl .gt_font_normal { font-weight: normal; }
 #vqjriyelkl .gt_font_bold { font-weight: bold; }
 #vqjriyelkl .gt_font_italic { font-style: italic; }
 #vqjriyelkl .gt_super { font-size: 65%; }
 #vqjriyelkl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vqjriyelkl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vqjriyelkl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vqjriyelkl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vqjriyelkl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vqjriyelkl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#kcxaonavjt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kcxaonavjt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kcxaonavjt p { margin: 0; padding: 0; }
 #kcxaonavjt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kcxaonavjt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kcxaonavjt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kcxaonavjt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kcxaonavjt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kcxaonavjt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kcxaonavjt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kcxaonavjt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kcxaonavjt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kcxaonavjt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kcxaonavjt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kcxaonavjt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kcxaonavjt .gt_spanner_row { border-bottom-style: hidden; }
 #kcxaonavjt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kcxaonavjt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kcxaonavjt .gt_from_md> :first-child { margin-top: 0; }
 #kcxaonavjt .gt_from_md> :last-child { margin-bottom: 0; }
 #kcxaonavjt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kcxaonavjt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kcxaonavjt .gt_indent_1 { text-indent: 5px; }
 #kcxaonavjt .gt_indent_2 { text-indent: calc(5px * 2); }
 #kcxaonavjt .gt_indent_3 { text-indent: calc(5px * 3); }
 #kcxaonavjt .gt_indent_4 { text-indent: calc(5px * 4); }
 #kcxaonavjt .gt_indent_5 { text-indent: calc(5px * 5); }
 #kcxaonavjt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kcxaonavjt .gt_row_group_first td { border-top-width: 2px; }
 #kcxaonavjt .gt_row_group_first th { border-top-width: 2px; }
 #kcxaonavjt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kcxaonavjt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kcxaonavjt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kcxaonavjt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kcxaonavjt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kcxaonavjt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kcxaonavjt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kcxaonavjt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kcxaonavjt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kcxaonavjt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kcxaonavjt .gt_left { text-align: left; }
 #kcxaonavjt .gt_center { text-align: center; }
 #kcxaonavjt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kcxaonavjt .gt_font_normal { font-weight: normal; }
 #kcxaonavjt .gt_font_bold { font-weight: bold; }
 #kcxaonavjt .gt_font_italic { font-style: italic; }
 #kcxaonavjt .gt_super { font-size: 65%; }
 #kcxaonavjt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kcxaonavjt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kcxaonavjt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kcxaonavjt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kcxaonavjt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kcxaonavjt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th id="stub-1" class="gt_row gt_left gt_stub" scope="row">Data collection</th>
<td class="gt_row gt_left" headers="stub-1 status">DONE</td>
<td class="gt_row gt_left" headers="stub-1 priority">high</td>
<td class="gt_row gt_right" headers="stub-1 progress">100%<br />


</div></td>
</tr>
<tr>
<th id="stub-2" class="gt_row gt_left gt_stub" scope="row">Analysis</th>
<td class="gt_row gt_left" headers="stub-2 status">IN_PROGRESS</td>
<td class="gt_row gt_left" headers="stub-2 priority">high</td>
<td class="gt_row gt_right" headers="stub-2 progress">65%<br />


</div></td>
</tr>
<tr>
<th id="stub-3" class="gt_row gt_left gt_stub" scope="row">Report writing</th>
<td class="gt_row gt_left" headers="stub-3 status">NOT_STARTED</td>
<td class="gt_row gt_left" headers="stub-3 priority">medium</td>
<td class="gt_row gt_right" headers="stub-3 progress">0%<br />


</div></td>
</tr>
<tr>
<th id="stub-4" class="gt_row gt_left gt_stub" scope="row">Peer review</th>
<td class="gt_row gt_left" headers="stub-4 status">DONE</td>
<td class="gt_row gt_left" headers="stub-4 priority">low</td>
<td class="gt_row gt_right" headers="stub-4 progress">100%<br />


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
#zmzljurlcl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zmzljurlcl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zmzljurlcl p { margin: 0; padding: 0; }
 #zmzljurlcl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zmzljurlcl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zmzljurlcl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zmzljurlcl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zmzljurlcl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zmzljurlcl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zmzljurlcl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zmzljurlcl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zmzljurlcl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zmzljurlcl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zmzljurlcl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zmzljurlcl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zmzljurlcl .gt_spanner_row { border-bottom-style: hidden; }
 #zmzljurlcl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zmzljurlcl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zmzljurlcl .gt_from_md> :first-child { margin-top: 0; }
 #zmzljurlcl .gt_from_md> :last-child { margin-bottom: 0; }
 #zmzljurlcl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zmzljurlcl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zmzljurlcl .gt_indent_1 { text-indent: 5px; }
 #zmzljurlcl .gt_indent_2 { text-indent: calc(5px * 2); }
 #zmzljurlcl .gt_indent_3 { text-indent: calc(5px * 3); }
 #zmzljurlcl .gt_indent_4 { text-indent: calc(5px * 4); }
 #zmzljurlcl .gt_indent_5 { text-indent: calc(5px * 5); }
 #zmzljurlcl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zmzljurlcl .gt_row_group_first td { border-top-width: 2px; }
 #zmzljurlcl .gt_row_group_first th { border-top-width: 2px; }
 #zmzljurlcl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zmzljurlcl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zmzljurlcl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zmzljurlcl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zmzljurlcl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zmzljurlcl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zmzljurlcl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zmzljurlcl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zmzljurlcl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zmzljurlcl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zmzljurlcl .gt_left { text-align: left; }
 #zmzljurlcl .gt_center { text-align: center; }
 #zmzljurlcl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zmzljurlcl .gt_font_normal { font-weight: normal; }
 #zmzljurlcl .gt_font_bold { font-weight: bold; }
 #zmzljurlcl .gt_font_italic { font-style: italic; }
 #zmzljurlcl .gt_super { font-size: 65%; }
 #zmzljurlcl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zmzljurlcl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zmzljurlcl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zmzljurlcl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zmzljurlcl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zmzljurlcl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fxowjquwmq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fxowjquwmq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fxowjquwmq p { margin: 0; padding: 0; }
 #fxowjquwmq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fxowjquwmq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fxowjquwmq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fxowjquwmq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fxowjquwmq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fxowjquwmq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fxowjquwmq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fxowjquwmq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fxowjquwmq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fxowjquwmq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fxowjquwmq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fxowjquwmq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fxowjquwmq .gt_spanner_row { border-bottom-style: hidden; }
 #fxowjquwmq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fxowjquwmq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fxowjquwmq .gt_from_md> :first-child { margin-top: 0; }
 #fxowjquwmq .gt_from_md> :last-child { margin-bottom: 0; }
 #fxowjquwmq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fxowjquwmq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fxowjquwmq .gt_indent_1 { text-indent: 5px; }
 #fxowjquwmq .gt_indent_2 { text-indent: calc(5px * 2); }
 #fxowjquwmq .gt_indent_3 { text-indent: calc(5px * 3); }
 #fxowjquwmq .gt_indent_4 { text-indent: calc(5px * 4); }
 #fxowjquwmq .gt_indent_5 { text-indent: calc(5px * 5); }
 #fxowjquwmq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fxowjquwmq .gt_row_group_first td { border-top-width: 2px; }
 #fxowjquwmq .gt_row_group_first th { border-top-width: 2px; }
 #fxowjquwmq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fxowjquwmq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fxowjquwmq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fxowjquwmq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fxowjquwmq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fxowjquwmq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fxowjquwmq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fxowjquwmq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fxowjquwmq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fxowjquwmq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fxowjquwmq .gt_left { text-align: left; }
 #fxowjquwmq .gt_center { text-align: center; }
 #fxowjquwmq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fxowjquwmq .gt_font_normal { font-weight: normal; }
 #fxowjquwmq .gt_font_bold { font-weight: bold; }
 #fxowjquwmq .gt_font_italic { font-style: italic; }
 #fxowjquwmq .gt_super { font-size: 65%; }
 #fxowjquwmq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fxowjquwmq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fxowjquwmq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fxowjquwmq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fxowjquwmq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fxowjquwmq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#purhsjhtsq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#purhsjhtsq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#purhsjhtsq p { margin: 0; padding: 0; }
 #purhsjhtsq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #purhsjhtsq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #purhsjhtsq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #purhsjhtsq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #purhsjhtsq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #purhsjhtsq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #purhsjhtsq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #purhsjhtsq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #purhsjhtsq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #purhsjhtsq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #purhsjhtsq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #purhsjhtsq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #purhsjhtsq .gt_spanner_row { border-bottom-style: hidden; }
 #purhsjhtsq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #purhsjhtsq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #purhsjhtsq .gt_from_md> :first-child { margin-top: 0; }
 #purhsjhtsq .gt_from_md> :last-child { margin-bottom: 0; }
 #purhsjhtsq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #purhsjhtsq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #purhsjhtsq .gt_indent_1 { text-indent: 5px; }
 #purhsjhtsq .gt_indent_2 { text-indent: calc(5px * 2); }
 #purhsjhtsq .gt_indent_3 { text-indent: calc(5px * 3); }
 #purhsjhtsq .gt_indent_4 { text-indent: calc(5px * 4); }
 #purhsjhtsq .gt_indent_5 { text-indent: calc(5px * 5); }
 #purhsjhtsq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #purhsjhtsq .gt_row_group_first td { border-top-width: 2px; }
 #purhsjhtsq .gt_row_group_first th { border-top-width: 2px; }
 #purhsjhtsq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #purhsjhtsq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #purhsjhtsq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #purhsjhtsq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #purhsjhtsq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #purhsjhtsq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #purhsjhtsq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #purhsjhtsq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #purhsjhtsq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #purhsjhtsq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #purhsjhtsq .gt_left { text-align: left; }
 #purhsjhtsq .gt_center { text-align: center; }
 #purhsjhtsq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #purhsjhtsq .gt_font_normal { font-weight: normal; }
 #purhsjhtsq .gt_font_bold { font-weight: bold; }
 #purhsjhtsq .gt_font_italic { font-style: italic; }
 #purhsjhtsq .gt_super { font-size: 65%; }
 #purhsjhtsq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #purhsjhtsq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #purhsjhtsq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #purhsjhtsq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #purhsjhtsq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #purhsjhtsq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ngjidtbnmf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ngjidtbnmf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ngjidtbnmf p { margin: 0; padding: 0; }
 #ngjidtbnmf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ngjidtbnmf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ngjidtbnmf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ngjidtbnmf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ngjidtbnmf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ngjidtbnmf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ngjidtbnmf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ngjidtbnmf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ngjidtbnmf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ngjidtbnmf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ngjidtbnmf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ngjidtbnmf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ngjidtbnmf .gt_spanner_row { border-bottom-style: hidden; }
 #ngjidtbnmf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ngjidtbnmf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ngjidtbnmf .gt_from_md> :first-child { margin-top: 0; }
 #ngjidtbnmf .gt_from_md> :last-child { margin-bottom: 0; }
 #ngjidtbnmf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ngjidtbnmf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ngjidtbnmf .gt_indent_1 { text-indent: 5px; }
 #ngjidtbnmf .gt_indent_2 { text-indent: calc(5px * 2); }
 #ngjidtbnmf .gt_indent_3 { text-indent: calc(5px * 3); }
 #ngjidtbnmf .gt_indent_4 { text-indent: calc(5px * 4); }
 #ngjidtbnmf .gt_indent_5 { text-indent: calc(5px * 5); }
 #ngjidtbnmf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ngjidtbnmf .gt_row_group_first td { border-top-width: 2px; }
 #ngjidtbnmf .gt_row_group_first th { border-top-width: 2px; }
 #ngjidtbnmf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ngjidtbnmf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ngjidtbnmf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ngjidtbnmf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ngjidtbnmf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ngjidtbnmf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ngjidtbnmf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ngjidtbnmf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ngjidtbnmf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ngjidtbnmf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ngjidtbnmf .gt_left { text-align: left; }
 #ngjidtbnmf .gt_center { text-align: center; }
 #ngjidtbnmf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ngjidtbnmf .gt_font_normal { font-weight: normal; }
 #ngjidtbnmf .gt_font_bold { font-weight: bold; }
 #ngjidtbnmf .gt_font_italic { font-style: italic; }
 #ngjidtbnmf .gt_super { font-size: 65%; }
 #ngjidtbnmf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ngjidtbnmf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ngjidtbnmf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ngjidtbnmf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ngjidtbnmf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ngjidtbnmf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pcsklhtsqf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pcsklhtsqf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pcsklhtsqf p { margin: 0; padding: 0; }
 #pcsklhtsqf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pcsklhtsqf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pcsklhtsqf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pcsklhtsqf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pcsklhtsqf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pcsklhtsqf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pcsklhtsqf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pcsklhtsqf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pcsklhtsqf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pcsklhtsqf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pcsklhtsqf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pcsklhtsqf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pcsklhtsqf .gt_spanner_row { border-bottom-style: hidden; }
 #pcsklhtsqf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pcsklhtsqf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pcsklhtsqf .gt_from_md> :first-child { margin-top: 0; }
 #pcsklhtsqf .gt_from_md> :last-child { margin-bottom: 0; }
 #pcsklhtsqf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pcsklhtsqf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pcsklhtsqf .gt_indent_1 { text-indent: 5px; }
 #pcsklhtsqf .gt_indent_2 { text-indent: calc(5px * 2); }
 #pcsklhtsqf .gt_indent_3 { text-indent: calc(5px * 3); }
 #pcsklhtsqf .gt_indent_4 { text-indent: calc(5px * 4); }
 #pcsklhtsqf .gt_indent_5 { text-indent: calc(5px * 5); }
 #pcsklhtsqf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pcsklhtsqf .gt_row_group_first td { border-top-width: 2px; }
 #pcsklhtsqf .gt_row_group_first th { border-top-width: 2px; }
 #pcsklhtsqf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pcsklhtsqf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pcsklhtsqf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pcsklhtsqf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pcsklhtsqf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pcsklhtsqf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pcsklhtsqf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pcsklhtsqf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pcsklhtsqf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pcsklhtsqf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pcsklhtsqf .gt_left { text-align: left; }
 #pcsklhtsqf .gt_center { text-align: center; }
 #pcsklhtsqf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pcsklhtsqf .gt_font_normal { font-weight: normal; }
 #pcsklhtsqf .gt_font_bold { font-weight: bold; }
 #pcsklhtsqf .gt_font_italic { font-style: italic; }
 #pcsklhtsqf .gt_super { font-size: 65%; }
 #pcsklhtsqf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pcsklhtsqf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pcsklhtsqf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pcsklhtsqf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pcsklhtsqf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pcsklhtsqf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#oocdgyxsjr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oocdgyxsjr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oocdgyxsjr p { margin: 0; padding: 0; }
 #oocdgyxsjr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oocdgyxsjr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oocdgyxsjr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oocdgyxsjr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oocdgyxsjr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oocdgyxsjr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oocdgyxsjr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oocdgyxsjr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oocdgyxsjr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oocdgyxsjr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oocdgyxsjr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oocdgyxsjr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oocdgyxsjr .gt_spanner_row { border-bottom-style: hidden; }
 #oocdgyxsjr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oocdgyxsjr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #oocdgyxsjr .gt_from_md> :first-child { margin-top: 0; }
 #oocdgyxsjr .gt_from_md> :last-child { margin-bottom: 0; }
 #oocdgyxsjr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #oocdgyxsjr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #oocdgyxsjr .gt_indent_1 { text-indent: 5px; }
 #oocdgyxsjr .gt_indent_2 { text-indent: calc(5px * 2); }
 #oocdgyxsjr .gt_indent_3 { text-indent: calc(5px * 3); }
 #oocdgyxsjr .gt_indent_4 { text-indent: calc(5px * 4); }
 #oocdgyxsjr .gt_indent_5 { text-indent: calc(5px * 5); }
 #oocdgyxsjr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oocdgyxsjr .gt_row_group_first td { border-top-width: 2px; }
 #oocdgyxsjr .gt_row_group_first th { border-top-width: 2px; }
 #oocdgyxsjr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oocdgyxsjr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oocdgyxsjr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oocdgyxsjr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oocdgyxsjr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oocdgyxsjr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oocdgyxsjr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oocdgyxsjr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oocdgyxsjr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oocdgyxsjr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oocdgyxsjr .gt_left { text-align: left; }
 #oocdgyxsjr .gt_center { text-align: center; }
 #oocdgyxsjr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oocdgyxsjr .gt_font_normal { font-weight: normal; }
 #oocdgyxsjr .gt_font_bold { font-weight: bold; }
 #oocdgyxsjr .gt_font_italic { font-style: italic; }
 #oocdgyxsjr .gt_super { font-size: 65%; }
 #oocdgyxsjr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oocdgyxsjr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oocdgyxsjr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oocdgyxsjr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oocdgyxsjr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oocdgyxsjr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#totftruxtq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#totftruxtq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#totftruxtq p { margin: 0; padding: 0; }
 #totftruxtq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #totftruxtq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #totftruxtq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #totftruxtq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #totftruxtq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #totftruxtq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #totftruxtq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #totftruxtq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #totftruxtq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #totftruxtq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #totftruxtq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #totftruxtq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #totftruxtq .gt_spanner_row { border-bottom-style: hidden; }
 #totftruxtq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #totftruxtq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #totftruxtq .gt_from_md> :first-child { margin-top: 0; }
 #totftruxtq .gt_from_md> :last-child { margin-bottom: 0; }
 #totftruxtq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #totftruxtq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #totftruxtq .gt_indent_1 { text-indent: 5px; }
 #totftruxtq .gt_indent_2 { text-indent: calc(5px * 2); }
 #totftruxtq .gt_indent_3 { text-indent: calc(5px * 3); }
 #totftruxtq .gt_indent_4 { text-indent: calc(5px * 4); }
 #totftruxtq .gt_indent_5 { text-indent: calc(5px * 5); }
 #totftruxtq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #totftruxtq .gt_row_group_first td { border-top-width: 2px; }
 #totftruxtq .gt_row_group_first th { border-top-width: 2px; }
 #totftruxtq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #totftruxtq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #totftruxtq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #totftruxtq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #totftruxtq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #totftruxtq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #totftruxtq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #totftruxtq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #totftruxtq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #totftruxtq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #totftruxtq .gt_left { text-align: left; }
 #totftruxtq .gt_center { text-align: center; }
 #totftruxtq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #totftruxtq .gt_font_normal { font-weight: normal; }
 #totftruxtq .gt_font_bold { font-weight: bold; }
 #totftruxtq .gt_font_italic { font-style: italic; }
 #totftruxtq .gt_super { font-size: 65%; }
 #totftruxtq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #totftruxtq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #totftruxtq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #totftruxtq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #totftruxtq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #totftruxtq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="2" id="team_alpha" class="gt_group_heading" scope="colgroup">Team alpha</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">Alice</td>
<td class="gt_row gt_right" headers="team_alpha stub-1 score">92</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">Bob</td>
<td class="gt_row gt_right" headers="team_alpha stub-2 score">87</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" id="team_beta" class="gt_group_heading" scope="colgroup">Team beta</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">Charlie</td>
<td class="gt_row gt_right" headers="team_beta stub-3 score">95</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Diana</td>
<td class="gt_row gt_right" headers="team_beta stub-4 score">78</td>
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
#qbwbterqzn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qbwbterqzn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qbwbterqzn p { margin: 0; padding: 0; }
 #qbwbterqzn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qbwbterqzn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qbwbterqzn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qbwbterqzn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qbwbterqzn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qbwbterqzn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qbwbterqzn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qbwbterqzn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qbwbterqzn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qbwbterqzn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qbwbterqzn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qbwbterqzn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qbwbterqzn .gt_spanner_row { border-bottom-style: hidden; }
 #qbwbterqzn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qbwbterqzn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qbwbterqzn .gt_from_md> :first-child { margin-top: 0; }
 #qbwbterqzn .gt_from_md> :last-child { margin-bottom: 0; }
 #qbwbterqzn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qbwbterqzn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qbwbterqzn .gt_indent_1 { text-indent: 5px; }
 #qbwbterqzn .gt_indent_2 { text-indent: calc(5px * 2); }
 #qbwbterqzn .gt_indent_3 { text-indent: calc(5px * 3); }
 #qbwbterqzn .gt_indent_4 { text-indent: calc(5px * 4); }
 #qbwbterqzn .gt_indent_5 { text-indent: calc(5px * 5); }
 #qbwbterqzn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qbwbterqzn .gt_row_group_first td { border-top-width: 2px; }
 #qbwbterqzn .gt_row_group_first th { border-top-width: 2px; }
 #qbwbterqzn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qbwbterqzn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qbwbterqzn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qbwbterqzn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qbwbterqzn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qbwbterqzn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qbwbterqzn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qbwbterqzn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qbwbterqzn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qbwbterqzn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qbwbterqzn .gt_left { text-align: left; }
 #qbwbterqzn .gt_center { text-align: center; }
 #qbwbterqzn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qbwbterqzn .gt_font_normal { font-weight: normal; }
 #qbwbterqzn .gt_font_bold { font-weight: bold; }
 #qbwbterqzn .gt_font_italic { font-style: italic; }
 #qbwbterqzn .gt_super { font-size: 65%; }
 #qbwbterqzn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qbwbterqzn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qbwbterqzn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qbwbterqzn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qbwbterqzn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qbwbterqzn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#owarbfpvgu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#owarbfpvgu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#owarbfpvgu p { margin: 0; padding: 0; }
 #owarbfpvgu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #owarbfpvgu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #owarbfpvgu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #owarbfpvgu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #owarbfpvgu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #owarbfpvgu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #owarbfpvgu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #owarbfpvgu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #owarbfpvgu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #owarbfpvgu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #owarbfpvgu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #owarbfpvgu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #owarbfpvgu .gt_spanner_row { border-bottom-style: hidden; }
 #owarbfpvgu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #owarbfpvgu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #owarbfpvgu .gt_from_md> :first-child { margin-top: 0; }
 #owarbfpvgu .gt_from_md> :last-child { margin-bottom: 0; }
 #owarbfpvgu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #owarbfpvgu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #owarbfpvgu .gt_indent_1 { text-indent: 5px; }
 #owarbfpvgu .gt_indent_2 { text-indent: calc(5px * 2); }
 #owarbfpvgu .gt_indent_3 { text-indent: calc(5px * 3); }
 #owarbfpvgu .gt_indent_4 { text-indent: calc(5px * 4); }
 #owarbfpvgu .gt_indent_5 { text-indent: calc(5px * 5); }
 #owarbfpvgu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #owarbfpvgu .gt_row_group_first td { border-top-width: 2px; }
 #owarbfpvgu .gt_row_group_first th { border-top-width: 2px; }
 #owarbfpvgu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #owarbfpvgu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #owarbfpvgu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #owarbfpvgu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #owarbfpvgu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #owarbfpvgu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #owarbfpvgu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #owarbfpvgu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #owarbfpvgu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #owarbfpvgu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #owarbfpvgu .gt_left { text-align: left; }
 #owarbfpvgu .gt_center { text-align: center; }
 #owarbfpvgu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #owarbfpvgu .gt_font_normal { font-weight: normal; }
 #owarbfpvgu .gt_font_bold { font-weight: bold; }
 #owarbfpvgu .gt_font_italic { font-style: italic; }
 #owarbfpvgu .gt_super { font-size: 65%; }
 #owarbfpvgu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #owarbfpvgu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #owarbfpvgu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #owarbfpvgu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #owarbfpvgu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #owarbfpvgu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | status      | priority | progress |
|-----------------|-------------|----------|----------|
| Data collection | Complete    | High ●   | 100      |
| Analysis        | In Progress | High ●   | 65       |
| Report writing  | Not Started | Medium ● | 0        |
| Peer review     | Complete    | Low ●    | 100      |


The text transformation methods provide a final layer of control over how your table content appears. Whether you need simple find-and-replace, switch-like mappings, or complex conditional logic, these methods let you shape the text to match your exact presentation needs.
