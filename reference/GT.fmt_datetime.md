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
    locale=None,
)
```


Format input values to datetime values using one of 41 preset date styles and one of 25 preset time styles, or with a format string. Input can be in the form of `datetime` values, or strings in the ISO 8601 forms of `YYYY-MM-DD HH:MM:SS` or `YYYY-MM-DD`.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`date_style: DateStyle = ``"iso"`  
The date style to use. By default this is the short name `"iso"` which corresponds to ISO 8601 date formatting. There are 41 date styles in total.

`time_style: TimeStyle = ``"iso"`  
The time style to use. By default this is the short name `"iso"` which corresponds to how times are formatted within ISO 8601 datetime values. There are 25 time styles in total.

`format_str: str | None = None`  
A format string to use instead of the preset styles. This can be a CLDR datetime pattern (e.g., `"EEEE, d MMMM y"`), which is localized using `locale=` (or the table locale), or a `strftime()` format string (any string containing `%`, e.g., `"%d.%m.%Y"`), which isn't localized. If `format_str=` is provided, the `date_style=`, `time_style=`, and `sep=` arguments are ignored.

`sep: str = ``" "`  
A string that separates the date and time components of the datetime string. The default is a space character (`" "`). This is ignored if `format_str=` is provided.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France). This can't be used with a `strftime()` format string in `format_str=`, since that isn't localized (with one, a table locale set in <a href="../reference/GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a> is ignored).


## Formatting With The `date_style=` And `time_style=` Arguments

If not supplying a formatting string to `format_str=` we need to supply a preset date style to the `date_style=` argument and a preset time style to the `time_style=` argument. The date and time parts are formatted separately and joined by `sep=`. The styles are numerous and can handle localization to any supported locale. Those termed flexible adapt their output to any `locale=` provided: the order of the fields, the punctuation, and even which fields are abbreviated follow the locale's conventions. That feature makes the flexible formats a better option for locales other than `"en"` (the default locale).

The following table provides a listing of all date styles and their output values (corresponding to an input of `2000-02-29 14:35:00`).

|     | Date Style              | Output                         | Notes    |
|-----|-------------------------|--------------------------------|----------|
| 1   | `"iso"`                 | `"2000-02-29"`                 | ISO 8601 |
| 2   | `"wday_month_day_year"` | `"Tuesday, February 29, 2000"` |          |
| 3   | `"wd_m_day_year"`       | `"Tue, Feb 29, 2000"`          |          |
| 4   | `"wday_day_month_year"` | `"Tuesday 29 February 2000"`   |          |
| 5   | `"month_day_year"`      | `"February 29, 2000"`          |          |
| 6   | `"m_day_year"`          | `"Feb 29, 2000"`               |          |
| 7   | `"day_m_year"`          | `"29 Feb 2000"`                |          |
| 8   | `"day_month_year"`      | `"29 February 2000"`           |          |
| 9   | `"day_month"`           | `"29 February"`                |          |
| 10  | `"day_m"`               | `"29 Feb"`                     |          |
| 11  | `"year"`                | `"2000"`                       |          |
| 12  | `"month"`               | `"February"`                   |          |
| 13  | `"day"`                 | `"29"`                         |          |
| 14  | `"year.mn.day"`         | `"2000/02/29"`                 |          |
| 15  | `"y.mn.day"`            | `"00/02/29"`                   |          |
| 16  | `"year_week"`           | `"2000-W09"`                   | ISO 8601 |
| 17  | `"year_quarter"`        | `"2000-Q1"`                    |          |
| 18  | `"yMd"`                 | `"2/29/2000"`                  | flexible |
| 19  | `"yMEd"`                | `"Tue, 2/29/2000"`             | flexible |
| 20  | `"yMMM"`                | `"Feb 2000"`                   | flexible |
| 21  | `"yMMMM"`               | `"February 2000"`              | flexible |
| 22  | `"yMMMd"`               | `"Feb 29, 2000"`               | flexible |
| 23  | `"yMMMEd"`              | `"Tue, Feb 29, 2000"`          | flexible |
| 24  | `"GyMd"`                | `"2/29/2000 AD"`               | flexible |
| 25  | `"GyMMMd"`              | `"Feb 29, 2000 AD"`            | flexible |
| 26  | `"GyMMMEd"`             | `"Tue, Feb 29, 2000 AD"`       | flexible |
| 27  | `"yM"`                  | `"2/2000"`                     | flexible |
| 28  | `"Md"`                  | `"2/29"`                       | flexible |
| 29  | `"MEd"`                 | `"Tue, 2/29"`                  | flexible |
| 30  | `"MMMd"`                | `"Feb 29"`                     | flexible |
| 31  | `"MMMEd"`               | `"Tue, Feb 29"`                | flexible |
| 32  | `"MMMMd"`               | `"February 29"`                | flexible |
| 33  | `"GyMMM"`               | `"Feb 2000 AD"`                | flexible |
| 34  | `"yQQQ"`                | `"Q1 2000"`                    | flexible |
| 35  | `"yQQQQ"`               | `"1st quarter 2000"`           | flexible |
| 36  | `"Gy"`                  | `"2000 AD"`                    | flexible |
| 37  | `"y"`                   | `"2000"`                       | flexible |
| 38  | `"M"`                   | `"2"`                          | flexible |
| 39  | `"MMM"`                 | `"Feb"`                        | flexible |
| 40  | `"d"`                   | `"29"`                         | flexible |
| 41  | `"Ed"`                  | `"29 Tue"`                     | flexible |

The `"year_week"` style gives the ISO 8601 week date in every locale: weeks start on Monday, week 1 is the week containing the first Thursday of the year, and the year shown is the one the week belongs to (so `2024-12-30` is `"2025-W01"`).

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

The styles with the time zone (`v`) give its generic name for an aware value (e.g., `"ET"` for `America/New_York`), falling back to a name like `"UTC"` or an offset like `"-0500"` for a zone without one. A naive value is taken to be in UTC.


## Formatting With A Pattern In `format_str=`

For full control over the output, a CLDR datetime pattern can be given to `format_str=`. In a pattern, runs of letters are fields that are replaced with parts of the datetime, and the length of a run sets the form of that field. Literal text that has letters must be put in single quotes (e.g., `"h 'o''clock' a"`, where `''` is a single quote). Some of the fields are:

| Field | Letters | Output for `2000-02-29 14:35:07` |
|----|----|----|
| year | `y`, `yy` | `"2000"`, `"00"` |
| quarter | `Q`, `QQQ`, `QQQQ` | `"1"`, `"Q1"`, `"1st quarter"` |
| month | `M`, `MM`, `MMM`, `MMMM` | `"2"`, `"02"`, `"Feb"`, `"February"` |
| day of the month | `d`, `dd` | `"29"`, `"29"` |
| day of the week | `E`, `EEEE` | `"Tue"`, `"Tuesday"` |
| hour (1-12) | `h`, `hh` | `"2"`, `"02"` |
| hour (0-23) | `H`, `HH` | `"14"`, `"14"` |
| AM or PM | `a` | `"PM"` |
| period of the day | `B` | `"in the afternoon"` |
| minute | `mm` | `"35"` |
| second | `ss` | `"07"` |
| time zone | `z`, `zzzz`, `xxx` | `"UTC"`, `"Coordinated Universal Time"`, `"+00:00"` |

The full list of fields is in the [CLDR date field symbol table](https://unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table). The generic time zone fields (`v` and `vvvv`, e.g., `"ET"` and `"Eastern Time"` for `America/New_York`) and the location ones (`V` and `VVVV`) fall back to the `z` and `zzzz` forms for a zone without a generic name, as with the time styles. The short GMT offset `O` gives forms like `"GMT-5"`, `"GMT+5:30"` and `"GMT"`, and `g` is the modified Julian day (days since 1858-11-17). The output of a pattern is localized (e.g., `"EEEE, d MMMM y"` gives `"Dienstag, 29 Februar 2000"` with `locale="de"`), though the pattern itself fixes the order of the fields and the punctuation.

A `strftime()` format string can be used instead (any value with `%` is treated as one). Its output isn't localized, so it can't be used together with `locale=`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a simple, two-column table (keeping only the `date` and `time` columns). With the `fmt_datetime()` method, we'll format the `date` column to display dates formatted with the `"month_day_year"` date style and the `time` column to display times formatted with the `"h_m_s_p"` time style.


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
#clbfhirrqn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#clbfhirrqn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#clbfhirrqn p { margin: 0; padding: 0; }
 #clbfhirrqn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #clbfhirrqn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #clbfhirrqn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #clbfhirrqn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #clbfhirrqn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #clbfhirrqn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #clbfhirrqn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #clbfhirrqn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #clbfhirrqn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #clbfhirrqn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #clbfhirrqn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #clbfhirrqn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #clbfhirrqn .gt_spanner_row { border-bottom-style: hidden; }
 #clbfhirrqn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #clbfhirrqn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #clbfhirrqn .gt_from_md> :first-child { margin-top: 0; }
 #clbfhirrqn .gt_from_md> :last-child { margin-bottom: 0; }
 #clbfhirrqn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #clbfhirrqn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #clbfhirrqn .gt_indent_1 { text-indent: 5px; }
 #clbfhirrqn .gt_indent_2 { text-indent: calc(5px * 2); }
 #clbfhirrqn .gt_indent_3 { text-indent: calc(5px * 3); }
 #clbfhirrqn .gt_indent_4 { text-indent: calc(5px * 4); }
 #clbfhirrqn .gt_indent_5 { text-indent: calc(5px * 5); }
 #clbfhirrqn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #clbfhirrqn .gt_row_group_first td { border-top-width: 2px; }
 #clbfhirrqn .gt_row_group_first th { border-top-width: 2px; }
 #clbfhirrqn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #clbfhirrqn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #clbfhirrqn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #clbfhirrqn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #clbfhirrqn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #clbfhirrqn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #clbfhirrqn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #clbfhirrqn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #clbfhirrqn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #clbfhirrqn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #clbfhirrqn .gt_left { text-align: left; }
 #clbfhirrqn .gt_center { text-align: center; }
 #clbfhirrqn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #clbfhirrqn .gt_font_normal { font-weight: normal; }
 #clbfhirrqn .gt_font_bold { font-weight: bold; }
 #clbfhirrqn .gt_font_italic { font-style: italic; }
 #clbfhirrqn .gt_super { font-size: 65%; }
 #clbfhirrqn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #clbfhirrqn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #clbfhirrqn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #clbfhirrqn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #clbfhirrqn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #clbfhirrqn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date                          | time  |
|-------------------------------|-------|
| January 15, 2015 12:00:00 AM  | 13:35 |
| February 15, 2015 12:00:00 AM | 14:40 |
| March 15, 2015 12:00:00 AM    | 15:45 |
| April 15, 2015 12:00:00 AM    | 16:50 |
| May 15, 2015 12:00:00 AM      | 17:55 |
| June 15, 2015 12:00:00 AM     | None  |
| None                          | 19:10 |
| August 15, 2015 12:00:00 AM   | 20:20 |


With a CLDR pattern in `format_str=`, we choose the fields and their order ourselves. The names of the weekdays and months are still localized, here for a table in French.


``` python
(
    GT(exibble_mini, locale="fr")
    .fmt_datetime(columns="date", format_str="EEEE d MMMM y")
)
```


<style>
#jouejkjtlf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jouejkjtlf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jouejkjtlf p { margin: 0; padding: 0; }
 #jouejkjtlf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jouejkjtlf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jouejkjtlf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jouejkjtlf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jouejkjtlf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jouejkjtlf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jouejkjtlf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jouejkjtlf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jouejkjtlf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jouejkjtlf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jouejkjtlf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jouejkjtlf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jouejkjtlf .gt_spanner_row { border-bottom-style: hidden; }
 #jouejkjtlf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jouejkjtlf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jouejkjtlf .gt_from_md> :first-child { margin-top: 0; }
 #jouejkjtlf .gt_from_md> :last-child { margin-bottom: 0; }
 #jouejkjtlf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jouejkjtlf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jouejkjtlf .gt_indent_1 { text-indent: 5px; }
 #jouejkjtlf .gt_indent_2 { text-indent: calc(5px * 2); }
 #jouejkjtlf .gt_indent_3 { text-indent: calc(5px * 3); }
 #jouejkjtlf .gt_indent_4 { text-indent: calc(5px * 4); }
 #jouejkjtlf .gt_indent_5 { text-indent: calc(5px * 5); }
 #jouejkjtlf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jouejkjtlf .gt_row_group_first td { border-top-width: 2px; }
 #jouejkjtlf .gt_row_group_first th { border-top-width: 2px; }
 #jouejkjtlf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jouejkjtlf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jouejkjtlf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jouejkjtlf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jouejkjtlf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jouejkjtlf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jouejkjtlf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jouejkjtlf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jouejkjtlf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jouejkjtlf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jouejkjtlf .gt_left { text-align: left; }
 #jouejkjtlf .gt_center { text-align: center; }
 #jouejkjtlf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jouejkjtlf .gt_font_normal { font-weight: normal; }
 #jouejkjtlf .gt_font_bold { font-weight: bold; }
 #jouejkjtlf .gt_font_italic { font-style: italic; }
 #jouejkjtlf .gt_super { font-size: 65%; }
 #jouejkjtlf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jouejkjtlf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jouejkjtlf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jouejkjtlf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jouejkjtlf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jouejkjtlf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| date                     | time  |
|--------------------------|-------|
| jeudi 15 janvier 2015    | 13:35 |
| dimanche 15 février 2015 | 14:40 |
| dimanche 15 mars 2015    | 15:45 |
| mercredi 15 avril 2015   | 16:50 |
| vendredi 15 mai 2015     | 17:55 |
| lundi 15 juin 2015       | None  |
| None                     | 19:10 |
| samedi 15 août 2015      | 20:20 |
