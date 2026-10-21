# GT.opt_stylize()

Stylize your table with a colorful look.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_options.py#L1596-L1716)

``` python
GT.opt_stylize(
    style=1,
    color="blue",
    add_row_striping=True,
)
```

With the [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize) method you can quickly style your table with a carefully curated set of background colors, line colors, and line styles. There are six styles to choose from and they largely vary in the extent of coloring applied to different table locations. Some have table borders applied, some apply darker colors to the table stub and summary sections, and, some even have vertical lines. In addition to choosing a `style` preset, there are six `color` variations that each use a range of five color tints. Each of the color tints have been fine-tuned to maximize the contrast between text and its background. There are 36 combinations of `style` and `color` to choose from. For examples of each style, see the [*Premade Themes*](../user-guide/premade-themes.md) page of the **User Guide**.

## Parameters

`style: int = 1`  
Six numbered styles are available. Simply provide a number from `1` (the default) to `6` to choose a distinct look.

`color: str = "blue"`  
The color scheme of the table. The default value is `"blue"`. The valid values are `"blue"`, `"cyan"`, `"pink"`, `"green"`, `"red"`, and `"gray"`.

`add_row_striping: bool = True`  
An option to enable row striping in the table body for the style chosen.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Using select columns from the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset, let's create a table with a number of components added. Following that, we'll apply a predefined style to the table using the [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize) method.

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
      .opt_stylize()
    )

gt_tbl
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

The table has been stylized with the default style and color. The default style is `1` and the default color is `"blue"`. The resulting table style is a combination of color and border settings that are applied to the table.

We can modify the overall style and choose a different color theme by providing different values to the `style=` and `color=` arguments.

``` python
gt_tbl.opt_stylize(style=2, color="green")
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
