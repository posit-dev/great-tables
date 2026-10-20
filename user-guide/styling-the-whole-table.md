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
#urqbjwycfc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#urqbjwycfc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#urqbjwycfc p { margin: 0; padding: 0; }
 #urqbjwycfc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #urqbjwycfc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #urqbjwycfc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #urqbjwycfc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #urqbjwycfc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #urqbjwycfc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #urqbjwycfc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #urqbjwycfc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #urqbjwycfc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #urqbjwycfc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #urqbjwycfc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #urqbjwycfc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #urqbjwycfc .gt_spanner_row { border-bottom-style: hidden; }
 #urqbjwycfc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #urqbjwycfc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #urqbjwycfc .gt_from_md> :first-child { margin-top: 0; }
 #urqbjwycfc .gt_from_md> :last-child { margin-bottom: 0; }
 #urqbjwycfc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #urqbjwycfc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #urqbjwycfc .gt_indent_1 { text-indent: 5px; }
 #urqbjwycfc .gt_indent_2 { text-indent: calc(5px * 2); }
 #urqbjwycfc .gt_indent_3 { text-indent: calc(5px * 3); }
 #urqbjwycfc .gt_indent_4 { text-indent: calc(5px * 4); }
 #urqbjwycfc .gt_indent_5 { text-indent: calc(5px * 5); }
 #urqbjwycfc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #urqbjwycfc .gt_row_group_first td { border-top-width: 2px; }
 #urqbjwycfc .gt_row_group_first th { border-top-width: 2px; }
 #urqbjwycfc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #urqbjwycfc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #urqbjwycfc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #urqbjwycfc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #urqbjwycfc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #urqbjwycfc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #urqbjwycfc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #urqbjwycfc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #urqbjwycfc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #urqbjwycfc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #urqbjwycfc .gt_left { text-align: left; }
 #urqbjwycfc .gt_center { text-align: center; }
 #urqbjwycfc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #urqbjwycfc .gt_font_normal { font-weight: normal; }
 #urqbjwycfc .gt_font_bold { font-weight: bold; }
 #urqbjwycfc .gt_font_italic { font-style: italic; }
 #urqbjwycfc .gt_super { font-size: 65%; }
 #urqbjwycfc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #urqbjwycfc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #urqbjwycfc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #urqbjwycfc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #urqbjwycfc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #urqbjwycfc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" id="title" class="gt_heading gt_title gt_font_normal" style="background-color: #fb9a99; background-color: #fdbf6f">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="background-color: #fb9a99; background-color: #e31a1c">subtitle</th>
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
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup" style="background-color: #cab2d6">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" style="background-color: #6a3d9a" scope="row">row_1</td>
<td class="gt_row gt_right" style="background-color: #a6cee3" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" style="background-color: #a6cee3" headers="grp_a stub-1 spanner char">apricot</td>
<td class="gt_row gt_left" style="background-color: #a6cee3" headers="grp_a stub-1 spanner fctr">one</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" style="border-top: 3px solid #000000; border-bottom: 3px solid #000000; border-left: 3px solid #000000; border-right: 3px solid #000000; background-color: #6a3d9a" scope="row">row_2</td>
<td class="gt_row gt_right" style="background-color: #a6cee3" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" style="background-color: #a6cee3" headers="grp_a stub-2 spanner char">banana</td>
<td class="gt_row gt_left" style="background-color: #a6cee3" headers="grp_a stub-2 spanner fctr">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup" style="background-color: #cab2d6">grp_b</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" style="background-color: #6a3d9a" scope="row">row_5</td>
<td class="gt_row gt_right" style="background-color: #a6cee3" headers="grp_b stub-3 num">5550.0</td>
<td class="gt_row gt_left" style="background-color: #a6cee3" headers="grp_b stub-3 spanner char">None</td>
<td class="gt_row gt_left" style="background-color: #a6cee3" headers="grp_b stub-3 spanner fctr">five</td>
</tr>
<tr>
<td id="grand-summary-Total" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" style="background-color: #808080" scope="row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" style="background-color: #b15928" headers="grand-summary-Total num">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" style="background-color: #b15928" headers="grand-summary-Total spanner char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" style="background-color: #b15928" headers="grand-summary-Total spanner fctr">---</td>
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
#qiwbxiwqtb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qiwbxiwqtb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qiwbxiwqtb p { margin: 0; padding: 0; }
 #qiwbxiwqtb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qiwbxiwqtb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qiwbxiwqtb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qiwbxiwqtb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qiwbxiwqtb .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qiwbxiwqtb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qiwbxiwqtb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qiwbxiwqtb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qiwbxiwqtb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qiwbxiwqtb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qiwbxiwqtb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qiwbxiwqtb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qiwbxiwqtb .gt_spanner_row { border-bottom-style: hidden; }
 #qiwbxiwqtb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qiwbxiwqtb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qiwbxiwqtb .gt_from_md> :first-child { margin-top: 0; }
 #qiwbxiwqtb .gt_from_md> :last-child { margin-bottom: 0; }
 #qiwbxiwqtb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qiwbxiwqtb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qiwbxiwqtb .gt_indent_1 { text-indent: 5px; }
 #qiwbxiwqtb .gt_indent_2 { text-indent: calc(5px * 2); }
 #qiwbxiwqtb .gt_indent_3 { text-indent: calc(5px * 3); }
 #qiwbxiwqtb .gt_indent_4 { text-indent: calc(5px * 4); }
 #qiwbxiwqtb .gt_indent_5 { text-indent: calc(5px * 5); }
 #qiwbxiwqtb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qiwbxiwqtb .gt_row_group_first td { border-top-width: 2px; }
 #qiwbxiwqtb .gt_row_group_first th { border-top-width: 2px; }
 #qiwbxiwqtb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qiwbxiwqtb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qiwbxiwqtb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qiwbxiwqtb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qiwbxiwqtb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qiwbxiwqtb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qiwbxiwqtb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qiwbxiwqtb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qiwbxiwqtb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qiwbxiwqtb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qiwbxiwqtb .gt_left { text-align: left; }
 #qiwbxiwqtb .gt_center { text-align: center; }
 #qiwbxiwqtb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qiwbxiwqtb .gt_font_normal { font-weight: normal; }
 #qiwbxiwqtb .gt_font_bold { font-weight: bold; }
 #qiwbxiwqtb .gt_font_italic { font-style: italic; }
 #qiwbxiwqtb .gt_super { font-size: 65%; }
 #qiwbxiwqtb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qiwbxiwqtb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qiwbxiwqtb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qiwbxiwqtb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qiwbxiwqtb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qiwbxiwqtb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" id="title" class="gt_heading gt_title gt_font_normal">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">subtitle</th>
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
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" style="background-color: yellow" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" style="background-color: yellow" headers="grp_a stub-1 spanner char">apricot</td>
<td class="gt_row gt_left" style="background-color: yellow" headers="grp_a stub-1 spanner fctr">one</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" style="background-color: yellow" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" style="background-color: yellow" headers="grp_a stub-2 spanner char">banana</td>
<td class="gt_row gt_left" style="background-color: yellow" headers="grp_a stub-2 spanner fctr">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" style="background-color: yellow" headers="grp_b stub-3 num">5550.0</td>
<td class="gt_row gt_left" style="background-color: yellow" headers="grp_b stub-3 spanner char">None</td>
<td class="gt_row gt_left" style="background-color: yellow" headers="grp_b stub-3 spanner fctr">five</td>
</tr>
<tr>
<td id="grand-summary-Total" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-Total num">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-Total spanner char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-Total spanner fctr">---</td>
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
#dldfxrlwiu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dldfxrlwiu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dldfxrlwiu p { margin: 0; padding: 0; }
 #dldfxrlwiu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dldfxrlwiu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dldfxrlwiu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dldfxrlwiu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dldfxrlwiu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dldfxrlwiu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dldfxrlwiu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dldfxrlwiu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dldfxrlwiu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dldfxrlwiu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dldfxrlwiu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dldfxrlwiu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dldfxrlwiu .gt_spanner_row { border-bottom-style: hidden; }
 #dldfxrlwiu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dldfxrlwiu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dldfxrlwiu .gt_from_md> :first-child { margin-top: 0; }
 #dldfxrlwiu .gt_from_md> :last-child { margin-bottom: 0; }
 #dldfxrlwiu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dldfxrlwiu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #dldfxrlwiu .gt_indent_1 { text-indent: 5px; }
 #dldfxrlwiu .gt_indent_2 { text-indent: calc(5px * 2); }
 #dldfxrlwiu .gt_indent_3 { text-indent: calc(5px * 3); }
 #dldfxrlwiu .gt_indent_4 { text-indent: calc(5px * 4); }
 #dldfxrlwiu .gt_indent_5 { text-indent: calc(5px * 5); }
 #dldfxrlwiu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dldfxrlwiu .gt_row_group_first td { border-top-width: 2px; }
 #dldfxrlwiu .gt_row_group_first th { border-top-width: 2px; }
 #dldfxrlwiu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dldfxrlwiu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dldfxrlwiu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dldfxrlwiu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dldfxrlwiu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dldfxrlwiu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dldfxrlwiu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dldfxrlwiu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dldfxrlwiu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dldfxrlwiu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dldfxrlwiu .gt_left { text-align: left; }
 #dldfxrlwiu .gt_center { text-align: center; }
 #dldfxrlwiu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dldfxrlwiu .gt_font_normal { font-weight: normal; }
 #dldfxrlwiu .gt_font_bold { font-weight: bold; }
 #dldfxrlwiu .gt_font_italic { font-style: italic; }
 #dldfxrlwiu .gt_super { font-size: 65%; }
 #dldfxrlwiu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dldfxrlwiu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dldfxrlwiu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dldfxrlwiu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dldfxrlwiu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dldfxrlwiu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" id="title" class="gt_heading gt_title gt_font_normal">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">subtitle</th>
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
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 spanner char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 spanner fctr">one</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 spanner char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 spanner fctr">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-3 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-3 spanner char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-3 spanner fctr">five</td>
</tr>
<tr>
<td id="grand-summary-Total" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-Total num">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-Total spanner char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-Total spanner fctr">---</td>
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
#nshgqqgmvm table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nshgqqgmvm thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nshgqqgmvm p { margin: 0; padding: 0; }
 #nshgqqgmvm .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nshgqqgmvm .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nshgqqgmvm .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nshgqqgmvm .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nshgqqgmvm .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nshgqqgmvm .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nshgqqgmvm .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nshgqqgmvm .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nshgqqgmvm .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nshgqqgmvm .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nshgqqgmvm .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nshgqqgmvm .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nshgqqgmvm .gt_spanner_row { border-bottom-style: hidden; }
 #nshgqqgmvm .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nshgqqgmvm .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nshgqqgmvm .gt_from_md> :first-child { margin-top: 0; }
 #nshgqqgmvm .gt_from_md> :last-child { margin-bottom: 0; }
 #nshgqqgmvm .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nshgqqgmvm .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nshgqqgmvm .gt_indent_1 { text-indent: 5px; }
 #nshgqqgmvm .gt_indent_2 { text-indent: calc(5px * 2); }
 #nshgqqgmvm .gt_indent_3 { text-indent: calc(5px * 3); }
 #nshgqqgmvm .gt_indent_4 { text-indent: calc(5px * 4); }
 #nshgqqgmvm .gt_indent_5 { text-indent: calc(5px * 5); }
 #nshgqqgmvm .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nshgqqgmvm .gt_row_group_first td { border-top-width: 2px; }
 #nshgqqgmvm .gt_row_group_first th { border-top-width: 2px; }
 #nshgqqgmvm .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nshgqqgmvm .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nshgqqgmvm .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nshgqqgmvm .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nshgqqgmvm .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nshgqqgmvm .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nshgqqgmvm .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nshgqqgmvm .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nshgqqgmvm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nshgqqgmvm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nshgqqgmvm .gt_left { text-align: left; }
 #nshgqqgmvm .gt_center { text-align: center; }
 #nshgqqgmvm .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nshgqqgmvm .gt_font_normal { font-weight: normal; }
 #nshgqqgmvm .gt_font_bold { font-weight: bold; }
 #nshgqqgmvm .gt_font_italic { font-style: italic; }
 #nshgqqgmvm .gt_super { font-size: 65%; }
 #nshgqqgmvm .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nshgqqgmvm .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nshgqqgmvm .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nshgqqgmvm .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nshgqqgmvm .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nshgqqgmvm .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" id="title" class="gt_heading gt_title gt_font_normal" style="background-color: yellow; background-color: blue">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="background-color: yellow; background-color: red">subtitle</th>
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
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 spanner char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 spanner fctr">one</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 spanner char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 spanner fctr">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-3 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-3 spanner char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-3 spanner fctr">five</td>
</tr>
<tr>
<td id="grand-summary-Total" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-Total num">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-Total spanner char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-Total spanner fctr">---</td>
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
#qxovzwpfiq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qxovzwpfiq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qxovzwpfiq p { margin: 0; padding: 0; }
 #qxovzwpfiq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qxovzwpfiq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qxovzwpfiq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qxovzwpfiq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qxovzwpfiq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qxovzwpfiq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qxovzwpfiq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qxovzwpfiq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qxovzwpfiq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qxovzwpfiq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qxovzwpfiq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qxovzwpfiq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qxovzwpfiq .gt_spanner_row { border-bottom-style: hidden; }
 #qxovzwpfiq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qxovzwpfiq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qxovzwpfiq .gt_from_md> :first-child { margin-top: 0; }
 #qxovzwpfiq .gt_from_md> :last-child { margin-bottom: 0; }
 #qxovzwpfiq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qxovzwpfiq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qxovzwpfiq .gt_indent_1 { text-indent: 5px; }
 #qxovzwpfiq .gt_indent_2 { text-indent: calc(5px * 2); }
 #qxovzwpfiq .gt_indent_3 { text-indent: calc(5px * 3); }
 #qxovzwpfiq .gt_indent_4 { text-indent: calc(5px * 4); }
 #qxovzwpfiq .gt_indent_5 { text-indent: calc(5px * 5); }
 #qxovzwpfiq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qxovzwpfiq .gt_row_group_first td { border-top-width: 2px; }
 #qxovzwpfiq .gt_row_group_first th { border-top-width: 2px; }
 #qxovzwpfiq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qxovzwpfiq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qxovzwpfiq .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qxovzwpfiq .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qxovzwpfiq .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qxovzwpfiq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qxovzwpfiq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qxovzwpfiq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qxovzwpfiq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qxovzwpfiq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qxovzwpfiq .gt_left { text-align: left; }
 #qxovzwpfiq .gt_center { text-align: center; }
 #qxovzwpfiq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qxovzwpfiq .gt_font_normal { font-weight: normal; }
 #qxovzwpfiq .gt_font_bold { font-weight: bold; }
 #qxovzwpfiq .gt_font_italic { font-style: italic; }
 #qxovzwpfiq .gt_super { font-size: 65%; }
 #qxovzwpfiq .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qxovzwpfiq .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qxovzwpfiq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qxovzwpfiq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qxovzwpfiq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qxovzwpfiq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" id="title" class="gt_heading gt_title gt_font_normal">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">subtitle</th>
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
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 spanner char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 spanner fctr">one</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 spanner char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 spanner fctr">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-3 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-3 spanner char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-3 spanner fctr">five</td>
</tr>
<tr>
<td id="grand-summary-Total" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-Total num">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-Total spanner char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-Total spanner fctr">---</td>
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
#ndwkoskxyh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ndwkoskxyh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ndwkoskxyh p { margin: 0; padding: 0; }
 #ndwkoskxyh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ndwkoskxyh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ndwkoskxyh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ndwkoskxyh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ndwkoskxyh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ndwkoskxyh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ndwkoskxyh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ndwkoskxyh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ndwkoskxyh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ndwkoskxyh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ndwkoskxyh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ndwkoskxyh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ndwkoskxyh .gt_spanner_row { border-bottom-style: hidden; }
 #ndwkoskxyh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ndwkoskxyh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ndwkoskxyh .gt_from_md> :first-child { margin-top: 0; }
 #ndwkoskxyh .gt_from_md> :last-child { margin-bottom: 0; }
 #ndwkoskxyh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ndwkoskxyh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ndwkoskxyh .gt_indent_1 { text-indent: 5px; }
 #ndwkoskxyh .gt_indent_2 { text-indent: calc(5px * 2); }
 #ndwkoskxyh .gt_indent_3 { text-indent: calc(5px * 3); }
 #ndwkoskxyh .gt_indent_4 { text-indent: calc(5px * 4); }
 #ndwkoskxyh .gt_indent_5 { text-indent: calc(5px * 5); }
 #ndwkoskxyh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ndwkoskxyh .gt_row_group_first td { border-top-width: 2px; }
 #ndwkoskxyh .gt_row_group_first th { border-top-width: 2px; }
 #ndwkoskxyh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ndwkoskxyh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ndwkoskxyh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ndwkoskxyh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ndwkoskxyh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ndwkoskxyh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ndwkoskxyh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ndwkoskxyh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ndwkoskxyh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ndwkoskxyh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ndwkoskxyh .gt_left { text-align: left; }
 #ndwkoskxyh .gt_center { text-align: center; }
 #ndwkoskxyh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ndwkoskxyh .gt_font_normal { font-weight: normal; }
 #ndwkoskxyh .gt_font_bold { font-weight: bold; }
 #ndwkoskxyh .gt_font_italic { font-style: italic; }
 #ndwkoskxyh .gt_super { font-size: 65%; }
 #ndwkoskxyh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ndwkoskxyh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ndwkoskxyh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ndwkoskxyh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ndwkoskxyh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ndwkoskxyh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" id="title" class="gt_heading gt_title gt_font_normal">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">subtitle</th>
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
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup" style="background-color: blue">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" style="background-color: yellow" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 spanner char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 spanner fctr">one</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" style="background-color: yellow; border-top: 3px dashed red; border-bottom: 3px dashed red; border-left: 3px dashed red; border-right: 3px dashed red" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 spanner char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 spanner fctr">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup" style="background-color: blue">grp_b</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" style="background-color: yellow" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-3 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-3 spanner char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-3 spanner fctr">five</td>
</tr>
<tr>
<td id="grand-summary-Total" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-Total num">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-Total spanner char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-Total spanner fctr">---</td>
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
#ojmkyvkbvh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ojmkyvkbvh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ojmkyvkbvh p { margin: 0; padding: 0; }
 #ojmkyvkbvh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ojmkyvkbvh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ojmkyvkbvh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ojmkyvkbvh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ojmkyvkbvh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ojmkyvkbvh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ojmkyvkbvh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ojmkyvkbvh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ojmkyvkbvh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ojmkyvkbvh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ojmkyvkbvh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ojmkyvkbvh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ojmkyvkbvh .gt_spanner_row { border-bottom-style: hidden; }
 #ojmkyvkbvh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ojmkyvkbvh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ojmkyvkbvh .gt_from_md> :first-child { margin-top: 0; }
 #ojmkyvkbvh .gt_from_md> :last-child { margin-bottom: 0; }
 #ojmkyvkbvh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ojmkyvkbvh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ojmkyvkbvh .gt_indent_1 { text-indent: 5px; }
 #ojmkyvkbvh .gt_indent_2 { text-indent: calc(5px * 2); }
 #ojmkyvkbvh .gt_indent_3 { text-indent: calc(5px * 3); }
 #ojmkyvkbvh .gt_indent_4 { text-indent: calc(5px * 4); }
 #ojmkyvkbvh .gt_indent_5 { text-indent: calc(5px * 5); }
 #ojmkyvkbvh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ojmkyvkbvh .gt_row_group_first td { border-top-width: 2px; }
 #ojmkyvkbvh .gt_row_group_first th { border-top-width: 2px; }
 #ojmkyvkbvh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ojmkyvkbvh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ojmkyvkbvh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ojmkyvkbvh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ojmkyvkbvh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ojmkyvkbvh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ojmkyvkbvh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ojmkyvkbvh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ojmkyvkbvh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ojmkyvkbvh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ojmkyvkbvh .gt_left { text-align: left; }
 #ojmkyvkbvh .gt_center { text-align: center; }
 #ojmkyvkbvh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ojmkyvkbvh .gt_font_normal { font-weight: normal; }
 #ojmkyvkbvh .gt_font_bold { font-weight: bold; }
 #ojmkyvkbvh .gt_font_italic { font-style: italic; }
 #ojmkyvkbvh .gt_super { font-size: 65%; }
 #ojmkyvkbvh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ojmkyvkbvh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ojmkyvkbvh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ojmkyvkbvh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ojmkyvkbvh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ojmkyvkbvh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" id="title" class="gt_heading gt_title gt_font_normal">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">subtitle</th>
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
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 spanner char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 spanner fctr">one</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 spanner char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 spanner fctr">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-3 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-3 spanner char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-3 spanner fctr">five</td>
</tr>
<tr>
<td id="grand-summary-Total" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-Total num">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-Total spanner char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-Total spanner fctr">---</td>
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
#tilwvlmibf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tilwvlmibf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tilwvlmibf p { margin: 0; padding: 0; }
 #tilwvlmibf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tilwvlmibf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tilwvlmibf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tilwvlmibf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tilwvlmibf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tilwvlmibf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tilwvlmibf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tilwvlmibf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #tilwvlmibf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tilwvlmibf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tilwvlmibf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tilwvlmibf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tilwvlmibf .gt_spanner_row { border-bottom-style: hidden; }
 #tilwvlmibf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tilwvlmibf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tilwvlmibf .gt_from_md> :first-child { margin-top: 0; }
 #tilwvlmibf .gt_from_md> :last-child { margin-bottom: 0; }
 #tilwvlmibf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tilwvlmibf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #tilwvlmibf .gt_indent_1 { text-indent: 5px; }
 #tilwvlmibf .gt_indent_2 { text-indent: calc(5px * 2); }
 #tilwvlmibf .gt_indent_3 { text-indent: calc(5px * 3); }
 #tilwvlmibf .gt_indent_4 { text-indent: calc(5px * 4); }
 #tilwvlmibf .gt_indent_5 { text-indent: calc(5px * 5); }
 #tilwvlmibf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #tilwvlmibf .gt_row_group_first td { border-top-width: 2px; }
 #tilwvlmibf .gt_row_group_first th { border-top-width: 2px; }
 #tilwvlmibf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tilwvlmibf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tilwvlmibf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tilwvlmibf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tilwvlmibf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tilwvlmibf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tilwvlmibf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tilwvlmibf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tilwvlmibf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tilwvlmibf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tilwvlmibf .gt_left { text-align: left; }
 #tilwvlmibf .gt_center { text-align: center; }
 #tilwvlmibf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tilwvlmibf .gt_font_normal { font-weight: normal; }
 #tilwvlmibf .gt_font_bold { font-weight: bold; }
 #tilwvlmibf .gt_font_italic { font-style: italic; }
 #tilwvlmibf .gt_super { font-size: 65%; }
 #tilwvlmibf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tilwvlmibf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tilwvlmibf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tilwvlmibf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #tilwvlmibf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tilwvlmibf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" id="title" class="gt_heading gt_title gt_font_normal">title</th>
</tr>
<tr class="gt_heading">
<th colspan="4" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">subtitle</th>
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
<th colspan="4" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 spanner char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 spanner fctr">one</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 spanner char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 spanner fctr">two</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-3 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-3 spanner char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-3 spanner fctr">five</td>
</tr>
<tr>
<td id="grand-summary-Total" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" style="background-color: yellow" scope="row">Total</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" style="background-color: lightblue" headers="grand-summary-Total num">5552.3331</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" style="background-color: lightblue" headers="grand-summary-Total spanner char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" style="background-color: lightblue" headers="grand-summary-Total spanner fctr">---</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="4" class="gt_sourcenote">yo</td>
</tr>
</tfoot>

</table>


With [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) and the full set of `loc` specifiers, you can style every part of a **Great Tables** output. This gives you the ability to create cohesive visual themes, draw attention to specific structural elements, and ensure your table communicates effectively at every level.
