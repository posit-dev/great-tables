## GT.rm_spanners()


Remove column spanners.


Usage

``` python
GT.rm_spanners(
    spanners=None,
    levels=None,
)
```


Column spanners are added with the <a href="GT.tab_spanner.html#great_tables.GT.tab_spanner" class="gdls-link"><code>tab_spanner()</code></a> method. The [rm_spanners()](GT.rm_spanners.md#great_tables.GT.rm_spanners) method allows for the removal of spanners while leaving the columns themselves intact. We can either target spanners by their ID values (with the `spanners=` argument) or by their levels (with the `levels=` argument).


## Parameters


`spanners: str | list[str] | None = None`  
The spanners to remove. Supplied as a single spanner ID or a list of spanner ID values. If `None` (the default), then all spanners will be considered for removal (subject to any constraint imposed by `levels=`).

`levels: int | list[int] | None = None`  
The spanner levels to remove, supplied as a single level or a list of levels. Spanners are placed on levels starting from `0` (the level closest to the column labels). If `None` (the default), then no levels-based constraint is applied. When supplied, only spanners residing on the specified levels (and also matching `spanners=`) are removed.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset, let's create a table with two spanners. We then remove the spanner with the ID `"performance"` while leaving the other spanner in place.


``` python
from great_tables import GT
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "hp", "trq", "mpg_c"]].head(5)

(
    GT(gtcars_mini)
    .tab_spanner(label="performance", columns=["hp", "trq"])
    .tab_spanner(label="economy", columns=["mpg_c"])
    .rm_spanners(spanners="performance")
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th rowspan="2" id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th rowspan="2" id="hp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">hp</th>
<th rowspan="2" id="trq" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">trq</th>
<th id="economy" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="col">economy</th>
</tr>
<tr class="gt_col_headings">
<th id="mpg_c" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">mpg_c</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_left">GT</td>
<td class="gt_row gt_right">647.0</td>
<td class="gt_row gt_right">550.0</td>
<td class="gt_row gt_right">11.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Speciale</td>
<td class="gt_row gt_right">597.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">13.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Spider</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">13.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Italia</td>
<td class="gt_row gt_right">562.0</td>
<td class="gt_row gt_right">398.0</td>
<td class="gt_row gt_right">13.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">488 GTB</td>
<td class="gt_row gt_right">661.0</td>
<td class="gt_row gt_right">561.0</td>
<td class="gt_row gt_right">15.0</td>
</tr>
</tbody>
</table>


## See Also

<a href="GT.tab_spanner.html#great_tables.GT.tab_spanner" class="gdls-link"><code>tab_spanner()</code></a> to add a spanner to a table.
