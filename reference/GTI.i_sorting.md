# GTI.i_sorting()

Let readers sort the table by its columns.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L354-L387)

``` python
GTI.i_sorting(enabled=True)
```

A column is sorted with the arrows under its label (or by clicking the label itself): once for ascending order, again for descending, and a third time to go back to the table's own order. With Shift held, a column is added to the sort (and is sorted within the columns before it). Rows are sorted by the column's values, not by how they're formatted, and stay in their row groups. The info panel (from the (i) button in the control bar) says how the table is sorted, and can put it back in its own order. Sorting is on by default; some columns can be left unsortable with [`i_cols_controls()`](../reference/GTI.i_cols_controls.md#great_tables.GTI.i_cols_controls).

## Parameters

`enabled: bool = True`  
Whether readers can sort the table.

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a table that keeps its rows in their order.

``` python
from great_tables import GTI, exibble

GTI(exibble[["num", "char", "fctr"]]).i_sorting(False)
```

| num       | char       | fctr  |
|-----------|------------|-------|
| 0.1111    | apricot    | one   |
| 2.222     | banana     | two   |
| 33.33     | coconut    | three |
| 444.4     | durian     | four  |
| 5550.0    | None       | five  |
| None      | fig        | six   |
| 777000.0  | grapefruit | seven |
| 8880000.0 | honeydew   | eight |
