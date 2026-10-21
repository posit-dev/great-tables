# GT.opt_footnote_spec()

Option to modify the formatting of footnote marks.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_options.py#L659-L767)

``` python
GT.opt_footnote_spec(
    spec_ref=None,
    spec_ftr=None,
)
```

Control how footnote marks are styled in two independent contexts: inline references next to cell content (`spec_ref`) and marks in the footer listing (`spec_ftr`). Each takes a compact DSL string composed of formatting codes.

The spec DSL codes are:

- `"^"`: superscript
- `"b"`: bold
- `"i"`: italic
- `"()"` or `"(x)"`: parentheses around the mark
- `"[]"` or `"[x]"`: square brackets around the mark
- `"."`: trailing period
- `"x"`: optional placeholder for readability (ignored in parsing)

## Parameters

`spec_ref: str | None = None`  
A spec string controlling the formatting of inline reference marks (marks that appear next to cell content). If `None`, the current setting is unchanged. The default value in the options system is `"^i"` (superscript + italic).

`spec_ftr: str | None = None`  
A spec string controlling the formatting of footer marks (marks that appear in the footnote listing at the bottom of the table). If `None`, the current setting is unchanged. The default value in the options system is `"^i"` (superscript + italic).

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Let's create a table with footnotes to demonstrate the spec DSL. We'll use superscript bold marks for inline references and superscript italic marks in the footer (the default).

``` python
from great_tables import GT, loc
import pandas as pd

df = pd.DataFrame({"city": ["Paris", "London", "Tokyo"], "pop_m": [2.1, 8.8, 13.9]})

(
    GT(df)
    .tab_header(title="Major Cities")
    .tab_footnote("2023 estimate", locations=loc.body(columns="pop_m", rows=[0, 1, 2]))
    .tab_footnote("Metropolitan area", locations=loc.column_labels(columns="pop_m"))
    .opt_footnote_spec(spec_ref="^b", spec_ftr="^i")
)
```

| Major Cities        |        |
|---------------------|--------|
| city                | pop_m1 |
| Paris               | 2 2.1  |
| London              | 2 8.8  |
| Tokyo               | 2 13.9 |
| 1 Metropolitan area |        |
| 2 2023 estimate     |        |

Use parenthesized marks at baseline (no superscript) in both the inline references and the footer listing.

``` python
(
    GT(df)
    .tab_header(title="Major Cities")
    .tab_footnote("2023 estimate", locations=loc.body(columns="pop_m", rows=[0, 1, 2]))
    .tab_footnote("Metropolitan area", locations=loc.column_labels(columns="pop_m"))
    .opt_footnote_spec(spec_ref="(x)", spec_ftr="(x)")
)
```

| Major Cities            |            |
|-------------------------|------------|
| city                    | pop_m(1)   |
| Paris                   | \(2\) 2.1  |
| London                  | \(2\) 8.8  |
| Tokyo                   | \(2\) 13.9 |
| \(1\) Metropolitan area |            |
| \(2\) 2023 estimate     |            |

Use superscript bold marks inline with bracketed marks and a trailing period in the footer.

``` python
(
    GT(df)
    .tab_header(title="Major Cities")
    .tab_footnote("2023 estimate", locations=loc.body(columns="pop_m", rows=[0, 1, 2]))
    .tab_footnote("Metropolitan area", locations=loc.column_labels(columns="pop_m"))
    .opt_footnote_spec(spec_ref="^b", spec_ftr="[x].")
)
```

| Major Cities             |        |
|--------------------------|--------|
| city                     | pop_m1 |
| Paris                    | 2 2.1  |
| London                   | 2 8.8  |
| Tokyo                    | 2 13.9 |
| \[1\]. Metropolitan area |        |
| \[2\]. 2023 estimate     |        |
