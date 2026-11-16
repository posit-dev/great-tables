# GTI.i_inspect()

Show readers what's in the data: its rows' numbers, its columns' dtypes, its size, and where

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L720-L797)

``` python
GTI.i_inspect(
    *,
    row_numbers=True,
    dtypes=True,
    dimensions=True,
    missing=True,
    row_start=None,
)
```

its values are missing.

Row numbers are in a narrow column before the others (with the rows' checkboxes, with [`i_selection()`](../reference/GTI.i_selection.md#great_tables.GTI.i_selection)), pinned with the stub as the table scrolls sideways: each row's is its place in the data, which stays with it as the rows are sorted, filtered and paged. A DataFrame's rows are numbered from 0, as its index is (and as Polars' `with_row_index()` numbers them), and a DuckDB relation's or an Ibis table's from 1, as a database's `ROW_NUMBER()` does; `row_start=` sets where they start. A dtype is under its column's label, as a short name (as Polars prints it, for any DataFrame library): `"i64"`, `"f64"`, `"str"`, `"bool"`, `"cat"`, `"date"`, `"datetime"`, and so on. The dimensions are in the status line above the table: what the data is (a Polars DataFrame or LazyFrame, a Pandas DataFrame, a PyArrow Table, a DuckDB relation or an Ibis table), its number of rows and columns (those shown, of the stub and the data), and how many of them are left as readers search, filter and hide columns ("Polars DataFrame · 12 of 47 rows × 6 columns"). A missing value (`None`, or NaN in a column of floats) has its cell tinted, whatever the cell shows (as [`sub_missing()`](../reference/GT.sub_missing.md#great_tables.GT.sub_missing) makes it). None of these are searched or exported, and they're all off by default (but in `GTI(preset="explorer")`).

Like the other `i_` methods (but for the `i_cols_` ones), a call sets all of these: those not given are shown.

## Parameters

`row_numbers: bool = True`  
Whether each row has its number, in a column before the others.

`dtypes: bool = True`  
Whether each column's dtype is under its label.

`dimensions: bool = True`  
Whether what the data is, and its number of rows and columns, are in the status line above the table.

`missing: bool = True`  
Whether the cells of missing values are tinted.

`row_start: int | None = None`  
The first row's number: `0` or `1`. By default, it's `0` for a DataFrame (of Polars, Pandas or PyArrow) and `1` for a DuckDB relation or an Ibis table.

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a table with every one of these: sort it, and the rows keep their numbers.

``` python
from great_tables import GTI, exibble

GTI(exibble[["num", "char", "fctr", "date"]]).sub_missing().i_inspect()
```

| num       | char       | fctr  | date       |
|-----------|------------|-------|------------|
| 0.1111    | apricot    | one   | 2015-01-15 |
| 2.222     | banana     | two   | 2015-02-15 |
| 33.33     | coconut    | three | 2015-03-15 |
| 444.4     | durian     | four  | 2015-04-15 |
| 5550.0    | --          | five  | 2015-05-15 |
| --         | fig        | six   | 2015-06-15 |
| 777000.0  | grapefruit | seven | --          |
| 8880000.0 | honeydew   | eight | 2015-08-15 |

The row numbers alone, counted from 1:

``` python
(
    GTI(exibble[["num", "char", "fctr"]])
    .i_inspect(dtypes=False, dimensions=False, missing=False, row_start=1)
)
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
