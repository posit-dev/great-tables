## GT.fmt_date()


Format values as dates.


Usage

``` python
GT.fmt_date(
    columns=None, rows=None, date_style="iso", pattern="{x}", locale=None
)
```


Format input values to time values using one of 17 preset date styles. Input can be in the form of `date` type or as a ISO-8601 string (in the form of `YYYY-MM-DD HH:MM:SS` or `YYYY-MM-DD`).


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`date_style: DateStyle = ``"iso"`  
The date style to use. By default this is the short name `"iso"` which corresponds to ISO 8601 date formatting. There are 41 date styles in total.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Formatting With The `date_style=` Argument

We need to supply a preset date style to the `date_style=` argument. The date styles are numerous and can handle localization to any supported locale. The following table provides a listing of all date styles and their output values (corresponding to an input date of `2000-02-29`).

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


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Adapting Output To A Specific `locale`

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). Note that a `locale` value provided here will override any global locale setting performed in <a href="GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>'s own `locale` argument (it is settable there as a value received by all other methods that have a `locale` argument).


## Examples

Let's use the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a simple, two-column table (keeping only the `date` and `time` columns). With the [fmt_date()](GT.fmt_date.md#great_tables.GT.fmt_date) method, we'll format the `date` column to display dates formatted with the `"month_day_year"` date style.


``` python
from great_tables import GT, exibble

exibble_mini = exibble[["date", "time"]]

(
    GT(exibble_mini)
    .fmt_date(columns="date", date_style="month_day_year")
)
```


| date              | time  |
|-------------------|-------|
| January 15, 2015  | 13:35 |
| February 15, 2015 | 14:40 |
| March 15, 2015    | 15:45 |
| April 15, 2015    | 16:50 |
| May 15, 2015      | 17:55 |
| June 15, 2015     |       |
|                   | 19:10 |
| August 15, 2015   | 20:20 |
