## GT.text_case_when()


Perform text replacements using a case-when approach.


Usage

``` python
GT.text_case_when(
    *cases,
    default=None,
    locations=None,
)
```


With [text_case_when()](GT.text_case_when.md#great_tables.GT.text_case_when) we supply a sequence of cases as `(predicate, replacement)` tuples. Each predicate is a function that takes the cell text (as a string) and returns `True` or `False`. The first predicate that returns `True` determines the replacement text. This is analogous to a series of if/elif statements applied to each cell.


## Parameters


`*cases: tuple[Callable[[str], bool], str]`  
One or more tuples of the form `(predicate_fn, new_text)` where `predicate_fn` is a callable that accepts a string and returns a boolean, and `new_text` is the replacement string to use when the predicate is `True`.

`default: str | None = None`  
The replacement text to use when no predicate matches. If `None` (the default), unmatched cells are left unchanged.

`locations: Loc | list[Loc] | None = None`  
The cell or set of cells to be associated with the text replacement. Supported locations include [loc.body()](loc.body.md#great_tables.loc.body), [loc.stub()](loc.stub.md#great_tables.loc.stub), [loc.row_groups()](loc.row_groups.md#great_tables.loc.row_groups), and [loc.column_labels()](loc.column_labels.md#great_tables.loc.column_labels). If `None`, defaults to [loc.body()](loc.body.md#great_tables.loc.body).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Conditionally replace cell values based on their content.


``` python
import pandas as pd
from great_tables import GT, loc

df = pd.DataFrame({"score": [95, 72, 88, 61, 100]})

(
    GT(df)
    .fmt_number(columns="score", decimals=0)
    .text_case_when(
        (lambda x: int(x) >= 90, "A"),
        (lambda x: int(x) >= 80, "B"),
        (lambda x: int(x) >= 70, "C"),
        default="F",
        locations=loc.body(columns="score"),
    )
)
```


| score |
|-------|
| A     |
| C     |
| B     |
| F     |
| A     |


Use string methods in predicates to match patterns.


``` python
from great_tables import GT, loc, exibble

(
    GT(exibble[["num", "char"]].head(4))
    .text_case_when(
        (lambda x: x.startswith("a"), "Starts with A"),
        (lambda x: len(x) > 6, "Long text"),
        default="other",
        locations=loc.body(columns="char"),
    )
)
```


| num    | char          |
|--------|---------------|
| 0.1111 | Starts with A |
| 2.222  | other         |
| 33.33  | Long text     |
| 444.4  | other         |
