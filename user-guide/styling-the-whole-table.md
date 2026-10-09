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
#lfzjeuuzzw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lfzjeuuzzw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lfzjeuuzzw p { margin: 0; padding: 0; }
 #lfzjeuuzzw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lfzjeuuzzw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lfzjeuuzzw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lfzjeuuzzw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lfzjeuuzzw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lfzjeuuzzw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lfzjeuuzzw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lfzjeuuzzw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lfzjeuuzzw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lfzjeuuzzw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lfzjeuuzzw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lfzjeuuzzw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lfzjeuuzzw .gt_spanner_row { border-bottom-style: hidden; }
 #lfzjeuuzzw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lfzjeuuzzw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lfzjeuuzzw .gt_from_md> :first-child { margin-top: 0; }
 #lfzjeuuzzw .gt_from_md> :last-child { margin-bottom: 0; }
 #lfzjeuuzzw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lfzjeuuzzw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lfzjeuuzzw .gt_indent_1 { text-indent: 5px; }
 #lfzjeuuzzw .gt_indent_2 { text-indent: calc(5px * 2); }
 #lfzjeuuzzw .gt_indent_3 { text-indent: calc(5px * 3); }
 #lfzjeuuzzw .gt_indent_4 { text-indent: calc(5px * 4); }
 #lfzjeuuzzw .gt_indent_5 { text-indent: calc(5px * 5); }
 #lfzjeuuzzw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lfzjeuuzzw .gt_row_group_first td { border-top-width: 2px; }
 #lfzjeuuzzw .gt_row_group_first th { border-top-width: 2px; }
 #lfzjeuuzzw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lfzjeuuzzw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lfzjeuuzzw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lfzjeuuzzw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lfzjeuuzzw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lfzjeuuzzw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lfzjeuuzzw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lfzjeuuzzw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lfzjeuuzzw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lfzjeuuzzw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lfzjeuuzzw .gt_left { text-align: left; }
 #lfzjeuuzzw .gt_center { text-align: center; }
 #lfzjeuuzzw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lfzjeuuzzw .gt_font_normal { font-weight: normal; }
 #lfzjeuuzzw .gt_font_bold { font-weight: bold; }
 #lfzjeuuzzw .gt_font_italic { font-style: italic; }
 #lfzjeuuzzw .gt_super { font-size: 65%; }
 #lfzjeuuzzw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lfzjeuuzzw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lfzjeuuzzw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lfzjeuuzzw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lfzjeuuzzw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lfzjeuuzzw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ntoallcxdv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ntoallcxdv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ntoallcxdv p { margin: 0; padding: 0; }
 #ntoallcxdv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ntoallcxdv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ntoallcxdv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ntoallcxdv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ntoallcxdv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ntoallcxdv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ntoallcxdv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ntoallcxdv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ntoallcxdv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ntoallcxdv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ntoallcxdv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ntoallcxdv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ntoallcxdv .gt_spanner_row { border-bottom-style: hidden; }
 #ntoallcxdv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ntoallcxdv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ntoallcxdv .gt_from_md> :first-child { margin-top: 0; }
 #ntoallcxdv .gt_from_md> :last-child { margin-bottom: 0; }
 #ntoallcxdv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ntoallcxdv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ntoallcxdv .gt_indent_1 { text-indent: 5px; }
 #ntoallcxdv .gt_indent_2 { text-indent: calc(5px * 2); }
 #ntoallcxdv .gt_indent_3 { text-indent: calc(5px * 3); }
 #ntoallcxdv .gt_indent_4 { text-indent: calc(5px * 4); }
 #ntoallcxdv .gt_indent_5 { text-indent: calc(5px * 5); }
 #ntoallcxdv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ntoallcxdv .gt_row_group_first td { border-top-width: 2px; }
 #ntoallcxdv .gt_row_group_first th { border-top-width: 2px; }
 #ntoallcxdv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ntoallcxdv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ntoallcxdv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ntoallcxdv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ntoallcxdv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ntoallcxdv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ntoallcxdv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ntoallcxdv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ntoallcxdv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ntoallcxdv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ntoallcxdv .gt_left { text-align: left; }
 #ntoallcxdv .gt_center { text-align: center; }
 #ntoallcxdv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ntoallcxdv .gt_font_normal { font-weight: normal; }
 #ntoallcxdv .gt_font_bold { font-weight: bold; }
 #ntoallcxdv .gt_font_italic { font-style: italic; }
 #ntoallcxdv .gt_super { font-size: 65%; }
 #ntoallcxdv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ntoallcxdv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ntoallcxdv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ntoallcxdv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ntoallcxdv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ntoallcxdv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ynoifoksak table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ynoifoksak thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ynoifoksak p { margin: 0; padding: 0; }
 #ynoifoksak .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ynoifoksak .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ynoifoksak .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ynoifoksak .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ynoifoksak .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ynoifoksak .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ynoifoksak .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ynoifoksak .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ynoifoksak .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ynoifoksak .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ynoifoksak .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ynoifoksak .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ynoifoksak .gt_spanner_row { border-bottom-style: hidden; }
 #ynoifoksak .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ynoifoksak .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ynoifoksak .gt_from_md> :first-child { margin-top: 0; }
 #ynoifoksak .gt_from_md> :last-child { margin-bottom: 0; }
 #ynoifoksak .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ynoifoksak .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ynoifoksak .gt_indent_1 { text-indent: 5px; }
 #ynoifoksak .gt_indent_2 { text-indent: calc(5px * 2); }
 #ynoifoksak .gt_indent_3 { text-indent: calc(5px * 3); }
 #ynoifoksak .gt_indent_4 { text-indent: calc(5px * 4); }
 #ynoifoksak .gt_indent_5 { text-indent: calc(5px * 5); }
 #ynoifoksak .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ynoifoksak .gt_row_group_first td { border-top-width: 2px; }
 #ynoifoksak .gt_row_group_first th { border-top-width: 2px; }
 #ynoifoksak .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ynoifoksak .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ynoifoksak .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ynoifoksak .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ynoifoksak .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ynoifoksak .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ynoifoksak .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ynoifoksak .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ynoifoksak .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ynoifoksak .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ynoifoksak .gt_left { text-align: left; }
 #ynoifoksak .gt_center { text-align: center; }
 #ynoifoksak .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ynoifoksak .gt_font_normal { font-weight: normal; }
 #ynoifoksak .gt_font_bold { font-weight: bold; }
 #ynoifoksak .gt_font_italic { font-style: italic; }
 #ynoifoksak .gt_super { font-size: 65%; }
 #ynoifoksak .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ynoifoksak .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ynoifoksak .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ynoifoksak .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ynoifoksak .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ynoifoksak .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#eqknfvnzuc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eqknfvnzuc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eqknfvnzuc p { margin: 0; padding: 0; }
 #eqknfvnzuc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eqknfvnzuc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eqknfvnzuc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eqknfvnzuc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eqknfvnzuc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eqknfvnzuc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eqknfvnzuc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eqknfvnzuc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eqknfvnzuc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eqknfvnzuc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eqknfvnzuc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eqknfvnzuc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eqknfvnzuc .gt_spanner_row { border-bottom-style: hidden; }
 #eqknfvnzuc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eqknfvnzuc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eqknfvnzuc .gt_from_md> :first-child { margin-top: 0; }
 #eqknfvnzuc .gt_from_md> :last-child { margin-bottom: 0; }
 #eqknfvnzuc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eqknfvnzuc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eqknfvnzuc .gt_indent_1 { text-indent: 5px; }
 #eqknfvnzuc .gt_indent_2 { text-indent: calc(5px * 2); }
 #eqknfvnzuc .gt_indent_3 { text-indent: calc(5px * 3); }
 #eqknfvnzuc .gt_indent_4 { text-indent: calc(5px * 4); }
 #eqknfvnzuc .gt_indent_5 { text-indent: calc(5px * 5); }
 #eqknfvnzuc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eqknfvnzuc .gt_row_group_first td { border-top-width: 2px; }
 #eqknfvnzuc .gt_row_group_first th { border-top-width: 2px; }
 #eqknfvnzuc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eqknfvnzuc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eqknfvnzuc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eqknfvnzuc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #eqknfvnzuc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eqknfvnzuc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eqknfvnzuc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eqknfvnzuc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eqknfvnzuc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eqknfvnzuc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eqknfvnzuc .gt_left { text-align: left; }
 #eqknfvnzuc .gt_center { text-align: center; }
 #eqknfvnzuc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eqknfvnzuc .gt_font_normal { font-weight: normal; }
 #eqknfvnzuc .gt_font_bold { font-weight: bold; }
 #eqknfvnzuc .gt_font_italic { font-style: italic; }
 #eqknfvnzuc .gt_super { font-size: 65%; }
 #eqknfvnzuc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eqknfvnzuc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #eqknfvnzuc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eqknfvnzuc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eqknfvnzuc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eqknfvnzuc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#bgnpznpzkt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bgnpznpzkt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bgnpznpzkt p { margin: 0; padding: 0; }
 #bgnpznpzkt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bgnpznpzkt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bgnpznpzkt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bgnpznpzkt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bgnpznpzkt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bgnpznpzkt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bgnpznpzkt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bgnpznpzkt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bgnpznpzkt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bgnpznpzkt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bgnpznpzkt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bgnpznpzkt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bgnpznpzkt .gt_spanner_row { border-bottom-style: hidden; }
 #bgnpznpzkt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bgnpznpzkt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bgnpznpzkt .gt_from_md> :first-child { margin-top: 0; }
 #bgnpznpzkt .gt_from_md> :last-child { margin-bottom: 0; }
 #bgnpznpzkt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bgnpznpzkt .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bgnpznpzkt .gt_indent_1 { text-indent: 5px; }
 #bgnpznpzkt .gt_indent_2 { text-indent: calc(5px * 2); }
 #bgnpznpzkt .gt_indent_3 { text-indent: calc(5px * 3); }
 #bgnpznpzkt .gt_indent_4 { text-indent: calc(5px * 4); }
 #bgnpznpzkt .gt_indent_5 { text-indent: calc(5px * 5); }
 #bgnpznpzkt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bgnpznpzkt .gt_row_group_first td { border-top-width: 2px; }
 #bgnpznpzkt .gt_row_group_first th { border-top-width: 2px; }
 #bgnpznpzkt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bgnpznpzkt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bgnpznpzkt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bgnpznpzkt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bgnpznpzkt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bgnpznpzkt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bgnpznpzkt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bgnpznpzkt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bgnpznpzkt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bgnpznpzkt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bgnpznpzkt .gt_left { text-align: left; }
 #bgnpznpzkt .gt_center { text-align: center; }
 #bgnpznpzkt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bgnpznpzkt .gt_font_normal { font-weight: normal; }
 #bgnpznpzkt .gt_font_bold { font-weight: bold; }
 #bgnpznpzkt .gt_font_italic { font-style: italic; }
 #bgnpznpzkt .gt_super { font-size: 65%; }
 #bgnpznpzkt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bgnpznpzkt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bgnpznpzkt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bgnpznpzkt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bgnpznpzkt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bgnpznpzkt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#wabspopohy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wabspopohy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wabspopohy p { margin: 0; padding: 0; }
 #wabspopohy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wabspopohy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wabspopohy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wabspopohy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wabspopohy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wabspopohy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wabspopohy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wabspopohy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wabspopohy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wabspopohy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wabspopohy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wabspopohy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wabspopohy .gt_spanner_row { border-bottom-style: hidden; }
 #wabspopohy .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wabspopohy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wabspopohy .gt_from_md> :first-child { margin-top: 0; }
 #wabspopohy .gt_from_md> :last-child { margin-bottom: 0; }
 #wabspopohy .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wabspopohy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wabspopohy .gt_indent_1 { text-indent: 5px; }
 #wabspopohy .gt_indent_2 { text-indent: calc(5px * 2); }
 #wabspopohy .gt_indent_3 { text-indent: calc(5px * 3); }
 #wabspopohy .gt_indent_4 { text-indent: calc(5px * 4); }
 #wabspopohy .gt_indent_5 { text-indent: calc(5px * 5); }
 #wabspopohy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wabspopohy .gt_row_group_first td { border-top-width: 2px; }
 #wabspopohy .gt_row_group_first th { border-top-width: 2px; }
 #wabspopohy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wabspopohy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wabspopohy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wabspopohy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #wabspopohy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wabspopohy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wabspopohy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wabspopohy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wabspopohy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wabspopohy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wabspopohy .gt_left { text-align: left; }
 #wabspopohy .gt_center { text-align: center; }
 #wabspopohy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wabspopohy .gt_font_normal { font-weight: normal; }
 #wabspopohy .gt_font_bold { font-weight: bold; }
 #wabspopohy .gt_font_italic { font-style: italic; }
 #wabspopohy .gt_super { font-size: 65%; }
 #wabspopohy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wabspopohy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #wabspopohy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wabspopohy .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wabspopohy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wabspopohy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#lalghewtlw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lalghewtlw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lalghewtlw p { margin: 0; padding: 0; }
 #lalghewtlw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lalghewtlw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lalghewtlw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lalghewtlw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lalghewtlw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lalghewtlw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lalghewtlw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lalghewtlw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lalghewtlw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lalghewtlw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lalghewtlw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lalghewtlw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lalghewtlw .gt_spanner_row { border-bottom-style: hidden; }
 #lalghewtlw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lalghewtlw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lalghewtlw .gt_from_md> :first-child { margin-top: 0; }
 #lalghewtlw .gt_from_md> :last-child { margin-bottom: 0; }
 #lalghewtlw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lalghewtlw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lalghewtlw .gt_indent_1 { text-indent: 5px; }
 #lalghewtlw .gt_indent_2 { text-indent: calc(5px * 2); }
 #lalghewtlw .gt_indent_3 { text-indent: calc(5px * 3); }
 #lalghewtlw .gt_indent_4 { text-indent: calc(5px * 4); }
 #lalghewtlw .gt_indent_5 { text-indent: calc(5px * 5); }
 #lalghewtlw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lalghewtlw .gt_row_group_first td { border-top-width: 2px; }
 #lalghewtlw .gt_row_group_first th { border-top-width: 2px; }
 #lalghewtlw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lalghewtlw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lalghewtlw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lalghewtlw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lalghewtlw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lalghewtlw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lalghewtlw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lalghewtlw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lalghewtlw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lalghewtlw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lalghewtlw .gt_left { text-align: left; }
 #lalghewtlw .gt_center { text-align: center; }
 #lalghewtlw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lalghewtlw .gt_font_normal { font-weight: normal; }
 #lalghewtlw .gt_font_bold { font-weight: bold; }
 #lalghewtlw .gt_font_italic { font-style: italic; }
 #lalghewtlw .gt_super { font-size: 65%; }
 #lalghewtlw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lalghewtlw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lalghewtlw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lalghewtlw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lalghewtlw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lalghewtlw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#trklvqlgwg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#trklvqlgwg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#trklvqlgwg p { margin: 0; padding: 0; }
 #trklvqlgwg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #trklvqlgwg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #trklvqlgwg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #trklvqlgwg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #trklvqlgwg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #trklvqlgwg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #trklvqlgwg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #trklvqlgwg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #trklvqlgwg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #trklvqlgwg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #trklvqlgwg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #trklvqlgwg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #trklvqlgwg .gt_spanner_row { border-bottom-style: hidden; }
 #trklvqlgwg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #trklvqlgwg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #trklvqlgwg .gt_from_md> :first-child { margin-top: 0; }
 #trklvqlgwg .gt_from_md> :last-child { margin-bottom: 0; }
 #trklvqlgwg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #trklvqlgwg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #trklvqlgwg .gt_indent_1 { text-indent: 5px; }
 #trklvqlgwg .gt_indent_2 { text-indent: calc(5px * 2); }
 #trklvqlgwg .gt_indent_3 { text-indent: calc(5px * 3); }
 #trklvqlgwg .gt_indent_4 { text-indent: calc(5px * 4); }
 #trklvqlgwg .gt_indent_5 { text-indent: calc(5px * 5); }
 #trklvqlgwg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #trklvqlgwg .gt_row_group_first td { border-top-width: 2px; }
 #trklvqlgwg .gt_row_group_first th { border-top-width: 2px; }
 #trklvqlgwg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #trklvqlgwg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #trklvqlgwg .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #trklvqlgwg .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #trklvqlgwg .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #trklvqlgwg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #trklvqlgwg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #trklvqlgwg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #trklvqlgwg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #trklvqlgwg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #trklvqlgwg .gt_left { text-align: left; }
 #trklvqlgwg .gt_center { text-align: center; }
 #trklvqlgwg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #trklvqlgwg .gt_font_normal { font-weight: normal; }
 #trklvqlgwg .gt_font_bold { font-weight: bold; }
 #trklvqlgwg .gt_font_italic { font-style: italic; }
 #trklvqlgwg .gt_super { font-size: 65%; }
 #trklvqlgwg .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #trklvqlgwg .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #trklvqlgwg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #trklvqlgwg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #trklvqlgwg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #trklvqlgwg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
