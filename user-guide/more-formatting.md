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
#djobukkymc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#djobukkymc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#djobukkymc p { margin: 0; padding: 0; }
 #djobukkymc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #djobukkymc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #djobukkymc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #djobukkymc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #djobukkymc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #djobukkymc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #djobukkymc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #djobukkymc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #djobukkymc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #djobukkymc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #djobukkymc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #djobukkymc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #djobukkymc .gt_spanner_row { border-bottom-style: hidden; }
 #djobukkymc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #djobukkymc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #djobukkymc .gt_from_md> :first-child { margin-top: 0; }
 #djobukkymc .gt_from_md> :last-child { margin-bottom: 0; }
 #djobukkymc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #djobukkymc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #djobukkymc .gt_indent_1 { text-indent: 5px; }
 #djobukkymc .gt_indent_2 { text-indent: calc(5px * 2); }
 #djobukkymc .gt_indent_3 { text-indent: calc(5px * 3); }
 #djobukkymc .gt_indent_4 { text-indent: calc(5px * 4); }
 #djobukkymc .gt_indent_5 { text-indent: calc(5px * 5); }
 #djobukkymc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #djobukkymc .gt_row_group_first td { border-top-width: 2px; }
 #djobukkymc .gt_row_group_first th { border-top-width: 2px; }
 #djobukkymc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #djobukkymc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #djobukkymc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #djobukkymc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #djobukkymc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #djobukkymc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #djobukkymc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #djobukkymc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #djobukkymc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #djobukkymc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #djobukkymc .gt_left { text-align: left; }
 #djobukkymc .gt_center { text-align: center; }
 #djobukkymc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #djobukkymc .gt_font_normal { font-weight: normal; }
 #djobukkymc .gt_font_bold { font-weight: bold; }
 #djobukkymc .gt_font_italic { font-style: italic; }
 #djobukkymc .gt_super { font-size: 65%; }
 #djobukkymc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #djobukkymc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #djobukkymc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #djobukkymc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #djobukkymc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #djobukkymc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ycbutmnixv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ycbutmnixv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ycbutmnixv p { margin: 0; padding: 0; }
 #ycbutmnixv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ycbutmnixv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ycbutmnixv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ycbutmnixv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ycbutmnixv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ycbutmnixv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ycbutmnixv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ycbutmnixv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ycbutmnixv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ycbutmnixv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ycbutmnixv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ycbutmnixv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ycbutmnixv .gt_spanner_row { border-bottom-style: hidden; }
 #ycbutmnixv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ycbutmnixv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ycbutmnixv .gt_from_md> :first-child { margin-top: 0; }
 #ycbutmnixv .gt_from_md> :last-child { margin-bottom: 0; }
 #ycbutmnixv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ycbutmnixv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ycbutmnixv .gt_indent_1 { text-indent: 5px; }
 #ycbutmnixv .gt_indent_2 { text-indent: calc(5px * 2); }
 #ycbutmnixv .gt_indent_3 { text-indent: calc(5px * 3); }
 #ycbutmnixv .gt_indent_4 { text-indent: calc(5px * 4); }
 #ycbutmnixv .gt_indent_5 { text-indent: calc(5px * 5); }
 #ycbutmnixv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ycbutmnixv .gt_row_group_first td { border-top-width: 2px; }
 #ycbutmnixv .gt_row_group_first th { border-top-width: 2px; }
 #ycbutmnixv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ycbutmnixv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ycbutmnixv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ycbutmnixv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ycbutmnixv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ycbutmnixv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ycbutmnixv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ycbutmnixv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ycbutmnixv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ycbutmnixv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ycbutmnixv .gt_left { text-align: left; }
 #ycbutmnixv .gt_center { text-align: center; }
 #ycbutmnixv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ycbutmnixv .gt_font_normal { font-weight: normal; }
 #ycbutmnixv .gt_font_bold { font-weight: bold; }
 #ycbutmnixv .gt_font_italic { font-style: italic; }
 #ycbutmnixv .gt_super { font-size: 65%; }
 #ycbutmnixv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ycbutmnixv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ycbutmnixv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ycbutmnixv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ycbutmnixv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ycbutmnixv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#nyinzrqsuz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nyinzrqsuz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nyinzrqsuz p { margin: 0; padding: 0; }
 #nyinzrqsuz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nyinzrqsuz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nyinzrqsuz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nyinzrqsuz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nyinzrqsuz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nyinzrqsuz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nyinzrqsuz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nyinzrqsuz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nyinzrqsuz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nyinzrqsuz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nyinzrqsuz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nyinzrqsuz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nyinzrqsuz .gt_spanner_row { border-bottom-style: hidden; }
 #nyinzrqsuz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nyinzrqsuz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nyinzrqsuz .gt_from_md> :first-child { margin-top: 0; }
 #nyinzrqsuz .gt_from_md> :last-child { margin-bottom: 0; }
 #nyinzrqsuz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nyinzrqsuz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nyinzrqsuz .gt_indent_1 { text-indent: 5px; }
 #nyinzrqsuz .gt_indent_2 { text-indent: calc(5px * 2); }
 #nyinzrqsuz .gt_indent_3 { text-indent: calc(5px * 3); }
 #nyinzrqsuz .gt_indent_4 { text-indent: calc(5px * 4); }
 #nyinzrqsuz .gt_indent_5 { text-indent: calc(5px * 5); }
 #nyinzrqsuz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nyinzrqsuz .gt_row_group_first td { border-top-width: 2px; }
 #nyinzrqsuz .gt_row_group_first th { border-top-width: 2px; }
 #nyinzrqsuz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nyinzrqsuz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nyinzrqsuz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nyinzrqsuz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nyinzrqsuz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nyinzrqsuz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nyinzrqsuz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nyinzrqsuz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nyinzrqsuz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nyinzrqsuz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nyinzrqsuz .gt_left { text-align: left; }
 #nyinzrqsuz .gt_center { text-align: center; }
 #nyinzrqsuz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nyinzrqsuz .gt_font_normal { font-weight: normal; }
 #nyinzrqsuz .gt_font_bold { font-weight: bold; }
 #nyinzrqsuz .gt_font_italic { font-style: italic; }
 #nyinzrqsuz .gt_super { font-size: 65%; }
 #nyinzrqsuz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nyinzrqsuz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nyinzrqsuz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nyinzrqsuz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nyinzrqsuz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nyinzrqsuz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dmgyjpstpo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dmgyjpstpo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dmgyjpstpo p { margin: 0; padding: 0; }
 #dmgyjpstpo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dmgyjpstpo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dmgyjpstpo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dmgyjpstpo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dmgyjpstpo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dmgyjpstpo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dmgyjpstpo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dmgyjpstpo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dmgyjpstpo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dmgyjpstpo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dmgyjpstpo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dmgyjpstpo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dmgyjpstpo .gt_spanner_row { border-bottom-style: hidden; }
 #dmgyjpstpo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dmgyjpstpo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dmgyjpstpo .gt_from_md> :first-child { margin-top: 0; }
 #dmgyjpstpo .gt_from_md> :last-child { margin-bottom: 0; }
 #dmgyjpstpo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dmgyjpstpo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dmgyjpstpo .gt_indent_1 { text-indent: 5px; }
 #dmgyjpstpo .gt_indent_2 { text-indent: calc(5px * 2); }
 #dmgyjpstpo .gt_indent_3 { text-indent: calc(5px * 3); }
 #dmgyjpstpo .gt_indent_4 { text-indent: calc(5px * 4); }
 #dmgyjpstpo .gt_indent_5 { text-indent: calc(5px * 5); }
 #dmgyjpstpo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dmgyjpstpo .gt_row_group_first td { border-top-width: 2px; }
 #dmgyjpstpo .gt_row_group_first th { border-top-width: 2px; }
 #dmgyjpstpo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dmgyjpstpo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dmgyjpstpo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dmgyjpstpo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dmgyjpstpo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dmgyjpstpo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dmgyjpstpo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dmgyjpstpo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dmgyjpstpo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dmgyjpstpo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dmgyjpstpo .gt_left { text-align: left; }
 #dmgyjpstpo .gt_center { text-align: center; }
 #dmgyjpstpo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dmgyjpstpo .gt_font_normal { font-weight: normal; }
 #dmgyjpstpo .gt_font_bold { font-weight: bold; }
 #dmgyjpstpo .gt_font_italic { font-style: italic; }
 #dmgyjpstpo .gt_super { font-size: 65%; }
 #dmgyjpstpo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dmgyjpstpo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dmgyjpstpo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dmgyjpstpo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dmgyjpstpo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dmgyjpstpo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dpggkeyfuj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dpggkeyfuj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dpggkeyfuj p { margin: 0; padding: 0; }
 #dpggkeyfuj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dpggkeyfuj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dpggkeyfuj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dpggkeyfuj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dpggkeyfuj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dpggkeyfuj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dpggkeyfuj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dpggkeyfuj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dpggkeyfuj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dpggkeyfuj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dpggkeyfuj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dpggkeyfuj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dpggkeyfuj .gt_spanner_row { border-bottom-style: hidden; }
 #dpggkeyfuj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dpggkeyfuj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dpggkeyfuj .gt_from_md> :first-child { margin-top: 0; }
 #dpggkeyfuj .gt_from_md> :last-child { margin-bottom: 0; }
 #dpggkeyfuj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dpggkeyfuj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dpggkeyfuj .gt_indent_1 { text-indent: 5px; }
 #dpggkeyfuj .gt_indent_2 { text-indent: calc(5px * 2); }
 #dpggkeyfuj .gt_indent_3 { text-indent: calc(5px * 3); }
 #dpggkeyfuj .gt_indent_4 { text-indent: calc(5px * 4); }
 #dpggkeyfuj .gt_indent_5 { text-indent: calc(5px * 5); }
 #dpggkeyfuj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dpggkeyfuj .gt_row_group_first td { border-top-width: 2px; }
 #dpggkeyfuj .gt_row_group_first th { border-top-width: 2px; }
 #dpggkeyfuj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dpggkeyfuj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dpggkeyfuj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dpggkeyfuj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dpggkeyfuj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dpggkeyfuj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dpggkeyfuj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dpggkeyfuj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dpggkeyfuj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dpggkeyfuj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dpggkeyfuj .gt_left { text-align: left; }
 #dpggkeyfuj .gt_center { text-align: center; }
 #dpggkeyfuj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dpggkeyfuj .gt_font_normal { font-weight: normal; }
 #dpggkeyfuj .gt_font_bold { font-weight: bold; }
 #dpggkeyfuj .gt_font_italic { font-style: italic; }
 #dpggkeyfuj .gt_super { font-size: 65%; }
 #dpggkeyfuj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dpggkeyfuj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dpggkeyfuj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dpggkeyfuj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dpggkeyfuj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dpggkeyfuj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#oirkliivlo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oirkliivlo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oirkliivlo p { margin: 0; padding: 0; }
 #oirkliivlo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oirkliivlo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oirkliivlo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oirkliivlo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oirkliivlo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oirkliivlo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oirkliivlo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oirkliivlo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oirkliivlo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oirkliivlo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oirkliivlo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oirkliivlo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oirkliivlo .gt_spanner_row { border-bottom-style: hidden; }
 #oirkliivlo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oirkliivlo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #oirkliivlo .gt_from_md> :first-child { margin-top: 0; }
 #oirkliivlo .gt_from_md> :last-child { margin-bottom: 0; }
 #oirkliivlo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #oirkliivlo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #oirkliivlo .gt_indent_1 { text-indent: 5px; }
 #oirkliivlo .gt_indent_2 { text-indent: calc(5px * 2); }
 #oirkliivlo .gt_indent_3 { text-indent: calc(5px * 3); }
 #oirkliivlo .gt_indent_4 { text-indent: calc(5px * 4); }
 #oirkliivlo .gt_indent_5 { text-indent: calc(5px * 5); }
 #oirkliivlo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oirkliivlo .gt_row_group_first td { border-top-width: 2px; }
 #oirkliivlo .gt_row_group_first th { border-top-width: 2px; }
 #oirkliivlo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oirkliivlo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oirkliivlo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oirkliivlo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oirkliivlo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oirkliivlo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oirkliivlo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oirkliivlo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oirkliivlo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oirkliivlo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oirkliivlo .gt_left { text-align: left; }
 #oirkliivlo .gt_center { text-align: center; }
 #oirkliivlo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oirkliivlo .gt_font_normal { font-weight: normal; }
 #oirkliivlo .gt_font_bold { font-weight: bold; }
 #oirkliivlo .gt_font_italic { font-style: italic; }
 #oirkliivlo .gt_super { font-size: 65%; }
 #oirkliivlo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oirkliivlo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oirkliivlo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oirkliivlo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oirkliivlo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oirkliivlo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fbjllpdjyq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fbjllpdjyq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fbjllpdjyq p { margin: 0; padding: 0; }
 #fbjllpdjyq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fbjllpdjyq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fbjllpdjyq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fbjllpdjyq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fbjllpdjyq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fbjllpdjyq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fbjllpdjyq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fbjllpdjyq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fbjllpdjyq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fbjllpdjyq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fbjllpdjyq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fbjllpdjyq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fbjllpdjyq .gt_spanner_row { border-bottom-style: hidden; }
 #fbjllpdjyq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fbjllpdjyq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fbjllpdjyq .gt_from_md> :first-child { margin-top: 0; }
 #fbjllpdjyq .gt_from_md> :last-child { margin-bottom: 0; }
 #fbjllpdjyq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fbjllpdjyq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fbjllpdjyq .gt_indent_1 { text-indent: 5px; }
 #fbjllpdjyq .gt_indent_2 { text-indent: calc(5px * 2); }
 #fbjllpdjyq .gt_indent_3 { text-indent: calc(5px * 3); }
 #fbjllpdjyq .gt_indent_4 { text-indent: calc(5px * 4); }
 #fbjllpdjyq .gt_indent_5 { text-indent: calc(5px * 5); }
 #fbjllpdjyq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fbjllpdjyq .gt_row_group_first td { border-top-width: 2px; }
 #fbjllpdjyq .gt_row_group_first th { border-top-width: 2px; }
 #fbjllpdjyq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fbjllpdjyq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fbjllpdjyq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fbjllpdjyq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fbjllpdjyq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fbjllpdjyq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fbjllpdjyq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fbjllpdjyq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fbjllpdjyq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fbjllpdjyq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fbjllpdjyq .gt_left { text-align: left; }
 #fbjllpdjyq .gt_center { text-align: center; }
 #fbjllpdjyq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fbjllpdjyq .gt_font_normal { font-weight: normal; }
 #fbjllpdjyq .gt_font_bold { font-weight: bold; }
 #fbjllpdjyq .gt_font_italic { font-style: italic; }
 #fbjllpdjyq .gt_super { font-size: 65%; }
 #fbjllpdjyq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fbjllpdjyq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fbjllpdjyq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fbjllpdjyq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fbjllpdjyq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fbjllpdjyq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#yxkkfispck table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#yxkkfispck thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#yxkkfispck p { margin: 0; padding: 0; }
 #yxkkfispck .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #yxkkfispck .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #yxkkfispck .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #yxkkfispck .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #yxkkfispck .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yxkkfispck .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yxkkfispck .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #yxkkfispck .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #yxkkfispck .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #yxkkfispck .gt_column_spanner_outer:first-child { padding-left: 0; }
 #yxkkfispck .gt_column_spanner_outer:last-child { padding-right: 0; }
 #yxkkfispck .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #yxkkfispck .gt_spanner_row { border-bottom-style: hidden; }
 #yxkkfispck .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #yxkkfispck .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #yxkkfispck .gt_from_md> :first-child { margin-top: 0; }
 #yxkkfispck .gt_from_md> :last-child { margin-bottom: 0; }
 #yxkkfispck .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #yxkkfispck .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #yxkkfispck .gt_indent_1 { text-indent: 5px; }
 #yxkkfispck .gt_indent_2 { text-indent: calc(5px * 2); }
 #yxkkfispck .gt_indent_3 { text-indent: calc(5px * 3); }
 #yxkkfispck .gt_indent_4 { text-indent: calc(5px * 4); }
 #yxkkfispck .gt_indent_5 { text-indent: calc(5px * 5); }
 #yxkkfispck .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #yxkkfispck .gt_row_group_first td { border-top-width: 2px; }
 #yxkkfispck .gt_row_group_first th { border-top-width: 2px; }
 #yxkkfispck .gt_striped { color: #333333; background-color: #F4F4F4; }
 #yxkkfispck .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yxkkfispck .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yxkkfispck .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #yxkkfispck .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #yxkkfispck .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #yxkkfispck .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #yxkkfispck .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #yxkkfispck .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yxkkfispck .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yxkkfispck .gt_left { text-align: left; }
 #yxkkfispck .gt_center { text-align: center; }
 #yxkkfispck .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #yxkkfispck .gt_font_normal { font-weight: normal; }
 #yxkkfispck .gt_font_bold { font-weight: bold; }
 #yxkkfispck .gt_font_italic { font-style: italic; }
 #yxkkfispck .gt_super { font-size: 65%; }
 #yxkkfispck .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yxkkfispck .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #yxkkfispck .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #yxkkfispck .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #yxkkfispck .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #yxkkfispck .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ltxhwhgipj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ltxhwhgipj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ltxhwhgipj p { margin: 0; padding: 0; }
 #ltxhwhgipj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ltxhwhgipj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ltxhwhgipj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ltxhwhgipj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ltxhwhgipj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ltxhwhgipj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ltxhwhgipj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ltxhwhgipj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ltxhwhgipj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ltxhwhgipj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ltxhwhgipj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ltxhwhgipj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ltxhwhgipj .gt_spanner_row { border-bottom-style: hidden; }
 #ltxhwhgipj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ltxhwhgipj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ltxhwhgipj .gt_from_md> :first-child { margin-top: 0; }
 #ltxhwhgipj .gt_from_md> :last-child { margin-bottom: 0; }
 #ltxhwhgipj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ltxhwhgipj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ltxhwhgipj .gt_indent_1 { text-indent: 5px; }
 #ltxhwhgipj .gt_indent_2 { text-indent: calc(5px * 2); }
 #ltxhwhgipj .gt_indent_3 { text-indent: calc(5px * 3); }
 #ltxhwhgipj .gt_indent_4 { text-indent: calc(5px * 4); }
 #ltxhwhgipj .gt_indent_5 { text-indent: calc(5px * 5); }
 #ltxhwhgipj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ltxhwhgipj .gt_row_group_first td { border-top-width: 2px; }
 #ltxhwhgipj .gt_row_group_first th { border-top-width: 2px; }
 #ltxhwhgipj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ltxhwhgipj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ltxhwhgipj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ltxhwhgipj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ltxhwhgipj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ltxhwhgipj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ltxhwhgipj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ltxhwhgipj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ltxhwhgipj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ltxhwhgipj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ltxhwhgipj .gt_left { text-align: left; }
 #ltxhwhgipj .gt_center { text-align: center; }
 #ltxhwhgipj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ltxhwhgipj .gt_font_normal { font-weight: normal; }
 #ltxhwhgipj .gt_font_bold { font-weight: bold; }
 #ltxhwhgipj .gt_font_italic { font-style: italic; }
 #ltxhwhgipj .gt_super { font-size: 65%; }
 #ltxhwhgipj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ltxhwhgipj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ltxhwhgipj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ltxhwhgipj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ltxhwhgipj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ltxhwhgipj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dsxyxrwztx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dsxyxrwztx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dsxyxrwztx p { margin: 0; padding: 0; }
 #dsxyxrwztx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dsxyxrwztx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dsxyxrwztx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dsxyxrwztx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dsxyxrwztx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dsxyxrwztx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dsxyxrwztx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dsxyxrwztx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dsxyxrwztx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dsxyxrwztx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dsxyxrwztx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dsxyxrwztx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dsxyxrwztx .gt_spanner_row { border-bottom-style: hidden; }
 #dsxyxrwztx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dsxyxrwztx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dsxyxrwztx .gt_from_md> :first-child { margin-top: 0; }
 #dsxyxrwztx .gt_from_md> :last-child { margin-bottom: 0; }
 #dsxyxrwztx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dsxyxrwztx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dsxyxrwztx .gt_indent_1 { text-indent: 5px; }
 #dsxyxrwztx .gt_indent_2 { text-indent: calc(5px * 2); }
 #dsxyxrwztx .gt_indent_3 { text-indent: calc(5px * 3); }
 #dsxyxrwztx .gt_indent_4 { text-indent: calc(5px * 4); }
 #dsxyxrwztx .gt_indent_5 { text-indent: calc(5px * 5); }
 #dsxyxrwztx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dsxyxrwztx .gt_row_group_first td { border-top-width: 2px; }
 #dsxyxrwztx .gt_row_group_first th { border-top-width: 2px; }
 #dsxyxrwztx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dsxyxrwztx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dsxyxrwztx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dsxyxrwztx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dsxyxrwztx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dsxyxrwztx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dsxyxrwztx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dsxyxrwztx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dsxyxrwztx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dsxyxrwztx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dsxyxrwztx .gt_left { text-align: left; }
 #dsxyxrwztx .gt_center { text-align: center; }
 #dsxyxrwztx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dsxyxrwztx .gt_font_normal { font-weight: normal; }
 #dsxyxrwztx .gt_font_bold { font-weight: bold; }
 #dsxyxrwztx .gt_font_italic { font-style: italic; }
 #dsxyxrwztx .gt_super { font-size: 65%; }
 #dsxyxrwztx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dsxyxrwztx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dsxyxrwztx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dsxyxrwztx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dsxyxrwztx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dsxyxrwztx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xswopawlkx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xswopawlkx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xswopawlkx p { margin: 0; padding: 0; }
 #xswopawlkx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xswopawlkx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xswopawlkx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xswopawlkx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xswopawlkx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xswopawlkx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xswopawlkx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xswopawlkx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xswopawlkx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xswopawlkx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xswopawlkx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xswopawlkx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xswopawlkx .gt_spanner_row { border-bottom-style: hidden; }
 #xswopawlkx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xswopawlkx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xswopawlkx .gt_from_md> :first-child { margin-top: 0; }
 #xswopawlkx .gt_from_md> :last-child { margin-bottom: 0; }
 #xswopawlkx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xswopawlkx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xswopawlkx .gt_indent_1 { text-indent: 5px; }
 #xswopawlkx .gt_indent_2 { text-indent: calc(5px * 2); }
 #xswopawlkx .gt_indent_3 { text-indent: calc(5px * 3); }
 #xswopawlkx .gt_indent_4 { text-indent: calc(5px * 4); }
 #xswopawlkx .gt_indent_5 { text-indent: calc(5px * 5); }
 #xswopawlkx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xswopawlkx .gt_row_group_first td { border-top-width: 2px; }
 #xswopawlkx .gt_row_group_first th { border-top-width: 2px; }
 #xswopawlkx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xswopawlkx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xswopawlkx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xswopawlkx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xswopawlkx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xswopawlkx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xswopawlkx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xswopawlkx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xswopawlkx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xswopawlkx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xswopawlkx .gt_left { text-align: left; }
 #xswopawlkx .gt_center { text-align: center; }
 #xswopawlkx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xswopawlkx .gt_font_normal { font-weight: normal; }
 #xswopawlkx .gt_font_bold { font-weight: bold; }
 #xswopawlkx .gt_font_italic { font-style: italic; }
 #xswopawlkx .gt_super { font-size: 65%; }
 #xswopawlkx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xswopawlkx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xswopawlkx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xswopawlkx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xswopawlkx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xswopawlkx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#emrsyzgjqt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#emrsyzgjqt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#emrsyzgjqt p { margin: 0; padding: 0; }
 #emrsyzgjqt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #emrsyzgjqt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #emrsyzgjqt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #emrsyzgjqt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #emrsyzgjqt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #emrsyzgjqt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #emrsyzgjqt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #emrsyzgjqt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #emrsyzgjqt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #emrsyzgjqt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #emrsyzgjqt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #emrsyzgjqt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #emrsyzgjqt .gt_spanner_row { border-bottom-style: hidden; }
 #emrsyzgjqt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #emrsyzgjqt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #emrsyzgjqt .gt_from_md> :first-child { margin-top: 0; }
 #emrsyzgjqt .gt_from_md> :last-child { margin-bottom: 0; }
 #emrsyzgjqt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #emrsyzgjqt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #emrsyzgjqt .gt_indent_1 { text-indent: 5px; }
 #emrsyzgjqt .gt_indent_2 { text-indent: calc(5px * 2); }
 #emrsyzgjqt .gt_indent_3 { text-indent: calc(5px * 3); }
 #emrsyzgjqt .gt_indent_4 { text-indent: calc(5px * 4); }
 #emrsyzgjqt .gt_indent_5 { text-indent: calc(5px * 5); }
 #emrsyzgjqt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #emrsyzgjqt .gt_row_group_first td { border-top-width: 2px; }
 #emrsyzgjqt .gt_row_group_first th { border-top-width: 2px; }
 #emrsyzgjqt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #emrsyzgjqt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #emrsyzgjqt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #emrsyzgjqt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #emrsyzgjqt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #emrsyzgjqt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #emrsyzgjqt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #emrsyzgjqt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #emrsyzgjqt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #emrsyzgjqt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #emrsyzgjqt .gt_left { text-align: left; }
 #emrsyzgjqt .gt_center { text-align: center; }
 #emrsyzgjqt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #emrsyzgjqt .gt_font_normal { font-weight: normal; }
 #emrsyzgjqt .gt_font_bold { font-weight: bold; }
 #emrsyzgjqt .gt_font_italic { font-style: italic; }
 #emrsyzgjqt .gt_super { font-size: 65%; }
 #emrsyzgjqt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #emrsyzgjqt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #emrsyzgjqt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #emrsyzgjqt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #emrsyzgjqt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #emrsyzgjqt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#kfsrzgyqed table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kfsrzgyqed thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kfsrzgyqed p { margin: 0; padding: 0; }
 #kfsrzgyqed .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kfsrzgyqed .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kfsrzgyqed .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kfsrzgyqed .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kfsrzgyqed .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kfsrzgyqed .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kfsrzgyqed .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kfsrzgyqed .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kfsrzgyqed .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kfsrzgyqed .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kfsrzgyqed .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kfsrzgyqed .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kfsrzgyqed .gt_spanner_row { border-bottom-style: hidden; }
 #kfsrzgyqed .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kfsrzgyqed .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kfsrzgyqed .gt_from_md> :first-child { margin-top: 0; }
 #kfsrzgyqed .gt_from_md> :last-child { margin-bottom: 0; }
 #kfsrzgyqed .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kfsrzgyqed .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kfsrzgyqed .gt_indent_1 { text-indent: 5px; }
 #kfsrzgyqed .gt_indent_2 { text-indent: calc(5px * 2); }
 #kfsrzgyqed .gt_indent_3 { text-indent: calc(5px * 3); }
 #kfsrzgyqed .gt_indent_4 { text-indent: calc(5px * 4); }
 #kfsrzgyqed .gt_indent_5 { text-indent: calc(5px * 5); }
 #kfsrzgyqed .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kfsrzgyqed .gt_row_group_first td { border-top-width: 2px; }
 #kfsrzgyqed .gt_row_group_first th { border-top-width: 2px; }
 #kfsrzgyqed .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kfsrzgyqed .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kfsrzgyqed .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kfsrzgyqed .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kfsrzgyqed .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kfsrzgyqed .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kfsrzgyqed .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kfsrzgyqed .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kfsrzgyqed .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kfsrzgyqed .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kfsrzgyqed .gt_left { text-align: left; }
 #kfsrzgyqed .gt_center { text-align: center; }
 #kfsrzgyqed .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kfsrzgyqed .gt_font_normal { font-weight: normal; }
 #kfsrzgyqed .gt_font_bold { font-weight: bold; }
 #kfsrzgyqed .gt_font_italic { font-style: italic; }
 #kfsrzgyqed .gt_super { font-size: 65%; }
 #kfsrzgyqed .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kfsrzgyqed .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kfsrzgyqed .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kfsrzgyqed .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kfsrzgyqed .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kfsrzgyqed .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#eugkiqrsdj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eugkiqrsdj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eugkiqrsdj p { margin: 0; padding: 0; }
 #eugkiqrsdj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eugkiqrsdj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eugkiqrsdj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eugkiqrsdj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eugkiqrsdj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eugkiqrsdj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eugkiqrsdj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eugkiqrsdj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eugkiqrsdj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eugkiqrsdj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eugkiqrsdj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eugkiqrsdj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eugkiqrsdj .gt_spanner_row { border-bottom-style: hidden; }
 #eugkiqrsdj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eugkiqrsdj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eugkiqrsdj .gt_from_md> :first-child { margin-top: 0; }
 #eugkiqrsdj .gt_from_md> :last-child { margin-bottom: 0; }
 #eugkiqrsdj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eugkiqrsdj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eugkiqrsdj .gt_indent_1 { text-indent: 5px; }
 #eugkiqrsdj .gt_indent_2 { text-indent: calc(5px * 2); }
 #eugkiqrsdj .gt_indent_3 { text-indent: calc(5px * 3); }
 #eugkiqrsdj .gt_indent_4 { text-indent: calc(5px * 4); }
 #eugkiqrsdj .gt_indent_5 { text-indent: calc(5px * 5); }
 #eugkiqrsdj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eugkiqrsdj .gt_row_group_first td { border-top-width: 2px; }
 #eugkiqrsdj .gt_row_group_first th { border-top-width: 2px; }
 #eugkiqrsdj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eugkiqrsdj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eugkiqrsdj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eugkiqrsdj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eugkiqrsdj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eugkiqrsdj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eugkiqrsdj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eugkiqrsdj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eugkiqrsdj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eugkiqrsdj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eugkiqrsdj .gt_left { text-align: left; }
 #eugkiqrsdj .gt_center { text-align: center; }
 #eugkiqrsdj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eugkiqrsdj .gt_font_normal { font-weight: normal; }
 #eugkiqrsdj .gt_font_bold { font-weight: bold; }
 #eugkiqrsdj .gt_font_italic { font-style: italic; }
 #eugkiqrsdj .gt_super { font-size: 65%; }
 #eugkiqrsdj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eugkiqrsdj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eugkiqrsdj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eugkiqrsdj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eugkiqrsdj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eugkiqrsdj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#duwcsezmol table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#duwcsezmol thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#duwcsezmol p { margin: 0; padding: 0; }
 #duwcsezmol .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #duwcsezmol .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #duwcsezmol .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #duwcsezmol .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #duwcsezmol .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #duwcsezmol .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #duwcsezmol .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #duwcsezmol .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #duwcsezmol .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #duwcsezmol .gt_column_spanner_outer:first-child { padding-left: 0; }
 #duwcsezmol .gt_column_spanner_outer:last-child { padding-right: 0; }
 #duwcsezmol .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #duwcsezmol .gt_spanner_row { border-bottom-style: hidden; }
 #duwcsezmol .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #duwcsezmol .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #duwcsezmol .gt_from_md> :first-child { margin-top: 0; }
 #duwcsezmol .gt_from_md> :last-child { margin-bottom: 0; }
 #duwcsezmol .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #duwcsezmol .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #duwcsezmol .gt_indent_1 { text-indent: 5px; }
 #duwcsezmol .gt_indent_2 { text-indent: calc(5px * 2); }
 #duwcsezmol .gt_indent_3 { text-indent: calc(5px * 3); }
 #duwcsezmol .gt_indent_4 { text-indent: calc(5px * 4); }
 #duwcsezmol .gt_indent_5 { text-indent: calc(5px * 5); }
 #duwcsezmol .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #duwcsezmol .gt_row_group_first td { border-top-width: 2px; }
 #duwcsezmol .gt_row_group_first th { border-top-width: 2px; }
 #duwcsezmol .gt_striped { color: #333333; background-color: #F4F4F4; }
 #duwcsezmol .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #duwcsezmol .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #duwcsezmol .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #duwcsezmol .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #duwcsezmol .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #duwcsezmol .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #duwcsezmol .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #duwcsezmol .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #duwcsezmol .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #duwcsezmol .gt_left { text-align: left; }
 #duwcsezmol .gt_center { text-align: center; }
 #duwcsezmol .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #duwcsezmol .gt_font_normal { font-weight: normal; }
 #duwcsezmol .gt_font_bold { font-weight: bold; }
 #duwcsezmol .gt_font_italic { font-style: italic; }
 #duwcsezmol .gt_super { font-size: 65%; }
 #duwcsezmol .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #duwcsezmol .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #duwcsezmol .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #duwcsezmol .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #duwcsezmol .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #duwcsezmol .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pitfvsbfek table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pitfvsbfek thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pitfvsbfek p { margin: 0; padding: 0; }
 #pitfvsbfek .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pitfvsbfek .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pitfvsbfek .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pitfvsbfek .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pitfvsbfek .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pitfvsbfek .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pitfvsbfek .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pitfvsbfek .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pitfvsbfek .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pitfvsbfek .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pitfvsbfek .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pitfvsbfek .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pitfvsbfek .gt_spanner_row { border-bottom-style: hidden; }
 #pitfvsbfek .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pitfvsbfek .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pitfvsbfek .gt_from_md> :first-child { margin-top: 0; }
 #pitfvsbfek .gt_from_md> :last-child { margin-bottom: 0; }
 #pitfvsbfek .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pitfvsbfek .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pitfvsbfek .gt_indent_1 { text-indent: 5px; }
 #pitfvsbfek .gt_indent_2 { text-indent: calc(5px * 2); }
 #pitfvsbfek .gt_indent_3 { text-indent: calc(5px * 3); }
 #pitfvsbfek .gt_indent_4 { text-indent: calc(5px * 4); }
 #pitfvsbfek .gt_indent_5 { text-indent: calc(5px * 5); }
 #pitfvsbfek .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pitfvsbfek .gt_row_group_first td { border-top-width: 2px; }
 #pitfvsbfek .gt_row_group_first th { border-top-width: 2px; }
 #pitfvsbfek .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pitfvsbfek .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pitfvsbfek .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pitfvsbfek .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pitfvsbfek .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pitfvsbfek .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pitfvsbfek .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pitfvsbfek .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pitfvsbfek .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pitfvsbfek .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pitfvsbfek .gt_left { text-align: left; }
 #pitfvsbfek .gt_center { text-align: center; }
 #pitfvsbfek .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pitfvsbfek .gt_font_normal { font-weight: normal; }
 #pitfvsbfek .gt_font_bold { font-weight: bold; }
 #pitfvsbfek .gt_font_italic { font-style: italic; }
 #pitfvsbfek .gt_super { font-size: 65%; }
 #pitfvsbfek .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pitfvsbfek .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pitfvsbfek .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pitfvsbfek .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pitfvsbfek .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pitfvsbfek .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wnzmydheeo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wnzmydheeo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wnzmydheeo p { margin: 0; padding: 0; }
 #wnzmydheeo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wnzmydheeo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wnzmydheeo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wnzmydheeo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wnzmydheeo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wnzmydheeo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnzmydheeo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wnzmydheeo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wnzmydheeo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wnzmydheeo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wnzmydheeo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wnzmydheeo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wnzmydheeo .gt_spanner_row { border-bottom-style: hidden; }
 #wnzmydheeo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wnzmydheeo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wnzmydheeo .gt_from_md> :first-child { margin-top: 0; }
 #wnzmydheeo .gt_from_md> :last-child { margin-bottom: 0; }
 #wnzmydheeo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wnzmydheeo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wnzmydheeo .gt_indent_1 { text-indent: 5px; }
 #wnzmydheeo .gt_indent_2 { text-indent: calc(5px * 2); }
 #wnzmydheeo .gt_indent_3 { text-indent: calc(5px * 3); }
 #wnzmydheeo .gt_indent_4 { text-indent: calc(5px * 4); }
 #wnzmydheeo .gt_indent_5 { text-indent: calc(5px * 5); }
 #wnzmydheeo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wnzmydheeo .gt_row_group_first td { border-top-width: 2px; }
 #wnzmydheeo .gt_row_group_first th { border-top-width: 2px; }
 #wnzmydheeo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wnzmydheeo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnzmydheeo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wnzmydheeo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wnzmydheeo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnzmydheeo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wnzmydheeo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wnzmydheeo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wnzmydheeo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnzmydheeo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wnzmydheeo .gt_left { text-align: left; }
 #wnzmydheeo .gt_center { text-align: center; }
 #wnzmydheeo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wnzmydheeo .gt_font_normal { font-weight: normal; }
 #wnzmydheeo .gt_font_bold { font-weight: bold; }
 #wnzmydheeo .gt_font_italic { font-style: italic; }
 #wnzmydheeo .gt_super { font-size: 65%; }
 #wnzmydheeo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnzmydheeo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wnzmydheeo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnzmydheeo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wnzmydheeo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wnzmydheeo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
