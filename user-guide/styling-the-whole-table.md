# Styling the Whole Table

In [Styling the Table Body](styling-the-table-body.md), we discussed styling table data with [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style). In this article we'll cover how the same method can be used to style many other parts of the table, like the header, specific spanner labels, the footer, and more. By targeting different location specifiers, you can apply fill colors, borders, and text styles to virtually any region of your table.

Whole-table styling is valuable when you want to establish visual hierarchy or brand consistency across the table. For example, giving the header a distinct background separates it from the data, while styling the stub helps readers distinguish identifiers from values. This kind of structural styling works well alongside the cell-level techniques covered on the previous page.


# All locations example

Below is a comprehensive example that shows all possible `loc` specifiers being used. Each table part receives a distinct background color so you can see exactly which region each specifier targets.


``` python
from great_tables import GT, exibble, loc, style

# https://colorbrewer2.org/#type=qualitative&scheme=Paired&n=12 and grey
brewer_colors = [
    "#a6cee3",
    "#1f78b4",
    "#b2df8a",
    "#33a02c",
    "#fb9a99",
    "#e31a1c",
    "#fdbf6f",
    "#ff7f00",
    "#cab2d6",
    "#6a3d9a",
    "#ffff99",
    "#b15928",
    "#808080",
]

c = iter(brewer_colors)

gt = (
    GT(exibble.loc[[0, 1, 4], ["num", "char", "fctr", "row", "group"]])
    .tab_header("title", "subtitle")
    .tab_stub(rowname_col="row", groupname_col="group")
    .tab_source_note("yo")
    .tab_spanner("spanner", ["char", "fctr"])
    .tab_stubhead("stubhead")
    .grand_summary_rows(fns={"Total": lambda x: x.sum(numeric_only=True)})
)

(
    gt.tab_style(style.fill(next(c)), loc.body())
    # Columns -----------
    # TODO: appears in browser, but not vs code
    .tab_style(style.fill(next(c)), loc.column_labels(columns="num"))
    .tab_style(style.fill(next(c)), loc.column_header())
    .tab_style(style.fill(next(c)), loc.spanner_labels(ids=["spanner"]))
    # Header -----------
    .tab_style(style.fill(next(c)), loc.header())
    .tab_style(style.fill(next(c)), loc.subtitle())
    .tab_style(style.fill(next(c)), loc.title())
    # Footer -----------
    .tab_style(style.borders(weight="3px"), loc.source_notes())
    .tab_style(style.fill(next(c)), loc.footer())
    # Stub --------------
    .tab_style(style.fill(next(c)), loc.row_groups())
    .tab_style(style.borders(weight="3px"), loc.stub(rows=1))
    .tab_style(style.fill(next(c)), loc.stub())
    .tab_style(style.fill(next(c)), loc.stubhead())
    # Summary Rows --------------
    .tab_style(style.fill(next(c)), loc.grand_summary())
    .tab_style(style.fill(next(c)), loc.grand_summary_stub())
)
```


<style>
#elexznbwzb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#elexznbwzb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#elexznbwzb p { margin: 0; padding: 0; }
 #elexznbwzb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #elexznbwzb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #elexznbwzb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #elexznbwzb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #elexznbwzb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #elexznbwzb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #elexznbwzb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #elexznbwzb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #elexznbwzb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #elexznbwzb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #elexznbwzb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #elexznbwzb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #elexznbwzb .gt_spanner_row { border-bottom-style: hidden; }
 #elexznbwzb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #elexznbwzb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #elexznbwzb .gt_from_md> :first-child { margin-top: 0; }
 #elexznbwzb .gt_from_md> :last-child { margin-bottom: 0; }
 #elexznbwzb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #elexznbwzb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #elexznbwzb .gt_indent_1 { text-indent: 5px; }
 #elexznbwzb .gt_indent_2 { text-indent: calc(5px * 2); }
 #elexznbwzb .gt_indent_3 { text-indent: calc(5px * 3); }
 #elexznbwzb .gt_indent_4 { text-indent: calc(5px * 4); }
 #elexznbwzb .gt_indent_5 { text-indent: calc(5px * 5); }
 #elexznbwzb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #elexznbwzb .gt_row_group_first td { border-top-width: 2px; }
 #elexznbwzb .gt_row_group_first th { border-top-width: 2px; }
 #elexznbwzb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #elexznbwzb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #elexznbwzb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #elexznbwzb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #elexznbwzb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #elexznbwzb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #elexznbwzb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #elexznbwzb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #elexznbwzb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #elexznbwzb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #elexznbwzb .gt_left { text-align: left; }
 #elexznbwzb .gt_center { text-align: center; }
 #elexznbwzb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #elexznbwzb .gt_font_normal { font-weight: normal; }
 #elexznbwzb .gt_font_bold { font-weight: bold; }
 #elexznbwzb .gt_font_italic { font-style: italic; }
 #elexznbwzb .gt_super { font-size: 65%; }
 #elexznbwzb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #elexznbwzb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #elexznbwzb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #elexznbwzb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #elexznbwzb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #elexznbwzb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal" style="background-color: #fb9a99; background-color: #fdbf6f">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="background-color: #fb9a99; background-color: #e31a1c">subtitle</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="stubhead" class="gt_col_heading gt_columns_bottom_border gt_left" style="background-color: #ffff99" scope="col">stubhead</th>
