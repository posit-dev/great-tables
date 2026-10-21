# vals.fmt_datetime()

Format values as datetimes.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_formats_vals.py#L1998-L2102)

``` python
vals.fmt_datetime(
    x,
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

`x: X`  
A list of values to be formatted.

`date_style: DateStyle = "iso"`  
The date style to use. By default this is the short name `"iso"` which corresponds to ISO 8601 date formatting. There are 41 date styles in total.

`time_style: TimeStyle = "iso"`  
The time style to use. By default this is the short name `"iso"` which corresponds to how times are formatted within ISO 8601 datetime values. There are 25 time styles in total.

`format_str: str | None = None`  
A format string to use instead of the preset styles. This can be a CLDR datetime pattern (e.g., `"EEEE, d MMMM y"`), which is localized using `locale=`, or a `strftime()` format string (any string containing `%`, e.g., `"%d.%m.%Y"`), which isn't localized. If `format_str=` is provided, the `date_style=`, `time_style=`, and `sep=` arguments are ignored.

`sep: str = " "`  
A string that separates the date and time components of the datetime string. The default is a space character (`" "`). This is ignored if `format_str=` is provided.

`pattern: str = "{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France). This can't be used with a `strftime()` format string in `format_str=`, since that isn't localized.

## Formatting With The `date_style` And `time_style` Arguments

The date and time parts are formatted separately, with the styles of [`fmt_date()`](../reference/vals.fmt_date.md#great_tables.vals.fmt_date) and [`fmt_time()`](../reference/vals.fmt_time.md#great_tables.vals.fmt_time) (see those for tables of the styles and their output), and joined by `sep=`.

## Formatting With A Pattern In `format_str=`

A CLDR datetime pattern given to `format_str=` sets the fields to show and their order. In a pattern, runs of letters are fields (e.g., `y` for the year, `MMMM` for the month's name, `d` for the day, `EEEE` for the weekday's name, `HH` for the hour, and `mm` for the minute) and literal text with letters must be put in single quotes. See [`GT.fmt_datetime()`](../reference/GT.fmt_datetime.md#great_tables.GT.fmt_datetime) for a table of the most common fields.

## Returns

`list[str]`  
A list of formatted values is returned.

## Examples

``` python
from great_tables import vals

vals.fmt_datetime(
    ["2025-01-01 09:30", "2025-07-14 17:45"],
    date_style="yMMMEd",
    time_style="hm",
)
```

    ['Wed, Jan 1, 2025 9:30 AM', 'Mon, Jul 14, 2025 5:45 PM']

A CLDR pattern in `format_str=` is localized:

``` python
vals.fmt_datetime(
    ["2025-01-01 09:30", "2025-07-14 17:45"],
    format_str="EEEE d MMMM y, HH:mm",
    locale="fr",
)
```

    ['mercredi 1 janvier 2025, 09:30', 'lundi 14 juillet 2025, 17:45']
