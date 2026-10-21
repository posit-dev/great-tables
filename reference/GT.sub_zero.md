# GT.sub_zero()

Substitute zero values in the table body.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_substitution.py#L102-L161)

``` python
GT.sub_zero(
    columns=None,
    rows=None,
    zero_text="nil",
)
```

Wherever there is numerical data that are zero in value, replacement text may be better for explanatory purposes. The [sub_zero()](../reference/GT.sub_zero.md#great_tables.GT.sub_zero) function allows for this replacement through its `zero_text=` argument. Only numeric values are replaced, so `False` in a boolean column is left as is.

## Parameters

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should be scanned for zeros. The default is all rows, resulting in all rows in all targeted columns being considered for this substitution. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`zero_text: str = "nil"`  
The text to be used in place of zero values in the rendered table. We can optionally use the [`md()`](../reference/md.md#great_tables.md) or [`html()`](../reference/html.md#great_tables.md) functions to style the text as Markdown or to retain HTML elements in the text.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Let's generate a simple table that contains an assortment of values that could potentially undergo some substitution via the [sub_zero()](../reference/GT.sub_zero.md#great_tables.GT.sub_zero) method (i.e., there are two `0` values). The ordering of the [`fmt_scientific()`](../reference/GT.fmt_scientific.md#great_tables.GT.fmt_scientific) and [sub_zero()](../reference/GT.sub_zero.md#great_tables.GT.sub_zero) calls in the example below doesn't affect the final result since any `sub_*()` method won't interfere with the formatting of the table.

``` python
from great_tables import GT
import polars as pl

single_vals_df = pl.DataFrame(
    {
        "i": range(1, 8),
        "numbers": [2.75, 0, -3.2, 8, 1e-10, 0, 2.6e9]
    }
)

GT(single_vals_df).fmt_scientific(columns="numbers").sub_zero()
```

| i   | numbers      |
|-----|--------------|
| 1   | 2.75         |
| 2   | nil          |
| 3   | −3.20        |
| 4   | 8.00         |
| 5   | 1.00 × 10⁻¹⁰ |
| 6   | nil          |
| 7   | 2.60 × 10⁹   |
