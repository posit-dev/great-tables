## vals.fmt_partsper()


Format values as parts-per quantities.


Usage

``` python
vals.fmt_partsper(
    x,
    to_units="per-mille",
    symbol="auto",
    decimals=2,
    drop_trailing_zeros=False,
    drop_trailing_dec_mark=True,
    scale_values=True,
    use_seps=True,
    pattern="{x}",
    sep_mark=",",
    dec_mark=".",
    force_sign=False,
    incl_space="auto",
    locale=None
)
```


With numeric values in a list, we can format the values so that they are rendered as parts-per quantities (per mille, ppm, ppb, etc.). The following keywords are available for the `to_units` parameter:

- `"per-mille"`: Per mille (1 part in 1,000)
- `"per-myriad"`: Per myriad (1 part in 10,000)
- `"pcm"`: Per cent mille (1 part in 100,000)
- `"ppm"`: Parts per million (1 part in 1,000,000)
- `"ppb"`: Parts per billion (1 part in 1,000,000,000)
- `"ppt"`: Parts per trillion (1 part in 1,000,000,000,000)
- `"ppq"`: Parts per quadrillion (1 part in 1,000,000,000,000,000)


## Parameters


`x: X`  
A list of values to be formatted.

`to_units: str = ``"per-mille"`  
A keyword that signifies the desired output quantity. This can be any from the following set: `"per-mille"`, `"per-myriad"`, `"pcm"`, `"ppm"`, `"ppb"`, `"ppt"`, or `"ppq"`.

`symbol: str = ``"auto"`  
The symbol/units to use for the quantity. By default, this is set to `"auto"` and the appropriate symbol will be chosen based on the `to_units` keyword. This can be changed by supplying a string (e.g., using `symbol="ppbV"` when `to_units="ppb"`).

`decimals: int = ``2`  
The `decimals` values corresponds to the exact number of decimal places to use. A value such as `2.34` can, for example, be formatted with `0` decimal places and it would result in `"2"`. With `4` decimal places, the formatted value becomes `"2.3400"`. The trailing zeros can be removed with `drop_trailing_zeros=True`.

`drop_trailing_zeros: bool = ``False`  
A boolean value that allows for removal of trailing zeros (those redundant zeros after the decimal mark).

`drop_trailing_dec_mark: bool = ``True`  
A boolean value that determines whether decimal marks should always appear even if there are no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By default trailing decimal marks are not shown.

`scale_values: bool = ``True`  
Should the values be scaled through multiplication according to the keyword set in `to_units`? By default this is `True` since the expectation is that normally values are proportions. Setting to `False` signifies that the values are already scaled and require only the appropriate symbol/units when formatted.

`use_seps: bool = ``True`  
The `use_seps` option allows for the use of digit group separators. The type of digit group separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This setting is `True` by default.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`sep_mark: str = ``","`  
The string to use as a separator between groups of digits. For example, using `sep_mark=","` with a value of `1000` would result in a formatted value of `"1,000"`. This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`dec_mark: str = ``"."`  
The string to be used as the decimal mark. For example, using `dec_mark=","` with the value `0.152` would result in a formatted value of `"0,152"`). This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`force_sign: bool = ``False`  
Should the positive sign be shown for positive values (effectively showing a sign for all values except zero)? If so, use `True` for this option. The default is `False`, where only negative numbers will display a minus sign.

`incl_space: str | bool = ``"auto"`  
An option for whether to include a space between the value and the symbol/units. The default is `"auto"` which provides spacing dependent on the mark itself (symbols like `‰` get no space; text abbreviations like `ppm` get a space). This can be directly controlled by using either `True` or `False`.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Returns


`list[str]`  
A list of formatted values is returned.


## Examples


``` python
from great_tables import vals

vals.fmt_partsper([0.001, 0.0001], to_units="per-mille")
```


    ['1.00‰', '0.10‰']


``` python
from great_tables import vals

vals.fmt_partsper([0.0000015, 0.00035], to_units="ppm")
```


    ['1.50 ppm', '350.00 ppm']
