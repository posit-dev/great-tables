# GT.opt_align_table_header()

Option to align the table header.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_options.py#L896-L946)

``` python
GT.opt_align_table_header(align="center")
```

By default, an added table header will have center alignment for both the title and the subtitle elements. This method allows us to easily set the horizontal alignment of the title and subtitle to the left, right, or center by using the `"align"` argument. This method serves as a convenient shortcut for `gt.tab_options(heading_align=<align>)`.

## Parameters

`align: str = "center"`  
The alignment of the title and subtitle elements in the table header. Options are `"center"` (the default), `"left"`, or `"right"`.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Using select columns from the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset, let's create a table with a number of components added. Following that, we'll align the header contents (consisting of the title and the subtitle) to the left with the [opt_align_table_header()](../reference/GT.opt_align_table_header.md#great_tables.GT.opt_align_table_header) method.

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
  .opt_align_table_header(align="left")
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
