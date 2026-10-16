# GT.fmt_flag()


Generate flag icons for countries from their country codes.


Usage

``` python
GT.fmt_flag(
    columns=None,
    rows=None,
    height="1em",
    sep=" ",
    use_title=True,
)
```


While it is fairly straightforward to insert images into body cells (using <a href="../reference/GT.fmt_image.html#great_tables.GT.fmt_image" class="gdls-link"><code>fmt_image()</code></a> is one way to it), there is often the need to incorporate specialized types of graphics within a table. One such group of graphics involves iconography representing different countries, and the [fmt_flag()](GT.fmt_flag.md#great_tables.GT.fmt_flag) method helps with inserting a flag icon (or multiple) in body cells. To make this work seamlessly, the input cells need to contain some reference to a country, and this can be in the form of a 2- or 3-letter ISO 3166-1 country code (e.g., Egypt has the `"EG"` country code). This method will parse the targeted body cells for those codes and insert the appropriate flag graphics.

Multiple flags can be included per cell by separating country codes with commas (e.g., `"GB,TT"`). The `sep=` argument allows for a common separator to be applied between flag icons.

Any code that isn't recognized as a 2- or 3-letter country code is left as is (i.e., the text is retained in place of a flag icon). This means that a column with a mix of valid and invalid codes can still be formatted, and the cells without flags can be identified and styled separately (e.g., with [tab_style()](GT.tab_style.md#great_tables.GT.tab_style)).


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`height: str | float | None = ``"1em"`  
The height of the flag icons. The default value is `"1em"`. If given as a number, it is assumed to be in pixels.

`sep: str = ``" "`  
In the output of multiple flag icons within a body cell, `sep=` provides the separator between each of the flag icons.

`use_title: bool = ``True`  
The option to include a title attribute with the country name when hovering over the flag icon. The default is `True`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use the [countrypops](data.countrypops.md#great_tables.data.countrypops) dataset to create a new table with flag icons. We will only include a few columns and rows from that table. The `country_code_2` column has 2-letter country codes in the format required for [fmt_flag()](GT.fmt_flag.md#great_tables.GT.fmt_flag) and using that method transforms the codes to circular flag icons.


``` python
from great_tables import GT
from great_tables.data import countrypops
import polars as pl

countrypops_mini = (
    pl.from_pandas(countrypops)
    .filter(pl.col("year") == 2021)
    .filter(pl.col("country_name").str.starts_with("S"))
    .sort("country_name")
    .head(10)
    .drop(["year", "country_code_3"])
)

(
    GT(countrypops_mini)
    .fmt_integer(columns="population")
    .fmt_flag(columns="country_code_2")
    .cols_label(
        country_code_2="",
        country_name="Country",
        population="Population (2021)"
    )
    .cols_move_to_start(columns="country_code_2")
)
```


<style>
#wyasyetzrj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wyasyetzrj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wyasyetzrj p { margin: 0; padding: 0; }
 #wyasyetzrj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wyasyetzrj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wyasyetzrj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wyasyetzrj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wyasyetzrj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wyasyetzrj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wyasyetzrj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wyasyetzrj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wyasyetzrj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wyasyetzrj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wyasyetzrj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wyasyetzrj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wyasyetzrj .gt_spanner_row { border-bottom-style: hidden; }
 #wyasyetzrj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wyasyetzrj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wyasyetzrj .gt_from_md> :first-child { margin-top: 0; }
 #wyasyetzrj .gt_from_md> :last-child { margin-bottom: 0; }
 #wyasyetzrj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wyasyetzrj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wyasyetzrj .gt_indent_1 { text-indent: 5px; }
 #wyasyetzrj .gt_indent_2 { text-indent: calc(5px * 2); }
 #wyasyetzrj .gt_indent_3 { text-indent: calc(5px * 3); }
 #wyasyetzrj .gt_indent_4 { text-indent: calc(5px * 4); }
 #wyasyetzrj .gt_indent_5 { text-indent: calc(5px * 5); }
 #wyasyetzrj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wyasyetzrj .gt_row_group_first td { border-top-width: 2px; }
 #wyasyetzrj .gt_row_group_first th { border-top-width: 2px; }
 #wyasyetzrj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wyasyetzrj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wyasyetzrj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wyasyetzrj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wyasyetzrj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wyasyetzrj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wyasyetzrj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wyasyetzrj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wyasyetzrj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wyasyetzrj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wyasyetzrj .gt_left { text-align: left; }
 #wyasyetzrj .gt_center { text-align: center; }
 #wyasyetzrj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wyasyetzrj .gt_font_normal { font-weight: normal; }
 #wyasyetzrj .gt_font_bold { font-weight: bold; }
 #wyasyetzrj .gt_font_italic { font-style: italic; }
 #wyasyetzrj .gt_super { font-size: 65%; }
 #wyasyetzrj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wyasyetzrj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wyasyetzrj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wyasyetzrj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wyasyetzrj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wyasyetzrj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|  | Country | Population (2021) |
|----|----|----|
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iU2Ftb2EiIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+U2Ftb2E8L3RpdGxlPjxtYXNrIGlkPSJjb3VudHJ5X2NvZGVfMi0wLWEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNjb3VudHJ5X2NvZGVfMi0wLWEpIj48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMCAyNTYgMjU2IDBoMjU2djUxMkgweiIgLz48cGF0aCBmaWxsPSIjMDA1MmI0IiBkPSJNMCAwaDI1NnYyNTZIMHoiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0ibTIwNSAxNjcgNC4yIDEyLjdoMTMuNGwtMTAuOCA3LjkgNC4xIDEyLjctMTAuOC03LjgtMTAuOSA3LjggNC4xLTEyLjctMTAuOC03LjloMTMuNHpNMTM3LjggNjYuOGw3IDIxLjJIMTY3bC0xOC4xIDEzLjIgNi45IDIxLjItMTguMS0xMy4xLTE4IDEzLjEgNi44LTIxLjItMTgtMTMuMmgyMi4zek0yMDQuNSA4OWw2LjkgMjEuM2gyMi4zbC0xOCAxMy4xIDYuOSAyMS4zLTE4LjEtMTMuMS0xOC4xIDEzLjEgNy0yMS4zLTE4LjItMTMuMWgyMi40em0tNTIuOCA4OSA2LjkgMjEuM0gxODFsLTE4LjEgMTMuMiA2LjkgMjEuMi0xOC4xLTEzLjEtMTggMTMuMSA2LjgtMjEuMi0xOC0xMy4yaDIyLjN6bS01OC41LTU1LjYgNi45IDIxLjNoMjIuM2wtMTggMTMuMSA2LjkgMjEuMy0xOC4xLTEzLjJMNzUgMTc4LjFsNi45LTIxLjMtMTgtMTMuMWgyMi4zeiIgLz48L2c+PC9zdmc+)</span> | Samoa | 218,764 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iU2FuIE1hcmlubyIgd2lkdGg9IjUxMiIgaGVpZ2h0PSI1MTIiIHZpZXdib3g9IjAgMCA1MTIgNTEyIiBzdHlsZT0idmVydGljYWwtYWxpZ246LTAuMTI1ZW07aW1hZ2UtcmVuZGVyaW5nOm9wdGltaXplUXVhbGl0eTtoZWlnaHQ6MWVtO3dpZHRoOjFlbTsiPjx0aXRsZT5TYW4gTWFyaW5vPC90aXRsZT48bWFzayBpZD0iY291bnRyeV9jb2RlXzItMS1hIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjY291bnRyeV9jb2RlXzItMS1hKSI+PHBhdGggZmlsbD0iIzMzOGFmMyIgZD0ibTAgMjU2IDI1Ni01Mi4zTDUxMiAyNTZ2MjU2SDB6IiAvPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0wIDBoNTEydjI1NkgweiIgLz48cGF0aCBmaWxsPSIjNmRhNTQ0IiBkPSJNMzU3LjYgMTc2LjYgMjU2IDI3OC4zIDE1NC40IDE3Ni42YTEyMS43IDEyMS43IDAgMCAwLTIwLjggNjguM3YzMy40YzAgNTMuNiAzNC42IDk5LjIgODIuNyAxMTUuOGEzNyAzNyAwIDAgMCA0IDQwbDM2LjQtMjkuMiAzNi40IDI5LjJhMzcgMzcgMCAwIDAgMy45LTQwLjUgMTIyLjYgMTIyLjYgMCAwIDAgODEuNC0xMTUuM3YtMzMuNGMwLTI1LjMtNy42LTQ4LjctMjAuOC02OC4zeiIgLz48cGF0aCBmaWxsPSIjZmZkYTQ0IiBkPSJNMjU2IDM2Ny4zYy00OS4xIDAtODktNDAtODktODl2LTMzLjRhODkuMSA4OS4xIDAgMCAxIDE3OCAwdjMzLjRjMCA0OS0zOS45IDg5LTg5IDg5eiIgLz48cGF0aCBmaWxsPSIjMzM4YWYzIiBkPSJNMzExLjcgMjc4LjN2LTMzLjRhNTUuNyA1NS43IDAgMCAwLTExMS40IDB2MzMuNGw1NS43IDExeiIgLz48cGF0aCBmaWxsPSIjNmRhNTQ0IiBkPSJNMjAwLjMgMjc4LjNhNTUuNyA1NS43IDAgMCAwIDExMS40IDB6IiAvPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Ik0zMjIuOCAxNTUuOEEzMy40IDMzLjQgMCAwIDAgMjY3IDEzMXYtMTkuNmgxMS4yVjg5SDI2N1Y3OGgtMjJ2MTFoLTExLjJ2MjIuM0gyNDV2MTkuNmEzMy40IDMzLjQgMCAwIDAtNDQuNSA0OS44djE5LjZoMTExLjN2LTE5LjZjNi44LTYuMSAxMS0xNSAxMS0yNC45eiIgLz48L2c+PC9zdmc+)</span> | San Marino | 33,745 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iU2FvIFRvbWUgYW5kIFByaW5jaXBlIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgdmlld2JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJ2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtpbWFnZS1yZW5kZXJpbmc6b3B0aW1pemVRdWFsaXR5O2hlaWdodDoxZW07d2lkdGg6MWVtOyI+PHRpdGxlPlNhbyBUb21lIGFuZCBQcmluY2lwZTwvdGl0bGU+PG1hc2sgaWQ9ImNvdW50cnlfY29kZV8yLTItYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2NvdW50cnlfY29kZV8yLTItYSkiPjxwYXRoIGZpbGw9IiM2ZGE1NDQiIGQ9Ik0wIDBoNTEydjE2N2wtNTIuNiA4My44TDUxMiAzNDV2MTY3SDBsNzItMjY0LjN6IiAvPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Ik0xMTQuOSAxNjYuOUg1MTJ2MTc4SDExNC45eiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMCAwdjUxMmwyNTYtMjU2eiIgLz48cGF0aCBmaWxsPSIjMzMzIiBkPSJtMzI1IDIxMS41IDExLjEgMzRIMzcybC0yOSAyMSAxMS4xIDM0LTI5LTIxLTI4LjkgMjEgMTEtMzQtMjguOC0yMUgzMTR6bTExMS40IDAgMTEgMzRoMzUuOGwtMjkgMjEgMTEuMSAzNC0yOS0yMS0yOC45IDIxIDExLjEtMzQtMjktMjFoMzUuOHoiIC8+PC9nPjwvc3ZnPg==)</span> | Sao Tome and Principe | 223,107 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iU2F1ZGkgQXJhYmlhIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgdmlld2JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJ2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtpbWFnZS1yZW5kZXJpbmc6b3B0aW1pemVRdWFsaXR5O2hlaWdodDoxZW07d2lkdGg6MWVtOyI+PHRpdGxlPlNhdWRpIEFyYWJpYTwvdGl0bGU+PG1hc2sgaWQ9ImNvdW50cnlfY29kZV8yLTMtYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2NvdW50cnlfY29kZV8yLTMtYSkiPjxwYXRoIGZpbGw9IiM0OTZlMmQiIGQ9Ik0wIDBoNTEydjUxMkgweiIgLz48ZyBmaWxsPSIjZWVlIj48cGF0aCBkPSJNMTQ0LjcgMzA2YzAgMTguNSAxNSAzMy41IDMzLjQgMzMuNWgxMDAuMmEyNy44IDI3LjggMCAwIDAgMjcuOCAyNy44aDMzLjRhMjcuOCAyNy44IDAgMCAwIDI3LjgtMjcuOFYzMDZ6bTIyNS40LTE2MS4zdjc4YzAgMTIuMi0xMCAyMi4yLTIyLjMgMjIuMnYzMy40YzMwLjcgMCA1NS43LTI1IDU1LjctNTUuN3YtNzcuOUgzNzB6bS0yMzkuMyA3OGMwIDEyLjItMTAgMjIuMi0yMi4zIDIyLjJ2MzMuNGMzMC43IDAgNTUuNy0yNSA1NS43LTU1Ljd2LTc3LjloLTMzLjR6IiAvPjxwYXRoIGQ9Ik0zMjAgMTQ0LjdoMzMuNHY3OEgzMjB6bS01MCA0NC41YTUuNiA1LjYgMCAwIDEtMTEuMiAwdi00NC41aC0zMy40djQ0LjVhNS42IDUuNiAwIDAgMS0xMS4xIDB2LTQ0LjVoLTMzLjR2NDQuNWEzOSAzOSAwIDAgMCAzOSAzOSAzOC43IDM4LjcgMCAwIDAgMjIuMi03IDM4LjcgMzguNyAwIDAgMCAyMi4yIDdjMS43IDAgMy40LS4xIDUtLjNhMjIuMyAyMi4zIDAgMCAxLTIxLjYgMTd2MzMuNGMzMC42IDAgNTUuNi0yNSA1NS42LTU1Ljd2LTc3LjlIMjcweiIgLz48cGF0aCBkPSJNMTgwLjkgMjQ0LjloNTB2MzMuNGgtNTB6IiAvPjwvZz48L2c+PC9zdmc+)</span> | Saudi Arabia | 35,950,396 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iU2VuZWdhbCIgd2lkdGg9IjUxMiIgaGVpZ2h0PSI1MTIiIHZpZXdib3g9IjAgMCA1MTIgNTEyIiBzdHlsZT0idmVydGljYWwtYWxpZ246LTAuMTI1ZW07aW1hZ2UtcmVuZGVyaW5nOm9wdGltaXplUXVhbGl0eTtoZWlnaHQ6MWVtO3dpZHRoOjFlbTsiPjx0aXRsZT5TZW5lZ2FsPC90aXRsZT48bWFzayBpZD0iY291bnRyeV9jb2RlXzItNC1hIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjY291bnRyeV9jb2RlXzItNC1hKSI+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0iTTE0NC44IDBoMjIyLjRsMzIgMjYwLTMyIDI1MkgxNDQuOGwtMzIuMS0yNTZ6IiAvPjxwYXRoIGZpbGw9IiM0OTZlMmQiIGQ9Ik0wIDBoMTQ0Ljh2NTEySDB6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0zNjcuMiAwSDUxMnY1MTJIMzY3LjJ6IiAvPjxwYXRoIGZpbGw9IiM0OTZlMmQiIGQ9Im0yNTYuMSAxNjcgMjIuMSA2OGg3MS41TDI5MiAyNzdsMjIgNjgtNTcuOC00Mi01Ny45IDQyIDIyLjEtNjgtNTcuOC00MkgyMzR6IiAvPjwvZz48L3N2Zz4=)</span> | Senegal | 16,876,720 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iU2VyYmlhIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgdmlld2JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJ2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtpbWFnZS1yZW5kZXJpbmc6b3B0aW1pemVRdWFsaXR5O2hlaWdodDoxZW07d2lkdGg6MWVtOyI+PHRpdGxlPlNlcmJpYTwvdGl0bGU+PG1hc2sgaWQ9ImNvdW50cnlfY29kZV8yLTUtYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2NvdW50cnlfY29kZV8yLTUtYSkiPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Im0wIDE2NyAyNTMuOC0xOS4zTDUxMiAxNjd2MTc4bC0yNTQuOSAzMi4zTDAgMzQ1eiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMCAwaDUxMnYxNjdIMHoiIC8+PHBhdGggZmlsbD0iI2VlZSIgZD0iTTAgMzQ1aDUxMnYxNjdIMHoiIC8+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTY2LjIgMTQ0Ljd2MTI3LjdjMCA3Mi42IDk0LjkgOTUgOTQuOSA5NXM5NC45LTIyLjQgOTQuOS05NVYxNDQuN3oiIC8+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0iTTEwNS40IDE2N2gxMTEuNHYtNDQuNmwtMjIuMyAxMS4yLTMzLjQtMzMuNC0zMy40IDMzLjQtMjIuMy0xMS4yem0xMjguMyAxMjMuMi03Mi4zLTcyLjRMODkgMjkwLjJsMjMuNyAyMy42IDQ4LjctNDguNyA0OC43IDQ4Ljd6IiAvPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0yMzMuNyAyMjIuNkgyMDBhMjIuMSAyMi4xIDAgMCAwIDMtMTEuMSAyMi4zIDIyLjMgMCAwIDAtNDItMTAuNSAyMi4zIDIyLjMgMCAwIDAtNDEuOSAxMC41IDIyLjEgMjIuMSAwIDAgMCAzIDExLjFIODlhMjMgMjMgMCAwIDAgMjMgMjIuM2gtLjdjMCAxMi4zIDEwIDIyLjIgMjIuMyAyMi4yIDAgMTEgNy44IDIwIDE4LjEgMjEuOWwtMTcuNSAzOS42YTcyLjEgNzIuMSAwIDAgMCAyNy4yIDUuMyA3Mi4xIDcyLjEgMCAwIDAgMjcuMi01LjNMMTcxLjEgMjg5YzEwLjMtMiAxOC4xLTExIDE4LjEtMjEuOSAxMi4zIDAgMjIuMy0xMCAyMi4zLTIyLjJoLS44YTIzIDIzIDAgMCAwIDIzLTIyLjN6IiAvPjwvZz48L3N2Zz4=)</span> | Serbia | 6,834,326 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iU2V5Y2hlbGxlcyIgd2lkdGg9IjUxMiIgaGVpZ2h0PSI1MTIiIHZpZXdib3g9IjAgMCA1MTIgNTEyIiBzdHlsZT0idmVydGljYWwtYWxpZ246LTAuMTI1ZW07aW1hZ2UtcmVuZGVyaW5nOm9wdGltaXplUXVhbGl0eTtoZWlnaHQ6MWVtO3dpZHRoOjFlbTsiPjx0aXRsZT5TZXljaGVsbGVzPC90aXRsZT48bWFzayBpZD0iY291bnRyeV9jb2RlXzItNi1hIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjY291bnRyeV9jb2RlXzItNi1hKSI+PHBhdGggZmlsbD0iIzAwNTJiNCIgZD0iTTAgMHYzMzJsMTUwLjktMTM4LjVMMjI1LjIgMHoiIC8+PHBhdGggZmlsbD0iI2ZmZGE0NCIgZD0iTTI3My4xIDI1My4zIDUxMiAwSDIyNS4yTDAgMzMydjgwLjJ6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik01MTIgMCAwIDQxMi4ydjUwLjRMMjc3LjkgMzkwIDUxMiAyNTZ6IiAvPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0wIDQ2Mi42IDUxMiAyNTZ2MTMzLjVsLTIyMy45IDc4LjhMMCA0ODguNHoiIC8+PHBhdGggZmlsbD0iIzZkYTU0NCIgZD0ibTUxMiAzODkuNS01MTIgOTlWNTEyaDUxMnoiIC8+PC9nPjwvc3ZnPg==)</span> | Seychelles | 99,258 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iU2llcnJhIExlb25lIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgdmlld2JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJ2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtpbWFnZS1yZW5kZXJpbmc6b3B0aW1pemVRdWFsaXR5O2hlaWdodDoxZW07d2lkdGg6MWVtOyI+PHRpdGxlPlNpZXJyYSBMZW9uZTwvdGl0bGU+PG1hc2sgaWQ9ImNvdW50cnlfY29kZV8yLTctYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2NvdW50cnlfY29kZV8yLTctYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Im0wIDE2NyAyNTMuOC0xOS4zTDUxMiAxNjd2MTc4bC0yNTQuOSAzMi4zTDAgMzQ1eiIgLz48cGF0aCBmaWxsPSIjNmRhNTQ0IiBkPSJNMCAwaDUxMnYxNjdIMHoiIC8+PHBhdGggZmlsbD0iIzMzOGFmMyIgZD0iTTAgMzQ1aDUxMnYxNjdIMHoiIC8+PC9nPjwvc3ZnPg==)</span> | Sierra Leone | 8,420,641 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iU2luZ2Fwb3JlIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgdmlld2JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJ2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTtpbWFnZS1yZW5kZXJpbmc6b3B0aW1pemVRdWFsaXR5O2hlaWdodDoxZW07d2lkdGg6MWVtOyI+PHRpdGxlPlNpbmdhcG9yZTwvdGl0bGU+PG1hc2sgaWQ9ImNvdW50cnlfY29kZV8yLTgtYSI+PGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiNmZmYiPjwvY2lyY2xlPjwvbWFzaz48ZyBtYXNrPSJ1cmwoI2NvdW50cnlfY29kZV8yLTgtYSkiPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Im0wIDI1NiAyNTcuNy01MUw1MTIgMjU2djI1NkgweiIgLz48cGF0aCBmaWxsPSIjZDgwMDI3IiBkPSJNMCAwaDUxMnYyNTZIMHoiIC8+PGcgZmlsbD0iI2VlZSI+PHBhdGggZD0iTTE1NS44IDEzMy42QTc4IDc4IDAgMCAxIDIxNyA1Ny41YTc4LjIgNzguMiAwIDAgMC0xNi43LTEuOCA3OCA3OCAwIDEgMCAxNi43IDE1NCA3OCA3OCAwIDAgMS02MS4yLTc2LjF6TTI1NiA2MS4ybDUuNSAxN2gxOGwtMTQuNiAxMC41IDUuNiAxN0wyNTYgOTUuMmwtMTQuNSAxMC41IDUuNi0xNy0xNC41LTEwLjVoMTcuOXoiIC8+PHBhdGggZD0ibTIxMi42IDk0LjYgNS42IDE3SDIzNmwtMTQuNCAxMC41IDUuNSAxNy0xNC41LTEwLjUtMTQuNCAxMC41IDUuNS0xNy0xNC41LTEwLjVoMTcuOXptODYuOCAwIDUuNSAxN2gxNy45bC0xNC41IDEwLjUgNS41IDE3LTE0LjQtMTAuNS0xNC41IDEwLjUgNS41LTE3LTE0LjQtMTAuNWgxNy44em0tMTYuNyA1MC4xIDUuNSAxN2gxNy45bC0xNC41IDEwLjUgNS41IDE3LTE0LjQtMTAuNS0xNC41IDEwLjUgNS41LTE3LTE0LjQtMTAuNWgxNy45em0tNTMuNCAwIDUuNSAxN2gxOGwtMTQuNSAxMC41IDUuNSAxNy0xNC41LTEwLjUtMTQuNCAxMC41IDUuNS0xNy0xNC41LTEwLjVoMTcuOXoiIC8+PC9nPjwvZz48L3N2Zz4=)</span> | Singapore | 5,453,566 |
| <span style="white-space:nowrap;">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iU2ludCBNYWFydGVuIChEdXRjaCBwYXJ0KSIgd2lkdGg9IjUxMiIgaGVpZ2h0PSI1MTIiIHZpZXdib3g9IjAgMCA1MTIgNTEyIiBzdHlsZT0idmVydGljYWwtYWxpZ246LTAuMTI1ZW07aW1hZ2UtcmVuZGVyaW5nOm9wdGltaXplUXVhbGl0eTtoZWlnaHQ6MWVtO3dpZHRoOjFlbTsiPjx0aXRsZT5TaW50IE1hYXJ0ZW4gKER1dGNoIHBhcnQpPC90aXRsZT48bWFzayBpZD0iY291bnRyeV9jb2RlXzItOS1hIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjY291bnRyeV9jb2RlXzItOS1hKSI+PHBhdGggZmlsbD0iI2Q4MDAyNyIgZD0iTTAgMGg1MTJ2MjU2bC0yNjUgNDUuMnoiIC8+PHBhdGggZmlsbD0iIzAwNTJiNCIgZD0iTTIxMCAyNTZoMzAydjI1NkgweiIgLz48cGF0aCBmaWxsPSIjZWVlIiBkPSJNMCAwdjUxMmwyNTYtMjU2eiIgLz48ZyBmaWxsPSIjZmZkYTQ0Ij48cGF0aCBkPSJNMjggMjU2YTczLjEgNzMuMSAwIDAgMC0uMiA1LjYgNzIuMyA3Mi4zIDAgMSAwIDE0NC41LTUuNnoiIC8+PGNpcmNsZSBjeD0iMTAwLjIiIGN5PSIyMDAuMyIgcj0iMjIuMyI+PC9jaXJjbGU+PC9nPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik01MCAxOTQuOFYyNjdjMCAzOC40IDUwLjIgNTAgNTAuMiA1MHM1MC0xMS42IDUwLTUwdi03Mi4zaC0xMDB6IiAvPjxwYXRoIGZpbGw9IiMzMzhhZjMiIGQ9Ik0xMDAuMiAyOTRjLTkuMy0zLjQtMjgtMTItMjgtMjd2LTUwSDEyOHY1MGMwIDE1LTE4LjYgMjMuNi0yNy44IDI2Ljl6IiAvPjxwYXRoIGZpbGw9IiNlZWUiIGQ9Ik0xMTEuMyAyNDQuOXYtMTEuMmwtMTEuMS01LjUtMTEuMiA1LjVWMjQ1bC01LjUgNS41djIyLjNoMzMuNHYtMjIuM3oiIC8+PC9nPjwvc3ZnPg==)</span> | Sint Maarten (Dutch part) | 42,846 |


