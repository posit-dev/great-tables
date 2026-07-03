## GT.rm_source_notes()


Remove table source notes.


Usage

``` python
GT.rm_source_notes(source_notes=None)
```


Source notes are added to the footer part of the table with the <a href="GT.tab_source_note.html#great_tables.GT.tab_source_note" class="gdls-link"><code>tab_source_note()</code></a> method. With [rm_source_notes()](GT.rm_source_notes.md#great_tables.GT.rm_source_notes) we can remove all of them at once or, by supplying the `source_notes=` argument, only those at specific indices.


## Parameters


`source_notes: int | list[int] | None = None`  
The source notes to remove. Supplied as a single index or a list of indices (`0`-based, in the order the source notes were added). If `None` (the default), then all source notes will be removed.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset, let's create a table with two source notes. We then remove the first of the two with the `source_notes=` argument.


``` python
from great_tables import GT
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

(
    GT(gtcars_mini)
    .tab_source_note(source_note="From edmunds.com")
    .tab_source_note(source_note="Prices in USD.")
    .rm_source_notes(source_notes=0)
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_left">GT</td>
<td class="gt_row gt_right">447000.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Speciale</td>
<td class="gt_row gt_right">291744.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Spider</td>
<td class="gt_row gt_right">263553.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Italia</td>
<td class="gt_row gt_right">233509.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">488 GTB</td>
<td class="gt_row gt_right">245400.0</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">Prices in USD.</td>
</tr>
</tfoot>

</table>


## See Also

<a href="GT.tab_source_note.html#great_tables.GT.tab_source_note" class="gdls-link"><code>tab_source_note()</code></a> to add a source note to a table.
