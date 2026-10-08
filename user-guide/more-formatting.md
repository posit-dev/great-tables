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
#tygwitruvz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tygwitruvz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tygwitruvz p { margin: 0; padding: 0; }
 #tygwitruvz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tygwitruvz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tygwitruvz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tygwitruvz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tygwitruvz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tygwitruvz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tygwitruvz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tygwitruvz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tygwitruvz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tygwitruvz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tygwitruvz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tygwitruvz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tygwitruvz .gt_spanner_row { border-bottom-style: hidden; }
 #tygwitruvz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tygwitruvz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tygwitruvz .gt_from_md> :first-child { margin-top: 0; }
 #tygwitruvz .gt_from_md> :last-child { margin-bottom: 0; }
 #tygwitruvz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tygwitruvz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tygwitruvz .gt_indent_1 { text-indent: 5px; }
 #tygwitruvz .gt_indent_2 { text-indent: calc(5px * 2); }
 #tygwitruvz .gt_indent_3 { text-indent: calc(5px * 3); }
 #tygwitruvz .gt_indent_4 { text-indent: calc(5px * 4); }
 #tygwitruvz .gt_indent_5 { text-indent: calc(5px * 5); }
 #tygwitruvz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tygwitruvz .gt_row_group_first td { border-top-width: 2px; }
 #tygwitruvz .gt_row_group_first th { border-top-width: 2px; }
 #tygwitruvz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tygwitruvz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tygwitruvz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tygwitruvz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tygwitruvz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tygwitruvz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tygwitruvz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tygwitruvz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tygwitruvz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tygwitruvz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tygwitruvz .gt_left { text-align: left; }
 #tygwitruvz .gt_center { text-align: center; }
 #tygwitruvz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tygwitruvz .gt_font_normal { font-weight: normal; }
 #tygwitruvz .gt_font_bold { font-weight: bold; }
 #tygwitruvz .gt_font_italic { font-style: italic; }
 #tygwitruvz .gt_super { font-size: 65%; }
 #tygwitruvz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tygwitruvz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tygwitruvz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tygwitruvz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tygwitruvz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tygwitruvz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#nxiywirmcs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nxiywirmcs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nxiywirmcs p { margin: 0; padding: 0; }
 #nxiywirmcs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nxiywirmcs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nxiywirmcs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nxiywirmcs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nxiywirmcs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nxiywirmcs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nxiywirmcs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nxiywirmcs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nxiywirmcs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nxiywirmcs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nxiywirmcs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nxiywirmcs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nxiywirmcs .gt_spanner_row { border-bottom-style: hidden; }
 #nxiywirmcs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nxiywirmcs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nxiywirmcs .gt_from_md> :first-child { margin-top: 0; }
 #nxiywirmcs .gt_from_md> :last-child { margin-bottom: 0; }
 #nxiywirmcs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nxiywirmcs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nxiywirmcs .gt_indent_1 { text-indent: 5px; }
 #nxiywirmcs .gt_indent_2 { text-indent: calc(5px * 2); }
 #nxiywirmcs .gt_indent_3 { text-indent: calc(5px * 3); }
 #nxiywirmcs .gt_indent_4 { text-indent: calc(5px * 4); }
 #nxiywirmcs .gt_indent_5 { text-indent: calc(5px * 5); }
 #nxiywirmcs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nxiywirmcs .gt_row_group_first td { border-top-width: 2px; }
 #nxiywirmcs .gt_row_group_first th { border-top-width: 2px; }
 #nxiywirmcs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nxiywirmcs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nxiywirmcs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nxiywirmcs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nxiywirmcs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nxiywirmcs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nxiywirmcs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nxiywirmcs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nxiywirmcs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nxiywirmcs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nxiywirmcs .gt_left { text-align: left; }
 #nxiywirmcs .gt_center { text-align: center; }
 #nxiywirmcs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nxiywirmcs .gt_font_normal { font-weight: normal; }
 #nxiywirmcs .gt_font_bold { font-weight: bold; }
 #nxiywirmcs .gt_font_italic { font-style: italic; }
 #nxiywirmcs .gt_super { font-size: 65%; }
 #nxiywirmcs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nxiywirmcs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nxiywirmcs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nxiywirmcs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nxiywirmcs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nxiywirmcs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#htsbssxczj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#htsbssxczj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#htsbssxczj p { margin: 0; padding: 0; }
 #htsbssxczj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #htsbssxczj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #htsbssxczj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #htsbssxczj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #htsbssxczj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #htsbssxczj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #htsbssxczj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #htsbssxczj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #htsbssxczj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #htsbssxczj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #htsbssxczj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #htsbssxczj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #htsbssxczj .gt_spanner_row { border-bottom-style: hidden; }
 #htsbssxczj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #htsbssxczj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #htsbssxczj .gt_from_md> :first-child { margin-top: 0; }
 #htsbssxczj .gt_from_md> :last-child { margin-bottom: 0; }
 #htsbssxczj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #htsbssxczj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #htsbssxczj .gt_indent_1 { text-indent: 5px; }
 #htsbssxczj .gt_indent_2 { text-indent: calc(5px * 2); }
 #htsbssxczj .gt_indent_3 { text-indent: calc(5px * 3); }
 #htsbssxczj .gt_indent_4 { text-indent: calc(5px * 4); }
 #htsbssxczj .gt_indent_5 { text-indent: calc(5px * 5); }
 #htsbssxczj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #htsbssxczj .gt_row_group_first td { border-top-width: 2px; }
 #htsbssxczj .gt_row_group_first th { border-top-width: 2px; }
 #htsbssxczj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #htsbssxczj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #htsbssxczj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #htsbssxczj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #htsbssxczj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #htsbssxczj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #htsbssxczj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #htsbssxczj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #htsbssxczj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #htsbssxczj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #htsbssxczj .gt_left { text-align: left; }
 #htsbssxczj .gt_center { text-align: center; }
 #htsbssxczj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #htsbssxczj .gt_font_normal { font-weight: normal; }
 #htsbssxczj .gt_font_bold { font-weight: bold; }
 #htsbssxczj .gt_font_italic { font-style: italic; }
 #htsbssxczj .gt_super { font-size: 65%; }
 #htsbssxczj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #htsbssxczj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #htsbssxczj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #htsbssxczj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #htsbssxczj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #htsbssxczj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dquglkkmlg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dquglkkmlg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dquglkkmlg p { margin: 0; padding: 0; }
 #dquglkkmlg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dquglkkmlg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dquglkkmlg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dquglkkmlg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dquglkkmlg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dquglkkmlg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dquglkkmlg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dquglkkmlg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dquglkkmlg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dquglkkmlg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dquglkkmlg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dquglkkmlg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dquglkkmlg .gt_spanner_row { border-bottom-style: hidden; }
 #dquglkkmlg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dquglkkmlg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dquglkkmlg .gt_from_md> :first-child { margin-top: 0; }
 #dquglkkmlg .gt_from_md> :last-child { margin-bottom: 0; }
 #dquglkkmlg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dquglkkmlg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dquglkkmlg .gt_indent_1 { text-indent: 5px; }
 #dquglkkmlg .gt_indent_2 { text-indent: calc(5px * 2); }
 #dquglkkmlg .gt_indent_3 { text-indent: calc(5px * 3); }
 #dquglkkmlg .gt_indent_4 { text-indent: calc(5px * 4); }
 #dquglkkmlg .gt_indent_5 { text-indent: calc(5px * 5); }
 #dquglkkmlg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dquglkkmlg .gt_row_group_first td { border-top-width: 2px; }
 #dquglkkmlg .gt_row_group_first th { border-top-width: 2px; }
 #dquglkkmlg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dquglkkmlg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dquglkkmlg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dquglkkmlg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dquglkkmlg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dquglkkmlg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dquglkkmlg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dquglkkmlg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dquglkkmlg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dquglkkmlg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dquglkkmlg .gt_left { text-align: left; }
 #dquglkkmlg .gt_center { text-align: center; }
 #dquglkkmlg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dquglkkmlg .gt_font_normal { font-weight: normal; }
 #dquglkkmlg .gt_font_bold { font-weight: bold; }
 #dquglkkmlg .gt_font_italic { font-style: italic; }
 #dquglkkmlg .gt_super { font-size: 65%; }
 #dquglkkmlg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dquglkkmlg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dquglkkmlg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dquglkkmlg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dquglkkmlg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dquglkkmlg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wyebefkgmm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wyebefkgmm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wyebefkgmm p { margin: 0; padding: 0; }
 #wyebefkgmm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wyebefkgmm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wyebefkgmm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wyebefkgmm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wyebefkgmm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wyebefkgmm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wyebefkgmm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wyebefkgmm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wyebefkgmm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wyebefkgmm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wyebefkgmm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wyebefkgmm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wyebefkgmm .gt_spanner_row { border-bottom-style: hidden; }
 #wyebefkgmm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wyebefkgmm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wyebefkgmm .gt_from_md> :first-child { margin-top: 0; }
 #wyebefkgmm .gt_from_md> :last-child { margin-bottom: 0; }
 #wyebefkgmm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wyebefkgmm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wyebefkgmm .gt_indent_1 { text-indent: 5px; }
 #wyebefkgmm .gt_indent_2 { text-indent: calc(5px * 2); }
 #wyebefkgmm .gt_indent_3 { text-indent: calc(5px * 3); }
 #wyebefkgmm .gt_indent_4 { text-indent: calc(5px * 4); }
 #wyebefkgmm .gt_indent_5 { text-indent: calc(5px * 5); }
 #wyebefkgmm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wyebefkgmm .gt_row_group_first td { border-top-width: 2px; }
 #wyebefkgmm .gt_row_group_first th { border-top-width: 2px; }
 #wyebefkgmm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wyebefkgmm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wyebefkgmm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wyebefkgmm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wyebefkgmm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wyebefkgmm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wyebefkgmm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wyebefkgmm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wyebefkgmm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wyebefkgmm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wyebefkgmm .gt_left { text-align: left; }
 #wyebefkgmm .gt_center { text-align: center; }
 #wyebefkgmm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wyebefkgmm .gt_font_normal { font-weight: normal; }
 #wyebefkgmm .gt_font_bold { font-weight: bold; }
 #wyebefkgmm .gt_font_italic { font-style: italic; }
 #wyebefkgmm .gt_super { font-size: 65%; }
 #wyebefkgmm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wyebefkgmm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wyebefkgmm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wyebefkgmm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wyebefkgmm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wyebefkgmm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#doxxvvdwgs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#doxxvvdwgs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#doxxvvdwgs p { margin: 0; padding: 0; }
 #doxxvvdwgs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #doxxvvdwgs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #doxxvvdwgs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #doxxvvdwgs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #doxxvvdwgs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #doxxvvdwgs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #doxxvvdwgs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #doxxvvdwgs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #doxxvvdwgs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #doxxvvdwgs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #doxxvvdwgs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #doxxvvdwgs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #doxxvvdwgs .gt_spanner_row { border-bottom-style: hidden; }
 #doxxvvdwgs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #doxxvvdwgs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #doxxvvdwgs .gt_from_md> :first-child { margin-top: 0; }
 #doxxvvdwgs .gt_from_md> :last-child { margin-bottom: 0; }
 #doxxvvdwgs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #doxxvvdwgs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #doxxvvdwgs .gt_indent_1 { text-indent: 5px; }
 #doxxvvdwgs .gt_indent_2 { text-indent: calc(5px * 2); }
 #doxxvvdwgs .gt_indent_3 { text-indent: calc(5px * 3); }
 #doxxvvdwgs .gt_indent_4 { text-indent: calc(5px * 4); }
 #doxxvvdwgs .gt_indent_5 { text-indent: calc(5px * 5); }
 #doxxvvdwgs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #doxxvvdwgs .gt_row_group_first td { border-top-width: 2px; }
 #doxxvvdwgs .gt_row_group_first th { border-top-width: 2px; }
 #doxxvvdwgs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #doxxvvdwgs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #doxxvvdwgs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #doxxvvdwgs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #doxxvvdwgs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #doxxvvdwgs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #doxxvvdwgs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #doxxvvdwgs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #doxxvvdwgs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #doxxvvdwgs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #doxxvvdwgs .gt_left { text-align: left; }
 #doxxvvdwgs .gt_center { text-align: center; }
 #doxxvvdwgs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #doxxvvdwgs .gt_font_normal { font-weight: normal; }
 #doxxvvdwgs .gt_font_bold { font-weight: bold; }
 #doxxvvdwgs .gt_font_italic { font-style: italic; }
 #doxxvvdwgs .gt_super { font-size: 65%; }
 #doxxvvdwgs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #doxxvvdwgs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #doxxvvdwgs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #doxxvvdwgs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #doxxvvdwgs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #doxxvvdwgs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#kevfrbdspa table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kevfrbdspa thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kevfrbdspa p { margin: 0; padding: 0; }
 #kevfrbdspa .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kevfrbdspa .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kevfrbdspa .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kevfrbdspa .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kevfrbdspa .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kevfrbdspa .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kevfrbdspa .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kevfrbdspa .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kevfrbdspa .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kevfrbdspa .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kevfrbdspa .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kevfrbdspa .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kevfrbdspa .gt_spanner_row { border-bottom-style: hidden; }
 #kevfrbdspa .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kevfrbdspa .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kevfrbdspa .gt_from_md> :first-child { margin-top: 0; }
 #kevfrbdspa .gt_from_md> :last-child { margin-bottom: 0; }
 #kevfrbdspa .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kevfrbdspa .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kevfrbdspa .gt_indent_1 { text-indent: 5px; }
 #kevfrbdspa .gt_indent_2 { text-indent: calc(5px * 2); }
 #kevfrbdspa .gt_indent_3 { text-indent: calc(5px * 3); }
 #kevfrbdspa .gt_indent_4 { text-indent: calc(5px * 4); }
 #kevfrbdspa .gt_indent_5 { text-indent: calc(5px * 5); }
 #kevfrbdspa .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kevfrbdspa .gt_row_group_first td { border-top-width: 2px; }
 #kevfrbdspa .gt_row_group_first th { border-top-width: 2px; }
 #kevfrbdspa .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kevfrbdspa .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kevfrbdspa .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kevfrbdspa .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kevfrbdspa .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kevfrbdspa .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kevfrbdspa .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kevfrbdspa .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kevfrbdspa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kevfrbdspa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kevfrbdspa .gt_left { text-align: left; }
 #kevfrbdspa .gt_center { text-align: center; }
 #kevfrbdspa .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kevfrbdspa .gt_font_normal { font-weight: normal; }
 #kevfrbdspa .gt_font_bold { font-weight: bold; }
 #kevfrbdspa .gt_font_italic { font-style: italic; }
 #kevfrbdspa .gt_super { font-size: 65%; }
 #kevfrbdspa .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kevfrbdspa .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kevfrbdspa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kevfrbdspa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kevfrbdspa .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kevfrbdspa .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#picxyxvbsl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#picxyxvbsl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#picxyxvbsl p { margin: 0; padding: 0; }
 #picxyxvbsl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #picxyxvbsl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #picxyxvbsl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #picxyxvbsl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #picxyxvbsl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #picxyxvbsl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #picxyxvbsl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #picxyxvbsl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #picxyxvbsl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #picxyxvbsl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #picxyxvbsl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #picxyxvbsl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #picxyxvbsl .gt_spanner_row { border-bottom-style: hidden; }
 #picxyxvbsl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #picxyxvbsl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #picxyxvbsl .gt_from_md> :first-child { margin-top: 0; }
 #picxyxvbsl .gt_from_md> :last-child { margin-bottom: 0; }
 #picxyxvbsl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #picxyxvbsl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #picxyxvbsl .gt_indent_1 { text-indent: 5px; }
 #picxyxvbsl .gt_indent_2 { text-indent: calc(5px * 2); }
 #picxyxvbsl .gt_indent_3 { text-indent: calc(5px * 3); }
 #picxyxvbsl .gt_indent_4 { text-indent: calc(5px * 4); }
 #picxyxvbsl .gt_indent_5 { text-indent: calc(5px * 5); }
 #picxyxvbsl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #picxyxvbsl .gt_row_group_first td { border-top-width: 2px; }
 #picxyxvbsl .gt_row_group_first th { border-top-width: 2px; }
 #picxyxvbsl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #picxyxvbsl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #picxyxvbsl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #picxyxvbsl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #picxyxvbsl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #picxyxvbsl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #picxyxvbsl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #picxyxvbsl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #picxyxvbsl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #picxyxvbsl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #picxyxvbsl .gt_left { text-align: left; }
 #picxyxvbsl .gt_center { text-align: center; }
 #picxyxvbsl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #picxyxvbsl .gt_font_normal { font-weight: normal; }
 #picxyxvbsl .gt_font_bold { font-weight: bold; }
 #picxyxvbsl .gt_font_italic { font-style: italic; }
 #picxyxvbsl .gt_super { font-size: 65%; }
 #picxyxvbsl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #picxyxvbsl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #picxyxvbsl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #picxyxvbsl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #picxyxvbsl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #picxyxvbsl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ghugnnlraf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ghugnnlraf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ghugnnlraf p { margin: 0; padding: 0; }
 #ghugnnlraf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ghugnnlraf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ghugnnlraf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ghugnnlraf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ghugnnlraf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ghugnnlraf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ghugnnlraf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ghugnnlraf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ghugnnlraf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ghugnnlraf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ghugnnlraf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ghugnnlraf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ghugnnlraf .gt_spanner_row { border-bottom-style: hidden; }
 #ghugnnlraf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ghugnnlraf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ghugnnlraf .gt_from_md> :first-child { margin-top: 0; }
 #ghugnnlraf .gt_from_md> :last-child { margin-bottom: 0; }
 #ghugnnlraf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ghugnnlraf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ghugnnlraf .gt_indent_1 { text-indent: 5px; }
 #ghugnnlraf .gt_indent_2 { text-indent: calc(5px * 2); }
 #ghugnnlraf .gt_indent_3 { text-indent: calc(5px * 3); }
 #ghugnnlraf .gt_indent_4 { text-indent: calc(5px * 4); }
 #ghugnnlraf .gt_indent_5 { text-indent: calc(5px * 5); }
 #ghugnnlraf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ghugnnlraf .gt_row_group_first td { border-top-width: 2px; }
 #ghugnnlraf .gt_row_group_first th { border-top-width: 2px; }
 #ghugnnlraf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ghugnnlraf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ghugnnlraf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ghugnnlraf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ghugnnlraf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ghugnnlraf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ghugnnlraf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ghugnnlraf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ghugnnlraf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ghugnnlraf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ghugnnlraf .gt_left { text-align: left; }
 #ghugnnlraf .gt_center { text-align: center; }
 #ghugnnlraf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ghugnnlraf .gt_font_normal { font-weight: normal; }
 #ghugnnlraf .gt_font_bold { font-weight: bold; }
 #ghugnnlraf .gt_font_italic { font-style: italic; }
 #ghugnnlraf .gt_super { font-size: 65%; }
 #ghugnnlraf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ghugnnlraf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ghugnnlraf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ghugnnlraf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ghugnnlraf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ghugnnlraf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dulbbhrinp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dulbbhrinp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dulbbhrinp p { margin: 0; padding: 0; }
 #dulbbhrinp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dulbbhrinp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dulbbhrinp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dulbbhrinp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dulbbhrinp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dulbbhrinp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dulbbhrinp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dulbbhrinp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dulbbhrinp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dulbbhrinp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dulbbhrinp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dulbbhrinp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dulbbhrinp .gt_spanner_row { border-bottom-style: hidden; }
 #dulbbhrinp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dulbbhrinp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dulbbhrinp .gt_from_md> :first-child { margin-top: 0; }
 #dulbbhrinp .gt_from_md> :last-child { margin-bottom: 0; }
 #dulbbhrinp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dulbbhrinp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dulbbhrinp .gt_indent_1 { text-indent: 5px; }
 #dulbbhrinp .gt_indent_2 { text-indent: calc(5px * 2); }
 #dulbbhrinp .gt_indent_3 { text-indent: calc(5px * 3); }
 #dulbbhrinp .gt_indent_4 { text-indent: calc(5px * 4); }
 #dulbbhrinp .gt_indent_5 { text-indent: calc(5px * 5); }
 #dulbbhrinp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dulbbhrinp .gt_row_group_first td { border-top-width: 2px; }
 #dulbbhrinp .gt_row_group_first th { border-top-width: 2px; }
 #dulbbhrinp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dulbbhrinp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dulbbhrinp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dulbbhrinp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dulbbhrinp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dulbbhrinp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dulbbhrinp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dulbbhrinp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dulbbhrinp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dulbbhrinp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dulbbhrinp .gt_left { text-align: left; }
 #dulbbhrinp .gt_center { text-align: center; }
 #dulbbhrinp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dulbbhrinp .gt_font_normal { font-weight: normal; }
 #dulbbhrinp .gt_font_bold { font-weight: bold; }
 #dulbbhrinp .gt_font_italic { font-style: italic; }
 #dulbbhrinp .gt_super { font-size: 65%; }
 #dulbbhrinp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dulbbhrinp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dulbbhrinp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dulbbhrinp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dulbbhrinp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dulbbhrinp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hyexvgisph table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hyexvgisph thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hyexvgisph p { margin: 0; padding: 0; }
 #hyexvgisph .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hyexvgisph .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hyexvgisph .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hyexvgisph .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hyexvgisph .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hyexvgisph .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hyexvgisph .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hyexvgisph .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hyexvgisph .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hyexvgisph .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hyexvgisph .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hyexvgisph .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hyexvgisph .gt_spanner_row { border-bottom-style: hidden; }
 #hyexvgisph .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hyexvgisph .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hyexvgisph .gt_from_md> :first-child { margin-top: 0; }
 #hyexvgisph .gt_from_md> :last-child { margin-bottom: 0; }
 #hyexvgisph .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hyexvgisph .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hyexvgisph .gt_indent_1 { text-indent: 5px; }
 #hyexvgisph .gt_indent_2 { text-indent: calc(5px * 2); }
 #hyexvgisph .gt_indent_3 { text-indent: calc(5px * 3); }
 #hyexvgisph .gt_indent_4 { text-indent: calc(5px * 4); }
 #hyexvgisph .gt_indent_5 { text-indent: calc(5px * 5); }
 #hyexvgisph .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hyexvgisph .gt_row_group_first td { border-top-width: 2px; }
 #hyexvgisph .gt_row_group_first th { border-top-width: 2px; }
 #hyexvgisph .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hyexvgisph .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hyexvgisph .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hyexvgisph .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hyexvgisph .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hyexvgisph .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hyexvgisph .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hyexvgisph .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hyexvgisph .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hyexvgisph .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hyexvgisph .gt_left { text-align: left; }
 #hyexvgisph .gt_center { text-align: center; }
 #hyexvgisph .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hyexvgisph .gt_font_normal { font-weight: normal; }
 #hyexvgisph .gt_font_bold { font-weight: bold; }
 #hyexvgisph .gt_font_italic { font-style: italic; }
 #hyexvgisph .gt_super { font-size: 65%; }
 #hyexvgisph .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hyexvgisph .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hyexvgisph .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hyexvgisph .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hyexvgisph .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hyexvgisph .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#osewxuramv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#osewxuramv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#osewxuramv p { margin: 0; padding: 0; }
 #osewxuramv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #osewxuramv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #osewxuramv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #osewxuramv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #osewxuramv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #osewxuramv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #osewxuramv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #osewxuramv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #osewxuramv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #osewxuramv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #osewxuramv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #osewxuramv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #osewxuramv .gt_spanner_row { border-bottom-style: hidden; }
 #osewxuramv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #osewxuramv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #osewxuramv .gt_from_md> :first-child { margin-top: 0; }
 #osewxuramv .gt_from_md> :last-child { margin-bottom: 0; }
 #osewxuramv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #osewxuramv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #osewxuramv .gt_indent_1 { text-indent: 5px; }
 #osewxuramv .gt_indent_2 { text-indent: calc(5px * 2); }
 #osewxuramv .gt_indent_3 { text-indent: calc(5px * 3); }
 #osewxuramv .gt_indent_4 { text-indent: calc(5px * 4); }
 #osewxuramv .gt_indent_5 { text-indent: calc(5px * 5); }
 #osewxuramv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #osewxuramv .gt_row_group_first td { border-top-width: 2px; }
 #osewxuramv .gt_row_group_first th { border-top-width: 2px; }
 #osewxuramv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #osewxuramv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #osewxuramv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #osewxuramv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #osewxuramv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #osewxuramv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #osewxuramv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #osewxuramv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #osewxuramv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #osewxuramv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #osewxuramv .gt_left { text-align: left; }
 #osewxuramv .gt_center { text-align: center; }
 #osewxuramv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #osewxuramv .gt_font_normal { font-weight: normal; }
 #osewxuramv .gt_font_bold { font-weight: bold; }
 #osewxuramv .gt_font_italic { font-style: italic; }
 #osewxuramv .gt_super { font-size: 65%; }
 #osewxuramv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #osewxuramv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #osewxuramv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #osewxuramv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #osewxuramv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #osewxuramv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#comhpvhiwa table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#comhpvhiwa thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#comhpvhiwa p { margin: 0; padding: 0; }
 #comhpvhiwa .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #comhpvhiwa .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #comhpvhiwa .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #comhpvhiwa .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #comhpvhiwa .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #comhpvhiwa .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #comhpvhiwa .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #comhpvhiwa .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #comhpvhiwa .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #comhpvhiwa .gt_column_spanner_outer:first-child { padding-left: 0; }
 #comhpvhiwa .gt_column_spanner_outer:last-child { padding-right: 0; }
 #comhpvhiwa .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #comhpvhiwa .gt_spanner_row { border-bottom-style: hidden; }
 #comhpvhiwa .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #comhpvhiwa .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #comhpvhiwa .gt_from_md> :first-child { margin-top: 0; }
 #comhpvhiwa .gt_from_md> :last-child { margin-bottom: 0; }
 #comhpvhiwa .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #comhpvhiwa .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #comhpvhiwa .gt_indent_1 { text-indent: 5px; }
 #comhpvhiwa .gt_indent_2 { text-indent: calc(5px * 2); }
 #comhpvhiwa .gt_indent_3 { text-indent: calc(5px * 3); }
 #comhpvhiwa .gt_indent_4 { text-indent: calc(5px * 4); }
 #comhpvhiwa .gt_indent_5 { text-indent: calc(5px * 5); }
 #comhpvhiwa .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #comhpvhiwa .gt_row_group_first td { border-top-width: 2px; }
 #comhpvhiwa .gt_row_group_first th { border-top-width: 2px; }
 #comhpvhiwa .gt_striped { color: #333333; background-color: #F4F4F4; }
 #comhpvhiwa .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #comhpvhiwa .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #comhpvhiwa .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #comhpvhiwa .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #comhpvhiwa .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #comhpvhiwa .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #comhpvhiwa .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #comhpvhiwa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #comhpvhiwa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #comhpvhiwa .gt_left { text-align: left; }
 #comhpvhiwa .gt_center { text-align: center; }
 #comhpvhiwa .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #comhpvhiwa .gt_font_normal { font-weight: normal; }
 #comhpvhiwa .gt_font_bold { font-weight: bold; }
 #comhpvhiwa .gt_font_italic { font-style: italic; }
 #comhpvhiwa .gt_super { font-size: 65%; }
 #comhpvhiwa .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #comhpvhiwa .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #comhpvhiwa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #comhpvhiwa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #comhpvhiwa .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #comhpvhiwa .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fwptnphylr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fwptnphylr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fwptnphylr p { margin: 0; padding: 0; }
 #fwptnphylr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fwptnphylr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fwptnphylr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fwptnphylr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fwptnphylr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fwptnphylr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fwptnphylr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fwptnphylr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fwptnphylr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fwptnphylr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fwptnphylr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fwptnphylr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fwptnphylr .gt_spanner_row { border-bottom-style: hidden; }
 #fwptnphylr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fwptnphylr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fwptnphylr .gt_from_md> :first-child { margin-top: 0; }
 #fwptnphylr .gt_from_md> :last-child { margin-bottom: 0; }
 #fwptnphylr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fwptnphylr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fwptnphylr .gt_indent_1 { text-indent: 5px; }
 #fwptnphylr .gt_indent_2 { text-indent: calc(5px * 2); }
 #fwptnphylr .gt_indent_3 { text-indent: calc(5px * 3); }
 #fwptnphylr .gt_indent_4 { text-indent: calc(5px * 4); }
 #fwptnphylr .gt_indent_5 { text-indent: calc(5px * 5); }
 #fwptnphylr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fwptnphylr .gt_row_group_first td { border-top-width: 2px; }
 #fwptnphylr .gt_row_group_first th { border-top-width: 2px; }
 #fwptnphylr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fwptnphylr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fwptnphylr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fwptnphylr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fwptnphylr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fwptnphylr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fwptnphylr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fwptnphylr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fwptnphylr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fwptnphylr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fwptnphylr .gt_left { text-align: left; }
 #fwptnphylr .gt_center { text-align: center; }
 #fwptnphylr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fwptnphylr .gt_font_normal { font-weight: normal; }
 #fwptnphylr .gt_font_bold { font-weight: bold; }
 #fwptnphylr .gt_font_italic { font-style: italic; }
 #fwptnphylr .gt_super { font-size: 65%; }
 #fwptnphylr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fwptnphylr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fwptnphylr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fwptnphylr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fwptnphylr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fwptnphylr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#sxuzatqocz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sxuzatqocz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sxuzatqocz p { margin: 0; padding: 0; }
 #sxuzatqocz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sxuzatqocz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sxuzatqocz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sxuzatqocz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sxuzatqocz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sxuzatqocz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sxuzatqocz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sxuzatqocz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sxuzatqocz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sxuzatqocz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sxuzatqocz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sxuzatqocz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sxuzatqocz .gt_spanner_row { border-bottom-style: hidden; }
 #sxuzatqocz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sxuzatqocz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sxuzatqocz .gt_from_md> :first-child { margin-top: 0; }
 #sxuzatqocz .gt_from_md> :last-child { margin-bottom: 0; }
 #sxuzatqocz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sxuzatqocz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sxuzatqocz .gt_indent_1 { text-indent: 5px; }
 #sxuzatqocz .gt_indent_2 { text-indent: calc(5px * 2); }
 #sxuzatqocz .gt_indent_3 { text-indent: calc(5px * 3); }
 #sxuzatqocz .gt_indent_4 { text-indent: calc(5px * 4); }
 #sxuzatqocz .gt_indent_5 { text-indent: calc(5px * 5); }
 #sxuzatqocz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sxuzatqocz .gt_row_group_first td { border-top-width: 2px; }
 #sxuzatqocz .gt_row_group_first th { border-top-width: 2px; }
 #sxuzatqocz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sxuzatqocz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sxuzatqocz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sxuzatqocz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sxuzatqocz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sxuzatqocz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sxuzatqocz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sxuzatqocz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sxuzatqocz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sxuzatqocz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sxuzatqocz .gt_left { text-align: left; }
 #sxuzatqocz .gt_center { text-align: center; }
 #sxuzatqocz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sxuzatqocz .gt_font_normal { font-weight: normal; }
 #sxuzatqocz .gt_font_bold { font-weight: bold; }
 #sxuzatqocz .gt_font_italic { font-style: italic; }
 #sxuzatqocz .gt_super { font-size: 65%; }
 #sxuzatqocz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sxuzatqocz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sxuzatqocz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sxuzatqocz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sxuzatqocz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sxuzatqocz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vyepkktjjg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vyepkktjjg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vyepkktjjg p { margin: 0; padding: 0; }
 #vyepkktjjg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vyepkktjjg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vyepkktjjg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vyepkktjjg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vyepkktjjg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vyepkktjjg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vyepkktjjg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vyepkktjjg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vyepkktjjg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vyepkktjjg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vyepkktjjg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vyepkktjjg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vyepkktjjg .gt_spanner_row { border-bottom-style: hidden; }
 #vyepkktjjg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vyepkktjjg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vyepkktjjg .gt_from_md> :first-child { margin-top: 0; }
 #vyepkktjjg .gt_from_md> :last-child { margin-bottom: 0; }
 #vyepkktjjg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vyepkktjjg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vyepkktjjg .gt_indent_1 { text-indent: 5px; }
 #vyepkktjjg .gt_indent_2 { text-indent: calc(5px * 2); }
 #vyepkktjjg .gt_indent_3 { text-indent: calc(5px * 3); }
 #vyepkktjjg .gt_indent_4 { text-indent: calc(5px * 4); }
 #vyepkktjjg .gt_indent_5 { text-indent: calc(5px * 5); }
 #vyepkktjjg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vyepkktjjg .gt_row_group_first td { border-top-width: 2px; }
 #vyepkktjjg .gt_row_group_first th { border-top-width: 2px; }
 #vyepkktjjg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vyepkktjjg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vyepkktjjg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vyepkktjjg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vyepkktjjg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vyepkktjjg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vyepkktjjg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vyepkktjjg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vyepkktjjg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vyepkktjjg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vyepkktjjg .gt_left { text-align: left; }
 #vyepkktjjg .gt_center { text-align: center; }
 #vyepkktjjg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vyepkktjjg .gt_font_normal { font-weight: normal; }
 #vyepkktjjg .gt_font_bold { font-weight: bold; }
 #vyepkktjjg .gt_font_italic { font-style: italic; }
 #vyepkktjjg .gt_super { font-size: 65%; }
 #vyepkktjjg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vyepkktjjg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vyepkktjjg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vyepkktjjg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vyepkktjjg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vyepkktjjg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#erswerfbaq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#erswerfbaq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#erswerfbaq p { margin: 0; padding: 0; }
 #erswerfbaq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #erswerfbaq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #erswerfbaq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #erswerfbaq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #erswerfbaq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #erswerfbaq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #erswerfbaq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #erswerfbaq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #erswerfbaq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #erswerfbaq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #erswerfbaq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #erswerfbaq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #erswerfbaq .gt_spanner_row { border-bottom-style: hidden; }
 #erswerfbaq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #erswerfbaq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #erswerfbaq .gt_from_md> :first-child { margin-top: 0; }
 #erswerfbaq .gt_from_md> :last-child { margin-bottom: 0; }
 #erswerfbaq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #erswerfbaq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #erswerfbaq .gt_indent_1 { text-indent: 5px; }
 #erswerfbaq .gt_indent_2 { text-indent: calc(5px * 2); }
 #erswerfbaq .gt_indent_3 { text-indent: calc(5px * 3); }
 #erswerfbaq .gt_indent_4 { text-indent: calc(5px * 4); }
 #erswerfbaq .gt_indent_5 { text-indent: calc(5px * 5); }
 #erswerfbaq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #erswerfbaq .gt_row_group_first td { border-top-width: 2px; }
 #erswerfbaq .gt_row_group_first th { border-top-width: 2px; }
 #erswerfbaq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #erswerfbaq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #erswerfbaq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #erswerfbaq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #erswerfbaq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #erswerfbaq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #erswerfbaq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #erswerfbaq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #erswerfbaq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #erswerfbaq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #erswerfbaq .gt_left { text-align: left; }
 #erswerfbaq .gt_center { text-align: center; }
 #erswerfbaq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #erswerfbaq .gt_font_normal { font-weight: normal; }
 #erswerfbaq .gt_font_bold { font-weight: bold; }
 #erswerfbaq .gt_font_italic { font-style: italic; }
 #erswerfbaq .gt_super { font-size: 65%; }
 #erswerfbaq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #erswerfbaq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #erswerfbaq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #erswerfbaq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #erswerfbaq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #erswerfbaq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
