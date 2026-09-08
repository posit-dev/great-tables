# GT.tab_source_note()


Add a source note citation.


Usage

``` python
GT.tab_source_note(source_note)
```


Add a source note to the footer part of the table. A source note is useful for citing the data included in the table. Several can be added to the footer, simply use the [tab_source_note()](GT.tab_source_note.md#great_tables.GT.tab_source_note) method multiple times and they will be inserted in the order provided. We can use Markdown formatting for the note, or, if the table is intended for HTML output, we can include HTML formatting.


## Parameters


`source_note: str | Text`  
Text to be used in the source note. We can optionally use the <a href="md.html#great_tables.md" class="gdls-link"><code>md()</code></a> or <a href="html.html#great_tables.html" class="gdls-link"><code>html()</code></a> helper functions to style the text as Markdown or to retain HTML elements in the text.


## Returns


`GT`  
The GT object is returned. This is the same object that the method is called on so that we can facilitate method chaining.


## Examples

With three columns from the [gtcars](data.gtcars.md#great_tables.data.gtcars) dataset, let's create a new table. We can use the [tab_source_note()](GT.tab_source_note.md#great_tables.GT.tab_source_note) method to add a source note to the table footer. Here we are citing the data source but this method can be used for any text you'd prefer to display in the footer component of the table.


``` python
from great_tables import GT
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "msrp"]].head(5)

(
    GT(gtcars_mini, rowname_col="model")
    .tab_source_note(source_note="From edmunds.com")
)
```


<style>
#ihordawgpq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ihordawgpq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ihordawgpq p { margin: 0; padding: 0; }
 #ihordawgpq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ihordawgpq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ihordawgpq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ihordawgpq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ihordawgpq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ihordawgpq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ihordawgpq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ihordawgpq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ihordawgpq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ihordawgpq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ihordawgpq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ihordawgpq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ihordawgpq .gt_spanner_row { border-bottom-style: hidden; }
 #ihordawgpq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ihordawgpq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ihordawgpq .gt_from_md> :first-child { margin-top: 0; }
 #ihordawgpq .gt_from_md> :last-child { margin-bottom: 0; }
 #ihordawgpq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ihordawgpq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ihordawgpq .gt_indent_1 { text-indent: 5px; }
 #ihordawgpq .gt_indent_2 { text-indent: calc(5px * 2); }
 #ihordawgpq .gt_indent_3 { text-indent: calc(5px * 3); }
 #ihordawgpq .gt_indent_4 { text-indent: calc(5px * 4); }
 #ihordawgpq .gt_indent_5 { text-indent: calc(5px * 5); }
 #ihordawgpq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ihordawgpq .gt_row_group_first td { border-top-width: 2px; }
 #ihordawgpq .gt_row_group_first th { border-top-width: 2px; }
 #ihordawgpq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ihordawgpq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ihordawgpq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ihordawgpq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ihordawgpq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ihordawgpq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ihordawgpq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ihordawgpq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ihordawgpq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ihordawgpq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ihordawgpq .gt_left { text-align: left; }
 #ihordawgpq .gt_center { text-align: center; }
 #ihordawgpq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ihordawgpq .gt_font_normal { font-weight: normal; }
 #ihordawgpq .gt_font_bold { font-weight: bold; }
 #ihordawgpq .gt_font_italic { font-style: italic; }
 #ihordawgpq .gt_super { font-size: 65%; }
 #ihordawgpq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ihordawgpq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ihordawgpq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ihordawgpq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ihordawgpq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ihordawgpq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="mfr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">mfr</th>
<th id="msrp" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">msrp</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<th class="gt_row gt_left gt_stub">GT</th>
<td class="gt_row gt_left">Ford</td>
<td class="gt_row gt_right">447000.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Speciale</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">291744.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Spider</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">263553.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">458 Italia</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">233509.0</td>
</tr>
<tr>
<th class="gt_row gt_left gt_stub">488 GTB</th>
<td class="gt_row gt_left">Ferrari</td>
<td class="gt_row gt_right">245400.0</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">From edmunds.com</td>
</tr>
</tfoot>

</table>
