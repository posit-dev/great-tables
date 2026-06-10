## GT.opt_all_caps()


Option to use all caps in select table locations.


Usage

``` python
GT.opt_all_caps(
    all_caps=True,
    locations=None,
)
```


Sometimes an all-capitalized look is suitable for a table. By using [opt_all_caps()](GT.opt_all_caps.md#great_tables.GT.opt_all_caps), we can transform characters in the column labels, the stub, and in all row groups in this way (and there's control over which of these locations are transformed). This method serves as a convenient shortcut for `tab_options(<location>_text_transform="uppercase", <location>_font_size="80%", <location>_font_weight="bolder")` (for all `locations` selected).


## Parameters


`all_caps: bool = ``True`  
Indicates whether the text transformation to all caps should be performed (`True`, the default) or reset to default values (`False`) for the `locations` targeted.

`locations: (`  
`    type[LocColumnLabels]`  
`    | type[LocRowGroups]`  
`    | type[LocStub]`  
`    | list[type[LocColumnLabels] | type[LocRowGroups] | type[LocStub]]`  
`    | str`  
`    | list[str]`  
`    | None`  
`)`  
`= None`  
Which locations should undergo this text transformation? By default it includes all of the [loc.column_labels](loc.column_labels.md#great_tables.loc.column_labels), the [loc.stub](loc.stub.md#great_tables.loc.stub), and the [loc.row_groups](loc.row_groups.md#great_tables.loc.row_groups) locations. However, we could just choose one or two of those.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using select columns from the [exibble](data.exibble.md#great_tables.data.exibble) dataset, let's create a table with a number of components added. Following that, we'll ensure that all text in the column labels, the stub, and in all row groups is transformed to all caps using the [opt_all_caps()](GT.opt_all_caps.md#great_tables.GT.opt_all_caps) method.


``` python
from great_tables import GT, exibble, loc, md

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
  .opt_all_caps()
)
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
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">$65,100.00</td>
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
<td class="gt_row gt_right"></td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">$13.26</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777,000.00</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right"></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right">8,880,000.00</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">$0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This is only a subset of the dataset.</td>
</tr>
</tfoot>

</table>


[opt_all_caps()](GT.opt_all_caps.md#great_tables.GT.opt_all_caps) accepts a `locations` parameter that allows us to specify which components should be transformed. For example, if we only want to ensure that all text in the stub and all row groups is converted to all caps:


``` python
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
  .opt_all_caps(locations=[loc.stub, loc.row_groups])
)
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
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_right">$17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_right">$1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_right">$65,100.00</td>
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
<td class="gt_row gt_right"></td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_right">$13.26</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777,000.00</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_right"></td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right">8,880,000.00</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_right">$0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">This is only a subset of the dataset.</td>
</tr>
</tfoot>

</table>
