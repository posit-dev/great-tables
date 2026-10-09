# Premade Themes

Building a complete table theme from scratch with [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) requires setting many individual options. For common styling needs, **Great Tables** offers a collection of `opt_*()` convenience methods that bundle these options into simple, one-line calls. This page demonstrates how to use premade themes and the various convenience methods available for quick table customization.

Premade themes are ideal for getting a polished look quickly, especially during exploratory work or when building dashboards where visual consistency matters more than pixel-perfect custom styling. For publication or brand-specific tables, you may want to start with a premade theme and then customize it further with [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) to match your exact requirements.

Great Tables provides convenience methods starting with `opt_` (e.g. [opt_row_striping()](../reference/GT.opt_row_striping.md#great_tables.GT.opt_row_striping)), as a shortcut for various styles that can be set via [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options).

There are two important kinds of `GT.opt_*()` methods:

- [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize): allows setting one of six premade table themes.
- The remaining `opt_*()` methods: shortcuts for common uses of [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options).

We'll use the basic GT object below for most examples, since it marks some of the table parts.


``` python
from great_tables import GT, exibble, md

lil_exibble = exibble.head(5)[["num", "char", "row", "group"]]

gt_ex = (
    GT(lil_exibble, rowname_col="row", groupname_col="group")
    .tab_header(
        title=md("Data listing from exibble"),
        subtitle=md("This is a **Great Tables** dataset."),
    )
    .tab_stubhead(label="row")
    .fmt_number(columns="num")
    .fmt_currency(columns="currency")
    .tab_source_note(source_note="This is only a portion of the dataset.")
    .opt_vertical_padding(scale=0.5)
)

gt_ex
```


<style>
#oqgrckchgd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oqgrckchgd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oqgrckchgd p { margin: 0; padding: 0; }
 #oqgrckchgd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oqgrckchgd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oqgrckchgd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oqgrckchgd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oqgrckchgd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oqgrckchgd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oqgrckchgd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oqgrckchgd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oqgrckchgd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oqgrckchgd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oqgrckchgd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oqgrckchgd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oqgrckchgd .gt_spanner_row { border-bottom-style: hidden; }
 #oqgrckchgd .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oqgrckchgd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #oqgrckchgd .gt_from_md> :first-child { margin-top: 0; }
 #oqgrckchgd .gt_from_md> :last-child { margin-bottom: 0; }
 #oqgrckchgd .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #oqgrckchgd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #oqgrckchgd .gt_indent_1 { text-indent: 5px; }
 #oqgrckchgd .gt_indent_2 { text-indent: calc(5px * 2); }
 #oqgrckchgd .gt_indent_3 { text-indent: calc(5px * 3); }
 #oqgrckchgd .gt_indent_4 { text-indent: calc(5px * 4); }
 #oqgrckchgd .gt_indent_5 { text-indent: calc(5px * 5); }
 #oqgrckchgd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oqgrckchgd .gt_row_group_first td { border-top-width: 2px; }
 #oqgrckchgd .gt_row_group_first th { border-top-width: 2px; }
 #oqgrckchgd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oqgrckchgd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oqgrckchgd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oqgrckchgd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oqgrckchgd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oqgrckchgd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oqgrckchgd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oqgrckchgd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oqgrckchgd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oqgrckchgd .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oqgrckchgd .gt_left { text-align: left; }
 #oqgrckchgd .gt_center { text-align: center; }
 #oqgrckchgd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oqgrckchgd .gt_font_normal { font-weight: normal; }
 #oqgrckchgd .gt_font_bold { font-weight: bold; }
 #oqgrckchgd .gt_font_italic { font-style: italic; }
 #oqgrckchgd .gt_super { font-size: 65%; }
 #oqgrckchgd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oqgrckchgd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oqgrckchgd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oqgrckchgd .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oqgrckchgd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oqgrckchgd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from exibble</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">This is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th id="row" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">row</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


# [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize): premade themes

Below are the first two premade styles. The first uses `color="blue"`, and the second uses `color="red"`.


``` python
gt_ex.opt_stylize(style=1, color="blue")
```


<style>
#qcazltxszh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qcazltxszh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qcazltxszh p { margin: 0; padding: 0; }
 #qcazltxszh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #004D80; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #004D80; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qcazltxszh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qcazltxszh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qcazltxszh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qcazltxszh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qcazltxszh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #qcazltxszh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qcazltxszh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qcazltxszh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qcazltxszh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qcazltxszh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qcazltxszh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qcazltxszh .gt_spanner_row { border-bottom-style: hidden; }
 #qcazltxszh .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qcazltxszh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: middle; }
 #qcazltxszh .gt_from_md> :first-child { margin-top: 0; }
 #qcazltxszh .gt_from_md> :last-child { margin-bottom: 0; }
 #qcazltxszh .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: none; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: none; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #qcazltxszh .gt_stub { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #0076BA; padding-left: 5px; padding-right: 5px; }
 #qcazltxszh .gt_indent_1 { text-indent: 5px; }
 #qcazltxszh .gt_indent_2 { text-indent: calc(5px * 2); }
 #qcazltxszh .gt_indent_3 { text-indent: calc(5px * 3); }
 #qcazltxszh .gt_indent_4 { text-indent: calc(5px * 4); }
 #qcazltxszh .gt_indent_5 { text-indent: calc(5px * 5); }
 #qcazltxszh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qcazltxszh .gt_row_group_first td { border-top-width: 2px; }
 #qcazltxszh .gt_row_group_first th { border-top-width: 2px; }
 #qcazltxszh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qcazltxszh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #qcazltxszh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qcazltxszh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qcazltxszh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qcazltxszh .gt_grand_summary_row { color: #333333; background-color: #89D3FE; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qcazltxszh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qcazltxszh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qcazltxszh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qcazltxszh .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qcazltxszh .gt_left { text-align: left; }
 #qcazltxszh .gt_center { text-align: center; }
 #qcazltxszh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qcazltxszh .gt_font_normal { font-weight: normal; }
 #qcazltxszh .gt_font_bold { font-weight: bold; }
 #qcazltxszh .gt_font_italic { font-style: italic; }
 #qcazltxszh .gt_super { font-size: 65%; }
 #qcazltxszh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qcazltxszh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qcazltxszh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qcazltxszh .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qcazltxszh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qcazltxszh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from exibble</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">This is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th id="row" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">row</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


``` python
gt_ex.opt_stylize(style=2, color="red")
```


<style>
#ldwcjwuitn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ldwcjwuitn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ldwcjwuitn p { margin: 0; padding: 0; }
 #ldwcjwuitn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #ldwcjwuitn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ldwcjwuitn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ldwcjwuitn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ldwcjwuitn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ldwcjwuitn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #ldwcjwuitn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ldwcjwuitn .gt_col_heading { color: #FFFFFF; background-color: #A81600; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ldwcjwuitn .gt_column_spanner_outer { color: #FFFFFF; background-color: #A81600; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ldwcjwuitn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ldwcjwuitn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ldwcjwuitn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ldwcjwuitn .gt_spanner_row { border-bottom-style: hidden; }
 #ldwcjwuitn .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ldwcjwuitn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #ldwcjwuitn .gt_from_md> :first-child { margin-top: 0; }
 #ldwcjwuitn .gt_from_md> :last-child { margin-bottom: 0; }
 #ldwcjwuitn .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #FFCCC7; border-left-style: solid; border-left-width: 1px; border-left-color: #FFCCC7; border-right-style: solid; border-right-width: 1px; border-right-color: #FFCCC7; vertical-align: middle; overflow-x: hidden; }
 #ldwcjwuitn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #5F5F5F; padding-left: 5px; padding-right: 5px; }
 #ldwcjwuitn .gt_indent_1 { text-indent: 5px; }
 #ldwcjwuitn .gt_indent_2 { text-indent: calc(5px * 2); }
 #ldwcjwuitn .gt_indent_3 { text-indent: calc(5px * 3); }
 #ldwcjwuitn .gt_indent_4 { text-indent: calc(5px * 4); }
 #ldwcjwuitn .gt_indent_5 { text-indent: calc(5px * 5); }
 #ldwcjwuitn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ldwcjwuitn .gt_row_group_first td { border-top-width: 2px; }
 #ldwcjwuitn .gt_row_group_first th { border-top-width: 2px; }
 #ldwcjwuitn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ldwcjwuitn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #ldwcjwuitn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ldwcjwuitn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ldwcjwuitn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ldwcjwuitn .gt_grand_summary_row { color: #FFFFFF; background-color: #FF644E; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ldwcjwuitn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ldwcjwuitn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ldwcjwuitn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ldwcjwuitn .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ldwcjwuitn .gt_left { text-align: left; }
 #ldwcjwuitn .gt_center { text-align: center; }
 #ldwcjwuitn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ldwcjwuitn .gt_font_normal { font-weight: normal; }
 #ldwcjwuitn .gt_font_bold { font-weight: bold; }
 #ldwcjwuitn .gt_font_italic { font-style: italic; }
 #ldwcjwuitn .gt_super { font-size: 65%; }
 #ldwcjwuitn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ldwcjwuitn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ldwcjwuitn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ldwcjwuitn .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ldwcjwuitn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ldwcjwuitn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from exibble</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">This is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th id="row" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">row</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


Notice that first table (blue) emphasizes the row labels with a solid background color. The second table (red) emphasizes the column labels, and uses solid lines to separate the body cell values. See [opt_stylize()](../reference/GT.opt_stylize.md#great_tables.GT.opt_stylize) for all available color options.

There are six styles available, each emphasizing different table parts. The `style=` values are numbered from `1` to `6`:

<style>
.shrink-example table {
    zoom: 60%;
}
</style>


1


<style>
#figwsyqpjc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#figwsyqpjc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#figwsyqpjc p { margin: 0; padding: 0; }
 #figwsyqpjc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #004D80; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #004D80; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #figwsyqpjc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #figwsyqpjc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #figwsyqpjc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #figwsyqpjc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #figwsyqpjc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #figwsyqpjc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #figwsyqpjc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #figwsyqpjc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #figwsyqpjc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #figwsyqpjc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #figwsyqpjc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #figwsyqpjc .gt_spanner_row { border-bottom-style: hidden; }
 #figwsyqpjc .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #figwsyqpjc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: middle; }
 #figwsyqpjc .gt_from_md> :first-child { margin-top: 0; }
 #figwsyqpjc .gt_from_md> :last-child { margin-bottom: 0; }
 #figwsyqpjc .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: none; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: none; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #figwsyqpjc .gt_stub { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #0076BA; padding-left: 5px; padding-right: 5px; }
 #figwsyqpjc .gt_indent_1 { text-indent: 5px; }
 #figwsyqpjc .gt_indent_2 { text-indent: calc(5px * 2); }
 #figwsyqpjc .gt_indent_3 { text-indent: calc(5px * 3); }
 #figwsyqpjc .gt_indent_4 { text-indent: calc(5px * 4); }
 #figwsyqpjc .gt_indent_5 { text-indent: calc(5px * 5); }
 #figwsyqpjc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #figwsyqpjc .gt_row_group_first td { border-top-width: 2px; }
 #figwsyqpjc .gt_row_group_first th { border-top-width: 2px; }
 #figwsyqpjc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #figwsyqpjc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #figwsyqpjc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #figwsyqpjc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #figwsyqpjc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #figwsyqpjc .gt_grand_summary_row { color: #333333; background-color: #89D3FE; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #figwsyqpjc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #figwsyqpjc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #figwsyqpjc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #figwsyqpjc .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #figwsyqpjc .gt_left { text-align: left; }
 #figwsyqpjc .gt_center { text-align: center; }
 #figwsyqpjc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #figwsyqpjc .gt_font_normal { font-weight: normal; }
 #figwsyqpjc .gt_font_bold { font-weight: bold; }
 #figwsyqpjc .gt_font_italic { font-style: italic; }
 #figwsyqpjc .gt_super { font-size: 65%; }
 #figwsyqpjc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #figwsyqpjc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #figwsyqpjc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #figwsyqpjc .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #figwsyqpjc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #figwsyqpjc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from exibble</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">This is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th id="row" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">row</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


2


<style>
#cxtqboeeps table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cxtqboeeps thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cxtqboeeps p { margin: 0; padding: 0; }
 #cxtqboeeps .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #cxtqboeeps .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cxtqboeeps .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cxtqboeeps .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cxtqboeeps .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cxtqboeeps .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #cxtqboeeps .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cxtqboeeps .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cxtqboeeps .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cxtqboeeps .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cxtqboeeps .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cxtqboeeps .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cxtqboeeps .gt_spanner_row { border-bottom-style: hidden; }
 #cxtqboeeps .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cxtqboeeps .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #cxtqboeeps .gt_from_md> :first-child { margin-top: 0; }
 #cxtqboeeps .gt_from_md> :last-child { margin-bottom: 0; }
 #cxtqboeeps .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: solid; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: solid; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #cxtqboeeps .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #5F5F5F; padding-left: 5px; padding-right: 5px; }
 #cxtqboeeps .gt_indent_1 { text-indent: 5px; }
 #cxtqboeeps .gt_indent_2 { text-indent: calc(5px * 2); }
 #cxtqboeeps .gt_indent_3 { text-indent: calc(5px * 3); }
 #cxtqboeeps .gt_indent_4 { text-indent: calc(5px * 4); }
 #cxtqboeeps .gt_indent_5 { text-indent: calc(5px * 5); }
 #cxtqboeeps .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cxtqboeeps .gt_row_group_first td { border-top-width: 2px; }
 #cxtqboeeps .gt_row_group_first th { border-top-width: 2px; }
 #cxtqboeeps .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cxtqboeeps .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #cxtqboeeps .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cxtqboeeps .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #cxtqboeeps .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cxtqboeeps .gt_grand_summary_row { color: #FFFFFF; background-color: #00A1FF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cxtqboeeps .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cxtqboeeps .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cxtqboeeps .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cxtqboeeps .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cxtqboeeps .gt_left { text-align: left; }
 #cxtqboeeps .gt_center { text-align: center; }
 #cxtqboeeps .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cxtqboeeps .gt_font_normal { font-weight: normal; }
 #cxtqboeeps .gt_font_bold { font-weight: bold; }
 #cxtqboeeps .gt_font_italic { font-style: italic; }
 #cxtqboeeps .gt_super { font-size: 65%; }
 #cxtqboeeps .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cxtqboeeps .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #cxtqboeeps .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cxtqboeeps .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cxtqboeeps .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cxtqboeeps .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from exibble</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">This is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th id="row" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">row</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


3


<style>
#bdiapsyzyk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bdiapsyzyk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bdiapsyzyk p { margin: 0; padding: 0; }
 #bdiapsyzyk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bdiapsyzyk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bdiapsyzyk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bdiapsyzyk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bdiapsyzyk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bdiapsyzyk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; }
 #bdiapsyzyk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bdiapsyzyk .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bdiapsyzyk .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bdiapsyzyk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bdiapsyzyk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bdiapsyzyk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bdiapsyzyk .gt_spanner_row { border-bottom-style: hidden; }
 #bdiapsyzyk .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bdiapsyzyk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; vertical-align: middle; }
 #bdiapsyzyk .gt_from_md> :first-child { margin-top: 0; }
 #bdiapsyzyk .gt_from_md> :last-child { margin-bottom: 0; }
 #bdiapsyzyk .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: dashed; border-top-width: 1px; border-top-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #929292; border-right-style: none; border-right-width: 1px; border-right-color: #929292; vertical-align: middle; overflow-x: hidden; }
 #bdiapsyzyk .gt_stub { color: #333333; background-color: #D5D5D5; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: none; border-right-width: 2px; border-right-color: #FFFFFF; padding-left: 5px; padding-right: 5px; }
 #bdiapsyzyk .gt_indent_1 { text-indent: 5px; }
 #bdiapsyzyk .gt_indent_2 { text-indent: calc(5px * 2); }
 #bdiapsyzyk .gt_indent_3 { text-indent: calc(5px * 3); }
 #bdiapsyzyk .gt_indent_4 { text-indent: calc(5px * 4); }
 #bdiapsyzyk .gt_indent_5 { text-indent: calc(5px * 5); }
 #bdiapsyzyk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bdiapsyzyk .gt_row_group_first td { border-top-width: 2px; }
 #bdiapsyzyk .gt_row_group_first th { border-top-width: 2px; }
 #bdiapsyzyk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bdiapsyzyk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; }
 #bdiapsyzyk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bdiapsyzyk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bdiapsyzyk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bdiapsyzyk .gt_grand_summary_row { color: #333333; background-color: #D5D5D5; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bdiapsyzyk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bdiapsyzyk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bdiapsyzyk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bdiapsyzyk .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bdiapsyzyk .gt_left { text-align: left; }
 #bdiapsyzyk .gt_center { text-align: center; }
 #bdiapsyzyk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bdiapsyzyk .gt_font_normal { font-weight: normal; }
 #bdiapsyzyk .gt_font_bold { font-weight: bold; }
 #bdiapsyzyk .gt_font_italic { font-style: italic; }
 #bdiapsyzyk .gt_super { font-size: 65%; }
 #bdiapsyzyk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bdiapsyzyk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bdiapsyzyk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bdiapsyzyk .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bdiapsyzyk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bdiapsyzyk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from exibble</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">This is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th id="row" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">row</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


4


<style>
#gshhsgivie table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gshhsgivie thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gshhsgivie p { margin: 0; padding: 0; }
 #gshhsgivie .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #gshhsgivie .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gshhsgivie .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gshhsgivie .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gshhsgivie .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gshhsgivie .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #gshhsgivie .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gshhsgivie .gt_col_heading { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gshhsgivie .gt_column_spanner_outer { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gshhsgivie .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gshhsgivie .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gshhsgivie .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gshhsgivie .gt_spanner_row { border-bottom-style: hidden; }
 #gshhsgivie .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gshhsgivie .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #gshhsgivie .gt_from_md> :first-child { margin-top: 0; }
 #gshhsgivie .gt_from_md> :last-child { margin-bottom: 0; }
 #gshhsgivie .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: dashed; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: dashed; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: dashed; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #gshhsgivie .gt_stub { color: #FFFFFF; background-color: #929292; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: dashed; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #gshhsgivie .gt_indent_1 { text-indent: 5px; }
 #gshhsgivie .gt_indent_2 { text-indent: calc(5px * 2); }
 #gshhsgivie .gt_indent_3 { text-indent: calc(5px * 3); }
 #gshhsgivie .gt_indent_4 { text-indent: calc(5px * 4); }
 #gshhsgivie .gt_indent_5 { text-indent: calc(5px * 5); }
 #gshhsgivie .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gshhsgivie .gt_row_group_first td { border-top-width: 2px; }
 #gshhsgivie .gt_row_group_first th { border-top-width: 2px; }
 #gshhsgivie .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gshhsgivie .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #gshhsgivie .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gshhsgivie .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gshhsgivie .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gshhsgivie .gt_grand_summary_row { color: #FFFFFF; background-color: #0076BA; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gshhsgivie .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gshhsgivie .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gshhsgivie .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gshhsgivie .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gshhsgivie .gt_left { text-align: left; }
 #gshhsgivie .gt_center { text-align: center; }
 #gshhsgivie .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gshhsgivie .gt_font_normal { font-weight: normal; }
 #gshhsgivie .gt_font_bold { font-weight: bold; }
 #gshhsgivie .gt_font_italic { font-style: italic; }
 #gshhsgivie .gt_super { font-size: 65%; }
 #gshhsgivie .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gshhsgivie .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gshhsgivie .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gshhsgivie .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gshhsgivie .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gshhsgivie .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from exibble</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">This is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th id="row" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">row</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


5


<style>
#gcwqbtdiqa table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#gcwqbtdiqa thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#gcwqbtdiqa p { margin: 0; padding: 0; }
 #gcwqbtdiqa .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #gcwqbtdiqa .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #gcwqbtdiqa .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #gcwqbtdiqa .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #gcwqbtdiqa .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gcwqbtdiqa .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #gcwqbtdiqa .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #gcwqbtdiqa .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #gcwqbtdiqa .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #gcwqbtdiqa .gt_column_spanner_outer:first-child { padding-left: 0; }
 #gcwqbtdiqa .gt_column_spanner_outer:last-child { padding-right: 0; }
 #gcwqbtdiqa .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #gcwqbtdiqa .gt_spanner_row { border-bottom-style: hidden; }
 #gcwqbtdiqa .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #gcwqbtdiqa .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #gcwqbtdiqa .gt_from_md> :first-child { margin-top: 0; }
 #gcwqbtdiqa .gt_from_md> :last-child { margin-bottom: 0; }
 #gcwqbtdiqa .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: solid; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: solid; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #gcwqbtdiqa .gt_stub { color: #FFFFFF; background-color: #929292; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #gcwqbtdiqa .gt_indent_1 { text-indent: 5px; }
 #gcwqbtdiqa .gt_indent_2 { text-indent: calc(5px * 2); }
 #gcwqbtdiqa .gt_indent_3 { text-indent: calc(5px * 3); }
 #gcwqbtdiqa .gt_indent_4 { text-indent: calc(5px * 4); }
 #gcwqbtdiqa .gt_indent_5 { text-indent: calc(5px * 5); }
 #gcwqbtdiqa .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #gcwqbtdiqa .gt_row_group_first td { border-top-width: 2px; }
 #gcwqbtdiqa .gt_row_group_first th { border-top-width: 2px; }
 #gcwqbtdiqa .gt_striped { color: #333333; background-color: #F4F4F4; }
 #gcwqbtdiqa .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #gcwqbtdiqa .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gcwqbtdiqa .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #gcwqbtdiqa .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #gcwqbtdiqa .gt_grand_summary_row { color: #FFFFFF; background-color: #929292; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #gcwqbtdiqa .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #gcwqbtdiqa .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #gcwqbtdiqa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gcwqbtdiqa .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gcwqbtdiqa .gt_left { text-align: left; }
 #gcwqbtdiqa .gt_center { text-align: center; }
 #gcwqbtdiqa .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #gcwqbtdiqa .gt_font_normal { font-weight: normal; }
 #gcwqbtdiqa .gt_font_bold { font-weight: bold; }
 #gcwqbtdiqa .gt_font_italic { font-style: italic; }
 #gcwqbtdiqa .gt_super { font-size: 65%; }
 #gcwqbtdiqa .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gcwqbtdiqa .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #gcwqbtdiqa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #gcwqbtdiqa .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #gcwqbtdiqa .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #gcwqbtdiqa .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from exibble</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">This is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th id="row" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">row</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


6


<style>
#qjbndpgito table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qjbndpgito thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qjbndpgito p { margin: 0; padding: 0; }
 #qjbndpgito .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qjbndpgito .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qjbndpgito .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qjbndpgito .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qjbndpgito .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qjbndpgito .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; }
 #qjbndpgito .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qjbndpgito .gt_col_heading { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qjbndpgito .gt_column_spanner_outer { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qjbndpgito .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qjbndpgito .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qjbndpgito .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qjbndpgito .gt_spanner_row { border-bottom-style: hidden; }
 #qjbndpgito .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qjbndpgito .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; vertical-align: middle; }
 #qjbndpgito .gt_from_md> :first-child { margin-top: 0; }
 #qjbndpgito .gt_from_md> :last-child { margin-bottom: 0; }
 #qjbndpgito .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: none; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #qjbndpgito .gt_stub { color: #333333; background-color: #89D3FE; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #qjbndpgito .gt_indent_1 { text-indent: 5px; }
 #qjbndpgito .gt_indent_2 { text-indent: calc(5px * 2); }
 #qjbndpgito .gt_indent_3 { text-indent: calc(5px * 3); }
 #qjbndpgito .gt_indent_4 { text-indent: calc(5px * 4); }
 #qjbndpgito .gt_indent_5 { text-indent: calc(5px * 5); }
 #qjbndpgito .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qjbndpgito .gt_row_group_first td { border-top-width: 2px; }
 #qjbndpgito .gt_row_group_first th { border-top-width: 2px; }
 #qjbndpgito .gt_striped { color: #333333; background-color: #EDF7FC; }
 #qjbndpgito .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; }
 #qjbndpgito .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qjbndpgito .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qjbndpgito .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qjbndpgito .gt_grand_summary_row { color: #333333; background-color: #D5D5D5; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qjbndpgito .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qjbndpgito .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qjbndpgito .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qjbndpgito .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qjbndpgito .gt_left { text-align: left; }
 #qjbndpgito .gt_center { text-align: center; }
 #qjbndpgito .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qjbndpgito .gt_font_normal { font-weight: normal; }
 #qjbndpgito .gt_font_bold { font-weight: bold; }
 #qjbndpgito .gt_font_italic { font-style: italic; }
 #qjbndpgito .gt_super { font-size: 65%; }
 #qjbndpgito .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qjbndpgito .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qjbndpgito .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qjbndpgito .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qjbndpgito .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qjbndpgito .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from exibble</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">This is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th id="row" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">row</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


When choosing a style, consider your audience and context. Styles 1 and 2 emphasize structure through color, making table regions visually distinct. Styles 3 and 4 use lines and shading for a more traditional look. Styles 5 and 6 are more minimal, relying on subtle separation. Heavier styling works well for standalone presentations, while lighter styling is better suited for tables embedded in text-heavy reports where the table should complement rather than dominate the page.


# `opt_*()` convenience methods

This section shows the different `opt_*()` methods available. They serve as convenience methods for common [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) tasks.


## Align table header


``` python
gt_ex.opt_align_table_header(align="left")
```


<style>
#koxjdpfixe table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#koxjdpfixe thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#koxjdpfixe p { margin: 0; padding: 0; }
 #koxjdpfixe .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #koxjdpfixe .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #koxjdpfixe .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #koxjdpfixe .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #koxjdpfixe .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #koxjdpfixe .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #koxjdpfixe .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #koxjdpfixe .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #koxjdpfixe .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #koxjdpfixe .gt_column_spanner_outer:first-child { padding-left: 0; }
 #koxjdpfixe .gt_column_spanner_outer:last-child { padding-right: 0; }
 #koxjdpfixe .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #koxjdpfixe .gt_spanner_row { border-bottom-style: hidden; }
 #koxjdpfixe .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #koxjdpfixe .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #koxjdpfixe .gt_from_md> :first-child { margin-top: 0; }
 #koxjdpfixe .gt_from_md> :last-child { margin-bottom: 0; }
 #koxjdpfixe .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #koxjdpfixe .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #koxjdpfixe .gt_indent_1 { text-indent: 5px; }
 #koxjdpfixe .gt_indent_2 { text-indent: calc(5px * 2); }
 #koxjdpfixe .gt_indent_3 { text-indent: calc(5px * 3); }
 #koxjdpfixe .gt_indent_4 { text-indent: calc(5px * 4); }
 #koxjdpfixe .gt_indent_5 { text-indent: calc(5px * 5); }
 #koxjdpfixe .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #koxjdpfixe .gt_row_group_first td { border-top-width: 2px; }
 #koxjdpfixe .gt_row_group_first th { border-top-width: 2px; }
 #koxjdpfixe .gt_striped { color: #333333; background-color: #F4F4F4; }
 #koxjdpfixe .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #koxjdpfixe .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #koxjdpfixe .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #koxjdpfixe .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #koxjdpfixe .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #koxjdpfixe .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #koxjdpfixe .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #koxjdpfixe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #koxjdpfixe .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #koxjdpfixe .gt_left { text-align: left; }
 #koxjdpfixe .gt_center { text-align: center; }
 #koxjdpfixe .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #koxjdpfixe .gt_font_normal { font-weight: normal; }
 #koxjdpfixe .gt_font_bold { font-weight: bold; }
 #koxjdpfixe .gt_font_italic { font-style: italic; }
 #koxjdpfixe .gt_super { font-size: 65%; }
 #koxjdpfixe .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #koxjdpfixe .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #koxjdpfixe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #koxjdpfixe .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #koxjdpfixe .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #koxjdpfixe .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from exibble</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">This is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th id="row" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">row</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


The title and subtitle are now left-aligned rather than centered, which works well for tables embedded in text-heavy documents.


## Make text ALL CAPS


``` python
gt_ex.opt_all_caps()
```


<style>
#xumtecfgal table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xumtecfgal thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xumtecfgal p { margin: 0; padding: 0; }
 #xumtecfgal .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xumtecfgal .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xumtecfgal .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xumtecfgal .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xumtecfgal .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xumtecfgal .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xumtecfgal .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xumtecfgal .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xumtecfgal .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xumtecfgal .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xumtecfgal .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xumtecfgal .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xumtecfgal .gt_spanner_row { border-bottom-style: hidden; }
 #xumtecfgal .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xumtecfgal .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xumtecfgal .gt_from_md> :first-child { margin-top: 0; }
 #xumtecfgal .gt_from_md> :last-child { margin-bottom: 0; }
 #xumtecfgal .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xumtecfgal .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xumtecfgal .gt_indent_1 { text-indent: 5px; }
 #xumtecfgal .gt_indent_2 { text-indent: calc(5px * 2); }
 #xumtecfgal .gt_indent_3 { text-indent: calc(5px * 3); }
 #xumtecfgal .gt_indent_4 { text-indent: calc(5px * 4); }
 #xumtecfgal .gt_indent_5 { text-indent: calc(5px * 5); }
 #xumtecfgal .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xumtecfgal .gt_row_group_first td { border-top-width: 2px; }
 #xumtecfgal .gt_row_group_first th { border-top-width: 2px; }
 #xumtecfgal .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xumtecfgal .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xumtecfgal .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xumtecfgal .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xumtecfgal .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xumtecfgal .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xumtecfgal .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xumtecfgal .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xumtecfgal .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xumtecfgal .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xumtecfgal .gt_left { text-align: left; }
 #xumtecfgal .gt_center { text-align: center; }
 #xumtecfgal .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xumtecfgal .gt_font_normal { font-weight: normal; }
 #xumtecfgal .gt_font_bold { font-weight: bold; }
 #xumtecfgal .gt_font_italic { font-style: italic; }
 #xumtecfgal .gt_super { font-size: 65%; }
 #xumtecfgal .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xumtecfgal .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xumtecfgal .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xumtecfgal .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xumtecfgal .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xumtecfgal .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from exibble</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">This is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th id="row" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">row</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


Column labels and row group labels are rendered in uppercase, giving the table a more formal, structured appearance.


## Reduce or expand padding


``` python
gt_ex.opt_vertical_padding(scale=0.3)
```


<style>
#bbbqhgagcd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bbbqhgagcd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bbbqhgagcd p { margin: 0; padding: 0; }
 #bbbqhgagcd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bbbqhgagcd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bbbqhgagcd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bbbqhgagcd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: -0.4px; padding-bottom: 1.6px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bbbqhgagcd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bbbqhgagcd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bbbqhgagcd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bbbqhgagcd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 0.75px; padding-bottom: 1.6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bbbqhgagcd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bbbqhgagcd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bbbqhgagcd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bbbqhgagcd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 0.75px; padding-bottom: 0.75px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bbbqhgagcd .gt_spanner_row { border-bottom-style: hidden; }
 #bbbqhgagcd .gt_group_heading { padding-top: 1.2px; padding-bottom: 1.2px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bbbqhgagcd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bbbqhgagcd .gt_from_md> :first-child { margin-top: 0; }
 #bbbqhgagcd .gt_from_md> :last-child { margin-bottom: 0; }
 #bbbqhgagcd .gt_row { padding-top: 1.2px; padding-bottom: 1.2px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bbbqhgagcd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bbbqhgagcd .gt_indent_1 { text-indent: 5px; }
 #bbbqhgagcd .gt_indent_2 { text-indent: calc(5px * 2); }
 #bbbqhgagcd .gt_indent_3 { text-indent: calc(5px * 3); }
 #bbbqhgagcd .gt_indent_4 { text-indent: calc(5px * 4); }
 #bbbqhgagcd .gt_indent_5 { text-indent: calc(5px * 5); }
 #bbbqhgagcd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bbbqhgagcd .gt_row_group_first td { border-top-width: 2px; }
 #bbbqhgagcd .gt_row_group_first th { border-top-width: 2px; }
 #bbbqhgagcd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bbbqhgagcd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bbbqhgagcd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bbbqhgagcd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bbbqhgagcd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bbbqhgagcd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bbbqhgagcd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bbbqhgagcd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bbbqhgagcd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bbbqhgagcd .gt_sourcenote { font-size: 90%; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bbbqhgagcd .gt_left { text-align: left; }
 #bbbqhgagcd .gt_center { text-align: center; }
 #bbbqhgagcd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bbbqhgagcd .gt_font_normal { font-weight: normal; }
 #bbbqhgagcd .gt_font_bold { font-weight: bold; }
 #bbbqhgagcd .gt_font_italic { font-style: italic; }
 #bbbqhgagcd .gt_super { font-size: 65%; }
 #bbbqhgagcd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bbbqhgagcd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bbbqhgagcd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bbbqhgagcd .gt_sourcenote { font-size: 90%; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bbbqhgagcd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bbbqhgagcd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from exibble</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">This is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th id="row" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">row</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


Reducing vertical padding creates a more compact table that fits more data into less vertical space.


``` python
gt_ex.opt_horizontal_padding(scale=3)
```


<style>
#tywpspdwoo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tywpspdwoo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tywpspdwoo p { margin: 0; padding: 0; }
 #tywpspdwoo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tywpspdwoo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tywpspdwoo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tywpspdwoo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 15px; padding-right: 15px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tywpspdwoo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tywpspdwoo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tywpspdwoo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tywpspdwoo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 15px; padding-right: 15px; overflow-x: hidden; }
 #tywpspdwoo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tywpspdwoo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tywpspdwoo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tywpspdwoo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tywpspdwoo .gt_spanner_row { border-bottom-style: hidden; }
 #tywpspdwoo .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tywpspdwoo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tywpspdwoo .gt_from_md> :first-child { margin-top: 0; }
 #tywpspdwoo .gt_from_md> :last-child { margin-bottom: 0; }
 #tywpspdwoo .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tywpspdwoo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 15px; padding-right: 15px; }
 #tywpspdwoo .gt_indent_1 { text-indent: 5px; }
 #tywpspdwoo .gt_indent_2 { text-indent: calc(5px * 2); }
 #tywpspdwoo .gt_indent_3 { text-indent: calc(5px * 3); }
 #tywpspdwoo .gt_indent_4 { text-indent: calc(5px * 4); }
 #tywpspdwoo .gt_indent_5 { text-indent: calc(5px * 5); }
 #tywpspdwoo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 15px; padding-right: 15px; vertical-align: top; }
 #tywpspdwoo .gt_row_group_first td { border-top-width: 2px; }
 #tywpspdwoo .gt_row_group_first th { border-top-width: 2px; }
 #tywpspdwoo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tywpspdwoo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tywpspdwoo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tywpspdwoo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #tywpspdwoo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tywpspdwoo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tywpspdwoo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tywpspdwoo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tywpspdwoo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tywpspdwoo .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #tywpspdwoo .gt_left { text-align: left; }
 #tywpspdwoo .gt_center { text-align: center; }
 #tywpspdwoo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tywpspdwoo .gt_font_normal { font-weight: normal; }
 #tywpspdwoo .gt_font_bold { font-weight: bold; }
 #tywpspdwoo .gt_font_italic { font-style: italic; }
 #tywpspdwoo .gt_super { font-size: 65%; }
 #tywpspdwoo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tywpspdwoo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #tywpspdwoo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tywpspdwoo .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #tywpspdwoo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tywpspdwoo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from exibble</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">This is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th id="row" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">row</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


Increasing horizontal padding adds breathing room between columns, which improves readability when columns contain long values.


## Set table outline


``` python
gt_ex.opt_table_outline()
```


<style>
#sfsvrpsfrf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sfsvrpsfrf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sfsvrpsfrf p { margin: 0; padding: 0; }
 #sfsvrpsfrf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D3D3D3; border-right-style: solid; border-right-width: 3px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D3D3D3; border-left-style: solid; border-left-width: 3px; border-left-color: #D3D3D3; }
 #sfsvrpsfrf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sfsvrpsfrf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sfsvrpsfrf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sfsvrpsfrf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sfsvrpsfrf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sfsvrpsfrf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sfsvrpsfrf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sfsvrpsfrf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sfsvrpsfrf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sfsvrpsfrf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sfsvrpsfrf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sfsvrpsfrf .gt_spanner_row { border-bottom-style: hidden; }
 #sfsvrpsfrf .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sfsvrpsfrf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sfsvrpsfrf .gt_from_md> :first-child { margin-top: 0; }
 #sfsvrpsfrf .gt_from_md> :last-child { margin-bottom: 0; }
 #sfsvrpsfrf .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sfsvrpsfrf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sfsvrpsfrf .gt_indent_1 { text-indent: 5px; }
 #sfsvrpsfrf .gt_indent_2 { text-indent: calc(5px * 2); }
 #sfsvrpsfrf .gt_indent_3 { text-indent: calc(5px * 3); }
 #sfsvrpsfrf .gt_indent_4 { text-indent: calc(5px * 4); }
 #sfsvrpsfrf .gt_indent_5 { text-indent: calc(5px * 5); }
 #sfsvrpsfrf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sfsvrpsfrf .gt_row_group_first td { border-top-width: 2px; }
 #sfsvrpsfrf .gt_row_group_first th { border-top-width: 2px; }
 #sfsvrpsfrf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sfsvrpsfrf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sfsvrpsfrf .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sfsvrpsfrf .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sfsvrpsfrf .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sfsvrpsfrf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sfsvrpsfrf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sfsvrpsfrf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sfsvrpsfrf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sfsvrpsfrf .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sfsvrpsfrf .gt_left { text-align: left; }
 #sfsvrpsfrf .gt_center { text-align: center; }
 #sfsvrpsfrf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sfsvrpsfrf .gt_font_normal { font-weight: normal; }
 #sfsvrpsfrf .gt_font_bold { font-weight: bold; }
 #sfsvrpsfrf .gt_font_italic { font-style: italic; }
 #sfsvrpsfrf .gt_super { font-size: 65%; }
 #sfsvrpsfrf .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sfsvrpsfrf .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sfsvrpsfrf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sfsvrpsfrf .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sfsvrpsfrf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sfsvrpsfrf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Data listing from exibble</th>
</tr>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">This is a <strong>Great Tables</strong> dataset.</th>
</tr>
<tr class="gt_col_headings">
<th id="row" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">row</th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" scope="col">num</th>
<th id="char" class="gt_col_heading gt_columns_bottom_border gt_left" scope="col">char</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<th colspan="3" class="gt_group_heading">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub">row_5</td>
<td class="gt_row gt_right">5,550.00</td>
<td class="gt_row gt_left">None</td>
</tr>
</tbody><tfoot>
<tr class="gt_sourcenotes">
<td colspan="3" class="gt_sourcenote">This is only a portion of the dataset.</td>
</tr>
</tfoot>

</table>


The `opt_*()` methods give you quick access to common styling patterns without needing to remember the specific [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) argument names. For full control, you can always drop down to [tab_options()](../reference/GT.tab_options.md#great_tables.GT.tab_options) directly, but these convenience methods cover the most frequent customization needs in just a single method call.
