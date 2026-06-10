## GT.fmt_time()


Format values as times.


Usage

``` python
GT.fmt_time(
    columns=None, rows=None, time_style="iso", pattern="{x}", locale=None
)
```


Format input values to time values using one of 5 preset time styles. Input can be in the form of `time` values, or strings in the ISO 8601 forms of `HH:MM:SS` or `YYYY-MM-DD HH:MM:SS`.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`time_style: TimeStyle = ``"iso"`  
The time style to use. By default this is the short name `"iso"` which corresponds to how times are formatted within ISO 8601 datetime values. There are 5 time styles in total.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Formatting With The `time_style=` Argument

We need to supply a preset time style to the `time_style=` argument. The time styles are numerous and can handle localization to any supported locale. The following table provides a listing of all time styles and their output values (corresponding to an input time of `14:35:00`).

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


## Adapting Output To A Specific `locale`

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). Note that a `locale` value provided here will override any global locale setting performed in <a href="GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>'s own `locale` argument (it is settable there as a value received by all other methods that have a `locale` argument).


## Examples

Let's use the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a simple, two-column table (keeping only the `date` and `time` columns). With the [fmt_time()](GT.fmt_time.md#great_tables.GT.fmt_time) method, we'll format the `time` column to display times formatted with the `"h_m_s_p"` time style.


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
| 2015-06-15 |            |
|            | 7:10:00 PM |
| 2015-08-15 | 8:20:00 PM |
