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
#fnuiraxpoo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fnuiraxpoo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fnuiraxpoo p { margin: 0; padding: 0; }
 #fnuiraxpoo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fnuiraxpoo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fnuiraxpoo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fnuiraxpoo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fnuiraxpoo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fnuiraxpoo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fnuiraxpoo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fnuiraxpoo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fnuiraxpoo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fnuiraxpoo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fnuiraxpoo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fnuiraxpoo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fnuiraxpoo .gt_spanner_row { border-bottom-style: hidden; }
 #fnuiraxpoo .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fnuiraxpoo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fnuiraxpoo .gt_from_md> :first-child { margin-top: 0; }
 #fnuiraxpoo .gt_from_md> :last-child { margin-bottom: 0; }
 #fnuiraxpoo .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fnuiraxpoo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fnuiraxpoo .gt_indent_1 { text-indent: 5px; }
 #fnuiraxpoo .gt_indent_2 { text-indent: calc(5px * 2); }
 #fnuiraxpoo .gt_indent_3 { text-indent: calc(5px * 3); }
 #fnuiraxpoo .gt_indent_4 { text-indent: calc(5px * 4); }
 #fnuiraxpoo .gt_indent_5 { text-indent: calc(5px * 5); }
 #fnuiraxpoo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fnuiraxpoo .gt_row_group_first td { border-top-width: 2px; }
 #fnuiraxpoo .gt_row_group_first th { border-top-width: 2px; }
 #fnuiraxpoo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fnuiraxpoo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fnuiraxpoo .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fnuiraxpoo .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #fnuiraxpoo .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fnuiraxpoo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fnuiraxpoo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fnuiraxpoo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fnuiraxpoo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fnuiraxpoo .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fnuiraxpoo .gt_left { text-align: left; }
 #fnuiraxpoo .gt_center { text-align: center; }
 #fnuiraxpoo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fnuiraxpoo .gt_font_normal { font-weight: normal; }
 #fnuiraxpoo .gt_font_bold { font-weight: bold; }
 #fnuiraxpoo .gt_font_italic { font-style: italic; }
 #fnuiraxpoo .gt_super { font-size: 65%; }
 #fnuiraxpoo .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fnuiraxpoo .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #fnuiraxpoo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fnuiraxpoo .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fnuiraxpoo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fnuiraxpoo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
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
#rqemybzbld table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rqemybzbld thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rqemybzbld p { margin: 0; padding: 0; }
 #rqemybzbld .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #004D80; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #004D80; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rqemybzbld .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rqemybzbld .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rqemybzbld .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rqemybzbld .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rqemybzbld .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #rqemybzbld .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rqemybzbld .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rqemybzbld .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rqemybzbld .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rqemybzbld .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rqemybzbld .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rqemybzbld .gt_spanner_row { border-bottom-style: hidden; }
 #rqemybzbld .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rqemybzbld .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: middle; }
 #rqemybzbld .gt_from_md> :first-child { margin-top: 0; }
 #rqemybzbld .gt_from_md> :last-child { margin-bottom: 0; }
 #rqemybzbld .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: none; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: none; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #rqemybzbld .gt_stub { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #0076BA; padding-left: 5px; padding-right: 5px; }
 #rqemybzbld .gt_indent_1 { text-indent: 5px; }
 #rqemybzbld .gt_indent_2 { text-indent: calc(5px * 2); }
 #rqemybzbld .gt_indent_3 { text-indent: calc(5px * 3); }
 #rqemybzbld .gt_indent_4 { text-indent: calc(5px * 4); }
 #rqemybzbld .gt_indent_5 { text-indent: calc(5px * 5); }
 #rqemybzbld .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rqemybzbld .gt_row_group_first td { border-top-width: 2px; }
 #rqemybzbld .gt_row_group_first th { border-top-width: 2px; }
 #rqemybzbld .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rqemybzbld .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #rqemybzbld .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rqemybzbld .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #rqemybzbld .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rqemybzbld .gt_grand_summary_row { color: #333333; background-color: #89D3FE; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rqemybzbld .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rqemybzbld .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rqemybzbld .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rqemybzbld .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rqemybzbld .gt_left { text-align: left; }
 #rqemybzbld .gt_center { text-align: center; }
 #rqemybzbld .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rqemybzbld .gt_font_normal { font-weight: normal; }
 #rqemybzbld .gt_font_bold { font-weight: bold; }
 #rqemybzbld .gt_font_italic { font-style: italic; }
 #rqemybzbld .gt_super { font-size: 65%; }
 #rqemybzbld .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rqemybzbld .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #rqemybzbld .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rqemybzbld .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rqemybzbld .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rqemybzbld .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
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
#sfbgfwzwba table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#sfbgfwzwba thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#sfbgfwzwba p { margin: 0; padding: 0; }
 #sfbgfwzwba .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #sfbgfwzwba .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #sfbgfwzwba .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #sfbgfwzwba .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #sfbgfwzwba .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sfbgfwzwba .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #sfbgfwzwba .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #sfbgfwzwba .gt_col_heading { color: #FFFFFF; background-color: #A81600; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #sfbgfwzwba .gt_column_spanner_outer { color: #FFFFFF; background-color: #A81600; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #sfbgfwzwba .gt_column_spanner_outer:first-child { padding-left: 0; }
 #sfbgfwzwba .gt_column_spanner_outer:last-child { padding-right: 0; }
 #sfbgfwzwba .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #sfbgfwzwba .gt_spanner_row { border-bottom-style: hidden; }
 #sfbgfwzwba .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #sfbgfwzwba .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #sfbgfwzwba .gt_from_md> :first-child { margin-top: 0; }
 #sfbgfwzwba .gt_from_md> :last-child { margin-bottom: 0; }
 #sfbgfwzwba .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #FFCCC7; border-left-style: solid; border-left-width: 1px; border-left-color: #FFCCC7; border-right-style: solid; border-right-width: 1px; border-right-color: #FFCCC7; vertical-align: middle; overflow-x: hidden; }
 #sfbgfwzwba .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #5F5F5F; padding-left: 5px; padding-right: 5px; }
 #sfbgfwzwba .gt_indent_1 { text-indent: 5px; }
 #sfbgfwzwba .gt_indent_2 { text-indent: calc(5px * 2); }
 #sfbgfwzwba .gt_indent_3 { text-indent: calc(5px * 3); }
 #sfbgfwzwba .gt_indent_4 { text-indent: calc(5px * 4); }
 #sfbgfwzwba .gt_indent_5 { text-indent: calc(5px * 5); }
 #sfbgfwzwba .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #sfbgfwzwba .gt_row_group_first td { border-top-width: 2px; }
 #sfbgfwzwba .gt_row_group_first th { border-top-width: 2px; }
 #sfbgfwzwba .gt_striped { color: #333333; background-color: #F4F4F4; }
 #sfbgfwzwba .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #sfbgfwzwba .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sfbgfwzwba .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #sfbgfwzwba .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #sfbgfwzwba .gt_grand_summary_row { color: #FFFFFF; background-color: #FF644E; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #sfbgfwzwba .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #sfbgfwzwba .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #sfbgfwzwba .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sfbgfwzwba .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sfbgfwzwba .gt_left { text-align: left; }
 #sfbgfwzwba .gt_center { text-align: center; }
 #sfbgfwzwba .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #sfbgfwzwba .gt_font_normal { font-weight: normal; }
 #sfbgfwzwba .gt_font_bold { font-weight: bold; }
 #sfbgfwzwba .gt_font_italic { font-style: italic; }
 #sfbgfwzwba .gt_super { font-size: 65%; }
 #sfbgfwzwba .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sfbgfwzwba .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #sfbgfwzwba .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #sfbgfwzwba .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #sfbgfwzwba .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #sfbgfwzwba .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
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
#spnleogltu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#spnleogltu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#spnleogltu p { margin: 0; padding: 0; }
 #spnleogltu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #004D80; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #004D80; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #spnleogltu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #spnleogltu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #spnleogltu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #spnleogltu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #spnleogltu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #spnleogltu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #spnleogltu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #spnleogltu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #spnleogltu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #spnleogltu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #spnleogltu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #spnleogltu .gt_spanner_row { border-bottom-style: hidden; }
 #spnleogltu .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #spnleogltu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: middle; }
 #spnleogltu .gt_from_md> :first-child { margin-top: 0; }
 #spnleogltu .gt_from_md> :last-child { margin-bottom: 0; }
 #spnleogltu .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: none; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: none; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #spnleogltu .gt_stub { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #0076BA; padding-left: 5px; padding-right: 5px; }
 #spnleogltu .gt_indent_1 { text-indent: 5px; }
 #spnleogltu .gt_indent_2 { text-indent: calc(5px * 2); }
 #spnleogltu .gt_indent_3 { text-indent: calc(5px * 3); }
 #spnleogltu .gt_indent_4 { text-indent: calc(5px * 4); }
 #spnleogltu .gt_indent_5 { text-indent: calc(5px * 5); }
 #spnleogltu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #spnleogltu .gt_row_group_first td { border-top-width: 2px; }
 #spnleogltu .gt_row_group_first th { border-top-width: 2px; }
 #spnleogltu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #spnleogltu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #spnleogltu .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #spnleogltu .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #spnleogltu .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #spnleogltu .gt_grand_summary_row { color: #333333; background-color: #89D3FE; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #spnleogltu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #spnleogltu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #spnleogltu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #spnleogltu .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #spnleogltu .gt_left { text-align: left; }
 #spnleogltu .gt_center { text-align: center; }
 #spnleogltu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #spnleogltu .gt_font_normal { font-weight: normal; }
 #spnleogltu .gt_font_bold { font-weight: bold; }
 #spnleogltu .gt_font_italic { font-style: italic; }
 #spnleogltu .gt_super { font-size: 65%; }
 #spnleogltu .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #spnleogltu .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #spnleogltu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #spnleogltu .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #spnleogltu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #spnleogltu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
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
#iqplzpwswh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iqplzpwswh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iqplzpwswh p { margin: 0; padding: 0; }
 #iqplzpwswh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #iqplzpwswh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iqplzpwswh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iqplzpwswh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iqplzpwswh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iqplzpwswh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #iqplzpwswh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iqplzpwswh .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iqplzpwswh .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iqplzpwswh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iqplzpwswh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iqplzpwswh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iqplzpwswh .gt_spanner_row { border-bottom-style: hidden; }
 #iqplzpwswh .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iqplzpwswh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #iqplzpwswh .gt_from_md> :first-child { margin-top: 0; }
 #iqplzpwswh .gt_from_md> :last-child { margin-bottom: 0; }
 #iqplzpwswh .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: solid; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: solid; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #iqplzpwswh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #5F5F5F; padding-left: 5px; padding-right: 5px; }
 #iqplzpwswh .gt_indent_1 { text-indent: 5px; }
 #iqplzpwswh .gt_indent_2 { text-indent: calc(5px * 2); }
 #iqplzpwswh .gt_indent_3 { text-indent: calc(5px * 3); }
 #iqplzpwswh .gt_indent_4 { text-indent: calc(5px * 4); }
 #iqplzpwswh .gt_indent_5 { text-indent: calc(5px * 5); }
 #iqplzpwswh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iqplzpwswh .gt_row_group_first td { border-top-width: 2px; }
 #iqplzpwswh .gt_row_group_first th { border-top-width: 2px; }
 #iqplzpwswh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #iqplzpwswh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #iqplzpwswh .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iqplzpwswh .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #iqplzpwswh .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iqplzpwswh .gt_grand_summary_row { color: #FFFFFF; background-color: #00A1FF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iqplzpwswh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iqplzpwswh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iqplzpwswh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iqplzpwswh .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iqplzpwswh .gt_left { text-align: left; }
 #iqplzpwswh .gt_center { text-align: center; }
 #iqplzpwswh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iqplzpwswh .gt_font_normal { font-weight: normal; }
 #iqplzpwswh .gt_font_bold { font-weight: bold; }
 #iqplzpwswh .gt_font_italic { font-style: italic; }
 #iqplzpwswh .gt_super { font-size: 65%; }
 #iqplzpwswh .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iqplzpwswh .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #iqplzpwswh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iqplzpwswh .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iqplzpwswh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iqplzpwswh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
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
#ishgkzxggd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ishgkzxggd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ishgkzxggd p { margin: 0; padding: 0; }
 #ishgkzxggd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ishgkzxggd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ishgkzxggd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ishgkzxggd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ishgkzxggd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ishgkzxggd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; }
 #ishgkzxggd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ishgkzxggd .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ishgkzxggd .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ishgkzxggd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ishgkzxggd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ishgkzxggd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ishgkzxggd .gt_spanner_row { border-bottom-style: hidden; }
 #ishgkzxggd .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ishgkzxggd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; vertical-align: middle; }
 #ishgkzxggd .gt_from_md> :first-child { margin-top: 0; }
 #ishgkzxggd .gt_from_md> :last-child { margin-bottom: 0; }
 #ishgkzxggd .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: dashed; border-top-width: 1px; border-top-color: #929292; border-left-style: none; border-left-width: 1px; border-left-color: #929292; border-right-style: none; border-right-width: 1px; border-right-color: #929292; vertical-align: middle; overflow-x: hidden; }
 #ishgkzxggd .gt_stub { color: #333333; background-color: #D5D5D5; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: none; border-right-width: 2px; border-right-color: #FFFFFF; padding-left: 5px; padding-right: 5px; }
 #ishgkzxggd .gt_indent_1 { text-indent: 5px; }
 #ishgkzxggd .gt_indent_2 { text-indent: calc(5px * 2); }
 #ishgkzxggd .gt_indent_3 { text-indent: calc(5px * 3); }
 #ishgkzxggd .gt_indent_4 { text-indent: calc(5px * 4); }
 #ishgkzxggd .gt_indent_5 { text-indent: calc(5px * 5); }
 #ishgkzxggd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ishgkzxggd .gt_row_group_first td { border-top-width: 2px; }
 #ishgkzxggd .gt_row_group_first th { border-top-width: 2px; }
 #ishgkzxggd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ishgkzxggd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #929292; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #929292; }
 #ishgkzxggd .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ishgkzxggd .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ishgkzxggd .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ishgkzxggd .gt_grand_summary_row { color: #333333; background-color: #D5D5D5; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ishgkzxggd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ishgkzxggd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ishgkzxggd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ishgkzxggd .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ishgkzxggd .gt_left { text-align: left; }
 #ishgkzxggd .gt_center { text-align: center; }
 #ishgkzxggd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ishgkzxggd .gt_font_normal { font-weight: normal; }
 #ishgkzxggd .gt_font_bold { font-weight: bold; }
 #ishgkzxggd .gt_font_italic { font-style: italic; }
 #ishgkzxggd .gt_super { font-size: 65%; }
 #ishgkzxggd .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ishgkzxggd .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ishgkzxggd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ishgkzxggd .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ishgkzxggd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ishgkzxggd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
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
#kcmkndhhyp table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kcmkndhhyp thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kcmkndhhyp p { margin: 0; padding: 0; }
 #kcmkndhhyp .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #kcmkndhhyp .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kcmkndhhyp .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kcmkndhhyp .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kcmkndhhyp .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kcmkndhhyp .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #kcmkndhhyp .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kcmkndhhyp .gt_col_heading { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kcmkndhhyp .gt_column_spanner_outer { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kcmkndhhyp .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kcmkndhhyp .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kcmkndhhyp .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kcmkndhhyp .gt_spanner_row { border-bottom-style: hidden; }
 #kcmkndhhyp .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kcmkndhhyp .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #kcmkndhhyp .gt_from_md> :first-child { margin-top: 0; }
 #kcmkndhhyp .gt_from_md> :last-child { margin-bottom: 0; }
 #kcmkndhhyp .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: dashed; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: dashed; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: dashed; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #kcmkndhhyp .gt_stub { color: #FFFFFF; background-color: #929292; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: dashed; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #kcmkndhhyp .gt_indent_1 { text-indent: 5px; }
 #kcmkndhhyp .gt_indent_2 { text-indent: calc(5px * 2); }
 #kcmkndhhyp .gt_indent_3 { text-indent: calc(5px * 3); }
 #kcmkndhhyp .gt_indent_4 { text-indent: calc(5px * 4); }
 #kcmkndhhyp .gt_indent_5 { text-indent: calc(5px * 5); }
 #kcmkndhhyp .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kcmkndhhyp .gt_row_group_first td { border-top-width: 2px; }
 #kcmkndhhyp .gt_row_group_first th { border-top-width: 2px; }
 #kcmkndhhyp .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kcmkndhhyp .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #kcmkndhhyp .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kcmkndhhyp .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #kcmkndhhyp .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kcmkndhhyp .gt_grand_summary_row { color: #FFFFFF; background-color: #0076BA; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kcmkndhhyp .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kcmkndhhyp .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kcmkndhhyp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kcmkndhhyp .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kcmkndhhyp .gt_left { text-align: left; }
 #kcmkndhhyp .gt_center { text-align: center; }
 #kcmkndhhyp .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kcmkndhhyp .gt_font_normal { font-weight: normal; }
 #kcmkndhhyp .gt_font_bold { font-weight: bold; }
 #kcmkndhhyp .gt_font_italic { font-style: italic; }
 #kcmkndhhyp .gt_super { font-size: 65%; }
 #kcmkndhhyp .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kcmkndhhyp .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #kcmkndhhyp .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kcmkndhhyp .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kcmkndhhyp .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kcmkndhhyp .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
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
#lflwyountx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lflwyountx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lflwyountx p { margin: 0; padding: 0; }
 #lflwyountx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D5D5D5; border-right-style: solid; border-right-width: 3px; border-right-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D5D5D5; border-left-style: solid; border-left-width: 3px; border-left-color: #D5D5D5; }
 #lflwyountx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lflwyountx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lflwyountx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lflwyountx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lflwyountx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #lflwyountx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lflwyountx .gt_col_heading { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lflwyountx .gt_column_spanner_outer { color: #FFFFFF; background-color: #004D80; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lflwyountx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lflwyountx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lflwyountx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lflwyountx .gt_spanner_row { border-bottom-style: hidden; }
 #lflwyountx .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lflwyountx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; vertical-align: middle; }
 #lflwyountx .gt_from_md> :first-child { margin-top: 0; }
 #lflwyountx .gt_from_md> :last-child { margin-bottom: 0; }
 #lflwyountx .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: solid; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: solid; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #lflwyountx .gt_stub { color: #FFFFFF; background-color: #929292; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #lflwyountx .gt_indent_1 { text-indent: 5px; }
 #lflwyountx .gt_indent_2 { text-indent: calc(5px * 2); }
 #lflwyountx .gt_indent_3 { text-indent: calc(5px * 3); }
 #lflwyountx .gt_indent_4 { text-indent: calc(5px * 4); }
 #lflwyountx .gt_indent_5 { text-indent: calc(5px * 5); }
 #lflwyountx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lflwyountx .gt_row_group_first td { border-top-width: 2px; }
 #lflwyountx .gt_row_group_first th { border-top-width: 2px; }
 #lflwyountx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lflwyountx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D5D5D5; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D5D5D5; }
 #lflwyountx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lflwyountx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #lflwyountx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lflwyountx .gt_grand_summary_row { color: #FFFFFF; background-color: #929292; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lflwyountx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lflwyountx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lflwyountx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lflwyountx .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lflwyountx .gt_left { text-align: left; }
 #lflwyountx .gt_center { text-align: center; }
 #lflwyountx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lflwyountx .gt_font_normal { font-weight: normal; }
 #lflwyountx .gt_font_bold { font-weight: bold; }
 #lflwyountx .gt_font_italic { font-style: italic; }
 #lflwyountx .gt_super { font-size: 65%; }
 #lflwyountx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lflwyountx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #lflwyountx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lflwyountx .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lflwyountx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lflwyountx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
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
#iovppbmhyx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iovppbmhyx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iovppbmhyx p { margin: 0; padding: 0; }
 #iovppbmhyx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #iovppbmhyx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iovppbmhyx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iovppbmhyx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iovppbmhyx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iovppbmhyx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; }
 #iovppbmhyx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iovppbmhyx .gt_col_heading { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iovppbmhyx .gt_column_spanner_outer { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iovppbmhyx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iovppbmhyx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iovppbmhyx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iovppbmhyx .gt_spanner_row { border-bottom-style: hidden; }
 #iovppbmhyx .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iovppbmhyx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; vertical-align: middle; }
 #iovppbmhyx .gt_from_md> :first-child { margin-top: 0; }
 #iovppbmhyx .gt_from_md> :last-child { margin-bottom: 0; }
 #iovppbmhyx .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #D5D5D5; border-left-style: none; border-left-width: 1px; border-left-color: #D5D5D5; border-right-style: none; border-right-width: 1px; border-right-color: #D5D5D5; vertical-align: middle; overflow-x: hidden; }
 #iovppbmhyx .gt_stub { color: #333333; background-color: #89D3FE; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D5D5D5; padding-left: 5px; padding-right: 5px; }
 #iovppbmhyx .gt_indent_1 { text-indent: 5px; }
 #iovppbmhyx .gt_indent_2 { text-indent: calc(5px * 2); }
 #iovppbmhyx .gt_indent_3 { text-indent: calc(5px * 3); }
 #iovppbmhyx .gt_indent_4 { text-indent: calc(5px * 4); }
 #iovppbmhyx .gt_indent_5 { text-indent: calc(5px * 5); }
 #iovppbmhyx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iovppbmhyx .gt_row_group_first td { border-top-width: 2px; }
 #iovppbmhyx .gt_row_group_first th { border-top-width: 2px; }
 #iovppbmhyx .gt_striped { color: #333333; background-color: #EDF7FC; }
 #iovppbmhyx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #5F5F5F; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #5F5F5F; }
 #iovppbmhyx .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iovppbmhyx .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #iovppbmhyx .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iovppbmhyx .gt_grand_summary_row { color: #333333; background-color: #D5D5D5; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iovppbmhyx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iovppbmhyx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iovppbmhyx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iovppbmhyx .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iovppbmhyx .gt_left { text-align: left; }
 #iovppbmhyx .gt_center { text-align: center; }
 #iovppbmhyx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iovppbmhyx .gt_font_normal { font-weight: normal; }
 #iovppbmhyx .gt_font_bold { font-weight: bold; }
 #iovppbmhyx .gt_font_italic { font-style: italic; }
 #iovppbmhyx .gt_super { font-size: 65%; }
 #iovppbmhyx .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iovppbmhyx .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #iovppbmhyx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iovppbmhyx .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iovppbmhyx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iovppbmhyx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right gt_striped">2.22</td>
