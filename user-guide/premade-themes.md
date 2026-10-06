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
#qlnpoinltk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qlnpoinltk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qlnpoinltk p { margin: 0; padding: 0; }
 #qlnpoinltk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qlnpoinltk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qlnpoinltk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qlnpoinltk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qlnpoinltk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qlnpoinltk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qlnpoinltk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qlnpoinltk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qlnpoinltk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qlnpoinltk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qlnpoinltk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qlnpoinltk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qlnpoinltk .gt_spanner_row { border-bottom-style: hidden; }
 #qlnpoinltk .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qlnpoinltk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qlnpoinltk .gt_from_md> :first-child { margin-top: 0; }
 #qlnpoinltk .gt_from_md> :last-child { margin-bottom: 0; }
 #qlnpoinltk .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qlnpoinltk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qlnpoinltk .gt_indent_1 { text-indent: 5px; }
 #qlnpoinltk .gt_indent_2 { text-indent: calc(5px * 2); }
 #qlnpoinltk .gt_indent_3 { text-indent: calc(5px * 3); }
 #qlnpoinltk .gt_indent_4 { text-indent: calc(5px * 4); }
 #qlnpoinltk .gt_indent_5 { text-indent: calc(5px * 5); }
 #qlnpoinltk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qlnpoinltk .gt_row_group_first td { border-top-width: 2px; }
 #qlnpoinltk .gt_row_group_first th { border-top-width: 2px; }
 #qlnpoinltk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qlnpoinltk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qlnpoinltk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qlnpoinltk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qlnpoinltk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qlnpoinltk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qlnpoinltk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qlnpoinltk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qlnpoinltk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qlnpoinltk .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qlnpoinltk .gt_left { text-align: left; }
 #qlnpoinltk .gt_center { text-align: center; }
 #qlnpoinltk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qlnpoinltk .gt_font_normal { font-weight: normal; }
 #qlnpoinltk .gt_font_bold { font-weight: bold; }
 #qlnpoinltk .gt_font_italic { font-style: italic; }
 #qlnpoinltk .gt_super { font-size: 65%; }
 #qlnpoinltk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qlnpoinltk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qlnpoinltk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qlnpoinltk .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qlnpoinltk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qlnpoinltk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#dzcjdzcopx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dzcjdzcopx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dzcjdzcopx p { margin: 0; padding: 0; }
 #dzcjdzcopx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #004D80; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #004D80; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dzcjdzcopx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dzcjdzcopx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dzcjdzcopx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dzcjdzcopx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dzcjdzcopx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #dzcjdzcopx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dzcjdzcopx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #dzcjdzcopx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dzcjdzcopx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dzcjdzcopx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dzcjdzcopx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dzcjdzcopx .gt_spanner_row { border-bottom-style: hidden; }
 #dzcjdzcopx .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dzcjdzcopx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: middle; }
 #dzcjdzcopx .gt_from_md> :first-child { margin-top: 0; }
 #dzcjdzcopx .gt_from_md> :last-child { margin-bottom: 0; }
 #dzcjdzcopx .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: none; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: none; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #dzcjdzcopx .gt_stub { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #0076BA; padding-left: 5px; padding-right: 5px; }
 #dzcjdzcopx .gt_indent_1 { text-indent: 5px; }
 #dzcjdzcopx .gt_indent_2 { text-indent: calc(5px * 2); }
 #dzcjdzcopx .gt_indent_3 { text-indent: calc(5px * 3); }
 #dzcjdzcopx .gt_indent_4 { text-indent: calc(5px * 4); }
 #dzcjdzcopx .gt_indent_5 { text-indent: calc(5px * 5); }
 #dzcjdzcopx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #dzcjdzcopx .gt_row_group_first td { border-top-width: 2px; }
 #dzcjdzcopx .gt_row_group_first th { border-top-width: 2px; }
 #dzcjdzcopx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dzcjdzcopx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #dzcjdzcopx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dzcjdzcopx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #dzcjdzcopx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dzcjdzcopx .gt_grand_summary_row { color: #333333; background-color: #89D3FE; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dzcjdzcopx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dzcjdzcopx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dzcjdzcopx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dzcjdzcopx .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dzcjdzcopx .gt_left { text-align: left; }
 #dzcjdzcopx .gt_center { text-align: center; }
 #dzcjdzcopx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dzcjdzcopx .gt_font_normal { font-weight: normal; }
 #dzcjdzcopx .gt_font_bold { font-weight: bold; }
 #dzcjdzcopx .gt_font_italic { font-style: italic; }
 #dzcjdzcopx .gt_super { font-size: 65%; }
 #dzcjdzcopx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dzcjdzcopx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #dzcjdzcopx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dzcjdzcopx .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #dzcjdzcopx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dzcjdzcopx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#oregjckszl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oregjckszl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oregjckszl p { margin: 0; padding: 0; }
 #oregjckszl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #oregjckszl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oregjckszl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oregjckszl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oregjckszl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oregjckszl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #oregjckszl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oregjckszl .gt_col_heading { color: #FFFFFF; background-color: #A81600; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oregjckszl .gt_column_spanner_outer { color: #FFFFFF; background-color: #A81600; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oregjckszl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oregjckszl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oregjckszl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oregjckszl .gt_spanner_row { border-bottom-style: hidden; }
 #oregjckszl .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oregjckszl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #oregjckszl .gt_from_md> :first-child { margin-top: 0; }
 #oregjckszl .gt_from_md> :last-child { margin-bottom: 0; }
 #oregjckszl .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #FFCCC7; border-left-style: solid; border-left-width: 1px; border-left-color: #FFCCC7; border-right-style: solid; border-right-width: 1px; border-right-color: #FFCCC7; vertical-align: middle; overflow-x: hidden; }
 #oregjckszl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #5F5F5F; padding-left: 5px; padding-right: 5px; }
 #oregjckszl .gt_indent_1 { text-indent: 5px; }
 #oregjckszl .gt_indent_2 { text-indent: calc(5px * 2); }
 #oregjckszl .gt_indent_3 { text-indent: calc(5px * 3); }
 #oregjckszl .gt_indent_4 { text-indent: calc(5px * 4); }
 #oregjckszl .gt_indent_5 { text-indent: calc(5px * 5); }
 #oregjckszl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oregjckszl .gt_row_group_first td { border-top-width: 2px; }
 #oregjckszl .gt_row_group_first th { border-top-width: 2px; }
 #oregjckszl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oregjckszl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #oregjckszl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oregjckszl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oregjckszl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oregjckszl .gt_grand_summary_row { color: #FFFFFF; background-color: #FF644E; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oregjckszl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oregjckszl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oregjckszl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oregjckszl .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oregjckszl .gt_left { text-align: left; }
 #oregjckszl .gt_center { text-align: center; }
 #oregjckszl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oregjckszl .gt_font_normal { font-weight: normal; }
 #oregjckszl .gt_font_bold { font-weight: bold; }
 #oregjckszl .gt_font_italic { font-style: italic; }
 #oregjckszl .gt_super { font-size: 65%; }
 #oregjckszl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oregjckszl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oregjckszl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oregjckszl .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oregjckszl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oregjckszl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#ihnrlhkwpv table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ihnrlhkwpv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ihnrlhkwpv p { margin: 0; padding: 0; }
 #ihnrlhkwpv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #004D80; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #004D80; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ihnrlhkwpv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ihnrlhkwpv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ihnrlhkwpv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ihnrlhkwpv .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ihnrlhkwpv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #ihnrlhkwpv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ihnrlhkwpv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ihnrlhkwpv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ihnrlhkwpv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ihnrlhkwpv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ihnrlhkwpv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ihnrlhkwpv .gt_spanner_row { border-bottom-style: hidden; }
 #ihnrlhkwpv .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ihnrlhkwpv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: middle; }
 #ihnrlhkwpv .gt_from_md> :first-child { margin-top: 0; }
 #ihnrlhkwpv .gt_from_md> :last-child { margin-bottom: 0; }
 #ihnrlhkwpv .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: none; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: none; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #ihnrlhkwpv .gt_stub { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #0076BA; padding-left: 5px; padding-right: 5px; }
 #ihnrlhkwpv .gt_indent_1 { text-indent: 5px; }
 #ihnrlhkwpv .gt_indent_2 { text-indent: calc(5px * 2); }
 #ihnrlhkwpv .gt_indent_3 { text-indent: calc(5px * 3); }
 #ihnrlhkwpv .gt_indent_4 { text-indent: calc(5px * 4); }
 #ihnrlhkwpv .gt_indent_5 { text-indent: calc(5px * 5); }
 #ihnrlhkwpv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ihnrlhkwpv .gt_row_group_first td { border-top-width: 2px; }
 #ihnrlhkwpv .gt_row_group_first th { border-top-width: 2px; }
 #ihnrlhkwpv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ihnrlhkwpv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #ihnrlhkwpv .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ihnrlhkwpv .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ihnrlhkwpv .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ihnrlhkwpv .gt_grand_summary_row { color: #333333; background-color: #89D3FE; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ihnrlhkwpv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ihnrlhkwpv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ihnrlhkwpv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ihnrlhkwpv .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ihnrlhkwpv .gt_left { text-align: left; }
 #ihnrlhkwpv .gt_center { text-align: center; }
 #ihnrlhkwpv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ihnrlhkwpv .gt_font_normal { font-weight: normal; }
 #ihnrlhkwpv .gt_font_bold { font-weight: bold; }
 #ihnrlhkwpv .gt_font_italic { font-style: italic; }
 #ihnrlhkwpv .gt_super { font-size: 65%; }
 #ihnrlhkwpv .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ihnrlhkwpv .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ihnrlhkwpv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ihnrlhkwpv .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ihnrlhkwpv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ihnrlhkwpv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#uuvdiqgqil table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uuvdiqgqil thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uuvdiqgqil p { margin: 0; padding: 0; }
 #uuvdiqgqil .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #uuvdiqgqil .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uuvdiqgqil .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uuvdiqgqil .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uuvdiqgqil .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uuvdiqgqil .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #uuvdiqgqil .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uuvdiqgqil .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uuvdiqgqil .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uuvdiqgqil .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uuvdiqgqil .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uuvdiqgqil .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uuvdiqgqil .gt_spanner_row { border-bottom-style: hidden; }
 #uuvdiqgqil .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uuvdiqgqil .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #uuvdiqgqil .gt_from_md> :first-child { margin-top: 0; }
 #uuvdiqgqil .gt_from_md> :last-child { margin-bottom: 0; }
 #uuvdiqgqil .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: solid; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: solid; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #uuvdiqgqil .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #5F5F5F; padding-left: 5px; padding-right: 5px; }
 #uuvdiqgqil .gt_indent_1 { text-indent: 5px; }
 #uuvdiqgqil .gt_indent_2 { text-indent: calc(5px * 2); }
 #uuvdiqgqil .gt_indent_3 { text-indent: calc(5px * 3); }
 #uuvdiqgqil .gt_indent_4 { text-indent: calc(5px * 4); }
 #uuvdiqgqil .gt_indent_5 { text-indent: calc(5px * 5); }
 #uuvdiqgqil .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uuvdiqgqil .gt_row_group_first td { border-top-width: 2px; }
 #uuvdiqgqil .gt_row_group_first th { border-top-width: 2px; }
 #uuvdiqgqil .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uuvdiqgqil .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #uuvdiqgqil .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uuvdiqgqil .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uuvdiqgqil .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uuvdiqgqil .gt_grand_summary_row { color: #FFFFFF; background-color: #00A1FF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uuvdiqgqil .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uuvdiqgqil .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uuvdiqgqil .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uuvdiqgqil .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uuvdiqgqil .gt_left { text-align: left; }
 #uuvdiqgqil .gt_center { text-align: center; }
 #uuvdiqgqil .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uuvdiqgqil .gt_font_normal { font-weight: normal; }
 #uuvdiqgqil .gt_font_bold { font-weight: bold; }
 #uuvdiqgqil .gt_font_italic { font-style: italic; }
 #uuvdiqgqil .gt_super { font-size: 65%; }
 #uuvdiqgqil .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uuvdiqgqil .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uuvdiqgqil .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uuvdiqgqil .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uuvdiqgqil .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uuvdiqgqil .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#rdvwbhympo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rdvwbhympo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rdvwbhympo p { margin: 0; padding: 0; }
 #rdvwbhympo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rdvwbhympo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rdvwbhympo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rdvwbhympo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rdvwbhympo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rdvwbhympo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; }
 #rdvwbhympo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rdvwbhympo .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rdvwbhympo .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rdvwbhympo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rdvwbhympo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rdvwbhympo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rdvwbhympo .gt_spanner_row { border-bottom-style: hidden; }
 #rdvwbhympo .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rdvwbhympo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; vertical-align: middle; }
 #rdvwbhympo .gt_from_md> :first-child { margin-top: 0; }
 #rdvwbhympo .gt_from_md> :last-child { margin-bottom: 0; }
 #rdvwbhympo .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: dashed; border-top-width: 1px; border-top-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #929292; border-right-style: none; border-right-width: 1px; border-right-color: #929292; vertical-align: middle; overflow-x: hidden; }
 #rdvwbhympo .gt_stub { color: #333333; background-color: #D5D5D5; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: none; border-right-width: 2px; border-right-color: #FFFFFF; padding-left: 5px; padding-right: 5px; }
 #rdvwbhympo .gt_indent_1 { text-indent: 5px; }
 #rdvwbhympo .gt_indent_2 { text-indent: calc(5px * 2); }
 #rdvwbhympo .gt_indent_3 { text-indent: calc(5px * 3); }
 #rdvwbhympo .gt_indent_4 { text-indent: calc(5px * 4); }
 #rdvwbhympo .gt_indent_5 { text-indent: calc(5px * 5); }
 #rdvwbhympo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rdvwbhympo .gt_row_group_first td { border-top-width: 2px; }
 #rdvwbhympo .gt_row_group_first th { border-top-width: 2px; }
 #rdvwbhympo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rdvwbhympo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; }
 #rdvwbhympo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rdvwbhympo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rdvwbhympo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rdvwbhympo .gt_grand_summary_row { color: #333333; background-color: #D5D5D5; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rdvwbhympo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rdvwbhympo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rdvwbhympo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rdvwbhympo .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rdvwbhympo .gt_left { text-align: left; }
 #rdvwbhympo .gt_center { text-align: center; }
 #rdvwbhympo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rdvwbhympo .gt_font_normal { font-weight: normal; }
 #rdvwbhympo .gt_font_bold { font-weight: bold; }
 #rdvwbhympo .gt_font_italic { font-style: italic; }
 #rdvwbhympo .gt_super { font-size: 65%; }
 #rdvwbhympo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rdvwbhympo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rdvwbhympo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rdvwbhympo .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rdvwbhympo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rdvwbhympo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#metwgncuxn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#metwgncuxn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#metwgncuxn p { margin: 0; padding: 0; }
 #metwgncuxn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #metwgncuxn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #metwgncuxn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #metwgncuxn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #metwgncuxn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #metwgncuxn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #metwgncuxn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #metwgncuxn .gt_col_heading { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #metwgncuxn .gt_column_spanner_outer { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #metwgncuxn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #metwgncuxn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #metwgncuxn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #metwgncuxn .gt_spanner_row { border-bottom-style: hidden; }
 #metwgncuxn .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #metwgncuxn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #metwgncuxn .gt_from_md> :first-child { margin-top: 0; }
 #metwgncuxn .gt_from_md> :last-child { margin-bottom: 0; }
 #metwgncuxn .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: dashed; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: dashed; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: dashed; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #metwgncuxn .gt_stub { color: #FFFFFF; background-color: #929292; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: dashed; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #metwgncuxn .gt_indent_1 { text-indent: 5px; }
 #metwgncuxn .gt_indent_2 { text-indent: calc(5px * 2); }
 #metwgncuxn .gt_indent_3 { text-indent: calc(5px * 3); }
 #metwgncuxn .gt_indent_4 { text-indent: calc(5px * 4); }
 #metwgncuxn .gt_indent_5 { text-indent: calc(5px * 5); }
 #metwgncuxn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #metwgncuxn .gt_row_group_first td { border-top-width: 2px; }
 #metwgncuxn .gt_row_group_first th { border-top-width: 2px; }
 #metwgncuxn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #metwgncuxn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #metwgncuxn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #metwgncuxn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #metwgncuxn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #metwgncuxn .gt_grand_summary_row { color: #FFFFFF; background-color: #0076BA; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #metwgncuxn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #metwgncuxn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #metwgncuxn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #metwgncuxn .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #metwgncuxn .gt_left { text-align: left; }
 #metwgncuxn .gt_center { text-align: center; }
 #metwgncuxn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #metwgncuxn .gt_font_normal { font-weight: normal; }
 #metwgncuxn .gt_font_bold { font-weight: bold; }
 #metwgncuxn .gt_font_italic { font-style: italic; }
 #metwgncuxn .gt_super { font-size: 65%; }
 #metwgncuxn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #metwgncuxn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #metwgncuxn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #metwgncuxn .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #metwgncuxn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #metwgncuxn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#kncufwjgbl table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kncufwjgbl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kncufwjgbl p { margin: 0; padding: 0; }
 #kncufwjgbl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #kncufwjgbl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kncufwjgbl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kncufwjgbl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kncufwjgbl .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kncufwjgbl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #kncufwjgbl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kncufwjgbl .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kncufwjgbl .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kncufwjgbl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kncufwjgbl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kncufwjgbl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kncufwjgbl .gt_spanner_row { border-bottom-style: hidden; }
 #kncufwjgbl .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kncufwjgbl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #kncufwjgbl .gt_from_md> :first-child { margin-top: 0; }
 #kncufwjgbl .gt_from_md> :last-child { margin-bottom: 0; }
 #kncufwjgbl .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: solid; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: solid; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #kncufwjgbl .gt_stub { color: #FFFFFF; background-color: #929292; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #kncufwjgbl .gt_indent_1 { text-indent: 5px; }
 #kncufwjgbl .gt_indent_2 { text-indent: calc(5px * 2); }
 #kncufwjgbl .gt_indent_3 { text-indent: calc(5px * 3); }
 #kncufwjgbl .gt_indent_4 { text-indent: calc(5px * 4); }
 #kncufwjgbl .gt_indent_5 { text-indent: calc(5px * 5); }
 #kncufwjgbl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kncufwjgbl .gt_row_group_first td { border-top-width: 2px; }
 #kncufwjgbl .gt_row_group_first th { border-top-width: 2px; }
 #kncufwjgbl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kncufwjgbl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #kncufwjgbl .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kncufwjgbl .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kncufwjgbl .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kncufwjgbl .gt_grand_summary_row { color: #FFFFFF; background-color: #929292; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kncufwjgbl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kncufwjgbl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kncufwjgbl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kncufwjgbl .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kncufwjgbl .gt_left { text-align: left; }
 #kncufwjgbl .gt_center { text-align: center; }
 #kncufwjgbl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kncufwjgbl .gt_font_normal { font-weight: normal; }
 #kncufwjgbl .gt_font_bold { font-weight: bold; }
 #kncufwjgbl .gt_font_italic { font-style: italic; }
 #kncufwjgbl .gt_super { font-size: 65%; }
 #kncufwjgbl .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kncufwjgbl .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kncufwjgbl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kncufwjgbl .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kncufwjgbl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kncufwjgbl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#oraoyaxbmn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oraoyaxbmn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oraoyaxbmn p { margin: 0; padding: 0; }
 #oraoyaxbmn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oraoyaxbmn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oraoyaxbmn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oraoyaxbmn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oraoyaxbmn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oraoyaxbmn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; }
 #oraoyaxbmn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oraoyaxbmn .gt_col_heading { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oraoyaxbmn .gt_column_spanner_outer { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oraoyaxbmn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oraoyaxbmn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oraoyaxbmn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oraoyaxbmn .gt_spanner_row { border-bottom-style: hidden; }
 #oraoyaxbmn .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oraoyaxbmn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; vertical-align: middle; }
 #oraoyaxbmn .gt_from_md> :first-child { margin-top: 0; }
 #oraoyaxbmn .gt_from_md> :last-child { margin-bottom: 0; }
 #oraoyaxbmn .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: none; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #oraoyaxbmn .gt_stub { color: #333333; background-color: #89D3FE; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #oraoyaxbmn .gt_indent_1 { text-indent: 5px; }
 #oraoyaxbmn .gt_indent_2 { text-indent: calc(5px * 2); }
 #oraoyaxbmn .gt_indent_3 { text-indent: calc(5px * 3); }
 #oraoyaxbmn .gt_indent_4 { text-indent: calc(5px * 4); }
 #oraoyaxbmn .gt_indent_5 { text-indent: calc(5px * 5); }
 #oraoyaxbmn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oraoyaxbmn .gt_row_group_first td { border-top-width: 2px; }
 #oraoyaxbmn .gt_row_group_first th { border-top-width: 2px; }
 #oraoyaxbmn .gt_striped { color: #333333; background-color: #EDF7FC; }
 #oraoyaxbmn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; }
 #oraoyaxbmn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oraoyaxbmn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #oraoyaxbmn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oraoyaxbmn .gt_grand_summary_row { color: #333333; background-color: #D5D5D5; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oraoyaxbmn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oraoyaxbmn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oraoyaxbmn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oraoyaxbmn .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oraoyaxbmn .gt_left { text-align: left; }
 #oraoyaxbmn .gt_center { text-align: center; }
 #oraoyaxbmn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oraoyaxbmn .gt_font_normal { font-weight: normal; }
 #oraoyaxbmn .gt_font_bold { font-weight: bold; }
 #oraoyaxbmn .gt_font_italic { font-style: italic; }
 #oraoyaxbmn .gt_super { font-size: 65%; }
 #oraoyaxbmn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oraoyaxbmn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #oraoyaxbmn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oraoyaxbmn .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oraoyaxbmn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oraoyaxbmn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#skdvmyfeoc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#skdvmyfeoc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#skdvmyfeoc p { margin: 0; padding: 0; }
 #skdvmyfeoc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #skdvmyfeoc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #skdvmyfeoc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #skdvmyfeoc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #skdvmyfeoc .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #skdvmyfeoc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #skdvmyfeoc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #skdvmyfeoc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #skdvmyfeoc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #skdvmyfeoc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #skdvmyfeoc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #skdvmyfeoc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #skdvmyfeoc .gt_spanner_row { border-bottom-style: hidden; }
 #skdvmyfeoc .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #skdvmyfeoc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #skdvmyfeoc .gt_from_md> :first-child { margin-top: 0; }
 #skdvmyfeoc .gt_from_md> :last-child { margin-bottom: 0; }
 #skdvmyfeoc .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #skdvmyfeoc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #skdvmyfeoc .gt_indent_1 { text-indent: 5px; }
 #skdvmyfeoc .gt_indent_2 { text-indent: calc(5px * 2); }
 #skdvmyfeoc .gt_indent_3 { text-indent: calc(5px * 3); }
 #skdvmyfeoc .gt_indent_4 { text-indent: calc(5px * 4); }
 #skdvmyfeoc .gt_indent_5 { text-indent: calc(5px * 5); }
 #skdvmyfeoc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #skdvmyfeoc .gt_row_group_first td { border-top-width: 2px; }
 #skdvmyfeoc .gt_row_group_first th { border-top-width: 2px; }
 #skdvmyfeoc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #skdvmyfeoc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #skdvmyfeoc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #skdvmyfeoc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #skdvmyfeoc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #skdvmyfeoc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #skdvmyfeoc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #skdvmyfeoc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #skdvmyfeoc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #skdvmyfeoc .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #skdvmyfeoc .gt_left { text-align: left; }
 #skdvmyfeoc .gt_center { text-align: center; }
 #skdvmyfeoc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #skdvmyfeoc .gt_font_normal { font-weight: normal; }
 #skdvmyfeoc .gt_font_bold { font-weight: bold; }
 #skdvmyfeoc .gt_font_italic { font-style: italic; }
 #skdvmyfeoc .gt_super { font-size: 65%; }
 #skdvmyfeoc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #skdvmyfeoc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #skdvmyfeoc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #skdvmyfeoc .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #skdvmyfeoc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #skdvmyfeoc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#uvykggcldy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#uvykggcldy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#uvykggcldy p { margin: 0; padding: 0; }
 #uvykggcldy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #uvykggcldy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #uvykggcldy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #uvykggcldy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #uvykggcldy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uvykggcldy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvykggcldy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #uvykggcldy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #uvykggcldy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #uvykggcldy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #uvykggcldy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #uvykggcldy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #uvykggcldy .gt_spanner_row { border-bottom-style: hidden; }
 #uvykggcldy .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #uvykggcldy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #uvykggcldy .gt_from_md> :first-child { margin-top: 0; }
 #uvykggcldy .gt_from_md> :last-child { margin-bottom: 0; }
 #uvykggcldy .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #uvykggcldy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #uvykggcldy .gt_indent_1 { text-indent: 5px; }
 #uvykggcldy .gt_indent_2 { text-indent: calc(5px * 2); }
 #uvykggcldy .gt_indent_3 { text-indent: calc(5px * 3); }
 #uvykggcldy .gt_indent_4 { text-indent: calc(5px * 4); }
 #uvykggcldy .gt_indent_5 { text-indent: calc(5px * 5); }
 #uvykggcldy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #uvykggcldy .gt_row_group_first td { border-top-width: 2px; }
 #uvykggcldy .gt_row_group_first th { border-top-width: 2px; }
 #uvykggcldy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #uvykggcldy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvykggcldy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uvykggcldy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #uvykggcldy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #uvykggcldy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #uvykggcldy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #uvykggcldy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #uvykggcldy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvykggcldy .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uvykggcldy .gt_left { text-align: left; }
 #uvykggcldy .gt_center { text-align: center; }
 #uvykggcldy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #uvykggcldy .gt_font_normal { font-weight: normal; }
 #uvykggcldy .gt_font_bold { font-weight: bold; }
 #uvykggcldy .gt_font_italic { font-style: italic; }
 #uvykggcldy .gt_super { font-size: 65%; }
 #uvykggcldy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvykggcldy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #uvykggcldy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #uvykggcldy .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #uvykggcldy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #uvykggcldy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#sjatbehjtk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sjatbehjtk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sjatbehjtk p { margin: 0; padding: 0; }
 #sjatbehjtk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #sjatbehjtk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sjatbehjtk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sjatbehjtk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: -0.4px; padding-bottom: 1.6px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sjatbehjtk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sjatbehjtk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sjatbehjtk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sjatbehjtk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 0.75px; padding-bottom: 1.6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sjatbehjtk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sjatbehjtk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sjatbehjtk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sjatbehjtk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 0.75px; padding-bottom: 0.75px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sjatbehjtk .gt_spanner_row { border-bottom-style: hidden; }
 #sjatbehjtk .gt_group_heading { padding-top: 1.2px; padding-bottom: 1.2px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sjatbehjtk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #sjatbehjtk .gt_from_md> :first-child { margin-top: 0; }
 #sjatbehjtk .gt_from_md> :last-child { margin-bottom: 0; }
 #sjatbehjtk .gt_row { padding-top: 1.2px; padding-bottom: 1.2px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #sjatbehjtk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #sjatbehjtk .gt_indent_1 { text-indent: 5px; }
 #sjatbehjtk .gt_indent_2 { text-indent: calc(5px * 2); }
 #sjatbehjtk .gt_indent_3 { text-indent: calc(5px * 3); }
 #sjatbehjtk .gt_indent_4 { text-indent: calc(5px * 4); }
 #sjatbehjtk .gt_indent_5 { text-indent: calc(5px * 5); }
 #sjatbehjtk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sjatbehjtk .gt_row_group_first td { border-top-width: 2px; }
 #sjatbehjtk .gt_row_group_first th { border-top-width: 2px; }
 #sjatbehjtk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sjatbehjtk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sjatbehjtk .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sjatbehjtk .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sjatbehjtk .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sjatbehjtk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sjatbehjtk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sjatbehjtk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sjatbehjtk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sjatbehjtk .gt_sourcenote { font-size: 90%; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sjatbehjtk .gt_left { text-align: left; }
 #sjatbehjtk .gt_center { text-align: center; }
 #sjatbehjtk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sjatbehjtk .gt_font_normal { font-weight: normal; }
 #sjatbehjtk .gt_font_bold { font-weight: bold; }
 #sjatbehjtk .gt_font_italic { font-style: italic; }
 #sjatbehjtk .gt_super { font-size: 65%; }
 #sjatbehjtk .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sjatbehjtk .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sjatbehjtk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sjatbehjtk .gt_sourcenote { font-size: 90%; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sjatbehjtk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sjatbehjtk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#kjbogzfskh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kjbogzfskh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kjbogzfskh p { margin: 0; padding: 0; }
 #kjbogzfskh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kjbogzfskh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kjbogzfskh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kjbogzfskh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 15px; padding-right: 15px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kjbogzfskh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kjbogzfskh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kjbogzfskh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kjbogzfskh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 15px; padding-right: 15px; overflow-x: hidden; }
 #kjbogzfskh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kjbogzfskh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kjbogzfskh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kjbogzfskh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kjbogzfskh .gt_spanner_row { border-bottom-style: hidden; }
 #kjbogzfskh .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kjbogzfskh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kjbogzfskh .gt_from_md> :first-child { margin-top: 0; }
 #kjbogzfskh .gt_from_md> :last-child { margin-bottom: 0; }
 #kjbogzfskh .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kjbogzfskh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 15px; padding-right: 15px; }
 #kjbogzfskh .gt_indent_1 { text-indent: 5px; }
 #kjbogzfskh .gt_indent_2 { text-indent: calc(5px * 2); }
 #kjbogzfskh .gt_indent_3 { text-indent: calc(5px * 3); }
 #kjbogzfskh .gt_indent_4 { text-indent: calc(5px * 4); }
 #kjbogzfskh .gt_indent_5 { text-indent: calc(5px * 5); }
 #kjbogzfskh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 15px; padding-right: 15px; vertical-align: top; }
 #kjbogzfskh .gt_row_group_first td { border-top-width: 2px; }
 #kjbogzfskh .gt_row_group_first th { border-top-width: 2px; }
 #kjbogzfskh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kjbogzfskh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kjbogzfskh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kjbogzfskh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kjbogzfskh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kjbogzfskh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kjbogzfskh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kjbogzfskh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kjbogzfskh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kjbogzfskh .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #kjbogzfskh .gt_left { text-align: left; }
 #kjbogzfskh .gt_center { text-align: center; }
 #kjbogzfskh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kjbogzfskh .gt_font_normal { font-weight: normal; }
 #kjbogzfskh .gt_font_bold { font-weight: bold; }
 #kjbogzfskh .gt_font_italic { font-style: italic; }
 #kjbogzfskh .gt_super { font-size: 65%; }
 #kjbogzfskh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kjbogzfskh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kjbogzfskh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kjbogzfskh .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #kjbogzfskh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kjbogzfskh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
