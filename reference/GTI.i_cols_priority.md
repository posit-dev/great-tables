# GTI.i_cols_priority()

Give columns a priority, for when the table drops columns to fit its container.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L1258-L1316)

``` python
GTI.i_cols_priority(
    columns=None,
    priority=1,
)
```

A table that drops columns to fit a narrow container (with [`i_responsive("collapse")`](../reference/GTI.i_responsive.md#great_tables.GTI.i_responsive), or `"auto"`, the default, once any column has a priority) drops those without a priority first, from the last; then those with the highest numbers (from the last, among those with the same). A column with priority 1 is never dropped, and neither are the stub and the row group column. Readers can see the columns dropped from a row with the button by its first cell.

Each call sets (or unsets) the priority of the columns it's given; a later call for a column replaces what an earlier one set.

## Parameters

`columns: SelectExpr = None`  
The columns to give the priority: a column name, a list of them, or a selector (e.g., Polars' `cs.numeric()`). With `None` (the default), every column but the stub. The stub and the row group column are never dropped (naming them does nothing).

`priority: int | None = 1`  
The columns' priority: a positive integer, where 1 (the default) keeps them, and higher numbers drop sooner. With `None`, the columns have none, and drop first.

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a table of Ontario's municipalities that keeps each one's latest population, and drops its land area before its status (narrow the window to see them go).

``` python
from great_tables import GTI
from great_tables.data import towny

(
    GTI(
        towny[["name", "status", "land_area_km2", "population_2021"]].head(10),
        rowname_col="name",
    )
    .fmt_integer(columns="population_2021")
    .i_cols_priority(columns="population_2021")
    .i_cols_priority(columns="status", priority=2)
    .i_cols_priority(columns="land_area_km2", priority=3)
)
```

|                        | status      | land_area_km2 | population_2021 |
|------------------------|-------------|---------------|-----------------|
| Addington Highlands    | lower-tier  | 1293.99       | 2,534           |
| Adelaide Metcalfe      | lower-tier  | 331.11        | 3,011           |
| Adjala-Tosorontio      | lower-tier  | 371.53        | 10,989          |
| Admaston/Bromley       | lower-tier  | 519.59        | 2,995           |
| Ajax                   | lower-tier  | 66.64         | 126,666         |
| Alberton               | single-tier | 116.6         | 954             |
| Alfred and Plantagenet | lower-tier  | 391.79        | 9,949           |
| Algonquin Highlands    | lower-tier  | 999.69        | 2,588           |
| Alnwick/Haldimand      | lower-tier  | 398.25        | 7,473           |
| Amaranth               | lower-tier  | 265.02        | 4,327           |
