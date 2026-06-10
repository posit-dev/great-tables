## GT.fmt_bytes()


Format values as bytes.


Usage

``` python
GT.fmt_bytes(
    columns=None,
    rows=None,
    standard="decimal",
    decimals=1,
    n_sigfig=None,
    drop_trailing_zeros=True,
    drop_trailing_dec_mark=True,
    use_seps=True,
    pattern="{x}",
    sep_mark=",",
    dec_mark=".",
    force_sign=False,
    incl_space=True,
    locale=None
)
```


With numeric values in a table, we can transform those to values of bytes with human readable units. The [fmt_bytes()](GT.fmt_bytes.md#great_tables.GT.fmt_bytes) method allows for the formatting of byte sizes to either of two common representations: (1) with decimal units (powers of 1000, examples being `"kB"` and `"MB"`), and (2) with binary units (powers of 1024, examples being `"KiB"` and `"MiB"`). It is assumed the input numeric values represent the number of bytes and automatic truncation of values will occur. The numeric values will be scaled to be in the range of 1 to \<1000 and then decorated with the correct unit symbol according to the standard chosen. For more control over the formatting of byte sizes, we can use the following options:

- decimals: choice of the number of decimal places, option to drop trailing zeros, and a choice of the decimal symbol
- digit grouping separators: options to enable/disable digit separators and provide a choice of separator symbol
- pattern: option to use a text pattern for decoration of the formatted values
- locale-based formatting: providing a locale ID will result in number formatting specific to the chosen locale


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`standard: str = ``"decimal"`  
The form of expressing large byte sizes is divided between: (1) decimal units (powers of 1000; e.g., `"kB"` and `"MB"`), and (2) binary units (powers of 1024; e.g., `"KiB"` and `"MiB"`). The default is to use decimal units with the `"decimal"` option. The alternative is to use binary units with the `"binary"` option.

`decimals: int = ``1`  
This corresponds to the exact number of decimal places to use. A value such as `2.34` can, for example, be formatted with `0` decimal places and it would result in `"2"`. With `4` decimal places, the formatted value becomes `"2.3400"`. The trailing zeros can be removed with `drop_trailing_zeros=True`.

`drop_trailing_zeros: bool = ``True`  
A boolean value that allows for removal of trailing zeros (those redundant zeros after the decimal mark).

`drop_trailing_dec_mark: bool = ``True`  
A boolean value that determines whether decimal marks should always appear even if there are no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By default trailing decimal marks are not shown.

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

`incl_space: bool = ``True`  
An option for whether to include a space between the value and the currency symbol. The default is to not introduce a space character.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Adapting Output To A Specific `locale`

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). The use of a valid locale ID here means separator and decimal marks will be correct for the given locale. Should any values be provided in `sep_mark` or `dec_mark`, they will be overridden by the locale's preferred values.

Note that a `locale` value provided here will override any global locale setting performed in <a href="GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>'s own `locale` argument (it is settable there as a value received by all other methods that have a `locale` argument).


## Examples

Let's use a single column from the [exibble](data.exibble.md#great_tables.data.exibble) dataset and create a new table. We'll format the `num` column to display as byte sizes in the decimal standard through use of the [fmt_bytes()](GT.fmt_bytes.md#great_tables.GT.fmt_bytes) method.


``` python
from great_tables import GT, exibble

(
    GT(exibble[["num"]])
    .fmt_bytes(columns="num", standard="decimal")
)
```


| num    |
|--------|
| 0 B    |
| 2 B    |
| 33 B   |
| 444 B  |
| 5.5 kB |
|        |
| 777 kB |
| 8.9 MB |
