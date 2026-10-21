# GT.rm_source_notes()

Remove table source notes.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_rm.py#L90-L142)

``` python
GT.rm_source_notes(source_notes=None)
```

Source notes are added to the footer part of the table with the [`tab_source_note()`](../reference/GT.tab_source_note.md#great_tables.GT.tab_source_note) method. With [rm_source_notes()](../reference/GT.rm_source_notes.md#great_tables.GT.rm_source_notes) we can remove all of them at once or, by supplying the `source_notes=` argument, only those at specific indices.

## Parameters

`source_notes: int | list[int] | None = None`  
The source notes to remove. Supplied as a single index or a list of indices (`0`-based, in the order the source notes were added). If `None` (the default), then all source notes will be removed.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Using a subset of the [gtcars](../reference/data.gtcars.md#great_tables.data.gtcars) dataset, let's create a table with two source notes. We then remove the first of the two with the `source_notes=` argument.

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

| mfr            | model        | msrp     |
|----------------|--------------|----------|
| Ford           | GT           | 447000.0 |
| Ferrari        | 458 Speciale | 291744.0 |
| Ferrari        | 458 Spider   | 263553.0 |
| Ferrari        | 458 Italia   | 233509.0 |
| Ferrari        | 488 GTB      | 245400.0 |
| Prices in USD. |              |          |

## See Also

[`tab_source_note()`](../reference/GT.tab_source_note.md#great_tables.GT.tab_source_note) to add a source note to a table.  
