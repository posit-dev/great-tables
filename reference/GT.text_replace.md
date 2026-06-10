## GT.text_replace()


Perform targeted text replacement with a regex pattern.


Usage

``` python
GT.text_replace(
    pattern,
    replacement,
    locations=None,
)
```


With [text_replace()](GT.text_replace.md#great_tables.GT.text_replace) we can target cells in specific locations and replace text fragments matching a regular expression pattern. This operates on the already-formatted cell content (i.e., after `fmt_*()` methods have been applied).


## Parameters


`pattern: str`  
A regex pattern used to target text fragments in the resolved cells.

`replacement: str`  
The replacement text for any matched text fragments. Backreferences (e.g., `"\\1"`) can be used to refer to capture groups in the pattern.

`locations: Loc | list[Loc] | None = None`  
The cell or set of cells to be associated with the text replacement. Supported locations include [loc.body()](loc.body.md#great_tables.loc.body), [loc.stub()](loc.stub.md#great_tables.loc.stub), [loc.row_groups()](loc.row_groups.md#great_tables.loc.row_groups), and [loc.column_labels()](loc.column_labels.md#great_tables.loc.column_labels). If `None`, defaults to [loc.body()](loc.body.md#great_tables.loc.body).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Use [text_replace()](GT.text_replace.md#great_tables.GT.text_replace) to add HTML emphasis tags around text in parentheses.


``` python
import pandas as pd
from great_tables import GT, loc

df = pd.DataFrame({"item": ["Column A (details)", "Colum B (info)"], "value": [1, 2]})

(
    GT(df)
    .text_replace(
        pattern=r"\((.+?)\)",
        replacement=r"(<em>\1</em>)",
        locations=loc.body(columns="item"),
    )
)
```


| item                 | value |
|----------------------|-------|
| Column A (*details*) | 1     |
| Colum B (*info*)     | 2     |


Replace underscores with spaces in the stub (row labels).


``` python
from great_tables import GT, loc, exibble

(
    GT(exibble[["num", "char", "row"]].head(4), rowname_col="row")
    .text_replace(pattern="_", replacement=" ", locations=loc.stub())
)
```


|       | num    | char    |
|-------|--------|---------|
| row 1 | 0.1111 | apricot |
| row 2 | 2.222  | banana  |
| row 3 | 33.33  | coconut |
| row 4 | 444.4  | durian  |
