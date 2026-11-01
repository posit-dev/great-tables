# GT.opt_vertical_padding()

Option to scale the vertical padding of the table.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_options.py#L949-L1043)

``` python
GT.opt_vertical_padding(scale=1.0)
```

This method allows us to scale the vertical padding of the table by a factor of `scale`. The default value is `1.0` and this method serves as a convenient shortcut for `gt.tab_options(heading_padding=<new_val>, column_labels_padding=<new_val>, data_row_padding=<new_val>, row_group_padding=<new_val>, source_notes_padding=<new_val>)`.

## Parameters

`scale: float = 1.0`  
The factor by which to scale the vertical padding. The default value is `1.0`. A value less than `1.0` will reduce the padding, and a value greater than `1.0` will increase the padding. The value must be between `0` and `3`.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Using select columns from the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset, let's create a table with a number of components added. Following that, we'll scale the vertical padding of the table by a factor of `3` using the [opt_vertical_padding()](../reference/GT.opt_vertical_padding.md#great_tables.GT.opt_vertical_padding) method.

``` python
from great_tables import GT, exibble, md

gt_tbl = (
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
)

gt_tbl.opt_vertical_padding(scale=3)
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

Now that's a tall table! The overall effect of scaling the vertical padding is that the table will appear taller and there will be more buffer space between the table elements. A value of `3` is pretty extreme and is likely to be too much in most cases, so, feel free to experiment with different values when looking to increase the vertical padding.

Let's go the other way (using a value less than `1`) and try to condense the content vertically with a `scale` factor of `0.5`. This will reduce the top and bottom padding globally and make the table appear more compact.

``` python
gt_tbl.opt_vertical_padding(scale=0.5)
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

A value of `0.5` provides a reasonable amount of vertical padding and the table will appear more compact. This is useful when space is limited and, in such a situation, this is a practical solution to that problem.
