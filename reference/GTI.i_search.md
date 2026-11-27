# GTI.i_search()

Let readers search the table.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L391-L422)

``` python
GTI.i_search(enabled=True)
```

A search shows only the rows with a cell that has the text searched for (as it's shown in the table, ignoring case and accents), and highlights the matches. The search is a button in the control bar below the table (or the `/` key, from within the table), which opens a search field; Esc clears the search, then closes the field. Searching is on by default; some columns can be left out of it with [`i_cols_controls()`](../reference/GTI.i_cols_controls.md#great_tables.GTI.i_cols_controls).

## Parameters

`enabled: bool = True`  
Whether readers can search the table.

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a table without a search.

``` python
from great_tables import GTI, exibble

GTI(exibble[["num", "char", "fctr"]]).i_search(False)
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
