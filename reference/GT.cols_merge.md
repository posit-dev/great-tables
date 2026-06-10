## GT.cols_merge()


Merge data from two or more columns into a single column.


Usage

``` python
GT.cols_merge(
    columns,
    hide_columns=None,
    rows=None,
    pattern=None,
)
```


This method takes input from two or more columns and allows the contents to be merged into a single column by using a pattern that specifies the arrangement. The first column in the `columns=` parameter operates as the target column (i.e., the column that will undergo mutation) whereas all following columns will be untouched. There is the option to hide the non-target columns. The formatting of values in different columns will be preserved upon merging.


## Parameters


`columns: SelectExpr`  
The columns for which the merging operations should be applied. The first column name resolved will be the target column (i.e., undergo mutation) and the other columns will serve to provide input. Can be a list of column names or a selection expression, though a list is preferred here to ensure the order of columns is exactly as intended (since order matters for the `pattern=` parameter).

`hide_columns: SelectExpr | Literal[False] = None`  
Any column names provided here will have their state changed to hidden (via internal use of `.cols_hide()`) if they aren't already hidden. This is convenient if the shared purpose of these specified columns is only to provide string input to the target column. To suppress any hiding of columns, `False` can be used here. By default, all columns other than the first one specified in `columns=` will be hidden.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should participate in the merging process. The default is all rows, resulting in all rows in `columns=` being formatted. Alternatively, we can supply a list of row indices.

`pattern: str | None = None`  
A formatting pattern that specifies the arrangement of the column values and any string literals. The pattern uses numbers (within `{}`) that correspond to the indices of columns provided in `columns=`. If two columns are provided in `columns=` and we would like to combine the cell data onto the first column, `"{0} {1}"` could be used. If a pattern isn't provided then a space-separated pattern that includes all columns will be generated automatically. The pattern can also use `<<`/`>>` to surround spans of text that will be removed if any of the contained `{}` yields a missing value. Further details are provided in the *How the pattern works* section.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Details


#### How the pattern works

There are two types of templating for the `pattern` string:

- `{` `}` for arranging single column values in a row-wise fashion
- `<<` `>>` to surround spans of text that will be removed if any of the contained `{` `}` yields a missing value

Integer values are placed in `{}` and those values correspond to the columns involved in the merge, in the order they are provided in the `columns=` argument. So the pattern `"{0} ({1}-{2})"` corresponds to the target column value listed first in [columns](loc.body.md#great_tables.loc.body.columns) and the second and third columns cited (formatted as a range in parentheses). With hypothetical values, this might result as the merged string `"38.2 (3-8)"`.

Because some values involved in merging may be missing, it is likely that something like `"38.2 (3-None)"` would be undesirable. For such cases, placing sections of text in `<<>>` results in the entire span being eliminated if there were to be an `None` value (arising from `{}` values). We could instead opt for a pattern like `"{0}<< ({1}-{2})>>"`, which results in `"38.2"` if either columns `{1}` or `{2}` have a `None` value. We can even use a more complex nesting pattern like `"{0}<< ({1}-<<{2}>>)>>"` to retain a lower limit in parentheses (where `{2}` is `None`) but remove the range altogether if `{1}` is `None`.

One more thing to note here is that if `.sub_missing()` is used on values in a column, those specific values affected won't be considered truly missing by `.cols_merge()` (since they have been explicitly handled with substitute text).


## Examples

Let's use a subset of the [sp500](data.sp500.md#great_tables.data.sp500) dataset to create a table. We'll merge the `open` & `close` columns together, and the `low` & `high` columns (putting an em dash between both).


``` python
from great_tables import GT
from great_tables.data import sp500
import polars as pl

sp500_mini = (
    pl.from_pandas(sp500)
    .slice(49, 6)
    .select("open", "close", "low", "high")
)

(
    GT(sp500_mini)
    .fmt_number(
        columns=["open", "close", "low", "high"],
        decimals=2,
        use_seps=False
    )
    .cols_merge(columns=["open", "close"], pattern="{0}--{1}")
    .cols_merge(columns=["low", "high"], pattern="{0}--{1}")
    .cols_label(open="open/close", low="low/high")
)
```


| open/close      | low/high        |
|-----------------|-----------------|
| 2033.47--2018.94 | 2017.22--2037.97 |
| 2033.13--2030.77 | 2026.61--2039.12 |
| 2031.73--2033.66 | 2022.31--2034.45 |
| 2024.37--2033.11 | 2020.46--2033.54 |
| 1996.47--2023.86 | 1996.47--2024.15 |
| 2003.66--1994.24 | 1990.73--2009.56 |


Now we'll use a portion of the [gtcars](data.gtcars.md#great_tables.data.gtcars) for the next example that accounts for missing values in the `pattern=` parameter. Use the `.cols_merge()` method twice to merge together the: (1) `trq` and `trq_rpm` columns, and (2) `mpg_c` & `mpg_h` columns. Given the presence of missing values, we can use patterns with `<<`/`>>` to create conditional text spans, avoiding results where any of the merged columns have missing values.


``` python
from great_tables.data import gtcars
import polars.selectors as cs

gtcars_pl = (
    pl.from_pandas(gtcars)
    .filter(pl.col("year") == 2017)
    .select(["mfr", "model", "trq", "trq_rpm", "mpg_c", "mpg_h"])
)

(
    GT(gtcars_pl)
    .fmt_integer(columns=[cs.starts_with("trq"), cs.starts_with("mpg")])
    .cols_merge(columns=["trq", "trq_rpm"], pattern="{0}<< ({1} rpm)>>")
    .cols_merge(columns=["mpg_c", "mpg_h"], pattern="<<{0} city<</{1} hwy>>>>")
    .cols_label(mfr="Manufacturer", model="Car Model", trq="Torque", mpg_c="MPG")
)
```


| Manufacturer | Car Model   | Torque          | MPG            |
|--------------|-------------|-----------------|----------------|
| Ford         | GT          | 550 (5,900 rpm) | 11 city/18 hwy |
| Ferrari      | GTC4Lusso   | 514 (5,750 rpm) | 12 city/17 hwy |
| Acura        | NSX         | 476 (2,000 rpm) | 21 city/22 hwy |
| Aston Martin | DB11        | 516 (1,500 rpm) | 15 city/21 hwy |
| Dodge        | Viper       | 600 (5,000 rpm) | 12 city/19 hwy |
| Lotus        | Evora       | 302 (3,500 rpm) | 16 city/24 hwy |
| Tesla        | Model S     | 243             |                |
| Porsche      | 718 Boxster | 280 (1,950 rpm) | 21 city/28 hwy |
| Porsche      | 718 Cayman  | 280 (1,950 rpm) | 20 city/29 hwy |
