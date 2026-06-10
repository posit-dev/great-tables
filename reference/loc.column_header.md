## loc.column_header


Target column spanners and column labels.


Usage

``` python
loc.column_header()
```


With [loc.column_header()](loc.column_header.md#great_tables.loc.column_header), we can target the column header which contains all of the column labels and any spanner labels that are present. This is useful for applying custom styling with the <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a> method. That method has a `locations=` argument and this class should be used there to perform the targeting.


## Returns


`LocColumnHeader`  
A LocColumnHeader object, which is used for a `locations=` argument if specifying the column header of the table.


## Examples

Let's use a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We create spanner labels through use of the <a href="GT.tab_spanner.html#great_tables.GT.tab_spanner" class="gdls-link"><code>tab_spanner()</code></a> method; this gives us a column header with a mix of column labels and spanner labels. We will style the entire column header at once by using `locations=loc.column_header()` within <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a>.


``` python
from great_tables import GT, style, loc
from great_tables.data import gtcars

(
    GT(gtcars[["mfr", "model", "hp", "trq", "msrp"]].head(5))
    .tab_spanner(
        label="performance",
        columns=["hp", "trq"]
    )
    .tab_spanner(
        label="make and model",
        columns=["mfr", "model"]
    )
    .tab_style(
        style=[
            style.text(color="white", weight="bold"),
            style.fill(color="steelblue")
        ],
        locations=loc.column_header()
    )
    .fmt_integer(columns=["hp", "trq"])
    .fmt_currency(columns="msrp", decimals=0)
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th colspan="2" id="make-and-model" class="gt_center gt_columns_top_border gt_column_spanner_outer" style="color: white; font-weight: bold; background-color: steelblue" scope="colgroup">make and model</th>
<th colspan="2" id="performance" class="gt_center gt_columns_top_border gt_column_spanner_outer" style="color: white; font-weight: bold; background-color: steelblue" scope="colgroup">performance</th>
<th rowspan="2" id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" style="color: white; font-weight: bold; background-color: steelblue" scope="col">msrp</th>
</tr>
<tr class="gt_col_headings">
<th id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" style="color: white; font-weight: bold; background-color: steelblue" scope="col">mfr</th>
<th id="model" class="gt_col_heading gt_columns_bottom_border gt_left" style="color: white; font-weight: bold; background-color: steelblue" scope="col">model</th>
<th id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" style="color: white; font-weight: bold; background-color: steelblue" scope="col">hp</th>
<th id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" style="color: white; font-weight: bold; background-color: steelblue" scope="col">trq</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_left">GT</td>
<td class="gt_row gt_right">647</td>
<td class="gt_row gt_right">550</td>
<td class="gt_row gt_right">$447,000</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Speciale</td>
<td class="gt_row gt_right">597</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$291,744</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Spider</td>
<td class="gt_row gt_right">562</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$263,553</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Italia</td>
<td class="gt_row gt_right">562</td>
<td class="gt_row gt_right">398</td>
<td class="gt_row gt_right">$233,509</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">488 GTB</td>
<td class="gt_row gt_right">661</td>
<td class="gt_row gt_right">561</td>
<td class="gt_row gt_right">$245,400</td>
</tr>
</tbody>
</table>
