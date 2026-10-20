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
#lohsibjzra table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lohsibjzra thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lohsibjzra p { margin: 0; padding: 0; }
 #lohsibjzra .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lohsibjzra .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lohsibjzra .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lohsibjzra .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lohsibjzra .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lohsibjzra .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lohsibjzra .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lohsibjzra .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lohsibjzra .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lohsibjzra .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lohsibjzra .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lohsibjzra .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lohsibjzra .gt_spanner_row { border-bottom-style: hidden; }
 #lohsibjzra .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lohsibjzra .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lohsibjzra .gt_from_md> :first-child { margin-top: 0; }
 #lohsibjzra .gt_from_md> :last-child { margin-bottom: 0; }
 #lohsibjzra .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lohsibjzra .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lohsibjzra .gt_indent_1 { text-indent: 5px; }
 #lohsibjzra .gt_indent_2 { text-indent: calc(5px * 2); }
 #lohsibjzra .gt_indent_3 { text-indent: calc(5px * 3); }
 #lohsibjzra .gt_indent_4 { text-indent: calc(5px * 4); }
 #lohsibjzra .gt_indent_5 { text-indent: calc(5px * 5); }
 #lohsibjzra .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lohsibjzra .gt_row_group_first td { border-top-width: 2px; }
 #lohsibjzra .gt_row_group_first th { border-top-width: 2px; }
 #lohsibjzra .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lohsibjzra .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lohsibjzra .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lohsibjzra .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lohsibjzra .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lohsibjzra .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lohsibjzra .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lohsibjzra .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lohsibjzra .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lohsibjzra .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lohsibjzra .gt_left { text-align: left; }
 #lohsibjzra .gt_center { text-align: center; }
 #lohsibjzra .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lohsibjzra .gt_font_normal { font-weight: normal; }
 #lohsibjzra .gt_font_bold { font-weight: bold; }
 #lohsibjzra .gt_font_italic { font-style: italic; }
 #lohsibjzra .gt_super { font-size: 65%; }
 #lohsibjzra .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lohsibjzra .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lohsibjzra .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lohsibjzra .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lohsibjzra .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lohsibjzra .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#lesvfhaujp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lesvfhaujp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lesvfhaujp p { margin: 0; padding: 0; }
 #lesvfhaujp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lesvfhaujp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lesvfhaujp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lesvfhaujp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lesvfhaujp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lesvfhaujp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lesvfhaujp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lesvfhaujp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lesvfhaujp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lesvfhaujp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lesvfhaujp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lesvfhaujp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lesvfhaujp .gt_spanner_row { border-bottom-style: hidden; }
 #lesvfhaujp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lesvfhaujp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lesvfhaujp .gt_from_md> :first-child { margin-top: 0; }
 #lesvfhaujp .gt_from_md> :last-child { margin-bottom: 0; }
 #lesvfhaujp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lesvfhaujp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lesvfhaujp .gt_indent_1 { text-indent: 5px; }
 #lesvfhaujp .gt_indent_2 { text-indent: calc(5px * 2); }
 #lesvfhaujp .gt_indent_3 { text-indent: calc(5px * 3); }
 #lesvfhaujp .gt_indent_4 { text-indent: calc(5px * 4); }
 #lesvfhaujp .gt_indent_5 { text-indent: calc(5px * 5); }
 #lesvfhaujp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lesvfhaujp .gt_row_group_first td { border-top-width: 2px; }
 #lesvfhaujp .gt_row_group_first th { border-top-width: 2px; }
 #lesvfhaujp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lesvfhaujp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lesvfhaujp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lesvfhaujp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lesvfhaujp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lesvfhaujp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lesvfhaujp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lesvfhaujp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lesvfhaujp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lesvfhaujp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lesvfhaujp .gt_left { text-align: left; }
 #lesvfhaujp .gt_center { text-align: center; }
 #lesvfhaujp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lesvfhaujp .gt_font_normal { font-weight: normal; }
 #lesvfhaujp .gt_font_bold { font-weight: bold; }
 #lesvfhaujp .gt_font_italic { font-style: italic; }
 #lesvfhaujp .gt_super { font-size: 65%; }
 #lesvfhaujp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lesvfhaujp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lesvfhaujp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lesvfhaujp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lesvfhaujp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lesvfhaujp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#jhkswgyfrl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#jhkswgyfrl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#jhkswgyfrl p { margin: 0; padding: 0; }
 #jhkswgyfrl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #jhkswgyfrl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #jhkswgyfrl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #jhkswgyfrl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #jhkswgyfrl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jhkswgyfrl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jhkswgyfrl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #jhkswgyfrl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #jhkswgyfrl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #jhkswgyfrl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #jhkswgyfrl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #jhkswgyfrl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #jhkswgyfrl .gt_spanner_row { border-bottom-style: hidden; }
 #jhkswgyfrl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #jhkswgyfrl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #jhkswgyfrl .gt_from_md> :first-child { margin-top: 0; }
 #jhkswgyfrl .gt_from_md> :last-child { margin-bottom: 0; }
 #jhkswgyfrl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #jhkswgyfrl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #jhkswgyfrl .gt_indent_1 { text-indent: 5px; }
 #jhkswgyfrl .gt_indent_2 { text-indent: calc(5px * 2); }
 #jhkswgyfrl .gt_indent_3 { text-indent: calc(5px * 3); }
 #jhkswgyfrl .gt_indent_4 { text-indent: calc(5px * 4); }
 #jhkswgyfrl .gt_indent_5 { text-indent: calc(5px * 5); }
 #jhkswgyfrl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #jhkswgyfrl .gt_row_group_first td { border-top-width: 2px; }
 #jhkswgyfrl .gt_row_group_first th { border-top-width: 2px; }
 #jhkswgyfrl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #jhkswgyfrl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jhkswgyfrl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jhkswgyfrl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #jhkswgyfrl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #jhkswgyfrl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #jhkswgyfrl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #jhkswgyfrl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #jhkswgyfrl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jhkswgyfrl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jhkswgyfrl .gt_left { text-align: left; }
 #jhkswgyfrl .gt_center { text-align: center; }
 #jhkswgyfrl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #jhkswgyfrl .gt_font_normal { font-weight: normal; }
 #jhkswgyfrl .gt_font_bold { font-weight: bold; }
 #jhkswgyfrl .gt_font_italic { font-style: italic; }
 #jhkswgyfrl .gt_super { font-size: 65%; }
 #jhkswgyfrl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jhkswgyfrl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #jhkswgyfrl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #jhkswgyfrl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #jhkswgyfrl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #jhkswgyfrl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qxldoajkxp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qxldoajkxp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qxldoajkxp p { margin: 0; padding: 0; }
 #qxldoajkxp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qxldoajkxp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qxldoajkxp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qxldoajkxp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qxldoajkxp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qxldoajkxp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qxldoajkxp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qxldoajkxp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qxldoajkxp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qxldoajkxp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qxldoajkxp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qxldoajkxp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qxldoajkxp .gt_spanner_row { border-bottom-style: hidden; }
 #qxldoajkxp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qxldoajkxp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qxldoajkxp .gt_from_md> :first-child { margin-top: 0; }
 #qxldoajkxp .gt_from_md> :last-child { margin-bottom: 0; }
 #qxldoajkxp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qxldoajkxp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qxldoajkxp .gt_indent_1 { text-indent: 5px; }
 #qxldoajkxp .gt_indent_2 { text-indent: calc(5px * 2); }
 #qxldoajkxp .gt_indent_3 { text-indent: calc(5px * 3); }
 #qxldoajkxp .gt_indent_4 { text-indent: calc(5px * 4); }
 #qxldoajkxp .gt_indent_5 { text-indent: calc(5px * 5); }
 #qxldoajkxp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qxldoajkxp .gt_row_group_first td { border-top-width: 2px; }
 #qxldoajkxp .gt_row_group_first th { border-top-width: 2px; }
 #qxldoajkxp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qxldoajkxp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qxldoajkxp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qxldoajkxp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qxldoajkxp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qxldoajkxp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qxldoajkxp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qxldoajkxp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qxldoajkxp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qxldoajkxp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qxldoajkxp .gt_left { text-align: left; }
 #qxldoajkxp .gt_center { text-align: center; }
 #qxldoajkxp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qxldoajkxp .gt_font_normal { font-weight: normal; }
 #qxldoajkxp .gt_font_bold { font-weight: bold; }
 #qxldoajkxp .gt_font_italic { font-style: italic; }
 #qxldoajkxp .gt_super { font-size: 65%; }
 #qxldoajkxp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qxldoajkxp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qxldoajkxp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qxldoajkxp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qxldoajkxp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qxldoajkxp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bekekflyrz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bekekflyrz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bekekflyrz p { margin: 0; padding: 0; }
 #bekekflyrz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bekekflyrz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bekekflyrz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bekekflyrz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bekekflyrz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bekekflyrz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bekekflyrz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bekekflyrz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bekekflyrz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bekekflyrz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bekekflyrz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bekekflyrz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bekekflyrz .gt_spanner_row { border-bottom-style: hidden; }
 #bekekflyrz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bekekflyrz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bekekflyrz .gt_from_md> :first-child { margin-top: 0; }
 #bekekflyrz .gt_from_md> :last-child { margin-bottom: 0; }
 #bekekflyrz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bekekflyrz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bekekflyrz .gt_indent_1 { text-indent: 5px; }
 #bekekflyrz .gt_indent_2 { text-indent: calc(5px * 2); }
 #bekekflyrz .gt_indent_3 { text-indent: calc(5px * 3); }
 #bekekflyrz .gt_indent_4 { text-indent: calc(5px * 4); }
 #bekekflyrz .gt_indent_5 { text-indent: calc(5px * 5); }
 #bekekflyrz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bekekflyrz .gt_row_group_first td { border-top-width: 2px; }
 #bekekflyrz .gt_row_group_first th { border-top-width: 2px; }
 #bekekflyrz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bekekflyrz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bekekflyrz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bekekflyrz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bekekflyrz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bekekflyrz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bekekflyrz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bekekflyrz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bekekflyrz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bekekflyrz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bekekflyrz .gt_left { text-align: left; }
 #bekekflyrz .gt_center { text-align: center; }
 #bekekflyrz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bekekflyrz .gt_font_normal { font-weight: normal; }
 #bekekflyrz .gt_font_bold { font-weight: bold; }
 #bekekflyrz .gt_font_italic { font-style: italic; }
 #bekekflyrz .gt_super { font-size: 65%; }
 #bekekflyrz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bekekflyrz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bekekflyrz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bekekflyrz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bekekflyrz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bekekflyrz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dqdjgxaytq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dqdjgxaytq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dqdjgxaytq p { margin: 0; padding: 0; }
 #dqdjgxaytq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dqdjgxaytq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dqdjgxaytq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dqdjgxaytq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dqdjgxaytq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dqdjgxaytq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dqdjgxaytq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dqdjgxaytq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dqdjgxaytq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dqdjgxaytq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dqdjgxaytq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dqdjgxaytq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dqdjgxaytq .gt_spanner_row { border-bottom-style: hidden; }
 #dqdjgxaytq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dqdjgxaytq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dqdjgxaytq .gt_from_md> :first-child { margin-top: 0; }
 #dqdjgxaytq .gt_from_md> :last-child { margin-bottom: 0; }
 #dqdjgxaytq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dqdjgxaytq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dqdjgxaytq .gt_indent_1 { text-indent: 5px; }
 #dqdjgxaytq .gt_indent_2 { text-indent: calc(5px * 2); }
 #dqdjgxaytq .gt_indent_3 { text-indent: calc(5px * 3); }
 #dqdjgxaytq .gt_indent_4 { text-indent: calc(5px * 4); }
 #dqdjgxaytq .gt_indent_5 { text-indent: calc(5px * 5); }
 #dqdjgxaytq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dqdjgxaytq .gt_row_group_first td { border-top-width: 2px; }
 #dqdjgxaytq .gt_row_group_first th { border-top-width: 2px; }
 #dqdjgxaytq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dqdjgxaytq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dqdjgxaytq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dqdjgxaytq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dqdjgxaytq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dqdjgxaytq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dqdjgxaytq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dqdjgxaytq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dqdjgxaytq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dqdjgxaytq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dqdjgxaytq .gt_left { text-align: left; }
 #dqdjgxaytq .gt_center { text-align: center; }
 #dqdjgxaytq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dqdjgxaytq .gt_font_normal { font-weight: normal; }
 #dqdjgxaytq .gt_font_bold { font-weight: bold; }
 #dqdjgxaytq .gt_font_italic { font-style: italic; }
 #dqdjgxaytq .gt_super { font-size: 65%; }
 #dqdjgxaytq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dqdjgxaytq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dqdjgxaytq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dqdjgxaytq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dqdjgxaytq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dqdjgxaytq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#qifgzuemsu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qifgzuemsu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qifgzuemsu p { margin: 0; padding: 0; }
 #qifgzuemsu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qifgzuemsu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qifgzuemsu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qifgzuemsu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qifgzuemsu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qifgzuemsu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qifgzuemsu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qifgzuemsu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qifgzuemsu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qifgzuemsu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qifgzuemsu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qifgzuemsu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qifgzuemsu .gt_spanner_row { border-bottom-style: hidden; }
 #qifgzuemsu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qifgzuemsu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qifgzuemsu .gt_from_md> :first-child { margin-top: 0; }
 #qifgzuemsu .gt_from_md> :last-child { margin-bottom: 0; }
 #qifgzuemsu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qifgzuemsu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qifgzuemsu .gt_indent_1 { text-indent: 5px; }
 #qifgzuemsu .gt_indent_2 { text-indent: calc(5px * 2); }
 #qifgzuemsu .gt_indent_3 { text-indent: calc(5px * 3); }
 #qifgzuemsu .gt_indent_4 { text-indent: calc(5px * 4); }
 #qifgzuemsu .gt_indent_5 { text-indent: calc(5px * 5); }
 #qifgzuemsu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qifgzuemsu .gt_row_group_first td { border-top-width: 2px; }
 #qifgzuemsu .gt_row_group_first th { border-top-width: 2px; }
 #qifgzuemsu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qifgzuemsu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qifgzuemsu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qifgzuemsu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qifgzuemsu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qifgzuemsu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qifgzuemsu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qifgzuemsu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qifgzuemsu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qifgzuemsu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qifgzuemsu .gt_left { text-align: left; }
 #qifgzuemsu .gt_center { text-align: center; }
 #qifgzuemsu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qifgzuemsu .gt_font_normal { font-weight: normal; }
 #qifgzuemsu .gt_font_bold { font-weight: bold; }
 #qifgzuemsu .gt_font_italic { font-style: italic; }
 #qifgzuemsu .gt_super { font-size: 65%; }
 #qifgzuemsu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qifgzuemsu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qifgzuemsu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qifgzuemsu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qifgzuemsu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qifgzuemsu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
