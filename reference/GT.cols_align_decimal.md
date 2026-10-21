# GT.cols_align_decimal()

Align all numeric values in a column along the decimal mark.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_boxhead.py#L307-L387)

``` python
GT.cols_align_decimal(
    columns=None,
    dec_mark=".",
    locale=None,
)
```

For numeric columns that contain values with more than one decimal place, it can be helpful to align them on the decimal mark so they are easier to scan and compare. The [cols_align_decimal()](../reference/GT.cols_align_decimal.md#great_tables.GT.cols_align_decimal) method does this by padding the formatted values with figure spaces (which are as wide as a digit) so that the decimal marks line up, and right-aligning the columns. This happens after formatting, so it works with values formatted by the `fmt_*()` methods, including ones with a `%` or other suffix. Only numeric columns are aligned, any other columns that are targeted are left unchanged.

## Parameters

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list. If `None`, all numeric columns are targeted.

`dec_mark: str = "."`  
The character used as the decimal mark in the formatted values. This is ignored if a `locale` is supplied.

`locale: str | None = None`  
An optional locale identifier that can be used to obtain the decimal mark. If not set, the locale set in `GT(locale=...)`, if any, is used.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Let's put some numbers with different numbers of decimal places in a table, format them with [`fmt_number()`](../reference/GT.fmt_number.md#great_tables.GT.fmt_number) and align them on the decimal mark.

``` python
import polars as pl
from great_tables import GT

df = pl.DataFrame({"num": [1.2, -33.52, 9023.2, -283.527, None, 0.401, 41.0]})

(
    GT(df)
    .fmt_number(columns="num", decimals=3, drop_trailing_zeros=True)
    .cols_align_decimal()
)
```

| num       |
|-----------|
|     1.2   |
|   −33.52  |
| 9,023.2   |
|  −283.527 |
| None      |
|     0.401 |
|    41     |
