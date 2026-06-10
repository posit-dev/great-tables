## GT.fmt_datetime()


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
