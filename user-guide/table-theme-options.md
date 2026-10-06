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
#mizkkmdvbs table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mizkkmdvbs thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mizkkmdvbs p { margin: 0; padding: 0; }
 #mizkkmdvbs .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mizkkmdvbs .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mizkkmdvbs .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mizkkmdvbs .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mizkkmdvbs .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mizkkmdvbs .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mizkkmdvbs .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mizkkmdvbs .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mizkkmdvbs .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mizkkmdvbs .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mizkkmdvbs .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mizkkmdvbs .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mizkkmdvbs .gt_spanner_row { border-bottom-style: hidden; }
 #mizkkmdvbs .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mizkkmdvbs .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mizkkmdvbs .gt_from_md> :first-child { margin-top: 0; }
 #mizkkmdvbs .gt_from_md> :last-child { margin-bottom: 0; }
 #mizkkmdvbs .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mizkkmdvbs .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mizkkmdvbs .gt_indent_1 { text-indent: 5px; }
 #mizkkmdvbs .gt_indent_2 { text-indent: calc(5px * 2); }
 #mizkkmdvbs .gt_indent_3 { text-indent: calc(5px * 3); }
 #mizkkmdvbs .gt_indent_4 { text-indent: calc(5px * 4); }
 #mizkkmdvbs .gt_indent_5 { text-indent: calc(5px * 5); }
 #mizkkmdvbs .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mizkkmdvbs .gt_row_group_first td { border-top-width: 2px; }
 #mizkkmdvbs .gt_row_group_first th { border-top-width: 2px; }
 #mizkkmdvbs .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mizkkmdvbs .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mizkkmdvbs .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mizkkmdvbs .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #mizkkmdvbs .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mizkkmdvbs .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mizkkmdvbs .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mizkkmdvbs .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mizkkmdvbs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mizkkmdvbs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mizkkmdvbs .gt_left { text-align: left; }
 #mizkkmdvbs .gt_center { text-align: center; }
 #mizkkmdvbs .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mizkkmdvbs .gt_font_normal { font-weight: normal; }
 #mizkkmdvbs .gt_font_bold { font-weight: bold; }
 #mizkkmdvbs .gt_font_italic { font-style: italic; }
 #mizkkmdvbs .gt_super { font-size: 65%; }
 #mizkkmdvbs .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mizkkmdvbs .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #mizkkmdvbs .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mizkkmdvbs .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mizkkmdvbs .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mizkkmdvbs .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
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
<th colspan="8" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
<td class="gt_row gt_right">2015-01-15</td>
<td class="gt_row gt_right">13:35</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
<td class="gt_row gt_right">2015-02-15</td>
<td class="gt_row gt_right">14:40</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_left">three</td>
<td class="gt_row gt_right">2015-03-15</td>
<td class="gt_row gt_right">15:45</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_left">four</td>
<td class="gt_row gt_right">2015-04-15</td>
<td class="gt_row gt_right">16:50</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
<td class="gt_row gt_right">2015-05-15</td>
<td class="gt_row gt_right">17:55</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">66495.1</td>
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
#obqehawxot table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#obqehawxot thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#obqehawxot p { margin: 0; padding: 0; }
 #obqehawxot .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: lightblue; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #obqehawxot .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #obqehawxot .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: lightblue; border-bottom-width: 0; }
 #obqehawxot .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: lightblue; border-top-width: 0; }
 #obqehawxot .gt_heading { background-color: gold; text-align: center; border-bottom-color: lightblue; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #obqehawxot .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #obqehawxot .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #obqehawxot .gt_col_heading { color: #333333; background-color: aquamarine; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #obqehawxot .gt_column_spanner_outer { color: #333333; background-color: aquamarine; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #obqehawxot .gt_column_spanner_outer:first-child { padding-left: 0; }
 #obqehawxot .gt_column_spanner_outer:last-child { padding-right: 0; }
 #obqehawxot .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #obqehawxot .gt_spanner_row { border-bottom-style: hidden; }
 #obqehawxot .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: lightyellow; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #obqehawxot .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: lightyellow; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #obqehawxot .gt_from_md> :first-child { margin-top: 0; }
 #obqehawxot .gt_from_md> :last-child { margin-bottom: 0; }
 #obqehawxot .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #obqehawxot .gt_stub { color: #333333; background-color: lightgreen; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #obqehawxot .gt_indent_1 { text-indent: 5px; }
 #obqehawxot .gt_indent_2 { text-indent: calc(5px * 2); }
 #obqehawxot .gt_indent_3 { text-indent: calc(5px * 3); }
 #obqehawxot .gt_indent_4 { text-indent: calc(5px * 4); }
 #obqehawxot .gt_indent_5 { text-indent: calc(5px * 5); }
 #obqehawxot .gt_stub_row_group { color: #333333; background-color: lightblue; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #obqehawxot .gt_row_group_first td { border-top-width: 2px; }
 #obqehawxot .gt_row_group_first th { border-top-width: 2px; }
 #obqehawxot .gt_striped { color: #333333; background-color: #F4F4F4; }
 #obqehawxot .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #obqehawxot .gt_summary_row { color: #333333; background-color: lightblue; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #obqehawxot .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #obqehawxot .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #obqehawxot .gt_grand_summary_row { color: #333333; background-color: lightpink; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #obqehawxot .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #obqehawxot .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #obqehawxot .gt_sourcenotes { color: #333333; background-color: #f1e2af; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #obqehawxot .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #obqehawxot .gt_left { text-align: left; }
 #obqehawxot .gt_center { text-align: center; }
 #obqehawxot .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #obqehawxot .gt_font_normal { font-weight: normal; }
 #obqehawxot .gt_font_bold { font-weight: bold; }
 #obqehawxot .gt_font_italic { font-style: italic; }
 #obqehawxot .gt_super { font-size: 65%; }
 #obqehawxot .gt_footnotes { color: font-color(lightblue); background-color: lightblue; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #obqehawxot .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #obqehawxot .gt_sourcenotes { color: #333333; background-color: #f1e2af; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #obqehawxot .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #obqehawxot .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #obqehawxot .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
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
<th colspan="8" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
<td class="gt_row gt_right">2015-01-15</td>
<td class="gt_row gt_right">13:35</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
<td class="gt_row gt_right">2015-02-15</td>
<td class="gt_row gt_right">14:40</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_left">three</td>
<td class="gt_row gt_right">2015-03-15</td>
<td class="gt_row gt_right">15:45</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_left">four</td>
<td class="gt_row gt_right">2015-04-15</td>
<td class="gt_row gt_right">16:50</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
<td class="gt_row gt_right">2015-05-15</td>
<td class="gt_row gt_right">17:55</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">66495.1</td>
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
#ryzqhyxtpv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ryzqhyxtpv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ryzqhyxtpv p { margin: 0; padding: 0; }
 #ryzqhyxtpv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ryzqhyxtpv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ryzqhyxtpv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ryzqhyxtpv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ryzqhyxtpv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ryzqhyxtpv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ryzqhyxtpv .gt_col_headings { border-top-style: solid; border-top-width: 5px; border-top-color: blue; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ryzqhyxtpv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ryzqhyxtpv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ryzqhyxtpv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ryzqhyxtpv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ryzqhyxtpv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ryzqhyxtpv .gt_spanner_row { border-bottom-style: hidden; }
 #ryzqhyxtpv .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ryzqhyxtpv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ryzqhyxtpv .gt_from_md> :first-child { margin-top: 0; }
 #ryzqhyxtpv .gt_from_md> :last-child { margin-bottom: 0; }
 #ryzqhyxtpv .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ryzqhyxtpv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ryzqhyxtpv .gt_indent_1 { text-indent: 5px; }
 #ryzqhyxtpv .gt_indent_2 { text-indent: calc(5px * 2); }
 #ryzqhyxtpv .gt_indent_3 { text-indent: calc(5px * 3); }
 #ryzqhyxtpv .gt_indent_4 { text-indent: calc(5px * 4); }
 #ryzqhyxtpv .gt_indent_5 { text-indent: calc(5px * 5); }
 #ryzqhyxtpv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ryzqhyxtpv .gt_row_group_first td { border-top-width: 2px; }
 #ryzqhyxtpv .gt_row_group_first th { border-top-width: 2px; }
 #ryzqhyxtpv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ryzqhyxtpv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ryzqhyxtpv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ryzqhyxtpv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ryzqhyxtpv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ryzqhyxtpv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ryzqhyxtpv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ryzqhyxtpv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ryzqhyxtpv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ryzqhyxtpv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ryzqhyxtpv .gt_left { text-align: left; }
 #ryzqhyxtpv .gt_center { text-align: center; }
 #ryzqhyxtpv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ryzqhyxtpv .gt_font_normal { font-weight: normal; }
 #ryzqhyxtpv .gt_font_bold { font-weight: bold; }
 #ryzqhyxtpv .gt_font_italic { font-style: italic; }
 #ryzqhyxtpv .gt_super { font-size: 65%; }
 #ryzqhyxtpv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ryzqhyxtpv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ryzqhyxtpv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ryzqhyxtpv .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ryzqhyxtpv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ryzqhyxtpv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
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
<th colspan="8" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
<td class="gt_row gt_right">2015-01-15</td>
<td class="gt_row gt_right">13:35</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
<td class="gt_row gt_right">2015-02-15</td>
<td class="gt_row gt_right">14:40</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_left">three</td>
<td class="gt_row gt_right">2015-03-15</td>
<td class="gt_row gt_right">15:45</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_left">four</td>
<td class="gt_row gt_right">2015-04-15</td>
<td class="gt_row gt_right">16:50</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
<td class="gt_row gt_right">2015-05-15</td>
<td class="gt_row gt_right">17:55</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">66495.1</td>
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
#vvnwohtbfh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vvnwohtbfh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vvnwohtbfh p { margin: 0; padding: 0; }
 #vvnwohtbfh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vvnwohtbfh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vvnwohtbfh .gt_title { color: #FFFFFF; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vvnwohtbfh .gt_subtitle { color: #FFFFFF; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vvnwohtbfh .gt_heading { background-color: purple; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vvnwohtbfh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vvnwohtbfh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vvnwohtbfh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vvnwohtbfh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vvnwohtbfh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vvnwohtbfh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vvnwohtbfh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vvnwohtbfh .gt_spanner_row { border-bottom-style: hidden; }
 #vvnwohtbfh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vvnwohtbfh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vvnwohtbfh .gt_from_md> :first-child { margin-top: 0; }
 #vvnwohtbfh .gt_from_md> :last-child { margin-bottom: 0; }
 #vvnwohtbfh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vvnwohtbfh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vvnwohtbfh .gt_indent_1 { text-indent: 5px; }
 #vvnwohtbfh .gt_indent_2 { text-indent: calc(5px * 2); }
 #vvnwohtbfh .gt_indent_3 { text-indent: calc(5px * 3); }
 #vvnwohtbfh .gt_indent_4 { text-indent: calc(5px * 4); }
 #vvnwohtbfh .gt_indent_5 { text-indent: calc(5px * 5); }
 #vvnwohtbfh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vvnwohtbfh .gt_row_group_first td { border-top-width: 2px; }
 #vvnwohtbfh .gt_row_group_first th { border-top-width: 2px; }
 #vvnwohtbfh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vvnwohtbfh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vvnwohtbfh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vvnwohtbfh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #vvnwohtbfh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vvnwohtbfh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vvnwohtbfh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vvnwohtbfh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vvnwohtbfh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vvnwohtbfh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vvnwohtbfh .gt_left { text-align: left; }
 #vvnwohtbfh .gt_center { text-align: center; }
 #vvnwohtbfh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vvnwohtbfh .gt_font_normal { font-weight: normal; }
 #vvnwohtbfh .gt_font_bold { font-weight: bold; }
 #vvnwohtbfh .gt_font_italic { font-style: italic; }
 #vvnwohtbfh .gt_super { font-size: 65%; }
 #vvnwohtbfh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vvnwohtbfh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #vvnwohtbfh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vvnwohtbfh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vvnwohtbfh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vvnwohtbfh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
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
<th colspan="8" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
<td class="gt_row gt_right">2015-01-15</td>
<td class="gt_row gt_right">13:35</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
<td class="gt_row gt_right">2015-02-15</td>
<td class="gt_row gt_right">14:40</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_left">three</td>
<td class="gt_row gt_right">2015-03-15</td>
<td class="gt_row gt_right">15:45</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_left">four</td>
<td class="gt_row gt_right">2015-04-15</td>
<td class="gt_row gt_right">16:50</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
<td class="gt_row gt_right">2015-05-15</td>
<td class="gt_row gt_right">17:55</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">66495.1</td>
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
#cyznolryst table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cyznolryst thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cyznolryst p { margin: 0; padding: 0; }
 #cyznolryst .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cyznolryst .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cyznolryst .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cyznolryst .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cyznolryst .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cyznolryst .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cyznolryst .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cyznolryst .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cyznolryst .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cyznolryst .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cyznolryst .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cyznolryst .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cyznolryst .gt_spanner_row { border-bottom-style: hidden; }
 #cyznolryst .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cyznolryst .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cyznolryst .gt_from_md> :first-child { margin-top: 0; }
 #cyznolryst .gt_from_md> :last-child { margin-bottom: 0; }
 #cyznolryst .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: dashed; border-top-width: 4px; border-top-color: red; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cyznolryst .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cyznolryst .gt_indent_1 { text-indent: 5px; }
 #cyznolryst .gt_indent_2 { text-indent: calc(5px * 2); }
 #cyznolryst .gt_indent_3 { text-indent: calc(5px * 3); }
 #cyznolryst .gt_indent_4 { text-indent: calc(5px * 4); }
 #cyznolryst .gt_indent_5 { text-indent: calc(5px * 5); }
 #cyznolryst .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cyznolryst .gt_row_group_first td { border-top-width: 2px; }
 #cyznolryst .gt_row_group_first th { border-top-width: 2px; }
 #cyznolryst .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cyznolryst .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cyznolryst .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cyznolryst .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cyznolryst .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cyznolryst .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cyznolryst .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cyznolryst .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cyznolryst .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cyznolryst .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cyznolryst .gt_left { text-align: left; }
 #cyznolryst .gt_center { text-align: center; }
 #cyznolryst .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cyznolryst .gt_font_normal { font-weight: normal; }
 #cyznolryst .gt_font_bold { font-weight: bold; }
 #cyznolryst .gt_font_italic { font-style: italic; }
 #cyznolryst .gt_super { font-size: 65%; }
 #cyznolryst .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cyznolryst .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cyznolryst .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cyznolryst .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cyznolryst .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cyznolryst .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
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
<th colspan="8" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
<td class="gt_row gt_right">2015-01-15</td>
<td class="gt_row gt_right">13:35</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
<td class="gt_row gt_right">2015-02-15</td>
<td class="gt_row gt_right">14:40</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_left">three</td>
<td class="gt_row gt_right">2015-03-15</td>
<td class="gt_row gt_right">15:45</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_left">four</td>
<td class="gt_row gt_right">2015-04-15</td>
<td class="gt_row gt_right">16:50</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
<td class="gt_row gt_right">2015-05-15</td>
<td class="gt_row gt_right">17:55</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">66495.1</td>
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
#hwudnhjpmc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hwudnhjpmc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hwudnhjpmc p { margin: 0; padding: 0; }
 #hwudnhjpmc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hwudnhjpmc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hwudnhjpmc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hwudnhjpmc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hwudnhjpmc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hwudnhjpmc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hwudnhjpmc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hwudnhjpmc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hwudnhjpmc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hwudnhjpmc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hwudnhjpmc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hwudnhjpmc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hwudnhjpmc .gt_spanner_row { border-bottom-style: hidden; }
 #hwudnhjpmc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hwudnhjpmc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hwudnhjpmc .gt_from_md> :first-child { margin-top: 0; }
 #hwudnhjpmc .gt_from_md> :last-child { margin-bottom: 0; }
 #hwudnhjpmc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: solid; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: solid; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hwudnhjpmc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hwudnhjpmc .gt_indent_1 { text-indent: 5px; }
 #hwudnhjpmc .gt_indent_2 { text-indent: calc(5px * 2); }
 #hwudnhjpmc .gt_indent_3 { text-indent: calc(5px * 3); }
 #hwudnhjpmc .gt_indent_4 { text-indent: calc(5px * 4); }
 #hwudnhjpmc .gt_indent_5 { text-indent: calc(5px * 5); }
 #hwudnhjpmc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hwudnhjpmc .gt_row_group_first td { border-top-width: 2px; }
 #hwudnhjpmc .gt_row_group_first th { border-top-width: 2px; }
 #hwudnhjpmc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hwudnhjpmc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hwudnhjpmc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hwudnhjpmc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #hwudnhjpmc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hwudnhjpmc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hwudnhjpmc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hwudnhjpmc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hwudnhjpmc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hwudnhjpmc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hwudnhjpmc .gt_left { text-align: left; }
 #hwudnhjpmc .gt_center { text-align: center; }
 #hwudnhjpmc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hwudnhjpmc .gt_font_normal { font-weight: normal; }
 #hwudnhjpmc .gt_font_bold { font-weight: bold; }
 #hwudnhjpmc .gt_font_italic { font-style: italic; }
 #hwudnhjpmc .gt_super { font-size: 65%; }
 #hwudnhjpmc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hwudnhjpmc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #hwudnhjpmc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hwudnhjpmc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hwudnhjpmc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hwudnhjpmc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
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
<th colspan="8" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
<td class="gt_row gt_right">2015-01-15</td>
<td class="gt_row gt_right">13:35</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
<td class="gt_row gt_right">2015-02-15</td>
<td class="gt_row gt_right">14:40</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_left">three</td>
<td class="gt_row gt_right">2015-03-15</td>
<td class="gt_row gt_right">15:45</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_left">four</td>
<td class="gt_row gt_right">2015-04-15</td>
<td class="gt_row gt_right">16:50</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
<td class="gt_row gt_right">2015-05-15</td>
<td class="gt_row gt_right">17:55</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">66495.1</td>
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
#lzpzmexkyi table {
          font-family: 'Times New Roman';
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lzpzmexkyi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lzpzmexkyi p { margin: 0; padding: 0; }
 #lzpzmexkyi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #FFFFFF; font-size: 16px; font-weight: normal; font-style: italic; background-color: green; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lzpzmexkyi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lzpzmexkyi .gt_title { color: #FFFFFF; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: green; border-bottom-width: 0; }
 #lzpzmexkyi .gt_subtitle { color: #FFFFFF; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: green; border-top-width: 0; }
 #lzpzmexkyi .gt_heading { background-color: green; text-align: center; border-bottom-color: green; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lzpzmexkyi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lzpzmexkyi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lzpzmexkyi .gt_col_heading { color: #FFFFFF; background-color: green; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lzpzmexkyi .gt_column_spanner_outer { color: #FFFFFF; background-color: green; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lzpzmexkyi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lzpzmexkyi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lzpzmexkyi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lzpzmexkyi .gt_spanner_row { border-bottom-style: hidden; }
 #lzpzmexkyi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #FFFFFF; background-color: green; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lzpzmexkyi .gt_empty_group_heading { padding: 0.5px; color: #FFFFFF; background-color: green; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lzpzmexkyi .gt_from_md> :first-child { margin-top: 0; }
 #lzpzmexkyi .gt_from_md> :last-child { margin-bottom: 0; }
 #lzpzmexkyi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lzpzmexkyi .gt_stub { color: #FFFFFF; background-color: green; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lzpzmexkyi .gt_indent_1 { text-indent: 5px; }
 #lzpzmexkyi .gt_indent_2 { text-indent: calc(5px * 2); }
 #lzpzmexkyi .gt_indent_3 { text-indent: calc(5px * 3); }
 #lzpzmexkyi .gt_indent_4 { text-indent: calc(5px * 4); }
 #lzpzmexkyi .gt_indent_5 { text-indent: calc(5px * 5); }
 #lzpzmexkyi .gt_stub_row_group { color: #FFFFFF; background-color: green; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lzpzmexkyi .gt_row_group_first td { border-top-width: 2px; }
 #lzpzmexkyi .gt_row_group_first th { border-top-width: 2px; }
 #lzpzmexkyi .gt_striped { color: #00008B; background-color: #F4F4F4; }
 #lzpzmexkyi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lzpzmexkyi .gt_summary_row { color: #FFFFFF; background-color: green; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lzpzmexkyi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lzpzmexkyi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lzpzmexkyi .gt_grand_summary_row { color: #FFFFFF; background-color: green; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lzpzmexkyi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lzpzmexkyi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lzpzmexkyi .gt_sourcenotes { color: #FFFFFF; background-color: green; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lzpzmexkyi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lzpzmexkyi .gt_left { text-align: left; }
 #lzpzmexkyi .gt_center { text-align: center; }
 #lzpzmexkyi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lzpzmexkyi .gt_font_normal { font-weight: normal; }
 #lzpzmexkyi .gt_font_bold { font-weight: bold; }
 #lzpzmexkyi .gt_font_italic { font-style: italic; }
 #lzpzmexkyi .gt_super { font-size: 65%; }
 #lzpzmexkyi .gt_footnotes { color: font-color(green); background-color: green; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lzpzmexkyi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lzpzmexkyi .gt_sourcenotes { color: #FFFFFF; background-color: green; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lzpzmexkyi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lzpzmexkyi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lzpzmexkyi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
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
<th colspan="8" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
<td class="gt_row gt_right">2015-01-15</td>
<td class="gt_row gt_right">13:35</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
<td class="gt_row gt_right">2015-02-15</td>
<td class="gt_row gt_right">14:40</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_left">three</td>
<td class="gt_row gt_right">2015-03-15</td>
<td class="gt_row gt_right">15:45</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_left">four</td>
<td class="gt_row gt_right">2015-04-15</td>
<td class="gt_row gt_right">16:50</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
<td class="gt_row gt_right">2015-05-15</td>
<td class="gt_row gt_right">17:55</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">66495.1</td>
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
#htemeixiwp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#htemeixiwp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#htemeixiwp p { margin: 0; padding: 0; }
 #htemeixiwp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: orange; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #htemeixiwp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #htemeixiwp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: orange; border-bottom-width: 0; }
 #htemeixiwp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: orange; border-top-width: 0; }
 #htemeixiwp .gt_heading { background-color: pink; text-align: center; border-bottom-color: orange; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #htemeixiwp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #htemeixiwp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #htemeixiwp .gt_col_heading { color: #333333; background-color: orange; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #htemeixiwp .gt_column_spanner_outer { color: #333333; background-color: orange; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #htemeixiwp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #htemeixiwp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #htemeixiwp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #htemeixiwp .gt_spanner_row { border-bottom-style: hidden; }
 #htemeixiwp .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: orange; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #htemeixiwp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: orange; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #htemeixiwp .gt_from_md> :first-child { margin-top: 0; }
 #htemeixiwp .gt_from_md> :last-child { margin-bottom: 0; }
 #htemeixiwp .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #htemeixiwp .gt_stub { color: #333333; background-color: orange; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #htemeixiwp .gt_indent_1 { text-indent: 5px; }
 #htemeixiwp .gt_indent_2 { text-indent: calc(5px * 2); }
 #htemeixiwp .gt_indent_3 { text-indent: calc(5px * 3); }
 #htemeixiwp .gt_indent_4 { text-indent: calc(5px * 4); }
 #htemeixiwp .gt_indent_5 { text-indent: calc(5px * 5); }
 #htemeixiwp .gt_stub_row_group { color: #333333; background-color: orange; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #htemeixiwp .gt_row_group_first td { border-top-width: 2px; }
 #htemeixiwp .gt_row_group_first th { border-top-width: 2px; }
 #htemeixiwp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #htemeixiwp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #htemeixiwp .gt_summary_row { color: #333333; background-color: orange; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #htemeixiwp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #htemeixiwp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #htemeixiwp .gt_grand_summary_row { color: #333333; background-color: orange; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #htemeixiwp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #htemeixiwp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #htemeixiwp .gt_sourcenotes { color: #333333; background-color: orange; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #htemeixiwp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #htemeixiwp .gt_left { text-align: left; }
 #htemeixiwp .gt_center { text-align: center; }
 #htemeixiwp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #htemeixiwp .gt_font_normal { font-weight: normal; }
 #htemeixiwp .gt_font_bold { font-weight: bold; }
 #htemeixiwp .gt_font_italic { font-style: italic; }
 #htemeixiwp .gt_super { font-size: 65%; }
 #htemeixiwp .gt_footnotes { color: font-color(orange); background-color: orange; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #htemeixiwp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #htemeixiwp .gt_sourcenotes { color: #333333; background-color: orange; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #htemeixiwp .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #htemeixiwp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #htemeixiwp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
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
<th colspan="8" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
<td class="gt_row gt_right">2015-01-15</td>
<td class="gt_row gt_right">13:35</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
<td class="gt_row gt_right">2015-02-15</td>
<td class="gt_row gt_right">14:40</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_left">three</td>
<td class="gt_row gt_right">2015-03-15</td>
<td class="gt_row gt_right">15:45</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_left">four</td>
<td class="gt_row gt_right">2015-04-15</td>
<td class="gt_row gt_right">16:50</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
<td class="gt_row gt_right">2015-05-15</td>
<td class="gt_row gt_right">17:55</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_stub gt_grand_summary_row">GRAND SUMMARY ROW</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">6030.0631</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_left gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">---</td>
<td class="gt_first_grand_summary_row_bottom gt_row gt_right gt_grand_summary_row">66495.1</td>
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
#stderbqvwt table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#stderbqvwt thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#stderbqvwt p { margin: 0; padding: 0; }
 #stderbqvwt .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #004D80; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #004D80; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #stderbqvwt .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #stderbqvwt .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #stderbqvwt .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #stderbqvwt .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #stderbqvwt .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #stderbqvwt .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #stderbqvwt .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #stderbqvwt .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #stderbqvwt .gt_column_spanner_outer:first-child { padding-left: 0; }
 #stderbqvwt .gt_column_spanner_outer:last-child { padding-right: 0; }
 #stderbqvwt .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #stderbqvwt .gt_spanner_row { border-bottom-style: hidden; }
 #stderbqvwt .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #stderbqvwt .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: middle; }
 #stderbqvwt .gt_from_md> :first-child { margin-top: 0; }
 #stderbqvwt .gt_from_md> :last-child { margin-bottom: 0; }
 #stderbqvwt .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #stderbqvwt .gt_stub { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #0076BA; padding-left: 5px; padding-right: 5px; }
 #stderbqvwt .gt_indent_1 { text-indent: 5px; }
 #stderbqvwt .gt_indent_2 { text-indent: calc(5px * 2); }
 #stderbqvwt .gt_indent_3 { text-indent: calc(5px * 3); }
 #stderbqvwt .gt_indent_4 { text-indent: calc(5px * 4); }
 #stderbqvwt .gt_indent_5 { text-indent: calc(5px * 5); }
 #stderbqvwt .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #stderbqvwt .gt_row_group_first td { border-top-width: 2px; }
 #stderbqvwt .gt_row_group_first th { border-top-width: 2px; }
 #stderbqvwt .gt_striped { color: #333333; background-color: #F4F4F4; }
 #stderbqvwt .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #stderbqvwt .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #stderbqvwt .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #stderbqvwt .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #stderbqvwt .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #stderbqvwt .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #stderbqvwt .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #stderbqvwt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #stderbqvwt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #stderbqvwt .gt_left { text-align: left; }
 #stderbqvwt .gt_center { text-align: center; }
 #stderbqvwt .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #stderbqvwt .gt_font_normal { font-weight: normal; }
 #stderbqvwt .gt_font_bold { font-weight: bold; }
 #stderbqvwt .gt_font_italic { font-style: italic; }
 #stderbqvwt .gt_super { font-size: 65%; }
 #stderbqvwt .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #stderbqvwt .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #stderbqvwt .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #stderbqvwt .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #stderbqvwt .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #stderbqvwt .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_title gt_font_normal">THE HEADING</th>
