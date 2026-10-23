# GT.fmt_passthrough()

Format values by passing them through, optionally escaping and decorating.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_formats.py#L9637-L9728)

``` python
GT.fmt_passthrough(
    columns=None,
    rows=None,
    escape=True,
    pattern="{x}",
)
```

The [fmt_passthrough()](../reference/GT.fmt_passthrough.md#great_tables.GT.fmt_passthrough) method allows you to mark cells as formatted without transforming them. This is useful in two situations:

- **Escaping**: When `escape=True` (the default), special characters in cell values are escaped for the output context (HTML or LaTeX). This protects against cross-site scripting (XSS) while giving you explicit control over which cells are escaped.
- **Decoration**: The `pattern=` argument lets you wrap values in a text pattern (e.g., `pattern="[{x}]"`) without changing the underlying value.

Since [fmt_passthrough()](../reference/GT.fmt_passthrough.md#great_tables.GT.fmt_passthrough) marks cells as formatted, they are no longer subject to the automatic escaping that applies to unformatted cells. Setting `escape=False` is the way to include raw HTML or LaTeX in cell values without using the [html()](../reference/html.md#great_tables.md) helper.

## Parameters

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

`escape: bool = True`  
Should the cell values be escaped for the output context? When `True` (the default), HTML special characters like `<`, `>`, and `&` are escaped in HTML output, and LaTeX special characters are escaped in LaTeX output. Set to `False` to pass values through without escaping, which is useful when cell values already contain trusted HTML or LaTeX markup.

`pattern: str = "{x}"`  
A formatting pattern that allows for decoration of the formatted value. The formatted value is represented by `{x}` (which can be used multiple times, if needed) and all other characters will be interpreted as string literals.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples

Using [fmt_passthrough()](../reference/GT.fmt_passthrough.md#great_tables.GT.fmt_passthrough) with `escape=True` (the default) to safely render user-supplied data:

``` python
from great_tables import GT
import pandas as pd

df = pd.DataFrame({"input": ["<b>bold</b>", "x & y", "normal text"]})

GT(df).fmt_passthrough(columns="input")
```

| input           |
|-----------------|
| \<b\>bold\</b\> |
| x & y           |
| normal text     |

Using `pattern=` to decorate values without otherwise changing them:

``` python
from great_tables import GT
import pandas as pd

df = pd.DataFrame({"code": ["ABC", "DEF", "GHI"]})

GT(df).fmt_passthrough(columns="code", pattern="[{x}]")
```

| code    |
|---------|
| \[ABC\] |
| \[DEF\] |
| \[GHI\] |

Using `escape=False` to pass through trusted HTML:

``` python
from great_tables import GT
import pandas as pd

df = pd.DataFrame({"content": ["<b>bold</b>", "<em>italic</em>"]})

GT(df).fmt_passthrough(columns="content", escape=False)
```

| content  |
|----------|
| **bold** |
| *italic* |
