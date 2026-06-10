## GT.tab_style()


Add custom style to one or more cells


Usage

``` python
GT.tab_style(
    style,
    locations,
)
```


With the [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) method we can target specific cells and apply styles to them. We do this with the combination of the [style](style.text.md#great_tables.style.text.style) and `location` arguments. The [style](style.text.md#great_tables.style.text.style) argument requires use of styling classes (e.g., `style.fill(color="red")`) and the `location` argument needs to be an expression of the cells we want to target using location targeting classes (e.g., `loc.body(columns=<column_name>)`). With the available suite of styling classes, here are some of the styles we can apply:

- the background color of the cell ([style.fill()](style.fill.md#great_tables.style.fill)'s [color](style.text.md#great_tables.style.text.color))
- the cell's text color, font, and size ([style.text()](style.text.md#great_tables.style.text)'s [color](style.text.md#great_tables.style.text.color), [font](style.text.md#great_tables.style.text.font), and [size](style.text.md#great_tables.style.text.size))
- the text style ([style.text()](style.text.md#great_tables.style.text)'s [style](style.text.md#great_tables.style.text.style)), enabling the use of italics or oblique text.
- the text weight ([style.text()](style.text.md#great_tables.style.text)'s [weight](style.text.md#great_tables.style.text.weight)), allowing the use of thin to bold text (the degree of choice is greater with variable fonts)
- the alignment of text ([style.text()](style.text.md#great_tables.style.text)'s [align](style.text.md#great_tables.style.text.align))
- cell borders with the [style.borders()](style.borders.md#great_tables.style.borders) class


## Parameters


`style: CellStyle | list[CellStyle]`  
The styles to use for the cells at the targeted `locations`. The [style.text()](style.text.md#great_tables.style.text), [style.fill()](style.fill.md#great_tables.style.fill), and [style.borders()](style.borders.md#great_tables.style.borders) classes can be used here to more easily generate valid styles.

`locations: Loc | list[Loc]`  
The cell or set of cells to be associated with the style. The [loc.body()](loc.body.md#great_tables.loc.body) class can be used here to easily target body cell locations.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use a small subset of the [exibble](data.exibble.md#great_tables.data.exibble) dataset to demonstrate how to use [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) to target specific cells and apply styles to them. We'll start by creating the `exibble_sm` table (a subset of the [exibble](data.exibble.md#great_tables.data.exibble) table) and then use [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) to apply a light cyan background color to the cells in the `num` column for the first two rows of the table. We'll then apply a larger font size to the cells in the `fctr` column for the last four rows of the table.


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


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right" style="background-color: lightcyan">0.1111</td>
<td class="gt_row gt_left">one</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right" style="background-color: lightcyan">2.222</td>
<td class="gt_row gt_left">two</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">three</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">four</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left" style="font-size: 22px">five</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right"></td>
<td class="gt_row gt_left" style="font-size: 22px">six</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777000.0</td>
<td class="gt_row gt_left" style="font-size: 22px">seven</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right">8880000.0</td>
<td class="gt_row gt_left" style="font-size: 22px">eight</td>
</tr>
</tbody>
</table>


Let's use [exibble](data.exibble.md#great_tables.data.exibble) once again to create a simple, two-column output table (keeping only the `num` and `currency` columns). With the [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) method (called thrice), we'll add style to the values already formatted by [fmt_number()](GT.fmt_number.md#great_tables.GT.fmt_number) and [fmt_currency()](GT.fmt_currency.md#great_tables.GT.fmt_currency). In the [style](style.text.md#great_tables.style.text.style) argument of the first two [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) call, we can define multiple types of styling with the [style.fill()](style.fill.md#great_tables.style.fill) and [style.text()](style.text.md#great_tables.style.text) classes (enclosing these in a list). The cells to be targeted for styling require the use of [loc.body()](loc.body.md#great_tables.loc.body), which is used here with different columns being targeted. For the final [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) call, we demonstrate the use of [style.borders()](style.borders.md#great_tables.style.borders) class as the [style](style.text.md#great_tables.style.text.style) argument, which is employed in conjunction with [loc.body()](loc.body.md#great_tables.loc.body) to locate the row to be styled.


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
|             | \$13.26     |
| 777,000.0   |             |
| 8,880,000.0 | \$0.44      |
