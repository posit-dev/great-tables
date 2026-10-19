# GT.tab_style()


Add custom style to one or more cells


Usage

``` python
GT.tab_style(
    style,
    locations,
)
```


With the [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) method we can target specific cells and apply styles to them. We do this with the combination of the `style` and `location` arguments. The `style` argument requires use of styling classes (e.g., `style.fill(color="red")`) and the `location` argument needs to be an expression of the cells we want to target using location targeting classes (e.g., `loc.body(columns=<column_name>)`). With the available suite of styling classes, here are some of the styles we can apply:

- the background color of the cell ([style.fill()](style.fill.md#great_tables.style.fill)'s `color`)
- the cell's text color, font, and size ([style.text()](style.text.md#great_tables.style.text)'s `color`, `font`, and `size`)
- the text style ([style.text()](style.text.md#great_tables.style.text)'s `style`), enabling the use of italics or oblique text.
- the text weight ([style.text()](style.text.md#great_tables.style.text)'s `weight`), allowing the use of thin to bold text (the degree of choice is greater with variable fonts)
- the alignment of text ([style.text()](style.text.md#great_tables.style.text)'s `align`)
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


<style>
#zaojvhywaq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zaojvhywaq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zaojvhywaq p { margin: 0; padding: 0; }
 #zaojvhywaq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zaojvhywaq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zaojvhywaq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zaojvhywaq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zaojvhywaq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zaojvhywaq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zaojvhywaq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zaojvhywaq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zaojvhywaq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zaojvhywaq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zaojvhywaq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zaojvhywaq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zaojvhywaq .gt_spanner_row { border-bottom-style: hidden; }
 #zaojvhywaq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zaojvhywaq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zaojvhywaq .gt_from_md> :first-child { margin-top: 0; }
 #zaojvhywaq .gt_from_md> :last-child { margin-bottom: 0; }
 #zaojvhywaq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zaojvhywaq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zaojvhywaq .gt_indent_1 { text-indent: 5px; }
 #zaojvhywaq .gt_indent_2 { text-indent: calc(5px * 2); }
 #zaojvhywaq .gt_indent_3 { text-indent: calc(5px * 3); }
 #zaojvhywaq .gt_indent_4 { text-indent: calc(5px * 4); }
 #zaojvhywaq .gt_indent_5 { text-indent: calc(5px * 5); }
 #zaojvhywaq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zaojvhywaq .gt_row_group_first td { border-top-width: 2px; }
 #zaojvhywaq .gt_row_group_first th { border-top-width: 2px; }
 #zaojvhywaq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zaojvhywaq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zaojvhywaq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zaojvhywaq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zaojvhywaq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zaojvhywaq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zaojvhywaq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zaojvhywaq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zaojvhywaq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zaojvhywaq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zaojvhywaq .gt_left { text-align: left; }
 #zaojvhywaq .gt_center { text-align: center; }
 #zaojvhywaq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zaojvhywaq .gt_font_normal { font-weight: normal; }
 #zaojvhywaq .gt_font_bold { font-weight: bold; }
 #zaojvhywaq .gt_font_italic { font-style: italic; }
 #zaojvhywaq .gt_super { font-size: 65%; }
 #zaojvhywaq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zaojvhywaq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zaojvhywaq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zaojvhywaq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zaojvhywaq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zaojvhywaq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

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
<th colspan="3" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" style="background-color: lightcyan" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 fctr">one</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" style="background-color: lightcyan" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" style="font-size: 22px" headers="grp_b stub-5 fctr">five</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" style="font-size: 22px" headers="grp_b stub-6 fctr">six</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" style="font-size: 22px" headers="grp_b stub-7 fctr">seven</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" style="font-size: 22px" headers="grp_b stub-8 fctr">eight</td>
</tr>
</tbody>
</table>


Let's use [exibble](data.exibble.md#great_tables.data.exibble) once again to create a simple, two-column output table (keeping only the `num` and `currency` columns). With the [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) method (called thrice), we'll add style to the values already formatted by <a href="../reference/GT.fmt_number.html#great_tables.GT.fmt_number" class="gdls-link"><code>fmt_number()</code></a> and <a href="../reference/GT.fmt_currency.html#great_tables.GT.fmt_currency" class="gdls-link"><code>fmt_currency()</code></a>. In the `style` argument of the first two [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) call, we can define multiple types of styling with the [style.fill()](style.fill.md#great_tables.style.fill) and [style.text()](style.text.md#great_tables.style.text) classes (enclosing these in a list). The cells to be targeted for styling require the use of [loc.body()](loc.body.md#great_tables.loc.body), which is used here with different columns being targeted. For the final [tab_style()](GT.tab_style.md#great_tables.GT.tab_style) call, we demonstrate the use of [style.borders()](style.borders.md#great_tables.style.borders) class as the `style` argument, which is employed in conjunction with [loc.body()](loc.body.md#great_tables.loc.body) to locate the row to be styled.


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


<style>
#vpufskxtht table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vpufskxtht thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vpufskxtht p { margin: 0; padding: 0; }
 #vpufskxtht .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vpufskxtht .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vpufskxtht .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vpufskxtht .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vpufskxtht .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vpufskxtht .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vpufskxtht .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vpufskxtht .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vpufskxtht .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vpufskxtht .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vpufskxtht .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vpufskxtht .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vpufskxtht .gt_spanner_row { border-bottom-style: hidden; }
 #vpufskxtht .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vpufskxtht .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vpufskxtht .gt_from_md> :first-child { margin-top: 0; }
 #vpufskxtht .gt_from_md> :last-child { margin-bottom: 0; }
 #vpufskxtht .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vpufskxtht .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vpufskxtht .gt_indent_1 { text-indent: 5px; }
 #vpufskxtht .gt_indent_2 { text-indent: calc(5px * 2); }
 #vpufskxtht .gt_indent_3 { text-indent: calc(5px * 3); }
 #vpufskxtht .gt_indent_4 { text-indent: calc(5px * 4); }
 #vpufskxtht .gt_indent_5 { text-indent: calc(5px * 5); }
 #vpufskxtht .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vpufskxtht .gt_row_group_first td { border-top-width: 2px; }
 #vpufskxtht .gt_row_group_first th { border-top-width: 2px; }
 #vpufskxtht .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vpufskxtht .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vpufskxtht .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vpufskxtht .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vpufskxtht .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vpufskxtht .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vpufskxtht .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vpufskxtht .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vpufskxtht .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vpufskxtht .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vpufskxtht .gt_left { text-align: left; }
 #vpufskxtht .gt_center { text-align: center; }
 #vpufskxtht .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vpufskxtht .gt_font_normal { font-weight: normal; }
 #vpufskxtht .gt_font_bold { font-weight: bold; }
 #vpufskxtht .gt_font_italic { font-style: italic; }
 #vpufskxtht .gt_super { font-size: 65%; }
 #vpufskxtht .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vpufskxtht .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vpufskxtht .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vpufskxtht .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vpufskxtht .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vpufskxtht .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

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
