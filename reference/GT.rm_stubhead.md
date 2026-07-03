## GT.rm_stubhead()


Remove the stubhead label.


Usage

``` python
GT.rm_stubhead()
```


We can remove the stubhead label (i.e., the label positioned above the table stub) with the [rm_stubhead()](GT.rm_stubhead.md#great_tables.GT.rm_stubhead) method. This is useful when a stubhead label is present but no longer wanted.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Using a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset, we create a table with a stub and a stubhead label. The label is then removed with the [rm_stubhead()](GT.rm_stubhead.md#great_tables.GT.rm_stubhead) method.


``` python
from great_tables import GT
from great_tables.data import gtcars

gtcars_mini = gtcars[["model", "mfr", "msrp"]].head(5)

(
    GT(gtcars_mini, rowname_col="model")
    .tab_stubhead(label="car")
    .rm_stubhead()
)
```


|              | mfr     | msrp     |
|--------------|---------|----------|
| GT           | Ford    | 447000.0 |
| 458 Speciale | Ferrari | 291744.0 |
| 458 Spider   | Ferrari | 263553.0 |
| 458 Italia   | Ferrari | 233509.0 |
| 488 GTB      | Ferrari | 245400.0 |


## See Also

<a href="GT.tab_stubhead.html#great_tables.GT.tab_stubhead" class="gdls-link"><code>tab_stubhead()</code></a> to add a stubhead label to a table.
