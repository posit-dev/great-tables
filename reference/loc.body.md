## loc.body


Target data cells in the table body.


Usage

``` python
loc.body(
    columns=None,
    rows=None,
    mask=None,
)
```


With [loc.body()](loc.body.md#great_tables.loc.body), we can target the data cells in the table body. This is useful for applying custom styling with the <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a> method. That method has a `locations=` argument and this class should be used there to perform the targeting.

> **Warning: Warning**
>
> `mask=` is still experimental.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
The rows to target. Can either be a single row name or a series of row names provided in a list.

`mask: PlExpr | None = None`  
The cells to target. If the underlying wrapped DataFrame is a Polars DataFrame, you can pass a Polars expression for cell-based selection. This argument must be used exclusively and cannot be combined with the `columns=` or `rows=` arguments.


## Returns


`LocBody`  
A LocBody object, which is used for a `locations=` argument if specifying the table body.


## Examples

Let's use a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We will style all of the body cells by using `locations=loc.body()` within <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a>.


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
            style.text(color="darkblue", weight="bold"),
            style.fill(color="gainsboro")
        ],
        locations=loc.body()
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
<td class="gt_row gt_left gt_stub">GT</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">647</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">550</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">$447,000</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">Ferrari</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Speciale</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">597</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">398</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">$291,744</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Spider</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">562</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">398</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">$263,553</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">458 Italia</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">562</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">398</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">$233,509</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">488 GTB</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">661</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">561</td>
<td class="gt_row gt_right" style="color: darkblue; font-weight: bold; background-color: gainsboro">$245,400</td>
</tr>
</tbody>
</table>
