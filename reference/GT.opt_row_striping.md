# GT.opt_row_striping()

Option to add or remove row striping.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_options.py#L838-L885)

``` python
GT.opt_row_striping(row_striping=True)
```

By default, a table does not have row striping enabled. However, this method allows us to easily enable or disable striped rows in the table body. It's a convenient shortcut for `tab_options(row_striping_include_table_body=<True|False>)`.

## Parameters

`row_striping: bool = True`  
A boolean that indicates whether row striping should be added or removed. Defaults to `True`.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Using only a few columns from the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset, let's create a table with a number of components added. Following that, we'll add row striping to every second row with the [opt_row_striping()](../reference/GT.opt_row_striping.md#great_tables.GT.opt_row_striping) method.

``` python
from great_tables import GT, exibble, md

(
    GT(
        exibble[["num", "char", "currency", "row", "group"]],
        rowname_col="row",
        groupname_col="group"
    )
    .tab_header(
        title=md("Data listing from **exibble**"),
        subtitle=md("`exibble` is a **Great Tables** dataset.")
    )
    .fmt_number(columns="num")
    .fmt_currency(columns="currency")
    .tab_source_note(source_note="This is only a subset of the dataset.")
    .opt_row_striping()
)
```

| Data listing from **exibble** |  |  |  |
|----|----|----|----|
| `exibble` is a **Great Tables** dataset. |  |  |  |
|  | num | char | currency |
| grp_a |  |  |  |
| row_1 | 0.11 | apricot | \$49.95 |
| row_2 | 2.22 | banana | \$17.95 |
| row_3 | 33.33 | coconut | \$1.39 |
| row_4 | 444.40 | durian | \$65,100.00 |
| grp_b |  |  |  |
| row_5 | 5,550.00 | None | \$1,325.81 |
| row_6 | None | fig | \$13.26 |
| row_7 | 777,000.00 | grapefruit | None |
| row_8 | 8,880,000.00 | honeydew | \$0.44 |
| This is only a subset of the dataset. |  |  |  |
