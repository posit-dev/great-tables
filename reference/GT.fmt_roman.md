## GT.fmt_roman()


Format values as Roman numerals.


Usage

``` python
GT.fmt_roman(
    columns=None,
    rows=None,
    case="upper",
    pattern="{x}",
)
```


With numeric values in a **gt** table we can transform those to Roman numerals, rounding values as necessary.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.

`case: str = ``"upper"`  
Should Roman numerals should be rendered as uppercase (`"upper"`) or lowercase (`"lower"`) letters? By default, this is set to `"upper"`.

`pattern: str = ``"{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by the `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's first create a DataFrame containing small numeric values and then introduce that to <a href="GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>. We'll then format the `roman` column to appear as Roman numerals with the [fmt_roman()](GT.fmt_roman.md#great_tables.GT.fmt_roman) method.


``` python
import pandas as pd
from great_tables import GT

numbers_tbl = pd.DataFrame({"arabic": [1, 8, 24, 85], "roman": [1, 8, 24, 85]})

(
    GT(numbers_tbl, rowname_col="arabic")
    .fmt_roman(columns="roman")
)
```


|     | roman |
|-----|-------|
| 1   | I     |
| 8   | VIII  |
| 24  | XXIV  |
| 85  | LXXXV |
