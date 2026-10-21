# GT.tab_style()

Add custom style to one or more cells

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_tab_create_modify.py#L18-L153)

``` python
GT.tab_style(
    style,
    locations,
)
```

With the [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) method we can target specific cells and apply styles to them. We do this with the combination of the `style` and `location` arguments. The `style` argument requires use of styling classes (e.g., `style.fill(color="red")`) and the `location` argument needs to be an expression of the cells we want to target using location targeting classes (e.g., `loc.body(columns=<column_name>)`). With the available suite of styling classes, here are some of the styles we can apply:

- the background color of the cell ([style.fill()](../reference/style.fill.md#great_tables.style.fill)'s `color`)
- the cell's text color, font, and size ([style.text()](../reference/style.text.md#great_tables.style.text)'s `color`, `font`, and `size`)
- the text style ([style.text()](../reference/style.text.md#great_tables.style.text)'s `style`), enabling the use of italics or oblique text.
- the text weight ([style.text()](../reference/style.text.md#great_tables.style.text)'s `weight`), allowing the use of thin to bold text (the degree of choice is greater with variable fonts)
- the alignment of text ([style.text()](../reference/style.text.md#great_tables.style.text)'s `align`)
- cell borders with the [style.borders()](../reference/style.borders.md#great_tables.style.borders) class

## Parameters

`style: CellStyle | list[CellStyle]`  
The styles to use for the cells at the targeted `locations`. The [style.text()](../reference/style.text.md#great_tables.style.text), [style.fill()](../reference/style.fill.md#great_tables.style.fill), and [style.borders()](../reference/style.borders.md#great_tables.style.borders) classes can be used here to more easily generate valid styles.

`locations: Loc | list[Loc]`  
The cell or set of cells to be associated with the style. The [loc.body()](../reference/loc.body.md#great_tables.loc.body) class can be used here to easily target body cell locations.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Let's use a small subset of the [exibble](../reference/data.exibble.md#great_tables.data.exibble) dataset to demonstrate how to use [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) to target specific cells and apply styles to them. We'll start by creating the `exibble_sm` table (a subset of the [exibble](../reference/data.exibble.md#great_tables.data.exibble) table) and then use [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) to apply a light cyan background color to the cells in the `num` column for the first two rows of the table. We'll then apply a larger font size to the cells in the `fctr` column for the last four rows of the table.

``` python
from great_tables import GT, style, loc, exibble

exibble_sm = exibble[["num", "fctr", "row", "group"]]

(
    GT(exibble_sm, rowname_col="row", groupname_col="group")
    .tab_style(
        style=style.fill(color="lightcyan"),
        locations=loc.body(columns="num", rows=["row_1", "row_2"]),
    )
    .tab_style(
        style=style.text(size="22px"),
        locations=loc.body(columns=["fctr"], rows=[4, 5, 6, 7]),
    )
)
```

|       | num       | fctr  |
|-------|-----------|-------|
| grp_a |           |       |
| row_1 | 0.1111    | one   |
| row_2 | 2.222     | two   |
| row_3 | 33.33     | three |
| row_4 | 444.4     | four  |
| grp_b |           |       |
| row_5 | 5550.0    | five  |
| row_6 | None      | six   |
| row_7 | 777000.0  | seven |
| row_8 | 8880000.0 | eight |

Let's use [exibble](../reference/data.exibble.md#great_tables.data.exibble) once again to create a simple, two-column output table (keeping only the `num` and `currency` columns). With the [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) method (called thrice), we'll add style to the values already formatted by [`fmt_number()`](../reference/GT.fmt_number.md#great_tables.GT.fmt_number) and [`fmt_currency()`](../reference/GT.fmt_currency.md#great_tables.GT.fmt_currency). In the `style` argument of the first two [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) call, we can define multiple types of styling with the [style.fill()](../reference/style.fill.md#great_tables.style.fill) and [style.text()](../reference/style.text.md#great_tables.style.text) classes (enclosing these in a list). The cells to be targeted for styling require the use of [loc.body()](../reference/loc.body.md#great_tables.loc.body), which is used here with different columns being targeted. For the final [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) call, we demonstrate the use of [style.borders()](../reference/style.borders.md#great_tables.style.borders) class as the `style` argument, which is employed in conjunction with [loc.body()](../reference/loc.body.md#great_tables.loc.body) to locate the row to be styled.

``` python
from great_tables import GT, style, loc, exibble

(
    GT(exibble[["num", "currency"]])
    .fmt_number(columns="num", decimals=1)
    .fmt_currency(columns="currency")
    .tab_style(
        style=[
            style.fill(color="lightcyan"),
            style.text(weight="bold")
        ],
        locations=loc.body(columns="num")
    )
    .tab_style(
        style=[
            style.fill(color="#F9E3D6"),
            style.text(style="italic")
        ],
        locations=loc.body(columns="currency")
    )
    .tab_style(
        style=style.borders(sides=["top", "bottom"], weight='2px', color="red"),
        locations=loc.body(rows=[4])
    )
)
```

| num         | currency    |
|-------------|-------------|
| 0.1         | \$49.95     |
| 2.2         | \$17.95     |
| 33.3        | \$1.39      |
| 444.4       | \$65,100.00 |
| 5,550.0     | \$1,325.81  |
| None        | \$13.26     |
| 777,000.0   | None        |
| 8,880,000.0 | \$0.44      |
