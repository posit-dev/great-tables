# Header, Footer, and Stub

Three structural components frame the data in your table: the **Table Header** introduces it with a title and optional subtitle, the **Table Footer** anchors it with source notes or other supplementary information, and the **Stub** provides a left-hand column of row identifiers. All three are added using the `tab_*()` family of methods.

A well-structured frame transforms a bare data grid into something self-explanatory. Without these components, your reader has to look outside the table for context: what is this data? Where did it come from? What do the rows represent? Adding a header, footer, and stub answers those questions inside the table itself, so it can stand on its own in a report, slide deck, or web page.


# Adding a Table Header

A **Table Header** is easy to add with the [tab_header()](../reference/GT.tab_header.md#great_tables.GT.tab_header) method. Let's see how a basic table looks with a *title* and a *subtitle*:


``` python
from great_tables import GT, md, html
from great_tables.data import countrypops

# Get the ten most populous countries in 2022
countries_mini = (
    countrypops[countrypops["year"] == 2022]
    .sort_values("population", ascending=False)
    .head(10)[["country_name", "population"]]
)

# Make a display table with the `countries_mini` table and
# put a heading just above the column labels
(
    GT(countries_mini)
    .tab_header(
        title = "The World's Most Populous Countries",
        subtitle = "The top ten in 2022 are presented"
    )
)
```


<style>
#pluednymxd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pluednymxd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pluednymxd p { margin: 0; padding: 0; }
 #pluednymxd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pluednymxd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pluednymxd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pluednymxd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pluednymxd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pluednymxd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pluednymxd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pluednymxd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pluednymxd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pluednymxd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pluednymxd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pluednymxd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pluednymxd .gt_spanner_row { border-bottom-style: hidden; }
 #pluednymxd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pluednymxd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pluednymxd .gt_from_md> :first-child { margin-top: 0; }
 #pluednymxd .gt_from_md> :last-child { margin-bottom: 0; }
 #pluednymxd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pluednymxd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pluednymxd .gt_indent_1 { text-indent: 5px; }
 #pluednymxd .gt_indent_2 { text-indent: calc(5px * 2); }
 #pluednymxd .gt_indent_3 { text-indent: calc(5px * 3); }
 #pluednymxd .gt_indent_4 { text-indent: calc(5px * 4); }
 #pluednymxd .gt_indent_5 { text-indent: calc(5px * 5); }
 #pluednymxd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pluednymxd .gt_row_group_first td { border-top-width: 2px; }
 #pluednymxd .gt_row_group_first th { border-top-width: 2px; }
 #pluednymxd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pluednymxd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pluednymxd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pluednymxd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pluednymxd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pluednymxd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pluednymxd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pluednymxd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pluednymxd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pluednymxd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pluednymxd .gt_left { text-align: left; }
 #pluednymxd .gt_center { text-align: center; }
 #pluednymxd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pluednymxd .gt_font_normal { font-weight: normal; }
 #pluednymxd .gt_font_bold { font-weight: bold; }
 #pluednymxd .gt_font_italic { font-style: italic; }
 #pluednymxd .gt_super { font-size: 65%; }
 #pluednymxd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pluednymxd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pluednymxd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pluednymxd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pluednymxd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pluednymxd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="2" id="title" class="gt_heading gt_title gt_font_normal">The World's Most Populous Countries</th>
</tr>
<tr class="gt_heading">
<th colspan="2" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">The top ten in 2022 are presented</th>
</tr>
<tr class="gt_col_headings">
<th id="country_name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">country_name</th>
<th id="population" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">population</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left" headers="country_name">India</td>
<td class="gt_row gt_right" headers="population">1417173173</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="country_name">China</td>
<td class="gt_row gt_right" headers="population">1412175000</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="country_name">United States</td>
<td class="gt_row gt_right" headers="population">333287557</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="country_name">Indonesia</td>
<td class="gt_row gt_right" headers="population">275501339</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="country_name">Pakistan</td>
<td class="gt_row gt_right" headers="population">235824862</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="country_name">Nigeria</td>
<td class="gt_row gt_right" headers="population">218541212</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="country_name">Brazil</td>
<td class="gt_row gt_right" headers="population">215313498</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="country_name">Bangladesh</td>
<td class="gt_row gt_right" headers="population">171186372</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="country_name">Russian Federation</td>
<td class="gt_row gt_right" headers="population">143555736</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="country_name">Mexico</td>
<td class="gt_row gt_right" headers="population">127504125</td>
</tr>
</tbody>
</table>


As a rule of thumb, any table that will be seen outside your own notebook benefits from a title. It also immediately orients the reader as to what the table's all about.

The **Header** provides an opportunity to describe the data that's presented. Using `subtitle=` allows us to insert a subtitle, which is an optional part of the **Header**. We may also style the `title=` and `subtitle=` using Markdown! We do this by wrapping the values passed to `title=` or `subtitle=` with the [md()](../reference/md.md#great_tables.md) helper function (we may also use [html()](../reference/html.md#great_tables.html) in a similar fashion). Here is an example with the table data truncated for brevity:


``` python
# Make a display table with the `countries_mini` table and
# put a heading just above the column labels
gt_tbl = (
    GT(countries_mini.head(2))
    .tab_header(
        title = md("The *World's* Most Populous Countries 🌐"),
        subtitle = md("The top **ten** in 2022 are presented")
    )
)

gt_tbl
```


<style>
#npajzngzyg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#npajzngzyg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#npajzngzyg p { margin: 0; padding: 0; }
 #npajzngzyg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #npajzngzyg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #npajzngzyg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #npajzngzyg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #npajzngzyg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #npajzngzyg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #npajzngzyg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #npajzngzyg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #npajzngzyg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #npajzngzyg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #npajzngzyg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #npajzngzyg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #npajzngzyg .gt_spanner_row { border-bottom-style: hidden; }
 #npajzngzyg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #npajzngzyg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #npajzngzyg .gt_from_md> :first-child { margin-top: 0; }
 #npajzngzyg .gt_from_md> :last-child { margin-bottom: 0; }
 #npajzngzyg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #npajzngzyg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #npajzngzyg .gt_indent_1 { text-indent: 5px; }
 #npajzngzyg .gt_indent_2 { text-indent: calc(5px * 2); }
 #npajzngzyg .gt_indent_3 { text-indent: calc(5px * 3); }
 #npajzngzyg .gt_indent_4 { text-indent: calc(5px * 4); }
 #npajzngzyg .gt_indent_5 { text-indent: calc(5px * 5); }
 #npajzngzyg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #npajzngzyg .gt_row_group_first td { border-top-width: 2px; }
 #npajzngzyg .gt_row_group_first th { border-top-width: 2px; }
 #npajzngzyg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #npajzngzyg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #npajzngzyg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #npajzngzyg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #npajzngzyg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #npajzngzyg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #npajzngzyg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #npajzngzyg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #npajzngzyg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #npajzngzyg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #npajzngzyg .gt_left { text-align: left; }
 #npajzngzyg .gt_center { text-align: center; }
 #npajzngzyg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #npajzngzyg .gt_font_normal { font-weight: normal; }
 #npajzngzyg .gt_font_bold { font-weight: bold; }
 #npajzngzyg .gt_font_italic { font-style: italic; }
 #npajzngzyg .gt_super { font-size: 65%; }
 #npajzngzyg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #npajzngzyg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #npajzngzyg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #npajzngzyg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #npajzngzyg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #npajzngzyg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="2" id="title" class="gt_heading gt_title gt_font_normal">The <em>World's</em> Most Populous Countries 🌐</th>
</tr>
<tr class="gt_heading">
<th colspan="2" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">The top <strong>ten</strong> in 2022 are presented</th>
</tr>
<tr class="gt_col_headings">
<th id="country_name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">country_name</th>
<th id="population" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">population</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left" headers="country_name">India</td>
<td class="gt_row gt_right" headers="population">1417173173</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="country_name">China</td>
<td class="gt_row gt_right" headers="population">1412175000</td>
</tr>
</tbody>
</table>


With a title and subtitle in place, the reader immediately knows what the table is about before looking at any data.


# Adding Source Notes

A *source note* can be added to the table's **Footer** through use of the [tab_source_note()](../reference/GT.tab_source_note.md#great_tables.GT.tab_source_note) method. It works in the same way as [tab_header()](../reference/GT.tab_header.md#great_tables.GT.tab_header) (it also allows for Markdown inputs) except it can be called multiple times. Each invocation results in the addition of a source note.


``` python
# Display the `countries_mini` data with a heading and two source notes
(
    gt_tbl
    .tab_source_note(
        source_note = "Total population counts all residents regardless of legal status or citizenship."
    )
    .tab_source_note(
        source_note = md("Source: [The World Bank](https://data.worldbank.org/indicator/SP.POP.TOTL).")
    )
)
```


<style>
#ofzelwhjac table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ofzelwhjac thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ofzelwhjac p { margin: 0; padding: 0; }
 #ofzelwhjac .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ofzelwhjac .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ofzelwhjac .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ofzelwhjac .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ofzelwhjac .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ofzelwhjac .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ofzelwhjac .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ofzelwhjac .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ofzelwhjac .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ofzelwhjac .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ofzelwhjac .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ofzelwhjac .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ofzelwhjac .gt_spanner_row { border-bottom-style: hidden; }
 #ofzelwhjac .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ofzelwhjac .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ofzelwhjac .gt_from_md> :first-child { margin-top: 0; }
 #ofzelwhjac .gt_from_md> :last-child { margin-bottom: 0; }
 #ofzelwhjac .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ofzelwhjac .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ofzelwhjac .gt_indent_1 { text-indent: 5px; }
 #ofzelwhjac .gt_indent_2 { text-indent: calc(5px * 2); }
 #ofzelwhjac .gt_indent_3 { text-indent: calc(5px * 3); }
 #ofzelwhjac .gt_indent_4 { text-indent: calc(5px * 4); }
 #ofzelwhjac .gt_indent_5 { text-indent: calc(5px * 5); }
 #ofzelwhjac .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ofzelwhjac .gt_row_group_first td { border-top-width: 2px; }
 #ofzelwhjac .gt_row_group_first th { border-top-width: 2px; }
 #ofzelwhjac .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ofzelwhjac .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ofzelwhjac .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ofzelwhjac .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ofzelwhjac .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ofzelwhjac .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ofzelwhjac .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ofzelwhjac .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ofzelwhjac .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ofzelwhjac .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ofzelwhjac .gt_left { text-align: left; }
 #ofzelwhjac .gt_center { text-align: center; }
 #ofzelwhjac .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ofzelwhjac .gt_font_normal { font-weight: normal; }
 #ofzelwhjac .gt_font_bold { font-weight: bold; }
 #ofzelwhjac .gt_font_italic { font-style: italic; }
 #ofzelwhjac .gt_super { font-size: 65%; }
 #ofzelwhjac .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ofzelwhjac .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ofzelwhjac .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ofzelwhjac .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ofzelwhjac .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ofzelwhjac .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="2" id="title" class="gt_heading gt_title gt_font_normal">The <em>World's</em> Most Populous Countries 🌐</th>
</tr>
<tr class="gt_heading">
<th colspan="2" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">The top <strong>ten</strong> in 2022 are presented</th>
</tr>
<tr class="gt_col_headings">
<th id="country_name" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">country_name</th>
<th id="population" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">population</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left" headers="country_name">India</td>
<td class="gt_row gt_right" headers="population">1417173173</td>
</tr>
<tr>
<td class="gt_row gt_left" headers="country_name">China</td>
<td class="gt_row gt_right" headers="population">1412175000</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="2" class="gt_sourcenote">Total population counts all residents regardless of legal status or citizenship.</td>
</tr>
<tr class="gt_sourcenotes">
<td colspan="2" class="gt_sourcenote">Source: [The World Bank](https://data.worldbank.org/indicator/SP.POP.TOTL).</td>
</tr>
</tfoot>

</table>


Source notes are pretty valuable because they provide provenance and credibility. Academic and business audiences might expect to know where data comes from. Including that information directly in the table saves readers from hunting through surrounding text. Source notes are also a good place for methodological caveats or disclaimers that apply to the entire table.

With just a few method calls, we have added essential context to the table. The title and subtitle tell the reader what data is being presented, and the source notes provide attribution. Together, these components frame the table body and help your audience understand the data at a glance.


# The Stub: Row Labels

The **Stub** is good to have whenever the first column of your data serves as an identifier rather than a measured value. Moving identifiers into the stub visually separates "what this row is about" from "what was measured", making the table easier to scan. If your rows represent people, places, time periods, or categories, those labels would go nicely in the stub.

The **Stub** is the area to the left of the table body that typically contains *row labels* and may also contain *row group labels*. Those subparts can be grouped in a sequence of *row groups*. The **Stub Head** provides a location for a label that describes the **Stub** (and could also be used to describe the column labels). The **Stub** is optional since there are cases where it wouldn't be useful (the display tables presented earlier looked just fine without one).

An easy way to generate a **Stub** part is by specifying a stub column in the [GT()](../reference/GT.md#great_tables.GT) class with the `rowname_col=` argument. This will signal to **Great Tables** that the named column should be used as the stub, using the contents of that column to make *row labels*. Let's add a stub with our `countries_mini` table by using `rowname_col=` in the call to [GT](../reference/GT.md#great_tables.GT):


``` python
GT(countries_mini).tab_stub(rowname_col="country_name")
```


<style>
#gektmmflzo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gektmmflzo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gektmmflzo p { margin: 0; padding: 0; }
 #gektmmflzo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gektmmflzo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gektmmflzo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gektmmflzo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gektmmflzo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gektmmflzo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gektmmflzo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gektmmflzo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gektmmflzo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gektmmflzo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gektmmflzo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gektmmflzo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gektmmflzo .gt_spanner_row { border-bottom-style: hidden; }
 #gektmmflzo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gektmmflzo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gektmmflzo .gt_from_md> :first-child { margin-top: 0; }
 #gektmmflzo .gt_from_md> :last-child { margin-bottom: 0; }
 #gektmmflzo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gektmmflzo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gektmmflzo .gt_indent_1 { text-indent: 5px; }
 #gektmmflzo .gt_indent_2 { text-indent: calc(5px * 2); }
 #gektmmflzo .gt_indent_3 { text-indent: calc(5px * 3); }
 #gektmmflzo .gt_indent_4 { text-indent: calc(5px * 4); }
 #gektmmflzo .gt_indent_5 { text-indent: calc(5px * 5); }
 #gektmmflzo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gektmmflzo .gt_row_group_first td { border-top-width: 2px; }
 #gektmmflzo .gt_row_group_first th { border-top-width: 2px; }
 #gektmmflzo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gektmmflzo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gektmmflzo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gektmmflzo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gektmmflzo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gektmmflzo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gektmmflzo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gektmmflzo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gektmmflzo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gektmmflzo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gektmmflzo .gt_left { text-align: left; }
 #gektmmflzo .gt_center { text-align: center; }
 #gektmmflzo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gektmmflzo .gt_font_normal { font-weight: normal; }
 #gektmmflzo .gt_font_bold { font-weight: bold; }
 #gektmmflzo .gt_font_italic { font-style: italic; }
 #gektmmflzo .gt_super { font-size: 65%; }
 #gektmmflzo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gektmmflzo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gektmmflzo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gektmmflzo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gektmmflzo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gektmmflzo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|                    | population |
|--------------------|------------|
| India              | 1417173173 |
| China              | 1412175000 |
| United States      | 333287557  |
| Indonesia          | 275501339  |
| Pakistan           | 235824862  |
| Nigeria            | 218541212  |
| Brazil             | 215313498  |
| Bangladesh         | 171186372  |
| Russian Federation | 143555736  |
| Mexico             | 127504125  |


Notice that the country names are now placed to the left? That's the **Stub**. Notably, there is a prominent border to the right of it but there's no label above the **Stub**. We can change this and apply what's known as a *stubhead label* through use of the [tab_stubhead()](../reference/GT.tab_stubhead.md#great_tables.GT.tab_stubhead) method:


``` python
(
    GT(countries_mini)
    .tab_stub(rowname_col="country_name")
    .tab_stubhead(label="country")
)
```


<style>
#nswoqyplju table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nswoqyplju thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nswoqyplju p { margin: 0; padding: 0; }
 #nswoqyplju .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nswoqyplju .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nswoqyplju .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nswoqyplju .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nswoqyplju .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nswoqyplju .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nswoqyplju .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nswoqyplju .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nswoqyplju .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nswoqyplju .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nswoqyplju .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nswoqyplju .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nswoqyplju .gt_spanner_row { border-bottom-style: hidden; }
 #nswoqyplju .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nswoqyplju .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nswoqyplju .gt_from_md> :first-child { margin-top: 0; }
 #nswoqyplju .gt_from_md> :last-child { margin-bottom: 0; }
 #nswoqyplju .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nswoqyplju .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nswoqyplju .gt_indent_1 { text-indent: 5px; }
 #nswoqyplju .gt_indent_2 { text-indent: calc(5px * 2); }
 #nswoqyplju .gt_indent_3 { text-indent: calc(5px * 3); }
 #nswoqyplju .gt_indent_4 { text-indent: calc(5px * 4); }
 #nswoqyplju .gt_indent_5 { text-indent: calc(5px * 5); }
 #nswoqyplju .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nswoqyplju .gt_row_group_first td { border-top-width: 2px; }
 #nswoqyplju .gt_row_group_first th { border-top-width: 2px; }
 #nswoqyplju .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nswoqyplju .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nswoqyplju .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nswoqyplju .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nswoqyplju .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nswoqyplju .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nswoqyplju .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nswoqyplju .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nswoqyplju .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nswoqyplju .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nswoqyplju .gt_left { text-align: left; }
 #nswoqyplju .gt_center { text-align: center; }
 #nswoqyplju .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nswoqyplju .gt_font_normal { font-weight: normal; }
 #nswoqyplju .gt_font_bold { font-weight: bold; }
 #nswoqyplju .gt_font_italic { font-style: italic; }
 #nswoqyplju .gt_super { font-size: 65%; }
 #nswoqyplju .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nswoqyplju .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nswoqyplju .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nswoqyplju .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nswoqyplju .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nswoqyplju .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| country            | population |
|--------------------|------------|
| India              | 1417173173 |
| China              | 1412175000 |
| United States      | 333287557  |
| Indonesia          | 275501339  |
| Pakistan           | 235824862  |
| Nigeria            | 218541212  |
| Brazil             | 215313498  |
| Bangladesh         | 171186372  |
| Russian Federation | 143555736  |
| Mexico             | 127504125  |


A very important thing to note here is that the table now has one column. Before, when there was no **Stub**, two columns were present (with the **Column Labels** of `"country_name"` and `"population"`) but now column number `1` (the only column remaining) is `population`.


# Row Groups

Grouping is most useful when your data has a natural categorical structure and you want readers to compare within and across categories. Rather than forcing the reader to mentally sort the rows, row groups do that work up front.

Let's incorporate row groups into the display table. This divides rows into groups, creating *row groups*, and results in a display of a *row group labels* right above each group. This can be easily done with a table containing row labels and the key is to use the `groupname_col=` argument of the [GT](../reference/GT.md#great_tables.GT) class. Here we will create four row groups (with row group labels `"Asia"`, `"Americas"`, `"Africa"`, and `"Europe"`) to have a grouping of rows.


``` python
regions = {
    "India": "Asia", "China": "Asia", "Indonesia": "Asia", "Pakistan": "Asia",
    "Bangladesh": "Asia", "United States": "Americas", "Brazil": "Americas",
    "Mexico": "Americas", "Nigeria": "Africa", "Russian Federation": "Europe",
}

country_groups = countries_mini.assign(region = countries_mini["country_name"].map(regions))

(
    GT(country_groups)
    .tab_stub(rowname_col="country_name", groupname_col="region")
    .tab_stubhead(label="country")
)
```


<style>
#vdazpxftrq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vdazpxftrq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vdazpxftrq p { margin: 0; padding: 0; }
 #vdazpxftrq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vdazpxftrq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vdazpxftrq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vdazpxftrq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vdazpxftrq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vdazpxftrq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vdazpxftrq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vdazpxftrq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vdazpxftrq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vdazpxftrq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vdazpxftrq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vdazpxftrq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vdazpxftrq .gt_spanner_row { border-bottom-style: hidden; }
 #vdazpxftrq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vdazpxftrq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vdazpxftrq .gt_from_md> :first-child { margin-top: 0; }
 #vdazpxftrq .gt_from_md> :last-child { margin-bottom: 0; }
 #vdazpxftrq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vdazpxftrq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vdazpxftrq .gt_indent_1 { text-indent: 5px; }
 #vdazpxftrq .gt_indent_2 { text-indent: calc(5px * 2); }
 #vdazpxftrq .gt_indent_3 { text-indent: calc(5px * 3); }
 #vdazpxftrq .gt_indent_4 { text-indent: calc(5px * 4); }
 #vdazpxftrq .gt_indent_5 { text-indent: calc(5px * 5); }
 #vdazpxftrq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vdazpxftrq .gt_row_group_first td { border-top-width: 2px; }
 #vdazpxftrq .gt_row_group_first th { border-top-width: 2px; }
 #vdazpxftrq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vdazpxftrq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vdazpxftrq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vdazpxftrq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vdazpxftrq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vdazpxftrq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vdazpxftrq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vdazpxftrq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vdazpxftrq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vdazpxftrq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vdazpxftrq .gt_left { text-align: left; }
 #vdazpxftrq .gt_center { text-align: center; }
 #vdazpxftrq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vdazpxftrq .gt_font_normal { font-weight: normal; }
 #vdazpxftrq .gt_font_bold { font-weight: bold; }
 #vdazpxftrq .gt_font_italic { font-style: italic; }
 #vdazpxftrq .gt_super { font-size: 65%; }
 #vdazpxftrq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vdazpxftrq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vdazpxftrq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vdazpxftrq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vdazpxftrq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vdazpxftrq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th id="country" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">country</th>
<th id="population" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">population</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="2" id="Asia" class="gt_group_heading" scope="colgroup">Asia</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">India</td>
<td class="gt_row gt_right" headers="Asia stub-1 population">1417173173</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">China</td>
<td class="gt_row gt_right" headers="Asia stub-2 population">1412175000</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Indonesia</td>
<td class="gt_row gt_right" headers="Asia stub-4 population">275501339</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">Pakistan</td>
<td class="gt_row gt_right" headers="Asia stub-5 population">235824862</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">Bangladesh</td>
<td class="gt_row gt_right" headers="Asia stub-8 population">171186372</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" id="Americas" class="gt_group_heading" scope="colgroup">Americas</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">United States</td>
<td class="gt_row gt_right" headers="Americas stub-3 population">333287557</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">Brazil</td>
<td class="gt_row gt_right" headers="Americas stub-7 population">215313498</td>
</tr>
<tr>
<td id="stub-10" class="gt_row gt_left gt_stub" scope="row">Mexico</td>
<td class="gt_row gt_right" headers="Americas stub-10 population">127504125</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" id="Africa" class="gt_group_heading" scope="colgroup">Africa</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">Nigeria</td>
<td class="gt_row gt_right" headers="Africa stub-6 population">218541212</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" id="Europe" class="gt_group_heading" scope="colgroup">Europe</td>
</tr>
<tr>
<td id="stub-9" class="gt_row gt_left gt_stub" scope="row">Russian Federation</td>
<td class="gt_row gt_right" headers="Europe stub-9 population">143555736</td>
</tr>
</tbody>
</table>


The table now groups its rows by region, with labels appearing above each group. Row groups make it much easier for readers to scan and compare related entries.


# GT Convenience Arguments

Rather than using the [tab_stub()](../reference/GT.tab_stub.md#great_tables.GT.tab_stub) method, the `GT(rowname_col=..., groupname_col=...)` arguments provide a quick way to specify row names and groups.


``` python
GT(country_groups, rowname_col="country_name", groupname_col="region")
```


<style>
#vexrtucfzd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vexrtucfzd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vexrtucfzd p { margin: 0; padding: 0; }
 #vexrtucfzd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vexrtucfzd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vexrtucfzd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vexrtucfzd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vexrtucfzd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vexrtucfzd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vexrtucfzd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vexrtucfzd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vexrtucfzd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vexrtucfzd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vexrtucfzd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vexrtucfzd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vexrtucfzd .gt_spanner_row { border-bottom-style: hidden; }
 #vexrtucfzd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vexrtucfzd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vexrtucfzd .gt_from_md> :first-child { margin-top: 0; }
 #vexrtucfzd .gt_from_md> :last-child { margin-bottom: 0; }
 #vexrtucfzd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vexrtucfzd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vexrtucfzd .gt_indent_1 { text-indent: 5px; }
 #vexrtucfzd .gt_indent_2 { text-indent: calc(5px * 2); }
 #vexrtucfzd .gt_indent_3 { text-indent: calc(5px * 3); }
 #vexrtucfzd .gt_indent_4 { text-indent: calc(5px * 4); }
 #vexrtucfzd .gt_indent_5 { text-indent: calc(5px * 5); }
 #vexrtucfzd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vexrtucfzd .gt_row_group_first td { border-top-width: 2px; }
 #vexrtucfzd .gt_row_group_first th { border-top-width: 2px; }
 #vexrtucfzd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vexrtucfzd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vexrtucfzd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vexrtucfzd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vexrtucfzd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vexrtucfzd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vexrtucfzd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vexrtucfzd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vexrtucfzd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vexrtucfzd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vexrtucfzd .gt_left { text-align: left; }
 #vexrtucfzd .gt_center { text-align: center; }
 #vexrtucfzd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vexrtucfzd .gt_font_normal { font-weight: normal; }
 #vexrtucfzd .gt_font_bold { font-weight: bold; }
 #vexrtucfzd .gt_font_italic { font-style: italic; }
 #vexrtucfzd .gt_super { font-size: 65%; }
 #vexrtucfzd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vexrtucfzd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vexrtucfzd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vexrtucfzd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vexrtucfzd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vexrtucfzd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" scope="col"></th>
<th id="population" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">population</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="2" id="Asia" class="gt_group_heading" scope="colgroup">Asia</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">India</td>
<td class="gt_row gt_right" headers="Asia stub-1 population">1417173173</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">China</td>
<td class="gt_row gt_right" headers="Asia stub-2 population">1412175000</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">Indonesia</td>
<td class="gt_row gt_right" headers="Asia stub-4 population">275501339</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">Pakistan</td>
<td class="gt_row gt_right" headers="Asia stub-5 population">235824862</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">Bangladesh</td>
<td class="gt_row gt_right" headers="Asia stub-8 population">171186372</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" id="Americas" class="gt_group_heading" scope="colgroup">Americas</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">United States</td>
<td class="gt_row gt_right" headers="Americas stub-3 population">333287557</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">Brazil</td>
<td class="gt_row gt_right" headers="Americas stub-7 population">215313498</td>
</tr>
<tr>
<td id="stub-10" class="gt_row gt_left gt_stub" scope="row">Mexico</td>
<td class="gt_row gt_right" headers="Americas stub-10 population">127504125</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" id="Africa" class="gt_group_heading" scope="colgroup">Africa</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">Nigeria</td>
<td class="gt_row gt_right" headers="Africa stub-6 population">218541212</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="2" id="Europe" class="gt_group_heading" scope="colgroup">Europe</td>
</tr>
<tr>
<td id="stub-9" class="gt_row gt_left gt_stub" scope="row">Russian Federation</td>
<td class="gt_row gt_right" headers="Europe stub-9 population">143555736</td>
</tr>
</tbody>
</table>


The stub provides a clear organizational framework for your data by separating identifiers from values. Whether you simply need named rows or a fully grouped hierarchy, the combination of `rowname_col=`, `groupname_col=`, and [tab_stubhead()](../reference/GT.tab_stubhead.md#great_tables.GT.tab_stubhead) gives you precise control over how readers navigate your table.
