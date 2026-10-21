# GT.tab_stub()

Add a table stub, to emphasize row and group information.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_modify_rows.py#L48-L122)

``` python
GT.tab_stub(
    rowname_col=None,
    groupname_col=None,
)
```

## Parameters

`rowname_col: str | list[str] | None = None`  
The column to use for row names. By default, no row names added. A list of columns creates a hierarchical stub: the last column holds the row names, and the columns before it are outer levels (outermost first), with repeated values merged across adjacent rows.

`groupname_col: str | None = None`  
The column to use for group names. By default no group names added.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

By default, all data is together in the body of the table.

``` python
from great_tables import GT, exibble

GT(exibble)
```

| num | char | fctr | date | time | datetime | currency | row | group |
|----|----|----|----|----|----|----|----|----|
| 0.1111 | apricot | one | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95 | row_1 | grp_a |
| 2.222 | banana | two | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95 | row_2 | grp_a |
| 33.33 | coconut | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39 | row_3 | grp_a |
| 444.4 | durian | four | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0 | row_4 | grp_a |
| 5550.0 | None | five | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81 | row_5 | grp_b |
| None | fig | six | 2015-06-15 | None | 2018-06-06 16:11 | 13.255 | row_6 | grp_b |
| 777000.0 | grapefruit | seven | None | 19:10 | 2018-07-07 05:22 | None | row_7 | grp_b |
| 8880000.0 | honeydew | eight | 2015-08-15 | 20:20 | None | 0.44 | row_8 | grp_b |

The table stub separates row names with a vertical line, and puts group names on their own line.

``` python
GT(exibble).tab_stub(rowname_col="row", groupname_col="group")
```

|       | num       | char       | fctr  | date       | time  | datetime         | currency |
|-------|-----------|------------|-------|------------|-------|------------------|----------|
| grp_a |           |            |       |            |       |                  |          |
| row_1 | 0.1111    | apricot    | one   | 2015-01-15 | 13:35 | 2018-01-01 02:22 | 49.95    |
| row_2 | 2.222     | banana     | two   | 2015-02-15 | 14:40 | 2018-02-02 14:33 | 17.95    |
| row_3 | 33.33     | coconut    | three | 2015-03-15 | 15:45 | 2018-03-03 03:44 | 1.39     |
| row_4 | 444.4     | durian     | four  | 2015-04-15 | 16:50 | 2018-04-04 15:55 | 65100.0  |
| grp_b |           |            |       |            |       |                  |          |
| row_5 | 5550.0    | None       | five  | 2015-05-15 | 17:55 | 2018-05-05 04:00 | 1325.81  |
| row_6 | None      | fig        | six   | 2015-06-15 | None  | 2018-06-06 16:11 | 13.255   |
| row_7 | 777000.0  | grapefruit | seven | None       | 19:10 | 2018-07-07 05:22 | None     |
| row_8 | 8880000.0 | honeydew   | eight | 2015-08-15 | 20:20 | None             | 0.44     |

Passing a list of columns to `rowname_col=` creates a hierarchical stub. Here, the rows are labeled by `"group"` and then `"row"`, and the repeated group values are merged.

``` python
GT(exibble[["group", "row", "num", "char"]]).tab_stub(rowname_col=["group", "row"])
```

|       |       | num       | char       |
|-------|-------|-----------|------------|
| grp_a | row_1 | 0.1111    | apricot    |
|       | row_2 | 2.222     | banana     |
|       | row_3 | 33.33     | coconut    |
|       | row_4 | 444.4     | durian     |
| grp_b | row_5 | 5550.0    | None       |
|       | row_6 | None      | fig        |
|       | row_7 | 777000.0  | grapefruit |
|       | row_8 | 8880000.0 | honeydew   |
