# GT.rm_header()

Remove the table header.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_rm.py#L11-L48)

``` python
GT.rm_header()
```

We can remove the table header (i.e., the part containing the title and the subtitle) with the [rm_header()](../reference/GT.rm_header.md#great_tables.GT.rm_header) method. This function is useful when you have received a [GT](../reference/GT.md#great_tables.GT) object with a header (perhaps from another function or a saved table) and you'd like to start from a clean slate.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Let's use a subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset to create a table with a header. We can then remove that header with the [rm_header()](../reference/GT.rm_header.md#great_tables.GT.rm_header) method.

``` python
from great_tables import GT, md
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

(
    GT(gtcars_mini)
    .tab_header(title=md("Data listing from **gtcars**"), subtitle="Just five cars")
    .rm_header()
)
```

| mfr     | model        | msrp     |
|---------|--------------|----------|
| Ford    | GT           | 447000.0 |
| Ferrari | 458 Speciale | 291744.0 |
| Ferrari | 458 Spider   | 263553.0 |
| Ferrari | 458 Italia   | 233509.0 |
| Ferrari | 488 GTB      | 245400.0 |

## See Also

[`tab_header()`](../reference/GT.tab_header.md#great_tables.GT.tab_header) to add a header to a table.  
