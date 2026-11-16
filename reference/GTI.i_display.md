# GTI.i_display()

Set how the table's rows look, and whether its parts are named.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L666-L738)

``` python
GTI.i_display(
    *,
    highlight=True,
    compact=False,
    wrap=True,
    monospace=False,
    parts=False,
)
```

## Parameters

`highlight: bool = True`  
Whether the row under the pointer (or the row tapped, on a touch screen) is highlighted.

`compact: bool = False`  
Whether the rows are compact, with half of their usual padding above and below (where it hasn't been set, as with `tab_options(data_row_padding=)`).

`wrap: bool = True`  
Whether the text in cells wraps. Without wrapping, the text is on one line, cut short (with an ellipsis) if it doesn't fit, so that every row is the same height.

`monospace: bool = False`  
Whether the column labels and the cells are in a monospaced font, for a table that's a look at data more than a presentation of it (as in `GTI(preset="explorer")`). The title, the notes and the controls keep the table's font.

`parts: bool = False`  
Whether the parts GTI adds to the table (its status line, column controls, row numbers, control bar, and so on) are outlined and named over it, from the start and for good, for a page that shows readers what they are, as a docs page does. The table works as ever under the names, which follow its parts as they move. Without it, readers can name the parts themselves, with `?` or the button in the table's info panel.

## Returns

`GTI`  
The GTI object is returned.

## Examples

Here's a compact table, without highlighting.

``` python
from great_tables import GTI, exibble

GTI(exibble[["num", "char", "fctr"]]).i_display(highlight=False, compact=True)
```

| num       | char       | fctr  |
|-----------|------------|-------|
| 0.1111    | apricot    | one   |
| 2.222     | banana     | two   |
| 33.33     | coconut    | three |
| 444.4     | durian     | four  |
| 5550.0    | None       | five  |
| None      | fig        | six   |
| 777000.0  | grapefruit | seven |
| 8880000.0 | honeydew   | eight |

And one for looking through data: compact, on one line to a row, and monospaced.

``` python
GTI(exibble[["num", "char", "fctr"]]).i_display(compact=True, wrap=False, monospace=True)
```

| num       | char       | fctr  |
|-----------|------------|-------|
| 0.1111    | apricot    | one   |
| 2.222     | banana     | two   |
| 33.33     | coconut    | three |
| 444.4     | durian     | four  |
| 5550.0    | None       | five  |
| None      | fig        | six   |
| 777000.0  | grapefruit | seven |
| 8880000.0 | honeydew   | eight |

And one with its parts named, as on a page that shows them: its status line and row numbers (from [i_inspect()](../reference/GTI.i_inspect.md#great_tables.GTI.i_inspect)), its column controls, and its control bar.

``` python
(
    GTI(exibble[["num", "char", "fctr"]])
    .i_inspect()
    .i_pagination(page_size=4)
    .i_display(parts=True)
)
```

| num       | char       | fctr  |
|-----------|------------|-------|
| 0.1111    | apricot    | one   |
| 2.222     | banana     | two   |
| 33.33     | coconut    | three |
| 444.4     | durian     | four  |
| 5550.0    | None       | five  |
| None      | fig        | six   |
| 777000.0  | grapefruit | seven |
| 8880000.0 | honeydew   | eight |
