## vals.fmt_duration()


Format values as time duration strings.


Usage

``` python
vals.fmt_duration(
    x,
    input_units=None,
    output_units=None,
    duration_style="narrow",
    trim_zero_units=True,
    max_output_units=None,
    pattern="{x}",
    use_seps=True,
    sep_mark=",",
    force_sign=False,
    locale=None
)
```


With numeric values in a list, we can transform those to values of time duration with various human readable styles. The [val_fmt_duration()](vals.fmt_duration.md#great_tables.vals.fmt_duration) function allows for formatting of duration values to narrow, wide, colon-separated, and ISO 8601 forms.


## Parameters


`x: X`  
A list of numeric values to be formatted as durations.

`input_units: str | None = None`  
The time units of the input numeric values. Required for numeric input. The accepted units are: `"seconds"`, `"minutes"`, `"hours"`, `"days"`, and `"weeks"`.

`output_units: 'str | list[str] | None' = None`  
Controls the output time units. The default (`None`) means that output units will be automatically chosen. Can be a list of keywords from: `"weeks"`, `"days"`, `"hours"`, `"minutes"`, or `"seconds"`.

`duration_style: str = ``"narrow"`  
Style for representing duration values. One of `"narrow"` (default, e.g., `"1d 8h 24m"`), `"wide"` (e.g., `"1 day 8 hours 24 minutes"`), `"colon-sep"` (e.g., `"1/08:24:00"`), or `"iso"` (e.g., `"P1DT8H24M"`).

`trim_zero_units: 'bool | list[str]' = ``True`  
Provides methods to remove output time units that have zero values. By default this is `True`. Can also be a list of `"leading"`, `"trailing"`, and/or `"internal"`.

`max_output_units: int | None = None`  
Maximum number of time units to display. By default (`None`), all possible time units will be displayed.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value.

`use_seps: bool = ``True`  
Whether to use digit group separators.

`sep_mark: str = ``","`  
The string to use as a separator between groups of digits.

`force_sign: bool = ``False`  
Should the positive sign be shown for positive values?

`locale: str | None = None`  
An optional locale identifier for formatting values.


## Returns


`list[str]`  
A list of formatted values is returned.


## Examples


``` python
from great_tables import vals

vals.fmt_duration([3661, 86400, 172800], input_units="seconds")
```


    ['1h 1m 1s', '1d', '2d']
