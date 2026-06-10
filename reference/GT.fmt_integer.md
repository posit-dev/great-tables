## GT.fmt_integer()


Format values as integers.


Usage

``` python
GT.fmt_integer(
    columns=None,
    rows=None,
    use_seps=True,
    scale_by=1,
    accounting=False,
    compact=False,
    pattern="{x}",
    sep_mark=",",
    force_sign=False,
    locale=None
)
```


With numeric values in one or more table columns, we can perform number-based formatting so that the targeted values are always rendered as integer values.

We can have fine control over integer formatting with the following options:

- digit grouping separators: options to enable/disable digit separators and provide a choice of separator symbol
- scaling: we can choose to scale targeted values by a multiplier value
- large-number suffixing: larger figures (thousands, millions, etc.) can be autoscaled and decorated with the appropriate suffixes
- pattern: option to use a text pattern for decoration of the formatted values
- locale-based formatting: providing a locale ID will result in number formatting specific to the chosen locale


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`use_seps: bool = ``True`  
The `use_seps` option allows for the use of digit group separators. The type of digit group separator is set by `sep_mark` and overridden if a locale ID is provided to `locale`. This setting is `True` by default.

`scale_by: float = ``1`  
All numeric values will be multiplied by the `scale_by` value before undergoing formatting. Since the `default` value is `1`, no values will be changed unless a different multiplier value is supplied.

`accounting: bool = ``False`  
Whether to use accounting style, which wraps negative numbers in parentheses instead of using a minus sign.

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


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Adapting Output To A Specific `locale`

This formatting method can adapt outputs according to a provided `locale` value. Examples include `"en"` for English (United States) and `"fr"` for French (France). The use of a valid locale ID here means separator marks will be correct for the given locale. Should any value be provided in `sep_mark`, it will be overridden by the locale's preferred value.

Note that a `locale` value provided here will override any global locale setting performed in <a href="GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>'s own `locale` argument (it is settable there as a value received by all other methods that have a `locale` argument).


## Examples

For this example, we'll use the [exibble](data.exibble.md#great_tables.data.exibble) dataset as the input table. With the [fmt_integer()](GT.fmt_integer.md#great_tables.GT.fmt_integer) method, we'll format the `num` column as integer values having no digit separators (with the `use_seps=False` option).


``` python
from great_tables import GT, exibble

(
    GT(exibble)
    .fmt_integer(columns="num", use_seps=False)
)
```


| num     | char       | fctr  | date       | time  | datetime         | currency | row   | group |
|---------|------------|-------|------------|-------|------------------|----------|-------|-------|
| 0       | apricot    | one   | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95    | row_1 | grp_a |
| 2       | banana     | two   | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95    | row_2 | grp_a |
| 33      | coconut    | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39     | row_3 | grp_a |
| 444     | durian     | four  | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0  | row_4 | grp_a |
| 5550    |            | five  | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81  | row_5 | grp_b |
|         | fig        | six   | 2015-06-15 |       | 2018-06-06 16:11 | 13.255   | row_6 | grp_b |
| 777000  | grapefruit | seven |            | 19:10 | 2018-07-07 05:22 |          | row_7 | grp_b |
| 8880000 | honeydew   | eight | 2015-08-15 | 20:20 |                  | 0.44     | row_8 | grp_b |
