## GT.cols_merge_uncert()


Merge columns to a value-with-uncertainty column.


Usage

``` python
GT.cols_merge_uncert(
    col_val, col_uncert, rows=None, sep=" +/- ", autohide=True
)
```


[cols_merge_uncert()](GT.cols_merge_uncert.md#great_tables.GT.cols_merge_uncert) is a specialized variant of [cols_merge()](GT.cols_merge.md#great_tables.GT.cols_merge). It takes as input a base value column (`col_val`) and either: (1) a single uncertainty column, or (2) two columns representing lower and upper uncertainty bounds. These columns will be essentially merged into a single column (that of `col_val`). What results is a column with values and associated uncertainties, and any columns specified in `col_uncert` are hidden from appearing in the output table.


## Parameters


`col_val: SelectExpr`  
The column that contains values for the base measurement. While column selection expressions can be used, it's recommended that a single column name be used to ensure that exactly one column is provided here.

`col_uncert: SelectExpr`  
The column or columns that contain uncertainty values. The most common case involves supplying a single column with uncertainties; these values will be combined with those in `col_val`. Less commonly, the lower and upper uncertainty bounds may be different. For that case, two columns representing the lower and upper uncertainty values away from `col_val`, respectively, should be provided as a list.

`rows: int | list[int] | None = None`  
In conjunction with `col_val`, we can specify which rows should participate in the merging process. The default is all rows. Alternatively, we can supply a list of row indices.

`sep: str = ``" +/- "`  
The separator text that contains the uncertainty mark for a single uncertainty value. The default value of `" +/- "` indicates that an appropriate plus/minus mark will be used depending on the output context. The plus/minus symbol (±) is used in HTML output.

`autohide: bool = ``True`  
An option to automatically hide any columns specified in `col_uncert`. Any columns with their state changed to hidden will behave the same as before, they just won't be displayed in the finalized table. Defaults to `True`.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Details


#### Specialized NA handling

This function employs specialized semantics for missing value handling that differ from the generic [cols_merge()](GT.cols_merge.md#great_tables.GT.cols_merge):

1.  Missing values in `col_val` result in missing values for the merged column (e.g., `NA` + `0.1` = `NA`)
2.  Missing values in `col_uncert` (but not `col_val`) result in base values only for the merged column (e.g., `12.0` + `NA` = `12.0`)
3.  Missing values in both `col_val` and `col_uncert` result in missing values for the merged column (e.g., `NA` + `NA` = `NA`)


## Examples

Use the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a simple, two-column table. Merge the `currency` and `num` columns together as a value with uncertainty.


``` python
from great_tables import GT
from great_tables.data import exibble
import polars as pl

exibble_mini = (
    pl.from_pandas(exibble)
    .select("num", "currency")
    .slice(0, 7)
)

(
    GT(exibble_mini)
    .fmt_number(columns="num", decimals=3, use_seps=False)
    .cols_merge_uncert(col_val="currency", col_uncert="num")
    .cols_label(currency="value + uncert.")
)
```


| value + uncert.    |
|--------------------|
| 49.95 ± 0.111      |
| 17.95 ± 2.222      |
| 1.39 ± 33.330      |
| 65100.0 ± 444.400  |
| 1325.81 ± 5550.000 |
| 13.255             |
|                    |


When there are missing values in the uncertainty column, the merged result shows only the base value. When the base value itself is missing, the entire merged cell is empty.


``` python
df = pl.DataFrame({
    "measurement": [12.5, 8.3, 15.0, 9.7],
    "error": [0.2, None, 0.5, None],
})

(
    GT(df)
    .fmt_number(columns="error", decimals=2)
    .cols_merge_uncert(col_val="measurement", col_uncert="error")
    .cols_label(measurement="Measurement")
)
```


| Measurement |
|-------------|
| 12.5 ± 0.20 |
| 8.3         |
| 15.0 ± 0.50 |
| 9.7         |