<th rowspan="2" id="num" class="gt_col_heading gt_columns_bottom_border gt_right" style="background-color: #b2df8a; background-color: #1f78b4" scope="col">num</th>
<th colspan="2" id="spanner" class="gt_center gt_columns_top_border gt_column_spanner_outer" style="background-color: #b2df8a; background-color: #33a02c" scope="colgroup">spanner</th>
</tr>
<tr class="gt_col_headings">
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" style="background-color: #b2df8a" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" style="background-color: #b2df8a" scope="col">fctr</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading" style="background-color: #cab2d6">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" style="background-color: #6a3d9a">row_1</td>
<td class="gt_row gt_right" style="background-color: #a6cee3">0.1111</td>
<td class="gt_row gt_left" style="background-color: #a6cee3">apricot</td>
<td class="gt_row gt_left" style="background-color: #a6cee3">one</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="border-top: 3px solid #000000; border-bottom: 3px solid #000000; border-left: 3px solid #000000; border-right: 3px solid #000000; background-color: #6a3d9a">row_2</td>
<td class="gt_row gt_right" style="background-color: #a6cee3">2.222</td>
<td class="gt_row gt_left" style="background-color: #a6cee3">banana</td>
<td class="gt_row gt_left" style="background-color: #a6cee3">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" style="background-color: #cab2d6">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="background-color: #6a3d9a">row_5</td>
<td class="gt_row gt_right" style="background-color: #a6cee3">5550.0</td>
<td class="gt_row gt_left" style="background-color: #a6cee3">None</td>
<td class="gt_row gt_left" style="background-color: #a6cee3">five</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" style="background-color: #808080">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" style="background-color: #b15928">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" style="background-color: #b15928">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" style="background-color: #b15928">---</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote" style="background-color: #ff7f00; border-top: 3px solid #000000; border-bottom: 3px solid #000000; border-left: 3px solid #000000; border-right: 3px solid #000000">yo</td>
</tr>
</tfoot>

</table>


Each color in the output maps to a specific table region, making it easy to identify the scope of every location specifier available in **Great Tables**.

This comprehensive example is useful as a reference, but in practice you would style only the parts that need visual distinction. The goal is to guide the reader's eye, not to color every region differently. Most tables benefit from styling just two or three regions (enough to create clear visual separation without overwhelming the content).


# Body

