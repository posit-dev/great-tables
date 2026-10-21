# GT.opt_table_outline()

Option to wrap an outline around the entire table.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_options.py#L1305-L1383)

``` python
GT.opt_table_outline(
    style="solid",
    width="3px",
    color="#D3D3D3",
)
```

The [opt_table_outline()](../reference/GT.opt_table_outline.md#great_tables.GT.opt_table_outline) method puts an outline of consistent `style=`, `width=`, and `color=` around the entire table. It'll write over any existing outside lines so long as the `width=` value is larger that of the existing lines. The default value of `style=` (`"solid"`) will draw a solid outline, whereas using `"none"` will remove any present outline.

## Parameters

`style: str = "solid"`  
The style of the table outline. The default value is `"solid"`. The valid values are `"solid"`, `"dashed"`, `"dotted"`, and `"none"`.

`width: str = "3px"`  
The width of the table outline. The default value is `"3px"`. The value must be in pixels and it must be an integer value.

`color: str = "#D3D3D3"`  
The color of the table outline, where the default is `"#D3D3D3"`. The value must either a hexadecimal color code or a color name.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Using select columns from the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset, let's create a table with a number of components added. Following that, we'll put an outline around the entire table using the [opt_table_outline()](../reference/GT.opt_table_outline.md#great_tables.GT.opt_table_outline) method.

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
  .opt_table_outline()
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
