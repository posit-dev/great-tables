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
#wjnnahuvpi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wjnnahuvpi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wjnnahuvpi p { margin: 0; padding: 0; }
 #wjnnahuvpi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wjnnahuvpi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wjnnahuvpi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wjnnahuvpi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wjnnahuvpi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wjnnahuvpi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjnnahuvpi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wjnnahuvpi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wjnnahuvpi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wjnnahuvpi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wjnnahuvpi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wjnnahuvpi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wjnnahuvpi .gt_spanner_row { border-bottom-style: hidden; }
 #wjnnahuvpi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wjnnahuvpi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wjnnahuvpi .gt_from_md> :first-child { margin-top: 0; }
 #wjnnahuvpi .gt_from_md> :last-child { margin-bottom: 0; }
 #wjnnahuvpi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wjnnahuvpi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wjnnahuvpi .gt_indent_1 { text-indent: 5px; }
 #wjnnahuvpi .gt_indent_2 { text-indent: calc(5px * 2); }
 #wjnnahuvpi .gt_indent_3 { text-indent: calc(5px * 3); }
 #wjnnahuvpi .gt_indent_4 { text-indent: calc(5px * 4); }
 #wjnnahuvpi .gt_indent_5 { text-indent: calc(5px * 5); }
 #wjnnahuvpi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wjnnahuvpi .gt_row_group_first td { border-top-width: 2px; }
 #wjnnahuvpi .gt_row_group_first th { border-top-width: 2px; }
 #wjnnahuvpi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wjnnahuvpi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjnnahuvpi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wjnnahuvpi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wjnnahuvpi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wjnnahuvpi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wjnnahuvpi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wjnnahuvpi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wjnnahuvpi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjnnahuvpi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wjnnahuvpi .gt_left { text-align: left; }
 #wjnnahuvpi .gt_center { text-align: center; }
 #wjnnahuvpi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wjnnahuvpi .gt_font_normal { font-weight: normal; }
 #wjnnahuvpi .gt_font_bold { font-weight: bold; }
 #wjnnahuvpi .gt_font_italic { font-style: italic; }
 #wjnnahuvpi .gt_super { font-size: 65%; }
 #wjnnahuvpi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjnnahuvpi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wjnnahuvpi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wjnnahuvpi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wjnnahuvpi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wjnnahuvpi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#naiebyyavj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#naiebyyavj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#naiebyyavj p { margin: 0; padding: 0; }
 #naiebyyavj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #naiebyyavj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #naiebyyavj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #naiebyyavj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #naiebyyavj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #naiebyyavj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #naiebyyavj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #naiebyyavj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #naiebyyavj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #naiebyyavj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #naiebyyavj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #naiebyyavj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #naiebyyavj .gt_spanner_row { border-bottom-style: hidden; }
 #naiebyyavj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #naiebyyavj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #naiebyyavj .gt_from_md> :first-child { margin-top: 0; }
 #naiebyyavj .gt_from_md> :last-child { margin-bottom: 0; }
 #naiebyyavj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #naiebyyavj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #naiebyyavj .gt_indent_1 { text-indent: 5px; }
 #naiebyyavj .gt_indent_2 { text-indent: calc(5px * 2); }
 #naiebyyavj .gt_indent_3 { text-indent: calc(5px * 3); }
 #naiebyyavj .gt_indent_4 { text-indent: calc(5px * 4); }
 #naiebyyavj .gt_indent_5 { text-indent: calc(5px * 5); }
 #naiebyyavj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #naiebyyavj .gt_row_group_first td { border-top-width: 2px; }
 #naiebyyavj .gt_row_group_first th { border-top-width: 2px; }
 #naiebyyavj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #naiebyyavj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #naiebyyavj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #naiebyyavj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #naiebyyavj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #naiebyyavj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #naiebyyavj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #naiebyyavj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #naiebyyavj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #naiebyyavj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #naiebyyavj .gt_left { text-align: left; }
 #naiebyyavj .gt_center { text-align: center; }
 #naiebyyavj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #naiebyyavj .gt_font_normal { font-weight: normal; }
 #naiebyyavj .gt_font_bold { font-weight: bold; }
 #naiebyyavj .gt_font_italic { font-style: italic; }
 #naiebyyavj .gt_super { font-size: 65%; }
 #naiebyyavj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #naiebyyavj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #naiebyyavj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #naiebyyavj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #naiebyyavj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #naiebyyavj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fcydgdvhwd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fcydgdvhwd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fcydgdvhwd p { margin: 0; padding: 0; }
 #fcydgdvhwd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fcydgdvhwd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fcydgdvhwd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fcydgdvhwd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fcydgdvhwd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fcydgdvhwd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fcydgdvhwd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fcydgdvhwd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fcydgdvhwd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fcydgdvhwd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fcydgdvhwd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fcydgdvhwd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fcydgdvhwd .gt_spanner_row { border-bottom-style: hidden; }
 #fcydgdvhwd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fcydgdvhwd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fcydgdvhwd .gt_from_md> :first-child { margin-top: 0; }
 #fcydgdvhwd .gt_from_md> :last-child { margin-bottom: 0; }
 #fcydgdvhwd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fcydgdvhwd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fcydgdvhwd .gt_indent_1 { text-indent: 5px; }
 #fcydgdvhwd .gt_indent_2 { text-indent: calc(5px * 2); }
 #fcydgdvhwd .gt_indent_3 { text-indent: calc(5px * 3); }
 #fcydgdvhwd .gt_indent_4 { text-indent: calc(5px * 4); }
 #fcydgdvhwd .gt_indent_5 { text-indent: calc(5px * 5); }
 #fcydgdvhwd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fcydgdvhwd .gt_row_group_first td { border-top-width: 2px; }
 #fcydgdvhwd .gt_row_group_first th { border-top-width: 2px; }
 #fcydgdvhwd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fcydgdvhwd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fcydgdvhwd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fcydgdvhwd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fcydgdvhwd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fcydgdvhwd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fcydgdvhwd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fcydgdvhwd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fcydgdvhwd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fcydgdvhwd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fcydgdvhwd .gt_left { text-align: left; }
 #fcydgdvhwd .gt_center { text-align: center; }
 #fcydgdvhwd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fcydgdvhwd .gt_font_normal { font-weight: normal; }
 #fcydgdvhwd .gt_font_bold { font-weight: bold; }
 #fcydgdvhwd .gt_font_italic { font-style: italic; }
 #fcydgdvhwd .gt_super { font-size: 65%; }
 #fcydgdvhwd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fcydgdvhwd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fcydgdvhwd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fcydgdvhwd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fcydgdvhwd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fcydgdvhwd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#scilialiyk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#scilialiyk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#scilialiyk p { margin: 0; padding: 0; }
 #scilialiyk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #scilialiyk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #scilialiyk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #scilialiyk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #scilialiyk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #scilialiyk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #scilialiyk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #scilialiyk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #scilialiyk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #scilialiyk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #scilialiyk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #scilialiyk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #scilialiyk .gt_spanner_row { border-bottom-style: hidden; }
 #scilialiyk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #scilialiyk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #scilialiyk .gt_from_md> :first-child { margin-top: 0; }
 #scilialiyk .gt_from_md> :last-child { margin-bottom: 0; }
 #scilialiyk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #scilialiyk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #scilialiyk .gt_indent_1 { text-indent: 5px; }
 #scilialiyk .gt_indent_2 { text-indent: calc(5px * 2); }
 #scilialiyk .gt_indent_3 { text-indent: calc(5px * 3); }
 #scilialiyk .gt_indent_4 { text-indent: calc(5px * 4); }
 #scilialiyk .gt_indent_5 { text-indent: calc(5px * 5); }
 #scilialiyk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #scilialiyk .gt_row_group_first td { border-top-width: 2px; }
 #scilialiyk .gt_row_group_first th { border-top-width: 2px; }
 #scilialiyk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #scilialiyk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #scilialiyk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #scilialiyk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #scilialiyk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #scilialiyk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #scilialiyk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #scilialiyk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #scilialiyk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #scilialiyk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #scilialiyk .gt_left { text-align: left; }
 #scilialiyk .gt_center { text-align: center; }
 #scilialiyk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #scilialiyk .gt_font_normal { font-weight: normal; }
 #scilialiyk .gt_font_bold { font-weight: bold; }
 #scilialiyk .gt_font_italic { font-style: italic; }
 #scilialiyk .gt_super { font-size: 65%; }
 #scilialiyk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #scilialiyk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #scilialiyk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #scilialiyk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #scilialiyk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #scilialiyk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zjkpqqpulk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zjkpqqpulk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zjkpqqpulk p { margin: 0; padding: 0; }
 #zjkpqqpulk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zjkpqqpulk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zjkpqqpulk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zjkpqqpulk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zjkpqqpulk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zjkpqqpulk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zjkpqqpulk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zjkpqqpulk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zjkpqqpulk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zjkpqqpulk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zjkpqqpulk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zjkpqqpulk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zjkpqqpulk .gt_spanner_row { border-bottom-style: hidden; }
 #zjkpqqpulk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zjkpqqpulk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zjkpqqpulk .gt_from_md> :first-child { margin-top: 0; }
 #zjkpqqpulk .gt_from_md> :last-child { margin-bottom: 0; }
 #zjkpqqpulk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zjkpqqpulk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zjkpqqpulk .gt_indent_1 { text-indent: 5px; }
 #zjkpqqpulk .gt_indent_2 { text-indent: calc(5px * 2); }
 #zjkpqqpulk .gt_indent_3 { text-indent: calc(5px * 3); }
 #zjkpqqpulk .gt_indent_4 { text-indent: calc(5px * 4); }
 #zjkpqqpulk .gt_indent_5 { text-indent: calc(5px * 5); }
 #zjkpqqpulk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zjkpqqpulk .gt_row_group_first td { border-top-width: 2px; }
 #zjkpqqpulk .gt_row_group_first th { border-top-width: 2px; }
 #zjkpqqpulk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zjkpqqpulk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zjkpqqpulk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zjkpqqpulk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zjkpqqpulk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zjkpqqpulk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zjkpqqpulk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zjkpqqpulk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zjkpqqpulk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zjkpqqpulk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zjkpqqpulk .gt_left { text-align: left; }
 #zjkpqqpulk .gt_center { text-align: center; }
 #zjkpqqpulk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zjkpqqpulk .gt_font_normal { font-weight: normal; }
 #zjkpqqpulk .gt_font_bold { font-weight: bold; }
 #zjkpqqpulk .gt_font_italic { font-style: italic; }
 #zjkpqqpulk .gt_super { font-size: 65%; }
 #zjkpqqpulk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zjkpqqpulk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zjkpqqpulk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zjkpqqpulk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zjkpqqpulk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zjkpqqpulk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ttykqbtvep table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ttykqbtvep thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ttykqbtvep p { margin: 0; padding: 0; }
 #ttykqbtvep .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ttykqbtvep .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ttykqbtvep .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ttykqbtvep .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ttykqbtvep .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ttykqbtvep .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ttykqbtvep .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ttykqbtvep .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ttykqbtvep .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ttykqbtvep .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ttykqbtvep .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ttykqbtvep .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ttykqbtvep .gt_spanner_row { border-bottom-style: hidden; }
 #ttykqbtvep .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ttykqbtvep .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ttykqbtvep .gt_from_md> :first-child { margin-top: 0; }
 #ttykqbtvep .gt_from_md> :last-child { margin-bottom: 0; }
 #ttykqbtvep .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ttykqbtvep .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ttykqbtvep .gt_indent_1 { text-indent: 5px; }
 #ttykqbtvep .gt_indent_2 { text-indent: calc(5px * 2); }
 #ttykqbtvep .gt_indent_3 { text-indent: calc(5px * 3); }
 #ttykqbtvep .gt_indent_4 { text-indent: calc(5px * 4); }
 #ttykqbtvep .gt_indent_5 { text-indent: calc(5px * 5); }
 #ttykqbtvep .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ttykqbtvep .gt_row_group_first td { border-top-width: 2px; }
 #ttykqbtvep .gt_row_group_first th { border-top-width: 2px; }
 #ttykqbtvep .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ttykqbtvep .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ttykqbtvep .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ttykqbtvep .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ttykqbtvep .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ttykqbtvep .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ttykqbtvep .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ttykqbtvep .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ttykqbtvep .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ttykqbtvep .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ttykqbtvep .gt_left { text-align: left; }
 #ttykqbtvep .gt_center { text-align: center; }
 #ttykqbtvep .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ttykqbtvep .gt_font_normal { font-weight: normal; }
 #ttykqbtvep .gt_font_bold { font-weight: bold; }
 #ttykqbtvep .gt_font_italic { font-style: italic; }
 #ttykqbtvep .gt_super { font-size: 65%; }
 #ttykqbtvep .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ttykqbtvep .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ttykqbtvep .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ttykqbtvep .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ttykqbtvep .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ttykqbtvep .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#gxmvgvlkes table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gxmvgvlkes thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gxmvgvlkes p { margin: 0; padding: 0; }
 #gxmvgvlkes .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gxmvgvlkes .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gxmvgvlkes .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gxmvgvlkes .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gxmvgvlkes .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gxmvgvlkes .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gxmvgvlkes .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gxmvgvlkes .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gxmvgvlkes .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gxmvgvlkes .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gxmvgvlkes .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gxmvgvlkes .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gxmvgvlkes .gt_spanner_row { border-bottom-style: hidden; }
 #gxmvgvlkes .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gxmvgvlkes .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gxmvgvlkes .gt_from_md> :first-child { margin-top: 0; }
 #gxmvgvlkes .gt_from_md> :last-child { margin-bottom: 0; }
 #gxmvgvlkes .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gxmvgvlkes .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gxmvgvlkes .gt_indent_1 { text-indent: 5px; }
 #gxmvgvlkes .gt_indent_2 { text-indent: calc(5px * 2); }
 #gxmvgvlkes .gt_indent_3 { text-indent: calc(5px * 3); }
 #gxmvgvlkes .gt_indent_4 { text-indent: calc(5px * 4); }
 #gxmvgvlkes .gt_indent_5 { text-indent: calc(5px * 5); }
 #gxmvgvlkes .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gxmvgvlkes .gt_row_group_first td { border-top-width: 2px; }
 #gxmvgvlkes .gt_row_group_first th { border-top-width: 2px; }
 #gxmvgvlkes .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gxmvgvlkes .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gxmvgvlkes .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gxmvgvlkes .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gxmvgvlkes .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gxmvgvlkes .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gxmvgvlkes .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gxmvgvlkes .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gxmvgvlkes .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gxmvgvlkes .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gxmvgvlkes .gt_left { text-align: left; }
 #gxmvgvlkes .gt_center { text-align: center; }
 #gxmvgvlkes .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gxmvgvlkes .gt_font_normal { font-weight: normal; }
 #gxmvgvlkes .gt_font_bold { font-weight: bold; }
 #gxmvgvlkes .gt_font_italic { font-style: italic; }
 #gxmvgvlkes .gt_super { font-size: 65%; }
 #gxmvgvlkes .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gxmvgvlkes .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gxmvgvlkes .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gxmvgvlkes .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gxmvgvlkes .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gxmvgvlkes .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#iaubpgneyc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iaubpgneyc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iaubpgneyc p { margin: 0; padding: 0; }
 #iaubpgneyc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #iaubpgneyc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iaubpgneyc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iaubpgneyc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iaubpgneyc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iaubpgneyc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iaubpgneyc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iaubpgneyc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iaubpgneyc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iaubpgneyc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iaubpgneyc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iaubpgneyc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iaubpgneyc .gt_spanner_row { border-bottom-style: hidden; }
 #iaubpgneyc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iaubpgneyc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #iaubpgneyc .gt_from_md> :first-child { margin-top: 0; }
 #iaubpgneyc .gt_from_md> :last-child { margin-bottom: 0; }
 #iaubpgneyc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #iaubpgneyc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #iaubpgneyc .gt_indent_1 { text-indent: 5px; }
 #iaubpgneyc .gt_indent_2 { text-indent: calc(5px * 2); }
 #iaubpgneyc .gt_indent_3 { text-indent: calc(5px * 3); }
 #iaubpgneyc .gt_indent_4 { text-indent: calc(5px * 4); }
 #iaubpgneyc .gt_indent_5 { text-indent: calc(5px * 5); }
 #iaubpgneyc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iaubpgneyc .gt_row_group_first td { border-top-width: 2px; }
 #iaubpgneyc .gt_row_group_first th { border-top-width: 2px; }
 #iaubpgneyc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #iaubpgneyc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iaubpgneyc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iaubpgneyc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #iaubpgneyc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iaubpgneyc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iaubpgneyc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iaubpgneyc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iaubpgneyc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iaubpgneyc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iaubpgneyc .gt_left { text-align: left; }
 #iaubpgneyc .gt_center { text-align: center; }
 #iaubpgneyc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iaubpgneyc .gt_font_normal { font-weight: normal; }
 #iaubpgneyc .gt_font_bold { font-weight: bold; }
 #iaubpgneyc .gt_font_italic { font-style: italic; }
 #iaubpgneyc .gt_super { font-size: 65%; }
 #iaubpgneyc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iaubpgneyc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #iaubpgneyc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iaubpgneyc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iaubpgneyc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iaubpgneyc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zpyusetxct table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zpyusetxct thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zpyusetxct p { margin: 0; padding: 0; }
 #zpyusetxct .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zpyusetxct .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zpyusetxct .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zpyusetxct .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zpyusetxct .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zpyusetxct .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zpyusetxct .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zpyusetxct .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zpyusetxct .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zpyusetxct .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zpyusetxct .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zpyusetxct .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zpyusetxct .gt_spanner_row { border-bottom-style: hidden; }
 #zpyusetxct .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zpyusetxct .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zpyusetxct .gt_from_md> :first-child { margin-top: 0; }
 #zpyusetxct .gt_from_md> :last-child { margin-bottom: 0; }
 #zpyusetxct .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zpyusetxct .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zpyusetxct .gt_indent_1 { text-indent: 5px; }
 #zpyusetxct .gt_indent_2 { text-indent: calc(5px * 2); }
 #zpyusetxct .gt_indent_3 { text-indent: calc(5px * 3); }
 #zpyusetxct .gt_indent_4 { text-indent: calc(5px * 4); }
 #zpyusetxct .gt_indent_5 { text-indent: calc(5px * 5); }
 #zpyusetxct .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zpyusetxct .gt_row_group_first td { border-top-width: 2px; }
 #zpyusetxct .gt_row_group_first th { border-top-width: 2px; }
 #zpyusetxct .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zpyusetxct .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zpyusetxct .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zpyusetxct .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zpyusetxct .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zpyusetxct .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zpyusetxct .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zpyusetxct .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zpyusetxct .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zpyusetxct .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zpyusetxct .gt_left { text-align: left; }
 #zpyusetxct .gt_center { text-align: center; }
 #zpyusetxct .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zpyusetxct .gt_font_normal { font-weight: normal; }
 #zpyusetxct .gt_font_bold { font-weight: bold; }
 #zpyusetxct .gt_font_italic { font-style: italic; }
 #zpyusetxct .gt_super { font-size: 65%; }
 #zpyusetxct .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zpyusetxct .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zpyusetxct .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zpyusetxct .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zpyusetxct .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zpyusetxct .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#htptsjrtgz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#htptsjrtgz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#htptsjrtgz p { margin: 0; padding: 0; }
 #htptsjrtgz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #htptsjrtgz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #htptsjrtgz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #htptsjrtgz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #htptsjrtgz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #htptsjrtgz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #htptsjrtgz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #htptsjrtgz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #htptsjrtgz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #htptsjrtgz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #htptsjrtgz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #htptsjrtgz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #htptsjrtgz .gt_spanner_row { border-bottom-style: hidden; }
 #htptsjrtgz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #htptsjrtgz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #htptsjrtgz .gt_from_md> :first-child { margin-top: 0; }
 #htptsjrtgz .gt_from_md> :last-child { margin-bottom: 0; }
 #htptsjrtgz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #htptsjrtgz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #htptsjrtgz .gt_indent_1 { text-indent: 5px; }
 #htptsjrtgz .gt_indent_2 { text-indent: calc(5px * 2); }
 #htptsjrtgz .gt_indent_3 { text-indent: calc(5px * 3); }
 #htptsjrtgz .gt_indent_4 { text-indent: calc(5px * 4); }
 #htptsjrtgz .gt_indent_5 { text-indent: calc(5px * 5); }
 #htptsjrtgz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #htptsjrtgz .gt_row_group_first td { border-top-width: 2px; }
 #htptsjrtgz .gt_row_group_first th { border-top-width: 2px; }
 #htptsjrtgz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #htptsjrtgz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #htptsjrtgz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #htptsjrtgz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #htptsjrtgz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #htptsjrtgz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #htptsjrtgz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #htptsjrtgz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #htptsjrtgz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #htptsjrtgz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #htptsjrtgz .gt_left { text-align: left; }
 #htptsjrtgz .gt_center { text-align: center; }
 #htptsjrtgz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #htptsjrtgz .gt_font_normal { font-weight: normal; }
 #htptsjrtgz .gt_font_bold { font-weight: bold; }
 #htptsjrtgz .gt_font_italic { font-style: italic; }
 #htptsjrtgz .gt_super { font-size: 65%; }
 #htptsjrtgz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #htptsjrtgz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #htptsjrtgz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #htptsjrtgz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #htptsjrtgz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #htptsjrtgz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ykuyzngwxn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ykuyzngwxn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ykuyzngwxn p { margin: 0; padding: 0; }
 #ykuyzngwxn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ykuyzngwxn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ykuyzngwxn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ykuyzngwxn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ykuyzngwxn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ykuyzngwxn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ykuyzngwxn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ykuyzngwxn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ykuyzngwxn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ykuyzngwxn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ykuyzngwxn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ykuyzngwxn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ykuyzngwxn .gt_spanner_row { border-bottom-style: hidden; }
 #ykuyzngwxn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ykuyzngwxn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ykuyzngwxn .gt_from_md> :first-child { margin-top: 0; }
 #ykuyzngwxn .gt_from_md> :last-child { margin-bottom: 0; }
 #ykuyzngwxn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ykuyzngwxn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ykuyzngwxn .gt_indent_1 { text-indent: 5px; }
 #ykuyzngwxn .gt_indent_2 { text-indent: calc(5px * 2); }
 #ykuyzngwxn .gt_indent_3 { text-indent: calc(5px * 3); }
 #ykuyzngwxn .gt_indent_4 { text-indent: calc(5px * 4); }
 #ykuyzngwxn .gt_indent_5 { text-indent: calc(5px * 5); }
 #ykuyzngwxn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ykuyzngwxn .gt_row_group_first td { border-top-width: 2px; }
 #ykuyzngwxn .gt_row_group_first th { border-top-width: 2px; }
 #ykuyzngwxn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ykuyzngwxn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ykuyzngwxn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ykuyzngwxn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ykuyzngwxn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ykuyzngwxn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ykuyzngwxn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ykuyzngwxn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ykuyzngwxn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ykuyzngwxn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ykuyzngwxn .gt_left { text-align: left; }
 #ykuyzngwxn .gt_center { text-align: center; }
 #ykuyzngwxn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ykuyzngwxn .gt_font_normal { font-weight: normal; }
 #ykuyzngwxn .gt_font_bold { font-weight: bold; }
 #ykuyzngwxn .gt_font_italic { font-style: italic; }
 #ykuyzngwxn .gt_super { font-size: 65%; }
 #ykuyzngwxn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ykuyzngwxn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ykuyzngwxn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ykuyzngwxn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ykuyzngwxn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ykuyzngwxn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xltfmejety table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xltfmejety thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xltfmejety p { margin: 0; padding: 0; }
 #xltfmejety .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xltfmejety .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xltfmejety .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xltfmejety .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xltfmejety .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xltfmejety .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xltfmejety .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xltfmejety .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xltfmejety .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xltfmejety .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xltfmejety .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xltfmejety .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xltfmejety .gt_spanner_row { border-bottom-style: hidden; }
 #xltfmejety .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xltfmejety .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xltfmejety .gt_from_md> :first-child { margin-top: 0; }
 #xltfmejety .gt_from_md> :last-child { margin-bottom: 0; }
 #xltfmejety .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xltfmejety .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xltfmejety .gt_indent_1 { text-indent: 5px; }
 #xltfmejety .gt_indent_2 { text-indent: calc(5px * 2); }
 #xltfmejety .gt_indent_3 { text-indent: calc(5px * 3); }
 #xltfmejety .gt_indent_4 { text-indent: calc(5px * 4); }
 #xltfmejety .gt_indent_5 { text-indent: calc(5px * 5); }
 #xltfmejety .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xltfmejety .gt_row_group_first td { border-top-width: 2px; }
 #xltfmejety .gt_row_group_first th { border-top-width: 2px; }
 #xltfmejety .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xltfmejety .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xltfmejety .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xltfmejety .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xltfmejety .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xltfmejety .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xltfmejety .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xltfmejety .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xltfmejety .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xltfmejety .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xltfmejety .gt_left { text-align: left; }
 #xltfmejety .gt_center { text-align: center; }
 #xltfmejety .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xltfmejety .gt_font_normal { font-weight: normal; }
 #xltfmejety .gt_font_bold { font-weight: bold; }
 #xltfmejety .gt_font_italic { font-style: italic; }
 #xltfmejety .gt_super { font-size: 65%; }
 #xltfmejety .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xltfmejety .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xltfmejety .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xltfmejety .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xltfmejety .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xltfmejety .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | status      | priority | progress |
|-----------------|-------------|----------|----------|
| Data collection | Complete    | High ●   | 100      |
| Analysis        | In Progress | High ●   | 65       |
| Report writing  | Not Started | Medium ● | 0        |
| Peer review     | Complete    | Low ●    | 100      |


The text transformation methods provide a final layer of control over how your table content appears. Whether you need simple find-and-replace, switch-like mappings, or complex conditional logic, these methods let you shape the text to match your exact presentation needs.
