# Header, Footer, and Stub

Three structural components frame the data in your table: the **Table Header** introduces it with a title and optional subtitle, the **Table Footer** anchors it with source notes or other supplementary information, and the **Stub** provides a left-hand column of row identifiers. All three are added using the `tab_*()` family of methods.

A well-structured frame transforms a bare data grid into something self-explanatory. Without these components, your reader has to look outside the table for context: what is this data? Where did it come from? What do the rows represent? Adding a header, footer, and stub answers those questions inside the table itself, so it can stand on its own in a report, slide deck, or web page.


# Adding a Table Header

A **Table Header** is easy to add with the [tab_header()](../reference/GT.tab_header.md#great_tables.GT.tab_header) method. Let's see how a basic table looks with a *title* and a *subtitle*:


``` python
from great_tables import GT, md, html
from great_tables.data import islands

islands_mini = islands.head(10)

# Make a display table with the `islands_tbl` table and
# put a heading just above the column labels
(
    GT(islands_mini)
    .tab_header(
        title = "Large Landmasses of the World",
        subtitle = "The top ten largest are presented"
    )
)
```


<style>
#erdfgpgoqv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#erdfgpgoqv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#erdfgpgoqv p { margin: 0; padding: 0; }
 #erdfgpgoqv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #erdfgpgoqv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #erdfgpgoqv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #erdfgpgoqv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #erdfgpgoqv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #erdfgpgoqv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #erdfgpgoqv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #erdfgpgoqv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #erdfgpgoqv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #erdfgpgoqv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #erdfgpgoqv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #erdfgpgoqv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #erdfgpgoqv .gt_spanner_row { border-bottom-style: hidden; }
 #erdfgpgoqv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #erdfgpgoqv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #erdfgpgoqv .gt_from_md> :first-child { margin-top: 0; }
 #erdfgpgoqv .gt_from_md> :last-child { margin-bottom: 0; }
 #erdfgpgoqv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #erdfgpgoqv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #erdfgpgoqv .gt_indent_1 { text-indent: 5px; }
 #erdfgpgoqv .gt_indent_2 { text-indent: calc(5px * 2); }
 #erdfgpgoqv .gt_indent_3 { text-indent: calc(5px * 3); }
 #erdfgpgoqv .gt_indent_4 { text-indent: calc(5px * 4); }
 #erdfgpgoqv .gt_indent_5 { text-indent: calc(5px * 5); }
 #erdfgpgoqv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #erdfgpgoqv .gt_row_group_first td { border-top-width: 2px; }
 #erdfgpgoqv .gt_row_group_first th { border-top-width: 2px; }
 #erdfgpgoqv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #erdfgpgoqv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #erdfgpgoqv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #erdfgpgoqv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #erdfgpgoqv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #erdfgpgoqv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #erdfgpgoqv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #erdfgpgoqv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #erdfgpgoqv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #erdfgpgoqv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #erdfgpgoqv .gt_left { text-align: left; }
 #erdfgpgoqv .gt_center { text-align: center; }
 #erdfgpgoqv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #erdfgpgoqv .gt_font_normal { font-weight: normal; }
 #erdfgpgoqv .gt_font_bold { font-weight: bold; }
 #erdfgpgoqv .gt_font_italic { font-style: italic; }
 #erdfgpgoqv .gt_super { font-size: 65%; }
 #erdfgpgoqv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #erdfgpgoqv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #erdfgpgoqv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #erdfgpgoqv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #erdfgpgoqv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #erdfgpgoqv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="2" class="gt_heading gt_title gt_font_normal">Large Landmasses of the World</th>
</tr>
<tr class="gt_heading">
<th colspan="2" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">The top ten largest are presented</th>
</tr>
<tr class="gt_col_headings">
<th id="name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">name</th>
<th id="size" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">size</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Africa</td>
<td class="gt_row gt_right">11506</td>
</tr>
<tr>
<td class="gt_row gt_left">Antarctica</td>
<td class="gt_row gt_right">5500</td>
</tr>
<tr>
<td class="gt_row gt_left">Asia</td>
<td class="gt_row gt_right">16988</td>
</tr>
<tr>
<td class="gt_row gt_left">Australia</td>
<td class="gt_row gt_right">2968</td>
</tr>
<tr>
<td class="gt_row gt_left">Axel Heiberg</td>
<td class="gt_row gt_right">16</td>
</tr>
<tr>
<td class="gt_row gt_left">Baffin</td>
<td class="gt_row gt_right">184</td>
</tr>
<tr>
<td class="gt_row gt_left">Banks</td>
<td class="gt_row gt_right">23</td>
</tr>
<tr>
<td class="gt_row gt_left">Borneo</td>
<td class="gt_row gt_right">280</td>
</tr>
<tr>
<td class="gt_row gt_left">Britain</td>
<td class="gt_row gt_right">84</td>
</tr>
<tr>
<td class="gt_row gt_left">Celebes</td>
<td class="gt_row gt_right">73</td>
</tr>
</tbody>
</table>


As a rule of thumb, any table that will be seen outside your own notebook benefits from a title. It also immediately orients the reader as to what the table's all about.

The **Header** provides an opportunity to describe the data that's presented. Using `subtitle=` allows us to insert a subtitle, which is an optional part of the **Header**. We may also style the `title=` and `subtitle=` using Markdown! We do this by wrapping the values passed to `title=` or `subtitle=` with the [md()](../reference/md.md#great_tables.md) helper function (we may also use [html()](../reference/html.md#great_tables.html) in a similar fashion). Here is an example with the table data truncated for brevity:


``` python
# Make a display table with the `islands_tbl` table and
# put a heading just above the column labels
gt_tbl = (
    GT(islands.head(2))
    .tab_header(
        title = md("Large Landmasses of the *World* 🌐"),
        subtitle = md("The top **ten** largest are presented")
    )
)

gt_tbl
```


<style>
#tfpilpjvjh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tfpilpjvjh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tfpilpjvjh p { margin: 0; padding: 0; }
 #tfpilpjvjh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tfpilpjvjh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tfpilpjvjh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tfpilpjvjh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tfpilpjvjh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tfpilpjvjh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tfpilpjvjh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tfpilpjvjh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tfpilpjvjh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tfpilpjvjh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tfpilpjvjh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tfpilpjvjh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tfpilpjvjh .gt_spanner_row { border-bottom-style: hidden; }
 #tfpilpjvjh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tfpilpjvjh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tfpilpjvjh .gt_from_md> :first-child { margin-top: 0; }
 #tfpilpjvjh .gt_from_md> :last-child { margin-bottom: 0; }
 #tfpilpjvjh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tfpilpjvjh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tfpilpjvjh .gt_indent_1 { text-indent: 5px; }
 #tfpilpjvjh .gt_indent_2 { text-indent: calc(5px * 2); }
 #tfpilpjvjh .gt_indent_3 { text-indent: calc(5px * 3); }
 #tfpilpjvjh .gt_indent_4 { text-indent: calc(5px * 4); }
 #tfpilpjvjh .gt_indent_5 { text-indent: calc(5px * 5); }
 #tfpilpjvjh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tfpilpjvjh .gt_row_group_first td { border-top-width: 2px; }
 #tfpilpjvjh .gt_row_group_first th { border-top-width: 2px; }
 #tfpilpjvjh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tfpilpjvjh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tfpilpjvjh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tfpilpjvjh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tfpilpjvjh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tfpilpjvjh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tfpilpjvjh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tfpilpjvjh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tfpilpjvjh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tfpilpjvjh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tfpilpjvjh .gt_left { text-align: left; }
 #tfpilpjvjh .gt_center { text-align: center; }
 #tfpilpjvjh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tfpilpjvjh .gt_font_normal { font-weight: normal; }
 #tfpilpjvjh .gt_font_bold { font-weight: bold; }
 #tfpilpjvjh .gt_font_italic { font-style: italic; }
 #tfpilpjvjh .gt_super { font-size: 65%; }
 #tfpilpjvjh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tfpilpjvjh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tfpilpjvjh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tfpilpjvjh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tfpilpjvjh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tfpilpjvjh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="2" class="gt_heading gt_title gt_font_normal">Large Landmasses of the <em>World</em> 🌐</th>
</tr>
<tr class="gt_heading">
<th colspan="2" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">The top <strong>ten</strong> largest are presented</th>
</tr>
<tr class="gt_col_headings">
<th id="name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">name</th>
<th id="size" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">size</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Africa</td>
<td class="gt_row gt_right">11506</td>
</tr>
<tr>
<td class="gt_row gt_left">Antarctica</td>
<td class="gt_row gt_right">5500</td>
</tr>
</tbody>
</table>


With a title and subtitle in place, the reader immediately knows what the table is about before looking at any data.


# Adding Source Notes

A *source note* can be added to the table's **Footer** through use of the [tab_source_note()](../reference/GT.tab_source_note.md#great_tables.GT.tab_source_note) method. It works in the same way as [tab_header()](../reference/GT.tab_header.md#great_tables.GT.tab_header) (it also allows for Markdown inputs) except it can be called multiple times. Each invocation results in the addition of a source note.


``` python
# Display the `islands_tbl` data with a heading and two source notes
(
    gt_tbl
    .tab_source_note(
        source_note = "Source: The World Almanac and Book of Facts, 1975, page 406."
    )
    .tab_source_note(
        source_note = md("Reference: McNeil, D. R. (1977) *Interactive Data Analysis*. Wiley.")
    )
)
```


<style>
#nbkzauofxw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nbkzauofxw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nbkzauofxw p { margin: 0; padding: 0; }
 #nbkzauofxw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nbkzauofxw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nbkzauofxw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nbkzauofxw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nbkzauofxw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nbkzauofxw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nbkzauofxw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nbkzauofxw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nbkzauofxw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nbkzauofxw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nbkzauofxw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nbkzauofxw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nbkzauofxw .gt_spanner_row { border-bottom-style: hidden; }
 #nbkzauofxw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nbkzauofxw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nbkzauofxw .gt_from_md> :first-child { margin-top: 0; }
 #nbkzauofxw .gt_from_md> :last-child { margin-bottom: 0; }
 #nbkzauofxw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nbkzauofxw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nbkzauofxw .gt_indent_1 { text-indent: 5px; }
 #nbkzauofxw .gt_indent_2 { text-indent: calc(5px * 2); }
 #nbkzauofxw .gt_indent_3 { text-indent: calc(5px * 3); }
 #nbkzauofxw .gt_indent_4 { text-indent: calc(5px * 4); }
 #nbkzauofxw .gt_indent_5 { text-indent: calc(5px * 5); }
 #nbkzauofxw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nbkzauofxw .gt_row_group_first td { border-top-width: 2px; }
 #nbkzauofxw .gt_row_group_first th { border-top-width: 2px; }
 #nbkzauofxw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nbkzauofxw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nbkzauofxw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nbkzauofxw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nbkzauofxw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nbkzauofxw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nbkzauofxw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nbkzauofxw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nbkzauofxw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nbkzauofxw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nbkzauofxw .gt_left { text-align: left; }
 #nbkzauofxw .gt_center { text-align: center; }
 #nbkzauofxw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nbkzauofxw .gt_font_normal { font-weight: normal; }
 #nbkzauofxw .gt_font_bold { font-weight: bold; }
 #nbkzauofxw .gt_font_italic { font-style: italic; }
 #nbkzauofxw .gt_super { font-size: 65%; }
 #nbkzauofxw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nbkzauofxw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nbkzauofxw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nbkzauofxw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nbkzauofxw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nbkzauofxw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="2" class="gt_heading gt_title gt_font_normal">Large Landmasses of the <em>World</em> 🌐</th>
</tr>
<tr class="gt_heading">
<th colspan="2" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">The top <strong>ten</strong> largest are presented</th>
</tr>
<tr class="gt_col_headings">
<th id="name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">name</th>
<th id="size" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">size</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Africa</td>
<td class="gt_row gt_right">11506</td>
</tr>
<tr>
<td class="gt_row gt_left">Antarctica</td>
<td class="gt_row gt_right">5500</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="2" class="gt_sourcenote">Source: The World Almanac and Book of Facts, 1975, page 406.</td>
</tr>
<tr class="gt_sourcenotes">
<td colspan="2" class="gt_sourcenote">Reference: McNeil, D. R. (1977) <em>Interactive Data Analysis</em>. Wiley.</td>
</tr>
</tfoot>

</table>


Source notes are pretty valuable because they provide provenance and credibility. Academic and business audiences might expect to know where data comes from. Including that information directly in the table saves readers from hunting through surrounding text. Source notes are also a good place for methodological caveats or disclaimers that apply to the entire table.

With just a few method calls, we have added essential context to the table. The title and subtitle tell the reader what data is being presented, and the source notes provide attribution. Together, these components frame the table body and help your audience understand the data at a glance.


# The Stub: Row Labels

The **Stub** is good to have whenever the first column of your data serves as an identifier rather than a measured value. Moving identifiers into the stub visually separates "what this row is about" from "what was measured", making the table easier to scan. If your rows represent people, places, time periods, or categories, those labels would go nicely in the stub.

The **Stub** is the area to the left of the table body that typically contains *row labels* and may also contain *row group labels*. Those subparts can be grouped in a sequence of *row groups*. The **Stub Head** provides a location for a label that describes the **Stub** (and could also be used to describe the column labels). The **Stub** is optional since there are cases where it wouldn't be useful (the display tables presented earlier looked just fine without one).

An easy way to generate a **Stub** part is by specifying a stub column in the [GT()](../reference/GT.md#great_tables.GT) class with the `rowname_col=` argument. This will signal to **Great Tables** that the named column should be used as the stub, using the contents of that column to make *row labels*. Let's add a stub with our `islands` dataset by using `rowname_col=` in the call to [GT](../reference/GT.md#great_tables.GT):


``` python
GT(islands_mini).tab_stub(rowname_col="name")
```


<style>
#eblbgzmfae table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eblbgzmfae thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eblbgzmfae p { margin: 0; padding: 0; }
 #eblbgzmfae .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eblbgzmfae .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eblbgzmfae .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eblbgzmfae .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eblbgzmfae .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eblbgzmfae .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eblbgzmfae .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eblbgzmfae .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eblbgzmfae .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eblbgzmfae .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eblbgzmfae .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eblbgzmfae .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eblbgzmfae .gt_spanner_row { border-bottom-style: hidden; }
 #eblbgzmfae .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eblbgzmfae .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eblbgzmfae .gt_from_md> :first-child { margin-top: 0; }
 #eblbgzmfae .gt_from_md> :last-child { margin-bottom: 0; }
 #eblbgzmfae .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eblbgzmfae .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eblbgzmfae .gt_indent_1 { text-indent: 5px; }
 #eblbgzmfae .gt_indent_2 { text-indent: calc(5px * 2); }
 #eblbgzmfae .gt_indent_3 { text-indent: calc(5px * 3); }
 #eblbgzmfae .gt_indent_4 { text-indent: calc(5px * 4); }
 #eblbgzmfae .gt_indent_5 { text-indent: calc(5px * 5); }
 #eblbgzmfae .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eblbgzmfae .gt_row_group_first td { border-top-width: 2px; }
 #eblbgzmfae .gt_row_group_first th { border-top-width: 2px; }
 #eblbgzmfae .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eblbgzmfae .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eblbgzmfae .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eblbgzmfae .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eblbgzmfae .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eblbgzmfae .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eblbgzmfae .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eblbgzmfae .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eblbgzmfae .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eblbgzmfae .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eblbgzmfae .gt_left { text-align: left; }
 #eblbgzmfae .gt_center { text-align: center; }
 #eblbgzmfae .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eblbgzmfae .gt_font_normal { font-weight: normal; }
 #eblbgzmfae .gt_font_bold { font-weight: bold; }
 #eblbgzmfae .gt_font_italic { font-style: italic; }
 #eblbgzmfae .gt_super { font-size: 65%; }
 #eblbgzmfae .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eblbgzmfae .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eblbgzmfae .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eblbgzmfae .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eblbgzmfae .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eblbgzmfae .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|              | size  |
|--------------|-------|
| Africa       | 11506 |
| Antarctica   | 5500  |
| Asia         | 16988 |
| Australia    | 2968  |
| Axel Heiberg | 16    |
| Baffin       | 184   |
| Banks        | 23    |
| Borneo       | 280   |
| Britain      | 84    |
| Celebes      | 73    |


Notice that the landmass names are now placed to the left? That's the **Stub**. Notably, there is a prominent border to the right of it but there's no label above the **Stub**. We can change this and apply what's known as a *stubhead label* through use of the [tab_stubhead()](../reference/GT.tab_stubhead.md#great_tables.GT.tab_stubhead) method:


``` python
(
    GT(islands_mini)
    .tab_stub(rowname_col="name")
    .tab_stubhead(label="landmass")
)
```


<style>
#ndwdycoqbj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ndwdycoqbj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ndwdycoqbj p { margin: 0; padding: 0; }
 #ndwdycoqbj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ndwdycoqbj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ndwdycoqbj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ndwdycoqbj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ndwdycoqbj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ndwdycoqbj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ndwdycoqbj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ndwdycoqbj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ndwdycoqbj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ndwdycoqbj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ndwdycoqbj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ndwdycoqbj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ndwdycoqbj .gt_spanner_row { border-bottom-style: hidden; }
 #ndwdycoqbj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ndwdycoqbj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ndwdycoqbj .gt_from_md> :first-child { margin-top: 0; }
 #ndwdycoqbj .gt_from_md> :last-child { margin-bottom: 0; }
 #ndwdycoqbj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ndwdycoqbj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ndwdycoqbj .gt_indent_1 { text-indent: 5px; }
 #ndwdycoqbj .gt_indent_2 { text-indent: calc(5px * 2); }
 #ndwdycoqbj .gt_indent_3 { text-indent: calc(5px * 3); }
 #ndwdycoqbj .gt_indent_4 { text-indent: calc(5px * 4); }
 #ndwdycoqbj .gt_indent_5 { text-indent: calc(5px * 5); }
 #ndwdycoqbj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ndwdycoqbj .gt_row_group_first td { border-top-width: 2px; }
 #ndwdycoqbj .gt_row_group_first th { border-top-width: 2px; }
 #ndwdycoqbj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ndwdycoqbj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ndwdycoqbj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ndwdycoqbj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ndwdycoqbj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ndwdycoqbj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ndwdycoqbj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ndwdycoqbj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ndwdycoqbj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ndwdycoqbj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ndwdycoqbj .gt_left { text-align: left; }
 #ndwdycoqbj .gt_center { text-align: center; }
 #ndwdycoqbj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ndwdycoqbj .gt_font_normal { font-weight: normal; }
 #ndwdycoqbj .gt_font_bold { font-weight: bold; }
 #ndwdycoqbj .gt_font_italic { font-style: italic; }
 #ndwdycoqbj .gt_super { font-size: 65%; }
 #ndwdycoqbj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ndwdycoqbj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ndwdycoqbj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ndwdycoqbj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ndwdycoqbj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ndwdycoqbj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| landmass     | size  |
|--------------|-------|
| Africa       | 11506 |
| Antarctica   | 5500  |
| Asia         | 16988 |
| Australia    | 2968  |
| Axel Heiberg | 16    |
| Baffin       | 184   |
| Banks        | 23    |
| Borneo       | 280   |
| Britain      | 84    |
| Celebes      | 73    |


A very important thing to note here is that the table now has one column. Before, when there was no **Stub**, two columns were present (with the **Column Labels** of `"name"` and `"size"`) but now column number `1` (the only column remaining) is `size`.


# Row Groups

Grouping is most useful when your data has a natural categorical structure and you want readers to compare within and across categories. Rather than forcing the reader to mentally sort the rows, row groups do that work up front.

Let's incorporate row groups into the display table. This divides rows into groups, creating *row groups*, and results in a display of a *row group labels* right above each group. This can be easily done with a table containing row labels and the key is to use the `groupname_col=` argument of the [GT](../reference/GT.md#great_tables.GT) class. Here we will create three row groups (with row group labels `"continent"`, `"country"`, and `"subregion"`) to have a grouping of rows.


``` python
island_groups = islands.head(10).assign(group = ["subregion"] * 2 + ["country"] * 2 + ["continent"] * 6)

(
    GT(island_groups)
    .tab_stub(rowname_col="name", groupname_col="group")
    .tab_stubhead(label="landmass")
)
```


<style>
#abgphawped table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#abgphawped thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#abgphawped p { margin: 0; padding: 0; }
 #abgphawped .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #abgphawped .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #abgphawped .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #abgphawped .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #abgphawped .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #abgphawped .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #abgphawped .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #abgphawped .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #abgphawped .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #abgphawped .gt_column_spanner_outer:first-child { padding-left: 0; }
 #abgphawped .gt_column_spanner_outer:last-child { padding-right: 0; }
 #abgphawped .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #abgphawped .gt_spanner_row { border-bottom-style: hidden; }
 #abgphawped .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #abgphawped .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #abgphawped .gt_from_md> :first-child { margin-top: 0; }
 #abgphawped .gt_from_md> :last-child { margin-bottom: 0; }
 #abgphawped .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #abgphawped .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #abgphawped .gt_indent_1 { text-indent: 5px; }
 #abgphawped .gt_indent_2 { text-indent: calc(5px * 2); }
 #abgphawped .gt_indent_3 { text-indent: calc(5px * 3); }
 #abgphawped .gt_indent_4 { text-indent: calc(5px * 4); }
 #abgphawped .gt_indent_5 { text-indent: calc(5px * 5); }
 #abgphawped .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #abgphawped .gt_row_group_first td { border-top-width: 2px; }
 #abgphawped .gt_row_group_first th { border-top-width: 2px; }
 #abgphawped .gt_striped { color: #333333; background-color: #F4F4F4; }
 #abgphawped .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #abgphawped .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #abgphawped .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #abgphawped .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #abgphawped .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #abgphawped .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #abgphawped .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #abgphawped .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #abgphawped .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #abgphawped .gt_left { text-align: left; }
 #abgphawped .gt_center { text-align: center; }
 #abgphawped .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #abgphawped .gt_font_normal { font-weight: normal; }
 #abgphawped .gt_font_bold { font-weight: bold; }
 #abgphawped .gt_font_italic { font-style: italic; }
 #abgphawped .gt_super { font-size: 65%; }
 #abgphawped .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #abgphawped .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #abgphawped .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #abgphawped .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #abgphawped .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #abgphawped .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th id="landmass" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">landmass</th>
<th id="size" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">size</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="2" class="gt_group_heading">subregion</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">Africa</td>
<td class="gt_row gt_right">11506</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Antarctica</td>
<td class="gt_row gt_right">5500</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading">country</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Asia</td>
<td class="gt_row gt_right">16988</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Australia</td>
<td class="gt_row gt_right">2968</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading">continent</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Axel Heiberg</td>
<td class="gt_row gt_right">16</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Baffin</td>
<td class="gt_row gt_right">184</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Banks</td>
<td class="gt_row gt_right">23</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Borneo</td>
<td class="gt_row gt_right">280</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Britain</td>
<td class="gt_row gt_right">84</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Celebes</td>
<td class="gt_row gt_right">73</td>
</tr>
</tbody>
</table>


The table now groups its rows by continent, country, and subregion, with labels appearing above each group. Row groups make it much easier for readers to scan and compare related entries.


# GT Convenience Arguments

Rather than using the [tab_stub()](../reference/GT.tab_stub.md#great_tables.GT.tab_stub) method, the `GT(rowname_col=..., groupname_col=...)` arguments provide a quick way to specify row names and groups.


``` python
GT(island_groups, rowname_col="name", groupname_col="group")
```


<style>
#ngmmucpliv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ngmmucpliv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ngmmucpliv p { margin: 0; padding: 0; }
 #ngmmucpliv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ngmmucpliv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ngmmucpliv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ngmmucpliv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ngmmucpliv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ngmmucpliv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ngmmucpliv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ngmmucpliv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ngmmucpliv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ngmmucpliv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ngmmucpliv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ngmmucpliv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ngmmucpliv .gt_spanner_row { border-bottom-style: hidden; }
 #ngmmucpliv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ngmmucpliv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ngmmucpliv .gt_from_md> :first-child { margin-top: 0; }
 #ngmmucpliv .gt_from_md> :last-child { margin-bottom: 0; }
 #ngmmucpliv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ngmmucpliv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ngmmucpliv .gt_indent_1 { text-indent: 5px; }
 #ngmmucpliv .gt_indent_2 { text-indent: calc(5px * 2); }
 #ngmmucpliv .gt_indent_3 { text-indent: calc(5px * 3); }
 #ngmmucpliv .gt_indent_4 { text-indent: calc(5px * 4); }
 #ngmmucpliv .gt_indent_5 { text-indent: calc(5px * 5); }
 #ngmmucpliv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ngmmucpliv .gt_row_group_first td { border-top-width: 2px; }
 #ngmmucpliv .gt_row_group_first th { border-top-width: 2px; }
 #ngmmucpliv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ngmmucpliv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ngmmucpliv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ngmmucpliv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ngmmucpliv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ngmmucpliv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ngmmucpliv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ngmmucpliv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ngmmucpliv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ngmmucpliv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ngmmucpliv .gt_left { text-align: left; }
 #ngmmucpliv .gt_center { text-align: center; }
 #ngmmucpliv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ngmmucpliv .gt_font_normal { font-weight: normal; }
 #ngmmucpliv .gt_font_bold { font-weight: bold; }
 #ngmmucpliv .gt_font_italic { font-style: italic; }
 #ngmmucpliv .gt_super { font-size: 65%; }
 #ngmmucpliv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ngmmucpliv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ngmmucpliv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ngmmucpliv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ngmmucpliv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ngmmucpliv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="size" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">size</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="2" class="gt_group_heading">subregion</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">Africa</td>
<td class="gt_row gt_right">11506</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Antarctica</td>
<td class="gt_row gt_right">5500</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading">country</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Asia</td>
<td class="gt_row gt_right">16988</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Australia</td>
<td class="gt_row gt_right">2968</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" class="gt_group_heading">continent</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Axel Heiberg</td>
<td class="gt_row gt_right">16</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Baffin</td>
<td class="gt_row gt_right">184</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Banks</td>
<td class="gt_row gt_right">23</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Borneo</td>
<td class="gt_row gt_right">280</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Britain</td>
<td class="gt_row gt_right">84</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">Celebes</td>
<td class="gt_row gt_right">73</td>
</tr>
</tbody>
</table>


The stub provides a clear organizational framework for your data by separating identifiers from values. Whether you simply need named rows or a fully grouped hierarchy, the combination of `rowname_col=`, `groupname_col=`, and [tab_stubhead()](../reference/GT.tab_stubhead.md#great_tables.GT.tab_stubhead) gives you precise control over how readers navigate your table.
