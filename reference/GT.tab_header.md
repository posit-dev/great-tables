# GT.tab_header()


Add a table header.


Usage

``` python
GT.tab_header(
    title,
    subtitle=None,
    preheader=None,
)
```


We can add a table header to the output table that contains a title and even a subtitle with the [tab_header()](GT.tab_header.md#great_tables.GT.tab_header) method. A table header is an optional table component that is positioned above the column labels. We have the flexibility to use Markdown or HTML formatting for the header's title and subtitle with the <a href="../reference/md.html#great_tables.md" class="gdls-link"><code>md()</code></a> and <a href="../reference/html.html#great_tables.html" class="gdls-link"><code>html()</code></a> helper functions.


## Parameters


`title: str | Text`  
Text to be used in the table title. We can elect to use the <a href="../reference/md.html#great_tables.md" class="gdls-link"><code>md()</code></a> and <a href="../reference/html.html#great_tables.html" class="gdls-link"><code>html()</code></a> helper functions to style the text as Markdown or to retain HTML elements in the text.

`subtitle: str | Text | None = None`  
Text to be used in the table subtitle. We can elect to use the <a href="../reference/md.html#great_tables.md" class="gdls-link"><code>md()</code></a> and <a href="../reference/html.html#great_tables.html" class="gdls-link"><code>html()</code></a> helper functions to style the text as Markdown or to retain HTML elements in the text.

`preheader: str | list[str] | None = None`  
Optional preheader content that is rendered above the table. Can be supplied as a list of strings.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

Let's use a small portion of the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset to create a table. A header part can be added to the table with the [tab_header()](GT.tab_header.md#great_tables.GT.tab_header) method. We'll add a title and the optional subtitle as well. With the <a href="../reference/md.html#great_tables.md" class="gdls-link"><code>md()</code></a> helper function, we can make sure the Markdown formatting is interpreted and transformed.


``` python
from great_tables import GT, md
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

(
    GT(gtcars_mini)
    .tab_header(
        title=md("Data listing from **gtcars**"),
        subtitle=md("`gtcars` is an R dataset")
    )
)
```


<style>
#exnlqeclyc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#exnlqeclyc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#exnlqeclyc p { margin: 0; padding: 0; }
 #exnlqeclyc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #exnlqeclyc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #exnlqeclyc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #exnlqeclyc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #exnlqeclyc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #exnlqeclyc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #exnlqeclyc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #exnlqeclyc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #exnlqeclyc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #exnlqeclyc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #exnlqeclyc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #exnlqeclyc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #exnlqeclyc .gt_spanner_row { border-bottom-style: hidden; }
 #exnlqeclyc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #exnlqeclyc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #exnlqeclyc .gt_from_md> :first-child { margin-top: 0; }
 #exnlqeclyc .gt_from_md> :last-child { margin-bottom: 0; }
 #exnlqeclyc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #exnlqeclyc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #exnlqeclyc .gt_indent_1 { text-indent: 5px; }
 #exnlqeclyc .gt_indent_2 { text-indent: calc(5px * 2); }
 #exnlqeclyc .gt_indent_3 { text-indent: calc(5px * 3); }
 #exnlqeclyc .gt_indent_4 { text-indent: calc(5px * 4); }
 #exnlqeclyc .gt_indent_5 { text-indent: calc(5px * 5); }
 #exnlqeclyc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #exnlqeclyc .gt_row_group_first td { border-top-width: 2px; }
 #exnlqeclyc .gt_row_group_first th { border-top-width: 2px; }
 #exnlqeclyc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #exnlqeclyc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #exnlqeclyc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #exnlqeclyc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #exnlqeclyc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #exnlqeclyc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #exnlqeclyc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #exnlqeclyc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #exnlqeclyc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #exnlqeclyc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #exnlqeclyc .gt_left { text-align: left; }
 #exnlqeclyc .gt_center { text-align: center; }
 #exnlqeclyc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #exnlqeclyc .gt_font_normal { font-weight: normal; }
 #exnlqeclyc .gt_font_bold { font-weight: bold; }
 #exnlqeclyc .gt_font_italic { font-style: italic; }
 #exnlqeclyc .gt_super { font-size: 65%; }
 #exnlqeclyc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #exnlqeclyc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #exnlqeclyc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #exnlqeclyc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #exnlqeclyc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #exnlqeclyc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from <strong>gtcars</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border"><code>gtcars</code> is an R dataset</th>
</tr>
<tr class="gt_col_headings">
<th id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_left">GT</td>
<td class="gt_row gt_right">447000.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Speciale</td>
<td class="gt_row gt_right">291744.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Spider</td>
<td class="gt_row gt_right">263553.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Italia</td>
<td class="gt_row gt_right">233509.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">488 GTB</td>
<td class="gt_row gt_right">245400.0</td>
</tr>
</tbody>
</table>


We can alternatively use the <a href="../reference/html.html#great_tables.html" class="gdls-link"><code>html()</code></a> helper function to retain HTML elements in the text.


``` python
from great_tables import GT, md, html
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

(
    GT(gtcars_mini)
    .tab_header(
        title=md("Data listing <strong>gtcars</strong>"),
        subtitle=html("From <span style='color:red;'>gtcars</span>")
    )
)
```


<style>
#zwrrbycoln table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zwrrbycoln thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zwrrbycoln p { margin: 0; padding: 0; }
 #zwrrbycoln .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zwrrbycoln .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zwrrbycoln .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zwrrbycoln .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zwrrbycoln .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zwrrbycoln .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zwrrbycoln .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zwrrbycoln .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zwrrbycoln .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zwrrbycoln .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zwrrbycoln .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zwrrbycoln .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zwrrbycoln .gt_spanner_row { border-bottom-style: hidden; }
 #zwrrbycoln .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zwrrbycoln .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zwrrbycoln .gt_from_md> :first-child { margin-top: 0; }
 #zwrrbycoln .gt_from_md> :last-child { margin-bottom: 0; }
 #zwrrbycoln .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zwrrbycoln .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zwrrbycoln .gt_indent_1 { text-indent: 5px; }
 #zwrrbycoln .gt_indent_2 { text-indent: calc(5px * 2); }
 #zwrrbycoln .gt_indent_3 { text-indent: calc(5px * 3); }
 #zwrrbycoln .gt_indent_4 { text-indent: calc(5px * 4); }
 #zwrrbycoln .gt_indent_5 { text-indent: calc(5px * 5); }
 #zwrrbycoln .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zwrrbycoln .gt_row_group_first td { border-top-width: 2px; }
 #zwrrbycoln .gt_row_group_first th { border-top-width: 2px; }
 #zwrrbycoln .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zwrrbycoln .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zwrrbycoln .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zwrrbycoln .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zwrrbycoln .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zwrrbycoln .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zwrrbycoln .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zwrrbycoln .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zwrrbycoln .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zwrrbycoln .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zwrrbycoln .gt_left { text-align: left; }
 #zwrrbycoln .gt_center { text-align: center; }
 #zwrrbycoln .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zwrrbycoln .gt_font_normal { font-weight: normal; }
 #zwrrbycoln .gt_font_bold { font-weight: bold; }
 #zwrrbycoln .gt_font_italic { font-style: italic; }
 #zwrrbycoln .gt_super { font-size: 65%; }
 #zwrrbycoln .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zwrrbycoln .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zwrrbycoln .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zwrrbycoln .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zwrrbycoln .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zwrrbycoln .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing <strong>gtcars</strong></th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">From <span style="color:red;">gtcars</span></th>
</tr>
<tr class="gt_col_headings">
<th id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th id="model" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">model</th>
<th id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_left">GT</td>
<td class="gt_row gt_right">447000.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Speciale</td>
<td class="gt_row gt_right">291744.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Spider</td>
<td class="gt_row gt_right">263553.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">458 Italia</td>
<td class="gt_row gt_right">233509.0</td>
</tr>
<tr>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_left">488 GTB</td>
<td class="gt_row gt_right">245400.0</td>
</tr>
</tbody>
</table>
