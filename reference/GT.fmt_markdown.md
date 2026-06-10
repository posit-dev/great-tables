## GT.fmt_markdown()


Format Markdown text.


Usage

``` python
GT.fmt_markdown(
    columns=None,
    rows=None,
)
```


Any Markdown-formatted text in the incoming cells will be transformed during render when using the [fmt_markdown()](GT.fmt_markdown.md#great_tables.GT.fmt_markdown) method.


## Parameters


`columns: SelectExpr = None`  
The columns to target. Can either be a single column name or a series of column names provided in a list.

`rows: int | list[int] | None = None`  
In conjunction with `columns=`, we can specify which of their rows should undergo formatting. The default is all rows, resulting in all rows in targeted columns being formatted. Alternatively, we can supply a list of row indices.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's first create a DataFrame containing some text that is Markdown-formatted and then introduce that to <a href="GT.html#great_tables.GT" class="gdls-link"><code>GT()</code></a>. We'll then transform the [md](md.md#great_tables.md) column with the [fmt_markdown()](GT.fmt_markdown.md#great_tables.GT.fmt_markdown) method.


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


<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="gt_col_headings">
<th id="md" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">md</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left"><h5 id="this-is-markdown." class="anchored" data-anchor-id="examples">This is Markdown.</h5>
<p>Markdown's syntax is comprised entirely of punctuation characters, which punctuation characters have been carefully chosen so as to look like what they mean... assuming you've ever used email.</p></td>
</tr>
<tr>
<td class="gt_row gt_left">Info on Markdown syntax can be found [here](https://daringfireball.net/projects/markdown/).</td>
</tr>
</tbody>
</table>