<td class="gt_row gt_left gt_striped">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right gt_striped">444.40</td>
<td class="gt_row gt_left gt_striped">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
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
#qwivjjlbik table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qwivjjlbik thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qwivjjlbik p { margin: 0; padding: 0; }
 #qwivjjlbik .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qwivjjlbik .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qwivjjlbik .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qwivjjlbik .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qwivjjlbik .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qwivjjlbik .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qwivjjlbik .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qwivjjlbik .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qwivjjlbik .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qwivjjlbik .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qwivjjlbik .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qwivjjlbik .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qwivjjlbik .gt_spanner_row { border-bottom-style: hidden; }
 #qwivjjlbik .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qwivjjlbik .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qwivjjlbik .gt_from_md> :first-child { margin-top: 0; }
 #qwivjjlbik .gt_from_md> :last-child { margin-bottom: 0; }
 #qwivjjlbik .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qwivjjlbik .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qwivjjlbik .gt_indent_1 { text-indent: 5px; }
 #qwivjjlbik .gt_indent_2 { text-indent: calc(5px * 2); }
 #qwivjjlbik .gt_indent_3 { text-indent: calc(5px * 3); }
 #qwivjjlbik .gt_indent_4 { text-indent: calc(5px * 4); }
 #qwivjjlbik .gt_indent_5 { text-indent: calc(5px * 5); }
 #qwivjjlbik .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qwivjjlbik .gt_row_group_first td { border-top-width: 2px; }
 #qwivjjlbik .gt_row_group_first th { border-top-width: 2px; }
 #qwivjjlbik .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qwivjjlbik .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qwivjjlbik .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qwivjjlbik .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #qwivjjlbik .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qwivjjlbik .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qwivjjlbik .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qwivjjlbik .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qwivjjlbik .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qwivjjlbik .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qwivjjlbik .gt_left { text-align: left; }
 #qwivjjlbik .gt_center { text-align: center; }
 #qwivjjlbik .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qwivjjlbik .gt_font_normal { font-weight: normal; }
 #qwivjjlbik .gt_font_bold { font-weight: bold; }
 #qwivjjlbik .gt_font_italic { font-style: italic; }
 #qwivjjlbik .gt_super { font-size: 65%; }
 #qwivjjlbik .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qwivjjlbik .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #qwivjjlbik .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qwivjjlbik .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qwivjjlbik .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qwivjjlbik .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
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
#ieusxhdrpy table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ieusxhdrpy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ieusxhdrpy p { margin: 0; padding: 0; }
 #ieusxhdrpy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ieusxhdrpy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ieusxhdrpy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ieusxhdrpy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ieusxhdrpy .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ieusxhdrpy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ieusxhdrpy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ieusxhdrpy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ieusxhdrpy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ieusxhdrpy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ieusxhdrpy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ieusxhdrpy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ieusxhdrpy .gt_spanner_row { border-bottom-style: hidden; }
 #ieusxhdrpy .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ieusxhdrpy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ieusxhdrpy .gt_from_md> :first-child { margin-top: 0; }
 #ieusxhdrpy .gt_from_md> :last-child { margin-bottom: 0; }
 #ieusxhdrpy .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ieusxhdrpy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 80%; font-weight: bolder; text-transform: uppercase; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ieusxhdrpy .gt_indent_1 { text-indent: 5px; }
 #ieusxhdrpy .gt_indent_2 { text-indent: calc(5px * 2); }
 #ieusxhdrpy .gt_indent_3 { text-indent: calc(5px * 3); }
 #ieusxhdrpy .gt_indent_4 { text-indent: calc(5px * 4); }
 #ieusxhdrpy .gt_indent_5 { text-indent: calc(5px * 5); }
 #ieusxhdrpy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ieusxhdrpy .gt_row_group_first td { border-top-width: 2px; }
 #ieusxhdrpy .gt_row_group_first th { border-top-width: 2px; }
 #ieusxhdrpy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ieusxhdrpy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ieusxhdrpy .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ieusxhdrpy .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #ieusxhdrpy .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ieusxhdrpy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ieusxhdrpy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ieusxhdrpy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ieusxhdrpy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ieusxhdrpy .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ieusxhdrpy .gt_left { text-align: left; }
 #ieusxhdrpy .gt_center { text-align: center; }
 #ieusxhdrpy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ieusxhdrpy .gt_font_normal { font-weight: normal; }
 #ieusxhdrpy .gt_font_bold { font-weight: bold; }
 #ieusxhdrpy .gt_font_italic { font-style: italic; }
 #ieusxhdrpy .gt_super { font-size: 65%; }
 #ieusxhdrpy .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ieusxhdrpy .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #ieusxhdrpy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ieusxhdrpy .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ieusxhdrpy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ieusxhdrpy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
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
#bfewpxrrmi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#bfewpxrrmi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#bfewpxrrmi p { margin: 0; padding: 0; }
 #bfewpxrrmi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #bfewpxrrmi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #bfewpxrrmi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #bfewpxrrmi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: -0.4px; padding-bottom: 1.6px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #bfewpxrrmi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bfewpxrrmi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bfewpxrrmi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #bfewpxrrmi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 0.75px; padding-bottom: 1.6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #bfewpxrrmi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #bfewpxrrmi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #bfewpxrrmi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #bfewpxrrmi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 0.75px; padding-bottom: 0.75px; overflow-x: hidden; display: inline-block; width: 100%; }
 #bfewpxrrmi .gt_spanner_row { border-bottom-style: hidden; }
 #bfewpxrrmi .gt_group_heading { padding-top: 1.2px; padding-bottom: 1.2px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #bfewpxrrmi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #bfewpxrrmi .gt_from_md> :first-child { margin-top: 0; }
 #bfewpxrrmi .gt_from_md> :last-child { margin-bottom: 0; }
 #bfewpxrrmi .gt_row { padding-top: 1.2px; padding-bottom: 1.2px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #bfewpxrrmi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #bfewpxrrmi .gt_indent_1 { text-indent: 5px; }
 #bfewpxrrmi .gt_indent_2 { text-indent: calc(5px * 2); }
 #bfewpxrrmi .gt_indent_3 { text-indent: calc(5px * 3); }
 #bfewpxrrmi .gt_indent_4 { text-indent: calc(5px * 4); }
 #bfewpxrrmi .gt_indent_5 { text-indent: calc(5px * 5); }
 #bfewpxrrmi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #bfewpxrrmi .gt_row_group_first td { border-top-width: 2px; }
 #bfewpxrrmi .gt_row_group_first th { border-top-width: 2px; }
 #bfewpxrrmi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #bfewpxrrmi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bfewpxrrmi .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bfewpxrrmi .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #bfewpxrrmi .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #bfewpxrrmi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #bfewpxrrmi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #bfewpxrrmi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #bfewpxrrmi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bfewpxrrmi .gt_sourcenote { font-size: 90%; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bfewpxrrmi .gt_left { text-align: left; }
 #bfewpxrrmi .gt_center { text-align: center; }
 #bfewpxrrmi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #bfewpxrrmi .gt_font_normal { font-weight: normal; }
 #bfewpxrrmi .gt_font_bold { font-weight: bold; }
 #bfewpxrrmi .gt_font_italic { font-style: italic; }
 #bfewpxrrmi .gt_super { font-size: 65%; }
 #bfewpxrrmi .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bfewpxrrmi .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #bfewpxrrmi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #bfewpxrrmi .gt_sourcenote { font-size: 90%; padding-top: 0.6px; padding-bottom: 0.6px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #bfewpxrrmi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #bfewpxrrmi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
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
#xyrfescebn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xyrfescebn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xyrfescebn p { margin: 0; padding: 0; }
 #xyrfescebn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xyrfescebn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xyrfescebn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xyrfescebn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 15px; padding-right: 15px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xyrfescebn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xyrfescebn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xyrfescebn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xyrfescebn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 15px; padding-right: 15px; overflow-x: hidden; }
 #xyrfescebn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xyrfescebn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xyrfescebn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xyrfescebn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xyrfescebn .gt_spanner_row { border-bottom-style: hidden; }
 #xyrfescebn .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xyrfescebn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xyrfescebn .gt_from_md> :first-child { margin-top: 0; }
 #xyrfescebn .gt_from_md> :last-child { margin-bottom: 0; }
 #xyrfescebn .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xyrfescebn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 15px; padding-right: 15px; }
 #xyrfescebn .gt_indent_1 { text-indent: 5px; }
 #xyrfescebn .gt_indent_2 { text-indent: calc(5px * 2); }
 #xyrfescebn .gt_indent_3 { text-indent: calc(5px * 3); }
 #xyrfescebn .gt_indent_4 { text-indent: calc(5px * 4); }
 #xyrfescebn .gt_indent_5 { text-indent: calc(5px * 5); }
 #xyrfescebn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 15px; padding-right: 15px; vertical-align: top; }
 #xyrfescebn .gt_row_group_first td { border-top-width: 2px; }
 #xyrfescebn .gt_row_group_first th { border-top-width: 2px; }
 #xyrfescebn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xyrfescebn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xyrfescebn .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xyrfescebn .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #xyrfescebn .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xyrfescebn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xyrfescebn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xyrfescebn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xyrfescebn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xyrfescebn .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #xyrfescebn .gt_left { text-align: left; }
 #xyrfescebn .gt_center { text-align: center; }
 #xyrfescebn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xyrfescebn .gt_font_normal { font-weight: normal; }
 #xyrfescebn .gt_font_bold { font-weight: bold; }
 #xyrfescebn .gt_font_italic { font-style: italic; }
 #xyrfescebn .gt_super { font-size: 65%; }
 #xyrfescebn .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xyrfescebn .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #xyrfescebn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xyrfescebn .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #xyrfescebn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xyrfescebn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
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
#nhkegjojvc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nhkegjojvc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nhkegjojvc p { margin: 0; padding: 0; }
 #nhkegjojvc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 3px; border-top-color: #D3D3D3; border-right-style: solid; border-right-width: 3px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 3px; border-bottom-color: #D3D3D3; border-left-style: solid; border-left-width: 3px; border-left-color: #D3D3D3; }
 #nhkegjojvc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nhkegjojvc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nhkegjojvc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nhkegjojvc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nhkegjojvc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nhkegjojvc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nhkegjojvc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #nhkegjojvc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nhkegjojvc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nhkegjojvc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nhkegjojvc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2.5px; padding-bottom: 2.5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nhkegjojvc .gt_spanner_row { border-bottom-style: hidden; }
 #nhkegjojvc .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nhkegjojvc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nhkegjojvc .gt_from_md> :first-child { margin-top: 0; }
 #nhkegjojvc .gt_from_md> :last-child { margin-bottom: 0; }
 #nhkegjojvc .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nhkegjojvc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #nhkegjojvc .gt_indent_1 { text-indent: 5px; }
 #nhkegjojvc .gt_indent_2 { text-indent: calc(5px * 2); }
 #nhkegjojvc .gt_indent_3 { text-indent: calc(5px * 3); }
 #nhkegjojvc .gt_indent_4 { text-indent: calc(5px * 4); }
 #nhkegjojvc .gt_indent_5 { text-indent: calc(5px * 5); }
 #nhkegjojvc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #nhkegjojvc .gt_row_group_first td { border-top-width: 2px; }
 #nhkegjojvc .gt_row_group_first th { border-top-width: 2px; }
 #nhkegjojvc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nhkegjojvc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nhkegjojvc .gt_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nhkegjojvc .gt_first_summary_row { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; }
 #nhkegjojvc .gt_last_summary_row_top { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nhkegjojvc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nhkegjojvc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nhkegjojvc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nhkegjojvc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nhkegjojvc .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nhkegjojvc .gt_left { text-align: left; }
 #nhkegjojvc .gt_center { text-align: center; }
 #nhkegjojvc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nhkegjojvc .gt_font_normal { font-weight: normal; }
 #nhkegjojvc .gt_font_bold { font-weight: bold; }
 #nhkegjojvc .gt_font_italic { font-style: italic; }
 #nhkegjojvc .gt_super { font-size: 65%; }
 #nhkegjojvc .gt_footnotes { color: font-color(#FFFFFF); background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nhkegjojvc .gt_footnote { margin: 0px; font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; }
 #nhkegjojvc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nhkegjojvc .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #nhkegjojvc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nhkegjojvc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<th colspan="3" class="gt_group_heading" scope="colgroup">grp_a</th>
</tr>

<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_1</td>
<td class="gt_row gt_right">0.11</td>
<td class="gt_row gt_left">apricot</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_2</td>
<td class="gt_row gt_right">2.22</td>
<td class="gt_row gt_left">banana</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_left">coconut</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_4</td>
<td class="gt_row gt_right">444.40</td>
<td class="gt_row gt_left">durian</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="3" class="gt_group_heading" scope="colgroup">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" scope="row">row_5</td>
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
