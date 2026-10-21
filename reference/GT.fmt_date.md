# GT.fmt_date()

Format values as dates.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_formats.py#L5284-L5439)

``` python
GT.fmt_date(
    columns=None,
    rows=None,
    date_style="iso",
    pattern="{x}",
    locale=None,
)
```

Format input values to date values using one of 41 preset date styles. Input can be in the form of `date` type or as a ISO-8601 string (in the form of `YYYY-MM-DD HH:MM:SS` or `YYYY-MM-DD`).

## Parameters

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`date_style: DateStyle = "iso"`  
The date style to use. By default this is the short name `"iso"` which corresponds to ISO 8601 date formatting. There are 41 date styles in total.

`pattern: str = "{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).

## Formatting With The `date_style=` Argument

We need to supply a preset date style to the `date_style=` argument. The date styles are numerous and can handle localization to any supported locale. A large segment of date styles are termed flexible date formats and this means that their output will adapt to any `locale=` provided: the order of the fields, the punctuation, and even which fields are abbreviated follow the locale's conventions (e.g., `"yMMMd"` is `"Feb 29, 2000"` in English and `"29. Feb. 2000"` in German). That feature makes the flexible date formats a better option for locales other than `"en"` (the default locale).

The following table provides a listing of all date styles and their output values (corresponding to an input date of `2000-02-29`).

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

The names of the flexible date styles are CLDR skeletons, where each letter stands for a field: `G` is the era, `y` the year, `Q` the quarter, `M` the month, `d` the day of the month, and `E` the day of the week. A longer run of `Q`, `M`, or `E` gives a longer form of that field.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Adapting Output To A Specific `locale`

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). Note that a `locale` value provided here will override any global locale setting performed in [`GT()`](../reference/GT.md#great_tables.GT)'s own `locale` argument (it is settable there as a value received by all other methods that have a `locale` argument).

## Examples

Let's use the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset to create a simple, two-column table (keeping only the `date` and `time` columns). With the [`fmt_date()`](../reference/GT.fmt_date.md#great_tables.GT.fmt_date) method, we'll format the `date` column to display dates formatted with the `"month_day_year"` date style.

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
| June 15, 2015     | None  |
| None              | 19:10 |
| August 15, 2015   | 20:20 |

A flexible date style adapts to the locale. Here, the `"yMMMEd"` style is used to format the dates for a table in German.

``` python
(
    GT(exibble_mini, locale="de")
    .fmt_date(columns="date", date_style="yMMMEd")
)
```

| date               | time  |
|--------------------|-------|
| Do., 15. Jan. 2015 | 13:35 |
| So., 15. Feb. 2015 | 14:40 |
| So., 15. März 2015 | 15:45 |
| Mi., 15. Apr. 2015 | 16:50 |
| Fr., 15. Mai 2015  | 17:55 |
| Mo., 15. Juni 2015 | None  |
| None               | 19:10 |
| Sa., 15. Aug. 2015 | 20:20 |
