# GT.fmt_time()

Format values as times.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_formats.py#L5473-L5621)

``` python
GT.fmt_time(
    columns=None,
    rows=None,
    time_style="iso",
    pattern="{x}",
    locale=None,
)
```

Format input values to time values using one of 25 preset time styles. Input can be in the form of `time` values, or strings in the ISO 8601 forms of `HH:MM:SS` or `YYYY-MM-DD HH:MM:SS`. For `datetime` values (and datetime strings), the time part is formatted. Dates without a time (e.g., `"2024-01-05"`) raise an error; use [`fmt_date()`](../reference/GT.fmt_date.md#great_tables.GT.fmt_date) for those.

## Parameters

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`time_style: TimeStyle = "iso"`  
The time style to use. By default this is the short name `"iso"` which corresponds to how times are formatted within ISO 8601 datetime values. There are 25 time styles in total.

`pattern: str = "{x}"`  
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

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). Note that a `locale` value provided here will override any global locale setting performed in [`GT()`](../reference/GT.md#great_tables.GT)'s own `locale` argument (it is settable there as a value received by all other methods that have a `locale` argument).

## Examples

Let's use the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset to create a simple, two-column table (keeping only the `date` and `time` columns). With the [`fmt_time()`](../reference/GT.fmt_time.md#great_tables.GT.fmt_time) method, we'll format the `time` column to display times formatted with the `"h_m_s_p"` time style.

``` python
from great_tables import GT, exibble

exibble_mini = exibble[["date", "time"]]

(
    GT(exibble_mini)
    .fmt_time(columns="time", time_style="h_m_s_p")
)
```

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
