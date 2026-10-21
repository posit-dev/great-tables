# GT.fmt_percent()

Format values as a percentage.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_formats.py#L1752-L1927)

``` python
GT.fmt_percent(
    columns=None,
    rows=None,
    decimals=2,
    drop_trailing_zeros=False,
    drop_trailing_dec_mark=True,
    scale_values=True,
    use_seps=True,
    min_sep_threshold=1,
    accounting=False,
    pattern="{x}",
    sep_mark=",",
    dec_mark=".",
    force_sign=False,
    placement="right",
    incl_space=False,
    locale=None,
)
```

With numeric values in a **gt** table, we can perform percentage-based formatting. It is assumed the input numeric values are proportional values and, in this case, the values will be automatically multiplied by `100` before decorating with a percent sign (the other case is accommodated though setting `scale_values` to `False`). For more control over percentage formatting, we can use the following options:

- percent sign placement: the percent sign can be placed after or before the values and a space can be inserted between the symbol and the value.
- decimals: choice of the number of decimal places, option to drop trailing zeros, and a choice of the decimal symbol
- digit grouping separators: options to enable/disable digit separators and provide a choice of separator symbol
- value scaling toggle: choose to disable automatic value scaling in the situation that values are already scaled coming in (and just require the percent symbol)
- pattern: option to use a text pattern for decoration of the formatted values
- locale-based formatting: providing a locale ID will result in number formatting specific to the chosen locale

## Parameters

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`decimals: int = 2`  
The `decimals` values corresponds to the exact number of decimal places to use. A value such as `2.34` can, for example, be formatted with `0` decimal places and it would result in `"2"`. With `4` decimal places, the formatted value becomes `"2.3400"`. The trailing zeros can be removed with `drop_trailing_zeros=True`.

`drop_trailing_zeros: bool = False`  
A boolean value that allows for removal of trailing zeros (those redundant zeros after the decimal mark).

`drop_trailing_dec_mark: bool = True`  
A boolean value that determines whether decimal marks should always appear even if there are no decimal digits to display after formatting (e.g., `23` becomes `23.` if `False`). By default trailing decimal marks are not shown.

`scale_values: bool = True`  
Should the values be scaled through multiplication by 100? By default this scaling is performed since the expectation is that incoming values are usually proportional. Setting to `False` signifies that the values are already scaled and require only the percent sign when formatted.

`use_seps: bool = True`  
The `use_seps` option allows for the use of digit group separators. The type of digit group separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This setting is `True` by default.

`min_sep_threshold: int = 1`  
The minimum number of digits in the integer part of a number for digit grouping separators to be used. The default of `1` uses separators from 4-digit numbers onward (e.g., `1,000`), `2` starts at 5-digit numbers (`10,000`), and `3` starts at 6-digit numbers (`100,000`). When a locale is in effect (through `locale=` or a locale set in [GT()](../reference/GT.md#great_tables.GT)), the locale's own minimum grouping digits value is used instead (it's `2` for locales like `"es"` and `"pl"`).

`accounting: bool = False`  
Whether to use accounting style, which wraps negative numbers in parentheses instead of using a minus sign.

`pattern: str = "{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`sep_mark: str = ","`  
The string to use as a separator between groups of digits. For example, using `sep_mark=","` with a value of `1000` would result in a formatted value of `"1,000"`. This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`dec_mark: str = "."`  
The string to be used as the decimal mark. For example, using `dec_mark=","` with the value `0.152` would result in a formatted value of `"0,152"`). This argument is ignored if a `locale` is supplied (i.e., is not `None`).

`force_sign: bool = False`  
Should the positive sign be shown for positive values (effectively showing a sign for all values except zero)? If so, use `True` for this option. The default is `False`, where only negative numbers will display a minus sign.

`placement: str = "right"`  
This option governs the placement of the percent sign. This can be either be `"right"` (the default) or `"left"`.

`incl_space: bool = False`  
An option for whether to include a space between the value and the percent sign. The default is to not introduce a space character.

`locale: str | None = None`  
An optional locale identifier that can be used for formatting values according the locale's rules. Examples include `"en"` for English (United States) and `"fr"` for French (France).

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Adapting Output To A Specific `locale`

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). The use of a valid locale ID here means separator and decimal marks will be correct for the given locale. Should any values be provided in `sep_mark` or `dec_mark`, they will be overridden by the locale's preferred values.

Note that a `locale` value provided here will override any global locale setting performed in [`GT()`](../reference/GT.md#great_tables.GT)'s own `locale` argument (it is settable there as a value received by all other methods that have a `locale` argument).

## Examples

Let's use the [towny](../reference/data.towny.md#great_tables.data.towny) dataset as the input table. With the [`fmt_percent()`](../reference/GT.fmt_percent.md#great_tables.GT.fmt_percent) method, we'll format the `pop_change_2016_2021_pct` column to to display values as percentages (to two decimal places).

``` python
from great_tables import GT
from great_tables.data import towny

towny_mini = (
    towny[["name", "pop_change_2016_2021_pct"]]
    .head(10)
)

(GT(towny_mini).fmt_percent("pop_change_2016_2021_pct", decimals=2))
```

| name                   | pop_change_2016_2021_pct |
|------------------------|--------------------------|
| Addington Highlands    | 9.32%                    |
| Adelaide Metcalfe      | 0.70%                    |
| Adjala-Tosorontio      | 0.13%                    |
| Admaston/Bromley       | 2.04%                    |
| Ajax                   | 5.84%                    |
| Alberton               | −1.55%                   |
| Alfred and Plantagenet | 2.78%                    |
| Algonquin Highlands    | 10.08%                   |
| Alnwick/Haldimand      | 8.79%                    |
| Amaranth               | 6.08%                    |
