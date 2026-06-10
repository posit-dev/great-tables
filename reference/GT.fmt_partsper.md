## GT.fmt_partsper()


Format values as parts-per quantities.


Usage

``` python
GT.fmt_partsper(
    columns=None,
    rows=None,
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


With numeric values in a **gt** table, we can format the values so that they are rendered as parts-per quantities (per mille, ppm, ppb, etc.). The following keywords are available for the `to_units` parameter:

- `"per-mille"`: Per mille (1 part in 1,000)
- `"per-myriad"`: Per myriad (1 part in 10,000)
- `"pcm"`: Per cent mille (1 part in 100,000)
- `"ppm"`: Parts per million (1 part in 1,000,000)
- `"ppb"`: Parts per billion (1 part in 1,000,000,000)
- `"ppt"`: Parts per trillion (1 part in 1,000,000,000,000)
- `"ppq"`: Parts per quadrillion (1 part in 1,000,000,000,000,000)

The function provides a lot of formatting control and we can use the following options:

- custom symbol/units: override the automatic symbol or units display with a custom choice
- decimals: choice of the number of decimal places, option to drop trailing zeros, and a choice of the decimal symbol
- digit grouping separators: options to enable/disable digit separators and provide a choice of separator symbol
- value scaling toggle: choose to disable automatic value scaling in the situation that values are already scaled coming in (and just require the appropriate symbol or unit display)
- pattern: option to use a text pattern for decoration of the formatted values
- locale-based formatting: providing a locale ID will result in number formatting specific to the chosen locale


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`to_units: str = ``"per-mille"`  
A keyword that signifies the desired output quantity. This can be any from the following set: `"per-mille"`, `"per-myriad"`, `"pcm"`, `"ppm"`, `"ppb"`, `"ppt"`, or `"ppq"`.

`symbol: str = ``"auto"`  
The symbol/units to use for the quantity. By default, this is set to `"auto"` and the appropriate symbol will be chosen based on the `to_units` keyword and the output context. This can be changed by supplying a string (e.g., using `symbol="ppbV"` when `to_units="ppb"`).

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


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Adapting Output To A Specific `locale`

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). The use of a valid locale ID here means separator and decimal marks will be correct for the given locale. Should any values be provided in `sep_mark` or `dec_mark`, they will be overridden by the locale's preferred values.

Note that a `locale` value provided here will override any global locale setting performed in <a href="GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>'s own `locale` argument (it is settable there as a value received by all other methods that have a `locale` argument).


## Examples

Let's use a small dataset with proportional values and format them as parts-per-mille values.


``` python
from great_tables import GT
import pandas as pd

df = pd.DataFrame({"x": [0.001, 0.0001, 0.00001, 0.5, -0.005]})

GT(df).fmt_partsper(columns="x", to_units="per-mille")
```


| x       |
|---------|
| 1.00‰   |
| 0.10‰   |
| 0.01‰   |
| 500.00‰ |
| −5.00‰  |


We can also format values as parts per million (ppm) using a Polars DataFrame:


``` python
import polars as pl
from great_tables import GT

df = pl.DataFrame({"x": [0.0000015, 0.00035, 0.0001]})

GT(df).fmt_partsper(columns="x", to_units="ppm")
```


| x          |
|------------|
| 1.50 ppm   |
| 350.00 ppm |
| 100.00 ppm |


If the values are already scaled (not proportions), set `scale_values=False` and use a custom symbol:


``` python
import polars as pl
from great_tables import GT

concentrations = pl.DataFrame({"gas": ["CO", "NO2", "O3"], "conc": [1.5, 35.0, 120.0]})

GT(concentrations).fmt_partsper(columns="conc", to_units="ppb", scale_values=False, symbol="ppbV")
```


| gas | conc        |
|-----|-------------|
| CO  | 1.50 ppbV   |
| NO2 | 35.00 ppbV  |
| O3  | 120.00 ppbV |
