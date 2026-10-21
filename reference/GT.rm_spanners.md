# GT.rm_spanners()

Remove column spanners.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_rm.py#L198-L286)

``` python
GT.rm_spanners(
    spanners=None,
    levels=None,
)
```

Column spanners are added with the [`tab_spanner()`](../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner) method. The [rm_spanners()](../reference/GT.rm_spanners.md#great_tables.GT.rm_spanners) method allows for the removal of spanners while leaving the columns themselves intact. We can either target spanners by their ID values (with the `spanners=` argument) or by their levels (with the `levels=` argument).

## Parameters

`spanners: str | list[str] | None = None`  
The spanners to remove. Supplied as a single spanner ID or a list of spanner ID values. If `None` (the default), then all spanners will be considered for removal (subject to any constraint imposed by `levels=`).

`levels: int | list[int] | None = None`  
The spanner levels to remove, supplied as a single level or a list of levels. Spanners are placed on levels starting from `0` (the level closest to the column labels). If `None` (the default), then no levels-based constraint is applied. When supplied, only spanners residing on the specified levels (and also matching `spanners=`) are removed.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Using a subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset, let's create a table with two spanners. We then remove the spanner with the ID `"performance"` while leaving the other spanner in place.

``` python
from great_tables import GT
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "hp", "trq", "mpg_c"]].head(5)

(
    GT(gtcars_mini)
    .tab_spanner(label="performance", columns=["hp", "trq"])
    .tab_spanner(label="economy", columns=["mpg_c"])
    .rm_spanners(spanners="performance")
)
```

| mfr     | model        | hp    | trq   | economy |
|---------|--------------|-------|-------|---------|
|         |              |       |       | mpg_c   |
| Ford    | GT           | 647.0 | 550.0 | 11.0    |
| Ferrari | 458 Speciale | 597.0 | 398.0 | 13.0    |
| Ferrari | 458 Spider   | 562.0 | 398.0 | 13.0    |
| Ferrari | 458 Italia   | 562.0 | 398.0 | 13.0    |
| Ferrari | 488 GTB      | 661.0 | 561.0 | 15.0    |

## See Also

[`tab_spanner()`](../reference/GT.tab_spanner.md#great_tables.GT.tab_spanner) to add a spanner to a table.  
