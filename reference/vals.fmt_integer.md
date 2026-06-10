## vals.fmt_integer()


Format values as integers.


Usage

``` python
vals.fmt_integer(
    x,
    use_seps=True,
    accounting=False,
    scale_by=1,
    compact=False,
    pattern="{x}",
    sep_mark=",",
    force_sign=False,
    locale=None
)
```


With numeric values in a list, we can perform number-based formatting so that the input values are always rendered as integer values. The following major options are available:

We can have fine control over integer formatting with the following options:

- digit grouping separators: options to enable/disable digit separators and provide a choice of separator symbol
- scaling: we can choose to scale targeted values by a multiplier value
- large-number suffixing: larger figures (thousands, millions, etc.) can be autoscaled and decorated with the appropriate suffixes
- pattern: option to use a text pattern for decoration of the formatted values
- locale-based formatting: providing a locale ID will result in number formatting specific to the chosen locale


## Parameters


`x: X`  
A list of values to be formatted.

`use_seps: bool = ``True`  
The `use_seps` option allows for the use of digit group separators. The type of digit group separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This setting is `True` by default.

`accounting: bool = ``False`  
An option to use accounting style for values. Normally, negative values will be shown with a minus sign but using accounting style will instead put any negative values in parentheses.

`scale_by: float = ``1`  
All numeric values will be multiplied by the `scale_by` value before undergoing formatting. Since the `default` value is `1`, no values will be changed unless a different multiplier value is supplied.

`compact: bool = ``False`  
A boolean value that allows for compact formatting of numeric values. Values will be scaled and decorated with the appropriate suffixes (e.g., `1230` becomes `1K`, and `1230000` becomes `1M`). The `compact` option is `False` by default.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`sep_mark: str = ``","`  
The string to use as a separator between groups of digits. For example, using `sep_mark=","` with a value of `1000` would result in a formatted value of `"1,000"`. This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`force_sign: bool = ``False`  
Should the positive sign be shown for positive values (effectively showing a sign for all values except zero)? If so, use `True` for this option. The default is `False`, where only negative numbers will display a minus sign.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Returns


`list[str]`  
A list of formatted values is returned.


## Examples


``` python
from great_tables import vals

vals.fmt_integer([100000.1, 2000000000.2], use_seps=False)
```


    ['100000', '2000000000']
