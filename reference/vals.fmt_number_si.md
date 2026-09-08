# vals.fmt_number_si()


Format values with SI (metric) prefixes.


Usage

``` python
vals.fmt_number_si(
    x,
    unit=None,
    decimals=2,
    n_sigfig=None,
    drop_trailing_zeros=False,
    drop_trailing_dec_mark=True,
    scale_by=1,
    prefix_mode="engineering",
    pattern="{x}",
    sep_mark=",",
    dec_mark=".",
    force_sign=False,
    incl_space=True,
    locale=None,
)
```


Format numeric values with SI (International System of Units) prefixes, automatically selecting the appropriate prefix to keep the mantissa in a readable range. SI prefixes range from quetta (Q, 10^30) to quecto (q, 10^-30) and are commonly used in scientific and engineering contexts to represent very large or very small quantities with units (e.g., `"5.2 kW"`, `"3.8 ng"`, `"1.2 GHz"`, etc.).


## Parameters


`x: X`  
A list of values to be formatted.

`unit: str | None = None`  
A character string specifying the unit to append after the SI prefix (e.g., `"g"` for grams, `"W"` for watts, `"Hz"` for hertz, `"m"` for meters). If `None`, only the prefix will be shown.

`decimals: int = ``2`  
The `decimals` values corresponds to the exact number of decimal places to use. A value such as `2.34` can, for example, be formatted with `0` decimal places and it would result in `"2"`. With `4` decimal places, the formatted value becomes `"2.3400"`. The trailing zeros can be removed with `drop_trailing_zeros=True`. If `n_sigfig` is provided, `decimals` is ignored.

`n_sigfig: int | None = None`  
A option to format numbers to *n* significant figures. By default, this is `None` and thus number values will be formatted according to the number of decimal places set via `decimals=`. If opting to format according to the rules of significant figures, `n_sigfig=` must be a number greater than or equal to `1`. Any values passed to the `decimals=` and `drop_trailing_zeros=` arguments will be ignored.

`drop_trailing_zeros: bool = ``False`  
A boolean value that allows for removal of trailing zeros (those redundant zeros after the decimal mark).

`drop_trailing_dec_mark: bool = ``True`  
A boolean value that determines whether decimal marks should always appear even if there are no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By default trailing decimal marks are not shown.

`scale_by: float = ``1`  
All numeric values will be multiplied by the `scale_by` value before undergoing formatting. Since the `default` value is `1`, no values will be changed unless a different multiplier value is supplied. This is useful for unit conversions (e.g., converting metric tons to grams by using `scale_by=1_000_000`).

`prefix_mode: str = ``"engineering"`  
The type of SI prefixes to use. Use `"engineering"` (the default) for prefixes that correspond to powers of 1000 only. Use `"decimal"` to include all SI prefixes (also those for powers of 10 and 100).

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`sep_mark: str = ``","`  
The string to use as a separator between groups of digits.

`dec_mark: str = ``"."`  
The string to be used as the decimal mark.

`force_sign: bool = ``False`  
Should the positive sign be shown for positive values (effectively showing a sign for all values except zero)? If so, use `True` for this option.

`incl_space: bool = ``True`  
An option for whether to include a space between the numerical value and the SI prefix + unit (e.g., `True` for `"1.5 kW"`, `False` for `"1.5kW"`). Per SI convention, there should be a space between the value and the unit symbol. The default is `True`.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France). When provided, overrides `sep_mark` and `dec_mark` with locale-appropriate values.


## Returns


`list[str]`  
A list of formatted values is returned.


## Examples

Let's format a vector of numeric values with SI prefixes.


``` python
from great_tables import vals

vals.fmt_number_si([1.5e9, 2.7e6, 4200, 0.3, 0.00012, 2.4e-8])
```


    ['1.50 G', '2.70 M', '4.20 k', '300.00 m', '120.00 µ', '24.00 n']


We can add a unit designation to show what the values represent (e.g., watts).


``` python
vals.fmt_number_si([1.5e9, 2.7e6, 4200], unit="W")
```


    ['1.50 GW', '2.70 MW', '4.20 kW']


The `scale_by` option is useful for unit conversions. For instance, to convert metric tons to grams before formatting:


``` python
vals.fmt_number_si([455, 331, 235, 30], unit="g", scale_by=1_000_000, decimals=0)
```


    ['455 Mg', '331 Mg', '235 Mg', '30 Mg']


We can control the space between the number and unit with `incl_space`.


``` python
vals.fmt_number_si([2.4e9, 5.0e9, 900e6], unit="Hz", incl_space=False, decimals=1)
```


    ['2.4GHz', '5.0GHz', '900.0MHz']
