# GT.rm_stubhead()

Remove the stubhead label.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_rm.py#L51-L87)

``` python
GT.rm_stubhead()
```

We can remove the stubhead label (i.e., the label positioned above the table stub) with the [rm_stubhead()](../reference/GT.rm_stubhead.md#great_tables.GT.rm_stubhead) method. This is useful when a stubhead label is present but no longer wanted.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Using a subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset, we create a table with a stub and a stubhead label. The label is then removed with the [rm_stubhead()](../reference/GT.rm_stubhead.md#great_tables.GT.rm_stubhead) method.

``` python
from great_tables import GT
from great_tables.data import gtcars

gtcars_mini = gtcars[["model", "mfr", "msrp"]].head(5)

(
    GT(gtcars_mini, rowname_col="model")
    .tab_stubhead(label="car")
    .rm_stubhead()
)
```

|              | mfr     | msrp     |
|--------------|---------|----------|
| GT           | Ford    | 447000.0 |
| 458 Speciale | Ferrari | 291744.0 |
| 458 Spider   | Ferrari | 263553.0 |
| 458 Italia   | Ferrari | 233509.0 |
| 488 GTB      | Ferrari | 245400.0 |

## See Also

[`tab_stubhead()`](../reference/GT.tab_stubhead.md#great_tables.GT.tab_stubhead) to add a stubhead label to a table.  