The table body is styled using [loc.body()](../reference/loc.body.md#great_tables.loc.body), which targets all data cells at once.


``` python
gt.tab_style(style.fill("yellow"), loc.body())
```


<style>
#imohltpzix table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#imohltpzix thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#imohltpzix p { margin: 0; padding: 0; }
 #imohltpzix .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #imohltpzix .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #imohltpzix .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #imohltpzix .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #imohltpzix .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #imohltpzix .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #imohltpzix .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #imohltpzix .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #imohltpzix .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #imohltpzix .gt_column_spanner_outer:first-child { padding-left: 0; }
 #imohltpzix .gt_column_spanner_outer:last-child { padding-right: 0; }
 #imohltpzix .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #imohltpzix .gt_spanner_row { border-bottom-style: hidden; }
 #imohltpzix .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #imohltpzix .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #imohltpzix .gt_from_md> :first-child { margin-top: 0; }
 #imohltpzix .gt_from_md> :last-child { margin-bottom: 0; }
 #imohltpzix .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #imohltpzix .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #imohltpzix .gt_indent_1 { text-indent: 5px; }
 #imohltpzix .gt_indent_2 { text-indent: calc(5px * 2); }
 #imohltpzix .gt_indent_3 { text-indent: calc(5px * 3); }
 #imohltpzix .gt_indent_4 { text-indent: calc(5px * 4); }
 #imohltpzix .gt_indent_5 { text-indent: calc(5px * 5); }
 #imohltpzix .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #imohltpzix .gt_row_group_first td { border-top-width: 2px; }
 #imohltpzix .gt_row_group_first th { border-top-width: 2px; }
 #imohltpzix .gt_striped { color: #333333; background-color: #F4F4F4; }
 #imohltpzix .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #imohltpzix .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #imohltpzix .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #imohltpzix .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #imohltpzix .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #imohltpzix .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #imohltpzix .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #imohltpzix .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #imohltpzix .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #imohltpzix .gt_left { text-align: left; }
 #imohltpzix .gt_center { text-align: center; }
 #imohltpzix .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #imohltpzix .gt_font_normal { font-weight: normal; }
 #imohltpzix .gt_font_bold { font-weight: bold; }
 #imohltpzix .gt_font_italic { font-style: italic; }
 #imohltpzix .gt_super { font-size: 65%; }
 #imohltpzix .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #imohltpzix .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #imohltpzix .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #imohltpzix .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #imohltpzix .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #imohltpzix .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">subtitle</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="stubhead" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">stubhead</th>
<th rowspan="2" id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th colspan="2" id="spanner" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">spanner</th>
</tr>
<tr class="gt_col_headings">
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right" style="background-color: yellow">0.1111</td>
<td class="gt_row gt_left" style="background-color: yellow">apricot</td>
<td class="gt_row gt_left" style="background-color: yellow">one</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right" style="background-color: yellow">2.222</td>
<td class="gt_row gt_left" style="background-color: yellow">banana</td>
<td class="gt_row gt_left" style="background-color: yellow">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right" style="background-color: yellow">5550.0</td>
<td class="gt_row gt_left" style="background-color: yellow">None</td>
<td class="gt_row gt_left" style="background-color: yellow">five</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">yo</td>
</tr>
</tfoot>

</table>


The yellow fill is applied to every data cell in the table body, leaving headers, stubs, and footers unchanged.


# Column labels

Column labels can be styled broadly with [loc.column_header()](../reference/loc.column_header.md#great_tables.loc.column_header), or you can target individual column labels and spanner labels separately for more precise control.


``` python
(
    gt
    .tab_style(style.fill("yellow"), loc.column_header())
    .tab_style(style.fill("blue"), loc.column_labels(columns="num"))
    .tab_style(style.fill("red"), loc.spanner_labels(ids=["spanner"]))
)
```


<style>
#softnkxtiw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#softnkxtiw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#softnkxtiw p { margin: 0; padding: 0; }
 #softnkxtiw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #softnkxtiw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #softnkxtiw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #softnkxtiw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #softnkxtiw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #softnkxtiw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #softnkxtiw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #softnkxtiw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #softnkxtiw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #softnkxtiw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #softnkxtiw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #softnkxtiw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #softnkxtiw .gt_spanner_row { border-bottom-style: hidden; }
 #softnkxtiw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #softnkxtiw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #softnkxtiw .gt_from_md> :first-child { margin-top: 0; }
 #softnkxtiw .gt_from_md> :last-child { margin-bottom: 0; }
 #softnkxtiw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #softnkxtiw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #softnkxtiw .gt_indent_1 { text-indent: 5px; }
 #softnkxtiw .gt_indent_2 { text-indent: calc(5px * 2); }
 #softnkxtiw .gt_indent_3 { text-indent: calc(5px * 3); }
 #softnkxtiw .gt_indent_4 { text-indent: calc(5px * 4); }
 #softnkxtiw .gt_indent_5 { text-indent: calc(5px * 5); }
 #softnkxtiw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #softnkxtiw .gt_row_group_first td { border-top-width: 2px; }
 #softnkxtiw .gt_row_group_first th { border-top-width: 2px; }
 #softnkxtiw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #softnkxtiw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #softnkxtiw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #softnkxtiw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #softnkxtiw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #softnkxtiw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #softnkxtiw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #softnkxtiw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #softnkxtiw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #softnkxtiw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #softnkxtiw .gt_left { text-align: left; }
 #softnkxtiw .gt_center { text-align: center; }
 #softnkxtiw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #softnkxtiw .gt_font_normal { font-weight: normal; }
 #softnkxtiw .gt_font_bold { font-weight: bold; }
 #softnkxtiw .gt_font_italic { font-style: italic; }
 #softnkxtiw .gt_super { font-size: 65%; }
 #softnkxtiw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #softnkxtiw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #softnkxtiw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #softnkxtiw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #softnkxtiw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #softnkxtiw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">subtitle</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="stubhead" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">stubhead</th>
<th rowspan="2" id="num" class="gt_col_heading gt_columns_bottom_border gt_right" style="background-color: yellow; background-color: blue" scope="col">num</th>
<th colspan="2" id="spanner" class="gt_center gt_columns_top_border gt_column_spanner_outer" style="background-color: yellow; background-color: red" scope="colgroup">spanner</th>
</tr>
<tr class="gt_col_headings">
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" style="background-color: yellow" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" style="background-color: yellow" scope="col">fctr</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">yo</td>
</tr>
</tfoot>

</table>


Here, [loc.column_header()](../reference/loc.column_header.md#great_tables.loc.column_header) applies a yellow background to the entire column labels row, then individual labels and spanners are overridden with more specific colors. This layered approach lets you set a base style and refine as needed.


# Header

The header area includes both the title and subtitle. You can style the entire header as one unit with [loc.header()](../reference/loc.header.md#great_tables.loc.header), or target the title and subtitle individually.


``` python
(
    gt.tab_style(style.fill("yellow"), loc.header())
    .tab_style(style.fill("blue"), loc.title())
    .tab_style(style.fill("red"), loc.subtitle())
)
```


<style>
#zsgcdlhazz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zsgcdlhazz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zsgcdlhazz p { margin: 0; padding: 0; }
 #zsgcdlhazz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zsgcdlhazz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zsgcdlhazz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zsgcdlhazz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zsgcdlhazz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zsgcdlhazz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zsgcdlhazz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zsgcdlhazz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zsgcdlhazz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zsgcdlhazz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zsgcdlhazz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zsgcdlhazz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zsgcdlhazz .gt_spanner_row { border-bottom-style: hidden; }
 #zsgcdlhazz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zsgcdlhazz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zsgcdlhazz .gt_from_md> :first-child { margin-top: 0; }
 #zsgcdlhazz .gt_from_md> :last-child { margin-bottom: 0; }
 #zsgcdlhazz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zsgcdlhazz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zsgcdlhazz .gt_indent_1 { text-indent: 5px; }
 #zsgcdlhazz .gt_indent_2 { text-indent: calc(5px * 2); }
 #zsgcdlhazz .gt_indent_3 { text-indent: calc(5px * 3); }
 #zsgcdlhazz .gt_indent_4 { text-indent: calc(5px * 4); }
 #zsgcdlhazz .gt_indent_5 { text-indent: calc(5px * 5); }
 #zsgcdlhazz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zsgcdlhazz .gt_row_group_first td { border-top-width: 2px; }
 #zsgcdlhazz .gt_row_group_first th { border-top-width: 2px; }
 #zsgcdlhazz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zsgcdlhazz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zsgcdlhazz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zsgcdlhazz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zsgcdlhazz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zsgcdlhazz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zsgcdlhazz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zsgcdlhazz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zsgcdlhazz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zsgcdlhazz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zsgcdlhazz .gt_left { text-align: left; }
 #zsgcdlhazz .gt_center { text-align: center; }
 #zsgcdlhazz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zsgcdlhazz .gt_font_normal { font-weight: normal; }
 #zsgcdlhazz .gt_font_bold { font-weight: bold; }
 #zsgcdlhazz .gt_font_italic { font-style: italic; }
 #zsgcdlhazz .gt_super { font-size: 65%; }
 #zsgcdlhazz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zsgcdlhazz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zsgcdlhazz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zsgcdlhazz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zsgcdlhazz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zsgcdlhazz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal" style="background-color: yellow; background-color: blue">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="background-color: yellow; background-color: red">subtitle</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="stubhead" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">stubhead</th>
<th rowspan="2" id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th colspan="2" id="spanner" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">spanner</th>
</tr>
<tr class="gt_col_headings">
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">yo</td>
</tr>
</tfoot>

</table>


The yellow covers the full header area, while the blue and red target the title and subtitle independently. When styles overlap, the more specific location wins.


# Footer

The footer contains source notes and can be styled as a whole with [loc.footer()](../reference/loc.footer.md#great_tables.loc.footer) or at the individual source note level with [loc.source_notes()](../reference/loc.source_notes.md#great_tables.loc.source_notes).


``` python
(
    gt.tab_style(
        style.fill("yellow"),
        loc.source_notes(),
    ).tab_style(
        style.borders(weight="3px"),
        loc.footer(),
    )
)
```


<style>
#lamohvdlyr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lamohvdlyr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lamohvdlyr p { margin: 0; padding: 0; }
 #lamohvdlyr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lamohvdlyr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lamohvdlyr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lamohvdlyr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lamohvdlyr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lamohvdlyr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lamohvdlyr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lamohvdlyr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lamohvdlyr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lamohvdlyr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lamohvdlyr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lamohvdlyr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lamohvdlyr .gt_spanner_row { border-bottom-style: hidden; }
 #lamohvdlyr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lamohvdlyr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lamohvdlyr .gt_from_md> :first-child { margin-top: 0; }
 #lamohvdlyr .gt_from_md> :last-child { margin-bottom: 0; }
 #lamohvdlyr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lamohvdlyr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lamohvdlyr .gt_indent_1 { text-indent: 5px; }
 #lamohvdlyr .gt_indent_2 { text-indent: calc(5px * 2); }
 #lamohvdlyr .gt_indent_3 { text-indent: calc(5px * 3); }
 #lamohvdlyr .gt_indent_4 { text-indent: calc(5px * 4); }
 #lamohvdlyr .gt_indent_5 { text-indent: calc(5px * 5); }
 #lamohvdlyr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lamohvdlyr .gt_row_group_first td { border-top-width: 2px; }
 #lamohvdlyr .gt_row_group_first th { border-top-width: 2px; }
 #lamohvdlyr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lamohvdlyr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lamohvdlyr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lamohvdlyr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lamohvdlyr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lamohvdlyr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lamohvdlyr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lamohvdlyr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lamohvdlyr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lamohvdlyr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lamohvdlyr .gt_left { text-align: left; }
 #lamohvdlyr .gt_center { text-align: center; }
 #lamohvdlyr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lamohvdlyr .gt_font_normal { font-weight: normal; }
 #lamohvdlyr .gt_font_bold { font-weight: bold; }
 #lamohvdlyr .gt_font_italic { font-style: italic; }
 #lamohvdlyr .gt_super { font-size: 65%; }
 #lamohvdlyr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lamohvdlyr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lamohvdlyr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lamohvdlyr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lamohvdlyr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lamohvdlyr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">subtitle</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="stubhead" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">stubhead</th>
<th rowspan="2" id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th colspan="2" id="spanner" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">spanner</th>
</tr>
<tr class="gt_col_headings">
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote" style="border-top: 3px solid #000000; border-bottom: 3px solid #000000; border-left: 3px solid #000000; border-right: 3px solid #000000; background-color: yellow">yo</td>
</tr>
</tfoot>

</table>


The source notes receive a yellow fill, while the entire footer region gets a heavy border. Both [loc.footer()](../reference/loc.footer.md#great_tables.loc.footer) and [loc.source_notes()](../reference/loc.source_notes.md#great_tables.loc.source_notes) target the same visual area but at different levels of granularity.


# Stub

The stub region includes row labels and row group labels. You can style these elements together or individually, and even target specific rows within the stub.


``` python
(
    gt.tab_style(style.fill("yellow"), loc.stub())
    .tab_style(style.fill("blue"), loc.row_groups())
    .tab_style(
        style.borders(style="dashed", weight="3px", color="red"),
        loc.stub(rows=[1]),
    )
)
```


<style>
#wnqujbjduj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wnqujbjduj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wnqujbjduj p { margin: 0; padding: 0; }
 #wnqujbjduj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wnqujbjduj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wnqujbjduj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wnqujbjduj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wnqujbjduj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wnqujbjduj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnqujbjduj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wnqujbjduj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wnqujbjduj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wnqujbjduj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wnqujbjduj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wnqujbjduj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wnqujbjduj .gt_spanner_row { border-bottom-style: hidden; }
 #wnqujbjduj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wnqujbjduj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wnqujbjduj .gt_from_md> :first-child { margin-top: 0; }
 #wnqujbjduj .gt_from_md> :last-child { margin-bottom: 0; }
 #wnqujbjduj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wnqujbjduj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wnqujbjduj .gt_indent_1 { text-indent: 5px; }
 #wnqujbjduj .gt_indent_2 { text-indent: calc(5px * 2); }
 #wnqujbjduj .gt_indent_3 { text-indent: calc(5px * 3); }
 #wnqujbjduj .gt_indent_4 { text-indent: calc(5px * 4); }
 #wnqujbjduj .gt_indent_5 { text-indent: calc(5px * 5); }
 #wnqujbjduj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wnqujbjduj .gt_row_group_first td { border-top-width: 2px; }
 #wnqujbjduj .gt_row_group_first th { border-top-width: 2px; }
 #wnqujbjduj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wnqujbjduj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnqujbjduj .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wnqujbjduj .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wnqujbjduj .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wnqujbjduj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wnqujbjduj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wnqujbjduj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wnqujbjduj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnqujbjduj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wnqujbjduj .gt_left { text-align: left; }
 #wnqujbjduj .gt_center { text-align: center; }
 #wnqujbjduj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wnqujbjduj .gt_font_normal { font-weight: normal; }
 #wnqujbjduj .gt_font_bold { font-weight: bold; }
 #wnqujbjduj .gt_font_italic { font-style: italic; }
 #wnqujbjduj .gt_super { font-size: 65%; }
 #wnqujbjduj .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnqujbjduj .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wnqujbjduj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wnqujbjduj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wnqujbjduj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wnqujbjduj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">subtitle</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="stubhead" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">stubhead</th>
<th rowspan="2" id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th colspan="2" id="spanner" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">spanner</th>
</tr>
<tr class="gt_col_headings">
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading" style="background-color: blue">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow; border-top: 3px dashed red; border-bottom: 3px dashed red; border-left: 3px dashed red; border-right: 3px dashed red">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" style="background-color: blue">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" style="background-color: yellow">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">yo</td>
</tr>
</tfoot>

</table>


The stub fills yellow, row group labels turn blue, and a dashed red border highlights a specific row in the stub. Using `rows=` within [loc.stub()](../reference/loc.stub.md#great_tables.loc.stub) lets you target individual row labels.


# Stubhead

The stubhead label sits above the stub column and can be styled with [loc.stubhead()](../reference/loc.stubhead.md#great_tables.loc.stubhead).


``` python
gt.tab_style(style.fill("yellow"), loc.stubhead())
```


<style>
#sliltboogh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sliltboogh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sliltboogh p { margin: 0; padding: 0; }
 #sliltboogh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sliltboogh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sliltboogh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sliltboogh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sliltboogh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sliltboogh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sliltboogh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sliltboogh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sliltboogh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sliltboogh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sliltboogh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sliltboogh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sliltboogh .gt_spanner_row { border-bottom-style: hidden; }
 #sliltboogh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sliltboogh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sliltboogh .gt_from_md> :first-child { margin-top: 0; }
 #sliltboogh .gt_from_md> :last-child { margin-bottom: 0; }
 #sliltboogh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sliltboogh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sliltboogh .gt_indent_1 { text-indent: 5px; }
 #sliltboogh .gt_indent_2 { text-indent: calc(5px * 2); }
 #sliltboogh .gt_indent_3 { text-indent: calc(5px * 3); }
 #sliltboogh .gt_indent_4 { text-indent: calc(5px * 4); }
 #sliltboogh .gt_indent_5 { text-indent: calc(5px * 5); }
 #sliltboogh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sliltboogh .gt_row_group_first td { border-top-width: 2px; }
 #sliltboogh .gt_row_group_first th { border-top-width: 2px; }
 #sliltboogh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sliltboogh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sliltboogh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sliltboogh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sliltboogh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sliltboogh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sliltboogh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sliltboogh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sliltboogh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sliltboogh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sliltboogh .gt_left { text-align: left; }
 #sliltboogh .gt_center { text-align: center; }
 #sliltboogh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sliltboogh .gt_font_normal { font-weight: normal; }
 #sliltboogh .gt_font_bold { font-weight: bold; }
 #sliltboogh .gt_font_italic { font-style: italic; }
 #sliltboogh .gt_super { font-size: 65%; }
 #sliltboogh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sliltboogh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sliltboogh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sliltboogh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sliltboogh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sliltboogh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">subtitle</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="stubhead" class="gt_col_heading gt_columns_bottom_border gt_left" style="background-color: yellow" scope="col">stubhead</th>
<th rowspan="2" id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th colspan="2" id="spanner" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">spanner</th>
</tr>
<tr class="gt_col_headings">
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">yo</td>
</tr>
</tfoot>

</table>


The stubhead label cell receives the yellow background. This is useful for visually linking the stubhead to the stub column below it.


# Grand Summary Rows

Grand summary rows appear at the bottom of the table. You can style the summary data cells and the summary stub area independently.


``` python
(
    gt.tab_style(
        style.fill("yellow"),
        loc.grand_summary_stub(),
    ).tab_style(
        style.fill("lightblue"),
        loc.grand_summary(),
    )
)
```


<style>
#njgfpadpgc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#njgfpadpgc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#njgfpadpgc p { margin: 0; padding: 0; }
 #njgfpadpgc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #njgfpadpgc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #njgfpadpgc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #njgfpadpgc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #njgfpadpgc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #njgfpadpgc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #njgfpadpgc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #njgfpadpgc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #njgfpadpgc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #njgfpadpgc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #njgfpadpgc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #njgfpadpgc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #njgfpadpgc .gt_spanner_row { border-bottom-style: hidden; }
 #njgfpadpgc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #njgfpadpgc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #njgfpadpgc .gt_from_md> :first-child { margin-top: 0; }
 #njgfpadpgc .gt_from_md> :last-child { margin-bottom: 0; }
 #njgfpadpgc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #njgfpadpgc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #njgfpadpgc .gt_indent_1 { text-indent: 5px; }
 #njgfpadpgc .gt_indent_2 { text-indent: calc(5px * 2); }
 #njgfpadpgc .gt_indent_3 { text-indent: calc(5px * 3); }
 #njgfpadpgc .gt_indent_4 { text-indent: calc(5px * 4); }
 #njgfpadpgc .gt_indent_5 { text-indent: calc(5px * 5); }
 #njgfpadpgc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #njgfpadpgc .gt_row_group_first td { border-top-width: 2px; }
 #njgfpadpgc .gt_row_group_first th { border-top-width: 2px; }
 #njgfpadpgc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #njgfpadpgc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #njgfpadpgc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #njgfpadpgc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #njgfpadpgc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #njgfpadpgc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #njgfpadpgc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #njgfpadpgc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #njgfpadpgc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #njgfpadpgc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #njgfpadpgc .gt_left { text-align: left; }
 #njgfpadpgc .gt_center { text-align: center; }
 #njgfpadpgc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #njgfpadpgc .gt_font_normal { font-weight: normal; }
 #njgfpadpgc .gt_font_bold { font-weight: bold; }
 #njgfpadpgc .gt_font_italic { font-style: italic; }
 #njgfpadpgc .gt_super { font-size: 65%; }
 #njgfpadpgc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #njgfpadpgc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #njgfpadpgc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #njgfpadpgc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #njgfpadpgc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #njgfpadpgc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">subtitle</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="stubhead" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">stubhead</th>
<th rowspan="2" id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th colspan="2" id="spanner" class="gt_center gt_columns_top_border gt_column_spanner_outer" scope="colgroup">spanner</th>
</tr>
<tr class="gt_col_headings">
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="4" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" style="background-color: yellow">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" style="background-color: lightblue">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" style="background-color: lightblue">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" style="background-color: lightblue">---</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">yo</td>
</tr>
</tfoot>

</table>


With [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) and the full set of `loc` specifiers, you can style every part of a **Great Tables** output. This gives you the ability to create cohesive visual themes, draw attention to specific structural elements, and ensure your table communicates effectively at every level.
