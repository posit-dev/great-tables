## loc.column_labels


Target column labels.


Usage

``` python
loc.column_labels(columns=None)
```


With [loc.column_labels()](loc.column_labels.md#great_tables.loc.column_labels), we can target the cells containing the column labels. This is useful for applying custom styling with the <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a> method. That method has a `locations=` argument and this class should be used there to perform the targeting.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list. If no columns are specified, all columns are targeted.


## Returns


`LocColumnLabels`  
A LocColumnLabels object, which is used for a `locations=` argument if specifying the table's column labels.


## Examples

Let's use a subset of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset in a new table. We will style all three of the column labels by using `locations=loc.column_labels()` within <a href="GT.tab_style.html#great_tables.GT.tab_style" class="gdls-link"><code>tab_style()</code></a>. Note that no specification of `columns=` is needed here because we want to target all columns.


``` python
from great_tables import GT, style, loc
from great_tables.data import gtcars

(
    GT(gtcars[["mfr", "model", "msrp"]].head(5))
    .tab_style(
        style=style.text(color="blue", size="large", weight="bold"),
        locations=loc.column_labels()
    )
)
```


| mfr     | model        | msrp     |
|---------|--------------|----------|
| Ford    | GT           | 447000.0 |
| Ferrari | 458 Speciale | 291744.0 |
| Ferrari | 458 Spider   | 263553.0 |
| Ferrari | 458 Italia   | 233509.0 |
| Ferrari | 488 GTB      | 245400.0 |
