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
#fwcyqhqeke table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fwcyqhqeke thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fwcyqhqeke p { margin: 0; padding: 0; }
 #fwcyqhqeke .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fwcyqhqeke .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fwcyqhqeke .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fwcyqhqeke .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fwcyqhqeke .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fwcyqhqeke .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fwcyqhqeke .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fwcyqhqeke .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fwcyqhqeke .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fwcyqhqeke .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fwcyqhqeke .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fwcyqhqeke .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fwcyqhqeke .gt_spanner_row { border-bottom-style: hidden; }
 #fwcyqhqeke .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fwcyqhqeke .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fwcyqhqeke .gt_from_md> :first-child { margin-top: 0; }
 #fwcyqhqeke .gt_from_md> :last-child { margin-bottom: 0; }
 #fwcyqhqeke .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fwcyqhqeke .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fwcyqhqeke .gt_indent_1 { text-indent: 5px; }
 #fwcyqhqeke .gt_indent_2 { text-indent: calc(5px * 2); }
 #fwcyqhqeke .gt_indent_3 { text-indent: calc(5px * 3); }
 #fwcyqhqeke .gt_indent_4 { text-indent: calc(5px * 4); }
 #fwcyqhqeke .gt_indent_5 { text-indent: calc(5px * 5); }
 #fwcyqhqeke .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fwcyqhqeke .gt_row_group_first td { border-top-width: 2px; }
 #fwcyqhqeke .gt_row_group_first th { border-top-width: 2px; }
 #fwcyqhqeke .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fwcyqhqeke .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fwcyqhqeke .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fwcyqhqeke .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fwcyqhqeke .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fwcyqhqeke .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fwcyqhqeke .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fwcyqhqeke .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fwcyqhqeke .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fwcyqhqeke .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fwcyqhqeke .gt_left { text-align: left; }
 #fwcyqhqeke .gt_center { text-align: center; }
 #fwcyqhqeke .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fwcyqhqeke .gt_font_normal { font-weight: normal; }
 #fwcyqhqeke .gt_font_bold { font-weight: bold; }
 #fwcyqhqeke .gt_font_italic { font-style: italic; }
 #fwcyqhqeke .gt_super { font-size: 65%; }
 #fwcyqhqeke .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fwcyqhqeke .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fwcyqhqeke .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fwcyqhqeke .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fwcyqhqeke .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fwcyqhqeke .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wnniawzjbc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wnniawzjbc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wnniawzjbc p { margin: 0; padding: 0; }
 #wnniawzjbc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wnniawzjbc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wnniawzjbc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wnniawzjbc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wnniawzjbc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wnniawzjbc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnniawzjbc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wnniawzjbc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wnniawzjbc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wnniawzjbc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wnniawzjbc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wnniawzjbc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wnniawzjbc .gt_spanner_row { border-bottom-style: hidden; }
 #wnniawzjbc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wnniawzjbc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wnniawzjbc .gt_from_md> :first-child { margin-top: 0; }
 #wnniawzjbc .gt_from_md> :last-child { margin-bottom: 0; }
 #wnniawzjbc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wnniawzjbc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wnniawzjbc .gt_indent_1 { text-indent: 5px; }
 #wnniawzjbc .gt_indent_2 { text-indent: calc(5px * 2); }
 #wnniawzjbc .gt_indent_3 { text-indent: calc(5px * 3); }
 #wnniawzjbc .gt_indent_4 { text-indent: calc(5px * 4); }
 #wnniawzjbc .gt_indent_5 { text-indent: calc(5px * 5); }
 #wnniawzjbc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wnniawzjbc .gt_row_group_first td { border-top-width: 2px; }
 #wnniawzjbc .gt_row_group_first th { border-top-width: 2px; }
 #wnniawzjbc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wnniawzjbc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnniawzjbc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wnniawzjbc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wnniawzjbc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnniawzjbc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wnniawzjbc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wnniawzjbc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wnniawzjbc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnniawzjbc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wnniawzjbc .gt_left { text-align: left; }
 #wnniawzjbc .gt_center { text-align: center; }
 #wnniawzjbc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wnniawzjbc .gt_font_normal { font-weight: normal; }
 #wnniawzjbc .gt_font_bold { font-weight: bold; }
 #wnniawzjbc .gt_font_italic { font-style: italic; }
 #wnniawzjbc .gt_super { font-size: 65%; }
 #wnniawzjbc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnniawzjbc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wnniawzjbc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnniawzjbc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wnniawzjbc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wnniawzjbc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#suthdkunmu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#suthdkunmu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#suthdkunmu p { margin: 0; padding: 0; }
 #suthdkunmu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #suthdkunmu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #suthdkunmu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #suthdkunmu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #suthdkunmu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #suthdkunmu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #suthdkunmu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #suthdkunmu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #suthdkunmu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #suthdkunmu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #suthdkunmu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #suthdkunmu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #suthdkunmu .gt_spanner_row { border-bottom-style: hidden; }
 #suthdkunmu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #suthdkunmu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #suthdkunmu .gt_from_md> :first-child { margin-top: 0; }
 #suthdkunmu .gt_from_md> :last-child { margin-bottom: 0; }
 #suthdkunmu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #suthdkunmu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #suthdkunmu .gt_indent_1 { text-indent: 5px; }
 #suthdkunmu .gt_indent_2 { text-indent: calc(5px * 2); }
 #suthdkunmu .gt_indent_3 { text-indent: calc(5px * 3); }
 #suthdkunmu .gt_indent_4 { text-indent: calc(5px * 4); }
 #suthdkunmu .gt_indent_5 { text-indent: calc(5px * 5); }
 #suthdkunmu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #suthdkunmu .gt_row_group_first td { border-top-width: 2px; }
 #suthdkunmu .gt_row_group_first th { border-top-width: 2px; }
 #suthdkunmu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #suthdkunmu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #suthdkunmu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #suthdkunmu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #suthdkunmu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #suthdkunmu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #suthdkunmu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #suthdkunmu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #suthdkunmu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #suthdkunmu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #suthdkunmu .gt_left { text-align: left; }
 #suthdkunmu .gt_center { text-align: center; }
 #suthdkunmu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #suthdkunmu .gt_font_normal { font-weight: normal; }
 #suthdkunmu .gt_font_bold { font-weight: bold; }
 #suthdkunmu .gt_font_italic { font-style: italic; }
 #suthdkunmu .gt_super { font-size: 65%; }
 #suthdkunmu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #suthdkunmu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #suthdkunmu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #suthdkunmu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #suthdkunmu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #suthdkunmu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qdaeechgbv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qdaeechgbv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qdaeechgbv p { margin: 0; padding: 0; }
 #qdaeechgbv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qdaeechgbv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qdaeechgbv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qdaeechgbv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qdaeechgbv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qdaeechgbv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qdaeechgbv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qdaeechgbv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qdaeechgbv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qdaeechgbv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qdaeechgbv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qdaeechgbv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qdaeechgbv .gt_spanner_row { border-bottom-style: hidden; }
 #qdaeechgbv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qdaeechgbv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qdaeechgbv .gt_from_md> :first-child { margin-top: 0; }
 #qdaeechgbv .gt_from_md> :last-child { margin-bottom: 0; }
 #qdaeechgbv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qdaeechgbv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qdaeechgbv .gt_indent_1 { text-indent: 5px; }
 #qdaeechgbv .gt_indent_2 { text-indent: calc(5px * 2); }
 #qdaeechgbv .gt_indent_3 { text-indent: calc(5px * 3); }
 #qdaeechgbv .gt_indent_4 { text-indent: calc(5px * 4); }
 #qdaeechgbv .gt_indent_5 { text-indent: calc(5px * 5); }
 #qdaeechgbv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qdaeechgbv .gt_row_group_first td { border-top-width: 2px; }
 #qdaeechgbv .gt_row_group_first th { border-top-width: 2px; }
 #qdaeechgbv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qdaeechgbv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qdaeechgbv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qdaeechgbv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qdaeechgbv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qdaeechgbv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qdaeechgbv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qdaeechgbv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qdaeechgbv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qdaeechgbv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qdaeechgbv .gt_left { text-align: left; }
 #qdaeechgbv .gt_center { text-align: center; }
 #qdaeechgbv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qdaeechgbv .gt_font_normal { font-weight: normal; }
 #qdaeechgbv .gt_font_bold { font-weight: bold; }
 #qdaeechgbv .gt_font_italic { font-style: italic; }
 #qdaeechgbv .gt_super { font-size: 65%; }
 #qdaeechgbv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qdaeechgbv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qdaeechgbv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qdaeechgbv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qdaeechgbv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qdaeechgbv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#cppecjfpuy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cppecjfpuy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cppecjfpuy p { margin: 0; padding: 0; }
 #cppecjfpuy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cppecjfpuy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cppecjfpuy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cppecjfpuy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cppecjfpuy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cppecjfpuy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cppecjfpuy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cppecjfpuy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cppecjfpuy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cppecjfpuy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cppecjfpuy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cppecjfpuy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cppecjfpuy .gt_spanner_row { border-bottom-style: hidden; }
 #cppecjfpuy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cppecjfpuy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cppecjfpuy .gt_from_md> :first-child { margin-top: 0; }
 #cppecjfpuy .gt_from_md> :last-child { margin-bottom: 0; }
 #cppecjfpuy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cppecjfpuy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cppecjfpuy .gt_indent_1 { text-indent: 5px; }
 #cppecjfpuy .gt_indent_2 { text-indent: calc(5px * 2); }
 #cppecjfpuy .gt_indent_3 { text-indent: calc(5px * 3); }
 #cppecjfpuy .gt_indent_4 { text-indent: calc(5px * 4); }
 #cppecjfpuy .gt_indent_5 { text-indent: calc(5px * 5); }
 #cppecjfpuy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cppecjfpuy .gt_row_group_first td { border-top-width: 2px; }
 #cppecjfpuy .gt_row_group_first th { border-top-width: 2px; }
 #cppecjfpuy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cppecjfpuy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cppecjfpuy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cppecjfpuy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cppecjfpuy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cppecjfpuy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cppecjfpuy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cppecjfpuy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cppecjfpuy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cppecjfpuy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cppecjfpuy .gt_left { text-align: left; }
 #cppecjfpuy .gt_center { text-align: center; }
 #cppecjfpuy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cppecjfpuy .gt_font_normal { font-weight: normal; }
 #cppecjfpuy .gt_font_bold { font-weight: bold; }
 #cppecjfpuy .gt_font_italic { font-style: italic; }
 #cppecjfpuy .gt_super { font-size: 65%; }
 #cppecjfpuy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cppecjfpuy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cppecjfpuy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cppecjfpuy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cppecjfpuy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cppecjfpuy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#avetsjhujf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#avetsjhujf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#avetsjhujf p { margin: 0; padding: 0; }
 #avetsjhujf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #avetsjhujf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #avetsjhujf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #avetsjhujf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #avetsjhujf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #avetsjhujf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #avetsjhujf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #avetsjhujf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #avetsjhujf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #avetsjhujf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #avetsjhujf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #avetsjhujf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #avetsjhujf .gt_spanner_row { border-bottom-style: hidden; }
 #avetsjhujf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #avetsjhujf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #avetsjhujf .gt_from_md> :first-child { margin-top: 0; }
 #avetsjhujf .gt_from_md> :last-child { margin-bottom: 0; }
 #avetsjhujf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #avetsjhujf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #avetsjhujf .gt_indent_1 { text-indent: 5px; }
 #avetsjhujf .gt_indent_2 { text-indent: calc(5px * 2); }
 #avetsjhujf .gt_indent_3 { text-indent: calc(5px * 3); }
 #avetsjhujf .gt_indent_4 { text-indent: calc(5px * 4); }
 #avetsjhujf .gt_indent_5 { text-indent: calc(5px * 5); }
 #avetsjhujf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #avetsjhujf .gt_row_group_first td { border-top-width: 2px; }
 #avetsjhujf .gt_row_group_first th { border-top-width: 2px; }
 #avetsjhujf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #avetsjhujf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #avetsjhujf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #avetsjhujf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #avetsjhujf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #avetsjhujf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #avetsjhujf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #avetsjhujf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #avetsjhujf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #avetsjhujf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #avetsjhujf .gt_left { text-align: left; }
 #avetsjhujf .gt_center { text-align: center; }
 #avetsjhujf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #avetsjhujf .gt_font_normal { font-weight: normal; }
 #avetsjhujf .gt_font_bold { font-weight: bold; }
 #avetsjhujf .gt_font_italic { font-style: italic; }
 #avetsjhujf .gt_super { font-size: 65%; }
 #avetsjhujf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #avetsjhujf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #avetsjhujf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #avetsjhujf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #avetsjhujf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #avetsjhujf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#sikierzhbk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sikierzhbk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sikierzhbk p { margin: 0; padding: 0; }
 #sikierzhbk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sikierzhbk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sikierzhbk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sikierzhbk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sikierzhbk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sikierzhbk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sikierzhbk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sikierzhbk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sikierzhbk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sikierzhbk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sikierzhbk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sikierzhbk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sikierzhbk .gt_spanner_row { border-bottom-style: hidden; }
 #sikierzhbk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sikierzhbk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sikierzhbk .gt_from_md> :first-child { margin-top: 0; }
 #sikierzhbk .gt_from_md> :last-child { margin-bottom: 0; }
 #sikierzhbk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sikierzhbk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sikierzhbk .gt_indent_1 { text-indent: 5px; }
 #sikierzhbk .gt_indent_2 { text-indent: calc(5px * 2); }
 #sikierzhbk .gt_indent_3 { text-indent: calc(5px * 3); }
 #sikierzhbk .gt_indent_4 { text-indent: calc(5px * 4); }
 #sikierzhbk .gt_indent_5 { text-indent: calc(5px * 5); }
 #sikierzhbk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sikierzhbk .gt_row_group_first td { border-top-width: 2px; }
 #sikierzhbk .gt_row_group_first th { border-top-width: 2px; }
 #sikierzhbk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sikierzhbk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sikierzhbk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sikierzhbk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sikierzhbk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sikierzhbk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sikierzhbk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sikierzhbk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sikierzhbk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sikierzhbk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sikierzhbk .gt_left { text-align: left; }
 #sikierzhbk .gt_center { text-align: center; }
 #sikierzhbk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sikierzhbk .gt_font_normal { font-weight: normal; }
 #sikierzhbk .gt_font_bold { font-weight: bold; }
 #sikierzhbk .gt_font_italic { font-style: italic; }
 #sikierzhbk .gt_super { font-size: 65%; }
 #sikierzhbk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sikierzhbk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sikierzhbk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sikierzhbk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sikierzhbk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sikierzhbk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#psreynczev table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#psreynczev thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#psreynczev p { margin: 0; padding: 0; }
 #psreynczev .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #psreynczev .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #psreynczev .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #psreynczev .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #psreynczev .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #psreynczev .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #psreynczev .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #psreynczev .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #psreynczev .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #psreynczev .gt_column_spanner_outer:first-child { padding-left: 0; }
 #psreynczev .gt_column_spanner_outer:last-child { padding-right: 0; }
 #psreynczev .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #psreynczev .gt_spanner_row { border-bottom-style: hidden; }
 #psreynczev .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #psreynczev .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #psreynczev .gt_from_md> :first-child { margin-top: 0; }
 #psreynczev .gt_from_md> :last-child { margin-bottom: 0; }
 #psreynczev .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #psreynczev .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #psreynczev .gt_indent_1 { text-indent: 5px; }
 #psreynczev .gt_indent_2 { text-indent: calc(5px * 2); }
 #psreynczev .gt_indent_3 { text-indent: calc(5px * 3); }
 #psreynczev .gt_indent_4 { text-indent: calc(5px * 4); }
 #psreynczev .gt_indent_5 { text-indent: calc(5px * 5); }
 #psreynczev .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #psreynczev .gt_row_group_first td { border-top-width: 2px; }
 #psreynczev .gt_row_group_first th { border-top-width: 2px; }
 #psreynczev .gt_striped { color: #333333; background-color: #F4F4F4; }
 #psreynczev .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #psreynczev .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #psreynczev .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #psreynczev .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #psreynczev .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #psreynczev .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #psreynczev .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #psreynczev .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #psreynczev .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #psreynczev .gt_left { text-align: left; }
 #psreynczev .gt_center { text-align: center; }
 #psreynczev .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #psreynczev .gt_font_normal { font-weight: normal; }
 #psreynczev .gt_font_bold { font-weight: bold; }
 #psreynczev .gt_font_italic { font-style: italic; }
 #psreynczev .gt_super { font-size: 65%; }
 #psreynczev .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #psreynczev .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #psreynczev .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #psreynczev .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #psreynczev .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #psreynczev .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bazowlrcip table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bazowlrcip thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bazowlrcip p { margin: 0; padding: 0; }
 #bazowlrcip .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bazowlrcip .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bazowlrcip .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bazowlrcip .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bazowlrcip .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bazowlrcip .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bazowlrcip .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bazowlrcip .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bazowlrcip .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bazowlrcip .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bazowlrcip .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bazowlrcip .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bazowlrcip .gt_spanner_row { border-bottom-style: hidden; }
 #bazowlrcip .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bazowlrcip .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bazowlrcip .gt_from_md> :first-child { margin-top: 0; }
 #bazowlrcip .gt_from_md> :last-child { margin-bottom: 0; }
 #bazowlrcip .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bazowlrcip .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bazowlrcip .gt_indent_1 { text-indent: 5px; }
 #bazowlrcip .gt_indent_2 { text-indent: calc(5px * 2); }
 #bazowlrcip .gt_indent_3 { text-indent: calc(5px * 3); }
 #bazowlrcip .gt_indent_4 { text-indent: calc(5px * 4); }
 #bazowlrcip .gt_indent_5 { text-indent: calc(5px * 5); }
 #bazowlrcip .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bazowlrcip .gt_row_group_first td { border-top-width: 2px; }
 #bazowlrcip .gt_row_group_first th { border-top-width: 2px; }
 #bazowlrcip .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bazowlrcip .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bazowlrcip .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bazowlrcip .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bazowlrcip .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bazowlrcip .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bazowlrcip .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bazowlrcip .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bazowlrcip .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bazowlrcip .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bazowlrcip .gt_left { text-align: left; }
 #bazowlrcip .gt_center { text-align: center; }
 #bazowlrcip .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bazowlrcip .gt_font_normal { font-weight: normal; }
 #bazowlrcip .gt_font_bold { font-weight: bold; }
 #bazowlrcip .gt_font_italic { font-style: italic; }
 #bazowlrcip .gt_super { font-size: 65%; }
 #bazowlrcip .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bazowlrcip .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bazowlrcip .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bazowlrcip .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bazowlrcip .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bazowlrcip .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bajioevqla table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bajioevqla thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bajioevqla p { margin: 0; padding: 0; }
 #bajioevqla .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bajioevqla .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bajioevqla .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bajioevqla .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bajioevqla .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bajioevqla .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bajioevqla .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bajioevqla .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bajioevqla .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bajioevqla .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bajioevqla .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bajioevqla .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bajioevqla .gt_spanner_row { border-bottom-style: hidden; }
 #bajioevqla .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bajioevqla .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bajioevqla .gt_from_md> :first-child { margin-top: 0; }
 #bajioevqla .gt_from_md> :last-child { margin-bottom: 0; }
 #bajioevqla .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bajioevqla .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bajioevqla .gt_indent_1 { text-indent: 5px; }
 #bajioevqla .gt_indent_2 { text-indent: calc(5px * 2); }
 #bajioevqla .gt_indent_3 { text-indent: calc(5px * 3); }
 #bajioevqla .gt_indent_4 { text-indent: calc(5px * 4); }
 #bajioevqla .gt_indent_5 { text-indent: calc(5px * 5); }
 #bajioevqla .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bajioevqla .gt_row_group_first td { border-top-width: 2px; }
 #bajioevqla .gt_row_group_first th { border-top-width: 2px; }
 #bajioevqla .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bajioevqla .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bajioevqla .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bajioevqla .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bajioevqla .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bajioevqla .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bajioevqla .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bajioevqla .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bajioevqla .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bajioevqla .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bajioevqla .gt_left { text-align: left; }
 #bajioevqla .gt_center { text-align: center; }
 #bajioevqla .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bajioevqla .gt_font_normal { font-weight: normal; }
 #bajioevqla .gt_font_bold { font-weight: bold; }
 #bajioevqla .gt_font_italic { font-style: italic; }
 #bajioevqla .gt_super { font-size: 65%; }
 #bajioevqla .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bajioevqla .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bajioevqla .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bajioevqla .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bajioevqla .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bajioevqla .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pssggfsqjt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pssggfsqjt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pssggfsqjt p { margin: 0; padding: 0; }
 #pssggfsqjt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pssggfsqjt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pssggfsqjt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pssggfsqjt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pssggfsqjt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pssggfsqjt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pssggfsqjt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pssggfsqjt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pssggfsqjt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pssggfsqjt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pssggfsqjt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pssggfsqjt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pssggfsqjt .gt_spanner_row { border-bottom-style: hidden; }
 #pssggfsqjt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pssggfsqjt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pssggfsqjt .gt_from_md> :first-child { margin-top: 0; }
 #pssggfsqjt .gt_from_md> :last-child { margin-bottom: 0; }
 #pssggfsqjt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pssggfsqjt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pssggfsqjt .gt_indent_1 { text-indent: 5px; }
 #pssggfsqjt .gt_indent_2 { text-indent: calc(5px * 2); }
 #pssggfsqjt .gt_indent_3 { text-indent: calc(5px * 3); }
 #pssggfsqjt .gt_indent_4 { text-indent: calc(5px * 4); }
 #pssggfsqjt .gt_indent_5 { text-indent: calc(5px * 5); }
 #pssggfsqjt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pssggfsqjt .gt_row_group_first td { border-top-width: 2px; }
 #pssggfsqjt .gt_row_group_first th { border-top-width: 2px; }
 #pssggfsqjt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pssggfsqjt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pssggfsqjt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pssggfsqjt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pssggfsqjt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pssggfsqjt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pssggfsqjt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pssggfsqjt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pssggfsqjt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pssggfsqjt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pssggfsqjt .gt_left { text-align: left; }
 #pssggfsqjt .gt_center { text-align: center; }
 #pssggfsqjt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pssggfsqjt .gt_font_normal { font-weight: normal; }
 #pssggfsqjt .gt_font_bold { font-weight: bold; }
 #pssggfsqjt .gt_font_italic { font-style: italic; }
 #pssggfsqjt .gt_super { font-size: 65%; }
 #pssggfsqjt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pssggfsqjt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pssggfsqjt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pssggfsqjt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pssggfsqjt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pssggfsqjt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#uchndxxqdz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uchndxxqdz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uchndxxqdz p { margin: 0; padding: 0; }
 #uchndxxqdz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #uchndxxqdz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uchndxxqdz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uchndxxqdz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uchndxxqdz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uchndxxqdz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uchndxxqdz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uchndxxqdz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uchndxxqdz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uchndxxqdz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uchndxxqdz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uchndxxqdz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uchndxxqdz .gt_spanner_row { border-bottom-style: hidden; }
 #uchndxxqdz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uchndxxqdz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #uchndxxqdz .gt_from_md> :first-child { margin-top: 0; }
 #uchndxxqdz .gt_from_md> :last-child { margin-bottom: 0; }
 #uchndxxqdz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #uchndxxqdz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #uchndxxqdz .gt_indent_1 { text-indent: 5px; }
 #uchndxxqdz .gt_indent_2 { text-indent: calc(5px * 2); }
 #uchndxxqdz .gt_indent_3 { text-indent: calc(5px * 3); }
 #uchndxxqdz .gt_indent_4 { text-indent: calc(5px * 4); }
 #uchndxxqdz .gt_indent_5 { text-indent: calc(5px * 5); }
 #uchndxxqdz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uchndxxqdz .gt_row_group_first td { border-top-width: 2px; }
 #uchndxxqdz .gt_row_group_first th { border-top-width: 2px; }
 #uchndxxqdz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uchndxxqdz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uchndxxqdz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uchndxxqdz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uchndxxqdz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uchndxxqdz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uchndxxqdz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uchndxxqdz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uchndxxqdz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uchndxxqdz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uchndxxqdz .gt_left { text-align: left; }
 #uchndxxqdz .gt_center { text-align: center; }
 #uchndxxqdz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uchndxxqdz .gt_font_normal { font-weight: normal; }
 #uchndxxqdz .gt_font_bold { font-weight: bold; }
 #uchndxxqdz .gt_font_italic { font-style: italic; }
 #uchndxxqdz .gt_super { font-size: 65%; }
 #uchndxxqdz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uchndxxqdz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uchndxxqdz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uchndxxqdz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uchndxxqdz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uchndxxqdz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#adhuumfbds table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#adhuumfbds thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#adhuumfbds p { margin: 0; padding: 0; }
 #adhuumfbds .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #adhuumfbds .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #adhuumfbds .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #adhuumfbds .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #adhuumfbds .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #adhuumfbds .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #adhuumfbds .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #adhuumfbds .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #adhuumfbds .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #adhuumfbds .gt_column_spanner_outer:first-child { padding-left: 0; }
 #adhuumfbds .gt_column_spanner_outer:last-child { padding-right: 0; }
 #adhuumfbds .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #adhuumfbds .gt_spanner_row { border-bottom-style: hidden; }
 #adhuumfbds .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #adhuumfbds .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #adhuumfbds .gt_from_md> :first-child { margin-top: 0; }
 #adhuumfbds .gt_from_md> :last-child { margin-bottom: 0; }
 #adhuumfbds .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #adhuumfbds .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #adhuumfbds .gt_indent_1 { text-indent: 5px; }
 #adhuumfbds .gt_indent_2 { text-indent: calc(5px * 2); }
 #adhuumfbds .gt_indent_3 { text-indent: calc(5px * 3); }
 #adhuumfbds .gt_indent_4 { text-indent: calc(5px * 4); }
 #adhuumfbds .gt_indent_5 { text-indent: calc(5px * 5); }
 #adhuumfbds .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #adhuumfbds .gt_row_group_first td { border-top-width: 2px; }
 #adhuumfbds .gt_row_group_first th { border-top-width: 2px; }
 #adhuumfbds .gt_striped { color: #333333; background-color: #F4F4F4; }
 #adhuumfbds .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #adhuumfbds .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #adhuumfbds .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #adhuumfbds .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #adhuumfbds .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #adhuumfbds .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #adhuumfbds .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #adhuumfbds .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #adhuumfbds .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #adhuumfbds .gt_left { text-align: left; }
 #adhuumfbds .gt_center { text-align: center; }
 #adhuumfbds .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #adhuumfbds .gt_font_normal { font-weight: normal; }
 #adhuumfbds .gt_font_bold { font-weight: bold; }
 #adhuumfbds .gt_font_italic { font-style: italic; }
 #adhuumfbds .gt_super { font-size: 65%; }
 #adhuumfbds .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #adhuumfbds .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #adhuumfbds .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #adhuumfbds .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #adhuumfbds .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #adhuumfbds .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dxszzsysje table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dxszzsysje thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dxszzsysje p { margin: 0; padding: 0; }
 #dxszzsysje .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dxszzsysje .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dxszzsysje .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dxszzsysje .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dxszzsysje .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dxszzsysje .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxszzsysje .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dxszzsysje .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dxszzsysje .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dxszzsysje .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dxszzsysje .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dxszzsysje .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dxszzsysje .gt_spanner_row { border-bottom-style: hidden; }
 #dxszzsysje .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dxszzsysje .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dxszzsysje .gt_from_md> :first-child { margin-top: 0; }
 #dxszzsysje .gt_from_md> :last-child { margin-bottom: 0; }
 #dxszzsysje .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dxszzsysje .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dxszzsysje .gt_indent_1 { text-indent: 5px; }
 #dxszzsysje .gt_indent_2 { text-indent: calc(5px * 2); }
 #dxszzsysje .gt_indent_3 { text-indent: calc(5px * 3); }
 #dxszzsysje .gt_indent_4 { text-indent: calc(5px * 4); }
 #dxszzsysje .gt_indent_5 { text-indent: calc(5px * 5); }
 #dxszzsysje .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dxszzsysje .gt_row_group_first td { border-top-width: 2px; }
 #dxszzsysje .gt_row_group_first th { border-top-width: 2px; }
 #dxszzsysje .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dxszzsysje .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxszzsysje .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dxszzsysje .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dxszzsysje .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dxszzsysje .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dxszzsysje .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dxszzsysje .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dxszzsysje .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxszzsysje .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dxszzsysje .gt_left { text-align: left; }
 #dxszzsysje .gt_center { text-align: center; }
 #dxszzsysje .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dxszzsysje .gt_font_normal { font-weight: normal; }
 #dxszzsysje .gt_font_bold { font-weight: bold; }
 #dxszzsysje .gt_font_italic { font-style: italic; }
 #dxszzsysje .gt_super { font-size: 65%; }
 #dxszzsysje .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxszzsysje .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dxszzsysje .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dxszzsysje .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dxszzsysje .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dxszzsysje .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#mlgfaomnmh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mlgfaomnmh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mlgfaomnmh p { margin: 0; padding: 0; }
 #mlgfaomnmh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mlgfaomnmh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mlgfaomnmh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mlgfaomnmh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mlgfaomnmh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mlgfaomnmh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mlgfaomnmh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mlgfaomnmh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mlgfaomnmh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mlgfaomnmh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mlgfaomnmh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mlgfaomnmh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mlgfaomnmh .gt_spanner_row { border-bottom-style: hidden; }
 #mlgfaomnmh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mlgfaomnmh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mlgfaomnmh .gt_from_md> :first-child { margin-top: 0; }
 #mlgfaomnmh .gt_from_md> :last-child { margin-bottom: 0; }
 #mlgfaomnmh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mlgfaomnmh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mlgfaomnmh .gt_indent_1 { text-indent: 5px; }
 #mlgfaomnmh .gt_indent_2 { text-indent: calc(5px * 2); }
 #mlgfaomnmh .gt_indent_3 { text-indent: calc(5px * 3); }
 #mlgfaomnmh .gt_indent_4 { text-indent: calc(5px * 4); }
 #mlgfaomnmh .gt_indent_5 { text-indent: calc(5px * 5); }
 #mlgfaomnmh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mlgfaomnmh .gt_row_group_first td { border-top-width: 2px; }
 #mlgfaomnmh .gt_row_group_first th { border-top-width: 2px; }
 #mlgfaomnmh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mlgfaomnmh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mlgfaomnmh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mlgfaomnmh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mlgfaomnmh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mlgfaomnmh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mlgfaomnmh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mlgfaomnmh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mlgfaomnmh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mlgfaomnmh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mlgfaomnmh .gt_left { text-align: left; }
 #mlgfaomnmh .gt_center { text-align: center; }
 #mlgfaomnmh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mlgfaomnmh .gt_font_normal { font-weight: normal; }
 #mlgfaomnmh .gt_font_bold { font-weight: bold; }
 #mlgfaomnmh .gt_font_italic { font-style: italic; }
 #mlgfaomnmh .gt_super { font-size: 65%; }
 #mlgfaomnmh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mlgfaomnmh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mlgfaomnmh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mlgfaomnmh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mlgfaomnmh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mlgfaomnmh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hnoxjajpqy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hnoxjajpqy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hnoxjajpqy p { margin: 0; padding: 0; }
 #hnoxjajpqy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hnoxjajpqy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hnoxjajpqy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hnoxjajpqy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hnoxjajpqy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hnoxjajpqy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hnoxjajpqy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hnoxjajpqy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hnoxjajpqy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hnoxjajpqy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hnoxjajpqy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hnoxjajpqy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hnoxjajpqy .gt_spanner_row { border-bottom-style: hidden; }
 #hnoxjajpqy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hnoxjajpqy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hnoxjajpqy .gt_from_md> :first-child { margin-top: 0; }
 #hnoxjajpqy .gt_from_md> :last-child { margin-bottom: 0; }
 #hnoxjajpqy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hnoxjajpqy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hnoxjajpqy .gt_indent_1 { text-indent: 5px; }
 #hnoxjajpqy .gt_indent_2 { text-indent: calc(5px * 2); }
 #hnoxjajpqy .gt_indent_3 { text-indent: calc(5px * 3); }
 #hnoxjajpqy .gt_indent_4 { text-indent: calc(5px * 4); }
 #hnoxjajpqy .gt_indent_5 { text-indent: calc(5px * 5); }
 #hnoxjajpqy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hnoxjajpqy .gt_row_group_first td { border-top-width: 2px; }
 #hnoxjajpqy .gt_row_group_first th { border-top-width: 2px; }
 #hnoxjajpqy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hnoxjajpqy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hnoxjajpqy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hnoxjajpqy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hnoxjajpqy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hnoxjajpqy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hnoxjajpqy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hnoxjajpqy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hnoxjajpqy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hnoxjajpqy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hnoxjajpqy .gt_left { text-align: left; }
 #hnoxjajpqy .gt_center { text-align: center; }
 #hnoxjajpqy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hnoxjajpqy .gt_font_normal { font-weight: normal; }
 #hnoxjajpqy .gt_font_bold { font-weight: bold; }
 #hnoxjajpqy .gt_font_italic { font-style: italic; }
 #hnoxjajpqy .gt_super { font-size: 65%; }
 #hnoxjajpqy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hnoxjajpqy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hnoxjajpqy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hnoxjajpqy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hnoxjajpqy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hnoxjajpqy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#gghfmxpgfx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gghfmxpgfx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gghfmxpgfx p { margin: 0; padding: 0; }
 #gghfmxpgfx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gghfmxpgfx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gghfmxpgfx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gghfmxpgfx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gghfmxpgfx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gghfmxpgfx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gghfmxpgfx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gghfmxpgfx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gghfmxpgfx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gghfmxpgfx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gghfmxpgfx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gghfmxpgfx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gghfmxpgfx .gt_spanner_row { border-bottom-style: hidden; }
 #gghfmxpgfx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gghfmxpgfx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gghfmxpgfx .gt_from_md> :first-child { margin-top: 0; }
 #gghfmxpgfx .gt_from_md> :last-child { margin-bottom: 0; }
 #gghfmxpgfx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gghfmxpgfx .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gghfmxpgfx .gt_indent_1 { text-indent: 5px; }
 #gghfmxpgfx .gt_indent_2 { text-indent: calc(5px * 2); }
 #gghfmxpgfx .gt_indent_3 { text-indent: calc(5px * 3); }
 #gghfmxpgfx .gt_indent_4 { text-indent: calc(5px * 4); }
 #gghfmxpgfx .gt_indent_5 { text-indent: calc(5px * 5); }
 #gghfmxpgfx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gghfmxpgfx .gt_row_group_first td { border-top-width: 2px; }
 #gghfmxpgfx .gt_row_group_first th { border-top-width: 2px; }
 #gghfmxpgfx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gghfmxpgfx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gghfmxpgfx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gghfmxpgfx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gghfmxpgfx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gghfmxpgfx .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gghfmxpgfx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gghfmxpgfx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gghfmxpgfx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gghfmxpgfx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gghfmxpgfx .gt_left { text-align: left; }
 #gghfmxpgfx .gt_center { text-align: center; }
 #gghfmxpgfx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gghfmxpgfx .gt_font_normal { font-weight: normal; }
 #gghfmxpgfx .gt_font_bold { font-weight: bold; }
 #gghfmxpgfx .gt_font_italic { font-style: italic; }
 #gghfmxpgfx .gt_super { font-size: 65%; }
 #gghfmxpgfx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gghfmxpgfx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gghfmxpgfx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gghfmxpgfx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gghfmxpgfx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gghfmxpgfx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