Here's another example (again using [countrypops](data.countrypops.md#great_tables.data.countrypops)) where we generate a table providing populations every five years for the Benelux countries (`"BEL"`, `"NLD"`, and `"LUX"`). After some filtering and a pivot, the [fmt_flag()](GT.fmt_flag.md#great_tables.GT.fmt_flag) method is used to obtain flag icons from 3-letter country codes present in the `country_code_3` column.


``` python
import polars.selectors as cs

countrypops_mini = (
    pl.from_pandas(countrypops)
    .filter(pl.col("country_code_3").is_in(["BEL", "NLD", "LUX"]))
    .filter((pl.col("year") % 10 == 0) & (pl.col("year") >= 1960))
    .pivot("year", index = ["country_code_3", "country_name"], values="population")
)

(
    GT(countrypops_mini)
    .tab_header(title="Populations of the Benelux Countries")
    .tab_spanner(label="Year", columns=cs.numeric())
    .fmt_integer(columns=cs.numeric())
    .fmt_flag(columns="country_code_3")
    .cols_label(
        country_code_3="",
        country_name="Country"
    )
)
```


<style>
#wqfryejtdi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wqfryejtdi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wqfryejtdi p { margin: 0; padding: 0; }
 #wqfryejtdi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wqfryejtdi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wqfryejtdi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wqfryejtdi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wqfryejtdi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wqfryejtdi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wqfryejtdi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wqfryejtdi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wqfryejtdi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wqfryejtdi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wqfryejtdi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wqfryejtdi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wqfryejtdi .gt_spanner_row { border-bottom-style: hidden; }
 #wqfryejtdi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wqfryejtdi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wqfryejtdi .gt_from_md> :first-child { margin-top: 0; }
 #wqfryejtdi .gt_from_md> :last-child { margin-bottom: 0; }
 #wqfryejtdi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wqfryejtdi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wqfryejtdi .gt_indent_1 { text-indent: 5px; }
 #wqfryejtdi .gt_indent_2 { text-indent: calc(5px * 2); }
 #wqfryejtdi .gt_indent_3 { text-indent: calc(5px * 3); }
 #wqfryejtdi .gt_indent_4 { text-indent: calc(5px * 4); }
 #wqfryejtdi .gt_indent_5 { text-indent: calc(5px * 5); }
 #wqfryejtdi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wqfryejtdi .gt_row_group_first td { border-top-width: 2px; }
 #wqfryejtdi .gt_row_group_first th { border-top-width: 2px; }
 #wqfryejtdi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wqfryejtdi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wqfryejtdi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wqfryejtdi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wqfryejtdi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wqfryejtdi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wqfryejtdi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wqfryejtdi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wqfryejtdi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wqfryejtdi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wqfryejtdi .gt_left { text-align: left; }
 #wqfryejtdi .gt_center { text-align: center; }
 #wqfryejtdi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wqfryejtdi .gt_font_normal { font-weight: normal; }
 #wqfryejtdi .gt_font_bold { font-weight: bold; }
 #wqfryejtdi .gt_font_italic { font-style: italic; }
 #wqfryejtdi .gt_super { font-size: 65%; }
 #wqfryejtdi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wqfryejtdi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wqfryejtdi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wqfryejtdi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wqfryejtdi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wqfryejtdi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="9" id="title" class="gt_heading gt_title gt_font_normal">Populations of the Benelux Countries</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="country_code_3" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th rowspan="2" id="country_name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">Country</th>
