## GT.tab_source_note()


Add a source note citation.


Usage

``` python
GT.tab_source_note(source_note)
```


Add a source note to the footer part of the table. A source note is useful for citing the data included in the table. Several can be added to the footer, simply use the [tab_source_note()](GT.tab_source_note.md#great_tables.GT.tab_source_note) method multiple times and they will be inserted in the order provided. We can use Markdown formatting for the note, or, if the table is intended for HTML output, we can include HTML formatting.


## Parameters


`source_note: str | Text`  
Text to be used in the source note. We can optionally use the <a href="md.html#great_tables.md" class="gdls-link"><code>md()</code></a> or <a href="html.html#great_tables.html" class="gdls-link"><code>html()</code></a> helper functions to style the text as Markdown or to retain HTML elements in the text.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

With three columns from the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset, let's create a new table. We can use the [tab_source_note()](GT.tab_source_note.md#great_tables.GT.tab_source_note) method to add a source note to the table footer. Here we are citing the data source but this method can be used for any text you'd prefer to display in the footer component of the table.


``` python
from great_tables import GT
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

(
    GT(gtcars_mini, rowname_col="model")
    .tab_source_note(source_note="From edmunds.com")
)
```


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">GT</th>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_right">447000.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Speciale</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">291744.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Spider</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">263553.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Italia</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">233509.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">488 GTB</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">245400.0</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">From edmunds.com</td>
</tr>
</tfoot>

</table>
