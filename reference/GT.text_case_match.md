## GT.text_case_match()


Perform text replacements with a switch-like approach.


Usage

``` python
GT.text_case_match(
    *cases,
    default=None,
    replace="all",
    locations=None,
)
```


With [text_case_match()](GT.text_case_match.md#great_tables.GT.text_case_match) we can supply a sequence of matching cases in the form of `(old_text, new_text)` tuples. Each tuple's first element specifies text to match (either a single string or a list of strings) and the second element provides the replacement. By default, the matching is performed on the entire cell text (`replace="all"`); use `replace="partial"` for substring matching and replacement.


## Parameters


`*cases: tuple[str | list[str], str]`  
One or more tuples of the form `(old_text, new_text)` where `old_text` is a string or list of strings to match, and `new_text` is the replacement string.

`default: str | None = None`  
The replacement text to use when cell values aren't matched by any of the supplied cases. If `None` (the default), unmatched cells are left unchanged.

`replace: Literal[``"all", `<span class="st">`"partial"``]`</span>` = ``"all"`  
The method for text replacement. Use `"all"` (the default) to match and replace the entire cell text, or `"partial"` to match and replace substrings within the cell text.

`locations: Loc | list[Loc] | None = None`  
The cell or set of cells to be associated with the text replacement. Supported locations include [loc.body()](loc.body.md#great_tables.loc.body), [loc.stub()](loc.stub.md#great_tables.loc.stub), [loc.row_groups()](loc.row_groups.md#great_tables.loc.row_groups), and [loc.column_labels()](loc.column_labels.md#great_tables.loc.column_labels). If `None`, defaults to [loc.body()](loc.body.md#great_tables.loc.body).


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Replace specific cell values in the `char` column with different text.


``` python
from great_tables import GT, loc, exibble

(
    GT(exibble[["num", "char"]].head(4))
    .text_case_match(
        ("apricot", "APRICOT"),
        (["banana", "coconut"], "tropical fruit"),
        default="other",
        locations=loc.body(columns="char"),
    )
)
```


| num    | char           |
|--------|----------------|
| 0.1111 | APRICOT        |
| 2.222  | tropical fruit |
| 33.33  | tropical fruit |
| 444.4  | other          |


Use `replace="partial"` to perform substring replacements.


``` python
from great_tables import GT, loc, exibble

(
    GT(exibble[["num", "char"]].head(4))
    .text_case_match(
        ("an", "@"),
        replace="partial",
        locations=loc.body(columns="char"),
    )
)
```


| num    | char    |
|--------|---------|
| 0.1111 | apricot |
| 2.222  | b@@a    |
| 33.33  | coconut |
| 444.4  | duri@   |
