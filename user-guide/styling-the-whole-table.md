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
#ooflckcxqo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ooflckcxqo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ooflckcxqo p { margin: 0; padding: 0; }
 #ooflckcxqo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ooflckcxqo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ooflckcxqo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ooflckcxqo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ooflckcxqo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ooflckcxqo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ooflckcxqo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ooflckcxqo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ooflckcxqo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ooflckcxqo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ooflckcxqo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ooflckcxqo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ooflckcxqo .gt_spanner_row { border-bottom-style: hidden; }
 #ooflckcxqo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ooflckcxqo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ooflckcxqo .gt_from_md> :first-child { margin-top: 0; }
 #ooflckcxqo .gt_from_md> :last-child { margin-bottom: 0; }
 #ooflckcxqo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ooflckcxqo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ooflckcxqo .gt_indent_1 { text-indent: 5px; }
 #ooflckcxqo .gt_indent_2 { text-indent: calc(5px * 2); }
 #ooflckcxqo .gt_indent_3 { text-indent: calc(5px * 3); }
 #ooflckcxqo .gt_indent_4 { text-indent: calc(5px * 4); }
 #ooflckcxqo .gt_indent_5 { text-indent: calc(5px * 5); }
 #ooflckcxqo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ooflckcxqo .gt_row_group_first td { border-top-width: 2px; }
 #ooflckcxqo .gt_row_group_first th { border-top-width: 2px; }
 #ooflckcxqo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ooflckcxqo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ooflckcxqo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ooflckcxqo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ooflckcxqo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ooflckcxqo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ooflckcxqo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ooflckcxqo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ooflckcxqo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ooflckcxqo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ooflckcxqo .gt_left { text-align: left; }
 #ooflckcxqo .gt_center { text-align: center; }
 #ooflckcxqo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ooflckcxqo .gt_font_normal { font-weight: normal; }
 #ooflckcxqo .gt_font_bold { font-weight: bold; }
 #ooflckcxqo .gt_font_italic { font-style: italic; }
 #ooflckcxqo .gt_super { font-size: 65%; }
 #ooflckcxqo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ooflckcxqo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ooflckcxqo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ooflckcxqo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ooflckcxqo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ooflckcxqo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#osgymeoacr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#osgymeoacr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#osgymeoacr p { margin: 0; padding: 0; }
 #osgymeoacr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #osgymeoacr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #osgymeoacr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #osgymeoacr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #osgymeoacr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #osgymeoacr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #osgymeoacr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #osgymeoacr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #osgymeoacr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #osgymeoacr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #osgymeoacr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #osgymeoacr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #osgymeoacr .gt_spanner_row { border-bottom-style: hidden; }
 #osgymeoacr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #osgymeoacr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #osgymeoacr .gt_from_md> :first-child { margin-top: 0; }
 #osgymeoacr .gt_from_md> :last-child { margin-bottom: 0; }
 #osgymeoacr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #osgymeoacr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #osgymeoacr .gt_indent_1 { text-indent: 5px; }
 #osgymeoacr .gt_indent_2 { text-indent: calc(5px * 2); }
 #osgymeoacr .gt_indent_3 { text-indent: calc(5px * 3); }
 #osgymeoacr .gt_indent_4 { text-indent: calc(5px * 4); }
 #osgymeoacr .gt_indent_5 { text-indent: calc(5px * 5); }
 #osgymeoacr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #osgymeoacr .gt_row_group_first td { border-top-width: 2px; }
 #osgymeoacr .gt_row_group_first th { border-top-width: 2px; }
 #osgymeoacr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #osgymeoacr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #osgymeoacr .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #osgymeoacr .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #osgymeoacr .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #osgymeoacr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #osgymeoacr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #osgymeoacr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #osgymeoacr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #osgymeoacr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #osgymeoacr .gt_left { text-align: left; }
 #osgymeoacr .gt_center { text-align: center; }
 #osgymeoacr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #osgymeoacr .gt_font_normal { font-weight: normal; }
 #osgymeoacr .gt_font_bold { font-weight: bold; }
 #osgymeoacr .gt_font_italic { font-style: italic; }
 #osgymeoacr .gt_super { font-size: 65%; }
 #osgymeoacr .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #osgymeoacr .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #osgymeoacr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #osgymeoacr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #osgymeoacr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #osgymeoacr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#gzidfxjlli table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gzidfxjlli thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gzidfxjlli p { margin: 0; padding: 0; }
 #gzidfxjlli .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gzidfxjlli .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gzidfxjlli .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gzidfxjlli .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gzidfxjlli .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gzidfxjlli .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gzidfxjlli .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gzidfxjlli .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gzidfxjlli .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gzidfxjlli .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gzidfxjlli .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gzidfxjlli .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gzidfxjlli .gt_spanner_row { border-bottom-style: hidden; }
 #gzidfxjlli .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gzidfxjlli .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gzidfxjlli .gt_from_md> :first-child { margin-top: 0; }
 #gzidfxjlli .gt_from_md> :last-child { margin-bottom: 0; }
 #gzidfxjlli .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gzidfxjlli .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gzidfxjlli .gt_indent_1 { text-indent: 5px; }
 #gzidfxjlli .gt_indent_2 { text-indent: calc(5px * 2); }
 #gzidfxjlli .gt_indent_3 { text-indent: calc(5px * 3); }
 #gzidfxjlli .gt_indent_4 { text-indent: calc(5px * 4); }
 #gzidfxjlli .gt_indent_5 { text-indent: calc(5px * 5); }
 #gzidfxjlli .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gzidfxjlli .gt_row_group_first td { border-top-width: 2px; }
 #gzidfxjlli .gt_row_group_first th { border-top-width: 2px; }
 #gzidfxjlli .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gzidfxjlli .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gzidfxjlli .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gzidfxjlli .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gzidfxjlli .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gzidfxjlli .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gzidfxjlli .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gzidfxjlli .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gzidfxjlli .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gzidfxjlli .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gzidfxjlli .gt_left { text-align: left; }
 #gzidfxjlli .gt_center { text-align: center; }
 #gzidfxjlli .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gzidfxjlli .gt_font_normal { font-weight: normal; }
 #gzidfxjlli .gt_font_bold { font-weight: bold; }
 #gzidfxjlli .gt_font_italic { font-style: italic; }
 #gzidfxjlli .gt_super { font-size: 65%; }
 #gzidfxjlli .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gzidfxjlli .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gzidfxjlli .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gzidfxjlli .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gzidfxjlli .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gzidfxjlli .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ogrwzgzlbd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ogrwzgzlbd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ogrwzgzlbd p { margin: 0; padding: 0; }
 #ogrwzgzlbd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ogrwzgzlbd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ogrwzgzlbd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ogrwzgzlbd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ogrwzgzlbd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ogrwzgzlbd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ogrwzgzlbd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ogrwzgzlbd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ogrwzgzlbd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ogrwzgzlbd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ogrwzgzlbd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ogrwzgzlbd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ogrwzgzlbd .gt_spanner_row { border-bottom-style: hidden; }
 #ogrwzgzlbd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ogrwzgzlbd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ogrwzgzlbd .gt_from_md> :first-child { margin-top: 0; }
 #ogrwzgzlbd .gt_from_md> :last-child { margin-bottom: 0; }
 #ogrwzgzlbd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ogrwzgzlbd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ogrwzgzlbd .gt_indent_1 { text-indent: 5px; }
 #ogrwzgzlbd .gt_indent_2 { text-indent: calc(5px * 2); }
 #ogrwzgzlbd .gt_indent_3 { text-indent: calc(5px * 3); }
 #ogrwzgzlbd .gt_indent_4 { text-indent: calc(5px * 4); }
 #ogrwzgzlbd .gt_indent_5 { text-indent: calc(5px * 5); }
 #ogrwzgzlbd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ogrwzgzlbd .gt_row_group_first td { border-top-width: 2px; }
 #ogrwzgzlbd .gt_row_group_first th { border-top-width: 2px; }
 #ogrwzgzlbd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ogrwzgzlbd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ogrwzgzlbd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ogrwzgzlbd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ogrwzgzlbd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ogrwzgzlbd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ogrwzgzlbd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ogrwzgzlbd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ogrwzgzlbd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ogrwzgzlbd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ogrwzgzlbd .gt_left { text-align: left; }
 #ogrwzgzlbd .gt_center { text-align: center; }
 #ogrwzgzlbd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ogrwzgzlbd .gt_font_normal { font-weight: normal; }
 #ogrwzgzlbd .gt_font_bold { font-weight: bold; }
 #ogrwzgzlbd .gt_font_italic { font-style: italic; }
 #ogrwzgzlbd .gt_super { font-size: 65%; }
 #ogrwzgzlbd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ogrwzgzlbd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ogrwzgzlbd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ogrwzgzlbd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ogrwzgzlbd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ogrwzgzlbd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ovlpbmnxpo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ovlpbmnxpo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ovlpbmnxpo p { margin: 0; padding: 0; }
 #ovlpbmnxpo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ovlpbmnxpo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ovlpbmnxpo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ovlpbmnxpo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ovlpbmnxpo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ovlpbmnxpo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ovlpbmnxpo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ovlpbmnxpo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ovlpbmnxpo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ovlpbmnxpo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ovlpbmnxpo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ovlpbmnxpo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ovlpbmnxpo .gt_spanner_row { border-bottom-style: hidden; }
 #ovlpbmnxpo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ovlpbmnxpo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ovlpbmnxpo .gt_from_md> :first-child { margin-top: 0; }
 #ovlpbmnxpo .gt_from_md> :last-child { margin-bottom: 0; }
 #ovlpbmnxpo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ovlpbmnxpo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ovlpbmnxpo .gt_indent_1 { text-indent: 5px; }
 #ovlpbmnxpo .gt_indent_2 { text-indent: calc(5px * 2); }
 #ovlpbmnxpo .gt_indent_3 { text-indent: calc(5px * 3); }
 #ovlpbmnxpo .gt_indent_4 { text-indent: calc(5px * 4); }
 #ovlpbmnxpo .gt_indent_5 { text-indent: calc(5px * 5); }
 #ovlpbmnxpo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ovlpbmnxpo .gt_row_group_first td { border-top-width: 2px; }
 #ovlpbmnxpo .gt_row_group_first th { border-top-width: 2px; }
 #ovlpbmnxpo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ovlpbmnxpo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ovlpbmnxpo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ovlpbmnxpo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ovlpbmnxpo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ovlpbmnxpo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ovlpbmnxpo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ovlpbmnxpo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ovlpbmnxpo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ovlpbmnxpo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ovlpbmnxpo .gt_left { text-align: left; }
 #ovlpbmnxpo .gt_center { text-align: center; }
 #ovlpbmnxpo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ovlpbmnxpo .gt_font_normal { font-weight: normal; }
 #ovlpbmnxpo .gt_font_bold { font-weight: bold; }
 #ovlpbmnxpo .gt_font_italic { font-style: italic; }
 #ovlpbmnxpo .gt_super { font-size: 65%; }
 #ovlpbmnxpo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ovlpbmnxpo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ovlpbmnxpo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ovlpbmnxpo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ovlpbmnxpo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ovlpbmnxpo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#umflgxrjcv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#umflgxrjcv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#umflgxrjcv p { margin: 0; padding: 0; }
 #umflgxrjcv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #umflgxrjcv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #umflgxrjcv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #umflgxrjcv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #umflgxrjcv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #umflgxrjcv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #umflgxrjcv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #umflgxrjcv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #umflgxrjcv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #umflgxrjcv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #umflgxrjcv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #umflgxrjcv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #umflgxrjcv .gt_spanner_row { border-bottom-style: hidden; }
 #umflgxrjcv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #umflgxrjcv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #umflgxrjcv .gt_from_md> :first-child { margin-top: 0; }
 #umflgxrjcv .gt_from_md> :last-child { margin-bottom: 0; }
 #umflgxrjcv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #umflgxrjcv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #umflgxrjcv .gt_indent_1 { text-indent: 5px; }
 #umflgxrjcv .gt_indent_2 { text-indent: calc(5px * 2); }
 #umflgxrjcv .gt_indent_3 { text-indent: calc(5px * 3); }
 #umflgxrjcv .gt_indent_4 { text-indent: calc(5px * 4); }
 #umflgxrjcv .gt_indent_5 { text-indent: calc(5px * 5); }
 #umflgxrjcv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #umflgxrjcv .gt_row_group_first td { border-top-width: 2px; }
 #umflgxrjcv .gt_row_group_first th { border-top-width: 2px; }
 #umflgxrjcv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #umflgxrjcv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #umflgxrjcv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #umflgxrjcv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #umflgxrjcv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #umflgxrjcv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #umflgxrjcv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #umflgxrjcv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #umflgxrjcv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #umflgxrjcv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #umflgxrjcv .gt_left { text-align: left; }
 #umflgxrjcv .gt_center { text-align: center; }
 #umflgxrjcv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #umflgxrjcv .gt_font_normal { font-weight: normal; }
 #umflgxrjcv .gt_font_bold { font-weight: bold; }
 #umflgxrjcv .gt_font_italic { font-style: italic; }
 #umflgxrjcv .gt_super { font-size: 65%; }
 #umflgxrjcv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #umflgxrjcv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #umflgxrjcv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #umflgxrjcv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #umflgxrjcv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #umflgxrjcv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rvdhpyclzu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rvdhpyclzu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rvdhpyclzu p { margin: 0; padding: 0; }
 #rvdhpyclzu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rvdhpyclzu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rvdhpyclzu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rvdhpyclzu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rvdhpyclzu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rvdhpyclzu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rvdhpyclzu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rvdhpyclzu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rvdhpyclzu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rvdhpyclzu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rvdhpyclzu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rvdhpyclzu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rvdhpyclzu .gt_spanner_row { border-bottom-style: hidden; }
 #rvdhpyclzu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rvdhpyclzu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rvdhpyclzu .gt_from_md> :first-child { margin-top: 0; }
 #rvdhpyclzu .gt_from_md> :last-child { margin-bottom: 0; }
 #rvdhpyclzu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rvdhpyclzu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rvdhpyclzu .gt_indent_1 { text-indent: 5px; }
 #rvdhpyclzu .gt_indent_2 { text-indent: calc(5px * 2); }
 #rvdhpyclzu .gt_indent_3 { text-indent: calc(5px * 3); }
 #rvdhpyclzu .gt_indent_4 { text-indent: calc(5px * 4); }
 #rvdhpyclzu .gt_indent_5 { text-indent: calc(5px * 5); }
 #rvdhpyclzu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rvdhpyclzu .gt_row_group_first td { border-top-width: 2px; }
 #rvdhpyclzu .gt_row_group_first th { border-top-width: 2px; }
 #rvdhpyclzu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rvdhpyclzu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rvdhpyclzu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rvdhpyclzu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rvdhpyclzu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rvdhpyclzu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rvdhpyclzu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rvdhpyclzu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rvdhpyclzu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rvdhpyclzu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rvdhpyclzu .gt_left { text-align: left; }
 #rvdhpyclzu .gt_center { text-align: center; }
 #rvdhpyclzu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rvdhpyclzu .gt_font_normal { font-weight: normal; }
 #rvdhpyclzu .gt_font_bold { font-weight: bold; }
 #rvdhpyclzu .gt_font_italic { font-style: italic; }
 #rvdhpyclzu .gt_super { font-size: 65%; }
 #rvdhpyclzu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rvdhpyclzu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rvdhpyclzu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rvdhpyclzu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rvdhpyclzu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rvdhpyclzu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#zggjnvfxsz table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zggjnvfxsz thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zggjnvfxsz p { margin: 0; padding: 0; }
 #zggjnvfxsz .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zggjnvfxsz .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zggjnvfxsz .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zggjnvfxsz .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zggjnvfxsz .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zggjnvfxsz .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zggjnvfxsz .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zggjnvfxsz .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zggjnvfxsz .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zggjnvfxsz .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zggjnvfxsz .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zggjnvfxsz .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zggjnvfxsz .gt_spanner_row { border-bottom-style: hidden; }
 #zggjnvfxsz .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zggjnvfxsz .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zggjnvfxsz .gt_from_md> :first-child { margin-top: 0; }
 #zggjnvfxsz .gt_from_md> :last-child { margin-bottom: 0; }
 #zggjnvfxsz .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zggjnvfxsz .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zggjnvfxsz .gt_indent_1 { text-indent: 5px; }
 #zggjnvfxsz .gt_indent_2 { text-indent: calc(5px * 2); }
 #zggjnvfxsz .gt_indent_3 { text-indent: calc(5px * 3); }
 #zggjnvfxsz .gt_indent_4 { text-indent: calc(5px * 4); }
 #zggjnvfxsz .gt_indent_5 { text-indent: calc(5px * 5); }
 #zggjnvfxsz .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zggjnvfxsz .gt_row_group_first td { border-top-width: 2px; }
 #zggjnvfxsz .gt_row_group_first th { border-top-width: 2px; }
 #zggjnvfxsz .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zggjnvfxsz .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zggjnvfxsz .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zggjnvfxsz .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #zggjnvfxsz .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zggjnvfxsz .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zggjnvfxsz .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zggjnvfxsz .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zggjnvfxsz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zggjnvfxsz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zggjnvfxsz .gt_left { text-align: left; }
 #zggjnvfxsz .gt_center { text-align: center; }
 #zggjnvfxsz .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zggjnvfxsz .gt_font_normal { font-weight: normal; }
 #zggjnvfxsz .gt_font_bold { font-weight: bold; }
 #zggjnvfxsz .gt_font_italic { font-style: italic; }
 #zggjnvfxsz .gt_super { font-size: 65%; }
 #zggjnvfxsz .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zggjnvfxsz .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #zggjnvfxsz .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zggjnvfxsz .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zggjnvfxsz .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zggjnvfxsz .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
