# vals.fmt_number()

Format numeric values.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_formats_vals.py#L112-L259)

``` python
vals.fmt_number(
    x,
    decimals=2,
    n_sigfig=None,
    drop_trailing_zeros=False,
    drop_trailing_dec_mark=True,
    use_seps=True,
    accounting=False,
    scale_by=1,
    compact=False,
    pattern="{x}",
    sep_mark=",",
    dec_mark=".",
    force_sign=False,
    min_sep_threshold=1,
    locale=None,
    system="intl",
)
```

With numeric values in a list, we can perform number-based formatting so that the values are rendered with some level of precision. The following major options are available:

- decimals: choice of the number of decimal places, option to drop trailing zeros, and a choice of the decimal symbol
- digit grouping separators: options to enable/disable digit separators and provide a choice of separator symbol
- scaling: we can choose to scale targeted values by a multiplier value
- large-number suffixing: larger figures (thousands, millions, etc.) can be autoscaled and decorated with the appropriate suffixes
- pattern: option to use a text pattern for decoration of the formatted values
- locale-based formatting: providing a locale ID will result in number formatting specific to the chosen locale

## Parameters

`x: X`  
A list of values to be formatted.

`decimals: int = 2`  
The `decimals` values corresponds to the exact number of decimal places to use. A value such as `2.34` can, for example, be formatted with `0` decimal places and it would result in `"2"`. With `4` decimal places, the formatted value becomes `"2.3400"`. The trailing zeros can be removed with `drop_trailing_zeros=True`. If you always need `decimals = 0`, the [`val_fmt_integer()`](../reference/vals.fmt_integer.md#great_tables.vals.fmt_integer) function should be considered.

`n_sigfig: int | None = None`  
A option to format numbers to *n* significant figures. By default, this is `None` and thus number values will be formatted according to the number of decimal places set via `decimals`. If opting to format according to the rules of significant figures, `n_sigfig` must be a number greater than or equal to `1`. Any values passed to the `decimals` and `drop_trailing_zeros` arguments will be ignored.

`drop_trailing_zeros: bool = False`  
A boolean value that allows for removal of trailing zeros (those redundant zeros after the decimal mark).

`drop_trailing_dec_mark: bool = True`  
A boolean value that determines whether decimal marks should always appear even if there are no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By default trailing decimal marks are not shown.

`use_seps: bool = True`  
The `use_seps` option allows for the use of digit group separators. The type of digit group separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This setting is `True` by default.

`accounting: bool = False`  
An option to use accounting style for values. Normally, negative values will be shown with a minus sign but using accounting style will instead put any negative values in parentheses.

`scale_by: float = 1`  
All numeric values will be multiplied by the `scale_by` value before undergoing formatting. Since the `default` value is `1`, no values will be changed unless a different multiplier value is supplied.

`compact: bool = False`  
A boolean value that allows for compact formatting of numeric values. Values will be scaled and decorated with the appropriate suffixes (e.g., `1230` becomes `1.23K`, and `1230000` becomes `1.23M`). The `compact` option is `False` by default. With `system="ind"`, values are expressed in lakhs and crores instead (e.g., `1234567` becomes `12.35 Lac`).

`pattern: str = "{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`sep_mark: str = ","`  
The string to use as a separator between groups of digits. For example, using `sep_mark=","` with a value of `1000` would result in a formatted value of `"1,000"`. This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`dec_mark: str = "."`  
The string to be used as the decimal mark. For example, using `dec_mark=","` with the value `0.152` would result in a formatted value of `"0,152"`). This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`force_sign: bool = False`  
Should the positive sign be shown for positive values (effectively showing a sign for all values except zero)? If so, use `True` for this option. The default is `False`, where only negative numbers will display a minus sign.

`min_sep_threshold: int = 1`  
The minimum number of digits in the integer part of a number for digit grouping separators to be used. The default of `1` uses separators from 4-digit numbers onward (e.g., `1,000`), `2` starts at 5-digit numbers (`10,000`), and `3` starts at 6-digit numbers (`100,000`). When a `locale=` value is provided, the locale's own minimum grouping digits value is used instead (it's `2` for locales like `"es"` and `"pl"`).

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).

`system: NumberSystem = "intl"`  
The numbering system to use for digit grouping. The international numbering system (`"intl"`, the default) always separates groups of three digits (e.g., `"1,234,567"`). The Indian numbering system (`"ind"`) separates the last three digits and then groups of two, which correspond to thousands, lakhs, crores, and higher quantities (e.g., `"12,34,567"`). The separator itself is still set by `sep_mark=` (or the locale) and can be turned off with `use_seps=False`.

## Returns

`list[str]`  
A list of formatted values is returned.

## Examples

``` python
from great_tables import vals

vals.fmt_number([0.325, 777000], decimals=2)
```

    ['0.33', '777,000.00']
