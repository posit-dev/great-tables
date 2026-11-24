# GT.tab_spanner_label_with()

Relabel column spanners using a function.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_spanners.py#L450-L539)

``` python
GT.tab_spanner_label_with(
    fn,
    spanners=None,
    levels=None,
)
```

The [tab_spanner_label_with()](../reference/GT.tab_spanner_label_with.md#great_tables.GT.tab_spanner_label_with) method allows for modification of spanner labels through a supplied function. This is useful for spanners made by [`tab_spanner_delim()`](../reference/GT.tab_spanner_delim.md#great_tables.GT.tab_spanner_delim), whose labels are pieces of the column names. By default, the function is applied to the labels of all spanners but this can be limited by spanner ID (with `spanners=`), by spanner level (with `levels=`), or both. Spanner IDs aren't changed, so methods that target spanners by ID still work after relabeling.

## Parameters

`fn: Callable[[str], str | BaseText]`  
A function that accepts a spanner label as input and returns a new label. It can return a string (which may use units notation, see [`define_units()`](../reference/define_units.md#great_tables.define_units)) or a label made with the [`md()`](../reference/md.md#great_tables.md) or [`html()`](../reference/html.md#great_tables.md) helper functions.

`spanners: str | list[str] | None = None`  
The spanners to relabel. Supplied as a single spanner ID or a list of spanner ID values. If `None` (the default), then all spanners will be relabeled (subject to any constraint imposed by `levels=`).

`levels: int | list[int] | None = None`  
The spanner levels to relabel, supplied as a single level or a list of levels. Spanners are placed on levels starting from `0` (the level closest to the column labels). If `None` (the default), then no levels-based constraint is applied.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Notes

Only plain-text labels are passed to `fn`. Labels made with [md()](../reference/md.md#great_tables.md) or [html()](../reference/html.md#great_tables.md), or that use units notation, are left as they are.

## Examples

Let's use a subset of the [towny](../reference/data.towny.md#great_tables.data.towny) dataset, where the `population_*` and `density_*` columns can be split at the underscore with [tab_spanner_delim()](../reference/GT.tab_spanner_delim.md#great_tables.GT.tab_spanner_delim). That gives us two spanners, labeled `"population"` and `"density"`.

``` python
from great_tables import GT
from great_tables.data import towny

towny_mini = towny[
    ["name", "population_2016", "population_2021", "density_2016", "density_2021"]
].head(5)

gt = GT(towny_mini, rowname_col="name").tab_spanner_delim(delim="_")
gt
```

|                     | population |        | density |         |
|---------------------|------------|--------|---------|---------|
|                     | 2016       | 2021   | 2016    | 2021    |
| Addington Highlands | 2318       | 2534   | 1.79    | 1.96    |
| Adelaide Metcalfe   | 2990       | 3011   | 9.03    | 9.09    |
| Adjala-Tosorontio   | 10975      | 10989  | 29.54   | 29.58   |
| Admaston/Bromley    | 2935       | 2995   | 5.65    | 5.76    |
| Ajax                | 119677     | 126666 | 1795.87 | 1900.75 |

We can pass `str.title` to the `fn` parameter to capitalize the spanner labels.

``` python
gt.tab_spanner_label_with(fn=str.title)
```

|                     | Population |        | Density |         |
|---------------------|------------|--------|---------|---------|
|                     | 2016       | 2021   | 2016    | 2021    |
| Addington Highlands | 2318       | 2534   | 1.79    | 1.96    |
| Adelaide Metcalfe   | 2990       | 3011   | 9.03    | 9.09    |
| Adjala-Tosorontio   | 10975      | 10989  | 29.54   | 29.58   |
| Admaston/Bromley    | 2935       | 2995   | 5.65    | 5.76    |
| Ajax                | 119677     | 126666 | 1795.87 | 1900.75 |

The function can return a string that uses units notation. Here, only the spanner with the ID `"density"` is relabeled, with the units of population density added to its label.

``` python
gt.tab_spanner_label_with(
    fn=lambda x: x.title() + " ({{ppl / km^2}})",
    spanners="density",
)
```

|                     | population |        | Density (ppl/km²) |         |
|---------------------|------------|--------|-------------------|---------|
|                     | 2016       | 2021   | 2016              | 2021    |
| Addington Highlands | 2318       | 2534   | 1.79              | 1.96    |
| Adelaide Metcalfe   | 2990       | 3011   | 9.03              | 9.09    |
| Adjala-Tosorontio   | 10975      | 10989  | 29.54             | 29.58   |
| Admaston/Bromley    | 2935       | 2995   | 5.65              | 5.76    |
| Ajax                | 119677     | 126666 | 1795.87           | 1900.75 |

## See Also

[`cols_label_with()`](../reference/GT.cols_label_with.md#great_tables.GT.cols_label_with) to relabel columns using a function.  
