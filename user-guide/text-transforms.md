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
#soytjygdvy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#soytjygdvy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#soytjygdvy p { margin: 0; padding: 0; }
 #soytjygdvy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #soytjygdvy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #soytjygdvy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #soytjygdvy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #soytjygdvy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #soytjygdvy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #soytjygdvy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #soytjygdvy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #soytjygdvy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #soytjygdvy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #soytjygdvy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #soytjygdvy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #soytjygdvy .gt_spanner_row { border-bottom-style: hidden; }
 #soytjygdvy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #soytjygdvy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #soytjygdvy .gt_from_md> :first-child { margin-top: 0; }
 #soytjygdvy .gt_from_md> :last-child { margin-bottom: 0; }
 #soytjygdvy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #soytjygdvy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #soytjygdvy .gt_indent_1 { text-indent: 5px; }
 #soytjygdvy .gt_indent_2 { text-indent: calc(5px * 2); }
 #soytjygdvy .gt_indent_3 { text-indent: calc(5px * 3); }
 #soytjygdvy .gt_indent_4 { text-indent: calc(5px * 4); }
 #soytjygdvy .gt_indent_5 { text-indent: calc(5px * 5); }
 #soytjygdvy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #soytjygdvy .gt_row_group_first td { border-top-width: 2px; }
 #soytjygdvy .gt_row_group_first th { border-top-width: 2px; }
 #soytjygdvy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #soytjygdvy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #soytjygdvy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #soytjygdvy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #soytjygdvy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #soytjygdvy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #soytjygdvy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #soytjygdvy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #soytjygdvy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #soytjygdvy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #soytjygdvy .gt_left { text-align: left; }
 #soytjygdvy .gt_center { text-align: center; }
 #soytjygdvy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #soytjygdvy .gt_font_normal { font-weight: normal; }
 #soytjygdvy .gt_font_bold { font-weight: bold; }
 #soytjygdvy .gt_font_italic { font-style: italic; }
 #soytjygdvy .gt_super { font-size: 65%; }
 #soytjygdvy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #soytjygdvy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #soytjygdvy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #soytjygdvy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #soytjygdvy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #soytjygdvy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xnvdblhgrl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xnvdblhgrl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xnvdblhgrl p { margin: 0; padding: 0; }
 #xnvdblhgrl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xnvdblhgrl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xnvdblhgrl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xnvdblhgrl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xnvdblhgrl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xnvdblhgrl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xnvdblhgrl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xnvdblhgrl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xnvdblhgrl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xnvdblhgrl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xnvdblhgrl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xnvdblhgrl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xnvdblhgrl .gt_spanner_row { border-bottom-style: hidden; }
 #xnvdblhgrl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xnvdblhgrl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xnvdblhgrl .gt_from_md> :first-child { margin-top: 0; }
 #xnvdblhgrl .gt_from_md> :last-child { margin-bottom: 0; }
 #xnvdblhgrl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xnvdblhgrl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xnvdblhgrl .gt_indent_1 { text-indent: 5px; }
 #xnvdblhgrl .gt_indent_2 { text-indent: calc(5px * 2); }
 #xnvdblhgrl .gt_indent_3 { text-indent: calc(5px * 3); }
 #xnvdblhgrl .gt_indent_4 { text-indent: calc(5px * 4); }
 #xnvdblhgrl .gt_indent_5 { text-indent: calc(5px * 5); }
 #xnvdblhgrl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xnvdblhgrl .gt_row_group_first td { border-top-width: 2px; }
 #xnvdblhgrl .gt_row_group_first th { border-top-width: 2px; }
 #xnvdblhgrl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xnvdblhgrl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xnvdblhgrl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xnvdblhgrl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xnvdblhgrl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xnvdblhgrl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xnvdblhgrl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xnvdblhgrl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xnvdblhgrl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xnvdblhgrl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xnvdblhgrl .gt_left { text-align: left; }
 #xnvdblhgrl .gt_center { text-align: center; }
 #xnvdblhgrl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xnvdblhgrl .gt_font_normal { font-weight: normal; }
 #xnvdblhgrl .gt_font_bold { font-weight: bold; }
 #xnvdblhgrl .gt_font_italic { font-style: italic; }
 #xnvdblhgrl .gt_super { font-size: 65%; }
 #xnvdblhgrl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xnvdblhgrl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xnvdblhgrl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xnvdblhgrl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xnvdblhgrl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xnvdblhgrl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pcfjczbxjb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pcfjczbxjb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pcfjczbxjb p { margin: 0; padding: 0; }
 #pcfjczbxjb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pcfjczbxjb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pcfjczbxjb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pcfjczbxjb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pcfjczbxjb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pcfjczbxjb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pcfjczbxjb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pcfjczbxjb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pcfjczbxjb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pcfjczbxjb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pcfjczbxjb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pcfjczbxjb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pcfjczbxjb .gt_spanner_row { border-bottom-style: hidden; }
 #pcfjczbxjb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pcfjczbxjb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pcfjczbxjb .gt_from_md> :first-child { margin-top: 0; }
 #pcfjczbxjb .gt_from_md> :last-child { margin-bottom: 0; }
 #pcfjczbxjb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pcfjczbxjb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pcfjczbxjb .gt_indent_1 { text-indent: 5px; }
 #pcfjczbxjb .gt_indent_2 { text-indent: calc(5px * 2); }
 #pcfjczbxjb .gt_indent_3 { text-indent: calc(5px * 3); }
 #pcfjczbxjb .gt_indent_4 { text-indent: calc(5px * 4); }
 #pcfjczbxjb .gt_indent_5 { text-indent: calc(5px * 5); }
 #pcfjczbxjb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pcfjczbxjb .gt_row_group_first td { border-top-width: 2px; }
 #pcfjczbxjb .gt_row_group_first th { border-top-width: 2px; }
 #pcfjczbxjb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pcfjczbxjb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pcfjczbxjb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pcfjczbxjb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pcfjczbxjb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pcfjczbxjb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pcfjczbxjb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pcfjczbxjb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pcfjczbxjb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pcfjczbxjb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pcfjczbxjb .gt_left { text-align: left; }
 #pcfjczbxjb .gt_center { text-align: center; }
 #pcfjczbxjb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pcfjczbxjb .gt_font_normal { font-weight: normal; }
 #pcfjczbxjb .gt_font_bold { font-weight: bold; }
 #pcfjczbxjb .gt_font_italic { font-style: italic; }
 #pcfjczbxjb .gt_super { font-size: 65%; }
 #pcfjczbxjb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pcfjczbxjb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pcfjczbxjb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pcfjczbxjb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pcfjczbxjb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pcfjczbxjb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tewroszqyg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tewroszqyg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tewroszqyg p { margin: 0; padding: 0; }
 #tewroszqyg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tewroszqyg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tewroszqyg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tewroszqyg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tewroszqyg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tewroszqyg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tewroszqyg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tewroszqyg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tewroszqyg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tewroszqyg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tewroszqyg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tewroszqyg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tewroszqyg .gt_spanner_row { border-bottom-style: hidden; }
 #tewroszqyg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tewroszqyg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tewroszqyg .gt_from_md> :first-child { margin-top: 0; }
 #tewroszqyg .gt_from_md> :last-child { margin-bottom: 0; }
 #tewroszqyg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tewroszqyg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tewroszqyg .gt_indent_1 { text-indent: 5px; }
 #tewroszqyg .gt_indent_2 { text-indent: calc(5px * 2); }
 #tewroszqyg .gt_indent_3 { text-indent: calc(5px * 3); }
 #tewroszqyg .gt_indent_4 { text-indent: calc(5px * 4); }
 #tewroszqyg .gt_indent_5 { text-indent: calc(5px * 5); }
 #tewroszqyg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tewroszqyg .gt_row_group_first td { border-top-width: 2px; }
 #tewroszqyg .gt_row_group_first th { border-top-width: 2px; }
 #tewroszqyg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tewroszqyg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tewroszqyg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tewroszqyg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tewroszqyg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tewroszqyg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tewroszqyg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tewroszqyg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tewroszqyg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tewroszqyg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tewroszqyg .gt_left { text-align: left; }
 #tewroszqyg .gt_center { text-align: center; }
 #tewroszqyg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tewroszqyg .gt_font_normal { font-weight: normal; }
 #tewroszqyg .gt_font_bold { font-weight: bold; }
 #tewroszqyg .gt_font_italic { font-style: italic; }
 #tewroszqyg .gt_super { font-size: 65%; }
 #tewroszqyg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tewroszqyg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tewroszqyg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tewroszqyg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tewroszqyg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tewroszqyg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xuvlwnokdd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xuvlwnokdd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xuvlwnokdd p { margin: 0; padding: 0; }
 #xuvlwnokdd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xuvlwnokdd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xuvlwnokdd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xuvlwnokdd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xuvlwnokdd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xuvlwnokdd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xuvlwnokdd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xuvlwnokdd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xuvlwnokdd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xuvlwnokdd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xuvlwnokdd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xuvlwnokdd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xuvlwnokdd .gt_spanner_row { border-bottom-style: hidden; }
 #xuvlwnokdd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xuvlwnokdd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xuvlwnokdd .gt_from_md> :first-child { margin-top: 0; }
 #xuvlwnokdd .gt_from_md> :last-child { margin-bottom: 0; }
 #xuvlwnokdd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xuvlwnokdd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xuvlwnokdd .gt_indent_1 { text-indent: 5px; }
 #xuvlwnokdd .gt_indent_2 { text-indent: calc(5px * 2); }
 #xuvlwnokdd .gt_indent_3 { text-indent: calc(5px * 3); }
 #xuvlwnokdd .gt_indent_4 { text-indent: calc(5px * 4); }
 #xuvlwnokdd .gt_indent_5 { text-indent: calc(5px * 5); }
 #xuvlwnokdd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xuvlwnokdd .gt_row_group_first td { border-top-width: 2px; }
 #xuvlwnokdd .gt_row_group_first th { border-top-width: 2px; }
 #xuvlwnokdd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xuvlwnokdd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xuvlwnokdd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xuvlwnokdd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xuvlwnokdd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xuvlwnokdd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xuvlwnokdd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xuvlwnokdd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xuvlwnokdd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xuvlwnokdd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xuvlwnokdd .gt_left { text-align: left; }
 #xuvlwnokdd .gt_center { text-align: center; }
 #xuvlwnokdd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xuvlwnokdd .gt_font_normal { font-weight: normal; }
 #xuvlwnokdd .gt_font_bold { font-weight: bold; }
 #xuvlwnokdd .gt_font_italic { font-style: italic; }
 #xuvlwnokdd .gt_super { font-size: 65%; }
 #xuvlwnokdd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xuvlwnokdd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xuvlwnokdd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xuvlwnokdd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xuvlwnokdd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xuvlwnokdd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zsvoannyet table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zsvoannyet thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zsvoannyet p { margin: 0; padding: 0; }
 #zsvoannyet .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zsvoannyet .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zsvoannyet .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zsvoannyet .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zsvoannyet .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zsvoannyet .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zsvoannyet .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zsvoannyet .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zsvoannyet .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zsvoannyet .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zsvoannyet .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zsvoannyet .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zsvoannyet .gt_spanner_row { border-bottom-style: hidden; }
 #zsvoannyet .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zsvoannyet .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zsvoannyet .gt_from_md> :first-child { margin-top: 0; }
 #zsvoannyet .gt_from_md> :last-child { margin-bottom: 0; }
 #zsvoannyet .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zsvoannyet .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zsvoannyet .gt_indent_1 { text-indent: 5px; }
 #zsvoannyet .gt_indent_2 { text-indent: calc(5px * 2); }
 #zsvoannyet .gt_indent_3 { text-indent: calc(5px * 3); }
 #zsvoannyet .gt_indent_4 { text-indent: calc(5px * 4); }
 #zsvoannyet .gt_indent_5 { text-indent: calc(5px * 5); }
 #zsvoannyet .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zsvoannyet .gt_row_group_first td { border-top-width: 2px; }
 #zsvoannyet .gt_row_group_first th { border-top-width: 2px; }
 #zsvoannyet .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zsvoannyet .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zsvoannyet .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zsvoannyet .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zsvoannyet .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zsvoannyet .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zsvoannyet .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zsvoannyet .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zsvoannyet .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zsvoannyet .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zsvoannyet .gt_left { text-align: left; }
 #zsvoannyet .gt_center { text-align: center; }
 #zsvoannyet .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zsvoannyet .gt_font_normal { font-weight: normal; }
 #zsvoannyet .gt_font_bold { font-weight: bold; }
 #zsvoannyet .gt_font_italic { font-style: italic; }
 #zsvoannyet .gt_super { font-size: 65%; }
 #zsvoannyet .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zsvoannyet .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zsvoannyet .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zsvoannyet .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zsvoannyet .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zsvoannyet .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#epfoercvev table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#epfoercvev thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#epfoercvev p { margin: 0; padding: 0; }
 #epfoercvev .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #epfoercvev .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #epfoercvev .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #epfoercvev .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #epfoercvev .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #epfoercvev .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #epfoercvev .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #epfoercvev .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #epfoercvev .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #epfoercvev .gt_column_spanner_outer:first-child { padding-left: 0; }
 #epfoercvev .gt_column_spanner_outer:last-child { padding-right: 0; }
 #epfoercvev .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #epfoercvev .gt_spanner_row { border-bottom-style: hidden; }
 #epfoercvev .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #epfoercvev .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #epfoercvev .gt_from_md> :first-child { margin-top: 0; }
 #epfoercvev .gt_from_md> :last-child { margin-bottom: 0; }
 #epfoercvev .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #epfoercvev .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #epfoercvev .gt_indent_1 { text-indent: 5px; }
 #epfoercvev .gt_indent_2 { text-indent: calc(5px * 2); }
 #epfoercvev .gt_indent_3 { text-indent: calc(5px * 3); }
 #epfoercvev .gt_indent_4 { text-indent: calc(5px * 4); }
 #epfoercvev .gt_indent_5 { text-indent: calc(5px * 5); }
 #epfoercvev .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #epfoercvev .gt_row_group_first td { border-top-width: 2px; }
 #epfoercvev .gt_row_group_first th { border-top-width: 2px; }
 #epfoercvev .gt_striped { color: #333333; background-color: #F4F4F4; }
 #epfoercvev .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #epfoercvev .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #epfoercvev .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #epfoercvev .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #epfoercvev .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #epfoercvev .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #epfoercvev .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #epfoercvev .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #epfoercvev .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #epfoercvev .gt_left { text-align: left; }
 #epfoercvev .gt_center { text-align: center; }
 #epfoercvev .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #epfoercvev .gt_font_normal { font-weight: normal; }
 #epfoercvev .gt_font_bold { font-weight: bold; }
 #epfoercvev .gt_font_italic { font-style: italic; }
 #epfoercvev .gt_super { font-size: 65%; }
 #epfoercvev .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #epfoercvev .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #epfoercvev .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #epfoercvev .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #epfoercvev .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #epfoercvev .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qefpwqpbtd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qefpwqpbtd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qefpwqpbtd p { margin: 0; padding: 0; }
 #qefpwqpbtd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qefpwqpbtd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qefpwqpbtd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qefpwqpbtd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qefpwqpbtd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qefpwqpbtd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qefpwqpbtd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qefpwqpbtd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qefpwqpbtd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qefpwqpbtd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qefpwqpbtd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qefpwqpbtd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qefpwqpbtd .gt_spanner_row { border-bottom-style: hidden; }
 #qefpwqpbtd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qefpwqpbtd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qefpwqpbtd .gt_from_md> :first-child { margin-top: 0; }
 #qefpwqpbtd .gt_from_md> :last-child { margin-bottom: 0; }
 #qefpwqpbtd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qefpwqpbtd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qefpwqpbtd .gt_indent_1 { text-indent: 5px; }
 #qefpwqpbtd .gt_indent_2 { text-indent: calc(5px * 2); }
 #qefpwqpbtd .gt_indent_3 { text-indent: calc(5px * 3); }
 #qefpwqpbtd .gt_indent_4 { text-indent: calc(5px * 4); }
 #qefpwqpbtd .gt_indent_5 { text-indent: calc(5px * 5); }
 #qefpwqpbtd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qefpwqpbtd .gt_row_group_first td { border-top-width: 2px; }
 #qefpwqpbtd .gt_row_group_first th { border-top-width: 2px; }
 #qefpwqpbtd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qefpwqpbtd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qefpwqpbtd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qefpwqpbtd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qefpwqpbtd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qefpwqpbtd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qefpwqpbtd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qefpwqpbtd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qefpwqpbtd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qefpwqpbtd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qefpwqpbtd .gt_left { text-align: left; }
 #qefpwqpbtd .gt_center { text-align: center; }
 #qefpwqpbtd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qefpwqpbtd .gt_font_normal { font-weight: normal; }
 #qefpwqpbtd .gt_font_bold { font-weight: bold; }
 #qefpwqpbtd .gt_font_italic { font-style: italic; }
 #qefpwqpbtd .gt_super { font-size: 65%; }
 #qefpwqpbtd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qefpwqpbtd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qefpwqpbtd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qefpwqpbtd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qefpwqpbtd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qefpwqpbtd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rbbcddkyhf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rbbcddkyhf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rbbcddkyhf p { margin: 0; padding: 0; }
 #rbbcddkyhf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rbbcddkyhf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rbbcddkyhf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rbbcddkyhf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rbbcddkyhf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rbbcddkyhf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rbbcddkyhf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rbbcddkyhf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rbbcddkyhf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rbbcddkyhf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rbbcddkyhf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rbbcddkyhf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rbbcddkyhf .gt_spanner_row { border-bottom-style: hidden; }
 #rbbcddkyhf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rbbcddkyhf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rbbcddkyhf .gt_from_md> :first-child { margin-top: 0; }
 #rbbcddkyhf .gt_from_md> :last-child { margin-bottom: 0; }
 #rbbcddkyhf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rbbcddkyhf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rbbcddkyhf .gt_indent_1 { text-indent: 5px; }
 #rbbcddkyhf .gt_indent_2 { text-indent: calc(5px * 2); }
 #rbbcddkyhf .gt_indent_3 { text-indent: calc(5px * 3); }
 #rbbcddkyhf .gt_indent_4 { text-indent: calc(5px * 4); }
 #rbbcddkyhf .gt_indent_5 { text-indent: calc(5px * 5); }
 #rbbcddkyhf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rbbcddkyhf .gt_row_group_first td { border-top-width: 2px; }
 #rbbcddkyhf .gt_row_group_first th { border-top-width: 2px; }
 #rbbcddkyhf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rbbcddkyhf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rbbcddkyhf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rbbcddkyhf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rbbcddkyhf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rbbcddkyhf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rbbcddkyhf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rbbcddkyhf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rbbcddkyhf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rbbcddkyhf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rbbcddkyhf .gt_left { text-align: left; }
 #rbbcddkyhf .gt_center { text-align: center; }
 #rbbcddkyhf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rbbcddkyhf .gt_font_normal { font-weight: normal; }
 #rbbcddkyhf .gt_font_bold { font-weight: bold; }
 #rbbcddkyhf .gt_font_italic { font-style: italic; }
 #rbbcddkyhf .gt_super { font-size: 65%; }
 #rbbcddkyhf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rbbcddkyhf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rbbcddkyhf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rbbcddkyhf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rbbcddkyhf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rbbcddkyhf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wmtqqnkmzp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wmtqqnkmzp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wmtqqnkmzp p { margin: 0; padding: 0; }
 #wmtqqnkmzp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wmtqqnkmzp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wmtqqnkmzp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wmtqqnkmzp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wmtqqnkmzp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wmtqqnkmzp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wmtqqnkmzp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wmtqqnkmzp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wmtqqnkmzp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wmtqqnkmzp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wmtqqnkmzp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wmtqqnkmzp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wmtqqnkmzp .gt_spanner_row { border-bottom-style: hidden; }
 #wmtqqnkmzp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wmtqqnkmzp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wmtqqnkmzp .gt_from_md> :first-child { margin-top: 0; }
 #wmtqqnkmzp .gt_from_md> :last-child { margin-bottom: 0; }
 #wmtqqnkmzp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wmtqqnkmzp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wmtqqnkmzp .gt_indent_1 { text-indent: 5px; }
 #wmtqqnkmzp .gt_indent_2 { text-indent: calc(5px * 2); }
 #wmtqqnkmzp .gt_indent_3 { text-indent: calc(5px * 3); }
 #wmtqqnkmzp .gt_indent_4 { text-indent: calc(5px * 4); }
 #wmtqqnkmzp .gt_indent_5 { text-indent: calc(5px * 5); }
 #wmtqqnkmzp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wmtqqnkmzp .gt_row_group_first td { border-top-width: 2px; }
 #wmtqqnkmzp .gt_row_group_first th { border-top-width: 2px; }
 #wmtqqnkmzp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wmtqqnkmzp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wmtqqnkmzp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wmtqqnkmzp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wmtqqnkmzp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wmtqqnkmzp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wmtqqnkmzp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wmtqqnkmzp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wmtqqnkmzp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wmtqqnkmzp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wmtqqnkmzp .gt_left { text-align: left; }
 #wmtqqnkmzp .gt_center { text-align: center; }
 #wmtqqnkmzp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wmtqqnkmzp .gt_font_normal { font-weight: normal; }
 #wmtqqnkmzp .gt_font_bold { font-weight: bold; }
 #wmtqqnkmzp .gt_font_italic { font-style: italic; }
 #wmtqqnkmzp .gt_super { font-size: 65%; }
 #wmtqqnkmzp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wmtqqnkmzp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wmtqqnkmzp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wmtqqnkmzp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wmtqqnkmzp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wmtqqnkmzp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vcmkdcmxko table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vcmkdcmxko thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vcmkdcmxko p { margin: 0; padding: 0; }
 #vcmkdcmxko .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vcmkdcmxko .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vcmkdcmxko .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vcmkdcmxko .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vcmkdcmxko .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vcmkdcmxko .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vcmkdcmxko .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vcmkdcmxko .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vcmkdcmxko .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vcmkdcmxko .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vcmkdcmxko .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vcmkdcmxko .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vcmkdcmxko .gt_spanner_row { border-bottom-style: hidden; }
 #vcmkdcmxko .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vcmkdcmxko .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vcmkdcmxko .gt_from_md> :first-child { margin-top: 0; }
 #vcmkdcmxko .gt_from_md> :last-child { margin-bottom: 0; }
 #vcmkdcmxko .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vcmkdcmxko .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vcmkdcmxko .gt_indent_1 { text-indent: 5px; }
 #vcmkdcmxko .gt_indent_2 { text-indent: calc(5px * 2); }
 #vcmkdcmxko .gt_indent_3 { text-indent: calc(5px * 3); }
 #vcmkdcmxko .gt_indent_4 { text-indent: calc(5px * 4); }
 #vcmkdcmxko .gt_indent_5 { text-indent: calc(5px * 5); }
 #vcmkdcmxko .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vcmkdcmxko .gt_row_group_first td { border-top-width: 2px; }
 #vcmkdcmxko .gt_row_group_first th { border-top-width: 2px; }
 #vcmkdcmxko .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vcmkdcmxko .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vcmkdcmxko .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vcmkdcmxko .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vcmkdcmxko .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vcmkdcmxko .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vcmkdcmxko .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vcmkdcmxko .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vcmkdcmxko .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vcmkdcmxko .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vcmkdcmxko .gt_left { text-align: left; }
 #vcmkdcmxko .gt_center { text-align: center; }
 #vcmkdcmxko .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vcmkdcmxko .gt_font_normal { font-weight: normal; }
 #vcmkdcmxko .gt_font_bold { font-weight: bold; }
 #vcmkdcmxko .gt_font_italic { font-style: italic; }
 #vcmkdcmxko .gt_super { font-size: 65%; }
 #vcmkdcmxko .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vcmkdcmxko .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vcmkdcmxko .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vcmkdcmxko .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vcmkdcmxko .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vcmkdcmxko .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#khttwrumic table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#khttwrumic thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#khttwrumic p { margin: 0; padding: 0; }
 #khttwrumic .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #khttwrumic .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #khttwrumic .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #khttwrumic .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #khttwrumic .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #khttwrumic .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khttwrumic .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #khttwrumic .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #khttwrumic .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #khttwrumic .gt_column_spanner_outer:first-child { padding-left: 0; }
 #khttwrumic .gt_column_spanner_outer:last-child { padding-right: 0; }
 #khttwrumic .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #khttwrumic .gt_spanner_row { border-bottom-style: hidden; }
 #khttwrumic .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #khttwrumic .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #khttwrumic .gt_from_md> :first-child { margin-top: 0; }
 #khttwrumic .gt_from_md> :last-child { margin-bottom: 0; }
 #khttwrumic .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #khttwrumic .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #khttwrumic .gt_indent_1 { text-indent: 5px; }
 #khttwrumic .gt_indent_2 { text-indent: calc(5px * 2); }
 #khttwrumic .gt_indent_3 { text-indent: calc(5px * 3); }
 #khttwrumic .gt_indent_4 { text-indent: calc(5px * 4); }
 #khttwrumic .gt_indent_5 { text-indent: calc(5px * 5); }
 #khttwrumic .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #khttwrumic .gt_row_group_first td { border-top-width: 2px; }
 #khttwrumic .gt_row_group_first th { border-top-width: 2px; }
 #khttwrumic .gt_striped { color: #333333; background-color: #F4F4F4; }
 #khttwrumic .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khttwrumic .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #khttwrumic .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #khttwrumic .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khttwrumic .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #khttwrumic .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #khttwrumic .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #khttwrumic .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khttwrumic .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #khttwrumic .gt_left { text-align: left; }
 #khttwrumic .gt_center { text-align: center; }
 #khttwrumic .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #khttwrumic .gt_font_normal { font-weight: normal; }
 #khttwrumic .gt_font_bold { font-weight: bold; }
 #khttwrumic .gt_font_italic { font-style: italic; }
 #khttwrumic .gt_super { font-size: 65%; }
 #khttwrumic .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khttwrumic .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #khttwrumic .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khttwrumic .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #khttwrumic .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #khttwrumic .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | status      | priority | progress |
|-----------------|-------------|----------|----------|
| Data collection | Complete    | High ●   | 100      |
| Analysis        | In Progress | High ●   | 65       |
| Report writing  | Not Started | Medium ● | 0        |
| Peer review     | Complete    | Low ●    | 100      |


The text transformation methods provide a final layer of control over how your table content appears. Whether you need simple find-and-replace, switch-like mappings, or complex conditional logic, these methods let you shape the text to match your exact presentation needs.
