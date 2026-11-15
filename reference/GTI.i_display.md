# GTI.i_display()

Set how the table's rows look.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/gti.py#L658-L710)

``` python
GTI.i_display(
    *,
    highlight=True,
    compact=False,
    wrap=True,
    monospace=False,
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
