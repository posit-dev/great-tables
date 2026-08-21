# GT.fmt_datetime()


Format values as datetimes.


Usage

``` python
GT.fmt_datetime(
    columns=None,
    rows=None,
    date_style="iso",
    time_style="iso",
    format_str=None,
    sep=" ",
    pattern="{x}",
    locale=None
)
```


Format input values to datetime values using one of 17 preset date styles and one of 5 preset time styles. Input can be in the form of `datetime` values, or strings in the ISO 8601 forms of `YYYY-MM-DD HH:MM:SS` or `YYYY-MM-DD`.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`date_style: DateStyle = ``"iso"`  
The date style to use. By default this is the short name `"iso"` which corresponds to ISO 8601 date formatting. There are 41 date styles in total.

`time_style: TimeStyle = ``"iso"`  
The time style to use. By default this is the short name `"iso"` which corresponds to how times are formatted within ISO 8601 datetime values. There are 5 time styles in total.

`format_str: str | None = None`  
A string that specifies the format of the datetime string. This is a `strftime()` format string that can be used to format date or datetime input. If `format=` is provided, the `date_style=` and `time_style=` arguments are ignored.

`sep: str = ``" "`  
A string that separates the date and time components of the datetime string. The default is a space character (`" "`). This is ignored if `format=` is provided.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France). Only relevant if `date_style=` or `time_style=` are provided.


## Formatting With The `date_style=` And `time_style=` Arguments

If not supplying a formatting string to `format_str=` we need to supply a preset date style to the `date_style=` argument and a preset time style to the `time_style=` argument. The date styles are numerous and can handle localization to any supported locale. The following table provides a listing of all date styles and their output values (corresponding to an input date of `2000-02-29 14:35:00`).

|     | Date Style              | Output                         |
|-----|-------------------------|--------------------------------|
| 1   | `"iso"`                 | `"2000-02-29"`                 |
| 2   | `"wday_month_day_year"` | `"Tuesday, February 29, 2000"` |
| 3   | `"wd_m_day_year"`       | `"Tue, Feb 29, 2000"`          |
| 4   | `"wday_day_month_year"` | `"Tuesday 29 February 2000"`   |
| 5   | `"month_day_year"`      | `"February 29, 2000"`          |
| 6   | `"m_day_year"`          | `"Feb 29, 2000"`               |
| 7   | `"day_m_year"`          | `"29 Feb 2000"`                |
| 8   | `"day_month_year"`      | `"29 February 2000"`           |
| 9   | `"day_month"`           | `"29 February"`                |
| 10  | `"day_m"`               | `"29 Feb"`                     |
| 11  | `"year"`                | `"2000"`                       |
| 12  | `"month"`               | `"February"`                   |
| 13  | `"day"`                 | `"29"`                         |
| 14  | `"year.mn.day"`         | `"2000/02/29"`                 |
| 15  | `"y.mn.day"`            | `"00/02/29"`                   |
| 16  | `"year_week"`           | `"2000-W09"`                   |
| 17  | `"year_quarter"`        | `"2000-Q1"`                    |

The time styles can also handle localization to any supported locale. The following table provides a listing of all time styles and their output values (corresponding to an input time of `2000-02-29 14:35:00`).

|     | Time Style    | Output         | Notes         |
|-----|---------------|----------------|---------------|
| 1   | `"iso"`       | `"14:35:00"`   | ISO 8601, 24h |
| 2   | `"iso-short"` | `"14:35"`      | ISO 8601, 24h |
| 3   | `"h_m_s_p"`   | `"2:35:00 PM"` | 12h           |
| 4   | `"h_m_p"`     | `"2:35 PM"`    | 12h           |
| 5   | `"h_p"`       | `"2 PM"`       | 12h           |


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a simple, two-column table (keeping only the `date` and `time` columns). With the [fmt_datetime()](GT.fmt_datetime.md#great_tables.GT.fmt_datetime) method, we'll format the `date` column to display dates formatted with the `"month_day_year"` date style and the `time` column to display times formatted with the `"h_m_s_p"` time style.


``` python
from great_tables import GT, exibble

exibble_mini = exibble[["date", "time"]]

(
    GT(exibble_mini)
    .fmt_datetime(
        columns="date",
        date_style="month_day_year",
        time_style="h_m_s_p"
    )
)
```


<style>
#obvgntmoem table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#obvgntmoem thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#obvgntmoem p { margin: 0; padding: 0; }
 #obvgntmoem .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #obvgntmoem .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #obvgntmoem .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #obvgntmoem .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #obvgntmoem .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #obvgntmoem .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #obvgntmoem .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #obvgntmoem .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #obvgntmoem .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #obvgntmoem .gt_column_spanner_outer:first-child { padding-left: 0; }
 #obvgntmoem .gt_column_spanner_outer:last-child { padding-right: 0; }
 #obvgntmoem .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #obvgntmoem .gt_spanner_row { border-bottom-style: hidden; }
 #obvgntmoem .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #obvgntmoem .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #obvgntmoem .gt_from_md> :first-child { margin-top: 0; }
 #obvgntmoem .gt_from_md> :last-child { margin-bottom: 0; }
 #obvgntmoem .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #obvgntmoem .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #obvgntmoem .gt_indent_1 { text-indent: 5px; }
 #obvgntmoem .gt_indent_2 { text-indent: calc(5px * 2); }
 #obvgntmoem .gt_indent_3 { text-indent: calc(5px * 3); }
 #obvgntmoem .gt_indent_4 { text-indent: calc(5px * 4); }
 #obvgntmoem .gt_indent_5 { text-indent: calc(5px * 5); }
 #obvgntmoem .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #obvgntmoem .gt_row_group_first td { border-top-width: 2px; }
 #obvgntmoem .gt_row_group_first th { border-top-width: 2px; }
 #obvgntmoem .gt_striped { color: #333333; background-color: #F4F4F4; }
 #obvgntmoem .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #obvgntmoem .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #obvgntmoem .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #obvgntmoem .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #obvgntmoem .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #obvgntmoem .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #obvgntmoem .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #obvgntmoem .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #obvgntmoem .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #obvgntmoem .gt_left { text-align: left; }
 #obvgntmoem .gt_center { text-align: center; }
 #obvgntmoem .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #obvgntmoem .gt_font_normal { font-weight: normal; }
 #obvgntmoem .gt_font_bold { font-weight: bold; }
 #obvgntmoem .gt_font_italic { font-style: italic; }
 #obvgntmoem .gt_super { font-size: 65%; }
 #obvgntmoem .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #obvgntmoem .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #obvgntmoem .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #obvgntmoem .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #obvgntmoem .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #obvgntmoem .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date                          | time  |
|-------------------------------|-------|
| January 15, 2015 12:00:00 AM  | 13:35 |
| February 15, 2015 12:00:00 AM | 14:40 |
| March 15, 2015 12:00:00 AM    | 15:45 |
| April 15, 2015 12:00:00 AM    | 16:50 |
| May 15, 2015 12:00:00 AM      | 17:55 |
| June 15, 2015 12:00:00 AM     |       |
|                               | 19:10 |
| August 15, 2015 12:00:00 AM   | 20:20 |