</tr>
<tr class="gt_heading">
<th colspan="8" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">(a subtitle)</th>
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
<th colspan="8" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_left">apricot</td>
<td class="gt_row gt_left">one</td>
<td class="gt_row gt_right">2015-01-15</td>
<td class="gt_row gt_right">13:35</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_left">banana</td>
<td class="gt_row gt_left">two</td>
<td class="gt_row gt_right">2015-02-15</td>
<td class="gt_row gt_right">14:40</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
<td class="gt_row gt_left">three</td>
<td class="gt_row gt_right">2015-03-15</td>
<td class="gt_row gt_right">15:45</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_left">durian</td>
<td class="gt_row gt_left">four</td>
<td class="gt_row gt_right">2015-04-15</td>
<td class="gt_row gt_right">16:50</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="8" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_left">None</td>
<td class="gt_row gt_left">five</td>
<td class="gt_row gt_right">2015-05-15</td>
<td class="gt_row gt_right">17:55</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_6</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_left">fig</td>
<td class="gt_row gt_left">six</td>
<td class="gt_row gt_right">2015-06-15</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">2018-06-06 16:11</td>
<td class="gt_row gt_right">13.255</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_7</td>
<td class="gt_row gt_right">777000.0</td>
<td class="gt_row gt_left">grapefruit</td>
<td class="gt_row gt_left">seven</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">19:10</td>
<td class="gt_row gt_right">2018-07-07 05:22</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_8</td>
<td class="gt_row gt_right">8880000.0</td>
<td class="gt_row gt_left">honeydew</td>
<td class="gt_row gt_left">eight</td>
<td class="gt_row gt_right">2015-08-15</td>
<td class="gt_row gt_right">20:20</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">0.44</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="8" class="gt_sourcenote">THE SOURCE NOTE</td>
</tr>
</tfoot>

</table>


With [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options), you can define the visual identity of your tables at a broad level. The structured naming convention makes it straightforward to find and set the options you need, and by combining multiple options together, you can build reusable themes that give all your tables a consistent, polished appearance.
