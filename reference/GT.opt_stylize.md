## GT.opt_stylize()


Stylize your table with a colorful look.


Usage

``` python
GT.opt_stylize(
    style=1,
    color="blue",
    add_row_striping=True,
)
```


With the [opt_stylize()](GT.opt_stylize.md#great_tables.GT.opt_stylize) method you can quickly style your table with a carefully curated set of background colors, line colors, and line styles. There are six styles to choose from and they largely vary in the extent of coloring applied to different table locations. Some have table borders applied, some apply darker colors to the table stub and summary sections, and, some even have vertical lines. In addition to choosing a [style](style.text.md#great_tables.style.text.style) preset, there are six [color](style.text.md#great_tables.style.text.color) variations that each use a range of five color tints. Each of the color tints have been fine-tuned to maximize the contrast between text and its background. There are 36 combinations of [style](style.text.md#great_tables.style.text.style) and [color](style.text.md#great_tables.style.text.color) to choose from. For examples of each style, see the [*Premade Themes*](../get-started/table-theme-premade.qmd) section of the **Get Started** guide.


## Parameters


`style: int = ``1`  
Six numbered styles are available. Simply provide a number from `1` (the default) to `6` to choose a distinct look.

`color: str = ``"blue"`  
The color scheme of the table. The default value is `"blue"`. The valid values are `"blue"`, `"cyan"`, `"pink"`, `"green"`, `"red"`, and `"gray"`.

`add_row_striping: bool = ``True`  
An option to enable row striping in the table body for the style chosen.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using select columns from the [exibble](data.exibble.md#great_tables.data.exibble) dataset, let's create a table with a number of components added. Following that, we'll apply a predefined style to the table using the [opt_stylize()](GT.opt_stylize.md#great_tables.GT.opt_stylize) method.


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


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">[exibble](data.exibble.md#great_tables.data.exibble) is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">$49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
<td class="gt_row gt_right gt_striped">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
<td class="gt_row gt_right gt_striped">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_right">$1,325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right gt_striped"></td>
<td class="gt_row gt_left gt_striped">fig</td>
<td class="gt_row gt_right gt_striped">$13.26</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777,000.00</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right"></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right gt_striped">8,880,000.00</td>
<td class="gt_row gt_left gt_striped">honeydew</td>
<td class="gt_row gt_right gt_striped">$0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This is only a subset of the dataset.</td>
</tr>
</tfoot>

</table>


The table has been stylized with the default style and color. The default style is `1` and the default color is `"blue"`. The resulting table style is a combination of color and border settings that are applied to the table.

We can modify the overall style and choose a different color theme by providing different values to the `style=` and `color=` arguments.


``` python
gt_tbl.opt_stylize(style=2, color="green")
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Data listing from <strong>exibble</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">[exibble](data.exibble.md#great_tables.data.exibble) is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_right">$49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
<td class="gt_row gt_right gt_striped">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
<td class="gt_row gt_right gt_striped">$65,100.00</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_right">$1,325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right gt_striped"></td>
<td class="gt_row gt_left gt_striped">fig</td>
<td class="gt_row gt_right gt_striped">$13.26</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777,000.00</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right"></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right gt_striped">8,880,000.00</td>
<td class="gt_row gt_left gt_striped">honeydew</td>
<td class="gt_row gt_right gt_striped">$0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This is only a subset of the dataset.</td>
</tr>
</tfoot>

</table>
