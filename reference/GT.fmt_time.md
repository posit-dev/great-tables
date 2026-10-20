# GT.fmt_time()


Format values as times.


Usage

``` python
GT.fmt_time(
    columns=None,
    rows=None,
    time_style="iso",
    pattern="{x}",
    locale=None,
)
```


Format input values to time values using one of 25 preset time styles. Input can be in the form of `time` values, or strings in the ISO 8601 forms of `HH:MM:SS` or `YYYY-MM-DD HH:MM:SS`. For `datetime` values (and datetime strings), the time part is formatted. Dates without a time (e.g., `"2024-01-05"`) raise an error; use <a href="../reference/GT.fmt_date.html#great_tables.GT.fmt_date" class="gdls-link"><code>fmt_date()</code></a> for those.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`time_style: TimeStyle = ``"iso"`  
The time style to use. By default this is the short name `"iso"` which corresponds to how times are formatted within ISO 8601 datetime values. There are 25 time styles in total.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Formatting With The `time_style=` Argument

We need to supply a preset time style to the `time_style=` argument. The time styles are numerous and can handle localization to any supported locale. Many of the time styles are termed flexible time formats and this means that their output will adapt to any `locale=` provided (e.g., `"hm"` is `"2:35 PM"` in English and `"午後2:35"` in Japanese). That feature makes the flexible time formats a better option for locales other than `"en"` (the default locale).

The following table provides a listing of all time styles and their output values (corresponding to an input of `2000-02-29 14:35:00`). It is noted which of these represent 12- or 24-hour time.

|     | Time Style    | Output                           | Notes         |
|-----|---------------|----------------------------------|---------------|
| 1   | `"iso"`       | `"14:35:00"`                     | ISO 8601, 24h |
| 2   | `"iso-short"` | `"14:35"`                        | ISO 8601, 24h |
| 3   | `"h_m_s_p"`   | `"2:35:00 PM"`                   | 12h           |
| 4   | `"h_m_p"`     | `"2:35 PM"`                      | 12h           |
| 5   | `"h_p"`       | `"2 PM"`                         | 12h           |
| 6   | `"Hms"`       | `"14:35:00"`                     | flexible, 24h |
| 7   | `"Hm"`        | `"14:35"`                        | flexible, 24h |
| 8   | `"H"`         | `"14"`                           | flexible, 24h |
| 9   | `"EHm"`       | `"Tue 14:35"`                    | flexible, 24h |
| 10  | `"EHms"`      | `"Tue 14:35:00"`                 | flexible, 24h |
| 11  | `"Hmsv"`      | `"14:35:00 UTC"`                 | flexible, 24h |
| 12  | `"Hmv"`       | `"14:35 UTC"`                    | flexible, 24h |
| 13  | `"hms"`       | `"2:35:00 PM"`                   | flexible, 12h |
| 14  | `"hm"`        | `"2:35 PM"`                      | flexible, 12h |
| 15  | `"h"`         | `"2 PM"`                         | flexible, 12h |
| 16  | `"Ehm"`       | `"Tue 2:35 PM"`                  | flexible, 12h |
| 17  | `"Ehms"`      | `"Tue 2:35:00 PM"`               | flexible, 12h |
| 18  | `"EBhms"`     | `"Tue 2:35:00 in the afternoon"` | flexible, 12h |
| 19  | `"Bhms"`      | `"2:35:00 in the afternoon"`     | flexible, 12h |
| 20  | `"EBhm"`      | `"Tue 2:35 in the afternoon"`    | flexible, 12h |
| 21  | `"Bhm"`       | `"2:35 in the afternoon"`        | flexible, 12h |
| 22  | `"Bh"`        | `"2 in the afternoon"`           | flexible, 12h |
| 23  | `"hmsv"`      | `"2:35:00 PM UTC"`               | flexible, 12h |
| 24  | `"hmv"`       | `"2:35 PM UTC"`                  | flexible, 12h |
| 25  | `"ms"`        | `"35:00"`                        | flexible      |

The names of the flexible time styles are CLDR skeletons, where each letter stands for a field: `H` is the hour (0-23), `h` the hour (1-12) with AM or PM, `B` the hour with a period of the day (e.g., "in the afternoon"), `m` the minute, `s` the second, `E` the day of the week, and `v` the time zone.

The styles with the day of the week (`E`) need `datetime` values (or datetime strings); a `time` value without a date raises an error with them. The styles with the time zone (`v`) give its generic name for an aware value (e.g., `"ET"` for `America/New_York`), falling back to a name like `"UTC"` or an offset like `"-0500"` for a zone without one. A naive value is taken to be in UTC.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Adapting Output To A Specific `locale`

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). Note that a `locale` value provided here will override any global locale setting performed in <a href="../reference/GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>'s own `locale` argument (it is settable there as a value received by all other methods that have a `locale` argument).


## Examples

Let's use the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a simple, two-column table (keeping only the `date` and `time` columns). With the <a href="../reference/GT.fmt_time.html#great_tables.GT.fmt_time" class="gdls-link"><code>fmt_time()</code></a> method, we'll format the `time` column to display times formatted with the `"h_m_s_p"` time style.


``` python
from great_tables import GT, exibble

exibble_mini = exibble[["date", "time"]]

(
    GT(exibble_mini)
    .fmt_time(columns="time", time_style="h_m_s_p")
)
```


