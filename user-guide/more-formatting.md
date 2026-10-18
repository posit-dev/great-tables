# More Formatting Options

The [Formatting Values](formatting-values.md) page introduced the basics of [fmt_number()](../reference/GT.fmt_number.md#great_tables.GT.fmt_number), [fmt_currency()](../reference/GT.fmt_currency.md#great_tables.GT.fmt_currency), [fmt_date()](../reference/GT.fmt_date.md#great_tables.GT.fmt_date), and [fmt_time()](../reference/GT.fmt_time.md#great_tables.GT.fmt_time). But **Great Tables** has a much larger formatting toolkit. This page covers additional formatters that handle percentages, byte sizes, durations, scientific units, icons, flags, images, boolean values, Markdown, and more. Each formatter transforms raw cell data into presentation-ready content.

When choosing a formatter, start with the semantic meaning of your data. If a column represents a file size, reach for [fmt_bytes()](../reference/GT.fmt_bytes.md#great_tables.GT.fmt_bytes) rather than [fmt_number()](../reference/GT.fmt_number.md#great_tables.GT.fmt_number) with manual suffix logic. If a column holds time durations, use [fmt_duration()](../reference/GT.fmt_duration.md#great_tables.GT.fmt_duration) instead of formatting seconds by hand. Semantic formatters produce more consistent output and handle edge cases (like unit boundaries and scaling) automatically, so you get correct results without writing extra logic.


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
#dbdhbfobeh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dbdhbfobeh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dbdhbfobeh p { margin: 0; padding: 0; }
 #dbdhbfobeh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dbdhbfobeh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dbdhbfobeh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dbdhbfobeh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dbdhbfobeh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dbdhbfobeh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dbdhbfobeh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dbdhbfobeh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dbdhbfobeh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dbdhbfobeh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dbdhbfobeh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dbdhbfobeh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dbdhbfobeh .gt_spanner_row { border-bottom-style: hidden; }
 #dbdhbfobeh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dbdhbfobeh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dbdhbfobeh .gt_from_md> :first-child { margin-top: 0; }
 #dbdhbfobeh .gt_from_md> :last-child { margin-bottom: 0; }
 #dbdhbfobeh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dbdhbfobeh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dbdhbfobeh .gt_indent_1 { text-indent: 5px; }
 #dbdhbfobeh .gt_indent_2 { text-indent: calc(5px * 2); }
 #dbdhbfobeh .gt_indent_3 { text-indent: calc(5px * 3); }
 #dbdhbfobeh .gt_indent_4 { text-indent: calc(5px * 4); }
 #dbdhbfobeh .gt_indent_5 { text-indent: calc(5px * 5); }
 #dbdhbfobeh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dbdhbfobeh .gt_row_group_first td { border-top-width: 2px; }
 #dbdhbfobeh .gt_row_group_first th { border-top-width: 2px; }
 #dbdhbfobeh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dbdhbfobeh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dbdhbfobeh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dbdhbfobeh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dbdhbfobeh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dbdhbfobeh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dbdhbfobeh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dbdhbfobeh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dbdhbfobeh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dbdhbfobeh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dbdhbfobeh .gt_left { text-align: left; }
 #dbdhbfobeh .gt_center { text-align: center; }
 #dbdhbfobeh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dbdhbfobeh .gt_font_normal { font-weight: normal; }
 #dbdhbfobeh .gt_font_bold { font-weight: bold; }
 #dbdhbfobeh .gt_font_italic { font-style: italic; }
 #dbdhbfobeh .gt_super { font-size: 65%; }
 #dbdhbfobeh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dbdhbfobeh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dbdhbfobeh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dbdhbfobeh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dbdhbfobeh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dbdhbfobeh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zrbzsaroas table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zrbzsaroas thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zrbzsaroas p { margin: 0; padding: 0; }
 #zrbzsaroas .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zrbzsaroas .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zrbzsaroas .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zrbzsaroas .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zrbzsaroas .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zrbzsaroas .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zrbzsaroas .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zrbzsaroas .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zrbzsaroas .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zrbzsaroas .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zrbzsaroas .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zrbzsaroas .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zrbzsaroas .gt_spanner_row { border-bottom-style: hidden; }
 #zrbzsaroas .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zrbzsaroas .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zrbzsaroas .gt_from_md> :first-child { margin-top: 0; }
 #zrbzsaroas .gt_from_md> :last-child { margin-bottom: 0; }
 #zrbzsaroas .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zrbzsaroas .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zrbzsaroas .gt_indent_1 { text-indent: 5px; }
 #zrbzsaroas .gt_indent_2 { text-indent: calc(5px * 2); }
 #zrbzsaroas .gt_indent_3 { text-indent: calc(5px * 3); }
 #zrbzsaroas .gt_indent_4 { text-indent: calc(5px * 4); }
 #zrbzsaroas .gt_indent_5 { text-indent: calc(5px * 5); }
 #zrbzsaroas .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zrbzsaroas .gt_row_group_first td { border-top-width: 2px; }
 #zrbzsaroas .gt_row_group_first th { border-top-width: 2px; }
 #zrbzsaroas .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zrbzsaroas .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zrbzsaroas .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zrbzsaroas .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zrbzsaroas .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zrbzsaroas .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zrbzsaroas .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zrbzsaroas .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zrbzsaroas .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zrbzsaroas .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zrbzsaroas .gt_left { text-align: left; }
 #zrbzsaroas .gt_center { text-align: center; }
 #zrbzsaroas .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zrbzsaroas .gt_font_normal { font-weight: normal; }
 #zrbzsaroas .gt_font_bold { font-weight: bold; }
 #zrbzsaroas .gt_font_italic { font-style: italic; }
 #zrbzsaroas .gt_super { font-size: 65%; }
 #zrbzsaroas .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zrbzsaroas .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zrbzsaroas .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zrbzsaroas .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zrbzsaroas .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zrbzsaroas .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zvcnqicwdl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zvcnqicwdl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zvcnqicwdl p { margin: 0; padding: 0; }
 #zvcnqicwdl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zvcnqicwdl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zvcnqicwdl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zvcnqicwdl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zvcnqicwdl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zvcnqicwdl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zvcnqicwdl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zvcnqicwdl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zvcnqicwdl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zvcnqicwdl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zvcnqicwdl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zvcnqicwdl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zvcnqicwdl .gt_spanner_row { border-bottom-style: hidden; }
 #zvcnqicwdl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zvcnqicwdl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zvcnqicwdl .gt_from_md> :first-child { margin-top: 0; }
 #zvcnqicwdl .gt_from_md> :last-child { margin-bottom: 0; }
 #zvcnqicwdl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zvcnqicwdl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zvcnqicwdl .gt_indent_1 { text-indent: 5px; }
 #zvcnqicwdl .gt_indent_2 { text-indent: calc(5px * 2); }
 #zvcnqicwdl .gt_indent_3 { text-indent: calc(5px * 3); }
 #zvcnqicwdl .gt_indent_4 { text-indent: calc(5px * 4); }
 #zvcnqicwdl .gt_indent_5 { text-indent: calc(5px * 5); }
 #zvcnqicwdl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zvcnqicwdl .gt_row_group_first td { border-top-width: 2px; }
 #zvcnqicwdl .gt_row_group_first th { border-top-width: 2px; }
 #zvcnqicwdl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zvcnqicwdl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zvcnqicwdl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zvcnqicwdl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zvcnqicwdl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zvcnqicwdl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zvcnqicwdl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zvcnqicwdl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zvcnqicwdl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zvcnqicwdl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zvcnqicwdl .gt_left { text-align: left; }
 #zvcnqicwdl .gt_center { text-align: center; }
 #zvcnqicwdl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zvcnqicwdl .gt_font_normal { font-weight: normal; }
 #zvcnqicwdl .gt_font_bold { font-weight: bold; }
 #zvcnqicwdl .gt_font_italic { font-style: italic; }
 #zvcnqicwdl .gt_super { font-size: 65%; }
 #zvcnqicwdl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zvcnqicwdl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zvcnqicwdl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zvcnqicwdl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zvcnqicwdl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zvcnqicwdl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#iqmzupjkli table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iqmzupjkli thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iqmzupjkli p { margin: 0; padding: 0; }
 #iqmzupjkli .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #iqmzupjkli .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iqmzupjkli .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iqmzupjkli .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iqmzupjkli .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iqmzupjkli .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iqmzupjkli .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iqmzupjkli .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iqmzupjkli .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iqmzupjkli .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iqmzupjkli .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iqmzupjkli .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iqmzupjkli .gt_spanner_row { border-bottom-style: hidden; }
 #iqmzupjkli .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iqmzupjkli .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #iqmzupjkli .gt_from_md> :first-child { margin-top: 0; }
 #iqmzupjkli .gt_from_md> :last-child { margin-bottom: 0; }
 #iqmzupjkli .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #iqmzupjkli .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #iqmzupjkli .gt_indent_1 { text-indent: 5px; }
 #iqmzupjkli .gt_indent_2 { text-indent: calc(5px * 2); }
 #iqmzupjkli .gt_indent_3 { text-indent: calc(5px * 3); }
 #iqmzupjkli .gt_indent_4 { text-indent: calc(5px * 4); }
 #iqmzupjkli .gt_indent_5 { text-indent: calc(5px * 5); }
 #iqmzupjkli .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iqmzupjkli .gt_row_group_first td { border-top-width: 2px; }
 #iqmzupjkli .gt_row_group_first th { border-top-width: 2px; }
 #iqmzupjkli .gt_striped { color: #333333; background-color: #F4F4F4; }
 #iqmzupjkli .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iqmzupjkli .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iqmzupjkli .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #iqmzupjkli .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iqmzupjkli .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iqmzupjkli .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iqmzupjkli .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iqmzupjkli .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iqmzupjkli .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iqmzupjkli .gt_left { text-align: left; }
 #iqmzupjkli .gt_center { text-align: center; }
 #iqmzupjkli .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iqmzupjkli .gt_font_normal { font-weight: normal; }
 #iqmzupjkli .gt_font_bold { font-weight: bold; }
 #iqmzupjkli .gt_font_italic { font-style: italic; }
 #iqmzupjkli .gt_super { font-size: 65%; }
 #iqmzupjkli .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iqmzupjkli .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #iqmzupjkli .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iqmzupjkli .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iqmzupjkli .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iqmzupjkli .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rgrmcedhyp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rgrmcedhyp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rgrmcedhyp p { margin: 0; padding: 0; }
 #rgrmcedhyp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rgrmcedhyp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rgrmcedhyp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rgrmcedhyp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rgrmcedhyp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rgrmcedhyp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rgrmcedhyp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rgrmcedhyp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rgrmcedhyp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rgrmcedhyp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rgrmcedhyp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rgrmcedhyp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rgrmcedhyp .gt_spanner_row { border-bottom-style: hidden; }
 #rgrmcedhyp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rgrmcedhyp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rgrmcedhyp .gt_from_md> :first-child { margin-top: 0; }
 #rgrmcedhyp .gt_from_md> :last-child { margin-bottom: 0; }
 #rgrmcedhyp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rgrmcedhyp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rgrmcedhyp .gt_indent_1 { text-indent: 5px; }
 #rgrmcedhyp .gt_indent_2 { text-indent: calc(5px * 2); }
 #rgrmcedhyp .gt_indent_3 { text-indent: calc(5px * 3); }
 #rgrmcedhyp .gt_indent_4 { text-indent: calc(5px * 4); }
 #rgrmcedhyp .gt_indent_5 { text-indent: calc(5px * 5); }
 #rgrmcedhyp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rgrmcedhyp .gt_row_group_first td { border-top-width: 2px; }
 #rgrmcedhyp .gt_row_group_first th { border-top-width: 2px; }
 #rgrmcedhyp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rgrmcedhyp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rgrmcedhyp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rgrmcedhyp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rgrmcedhyp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rgrmcedhyp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rgrmcedhyp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rgrmcedhyp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rgrmcedhyp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rgrmcedhyp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rgrmcedhyp .gt_left { text-align: left; }
 #rgrmcedhyp .gt_center { text-align: center; }
 #rgrmcedhyp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rgrmcedhyp .gt_font_normal { font-weight: normal; }
 #rgrmcedhyp .gt_font_bold { font-weight: bold; }
 #rgrmcedhyp .gt_font_italic { font-style: italic; }
 #rgrmcedhyp .gt_super { font-size: 65%; }
 #rgrmcedhyp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rgrmcedhyp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rgrmcedhyp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rgrmcedhyp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rgrmcedhyp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rgrmcedhyp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wzmksfvpay table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wzmksfvpay thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wzmksfvpay p { margin: 0; padding: 0; }
 #wzmksfvpay .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wzmksfvpay .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wzmksfvpay .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wzmksfvpay .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wzmksfvpay .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wzmksfvpay .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wzmksfvpay .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wzmksfvpay .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wzmksfvpay .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wzmksfvpay .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wzmksfvpay .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wzmksfvpay .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wzmksfvpay .gt_spanner_row { border-bottom-style: hidden; }
 #wzmksfvpay .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wzmksfvpay .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wzmksfvpay .gt_from_md> :first-child { margin-top: 0; }
 #wzmksfvpay .gt_from_md> :last-child { margin-bottom: 0; }
 #wzmksfvpay .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wzmksfvpay .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wzmksfvpay .gt_indent_1 { text-indent: 5px; }
 #wzmksfvpay .gt_indent_2 { text-indent: calc(5px * 2); }
 #wzmksfvpay .gt_indent_3 { text-indent: calc(5px * 3); }
 #wzmksfvpay .gt_indent_4 { text-indent: calc(5px * 4); }
 #wzmksfvpay .gt_indent_5 { text-indent: calc(5px * 5); }
 #wzmksfvpay .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wzmksfvpay .gt_row_group_first td { border-top-width: 2px; }
 #wzmksfvpay .gt_row_group_first th { border-top-width: 2px; }
 #wzmksfvpay .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wzmksfvpay .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wzmksfvpay .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wzmksfvpay .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wzmksfvpay .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wzmksfvpay .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wzmksfvpay .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wzmksfvpay .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wzmksfvpay .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wzmksfvpay .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wzmksfvpay .gt_left { text-align: left; }
 #wzmksfvpay .gt_center { text-align: center; }
 #wzmksfvpay .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wzmksfvpay .gt_font_normal { font-weight: normal; }
 #wzmksfvpay .gt_font_bold { font-weight: bold; }
 #wzmksfvpay .gt_font_italic { font-style: italic; }
 #wzmksfvpay .gt_super { font-size: 65%; }
 #wzmksfvpay .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wzmksfvpay .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wzmksfvpay .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wzmksfvpay .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wzmksfvpay .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wzmksfvpay .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#mpvfhxlfsr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mpvfhxlfsr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mpvfhxlfsr p { margin: 0; padding: 0; }
 #mpvfhxlfsr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mpvfhxlfsr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mpvfhxlfsr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mpvfhxlfsr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mpvfhxlfsr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mpvfhxlfsr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mpvfhxlfsr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mpvfhxlfsr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mpvfhxlfsr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mpvfhxlfsr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mpvfhxlfsr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mpvfhxlfsr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mpvfhxlfsr .gt_spanner_row { border-bottom-style: hidden; }
 #mpvfhxlfsr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mpvfhxlfsr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mpvfhxlfsr .gt_from_md> :first-child { margin-top: 0; }
 #mpvfhxlfsr .gt_from_md> :last-child { margin-bottom: 0; }
 #mpvfhxlfsr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mpvfhxlfsr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mpvfhxlfsr .gt_indent_1 { text-indent: 5px; }
 #mpvfhxlfsr .gt_indent_2 { text-indent: calc(5px * 2); }
 #mpvfhxlfsr .gt_indent_3 { text-indent: calc(5px * 3); }
 #mpvfhxlfsr .gt_indent_4 { text-indent: calc(5px * 4); }
 #mpvfhxlfsr .gt_indent_5 { text-indent: calc(5px * 5); }
 #mpvfhxlfsr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mpvfhxlfsr .gt_row_group_first td { border-top-width: 2px; }
 #mpvfhxlfsr .gt_row_group_first th { border-top-width: 2px; }
 #mpvfhxlfsr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mpvfhxlfsr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mpvfhxlfsr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mpvfhxlfsr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mpvfhxlfsr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mpvfhxlfsr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mpvfhxlfsr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mpvfhxlfsr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mpvfhxlfsr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mpvfhxlfsr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mpvfhxlfsr .gt_left { text-align: left; }
 #mpvfhxlfsr .gt_center { text-align: center; }
 #mpvfhxlfsr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mpvfhxlfsr .gt_font_normal { font-weight: normal; }
 #mpvfhxlfsr .gt_font_bold { font-weight: bold; }
 #mpvfhxlfsr .gt_font_italic { font-style: italic; }
 #mpvfhxlfsr .gt_super { font-size: 65%; }
 #mpvfhxlfsr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mpvfhxlfsr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mpvfhxlfsr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mpvfhxlfsr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mpvfhxlfsr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mpvfhxlfsr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qmhojcgofb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qmhojcgofb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qmhojcgofb p { margin: 0; padding: 0; }
 #qmhojcgofb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qmhojcgofb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qmhojcgofb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qmhojcgofb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qmhojcgofb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qmhojcgofb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qmhojcgofb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qmhojcgofb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qmhojcgofb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qmhojcgofb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qmhojcgofb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qmhojcgofb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qmhojcgofb .gt_spanner_row { border-bottom-style: hidden; }
 #qmhojcgofb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qmhojcgofb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qmhojcgofb .gt_from_md> :first-child { margin-top: 0; }
 #qmhojcgofb .gt_from_md> :last-child { margin-bottom: 0; }
 #qmhojcgofb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qmhojcgofb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qmhojcgofb .gt_indent_1 { text-indent: 5px; }
 #qmhojcgofb .gt_indent_2 { text-indent: calc(5px * 2); }
 #qmhojcgofb .gt_indent_3 { text-indent: calc(5px * 3); }
 #qmhojcgofb .gt_indent_4 { text-indent: calc(5px * 4); }
 #qmhojcgofb .gt_indent_5 { text-indent: calc(5px * 5); }
 #qmhojcgofb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qmhojcgofb .gt_row_group_first td { border-top-width: 2px; }
 #qmhojcgofb .gt_row_group_first th { border-top-width: 2px; }
 #qmhojcgofb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qmhojcgofb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qmhojcgofb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qmhojcgofb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qmhojcgofb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qmhojcgofb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qmhojcgofb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qmhojcgofb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qmhojcgofb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qmhojcgofb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qmhojcgofb .gt_left { text-align: left; }
 #qmhojcgofb .gt_center { text-align: center; }
 #qmhojcgofb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qmhojcgofb .gt_font_normal { font-weight: normal; }
 #qmhojcgofb .gt_font_bold { font-weight: bold; }
 #qmhojcgofb .gt_font_italic { font-style: italic; }
 #qmhojcgofb .gt_super { font-size: 65%; }
 #qmhojcgofb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qmhojcgofb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qmhojcgofb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qmhojcgofb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qmhojcgofb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qmhojcgofb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hvkohasyda table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hvkohasyda thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hvkohasyda p { margin: 0; padding: 0; }
 #hvkohasyda .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hvkohasyda .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hvkohasyda .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hvkohasyda .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hvkohasyda .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hvkohasyda .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hvkohasyda .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hvkohasyda .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hvkohasyda .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hvkohasyda .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hvkohasyda .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hvkohasyda .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hvkohasyda .gt_spanner_row { border-bottom-style: hidden; }
 #hvkohasyda .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hvkohasyda .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hvkohasyda .gt_from_md> :first-child { margin-top: 0; }
 #hvkohasyda .gt_from_md> :last-child { margin-bottom: 0; }
 #hvkohasyda .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hvkohasyda .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hvkohasyda .gt_indent_1 { text-indent: 5px; }
 #hvkohasyda .gt_indent_2 { text-indent: calc(5px * 2); }
 #hvkohasyda .gt_indent_3 { text-indent: calc(5px * 3); }
 #hvkohasyda .gt_indent_4 { text-indent: calc(5px * 4); }
 #hvkohasyda .gt_indent_5 { text-indent: calc(5px * 5); }
 #hvkohasyda .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hvkohasyda .gt_row_group_first td { border-top-width: 2px; }
 #hvkohasyda .gt_row_group_first th { border-top-width: 2px; }
 #hvkohasyda .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hvkohasyda .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hvkohasyda .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hvkohasyda .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hvkohasyda .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hvkohasyda .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hvkohasyda .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hvkohasyda .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hvkohasyda .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hvkohasyda .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hvkohasyda .gt_left { text-align: left; }
 #hvkohasyda .gt_center { text-align: center; }
 #hvkohasyda .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hvkohasyda .gt_font_normal { font-weight: normal; }
 #hvkohasyda .gt_font_bold { font-weight: bold; }
 #hvkohasyda .gt_font_italic { font-style: italic; }
 #hvkohasyda .gt_super { font-size: 65%; }
 #hvkohasyda .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hvkohasyda .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hvkohasyda .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hvkohasyda .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hvkohasyda .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hvkohasyda .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#uggtikgfzy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uggtikgfzy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uggtikgfzy p { margin: 0; padding: 0; }
 #uggtikgfzy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #uggtikgfzy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uggtikgfzy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uggtikgfzy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uggtikgfzy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uggtikgfzy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uggtikgfzy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uggtikgfzy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uggtikgfzy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uggtikgfzy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uggtikgfzy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uggtikgfzy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uggtikgfzy .gt_spanner_row { border-bottom-style: hidden; }
 #uggtikgfzy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uggtikgfzy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #uggtikgfzy .gt_from_md> :first-child { margin-top: 0; }
 #uggtikgfzy .gt_from_md> :last-child { margin-bottom: 0; }
 #uggtikgfzy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #uggtikgfzy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #uggtikgfzy .gt_indent_1 { text-indent: 5px; }
 #uggtikgfzy .gt_indent_2 { text-indent: calc(5px * 2); }
 #uggtikgfzy .gt_indent_3 { text-indent: calc(5px * 3); }
 #uggtikgfzy .gt_indent_4 { text-indent: calc(5px * 4); }
 #uggtikgfzy .gt_indent_5 { text-indent: calc(5px * 5); }
 #uggtikgfzy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uggtikgfzy .gt_row_group_first td { border-top-width: 2px; }
 #uggtikgfzy .gt_row_group_first th { border-top-width: 2px; }
 #uggtikgfzy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uggtikgfzy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uggtikgfzy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uggtikgfzy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uggtikgfzy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uggtikgfzy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uggtikgfzy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uggtikgfzy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uggtikgfzy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uggtikgfzy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uggtikgfzy .gt_left { text-align: left; }
 #uggtikgfzy .gt_center { text-align: center; }
 #uggtikgfzy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uggtikgfzy .gt_font_normal { font-weight: normal; }
 #uggtikgfzy .gt_font_bold { font-weight: bold; }
 #uggtikgfzy .gt_font_italic { font-style: italic; }
 #uggtikgfzy .gt_super { font-size: 65%; }
 #uggtikgfzy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uggtikgfzy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uggtikgfzy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uggtikgfzy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uggtikgfzy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uggtikgfzy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#aurwnysujh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#aurwnysujh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#aurwnysujh p { margin: 0; padding: 0; }
 #aurwnysujh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #aurwnysujh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #aurwnysujh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #aurwnysujh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #aurwnysujh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aurwnysujh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aurwnysujh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #aurwnysujh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #aurwnysujh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #aurwnysujh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #aurwnysujh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #aurwnysujh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #aurwnysujh .gt_spanner_row { border-bottom-style: hidden; }
 #aurwnysujh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #aurwnysujh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #aurwnysujh .gt_from_md> :first-child { margin-top: 0; }
 #aurwnysujh .gt_from_md> :last-child { margin-bottom: 0; }
 #aurwnysujh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #aurwnysujh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #aurwnysujh .gt_indent_1 { text-indent: 5px; }
 #aurwnysujh .gt_indent_2 { text-indent: calc(5px * 2); }
 #aurwnysujh .gt_indent_3 { text-indent: calc(5px * 3); }
 #aurwnysujh .gt_indent_4 { text-indent: calc(5px * 4); }
 #aurwnysujh .gt_indent_5 { text-indent: calc(5px * 5); }
 #aurwnysujh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #aurwnysujh .gt_row_group_first td { border-top-width: 2px; }
 #aurwnysujh .gt_row_group_first th { border-top-width: 2px; }
 #aurwnysujh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #aurwnysujh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aurwnysujh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aurwnysujh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #aurwnysujh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #aurwnysujh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #aurwnysujh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #aurwnysujh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #aurwnysujh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aurwnysujh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aurwnysujh .gt_left { text-align: left; }
 #aurwnysujh .gt_center { text-align: center; }
 #aurwnysujh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #aurwnysujh .gt_font_normal { font-weight: normal; }
 #aurwnysujh .gt_font_bold { font-weight: bold; }
 #aurwnysujh .gt_font_italic { font-style: italic; }
 #aurwnysujh .gt_super { font-size: 65%; }
 #aurwnysujh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aurwnysujh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #aurwnysujh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #aurwnysujh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #aurwnysujh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #aurwnysujh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#uizfovykar table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uizfovykar thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uizfovykar p { margin: 0; padding: 0; }
 #uizfovykar .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #uizfovykar .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uizfovykar .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uizfovykar .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uizfovykar .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uizfovykar .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uizfovykar .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uizfovykar .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uizfovykar .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uizfovykar .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uizfovykar .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uizfovykar .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uizfovykar .gt_spanner_row { border-bottom-style: hidden; }
 #uizfovykar .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uizfovykar .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #uizfovykar .gt_from_md> :first-child { margin-top: 0; }
 #uizfovykar .gt_from_md> :last-child { margin-bottom: 0; }
 #uizfovykar .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #uizfovykar .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #uizfovykar .gt_indent_1 { text-indent: 5px; }
 #uizfovykar .gt_indent_2 { text-indent: calc(5px * 2); }
 #uizfovykar .gt_indent_3 { text-indent: calc(5px * 3); }
 #uizfovykar .gt_indent_4 { text-indent: calc(5px * 4); }
 #uizfovykar .gt_indent_5 { text-indent: calc(5px * 5); }
 #uizfovykar .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uizfovykar .gt_row_group_first td { border-top-width: 2px; }
 #uizfovykar .gt_row_group_first th { border-top-width: 2px; }
 #uizfovykar .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uizfovykar .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uizfovykar .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uizfovykar .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uizfovykar .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uizfovykar .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uizfovykar .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uizfovykar .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uizfovykar .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uizfovykar .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uizfovykar .gt_left { text-align: left; }
 #uizfovykar .gt_center { text-align: center; }
 #uizfovykar .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uizfovykar .gt_font_normal { font-weight: normal; }
 #uizfovykar .gt_font_bold { font-weight: bold; }
 #uizfovykar .gt_font_italic { font-style: italic; }
 #uizfovykar .gt_super { font-size: 65%; }
 #uizfovykar .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uizfovykar .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uizfovykar .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uizfovykar .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uizfovykar .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uizfovykar .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fuhfxnafrz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fuhfxnafrz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fuhfxnafrz p { margin: 0; padding: 0; }
 #fuhfxnafrz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fuhfxnafrz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fuhfxnafrz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fuhfxnafrz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fuhfxnafrz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fuhfxnafrz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fuhfxnafrz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fuhfxnafrz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fuhfxnafrz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fuhfxnafrz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fuhfxnafrz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fuhfxnafrz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fuhfxnafrz .gt_spanner_row { border-bottom-style: hidden; }
 #fuhfxnafrz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fuhfxnafrz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fuhfxnafrz .gt_from_md> :first-child { margin-top: 0; }
 #fuhfxnafrz .gt_from_md> :last-child { margin-bottom: 0; }
 #fuhfxnafrz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fuhfxnafrz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fuhfxnafrz .gt_indent_1 { text-indent: 5px; }
 #fuhfxnafrz .gt_indent_2 { text-indent: calc(5px * 2); }
 #fuhfxnafrz .gt_indent_3 { text-indent: calc(5px * 3); }
 #fuhfxnafrz .gt_indent_4 { text-indent: calc(5px * 4); }
 #fuhfxnafrz .gt_indent_5 { text-indent: calc(5px * 5); }
 #fuhfxnafrz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fuhfxnafrz .gt_row_group_first td { border-top-width: 2px; }
 #fuhfxnafrz .gt_row_group_first th { border-top-width: 2px; }
 #fuhfxnafrz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fuhfxnafrz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fuhfxnafrz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fuhfxnafrz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fuhfxnafrz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fuhfxnafrz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fuhfxnafrz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fuhfxnafrz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fuhfxnafrz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fuhfxnafrz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fuhfxnafrz .gt_left { text-align: left; }
 #fuhfxnafrz .gt_center { text-align: center; }
 #fuhfxnafrz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fuhfxnafrz .gt_font_normal { font-weight: normal; }
 #fuhfxnafrz .gt_font_bold { font-weight: bold; }
 #fuhfxnafrz .gt_font_italic { font-style: italic; }
 #fuhfxnafrz .gt_super { font-size: 65%; }
 #fuhfxnafrz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fuhfxnafrz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fuhfxnafrz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fuhfxnafrz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fuhfxnafrz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fuhfxnafrz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ucmqahwdii table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ucmqahwdii thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ucmqahwdii p { margin: 0; padding: 0; }
 #ucmqahwdii .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ucmqahwdii .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ucmqahwdii .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ucmqahwdii .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ucmqahwdii .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ucmqahwdii .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ucmqahwdii .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ucmqahwdii .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ucmqahwdii .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ucmqahwdii .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ucmqahwdii .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ucmqahwdii .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ucmqahwdii .gt_spanner_row { border-bottom-style: hidden; }
 #ucmqahwdii .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ucmqahwdii .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ucmqahwdii .gt_from_md> :first-child { margin-top: 0; }
 #ucmqahwdii .gt_from_md> :last-child { margin-bottom: 0; }
 #ucmqahwdii .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ucmqahwdii .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ucmqahwdii .gt_indent_1 { text-indent: 5px; }
 #ucmqahwdii .gt_indent_2 { text-indent: calc(5px * 2); }
 #ucmqahwdii .gt_indent_3 { text-indent: calc(5px * 3); }
 #ucmqahwdii .gt_indent_4 { text-indent: calc(5px * 4); }
 #ucmqahwdii .gt_indent_5 { text-indent: calc(5px * 5); }
 #ucmqahwdii .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ucmqahwdii .gt_row_group_first td { border-top-width: 2px; }
 #ucmqahwdii .gt_row_group_first th { border-top-width: 2px; }
 #ucmqahwdii .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ucmqahwdii .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ucmqahwdii .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ucmqahwdii .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ucmqahwdii .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ucmqahwdii .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ucmqahwdii .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ucmqahwdii .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ucmqahwdii .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ucmqahwdii .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ucmqahwdii .gt_left { text-align: left; }
 #ucmqahwdii .gt_center { text-align: center; }
 #ucmqahwdii .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ucmqahwdii .gt_font_normal { font-weight: normal; }
 #ucmqahwdii .gt_font_bold { font-weight: bold; }
 #ucmqahwdii .gt_font_italic { font-style: italic; }
 #ucmqahwdii .gt_super { font-size: 65%; }
 #ucmqahwdii .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ucmqahwdii .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ucmqahwdii .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ucmqahwdii .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ucmqahwdii .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ucmqahwdii .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|  | icon_name | users |
|----|----|----|
| Web | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpzdGVlbGJsdWU7c3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjEuMGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0zNTIgMjU2YzAgMjIuMi0xLjIgNDMuNi0zLjMgNjRIMTYzLjNjLTIuMi0yMC40LTMuMy00MS44LTMuMy02NHMxLjItNDMuNiAzLjMtNjRIMzQ4LjdjMi4yIDIwLjQgMy4zIDQxLjggMy4zIDY0em0yOC44LTY0SDUwMy45YzUuMyAyMC41IDguMSA0MS45IDguMSA2NHMtMi44IDQzLjUtOC4xIDY0SDM4MC44YzIuMS0yMC42IDMuMi00MiAzLjItNjRzLTEuMS00My40LTMuMi02NHptMTEyLjYtMzJIMzc2LjdjLTEwLTYzLjktMjkuOC0xMTcuNC01NS4zLTE1MS42Yzc4LjMgMjAuNyAxNDIgNzcuNSAxNzEuOSAxNTEuNnptLTE0OS4xIDBIMTY3LjdjNi4xLTM2LjQgMTUuNS02OC42IDI3LTk0LjdjMTAuNS0yMy42IDIyLjItNDAuNyAzMy41LTUxLjVDMjM5LjQgMy4yIDI0OC43IDAgMjU2IDBzMTYuNiAzLjIgMjcuOCAxMy44YzExLjMgMTAuOCAyMyAyNy45IDMzLjUgNTEuNWMxMS42IDI2IDIxIDU4LjIgMjcgOTQuN3ptLTIwOSAwSDE4LjZDNDguNiA4NS45IDExMi4yIDI5LjEgMTkwLjYgOC40QzE2NS4xIDQyLjYgMTQ1LjMgOTYuMSAxMzUuMyAxNjB6TTguMSAxOTJIMTMxLjJjLTIuMSAyMC42LTMuMiA0Mi0zLjIgNjRzMS4xIDQzLjQgMy4yIDY0SDguMUMyLjggMjk5LjUgMCAyNzguMSAwIDI1NnMyLjgtNDMuNSA4LjEtNjR6TTE5NC43IDQ0Ni42Yy0xMS42LTI2LTIwLjktNTguMi0yNy05NC42SDM0NC4zYy02LjEgMzYuNC0xNS41IDY4LjYtMjcgOTQuNmMtMTAuNSAyMy42LTIyLjIgNDAuNy0zMy41IDUxLjVDMjcyLjYgNTA4LjggMjYzLjMgNTEyIDI1NiA1MTJzLTE2LjYtMy4yLTI3LjgtMTMuOGMtMTEuMy0xMC44LTIzLTI3LjktMzMuNS01MS41ek0xMzUuMyAzNTJjMTAgNjMuOSAyOS44IDExNy40IDU1LjMgMTUxLjZDMTEyLjIgNDgyLjkgNDguNiA0MjYuMSAxOC42IDM1MkgxMzUuM3ptMzU4LjEgMGMtMzAgNzQuMS05My42IDEzMC45LTE3MS45IDE1MS42YzI1LjUtMzQuMiA0NS4yLTg3LjcgNTUuMy0xNTEuNkg0OTMuNHoiIC8+PC9zdmc+" class="fa" /></span> | 45.00K |
| Mobile | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpzdGVlbGJsdWU7c3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjAuNzVlbTtwb3NpdGlvbjpyZWxhdGl2ZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtvdmVyZmxvdzp2aXNpYmxlOyI+ICA8cGF0aCBkPSJNODAgMEM0NC43IDAgMTYgMjguNyAxNiA2NFY0NDhjMCAzNS4zIDI4LjcgNjQgNjQgNjRIMzA0YzM1LjMgMCA2NC0yOC43IDY0LTY0VjY0YzAtMzUuMy0yOC43LTY0LTY0LTY0SDgwem04MCA0MzJoNjRjOC44IDAgMTYgNy4yIDE2IDE2cy03LjIgMTYtMTYgMTZIMTYwYy04LjggMC0xNi03LjItMTYtMTZzNy4yLTE2IDE2LTE2eiIgLz48L3N2Zz4=" class="fa" /></span> | 32.00K |
| Desktop | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTc2IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpzdGVlbGJsdWU7c3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjEuMTJlbTtwb3NpdGlvbjpyZWxhdGl2ZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtvdmVyZmxvdzp2aXNpYmxlOyI+ICA8cGF0aCBkPSJNNjQgMEMyOC43IDAgMCAyOC43IDAgNjRWMzUyYzAgMzUuMyAyOC43IDY0IDY0IDY0SDI0MGwtMTAuNyAzMkgxNjBjLTE3LjcgMC0zMiAxNC4zLTMyIDMyczE0LjMgMzIgMzIgMzJINDE2YzE3LjcgMCAzMi0xNC4zIDMyLTMycy0xNC4zLTMyLTMyLTMySDM0Ni43TDMzNiA0MTZINTEyYzM1LjMgMCA2NC0yOC43IDY0LTY0VjY0YzAtMzUuMy0yOC43LTY0LTY0LTY0SDY0ek01MTIgNjRWMjg4SDY0VjY0SDUxMnoiIC8+PC9zdmc+" class="fa" /></span> | 12.00K |


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
#esgmdryvrb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#esgmdryvrb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#esgmdryvrb p { margin: 0; padding: 0; }
 #esgmdryvrb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #esgmdryvrb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #esgmdryvrb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #esgmdryvrb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #esgmdryvrb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #esgmdryvrb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #esgmdryvrb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #esgmdryvrb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #esgmdryvrb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #esgmdryvrb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #esgmdryvrb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #esgmdryvrb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #esgmdryvrb .gt_spanner_row { border-bottom-style: hidden; }
 #esgmdryvrb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #esgmdryvrb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #esgmdryvrb .gt_from_md> :first-child { margin-top: 0; }
 #esgmdryvrb .gt_from_md> :last-child { margin-bottom: 0; }
 #esgmdryvrb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #esgmdryvrb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #esgmdryvrb .gt_indent_1 { text-indent: 5px; }
 #esgmdryvrb .gt_indent_2 { text-indent: calc(5px * 2); }
 #esgmdryvrb .gt_indent_3 { text-indent: calc(5px * 3); }
 #esgmdryvrb .gt_indent_4 { text-indent: calc(5px * 4); }
 #esgmdryvrb .gt_indent_5 { text-indent: calc(5px * 5); }
 #esgmdryvrb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #esgmdryvrb .gt_row_group_first td { border-top-width: 2px; }
 #esgmdryvrb .gt_row_group_first th { border-top-width: 2px; }
 #esgmdryvrb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #esgmdryvrb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #esgmdryvrb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #esgmdryvrb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #esgmdryvrb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #esgmdryvrb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #esgmdryvrb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #esgmdryvrb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #esgmdryvrb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #esgmdryvrb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #esgmdryvrb .gt_left { text-align: left; }
 #esgmdryvrb .gt_center { text-align: center; }
 #esgmdryvrb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #esgmdryvrb .gt_font_normal { font-weight: normal; }
 #esgmdryvrb .gt_font_bold { font-weight: bold; }
 #esgmdryvrb .gt_font_italic { font-style: italic; }
 #esgmdryvrb .gt_super { font-size: 65%; }
 #esgmdryvrb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #esgmdryvrb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #esgmdryvrb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #esgmdryvrb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #esgmdryvrb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #esgmdryvrb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|  | icon_name | users |
|----|----|----|
| Web | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpyb3lhbGJsdWU7c3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjEuMGVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik0zNTIgMjU2YzAgMjIuMi0xLjIgNDMuNi0zLjMgNjRIMTYzLjNjLTIuMi0yMC40LTMuMy00MS44LTMuMy02NHMxLjItNDMuNiAzLjMtNjRIMzQ4LjdjMi4yIDIwLjQgMy4zIDQxLjggMy4zIDY0em0yOC44LTY0SDUwMy45YzUuMyAyMC41IDguMSA0MS45IDguMSA2NHMtMi44IDQzLjUtOC4xIDY0SDM4MC44YzIuMS0yMC42IDMuMi00MiAzLjItNjRzLTEuMS00My40LTMuMi02NHptMTEyLjYtMzJIMzc2LjdjLTEwLTYzLjktMjkuOC0xMTcuNC01NS4zLTE1MS42Yzc4LjMgMjAuNyAxNDIgNzcuNSAxNzEuOSAxNTEuNnptLTE0OS4xIDBIMTY3LjdjNi4xLTM2LjQgMTUuNS02OC42IDI3LTk0LjdjMTAuNS0yMy42IDIyLjItNDAuNyAzMy41LTUxLjVDMjM5LjQgMy4yIDI0OC43IDAgMjU2IDBzMTYuNiAzLjIgMjcuOCAxMy44YzExLjMgMTAuOCAyMyAyNy45IDMzLjUgNTEuNWMxMS42IDI2IDIxIDU4LjIgMjcgOTQuN3ptLTIwOSAwSDE4LjZDNDguNiA4NS45IDExMi4yIDI5LjEgMTkwLjYgOC40QzE2NS4xIDQyLjYgMTQ1LjMgOTYuMSAxMzUuMyAxNjB6TTguMSAxOTJIMTMxLjJjLTIuMSAyMC42LTMuMiA0Mi0zLjIgNjRzMS4xIDQzLjQgMy4yIDY0SDguMUMyLjggMjk5LjUgMCAyNzguMSAwIDI1NnMyLjgtNDMuNSA4LjEtNjR6TTE5NC43IDQ0Ni42Yy0xMS42LTI2LTIwLjktNTguMi0yNy05NC42SDM0NC4zYy02LjEgMzYuNC0xNS41IDY4LjYtMjcgOTQuNmMtMTAuNSAyMy42LTIyLjIgNDAuNy0zMy41IDUxLjVDMjcyLjYgNTA4LjggMjYzLjMgNTEyIDI1NiA1MTJzLTE2LjYtMy4yLTI3LjgtMTMuOGMtMTEuMy0xMC44LTIzLTI3LjktMzMuNS01MS41ek0xMzUuMyAzNTJjMTAgNjMuOSAyOS44IDExNy40IDU1LjMgMTUxLjZDMTEyLjIgNDgyLjkgNDguNiA0MjYuMSAxOC42IDM1MkgxMzUuM3ptMzU4LjEgMGMtMzAgNzQuMS05My42IDEzMC45LTE3MS45IDE1MS42YzI1LjUtMzQuMiA0NS4yLTg3LjcgNTUuMy0xNTEuNkg0OTMuNHoiIC8+PC9zdmc+" class="fa" /></span> | 45000 |
| Mobile | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMzg0IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpmb3Jlc3RncmVlbjtzdHJva2Utd2lkdGg6MXB4O2hlaWdodDoxZW07d2lkdGg6MC43NWVtO3Bvc2l0aW9uOnJlbGF0aXZlO3ZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO292ZXJmbG93OnZpc2libGU7Ij4gIDxwYXRoIGQ9Ik04MCAwQzQ0LjcgMCAxNiAyOC43IDE2IDY0VjQ0OGMwIDM1LjMgMjguNyA2NCA2NCA2NEgzMDRjMzUuMyAwIDY0LTI4LjcgNjQtNjRWNjRjMC0zNS4zLTI4LjctNjQtNjQtNjRIODB6bTgwIDQzMmg2NGM4LjggMCAxNiA3LjIgMTYgMTZzLTcuMiAxNi0xNiAxNkgxNjBjLTguOCAwLTE2LTcuMi0xNi0xNnM3LjItMTYgMTYtMTZ6IiAvPjwvc3ZnPg==" class="fa" /></span> | 32000 |
| Desktop | <span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgNTc2IDUxMiIgcHJlc2VydmVhc3BlY3RyYXRpbz0ibm9uZSIgYXJpYS1oaWRkZW49InRydWUiIHJvbGU9ImltZyIgY2xhc3M9ImZhIiBzdHlsZT0iZmlsbDpzbGF0ZWdyYXk7c3Ryb2tlLXdpZHRoOjFweDtoZWlnaHQ6MWVtO3dpZHRoOjEuMTJlbTtwb3NpdGlvbjpyZWxhdGl2ZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtvdmVyZmxvdzp2aXNpYmxlOyI+ICA8cGF0aCBkPSJNNjQgMEMyOC43IDAgMCAyOC43IDAgNjRWMzUyYzAgMzUuMyAyOC43IDY0IDY0IDY0SDI0MGwtMTAuNyAzMkgxNjBjLTE3LjcgMC0zMiAxNC4zLTMyIDMyczE0LjMgMzIgMzIgMzJINDE2YzE3LjcgMCAzMi0xNC4zIDMyLTMycy0xNC4zLTMyLTMyLTMySDM0Ni43TDMzNiA0MTZINTEyYzM1LjMgMCA2NC0yOC43IDY0LTY0VjY0YzAtMzUuMy0yOC43LTY0LTY0LTY0SDY0ek01MTIgNjRWMjg4SDY0VjY0SDUxMnoiIC8+PC9zdmc+" class="fa" /></span> | 12000 |


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
#zkgppqtzup table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zkgppqtzup thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zkgppqtzup p { margin: 0; padding: 0; }
 #zkgppqtzup .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zkgppqtzup .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zkgppqtzup .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zkgppqtzup .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zkgppqtzup .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zkgppqtzup .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zkgppqtzup .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zkgppqtzup .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zkgppqtzup .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zkgppqtzup .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zkgppqtzup .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zkgppqtzup .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zkgppqtzup .gt_spanner_row { border-bottom-style: hidden; }
 #zkgppqtzup .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zkgppqtzup .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zkgppqtzup .gt_from_md> :first-child { margin-top: 0; }
 #zkgppqtzup .gt_from_md> :last-child { margin-bottom: 0; }
 #zkgppqtzup .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zkgppqtzup .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zkgppqtzup .gt_indent_1 { text-indent: 5px; }
 #zkgppqtzup .gt_indent_2 { text-indent: calc(5px * 2); }
 #zkgppqtzup .gt_indent_3 { text-indent: calc(5px * 3); }
 #zkgppqtzup .gt_indent_4 { text-indent: calc(5px * 4); }
 #zkgppqtzup .gt_indent_5 { text-indent: calc(5px * 5); }
 #zkgppqtzup .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zkgppqtzup .gt_row_group_first td { border-top-width: 2px; }
 #zkgppqtzup .gt_row_group_first th { border-top-width: 2px; }
 #zkgppqtzup .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zkgppqtzup .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zkgppqtzup .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zkgppqtzup .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zkgppqtzup .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zkgppqtzup .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zkgppqtzup .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zkgppqtzup .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zkgppqtzup .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zkgppqtzup .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zkgppqtzup .gt_left { text-align: left; }
 #zkgppqtzup .gt_center { text-align: center; }
 #zkgppqtzup .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zkgppqtzup .gt_font_normal { font-weight: normal; }
 #zkgppqtzup .gt_font_bold { font-weight: bold; }
 #zkgppqtzup .gt_font_italic { font-style: italic; }
 #zkgppqtzup .gt_super { font-size: 65%; }
 #zkgppqtzup .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zkgppqtzup .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zkgppqtzup .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zkgppqtzup .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zkgppqtzup .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zkgppqtzup .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|  | Flag | GDP (USD trillions) |
|----|----|----|
| United States | <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iVW5pdGVkIFN0YXRlcyIgd2lkdGg9IjUxMiIgaGVpZ2h0PSI1MTIiIHZpZXdib3g9IjAgMCA1MTIgNTEyIiBzdHlsZT0idmVydGljYWwtYWxpZ246LTAuMTI1ZW07aW1hZ2UtcmVuZGVyaW5nOm9wdGltaXplUXVhbGl0eTtoZWlnaHQ6MWVtO3dpZHRoOjFlbTsiPjx0aXRsZT5Vbml0ZWQgU3RhdGVzPC90aXRsZT48bWFzayBpZD0iY291bnRyeV9jb2RlLTAtYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2NvdW50cnlfY29kZS0wLWEpIj48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMjU2IDBoMjU2djY0bC0zMiAzMiAzMiAzMnY2NGwtMzIgMzIgMzIgMzJ2NjRsLTMyIDMyIDMyIDMydjY0bC0yNTYgMzJMMCA0NDh2LTY0bDMyLTMyLTMyLTMydi02NHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTIyNCA2NGgyODh2NjRIMjI0Wm0wIDEyOGgyODh2NjRIMjU2Wk0wIDMyMGg1MTJ2NjRIMFptMCAxMjhoNTEydjY0SDBaIiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0wIDBoMjU2djI1NkgwWiIgLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJtMTg3IDI0MyA1Ny00MWgtNzBsNTcgNDEtMjItNjd6bS04MSAwIDU3LTQxSDkzbDU3IDQxLTIyLTY3em0tODEgMCA1Ny00MUgxMmw1NyA0MS0yMi02N3ptMTYyLTgxIDU3LTQxaC03MGw1NyA0MS0yMi02N3ptLTgxIDAgNTctNDFIOTNsNTcgNDEtMjItNjd6bS04MSAwIDU3LTQxSDEybDU3IDQxLTIyLTY3Wm0xNjItODIgNTctNDFoLTcwbDU3IDQxLTIyLTY3Wm0tODEgMCA1Ny00MUg5M2w1NyA0MS0yMi02N3ptLTgxIDAgNTctNDFIMTJsNTcgNDEtMjItNjdaIiAvPjwvZz48L3N2Zz4=)</span> | 25.5 |
| United Kingdom | <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iVW5pdGVkIEtpbmdkb20iIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+VW5pdGVkIEtpbmdkb208L3RpdGxlPjxtYXNrIGlkPSJjb3VudHJ5X2NvZGUtMS1hIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjY291bnRyeV9jb2RlLTEtYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Im0wIDAgOCAyMi04IDIzdjIzbDMyIDU0LTMyIDU0djMybDMyIDQ4LTMyIDQ4djMybDMyIDU0LTMyIDU0djY4bDIyLTggMjMgOGgyM2w1NC0zMiA1NCAzMmgzMmw0OC0zMiA0OCAzMmgzMmw1NC0zMiA1NCAzMmg2OGwtOC0yMiA4LTIzdi0yM2wtMzItNTQgMzItNTR2LTMybC0zMi00OCAzMi00OHYtMzJsLTMyLTU0IDMyLTU0VjBsLTIyIDgtMjMtOGgtMjNsLTU0IDMyLTU0LTMyaC0zMmwtNDggMzItNDgtMzJoLTMybC01NCAzMkw2OCAwSDB6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0zMzYgMHYxMDhMNDQ0IDBabTE3NiA2OEw0MDQgMTc2aDEwOHpNMCAxNzZoMTA4TDAgNjhaTTY4IDBsMTA4IDEwOFYwWm0xMDggNTEyVjQwNEw2OCA1MTJaTTAgNDQ0bDEwOC0xMDhIMFptNTEyLTEwOEg0MDRsMTA4IDEwOFptLTY4IDE3NkwzMzYgNDA0djEwOHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMHY0NWwxMzEgMTMxaDQ1TDAgMHptMjA4IDB2MjA4SDB2OTZoMjA4djIwOGg5NlYzMDRoMjA4di05NkgzMDRWMGgtOTZ6bTI1OSAwTDMzNiAxMzF2NDVMNTEyIDBoLTQ1ek0xNzYgMzM2IDAgNTEyaDQ1bDEzMS0xMzF2LTQ1em0xNjAgMCAxNzYgMTc2di00NUwzODEgMzM2aC00NXoiIC8+PC9nPjwvc3ZnPg==)</span> | 3.1 |
| Japan | <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iSmFwYW4iIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+SmFwYW48L3RpdGxlPjxtYXNrIGlkPSJjb3VudHJ5X2NvZGUtMi1hIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjY291bnRyeV9jb2RlLTItYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0wIDBoNTEydjUxMkgweiIgLz48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjExMS4zIiBmaWxsPSIjZDgwMDI3Ij48L2NpcmNsZT48L2c+PC9zdmc+)</span> | 4.2 |
| Germany | <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iR2VybWFueSIgd2lkdGg9IjUxMiIgaGVpZ2h0PSI1MTIiIHZpZXdib3g9IjAgMCA1MTIgNTEyIiBzdHlsZT0idmVydGljYWwtYWxpZ246LTAuMTI1ZW07aW1hZ2UtcmVuZGVyaW5nOm9wdGltaXplUXVhbGl0eTtoZWlnaHQ6MWVtO3dpZHRoOjFlbTsiPjx0aXRsZT5HZXJtYW55PC90aXRsZT48bWFzayBpZD0iY291bnRyeV9jb2RlLTMtYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2NvdW50cnlfY29kZS0zLWEpIj48cGF0aCBmaWxsPSIjZmZkYTQ0IiBkPSJtMCAzNDUgMjU2LjctMjUuNUw1MTIgMzQ1djE2N0gweiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJtMCAxNjcgMjU1LTIzIDI1NyAyM3YxNzhIMHoiIC8+PHBhdGggZmlsbD0iIzMzMyIgZD0iTTAgMGg1MTJ2MTY3SDB6IiAvPjwvZz48L3N2Zz4=)</span> | 4.1 |
| Brazil | <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iQnJhemlsIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgdmlld2JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJ2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtpbWFnZS1yZW5kZXJpbmc6b3B0aW1pemVRdWFsaXR5O2hlaWdodDoxZW07d2lkdGg6MWVtOyI+PHRpdGxlPkJyYXppbDwvdGl0bGU+PG1hc2sgaWQ9ImNvdW50cnlfY29kZS00LWEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNjb3VudHJ5X2NvZGUtNC1hKSI+PHBhdGggZmlsbD0iIzZkYTU0NCIgZD0iTTAgMGg1MTJ2NTEySDB6IiAvPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Ik0yNTYgMTAwLjIgNDY3LjUgMjU2IDI1NiA0MTEuOCA0NC41IDI1NnoiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTE3NC4yIDIyMWE4NyA4NyAwIDAgMC03LjIgMzYuM2wxNjIgNDkuOGE4OC41IDg4LjUgMCAwIDAgMTQuNC0zNGMtNDAuNi02NS4zLTExOS43LTgwLjMtMTY5LjEtNTJ6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0yNTUuNyAxNjdhODkgODkgMCAwIDAtNDEuOSAxMC42IDg5IDg5IDAgMCAwLTM5LjYgNDMuNCAxODEuNyAxODEuNyAwIDAgMSAxNjkuMSA1Mi4yIDg5IDg5IDAgMCAwLTktNTkuNCA4OSA4OSAwIDAgMC03OC42LTQ2Ljh6TTIxMiAyNTAuNWExNDkgMTQ5IDAgMCAwLTQ1IDYuOCA4OSA4OSAwIDAgMCAxMC41IDQwLjkgODkgODkgMCAwIDAgMTIwLjYgMzYuMiA4OSA4OSAwIDAgMCAzMC43LTI3LjNBMTUxIDE1MSAwIDAgMCAyMTIgMjUwLjV6IiAvPjwvZz48L3N2Zz4=)</span> | 1.9 |


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
#eohcfhorvt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eohcfhorvt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eohcfhorvt p { margin: 0; padding: 0; }
 #eohcfhorvt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eohcfhorvt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eohcfhorvt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eohcfhorvt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eohcfhorvt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eohcfhorvt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eohcfhorvt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eohcfhorvt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eohcfhorvt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eohcfhorvt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eohcfhorvt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eohcfhorvt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eohcfhorvt .gt_spanner_row { border-bottom-style: hidden; }
 #eohcfhorvt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eohcfhorvt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eohcfhorvt .gt_from_md> :first-child { margin-top: 0; }
 #eohcfhorvt .gt_from_md> :last-child { margin-bottom: 0; }
 #eohcfhorvt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eohcfhorvt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eohcfhorvt .gt_indent_1 { text-indent: 5px; }
 #eohcfhorvt .gt_indent_2 { text-indent: calc(5px * 2); }
 #eohcfhorvt .gt_indent_3 { text-indent: calc(5px * 3); }
 #eohcfhorvt .gt_indent_4 { text-indent: calc(5px * 4); }
 #eohcfhorvt .gt_indent_5 { text-indent: calc(5px * 5); }
 #eohcfhorvt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eohcfhorvt .gt_row_group_first td { border-top-width: 2px; }
 #eohcfhorvt .gt_row_group_first th { border-top-width: 2px; }
 #eohcfhorvt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eohcfhorvt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eohcfhorvt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eohcfhorvt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eohcfhorvt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eohcfhorvt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eohcfhorvt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eohcfhorvt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eohcfhorvt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eohcfhorvt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eohcfhorvt .gt_left { text-align: left; }
 #eohcfhorvt .gt_center { text-align: center; }
 #eohcfhorvt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eohcfhorvt .gt_font_normal { font-weight: normal; }
 #eohcfhorvt .gt_font_bold { font-weight: bold; }
 #eohcfhorvt .gt_font_italic { font-style: italic; }
 #eohcfhorvt .gt_super { font-size: 65%; }
 #eohcfhorvt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eohcfhorvt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eohcfhorvt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eohcfhorvt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eohcfhorvt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eohcfhorvt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
