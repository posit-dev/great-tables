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
#mtcoymbdbt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mtcoymbdbt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mtcoymbdbt p { margin: 0; padding: 0; }
 #mtcoymbdbt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mtcoymbdbt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mtcoymbdbt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mtcoymbdbt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mtcoymbdbt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mtcoymbdbt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mtcoymbdbt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mtcoymbdbt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mtcoymbdbt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mtcoymbdbt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mtcoymbdbt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mtcoymbdbt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mtcoymbdbt .gt_spanner_row { border-bottom-style: hidden; }
 #mtcoymbdbt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mtcoymbdbt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mtcoymbdbt .gt_from_md> :first-child { margin-top: 0; }
 #mtcoymbdbt .gt_from_md> :last-child { margin-bottom: 0; }
 #mtcoymbdbt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mtcoymbdbt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mtcoymbdbt .gt_indent_1 { text-indent: 5px; }
 #mtcoymbdbt .gt_indent_2 { text-indent: calc(5px * 2); }
 #mtcoymbdbt .gt_indent_3 { text-indent: calc(5px * 3); }
 #mtcoymbdbt .gt_indent_4 { text-indent: calc(5px * 4); }
 #mtcoymbdbt .gt_indent_5 { text-indent: calc(5px * 5); }
 #mtcoymbdbt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mtcoymbdbt .gt_row_group_first td { border-top-width: 2px; }
 #mtcoymbdbt .gt_row_group_first th { border-top-width: 2px; }
 #mtcoymbdbt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mtcoymbdbt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mtcoymbdbt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mtcoymbdbt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mtcoymbdbt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mtcoymbdbt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mtcoymbdbt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mtcoymbdbt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mtcoymbdbt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mtcoymbdbt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mtcoymbdbt .gt_left { text-align: left; }
 #mtcoymbdbt .gt_center { text-align: center; }
 #mtcoymbdbt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mtcoymbdbt .gt_font_normal { font-weight: normal; }
 #mtcoymbdbt .gt_font_bold { font-weight: bold; }
 #mtcoymbdbt .gt_font_italic { font-style: italic; }
 #mtcoymbdbt .gt_super { font-size: 65%; }
 #mtcoymbdbt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mtcoymbdbt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mtcoymbdbt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mtcoymbdbt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mtcoymbdbt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mtcoymbdbt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ndgfwrgyjk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ndgfwrgyjk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ndgfwrgyjk p { margin: 0; padding: 0; }
 #ndgfwrgyjk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ndgfwrgyjk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ndgfwrgyjk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ndgfwrgyjk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ndgfwrgyjk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ndgfwrgyjk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ndgfwrgyjk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ndgfwrgyjk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ndgfwrgyjk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ndgfwrgyjk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ndgfwrgyjk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ndgfwrgyjk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ndgfwrgyjk .gt_spanner_row { border-bottom-style: hidden; }
 #ndgfwrgyjk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ndgfwrgyjk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ndgfwrgyjk .gt_from_md> :first-child { margin-top: 0; }
 #ndgfwrgyjk .gt_from_md> :last-child { margin-bottom: 0; }
 #ndgfwrgyjk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ndgfwrgyjk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ndgfwrgyjk .gt_indent_1 { text-indent: 5px; }
 #ndgfwrgyjk .gt_indent_2 { text-indent: calc(5px * 2); }
 #ndgfwrgyjk .gt_indent_3 { text-indent: calc(5px * 3); }
 #ndgfwrgyjk .gt_indent_4 { text-indent: calc(5px * 4); }
 #ndgfwrgyjk .gt_indent_5 { text-indent: calc(5px * 5); }
 #ndgfwrgyjk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ndgfwrgyjk .gt_row_group_first td { border-top-width: 2px; }
 #ndgfwrgyjk .gt_row_group_first th { border-top-width: 2px; }
 #ndgfwrgyjk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ndgfwrgyjk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ndgfwrgyjk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ndgfwrgyjk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ndgfwrgyjk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ndgfwrgyjk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ndgfwrgyjk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ndgfwrgyjk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ndgfwrgyjk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ndgfwrgyjk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ndgfwrgyjk .gt_left { text-align: left; }
 #ndgfwrgyjk .gt_center { text-align: center; }
 #ndgfwrgyjk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ndgfwrgyjk .gt_font_normal { font-weight: normal; }
 #ndgfwrgyjk .gt_font_bold { font-weight: bold; }
 #ndgfwrgyjk .gt_font_italic { font-style: italic; }
 #ndgfwrgyjk .gt_super { font-size: 65%; }
 #ndgfwrgyjk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ndgfwrgyjk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ndgfwrgyjk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ndgfwrgyjk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ndgfwrgyjk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ndgfwrgyjk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xkqwomcstn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xkqwomcstn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xkqwomcstn p { margin: 0; padding: 0; }
 #xkqwomcstn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xkqwomcstn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xkqwomcstn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xkqwomcstn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xkqwomcstn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xkqwomcstn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xkqwomcstn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xkqwomcstn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xkqwomcstn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xkqwomcstn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xkqwomcstn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xkqwomcstn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xkqwomcstn .gt_spanner_row { border-bottom-style: hidden; }
 #xkqwomcstn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xkqwomcstn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xkqwomcstn .gt_from_md> :first-child { margin-top: 0; }
 #xkqwomcstn .gt_from_md> :last-child { margin-bottom: 0; }
 #xkqwomcstn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xkqwomcstn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xkqwomcstn .gt_indent_1 { text-indent: 5px; }
 #xkqwomcstn .gt_indent_2 { text-indent: calc(5px * 2); }
 #xkqwomcstn .gt_indent_3 { text-indent: calc(5px * 3); }
 #xkqwomcstn .gt_indent_4 { text-indent: calc(5px * 4); }
 #xkqwomcstn .gt_indent_5 { text-indent: calc(5px * 5); }
 #xkqwomcstn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xkqwomcstn .gt_row_group_first td { border-top-width: 2px; }
 #xkqwomcstn .gt_row_group_first th { border-top-width: 2px; }
 #xkqwomcstn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xkqwomcstn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xkqwomcstn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xkqwomcstn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xkqwomcstn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xkqwomcstn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xkqwomcstn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xkqwomcstn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xkqwomcstn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xkqwomcstn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xkqwomcstn .gt_left { text-align: left; }
 #xkqwomcstn .gt_center { text-align: center; }
 #xkqwomcstn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xkqwomcstn .gt_font_normal { font-weight: normal; }
 #xkqwomcstn .gt_font_bold { font-weight: bold; }
 #xkqwomcstn .gt_font_italic { font-style: italic; }
 #xkqwomcstn .gt_super { font-size: 65%; }
 #xkqwomcstn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xkqwomcstn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xkqwomcstn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xkqwomcstn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xkqwomcstn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xkqwomcstn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jlrossyqqm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jlrossyqqm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jlrossyqqm p { margin: 0; padding: 0; }
 #jlrossyqqm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jlrossyqqm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jlrossyqqm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jlrossyqqm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jlrossyqqm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jlrossyqqm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jlrossyqqm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jlrossyqqm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jlrossyqqm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jlrossyqqm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jlrossyqqm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jlrossyqqm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jlrossyqqm .gt_spanner_row { border-bottom-style: hidden; }
 #jlrossyqqm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jlrossyqqm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jlrossyqqm .gt_from_md> :first-child { margin-top: 0; }
 #jlrossyqqm .gt_from_md> :last-child { margin-bottom: 0; }
 #jlrossyqqm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jlrossyqqm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jlrossyqqm .gt_indent_1 { text-indent: 5px; }
 #jlrossyqqm .gt_indent_2 { text-indent: calc(5px * 2); }
 #jlrossyqqm .gt_indent_3 { text-indent: calc(5px * 3); }
 #jlrossyqqm .gt_indent_4 { text-indent: calc(5px * 4); }
 #jlrossyqqm .gt_indent_5 { text-indent: calc(5px * 5); }
 #jlrossyqqm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jlrossyqqm .gt_row_group_first td { border-top-width: 2px; }
 #jlrossyqqm .gt_row_group_first th { border-top-width: 2px; }
 #jlrossyqqm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jlrossyqqm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jlrossyqqm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jlrossyqqm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jlrossyqqm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jlrossyqqm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jlrossyqqm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jlrossyqqm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jlrossyqqm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jlrossyqqm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jlrossyqqm .gt_left { text-align: left; }
 #jlrossyqqm .gt_center { text-align: center; }
 #jlrossyqqm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jlrossyqqm .gt_font_normal { font-weight: normal; }
 #jlrossyqqm .gt_font_bold { font-weight: bold; }
 #jlrossyqqm .gt_font_italic { font-style: italic; }
 #jlrossyqqm .gt_super { font-size: 65%; }
 #jlrossyqqm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jlrossyqqm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jlrossyqqm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jlrossyqqm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jlrossyqqm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jlrossyqqm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bpmjduvqva table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bpmjduvqva thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bpmjduvqva p { margin: 0; padding: 0; }
 #bpmjduvqva .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bpmjduvqva .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bpmjduvqva .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bpmjduvqva .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bpmjduvqva .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bpmjduvqva .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpmjduvqva .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bpmjduvqva .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bpmjduvqva .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bpmjduvqva .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bpmjduvqva .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bpmjduvqva .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bpmjduvqva .gt_spanner_row { border-bottom-style: hidden; }
 #bpmjduvqva .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bpmjduvqva .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bpmjduvqva .gt_from_md> :first-child { margin-top: 0; }
 #bpmjduvqva .gt_from_md> :last-child { margin-bottom: 0; }
 #bpmjduvqva .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bpmjduvqva .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bpmjduvqva .gt_indent_1 { text-indent: 5px; }
 #bpmjduvqva .gt_indent_2 { text-indent: calc(5px * 2); }
 #bpmjduvqva .gt_indent_3 { text-indent: calc(5px * 3); }
 #bpmjduvqva .gt_indent_4 { text-indent: calc(5px * 4); }
 #bpmjduvqva .gt_indent_5 { text-indent: calc(5px * 5); }
 #bpmjduvqva .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bpmjduvqva .gt_row_group_first td { border-top-width: 2px; }
 #bpmjduvqva .gt_row_group_first th { border-top-width: 2px; }
 #bpmjduvqva .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bpmjduvqva .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpmjduvqva .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bpmjduvqva .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bpmjduvqva .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bpmjduvqva .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bpmjduvqva .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bpmjduvqva .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bpmjduvqva .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpmjduvqva .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bpmjduvqva .gt_left { text-align: left; }
 #bpmjduvqva .gt_center { text-align: center; }
 #bpmjduvqva .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bpmjduvqva .gt_font_normal { font-weight: normal; }
 #bpmjduvqva .gt_font_bold { font-weight: bold; }
 #bpmjduvqva .gt_font_italic { font-style: italic; }
 #bpmjduvqva .gt_super { font-size: 65%; }
 #bpmjduvqva .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpmjduvqva .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bpmjduvqva .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bpmjduvqva .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bpmjduvqva .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bpmjduvqva .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pildoygesu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pildoygesu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pildoygesu p { margin: 0; padding: 0; }
 #pildoygesu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pildoygesu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pildoygesu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pildoygesu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pildoygesu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pildoygesu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pildoygesu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pildoygesu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pildoygesu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pildoygesu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pildoygesu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pildoygesu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pildoygesu .gt_spanner_row { border-bottom-style: hidden; }
 #pildoygesu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pildoygesu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pildoygesu .gt_from_md> :first-child { margin-top: 0; }
 #pildoygesu .gt_from_md> :last-child { margin-bottom: 0; }
 #pildoygesu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pildoygesu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pildoygesu .gt_indent_1 { text-indent: 5px; }
 #pildoygesu .gt_indent_2 { text-indent: calc(5px * 2); }
 #pildoygesu .gt_indent_3 { text-indent: calc(5px * 3); }
 #pildoygesu .gt_indent_4 { text-indent: calc(5px * 4); }
 #pildoygesu .gt_indent_5 { text-indent: calc(5px * 5); }
 #pildoygesu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pildoygesu .gt_row_group_first td { border-top-width: 2px; }
 #pildoygesu .gt_row_group_first th { border-top-width: 2px; }
 #pildoygesu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pildoygesu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pildoygesu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pildoygesu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pildoygesu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pildoygesu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pildoygesu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pildoygesu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pildoygesu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pildoygesu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pildoygesu .gt_left { text-align: left; }
 #pildoygesu .gt_center { text-align: center; }
 #pildoygesu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pildoygesu .gt_font_normal { font-weight: normal; }
 #pildoygesu .gt_font_bold { font-weight: bold; }
 #pildoygesu .gt_font_italic { font-style: italic; }
 #pildoygesu .gt_super { font-size: 65%; }
 #pildoygesu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pildoygesu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pildoygesu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pildoygesu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pildoygesu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pildoygesu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#tumsxwwlgb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tumsxwwlgb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tumsxwwlgb p { margin: 0; padding: 0; }
 #tumsxwwlgb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tumsxwwlgb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tumsxwwlgb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tumsxwwlgb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tumsxwwlgb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tumsxwwlgb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tumsxwwlgb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tumsxwwlgb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tumsxwwlgb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tumsxwwlgb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tumsxwwlgb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tumsxwwlgb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tumsxwwlgb .gt_spanner_row { border-bottom-style: hidden; }
 #tumsxwwlgb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tumsxwwlgb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tumsxwwlgb .gt_from_md> :first-child { margin-top: 0; }
 #tumsxwwlgb .gt_from_md> :last-child { margin-bottom: 0; }
 #tumsxwwlgb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tumsxwwlgb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tumsxwwlgb .gt_indent_1 { text-indent: 5px; }
 #tumsxwwlgb .gt_indent_2 { text-indent: calc(5px * 2); }
 #tumsxwwlgb .gt_indent_3 { text-indent: calc(5px * 3); }
 #tumsxwwlgb .gt_indent_4 { text-indent: calc(5px * 4); }
 #tumsxwwlgb .gt_indent_5 { text-indent: calc(5px * 5); }
 #tumsxwwlgb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tumsxwwlgb .gt_row_group_first td { border-top-width: 2px; }
 #tumsxwwlgb .gt_row_group_first th { border-top-width: 2px; }
 #tumsxwwlgb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tumsxwwlgb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tumsxwwlgb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tumsxwwlgb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tumsxwwlgb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tumsxwwlgb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tumsxwwlgb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tumsxwwlgb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tumsxwwlgb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tumsxwwlgb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tumsxwwlgb .gt_left { text-align: left; }
 #tumsxwwlgb .gt_center { text-align: center; }
 #tumsxwwlgb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tumsxwwlgb .gt_font_normal { font-weight: normal; }
 #tumsxwwlgb .gt_font_bold { font-weight: bold; }
 #tumsxwwlgb .gt_font_italic { font-style: italic; }
 #tumsxwwlgb .gt_super { font-size: 65%; }
 #tumsxwwlgb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tumsxwwlgb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tumsxwwlgb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tumsxwwlgb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tumsxwwlgb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tumsxwwlgb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qznpohnbvx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qznpohnbvx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qznpohnbvx p { margin: 0; padding: 0; }
 #qznpohnbvx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qznpohnbvx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qznpohnbvx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qznpohnbvx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qznpohnbvx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qznpohnbvx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qznpohnbvx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qznpohnbvx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qznpohnbvx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qznpohnbvx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qznpohnbvx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qznpohnbvx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qznpohnbvx .gt_spanner_row { border-bottom-style: hidden; }
 #qznpohnbvx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qznpohnbvx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qznpohnbvx .gt_from_md> :first-child { margin-top: 0; }
 #qznpohnbvx .gt_from_md> :last-child { margin-bottom: 0; }
 #qznpohnbvx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qznpohnbvx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qznpohnbvx .gt_indent_1 { text-indent: 5px; }
 #qznpohnbvx .gt_indent_2 { text-indent: calc(5px * 2); }
 #qznpohnbvx .gt_indent_3 { text-indent: calc(5px * 3); }
 #qznpohnbvx .gt_indent_4 { text-indent: calc(5px * 4); }
 #qznpohnbvx .gt_indent_5 { text-indent: calc(5px * 5); }
 #qznpohnbvx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qznpohnbvx .gt_row_group_first td { border-top-width: 2px; }
 #qznpohnbvx .gt_row_group_first th { border-top-width: 2px; }
 #qznpohnbvx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qznpohnbvx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qznpohnbvx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qznpohnbvx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qznpohnbvx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qznpohnbvx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qznpohnbvx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qznpohnbvx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qznpohnbvx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qznpohnbvx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qznpohnbvx .gt_left { text-align: left; }
 #qznpohnbvx .gt_center { text-align: center; }
 #qznpohnbvx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qznpohnbvx .gt_font_normal { font-weight: normal; }
 #qznpohnbvx .gt_font_bold { font-weight: bold; }
 #qznpohnbvx .gt_font_italic { font-style: italic; }
 #qznpohnbvx .gt_super { font-size: 65%; }
 #qznpohnbvx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qznpohnbvx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qznpohnbvx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qznpohnbvx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qznpohnbvx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qznpohnbvx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rgteynaxsf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rgteynaxsf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rgteynaxsf p { margin: 0; padding: 0; }
 #rgteynaxsf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rgteynaxsf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rgteynaxsf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rgteynaxsf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rgteynaxsf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rgteynaxsf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rgteynaxsf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rgteynaxsf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rgteynaxsf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rgteynaxsf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rgteynaxsf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rgteynaxsf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rgteynaxsf .gt_spanner_row { border-bottom-style: hidden; }
 #rgteynaxsf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rgteynaxsf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rgteynaxsf .gt_from_md> :first-child { margin-top: 0; }
 #rgteynaxsf .gt_from_md> :last-child { margin-bottom: 0; }
 #rgteynaxsf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rgteynaxsf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rgteynaxsf .gt_indent_1 { text-indent: 5px; }
 #rgteynaxsf .gt_indent_2 { text-indent: calc(5px * 2); }
 #rgteynaxsf .gt_indent_3 { text-indent: calc(5px * 3); }
 #rgteynaxsf .gt_indent_4 { text-indent: calc(5px * 4); }
 #rgteynaxsf .gt_indent_5 { text-indent: calc(5px * 5); }
 #rgteynaxsf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rgteynaxsf .gt_row_group_first td { border-top-width: 2px; }
 #rgteynaxsf .gt_row_group_first th { border-top-width: 2px; }
 #rgteynaxsf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rgteynaxsf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rgteynaxsf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rgteynaxsf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rgteynaxsf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rgteynaxsf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rgteynaxsf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rgteynaxsf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rgteynaxsf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rgteynaxsf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rgteynaxsf .gt_left { text-align: left; }
 #rgteynaxsf .gt_center { text-align: center; }
 #rgteynaxsf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rgteynaxsf .gt_font_normal { font-weight: normal; }
 #rgteynaxsf .gt_font_bold { font-weight: bold; }
 #rgteynaxsf .gt_font_italic { font-style: italic; }
 #rgteynaxsf .gt_super { font-size: 65%; }
 #rgteynaxsf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rgteynaxsf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rgteynaxsf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rgteynaxsf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rgteynaxsf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rgteynaxsf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#kndrayatvv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kndrayatvv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kndrayatvv p { margin: 0; padding: 0; }
 #kndrayatvv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kndrayatvv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kndrayatvv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kndrayatvv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kndrayatvv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kndrayatvv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kndrayatvv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kndrayatvv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kndrayatvv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kndrayatvv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kndrayatvv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kndrayatvv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kndrayatvv .gt_spanner_row { border-bottom-style: hidden; }
 #kndrayatvv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kndrayatvv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kndrayatvv .gt_from_md> :first-child { margin-top: 0; }
 #kndrayatvv .gt_from_md> :last-child { margin-bottom: 0; }
 #kndrayatvv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kndrayatvv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kndrayatvv .gt_indent_1 { text-indent: 5px; }
 #kndrayatvv .gt_indent_2 { text-indent: calc(5px * 2); }
 #kndrayatvv .gt_indent_3 { text-indent: calc(5px * 3); }
 #kndrayatvv .gt_indent_4 { text-indent: calc(5px * 4); }
 #kndrayatvv .gt_indent_5 { text-indent: calc(5px * 5); }
 #kndrayatvv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kndrayatvv .gt_row_group_first td { border-top-width: 2px; }
 #kndrayatvv .gt_row_group_first th { border-top-width: 2px; }
 #kndrayatvv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kndrayatvv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kndrayatvv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kndrayatvv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kndrayatvv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kndrayatvv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kndrayatvv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kndrayatvv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kndrayatvv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kndrayatvv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kndrayatvv .gt_left { text-align: left; }
 #kndrayatvv .gt_center { text-align: center; }
 #kndrayatvv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kndrayatvv .gt_font_normal { font-weight: normal; }
 #kndrayatvv .gt_font_bold { font-weight: bold; }
 #kndrayatvv .gt_font_italic { font-style: italic; }
 #kndrayatvv .gt_super { font-size: 65%; }
 #kndrayatvv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kndrayatvv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kndrayatvv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kndrayatvv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kndrayatvv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kndrayatvv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hqkysmkxez table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hqkysmkxez thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hqkysmkxez p { margin: 0; padding: 0; }
 #hqkysmkxez .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hqkysmkxez .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hqkysmkxez .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hqkysmkxez .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hqkysmkxez .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hqkysmkxez .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hqkysmkxez .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hqkysmkxez .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hqkysmkxez .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hqkysmkxez .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hqkysmkxez .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hqkysmkxez .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hqkysmkxez .gt_spanner_row { border-bottom-style: hidden; }
 #hqkysmkxez .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hqkysmkxez .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hqkysmkxez .gt_from_md> :first-child { margin-top: 0; }
 #hqkysmkxez .gt_from_md> :last-child { margin-bottom: 0; }
 #hqkysmkxez .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hqkysmkxez .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hqkysmkxez .gt_indent_1 { text-indent: 5px; }
 #hqkysmkxez .gt_indent_2 { text-indent: calc(5px * 2); }
 #hqkysmkxez .gt_indent_3 { text-indent: calc(5px * 3); }
 #hqkysmkxez .gt_indent_4 { text-indent: calc(5px * 4); }
 #hqkysmkxez .gt_indent_5 { text-indent: calc(5px * 5); }
 #hqkysmkxez .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hqkysmkxez .gt_row_group_first td { border-top-width: 2px; }
 #hqkysmkxez .gt_row_group_first th { border-top-width: 2px; }
 #hqkysmkxez .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hqkysmkxez .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hqkysmkxez .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hqkysmkxez .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hqkysmkxez .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hqkysmkxez .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hqkysmkxez .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hqkysmkxez .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hqkysmkxez .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hqkysmkxez .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hqkysmkxez .gt_left { text-align: left; }
 #hqkysmkxez .gt_center { text-align: center; }
 #hqkysmkxez .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hqkysmkxez .gt_font_normal { font-weight: normal; }
 #hqkysmkxez .gt_font_bold { font-weight: bold; }
 #hqkysmkxez .gt_font_italic { font-style: italic; }
 #hqkysmkxez .gt_super { font-size: 65%; }
 #hqkysmkxez .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hqkysmkxez .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hqkysmkxez .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hqkysmkxez .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hqkysmkxez .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hqkysmkxez .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bkeoouwoor table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bkeoouwoor thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bkeoouwoor p { margin: 0; padding: 0; }
 #bkeoouwoor .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bkeoouwoor .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bkeoouwoor .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bkeoouwoor .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bkeoouwoor .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bkeoouwoor .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bkeoouwoor .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bkeoouwoor .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bkeoouwoor .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bkeoouwoor .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bkeoouwoor .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bkeoouwoor .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bkeoouwoor .gt_spanner_row { border-bottom-style: hidden; }
 #bkeoouwoor .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bkeoouwoor .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bkeoouwoor .gt_from_md> :first-child { margin-top: 0; }
 #bkeoouwoor .gt_from_md> :last-child { margin-bottom: 0; }
 #bkeoouwoor .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bkeoouwoor .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bkeoouwoor .gt_indent_1 { text-indent: 5px; }
 #bkeoouwoor .gt_indent_2 { text-indent: calc(5px * 2); }
 #bkeoouwoor .gt_indent_3 { text-indent: calc(5px * 3); }
 #bkeoouwoor .gt_indent_4 { text-indent: calc(5px * 4); }
 #bkeoouwoor .gt_indent_5 { text-indent: calc(5px * 5); }
 #bkeoouwoor .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bkeoouwoor .gt_row_group_first td { border-top-width: 2px; }
 #bkeoouwoor .gt_row_group_first th { border-top-width: 2px; }
 #bkeoouwoor .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bkeoouwoor .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bkeoouwoor .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bkeoouwoor .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bkeoouwoor .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bkeoouwoor .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bkeoouwoor .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bkeoouwoor .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bkeoouwoor .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bkeoouwoor .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bkeoouwoor .gt_left { text-align: left; }
 #bkeoouwoor .gt_center { text-align: center; }
 #bkeoouwoor .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bkeoouwoor .gt_font_normal { font-weight: normal; }
 #bkeoouwoor .gt_font_bold { font-weight: bold; }
 #bkeoouwoor .gt_font_italic { font-style: italic; }
 #bkeoouwoor .gt_super { font-size: 65%; }
 #bkeoouwoor .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bkeoouwoor .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bkeoouwoor .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bkeoouwoor .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bkeoouwoor .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bkeoouwoor .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | status      | priority | progress |
|-----------------|-------------|----------|----------|
| Data collection | Complete    | High ●   | 100      |
| Analysis        | In Progress | High ●   | 65       |
| Report writing  | Not Started | Medium ● | 0        |
| Peer review     | Complete    | Low ●    | 100      |


The text transformation methods provide a final layer of control over how your table content appears. Whether you need simple find-and-replace, switch-like mappings, or complex conditional logic, these methods let you shape the text to match your exact presentation needs.