<style>
#nkhdngffzb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nkhdngffzb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nkhdngffzb p { margin: 0; padding: 0; }
 #nkhdngffzb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nkhdngffzb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nkhdngffzb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nkhdngffzb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nkhdngffzb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nkhdngffzb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nkhdngffzb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nkhdngffzb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nkhdngffzb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nkhdngffzb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nkhdngffzb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nkhdngffzb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nkhdngffzb .gt_spanner_row { border-bottom-style: hidden; }
 #nkhdngffzb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nkhdngffzb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nkhdngffzb .gt_from_md> :first-child { margin-top: 0; }
 #nkhdngffzb .gt_from_md> :last-child { margin-bottom: 0; }
 #nkhdngffzb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nkhdngffzb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nkhdngffzb .gt_indent_1 { text-indent: 5px; }
 #nkhdngffzb .gt_indent_2 { text-indent: calc(5px * 2); }
 #nkhdngffzb .gt_indent_3 { text-indent: calc(5px * 3); }
 #nkhdngffzb .gt_indent_4 { text-indent: calc(5px * 4); }
 #nkhdngffzb .gt_indent_5 { text-indent: calc(5px * 5); }
 #nkhdngffzb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nkhdngffzb .gt_row_group_first td { border-top-width: 2px; }
 #nkhdngffzb .gt_row_group_first th { border-top-width: 2px; }
 #nkhdngffzb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nkhdngffzb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nkhdngffzb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nkhdngffzb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nkhdngffzb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nkhdngffzb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nkhdngffzb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nkhdngffzb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nkhdngffzb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nkhdngffzb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nkhdngffzb .gt_left { text-align: left; }
 #nkhdngffzb .gt_center { text-align: center; }
 #nkhdngffzb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nkhdngffzb .gt_font_normal { font-weight: normal; }
 #nkhdngffzb .gt_font_bold { font-weight: bold; }
 #nkhdngffzb .gt_font_italic { font-style: italic; }
 #nkhdngffzb .gt_super { font-size: 65%; }
 #nkhdngffzb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nkhdngffzb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nkhdngffzb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nkhdngffzb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nkhdngffzb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nkhdngffzb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | time       |
|------------|------------|
| 2015-01-15 | 1:35:00 PM |
| 2015-02-15 | 2:40:00 PM |
| 2015-03-15 | 3:45:00 PM |
| 2015-04-15 | 4:50:00 PM |
| 2015-05-15 | 5:55:00 PM |
| 2015-06-15 | None       |
| None       | 7:10:00 PM |
| 2015-08-15 | 8:20:00 PM |


A flexible time style adapts to the locale. Here, the `"hm"` style is used to format the times for a table in Japanese.


``` python
(
    GT(exibble_mini, locale="ja")
    .fmt_time(columns="time", time_style="hm")
)
```


<style>
#nlqnkfkfse table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nlqnkfkfse thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nlqnkfkfse p { margin: 0; padding: 0; }
 #nlqnkfkfse .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nlqnkfkfse .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nlqnkfkfse .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nlqnkfkfse .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nlqnkfkfse .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nlqnkfkfse .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nlqnkfkfse .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nlqnkfkfse .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nlqnkfkfse .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nlqnkfkfse .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nlqnkfkfse .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nlqnkfkfse .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nlqnkfkfse .gt_spanner_row { border-bottom-style: hidden; }
 #nlqnkfkfse .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nlqnkfkfse .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nlqnkfkfse .gt_from_md> :first-child { margin-top: 0; }
 #nlqnkfkfse .gt_from_md> :last-child { margin-bottom: 0; }
 #nlqnkfkfse .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nlqnkfkfse .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nlqnkfkfse .gt_indent_1 { text-indent: 5px; }
 #nlqnkfkfse .gt_indent_2 { text-indent: calc(5px * 2); }
 #nlqnkfkfse .gt_indent_3 { text-indent: calc(5px * 3); }
 #nlqnkfkfse .gt_indent_4 { text-indent: calc(5px * 4); }
 #nlqnkfkfse .gt_indent_5 { text-indent: calc(5px * 5); }
 #nlqnkfkfse .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nlqnkfkfse .gt_row_group_first td { border-top-width: 2px; }
 #nlqnkfkfse .gt_row_group_first th { border-top-width: 2px; }
 #nlqnkfkfse .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nlqnkfkfse .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nlqnkfkfse .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nlqnkfkfse .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nlqnkfkfse .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nlqnkfkfse .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nlqnkfkfse .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nlqnkfkfse .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nlqnkfkfse .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nlqnkfkfse .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nlqnkfkfse .gt_left { text-align: left; }
 #nlqnkfkfse .gt_center { text-align: center; }
 #nlqnkfkfse .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nlqnkfkfse .gt_font_normal { font-weight: normal; }
 #nlqnkfkfse .gt_font_bold { font-weight: bold; }
 #nlqnkfkfse .gt_font_italic { font-style: italic; }
 #nlqnkfkfse .gt_super { font-size: 65%; }
 #nlqnkfkfse .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nlqnkfkfse .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nlqnkfkfse .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nlqnkfkfse .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nlqnkfkfse .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nlqnkfkfse .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date       | time     |
|------------|----------|
| 2015-01-15 | 午後1:35 |
| 2015-02-15 | 午後2:40 |
| 2015-03-15 | 午後3:45 |
| 2015-04-15 | 午後4:50 |
| 2015-05-15 | 午後5:55 |
| 2015-06-15 | None     |
| None       | 午後7:10 |
| 2015-08-15 | 午後8:20 |
