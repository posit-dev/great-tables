# Table Theme Options

When you need to apply broad visual changes across an entire table, [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) is the right tool. Rather than styling individual cells or specific locations, this method lets you set colors, fonts, borders, and spacing for entire table parts in a single call. This page explains the structure of option names, demonstrates how to style different parts, and shows how to build a complete table theme.

A useful way to think about the relationship between [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) and [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style): use [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) when you want to set broad defaults for entire table parts (e.g., "all column labels should have this background color"). Use [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) when you need to target specific cells, columns, or rows. The two work together naturally: [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) sets the base theme, and [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style) applies targeted overrides on top of it.

Great Tables exposes options to customize the appearance of tables via two methods:

- [tab_style()](../reference/GT.tab_style.md#great_tables.GT.tab_style): targeted styles (e.g. color a specific cell of data, or a specific group label).
- [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options): broad styles (e.g. color the header and source notes).

Both methods target parts of the table, as shown in the diagram below.

<img src="../assets/gt_parts_of_a_table.svg" class="img-fluid" />

This page covers how to style and theme your table using [GT.tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options), which is meant to quickly set a broad range of styles.

We'll use the basic GT object below for most examples, since it marks some of the table parts.


``` python
from great_tables import GT, exibble

gt_ex = (
    GT(exibble.head(5), rowname_col="row", groupname_col="group")
    .tab_header("THE HEADING", "(a subtitle)")
    .tab_stubhead("THE STUBHEAD")
    .tab_source_note("THE SOURCE NOTE")
    .grand_summary_rows(fns={"GRAND SUMMARY ROW": lambda df: df.sum(numeric_only=True)})
)

gt_ex
```


<style>
#khoqgskgwd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#khoqgskgwd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#khoqgskgwd p { margin: 0; padding: 0; }
 #khoqgskgwd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #khoqgskgwd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #khoqgskgwd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #khoqgskgwd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #khoqgskgwd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #khoqgskgwd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khoqgskgwd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #khoqgskgwd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #khoqgskgwd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #khoqgskgwd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #khoqgskgwd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #khoqgskgwd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #khoqgskgwd .gt_spanner_row { border-bottom-style: hidden; }
 #khoqgskgwd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #khoqgskgwd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #khoqgskgwd .gt_from_md> :first-child { margin-top: 0; }
 #khoqgskgwd .gt_from_md> :last-child { margin-bottom: 0; }
 #khoqgskgwd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #khoqgskgwd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #khoqgskgwd .gt_indent_1 { text-indent: 5px; }
 #khoqgskgwd .gt_indent_2 { text-indent: calc(5px * 2); }
 #khoqgskgwd .gt_indent_3 { text-indent: calc(5px * 3); }
 #khoqgskgwd .gt_indent_4 { text-indent: calc(5px * 4); }
 #khoqgskgwd .gt_indent_5 { text-indent: calc(5px * 5); }
 #khoqgskgwd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #khoqgskgwd .gt_row_group_first td { border-top-width: 2px; }
 #khoqgskgwd .gt_row_group_first th { border-top-width: 2px; }
 #khoqgskgwd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #khoqgskgwd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khoqgskgwd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #khoqgskgwd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #khoqgskgwd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #khoqgskgwd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #khoqgskgwd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #khoqgskgwd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #khoqgskgwd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khoqgskgwd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #khoqgskgwd .gt_left { text-align: left; }
 #khoqgskgwd .gt_center { text-align: center; }
 #khoqgskgwd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #khoqgskgwd .gt_font_normal { font-weight: normal; }
 #khoqgskgwd .gt_font_bold { font-weight: bold; }
 #khoqgskgwd .gt_font_italic { font-style: italic; }
 #khoqgskgwd .gt_super { font-size: 65%; }
 #khoqgskgwd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khoqgskgwd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #khoqgskgwd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #khoqgskgwd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #khoqgskgwd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #khoqgskgwd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" id="title" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
</tr>
<tr class="gt_col_headings">
<th id="THE-STUBHEAD" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">THE STUBHEAD</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 fctr">one</td>
<td class="gt_row gt_right" headers="grp_a stub-1 date">2015-01-15</td>
<td class="gt_row gt_right" headers="grp_a stub-1 time">13:35</td>
<td class="gt_row gt_right" headers="grp_a stub-1 datetime">2018-01-01 02:22</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
<td class="gt_row gt_right" headers="grp_a stub-2 date">2015-02-15</td>
<td class="gt_row gt_right" headers="grp_a stub-2 time">14:40</td>
<td class="gt_row gt_right" headers="grp_a stub-2 datetime">2018-02-02 14:33</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
<td class="gt_row gt_right" headers="grp_a stub-3 date">2015-03-15</td>
<td class="gt_row gt_right" headers="grp_a stub-3 time">15:45</td>
<td class="gt_row gt_right" headers="grp_a stub-3 datetime">2018-03-03 03:44</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
<td class="gt_row gt_right" headers="grp_a stub-4 date">2015-04-15</td>
<td class="gt_row gt_right" headers="grp_a stub-4 time">16:50</td>
<td class="gt_row gt_right" headers="grp_a stub-4 datetime">2018-04-04 15:55</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-5 fctr">five</td>
<td class="gt_row gt_right" headers="grp_b stub-5 date">2015-05-15</td>
<td class="gt_row gt_right" headers="grp_b stub-5 time">17:55</td>
<td class="gt_row gt_right" headers="grp_b stub-5 datetime">2018-05-05 04:00</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="grand-summary-GRAND-SUMMARY-ROW" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW num">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW fctr">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW date">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW time">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW datetime">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW currency">66495.1</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="8" class="gt_sourcenote">THE SOURCE NOTE</td>
</tr>
</tfoot>

</table>


# Table option parts

As the graph above showed, tables are made of many parts. These include the heading, column labels, and the stub. [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) organizes options based on table part.

The code below illustrates the table parts [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) can target, by setting the background color for various parts.


``` python
(
    gt_ex
    .tab_options(
        container_width = "100%",
        table_background_color="lightblue",
        heading_background_color = "gold",
        column_labels_background_color="aquamarine",
        row_group_background_color="lightyellow",
        stub_background_color="lightgreen",
        source_notes_background_color="#f1e2af",
        grand_summary_row_background_color="lightpink",
    )
)
```


<style>
#hjgbicvkhe table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hjgbicvkhe thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hjgbicvkhe p { margin: 0; padding: 0; }
 #hjgbicvkhe .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: lightblue; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hjgbicvkhe .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hjgbicvkhe .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: lightblue; border-bottom-width: 0; }
 #hjgbicvkhe .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: lightblue; border-top-width: 0; }
 #hjgbicvkhe .gt_heading { background-color: gold; text-align: center; border-bottom-color: lightblue; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hjgbicvkhe .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjgbicvkhe .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hjgbicvkhe .gt_col_heading { color: #333333; background-color: aquamarine; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hjgbicvkhe .gt_column_spanner_outer { color: #333333; background-color: aquamarine; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hjgbicvkhe .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hjgbicvkhe .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hjgbicvkhe .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hjgbicvkhe .gt_spanner_row { border-bottom-style: hidden; }
 #hjgbicvkhe .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: lightyellow; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hjgbicvkhe .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: lightyellow; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hjgbicvkhe .gt_from_md> :first-child { margin-top: 0; }
 #hjgbicvkhe .gt_from_md> :last-child { margin-bottom: 0; }
 #hjgbicvkhe .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hjgbicvkhe .gt_stub { color: #333333; background-color: lightgreen; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hjgbicvkhe .gt_indent_1 { text-indent: 5px; }
 #hjgbicvkhe .gt_indent_2 { text-indent: calc(5px * 2); }
 #hjgbicvkhe .gt_indent_3 { text-indent: calc(5px * 3); }
 #hjgbicvkhe .gt_indent_4 { text-indent: calc(5px * 4); }
 #hjgbicvkhe .gt_indent_5 { text-indent: calc(5px * 5); }
 #hjgbicvkhe .gt_stub_row_group { color: #333333; background-color: lightblue; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hjgbicvkhe .gt_row_group_first td { border-top-width: 2px; }
 #hjgbicvkhe .gt_row_group_first th { border-top-width: 2px; }
 #hjgbicvkhe .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hjgbicvkhe .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjgbicvkhe .gt_summary_row { color: #333333; background-color: lightblue; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hjgbicvkhe .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hjgbicvkhe .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hjgbicvkhe .gt_grand_summary_row { color: #333333; background-color: lightpink; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hjgbicvkhe .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hjgbicvkhe .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hjgbicvkhe .gt_sourcenotes { color: #333333; background-color: #f1e2af; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjgbicvkhe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hjgbicvkhe .gt_left { text-align: left; }
 #hjgbicvkhe .gt_center { text-align: center; }
 #hjgbicvkhe .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hjgbicvkhe .gt_font_normal { font-weight: normal; }
 #hjgbicvkhe .gt_font_bold { font-weight: bold; }
 #hjgbicvkhe .gt_font_italic { font-style: italic; }
 #hjgbicvkhe .gt_super { font-size: 65%; }
 #hjgbicvkhe .gt_footnotes { color: font-color(lightblue); background-color: lightblue; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjgbicvkhe .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hjgbicvkhe .gt_sourcenotes { color: #333333; background-color: #f1e2af; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hjgbicvkhe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hjgbicvkhe .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hjgbicvkhe .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" id="title" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
</tr>
<tr class="gt_col_headings">
<th id="THE-STUBHEAD" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">THE STUBHEAD</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 fctr">one</td>
<td class="gt_row gt_right" headers="grp_a stub-1 date">2015-01-15</td>
<td class="gt_row gt_right" headers="grp_a stub-1 time">13:35</td>
<td class="gt_row gt_right" headers="grp_a stub-1 datetime">2018-01-01 02:22</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
<td class="gt_row gt_right" headers="grp_a stub-2 date">2015-02-15</td>
<td class="gt_row gt_right" headers="grp_a stub-2 time">14:40</td>
<td class="gt_row gt_right" headers="grp_a stub-2 datetime">2018-02-02 14:33</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
<td class="gt_row gt_right" headers="grp_a stub-3 date">2015-03-15</td>
<td class="gt_row gt_right" headers="grp_a stub-3 time">15:45</td>
<td class="gt_row gt_right" headers="grp_a stub-3 datetime">2018-03-03 03:44</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
<td class="gt_row gt_right" headers="grp_a stub-4 date">2015-04-15</td>
<td class="gt_row gt_right" headers="grp_a stub-4 time">16:50</td>
<td class="gt_row gt_right" headers="grp_a stub-4 datetime">2018-04-04 15:55</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-5 fctr">five</td>
<td class="gt_row gt_right" headers="grp_b stub-5 date">2015-05-15</td>
<td class="gt_row gt_right" headers="grp_b stub-5 time">17:55</td>
<td class="gt_row gt_right" headers="grp_b stub-5 datetime">2018-05-05 04:00</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="grand-summary-GRAND-SUMMARY-ROW" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW num">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW fctr">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW date">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW time">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW datetime">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW currency">66495.1</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="8" class="gt_sourcenote">THE SOURCE NOTE</td>
</tr>
</tfoot>

</table>


Notice two important pieces:

- The argument `heading_background_color="gold"` sets the heading part's background to gold.
- Parts like `container` and `table` are the broadest. They cover all the other parts of the table.


# Finding options: part, type, attribute

Option names in [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) follow a consistent naming convention. Understanding the pattern makes it easy to find the exact option you need without searching through documentation. The format is:

``` python
{part name}_{type}_{attribute}
```

For example, the option `row_group_border_top_color` has these pieces:

- **part**: `row_group`
- **type**: `border_top`
- **attribute**: `color`

> **Note: Note**
>
> Here are the parts supported in [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options):
>
> - container, table
> - heading, source_note
> - column_labels, row_group, stub, stub_row
> - table_body


# Styling borders

Many table parts support customizing border colors and style. This is shown below for column labels.


``` python
gt_ex.tab_options(
    column_labels_border_top_color="blue",
    column_labels_border_top_style="solid",
    column_labels_border_top_width="5px"
)
```


<style>
#gidoxuknfe table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gidoxuknfe thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gidoxuknfe p { margin: 0; padding: 0; }
 #gidoxuknfe .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gidoxuknfe .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gidoxuknfe .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gidoxuknfe .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gidoxuknfe .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gidoxuknfe .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gidoxuknfe .gt_col_headings { border-top-style: solid; border-top-width: 5px; border-top-color: blue; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gidoxuknfe .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gidoxuknfe .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gidoxuknfe .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gidoxuknfe .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gidoxuknfe .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gidoxuknfe .gt_spanner_row { border-bottom-style: hidden; }
 #gidoxuknfe .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gidoxuknfe .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gidoxuknfe .gt_from_md> :first-child { margin-top: 0; }
 #gidoxuknfe .gt_from_md> :last-child { margin-bottom: 0; }
 #gidoxuknfe .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gidoxuknfe .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gidoxuknfe .gt_indent_1 { text-indent: 5px; }
 #gidoxuknfe .gt_indent_2 { text-indent: calc(5px * 2); }
 #gidoxuknfe .gt_indent_3 { text-indent: calc(5px * 3); }
 #gidoxuknfe .gt_indent_4 { text-indent: calc(5px * 4); }
 #gidoxuknfe .gt_indent_5 { text-indent: calc(5px * 5); }
 #gidoxuknfe .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gidoxuknfe .gt_row_group_first td { border-top-width: 2px; }
 #gidoxuknfe .gt_row_group_first th { border-top-width: 2px; }
 #gidoxuknfe .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gidoxuknfe .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gidoxuknfe .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gidoxuknfe .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gidoxuknfe .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gidoxuknfe .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gidoxuknfe .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gidoxuknfe .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gidoxuknfe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gidoxuknfe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gidoxuknfe .gt_left { text-align: left; }
 #gidoxuknfe .gt_center { text-align: center; }
 #gidoxuknfe .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gidoxuknfe .gt_font_normal { font-weight: normal; }
 #gidoxuknfe .gt_font_bold { font-weight: bold; }
 #gidoxuknfe .gt_font_italic { font-style: italic; }
 #gidoxuknfe .gt_super { font-size: 65%; }
 #gidoxuknfe .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gidoxuknfe .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gidoxuknfe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gidoxuknfe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gidoxuknfe .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gidoxuknfe .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" id="title" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
</tr>
<tr class="gt_col_headings">
<th id="THE-STUBHEAD" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">THE STUBHEAD</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 fctr">one</td>
<td class="gt_row gt_right" headers="grp_a stub-1 date">2015-01-15</td>
<td class="gt_row gt_right" headers="grp_a stub-1 time">13:35</td>
<td class="gt_row gt_right" headers="grp_a stub-1 datetime">2018-01-01 02:22</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
<td class="gt_row gt_right" headers="grp_a stub-2 date">2015-02-15</td>
<td class="gt_row gt_right" headers="grp_a stub-2 time">14:40</td>
<td class="gt_row gt_right" headers="grp_a stub-2 datetime">2018-02-02 14:33</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
<td class="gt_row gt_right" headers="grp_a stub-3 date">2015-03-15</td>
<td class="gt_row gt_right" headers="grp_a stub-3 time">15:45</td>
<td class="gt_row gt_right" headers="grp_a stub-3 datetime">2018-03-03 03:44</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
<td class="gt_row gt_right" headers="grp_a stub-4 date">2015-04-15</td>
<td class="gt_row gt_right" headers="grp_a stub-4 time">16:50</td>
<td class="gt_row gt_right" headers="grp_a stub-4 datetime">2018-04-04 15:55</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-5 fctr">five</td>
<td class="gt_row gt_right" headers="grp_b stub-5 date">2015-05-15</td>
<td class="gt_row gt_right" headers="grp_b stub-5 time">17:55</td>
<td class="gt_row gt_right" headers="grp_b stub-5 datetime">2018-05-05 04:00</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="grand-summary-GRAND-SUMMARY-ROW" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW num">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW fctr">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW date">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW time">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW datetime">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW currency">66495.1</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="8" class="gt_sourcenote">THE SOURCE NOTE</td>
</tr>
</tfoot>

</table>


The column labels section now has a thick blue border on top. Each border option follows the same triplet of `color`, `style`, and `width` attributes, which you can combine to create the exact look you want.


# Styling background color


``` python
gt_ex.tab_options(
    heading_background_color="purple"
)
```


<style>
#uvlrsgihhb table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uvlrsgihhb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uvlrsgihhb p { margin: 0; padding: 0; }
 #uvlrsgihhb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #uvlrsgihhb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uvlrsgihhb .gt_title { color: #FFFFFF; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uvlrsgihhb .gt_subtitle { color: #FFFFFF; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uvlrsgihhb .gt_heading { background-color: purple; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uvlrsgihhb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvlrsgihhb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uvlrsgihhb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uvlrsgihhb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uvlrsgihhb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uvlrsgihhb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uvlrsgihhb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uvlrsgihhb .gt_spanner_row { border-bottom-style: hidden; }
 #uvlrsgihhb .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uvlrsgihhb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #uvlrsgihhb .gt_from_md> :first-child { margin-top: 0; }
 #uvlrsgihhb .gt_from_md> :last-child { margin-bottom: 0; }
 #uvlrsgihhb .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #uvlrsgihhb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #uvlrsgihhb .gt_indent_1 { text-indent: 5px; }
 #uvlrsgihhb .gt_indent_2 { text-indent: calc(5px * 2); }
 #uvlrsgihhb .gt_indent_3 { text-indent: calc(5px * 3); }
 #uvlrsgihhb .gt_indent_4 { text-indent: calc(5px * 4); }
 #uvlrsgihhb .gt_indent_5 { text-indent: calc(5px * 5); }
 #uvlrsgihhb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uvlrsgihhb .gt_row_group_first td { border-top-width: 2px; }
 #uvlrsgihhb .gt_row_group_first th { border-top-width: 2px; }
 #uvlrsgihhb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uvlrsgihhb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvlrsgihhb .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uvlrsgihhb .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uvlrsgihhb .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvlrsgihhb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uvlrsgihhb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uvlrsgihhb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uvlrsgihhb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvlrsgihhb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uvlrsgihhb .gt_left { text-align: left; }
 #uvlrsgihhb .gt_center { text-align: center; }
 #uvlrsgihhb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uvlrsgihhb .gt_font_normal { font-weight: normal; }
 #uvlrsgihhb .gt_font_bold { font-weight: bold; }
 #uvlrsgihhb .gt_font_italic { font-style: italic; }
 #uvlrsgihhb .gt_super { font-size: 65%; }
 #uvlrsgihhb .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvlrsgihhb .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uvlrsgihhb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvlrsgihhb .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uvlrsgihhb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uvlrsgihhb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" id="title" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
</tr>
<tr class="gt_col_headings">
<th id="THE-STUBHEAD" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">THE STUBHEAD</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 fctr">one</td>
<td class="gt_row gt_right" headers="grp_a stub-1 date">2015-01-15</td>
<td class="gt_row gt_right" headers="grp_a stub-1 time">13:35</td>
<td class="gt_row gt_right" headers="grp_a stub-1 datetime">2018-01-01 02:22</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
<td class="gt_row gt_right" headers="grp_a stub-2 date">2015-02-15</td>
<td class="gt_row gt_right" headers="grp_a stub-2 time">14:40</td>
<td class="gt_row gt_right" headers="grp_a stub-2 datetime">2018-02-02 14:33</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
<td class="gt_row gt_right" headers="grp_a stub-3 date">2015-03-15</td>
<td class="gt_row gt_right" headers="grp_a stub-3 time">15:45</td>
<td class="gt_row gt_right" headers="grp_a stub-3 datetime">2018-03-03 03:44</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
<td class="gt_row gt_right" headers="grp_a stub-4 date">2015-04-15</td>
<td class="gt_row gt_right" headers="grp_a stub-4 time">16:50</td>
<td class="gt_row gt_right" headers="grp_a stub-4 datetime">2018-04-04 15:55</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-5 fctr">five</td>
<td class="gt_row gt_right" headers="grp_b stub-5 date">2015-05-15</td>
<td class="gt_row gt_right" headers="grp_b stub-5 time">17:55</td>
<td class="gt_row gt_right" headers="grp_b stub-5 datetime">2018-05-05 04:00</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="grand-summary-GRAND-SUMMARY-ROW" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW num">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW fctr">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW date">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW time">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW datetime">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW currency">66495.1</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="8" class="gt_sourcenote">THE SOURCE NOTE</td>
</tr>
</tfoot>

</table>


The heading area (title and subtitle) is now purple. Background color options are available for every table part, letting you assign a distinct visual identity to each region.


# Styling body cells

The table body can style the lines between individual cells. Use the `hline` and `vline` option types to specify cell line color, style, and width.

For example, the code below changes horizontal lines (`hline`) between cells to be red, dashed lines.


``` python
gt_ex.tab_options(
    table_body_hlines_color="red",
    table_body_hlines_style="dashed",
    table_body_hlines_width="4px",
)
```


<style>
#gcyuqvjzmw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gcyuqvjzmw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gcyuqvjzmw p { margin: 0; padding: 0; }
 #gcyuqvjzmw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #gcyuqvjzmw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gcyuqvjzmw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gcyuqvjzmw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gcyuqvjzmw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gcyuqvjzmw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gcyuqvjzmw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gcyuqvjzmw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gcyuqvjzmw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gcyuqvjzmw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gcyuqvjzmw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gcyuqvjzmw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gcyuqvjzmw .gt_spanner_row { border-bottom-style: hidden; }
 #gcyuqvjzmw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gcyuqvjzmw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #gcyuqvjzmw .gt_from_md> :first-child { margin-top: 0; }
 #gcyuqvjzmw .gt_from_md> :last-child { margin-bottom: 0; }
 #gcyuqvjzmw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: dashed; border-top-width: 4px; border-top-color: red; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #gcyuqvjzmw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #gcyuqvjzmw .gt_indent_1 { text-indent: 5px; }
 #gcyuqvjzmw .gt_indent_2 { text-indent: calc(5px * 2); }
 #gcyuqvjzmw .gt_indent_3 { text-indent: calc(5px * 3); }
 #gcyuqvjzmw .gt_indent_4 { text-indent: calc(5px * 4); }
 #gcyuqvjzmw .gt_indent_5 { text-indent: calc(5px * 5); }
 #gcyuqvjzmw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gcyuqvjzmw .gt_row_group_first td { border-top-width: 2px; }
 #gcyuqvjzmw .gt_row_group_first th { border-top-width: 2px; }
 #gcyuqvjzmw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gcyuqvjzmw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gcyuqvjzmw .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gcyuqvjzmw .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gcyuqvjzmw .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gcyuqvjzmw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gcyuqvjzmw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gcyuqvjzmw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gcyuqvjzmw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gcyuqvjzmw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gcyuqvjzmw .gt_left { text-align: left; }
 #gcyuqvjzmw .gt_center { text-align: center; }
 #gcyuqvjzmw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gcyuqvjzmw .gt_font_normal { font-weight: normal; }
 #gcyuqvjzmw .gt_font_bold { font-weight: bold; }
 #gcyuqvjzmw .gt_font_italic { font-style: italic; }
 #gcyuqvjzmw .gt_super { font-size: 65%; }
 #gcyuqvjzmw .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gcyuqvjzmw .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gcyuqvjzmw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gcyuqvjzmw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gcyuqvjzmw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gcyuqvjzmw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" id="title" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
</tr>
<tr class="gt_col_headings">
<th id="THE-STUBHEAD" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">THE STUBHEAD</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 fctr">one</td>
<td class="gt_row gt_right" headers="grp_a stub-1 date">2015-01-15</td>
<td class="gt_row gt_right" headers="grp_a stub-1 time">13:35</td>
<td class="gt_row gt_right" headers="grp_a stub-1 datetime">2018-01-01 02:22</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
<td class="gt_row gt_right" headers="grp_a stub-2 date">2015-02-15</td>
<td class="gt_row gt_right" headers="grp_a stub-2 time">14:40</td>
<td class="gt_row gt_right" headers="grp_a stub-2 datetime">2018-02-02 14:33</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
<td class="gt_row gt_right" headers="grp_a stub-3 date">2015-03-15</td>
<td class="gt_row gt_right" headers="grp_a stub-3 time">15:45</td>
<td class="gt_row gt_right" headers="grp_a stub-3 datetime">2018-03-03 03:44</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
<td class="gt_row gt_right" headers="grp_a stub-4 date">2015-04-15</td>
<td class="gt_row gt_right" headers="grp_a stub-4 time">16:50</td>
<td class="gt_row gt_right" headers="grp_a stub-4 datetime">2018-04-04 15:55</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-5 fctr">five</td>
<td class="gt_row gt_right" headers="grp_b stub-5 date">2015-05-15</td>
<td class="gt_row gt_right" headers="grp_b stub-5 time">17:55</td>
<td class="gt_row gt_right" headers="grp_b stub-5 datetime">2018-05-05 04:00</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="grand-summary-GRAND-SUMMARY-ROW" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW num">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW fctr">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW date">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW time">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW datetime">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW currency">66495.1</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="8" class="gt_sourcenote">THE SOURCE NOTE</td>
</tr>
</tfoot>

</table>


In order to define the vertical lines between cells, set `vline` styles. For example, the code below makes both horizontal and vertical lines between cells solid.


``` python
gt_ex.tab_options(
    table_body_hlines_style="solid",
    table_body_vlines_style="solid",
)
```


<style>
#twqavwgzcd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#twqavwgzcd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#twqavwgzcd p { margin: 0; padding: 0; }
 #twqavwgzcd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #twqavwgzcd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #twqavwgzcd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #twqavwgzcd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #twqavwgzcd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #twqavwgzcd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #twqavwgzcd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #twqavwgzcd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #twqavwgzcd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #twqavwgzcd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #twqavwgzcd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #twqavwgzcd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #twqavwgzcd .gt_spanner_row { border-bottom-style: hidden; }
 #twqavwgzcd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #twqavwgzcd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #twqavwgzcd .gt_from_md> :first-child { margin-top: 0; }
 #twqavwgzcd .gt_from_md> :last-child { margin-bottom: 0; }
 #twqavwgzcd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: solid; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: solid; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #twqavwgzcd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #twqavwgzcd .gt_indent_1 { text-indent: 5px; }
 #twqavwgzcd .gt_indent_2 { text-indent: calc(5px * 2); }
 #twqavwgzcd .gt_indent_3 { text-indent: calc(5px * 3); }
 #twqavwgzcd .gt_indent_4 { text-indent: calc(5px * 4); }
 #twqavwgzcd .gt_indent_5 { text-indent: calc(5px * 5); }
 #twqavwgzcd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #twqavwgzcd .gt_row_group_first td { border-top-width: 2px; }
 #twqavwgzcd .gt_row_group_first th { border-top-width: 2px; }
 #twqavwgzcd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #twqavwgzcd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #twqavwgzcd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #twqavwgzcd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #twqavwgzcd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #twqavwgzcd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #twqavwgzcd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #twqavwgzcd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #twqavwgzcd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #twqavwgzcd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #twqavwgzcd .gt_left { text-align: left; }
 #twqavwgzcd .gt_center { text-align: center; }
 #twqavwgzcd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #twqavwgzcd .gt_font_normal { font-weight: normal; }
 #twqavwgzcd .gt_font_bold { font-weight: bold; }
 #twqavwgzcd .gt_font_italic { font-style: italic; }
 #twqavwgzcd .gt_super { font-size: 65%; }
 #twqavwgzcd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #twqavwgzcd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #twqavwgzcd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #twqavwgzcd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #twqavwgzcd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #twqavwgzcd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" id="title" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
</tr>
<tr class="gt_col_headings">
<th id="THE-STUBHEAD" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">THE STUBHEAD</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 fctr">one</td>
<td class="gt_row gt_right" headers="grp_a stub-1 date">2015-01-15</td>
<td class="gt_row gt_right" headers="grp_a stub-1 time">13:35</td>
<td class="gt_row gt_right" headers="grp_a stub-1 datetime">2018-01-01 02:22</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
<td class="gt_row gt_right" headers="grp_a stub-2 date">2015-02-15</td>
<td class="gt_row gt_right" headers="grp_a stub-2 time">14:40</td>
<td class="gt_row gt_right" headers="grp_a stub-2 datetime">2018-02-02 14:33</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
<td class="gt_row gt_right" headers="grp_a stub-3 date">2015-03-15</td>
<td class="gt_row gt_right" headers="grp_a stub-3 time">15:45</td>
<td class="gt_row gt_right" headers="grp_a stub-3 datetime">2018-03-03 03:44</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
<td class="gt_row gt_right" headers="grp_a stub-4 date">2015-04-15</td>
<td class="gt_row gt_right" headers="grp_a stub-4 time">16:50</td>
<td class="gt_row gt_right" headers="grp_a stub-4 datetime">2018-04-04 15:55</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-5 fctr">five</td>
<td class="gt_row gt_right" headers="grp_b stub-5 date">2015-05-15</td>
<td class="gt_row gt_right" headers="grp_b stub-5 time">17:55</td>
<td class="gt_row gt_right" headers="grp_b stub-5 datetime">2018-05-05 04:00</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="grand-summary-GRAND-SUMMARY-ROW" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW num">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW fctr">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW date">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW time">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW datetime">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW currency">66495.1</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="8" class="gt_sourcenote">THE SOURCE NOTE</td>
</tr>
</tfoot>

</table>


With both `hlines` and `vlines` set to solid, the table body displays a classic grid appearance. Setting either to `"none"` removes those lines entirely for a cleaner, minimal look.


# Set options across table parts

Some options starting with `table_` apply to all parts of the table. For example, fonts and background color apply everywhere.


``` python
gt_ex.tab_options(
    table_background_color="green",
    table_font_color="darkblue",
    table_font_style="italic",
    table_font_names="Times New Roman"
)
```


<style>
#mggoipfddt table {
          font-family: 'Times New Roman';
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mggoipfddt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mggoipfddt p { margin: 0; padding: 0; }
 #mggoipfddt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #FFFFFF; font-size: 16px; font-weight: normal; font-style: italic; background-color: green; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mggoipfddt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mggoipfddt .gt_title { color: #FFFFFF; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: green; border-bottom-width: 0; }
 #mggoipfddt .gt_subtitle { color: #FFFFFF; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: green; border-top-width: 0; }
 #mggoipfddt .gt_heading { background-color: green; text-align: center; border-bottom-color: green; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mggoipfddt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mggoipfddt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mggoipfddt .gt_col_heading { color: #FFFFFF; background-color: green; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mggoipfddt .gt_column_spanner_outer { color: #FFFFFF; background-color: green; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mggoipfddt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mggoipfddt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mggoipfddt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mggoipfddt .gt_spanner_row { border-bottom-style: hidden; }
 #mggoipfddt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #FFFFFF; background-color: green; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mggoipfddt .gt_empty_group_heading { padding: 0.5px; color: #FFFFFF; background-color: green; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mggoipfddt .gt_from_md> :first-child { margin-top: 0; }
 #mggoipfddt .gt_from_md> :last-child { margin-bottom: 0; }
 #mggoipfddt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mggoipfddt .gt_stub { color: #FFFFFF; background-color: green; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mggoipfddt .gt_indent_1 { text-indent: 5px; }
 #mggoipfddt .gt_indent_2 { text-indent: calc(5px * 2); }
 #mggoipfddt .gt_indent_3 { text-indent: calc(5px * 3); }
 #mggoipfddt .gt_indent_4 { text-indent: calc(5px * 4); }
 #mggoipfddt .gt_indent_5 { text-indent: calc(5px * 5); }
 #mggoipfddt .gt_stub_row_group { color: #FFFFFF; background-color: green; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mggoipfddt .gt_row_group_first td { border-top-width: 2px; }
 #mggoipfddt .gt_row_group_first th { border-top-width: 2px; }
 #mggoipfddt .gt_striped { color: #00008B; background-color: #F4F4F4; }
 #mggoipfddt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mggoipfddt .gt_summary_row { color: #FFFFFF; background-color: green; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mggoipfddt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mggoipfddt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mggoipfddt .gt_grand_summary_row { color: #FFFFFF; background-color: green; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mggoipfddt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mggoipfddt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mggoipfddt .gt_sourcenotes { color: #FFFFFF; background-color: green; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mggoipfddt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mggoipfddt .gt_left { text-align: left; }
 #mggoipfddt .gt_center { text-align: center; }
 #mggoipfddt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mggoipfddt .gt_font_normal { font-weight: normal; }
 #mggoipfddt .gt_font_bold { font-weight: bold; }
 #mggoipfddt .gt_font_italic { font-style: italic; }
 #mggoipfddt .gt_super { font-size: 65%; }
 #mggoipfddt .gt_footnotes { color: font-color(green); background-color: green; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mggoipfddt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mggoipfddt .gt_sourcenotes { color: #FFFFFF; background-color: green; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mggoipfddt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mggoipfddt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mggoipfddt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" id="title" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
</tr>
<tr class="gt_col_headings">
<th id="THE-STUBHEAD" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">THE STUBHEAD</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 fctr">one</td>
<td class="gt_row gt_right" headers="grp_a stub-1 date">2015-01-15</td>
<td class="gt_row gt_right" headers="grp_a stub-1 time">13:35</td>
<td class="gt_row gt_right" headers="grp_a stub-1 datetime">2018-01-01 02:22</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
<td class="gt_row gt_right" headers="grp_a stub-2 date">2015-02-15</td>
<td class="gt_row gt_right" headers="grp_a stub-2 time">14:40</td>
<td class="gt_row gt_right" headers="grp_a stub-2 datetime">2018-02-02 14:33</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
<td class="gt_row gt_right" headers="grp_a stub-3 date">2015-03-15</td>
<td class="gt_row gt_right" headers="grp_a stub-3 time">15:45</td>
<td class="gt_row gt_right" headers="grp_a stub-3 datetime">2018-03-03 03:44</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
<td class="gt_row gt_right" headers="grp_a stub-4 date">2015-04-15</td>
<td class="gt_row gt_right" headers="grp_a stub-4 time">16:50</td>
<td class="gt_row gt_right" headers="grp_a stub-4 datetime">2018-04-04 15:55</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-5 fctr">five</td>
<td class="gt_row gt_right" headers="grp_b stub-5 date">2015-05-15</td>
<td class="gt_row gt_right" headers="grp_b stub-5 time">17:55</td>
<td class="gt_row gt_right" headers="grp_b stub-5 datetime">2018-05-05 04:00</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="grand-summary-GRAND-SUMMARY-ROW" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW num">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW fctr">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW date">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW time">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW datetime">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW currency">66495.1</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="8" class="gt_sourcenote">THE SOURCE NOTE</td>
</tr>
</tfoot>

</table>


Options set across the whole table, can be overridden by styling a specific part.


``` python
gt_ex.tab_options(
    table_background_color="orange",
    heading_background_color="pink"
)
```


<style>
#qyvoxegfwt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qyvoxegfwt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qyvoxegfwt p { margin: 0; padding: 0; }
 #qyvoxegfwt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: orange; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qyvoxegfwt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qyvoxegfwt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: orange; border-bottom-width: 0; }
 #qyvoxegfwt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: orange; border-top-width: 0; }
 #qyvoxegfwt .gt_heading { background-color: pink; text-align: center; border-bottom-color: orange; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qyvoxegfwt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qyvoxegfwt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qyvoxegfwt .gt_col_heading { color: #333333; background-color: orange; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qyvoxegfwt .gt_column_spanner_outer { color: #333333; background-color: orange; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qyvoxegfwt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qyvoxegfwt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qyvoxegfwt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qyvoxegfwt .gt_spanner_row { border-bottom-style: hidden; }
 #qyvoxegfwt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: orange; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qyvoxegfwt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: orange; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qyvoxegfwt .gt_from_md> :first-child { margin-top: 0; }
 #qyvoxegfwt .gt_from_md> :last-child { margin-bottom: 0; }
 #qyvoxegfwt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qyvoxegfwt .gt_stub { color: #333333; background-color: orange; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qyvoxegfwt .gt_indent_1 { text-indent: 5px; }
 #qyvoxegfwt .gt_indent_2 { text-indent: calc(5px * 2); }
 #qyvoxegfwt .gt_indent_3 { text-indent: calc(5px * 3); }
 #qyvoxegfwt .gt_indent_4 { text-indent: calc(5px * 4); }
 #qyvoxegfwt .gt_indent_5 { text-indent: calc(5px * 5); }
 #qyvoxegfwt .gt_stub_row_group { color: #333333; background-color: orange; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qyvoxegfwt .gt_row_group_first td { border-top-width: 2px; }
 #qyvoxegfwt .gt_row_group_first th { border-top-width: 2px; }
 #qyvoxegfwt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qyvoxegfwt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qyvoxegfwt .gt_summary_row { color: #333333; background-color: orange; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qyvoxegfwt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qyvoxegfwt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qyvoxegfwt .gt_grand_summary_row { color: #333333; background-color: orange; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qyvoxegfwt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qyvoxegfwt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qyvoxegfwt .gt_sourcenotes { color: #333333; background-color: orange; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qyvoxegfwt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qyvoxegfwt .gt_left { text-align: left; }
 #qyvoxegfwt .gt_center { text-align: center; }
 #qyvoxegfwt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qyvoxegfwt .gt_font_normal { font-weight: normal; }
 #qyvoxegfwt .gt_font_bold { font-weight: bold; }
 #qyvoxegfwt .gt_font_italic { font-style: italic; }
 #qyvoxegfwt .gt_super { font-size: 65%; }
 #qyvoxegfwt .gt_footnotes { color: font-color(orange); background-color: orange; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qyvoxegfwt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qyvoxegfwt .gt_sourcenotes { color: #333333; background-color: orange; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qyvoxegfwt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qyvoxegfwt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qyvoxegfwt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" id="title" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
</tr>
<tr class="gt_col_headings">
<th id="THE-STUBHEAD" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">THE STUBHEAD</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 fctr">one</td>
<td class="gt_row gt_right" headers="grp_a stub-1 date">2015-01-15</td>
<td class="gt_row gt_right" headers="grp_a stub-1 time">13:35</td>
<td class="gt_row gt_right" headers="grp_a stub-1 datetime">2018-01-01 02:22</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
<td class="gt_row gt_right" headers="grp_a stub-2 date">2015-02-15</td>
<td class="gt_row gt_right" headers="grp_a stub-2 time">14:40</td>
<td class="gt_row gt_right" headers="grp_a stub-2 datetime">2018-02-02 14:33</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
<td class="gt_row gt_right" headers="grp_a stub-3 date">2015-03-15</td>
<td class="gt_row gt_right" headers="grp_a stub-3 time">15:45</td>
<td class="gt_row gt_right" headers="grp_a stub-3 datetime">2018-03-03 03:44</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
<td class="gt_row gt_right" headers="grp_a stub-4 date">2015-04-15</td>
<td class="gt_row gt_right" headers="grp_a stub-4 time">16:50</td>
<td class="gt_row gt_right" headers="grp_a stub-4 datetime">2018-04-04 15:55</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-5 fctr">five</td>
<td class="gt_row gt_right" headers="grp_b stub-5 date">2015-05-15</td>
<td class="gt_row gt_right" headers="grp_b stub-5 time">17:55</td>
<td class="gt_row gt_right" headers="grp_b stub-5 datetime">2018-05-05 04:00</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="grand-summary-GRAND-SUMMARY-ROW" class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row" scope="row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW num">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW char">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW fctr">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW date">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW time">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW datetime">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row" headers="grand-summary-GRAND-SUMMARY-ROW currency">66495.1</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="8" class="gt_sourcenote">THE SOURCE NOTE</td>
</tr>
</tfoot>

</table>


The orange background applies everywhere except the heading, which overrides it with pink. This layered approach means you can set sensible table-wide defaults and then customize individual parts as needed.

If you find yourself applying the same [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) settings across multiple tables, consider wrapping them in a function. This ensures visual consistency and lets you update the theme in one place. The next page on [Premade Themes](premade-themes.md) shows exactly how this works with the `opt_*()` convenience methods, which are essentially pre-built theme functions that are included in **Great Tables**.


# A basic theme

Based on the sections above, we can design an overall theme for a table.

This requires setting a decent number of options, but it makes a big difference when presenting a table! Below is a table with a simple, blue theme. (The code is hidden by default, but can be expanded to see all the options set.)


Code

``` python
from great_tables import GT, exibble

# TODO: are there names we can give the three colors?
# e.g. primary = "#0076BA", etc..

(GT(exibble, rowname_col="row", groupname_col="group")
    .tab_header("THE HEADING", "(a subtitle)")
    .tab_stubhead("THE STUBHEAD")
    .tab_source_note("THE SOURCE NOTE")
    .tab_options(
        # table ----
        table_border_top_color="#004D80",
        table_border_bottom_color="#004D80",

        # heading ----
        heading_border_bottom_color="#0076BA",

        # column labels ----
        column_labels_border_top_color="#0076BA",
        column_labels_border_bottom_color="#0076BA",
        column_labels_background_color="#FFFFFF",

        # row group ----
        row_group_border_top_color="#0076BA",
        row_group_border_bottom_color="#0076BA",

        # stub ----
        stub_background_color="#0076BA",
        stub_border_style="solid",
        stub_border_color="#0076BA",

        # table body ----
        table_body_border_top_color="#0076BA",
        table_body_border_bottom_color="#0076BA",
        table_body_hlines_style="none",
        table_body_vlines_style="none",

        # misc ----
        #row_striping_background_color="#F4F4F4"
    )

)
```


<style>
#sxlqkfxaub table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sxlqkfxaub thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sxlqkfxaub p { margin: 0; padding: 0; }
 #sxlqkfxaub .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #004D80; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #004D80; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sxlqkfxaub .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sxlqkfxaub .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sxlqkfxaub .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sxlqkfxaub .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sxlqkfxaub .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #sxlqkfxaub .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sxlqkfxaub .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sxlqkfxaub .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sxlqkfxaub .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sxlqkfxaub .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sxlqkfxaub .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sxlqkfxaub .gt_spanner_row { border-bottom-style: hidden; }
 #sxlqkfxaub .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sxlqkfxaub .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: middle; }
 #sxlqkfxaub .gt_from_md> :first-child { margin-top: 0; }
 #sxlqkfxaub .gt_from_md> :last-child { margin-bottom: 0; }
 #sxlqkfxaub .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sxlqkfxaub .gt_stub { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #0076BA; padding-left: 5px; padding-right: 5px; }
 #sxlqkfxaub .gt_indent_1 { text-indent: 5px; }
 #sxlqkfxaub .gt_indent_2 { text-indent: calc(5px * 2); }
 #sxlqkfxaub .gt_indent_3 { text-indent: calc(5px * 3); }
 #sxlqkfxaub .gt_indent_4 { text-indent: calc(5px * 4); }
 #sxlqkfxaub .gt_indent_5 { text-indent: calc(5px * 5); }
 #sxlqkfxaub .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sxlqkfxaub .gt_row_group_first td { border-top-width: 2px; }
 #sxlqkfxaub .gt_row_group_first th { border-top-width: 2px; }
 #sxlqkfxaub .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sxlqkfxaub .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #sxlqkfxaub .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sxlqkfxaub .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sxlqkfxaub .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sxlqkfxaub .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sxlqkfxaub .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sxlqkfxaub .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sxlqkfxaub .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sxlqkfxaub .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sxlqkfxaub .gt_left { text-align: left; }
 #sxlqkfxaub .gt_center { text-align: center; }
 #sxlqkfxaub .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sxlqkfxaub .gt_font_normal { font-weight: normal; }
 #sxlqkfxaub .gt_font_bold { font-weight: bold; }
 #sxlqkfxaub .gt_font_italic { font-style: italic; }
 #sxlqkfxaub .gt_super { font-size: 65%; }
 #sxlqkfxaub .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sxlqkfxaub .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sxlqkfxaub .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sxlqkfxaub .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sxlqkfxaub .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sxlqkfxaub .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" aria-labelledby="title" aria-describedby="subtitle" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" id="title" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" id="subtitle" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
</tr>
<tr class="gt_col_headings">
<th id="THE-STUBHEAD" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">THE STUBHEAD</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
<th id="fctr" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">fctr</th>
<th id="date" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">date</th>
<th id="time" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">time</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="8" id="grp_a" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td id="stub-1" class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right" headers="grp_a stub-1 num">0.1111</td>
<td class="gt_row gt_left" headers="grp_a stub-1 char">apricot</td>
<td class="gt_row gt_left" headers="grp_a stub-1 fctr">one</td>
<td class="gt_row gt_right" headers="grp_a stub-1 date">2015-01-15</td>
<td class="gt_row gt_right" headers="grp_a stub-1 time">13:35</td>
<td class="gt_row gt_right" headers="grp_a stub-1 datetime">2018-01-01 02:22</td>
<td class="gt_row gt_right" headers="grp_a stub-1 currency">49.95</td>
</tr>
<tr>
<td id="stub-2" class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right" headers="grp_a stub-2 num">2.222</td>
<td class="gt_row gt_left" headers="grp_a stub-2 char">banana</td>
<td class="gt_row gt_left" headers="grp_a stub-2 fctr">two</td>
<td class="gt_row gt_right" headers="grp_a stub-2 date">2015-02-15</td>
<td class="gt_row gt_right" headers="grp_a stub-2 time">14:40</td>
<td class="gt_row gt_right" headers="grp_a stub-2 datetime">2018-02-02 14:33</td>
<td class="gt_row gt_right" headers="grp_a stub-2 currency">17.95</td>
</tr>
<tr>
<td id="stub-3" class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right" headers="grp_a stub-3 num">33.33</td>
<td class="gt_row gt_left" headers="grp_a stub-3 char">coconut</td>
<td class="gt_row gt_left" headers="grp_a stub-3 fctr">three</td>
<td class="gt_row gt_right" headers="grp_a stub-3 date">2015-03-15</td>
<td class="gt_row gt_right" headers="grp_a stub-3 time">15:45</td>
<td class="gt_row gt_right" headers="grp_a stub-3 datetime">2018-03-03 03:44</td>
<td class="gt_row gt_right" headers="grp_a stub-3 currency">1.39</td>
</tr>
<tr>
<td id="stub-4" class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right" headers="grp_a stub-4 num">444.4</td>
<td class="gt_row gt_left" headers="grp_a stub-4 char">durian</td>
<td class="gt_row gt_left" headers="grp_a stub-4 fctr">four</td>
<td class="gt_row gt_right" headers="grp_a stub-4 date">2015-04-15</td>
<td class="gt_row gt_right" headers="grp_a stub-4 time">16:50</td>
<td class="gt_row gt_right" headers="grp_a stub-4 datetime">2018-04-04 15:55</td>
<td class="gt_row gt_right" headers="grp_a stub-4 currency">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" id="grp_b" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td id="stub-5" class="gt_row gt_left gt_stub" scope="row">row_5</td>
<td class="gt_row gt_right" headers="grp_b stub-5 num">5550.0</td>
<td class="gt_row gt_left" headers="grp_b stub-5 char">None</td>
<td class="gt_row gt_left" headers="grp_b stub-5 fctr">five</td>
<td class="gt_row gt_right" headers="grp_b stub-5 date">2015-05-15</td>
<td class="gt_row gt_right" headers="grp_b stub-5 time">17:55</td>
<td class="gt_row gt_right" headers="grp_b stub-5 datetime">2018-05-05 04:00</td>
<td class="gt_row gt_right" headers="grp_b stub-5 currency">1325.81</td>
</tr>
<tr>
<td id="stub-6" class="gt_row gt_left gt_stub" scope="row">row_6</td>
<td class="gt_row gt_right" headers="grp_b stub-6 num">None</td>
<td class="gt_row gt_left" headers="grp_b stub-6 char">fig</td>
<td class="gt_row gt_left" headers="grp_b stub-6 fctr">six</td>
<td class="gt_row gt_right" headers="grp_b stub-6 date">2015-06-15</td>
<td class="gt_row gt_right" headers="grp_b stub-6 time">None</td>
<td class="gt_row gt_right" headers="grp_b stub-6 datetime">2018-06-06 16:11</td>
<td class="gt_row gt_right" headers="grp_b stub-6 currency">13.255</td>
</tr>
<tr>
<td id="stub-7" class="gt_row gt_left gt_stub" scope="row">row_7</td>
<td class="gt_row gt_right" headers="grp_b stub-7 num">777000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-7 char">grapefruit</td>
<td class="gt_row gt_left" headers="grp_b stub-7 fctr">seven</td>
<td class="gt_row gt_right" headers="grp_b stub-7 date">None</td>
<td class="gt_row gt_right" headers="grp_b stub-7 time">19:10</td>
<td class="gt_row gt_right" headers="grp_b stub-7 datetime">2018-07-07 05:22</td>
<td class="gt_row gt_right" headers="grp_b stub-7 currency">None</td>
</tr>
<tr>
<td id="stub-8" class="gt_row gt_left gt_stub" scope="row">row_8</td>
<td class="gt_row gt_right" headers="grp_b stub-8 num">8880000.0</td>
<td class="gt_row gt_left" headers="grp_b stub-8 char">honeydew</td>
<td class="gt_row gt_left" headers="grp_b stub-8 fctr">eight</td>
<td class="gt_row gt_right" headers="grp_b stub-8 date">2015-08-15</td>
<td class="gt_row gt_right" headers="grp_b stub-8 time">20:20</td>
<td class="gt_row gt_right" headers="grp_b stub-8 datetime">None</td>
<td class="gt_row gt_right" headers="grp_b stub-8 currency">0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="8" class="gt_sourcenote">THE SOURCE NOTE</td>
</tr>
</tfoot>

</table>


With [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options), you can define the visual identity of your tables at a broad level. The structured naming convention makes it straightforward to find and set the options you need, and by combining multiple options together, you can build reusable themes that give all your tables a consistent, polished appearance.
