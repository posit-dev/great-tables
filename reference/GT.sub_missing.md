## GT.sub_missing()


Substitute missing values in the table body.


Usage

``` python
GT.sub_missing(
    columns=None,
    rows=None,
    missing_text=None,
)
```


Wherever there is missing data (i.e., `None` values) customizable content may present better than the standard representation of missing values that would otherwise appear. The [sub_missing()](GT.sub_missing.md#great_tables.GT.sub_missing) method allows for this replacement through its `missing_text=` argument. And by not supplying anything to `missing_text=`, an em dash will serve as a default indicator of missingness.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should be scanned for missing values. The default is all rows, resulting in all rows in all targeted columns being considered for this substitution. Alternatively, we can supply a list of row indices.

`missing_text: str | Text | None = None`  
The text to be used in place of missing values in the rendered table. We can optionally use the <a href="md.html#great_tables.md" class="gdls-link"><code>md()</code></a> or <a href="html.html#great_tables.html" class="gdls-link"><code>html()</code></a> helper functions to style the text as Markdown or to retain HTML elements in the text.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using a subset of the [exibble](data.exibble.md#great_tables.data.exibble) dataset, let's create a new table. The missing values in two selections of columns will be given different variations of replacement text (across two separate calls of [sub_missing()](GT.sub_missing.md#great_tables.GT.sub_missing)).


``` python
from great_tables import GT, md, html, exibble
import polars as pl
import polars.selectors as cs

exibble_mini = pl.from_pandas(exibble).drop("row", "group", "fctr").slice(4, 8)

(
    GT(exibble_mini)
    .sub_missing(
        columns=["num", "char"],
        missing_text="missing"
    )
    .sub_missing(
        columns=cs.contains(("date", "time")) | cs.by_name("currency"),
        missing_text="nothing"
    )
)
```


| num       | char       | date       | time    | datetime         | currency |
|-----------|------------|------------|---------|------------------|----------|
| 5550.0    | missing    | 2015-05-15 | 17:55   | 2018-05-05 04:00 | 1325.81  |
| missing   | fig        | 2015-06-15 | nothing | 2018-06-06 16:11 | 13.255   |
| 777000.0  | grapefruit | nothing    | 19:10   | 2018-07-07 05:22 | nothing  |
| 8880000.0 | honeydew   | 2015-08-15 | 20:20   | nothing          | 0.44     |
