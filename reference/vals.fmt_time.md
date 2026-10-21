# vals.fmt_time()

Format values as times.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_formats_vals.py#L1895-L1995)

``` python
vals.fmt_time(
    x,
    time_style="iso",
    pattern="{x}",
    locale=None,
)
```

Format input values to time values using one of 25 preset time styles. Input can be in the form of `time` values, or strings in the ISO 8601 forms of `HH:MM:SS` or `YYYY-MM-DD HH:MM:SS`.

## Parameters

`x: X`  
A list of values to be formatted.

`time_style: TimeStyle = "iso"`  
The time style to use. By default this is the short name `"iso"` which corresponds to how times are formatted within ISO 8601 datetime values. There are 25 time styles in total.

`pattern: str = "{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).

## Formatting With The `time_style` Argument

We need to supply a preset time style to the `time_style` argument. The time styles are numerous and can handle localization to any supported locale. Those termed flexible adapt their output to any `locale=` provided. The following table provides a listing of all time styles and their output values (corresponding to an input of `2000-02-29 14:35:00`).

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

`list[str]`  
A list of formatted values is returned.

## Examples

``` python
from great_tables import vals

vals.fmt_time(["05:32:17", "13:01:02"], time_style="h_m_s_p")
```

    ['5:32:17 AM', '1:01:02 PM']