<th colspan="7" id="Year" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">Year</th>
</tr>
<tr class="gt_col_headings">
<th id="1960" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1960</th>
<th id="1970" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1970</th>
<th id="1980" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1980</th>
<th id="1990" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">1990</th>
<th id="2000" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2000</th>
<th id="2010" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2010</th>
<th id="2020" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">2020</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left" headers="country_code_3"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iQmVsZ2l1bSIgd2lkdGg9IjUxMiIgaGVpZ2h0PSI1MTIiIHZpZXdib3g9IjAgMCA1MTIgNTEyIiBzdHlsZT0idmVydGljYWwtYWxpZ246LTAuMTI1ZW07aW1hZ2UtcmVuZGVyaW5nOm9wdGltaXplUXVhbGl0eTtoZWlnaHQ6MWVtO3dpZHRoOjFlbTsiPjx0aXRsZT5CZWxnaXVtPC90aXRsZT48bWFzayBpZD0iY291bnRyeV9jb2RlXzMtMC1hIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjY291bnRyeV9jb2RlXzMtMC1hKSI+PHBhdGggZmlsbD0iIzMzMyIgZD0iTTAgMGgxNjdsMzguMiAyNTIuNkwxNjcgNTEySDB6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0zNDUgMGgxNjd2NTEySDM0NWwtMzYuNy0yNTZ6IiAvPjxwYXRoIGZpbGw9IiNmZmRhNDQiIGQ9Ik0xNjcgMGgxNzh2NTEySDE2N3oiIC8+PC9nPjwvc3ZnPg==" /></span></td>
<td class="gt_row gt_left" headers="country_name">Belgium</td>
<td class="gt_row gt_right" headers="Year 1960">9,153,489</td>
<td class="gt_row gt_right" headers="Year 1970">9,655,549</td>
<td class="gt_row gt_right" headers="Year 1980">9,859,242</td>
<td class="gt_row gt_right" headers="Year 1990">9,967,379</td>
<td class="gt_row gt_right" headers="Year 2000">10,251,250</td>
<td class="gt_row gt_right" headers="Year 2010">10,895,586</td>
<td class="gt_row gt_right" headers="Year 2020">11,538,604</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="country_code_3"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iTHV4ZW1ib3VyZyIgd2lkdGg9IjUxMiIgaGVpZ2h0PSI1MTIiIHZpZXdib3g9IjAgMCA1MTIgNTEyIiBzdHlsZT0idmVydGljYWwtYWxpZ246LTAuMTI1ZW07aW1hZ2UtcmVuZGVyaW5nOm9wdGltaXplUXVhbGl0eTtoZWlnaHQ6MWVtO3dpZHRoOjFlbTsiPjx0aXRsZT5MdXhlbWJvdXJnPC90aXRsZT48bWFzayBpZD0iY291bnRyeV9jb2RlXzMtMS1hIj48Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI1NiIgZmlsbD0iI2ZmZiI+PC9jaXJjbGU+PC9tYXNrPjxnIG1hc2s9InVybCgjY291bnRyeV9jb2RlXzMtMS1hKSI+PHBhdGggZmlsbD0iI2VlZSIgZD0ibTAgMTY3IDI1My44LTE5LjNMNTEyIDE2N3YxNzhsLTI1NC45IDMyLjNMMCAzNDV6IiAvPjxwYXRoIGZpbGw9IiNkODAwMjciIGQ9Ik0wIDBoNTEydjE2N0gweiIgLz48cGF0aCBmaWxsPSIjMzM4YWYzIiBkPSJNMCAzNDVoNTEydjE2N0gweiIgLz48L2c+PC9zdmc+" /></span></td>
<td class="gt_row gt_left" headers="country_name">Luxembourg</td>
<td class="gt_row gt_right" headers="Year 1960">313,970</td>
<td class="gt_row gt_right" headers="Year 1970">339,171</td>
<td class="gt_row gt_right" headers="Year 1980">364,150</td>
<td class="gt_row gt_right" headers="Year 1990">381,850</td>
<td class="gt_row gt_right" headers="Year 2000">436,300</td>
<td class="gt_row gt_right" headers="Year 2010">506,953</td>
<td class="gt_row gt_right" headers="Year 2020">630,419</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="country_code_3"><span style="white-space:nowrap;"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHJvbGU9ImltZyIgYXJpYS1sYWJlbD0iTmV0aGVybGFuZHMiIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiB2aWV3Ym94PSIwIDAgNTEyIDUxMiIgc3R5bGU9InZlcnRpY2FsLWFsaWduOi0wLjEyNWVtO2ltYWdlLXJlbmRlcmluZzpvcHRpbWl6ZVF1YWxpdHk7aGVpZ2h0OjFlbTt3aWR0aDoxZW07Ij48dGl0bGU+TmV0aGVybGFuZHM8L3RpdGxlPjxtYXNrIGlkPSJjb3VudHJ5X2NvZGVfMy0yLWEiPjxjaXJjbGUgY3g9IjI1NiIgY3k9IjI1NiIgcj0iMjU2IiBmaWxsPSIjZmZmIj48L2NpcmNsZT48L21hc2s+PGcgbWFzaz0idXJsKCNjb3VudHJ5X2NvZGVfMy0yLWEpIj48cGF0aCBmaWxsPSIjZWVlIiBkPSJtMCAxNjcgMjUzLjgtMTkuM0w1MTIgMTY3djE3OGwtMjU0LjkgMzIuM0wwIDM0NXoiIC8+PHBhdGggZmlsbD0iI2EyMDAxZCIgZD0iTTAgMGg1MTJ2MTY3SDB6IiAvPjxwYXRoIGZpbGw9IiMwMDUyYjQiIGQ9Ik0wIDM0NWg1MTJ2MTY3SDB6IiAvPjwvZz48L3N2Zz4=" /></span></td>
<td class="gt_row gt_left" headers="country_name">Netherlands</td>
<td class="gt_row gt_right" headers="Year 1960">11,486,631</td>
<td class="gt_row gt_right" headers="Year 1970">13,038,526</td>
<td class="gt_row gt_right" headers="Year 1980">14,149,800</td>
<td class="gt_row gt_right" headers="Year 1990">14,951,510</td>
<td class="gt_row gt_right" headers="Year 2000">15,925,513</td>
<td class="gt_row gt_right" headers="Year 2010">16,615,394</td>
<td class="gt_row gt_right" headers="Year 2020">17,441,500</td>
</tr>
</tbody>
</table>
