# GT.fmt_markdown()


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


<style>
#sbftzbmneg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sbftzbmneg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sbftzbmneg p { margin: 0; padding: 0; }
 #sbftzbmneg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sbftzbmneg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sbftzbmneg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sbftzbmneg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sbftzbmneg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sbftzbmneg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sbftzbmneg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sbftzbmneg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sbftzbmneg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sbftzbmneg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sbftzbmneg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sbftzbmneg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sbftzbmneg .gt_spanner_row { border-bottom-style: hidden; }
 #sbftzbmneg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sbftzbmneg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sbftzbmneg .gt_from_md> :first-child { margin-top: 0; }
 #sbftzbmneg .gt_from_md> :last-child { margin-bottom: 0; }
 #sbftzbmneg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sbftzbmneg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sbftzbmneg .gt_indent_1 { text-indent: 5px; }
 #sbftzbmneg .gt_indent_2 { text-indent: calc(5px * 2); }
 #sbftzbmneg .gt_indent_3 { text-indent: calc(5px * 3); }
 #sbftzbmneg .gt_indent_4 { text-indent: calc(5px * 4); }
 #sbftzbmneg .gt_indent_5 { text-indent: calc(5px * 5); }
 #sbftzbmneg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sbftzbmneg .gt_row_group_first td { border-top-width: 2px; }
 #sbftzbmneg .gt_row_group_first th { border-top-width: 2px; }
 #sbftzbmneg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sbftzbmneg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sbftzbmneg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sbftzbmneg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sbftzbmneg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sbftzbmneg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sbftzbmneg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sbftzbmneg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sbftzbmneg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sbftzbmneg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sbftzbmneg .gt_left { text-align: left; }
 #sbftzbmneg .gt_center { text-align: center; }
 #sbftzbmneg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sbftzbmneg .gt_font_normal { font-weight: normal; }
 #sbftzbmneg .gt_font_bold { font-weight: bold; }
 #sbftzbmneg .gt_font_italic { font-style: italic; }
 #sbftzbmneg .gt_super { font-size: 65%; }
 #sbftzbmneg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sbftzbmneg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sbftzbmneg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sbftzbmneg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sbftzbmneg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sbftzbmneg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

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
<td class="gt_row gt_left"><h3 id="this-is-markdown." class="anchored">This is Markdown.</h3>
<p>Markdown's syntax is comprised entirely of punctuation characters, which punctuation characters have been carefully chosen so as to look like what they mean... assuming you've ever used email.</p></td>
</tr>
<tr>
<td class="gt_row gt_left">Info on Markdown syntax can be found [here](https://daringfireball.net/projects/markdown/).</td>
</tr>
</tbody>
</table>