#xuthjrypnp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xuthjrypnp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xuthjrypnp p { margin: 0; padding: 0; }
 #xuthjrypnp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D3D3D3; border-right-style: solid; border-right-width: 3px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D3D3D3; border-left-style: solid; border-left-width: 3px; border-left-color: #D3D3D3; }
 #xuthjrypnp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xuthjrypnp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xuthjrypnp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xuthjrypnp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xuthjrypnp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xuthjrypnp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xuthjrypnp .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xuthjrypnp .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xuthjrypnp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xuthjrypnp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xuthjrypnp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xuthjrypnp .gt_spanner_row { border-bottom-style: hidden; }
 #xuthjrypnp .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xuthjrypnp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xuthjrypnp .gt_from_md> :first-child { margin-top: 0; }
 #xuthjrypnp .gt_from_md> :last-child { margin-bottom: 0; }
 #xuthjrypnp .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xuthjrypnp .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xuthjrypnp .gt_indent_1 { text-indent: 5px; }
 #xuthjrypnp .gt_indent_2 { text-indent: calc(5px * 2); }
 #xuthjrypnp .gt_indent_3 { text-indent: calc(5px * 3); }
 #xuthjrypnp .gt_indent_4 { text-indent: calc(5px * 4); }
 #xuthjrypnp .gt_indent_5 { text-indent: calc(5px * 5); }
 #xuthjrypnp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xuthjrypnp .gt_row_group_first td { border-top-width: 2px; }
 #xuthjrypnp .gt_row_group_first th { border-top-width: 2px; }
 #xuthjrypnp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xuthjrypnp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xuthjrypnp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xuthjrypnp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xuthjrypnp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xuthjrypnp .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xuthjrypnp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xuthjrypnp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xuthjrypnp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xuthjrypnp .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xuthjrypnp .gt_left { text-align: left; }
 #xuthjrypnp .gt_center { text-align: center; }
 #xuthjrypnp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xuthjrypnp .gt_font_normal { font-weight: normal; }
 #xuthjrypnp .gt_font_bold { font-weight: bold; }
 #xuthjrypnp .gt_font_italic { font-style: italic; }
 #xuthjrypnp .gt_super { font-size: 65%; }
 #xuthjrypnp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xuthjrypnp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xuthjrypnp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xuthjrypnp .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xuthjrypnp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xuthjrypnp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
