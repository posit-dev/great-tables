## GT.rm_footnotes()


Remove table footnotes.


Usage

``` python
GT.rm_footnotes(footnotes=None)
```


Footnotes are added to targeted locations with the <a href="GT.tab_footnote.html#great_tables.GT.tab_footnote" class="gdls-link"><code>tab_footnote()</code></a> method. With [rm_footnotes()](GT.rm_footnotes.md#great_tables.GT.rm_footnotes) we can remove all of them at once or, by supplying the `footnotes=` argument, only those at specific indices.


## Parameters


`footnotes: int | list[int] | None = None`  
The footnotes to remove. Supplied as a single index or a list of indices (`0`-based, in the order the footnotes were added). If `None` (the default), then all footnotes will be removed.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset, let's create a table with two footnotes. We then remove all footnotes by calling [rm_footnotes()](GT.rm_footnotes.md#great_tables.GT.rm_footnotes) without any arguments.


``` python
from great_tables import GT
from great_tables.loc import body
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

(
    GT(gtcars_mini)
    .tab_footnote(footnote="Manufacturer.", locations=body(columns="mfr", rows=[0]))
    .tab_footnote(footnote="Price.", locations=body(columns="msrp", rows=[0]))
    .rm_footnotes()
)
```


| mfr     | model        | msrp     |
|---------|--------------|----------|
| Ford    | GT           | 447000.0 |
| Ferrari | 458 Speciale | 291744.0 |
| Ferrari | 458 Spider   | 263553.0 |
| Ferrari | 458 Italia   | 233509.0 |
| Ferrari | 488 GTB      | 245400.0 |


## See Also

<a href="GT.tab_footnote.html#great_tables.GT.tab_footnote" class="gdls-link"><code>tab_footnote()</code></a> to add a footnote to a table.
