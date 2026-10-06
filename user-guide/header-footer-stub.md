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
#glgrcwhhwj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#glgrcwhhwj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#glgrcwhhwj p { margin: 0; padding: 0; }
 #glgrcwhhwj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #glgrcwhhwj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #glgrcwhhwj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #glgrcwhhwj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #glgrcwhhwj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #glgrcwhhwj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #glgrcwhhwj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #glgrcwhhwj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #glgrcwhhwj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #glgrcwhhwj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #glgrcwhhwj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #glgrcwhhwj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #glgrcwhhwj .gt_spanner_row { border-bottom-style: hidden; }
 #glgrcwhhwj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #glgrcwhhwj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #glgrcwhhwj .gt_from_md> :first-child { margin-top: 0; }
 #glgrcwhhwj .gt_from_md> :last-child { margin-bottom: 0; }
 #glgrcwhhwj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #glgrcwhhwj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #glgrcwhhwj .gt_indent_1 { text-indent: 5px; }
 #glgrcwhhwj .gt_indent_2 { text-indent: calc(5px * 2); }
 #glgrcwhhwj .gt_indent_3 { text-indent: calc(5px * 3); }
 #glgrcwhhwj .gt_indent_4 { text-indent: calc(5px * 4); }
 #glgrcwhhwj .gt_indent_5 { text-indent: calc(5px * 5); }
 #glgrcwhhwj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #glgrcwhhwj .gt_row_group_first td { border-top-width: 2px; }
 #glgrcwhhwj .gt_row_group_first th { border-top-width: 2px; }
 #glgrcwhhwj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #glgrcwhhwj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #glgrcwhhwj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #glgrcwhhwj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #glgrcwhhwj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #glgrcwhhwj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #glgrcwhhwj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #glgrcwhhwj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #glgrcwhhwj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #glgrcwhhwj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #glgrcwhhwj .gt_left { text-align: left; }
 #glgrcwhhwj .gt_center { text-align: center; }
 #glgrcwhhwj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #glgrcwhhwj .gt_font_normal { font-weight: normal; }
 #glgrcwhhwj .gt_font_bold { font-weight: bold; }
 #glgrcwhhwj .gt_font_italic { font-style: italic; }
 #glgrcwhhwj .gt_super { font-size: 65%; }
 #glgrcwhhwj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #glgrcwhhwj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #glgrcwhhwj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #glgrcwhhwj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #glgrcwhhwj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #glgrcwhhwj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#flkrcgntgg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#flkrcgntgg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#flkrcgntgg p { margin: 0; padding: 0; }
 #flkrcgntgg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #flkrcgntgg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #flkrcgntgg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #flkrcgntgg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #flkrcgntgg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #flkrcgntgg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #flkrcgntgg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #flkrcgntgg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #flkrcgntgg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #flkrcgntgg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #flkrcgntgg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #flkrcgntgg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #flkrcgntgg .gt_spanner_row { border-bottom-style: hidden; }
 #flkrcgntgg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #flkrcgntgg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #flkrcgntgg .gt_from_md> :first-child { margin-top: 0; }
 #flkrcgntgg .gt_from_md> :last-child { margin-bottom: 0; }
 #flkrcgntgg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #flkrcgntgg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #flkrcgntgg .gt_indent_1 { text-indent: 5px; }
 #flkrcgntgg .gt_indent_2 { text-indent: calc(5px * 2); }
 #flkrcgntgg .gt_indent_3 { text-indent: calc(5px * 3); }
 #flkrcgntgg .gt_indent_4 { text-indent: calc(5px * 4); }
 #flkrcgntgg .gt_indent_5 { text-indent: calc(5px * 5); }
 #flkrcgntgg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #flkrcgntgg .gt_row_group_first td { border-top-width: 2px; }
 #flkrcgntgg .gt_row_group_first th { border-top-width: 2px; }
 #flkrcgntgg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #flkrcgntgg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #flkrcgntgg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #flkrcgntgg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #flkrcgntgg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #flkrcgntgg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #flkrcgntgg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #flkrcgntgg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #flkrcgntgg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #flkrcgntgg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #flkrcgntgg .gt_left { text-align: left; }
 #flkrcgntgg .gt_center { text-align: center; }
 #flkrcgntgg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #flkrcgntgg .gt_font_normal { font-weight: normal; }
 #flkrcgntgg .gt_font_bold { font-weight: bold; }
 #flkrcgntgg .gt_font_italic { font-style: italic; }
 #flkrcgntgg .gt_super { font-size: 65%; }
 #flkrcgntgg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #flkrcgntgg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #flkrcgntgg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #flkrcgntgg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #flkrcgntgg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #flkrcgntgg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ujtbwulfsb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ujtbwulfsb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ujtbwulfsb p { margin: 0; padding: 0; }
 #ujtbwulfsb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ujtbwulfsb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ujtbwulfsb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ujtbwulfsb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ujtbwulfsb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ujtbwulfsb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ujtbwulfsb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ujtbwulfsb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ujtbwulfsb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ujtbwulfsb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ujtbwulfsb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ujtbwulfsb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ujtbwulfsb .gt_spanner_row { border-bottom-style: hidden; }
 #ujtbwulfsb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ujtbwulfsb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ujtbwulfsb .gt_from_md> :first-child { margin-top: 0; }
 #ujtbwulfsb .gt_from_md> :last-child { margin-bottom: 0; }
 #ujtbwulfsb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ujtbwulfsb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ujtbwulfsb .gt_indent_1 { text-indent: 5px; }
 #ujtbwulfsb .gt_indent_2 { text-indent: calc(5px * 2); }
 #ujtbwulfsb .gt_indent_3 { text-indent: calc(5px * 3); }
 #ujtbwulfsb .gt_indent_4 { text-indent: calc(5px * 4); }
 #ujtbwulfsb .gt_indent_5 { text-indent: calc(5px * 5); }
 #ujtbwulfsb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ujtbwulfsb .gt_row_group_first td { border-top-width: 2px; }
 #ujtbwulfsb .gt_row_group_first th { border-top-width: 2px; }
 #ujtbwulfsb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ujtbwulfsb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ujtbwulfsb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ujtbwulfsb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ujtbwulfsb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ujtbwulfsb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ujtbwulfsb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ujtbwulfsb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ujtbwulfsb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ujtbwulfsb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ujtbwulfsb .gt_left { text-align: left; }
 #ujtbwulfsb .gt_center { text-align: center; }
 #ujtbwulfsb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ujtbwulfsb .gt_font_normal { font-weight: normal; }
 #ujtbwulfsb .gt_font_bold { font-weight: bold; }
 #ujtbwulfsb .gt_font_italic { font-style: italic; }
 #ujtbwulfsb .gt_super { font-size: 65%; }
 #ujtbwulfsb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ujtbwulfsb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ujtbwulfsb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ujtbwulfsb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ujtbwulfsb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ujtbwulfsb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#fdiazduard table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fdiazduard thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fdiazduard p { margin: 0; padding: 0; }
 #fdiazduard .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fdiazduard .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fdiazduard .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fdiazduard .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fdiazduard .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fdiazduard .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fdiazduard .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fdiazduard .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fdiazduard .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fdiazduard .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fdiazduard .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fdiazduard .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fdiazduard .gt_spanner_row { border-bottom-style: hidden; }
 #fdiazduard .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fdiazduard .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fdiazduard .gt_from_md> :first-child { margin-top: 0; }
 #fdiazduard .gt_from_md> :last-child { margin-bottom: 0; }
 #fdiazduard .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fdiazduard .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fdiazduard .gt_indent_1 { text-indent: 5px; }
 #fdiazduard .gt_indent_2 { text-indent: calc(5px * 2); }
 #fdiazduard .gt_indent_3 { text-indent: calc(5px * 3); }
 #fdiazduard .gt_indent_4 { text-indent: calc(5px * 4); }
 #fdiazduard .gt_indent_5 { text-indent: calc(5px * 5); }
 #fdiazduard .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fdiazduard .gt_row_group_first td { border-top-width: 2px; }
 #fdiazduard .gt_row_group_first th { border-top-width: 2px; }
 #fdiazduard .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fdiazduard .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fdiazduard .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fdiazduard .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fdiazduard .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fdiazduard .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fdiazduard .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fdiazduard .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fdiazduard .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fdiazduard .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fdiazduard .gt_left { text-align: left; }
 #fdiazduard .gt_center { text-align: center; }
 #fdiazduard .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fdiazduard .gt_font_normal { font-weight: normal; }
 #fdiazduard .gt_font_bold { font-weight: bold; }
 #fdiazduard .gt_font_italic { font-style: italic; }
 #fdiazduard .gt_super { font-size: 65%; }
 #fdiazduard .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fdiazduard .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fdiazduard .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fdiazduard .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fdiazduard .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fdiazduard .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#khzyxssuwj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#khzyxssuwj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#khzyxssuwj p { margin: 0; padding: 0; }
 #khzyxssuwj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #khzyxssuwj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #khzyxssuwj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #khzyxssuwj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #khzyxssuwj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #khzyxssuwj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khzyxssuwj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #khzyxssuwj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #khzyxssuwj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #khzyxssuwj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #khzyxssuwj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #khzyxssuwj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #khzyxssuwj .gt_spanner_row { border-bottom-style: hidden; }
 #khzyxssuwj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #khzyxssuwj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #khzyxssuwj .gt_from_md> :first-child { margin-top: 0; }
 #khzyxssuwj .gt_from_md> :last-child { margin-bottom: 0; }
 #khzyxssuwj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #khzyxssuwj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #khzyxssuwj .gt_indent_1 { text-indent: 5px; }
 #khzyxssuwj .gt_indent_2 { text-indent: calc(5px * 2); }
 #khzyxssuwj .gt_indent_3 { text-indent: calc(5px * 3); }
 #khzyxssuwj .gt_indent_4 { text-indent: calc(5px * 4); }
 #khzyxssuwj .gt_indent_5 { text-indent: calc(5px * 5); }
 #khzyxssuwj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #khzyxssuwj .gt_row_group_first td { border-top-width: 2px; }
 #khzyxssuwj .gt_row_group_first th { border-top-width: 2px; }
 #khzyxssuwj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #khzyxssuwj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khzyxssuwj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #khzyxssuwj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #khzyxssuwj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khzyxssuwj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #khzyxssuwj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #khzyxssuwj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #khzyxssuwj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khzyxssuwj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #khzyxssuwj .gt_left { text-align: left; }
 #khzyxssuwj .gt_center { text-align: center; }
 #khzyxssuwj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #khzyxssuwj .gt_font_normal { font-weight: normal; }
 #khzyxssuwj .gt_font_bold { font-weight: bold; }
 #khzyxssuwj .gt_font_italic { font-style: italic; }
 #khzyxssuwj .gt_super { font-size: 65%; }
 #khzyxssuwj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khzyxssuwj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #khzyxssuwj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khzyxssuwj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #khzyxssuwj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #khzyxssuwj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#vwosnfdcmw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vwosnfdcmw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vwosnfdcmw p { margin: 0; padding: 0; }
 #vwosnfdcmw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vwosnfdcmw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vwosnfdcmw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vwosnfdcmw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vwosnfdcmw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vwosnfdcmw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vwosnfdcmw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vwosnfdcmw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vwosnfdcmw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vwosnfdcmw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vwosnfdcmw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vwosnfdcmw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vwosnfdcmw .gt_spanner_row { border-bottom-style: hidden; }
 #vwosnfdcmw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vwosnfdcmw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vwosnfdcmw .gt_from_md> :first-child { margin-top: 0; }
 #vwosnfdcmw .gt_from_md> :last-child { margin-bottom: 0; }
 #vwosnfdcmw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vwosnfdcmw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vwosnfdcmw .gt_indent_1 { text-indent: 5px; }
 #vwosnfdcmw .gt_indent_2 { text-indent: calc(5px * 2); }
 #vwosnfdcmw .gt_indent_3 { text-indent: calc(5px * 3); }
 #vwosnfdcmw .gt_indent_4 { text-indent: calc(5px * 4); }
 #vwosnfdcmw .gt_indent_5 { text-indent: calc(5px * 5); }
 #vwosnfdcmw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vwosnfdcmw .gt_row_group_first td { border-top-width: 2px; }
 #vwosnfdcmw .gt_row_group_first th { border-top-width: 2px; }
 #vwosnfdcmw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vwosnfdcmw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vwosnfdcmw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vwosnfdcmw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vwosnfdcmw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vwosnfdcmw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vwosnfdcmw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vwosnfdcmw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vwosnfdcmw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vwosnfdcmw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vwosnfdcmw .gt_left { text-align: left; }
 #vwosnfdcmw .gt_center { text-align: center; }
 #vwosnfdcmw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vwosnfdcmw .gt_font_normal { font-weight: normal; }
 #vwosnfdcmw .gt_font_bold { font-weight: bold; }
 #vwosnfdcmw .gt_font_italic { font-style: italic; }
 #vwosnfdcmw .gt_super { font-size: 65%; }
 #vwosnfdcmw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vwosnfdcmw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vwosnfdcmw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vwosnfdcmw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vwosnfdcmw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vwosnfdcmw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wvfajyapcc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wvfajyapcc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wvfajyapcc p { margin: 0; padding: 0; }
 #wvfajyapcc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wvfajyapcc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wvfajyapcc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wvfajyapcc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wvfajyapcc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wvfajyapcc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wvfajyapcc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wvfajyapcc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wvfajyapcc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wvfajyapcc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wvfajyapcc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wvfajyapcc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wvfajyapcc .gt_spanner_row { border-bottom-style: hidden; }
 #wvfajyapcc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wvfajyapcc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wvfajyapcc .gt_from_md> :first-child { margin-top: 0; }
 #wvfajyapcc .gt_from_md> :last-child { margin-bottom: 0; }
 #wvfajyapcc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wvfajyapcc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wvfajyapcc .gt_indent_1 { text-indent: 5px; }
 #wvfajyapcc .gt_indent_2 { text-indent: calc(5px * 2); }
 #wvfajyapcc .gt_indent_3 { text-indent: calc(5px * 3); }
 #wvfajyapcc .gt_indent_4 { text-indent: calc(5px * 4); }
 #wvfajyapcc .gt_indent_5 { text-indent: calc(5px * 5); }
 #wvfajyapcc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wvfajyapcc .gt_row_group_first td { border-top-width: 2px; }
 #wvfajyapcc .gt_row_group_first th { border-top-width: 2px; }
 #wvfajyapcc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wvfajyapcc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wvfajyapcc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wvfajyapcc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wvfajyapcc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wvfajyapcc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wvfajyapcc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wvfajyapcc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wvfajyapcc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wvfajyapcc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wvfajyapcc .gt_left { text-align: left; }
 #wvfajyapcc .gt_center { text-align: center; }
 #wvfajyapcc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wvfajyapcc .gt_font_normal { font-weight: normal; }
 #wvfajyapcc .gt_font_bold { font-weight: bold; }
 #wvfajyapcc .gt_font_italic { font-style: italic; }
 #wvfajyapcc .gt_super { font-size: 65%; }
 #wvfajyapcc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wvfajyapcc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wvfajyapcc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wvfajyapcc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wvfajyapcc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wvfajyapcc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
