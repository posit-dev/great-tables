# GTI.i_selection()

Let readers select the table's rows.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L499-L534)

``` python
GTI.i_selection(mode="multiple")
```

Rows are selected by clicking them or their checkboxes, in a column before the others. With `"single"`, selecting a row clears the one selected before; with `"multiple"`, Shift-click selects a range of rows, and a checkbox in the column labels selects every row that matches the search. The info panel (from the (i) button in the control bar) says how many rows are selected, and can clear the selection. Selection is off by default.

## Parameters

`mode: SelectionMode | None = "multiple"`  
One of `"multiple"` (several rows), `"single"` (one row at a time), or `None` (no rows can be selected).

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a table where readers can select one row at a time.

``` python
from great_tables import GTI, exibble

GTI(exibble[["num", "char", "fctr"]]).i_selection("single")
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
