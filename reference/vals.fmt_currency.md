## vals.fmt_currency()


Format values as currencies.


Usage

``` python
vals.fmt_currency(
    x,
    currency=None,
    use_subunits=True,
    decimals=None,
    drop_trailing_dec_mark=True,
    accounting=False,
    use_seps=True,
    scale_by=1,
    compact=False,
    pattern="{x}",
    sep_mark=",",
    dec_mark=".",
    force_sign=False,
    placement="left",
    incl_space=False,
    locale=None
)
```


With numeric values, we can perform currency-based formatting with the [val_fmt_currency()](vals.fmt_currency.md#great_tables.vals.fmt_currency) function. This supports both automatic formatting with a three-letter currency code. We have fine control over the conversion from numeric values to currency values, where we could take advantage of the following options:

- the currency: providing a currency code or common currency name will procure the correct currency symbol and number of currency subunits
- currency symbol placement: the currency symbol can be placed before or after the values
- decimals/subunits: choice of the number of decimal places, and a choice of the decimal symbol, and an option on whether to include or exclude the currency subunits (the decimal portion)
- digit grouping separators: options to enable/disable digit separators and provide a choice of separator symbol
- scaling: we can choose to scale targeted values by a multiplier value
- pattern: option to use a text pattern for decoration of the formatted currency values
- locale-based formatting: providing a locale ID will result in currency formatting specific to the chosen locale; it will also retrieve the locale's currency if none is explicitly given


## Parameters


`x: X`  
A list of values to be formatted.

`currency: str | None = None`  
The currency to use for the numeric value. This input can be supplied as a 3-letter currency code (e.g., `"USD"` for U.S. Dollars, `"EUR"` for the Euro currency).

`use_subunits: bool = ``True`  
An option for whether the subunits portion of a currency value should be displayed. For example, with an input value of `273.81`, the default formatting will produce `"$273.81"`. Removing the subunits (with `use_subunits = False`) will give us `"$273"`.

`decimals: int | None = None`  
The `decimals` values corresponds to the exact number of decimal places to use. This value is optional as a currency has an intrinsic number of decimal places (i.e., the subunits). A value such as `2.34` can, for example, be formatted with `0` decimal places and if the currency used is `"USD"` it would result in `"$2"`. With `4` decimal places, the formatted value becomes `"$2.3400"`.

`drop_trailing_dec_mark: bool = ``True`  
A boolean value that determines whether decimal marks should always appear even if there are no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By default trailing decimal marks are not shown.

`accounting: bool = ``False`  
An option to use accounting style for values. Normally, negative values will be shown with a minus sign but using accounting style will instead put any negative values in parentheses.

`use_seps: bool = ``True`  
The `use_seps` option allows for the use of digit group separators. The type of digit group separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This setting is `True` by default.

`scale_by: float = ``1`  
All numeric values will be multiplied by the `scale_by` value before undergoing formatting. Since the `default` value is `1`, no values will be changed unless a different multiplier value is supplied.

`compact: bool = ``False`  
Whether to use compact formatting. This is a boolean value that, when set to `True`, will format large numbers in a more compact form (e.g., `1,000,000` becomes `1M`). This is `False` by default.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`sep_mark: str = ``","`  
The string to use as a separator between groups of digits. For example, using `sep_mark=","` with a value of `1000` would result in a formatted value of `"1,000"`. This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`dec_mark: str = ``"."`  
The string to be used as the decimal mark. For example, using `dec_mark=","` with the value `0.152` would result in a formatted value of `"0,152"`). This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`force_sign: bool = ``False`  
Should the positive sign be shown for positive values (effectively showing a sign for all values except zero)? If so, use `True` for this option. The default is `False`, where only negative numbers will display a minus sign.

`placement: str = ``"left"`  
The placement of the currency symbol. This can be either be `"left"` (as in `"$450"`) or `"right"` (which yields `"450$"`).

`incl_space: bool = ``False`  
An option for whether to include a space between the value and the currency symbol. The default is to not introduce a space character.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Returns


`list[str]`  
A list of formatted values is returned.


## Examples


``` python
from great_tables import vals

vals.fmt_currency([1.02, 3.46], decimals=3)
```


    ['$1.020', '$3.460']
