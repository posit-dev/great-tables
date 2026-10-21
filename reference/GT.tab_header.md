# GT.tab_header()

Add a table header.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_heading.py#L12-L87)

``` python
GT.tab_header(
    title,
    subtitle=None,
    preheader=None,
)
```

We can add a table header to the output table that contains a title and even a subtitle with the [tab_header()](../reference/GT.tab_header.md#great_tables.GT.tab_header) method. A table header is an optional table component that is positioned above the column labels. We have the flexibility to use Markdown or HTML formatting for the header's title and subtitle with the [`md()`](../reference/md.md#great_tables.md) and [`html()`](../reference/html.md#great_tables.md) helper functions.

## Parameters

`title: str | Text`  
Text to be used in the table title. We can elect to use the [`md()`](../reference/md.md#great_tables.md) and [`html()`](../reference/html.md#great_tables.md) helper functions to style the text as Markdown or to retain HTML elements in the text.

`subtitle: str | Text | None = None`  
Text to be used in the table subtitle. We can elect to use the [`md()`](../reference/md.md#great_tables.md) and [`html()`](../reference/html.md#great_tables.md) helper functions to style the text as Markdown or to retain HTML elements in the text.

`preheader: str | list[str] | None = None`  
Optional preheader content that is rendered above the table. Can be supplied as a list of strings.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Let's use a small portion of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset to create a table. A header part can be added to the table with the [tab_header()](../reference/GT.tab_header.md#great_tables.GT.tab_header) method. We'll add a title and the optional subtitle as well. With the [`md()`](../reference/md.md#great_tables.md) helper function, we can make sure the Markdown formatting is interpreted and transformed.

``` python
from great_tables import GT, md
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

(
    GT(gtcars_mini)
    .tab_header(
        title=md("Data listing from **gtcars**"),
        subtitle=md("`gtcars` is an R dataset")
    )
)
```

| Data listing from **gtcars** |              |          |
|------------------------------|--------------|----------|
| `gtcars` is an R dataset     |              |          |
| mfr                          | model        | msrp     |
| Ford                         | GT           | 447000.0 |
| Ferrari                      | 458 Speciale | 291744.0 |
| Ferrari                      | 458 Spider   | 263553.0 |
| Ferrari                      | 458 Italia   | 233509.0 |
| Ferrari                      | 488 GTB      | 245400.0 |

We can alternatively use the [`html()`](../reference/html.md#great_tables.md) helper function to retain HTML elements in the text.

``` python
from great_tables import GT, md, html
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

(
    GT(gtcars_mini)
    .tab_header(
        title=md("Data listing <strong>gtcars</strong>"),
        subtitle=html("From <span style='color:red;'>gtcars</span>")
    )
)
```

| Data listing **gtcars** |              |          |
|-------------------------|--------------|----------|
| From gtcars             |              |          |
| mfr                     | model        | msrp     |
| Ford                    | GT           | 447000.0 |
| Ferrari                 | 458 Speciale | 291744.0 |
| Ferrari                 | 458 Spider   | 263553.0 |
| Ferrari                 | 458 Italia   | 233509.0 |
| Ferrari                 | 488 GTB      | 245400.0 |
