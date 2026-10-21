# GT.tab_source_note()

Add a source note citation.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_source_notes.py#L11-L54)

``` python
GT.tab_source_note(source_note)
```

Add a source note to the footer part of the table. A source note is useful for citing the data included in the table. Several can be added to the footer, simply use the [tab_source_note()](../reference/GT.tab_source_note.md#great_tables.GT.tab_source_note) method multiple times and they will be inserted in the order provided. We can use Markdown formatting for the note, or, if the table is intended for HTML output, we can include HTML formatting.

## Parameters

`source_note: str | Text`  
Text to be used in the source note. We can optionally use the [`md()`](../reference/md.md#great_tables.md) or [`html()`](../reference/html.md#great_tables.md) helper functions to style the text as Markdown or to retain HTML elements in the text.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

With three columns from the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset, let's create a new table. We can use the [tab_source_note()](../reference/GT.tab_source_note.md#great_tables.GT.tab_source_note) method to add a source note to the table footer. Here we are citing the data source but this method can be used for any text you'd prefer to display in the footer component of the table.

``` python
from great_tables import GT
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

(
    GT(gtcars_mini, rowname_col="model")
    .tab_source_note(source_note="From edmunds.com")
)
```

|                  | mfr     | msrp     |
|------------------|---------|----------|
| GT               | Ford    | 447000.0 |
| 458 Speciale     | Ferrari | 291744.0 |
| 458 Spider       | Ferrari | 263553.0 |
| 458 Italia       | Ferrari | 233509.0 |
| 488 GTB          | Ferrari | 245400.0 |
| From edmunds.com |         |          |
