# GT.tab_stubhead()

Add label text to the stubhead.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_stubhead.py#L11-L78)

``` python
GT.tab_stubhead(label)
```

Add a label to the stubhead of a table. The stubhead is the lone element that is positioned left of the column labels, and above the stub. If a stub does not exist, then there is no stubhead (so no change will be made when using this method in that case). We have the flexibility to use Markdown formatting for the stubhead label (through use of the [`md()`](../reference/md.md#great_tables.md) helper function). Furthermore, we can use HTML for the stubhead label so long as we also use the [`html()`](../reference/html.md#great_tables.md) helper function.

## Parameters

`label: str | Text | list[str | Text]`  
The text to be used as the stubhead label. We can optionally use the [`md()`](../reference/md.md#great_tables.md) and [`html()`](../reference/html.md#great_tables.md) helper functions to style the text as Markdown or to retain HTML elements in the text. With a hierarchical stub (where `rowname_col=` is a list of columns), a single label spans all of the stub columns; alternatively, a list of labels can be provided, one per stub column (outermost first).

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Using a small subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset, we can create a table with row labels. Since we have row labels in the stub (via use of `rowname_col="model"` in the [GT()](../reference/GT.md#great_tables.GT) call) we have a stubhead, so, let's add a stubhead label (`"car"`) with the [tab_stubhead()](../reference/GT.tab_stubhead.md#great_tables.GT.tab_stubhead) method to describe what's in the stub.

``` python
from great_tables import GT
from great_tables.data import gtcars

gtcars_mini = gtcars[["model", "year", "hp", "trq"]].head(5)

(
    GT(gtcars_mini, rowname_col="model")
    .tab_stubhead(label="car")
)
```

| car          | year | hp    | trq   |
|--------------|------|-------|-------|
| GT           | 2017 | 647.0 | 550.0 |
| 458 Speciale | 2015 | 597.0 | 398.0 |
| 458 Spider   | 2015 | 562.0 | 398.0 |
| 458 Italia   | 2014 | 562.0 | 398.0 |
| 488 GTB      | 2016 | 661.0 | 561.0 |

We can also use Markdown formatting for the stubhead label. In this example, we'll use `md("*Car*")` to make the label italicized.

``` python
from great_tables import GT, md
from great_tables.data import gtcars

(
    GT(gtcars_mini, rowname_col="model")
    .tab_stubhead(label=md("*Car*"))
)
```

| *Car*        | year | hp    | trq   |
|--------------|------|-------|-------|
| GT           | 2017 | 647.0 | 550.0 |
| 458 Speciale | 2015 | 597.0 | 398.0 |
| 458 Spider   | 2015 | 562.0 | 398.0 |
| 458 Italia   | 2014 | 562.0 | 398.0 |
| 488 GTB      | 2016 | 661.0 | 561.0 |
