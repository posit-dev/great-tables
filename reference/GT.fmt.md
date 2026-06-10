## GT.fmt()


Set a column format with a formatter function.


Usage

``` python
GT.fmt(
    fns,
    columns=None,
    rows=None,
    is_substitution=False,
)
```


The [fmt()](GT.fmt.md#great_tables.GT.fmt) method provides a way to execute custom formatting functionality with raw data values in a way that can consider all output contexts.

Along with the [columns](loc.body.md#great_tables.loc.body.columns) and [rows](loc.stub.md#great_tables.loc.stub.rows) arguments that provide some precision in targeting data cells, the `fns` argument allows you to define a function for manipulating the raw data.


## Parameters


`fns: FormatFn`  
A formatting function to apply to the targeted cells.

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in [columns](loc.body.md#great_tables.loc.body.columns) being formatted. Alternatively, we can supply a list of row indices.

`is_substitution: bool = ``False`  
Whether the formatter is a substitution. Substitutions are run last, after other formatters.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use the [exibble](data.exibble.md#great_tables.data.exibble) dataset to create a table. With the [fmt()](GT.fmt.md#great_tables.GT.fmt) method, we'll add a prefix `^` and a suffix `$` to the `row` and `group` columns.


``` python
from great_tables import GT, exibble

(
    GT(exibble)
    .fmt(lambda x: f"^{x}$", columns=["row", "group"])
)
```


| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | ^row_1\$ | ^grp_a\$ |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | ^row_2\$ | ^grp_a\$ |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | ^row_3\$ | ^grp_a\$ |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | ^row_4\$ | ^grp_a\$ |
| 5550.0 |  | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | ^row_5\$ | ^grp_b\$ |
|  | fig | six | 2015-06-15 |  | 2018-06-06 16:11 | 13.255 | ^row_6\$ | ^grp_b\$ |
| 777000.0 | grapefruit | seven |  | 19:10 | 2018-07-07 05:22 |  | ^row_7\$ | ^grp_b\$ |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 |  | 0.44 | ^row_8\$ | ^grp_b\$ |
