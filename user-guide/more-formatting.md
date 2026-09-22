# More Formatting Options

The [Formatting Values](formatting-values.md) page introduced the basics of `fmt_number()`, `fmt_currency()`, `fmt_date()`, and `fmt_time()`. But **Great Tables** has a much larger formatting toolkit. This page covers additional formatters that handle percentages, byte sizes, durations, scientific units, icons, flags, images, boolean values, Markdown, and more. Each formatter transforms raw cell data into presentation-ready content.

When choosing a formatter, start with the semantic meaning of your data. If a column represents a file size, reach for `fmt_bytes()` rather than `fmt_number()` with manual suffix logic. If a column holds time durations, use `fmt_duration()` instead of formatting seconds by hand. Semantic formatters produce more consistent output and handle edge cases (like unit boundaries and scaling) automatically, so you get correct results without writing extra logic.


# Percentage Formatting

The [fmt_percent()](../reference/GT.fmt_percent.md#great_tables.GT.fmt_percent) method formats numeric values as percentages. By default, it assumes the input values are proportions (e.g., `0.25` becomes `"25.00%"`). If your values are already in percent form, set `scale_values=False`.


``` python
import polars as pl
from great_tables import GT

pct_df = pl.DataFrame({
    "metric": ["Conversion rate", "Bounce rate", "Click-through"],
    "proportion": [0.034, 0.621, 0.158],
    "already_pct": [3.4, 62.1, 15.8],
})

(
    GT(pct_df, rowname_col="metric")
    .fmt_percent(columns="proportion", decimals=1)
    .fmt_percent(columns="already_pct", decimals=1, scale_values=False)
)
```


<style>
#tqkrgdvtlr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tqkrgdvtlr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tqkrgdvtlr p { margin: 0; padding: 0; }
 #tqkrgdvtlr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tqkrgdvtlr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tqkrgdvtlr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tqkrgdvtlr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tqkrgdvtlr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tqkrgdvtlr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tqkrgdvtlr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tqkrgdvtlr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tqkrgdvtlr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tqkrgdvtlr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tqkrgdvtlr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tqkrgdvtlr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tqkrgdvtlr .gt_spanner_row { border-bottom-style: hidden; }
 #tqkrgdvtlr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tqkrgdvtlr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tqkrgdvtlr .gt_from_md> :first-child { margin-top: 0; }
 #tqkrgdvtlr .gt_from_md> :last-child { margin-bottom: 0; }
 #tqkrgdvtlr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tqkrgdvtlr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tqkrgdvtlr .gt_indent_1 { text-indent: 5px; }
 #tqkrgdvtlr .gt_indent_2 { text-indent: calc(5px * 2); }
 #tqkrgdvtlr .gt_indent_3 { text-indent: calc(5px * 3); }
 #tqkrgdvtlr .gt_indent_4 { text-indent: calc(5px * 4); }
 #tqkrgdvtlr .gt_indent_5 { text-indent: calc(5px * 5); }
 #tqkrgdvtlr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tqkrgdvtlr .gt_row_group_first td { border-top-width: 2px; }
 #tqkrgdvtlr .gt_row_group_first th { border-top-width: 2px; }
 #tqkrgdvtlr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tqkrgdvtlr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tqkrgdvtlr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tqkrgdvtlr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tqkrgdvtlr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tqkrgdvtlr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tqkrgdvtlr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tqkrgdvtlr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tqkrgdvtlr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tqkrgdvtlr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tqkrgdvtlr .gt_left { text-align: left; }
 #tqkrgdvtlr .gt_center { text-align: center; }
 #tqkrgdvtlr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tqkrgdvtlr .gt_font_normal { font-weight: normal; }
 #tqkrgdvtlr .gt_font_bold { font-weight: bold; }
 #tqkrgdvtlr .gt_font_italic { font-style: italic; }
 #tqkrgdvtlr .gt_super { font-size: 65%; }
 #tqkrgdvtlr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tqkrgdvtlr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tqkrgdvtlr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tqkrgdvtlr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tqkrgdvtlr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tqkrgdvtlr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | proportion | already_pct |
|-----------------|------------|-------------|
| Conversion rate | 3.4%       | 3.4%        |
| Bounce rate     | 62.1%      | 62.1%       |
| Click-through   | 15.8%      | 15.8%       |


Both columns display correctly as percentages, but the `proportion` column needed scaling (the default behavior) while `already_pct` did not.


# Byte Size Formatting

The [fmt_bytes()](../reference/GT.fmt_bytes.md#great_tables.GT.fmt_bytes) method converts raw byte counts into human-readable sizes. It automatically selects the appropriate unit (kB, MB, GB, etc.) based on the magnitude of the value.


``` python
bytes_df = pl.DataFrame({
    "file": ["photo.jpg", "video.mp4", "document.pdf", "database.sqlite"],
    "size_bytes": [2_048_000, 1_573_000_000, 524_288, 85_000_000_000],
})

(
    GT(bytes_df, rowname_col="file")
    .fmt_bytes(columns="size_bytes", standard="decimal")
)
```


<style>
#vubpndyjff table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vubpndyjff thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vubpndyjff p { margin: 0; padding: 0; }
 #vubpndyjff .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vubpndyjff .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vubpndyjff .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vubpndyjff .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vubpndyjff .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vubpndyjff .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vubpndyjff .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vubpndyjff .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vubpndyjff .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vubpndyjff .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vubpndyjff .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vubpndyjff .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vubpndyjff .gt_spanner_row { border-bottom-style: hidden; }
 #vubpndyjff .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vubpndyjff .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vubpndyjff .gt_from_md> :first-child { margin-top: 0; }
 #vubpndyjff .gt_from_md> :last-child { margin-bottom: 0; }
 #vubpndyjff .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vubpndyjff .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vubpndyjff .gt_indent_1 { text-indent: 5px; }
 #vubpndyjff .gt_indent_2 { text-indent: calc(5px * 2); }
 #vubpndyjff .gt_indent_3 { text-indent: calc(5px * 3); }
 #vubpndyjff .gt_indent_4 { text-indent: calc(5px * 4); }
 #vubpndyjff .gt_indent_5 { text-indent: calc(5px * 5); }
 #vubpndyjff .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vubpndyjff .gt_row_group_first td { border-top-width: 2px; }
 #vubpndyjff .gt_row_group_first th { border-top-width: 2px; }
 #vubpndyjff .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vubpndyjff .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vubpndyjff .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vubpndyjff .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vubpndyjff .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vubpndyjff .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vubpndyjff .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vubpndyjff .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vubpndyjff .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vubpndyjff .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vubpndyjff .gt_left { text-align: left; }
 #vubpndyjff .gt_center { text-align: center; }
 #vubpndyjff .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vubpndyjff .gt_font_normal { font-weight: normal; }
 #vubpndyjff .gt_font_bold { font-weight: bold; }
 #vubpndyjff .gt_font_italic { font-style: italic; }
 #vubpndyjff .gt_super { font-size: 65%; }
 #vubpndyjff .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vubpndyjff .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vubpndyjff .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vubpndyjff .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vubpndyjff .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vubpndyjff .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | size_bytes |
|-----------------|------------|
| photo.jpg       | 2 MB       |
| video.mp4       | 1.6 GB     |
| document.pdf    | 524.3 kB   |
| database.sqlite | 85 GB      |


The `standard=` argument controls the unit system. Use `"decimal"` for powers of 1000 (kB, MB, GB) or `"binary"` for powers of 1024 (KiB, MiB, GiB).


``` python
(
    GT(bytes_df, rowname_col="file")
    .fmt_bytes(columns="size_bytes", standard="binary")
)
```


<style>
#phzleznpfm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#phzleznpfm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#phzleznpfm p { margin: 0; padding: 0; }
 #phzleznpfm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #phzleznpfm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #phzleznpfm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #phzleznpfm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #phzleznpfm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #phzleznpfm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #phzleznpfm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #phzleznpfm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #phzleznpfm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #phzleznpfm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #phzleznpfm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #phzleznpfm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #phzleznpfm .gt_spanner_row { border-bottom-style: hidden; }
 #phzleznpfm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #phzleznpfm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #phzleznpfm .gt_from_md> :first-child { margin-top: 0; }
 #phzleznpfm .gt_from_md> :last-child { margin-bottom: 0; }
 #phzleznpfm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #phzleznpfm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #phzleznpfm .gt_indent_1 { text-indent: 5px; }
 #phzleznpfm .gt_indent_2 { text-indent: calc(5px * 2); }
 #phzleznpfm .gt_indent_3 { text-indent: calc(5px * 3); }
 #phzleznpfm .gt_indent_4 { text-indent: calc(5px * 4); }
 #phzleznpfm .gt_indent_5 { text-indent: calc(5px * 5); }
 #phzleznpfm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #phzleznpfm .gt_row_group_first td { border-top-width: 2px; }
 #phzleznpfm .gt_row_group_first th { border-top-width: 2px; }
 #phzleznpfm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #phzleznpfm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #phzleznpfm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #phzleznpfm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #phzleznpfm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #phzleznpfm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #phzleznpfm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #phzleznpfm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #phzleznpfm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #phzleznpfm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #phzleznpfm .gt_left { text-align: left; }
 #phzleznpfm .gt_center { text-align: center; }
 #phzleznpfm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #phzleznpfm .gt_font_normal { font-weight: normal; }
 #phzleznpfm .gt_font_bold { font-weight: bold; }
 #phzleznpfm .gt_font_italic { font-style: italic; }
 #phzleznpfm .gt_super { font-size: 65%; }
 #phzleznpfm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #phzleznpfm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #phzleznpfm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #phzleznpfm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #phzleznpfm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #phzleznpfm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                 | size_bytes |
|-----------------|------------|
| photo.jpg       | 2 MiB      |
| video.mp4       | 1.5 GiB    |
| document.pdf    | 512 KiB    |
| database.sqlite | 79.2 GiB   |


With the binary standard, the same byte values display in KiB, MiB, and GiB units. Choose whichever standard matches the conventions of your domain.

As a rule of thumb, use decimal units (kB, MB, GB) for storage marketed to consumers (disk drives, cloud storage quotas, and network transfer speeds all use powers of 1000). Use binary units (KiB, MiB, GiB) for memory and technical contexts where powers of 1024 are precise, such as RAM capacity, cache sizes, and buffer allocations. Picking the right standard avoids confusing your readers with numbers that don't match what they see elsewhere.


# Duration Formatting

The [fmt_duration()](../reference/GT.fmt_duration.md#great_tables.GT.fmt_duration) method formats numeric values (or `timedelta` objects) as styled time duration strings. You specify the input unit and the method handles the conversion and display.


``` python
duration_df = pl.DataFrame({
    "event": ["Sprint", "Marathon", "Triathlon", "Ultra"],
    "seconds": [58, 7380, 21600, 172800],
})

(
    GT(duration_df, rowname_col="event")
    .fmt_duration(columns="seconds", input_units="seconds")
)
```


<style>
#qjkrgibjlp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qjkrgibjlp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qjkrgibjlp p { margin: 0; padding: 0; }
 #qjkrgibjlp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qjkrgibjlp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qjkrgibjlp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qjkrgibjlp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qjkrgibjlp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qjkrgibjlp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qjkrgibjlp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qjkrgibjlp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qjkrgibjlp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qjkrgibjlp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qjkrgibjlp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qjkrgibjlp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qjkrgibjlp .gt_spanner_row { border-bottom-style: hidden; }
 #qjkrgibjlp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qjkrgibjlp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qjkrgibjlp .gt_from_md> :first-child { margin-top: 0; }
 #qjkrgibjlp .gt_from_md> :last-child { margin-bottom: 0; }
 #qjkrgibjlp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qjkrgibjlp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qjkrgibjlp .gt_indent_1 { text-indent: 5px; }
 #qjkrgibjlp .gt_indent_2 { text-indent: calc(5px * 2); }
 #qjkrgibjlp .gt_indent_3 { text-indent: calc(5px * 3); }
 #qjkrgibjlp .gt_indent_4 { text-indent: calc(5px * 4); }
 #qjkrgibjlp .gt_indent_5 { text-indent: calc(5px * 5); }
 #qjkrgibjlp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qjkrgibjlp .gt_row_group_first td { border-top-width: 2px; }
 #qjkrgibjlp .gt_row_group_first th { border-top-width: 2px; }
 #qjkrgibjlp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qjkrgibjlp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qjkrgibjlp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qjkrgibjlp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qjkrgibjlp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qjkrgibjlp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qjkrgibjlp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qjkrgibjlp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qjkrgibjlp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qjkrgibjlp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qjkrgibjlp .gt_left { text-align: left; }
 #qjkrgibjlp .gt_center { text-align: center; }
 #qjkrgibjlp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qjkrgibjlp .gt_font_normal { font-weight: normal; }
 #qjkrgibjlp .gt_font_bold { font-weight: bold; }
 #qjkrgibjlp .gt_font_italic { font-style: italic; }
 #qjkrgibjlp .gt_super { font-size: 65%; }
 #qjkrgibjlp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qjkrgibjlp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qjkrgibjlp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qjkrgibjlp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qjkrgibjlp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qjkrgibjlp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|           | seconds |
|-----------|---------|
| Sprint    | 58s     |
| Marathon  | 2h 3m   |
| Triathlon | 6h      |
| Ultra     | 2d      |


The `duration_style=` argument controls the output format. The available styles are:

- `"narrow"` (the default): compact format like `"2d 3h 15m"`
- `"wide"`: spelled out like `"2 days 3 hours 15 minutes"`
- `"colon-sep"`: clock format like `"51:03:15"`
- `"iso"`: ISO 8601 format like `"P2DT3H15M"`


``` python
(
    GT(duration_df, rowname_col="event")
    .fmt_duration(columns="seconds", input_units="seconds", duration_style="wide")
)
```


<style>
#phlrjatvqv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#phlrjatvqv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#phlrjatvqv p { margin: 0; padding: 0; }
 #phlrjatvqv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #phlrjatvqv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #phlrjatvqv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #phlrjatvqv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #phlrjatvqv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #phlrjatvqv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #phlrjatvqv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #phlrjatvqv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #phlrjatvqv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #phlrjatvqv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #phlrjatvqv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #phlrjatvqv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #phlrjatvqv .gt_spanner_row { border-bottom-style: hidden; }
 #phlrjatvqv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #phlrjatvqv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #phlrjatvqv .gt_from_md> :first-child { margin-top: 0; }
 #phlrjatvqv .gt_from_md> :last-child { margin-bottom: 0; }
 #phlrjatvqv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #phlrjatvqv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #phlrjatvqv .gt_indent_1 { text-indent: 5px; }
 #phlrjatvqv .gt_indent_2 { text-indent: calc(5px * 2); }
 #phlrjatvqv .gt_indent_3 { text-indent: calc(5px * 3); }
 #phlrjatvqv .gt_indent_4 { text-indent: calc(5px * 4); }
 #phlrjatvqv .gt_indent_5 { text-indent: calc(5px * 5); }
 #phlrjatvqv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #phlrjatvqv .gt_row_group_first td { border-top-width: 2px; }
 #phlrjatvqv .gt_row_group_first th { border-top-width: 2px; }
 #phlrjatvqv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #phlrjatvqv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #phlrjatvqv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #phlrjatvqv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #phlrjatvqv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #phlrjatvqv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #phlrjatvqv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #phlrjatvqv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #phlrjatvqv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #phlrjatvqv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #phlrjatvqv .gt_left { text-align: left; }
 #phlrjatvqv .gt_center { text-align: center; }
 #phlrjatvqv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #phlrjatvqv .gt_font_normal { font-weight: normal; }
 #phlrjatvqv .gt_font_bold { font-weight: bold; }
 #phlrjatvqv .gt_font_italic { font-style: italic; }
 #phlrjatvqv .gt_super { font-size: 65%; }
 #phlrjatvqv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #phlrjatvqv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #phlrjatvqv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #phlrjatvqv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #phlrjatvqv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #phlrjatvqv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|           | seconds           |
|-----------|-------------------|
| Sprint    | 58 seconds        |
| Marathon  | 2 hours 3 minutes |
| Triathlon | 6 hours           |
| Ultra     | 2 days            |


You can limit the number of output units with `max_output_units=` to keep the display concise.


``` python
(
    GT(duration_df, rowname_col="event")
    .fmt_duration(columns="seconds", input_units="seconds", max_output_units=2)
)
```


<style>
#rihskdymgr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rihskdymgr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rihskdymgr p { margin: 0; padding: 0; }
 #rihskdymgr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rihskdymgr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rihskdymgr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rihskdymgr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rihskdymgr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rihskdymgr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rihskdymgr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rihskdymgr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rihskdymgr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rihskdymgr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rihskdymgr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rihskdymgr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rihskdymgr .gt_spanner_row { border-bottom-style: hidden; }
 #rihskdymgr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rihskdymgr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rihskdymgr .gt_from_md> :first-child { margin-top: 0; }
 #rihskdymgr .gt_from_md> :last-child { margin-bottom: 0; }
 #rihskdymgr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rihskdymgr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rihskdymgr .gt_indent_1 { text-indent: 5px; }
 #rihskdymgr .gt_indent_2 { text-indent: calc(5px * 2); }
 #rihskdymgr .gt_indent_3 { text-indent: calc(5px * 3); }
 #rihskdymgr .gt_indent_4 { text-indent: calc(5px * 4); }
 #rihskdymgr .gt_indent_5 { text-indent: calc(5px * 5); }
 #rihskdymgr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rihskdymgr .gt_row_group_first td { border-top-width: 2px; }
 #rihskdymgr .gt_row_group_first th { border-top-width: 2px; }
 #rihskdymgr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rihskdymgr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rihskdymgr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rihskdymgr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rihskdymgr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rihskdymgr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rihskdymgr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rihskdymgr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rihskdymgr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rihskdymgr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rihskdymgr .gt_left { text-align: left; }
 #rihskdymgr .gt_center { text-align: center; }
 #rihskdymgr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rihskdymgr .gt_font_normal { font-weight: normal; }
 #rihskdymgr .gt_font_bold { font-weight: bold; }
 #rihskdymgr .gt_font_italic { font-style: italic; }
 #rihskdymgr .gt_super { font-size: 65%; }
 #rihskdymgr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rihskdymgr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rihskdymgr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rihskdymgr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rihskdymgr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rihskdymgr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|           | seconds |
|-----------|---------|
| Sprint    | 58s     |
| Marathon  | 2h 3m   |
| Triathlon | 6h      |
| Ultra     | 2d      |


Limiting the output to two units (e.g., `"2d 3h"` instead of `"2d 3h 15m"`) keeps the display compact when exact precision is not required.


# Engineering Notation

The [fmt_engineering()](../reference/GT.fmt_engineering.md#great_tables.GT.fmt_engineering) method formats values in engineering notation, where the exponent is always a multiple of 3. This aligns with SI prefixes (kilo, mega, milli, micro, etc.) and is common in technical and scientific contexts.


``` python
eng_df = pl.DataFrame({
    "quantity": ["Resistance", "Capacitance", "Frequency", "Power"],
    "value": [4700.0, 0.0000001, 2400000000.0, 0.0035],
})

(
    GT(eng_df, rowname_col="quantity")
    .fmt_engineering(columns="value")
)
```


<style>
#ltukftmbif table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ltukftmbif thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ltukftmbif p { margin: 0; padding: 0; }
 #ltukftmbif .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ltukftmbif .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ltukftmbif .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ltukftmbif .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ltukftmbif .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ltukftmbif .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ltukftmbif .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ltukftmbif .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ltukftmbif .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ltukftmbif .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ltukftmbif .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ltukftmbif .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ltukftmbif .gt_spanner_row { border-bottom-style: hidden; }
 #ltukftmbif .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ltukftmbif .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ltukftmbif .gt_from_md> :first-child { margin-top: 0; }
 #ltukftmbif .gt_from_md> :last-child { margin-bottom: 0; }
 #ltukftmbif .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ltukftmbif .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ltukftmbif .gt_indent_1 { text-indent: 5px; }
 #ltukftmbif .gt_indent_2 { text-indent: calc(5px * 2); }
 #ltukftmbif .gt_indent_3 { text-indent: calc(5px * 3); }
 #ltukftmbif .gt_indent_4 { text-indent: calc(5px * 4); }
 #ltukftmbif .gt_indent_5 { text-indent: calc(5px * 5); }
 #ltukftmbif .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ltukftmbif .gt_row_group_first td { border-top-width: 2px; }
 #ltukftmbif .gt_row_group_first th { border-top-width: 2px; }
 #ltukftmbif .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ltukftmbif .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ltukftmbif .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ltukftmbif .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ltukftmbif .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ltukftmbif .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ltukftmbif .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ltukftmbif .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ltukftmbif .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ltukftmbif .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ltukftmbif .gt_left { text-align: left; }
 #ltukftmbif .gt_center { text-align: center; }
 #ltukftmbif .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ltukftmbif .gt_font_normal { font-weight: normal; }
 #ltukftmbif .gt_font_bold { font-weight: bold; }
 #ltukftmbif .gt_font_italic { font-style: italic; }
 #ltukftmbif .gt_super { font-size: 65%; }
 #ltukftmbif .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ltukftmbif .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ltukftmbif .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ltukftmbif .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ltukftmbif .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ltukftmbif .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|             | value                    |
|-------------|--------------------------|
| Resistance  | 4.70 × 10<sup>3</sup>    |
| Capacitance | 100.00 × 10<sup>−9</sup> |
| Frequency   | 2.40 × 10<sup>9</sup>    |
| Power       | 3.50 × 10<sup>−3</sup>   |


Each value is expressed with a mantissa between 1 and 999 and an exponent that is a multiple of 3. This makes it straightforward to mentally convert to SI prefixes (e.g., `4.7 x 10^3` = 4.7 kilo).

Engineering notation is preferred over scientific notation when your audience thinks in terms of SI prefixes. Because the exponent is always a multiple of 3, values map directly to familiar units: kilohms, microfarads, gigahertz, milliwatts, and so on. Readers can interpret the numbers without mental conversion. If your data spans a wide range of magnitudes in a technical domain, engineering notation is almost always the better choice.


# Parts-Per Formatting

The [fmt_partsper()](../reference/GT.fmt_partsper.md#great_tables.GT.fmt_partsper) method formats values as parts-per quantities: per mille, ppm, ppb, and more. By default, it assumes input values are proportions and scales them accordingly.


``` python
ppm_df = pl.DataFrame({
    "substance": ["Lead", "Mercury", "Arsenic"],
    "concentration": [0.000015, 0.000001, 0.00001],
})

(
    GT(ppm_df, rowname_col="substance")
    .fmt_partsper(columns="concentration", to_units="ppm")
)
```


<style>
#dbjirlnnzx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dbjirlnnzx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dbjirlnnzx p { margin: 0; padding: 0; }
 #dbjirlnnzx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dbjirlnnzx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dbjirlnnzx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dbjirlnnzx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dbjirlnnzx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dbjirlnnzx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dbjirlnnzx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dbjirlnnzx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dbjirlnnzx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dbjirlnnzx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dbjirlnnzx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dbjirlnnzx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dbjirlnnzx .gt_spanner_row { border-bottom-style: hidden; }
 #dbjirlnnzx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dbjirlnnzx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dbjirlnnzx .gt_from_md> :first-child { margin-top: 0; }
 #dbjirlnnzx .gt_from_md> :last-child { margin-bottom: 0; }
 #dbjirlnnzx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dbjirlnnzx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dbjirlnnzx .gt_indent_1 { text-indent: 5px; }
 #dbjirlnnzx .gt_indent_2 { text-indent: calc(5px * 2); }
 #dbjirlnnzx .gt_indent_3 { text-indent: calc(5px * 3); }
 #dbjirlnnzx .gt_indent_4 { text-indent: calc(5px * 4); }
 #dbjirlnnzx .gt_indent_5 { text-indent: calc(5px * 5); }
 #dbjirlnnzx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dbjirlnnzx .gt_row_group_first td { border-top-width: 2px; }
 #dbjirlnnzx .gt_row_group_first th { border-top-width: 2px; }
 #dbjirlnnzx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dbjirlnnzx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dbjirlnnzx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dbjirlnnzx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dbjirlnnzx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dbjirlnnzx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dbjirlnnzx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dbjirlnnzx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dbjirlnnzx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dbjirlnnzx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dbjirlnnzx .gt_left { text-align: left; }
 #dbjirlnnzx .gt_center { text-align: center; }
 #dbjirlnnzx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dbjirlnnzx .gt_font_normal { font-weight: normal; }
 #dbjirlnnzx .gt_font_bold { font-weight: bold; }
 #dbjirlnnzx .gt_font_italic { font-style: italic; }
 #dbjirlnnzx .gt_super { font-size: 65%; }
 #dbjirlnnzx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dbjirlnnzx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dbjirlnnzx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dbjirlnnzx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dbjirlnnzx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dbjirlnnzx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | concentration |
|---------|---------------|
| Lead    | 15.00 ppm     |
| Mercury | 1.00 ppm      |
| Arsenic | 10.00 ppm     |


The `to_units=` argument accepts the following values: `"per-mille"`, `"per-myriad"`, `"pcm"`, `"ppm"`, `"ppb"`, `"ppt"`, and `"ppq"`.


# Roman Numeral Formatting

The [fmt_roman()](../reference/GT.fmt_roman.md#great_tables.GT.fmt_roman) method converts integer values into Roman numerals. This can be useful for numbering chapters, sections, or ranked items.


``` python
roman_df = pl.DataFrame({
    "event": ["Opening", "Keynote", "Workshop", "Closing"],
    "order": [1, 2, 3, 4],
})

(
    GT(roman_df, rowname_col="event")
    .fmt_roman(columns="order")
)
```


<style>
#axckcfgyvb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#axckcfgyvb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#axckcfgyvb p { margin: 0; padding: 0; }
 #axckcfgyvb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #axckcfgyvb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #axckcfgyvb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #axckcfgyvb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #axckcfgyvb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #axckcfgyvb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #axckcfgyvb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #axckcfgyvb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #axckcfgyvb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #axckcfgyvb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #axckcfgyvb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #axckcfgyvb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #axckcfgyvb .gt_spanner_row { border-bottom-style: hidden; }
 #axckcfgyvb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #axckcfgyvb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #axckcfgyvb .gt_from_md> :first-child { margin-top: 0; }
 #axckcfgyvb .gt_from_md> :last-child { margin-bottom: 0; }
 #axckcfgyvb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #axckcfgyvb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #axckcfgyvb .gt_indent_1 { text-indent: 5px; }
 #axckcfgyvb .gt_indent_2 { text-indent: calc(5px * 2); }
 #axckcfgyvb .gt_indent_3 { text-indent: calc(5px * 3); }
 #axckcfgyvb .gt_indent_4 { text-indent: calc(5px * 4); }
 #axckcfgyvb .gt_indent_5 { text-indent: calc(5px * 5); }
 #axckcfgyvb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #axckcfgyvb .gt_row_group_first td { border-top-width: 2px; }
 #axckcfgyvb .gt_row_group_first th { border-top-width: 2px; }
 #axckcfgyvb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #axckcfgyvb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #axckcfgyvb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #axckcfgyvb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #axckcfgyvb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #axckcfgyvb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #axckcfgyvb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #axckcfgyvb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #axckcfgyvb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #axckcfgyvb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #axckcfgyvb .gt_left { text-align: left; }
 #axckcfgyvb .gt_center { text-align: center; }
 #axckcfgyvb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #axckcfgyvb .gt_font_normal { font-weight: normal; }
 #axckcfgyvb .gt_font_bold { font-weight: bold; }
 #axckcfgyvb .gt_font_italic { font-style: italic; }
 #axckcfgyvb .gt_super { font-size: 65%; }
 #axckcfgyvb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #axckcfgyvb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #axckcfgyvb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #axckcfgyvb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #axckcfgyvb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #axckcfgyvb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|          | order |
|----------|-------|
| Opening  | I     |
| Keynote  | II    |
| Workshop | III   |
| Closing  | IV    |


The `case=` argument accepts `"upper"` (the default, producing `"I"`, `"II"`, `"III"`) or `"lower"` (producing `"i"`, `"ii"`, `"iii"`).


# Scientific Units

The [fmt_units()](../reference/GT.fmt_units.md#great_tables.GT.fmt_units) method renders measurement units with proper subscripts, superscripts, and special symbols. It uses a concise notation syntax where `^` indicates superscripts, `_` indicates subscripts, and special names are referenced with colons.


``` python
units_df = pl.DataFrame({
    "quantity": ["Speed of light", "Boltzmann constant", "Planck constant", "Acceleration"],
    "units": ["m/s", "J Hz^-1", "kg m^2 s^-1", "m s^-2"],
})

(
    GT(units_df, rowname_col="quantity")
    .fmt_units(columns="units")
)
```


<style>
#hsebnnyjmy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hsebnnyjmy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hsebnnyjmy p { margin: 0; padding: 0; }
 #hsebnnyjmy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hsebnnyjmy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hsebnnyjmy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hsebnnyjmy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hsebnnyjmy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hsebnnyjmy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hsebnnyjmy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hsebnnyjmy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hsebnnyjmy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hsebnnyjmy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hsebnnyjmy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hsebnnyjmy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hsebnnyjmy .gt_spanner_row { border-bottom-style: hidden; }
 #hsebnnyjmy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hsebnnyjmy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hsebnnyjmy .gt_from_md> :first-child { margin-top: 0; }
 #hsebnnyjmy .gt_from_md> :last-child { margin-bottom: 0; }
 #hsebnnyjmy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hsebnnyjmy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hsebnnyjmy .gt_indent_1 { text-indent: 5px; }
 #hsebnnyjmy .gt_indent_2 { text-indent: calc(5px * 2); }
 #hsebnnyjmy .gt_indent_3 { text-indent: calc(5px * 3); }
 #hsebnnyjmy .gt_indent_4 { text-indent: calc(5px * 4); }
 #hsebnnyjmy .gt_indent_5 { text-indent: calc(5px * 5); }
 #hsebnnyjmy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hsebnnyjmy .gt_row_group_first td { border-top-width: 2px; }
 #hsebnnyjmy .gt_row_group_first th { border-top-width: 2px; }
 #hsebnnyjmy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hsebnnyjmy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hsebnnyjmy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hsebnnyjmy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hsebnnyjmy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hsebnnyjmy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hsebnnyjmy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hsebnnyjmy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hsebnnyjmy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hsebnnyjmy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hsebnnyjmy .gt_left { text-align: left; }
 #hsebnnyjmy .gt_center { text-align: center; }
 #hsebnnyjmy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hsebnnyjmy .gt_font_normal { font-weight: normal; }
 #hsebnnyjmy .gt_font_bold { font-weight: bold; }
 #hsebnnyjmy .gt_font_italic { font-style: italic; }
 #hsebnnyjmy .gt_super { font-size: 65%; }
 #hsebnnyjmy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hsebnnyjmy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hsebnnyjmy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hsebnnyjmy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hsebnnyjmy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hsebnnyjmy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|  | units |
|----|----|
| Speed of light | m/s |
| Boltzmann constant | J Hz<span style="white-space:nowrap;"><sup>−1</sup></span> |
| Planck constant | kg m<span style="white-space:nowrap;"><sup>2</sup></span> s<span style="white-space:nowrap;"><sup>−1</sup></span> |
| Acceleration | m s<span style="white-space:nowrap;"><sup>−2</sup></span> |


The units notation supports Greek letters (`:alpha:`, `:beta:`, `:sigma:`), chemical formulas in percent delimiters (`%H2O%`), and combined subscripts and superscripts (`t_i^2`).


# True/False Formatting

The [fmt_tf()](../reference/GT.fmt_tf.md#great_tables.GT.fmt_tf) method transforms boolean values into visual indicators. It offers a variety of preset styles including text labels, check marks, shapes, and arrows.


``` python
tf_df = pl.DataFrame({
    "feature": ["Dark mode", "Auto-save", "Spell check", "Notifications"],
    "enabled": [True, True, False, True],
    "premium": [False, True, False, True],
})

(
    GT(tf_df, rowname_col="feature")
    .fmt_tf(columns="enabled", tf_style="check-mark")
    .fmt_tf(columns="premium", tf_style="circles")
)
```


<style>
#tsdorrogwr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tsdorrogwr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tsdorrogwr p { margin: 0; padding: 0; }
 #tsdorrogwr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tsdorrogwr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tsdorrogwr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tsdorrogwr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tsdorrogwr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tsdorrogwr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tsdorrogwr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tsdorrogwr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tsdorrogwr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tsdorrogwr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tsdorrogwr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tsdorrogwr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tsdorrogwr .gt_spanner_row { border-bottom-style: hidden; }
 #tsdorrogwr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tsdorrogwr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tsdorrogwr .gt_from_md> :first-child { margin-top: 0; }
 #tsdorrogwr .gt_from_md> :last-child { margin-bottom: 0; }
 #tsdorrogwr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tsdorrogwr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tsdorrogwr .gt_indent_1 { text-indent: 5px; }
 #tsdorrogwr .gt_indent_2 { text-indent: calc(5px * 2); }
 #tsdorrogwr .gt_indent_3 { text-indent: calc(5px * 3); }
 #tsdorrogwr .gt_indent_4 { text-indent: calc(5px * 4); }
 #tsdorrogwr .gt_indent_5 { text-indent: calc(5px * 5); }
 #tsdorrogwr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tsdorrogwr .gt_row_group_first td { border-top-width: 2px; }
 #tsdorrogwr .gt_row_group_first th { border-top-width: 2px; }
 #tsdorrogwr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tsdorrogwr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tsdorrogwr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tsdorrogwr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tsdorrogwr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tsdorrogwr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tsdorrogwr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tsdorrogwr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tsdorrogwr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tsdorrogwr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tsdorrogwr .gt_left { text-align: left; }
 #tsdorrogwr .gt_center { text-align: center; }
 #tsdorrogwr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tsdorrogwr .gt_font_normal { font-weight: normal; }
 #tsdorrogwr .gt_font_bold { font-weight: bold; }
 #tsdorrogwr .gt_font_italic { font-style: italic; }
 #tsdorrogwr .gt_super { font-size: 65%; }
 #tsdorrogwr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tsdorrogwr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tsdorrogwr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tsdorrogwr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tsdorrogwr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tsdorrogwr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|               | enabled | premium |
|---------------|---------|---------|
| Dark mode     | ✔       | ⭘       |
| Auto-save     | ✔       | ●       |
| Spell check   | ✘       | ⭘       |
| Notifications | ✔       | ●       |


The available `tf_style=` values include: `"true-false"`, `"yes-no"`, `"up-down"`, `"check-mark"`, `"circles"`, `"squares"`, `"diamonds"`, `"arrows"`, `"triangles"`, and `"triangles-lr"`.

You can also apply colors to the True/False indicators using the `colors=` argument.


``` python
(
    GT(tf_df, rowname_col="feature")
    .fmt_tf(columns="enabled", tf_style="check-mark", colors=["green", "red"])
)
```


<style>
#vlcxtxrkjf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vlcxtxrkjf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vlcxtxrkjf p { margin: 0; padding: 0; }
 #vlcxtxrkjf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vlcxtxrkjf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vlcxtxrkjf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vlcxtxrkjf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vlcxtxrkjf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vlcxtxrkjf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vlcxtxrkjf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vlcxtxrkjf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vlcxtxrkjf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vlcxtxrkjf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vlcxtxrkjf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vlcxtxrkjf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vlcxtxrkjf .gt_spanner_row { border-bottom-style: hidden; }
 #vlcxtxrkjf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vlcxtxrkjf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vlcxtxrkjf .gt_from_md> :first-child { margin-top: 0; }
 #vlcxtxrkjf .gt_from_md> :last-child { margin-bottom: 0; }
 #vlcxtxrkjf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vlcxtxrkjf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vlcxtxrkjf .gt_indent_1 { text-indent: 5px; }
 #vlcxtxrkjf .gt_indent_2 { text-indent: calc(5px * 2); }
 #vlcxtxrkjf .gt_indent_3 { text-indent: calc(5px * 3); }
 #vlcxtxrkjf .gt_indent_4 { text-indent: calc(5px * 4); }
 #vlcxtxrkjf .gt_indent_5 { text-indent: calc(5px * 5); }
 #vlcxtxrkjf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vlcxtxrkjf .gt_row_group_first td { border-top-width: 2px; }
 #vlcxtxrkjf .gt_row_group_first th { border-top-width: 2px; }
 #vlcxtxrkjf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vlcxtxrkjf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vlcxtxrkjf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vlcxtxrkjf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vlcxtxrkjf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vlcxtxrkjf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vlcxtxrkjf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vlcxtxrkjf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vlcxtxrkjf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vlcxtxrkjf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vlcxtxrkjf .gt_left { text-align: left; }
 #vlcxtxrkjf .gt_center { text-align: center; }
 #vlcxtxrkjf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vlcxtxrkjf .gt_font_normal { font-weight: normal; }
 #vlcxtxrkjf .gt_font_bold { font-weight: bold; }
 #vlcxtxrkjf .gt_font_italic { font-style: italic; }
 #vlcxtxrkjf .gt_super { font-size: 65%; }
 #vlcxtxrkjf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vlcxtxrkjf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vlcxtxrkjf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vlcxtxrkjf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vlcxtxrkjf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vlcxtxrkjf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|               | enabled                            | premium |
|---------------|------------------------------------|---------|
| Dark mode     | <span style="color:green">✔</span> | False   |
| Auto-save     | <span style="color:green">✔</span> | True    |
| Spell check   | <span style="color:red">✘</span>   | False   |
| Notifications | <span style="color:green">✔</span> | True    |


When you provide two colors, the first applies to `True` values and the second to `False` values.


# Markdown in Cells

The [fmt_markdown()](../reference/GT.fmt_markdown.md#great_tables.GT.fmt_markdown) method renders Markdown-formatted text that appears in cells. This is useful when your data contains text with emphasis, links, or other inline formatting.


``` python
md_df = pl.DataFrame({
    "package": ["polars", "pandas", "numpy"],
    "description": [
        "**Fast** DataFrame library for *Rust* and Python",
        "Flexible data analysis with **labeled** axes",
        "Fundamental package for *scientific computing*",
    ],
})

(
    GT(md_df, rowname_col="package")
    .fmt_markdown(columns="description")
)
```


<style>
#iiahptawor table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iiahptawor thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iiahptawor p { margin: 0; padding: 0; }
 #iiahptawor .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #iiahptawor .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iiahptawor .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iiahptawor .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iiahptawor .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iiahptawor .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iiahptawor .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iiahptawor .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iiahptawor .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iiahptawor .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iiahptawor .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iiahptawor .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iiahptawor .gt_spanner_row { border-bottom-style: hidden; }
 #iiahptawor .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iiahptawor .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #iiahptawor .gt_from_md> :first-child { margin-top: 0; }
 #iiahptawor .gt_from_md> :last-child { margin-bottom: 0; }
 #iiahptawor .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #iiahptawor .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #iiahptawor .gt_indent_1 { text-indent: 5px; }
 #iiahptawor .gt_indent_2 { text-indent: calc(5px * 2); }
 #iiahptawor .gt_indent_3 { text-indent: calc(5px * 3); }
 #iiahptawor .gt_indent_4 { text-indent: calc(5px * 4); }
 #iiahptawor .gt_indent_5 { text-indent: calc(5px * 5); }
 #iiahptawor .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iiahptawor .gt_row_group_first td { border-top-width: 2px; }
 #iiahptawor .gt_row_group_first th { border-top-width: 2px; }
 #iiahptawor .gt_striped { color: #333333; background-color: #F4F4F4; }
 #iiahptawor .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iiahptawor .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iiahptawor .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #iiahptawor .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iiahptawor .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iiahptawor .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iiahptawor .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iiahptawor .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iiahptawor .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iiahptawor .gt_left { text-align: left; }
 #iiahptawor .gt_center { text-align: center; }
 #iiahptawor .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iiahptawor .gt_font_normal { font-weight: normal; }
 #iiahptawor .gt_font_bold { font-weight: bold; }
 #iiahptawor .gt_font_italic { font-style: italic; }
 #iiahptawor .gt_super { font-size: 65%; }
 #iiahptawor .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iiahptawor .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #iiahptawor .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iiahptawor .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iiahptawor .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iiahptawor .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|        | description                                      |
|--------|--------------------------------------------------|
| polars | **Fast** DataFrame library for *Rust* and Python |
| pandas | Flexible data analysis with **labeled** axes     |
| numpy  | Fundamental package for *scientific computing*   |


The Markdown is converted to HTML during rendering, so standard inline Markdown syntax (bold, italic, links, code) is supported.


# Icons in Cells

The [fmt_icon()](../reference/GT.fmt_icon.md#great_tables.GT.fmt_icon) method renders Font Awesome icons based on icon names stored in cells. This is a visually engaging way to represent categories, statuses, or types.


``` python
icon_df = pl.DataFrame({
    "platform": ["Web", "Mobile", "Desktop"],
    "icon_name": ["globe", "mobile", "desktop"],
    "users": [45000, 32000, 12000],
})

(
    GT(icon_df, rowname_col="platform")
    .fmt_icon(columns="icon_name", fill_color="steelblue")
    .fmt_number(columns="users", compact=True)
)
```


<style>
#tehqrgmhmv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tehqrgmhmv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tehqrgmhmv p { margin: 0; padding: 0; }
 #tehqrgmhmv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tehqrgmhmv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tehqrgmhmv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tehqrgmhmv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tehqrgmhmv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tehqrgmhmv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tehqrgmhmv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tehqrgmhmv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tehqrgmhmv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tehqrgmhmv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tehqrgmhmv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tehqrgmhmv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tehqrgmhmv .gt_spanner_row { border-bottom-style: hidden; }
 #tehqrgmhmv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tehqrgmhmv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tehqrgmhmv .gt_from_md> :first-child { margin-top: 0; }
 #tehqrgmhmv .gt_from_md> :last-child { margin-bottom: 0; }
 #tehqrgmhmv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tehqrgmhmv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tehqrgmhmv .gt_indent_1 { text-indent: 5px; }
 #tehqrgmhmv .gt_indent_2 { text-indent: calc(5px * 2); }
 #tehqrgmhmv .gt_indent_3 { text-indent: calc(5px * 3); }
 #tehqrgmhmv .gt_indent_4 { text-indent: calc(5px * 4); }
 #tehqrgmhmv .gt_indent_5 { text-indent: calc(5px * 5); }
 #tehqrgmhmv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tehqrgmhmv .gt_row_group_first td { border-top-width: 2px; }
 #tehqrgmhmv .gt_row_group_first th { border-top-width: 2px; }
 #tehqrgmhmv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tehqrgmhmv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tehqrgmhmv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tehqrgmhmv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tehqrgmhmv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tehqrgmhmv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tehqrgmhmv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tehqrgmhmv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tehqrgmhmv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tehqrgmhmv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tehqrgmhmv .gt_left { text-align: left; }
 #tehqrgmhmv .gt_center { text-align: center; }
 #tehqrgmhmv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tehqrgmhmv .gt_font_normal { font-weight: normal; }
 #tehqrgmhmv .gt_font_bold { font-weight: bold; }
 #tehqrgmhmv .gt_font_italic { font-style: italic; }
 #tehqrgmhmv .gt_super { font-size: 65%; }
 #tehqrgmhmv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tehqrgmhmv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tehqrgmhmv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tehqrgmhmv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tehqrgmhmv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tehqrgmhmv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|  | icon_name | users |
|----|----|----|
| Web | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpzdGVlbGJsdWU7ZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MS4wZW07cG9zaXRpb246cmVsYXRpdmU7dmVydGljYWwtYWxpZ246LTAuMTI1ZW07b3ZlcmZsb3c6dmlzaWJsZTsiPiAgPHBhdGggZD0iTTM1MiAyNTZjMCAyMi4yLTEuMiA0My42LTMuMyA2NEgxNjMuM2MtMi4yLTIwLjQtMy4zLTQxLjgtMy4zLTY0czEuMi00My42IDMuMy02NEgzNDguN2MyLjIgMjAuNCAzLjMgNDEuOCAzLjMgNjR6bTI4LjgtNjRINTAzLjljNS4zIDIwLjUgOC4xIDQxLjkgOC4xIDY0cy0yLjggNDMuNS04LjEgNjRIMzgwLjhjMi4xLTIwLjYgMy4yLTQyIDMuMi02NHMtMS4xLTQzLjQtMy4yLTY0em0xMTIuNi0zMkgzNzYuN2MtMTAtNjMuOS0yOS44LTExNy40LTU1LjMtMTUxLjZjNzguMyAyMC43IDE0MiA3Ny41IDE3MS45IDE1MS42em0tMTQ5LjEgMEgxNjcuN2M2LjEtMzYuNCAxNS41LTY4LjYgMjctOTQuN2MxMC41LTIzLjYgMjIuMi00MC43IDMzLjUtNTEuNUMyMzkuNCAzLjIgMjQ4LjcgMCAyNTYgMHMxNi42IDMuMiAyNy44IDEzLjhjMTEuMyAxMC44IDIzIDI3LjkgMzMuNSA1MS41YzExLjYgMjYgMjEgNTguMiAyNyA5NC43em0tMjA5IDBIMTguNkM0OC42IDg1LjkgMTEyLjIgMjkuMSAxOTAuNiA4LjRDMTY1LjEgNDIuNiAxNDUuMyA5Ni4xIDEzNS4zIDE2MHpNOC4xIDE5MkgxMzEuMmMtMi4xIDIwLjYtMy4yIDQyLTMuMiA2NHMxLjEgNDMuNCAzLjIgNjRIOC4xQzIuOCAyOTkuNSAwIDI3OC4xIDAgMjU2czIuOC00My41IDguMS02NHpNMTk0LjcgNDQ2LjZjLTExLjYtMjYtMjAuOS01OC4yLTI3LTk0LjZIMzQ0LjNjLTYuMSAzNi40LTE1LjUgNjguNi0yNyA5NC42Yy0xMC41IDIzLjYtMjIuMiA0MC43LTMzLjUgNTEuNUMyNzIuNiA1MDguOCAyNjMuMyA1MTIgMjU2IDUxMnMtMTYuNi0zLjItMjcuOC0xMy44Yy0xMS4zLTEwLjgtMjMtMjcuOS0zMy41LTUxLjV6TTEzNS4zIDM1MmMxMCA2My45IDI5LjggMTE3LjQgNTUuMyAxNTEuNkMxMTIuMiA0ODIuOSA0OC42IDQyNi4xIDE4LjYgMzUySDEzNS4zem0zNTguMSAwYy0zMCA3NC4xLTkzLjYgMTMwLjktMTcxLjkgMTUxLjZjMjUuNS0zNC4yIDQ1LjItODcuNyA1NS4zLTE1MS42SDQ5My40eiIgLz48L3N2Zz4=" class="fa" /></span> | 45.00K |
| Mobile | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpzdGVlbGJsdWU7ZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MC43NWVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik04MCAwQzQ0LjcgMCAxNiAyOC43IDE2IDY0VjQ0OGMwIDM1LjMgMjguNyA2NCA2NCA2NEgzMDRjMzUuMyAwIDY0LTI4LjcgNjQtNjRWNjRjMC0zNS4zLTI4LjctNjQtNjQtNjRIODB6bTgwIDQzMmg2NGM4LjggMCAxNiA3LjIgMTYgMTZzLTcuMiAxNi0xNiAxNkgxNjBjLTguOCAwLTE2LTcuMi0xNi0xNnM3LjItMTYgMTYtMTZ6IiAvPjwvc3ZnPg==" class="fa" /></span> | 32.00K |
| Desktop | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTc2IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpzdGVlbGJsdWU7ZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MS4xMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik02NCAwQzI4LjcgMCAwIDI4LjcgMCA2NFYzNTJjMCAzNS4zIDI4LjcgNjQgNjQgNjRIMjQwbC0xMC43IDMySDE2MGMtMTcuNyAwLTMyIDE0LjMtMzIgMzJzMTQuMyAzMiAzMiAzMkg0MTZjMTcuNyAwIDMyLTE0LjMgMzItMzJzLTE0LjMtMzItMzItMzJIMzQ2LjdMMzM2IDQxNkg1MTJjMzUuMyAwIDY0LTI4LjcgNjQtNjRWNjRjMC0zNS4zLTI4LjctNjQtNjQtNjRINjR6TTUxMiA2NFYyODhINjRWNjRINTEyeiIgLz48L3N2Zz4=" class="fa" /></span> | 12.00K |


The `fill_color=` argument accepts a single color (applied to all icons) or a dictionary mapping icon names to specific colors.


``` python
(
    GT(icon_df, rowname_col="platform")
    .fmt_icon(
        columns="icon_name",
        fill_color={"globe": "royalblue", "mobile": "forestgreen", "desktop": "slategray"}
    )
)
```


<style>
#hddqlyzxex table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hddqlyzxex thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hddqlyzxex p { margin: 0; padding: 0; }
 #hddqlyzxex .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hddqlyzxex .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hddqlyzxex .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hddqlyzxex .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hddqlyzxex .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hddqlyzxex .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hddqlyzxex .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hddqlyzxex .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hddqlyzxex .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hddqlyzxex .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hddqlyzxex .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hddqlyzxex .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hddqlyzxex .gt_spanner_row { border-bottom-style: hidden; }
 #hddqlyzxex .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hddqlyzxex .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hddqlyzxex .gt_from_md> :first-child { margin-top: 0; }
 #hddqlyzxex .gt_from_md> :last-child { margin-bottom: 0; }
 #hddqlyzxex .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hddqlyzxex .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hddqlyzxex .gt_indent_1 { text-indent: 5px; }
 #hddqlyzxex .gt_indent_2 { text-indent: calc(5px * 2); }
 #hddqlyzxex .gt_indent_3 { text-indent: calc(5px * 3); }
 #hddqlyzxex .gt_indent_4 { text-indent: calc(5px * 4); }
 #hddqlyzxex .gt_indent_5 { text-indent: calc(5px * 5); }
 #hddqlyzxex .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hddqlyzxex .gt_row_group_first td { border-top-width: 2px; }
 #hddqlyzxex .gt_row_group_first th { border-top-width: 2px; }
 #hddqlyzxex .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hddqlyzxex .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hddqlyzxex .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hddqlyzxex .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hddqlyzxex .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hddqlyzxex .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hddqlyzxex .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hddqlyzxex .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hddqlyzxex .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hddqlyzxex .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hddqlyzxex .gt_left { text-align: left; }
 #hddqlyzxex .gt_center { text-align: center; }
 #hddqlyzxex .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hddqlyzxex .gt_font_normal { font-weight: normal; }
 #hddqlyzxex .gt_font_bold { font-weight: bold; }
 #hddqlyzxex .gt_font_italic { font-style: italic; }
 #hddqlyzxex .gt_super { font-size: 65%; }
 #hddqlyzxex .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hddqlyzxex .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hddqlyzxex .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hddqlyzxex .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hddqlyzxex .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hddqlyzxex .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|  | icon_name | users |
|----|----|----|
| Web | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpyb3lhbGJsdWU7ZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MS4wZW07cG9zaXRpb246cmVsYXRpdmU7dmVydGljYWwtYWxpZ246LTAuMTI1ZW07b3ZlcmZsb3c6dmlzaWJsZTsiPiAgPHBhdGggZD0iTTM1MiAyNTZjMCAyMi4yLTEuMiA0My42LTMuMyA2NEgxNjMuM2MtMi4yLTIwLjQtMy4zLTQxLjgtMy4zLTY0czEuMi00My42IDMuMy02NEgzNDguN2MyLjIgMjAuNCAzLjMgNDEuOCAzLjMgNjR6bTI4LjgtNjRINTAzLjljNS4zIDIwLjUgOC4xIDQxLjkgOC4xIDY0cy0yLjggNDMuNS04LjEgNjRIMzgwLjhjMi4xLTIwLjYgMy4yLTQyIDMuMi02NHMtMS4xLTQzLjQtMy4yLTY0em0xMTIuNi0zMkgzNzYuN2MtMTAtNjMuOS0yOS44LTExNy40LTU1LjMtMTUxLjZjNzguMyAyMC43IDE0MiA3Ny41IDE3MS45IDE1MS42em0tMTQ5LjEgMEgxNjcuN2M2LjEtMzYuNCAxNS41LTY4LjYgMjctOTQuN2MxMC41LTIzLjYgMjIuMi00MC43IDMzLjUtNTEuNUMyMzkuNCAzLjIgMjQ4LjcgMCAyNTYgMHMxNi42IDMuMiAyNy44IDEzLjhjMTEuMyAxMC44IDIzIDI3LjkgMzMuNSA1MS41YzExLjYgMjYgMjEgNTguMiAyNyA5NC43em0tMjA5IDBIMTguNkM0OC42IDg1LjkgMTEyLjIgMjkuMSAxOTAuNiA4LjRDMTY1LjEgNDIuNiAxNDUuMyA5Ni4xIDEzNS4zIDE2MHpNOC4xIDE5MkgxMzEuMmMtMi4xIDIwLjYtMy4yIDQyLTMuMiA2NHMxLjEgNDMuNCAzLjIgNjRIOC4xQzIuOCAyOTkuNSAwIDI3OC4xIDAgMjU2czIuOC00My41IDguMS02NHpNMTk0LjcgNDQ2LjZjLTExLjYtMjYtMjAuOS01OC4yLTI3LTk0LjZIMzQ0LjNjLTYuMSAzNi40LTE1LjUgNjguNi0yNyA5NC42Yy0xMC41IDIzLjYtMjIuMiA0MC43LTMzLjUgNTEuNUMyNzIuNiA1MDguOCAyNjMuMyA1MTIgMjU2IDUxMnMtMTYuNi0zLjItMjcuOC0xMy44Yy0xMS4zLTEwLjgtMjMtMjcuOS0zMy41LTUxLjV6TTEzNS4zIDM1MmMxMCA2My45IDI5LjggMTE3LjQgNTUuMyAxNTEuNkMxMTIuMiA0ODIuOSA0OC42IDQyNi4xIDE4LjYgMzUySDEzNS4zem0zNTguMSAwYy0zMCA3NC4xLTkzLjYgMTMwLjktMTcxLjkgMTUxLjZjMjUuNS0zNC4yIDQ1LjItODcuNyA1NS4zLTE1MS42SDQ5My40eiIgLz48L3N2Zz4=" class="fa" /></span> | 45000 |
| Mobile | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpmb3Jlc3RncmVlbjtmaWxsLW9wYWNpdHk6Tm9uZTtzdHJva2Utd2lkdGg6MXB4O3N0cm9rZS1vcGFjaXR5Ok5vbmU7aGVpZ2h0OjFlbTt3aWR0aDowLjc1ZW07cG9zaXRpb246cmVsYXRpdmU7dmVydGljYWwtYWxpZ246LTAuMTI1ZW07b3ZlcmZsb3c6dmlzaWJsZTsiPiAgPHBhdGggZD0iTTgwIDBDNDQuNyAwIDE2IDI4LjcgMTYgNjRWNDQ4YzAgMzUuMyAyOC43IDY0IDY0IDY0SDMwNGMzNS4zIDAgNjQtMjguNyA2NC02NFY2NGMwLTM1LjMtMjguNy02NC02NC02NEg4MHptODAgNDMyaDY0YzguOCAwIDE2IDcuMiAxNiAxNnMtNy4yIDE2LTE2IDE2SDE2MGMtOC44IDAtMTYtNy4yLTE2LTE2czcuMi0xNiAxNi0xNnoiIC8+PC9zdmc+" class="fa" /></span> | 32000 |
| Desktop | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTc2IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpzbGF0ZWdyYXk7ZmlsbC1vcGFjaXR5Ok5vbmU7c3Ryb2tlLXdpZHRoOjFweDtzdHJva2Utb3BhY2l0eTpOb25lO2hlaWdodDoxZW07d2lkdGg6MS4xMmVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik02NCAwQzI4LjcgMCAwIDI4LjcgMCA2NFYzNTJjMCAzNS4zIDI4LjcgNjQgNjQgNjRIMjQwbC0xMC43IDMySDE2MGMtMTcuNyAwLTMyIDE0LjMtMzIgMzJzMTQuMyAzMiAzMiAzMkg0MTZjMTcuNyAwIDMyLTE0LjMgMzItMzJzLTE0LjMtMzItMzItMzJIMzQ2LjdMMzM2IDQxNkg1MTJjMzUuMyAwIDY0LTI4LjcgNjQtNjRWNjRjMC0zNS4zLTI4LjctNjQtNjQtNjRINjR6TTUxMiA2NFYyODhINjRWNjRINTEyeiIgLz48L3N2Zz4=" class="fa" /></span> | 12000 |


Using a dictionary for `fill_color=` lets you assign semantically meaningful colors to each icon, making the visual distinction immediate.


# Country Flags

The [fmt_flag()](../reference/GT.fmt_flag.md#great_tables.GT.fmt_flag) method generates flag icons from ISO 3166-1 country codes (two- or three-letter codes). This is useful for international datasets.


``` python
country_df = pl.DataFrame({
    "country_code": ["US", "GB", "JP", "DE", "BR"],
    "country": ["United States", "United Kingdom", "Japan", "Germany", "Brazil"],
    "gdp_trillion": [25.5, 3.1, 4.2, 4.1, 1.9],
})

(
    GT(country_df, rowname_col="country")
    .fmt_flag(columns="country_code")
    .fmt_number(columns="gdp_trillion", decimals=1)
    .cols_label(country_code="Flag", gdp_trillion="GDP (USD trillions)")
)
```


<style>
#vtlflgtfgu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vtlflgtfgu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vtlflgtfgu p { margin: 0; padding: 0; }
 #vtlflgtfgu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vtlflgtfgu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vtlflgtfgu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vtlflgtfgu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vtlflgtfgu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vtlflgtfgu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vtlflgtfgu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vtlflgtfgu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vtlflgtfgu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vtlflgtfgu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vtlflgtfgu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vtlflgtfgu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vtlflgtfgu .gt_spanner_row { border-bottom-style: hidden; }
 #vtlflgtfgu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vtlflgtfgu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vtlflgtfgu .gt_from_md> :first-child { margin-top: 0; }
 #vtlflgtfgu .gt_from_md> :last-child { margin-bottom: 0; }
 #vtlflgtfgu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vtlflgtfgu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vtlflgtfgu .gt_indent_1 { text-indent: 5px; }
 #vtlflgtfgu .gt_indent_2 { text-indent: calc(5px * 2); }
 #vtlflgtfgu .gt_indent_3 { text-indent: calc(5px * 3); }
 #vtlflgtfgu .gt_indent_4 { text-indent: calc(5px * 4); }
 #vtlflgtfgu .gt_indent_5 { text-indent: calc(5px * 5); }
 #vtlflgtfgu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vtlflgtfgu .gt_row_group_first td { border-top-width: 2px; }
 #vtlflgtfgu .gt_row_group_first th { border-top-width: 2px; }
 #vtlflgtfgu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vtlflgtfgu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vtlflgtfgu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vtlflgtfgu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vtlflgtfgu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vtlflgtfgu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vtlflgtfgu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vtlflgtfgu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vtlflgtfgu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vtlflgtfgu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vtlflgtfgu .gt_left { text-align: left; }
 #vtlflgtfgu .gt_center { text-align: center; }
 #vtlflgtfgu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vtlflgtfgu .gt_font_normal { font-weight: normal; }
 #vtlflgtfgu .gt_font_bold { font-weight: bold; }
 #vtlflgtfgu .gt_font_italic { font-style: italic; }
 #vtlflgtfgu .gt_super { font-size: 65%; }
 #vtlflgtfgu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vtlflgtfgu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vtlflgtfgu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vtlflgtfgu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vtlflgtfgu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vtlflgtfgu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|  | Flag | GDP (USD trillions) |
|----|----|----|
| United States | <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+VW5pdGVkIFN0YXRlczwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTI1NiAwaDI1NnY2NGwtMzIgMzIgMzIgMzJ2NjRsLTMyIDMyIDMyIDMydjY0bC0zMiAzMiAzMiAzMnY2NGwtMjU2IDMyTDAgNDQ4di02NGwzMi0zMi0zMi0zMnYtNjR6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0yMjQgNjRoMjg4djY0SDIyNFptMCAxMjhoMjg4djY0SDI1NlpNMCAzMjBoNTEydjY0SDBabTAgMTI4aDUxMnY2NEgwWiIgLz48cGF0aCBmaWxsPSIjMDA1MmI0IiBkPSJNMCAwaDI1NnYyNTZIMFoiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0ibTE4NyAyNDMgNTctNDFoLTcwbDU3IDQxLTIyLTY3em0tODEgMCA1Ny00MUg5M2w1NyA0MS0yMi02N3ptLTgxIDAgNTctNDFIMTJsNTcgNDEtMjItNjd6bTE2Mi04MSA1Ny00MWgtNzBsNTcgNDEtMjItNjd6bS04MSAwIDU3LTQxSDkzbDU3IDQxLTIyLTY3em0tODEgMCA1Ny00MUgxMmw1NyA0MS0yMi02N1ptMTYyLTgyIDU3LTQxaC03MGw1NyA0MS0yMi02N1ptLTgxIDAgNTctNDFIOTNsNTcgNDEtMjItNjd6bS04MSAwIDU3LTQxSDEybDU3IDQxLTIyLTY3WiIgLz48L2c+PC9zdmc+)</span> | 25.5 |
| United Kingdom | <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+VW5pdGVkIEtpbmdkb208L3RpdGxlPjxtYXNrIGlkPSJhIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Im0wIDAgOCAyMi04IDIzdjIzbDMyIDU0LTMyIDU0djMybDMyIDQ4LTMyIDQ4djMybDMyIDU0LTMyIDU0djY4bDIyLTggMjMgOGgyM2w1NC0zMiA1NCAzMmgzMmw0OC0zMiA0OCAzMmgzMmw1NC0zMiA1NCAzMmg2OGwtOC0yMiA4LTIzdi0yM2wtMzItNTQgMzItNTR2LTMybC0zMi00OCAzMi00OHYtMzJsLTMyLTU0IDMyLTU0VjBsLTIyIDgtMjMtOGgtMjNsLTU0IDMyLTU0LTMyaC0zMmwtNDggMzItNDgtMzJoLTMybC01NCAzMkw2OCAwSDB6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0zMzYgMHYxMDhMNDQ0IDBabTE3NiA2OEw0MDQgMTc2aDEwOHpNMCAxNzZoMTA4TDAgNjhaTTY4IDBsMTA4IDEwOFYwWm0xMDggNTEyVjQwNEw2OCA1MTJaTTAgNDQ0bDEwOC0xMDhIMFptNTEyLTEwOEg0MDRsMTA4IDEwOFptLTY4IDE3NkwzMzYgNDA0djEwOHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMHY0NWwxMzEgMTMxaDQ1TDAgMHptMjA4IDB2MjA4SDB2OTZoMjA4djIwOGg5NlYzMDRoMjA4di05NkgzMDRWMGgtOTZ6bTI1OSAwTDMzNiAxMzF2NDVMNTEyIDBoLTQ1ek0xNzYgMzM2IDAgNTEyaDQ1bDEzMS0xMzF2LTQ1em0xNjAgMCAxNzYgMTc2di00NUwzODEgMzM2aC00NXoiIC8+PC9nPjwvc3ZnPg==)</span> | 3.1 |
| Japan | <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+SmFwYW48L3RpdGxlPjxtYXNrIGlkPSJhIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0wIDBoNTEydjUxMkgweiIgLz48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjExMS4zIiBmaWxsPSIjZDgwMDI3Ij48L2NpcmNsZT48L2c+PC9zdmc+)</span> | 4.2 |
| Germany | <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+R2VybWFueTwvdGl0bGU+PG1hc2sgaWQ9ImEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNhKSI+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0ibTAgMzQ1IDI1Ni43LTI1LjVMNTEyIDM0NXYxNjdIMHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0ibTAgMTY3IDI1NS0yMyAyNTcgMjN2MTc4SDB6IiAvPjxwYXRoIGZpbGw9IiMzMzMiIGQ9Ik0wIDBoNTEydjE2N0gweiIgLz48L2c+PC9zdmc+)</span> | 4.1 |
| Brazil | <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGFyaWEtaGlkZGVuPSJ0cnVlIiByb2xlPSJpbWciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+QnJhemlsPC90aXRsZT48bWFzayBpZD0iYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2EpIj48cGF0aCBmaWxsPSIjNmRhNTQ0IiBkPSJNMCAwaDUxMnY1MTJIMHoiIC8+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0iTTI1NiAxMDAuMiA0NjcuNSAyNTYgMjU2IDQxMS44IDQ0LjUgMjU2eiIgLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMTc0LjIgMjIxYTg3IDg3IDAgMCAwLTcuMiAzNi4zbDE2MiA0OS44YTg4LjUgODguNSAwIDAgMCAxNC40LTM0Yy00MC42LTY1LjMtMTE5LjctODAuMy0xNjkuMS01MnoiIC8+PHBhdGggZmlsbD0iIzAwNTJiNCIgZD0iTTI1NS43IDE2N2E4OSA4OSAwIDAgMC00MS45IDEwLjYgODkgODkgMCAwIDAtMzkuNiA0My40IDE4MS43IDE4MS43IDAgMCAxIDE2OS4xIDUyLjIgODkgODkgMCAwIDAtOS01OS40IDg5IDg5IDAgMCAwLTc4LjYtNDYuOHpNMjEyIDI1MC41YTE0OSAxNDkgMCAwIDAtNDUgNi44IDg5IDg5IDAgMCAwIDEwLjUgNDAuOSA4OSA4OSAwIDAgMCAxMjAuNiAzNi4yIDg5IDg5IDAgMCAwIDMwLjctMjcuM0ExNTEgMTUxIDAgMCAwIDIxMiAyNTAuNXoiIC8+PC9nPjwvc3ZnPg==)</span> | 1.9 |


The flags render as small inline images with a hover tooltip showing the country name (controlled by `use_title=`).


# Images in Cells

The [fmt_image()](../reference/GT.fmt_image.md#great_tables.GT.fmt_image) method renders image paths or URLs as inline images within cells. This is useful for product catalogs, team rosters, or any dataset where visual identification matters.

``` python
img_df = pl.DataFrame({
    "planet": ["Earth", "Mars", "Jupiter"],
    "image_file": ["earth.png", "mars.png", "jupiter.png"],
    "diameter_km": [12742, 6779, 139820],
})

(
    GT(img_df, rowname_col="planet")
    .fmt_image(columns="image_file", path="images/", height="40px")
    .fmt_number(columns="diameter_km", use_seps=True)
)
```

The `path=` argument provides a common prefix for all file references, and `height=`/`width=` control the rendered dimensions. When `encode=True` (the default), local image files are base64-encoded directly into the HTML output, making the table self-contained.


# Custom Formatting with [fmt()](../reference/GT.fmt.md#great_tables.GT.fmt)

When none of the built-in formatters fit your needs, the generic [fmt()](../reference/GT.fmt.md#great_tables.GT.fmt) method lets you supply any function as a formatter. The function receives a raw cell value and should return a formatted string.


``` python
def format_score(value):
    """Convert a 0-100 score to a letter grade."""
    if value >= 90:
        return "A"
    elif value >= 80:
        return "B"
    elif value >= 70:
        return "C"
    elif value >= 60:
        return "D"
    else:
        return "F"

grades_df = pl.DataFrame({
    "student": ["Alice", "Bob", "Charlie", "Diana"],
    "score": [95, 82, 67, 91],
})

(
    GT(grades_df, rowname_col="student")
    .fmt(fns=format_score, columns="score")
)
```


<style>
#wdmnxbjrxe table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wdmnxbjrxe thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wdmnxbjrxe p { margin: 0; padding: 0; }
 #wdmnxbjrxe .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wdmnxbjrxe .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wdmnxbjrxe .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wdmnxbjrxe .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wdmnxbjrxe .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wdmnxbjrxe .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wdmnxbjrxe .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wdmnxbjrxe .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wdmnxbjrxe .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wdmnxbjrxe .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wdmnxbjrxe .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wdmnxbjrxe .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wdmnxbjrxe .gt_spanner_row { border-bottom-style: hidden; }
 #wdmnxbjrxe .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wdmnxbjrxe .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wdmnxbjrxe .gt_from_md> :first-child { margin-top: 0; }
 #wdmnxbjrxe .gt_from_md> :last-child { margin-bottom: 0; }
 #wdmnxbjrxe .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wdmnxbjrxe .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wdmnxbjrxe .gt_indent_1 { text-indent: 5px; }
 #wdmnxbjrxe .gt_indent_2 { text-indent: calc(5px * 2); }
 #wdmnxbjrxe .gt_indent_3 { text-indent: calc(5px * 3); }
 #wdmnxbjrxe .gt_indent_4 { text-indent: calc(5px * 4); }
 #wdmnxbjrxe .gt_indent_5 { text-indent: calc(5px * 5); }
 #wdmnxbjrxe .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wdmnxbjrxe .gt_row_group_first td { border-top-width: 2px; }
 #wdmnxbjrxe .gt_row_group_first th { border-top-width: 2px; }
 #wdmnxbjrxe .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wdmnxbjrxe .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wdmnxbjrxe .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wdmnxbjrxe .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wdmnxbjrxe .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wdmnxbjrxe .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wdmnxbjrxe .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wdmnxbjrxe .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wdmnxbjrxe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wdmnxbjrxe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wdmnxbjrxe .gt_left { text-align: left; }
 #wdmnxbjrxe .gt_center { text-align: center; }
 #wdmnxbjrxe .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wdmnxbjrxe .gt_font_normal { font-weight: normal; }
 #wdmnxbjrxe .gt_font_bold { font-weight: bold; }
 #wdmnxbjrxe .gt_font_italic { font-style: italic; }
 #wdmnxbjrxe .gt_super { font-size: 65%; }
 #wdmnxbjrxe .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wdmnxbjrxe .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wdmnxbjrxe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wdmnxbjrxe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wdmnxbjrxe .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wdmnxbjrxe .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|         | score |
|---------|-------|
| Alice   | A     |
| Bob     | B     |
| Charlie | D     |
| Diana   | A     |


The [fmt()](../reference/GT.fmt.md#great_tables.GT.fmt) method is the escape hatch for any formatting logic that the specialized `fmt_*()` methods do not cover. Your function can return plain text or HTML strings for rich formatting.

[fmt()](../reference/GT.fmt.md#great_tables.GT.fmt) is what makes **Great Tables**' formatting system fully extensible. Any transformation you can express in Python (lookups, conditional logic, external API calls) can become a cell formatter. If you find yourself writing the same custom formatter repeatedly, consider wrapping it in a reusable function and sharing it across tables. This is exactly the pattern described in the [Extending Great Tables](extensions.md) page.

The formatting methods in **Great Tables** cover a wide spectrum of data types and presentation needs. From scientific notation to country flags, from boolean indicators to custom functions, you have the tools to make every column in your table look exactly right for its audience and context.
