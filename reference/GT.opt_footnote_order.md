# GT.opt_footnote_order()

Option to modify the ordering of footnotes.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_options.py#L832-L897)

``` python
GT.opt_footnote_order(order="marks_last")
```

Control the arrangement of marked footnotes (those attached to cells) relative to unmarked footnotes (general notes added with [tab_footnote()](../reference/GT.tab_footnote.md#great_tables.GT.tab_footnote) without `locations=`) in the footer.

## Parameters

`order: str = "marks_last"`  
The ordering mode. One of:

- `"marks_last"`: unmarked footnotes first, then marked (the default)
- `"marks_first"`: marked footnotes first, then unmarked
- `"preserve_order"`: all footnotes in the order they were added

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Let's create a table with both marked and unmarked footnotes to demonstrate the ordering modes. With `"marks_first"`, the marked footnotes appear before the unmarked ones.

``` python
from great_tables import GT, loc
import pandas as pd

df = pd.DataFrame({"city": ["Paris", "London"], "pop_m": [2.1, 8.8]})

(
    GT(df)
    .tab_header(title="Major Cities")
    .tab_footnote("2023 estimate", locations=loc.body(columns="pop_m", rows=[0, 1]))
    .tab_footnote("Rounded to nearest 100k", locations=None)
    .tab_footnote("Source: UN World Urbanization Prospects", locations=None)
    .opt_footnote_order(order="marks_first")
)
```

| Major Cities                            |       |
|-----------------------------------------|-------|
| city                                    | pop_m |
| Paris                                   | 1 2.1 |
| London                                  | 1 8.8 |
| 1 2023 estimate                         |       |
| Rounded to nearest 100k                 |       |
| Source: UN World Urbanization Prospects |       |

With `"preserve_order"`, all footnotes appear in the order they were added, and marks are assigned by insertion order rather than visual reading order.

``` python
(
    GT(df)
    .tab_header(title="Major Cities")
    .tab_footnote("2023 estimate", locations=loc.body(columns="pop_m", rows=[0, 1]))
    .tab_footnote("Source: UN World Urbanization Prospects", locations=None)
    .tab_footnote("City proper only", locations=loc.body(columns="city", rows=[0]))
    .opt_footnote_order(order="preserve_order")
)
```

| Major Cities                            |       |
|-----------------------------------------|-------|
| city                                    | pop_m |
| Paris2                                  | 1 2.1 |
| London                                  | 1 8.8 |
| 1 2023 estimate                         |       |
| Source: UN World Urbanization Prospects |       |
| 2 City proper only                      |       |
