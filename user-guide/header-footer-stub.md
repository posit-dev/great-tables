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
#dcmicispkr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dcmicispkr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dcmicispkr p { margin: 0; padding: 0; }
 #dcmicispkr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dcmicispkr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dcmicispkr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dcmicispkr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dcmicispkr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dcmicispkr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dcmicispkr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dcmicispkr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dcmicispkr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dcmicispkr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dcmicispkr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dcmicispkr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dcmicispkr .gt_spanner_row { border-bottom-style: hidden; }
 #dcmicispkr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dcmicispkr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dcmicispkr .gt_from_md> :first-child { margin-top: 0; }
 #dcmicispkr .gt_from_md> :last-child { margin-bottom: 0; }
 #dcmicispkr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dcmicispkr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dcmicispkr .gt_indent_1 { text-indent: 5px; }
 #dcmicispkr .gt_indent_2 { text-indent: calc(5px * 2); }
 #dcmicispkr .gt_indent_3 { text-indent: calc(5px * 3); }
 #dcmicispkr .gt_indent_4 { text-indent: calc(5px * 4); }
 #dcmicispkr .gt_indent_5 { text-indent: calc(5px * 5); }
 #dcmicispkr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dcmicispkr .gt_row_group_first td { border-top-width: 2px; }
 #dcmicispkr .gt_row_group_first th { border-top-width: 2px; }
 #dcmicispkr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dcmicispkr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dcmicispkr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dcmicispkr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dcmicispkr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dcmicispkr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dcmicispkr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dcmicispkr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dcmicispkr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dcmicispkr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dcmicispkr .gt_left { text-align: left; }
 #dcmicispkr .gt_center { text-align: center; }
 #dcmicispkr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dcmicispkr .gt_font_normal { font-weight: normal; }
 #dcmicispkr .gt_font_bold { font-weight: bold; }
 #dcmicispkr .gt_font_italic { font-style: italic; }
 #dcmicispkr .gt_super { font-size: 65%; }
 #dcmicispkr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dcmicispkr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dcmicispkr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dcmicispkr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dcmicispkr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dcmicispkr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#oxeqredeih table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oxeqredeih thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oxeqredeih p { margin: 0; padding: 0; }
 #oxeqredeih .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oxeqredeih .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oxeqredeih .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oxeqredeih .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oxeqredeih .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oxeqredeih .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oxeqredeih .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oxeqredeih .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oxeqredeih .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oxeqredeih .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oxeqredeih .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oxeqredeih .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oxeqredeih .gt_spanner_row { border-bottom-style: hidden; }
 #oxeqredeih .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oxeqredeih .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #oxeqredeih .gt_from_md> :first-child { margin-top: 0; }
 #oxeqredeih .gt_from_md> :last-child { margin-bottom: 0; }
 #oxeqredeih .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #oxeqredeih .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #oxeqredeih .gt_indent_1 { text-indent: 5px; }
 #oxeqredeih .gt_indent_2 { text-indent: calc(5px * 2); }
 #oxeqredeih .gt_indent_3 { text-indent: calc(5px * 3); }
 #oxeqredeih .gt_indent_4 { text-indent: calc(5px * 4); }
 #oxeqredeih .gt_indent_5 { text-indent: calc(5px * 5); }
 #oxeqredeih .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oxeqredeih .gt_row_group_first td { border-top-width: 2px; }
 #oxeqredeih .gt_row_group_first th { border-top-width: 2px; }
 #oxeqredeih .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oxeqredeih .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oxeqredeih .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oxeqredeih .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oxeqredeih .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oxeqredeih .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oxeqredeih .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oxeqredeih .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oxeqredeih .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oxeqredeih .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oxeqredeih .gt_left { text-align: left; }
 #oxeqredeih .gt_center { text-align: center; }
 #oxeqredeih .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oxeqredeih .gt_font_normal { font-weight: normal; }
 #oxeqredeih .gt_font_bold { font-weight: bold; }
 #oxeqredeih .gt_font_italic { font-style: italic; }
 #oxeqredeih .gt_super { font-size: 65%; }
 #oxeqredeih .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oxeqredeih .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oxeqredeih .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oxeqredeih .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oxeqredeih .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oxeqredeih .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pbrzfrovkm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pbrzfrovkm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pbrzfrovkm p { margin: 0; padding: 0; }
 #pbrzfrovkm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pbrzfrovkm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pbrzfrovkm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pbrzfrovkm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pbrzfrovkm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pbrzfrovkm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pbrzfrovkm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pbrzfrovkm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pbrzfrovkm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pbrzfrovkm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pbrzfrovkm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pbrzfrovkm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pbrzfrovkm .gt_spanner_row { border-bottom-style: hidden; }
 #pbrzfrovkm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pbrzfrovkm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pbrzfrovkm .gt_from_md> :first-child { margin-top: 0; }
 #pbrzfrovkm .gt_from_md> :last-child { margin-bottom: 0; }
 #pbrzfrovkm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pbrzfrovkm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pbrzfrovkm .gt_indent_1 { text-indent: 5px; }
 #pbrzfrovkm .gt_indent_2 { text-indent: calc(5px * 2); }
 #pbrzfrovkm .gt_indent_3 { text-indent: calc(5px * 3); }
 #pbrzfrovkm .gt_indent_4 { text-indent: calc(5px * 4); }
 #pbrzfrovkm .gt_indent_5 { text-indent: calc(5px * 5); }
 #pbrzfrovkm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pbrzfrovkm .gt_row_group_first td { border-top-width: 2px; }
 #pbrzfrovkm .gt_row_group_first th { border-top-width: 2px; }
 #pbrzfrovkm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pbrzfrovkm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pbrzfrovkm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pbrzfrovkm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pbrzfrovkm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pbrzfrovkm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pbrzfrovkm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pbrzfrovkm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pbrzfrovkm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pbrzfrovkm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pbrzfrovkm .gt_left { text-align: left; }
 #pbrzfrovkm .gt_center { text-align: center; }
 #pbrzfrovkm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pbrzfrovkm .gt_font_normal { font-weight: normal; }
 #pbrzfrovkm .gt_font_bold { font-weight: bold; }
 #pbrzfrovkm .gt_font_italic { font-style: italic; }
 #pbrzfrovkm .gt_super { font-size: 65%; }
 #pbrzfrovkm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pbrzfrovkm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pbrzfrovkm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pbrzfrovkm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pbrzfrovkm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pbrzfrovkm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#pqchhgfgbj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pqchhgfgbj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pqchhgfgbj p { margin: 0; padding: 0; }
 #pqchhgfgbj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pqchhgfgbj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pqchhgfgbj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pqchhgfgbj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pqchhgfgbj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pqchhgfgbj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pqchhgfgbj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pqchhgfgbj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pqchhgfgbj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pqchhgfgbj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pqchhgfgbj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pqchhgfgbj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pqchhgfgbj .gt_spanner_row { border-bottom-style: hidden; }
 #pqchhgfgbj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pqchhgfgbj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pqchhgfgbj .gt_from_md> :first-child { margin-top: 0; }
 #pqchhgfgbj .gt_from_md> :last-child { margin-bottom: 0; }
 #pqchhgfgbj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pqchhgfgbj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pqchhgfgbj .gt_indent_1 { text-indent: 5px; }
 #pqchhgfgbj .gt_indent_2 { text-indent: calc(5px * 2); }
 #pqchhgfgbj .gt_indent_3 { text-indent: calc(5px * 3); }
 #pqchhgfgbj .gt_indent_4 { text-indent: calc(5px * 4); }
 #pqchhgfgbj .gt_indent_5 { text-indent: calc(5px * 5); }
 #pqchhgfgbj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pqchhgfgbj .gt_row_group_first td { border-top-width: 2px; }
 #pqchhgfgbj .gt_row_group_first th { border-top-width: 2px; }
 #pqchhgfgbj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pqchhgfgbj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pqchhgfgbj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pqchhgfgbj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #pqchhgfgbj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pqchhgfgbj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pqchhgfgbj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pqchhgfgbj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pqchhgfgbj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pqchhgfgbj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pqchhgfgbj .gt_left { text-align: left; }
 #pqchhgfgbj .gt_center { text-align: center; }
 #pqchhgfgbj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pqchhgfgbj .gt_font_normal { font-weight: normal; }
 #pqchhgfgbj .gt_font_bold { font-weight: bold; }
 #pqchhgfgbj .gt_font_italic { font-style: italic; }
 #pqchhgfgbj .gt_super { font-size: 65%; }
 #pqchhgfgbj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pqchhgfgbj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #pqchhgfgbj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pqchhgfgbj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pqchhgfgbj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pqchhgfgbj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zczjnzwjbf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zczjnzwjbf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zczjnzwjbf p { margin: 0; padding: 0; }
 #zczjnzwjbf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zczjnzwjbf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zczjnzwjbf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zczjnzwjbf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zczjnzwjbf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zczjnzwjbf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zczjnzwjbf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zczjnzwjbf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zczjnzwjbf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zczjnzwjbf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zczjnzwjbf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zczjnzwjbf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zczjnzwjbf .gt_spanner_row { border-bottom-style: hidden; }
 #zczjnzwjbf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zczjnzwjbf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zczjnzwjbf .gt_from_md> :first-child { margin-top: 0; }
 #zczjnzwjbf .gt_from_md> :last-child { margin-bottom: 0; }
 #zczjnzwjbf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zczjnzwjbf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zczjnzwjbf .gt_indent_1 { text-indent: 5px; }
 #zczjnzwjbf .gt_indent_2 { text-indent: calc(5px * 2); }
 #zczjnzwjbf .gt_indent_3 { text-indent: calc(5px * 3); }
 #zczjnzwjbf .gt_indent_4 { text-indent: calc(5px * 4); }
 #zczjnzwjbf .gt_indent_5 { text-indent: calc(5px * 5); }
 #zczjnzwjbf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zczjnzwjbf .gt_row_group_first td { border-top-width: 2px; }
 #zczjnzwjbf .gt_row_group_first th { border-top-width: 2px; }
 #zczjnzwjbf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zczjnzwjbf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zczjnzwjbf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zczjnzwjbf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zczjnzwjbf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zczjnzwjbf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zczjnzwjbf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zczjnzwjbf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zczjnzwjbf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zczjnzwjbf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zczjnzwjbf .gt_left { text-align: left; }
 #zczjnzwjbf .gt_center { text-align: center; }
 #zczjnzwjbf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zczjnzwjbf .gt_font_normal { font-weight: normal; }
 #zczjnzwjbf .gt_font_bold { font-weight: bold; }
 #zczjnzwjbf .gt_font_italic { font-style: italic; }
 #zczjnzwjbf .gt_super { font-size: 65%; }
 #zczjnzwjbf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zczjnzwjbf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zczjnzwjbf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zczjnzwjbf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zczjnzwjbf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zczjnzwjbf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#akzdlajqnv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#akzdlajqnv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#akzdlajqnv p { margin: 0; padding: 0; }
 #akzdlajqnv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #akzdlajqnv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #akzdlajqnv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #akzdlajqnv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #akzdlajqnv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #akzdlajqnv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #akzdlajqnv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #akzdlajqnv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #akzdlajqnv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #akzdlajqnv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #akzdlajqnv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #akzdlajqnv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #akzdlajqnv .gt_spanner_row { border-bottom-style: hidden; }
 #akzdlajqnv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #akzdlajqnv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #akzdlajqnv .gt_from_md> :first-child { margin-top: 0; }
 #akzdlajqnv .gt_from_md> :last-child { margin-bottom: 0; }
 #akzdlajqnv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #akzdlajqnv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #akzdlajqnv .gt_indent_1 { text-indent: 5px; }
 #akzdlajqnv .gt_indent_2 { text-indent: calc(5px * 2); }
 #akzdlajqnv .gt_indent_3 { text-indent: calc(5px * 3); }
 #akzdlajqnv .gt_indent_4 { text-indent: calc(5px * 4); }
 #akzdlajqnv .gt_indent_5 { text-indent: calc(5px * 5); }
 #akzdlajqnv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #akzdlajqnv .gt_row_group_first td { border-top-width: 2px; }
 #akzdlajqnv .gt_row_group_first th { border-top-width: 2px; }
 #akzdlajqnv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #akzdlajqnv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #akzdlajqnv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #akzdlajqnv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #akzdlajqnv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #akzdlajqnv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #akzdlajqnv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #akzdlajqnv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #akzdlajqnv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #akzdlajqnv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #akzdlajqnv .gt_left { text-align: left; }
 #akzdlajqnv .gt_center { text-align: center; }
 #akzdlajqnv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #akzdlajqnv .gt_font_normal { font-weight: normal; }
 #akzdlajqnv .gt_font_bold { font-weight: bold; }
 #akzdlajqnv .gt_font_italic { font-style: italic; }
 #akzdlajqnv .gt_super { font-size: 65%; }
 #akzdlajqnv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #akzdlajqnv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #akzdlajqnv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #akzdlajqnv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #akzdlajqnv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #akzdlajqnv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#hrxgdhugkn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hrxgdhugkn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hrxgdhugkn p { margin: 0; padding: 0; }
 #hrxgdhugkn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hrxgdhugkn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hrxgdhugkn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hrxgdhugkn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hrxgdhugkn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hrxgdhugkn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hrxgdhugkn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hrxgdhugkn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hrxgdhugkn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hrxgdhugkn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hrxgdhugkn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hrxgdhugkn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hrxgdhugkn .gt_spanner_row { border-bottom-style: hidden; }
 #hrxgdhugkn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hrxgdhugkn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hrxgdhugkn .gt_from_md> :first-child { margin-top: 0; }
 #hrxgdhugkn .gt_from_md> :last-child { margin-bottom: 0; }
 #hrxgdhugkn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hrxgdhugkn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hrxgdhugkn .gt_indent_1 { text-indent: 5px; }
 #hrxgdhugkn .gt_indent_2 { text-indent: calc(5px * 2); }
 #hrxgdhugkn .gt_indent_3 { text-indent: calc(5px * 3); }
 #hrxgdhugkn .gt_indent_4 { text-indent: calc(5px * 4); }
 #hrxgdhugkn .gt_indent_5 { text-indent: calc(5px * 5); }
 #hrxgdhugkn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hrxgdhugkn .gt_row_group_first td { border-top-width: 2px; }
 #hrxgdhugkn .gt_row_group_first th { border-top-width: 2px; }
 #hrxgdhugkn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hrxgdhugkn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hrxgdhugkn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hrxgdhugkn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hrxgdhugkn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hrxgdhugkn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hrxgdhugkn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hrxgdhugkn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hrxgdhugkn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hrxgdhugkn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hrxgdhugkn .gt_left { text-align: left; }
 #hrxgdhugkn .gt_center { text-align: center; }
 #hrxgdhugkn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hrxgdhugkn .gt_font_normal { font-weight: normal; }
 #hrxgdhugkn .gt_font_bold { font-weight: bold; }
 #hrxgdhugkn .gt_font_italic { font-style: italic; }
 #hrxgdhugkn .gt_super { font-size: 65%; }
 #hrxgdhugkn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hrxgdhugkn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hrxgdhugkn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hrxgdhugkn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hrxgdhugkn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hrxgdhugkn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
