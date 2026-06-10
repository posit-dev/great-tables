## vals.fmt_date()


Format values as dates.


Usage

``` python
vals.fmt_date(
    x,
    date_style="iso",
    pattern="{x}",
    locale=None,
)
```


Format input values to time values using one of 17 preset date styles. Input can be in the form of `date` type or as a ISO-8601 string (in the form of `YYYY-MM-DD HH:MM:SS` or `YYYY-MM-DD`).


## Parameters


`x: X`  
A list of values to be formatted.

`date_style: DateStyle = ``"iso"`  
The date style to use. By default this is the short name `"iso"` which corresponds to ISO 8601 date formatting. There are 41 date styles in total and their short names can be viewed using `info_date_style()`.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Formatting With The `date_style` Argument

We need to supply a preset date style to the `date_style` argument. The date styles are numerous and can handle localization to any supported locale. The following table provides a listing of all date styles and their output values (corresponding to an input date of `2000-02-29`).

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

We can use the `info_date_style()` function within the console to view a similar table of date styles with example output.


## Returns


`list[str]`  
A list of formatted values is returned.


## Examples


``` python
from great_tables import vals

vals.fmt_date(["2025-01-01", "2025-01-02"], date_style="month_day_year")
```


    ['January 1, 2025', 'January 2, 2025']
