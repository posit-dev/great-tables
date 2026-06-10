## vals.fmt_time()


Format values as times.


Usage

``` python
vals.fmt_time(
    x,
    time_style="iso",
    pattern="{x}",
    locale=None,
)
```


Format input values to time values using one of 5 preset time styles. Input can be in the form of `time` values, or strings in the ISO 8601 forms of `HH:MM:SS` or `YYYY-MM-DD HH:MM:SS`.


## Parameters


`x: X`  
A list of values to be formatted.

`time_style: TimeStyle = ``"iso"`  
The time style to use. By default this is the short name `"iso"` which corresponds to how times are formatted within ISO 8601 datetime values. There are 5 time styles in total and their short names can be viewed using `info_time_style()`.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Formatting With The `time_style` Argument

We need to supply a preset time style to the `time_style` argument. The time styles are numerous and can handle localization to any supported locale. The following table provides a listing of all time styles and their output values (corresponding to an input time of `14:35:00`).

|     | Time Style    | Output         | Notes         |
|-----|---------------|----------------|---------------|
| 1   | `"iso"`       | `"14:35:00"`   | ISO 8601, 24h |
| 2   | `"iso-short"` | `"14:35"`      | ISO 8601, 24h |
| 3   | `"h_m_s_p"`   | `"2:35:00 PM"` | 12h           |
| 4   | `"h_m_p"`     | `"2:35 PM"`    | 12h           |
| 5   | `"h_p"`       | `"2 PM"`       | 12h           |

We can use the `info_time_style()` function within the console to view a similar table of time styles with example output.


## Returns


`list[str]`  
A list of formatted values is returned.


## Examples


``` python
from great_tables import vals

vals.fmt_time(["05:32:17", "13:01:02"], time_style="h_m_s_p")
```


    ['5:32:17 AM', '1:01:02 PM']
