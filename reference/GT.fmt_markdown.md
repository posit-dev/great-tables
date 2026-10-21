# GT.fmt_markdown()

Format Markdown text.

Usage

[Source](https://github.com/posit-dev/great-tables/blob/main/great_tables/_formats.py#L6295-L6360)

``` python
GT.fmt_markdown(
    columns=None,
    rows=None,
)
```

Any Markdown-formatted text in the incoming cells will be transformed during render when using the [`fmt_markdown()`](../reference/GT.fmt_markdown.md#great_tables.GT.fmt_markdown) method.

## Parameters

`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: RowSelectExpr = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a row index, a list of row indices, or (for Polars DataFrames) a Polars expression such as `pl.col("x") > 0`.

## Returns

`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.

## Examples:

Let's first create a DataFrame containing some text that is Markdown-formatted and then introduce that to [`GT()`](../reference/GT.md#great_tables.GT). We'll then transform the [md](../reference/md.md#great_tables.md) column with the [`fmt_markdown()`](../reference/GT.fmt_markdown.md#great_tables.GT.fmt_markdown) method.

``` python
import pandas as pd
from great_tables import GT
from great_tables.data import towny

text_1 = """
### This is Markdown.

Markdown's syntax is comprised entirely of
punctuation characters, which punctuation
characters have been carefully chosen so as
to look like what they mean... assuming
you've ever used email.
"""

text_2 = """
Info on Markdown syntax can be found
[here](https://daringfireball.net/projects/markdown/).
"""

df = pd.DataFrame({"md": [text_1, text_2]})

(GT(df).fmt_markdown("md"))
```

| md |
|----|
| This is Markdown. Markdown's syntax is comprised entirely of punctuation characters, which punctuation characters have been carefully chosen so as to look like what they mean... assuming you've ever used email. |
| Info on Markdown syntax can be found [here](https://daringfireball.net/projects/markdown/). |
