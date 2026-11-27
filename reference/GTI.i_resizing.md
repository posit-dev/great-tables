# GTI.i_resizing()

Let readers resize the table's columns.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L424-L453)

``` python
GTI.i_resizing(enabled=True)
```

A column is resized by dragging the handle at the end of its label (or, with the handle focused, with the arrow keys); double-clicking the handle sets the column back to its own width. Resizing is on by default; some columns can be kept at their width with [`i_cols_controls()`](../reference/GTI.i_cols_controls.md#great_tables.GTI.i_cols_controls).

## Parameters

`enabled: bool = True`  
Whether readers can resize the table's columns.

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a table with columns of a fixed width.

``` python
from great_tables import GTI, exibble

GTI(exibble[["num", "char", "fctr"]]).i_resizing(False)
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
