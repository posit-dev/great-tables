## loc.stub


Target the table stub.


Usage

``` python
loc.stub(rows=None)
```


With [loc.stub()](loc.stub.md#great_tables.loc.stub) we can target the cells containing the row labels, which reside in the table stub. This is useful for applying custom styling with the <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a> method. That method has a `locations=` argument and this class should be used there to perform the targeting.


## Parameters


`rows: RowSelectExpr = None`  
The rows to target within the stub. Can either be a single row name or a series of row names provided in a list. If no rows are specified, all rows are targeted.


## Returns


`LocStub`  
A LocStub object, which is used for a `locations=` argument if specifying the table's stub.


## Examples

Let's use a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We will style the entire table stub (the row labels) by using `locations=loc.stub()` within <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a>.


``` python
from great_tables import GT, style, loc
from great_tables.data import gtcars

(
    GT(
        gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5),
        rowname_col="model",
        groupname_col="mfr"
    )
    .tab_stubhead(label="car")
    .tab_style(
        style=[
            style.text(color="crimson", weight="bold"),
            style.fill(color="lightgray")
        ],
        locations=loc.stub()
    )
    .fmt_integer(columns=["hp", "trq"])
    .fmt_currency(columns="msrp", decimals=0)
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th id="car" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">car</th>
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
<th id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">Ford</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" style="color: crimson; font-weight: bold; background-color: lightgray">GT</td>
<td class="gt_row gt_right">647</td>
<td class="gt_row gt_right">550</td>
<td class="gt_row gt_right">$447,000</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">Ferrari</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="color: crimson; font-weight: bold; background-color: lightgray">458 Speciale</td>
<td class="gt_row gt_right">597</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$291,744</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="color: crimson; font-weight: bold; background-color: lightgray">458 Spider</td>
<td class="gt_row gt_right">562</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$263,553</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="color: crimson; font-weight: bold; background-color: lightgray">458 Italia</td>
<td class="gt_row gt_right">562</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$233,509</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="color: crimson; font-weight: bold; background-color: lightgray">488 GTB</td>
<td class="gt_row gt_right">661</td>
<td class="gt_row gt_right">561</td>
<td class="gt_row gt_right">$245,400</td>
</tr>
</tbody>
</table>
