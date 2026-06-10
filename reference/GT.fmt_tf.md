## GT.fmt_tf()


Format True and False values


Usage

``` python
GT.fmt_tf(
    columns=None,
    rows=None,
    tf_style="true-false",
    pattern="{x}",
    true_val=None,
    false_val=None,
    na_val=None,
    colors=None
)
```


There can be times where boolean values are useful in a display table. You might want to express a 'yes' or 'no', a 'true' or 'false', or, perhaps use pairings of complementary symbols that make sense in a table. The [fmt_tf()](GT.fmt_tf.md#great_tables.GT.fmt_tf) method has a set of `tf_style=` presets that can be used to quickly map `True`/`False` values to strings, or, symbols like up/down or left/right arrows and open/closed shapes.

While the presets are nice, you can provide your own mappings through the `true_val=` and `false_val=` arguments. For extra customization, you can also apply color to the individual `True`, `False`, and NA mappings. Just supply a list of colors (up to a length of 3) to the `colors=` argument.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`tf_style: str = ``"true-false"`  
The `True`/`False` mapping style to use. By default this is the short name `"true-false"` which corresponds to the words `"true"` and `"false"`. Two other `tf_style=` values produce words: `"yes-no"` and `"up-down"`. The remaining options involve pairs of symbols (e.g., `"check-mark"` displays a check mark for `True` and an ✗ symbol for `False`).

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

`true_val: str | None = None`  
While the choice of a `tf_style=` will typically supply the `true_val=` and `false_val=` text, we could override this and supply text for any `True` values. This doesn't need to be used in conjunction with `false_val=`.

`false_val: str | None = None`  
While the choice of a `tf_style=` will typically supply the `true_val=` and `false_val=` text, we could override this and supply text for any `False` values. This doesn't need to be used in conjunction with `true_val=`.

`na_val: str | None = None`  
None of the `tf_style` presets will replace any missing values encountered in the targeted cells. While we always have the option to use [sub_missing()](GT.sub_missing.md#great_tables.GT.sub_missing) for NA replacement, we have the opportunity handle missing values here with the `na_val=` option. This is useful because we also have the means to add color to the `na_val=` text or symbol and doing that requires that a replacement value for NAs is specified here.

`colors: list[str] | None = None`  
Providing a list of color values to colors will progressively add color to the formatted result depending on the number of colors provided. With a single color, all formatted values will be in that color. Using two colors results in `True` values being the first color, and `False` values receiving the second. With the three-color option, the final color will be given to any missing values replaced through `na_val=`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Formatting With The `tf_style=` Argument

We need to supply a preset `tf_style=` value. The following table provides a listing of all `tf_style=` values and their output `True` and `False` values.

|     | TF Style       | Output                                              |
|-----|----------------|-----------------------------------------------------|
| 1   | `"true-false"` | `"true" /`"false"`| | 2 |`"yes-no"`|`"yes" / `"no"` |
| 3   | `"up-down"`    | `"up" /`"down"`| | 4 |`"check-mark"`|`"✓" / `"✗"`   |
| 5   | `"circles"`    | `"●" /`"○"`| | 6 |`"squares"`|`"■" / `"□"`          |
| 7   | `"diamonds"`   | `"◆" /`"◇"`| | 8 |`"arrows"`|`"↑" / `"↓"`           |
| 9   | `"triangles"`  | `"▲" /`"▼"`| | 10 |`"triangles-lr"`|`"▶" / `"◀"`    |


## Examples

Let's use a subset of the [sp500](data.sp500.md#great_tables.data.sp500) dataset to create a small table containing opening and closing price data for the last few days in 2015. We added a boolean column (`dir`) where `True` indicates a price increase from opening to closing and `False` is the opposite. Using [fmt_tf()](GT.fmt_tf.md#great_tables.GT.fmt_tf) generates up and down arrows in the `dir` column. We elect to use green upward arrows and red downward arrows (through the `colors=` option).


``` python
from great_tables import GT
from great_tables.data import sp500
import polars as pl

sp500_mini = (
    pl.from_pandas(sp500)
    .slice(0, 5)
    .drop(["volume", "adj_close", "high", "low"])
    .with_columns(dir = pl.col("close") > pl.col("open"))
)

(
    GT(sp500_mini, rowname_col="date")
    .fmt_tf(columns="dir", tf_style="arrows", colors=["green", "red"])
    .fmt_currency(columns=["open", "close"])
    .cols_label(
        open="Opening",
        close="Closing",
        dir=""
    )
)
```


|            | Opening    | Closing    |                                    |
|------------|------------|------------|------------------------------------|
| 2015-12-31 | \$2,060.59 | \$2,043.94 | <span style="color:red">↓</span>   |
| 2015-12-30 | \$2,077.34 | \$2,063.36 | <span style="color:red">↓</span>   |
| 2015-12-29 | \$2,060.54 | \$2,078.36 | <span style="color:green">↑</span> |
| 2015-12-28 | \$2,057.77 | \$2,056.50 | <span style="color:red">↓</span>   |
| 2015-12-24 | \$2,063.52 | \$2,060.99 | <span style="color:red">↓</span>   |
